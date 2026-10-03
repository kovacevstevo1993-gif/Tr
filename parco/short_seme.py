#!/usr/bin/env python3
"""Short 'Il seme magico' (9:16, 1080x1920, 24 fps): tre ambienti (bosco -> giardino -> tramonto), i personaggi fanno
quello che dice la narrazione. Ambienti animati (vento, nuvole, raggi, lucciole, foglie, uccellini, farfalle, pioggia),
albero che cresce davvero, mele che cadono e vengono prese al volo, transizioni a cerchio magico.
    python3 short_seme.py info | prep | test 1.0 5.5 | render muto.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import morph as MO

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 24
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
AUD = "audioF"
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
    at("n1", 0.4); at("n2", 0.35); at("t1", 0.15); at("n3", 0.5); at("n4", 0.6); at("t2", 0.2); at("n5", 0.5)
    at("n6", 0.5); at("t3", 0.2); at("c1", 0.05); at("s1", 0.1); at("n7", 0.6); at("c2", 0.25); at("s2", 0.1)
    at("n8", 0.5); at("t4", 0.25); at("n9", 0.7); at("c3", 0.3); at("s3", 0.1); at("n10", 0.5); at("end", 0.45)
    return t + 2.2
DUR = _seq()
E = lambda k: V[k] + D[k]
SAY = {"n1": "narr", "n2": "narr", "t1": "mouse", "n3": "narr", "n4": "narr", "t2": "mouse", "n5": "narr", "n6": "narr",
       "t3": "mouse", "c1": "chip", "s1": "spike", "n7": "narr", "c2": "chip", "s2": "spike", "n8": "narr", "t4": "mouse",
       "n9": "narr", "c3": "chip", "s3": "spike", "n10": "narr", "end": "mouse"}
TXT = {"n1": "Nel bosco magico, il topolino passeggia felice.", "n2": "Guarda! Un seme che brilla!", "t1": "Che bello!",
       "n3": "Lo porta nel suo giardino... e lo pianta nella terra.",
       "n4": "Ma il seme ha sete! Ecco una nuvoletta che porta la pioggia!", "t2": "Evviva!", "n5": "Pop! Spunta un germoglio!",
       "n6": "Il topolino chiama i suoi amici.", "t3": "Chip! Spike! Venite!", "c1": "Arrivo!", "s1": "Aspettami!",
       "n7": "E l'albero cresce, cresce, cresce... altissimo!", "c2": "Che alto!", "s2": "Che meraviglia!",
       "n8": "Splash! Cadono le mele rosse!", "t4": "Prendiamole!", "n9": "Al tramonto, gli amici mangiano insieme le mele dolci.",
       "c3": "Che buona!", "s3": "Buonissima!", "n10": "Stare insieme è sempre più bello.", "end": "Bambini Ciao Ciao! Iscrivetevi al canale!"}
COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 170), "spike": (200, 225, 255)}
VOICES = [(k, V[k], SAY[k], TXT[k], D[k]) for k in V]

# ------------------------------------------------------------------ scene e momenti chiave
TB = V["n3"] + 1.3                    # cerchio magico: bosco -> giardino
TC = V["n9"] - 0.3                    # cerchio magico: giardino -> tramonto
IRIS = 0.9
T_ARR = V["n2"] + 0.1                 # il topolino arriva al seme
T_PICK = V["n2"] + 1.0                # si china a prenderlo
T_HOLD = V["t1"] - 0.15
T_PLANT = TB + 1.3                    # arriva dove piantare
T_SEED_IN = T_PLANT + 0.6             # il seme entra nella terra
CL0 = V["n4"] + 1.7                   # la nuvoletta entra
RAIN0, RAIN1 = CL0 + 1.4, V["n5"] + 0.2
CL1 = RAIN1 + 0.5
T_SPR = V["n5"] + 0.55                # spunta il germoglio
T_CHIP, T_SPIKE = V["t3"] + 0.7, V["t3"] + 1.1
T_CHIP_END, T_SPIKE_END = E("s1") + 0.25, E("s1") + 0.5
G0 = V["n7"] + 0.35                   # l'albero cresce
G1 = G0 + 3.3
FALL0 = V["n8"] + 0.25                # cadono le mele
LAND = {"mouse": V["t4"] + 0.9, "chip": V["t4"] + 1.1, "spike": V["t4"] + 1.3}   # mela che atterra nelle mani
ET = {"mouse": V["n9"] + 1.2, "chip": V["n9"] + 1.9, "spike": V["n9"] + 2.5}     # primo morso
T_DANCE = V["n10"] - 0.1
P = (760, 1610)                       # dove si pianta (base dell'albero)
TREE_H = 1250
SEED0 = (575, 1550)                   # il seme nel bosco
SCENES = [("bosco", 0.0), ("giardino", TB), ("tramonto", TC)]

GAIT = []


def walk(name, t0, t1, period=0.56):
    GAIT.append((name, t0, t1, period, "walk"))
    pl = ["cammina_sx", "neutro", "cammina_dx", "neutro"]; q = period / 4; ev = []; i = 0
    while t0 + i * q < t1 - 1e-6:
        ev.append((t0 + i * q, pl[i % 4], q * 0.98)); i += 1
    ev.append((t1, "neutro", 0.3)); return ev


def run(name, t0, t1, period=0.42):
    GAIT.append((name, t0, t1, period, "run"))
    pl = ["corre", "corre_m"]; q = period / 2; ev = []; i = 0
    while t0 + i * q < t1 - 1e-6:
        ev.append((t0 + i * q, pl[i % 2], q * 0.98)); i += 1
    ev.append((t1, "neutro", 0.32)); return ev


def dance(t0, t1, first="balla", beat=0.46):
    pl = [first, first + "_m" if not first.endswith("_m") else first[:-2]]; ev = []; i = 0
    while t0 + i * beat < t1:
        ev.append((t0 + i * beat, pl[i % 2], beat * 0.9)); i += 1
    return ev


def eat(n):
    """mani aperte -> mela in mano -> morso -> masticare (mangia_mela / mangia_mela2 alternati)"""
    ev = [(LAND[n] - 0.6, "riceve", 0.3), (LAND[n], "tiene_mela", 0.28), (ET[n], "mangia_mela", 0.25)]
    t = ET[n] + 0.55; i = 0
    while t < T_DANCE - 0.3:
        ev.append((t, "mangia_mela2" if i % 2 == 0 else "mangia_mela", 0.2)); t += 0.4; i += 1
    return ev


EV = {
    "mouse": [(0.0, "neutro", 0.01)] + walk("mouse", 0.0, T_ARR) + [
        (T_ARR, "sorpreso", 0.2), (T_PICK, "china", 0.3), (T_HOLD, "tiene", 0.3), (V["n3"] + 0.5, "neutro", 0.3)]
        + walk("mouse", V["n3"] + 0.9, T_PLANT) + [
        (T_PLANT, "china", 0.3), (T_SEED_IN + 0.6, "neutro", 0.3), (V["n4"] + 0.3, "sorpreso", 0.2), (RAIN0 - 0.2, "riceve", 0.3),
        (V["t2"] - 0.15, "salto", 0.2), (V["t2"] + 0.55, "ride", 0.25), (T_SPR - 0.1, "sorpreso", 0.15), (T_SPR + 0.8, "ride", 0.25),
        (V["n6"] + 0.3, "indica_m", 0.3), (V["t3"] - 0.05, "saluta2", 0.25), (E("t3") + 0.1, "neutro", 0.3),
        (G0 - 0.1, "guarda_su", 0.3), (V["s2"], "ride", 0.25), (FALL0, "guarda_su_m", 0.25), (FALL0 + 0.9, "salto", 0.2),
        (V["t4"] - 0.1, "afferra", 0.2)] + eat("mouse") + dance(T_DANCE, V["end"] - 0.15, "balla") + [(V["end"] - 0.1, "saluta2", 0.25)],
    "chip": [(0.0, "neutro", 0.01)] + run("chip", T_CHIP, T_CHIP_END - 0.3) + [
        (G0, "guarda_su_m", 0.3), (V["c2"] - 0.05, "sorpreso", 0.15), (V["s2"] + 0.3, "ride", 0.25), (FALL0 + 0.2, "afferra", 0.2),
        (FALL0 + 1.0, "salto", 0.2), (V["t4"] - 0.1, "afferra", 0.2)]
        + eat("chip") + dance(T_DANCE, V["end"] - 0.15, "balla_m") + [(V["end"] - 0.1, "saluta2", 0.25)],
    "spike": [(0.0, "neutro", 0.01)] + run("spike", T_SPIKE, T_SPIKE_END - 0.3) + [
        (G0, "guarda_su", 0.3), (V["c2"] + 0.1, "sorpreso", 0.15), (V["s2"] + 0.2, "ride", 0.25), (FALL0 + 0.1, "afferra", 0.2),
        (FALL0 + 0.9, "salto", 0.2), (V["t4"] - 0.05, "afferra", 0.2)]
        + eat("spike") + dance(T_DANCE, V["end"] - 0.15, "balla") + [(V["end"] - 0.1, "saluta2", 0.25)],
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
EAT = ET
APPEAR = {"mouse": 0.0, "chip": T_CHIP, "spike": T_SPIKE}
HAS_MOUTH = {}
for _n, _f in (("mouse", "topo"), ("chip", "chip"), ("spike", "spike")):
    HAS_MOUTH[_n] = all(os.path.exists(os.path.join(HERE, "assets", "pose", f"{_f}_{m}.png")) for m in ("parla_a", "parla_o"))
HAND = {"mouse": (0, 0.49), "chip": (0, 0.47), "spike": (0, 0.50)}     # dove atterra la mela (mani a 'riceve'/'tiene')
MOUTH = {"mouse": (4, 0.62), "chip": (4, 0.62), "spike": (4, 0.62)}
SEEDH = (0, 0.42)                                                      # seme tra le mani del topolino in posa 'tiene'

KF = {   # posizioni (t, x, y)
    "mouse": [(0, 380, 1240), (T_ARR, 480, 1530), (V["n3"] + 0.9, 480, 1530), (T_PLANT, 560, 1640), (999, 560, 1640)],
    "chip": [(0, 300, 1250), (T_CHIP, 300, 1250), (T_CHIP_END, 300, 1670), (999, 300, 1670)],
    "spike": [(0, 850, 1250), (T_SPIKE, 850, 1250), (T_SPIKE_END, 880, 1690), (999, 880, 1690)],
}
CHARS = ["spike", "chip", "mouse"]
H_CH = {"mouse": 640, "chip": 600, "spike": 560}


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


def pose_state(name, t):
    ev = EV[name]; idx = 0
    for i, e in enumerate(ev):
        if e[0] <= t: idx = i
    t0, pose, dur = ev[idx]
    prev = ev[idx - 1][1] if idx > 0 else pose
    if prev != pose and t < t0 + dur: return prev, pose, (t - t0) / dur
    return pose, pose, 1.0


def precompute():
    pairs = set()
    for name, ev in EV.items():
        for a, b in zip(ev, ev[1:]):
            if a[1] != b[1]: pairs.add((name, a[1], b[1]))
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


def _m(e): return "parla_a" if e > 0.52 else ("parla_o" if e > 0.17 else "neutro")


def mouth_pose(name, t):
    cur = _m(talk(name, t)); prev = _m(talk(name, t - 1.0 / FPS))
    return prev if (prev == "parla_a" and cur == "parla_o") else cur


def char_canvas(name, t):
    A, B, u = pose_state(name, t)
    if A == B == "neutro" and HAS_MOUTH.get(name, False):
        A = B = mouth_pose(name, t)
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


def sized(name, w=None, h=None, flipx=False):
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
    """alone morbido (gradiente a cerchi concentrici, dal più grande al più piccolo) nel livello di luce"""
    for k in range(n):
        f = (k + 1) / n; rr = r * (1 - k / n); lv = a * f ** 2.2
        c.gd.ellipse([c.X(x) - rr * c.Z, c.Y(y) - rr * c.Z, c.X(x) + rr * c.Z, c.Y(y) + rr * c.Z], fill=tuple(int(v * lv) for v in col))
    c.glow_used = True


RB = [(255, 70, 70), (255, 150, 50), (255, 225, 70), (100, 210, 100), (80, 160, 255), (110, 100, 230), (190, 110, 230)]
_RBC = np.array(RB, dtype=np.float32)
def rainbow(c, t0, cx, cy, R=620, band=36, alpha=0.5):
    """arcobaleno con bordi morbidi (calcolato per pixel, niente gradini)"""
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
    """sprite 3D che batte le ali: schiacciamento orizzontale (ali aperte -> quasi chiuse)"""
    im = load(name)
    w = max(16, min(int(size * c.Z), 900)); h = int(w * im.height / im.width)
    fl = 0.30 + 0.70 * abs(math.cos(phase))
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
CAM = [  # (t, cx, cy, z)
    (0.0, 575, 1560, 2.4), (1.0, 575, 1540, 2.3), (2.6, 560, 1450, 1.45), (V["n2"], 560, 1450, 1.35), (T_PICK, 560, 1520, 1.55),
    (V["t1"] + 0.3, 580, 1480, 1.6), (V["n3"] + 0.6, 600, 1400, 1.2), (TB + 0.6, 620, 1400, 1.2),
    (T_PLANT - 0.2, 640, 1500, 1.5), (T_SEED_IN + 0.3, 700, 1580, 1.8), (V["n4"] + 1.0, 700, 1250, 1.2), (CL0 + 0.6, 700, 1020, 1.22),
    (RAIN0 + 1.5, 680, 1040, 1.25), (T_SPR - 0.3, 740, 1500, 1.5), (T_SPR + 0.5, 750, 1560, 1.95), (V["n6"] + 0.1, 700, 1400, 1.25),
    (V["t3"] + 0.4, 640, 1300, 1.05), (G0 - 0.3, 700, 1450, 1.5), (G0 + 1.6, 720, 1150, 1.25), (G1, 650, 960, 1.0),
    (FALL0 + 0.5, 600, 1000, 1.0), (V["t4"] - 0.2, 600, 1400, 1.2), (TC + 0.2, 540, 1400, 1.15),
    (V["n9"] + 1.0, 470, 1330, 1.15), (ET["chip"] + 0.8, 480, 1400, 1.2), (V["n10"], 520, 1300, 1.05),
    (V["end"] - 0.2, 560, 1420, 1.0), (DUR, 560, 1400, 0.98),
]
SHAKES = [(G0 + 0.4, 14), (G0 + 1.5, 14), (G0 + 2.6, 18), (G1, 22), (T_SEED_IN, 5), (T_SPR, 6)]
def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 7 * math.sin(t * 0.8); cy += 5 * math.sin(t * 1.1 + 1)
    for kt, amp in SHAKES:
        if kt <= t < kt + 0.3:
            k = (1 - (t - kt) / 0.3) * amp; cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    z = max(1.0, z); hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


# ------------------------------------------------------------------ personaggio
def cstate(name, t):
    x, y, mv = kf_pos(name, t)
    kind, ph, per = gait_info(name, t)
    hop = 0.0; rot = 0.0; sq = 1.0
    if kind == "walk":
        hop = (1 - abs(math.cos(2 * math.pi * ph))) * 20; rot = math.sin(2 * math.pi * ph) * 2.6; sq = 1 + 0.018 * math.cos(4 * math.pi * ph)
    elif kind == "run":
        hop = abs(math.sin(2 * math.pi * ph)) * 46; rot = math.sin(2 * math.pi * ph) * 3.5 - 3; sq = 1 + 0.03 * math.cos(4 * math.pi * ph)
    A, B, u = pose_state(name, t)
    for pose, t0 in ((e[1], e[0]) for e in EV[name]):
        if pose in ("salto", "afferra") and t0 - 0.05 <= t < t0 + 0.75:
            p = clamp((t - (t0 - 0.05)) / 0.8); hop += 4 * p * (1 - p) * (110 if pose == "salto" else 60)
            if t < t0 + 0.1: sq *= 1 - 0.07 * clamp((t - (t0 - 0.05)) / 0.15)
            elif p > 0.85: sq *= 1 - 0.06 * math.sin(math.pi * (p - 0.85) / 0.15)
    for pose, t0 in ((e[1], e[0]) for e in EV[name]):
        if pose == "neutro" and t0 > 1.0: sq *= 1 + osc(t, t0 + 0.05, 0.05, 8, 24)
    if EAT[name] + 0.5 <= t < T_DANCE: sq *= 1 + 0.028 * math.sin((t - EAT[name]) * 24); rot += math.sin((t - EAT[name]) * 12) * 1.2
    tk = talk(name, t); sq *= 1 + 0.022 * tk; rot += math.sin(t * 11 + len(name)) * 1.3 * tk
    if A == B and A in ("tiene", "neutro", "saluta", "saluta2", "guarda_su", "guarda_su_m", "indica", "indica_m", "sbircia", "riceve"):
        sq *= 1 + 0.01 * math.sin(t * 3.2 + len(name) * 2)
    if A in ("balla", "balla_m") or B in ("balla", "balla_m"):
        ph2 = ((t - T_DANCE) / 0.46) % 1; hop += abs(math.sin(math.pi * ph2)) * 30; rot += math.sin(math.pi * 2 * ph2) * 3.5
    if A == "saluta2" and t > V["end"]: rot += math.sin(t * 6 + len(name)) * 2
    return x, y, persp(y), hop, rot, sq


_shd = None
def shadow(img, x, y, w, k=1.0):
    global _shd
    if _shd is None:
        sh = Image.new("RGBA", (300, 90), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([25, 25, 275, 65], fill=(30, 40, 10, 130)); _shd = sh.filter(ImageFilter.GaussianBlur(9))
    s2 = _shd.resize((max(2, int(w * 1.35)), max(2, int(w * 1.35 * 90 / 300))), Image.BICUBIC)
    if k < 1: s2.putalpha(s2.getchannel("A").point(lambda v: int(v * k)))
    img.paste(s2, (int(x - s2.width / 2), int(y - s2.height / 2)), s2)


def dust(c, t):
    ev = []
    for (name, t0, t1, per, kind) in GAIT:
        q = per / 2; k = 0
        while t0 + k * q < t1:
            ev.append((name, t0 + k * q + 0.02, 1.0 if kind == "run" else 0.55)); k += 1
    for name, evl in EV.items():
        for (te, pose, dur) in evl:
            if pose in ("salto", "afferra"): ev.append((name, te + 0.72, 1.3))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay); used = False
    for (name, te, amp) in ev:
        u = (t - te) / 0.5
        if not 0 <= u < 1 or t < APPEAR[name]: continue
        used = True; x, y, _ = kf_pos(name, te); s = persp(y)
        for j in range(3):
            dx = (j - 1) * 46 * s * amp + math.sin(j * 2.1) * 10; r = (14 + 46 * u) * s * amp * c.Z; a = int(110 * (1 - u) * amp)
            px, py = c.X(x + dx + (j - 1) * 40 * u), c.Y(y - 6 * s - 24 * u * s)
            ld.ellipse([px - r, py - r * 0.7, px + r, py + r * 0.7], fill=(226, 214, 176, min(150, a)))
    if used:
        lay = lay.filter(ImageFilter.GaussianBlur(7)); c.img.paste(lay, (0, 0), lay)


def draw_char(img, c, name, t):
    x, y, s, hop, rot, sq = cstate(name, t)
    cv, pose = char_canvas(name, t)
    im = Image.fromarray(np.ascontiguousarray(cv), "RGBA")
    if rot: im = im.rotate(rot, resample=Image.BILINEAR, center=(MO.AX, MO.AY))
    f = s * c.Z
    nw, nh = max(2, int(MO.CW * f / math.sqrt(sq))), max(2, int(MO.CH * f * sq))
    r = im.resize((nw, nh), Image.LANCZOS if f < 1 else Image.BICUBIC)
    px, py = c.X(x) - MO.AX * nw / MO.CW, c.Y(y - hop * s) - MO.AY * nh / MO.CH
    shadow(img, c.X(x + 18 * s), c.Y(y), H_CH[name] * 0.5 * c.Z * s, max(0.45, 1 - hop / 130))
    img.paste(r, (int(px), int(py)), r)
    return pose


# ------------------------------------------------------------------ ambienti animati
_bg = {}
def bg_arr(sid):
    if sid not in _bg:
        _bg[sid] = Image.open(os.path.join(HERE, "assets", "amb", sid + ".png")).convert("RGB").resize((W, H), Image.BICUBIC)
    return _bg[sid]


_grid = None
def sway(arr, sid, t, cx, cy, Z):
    """vento: le chiome e i fiori ondeggiano, le nuvole scorrono (deformazione per righe, in coordinate del mondo)"""
    global _grid
    if _grid is None:
        _grid = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    xs, ys = _grid
    wy = (ys - H / 2) / Z + cy                      # y nel mondo di ogni riga
    wx = (xs - W / 2) / Z + cx
    if sid == "bosco":
        w = np.clip(1 - wy / 850.0, 0, 1) ** 1.3 * 7.0 + np.exp(-((wy - 1180) / 160.0) ** 2) * 3.0
    elif sid == "giardino":
        w = np.exp(-((wy - 520) / 230.0) ** 2) * 6.5 + np.exp(-((wy - 1250) / 230.0) ** 2) * 4.0
    else:
        w = np.exp(-((wy - 560) / 240.0) ** 2) * 3.5 + np.exp(-((wy - 1230) / 260.0) ** 2) * 3.5
    dx = w * np.sin(2 * math.pi * 0.28 * t + wy * 0.012 + wx * 0.006)
    if sid != "bosco":                               # nuvole che scorrono
        sk = np.clip(1 - wy / 330.0, 0, 1) ** 0.8 * 26.0
        dx = dx + sk * math.sin(0.35 * t) + sk * 0.0
    return cv2.remap(arr, xs + dx.astype(np.float32), ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def leaf(d, x, y, r, ang, col):
    c, s = math.cos(ang), math.sin(ang)
    pts = [(x + c * r * 1.0, y + s * r * 1.0), (x - s * r * 0.45, y + c * r * 0.45), (x - c * r, y - s * r), (x + s * r * 0.45, y - c * r * 0.45)]
    d.polygon(pts, fill=col)


def ambient(c, sid, t):
    """particelle e luci dell'ambiente (raggi, polvere, lucciole, foglie, uccellini, farfalle)"""
    X, Y, Z = c.X, c.Y, c.Z
    if sid == "bosco":
        for k in range(5):                           # raggi di luce che pulsano
            a0 = 0.55 + 0.5 * math.sin(t * 0.7 + k * 1.3); x0 = 380 + k * 110
            c.gd.polygon([(X(x0), Y(0)), (X(x0 + 110), Y(0)), (X(x0 + 520), Y(1500)), (X(x0 + 150), Y(1500))],
                         fill=(int(15 * a0), int(13 * a0), int(5 * a0))); c.glow_used = True
    if sid == "giardino":                            # bagliore del sole
        g = 0.75 + 0.25 * math.sin(t * 1.3); glow_blob(c, 80, 120, 560, (70, 60, 28), g)
    if sid == "tramonto":
        g = 0.8 + 0.2 * math.sin(t * 0.9); glow_blob(c, 850, 560, 700, (90, 50, 18), g)
    # lucciole / pulviscolo luminoso
    n = 26 if sid != "giardino" else 14
    rng = np.random.default_rng({"bosco": 5, "giardino": 8, "tramonto": 11}[sid])
    for k in range(n):
        bx, by, sp, ph = rng.uniform(40, 1040), rng.uniform(500, 1750), rng.uniform(0.3, 1.0), rng.uniform(0, 6.28)
        px = bx + math.sin(t * 0.6 * sp + ph) * 60; py = by + math.sin(t * 0.8 * sp + ph * 1.7) * 40 - (t * 12 * sp) % 120
        a = 0.35 + 0.65 * max(0.0, math.sin(t * 2.1 * sp + ph))
        r = (3 + 3 * sp) * Z; col = (255, 235, 130) if sid != "giardino" else (255, 250, 210)
        c.gd.ellipse([X(px) - r * 2.4, Y(py) - r * 2.4, X(px) + r * 2.4, Y(py) + r * 2.4], fill=tuple(int(v * a * 0.22) for v in col))
        c.gd.ellipse([X(px) - r, Y(py) - r, X(px) + r, Y(py) + r], fill=tuple(int(v * a) for v in col)); c.glow_used = True
    # foglie che cadono (bosco e giardino)
    if sid in ("bosco", "giardino"):
        rng = np.random.default_rng(21)
        for k in range(12):
            bx, sp, ph = rng.uniform(0, 1080), rng.uniform(0.6, 1.2), rng.uniform(0, 6.28)
            u = ((t * 0.07 * sp + ph / 6.28) % 1.0); px = bx + math.sin(t * 0.9 * sp + ph) * 70; py = -60 + u * 1700
            leaf(c.d, X(px), Y(py), 15 * Z, t * 1.4 * sp + ph, (96, 168, 60, 235) if k % 3 else (214, 170, 60, 235))
    # uccellini che attraversano il cielo
    if sid in ("giardino", "tramonto"):
        t0 = TB + 0.6 if sid == "giardino" else TC + 0.8
        for k, (dt, yy, d_, sz) in enumerate(((0.0, 330, 1, 150), (1.4, 220, 1, 110), (3.2, 420, -1, 130))):
            u = (t - (t0 + dt)) / 5.5
            if 0 <= u <= 1:
                px = lerp(-150, 1230, u) if d_ > 0 else lerp(1230, -150, u); py = yy + 40 * math.sin(u * 9 + k)
                flap(c, "bird", X(px), Y(py), sz, -8 * math.sin(u * 9 + k), t * 17 + k, mirror=(d_ < 0))
    # farfalle (bosco e giardino)
    if sid in ("bosco", "giardino"):
        for k, (cx_, cy_, ph) in enumerate(((300, 1250, 0.0), (800, 1000, 2.0))):
            px = cx_ + 150 * math.sin(t * 0.5 + ph) + 40 * math.sin(t * 2.3 + ph); py = cy_ + 90 * math.sin(t * 0.7 + ph * 1.3) + 25 * math.sin(t * 3.1)
            flap(c, "bf_open", X(px), Y(py), 70, 12 * math.sin(t * 0.7 + ph), t * 22 + ph)


