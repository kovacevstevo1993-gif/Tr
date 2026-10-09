#!/usr/bin/env python3
"""Short 'Il castello di sabbia' (9:16, 1080x1920, 30 fps): topolino, ELEFANTINO e Chip su tre spiagge animate
(giorno -> baia dorata -> tramonto). Onda che distrugge il castello, getti d'acqua dalla proboscide, castello che cresce,
bandiera, arcobaleno. Personaggi con luce, ombra proiettata e riflesso di bordo per sembrare 3D.
    python3 short_castello.py info | prep | test 1.0 5.5 | render muto.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import morph as MO

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
AUD = "audioG"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))


def lerp(a, b, u): return a + (b - a) * u
def clamp(u, a=0.0, b=1.0): return max(a, min(b, u))
def ease(u): u = clamp(u); return u * u * (3 - 2 * u)
def back(u, k=1.7): u = clamp(u); return 1 + (k + 1) * (u - 1) ** 3 + k * (u - 1) ** 2
def osc(t, t0, amp=1.0, decay=7.0, freq=26.0):
    return amp * math.exp(-decay * (t - t0)) * math.sin(freq * (t - t0)) if t >= t0 else 0.0


# ------------------------------------------------------------------ copione: tempi dalle voci
V = {}
def _seq():
    t = 0.0
    def at(k, gap):
        nonlocal t
        V[k] = t + gap; t = V[k] + D[k]
    at("n1", 0.5); at("t1", 0.2); at("n2", 0.4); at("t2", 0.5); at("n3", 0.6); at("e1", 0.15); at("n4", 0.5); at("n5", 1.7)
    at("c1", 0.9); at("n6", 1.0); at("e2", 0.4); at("n7", 0.8); at("c2", 0.2); at("t3", 0.1); at("end", 0.5)
    return t + 2.4
DUR = _seq()
SAY = {"n1": "narr", "t1": "mouse", "n2": "narr", "t2": "mouse", "n3": "narr", "e1": "ele", "n4": "narr", "n5": "narr", "c1": "chip",
       "n6": "narr", "e2": "ele", "n7": "narr", "c2": "chip", "t3": "mouse", "end": "mouse"}
TXT = {"n1": "Sulla spiaggia, il topolino costruisce un bellissimo castello di sabbia.", "t1": "Che bello!",
       "n2": "Ma arriva una grande onda... Splash!", "t2": "Oh no!", "n3": "Per fortuna arriva un nuovo amico: l'elefantino!",
       "e1": "Ciao!", "n4": "Riempie il secchiello con la proboscide... e spruzza l'acqua sulla sabbia!",
       "n5": "Con la sabbia bagnata, costruiscono insieme un castello altissimo!", "c1": "Ecco la bandiera!",
       "n6": "E con un grande spruzzo, appare un arcobaleno!", "e2": "Che meraviglia!",
       "n7": "Al tramonto, gli amici sono felici. Insieme è tutto più bello!", "c2": "Evviva!", "t3": "Evviva!",
       "end": "Bambini Ciao Ciao! Iscrivetevi al canale!"}
COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 170), "ele": (200, 232, 255)}
VOICES = [(k, V[k], SAY[k], TXT[k], D[k]) for k in V]
E = lambda k: V[k] + D[k]

# scene
TB = V["n4"] + 5.3                    # cerchio magico: spiaggia -> baia
TC = V["n7"] - 0.55                   # baia -> tramonto
IRIS = 0.9
SCENES = [("spiaggia", 0.0), ("spiaggia_baia", TB), ("spiaggia_tramonto", TC)]
HZ = 935                              # orizzonte (coordinate mondo)
SHORE = {"spiaggia": [(-50, 1490), (0, 1476), (464, 1371), (1080, 1223), (1130, 1205)],
         "spiaggia_baia": [(-50, 1330), (0, 1330), (468, 1395), (760, 1350), (972, 1290), (1130, 1260)],
         "spiaggia_tramonto": [(-50, 1490), (0, 1476), (464, 1371), (1080, 1223), (1130, 1205)]}
def shore_y(sid, x):
    p = SHORE[sid]; xs = [a for a, b in p]; ys = [b for a, b in p]
    return np.interp(x, xs, ys)

# onda
T_W = V["n2"] + 2.35                  # l'onda arriva al castello (Splash!)
T_WS = T_W - 1.4                      # il fronte entra sulla sabbia
T_WE = T_W + 3.0
CASTLE1 = (600, 1665)
BUCKET0 = (910, 1752)
HEAP_X = CASTLE1
# S1: elefantino
T_E_IN = V["n3"] + 0.9
ELE_X, ELE_Y = 925, 1640
T_E_ARR = V["e1"] - 0.55
T_FILL0 = V["n4"] + 0.15              # inizia a riempire
T_FILL1 = T_FILL0 + 1.5
T_SPRAY0 = V["n4"] + 2.35
T_SPRAY1 = TB - 0.45
# S2: costruzione
T_BUILD = [V["n5"] + 0.7, V["n5"] + 1.6, V["n5"] + 2.5, V["n5"] + 3.4]
BUILD_S = [0.34, 0.58, 0.80, 1.0]
CASTLE2 = (610, 1660)
CASTLE_H = 800
T_CHIP_IN = V["n5"] + 2.0
T_LANCIA = V["c1"] - 0.2
T_FLAG0 = V["c1"] + 0.05
T_FLAG1 = T_FLAG0 + 0.85
T_FOUNT0 = V["n6"] + 0.5
T_FOUNT1 = T_FOUNT0 + 2.5
T_RAIN = V["n6"] + 1.1
# S3
CASTLE3 = (850, 1610)
T_DANCE = V["n7"] + 0.9
T_SPR3 = V["n7"] + 3.0

GAIT = []
FLIP_WALK = ["cammina_dx", "passa_dx", "cammina_dx_m", "passa_dx_m"]


def walk(name, t0, t1, period=0.60):
    GAIT.append((name, t0, t1, period, "walk"))
    q = period / 4; ev = []; i = 0
    while t0 + i * q < t1 - 1e-6:
        ev.append((t0 + i * q, FLIP_WALK[i % 4], q * 1.0)); i += 1
    ev.append((t1, "neutro", 0.3)); return ev


def run(name, t0, t1, period=0.44):
    GAIT.append((name, t0, t1, period, "run"))
    pl = ["corre", "corre_m"]; q = period / 2; ev = []; i = 0
    while t0 + i * q < t1 - 1e-6:
        ev.append((t0 + i * q, pl[i % 2], q * 0.98)); i += 1
    ev.append((t1, "neutro", 0.32)); return ev


def dance(t0, t1, seq, beat=0.5):
    ev = []; i = 0
    while t0 + i * beat < t1:
        ev.append((t0 + i * beat, seq[i % len(seq)], beat * 0.85)); i += 1
    return ev


def pat(t0, t1, beat=0.34):
    """sabbia battuta: due pose alternate (batte_sabbia / china) per un tamburellare vero"""
    return [(t0 + i * beat, "batte_sabbia" if i % 2 == 0 else "batte_sabbia", 0.15) for i in range(int((t1 - t0) / beat))]


EV = {
    "mouse": [(0.0, "batte_sabbia", 0.01), (V["t1"] - 0.15, "ride", 0.2), (V["t1"] + 0.95, "batte_sabbia", 0.25),
              (T_WS - 1.15, "sorpreso", 0.15), (T_W - 0.8, "fuggi", 0.15), (T_W + 0.35, "sorpreso", 0.2),
              (V["t2"] - 0.25, "triste", 0.25), (V["e1"] + 0.4, "sorpreso", 0.15), (V["n4"] + 0.3, "neutro", 0.25),
              (T_SPRAY0 + 0.6, "sorpreso", 0.15), (T_SPRAY0 + 1.3, "ride", 0.2), (TB - 0.6, "neutro", 0.3)]
             + walk("mouse", TB + 0.05, TB + 0.95) +
             [(max(V["n5"] - 0.1, TB + 1.05), "batte_sabbia", 0.2), (T_BUILD[3] + 0.5, "ride", 0.2), (V["c1"] - 0.15, "sorpreso", 0.15),
              (T_FLAG1 - 0.1, "salto", 0.15), (T_FLAG1 + 1.0, "ride", 0.2), (T_FOUNT0 - 0.1, "salto", 0.15), (T_FOUNT0 + 1.0, "ride", 0.2),
              (V["e2"] - 0.1, "saluta2", 0.2), (E("e2") + 0.2, "neutro", 0.3)]
             + walk("mouse", TC + 0.25, TC + 1.55) + [(TC + 1.6, "neutro", 0.3), (V["n7"] + 0.5, "saluta2", 0.2)]
             + dance(T_DANCE, V["c2"] + 0.2, ["balla", "balla_m"], 0.5)
             + [(V["c2"] + 0.25, "salto", 0.15), (V["t3"] + 0.6, "ride", 0.2)] + dance(V["t3"] + 1.0, V["end"] - 0.15, ["balla_m", "balla"], 0.5)
             + [(V["end"] - 0.1, "saluta2", 0.2)],
    "ele": [(0.0, "neutro", 0.01), (T_E_IN - 0.1, "neutro", 0.01)] + walk("ele", T_E_IN, T_E_ARR) + [
        (V["e1"] - 0.2, "saluta2", 0.2), (E("e1") + 0.15, "neutro", 0.25), (T_FILL0, "riempie", 0.2), (T_FILL1, "neutro", 0.2),
        (T_SPRAY0, "spruzza_giu", 0.2), (T_SPRAY1, "neutro", 0.25)]
        + walk("ele", TB + 0.05, TB + 0.9) + [
        (V["n5"] - 0.1, "batte_sabbia", 0.2), (T_BUILD[3] + 0.5, "sorpreso", 0.15), (V["c1"] + 0.2, "ride", 0.2),
        (T_FOUNT0 - 0.15, "spruzza", 0.15), (T_FOUNT1, "ride", 0.2), (E("e2") + 0.1, "neutro", 0.3)]
        + walk("ele", TC + 0.25, TC + 1.55) + [(TC + 1.6, "neutro", 0.3), (V["n7"] + 0.5, "saluta2", 0.2), (V["n7"] + 1.5, "saluta2_m", 0.2),
        (V["n7"] + 2.3, "saluta2", 0.2), (T_SPR3, "spruzza", 0.15), (V["c2"] + 0.2, "ride", 0.2), (V["t3"] + 1.2, "saluta2", 0.2),
        (V["t3"] + 1.7, "saluta2_m", 0.2), (V["t3"] + 2.2, "saluta2", 0.2), (V["end"] - 0.1, "saluta2", 0.2)],
    "chip": [(0.0, "neutro", 0.01)] + run("chip", T_CHIP_IN, T_LANCIA - 0.35) + [
        (T_LANCIA, "lancia", 0.15), (T_FLAG1 - 0.1, "salto", 0.15), (T_FLAG1 + 0.9, "ride", 0.2), (T_FOUNT0 + 0.2, "salto", 0.15),
        (T_FOUNT0 + 1.2, "ride", 0.2), (E("e2"), "neutro", 0.3)]
        + walk("chip", TC + 0.25, TC + 1.4) + [(TC + 1.45, "neutro", 0.3), (V["n7"] + 0.5, "saluta2", 0.2)]
        + dance(T_DANCE, V["c2"] - 0.1, ["balla_m", "balla"], 0.5)
        + [(V["c2"] - 0.05, "salto", 0.15), (V["c2"] + 0.9, "ride", 0.2)] + dance(V["t3"] + 1.0, V["end"] - 0.15, ["balla", "balla_m"], 0.5)
        + [(V["end"] - 0.1, "saluta2", 0.2)],
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
APPEAR = {"mouse": 0.0, "ele": T_E_IN - 0.5, "chip": T_CHIP_IN - 0.3}
ALIAS = {"ele": {"salto": "spruzza", "balla": "saluta2", "saluta": "saluta2", "indica": "saluta2", "corre": "cammina_dx", "guarda_su": "sorpreso",
                 "parla_o": "parla_a", "lancia": "saluta2"}}
HAS_MOUTH = {"mouse": ("parla_a", "parla_o"), "chip": ("parla_a", "parla_o"), "ele": ("parla_a",)}
CS = 0.86                              # scala generale dei personaggi
H_CH = {"mouse": 640 * CS, "chip": 600 * CS, "ele": 660 * CS}
CHARS = ["mouse", "ele", "chip"]

KF = {   # (t, x, y)
    "mouse": [(0, 320, 1670), (T_W - 0.8, 320, 1670), (T_W + 0.3, 290, 1690), (TB, 290, 1690), (TB + 0.95, 390, 1690),
              (TC, 390, 1690), (TC + 1.55, 255, 1745), (999, 255, 1745)],
    "ele": [(0, 1300, ELE_Y), (T_E_IN, 1300, ELE_Y), (T_E_ARR, ELE_X, ELE_Y), (TB, ELE_X, ELE_Y), (TB + 0.9, 860, 1665),
            (TC, 860, 1665), (TC + 1.55, 690, 1755), (999, 690, 1755)],
    "chip": [(0, -250, 1745), (T_CHIP_IN, -250, 1745), (T_LANCIA - 0.35, 130, 1750), (TC, 130, 1750), (TC + 1.4, 470, 1775), (999, 470, 1775)],
}
# punti utili sulle pose (frazione dell'altezza, rispetto ai piedi): (dx, dy_alto)
TIP = {"riempie": (0.0, 0.40), "spruzza_giu": (-0.15, 0.53), "spruzza": (0.02, 1.37)}
LAUNCH = (0.24, 0.54)      # mano di Chip che lancia la bandiera


def persp(y): return clamp(0.5 + (y - 1200) / 440 * 0.5, 0.5, 1.1)


def gait_info(name, t):
    for (n, t0, t1, per, kind) in GAIT:
        if n == name and t0 <= t < t1: return kind, ((t - t0) / per) % 1.0, per
    return None, 0.0, 1.0


def kf_pos(name, t):
    kf = KF[name]
    if t <= kf[0][0]: return kf[0][1], kf[0][2], False
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        if t0 <= t <= t1:
            mv = (x0, y0) != (x1, y1)
            u = (t - t0) / (t1 - t0) if (gait_info(name, t)[0] or not mv) else ease((t - t0) / (t1 - t0))
            return lerp(x0, x1, u), lerp(y0, y1, u), mv
    return kf[-1][1], kf[-1][2], False


def rp(name, pose):
    """risolve le pose che non esistono per quel personaggio (nessuna nuova immagine: saldo Pollinations finito)"""
    al = ALIAS.get(name, {}); m = pose.endswith("_m"); b = pose[:-2] if m else pose
    b = al.get(b, b); return b + ("_m" if m else "")


_iou = {}
def pair_dur(name, A, B, dur):
    """più la sagoma cambia, più il passaggio è breve (niente 'fantasmi' a metà strada)"""
    key = (name, rp(name, A), rp(name, B))
    if key not in _iou:
        a = MO.aligned(name, key[1])[..., 3] > 128; b = MO.aligned(name, key[2])[..., 3] > 128
        _iou[key] = float((a & b).sum() / max(1, (a | b).sum()))
    q = _iou[key]
    return min(dur, 0.22 if q > 0.85 else (0.14 if q > 0.70 else 0.09))


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
            A, B = rp(name, a[1]), rp(name, b[1])
            if A != B: pairs.add((name, A, B))
    return sorted(pairs)


# ------------------------------------------------------------------ audio -> parlato (bocca)
_env = {}
def talk(who, t):
    for k, t0, w, tx, d in VOICES:
        if w == who and t0 <= t <= t0 + d:
            if k not in _env:
                with wave.open(os.path.join(HERE, AUD, f"{k}.wav")) as wf:
                    a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
                win = 44100 // (FPS * 2); n = len(a) // win + 1
                e = np.array([np.sqrt(np.mean(a[i * win:(i + 1) * win] ** 2) + 1e-12) for i in range(n)]); _env[k] = e / (np.percentile(e, 95) + 1e-9)
            e = _env[k]; return min(1.0, e[min(len(e) - 1, int((t - t0) * FPS * 2))])
    return 0.0


def mouth_pose(name, t):
    mp = HAS_MOUTH[name]
    def m(e):
        if len(mp) == 1: return "parla_a" if e > 0.30 else "neutro"
        return "parla_a" if e > 0.52 else ("parla_o" if e > 0.17 else "neutro")
    cur = m(talk(name, t)); prev = m(talk(name, t - 1.0 / FPS))
    return prev if (prev == "parla_a" and cur == "parla_o") else cur


def char_canvas(name, t):
    A, B, u = pose_state(name, t)
    if A == B == "neutro": A = B = mouth_pose(name, t)
    A, B = rp(name, A), rp(name, B)
    if A == B: return MO.aligned(name, A), A
    fr = MO.transition(name, A, B); idx = int(ease(u) * (MO.K + 1))
    if idx <= 0: return MO.aligned(name, A), A
    if idx >= MO.K + 1: return MO.aligned(name, B), B
    return fr[idx - 1], B


# ------------------------------------------------------------------ oggetti 3D
_obj = {}
def load(name):
    if name not in _obj: _obj[name] = Image.open(os.path.join(HERE, "assets", "obj", name + ".png")).convert("RGBA")
    return _obj[name]


def sized(name, w=None, h=None):
    im = load(name)
    if w is None: w = im.width * h / im.height
    if h is None: h = im.height * w / im.width
    return im.resize((max(2, int(w)), max(2, int(h))), Image.LANCZOS)


def star4(d, x, y, r, col):
    k = 0.2; d.polygon([(x, y - r), (x + r * k, y - r * k), (x + r, y), (x + r * k, y + r * k), (x, y + r), (x - r * k, y + r * k), (x - r, y), (x - r * k, y - r * k)], fill=col)


def heart(d, x, y, r, col):
    pts = []
    for i in range(40):
        a = i / 40 * 2 * math.pi
        pts.append((x + r * math.sin(a) ** 3, y - r * (13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)) / 16))
    d.polygon(pts, fill=col)


class Ctx: pass


def paste_c(c, im, x, y, ax=0.5, ay=0.5):
    """incolla uno sprite con ancora (ax, ay) in coordinate schermo"""
    c.img.paste(im, (int(x - im.width * ax), int(y - im.height * ay)), im)


def sparkles(c, x, y, t0, dur, n=14, spread=120, rise=60, size=16, seed=1):
    t = c.t
    if not (t0 <= t < t0 + dur): return
    cols = ((255, 245, 170), (255, 255, 255), (255, 210, 120))
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


RB = [(255, 70, 70), (255, 150, 50), (255, 225, 70), (100, 210, 100), (80, 160, 255), (110, 100, 230), (190, 110, 230)]
_RBC = np.array(RB, dtype=np.float32)
def rainbow(c, t0, cx, cy, R=620, band=36, alpha=0.5):
    if c.t < t0: return
    p = ease((c.t - t0) / 1.6); a = min(1, (c.t - t0) / 0.6) * alpha
    ox, oy = c.X(cx), c.Y(cy); y1 = int(min(H, max(0, oy)))
    if y1 < 4: return
    yy, xx = np.mgrid[0:y1, 0:W].astype(np.float32)
    dx, dy = xx - ox, yy - oy
    idx = R / band - np.sqrt(dx * dx + dy * dy) / (c.Z * band)
    ang = np.arctan2(-dy, dx)
    vis = (idx >= 0) & (idx < 7) & ((math.pi - ang) <= math.pi * p + 1e-3)
    fr = idx - np.floor(idx); edge = np.clip(np.minimum(fr, 1 - fr) * 5, 0, 1) * 0.6 + 0.4
    col = _RBC[np.clip(np.floor(idx).astype(int), 0, 6)]
    al = (vis * a * edge).astype(np.float32)[..., None]
    reg = np.asarray(c.img.crop((0, 0, W, y1))).astype(np.float32)
    out = reg * (1 - al) + col * al
    c.img.paste(Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), (0, 0))


def flap(c, name, x, y, size, ang, phase, mirror=False):
    im = load(name)
    w = max(16, min(int(size * c.Z), 900)); h = int(w * im.height / im.width)
    fl = 0.34 + 0.66 * abs(math.cos(phase))
    r = im.resize((max(4, int(w * fl)), h), Image.LANCZOS)
    if mirror: r = r.transpose(Image.FLIP_LEFT_RIGHT)
    r = r.rotate(ang, resample=Image.BICUBIC, expand=True)
    c.img.paste(r, (int(x - r.width / 2), int(y - r.height / 2)), r)


def subscribe_button(img, t, t0, cy=1810):
    if t < t0: return
    u = back((t - t0) / 0.45); s = max(0.05, u) * (1 + 0.03 * math.sin((t - t0) * 6))
    w, h = 520, 130; Sx = 2; cv = Image.new("RGBA", (w * Sx, h * Sx + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
    d.rounded_rectangle([6 * Sx, 10 * Sx, (w - 6) * Sx, (h - 6) * Sx], radius=34 * Sx, fill=(0, 0, 0, 70))
    d.rounded_rectangle([0, 0, (w - 12) * Sx, (h - 16) * Sx], radius=34 * Sx, fill=(232, 36, 36, 255), outline=(255, 255, 255, 255), width=4 * Sx)
    d.text((((w - 12) / 2 + 34) * Sx, (h - 16) / 2 * Sx), "ISCRIVITI", font=ImageFont.truetype(FONT, 54 * Sx), fill=(255, 255, 255, 255), anchor="mm")
    bell = Image.new("RGBA", (90 * Sx, 90 * Sx), (0, 0, 0, 0)); bd = ImageDraw.Draw(bell)
    bd.pieslice([20 * Sx, 12 * Sx, 70 * Sx, 62 * Sx], 180, 360, fill=(255, 255, 255, 255)); bd.polygon([(20 * Sx, 38 * Sx), (70 * Sx, 38 * Sx), (78 * Sx, 62 * Sx), (12 * Sx, 62 * Sx)], fill=(255, 255, 255, 255))
    bd.ellipse([36 * Sx, 62 * Sx, 54 * Sx, 78 * Sx], fill=(255, 255, 255, 255)); bd.ellipse([40 * Sx, 4 * Sx, 50 * Sx, 14 * Sx], fill=(255, 255, 255, 255))
    bell = bell.rotate(math.sin((t - t0) * 14) * 16 * max(0, 1 - (t - t0) / 1.8), resample=Image.BICUBIC, center=(45 * Sx, 14 * Sx))
    cv.paste(bell, (24 * Sx, int(((h - 16) / 2 - 45) * Sx)), bell)
    cv = cv.resize((int(w * s), int((h + 10) * s)), Image.LANCZOS); img.paste(cv, (int(W / 2 - cv.width / 2), int(cy - cv.height / 2)), cv)


def text(d, s, x, y, size, fill, out, ow):
    d.text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)


# ------------------------------------------------------------------ camera
CAM = [  # (t, cx, cy, z): cy è sempre "in basso" (la camera si ferma al bordo dell'immagine)
    (0.0, 480, 1900, 1.4), (1.6, 500, 1900, 1.32), (3.5, 540, 1900, 1.25), (V["t1"] + 0.2, 480, 1900, 1.34),
    (V["n2"] + 0.5, 600, 1900, 1.15), (T_W - 0.3, 600, 1900, 1.3), (T_W + 0.6, 540, 1900, 1.25), (V["t2"] + 0.2, 480, 1900, 1.3),
    (V["n3"] + 0.4, 600, 1900, 1.1), (T_E_ARR, 600, 1900, 1.1), (E("e1"), 600, 1900, 1.1), (T_FILL0 + 0.5, 700, 1900, 1.18),
    (T_FILL1 + 0.2, 640, 1900, 1.12), (T_SPRAY0 + 0.6, 620, 1900, 1.12), (TB - 0.3, 700, 1900, 1.15), (TB + 0.9, 560, 1900, 1.2),
    (V["n5"] + 0.4, 600, 1900, 1.2), (T_BUILD[2], 600, 1900, 1.12), (T_BUILD[3] + 0.4, 580, 1900, 1.06), (V["c1"] - 0.2, 520, 1900, 1.1),
    (T_FLAG1, 560, 1900, 1.08), (T_FOUNT0 - 0.2, 580, 1900, 1.06), (T_FOUNT0 + 0.8, 580, 1900, 1.0), (T_FOUNT1, 580, 1900, 1.02),
    (TC + 0.3, 540, 1900, 1.05), (V["n7"] + 0.9, 520, 1900, 1.06), (V["c2"], 520, 1900, 1.1), (V["end"] - 0.3, 540, 1900, 1.06),
    (DUR, 540, 1900, 1.02),
]
SHAKES = [(T_W, 26), (T_W + 0.25, 12), (T_BUILD[0], 5), (T_BUILD[1], 6), (T_BUILD[2], 7), (T_BUILD[3], 9), (T_FLAG1, 6)]
def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 8 * math.sin(t * 0.8); cy += 6 * math.sin(t * 1.1 + 1)
    for kt, amp in SHAKES:
        if kt <= t < kt + 0.35:
            k = (1 - (t - kt) / 0.35) * amp; cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    z = max(1.0, z); hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


# ------------------------------------------------------------------ personaggio
def cstate(name, t):
    x, y, mv = kf_pos(name, t)
    kind, ph, per = gait_info(name, t)
    hop = 0.0; rot = 0.0; sq = 1.0
    if kind == "walk":
        hop = (1 - abs(math.cos(2 * math.pi * ph))) * 16; rot = math.sin(2 * math.pi * ph) * 2.2; sq = 1 + 0.016 * math.cos(4 * math.pi * ph)
    elif kind == "run":
        hop = abs(math.sin(2 * math.pi * ph)) * 46; rot = math.sin(2 * math.pi * ph) * 3.5 - 3; sq = 1 + 0.03 * math.cos(4 * math.pi * ph)
    A, B, u = pose_state(name, t)
    for pose, t0 in ((e[1], e[0]) for e in EV[name]):
        if pose in ("salto", "fuggi") and t0 - 0.05 <= t < t0 + 0.8:
            p = clamp((t - (t0 - 0.05)) / 0.85); hop += 4 * p * (1 - p) * (120 if pose == "salto" else 95)
            if t < t0 + 0.1: sq *= 1 - 0.07 * clamp((t - (t0 - 0.05)) / 0.15)
            elif p > 0.85: sq *= 1 - 0.06 * math.sin(math.pi * (p - 0.85) / 0.15)
    for pose, t0 in ((e[1], e[0]) for e in EV[name]):
        if pose == "neutro" and t0 > 1.0: sq *= 1 + osc(t, t0 + 0.05, 0.05, 8, 24)
    tk = talk(name, t); sq *= 1 + 0.022 * tk; rot += math.sin(t * 11 + len(name)) * 1.3 * tk
    if A == B and A in ("batte_sabbia",):                       # tamburella la sabbia
        beat = math.sin(t * 2 * math.pi * 2.6 + len(name)); sq *= 1 + 0.03 * beat; rot += 1.6 * beat
    if A == B and A in ("tiene", "neutro", "saluta", "saluta2", "saluta2_m", "guarda_su", "triste", "sorpreso", "riempie", "spruzza_giu", "spruzza"):
        sq *= 1 + 0.012 * math.sin(t * 3.2 + len(name) * 2)            # respiro
    if A in ("balla", "balla_m") or B in ("balla", "balla_m"):
        ph2 = ((t - T_DANCE) / 0.5) % 1; hop += abs(math.sin(math.pi * ph2)) * 34; rot += math.sin(math.pi * 2 * ph2) * 3.5
    if A in ("saluta2", "saluta2_m") and t > V["end"]: rot += math.sin(t * 6 + len(name)) * 2
    if A == "triste": rot += math.sin(t * 2.0) * 1.2
    return x, y, persp(y), hop, rot, sq


SUN = {"spiaggia": (1.0, 0.35), "spiaggia_baia": (1.0, 0.30), "spiaggia_tramonto": (0.0, -0.40)}   # (inclinazione, schiacciamento ombra: <0 = verso la camera)
TINT = {"spiaggia": (1.0, 1.0, 1.0), "spiaggia_baia": (1.03, 0.96, 0.86), "spiaggia_tramonto": (1.0, 0.80, 0.66)}
RIM = {"spiaggia": ((255, 244, 214), 0.20), "spiaggia_baia": ((255, 214, 150), 0.30), "spiaggia_tramonto": ((255, 150, 70), 0.62)}
RIMDIR = {"spiaggia": (-1, -1), "spiaggia_baia": (-1, -1), "spiaggia_tramonto": (0, -1)}   # da dove viene la luce (dx, dy)


def cast_shadow(c, name, x, y, s, hop, r, nw, nh, sid):
    """ombra proiettata del personaggio (sagoma appiattita) + ombra di contatto"""
    shx, k = SUN[sid]
    al = np.asarray(r.getchannel("A")).astype(np.float32) / 255
    fy = nh * (MO.AY / MO.CH); fx = nw * (MO.AX / MO.CW)
    ext = int(nh * 0.45)
    if k > 0:
        M = np.float32([[1, -shx * 0.9, shx * 0.9 * fy], [0, k, fy * (1 - k)]])
    else:
        M = np.float32([[1, 0, 0], [0, k, fy * (1 - k)]])
    sh = cv2.warpAffine(al, M, (nw + int(abs(shx) * nh * 0.6) + 40, nh + ext), flags=cv2.INTER_LINEAR)
    sig = max(4.0, 11 * c.Z * s); sh = cv2.GaussianBlur(sh, (0, 0), sig)
    fall = clamp(1 - hop / 160.0, 0.4, 1)
    a = (sh * (0.30 if sid != "spiaggia_tramonto" else 0.28) * fall * 255).astype(np.uint8)
    lay = Image.new("RGBA", (sh.shape[1], sh.shape[0]), (20, 22, 40, 0)); lay.putalpha(Image.fromarray(a))
    px, py = c.X(x) - fx, c.Y(y) - fy
    c.img.paste(lay, (int(px), int(py)), lay)


def draw_char(c, name, t):
    x, y, s, hop, rot, sq = cstate(name, t)
    cv, pose = char_canvas(name, t)
    im = Image.fromarray(np.ascontiguousarray(cv), "RGBA")
    if rot: im = im.rotate(rot, resample=Image.BILINEAR, center=(MO.AX, MO.AY))
    f = s * c.Z * CS
    nw, nh = max(2, int(MO.CW * f / math.sqrt(sq))), max(2, int(MO.CH * f * sq))
    r = im.resize((nw, nh), Image.LANCZOS if f < 1 else Image.BICUBIC)
    px, py = c.X(x) - MO.AX * nw / MO.CW, c.Y(y - hop * s) - MO.AY * nh / MO.CH
    sid = c.sid
    cast_shadow(c, name, x, y, s, hop, r, nw, nh, sid)
    # contatto a terra (macchia scura sotto i piedi)
    wsh = H_CH[name] * 0.45 * c.Z * s
    ell = Image.new("RGBA", (int(wsh * 2.4), int(wsh * 0.7)), (0, 0, 0, 0)); ImageDraw.Draw(ell).ellipse([wsh * 0.2, wsh * 0.12, wsh * 2.2, wsh * 0.58], fill=(15, 15, 30, int(95 * clamp(1 - hop / 130, 0.3, 1))))
    ell = ell.filter(ImageFilter.GaussianBlur(max(3, 6 * c.Z))); c.img.paste(ell, (int(c.X(x) - ell.width / 2), int(c.Y(y) - ell.height * 0.5)), ell)
    # luce: tinta dell'ambiente + riflesso di bordo
    arr = np.asarray(r).astype(np.float32); a = arr[..., 3] / 255.0
    rgb = arr[..., :3] * np.array(TINT[sid], dtype=np.float32)
    rimc, rimk = RIM[sid]; dx, dy = RIMDIR[sid]
    sg = max(3.0, 8 * f)
    L = cv2.GaussianBlur(a, (0, 0), sg)
    sh_ = np.float32([[1, 0, -dx * sg * 1.1], [0, 1, -dy * sg * 1.1]])
    Ls = cv2.warpAffine(L, sh_, (nw, nh))
    rim = np.clip(a * (1 - Ls * 1.25), 0, 1) ** 1.3
    rgb = rgb * (1 - 0.35 * (1 - np.clip(a * L * 1.2, 0, 1))[..., None] * 0) + rim[..., None] * np.array(rimc, dtype=np.float32) * rimk
    # leggera ombra propria in basso (volume)
    shade = np.linspace(1.02, 0.90, nh, dtype=np.float32)[:, None, None]
    rgb = np.clip(rgb * shade, 0, 255)
    out = Image.fromarray(np.dstack([rgb, arr[..., 3]]).astype(np.uint8), "RGBA")
    c.img.paste(out, (int(px), int(py)), out)
    return pose


# ------------------------------------------------------------------ ambienti animati
_bg = {}
def bg_arr(sid):
    if sid not in _bg:
        _bg[sid] = Image.open(os.path.join(HERE, "assets", "amb", sid + ".png")).convert("RGB").resize((W, H), Image.BICUBIC)
    return _bg[sid]


_grid = None
def sway(arr, sid, t, cx, cy, Z):
    """mare che ondeggia (più ampio verso riva), palme nel vento, nuvole che scorrono, barca che dondola"""
    global _grid
    if _grid is None: _grid = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    xs, ys = _grid
    wy = (ys - H / 2) / Z + cy; wx = (xs - W / 2) / Z + cx
    sh = shore_y(sid, wx).astype(np.float32)
    sea = np.clip((sh - wy) / 70, 0, 1) * np.clip((wy - HZ) / 40, 0, 1)
    dep = np.clip((wy - HZ) / (sh - HZ + 1), 0, 1)
    dx = sea * (1.5 + 5.5 * dep) * np.sin(2 * math.pi * 0.32 * t + wy * 0.05 + wx * 0.004)
    dy = sea * (0.8 + 2.8 * dep) * np.sin(2 * math.pi * 0.45 * t + wx * 0.021 + wy * 0.03)
    if sid == "spiaggia": palm = np.exp(-((wy - 700) / 190.0) ** 2) * np.clip((wx - 780) / 90, 0, 1) * 7.0
    elif sid == "spiaggia_baia": palm = np.exp(-((wy - 690) / 190.0) ** 2) * np.clip((wx - 820) / 90, 0, 1) * 7.0
    else: palm = (np.exp(-((wy - 640) / 220.0) ** 2) * (np.clip((wx - 780) / 90, 0, 1) + np.clip((100 - wx) / 90, 0, 1)) * 5.0)
    dx = dx + palm * np.sin(2 * math.pi * 0.35 * t + wy * 0.013)
    sky = np.clip((HZ - wy) / 500, 0, 1) ** 0.8
    dx = dx + sky * 16 * np.sin(0.30 * t + wx * 0.002)
    if sid != "spiaggia_baia":                                     # la barca dondola
        bx = 565 if sid == "spiaggia" else 547
        dy = dy + np.exp(-(((wx - bx) / 170) ** 2 + ((wy - 970) / 110) ** 2)) * 4.0 * math.sin(2 * math.pi * 0.5 * t)
    return cv2.remap(arr, xs + (dx * Z).astype(np.float32), ys + (dy * Z).astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def glints(c, sid, t):
    """riflessi che scintillano sul mare"""
    rng = np.random.default_rng({"spiaggia": 3, "spiaggia_baia": 5, "spiaggia_tramonto": 9}[sid]); X, Y, Z = c.X, c.Y, c.Z
    n = 46
    for k in range(n):
        bx = rng.uniform(40, 1040); by = rng.uniform(HZ + 15, float(shore_y(sid, bx)) - 50); ph = rng.uniform(0, 6.28); sp = rng.uniform(0.8, 2.2)
        a = max(0.0, math.sin(t * sp * 2.0 + ph)) ** 3
        if a < 0.08: continue
        r = (5 + 9 * (by - HZ) / 400) * Z * (0.5 + a)
        col = (255, 255, 255) if sid != "spiaggia_tramonto" else (255, 225, 170)
        star4(c.gd, X(bx), Y(by), r, tuple(int(v * a * 0.9) for v in col)); c.glow_used = True


def foam_line(c, sid, t):
    """schiuma che respira sulla battigia"""
    X, Y, Z = c.X, c.Y, c.Z
    pts_t, pts_b = [], []
    for x in range(-60, 1150, 40):
        sy = float(shore_y(sid, x)); w = 7 * math.sin(t * 1.3 + x * 0.012) + 4 * math.sin(t * 2.1 + x * 0.03)
        pts_t.append((X(x), Y(sy + w - 10))); pts_b.append((X(x), Y(sy + w + 8 + 4 * math.sin(t * 1.7 + x * 0.02))))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(lay).polygon(pts_t + pts_b[::-1], fill=(255, 255, 255, 90))
    lay = lay.filter(ImageFilter.GaussianBlur(4 * Z)); c.img.paste(lay, (0, 0), lay)


def gull(c, x, y, size, t, ph, mirror=False):
    flap(c, "seagull", x, y, size, -6 * math.sin(t * 2 + ph), t * 9 + ph, mirror)


def ambient(c, sid, t):
    X, Y, Z = c.X, c.Y, c.Z
    glints(c, sid, t)
    if sid == "spiaggia_tramonto":
        g = 0.8 + 0.2 * math.sin(t * 0.9); glow_blob(c, 486, 930, 760, (120, 62, 20), g)
        for k in range(6):                                     # raggi di sole
            a0 = 0.5 + 0.5 * math.sin(t * 0.6 + k * 1.1); ang = -math.pi / 2 + (k - 2.5) * 0.28
            x1, y1 = 486 + math.cos(ang) * 1500, 930 + math.sin(ang) * 1500
            c.gd.polygon([(X(486), Y(930)), (X(x1 - 70), Y(y1)), (X(x1 + 70), Y(y1))], fill=(int(16 * a0), int(9 * a0), int(3 * a0))); c.glow_used = True
    elif sid == "spiaggia_baia":
        g = 0.8 + 0.2 * math.sin(t * 1.1); glow_blob(c, 140, 150, 620, (80, 66, 30), g)
    else:
        g = 0.8 + 0.2 * math.sin(t * 1.3); glow_blob(c, 900, 120, 560, (70, 62, 34), g)
    # gabbiani che attraversano il cielo
    plan = {"spiaggia": [(1.0, 360, 1, 190), (3.6, 250, -1, 150), (12.0, 420, 1, 170)],
            "spiaggia_baia": [(TB + 4.0, 300, 1, 180), (TB + 9.0, 230, -1, 140)],
            "spiaggia_tramonto": [(TC + 1.0, 400, 1, 160), (TC + 3.0, 300, -1, 130), (TC + 7.0, 360, 1, 150)]}[sid]
    for k, (t0, yy, d_, sz) in enumerate(plan):
        u = (t - t0) / 6.5
        if 0 <= u <= 1:
            px = lerp(-200, 1280, u) if d_ > 0 else lerp(1280, -200, u); py = yy + 46 * math.sin(u * 8 + k)
            gull(c, X(px), Y(py), sz, t, k, mirror=(d_ < 0))
    # granelli di sabbia/pulviscolo nell'aria
    rng = np.random.default_rng(12)
    for k in range(18):
        bx, by, sp, ph = rng.uniform(40, 1040), rng.uniform(900, 1800), rng.uniform(0.3, 1.0), rng.uniform(0, 6.28)
        px = (bx + t * 25 * sp) % 1100 - 10; py = by + math.sin(t * 0.7 * sp + ph) * 30
        a = 0.25 + 0.5 * max(0.0, math.sin(t * 1.7 * sp + ph)); r = (2 + 2 * sp) * Z
        c.d.ellipse([X(px) - r, Y(py) - r, X(px) + r, Y(py) + r], fill=(255, 246, 215, int(150 * a)))
    if sid == "spiaggia_baia":                                  # farfalle sulla baia
        for k, (cx_, cy_, ph) in enumerate(((250, 1250, 0.0), (800, 1100, 2.0))):
            px = cx_ + 160 * math.sin(t * 0.5 + ph) + 40 * math.sin(t * 2.3 + ph); py = cy_ + 90 * math.sin(t * 0.7 + ph * 1.3) + 25 * math.sin(t * 3.1)
            flap(c, "bf_open", X(px), Y(py), 70 * Z, 12 * math.sin(t * 0.7 + ph), t * 22 + ph)


# ------------------------------------------------------------------ getti d'acqua
G = 2300.0
def water_drop(c, x, y, r, a=215):
    X, Y = c.X(x), c.Y(y)
    c.d.ellipse([X - r, Y - r * 1.15, X + r, Y + r * 1.15], fill=(176, 226, 255, a))
    c.d.ellipse([X - r * 0.45, Y - r * 0.7, X + r * 0.15, Y - r * 0.2], fill=(255, 255, 255, min(255, a + 30)))


def stream(c, tip_fn, vel_fn, ta, tb, ground, wid=15.0, ref=0.0):
    """getto continuo: il fluido emesso al tempo tau ha velocità vel_fn(tau). Disegna la scia con bordi luminosi.
    tip_fn(tau) -> (x0, y0) punto d'uscita al tempo tau"""
    t = c.t
    if t < ta: return None
    pts = []; land = None
    tau_hi = min(t, tb); tau_lo = max(ta, t - 1.6)
    n = 34
    for i in range(n + 1):
        tau = tau_hi - (tau_hi - tau_lo) * i / n
        x0, y0 = tip_fn(tau); vx, vy = vel_fn(tau); a = t - tau
        x = x0 + vx * a; y = y0 + vy * a + 0.5 * G * a * a
        if y >= ground:
            # trova il punto d'impatto e ferma
            disc = vy * vy + 2 * G * (ground - y0); ai = (-vy + math.sqrt(max(0, disc))) / G
            land = (x0 + vx * ai, ground, tau); break
        pts.append((x, y, a))
    if len(pts) >= 2:
        for lw, col in ((1.0, (150, 205, 245, 170)), (0.62, (205, 238, 255, 225)), (0.25, (255, 255, 255, 250))):
            for (x1, y1, a1), (x2, y2, a2) in zip(pts, pts[1:]):
                wd = max(2, wid * lw * c.Z * (1.0 - 0.45 * min(1, a1 / 1.2)))
                c.d.line([(c.X(x1), c.Y(y1)), (c.X(x2), c.Y(y2))], fill=col, width=int(wd))
        # gocce staccate attorno al getto
        rng = np.random.default_rng(int(ta * 100) % 997)
        for k in range(14):
            idx = int(rng.integers(0, len(pts))); x, y, a = pts[idx]
            x += rng.normal() * 16; y += rng.normal() * 12
            water_drop(c, x, y, (3 + 3 * rng.random()) * c.Z, 190)
    return land


