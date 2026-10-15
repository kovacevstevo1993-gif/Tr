#!/usr/bin/env python3
"""Short 'Il razzo per la luna' (9:16, 1080x1920, 30 fps): topolino e Chip.
Giardino di notte (costruiscono il razzo, conto alla rovescia INTERATTIVO 3-2-1) -> spazio (stelle, Saturno) -> luna (salti al rallentatore,
'la luna è di formaggio?', bandiera, ciao Terra).
Regole del 15/10/2026: NIENTE sottotitoli, personaggi GRANDI e al CENTRO, movimenti più naturali:
  - 'corpo vivo': deformazione continua delle pose (testa che si inclina e annuisce quando parla, respiro, peso che si sposta,
    il busto che segue i salti con ritardo), anticipo e assestamento su ogni salto
  - facce dei personaggi nell'oblò del razzo (con bocca che parla)
  - salti a bassa gravità con polvere lunare, fiamma e fumo del razzo, stelle a 3 livelli, numeri del conto alla rovescia
    python3 short_razzo.py info | prep | test 1.0 5.5 | renderpart a b out.mp4 | render muto.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import morph as MO

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
AUD = "audioJ"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))
WD = json.load(open(os.path.join(HERE, AUD, "parole.json")))


def lerp(a, b, u): return a + (b - a) * u
def clamp(u, a=0.0, b=1.0): return max(a, min(b, u))
def ease(u): u = clamp(u); return u * u * (3 - 2 * u)
def back(u, k=1.7): u = clamp(u); return 1 + (k + 1) * (u - 1) ** 3 + k * (u - 1) ** 2
def osc(t, t0, amp=1.0, decay=7.0, freq=26.0):
    return amp * math.exp(-decay * (t - t0)) * math.sin(freq * (t - t0)) if t >= t0 else 0.0


# ------------------------------------------------------------------ copione
V = {}
def _seq():
    t = 0.0
    def at(k, gap):
        nonlocal t
        V[k] = t + gap; t = V[k] + D[k]
    at("n1", 0.6); at("c1", 0.2); at("n2", 0.3); at("t1", 0.25); at("n3", 1.5); at("c2", 0.2); at("n4", 2.2); at("t2", 0.3)
    at("n5", 0.6); at("t3", 0.5); at("c3", 0.1); at("n6", 0.4); at("t4", 0.4); at("end", 0.4)
    return t + 2.7
DUR = _seq()
SAY = {"n1": "narr", "c1": "chip", "n2": "narr", "t1": "mouse", "n3": "narr", "c2": "chip", "n4": "narr", "t2": "mouse",
       "n5": "narr", "t3": "mouse", "c3": "chip", "n6": "narr", "t4": "mouse", "end": "mouse"}
VOICES = [(k, V[k], SAY[k], D[k]) for k in V]
E = lambda k: V[k] + D[k]


def word(k, w, frac=0.5):
    for (ww, a, b) in WD.get(k, []):
        if w.lower() in ww.lower(): return V[k] + a
    return V[k] + D[k] * frac


# ------------------------------------------------------------------ eventi
T_B1 = word("n1", "costruiscono") - 0.1          # corpo del razzo
T_B2 = word("n1", "razzo") + 0.1                 # Chip lancia la punta
T_B2L = T_B2 + 0.55                              # la punta si incastra
T_B3 = word("n1", "scatola") + 0.25              # ultimi colpi + scintille
T_IN = {"mouse": word("n2", "salgono") + 0.05, "chip": word("n2", "salgono") + 0.35}   # saltano dentro
T_CNT = [word("n2", "tre"), word("n2", "due"), word("n2", "uno")]
T_LAUNCH = V["t1"] + 0.12
T_W1 = T_LAUNCH + 2.1
T_SAT = V["c2"] - 0.6
T_W2 = E("c2") + 0.9
T_LAND = T_W2 + 1.25
T_OUT = {"mouse": T_LAND + 0.45, "chip": T_LAND + 0.75}
T_J1 = word("n4", "salta") - 0.25                # salti lunari
T_PICK = word("n5", "pensa") - 0.1               # si china e raccoglie il sasso
T_THINK = word("n5", "formaggio") - 0.15         # nuvoletta col formaggio
T_BITE = V["t3"] - 0.15
T_SPIT = V["t3"] + 0.25
T_FLAG0 = word("n6", "piantano") - 0.25; T_FLAG1 = T_FLAG0 + 0.7
T_WAVE = word("n6", "salutano") - 0.1
SCENES = [("notte_giardino", 0.0), ("spazio", T_W1), ("luna", T_W2)]
WIPES = [T_W1, T_W2]


# ------------------------------------------------------------------ utilità grafiche
_obj = {}
def load(name):
    if name not in _obj: _obj[name] = Image.open(os.path.join(HERE, "assets", "obj", name + ".png")).convert("RGBA")
    return _obj[name]


_sz = {}
def sized(name, w=None, h=None):
    im = load(name)
    if w is None: w = im.width * h / im.height
    if h is None: h = im.height * w / im.width
    key = (name, int(w), int(h))
    if key not in _sz:
        _sz[key] = im.resize((max(2, int(w)), max(2, int(h))), Image.LANCZOS)
        if len(_sz) > 200: _sz.pop(next(iter(_sz)))
    return _sz[key]


class Ctx: pass


def star4(d, x, y, r, col):
    k = 0.2; d.polygon([(x, y - r), (x + r * k, y - r * k), (x + r, y), (x + r * k, y + r * k), (x, y + r), (x - r * k, y + r * k), (x - r, y), (x - r * k, y - r * k)], fill=col)


def text(d, s, x, y, size, fill, out, ow):
    d.text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)


def sparkles(c, x, y, t0, dur, n=14, spread=120, rise=60, size=16, seed=1):
    t = c.t
    if not (t0 <= t < t0 + dur): return
    cols = ((255, 245, 170), (255, 255, 255), (190, 225, 255))
    for k in range(n):
        ph = (k * 0.618 + seed * 0.37) % 1.0; life = 0.5 + 0.5 * ((k * 0.41 + seed) % 1.0); u = ((t - t0) / dur * 1.4 + ph) % 1.0
        if u > life: continue
        a = k * 2.399 + seed; r = spread * (0.25 + 0.75 * ((k * 0.37 + seed * 0.11) % 1.0)) * (0.4 + u)
        px, py = c.X(x + math.cos(a) * r), c.Y(y + math.sin(a) * r * 0.8 - rise * u)
        fade = math.sin(math.pi * u / life); col = tuple(int(v * fade) for v in cols[k % 3]); rr = size * c.Z * (0.5 + fade * 0.7)
        star4(c.gd, px, py, rr, col); c.glow_used = True


def glow_blob(c, x, y, r, col, a=1.0, n=9):
    for k in range(n):
        f = (k + 1) / n; rr = r * (1 - k / n); lv = a * f ** 2.2
        c.gd.ellipse([c.X(x) - rr * c.Z, c.Y(y) - rr * c.Z, c.X(x) + rr * c.Z, c.Y(y) + rr * c.Z], fill=tuple(int(v * lv) for v in col))
    c.glow_used = True


def tinted(im, tint):
    a = np.asarray(im).astype(np.float32); a[..., :3] = np.clip(a[..., :3] * np.array(tint, dtype=np.float32), 0, 255)
    return Image.fromarray(a.astype(np.uint8), "RGBA")


def paste_c(c, im, x, y, ang=0.0):
    if ang: im = im.rotate(ang, resample=Image.BICUBIC, expand=True)
    c.img.paste(im, (int(c.X(x) - im.width / 2), int(c.Y(y) - im.height / 2)), im)


def puff(c, x, y, t0, dur=0.9, n=18, spread=150, size=26, seed=1, col=(235, 235, 240), grav=120):
    t = c.t
    if not (t0 <= t < t0 + dur): return
    u = (t - t0) / dur
    for k in range(n):
        a = (k * 2.399 + seed) % 6.283; sp = spread * (0.5 + 0.5 * ((k * 0.37 + seed * 0.1) % 1.0))
        px = x + math.cos(a) * sp * (1 - (1 - u) ** 2) * 1.2; py = y - abs(math.sin(a)) * sp * 0.6 * (1 - (1 - u) ** 2) + grav * u * u
        rr = size * (0.6 + 0.6 * ((k * 0.61) % 1.0)) * (1 + u) * c.Z
        c.d.ellipse([c.X(px) - rr, c.Y(py) - rr, c.X(px) + rr, c.Y(py) + rr], fill=col + (int(200 * (1 - u) ** 1.2),))


def subscribe_button(img, t, t0, cy=1760):
    if t < t0: return
    u = back((t - t0) / 0.45); s = max(0.05, u) * (1 + 0.03 * math.sin((t - t0) * 6))
    w, h = 560, 140; Sx = 2; cv = Image.new("RGBA", (w * Sx, h * Sx + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
    d.rounded_rectangle([6 * Sx, 10 * Sx, (w - 6) * Sx, (h - 6) * Sx], radius=34 * Sx, fill=(0, 0, 0, 70))
    d.rounded_rectangle([0, 0, (w - 12) * Sx, (h - 16) * Sx], radius=34 * Sx, fill=(232, 36, 36, 255), outline=(255, 255, 255, 255), width=4 * Sx)
    d.text((((w - 12) / 2 + 34) * Sx, (h - 16) / 2 * Sx), "ISCRIVITI", font=ImageFont.truetype(FONT, 58 * Sx), fill=(255, 255, 255, 255), anchor="mm")
    bell = Image.new("RGBA", (90 * Sx, 90 * Sx), (0, 0, 0, 0)); bd = ImageDraw.Draw(bell)
    bd.pieslice([20 * Sx, 12 * Sx, 70 * Sx, 62 * Sx], 180, 360, fill=(255, 255, 255, 255)); bd.polygon([(20 * Sx, 38 * Sx), (70 * Sx, 38 * Sx), (78 * Sx, 62 * Sx), (12 * Sx, 62 * Sx)], fill=(255, 255, 255, 255))
    bd.ellipse([36 * Sx, 62 * Sx, 54 * Sx, 78 * Sx], fill=(255, 255, 255, 255)); bd.ellipse([40 * Sx, 4 * Sx, 50 * Sx, 14 * Sx], fill=(255, 255, 255, 255))
    bell = bell.rotate(math.sin((t - t0) * 14) * 16 * max(0, 1 - (t - t0) / 1.8), resample=Image.BICUBIC, center=(45 * Sx, 14 * Sx))
    cv.paste(bell, (24 * Sx, int(((h - 16) / 2 - 45) * Sx)), bell)
    cv = cv.resize((int(w * s), int((h + 10) * s)), Image.LANCZOS); img.paste(cv, (int(W / 2 - cv.width / 2), int(cy - cv.height / 2)), cv)


# ------------------------------------------------------------------ pose
def loop(t0, t1, seq, beat=0.5):
    ev = []; i = 0
    while t0 + i * beat < t1:
        ev.append((t0 + i * beat, seq[i % len(seq)], beat * 0.85)); i += 1
    return ev


def hammer(t0, t1, beat=0.36):
    return [(t0 + i * beat, "batte_sabbia" if i % 2 == 0 else "china", 0.12) for i in range(int((t1 - t0) / beat))]


JUMPS = {   # salti lunari: (inizio, durata, altezza)
    "mouse": [(T_J1, 1.55, 430), (T_J1 + 1.75, 1.45, 380), (V["t2"] + 0.05, 1.6, 470)],
    "chip": [(T_J1 + 0.35, 1.5, 400), (T_J1 + 2.0, 1.5, 420)],
}

EV = {
    "mouse": [(0.0, "guarda_su", 0.01), (1.3, "indica", 0.2), (V["n1"] + 0.8, "ride", 0.2)] + hammer(T_B1 - 0.2, T_B2 - 0.3)
             + [(T_B2 - 0.3, "guarda_su", 0.2), (T_B2L + 0.05, "salto", 0.12), (T_B2L + 0.6, "ride", 0.2), (V["c1"] + 0.3, "indica", 0.2),
                (T_IN["mouse"] - 0.25, "china", 0.12), (T_IN["mouse"], "salto", 0.12),
                (T_OUT["mouse"] - 0.05, "salto", 0.01), (T_OUT["mouse"] + 0.75, "sorpreso", 0.15), (V["n4"] + 0.4, "guarda_su", 0.2)]
             + [e for (j0, jd, _) in JUMPS["mouse"] for e in ((j0 - 0.18, "china", 0.12), (j0 + 0.02, "salto", 0.12), (j0 + jd - 0.05, "ride", 0.15))]
             + [(T_PICK, "china", 0.15), (T_PICK + 0.55, "tiene", 0.15), (T_THINK, "guarda_su", 0.2), (T_BITE - 0.25, "tiene", 0.15),
                (T_SPIT, "fuggi", 0.1), (T_SPIT + 0.6, "sorpreso", 0.15), (E("c3") + 0.1, "ride", 0.2),
                (T_WAVE, "saluta2", 0.2), (V["t4"] + 0.3, "saluta2_m", 0.2)]
             + loop(E("t4") + 0.2, DUR + 1, ["salto", "balla", "saluta2", "ride", "saluta2_m", "balla_m"], 0.55),
    "chip": [(0.0, "saluta2", 0.01), (1.4, "ride", 0.2)] + hammer(T_B1, T_B2 - 0.7)
            + [(T_B2 - 0.55, "tiene", 0.15), (T_B2 - 0.2, "lancia", 0.12), (T_B2L + 0.1, "guarda_su", 0.2), (V["c1"] - 0.15, "salto", 0.12),
               (E("c1") + 0.4, "ride", 0.2), (T_IN["chip"] - 0.25, "china", 0.12), (T_IN["chip"], "salto", 0.12),
               (T_OUT["chip"] - 0.05, "salto", 0.01), (T_OUT["chip"] + 0.75, "ride", 0.15), (V["n4"] + 0.5, "indica", 0.2)]
            + [e for (j0, jd, _) in JUMPS["chip"] for e in ((j0 - 0.18, "ride", 0.12), (j0 + 0.02, "salto", 0.12), (j0 + jd - 0.05, "ride", 0.15))]
            + [(T_PICK + 0.2, "guarda_su", 0.2), (T_THINK + 0.3, "sorpreso", 0.15), (V["t3"] + 0.6, "ride", 0.2), (V["c3"] - 0.1, "ride", 0.2),
               (T_FLAG0 - 0.45, "tiene", 0.15), (T_FLAG0, "lancia", 0.12), (T_FLAG1 + 0.1, "ride", 0.2), (T_WAVE + 0.1, "saluta2", 0.2),
               (V["t4"] + 0.4, "saluta2_m", 0.2)]
            + loop(E("t4") + 0.3, DUR + 1, ["balla", "salto", "saluta2_m", "ride", "saluta2", "balla_m"], 0.55),
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
HAS_MOUTH = {"mouse": ("parla_a", "parla_o"), "chip": ("parla_a", "parla_o")}
CHS = 1.0
H_CH = {"mouse": 640 * CHS, "chip": 600 * CHS}
CHARS = ["mouse", "chip"]


def rp(name, pose): return pose


_iou = {}
def pair_dur(name, A, B, dur):
    key = (name, A, B)
    if key not in _iou:
        a = MO.aligned(name, A)[..., 3] > 128; b = MO.aligned(name, B)[..., 3] > 128
        _iou[key] = float((a & b).sum() / max(1, (a | b).sum()))
    q = _iou[key]
    return min(dur, 0.24 if q > 0.85 else (0.16 if q > 0.70 else 0.10))


def pose_state(name, t):
    ev = EV[name]; idx = 0
    for i, e in enumerate(ev):
        if e[0] <= t: idx = i
    t0, pose, dur = ev[idx]
    prev = ev[idx - 1][1] if idx > 0 else pose
    if prev != pose:
        dur = pair_dur(name, prev, pose, dur)
        if t < t0 + dur: return prev, pose, (t - t0) / dur
    return pose, pose, 1.0


def precompute():
    pairs = set()
    for name, ev in EV.items():
        for a, b in zip(ev, ev[1:]):
            if a[1] != b[1]: pairs.add((name, a[1], b[1]))
        for p in ("parla_a", "parla_o"):
            pairs.add((name, "neutro", p)); pairs.add((name, p, "neutro"))
    return sorted(pairs)


_env = {}
def talk(who, t):
    for k, t0, w, d in VOICES:
        if w == who and t0 <= t <= t0 + d:
            if k not in _env:
                with wave.open(os.path.join(HERE, AUD, f"{k}.wav")) as wf:
                    a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
                win = 44100 // (FPS * 2); n = len(a) // win + 1
                e = np.array([np.sqrt(np.mean(a[i * win:(i + 1) * win] ** 2) + 1e-12) for i in range(n)]); _env[k] = e / (np.percentile(e, 95) + 1e-9)
            e = _env[k]; return min(1.0, e[min(len(e) - 1, int((t - t0) * FPS * 2))])
    return 0.0


def mouth_pose(name, t):
    def m(e): return "parla_a" if e > 0.52 else ("parla_o" if e > 0.17 else "neutro")
    cur = m(talk(name, t)); prev = m(talk(name, t - 1.0 / FPS))
    return prev if (prev == "parla_a" and cur == "parla_o") else cur


def char_canvas(name, t):
    A, B, u = pose_state(name, t)
    if A == B == "neutro": A = B = mouth_pose(name, t)
    if A == B: return MO.aligned(name, A)
    fr = MO.transition(name, A, B); idx = int(ease(u) * (MO.K + 1))
    if idx <= 0: return MO.aligned(name, A)
    if idx >= MO.K + 1: return MO.aligned(name, B)
    return fr[idx - 1]


# ------------------------------------------------------------------ corpo vivo (deformazione naturale delle pose)
_grids = {}
def alive_warp(arr, t, name, head_ang, sway, breath, lean):
    """testa che ruota attorno al collo (peso graduale), busto che oscilla (piedi fermi), respiro, inclinazione in avanti"""
    h, w = arr.shape[:2]
    key = (w, h)
    if key not in _grids:
        _grids[key] = np.meshgrid(np.arange(w, dtype=np.float32), np.arange(h, dtype=np.float32))
        if len(_grids) > 30: _grids.pop(next(iter(_grids)))
    xs, ys = _grids[key]
    al = arr[..., 3] > 40; rows = np.nonzero(al.any(axis=1))[0]
    if len(rows) < 4: return arr
    top, bot = float(rows[0]), float(rows[-1]); hh = bot - top
    yn = (ys - top) / max(1.0, hh)                                    # 0 = cima della testa, 1 = piedi
    cx = w / 2.0
    neck_y = top + 0.50 * hh
    wh = np.clip((0.60 - yn) / 0.22, 0, 1); wh = wh * wh * (3 - 2 * wh)       # peso della testa
    a = -math.radians(head_ang) * wh
    dxh = (xs - cx); dyh = (ys - neck_y)
    sx = cx + dxh * np.cos(a) - dyh * np.sin(a)
    sy = neck_y + dxh * np.sin(a) + dyh * np.cos(a)
    body = np.clip(1 - yn, 0, 1) ** 1.4                                # piedi fermi, la cima si muove di più
    sx = sx - sway * body - lean * body * 0.6
    sy = sy + breath * hh * (yn - 1) * 0.6 * np.clip(1 - yn, 0, 1)    # respiro: busto e testa salgono un poco
    return cv2.remap(arr, sx.astype(np.float32), sy.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))


def jump_state(name, t):
    """(altezza, fase 0..1 o None) dei salti lunari e dei salti dentro/fuori dal razzo"""
    for (j0, jd, hgt) in JUMPS.get(name, []):
        if j0 <= t < j0 + jd:
            p = (t - j0) / jd; return 4 * p * (1 - p) * hgt, p
    return 0.0, None


# ------------------------------------------------------------------ luce
SUN = {"notte_giardino": (-0.6, 0.28), "spazio": (0.5, 0.3), "luna": (0.8, 0.32)}
TINT = {"notte_giardino": (0.80, 0.86, 1.05), "spazio": (0.95, 0.92, 1.05), "luna": (0.98, 0.98, 1.02)}
RIM = {"notte_giardino": ((255, 200, 120), 0.50), "spazio": ((200, 160, 255), 0.45), "luna": ((150, 200, 255), 0.55)}
RIMDIR = {"notte_giardino": (-1, -1), "spazio": (1, -1), "luna": (-1, -1)}
SHCOL = {"notte_giardino": (10, 15, 40), "spazio": (10, 10, 30), "luna": (20, 20, 35)}


def contact(c, x, y, wsh, a=110):
    wsh *= c.Z
    ell = Image.new("RGBA", (int(wsh * 2.4) + 2, int(wsh * 0.7) + 2), (0, 0, 0, 0))
    ImageDraw.Draw(ell).ellipse([wsh * 0.2, wsh * 0.12, wsh * 2.2, wsh * 0.58], fill=SHCOL[c.sid] + (a,))
    ell = ell.filter(ImageFilter.GaussianBlur(max(3, 6 * c.Z))); c.img.paste(ell, (int(c.X(x) - ell.width / 2), int(c.Y(y) - ell.height * 0.5)), ell)


def draw_char(c, name, t, x, y, scale=1.0, hop=0.0, rot=0.0, alpha=1.0):
    cv = char_canvas(name, t)
    A, B, u = pose_state(name, t)
    sq = 1.0
    tk = talk(name, t)
    # anticipo/atterraggio sui salti (squash), respiro e dondolio sempre presenti
    for pose_, t0 in ((e[1], e[0]) for e in EV[name]):
        if pose_ == "china" and t0 <= t < t0 + 0.2: sq *= 1 - 0.06 * math.sin(math.pi * (t - t0) / 0.2)
        if pose_ in ("ride", "neutro") and t0 > 1.0: sq *= 1 + osc(t, t0 + 0.03, 0.05, 8, 22)
    jh, jp = jump_state(name, t); hop += jh
    if jp is not None and jp > 0.88: sq *= 1 - 0.08 * math.sin(math.pi * (jp - 0.88) / 0.12)
    ph = len(name) * 1.7
    head = 4.0 * math.sin(t * 1.3 + ph) + 2.0 * math.sin(t * 2.9 + ph) + 5.5 * tk * math.sin(t * 9 + ph)
    if A == B and A in ("ride", "balla", "balla_m", "salto"): head += 5 * math.sin(t * 8 + ph)
    sway = 7 * math.sin(t * 1.1 + ph) + (10 * math.sin(t * 7 + ph) if A == B and A.startswith("balla") else 0)
    breath = 0.012 * math.sin(t * 2.4 + ph)
    lean = 0.0
    if jp is not None: lean = -18 * math.sin(math.pi * jp)                   # il busto resta indietro mentre sale
    f = c.Z * CHS * scale
    nw, nh = max(2, int(MO.CW * f / math.sqrt(sq))), max(2, int(MO.CH * f * sq))
    small = cv2.resize(np.ascontiguousarray(cv), (nw, nh), interpolation=cv2.INTER_AREA if f < 1 else cv2.INTER_CUBIC)
    small = alive_warp(small, t, name, head, sway * f, breath, lean * f)
    im = Image.fromarray(small, "RGBA")
    if rot: im = im.rotate(rot, resample=Image.BILINEAR, center=(MO.AX * nw / MO.CW, MO.AY * nh / MO.CH))
    px, py = c.X(x) - MO.AX * nw / MO.CW, c.Y(y - hop) - MO.AY * nh / MO.CH
    contact(c, x, y, H_CH[name] * 0.42 * scale * clamp(1 - hop / 600, 0.35, 1), int(110 * clamp(1 - hop / 700, 0.3, 1)))
    arr = np.asarray(im).astype(np.float32); a = arr[..., 3] / 255.0
    rgb = arr[..., :3] * np.array(TINT[c.sid], dtype=np.float32)
    rimc, rimk = RIM[c.sid]; dx, dy = RIMDIR[c.sid]
    sg = max(3.0, 8 * f)
    Lb = cv2.GaussianBlur(a, (0, 0), sg)
    Ls = cv2.warpAffine(Lb, np.float32([[1, 0, -dx * sg * 1.1], [0, 1, -dy * sg * 1.1]]), (im.width, im.height))
    rim = np.clip(a * (1 - Ls * 1.25), 0, 1) ** 1.3
    rgb = rgb + rim[..., None] * np.array(rimc, dtype=np.float32) * rimk
    gy = np.linspace(0, 1, im.height, dtype=np.float32)[:, None, None]
    rgb = rgb * (1.03 - 0.12 * gy)
    al = arr[..., 3] * alpha
    out = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), al]).astype(np.uint8), "RGBA")
    c.img.paste(out, (int(px), int(py)), out)


def hand_pt(name, x, y, frac=0.40, dx=0.0, hop=0.0):
    return x + dx, y - hop - H_CH[name] * frac


# ------------------------------------------------------------------ razzo
RK_H = {"notte_giardino": 1000.0, "spazio": 1250.0, "luna": 900.0}
PORT = (0.50, 0.50, 0.155)                          # centro (frazioni) e raggio (frazione della larghezza) dell'oblò


def rocket_draw(c, x, ybase, hgt, t, ang=0.0, build=1.0, nose=1.0, faces=True):
    """razzo di cartone; build: comparsa del corpo, nose: 0..1 la punta (in volo da Chip) è al suo posto"""
    im = load("rocket"); rw = hgt * im.width / im.height
    if build <= 0: return
    full = sized("rocket", w=rw * c.Z, h=hgt * c.Z * clamp(build, 0.05, 1.2))
    cut = int(full.height * 0.30)
    body = full.crop((0, cut, full.width, full.height))
    cy_body = ybase - hgt * build * 0.35
    lay = Image.new("RGBA", (full.width + 40, full.height + 40), (0, 0, 0, 0))
    lay.paste(body, (20, 20 + cut), body)
    if nose >= 1:
        nz = full.crop((0, 0, full.width, cut + 4)); lay.paste(nz, (20, 20), nz)
    if faces and build >= 1: porthole_faces(c, lay, full, t)
    if ang: lay = lay.rotate(ang, resample=Image.BICUBIC, expand=False)
    c.img.paste(lay, (int(c.X(x) - lay.width / 2), int(c.Y(ybase) - (full.height + 20))), lay)
    return rw


_mask = {}
def porthole_faces(c, lay, full, t):
    """facce dei due amici nell'oblò (con la bocca che parla), poi vetro con riflesso"""
    if t < T_IN["mouse"] + 0.5 or (c.sid == "luna" and t > T_OUT["chip"] - 0.1): return
    W_, H_ = full.width, full.height
    R = int(PORT[2] * W_); cx, cy = int(PORT[0] * W_) + 20, int(PORT[1] * H_) + 20
    key = R
    if key not in _mask:
        m = Image.new("L", (2 * R, 2 * R), 0); ImageDraw.Draw(m).ellipse([0, 0, 2 * R - 1, 2 * R - 1], fill=255); _mask[key] = m
    win = Image.new("RGBA", (2 * R, 2 * R), (25, 30, 60, 255))
    who = [n for n in ("mouse", "chip") if t >= T_IN[n] + 0.5]
    for i, n in enumerate(who):
        cv = char_canvas(n, t); al = cv[..., 3] > 40; rows = np.nonzero(al.any(axis=1))[0]
        if not len(rows): continue
        top = rows[0]; hh = rows[-1] - top
        crop = cv[top:int(top + hh * 0.52), :]
        cols = np.nonzero((crop[..., 3] > 40).any(axis=0))[0]; crop = crop[:, cols[0]:cols[-1] + 1]
        hw = int(2 * R * (0.70 if len(who) == 2 else 0.95)); hh2 = int(crop.shape[0] * hw / crop.shape[1])
        head = Image.fromarray(np.ascontiguousarray(crop), "RGBA").resize((hw, hh2), Image.LANCZOS)
        bob = int(4 * math.sin(t * 3 + i * 2) + 6 * talk(n, t))
        ox = (int(R * 0.10) - int(hw * 0.25) if i == 0 else int(R * 0.85)) if len(who) == 2 else int(R - hw / 2)
        win.paste(head, (ox, int(R * 0.35) + bob), head)
    win.putalpha(_mask[key])
    lay.paste(win, (cx - R, cy - R), win)
    d = ImageDraw.Draw(lay, "RGBA")                                           # vetro: riflesso
    d.chord([cx - R * 0.8, cy - R * 0.85, cx + R * 0.3, cy + R * 0.1], 180, 300, fill=(255, 255, 255, 60))
    d.ellipse([cx - R * 0.55, cy - R * 0.62, cx - R * 0.35, cy - R * 0.42], fill=(255, 255, 255, 120))