def tree_state(t):
    """scala dell'albero (0 = non c'è): tre scatti 'cresce, cresce, cresce' + rimbalzo finale"""
    if t < G0: return 0.0
    u = clamp((t - G0) / (G1 - G0))
    if u < 1.0:
        k = int(u * 3); f = u * 3 - k
        return 0.1 + 0.9 * ((k + back(f, 1.2)) / 3.0)
    return 1.0 + 0.035 * math.exp(-5 * (t - G1)) * math.sin(22 * (t - G1))


def apple_sim(i, t, x0, y0, xg, yg, tf):
    """caduta con rimbalzi: ritorna (x, y, squash)"""
    if t < tf: return None
    vy = 0.0; y = y0; x = x0; tt = tf; dt = 1.0 / 240; vx = (xg - x0) / 1.2 * 0.9
    while tt < t:
        vy += 2600 * dt; y += vy * dt; x += vx * dt; tt += dt
        if y >= yg:
            y = yg; vy = -vy * 0.42
            vx *= 0.7
            if abs(vy) < 90: vy = 0.0; vx *= 0.5
    sq = 1.0
    return x, y, vy


APPLES = [(0.0, -160, 110), (0.25, 40, 150), (0.5, -60, 100), (0.75, 190, 130), (1.0, 110, 120), (1.25, -230, 140)]   # (ritardo, dx dal tronco, dy dalla chioma)