def splash(c, x, y, t0, dur=0.7, n=18, power=330, seed=1):
    t = c.t
    if not (t0 <= t < t0 + dur): return
    rng = np.random.default_rng(seed)
    for k in range(n):
        a = -math.pi / 2 + rng.uniform(-1.2, 1.2); v = power * rng.uniform(0.5, 1.2); u = t - t0
        px = x + math.cos(a) * v * u; py = y + math.sin(a) * v * u + 0.5 * G * u * u * 0.8
        if py > y + 8: continue
        water_drop(c, px, py, (3 + 4 * rng.random()) * c.Z * (1 - 0.5 * u / dur), int(215 * (1 - u / dur)))
    r = (20 + 150 * clamp((t - t0) / dur)) * c.Z
    c.d.ellipse([c.X(x) - r, c.Y(y) - r * 0.3, c.X(x) + r, c.Y(y) + r * 0.3], outline=(235, 248, 255, int(220 * (1 - (t - t0) / dur))), width=max(2, int(5 * c.Z)))


def fountain(c, x0, y0, ta, tb, seed=3, rate=240):
    """grande spruzzo verso l'alto (gocce con scia)"""
    t = c.t
    if t < ta: return
    rng = np.random.default_rng(seed)
    n = int((tb - ta) * rate)
    for i in range(n):
        ti = ta + (tb - ta) * i / n; age = t - ti
        if age < 0 or age > 1.8: continue
        ang = -math.pi / 2 + rng.normal() * 0.16; v = rng.uniform(900, 1700)
        x = x0 + math.cos(ang) * v * age; y = y0 + math.sin(ang) * v * age + 0.5 * G * age * age
        if i % 3 == 0:
            xp = x0 + math.cos(ang) * v * (age - 0.04); yp = y0 + math.sin(ang) * v * (age - 0.04) + 0.5 * G * (age - 0.04) ** 2
            c.d.line([(c.X(xp), c.Y(yp)), (c.X(x), c.Y(y))], fill=(205, 238, 255, 170), width=max(2, int(5 * c.Z)))
        water_drop(c, x, y, (3.5 + 4 * rng.random()) * c.Z, 205)