def flame(c, x, y, t, size=1.0, ang=0.0):
    """fiamma del motore: coni sovrapposti che tremano + bagliore"""
    for k, (col, sc) in enumerate((((255, 120, 30), 1.0), ((255, 200, 60), 0.72), ((255, 250, 210), 0.42))):
        L = size * 330 * sc * (1 + 0.15 * math.sin(t * 40 + k) + 0.08 * math.sin(t * 67)); wd = size * 95 * sc
        pts = []
        for i in range(17):
            u = i / 16; xx = math.sin(math.pi * u) * wd * (1 - 0.15 * math.sin(t * 50 + i))
            pts.append((xx * (1 if u < 0.5 else 1), L * (u ** 0.8 if i else 0)))
        poly = [(x + (-wd + 2 * wd * i / 16) * 0.5, y) for i in range(17)]
        tri = [(x - wd * 0.5, y), (x + wd * 0.5, y), (x + 8 * math.sin(t * 30), y + L)]
        c.d.polygon([(c.X(px), c.Y(py)) for px, py in tri], fill=col + (230,))
    glow_blob(c, x, y + 120 * size, 260 * size, (120, 70, 20), 0.9)


def smoke(c, x, y, t, t0, n=24, spread=420, life=2.2, seed=3):
    """fumo del decollo che si allarga a terra"""
    if t < t0: return
    for k in range(n):
        tk = t0 + k * 0.05
        if t < tk: continue
        u = clamp((t - tk) / life); side = -1 if k % 2 else 1
        px = x + side * spread * (1 - (1 - u) ** 2) * (0.4 + 0.6 * ((k * 0.37) % 1)); py = y - 60 * u * ((k * 0.61) % 1)
        rr = (60 + 140 * u) * c.Z * (0.6 + 0.4 * ((k * 0.73) % 1))
        g = int(230 - 40 * ((k * 0.3) % 1))
        c.d.ellipse([c.X(px) - rr, c.Y(py) - rr * 0.8, c.X(px) + rr, c.Y(py) + rr * 0.8], fill=(g, g, g + 8, int(190 * (1 - u) ** 0.8)))