def props(c, sid, t, hero):
    """oggetti della storia: seme, terra, germoglio, albero, nuvola+pioggia, mele"""
    X, Y, Z = c.X, c.Y, c.Z
    px, py = P
    if sid == "bosco" or sid == "giardino":
        pass
    if sid == "bosco":
        if t < T_PICK + 0.45:                         # il seme che brilla a terra
            bob = 8 * math.sin(t * 3); gx, gy = SEED0[0], SEED0[1] - 40 + bob
            g = 0.7 + 0.3 * math.sin(t * 8); glow_blob(c, gx, gy, 140 * g, (150, 110, 30))
            s = sized("seed", h=70 * Z * (1 + 0.06 * math.sin(t * 6))); c.img.paste(s, (int(X(gx) - s.width / 2), int(Y(gy) - s.height / 2)), s)
            sparkles(c, gx, gy, 0.0, TB, n=10, spread=90, rise=60, size=14, seed=2)
    if sid == "giardino" or sid == "tramonto":
        # terra + germoglio
        if sid == "giardino" and T_SEED_IN + 0.15 <= t and t < G0 + 0.6:
            sp = load("sprout"); sy = int(sp.height * 0.64)
            mound = sp.crop((0, sy, sp.width, sp.height)); stem = sp.crop((0, 0, sp.width, sy))
            k = 300.0 / sp.height * Z
            mw, mh = max(2, int(mound.width * k)), max(2, int(mound.height * k))
            c.img.paste(mound.resize((mw, mh), Image.LANCZOS), (int(X(px) - mw / 2), int(Y(py) - mh * 0.85)), mound.resize((mw, mh), Image.LANCZOS))
            if t >= T_SPR:
                u = back((t - T_SPR) / 0.7, 2.2) * (1 - clamp((t - (G0 + 0.2)) / 0.4))
                if u > 0.02:
                    st = stem.resize((max(2, int(stem.width * k * u)), max(2, int(stem.height * k * u))), Image.LANCZOS)
                    c.img.paste(st, (int(X(px) - st.width / 2), int(Y(py) - mh * 0.85 - st.height + 8 * Z)), st)
                    sparkles(c, px, py - 150, T_SPR, 1.4, n=14, spread=110, rise=90, size=15, seed=7)
        # albero
        ts = tree_state(t)
        if ts > 0:
            tw = TREE_H * load("tree").width / load("tree").height
            shadow(c.img, X(px + 20), Y(py + 6), tw * 0.5 * ts * Z, 0.9)
            tr = sized("tree", h=TREE_H * ts * Z)
            if sid == "tramonto":
                tr = Image.fromarray(np.dstack([np.clip(np.asarray(tr)[..., :3].astype(np.float32) * np.array([1.0, 0.9, 0.8]), 0, 255).astype(np.uint8), np.asarray(tr)[..., 3]]), "RGBA")
            c.img.paste(tr, (int(X(px) - tr.width / 2), int(Y(py) - tr.height + 12 * Z)), tr)
            if G0 <= t < G1 + 0.6:
                sparkles(c, px, py - TREE_H * 0.55 * ts, G0, G1 - G0 + 0.6, n=26, spread=300, rise=40, size=20, seed=4)
        # nuvoletta e pioggia
        if sid == "giardino" and CL0 <= t < CL1 + 1.6:
            if t < CL0 + 1.6: u = ease((t - CL0) / 1.6); cxp = lerp(1350, 700, u); cyp = 650 + 30 * math.sin(t * 2)
            elif t < CL1: cxp = 700 + 18 * math.sin(t * 1.7); cyp = 650 + 14 * math.sin(t * 2.3)
            else: u = ease((t - CL1) / 1.5); cxp = lerp(700, 1400, u); cyp = 650 - 120 * u
            raining = RAIN0 <= t < RAIN1
            sqz = 1 + (0.05 * math.sin(t * 14) if raining else 0.02 * math.sin(t * 3))
            cl = sized("cloud", w=380 * Z * sqz, h=265 * Z / sqz)
            c.img.paste(cl, (int(X(cxp) - cl.width / 2), int(Y(cyp) - cl.height / 2)), cl)
            if raining:
                f = min(1, (t - RAIN0) / 0.4) * min(1, (RAIN1 - t) / 0.4)
                lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
                rr_ = np.random.default_rng(3); XR, PH, SP, LN = rr_.random(260), rr_.random(260), rr_.uniform(1.1, 1.9, 260), rr_.uniform(26, 52, 260)
                for k in range(260):
                    u = ((t - RAIN0) * SP[k] + PH[k]) % 1.0
                    x = cxp - 170 + XR[k] * 340 + u * 30; y0 = cyp + 120; yend = py + (k % 9) * 14 - 8
                    y = y0 + u * (yend - y0)
                    ld.line([(X(x), Y(y)), (X(x - 4), Y(y - LN[k]))], fill=(215, 235, 255, int(235 * f)), width=max(3, int(5 * Z)))
                    if u > 0.94:
                        ld.ellipse([X(x) - 14 * Z, Y(y) - 4 * Z, X(x) + 14 * Z, Y(y) + 4 * Z], outline=(210, 235, 255, int(170 * f)), width=2)
                c.img.paste(lay, (0, 0), lay)
        # mele
        ap = sized("apple", h=74 * Z)
        if sid == "giardino":
            for i, (dl, dx, dy) in enumerate(APPLES):
                tf = FALL0 + dl
                if t < tf: continue
                x0 = P[0] + dx; y0 = P[1] - TREE_H * 0.78 + dy
                xg = (180, 380, 640, 960, 1010, 120)[i]; yg = (1690, 1720, 1700, 1740, 1660, 1650)[i]
                r = apple_sim(i, t, x0, y0, xg, yg, tf)
                if r:
                    x, y, vy = r; s2 = 1.0
                    a2 = ap.rotate(math.degrees(0.002 * (x - x0)) * 3 % 360, resample=Image.BICUBIC, expand=True) if abs(vy) > 1 else ap
                    c.img.paste(a2, (int(X(x) - a2.width / 2), int(Y(y) - a2.height)), a2)
            for n_, tl in LAND.items():                      # mele-eroi: dalla chioma alle mani
                t0 = tl - 0.95
                if t0 <= t < tl + 0.2:
                    x, y, s, hop, rot, sq = cstate(n_, t)
                    hx, hy = x + HAND[n_][0] * s, y - hop * s - H_CH[n_] * HAND[n_][1] * s
                    uu = clamp((t - t0) / 0.95); k = ("mouse", "chip", "spike").index(n_)
                    sx, sy = P[0] + (-120, 0, 120)[k], P[1] - TREE_H * 0.7
                    qx, qy = lerp(sx, hx, ease(uu)), lerp(sy, hy, uu ** 2.2) - 80 * math.sin(math.pi * uu)
                    a2 = ap.rotate(uu * 300, resample=Image.BICUBIC, expand=True)
                    if t > tl: a2.putalpha(a2.getchannel("A").point(lambda v, f=1 - clamp((t - tl) / 0.2): int(v * f)))
                    c.img.paste(a2, (int(X(qx) - a2.width / 2), int(Y(qy) - a2.height / 2)), a2)