# ------------------------------------------------------------------ oggetti di scena
def dust_puff(c, x, y, t0, big=1.0, seed=0):
    u = (c.t - t0) / 0.7
    if not 0 <= u < 1: return
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    for j in range(7):
        dx = (j - 3) * 52 * big + math.sin(j * 2.1 + seed) * 12; r = (22 + 58 * u) * big * c.Z; a = int(150 * (1 - u))
        ld.ellipse([c.X(x + dx * (0.6 + u)) - r, c.Y(y - 14 - 50 * u * (1 + 0.3 * math.sin(j))) - r * 0.8, c.X(x + dx * (0.6 + u)) + r, c.Y(y - 14 - 50 * u * (1 + 0.3 * math.sin(j))) + r * 0.8], fill=(236, 214, 160, a))
    lay = lay.filter(ImageFilter.GaussianBlur(8)); c.img.paste(lay, (0, 0), lay)


def wave_D(t):
    if t < T_WS or t > T_WE: return None
    if t < T_W + 0.45: return 330 * ease((t - T_WS) / (T_W + 0.45 - T_WS)) ** 0.8
    return 330 * (1 - ease((t - T_W - 0.45) / (T_WE - T_W - 0.45)))


def wave_front(sid, x, t):
    """posizione y del fronte dell'onda sulla sabbia in x (None se assente); x può essere un array"""
    D_ = wave_D(t)
    if D_ is None: return None
    sh = shore_y(sid, x); g = 0.42 + 0.58 * np.exp(-((x - 640) / 330.0) ** 2)
    return sh + D_ * g + 10 * np.sin(x * 0.02 + t * 3)


