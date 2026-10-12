"""Interpolazione fluida tra pose dello stesso personaggio (flusso ottico DIS + dissolvenza).
Le pose sono allineate su una tela comune: ancora = centro del busto in x, piedi in y.
    aligned(chi, pose)         -> RGBA numpy (CH x CW x 4) uint8   ("<pose>_m" = specchiata)
    transition(chi, A, B, k)   -> frame k di K (0..K-1) dal caso A al caso B, in cache su disco
"""
import os, hashlib
import numpy as np, cv2
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
CW, CH = 920, 1180
AX, AY = 460, 1120
K = 8
TARGET_H = {"mouse": 640, "chip": 600, "spike": 560, "ele": 660}   # altezza (px) del personaggio in posa 'tiene' alla scala 1
CACHE = "/tmp/claude-0/morph_cache8s"
os.makedirs(CACHE, exist_ok=True)
_al = {}

# pose non ancora generate -> pose simili già disponibili (finché non c'è credito Pollinations)
SUBST = {"salto": "ride", "balla": "ride", "guarda_su": "sorpreso", "afferra": "corre", "indica": "saluta", "mangia": "tiene"}

def _src(chi, pose):
    d = os.path.join(HERE, "assets", "pose"); n = 'topo' if chi == 'mouse' else chi
    f = os.path.join(d, f"{n}_{pose}.png")
    if not os.path.exists(f) and pose in SUBST: f = os.path.join(d, f"{n}_{SUBST[pose]}.png")
    return f

_sc = {}
def _scale(chi):
    """scala che porta la posa 'tiene' all'altezza TARGET_H"""
    if chi not in _sc:
        im = Image.open(_src(chi, "tiene")).convert("RGBA")
        a = np.asarray(im.getchannel("A")) > 150; ys = np.nonzero(a.any(axis=1))[0]
        _sc[chi] = TARGET_H[chi] / float(ys.max() - ys.min())
    return _sc[chi]

def aligned(chi, pose):
    key = (chi, pose)
    if key in _al: return _al[key]
    mirror = pose.endswith("_m"); base = pose[:-2] if mirror else pose
    im = Image.open(_src(chi, base)).convert("RGBA")
    a = im.getchannel("A").point(lambda v: 255 if v > 150 else 0).filter(ImageFilter.MinFilter(5))
    im.putalpha(a.filter(ImageFilter.GaussianBlur(0.8)))
    al = np.asarray(a) > 0; ys, xs = np.nonzero(al)
    top, bot = ys.min(), ys.max(); h = bot - top
    tor = al[int(top + h * 0.35):int(top + h * 0.7)]; cx = np.nonzero(tor)[1].mean() if tor.any() else xs.mean()
    sc = _scale(chi)
    im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.LANCZOS)
    cx, bot = cx * sc, bot * sc
    canvas = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    canvas.paste(im, (int(round(AX - cx)), int(round(AY - bot))), im)
    arr = np.asarray(canvas)
    if mirror: arr = arr[:, ::-1].copy()
    _al[key] = arr
    return arr

def _prem(arr):
    f = arr.astype(np.float32); a = f[..., 3:4] / 255.0
    return np.concatenate([f[..., :3] * a, f[..., 3:4]], axis=2)

def _flow(src, dst):
    """Farneback multi-scala su luminanza+silhouette (regge spostamenti grandi anche sul pelo liscio)."""
    def g(x):
        a = x[..., 3].astype(np.float32) / 255.0
        lum = cv2.cvtColor(x[..., :3], cv2.COLOR_RGB2GRAY).astype(np.float32) * a
        gg = 0.45 * lum + 0.55 * a * 255.0
        gg = cv2.GaussianBlur(gg, (0, 0), 3)
        return np.clip(cv2.resize(gg, (CW // 3, CH // 3)), 0, 255).astype(np.uint8)
    f = cv2.calcOpticalFlowFarneback(g(src), g(dst), None, 0.5, 6, 31, 6, 7, 1.6, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
    return cv2.resize(f, (CW, CH)) * 3.0

def _over_gray(arr):
    a = arr[..., 3:4].astype(np.float32) / 255.0
    return arr[..., :3].astype(np.float32) * a + 128.0 * (1 - a)

def _remap(img, flow, k):
    yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
    return cv2.remap(img, xx - k * flow[..., 0], yy - k * flow[..., 1], cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

def SHARP(t):
    u = min(1.0, max(0.0, (t - 0.44) / 0.12)); return u * u * (3 - 2 * u)

def _build(chi, A, B):
    a, b = aligned(chi, A), aligned(chi, B)
    fab, fba = _flow(a, b), _flow(b, a)
    pa, pb = _prem(a), _prem(b); out = []
    for i in range(K):
        t = (i + 1) / (K + 1)                       # istanti interni (A e B esclusi)
        wa = _remap(pa, fab, t); wb = _remap(pb, fba, 1 - t)
        w = SHARP(t)                                  # niente doppia esposizione: A fino a metà, B dopo, sfumatura stretta al centro
        m = wa * (1 - w) + wb * w
        al = np.clip(m[..., 3:4], 1, 255)
        rgb = np.clip(m[..., :3] / al * 255.0, 0, 255)
        a2 = np.clip((m[..., 3:4] / 255.0) * 1.9, 0, 1) ** 0.8 * 255.0     # riempie le zone 'fantasma' (alpha parziale)
        out.append(np.concatenate([rgb, a2], axis=2).astype(np.uint8))
    return out

_tr = {}
def transition(chi, A, B):
    """lista di K frame intermedi A->B (cache su disco + ultime 8 in memoria)"""
    key = (chi, A, B)
    if key in _tr:
        v = _tr.pop(key); _tr[key] = v; return v
    f = os.path.join(CACHE, f"{chi}_{A}__{B}.npy")
    if os.path.exists(f):
        fr = np.load(f, mmap_mode='r')
    else:
        fr = np.stack(_build(chi, A, B)); np.save(f + ".tmp.npy", fr); os.replace(f + ".tmp.npy", f)
    _tr[key] = fr
    while len(_tr) > 24: _tr.pop(next(iter(_tr)))
    return fr