def seed_follow(c, t):
    """il seme tra le mani del topolino (dalla raccolta al momento in cui lo pianta)"""
    if not (T_PICK + 0.35 <= t < T_SEED_IN): return
    x, y, s, hop, rot, sq = cstate("mouse", t)
    hx, hy = x + SEEDH[0] * s, y - hop * s - H_CH["mouse"] * SEEDH[1] * s
    if t < T_HOLD: hx, hy = lerp(SEED0[0], hx, ease((t - (T_PICK + 0.35)) / 0.45)), lerp(SEED0[1] - 40, hy, ease((t - (T_PICK + 0.35)) / 0.45))
    if t >= T_PLANT + 0.1:                              # tuffo nella terra
        u = clamp((t - (T_PLANT + 0.1)) / (T_SEED_IN - T_PLANT - 0.1)); hx, hy = lerp(hx, P[0], ease(u)), lerp(hy, P[1] - 30, u ** 1.5) - 110 * math.sin(math.pi * u)
    g = 0.75 + 0.25 * math.sin(t * 9); glow_blob(c, hx, hy, 120 * g, (150, 110, 30))
    s2 = sized("seed", h=62 * c.Z); c.img.paste(s2, (int(c.X(hx) - s2.width / 2), int(c.Y(hy) - s2.height / 2)), s2)