_noise = None
def noise_tex():
    global _noise
    if _noise is None:
        rng = np.random.default_rng(5); n = rng.random((64, 36)).astype(np.float32)
        n = cv2.GaussianBlur(cv2.resize(n, (W // 2, H // 2), interpolation=cv2.INTER_CUBIC), (0, 0), 5); _noise = ((n - n.min()) / (n.max() - n.min())).astype(np.float32)
    return _noise


def water_sheet(c, t):
    """acqua che invade la sabbia: trasparente verso riva, più densa e schiumosa al fronte"""
    Dw = wave_D(t)
    if Dw is None: return
    Z = c.Z; y0 = int(max(0, c.Y(1180))); y1 = int(min(H, c.Y(2000)))
    if y1 - y0 < 4: return
    yy, xx = np.mgrid[y0:y1, 0:W].astype(np.float32)
    wx = (xx - W / 2) / Z + c.cx; wy = (yy - H / 2) / Z + c.cy
    sh = shore_y("spiaggia", wx).astype(np.float32); fr = wave_front("spiaggia", wx, t).astype(np.float32)
    d = (wy - sh) / np.maximum(fr - sh, 1.0)
    inside = ((d > 0) & (d < 1)).astype(np.float32)
    fade = clamp((T_WE - t) / 0.9)
    nz = noise_tex(); nh, nw_ = nz.shape
    u = ((xx * 0.5 + t * 22) % nw_).astype(np.float32); v = ((yy * 0.5 - t * 14) % nh).astype(np.float32)
    n1 = cv2.remap(nz, u, v, cv2.INTER_LINEAR, borderMode=cv2.BORDER_WRAP)
    alpha = np.clip(d * 2.2, 0, 1) ** 1.2 * 0.62 * inside
    near = np.exp(-((wy - fr) / (26.0)) ** 2) * (0.55 + 0.9 * n1)           # schiuma al fronte
    near2 = np.exp(-((wy - fr + 54) / 14.0) ** 2) * (0.25 + 0.7 * n1) * 0.7
    foam = np.clip(near + near2, 0, 1) * (wy < fr + 18)
    base = np.array([60, 184, 206], np.float32); lite = np.array([150, 232, 240], np.float32)
    col = base[None, None, :] * (1 - n1[..., None] * 0.6) + lite[None, None, :] * (n1[..., None] * 0.6)
    reg = np.asarray(c.img.crop((0, y0, W, y1))).astype(np.float32)
    out = reg * (1 - (alpha * fade)[..., None]) + col * (alpha * fade)[..., None]
    out = out * (1 - (foam * fade)[..., None]) + 255.0 * (foam * fade)[..., None]
    c.img.paste(Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), (0, y0))


def noise_at(xx, yy, t, sx=22.0, sy=-14.0):
    nz = noise_tex(); nh, nw_ = nz.shape
    u = ((xx * 0.5 + t * sx) % nw_).astype(np.float32); v = ((yy * 0.5 + t * sy) % nh).astype(np.float32)
    return cv2.remap(nz, u, v, cv2.INTER_LINEAR, borderMode=cv2.BORDER_WRAP)


def crest(c, t):
    """cresta dell'onda gigante che avanza sul mare: faccia scura trasparente + schiuma rumorosa (niente poligoni piatti)"""
    sid = "spiaggia"; Z = c.Z
    u2 = clamp(t / (T_WS + 0.2)) ** 1.4; fade = 1 - clamp((t - T_WS - 0.1) / 0.5)
    if fade <= 0: return
    y0 = int(max(0, c.Y(HZ + 10))); y1 = int(min(H, c.Y(1620)))
    if y1 - y0 < 4: return
    yy, xx = np.mgrid[y0:y1, 0:W].astype(np.float32)
    wx = (xx - W / 2) / Z + c.cx; wy = (yy - H / 2) / Z + c.cy
    sh = shore_y(sid, wx).astype(np.float32)
    yc = (HZ + 90) * (1 - u2) + (sh - 30) * u2 + 6 * np.sin(wx * 0.02 + t * 2)
    hg = (30 + 75 * u2) * (0.78 + 0.22 * np.sin(wx * 0.011 + 1.3))
    r = (wy - yc) / hg
    n1 = noise_at(xx, yy, t)
    face = np.clip(1 - np.abs(r + 0.15) / 0.85, 0, 1) ** 1.4 * (0.30 + 0.35 * u2) * fade
    foam = (np.exp(-((r + 0.85) / 0.16) ** 2) * (0.55 + 0.9 * n1) + np.exp(-((r + 0.55) / 0.30) ** 2) * (0.20 + 0.5 * n1) * 0.8)
    foam = np.clip(foam, 0, 1) * (0.45 + 0.55 * u2) * fade
    reg = np.asarray(c.img.crop((0, y0, W, y1))).astype(np.float32)
    out = reg * (1 - face[..., None]) + np.array([28, 132, 168], np.float32) * face[..., None]
    out = out * (1 - foam[..., None]) + 255.0 * foam[..., None]
    c.img.paste(Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), (0, y0))


def big_wave(c, t):
    """onda gigante: prima una cresta che avanza sul mare, poi l'acqua che invade la sabbia"""
    sid = "spiaggia"; X, Y, Z = c.X, c.Y, c.Z
    if t < T_WS + 0.7: crest(c, t)
    if T_WS <= t < T_WE: water_sheet(c, t)
    if t >= T_W + 0.5:                                       # sabbia bagnata che resta (si asciuga piano)
        w_ = clamp(1 - (t - T_W - 0.5) / 14.0, 0.0, 1.0) * clamp((t - T_W - 0.5) / 0.6)
        pts_t, pts_b = [], []
        for x in range(-60, 1150, 30):
            sh = float(shore_y(sid, x)); g = 0.42 + 0.58 * math.exp(-((x - 640) / 330.0) ** 2)
            pts_t.append((X(x), Y(sh))); pts_b.append((X(x), Y(sh + 300 * g + 12)))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(lay).polygon(pts_t + pts_b[::-1], fill=(84, 62, 28, int(64 * w_)))
        lay = lay.filter(ImageFilter.GaussianBlur(14 * Z)); c.img.paste(lay, (0, 0), lay)


def castle1_scale(t):
    """il castello del topolino cresce a scatti nei primi secondi"""
    st = [(0.0, 0.52), (0.9, 0.7), (1.9, 0.85), (2.9, 1.0)]
    s = st[0][1]
    for t0, v in st:
        if t >= t0: s = lerp(s, v, 1.0) if False else v
    k = [i for i, (t0, v) in enumerate(st) if t >= t0][-1]
    prev = st[k - 1][1] if k > 0 else st[0][1]
    return lerp(prev, st[k][1], back((t - st[k][0]) / 0.35, 1.5)) if k > 0 else st[0][1]


def props_s1(c, t):
    X, Y, Z = c.X, c.Y, c.Z
    cx, cy = CASTLE1
    # pala piantata nella sabbia
    sv = sized("shovel", h=210 * Z); c.img.paste(sv, (int(X(520) - sv.width / 2), int(Y(1706) - sv.height * 0.92)), sv)
    # castello / macerie
    if t < T_W + 0.05:
        s = castle1_scale(t); cs = sized("castle_small", w=520 * s * Z)
        if t >= T_WS + 0.4:                                         # trema all'arrivo dell'onda
            cs = cs.rotate(2.0 * math.sin(t * 40) * clamp((t - T_WS - 0.4) / 0.9), resample=Image.BICUBIC, expand=True)
        c.img.paste(cs, (int(X(cx) - cs.width / 2), int(Y(cy) - cs.height * 0.86)), cs)
        for kt in (0.9, 1.9, 2.9): dust_puff(c, cx, cy, kt, 0.8, seed=kt)
    else:
        he = sized("sand_heap", w=500 * Z)
        wet = clamp((t - T_SPRAY0 - 0.7) / 1.2)
        if wet > 0:
            arr = np.asarray(he).astype(np.float32); arr[..., :3] *= (1 - 0.30 * wet); he = Image.fromarray(arr.astype(np.uint8), "RGBA")
        c.img.paste(he, (int(X(cx) - he.width / 2), int(Y(cy + 20) - he.height * 0.72)), he)
        if wet > 0 and t < T_SPRAY1 + 1.0:
            sparkles(c, cx, cy - 40, T_SPRAY0 + 0.7, 2.6, n=8, spread=140, rise=20, size=11, seed=5)
def fg_s1(c, t):
    """secchiello in primo piano (davanti all'elefantino) che si riempie e poi si svuota"""
    X, Y, Z = c.X, c.Y, c.Z
    bx, by = BUCKET0
    bk = sized("bucket", w=190 * Z)
    x0, y0 = int(X(bx) - bk.width / 2), int(Y(by) - bk.height * 0.9)
    c.img.paste(bk, (x0, y0), bk)
    fill = clamp((t - T_FILL0 - 0.35) / (T_FILL1 - T_FILL0 - 0.35)) * (1 - 0.55 * clamp((t - T_SPRAY0 - 0.2) / (T_SPRAY1 - T_SPRAY0)))
    if fill > 0.02:
        lay = Image.new("RGBA", bk.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.ellipse([bk.width * 0.14, bk.height * (0.20 - 0.03 * fill), bk.width * 0.86, bk.height * (0.20 - 0.03 * fill) + bk.height * 0.2], fill=(70, 186, 232, 235), outline=(215, 246, 255, 255), width=3)
        c.img.paste(lay, (x0, y0), lay)


def bucket_rim(): return BUCKET0[1] - 0.72 * (190 * 0.9)




def tip_world(name, pose, t):
    x, y, s, hop, rot, sq = cstate(name, t); dx, dy = TIP[pose]
    return x + dx * H_CH[name] * s, y - hop * s - dy * H_CH[name] * s


def jets_s1(c, t):
    # riempie il secchiello
    if T_FILL0 + 0.3 <= t < T_FILL1 + 0.8:
        land = stream(c, lambda tau: tip_world("ele", "riempie", min(max(tau, T_FILL0), T_FILL1)), lambda tau: (-8, 120), T_FILL0 + 0.3, T_FILL1 - 0.1, bucket_rim(), wid=22)
        if land: splash(c, land[0], land[1], t - (t * 12 % 0.2), 0.3, 6, 140, seed=int(t * 12))
    # spruzza sul mucchio di sabbia
    if T_SPRAY0 + 0.3 <= t < T_SPRAY1 + 0.9:
        def vel(tau):
            sw = math.sin((tau - T_SPRAY0) * 3.0)
            return (-470 + 120 * sw, -210)
        land = stream(c, lambda tau: tip_world("ele", "spruzza_giu", min(max(tau, T_SPRAY0), T_SPRAY1)), vel, T_SPRAY0 + 0.3, T_SPRAY1, CASTLE1[1] - 70, wid=28)
        if land:
            splash(c, land[0], land[1], t - (t * 9 % 0.35), 0.5, 10, 260, seed=int(t * 9))


def props_s2(c, t):
    X, Y, Z = c.X, c.Y, c.Z
    cx, cy = CASTLE2
    # secchiello e pala accanto
    bk = sized("bucket", w=190 * Z); c.img.paste(bk, (int(X(985) - bk.width / 2), int(Y(1790) - bk.height * 0.9)), bk)
    sv = sized("shovel", h=200 * Z); c.img.paste(sv, (int(X(705) - sv.width / 2), int(Y(1790) - sv.height * 0.92)), sv)
    st = 0.0; tl = None
    for i, tb_ in enumerate(T_BUILD):
        if t >= tb_: st = BUILD_S[i]; tl = tb_; i0 = i
    if st > 0:
        prev = BUILD_S[i0 - 1] if i0 > 0 else 0.12
        s = lerp(prev, st, back((t - tl) / 0.45, 1.5))
        cs = sized("castle_big", h=CASTLE_H * s * Z)
        c.img.paste(cs, (int(X(cx) - cs.width / 2), int(Y(cy + 8) - cs.height * 0.97)), cs)
        for kt in T_BUILD: dust_puff(c, cx, cy, kt, 1.4, seed=kt)
        if t >= T_BUILD[3] and t < T_BUILD[3] + 2.0: sparkles(c, cx, cy - CASTLE_H * 0.55, T_BUILD[3], 2.0, n=22, spread=300, rise=40, size=18, seed=4)
    elif t >= T_BUILD[0] - 0.8:
        mound = sized("sand_heap", w=300 * Z); c.img.paste(mound, (int(X(cx) - mound.width / 2), int(Y(cy + 12) - mound.height * 0.72)), mound)
    flag_draw(c, t, CASTLE2, CASTLE_H)


def flag_pos0(t):
    x, y, s, hop, rot, sq = cstate("chip", t)
    return x + LAUNCH[0] * H_CH["chip"] * s, y - hop * s - LAUNCH[1] * H_CH["chip"] * s


def flag_draw(c, t, castle, ch, ground_tint=1.0):
    """bandiera: in mano a Chip, lanciata, piantata in cima al castello e che sventola"""
    X, Y, Z = c.X, c.Y, c.Z
    top = (castle[0] + 10, castle[1] - ch * 0.93)
    if t < T_LANCIA - 0.02: return
    if t < T_FLAG0:
        px, py = flag_pos0(t); ang = -60 + 40 * ((t - T_LANCIA) / max(0.05, T_FLAG0 - T_LANCIA)); wave_k = 0.4
    elif t < T_FLAG1:
        u = (t - T_FLAG0) / (T_FLAG1 - T_FLAG0); p0 = flag_pos0(T_FLAG0)
        px = lerp(p0[0], top[0], ease(u)); py = lerp(p0[1], top[1], u) - 340 * math.sin(math.pi * u); ang = -20 + 380 * u; wave_k = 1.0
    else:
        px, py = top; ang = 4 * osc(t, T_FLAG1, 1.0, 5, 30); wave_k = 1.0
        if t < T_FLAG1 + 0.6: py += 10 * math.sin(math.pi * clamp((t - T_FLAG1) / 0.3))
    L = 190 * Z; pw = 8 * Z
    a = math.radians(ang - 90); ux, uy = math.cos(a), math.sin(a)
    x0, y0 = X(px), Y(py)
    x1, y1 = x0 + ux * L, y0 + uy * L
    c.d.line([(x0, y0), (x1, y1)], fill=(120, 76, 38, 255), width=int(pw)); c.d.ellipse([x1 - pw * 0.9, y1 - pw * 0.9, x1 + pw * 0.9, y1 + pw * 0.9], fill=(255, 214, 74, 255))
    # tessuto che sventola
    nx, ny = -uy, ux; fw, fh = 112 * Z, 74 * Z
    top_pts, bot_pts = [], []
    for i in range(11):
        f = i / 10; w_ = math.sin(t * 9 - f * 4.2) * 11 * Z * f * wave_k
        bx_ = x1 - ux * 6 * Z + nx * fw * f + ux * w_ * 0.0 + ux * w_; by_ = y1 - uy * 6 * Z + ny * fw * f + uy * w_
        sc = 1 - 0.55 * f
        top_pts.append((bx_ + ux * 0, by_ + uy * 0)); bot_pts.append((bx_ + ux * fh * sc, by_ + uy * fh * sc))
    c.d.polygon(top_pts + bot_pts[::-1], fill=(232, 52, 64, 255), outline=(150, 20, 34, 255))
    mx, my = (top_pts[3][0] + bot_pts[3][0]) / 2, (top_pts[3][1] + bot_pts[3][1]) / 2
    star4(c.d, mx, my, 16 * Z, (255, 236, 120, 255))


def jets_s2(c, t):
    if T_FOUNT0 <= t < T_FOUNT1 + 2.0:
        x0, y0 = tip_world("ele", "spruzza", min(max(t, T_FOUNT0), T_FOUNT1))
        fountain(c, x0, y0, T_FOUNT0, T_FOUNT1)
        if T_FOUNT0 + 0.2 < t < T_FOUNT1 + 1.4: sparkles(c, x0, y0 - 140, T_FOUNT0, T_FOUNT1 - T_FOUNT0 + 1.4, n=16, spread=200, rise=70, size=15, seed=11)


def props_s3(c, t):
    X, Y, Z = c.X, c.Y, c.Z
    cx, cy = CASTLE3
    cs = sized("castle_big", h=CASTLE_H * 0.78 * Z)
    arr = np.asarray(cs).astype(np.float32); arr[..., :3] = np.clip(arr[..., :3] * np.array([1.0, 0.82, 0.68]) + np.array([14, 4, 0]), 0, 255)
    cs = Image.fromarray(arr.astype(np.uint8), "RGBA")
    # ombra lunga del castello verso la camera
    shd = cs.copy(); a_ = np.asarray(shd.getchannel("A")).astype(np.float32) / 255
    M = np.float32([[1, 0, 0], [0, -0.30, cs.height * 0.97 * 1.30]]); sh = cv2.warpAffine(a_, M, (cs.width, cs.height + int(cs.height * 0.45)))
    sh = cv2.GaussianBlur(sh, (0, 0), 10 * Z); lay = Image.new("RGBA", (sh.shape[1], sh.shape[0]), (20, 20, 40, 0)); lay.putalpha(Image.fromarray((sh * 90).astype(np.uint8)))
    c.img.paste(lay, (int(X(cx) - cs.width / 2), int(Y(cy + 8) - cs.height * 0.97)), lay)
    c.img.paste(cs, (int(X(cx) - cs.width / 2), int(Y(cy + 8) - cs.height * 0.97)), cs)
    flag_draw(c, t, (cx, cy), CASTLE_H * 0.78)
    if T_SPR3 <= t < T_SPR3 + 2.6:
        x0, y0 = tip_world("ele", "spruzza", T_SPR3 + 0.01) if False else (None, None)


def jets_s3(c, t):
    if T_SPR3 <= t < T_SPR3 + 2.2:
        x0, y0 = tip_world("ele", "spruzza", t if True else T_SPR3)
        fountain(c, x0, y0, T_SPR3, T_SPR3 + 1.6, seed=8, rate=200)
        sparkles(c, x0, y0 - 120, T_SPR3, 2.2, n=14, spread=180, rise=60, size=14, seed=13)


# ------------------------------------------------------------------ fotogramma
def scene_at(t):
    cur = SCENES[0][0]
    for sid, t0 in SCENES:
        if t >= t0: cur = sid
    return cur


def scene_img(sid, t, cx, cy, Z):
    base = bg_arr(sid).resize((W, H), Image.BICUBIC, box=(cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z))
    arr = sway(np.asarray(base), sid, t, cx, cy, Z)
    img = Image.fromarray(arr).filter(ImageFilter.GaussianBlur(0.4 + 0.9 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z; c.sid = sid; c.cx = cx; c.cy = cy
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    foam_line(c, sid, t)
    if sid == "spiaggia_baia" and T_RAIN <= t < TC + 1: rainbow(c, T_RAIN, CASTLE2[0] + 20, 1480, R=760, band=40, alpha=0.55)
    ambient(c, sid, t)
    if sid == "spiaggia":
        props_s1(c, t); big_wave(c, t)
    if sid == "spiaggia_baia": props_s2(c, t)
    if sid == "spiaggia_tramonto": props_s3(c, t)
    if sid == "spiaggia_tramonto" and t >= V["n7"] + 0.4:           # cuori
        for k in range(10):
            uu = ((t - V["n7"]) * 0.45 + k / 10) % 1.0; hpx = c.X(220 + k * 70 + math.sin(uu * 8 + k) * 40); hpy = c.Y(1450 - uu * 640)
            heart(c.d, hpx, hpy, 28 * Z * (0.6 + 0.4 * math.sin(math.pi * uu)), (255, 120, 160, int(220 * math.sin(math.pi * uu))))
    vis = [n for n in CHARS if t >= APPEAR[n]]
    for n in sorted(vis, key=lambda n: kf_pos(n, t)[1]): draw_char(c, n, t)
    if sid == "spiaggia": fg_s1(c, t); jets_s1(c, t)
    if sid == "spiaggia_baia": jets_s2(c, t)
    if sid == "spiaggia_tramonto": jets_s3(c, t)
    if sid == "spiaggia" and T_W <= t < T_W + 0.9:                  # Splash sul castello
        for k in range(3): splash(c, CASTLE1[0] + (k - 1) * 120, CASTLE1[1] - 40, T_W + k * 0.05, 0.85, 22, 520, seed=k + 7)
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); img = ImageChops.add(ImageChops.add(img, c.glow), g2)
    if sid == "spiaggia_baia": img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 232, 196))), 0.18)
    if sid == "spiaggia_tramonto": img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 214, 176))), 0.20)
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
    for (s0, t0), (s1, t1) in zip(SCENES, SCENES[1:]):             # cerchio magico tra due ambienti
        if t1 <= t < t1 + IRIS:
            nxt = scene_img(s1, t, cx, cy, Z); prv = scene_img(s0, t, cx, cy, Z)
            mx, my, _ = kf_pos("mouse", t); mx = (mx - cx) * Z + W / 2; my = (my - 300 - cy) * Z + H / 2
            r = ease((t - t1) / IRIS) * 2300
            m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([mx - r, my - r, mx + r, my + r], fill=255)
            img = Image.composite(nxt, prv, m)
            d0 = ImageDraw.Draw(img, "RGBA")
            for q in range(3):
                rr = r - q * 10
                if rr > 2: d0.ellipse([mx - rr, my - rr, mx + rr, my + rr], outline=(255, 238, 150, int(230 - q * 70)), width=14 - q * 4)
            for q in range(18):
                a = q * 2.4 + t * 3; star4(d0, mx + math.cos(a) * r, my + math.sin(a) * r, 18 + 8 * (q % 3), (255, 245, 190, 255))
    arr = np.asarray(img).astype(np.float32) * 0.62 + np.asarray(ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 246, 232)))).astype(np.float32) * 0.38
    img = Image.fromarray(np.clip(arr * _VIG, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img, "RGBA")
    if t < 2.5:                                                      # HOOK
        u = back(t / 0.35); a = int(255 * clamp((2.5 - t) / 0.4))
        text(d, "ARRIVA", W / 2, 205 - 10 * math.sin(t * 6), int(180 * max(0.1, u)), (255, 240, 120, a), (190, 40, 70, a), 12)
        if t >= 0.4: text(d, "L'ONDA!", W / 2, 370, int(140 * max(0.1, back((t - 0.4) / 0.35))), (255, 255, 255, a), (30, 90, 160, a), 10)
    for k, t0, who, txt, dur in VOICES:                              # sottotitoli
        if t0 - 0.05 <= t <= t0 + dur + 0.3:
            u = ease((t - t0 + 0.05) / 0.18); f = ImageFont.truetype(FONT, 66 if who == "narr" else 78); lines = []; cur = ""
            for wd in txt.split():
                tl_ = (cur + " " + wd).strip(); bb = d.textbbox((0, 0), tl_, font=f, anchor="mm", stroke_width=6)
                if bb[2] - bb[0] > 930 and cur: lines.append(cur); cur = wd
                else: cur = tl_
            lines.append(cur); yy = (640 if t < 2.5 else 250) - 41 * (len(lines) - 1) + (1 - u) * 14
            for ln in lines: text(d, ln, W / 2, yy, 66 if who == "narr" else 78, COL[who] + (int(255 * u),), (50, 40, 30, int(255 * u)), 7); yy += 84
            break
    subscribe_button(img, t, V["end"] + 0.9, cy=1810)
    return img.tobytes()


def _prep(p):
    try: MO.transition(*p); return None
    except Exception as e: return (p, str(e)[:80])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2)); print({k: round(v, 2) for k, v in V.items()})
        print({"TB": round(TB, 2), "TC": round(TC, 2), "T_W": round(T_W, 2), "T_SPRAY0": round(T_SPRAY0, 2), "T_FOUNT0": round(T_FOUNT0, 2)})
    elif cmd == "prep":
        import time
        t0 = time.time(); ps = precompute(); print(len(ps), "transizioni")
        with Pool(4) as pool:
            for r in pool.imap_unordered(_prep, ps):
                if r: print("manca", r)
        print("fatto in", round(time.time() - t0), "s")
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts) * FPS))).save(f"test_c_{ts}.png")
    else:
        out = sys.argv[2]; N = int(DUR * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 60 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