# ------------------------------------------------------------------ sfondi
_bg = {}
def bg_arr(sid):
    if sid not in _bg:
        im = Image.open(os.path.join(HERE, "assets", "amb", sid + ".png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.6))
        a = np.asarray(im).astype(np.float32)
        if sid == "luna":                                                    # suolo lunare grigio (non sabbia)
            yy = np.arange(H)[:, None]; m = np.clip((yy - 1050) / 80.0, 0, 1)[..., None]
            g = a.mean(axis=2, keepdims=True) * np.array([0.96, 0.98, 1.06], np.float32)
            a = a * (1 - m) + g * m
        _bg[sid] = a
    return _bg[sid]


_grid = None
def background(sid, t):
    global _grid
    if _grid is None: _grid = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    xs, ys = _grid; arr = bg_arr(sid)
    if sid == "spazio":
        sy = (ys - (t - T_W1) * 60) % H                                     # la nebulosa scorre: si sale
        out = cv2.remap(arr, xs, sy.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    elif sid == "notte_giardino":
        dx = 3 * np.sin(0.8 * t + ys * 0.01) * np.clip((ys - 700) / 600, 0, 1) * np.clip((1350 - ys) / 300, 0, 1)   # cespugli nel vento
        out = cv2.remap(arr, (xs + dx).astype(np.float32), ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    else:
        out = arr
    return np.clip(out, 0, 255).astype(np.uint8)


_sr = np.random.default_rng(31)
STARS = [(float(_sr.uniform(0, W)), float(_sr.uniform(0, H)), float(_sr.choice([0.3, 0.6, 1.0, 1.6], p=[.45, .3, .17, .08])), float(_sr.uniform(0, 6.28))) for _ in range(260)]


def starfield(c, t, speed):
    for (x, y0, d, ph) in STARS:
        y = (y0 + (t - T_W1) * speed * d) % H
        tw = 0.6 + 0.4 * math.sin(t * (2 + d) + ph); r = (1.2 + 2.2 * d) * tw
        ln = speed * d * 0.06
        if ln > 4: c.gd.line([(x, y), (x, y - ln)], fill=(int(220 * tw),) * 3, width=max(1, int(r)))
        else: star4(c.gd, x, y, r * 1.6, (int(230 * tw),) * 3)
    c.glow_used = True


def fireflies(c, t):
    for k in range(22):
        rng = np.random.default_rng(200 + k); x0 = rng.uniform(0, W); y0 = rng.uniform(800, 1500)
        x = x0 + 40 * math.sin(t * 0.7 + k); y = y0 + 30 * math.sin(t * 0.9 + k * 2)
        a = max(0.0, math.sin(t * rng.uniform(1.5, 3) + k)) ** 2
        if a > 0.05: glow_blob(c, x, y, 16, (int(160 * a), int(200 * a), int(60 * a)), 1.0, 4)


def moon_dust(c, t):
    for (j0s, nm) in ((JUMPS["mouse"], "mouse"), (JUMPS["chip"], "chip")):
        x, y = POS3[nm]
        for (j0, jd, _) in j0s:
            puff(c, x, y, j0, 1.2, n=14, spread=150, size=18, seed=int(j0 * 10), col=(205, 205, 215), grav=20)
            puff(c, x, y, j0 + jd, 1.4, n=16, spread=190, size=20, seed=int(j0 * 7), col=(205, 205, 215), grav=15)


def cheese_bubble(c, t, x, y):
    """nuvoletta del pensiero con una fetta di formaggio coi buchi"""
    if not (T_THINK <= t < V["t3"] + 0.2): return
    u = back(clamp((t - T_THINK) / 0.35)); k = clamp((V["t3"] + 0.2 - t) / 0.2)
    s = u * k
    if s <= 0.02: return
    for i, (dx, dy, r) in enumerate(((60, -60, 16), (110, -130, 26))):
        c.d.ellipse([c.X(x + dx) - r * s * c.Z, c.Y(y + dy) - r * s * c.Z, c.X(x + dx) + r * s * c.Z, c.Y(y + dy) + r * s * c.Z], fill=(255, 255, 255, 235))
    bx, by = x + 230, y - 300; R = 150 * s
    for (ox, oy, rr) in ((0, 0, 1.0), (-0.7, 0.1, 0.65), (0.7, 0.1, 0.65), (-0.35, -0.45, 0.6), (0.35, -0.45, 0.6), (0, 0.45, 0.6)):
        c.d.ellipse([c.X(bx + ox * R) - rr * R * c.Z, c.Y(by + oy * R) - rr * R * 0.8 * c.Z, c.X(bx + ox * R) + rr * R * c.Z, c.Y(by + oy * R) + rr * R * 0.8 * c.Z], fill=(255, 255, 255, 245))
    wob = 4 * math.sin(t * 5)
    tri = [(bx - R * 0.75, by + R * 0.35), (bx + R * 0.75, by + R * 0.35), (bx + R * 0.45, by - R * 0.45 + wob)]
    c.d.polygon([(c.X(px), c.Y(py)) for px, py in tri], fill=(255, 205, 60, 255), outline=(220, 150, 30, 255))
    c.d.polygon([(c.X(bx - R * 0.75), c.Y(by + R * 0.35)), (c.X(bx + R * 0.75), c.Y(by + R * 0.35)), (c.X(bx + R * 0.75), c.Y(by + R * 0.55)), (c.X(bx - R * 0.75), c.Y(by + R * 0.55))], fill=(240, 175, 40, 255))
    for (hx, hy, hr) in ((0.1, 0.1, 0.11), (0.4, -0.1, 0.08), (-0.3, 0.2, 0.09), (0.35, 0.25, 0.06)):
        c.d.ellipse([c.X(bx + hx * R) - hr * R * c.Z, c.Y(by + hy * R) - hr * R * c.Z, c.X(bx + hx * R) + hr * R * c.Z, c.Y(by + hy * R) + hr * R * c.Z], fill=(220, 150, 30, 255))


def rock(c, x, y, r, ang=0.0):
    pts = []
    for i in range(10):
        a = i / 10 * 6.283 + ang; rr = r * (0.82 + 0.18 * math.sin(i * 2.7))
        pts.append((c.X(x + math.cos(a) * rr), c.Y(y + math.sin(a) * rr * 0.85)))
    c.d.polygon(pts, fill=(150, 150, 160, 255), outline=(95, 95, 110, 255))
    c.d.ellipse([c.X(x - r * 0.1) - r * 0.6 * c.Z, c.Y(y + r * 0.15) - r * 0.45 * c.Z, c.X(x + r * 0.5) + r * 0.2 * c.Z, c.Y(y + r * 0.7) + r * 0.1 * c.Z], fill=(110, 110, 124, 140))
    c.d.ellipse([c.X(x - r * 0.3) - r * 0.18 * c.Z, c.Y(y - r * 0.2) - r * 0.14 * c.Z, c.X(x - r * 0.3) + r * 0.18 * c.Z, c.Y(y - r * 0.2) + r * 0.14 * c.Z], fill=(115, 115, 128, 255))
    c.d.ellipse([c.X(x + r * 0.25) - r * 0.12 * c.Z, c.Y(y + r * 0.2) - r * 0.1 * c.Z, c.X(x + r * 0.25) + r * 0.12 * c.Z, c.Y(y + r * 0.2) + r * 0.1 * c.Z], fill=(115, 115, 128, 255))
    c.d.ellipse([c.X(x - r * 0.4) - r * 0.15 * c.Z, c.Y(y - r * 0.55) - r * 0.08 * c.Z, c.X(x - r * 0.4) + r * 0.15 * c.Z, c.Y(y - r * 0.55) + r * 0.08 * c.Z], fill=(200, 200, 212, 200))


def flag(c, t, x, ybase):
    """bandiera rossa con stella che sventola (piantata da Chip)"""
    if t < T_FLAG0: return
    if t < T_FLAG1:
        p = (t - T_FLAG0) / (T_FLAG1 - T_FLAG0); hx, hy = POS3["chip"][0] + 60, POS3["chip"][1] - 380
        fx = lerp(hx, x, p); fy = lerp(hy, ybase, p) - 4 * p * (1 - p) * 260; ang = 300 * (1 - p)
    else: fx, fy, ang = x, ybase, osc(t, T_FLAG1, 10, 7, 18)
    lay = Image.new("RGBA", (420, 520), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rectangle([200, 40, 212, 520], fill=(225, 225, 235, 255))
    d.ellipse([196, 28, 216, 48], fill=(255, 215, 80, 255))
    pts = []
    for i in range(13):
        u = i / 12; wv = 14 * math.sin(t * 6 - u * 6) * u
        pts.append((212 + 190 * u, 52 + wv))
    for i in range(12, -1, -1):
        u = i / 12; wv = 14 * math.sin(t * 6 - u * 6) * u
        pts.append((212 + 190 * u, 172 + wv))
    d.polygon(pts, fill=(225, 40, 50, 255))
    star = [(307 + 40 * math.cos(math.radians(-90 + i * 36)) * (1 if i % 2 == 0 else 0.45), 112 + 40 * math.sin(math.radians(-90 + i * 36)) * (1 if i % 2 == 0 else 0.45)) for i in range(10)]
    d.polygon(star, fill=(255, 255, 255, 255))
    lay = lay.resize((int(420 * c.Z), int(520 * c.Z)), Image.LANCZOS).rotate(ang, resample=Image.BICUBIC, center=(206 * c.Z, 520 * c.Z))
    c.img.paste(lay, (int(c.X(fx) - 206 * c.Z), int(c.Y(fy) - 520 * c.Z)), lay)
    if T_FLAG1 <= t < T_FLAG1 + 0.8:
        puff(c, x, ybase, T_FLAG1, 0.9, n=12, spread=110, size=16, seed=4, col=(205, 205, 215), grav=10)
        sparkles(c, x + 90, ybase - 420, T_FLAG1, 0.8, n=10, spread=120, rise=30, size=16, seed=5)


# ------------------------------------------------------------------ scene
POS1 = {"mouse": (250.0, 1790.0), "chip": (850.0, 1800.0)}
RK1 = (560.0, 1650.0)
POS3 = {"mouse": (320.0, 1720.0), "chip": (640.0, 1740.0)}
RK3 = (880.0, 1560.0)
FLAG3 = (480.0, 1470.0)


def rocket1_state(t):
    """(y base, angolo, build, nose) del razzo nella S1"""
    build = back(clamp((t - T_B1) / 0.45), 1.4) if t >= T_B1 else 0.0
    nose = 1.0 if t >= T_B2L else 0.0
    yb = RK1[1]; ang = 0.0
    if T_CNT[0] <= t < T_LAUNCH:                                               # tremolio del conto alla rovescia
        k = clamp((t - T_CNT[0]) / (T_LAUNCH - T_CNT[0])); ang = (1 + 3 * k) * math.sin(t * 47); yb += 2 * k * math.sin(t * 61)
    if t >= T_LAUNCH:
        u = t - T_LAUNCH; yb -= 60 * u * u + 260 * u * u * u; ang = 1.5 * math.sin(t * 30)
    return yb, ang, build, nose


def draw_s1(c, t):
    fireflies(c, t)
    yb, ang, build, nose = rocket1_state(t)
    items = [(RK1[1], "rocket")] + [(POS1[n][1], n) for n in CHARS]
    if t >= T_LAUNCH:
        flame(c, RK1[0], yb - 10, t, 2.1); smoke(c, RK1[0], RK1[1], t, T_LAUNCH - 0.1, n=40, spread=560, life=2.4)
    elif t >= T_CNT[0]:
        k = clamp((t - T_CNT[0]) / (T_LAUNCH - T_CNT[0]))
        smoke(c, RK1[0], RK1[1], t, T_CNT[0], n=int(4 + 10 * k), spread=160, life=1.6)
        if t >= T_CNT[2]: flame(c, RK1[0], yb - 10, t, 0.35 + 0.4 * clamp((t - T_CNT[2]) / 0.6))
    for _, kind in sorted(items):
        if kind == "rocket":
            if build > 0:
                contact(c, RK1[0], RK1[1], 260, 120 if t < T_LAUNCH else int(120 * clamp(1 - (t - T_LAUNCH) / 0.6)))
                rocket_draw(c, RK1[0], yb, RK_H["notte_giardino"], t, ang, build, nose)
                if T_B1 <= t < T_B1 + 0.6: puff(c, RK1[0], RK1[1], T_B1, 0.6, n=16, spread=280, size=24, seed=2, col=(225, 210, 180))
                if T_B3 <= t < T_B3 + 1.0: sparkles(c, RK1[0], RK1[1] - 500, T_B3, 1.0, n=20, spread=380, rise=60, size=20, seed=7)
            if T_B2 <= t < T_B2L:                                                # la punta lanciata da Chip vola sul razzo
                p = (t - T_B2) / (T_B2L - T_B2); hx, hy = POS1["chip"][0] - 40, POS1["chip"][1] - 420
                tx, ty = RK1[0], RK1[1] - RK_H["notte_giardino"] * 0.85
                x_, y_ = lerp(hx, tx, p), lerp(hy, ty, p) - 4 * p * (1 - p) * 380
                im = load("rocket"); full = sized("rocket", h=RK_H["notte_giardino"] * c.Z); nz = full.crop((0, 0, full.width, int(full.height * 0.31)))
                paste_c(c, nz, x_, y_, 360 * (1 - p))
            if T_B2L <= t < T_B2L + 0.6: sparkles(c, RK1[0], RK1[1] - RK_H["notte_giardino"] * 0.75, T_B2L, 0.6, n=12, spread=130, rise=20, size=18, seed=3)
        else:
            n = kind; x, y = POS1[n]
            if t < T_IN[n]: draw_char(c, n, t, x, y)
            elif t < T_IN[n] + 0.55:                                             # salta dentro l'oblò e rimpicciolisce
                p = (t - T_IN[n]) / 0.55; tx = RK1[0]; ty = RK1[1] - RK_H["notte_giardino"] * 0.42
                xx = lerp(x, tx, ease(p)); yy = lerp(y, ty, p) - 4 * p * (1 - p) * 330
                draw_char(c, n, t, xx, yy, scale=lerp(1, 0.25, p ** 1.5), alpha=clamp((1 - p) * 3))
    # numeri del conto alla rovescia (i bambini contano)
    for i, tc in enumerate(T_CNT):
        if tc - 0.05 <= t < min(tc + 0.55, (T_CNT + [V["t1"]])[i + 1] - 0.03):
            u = (t - tc + 0.05) / 0.6; s = back(clamp(u / 0.3)) * (1 - 0.15 * u); a = int(255 * clamp((1 - u) * 3))
            text(c.d, str(3 - i), W / 2, 520, int(420 * s), (255, 230, 80, a), (190, 50, 60, a), 16)
    if V["t1"] - 0.02 <= t < V["t1"] + 0.8:
        u = (t - V["t1"] + 0.02) / 0.8; a = int(255 * clamp((1 - u) * 2.5))
        text(c.d, "VIA!", W / 2, 520, int(300 * back(clamp(u / 0.25))), (255, 255, 255, a), (230, 60, 40, a), 16)


def draw_s2(c, t):
    starfield(c, t, 900)
    u = t - T_SAT                                                                # Saturno che passa
    if -1.5 < u < 4.5:
        sx = 210 + 30 * u; sy = -250 + 330 * (u + 1.5)
        sp = sized("saturn", w=520 * c.Z); paste_c(c, sp, sx, sy, -12)
    for k in range(3):                                                         # comete
        t0 = T_W1 + 0.6 + k * 1.3; p = (t - t0) / 0.9
        if 0 <= p < 1:
            x0, y0 = 1150 - p * 1500, 200 + k * 260 + p * 500
            c.gd.line([(x0, y0), (x0 + 260, y0 - 90)], fill=(160, 180, 255), width=5); c.glow_used = True
            star4(c.gd, x0, y0, 18, (255, 255, 255))
    wob = 3 * math.sin(t * 2.1)
    x, yb = 540 + 30 * math.sin(t * 0.9), 1530 + 25 * math.sin(t * 1.7)
    if T_W2 - 0.9 < t: yb -= 1200 * ((t - T_W2 + 0.9) / 0.9) ** 2
    flame(c, x, yb - 10, t, 1.35, wob)
    rocket_draw(c, x, yb, RK_H["spazio"], t, wob)


def draw_s3(c, t):
    # razzo che atterra
    p = clamp((t - T_W2) / (T_LAND - T_W2))
    yb = RK3[1] - 1600 * (1 - ease(p)) ** 1.6
    if t < T_LAND + 0.2: flame(c, RK3[0], yb - 10, t, 0.9 * (1 - clamp((t - T_LAND) / 0.2)))
    if T_LAND <= t < T_LAND + 1.4: puff(c, RK3[0], RK3[1], T_LAND, 1.4, n=24, spread=320, size=30, seed=9, col=(205, 205, 215), grav=10)
    contact(c, RK3[0], RK3[1], 230, int(120 * p))
    rocket_draw(c, RK3[0], yb + 5 * osc(t, T_LAND, 1, 8, 20), RK_H["luna"], t)
    moon_dust(c, t)
    items = [(POS3[n][1], n) for n in CHARS] + [(FLAG3[1], "flag")]
    for _, kind in sorted(items):
        if kind == "flag": flag(c, t, *FLAG3); continue
        n = kind; x, y = POS3[n]
        if t < T_OUT[n]: continue
        if t < T_OUT[n] + 0.8:                                                   # esce dall'oblò con un salto lento
            q = (t - T_OUT[n]) / 0.8; sx_ = RK3[0]; sy_ = RK3[1] - RK_H["luna"] * 0.42
            xx = lerp(sx_, x, ease(q)); yy = lerp(sy_, y, q) - 4 * q * (1 - q) * 260
            draw_char(c, n, t, xx, yy, scale=lerp(0.3, 1, q ** 0.7))
            if q > 0.9: puff(c, x, y, T_OUT[n] + 0.72, 0.9, n=12, spread=140, size=18, seed=3, col=(205, 205, 215), grav=10)
            continue
        draw_char(c, n, t, x, y)
        if n == "mouse":                                                         # il sasso: raccolto, 'assaggiato', sputato
            if t < T_PICK + 0.45:
                if t >= T_W2 + 1.0: rock(c, x + 40, y - 30, 70)                      # il sasso è a terra davanti a lui
            elif t < T_BITE:
                hx, hy = hand_pt(n, x, y, 0.34); rock(c, hx, hy, 70)
            elif T_BITE <= t < T_SPIT:
                q = (t - T_BITE) / (T_SPIT - T_BITE); hx, hy = hand_pt(n, x, y, lerp(0.34, 0.64, ease(q))); rock(c, hx, hy, 70)
            elif T_SPIT <= t < T_SPIT + 1.6:
                q = (t - T_SPIT) / 1.6; rx = x + 40 + 420 * q; ry = y - H_CH[n] * 0.66 + (-500 * q + 620 * q * q) * 1.0
                if ry < y: rock(c, rx, ry, 70, q * 8)
                else: rock(c, rx, y - 30, 70)
            elif t >= T_SPIT + 1.6: rock(c, x + 460, y - 30, 70)
            cheese_bubble(c, t, x, y - H_CH[n] * 0.95)
            if T_SPIT <= t < T_SPIT + 0.7:
                u = (t - T_SPIT) / 0.7; a = int(255 * (1 - u))
                text(c.d, "BLEAH!", c.X(x + 60), c.Y(y - H_CH[n] * 1.15) - 40 * u, int(110 * c.Z * back(u / 0.25)), (180, 255, 120, a), (40, 110, 40, a), int(9 * c.Z))
    if T_WAVE <= t < T_WAVE + 2.0: sparkles(c, 540, 330, T_WAVE, 2.0, n=24, spread=320, rise=40, size=22, seed=12)


def wipe(c, t):
    """lampo di luce + stelle che corrono (cambio ambiente)"""
    for tw in WIPES:
        if abs(t - tw) > 0.55: continue
        cover = ease(1 - abs(t - tw) / 0.5)
        wash = Image.new("RGBA", (W, H), (255, 252, 240, int(255 * cover))); c.img.paste(wash, (0, 0), wash)


# ------------------------------------------------------------------ camera
CAM = [  # (t, cx, cy, z)
    (0.0, 540, 1250, 1.12), (V["n1"] + 0.6, 540, 1260, 1.08), (T_B1 - 0.2, 540, 1200, 1.0), (T_B2L + 0.4, 560, 1150, 1.05),
    (V["c1"], 700, 1350, 1.35), (E("c1") + 0.3, 560, 1200, 1.04), (T_IN["chip"] + 0.6, 560, 1150, 1.08), (T_CNT[0], 560, 1150, 1.12),
    (T_LAUNCH, 560, 1150, 1.22), (T_LAUNCH + 1.0, 560, 960, 1.0), (T_W1 - 0.01, 560, 960, 1.0),
    (T_W1, 540, 1150, 1.0), (T_SAT, 540, 1150, 1.0), (V["c2"] + 0.1, 420, 1000, 1.3), (E("c2") + 0.3, 480, 1100, 1.15), (T_W2 - 0.01, 540, 1100, 1.0),
    (T_W2, 620, 1250, 1.0), (T_LAND + 0.5, 600, 1300, 1.05), (T_OUT["chip"] + 0.9, 480, 1350, 1.18), (T_J1, 480, 1200, 1.05),
    (V["t2"] + 1.6, 480, 1250, 1.08), (T_PICK, 400, 1450, 1.3), (T_THINK + 0.2, 470, 1300, 1.25), (T_SPIT + 0.4, 420, 1420, 1.32),
    (V["c3"] + 0.4, 480, 1400, 1.2), (T_FLAG0, 480, 1350, 1.12), (T_WAVE + 0.8, 540, 1100, 1.0), (DUR, 540, 1150, 1.03),
]
SHAKES = [(T_B1, 10), (T_B2L, 8), (T_LAUNCH, 26), (T_LAUNCH + 0.4, 16), (T_LAND, 22), (T_SPIT, 8)]


def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 5 * math.sin(t * 0.8) + 3 * math.sin(t * 2.3); cy += 4 * math.sin(t * 1.1 + 1)
    for kt, amp in SHAKES:
        if kt <= t < kt + 0.5:
            k = (1 - (t - kt) / 0.5) * amp; cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    if T_CNT[0] <= t < T_LAUNCH: k = 3 + 8 * clamp((t - T_CNT[0]) / (T_LAUNCH - T_CNT[0])); cx += math.sin(t * 70) * k; cy += math.cos(t * 63) * k
    z = max(1.0, z); hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


def scene_at(t):
    cur = SCENES[0][0]
    for sid, t0 in SCENES:
        if t >= t0: cur = sid
    return cur


def scene_img(sid, t, cx, cy, Z):
    arr = background(sid, t)
    box = (cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z)
    img = Image.fromarray(arr).resize((W, H), Image.BICUBIC, box=box).filter(ImageFilter.GaussianBlur(0.3 + 0.8 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z; c.sid = sid
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    if sid == "notte_giardino": draw_s1(c, t)
    elif sid == "spazio": draw_s2(c, t)
    else:
        glow_blob(c, 540, 330, 330, (30, 60, 90), 0.8 + 0.2 * math.sin(t * 1.3))              # alone della Terra
        draw_s3(c, t)
    wipe(c, t)
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); img = ImageChops.add(ImageChops.add(c.img, c.glow), g2)
    else: img = c.img
    return img


def vignette():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.70)) ** 2)
    return np.clip(1 - 0.30 * np.clip(r - 0.45, 0, 1) ** 1.6, 0.6, 1)[..., None].astype(np.float32)
_VIG = None


def frame(i):
    global _VIG
    if _VIG is None: _VIG = vignette()
    t = i / FPS; cx, cy, Z = camera(t)
    sid = scene_at(t)
    img = scene_img(sid, t, cx, cy, Z)
    arr = np.asarray(img).astype(np.float32)
    bright = np.clip(arr - 215, 0, 255) * 3.0
    arr = arr + cv2.resize(cv2.GaussianBlur(cv2.resize(bright, (W // 4, H // 4), interpolation=cv2.INTER_AREA), (0, 0), 3.5), (W, H)) * 0.20
    rng = np.random.default_rng(i)
    arr = arr + rng.normal(0, 2.0, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    img = Image.fromarray(np.clip(arr * _VIG, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img, "RGBA")
    if t < 2.3:                                                                  # HOOK
        u = back(t / 0.35); a = int(255 * clamp((2.3 - t) / 0.4))
        text(d, "SULLA LUNA?!", W / 2, 260 - 10 * math.sin(t * 6), int(118 * clamp(max(0.6, u), 0, 1.0)), (255, 235, 90, a), (110, 40, 160, a), 13)
    subscribe_button(img, t, V["end"] + 0.9)
    return img.tobytes()


def _prep(p):
    try: MO.transition(*p); return None
    except Exception as e: return (p, str(e)[:80])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2)); print({k: round(v, 2) for k, v in V.items()})
        print({k: round(v, 2) for k, v in dict(T_B1=T_B1, T_B2=T_B2, T_CNT0=T_CNT[0], T_LAUNCH=T_LAUNCH, T_W1=T_W1, T_W2=T_W2, T_LAND=T_LAND,
                                                     T_J1=T_J1, T_PICK=T_PICK, T_THINK=T_THINK, T_BITE=T_BITE, T_FLAG0=T_FLAG0, T_WAVE=T_WAVE).items()})
    elif cmd == "prep":
        import time
        t0 = time.time(); ps = precompute(); print(len(ps), "transizioni")
        with Pool(4) as pool:
            for r in pool.imap_unordered(_prep, ps):
                if r: print("manca", r)
        print("fatto in", round(time.time() - t0), "s")
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(round(float(ts) * FPS)))).save(f"/tmp/claude-0/prova/test_r_{ts}.png")
    else:
        if cmd == "renderpart": a, b, out = int(sys.argv[2]), min(int(sys.argv[3]), int(DUR * FPS)), sys.argv[4]
        else: a, b, out = 0, int(DUR * FPS), sys.argv[2]
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(a, b), chunksize=4)):
                ff.stdin.write(fr)
                if n % 90 == 0: print(f"{a + n}/{b}", flush=True)
        ff.stdin.close(); ff.wait()