# ------------------------------------------------------------------ fotogramma
def scene_at(t):
    cur = SCENES[0][0]
    for sid, t0 in SCENES:
        if t >= t0: cur = sid
    return cur


def scene_img(sid, t, cx, cy, Z):
    base = bg_arr(sid).resize((W, H), Image.BICUBIC, box=(cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z))
    arr = sway(np.asarray(base), sid, t, cx, cy, Z)
    img = Image.fromarray(arr).filter(ImageFilter.GaussianBlur(0.4 + 0.8 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    if sid == "giardino" and RAIN1 + 0.2 <= t < TC + 1: rainbow(c, RAIN1 + 0.2, P[0] - 60, 1500, R=640)
    ambient(c, sid, t)
    props(c, sid, t, None)
    vis = [n for n in CHARS if t >= APPEAR[n]]
    for n in sorted(vis, key=lambda n: kf_pos(n, t)[1]): draw_char(img, c, n, t)
    seed_follow(c, t) if sid in ("bosco", "giardino") else None
    dust(c, t)
    if t >= V["n10"] and sid == "tramonto":                         # cuori e coriandoli
        for k in range(10):
            uu = ((t - V["n10"]) * 0.5 + k / 10) % 1.0; hpx = c.X(250 + k * 62 + math.sin(uu * 8 + k) * 40); hpy = c.Y(1300 - uu * 560)
            heart(c.d, hpx, hpy, 30 * Z * (0.6 + 0.4 * math.sin(math.pi * uu)), (255, 110, 150, int(235 * math.sin(math.pi * uu))))
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); img = ImageChops.add(ImageChops.add(img, c.glow), g2)
    # colore dell'ambiente
    if sid == "giardino" and RAIN0 - 0.3 <= t < RAIN1 + 0.6:        # cielo di pioggia
        f = clamp((t - (RAIN0 - 0.3)) / 0.7) * clamp((RAIN1 + 0.6 - t) / 0.8)
        img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (176, 190, 214))), 0.55 * f)
    if sid == "tramonto": img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 214, 176))), 0.25)
    return img


def frame(i):
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
    img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 246, 232))), 0.4)
    d = ImageDraw.Draw(img, "RGBA")
    if t < 2.4:                                                      # HOOK
        u = back(t / 0.35); a = int(255 * clamp((2.4 - t) / 0.4))
        text(d, "COSA C'È", W / 2, 300 - 10 * math.sin(t * 6), int(170 * max(0.1, u)), (255, 240, 120, a), (190, 40, 70, a), 12)
        text(d, "NEL BOSCO?", W / 2, 470, int(120 * max(0.1, back((t - 0.4) / 0.35))), (255, 255, 255, a), (60, 40, 120, a), 10)
    for k, t0, who, txt, dur in VOICES:                              # sottotitoli
        if t0 - 0.05 <= t <= t0 + dur + 0.3:
            u = ease((t - t0 + 0.05) / 0.18); f = ImageFont.truetype(FONT, 66 if who == "narr" else 78); lines = []; cur = ""
            for wd in txt.split():
                tl_ = (cur + " " + wd).strip(); bb = d.textbbox((0, 0), tl_, font=f, anchor="mm", stroke_width=6)
                if bb[2] - bb[0] > 930 and cur: lines.append(cur); cur = wd
                else: cur = tl_
            lines.append(cur); yy = (1660 if t < 2.4 else 250) - 41 * (len(lines) - 1) + (1 - u) * 14
            for ln in lines: text(d, ln, W / 2, yy, 66 if who == "narr" else 78, COL[who] + (int(255 * u),), (60, 40, 20, int(255 * u)), 7); yy += 84
            break
    subscribe_button(img, t, V["end"] + 0.9, cy=1810)
    return img.tobytes()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2)); print({k: round(v, 2) for k, v in V.items()})
        print({"TB": TB, "TC": TC, "G0": G0, "G1": G1, "FALL0": FALL0, "LAND": LAND, "ET": ET})
    elif cmd == "prep":
        import time
        t0 = time.time(); ps = precompute(); print(len(ps), "transizioni")
        for n, (nm, a, b) in enumerate(ps):
            try: MO.transition(nm, a, b)
            except Exception as e: print("manca", nm, a, b, str(e)[:60])
        print("fatto in", round(time.time() - t0), "s")
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts) * FPS))).save(f"test_s_{ts}.png")
    else:
        out = sys.argv[2]; N = int(DUR * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
