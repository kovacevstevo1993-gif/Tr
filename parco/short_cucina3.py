#!/usr/bin/env python3
"""Short v2 'Il barattolo misterioso' (9:16, 1080x1920, 24 fps) - versione movimentata.
Pose con transizioni fluide (morph.py), camera cinematografica, corsa verso la camera, conto 1-2-3,
farfalla magica da inseguire, condivisione dei biscotti, ballo e finale 'Bambini Ciao Ciao'.
    python3 short_cucina2.py info
    python3 short_cucina2.py test 1.0 5.5 12            # fotogrammi di controllo
    python3 short_cucina2.py render muto2.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import morph as MO

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 24
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
AUD = "audioE"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))


def lerp(a, b, u): return a + (b - a) * u
def clamp(u, a=0.0, b=1.0): return max(a, min(b, u))
def ease(u): u = clamp(u); return u * u * (3 - 2 * u)
def back(u, k=1.7): u = clamp(u); return 1 + (k + 1) * (u - 1) ** 3 + k * (u - 1) ** 2
def osc(t, t0, amp=1.0, decay=7.0, freq=26.0):
    """oscillazione smorzata (rimbalzo) che parte a t0"""
    return amp * math.exp(-decay * (t - t0)) * math.sin(freq * (t - t0)) if t >= t0 else 0.0


# ------------------------------------------------------------------ copione: tempi dalle voci
V = {}
def _seq():
    t = 0.0
    def at(k, gap):
        nonlocal t
        V[k] = t + gap; t = V[k] + D[k]
    at("n1", 0.3); at("t1", 0.1); at("n2", 0.2); at("t2", 0.2); at("c1", 0.05); at("s1", 0.1)
    at("n3", 0.5); at("t3", 0.25); at("c3", 0.1); at("s3", 0.1)
    global TP; TP = t + 0.05
    at("o1", 0.3); at("o2", -0.12); at("n4", 0.25); at("c2", 0.25); at("s2", 0.1)
    at("n5", 0.35); at("t4", 0.2); at("n6", 0.5); at("c4", 0.7); at("s4", 0.1)
    at("n7", 0.45); at("end", 0.45)
    return t + 2.2
DUR = _seq()
E = lambda k: V[k] + D[k]
SAY = {"n1": "narr", "t1": "mouse", "n2": "narr", "t2": "mouse", "c1": "chip", "s1": "spike", "n3": "narr", "t3": "mouse",
       "c3": "chip", "s3": "spike", "o1": "mouse", "o2": "chip", "n4": "narr", "c2": "chip", "s2": "spike", "n5": "narr",
       "t4": "mouse", "n6": "narr", "c4": "chip", "s4": "spike", "n7": "narr", "end": "mouse"}
TXT = {"n1": "Zitti, zitti... sentite? Qualcosa bussa nel barattolo dei biscotti!", "t1": "Toc toc? Chi c'è?",
       "n2": "Il topolino chiama i suoi amici.", "t2": "Chip! Spike! Venite!", "c1": "Arrivo!", "s1": "Aspettami!",
       "n3": "Ora tutti insieme... contiamo fino a tre!", "t3": "Uno!", "c3": "Due!", "s3": "Tre!", "o1": "Oh!", "o2": "Oh!",
       "n4": "Ma guarda! È una farfalla magica!", "c2": "Che bella!", "s2": "Prendiamola!",
       "n5": "Ma la farfalla è troppo veloce... e vola via dalla finestra.", "t4": "Ciao ciao, farfalla!",
       "n6": "Però lascia una magia: un biscotto per ognuno!", "c4": "Che buono!", "s4": "Buonissimo!",
       "n7": "Condividere è sempre più bello.", "end": "Bambini Ciao Ciao! Iscrivetevi al canale!"}
COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 170), "spike": (200, 225, 255)}
VOICES = [(k, V[k], SAY[k], TXT[k], D[k]) for k in V]

# ------------------------------------------------------------------ luoghi
JAR = (905, 1640)                     # base del barattolo (mondo)
KNOCKS = [0.9, 1.8, 2.5, 4.4, 5.3, V["t1"] + 0.9, V["n2"] + 0.9, V["t2"] + 1.3, V["c1"] + 0.2,
          V["n3"] + 1.0, V["n3"] + 2.2, V["t3"] - 0.1, V["c3"] - 0.1, V["s3"] - 0.1]
GAIT = []                             # (nome, t0, t1, periodo, tipo)


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


T_WALK = 3.5
T_CHIP, T_SPIKE = V["t2"] + 0.9, V["t2"] + 1.3
T_CHIP_END, T_SPIKE_END = E("s1") + 0.3, E("s1") + 0.55
# biscotto: istante in cui atterra nelle mani, e inizio del morso (per personaggio)
LAND = {"spike": V["n6"] + 2.15, "chip": V["n6"] + 2.5, "mouse": V["n6"] + 2.85}
ET = {"chip": V["c4"] - 0.45, "spike": V["s4"] - 0.4, "mouse": V["s4"] + 0.15}
T_DANCE = V["n7"] - 0.1


def eat(n):
    """riceve (mani aperte) -> biscotto in mano -> morso -> masticare (mangia/mangia2 alternati)"""
    ev = [(LAND[n] - 0.6, "riceve", 0.3), (LAND[n], "tiene_biscotto", 0.28), (ET[n], "mangia", 0.25)]
    t = ET[n] + 0.55; i = 0
    while t < T_DANCE - 0.3:
        ev.append((t, "mangia2" if i % 2 == 0 else "mangia", 0.2)); t += 0.4; i += 1
    return ev


EV = {
    "mouse": [(0.0, "neutro", 0.01)] + walk("mouse", 0.0, T_WALK) + [
        (T_WALK, "sbircia", 0.35), (4.4, "sorpreso", 0.16), (4.9, "sbircia", 0.3), (V["t1"] - 0.2, "orecchio_m", 0.3),
        (E("t1") + 0.2, "neutro", 0.3), (V["n2"] + 0.25, "indica_m", 0.3), (V["t2"] - 0.05, "saluta2", 0.25),
        (E("t2") + 0.1, "neutro", 0.3), (V["n3"] - 0.2, "tiene", 0.3), (V["t3"] - 0.18, "salto", 0.2), (V["t3"] + 0.42, "tiene", 0.25),
        (TP - 0.04, "sorpreso", 0.12), (V["o1"], "guarda_su", 0.25), (V["s2"] - 0.2, "indica", 0.25), (V["n5"] + 0.4, "guarda_su_m", 0.3),
        (TP + 8.2, "triste", 0.35), (V["t4"] - 0.1, "saluta2", 0.25), (E("t4") + 0.3, "neutro", 0.3)]
        + eat("mouse") + dance(T_DANCE, V["end"] - 0.15, "balla") + [(V["end"] - 0.1, "saluta2", 0.25)],
    "chip": [(0.0, "neutro", 0.01)] + run("chip", T_CHIP, T_CHIP_END - 0.3) + [
        (V["n3"] - 0.1, "tiene", 0.3), (V["c3"] - 0.18, "salto", 0.2), (V["c3"] + 0.42, "tiene", 0.25),
        (TP - 0.04, "sorpreso", 0.12), (V["o2"], "guarda_su_m", 0.25), (V["c2"] + 0.2, "indica_m", 0.25), (V["s2"] + 0.05, "afferra", 0.18),
        (V["s2"] + 0.9, "salto", 0.2), (V["s2"] + 1.4, "guarda_su", 0.3), (V["t4"] - 0.05, "saluta2", 0.25), (E("t4") + 0.2, "neutro", 0.3)]
        + eat("chip") + dance(T_DANCE, V["end"] - 0.15, "balla_m") + [(V["end"] - 0.1, "saluta2", 0.25)],
    "spike": [(0.0, "neutro", 0.01)] + run("spike", T_SPIKE, T_SPIKE_END - 0.3) + [
        (V["n3"] - 0.1, "tiene", 0.3), (V["s3"] - 0.18, "salto", 0.2), (V["s3"] + 0.42, "tiene", 0.25),
        (TP - 0.04, "sorpreso", 0.12), (V["o2"] + 0.2, "guarda_su", 0.25), (V["s2"], "afferra", 0.18), (V["s2"] + 0.8, "salto", 0.2),
        (V["s2"] + 1.3, "guarda_su_m", 0.3), (V["t4"] - 0.05, "saluta2", 0.25), (E("t4") + 0.3, "neutro", 0.3)]
        + eat("spike") + dance(T_DANCE, V["end"] - 0.15, "balla") + [(V["end"] - 0.1, "saluta2", 0.25)],
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
EAT = ET
APPEAR = {"mouse": 0.0, "chip": T_CHIP, "spike": T_SPIKE}
HAS_MOUTH = {}                       # personaggi con pose parla_a/parla_o (si riempie a caricamento)
for _n, _f in (("mouse", "topo"), ("chip", "chip"), ("spike", "spike")):
    HAS_MOUTH[_n] = all(os.path.exists(os.path.join(HERE, "assets", "pose", f"{_f}_{m}.png")) for m in ("parla_a", "parla_o"))
# posizione delle mani con il biscotto in posa 'riceve': (scostamento x in px/scala, altezza come frazione del personaggio)
HAND = {"mouse": (0, 0.49), "chip": (0, 0.47), "spike": (0, 0.50)}
MOUTH = {"mouse": (4, 0.62), "chip": (4, 0.62), "spike": (4, 0.62)}

KF = {   # posizioni (t, x, y)
    "mouse": [(0, 540, 1342), (T_WALK, 690, 1640), (999, 690, 1640)],
    "chip": [(0, 610, 1345), (T_CHIP, 610, 1345), (T_CHIP_END, 460, 1662), (V["s2"] - 0.1, 460, 1662), (V["s2"] + 0.35, 330, 1700),
             (V["s2"] + 1.0, 560, 1650), (V["s2"] + 1.5, 460, 1662), (999, 460, 1662)],
    "spike": [(0, 330, 1345), (T_SPIKE, 330, 1345), (T_SPIKE_END, 235, 1670), (V["s2"] - 0.1, 235, 1670), (V["s2"] + 0.45, 420, 1730),
              (V["s2"] + 1.1, 300, 1680), (V["s2"] + 1.5, 235, 1670), (999, 235, 1670)],
}
CHARS = ["spike", "chip", "mouse"]
H_CH = {"mouse": 640, "chip": 600, "spike": 560}


def persp(y): return clamp(0.58 + (y - 1340) / 310 * 0.42, 0.5, 1.3)


def kf_pos(name, t):
    kf = KF[name]
    if t <= kf[0][0]: return kf[0][1], kf[0][2], False
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        if t0 <= t <= t1:
            mv = (x0, y0) != (x1, y1); u = ease((t - t0) / (t1 - t0)) if mv else 0
            if mv and name == "mouse" and t < T_WALK: u = (t - t0) / (t1 - t0)       # camminata a velocità costante
            return lerp(x0, x1, u), lerp(y0, y1, u), mv
    return kf[-1][1], kf[-1][2], False


def pose_state(name, t):
    """(posa A, posa B, u) : in transizione A->B oppure ferma (A==B)"""
    ev = EV[name]; idx = 0
    for i, e in enumerate(ev):
        if e[0] <= t: idx = i
    t0, pose, dur = ev[idx]
    prev = ev[idx - 1][1] if idx > 0 else pose
    if prev != pose and t < t0 + dur: return prev, pose, (t - t0) / dur
    return pose, pose, 1.0


def gait_info(name, t):
    for (n, t0, t1, per, kind) in GAIT:
        if n == name and t0 <= t < t1: return kind, ((t - t0) / per) % 1.0, per
    return None, 0.0, 1.0


def precompute():
    pairs = set()
    for name, ev in EV.items():
        for a, b in zip(ev, ev[1:]):
            if a[1] != b[1]: pairs.add((name, a[1], b[1]))
    return sorted(pairs)


def _m(e): return "parla_a" if e > 0.52 else ("parla_o" if e > 0.17 else "neutro")


def mouth_pose(name, t):
    """bocca che segue l'ampiezza della voce; un fotogramma di isteresi (senza stato: si renderizza in parallelo)"""
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


# ------------------------------------------------------------------ oggetti disegnati
_obj = {}
def _load(name, h=None):
    if name not in _obj: _obj[name] = Image.open(os.path.join(HERE, "assets", "obj", name + ".png")).convert("RGBA")
    return _obj[name]


JAR_H = 380                           # altezza del barattolo nel mondo (px)
def jar_img(jh, lift=0.0, lid=True):
    """barattolo 3D (corpo + coperchio rosso, che si può sollevare). Ritorna (immagine, larghezza, altezza)"""
    body, cap = _load("jar_open"), _load("lid")
    k = jh / float(body.height + cap.height); w = max(2, int(body.width * k)); bh = max(2, int(body.height * k)); ch = max(2, int(cap.height * k))
    li = int(lift); cv = Image.new("RGBA", (w, bh + ch + li), (0, 0, 0, 0))
    cv.paste(body.resize((w, bh), Image.LANCZOS), (0, ch + li))
    if lid:
        cp = cap.resize((w, ch), Image.LANCZOS); cv.paste(cp, (0, 0), cp)
    return cv, w, cv.height


def lid_img(lh):
    cap = _load("lid"); return cap.resize((max(2, int(cap.width * lh / cap.height)), max(2, int(lh))), Image.LANCZOS)


def cookie_sprite():
    if "ck" not in _obj: _obj["ck"] = _load("cookie").resize((120, 120), Image.LANCZOS)
    return _obj["ck"]


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


RB = [(255, 70, 70), (255, 150, 50), (255, 225, 70), (100, 210, 100), (80, 160, 255), (110, 100, 230), (190, 110, 230)]
def rainbow(c, t0, cx=560, cy=1360, R=560, band=34, alpha=0.5):
    if c.t < t0: return
    p = ease((c.t - t0) / 1.6); a = min(1, (c.t - t0) / 0.6) * alpha
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i, col in enumerate(RB):
        r = (R - i * band) * c.Z; d.arc([c.X(cx) - r, c.Y(cy) - r, c.X(cx) + r, c.Y(cy) + r], 180, 180 + 180 * p, fill=col + (int(255 * a),), width=int(band * c.Z) + 1)
    lay = lay.filter(ImageFilter.GaussianBlur(1.8)); c.img.paste(lay, (0, 0), lay)


def butterfly_draw(c, x, y, size, ang, phase, cols=None):
    """farfalla magica 3D: il battito delle ali è uno 'schiacciamento' orizzontale (ali aperte -> quasi chiuse)"""
    im = _load("bf_open"); w = max(20, min(int(size * c.Z * 2.4), 800)); h = int(w * im.height / im.width)
    fl = 0.28 + 0.72 * abs(math.cos(phase))
    r = im.resize((max(4, int(w * fl)), h), Image.LANCZOS).rotate(ang, resample=Image.BICUBIC, expand=True)
    c.img.paste(r, (int(x - r.width / 2), int(y - r.height / 2)), r)


# percorso della farfalla (mondo): (tempo relativo a TP, x, y)
BF = [(0.0, 905, 1330), (1.0, 850, 1120), (2.2, 600, 930), (3.4, 270, 1060), (4.6, 480, 790), (5.8, 880, 870), (7.2, 800, 560), (8.6, 810, 330)]
def bf_pos(t):
    u = t - TP
    if u <= BF[0][0]: return BF[0][1], BF[0][2]
    for (t0, x0, y0), (t1, x1, y1) in zip(BF, BF[1:]):
        if t0 <= u <= t1:
            f = ease((u - t0) / (t1 - t0)) * 0.55 + 0.45 * (u - t0) / (t1 - t0)
            return lerp(x0, x1, f) + 40 * math.sin(u * 5.0), lerp(y0, y1, f) + 26 * math.sin(u * 7.0)
    return BF[-1][1], BF[-1][2]


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


def text(d, s, x, y, size, fill, out, ow, rot=0):
    d.text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)


def pop_text(c, s, wx, wy, t0, dur, size, fill, out, rot=0, ow=10, margin=330):
    """testo grande che 'salta fuori' (coordinate mondo) e svanisce"""
    t = c.t
    if not (t0 <= t < t0 + dur): return
    u = back((t - t0) / 0.28); a = int(255 * clamp((t0 + dur - t) / 0.25))
    f = ImageFont.truetype(FONT, max(10, int(size * c.Z * max(0.05, u)))); lay = Image.new("RGBA", (900, 500), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.text((450, 250), s, font=f, fill=fill + (a,), anchor="mm", stroke_width=max(2, int(ow * c.Z)), stroke_fill=out + (a,))
    lay = lay.rotate(rot + 5 * math.sin((t - t0) * 12), resample=Image.BICUBIC)
    sx = clamp(c.X(wx), margin, W - margin); sy = clamp(c.Y(wy), 300, H - 400)
    c.img.paste(lay, (int(sx - 450), int(sy - 250)), lay)


# ------------------------------------------------------------------ camera
def _ck(*a): return a
CAM = [  # (t, cx, cy, z)
    (0.0, 790, 1500, 1.5), (3.0, 730, 1500, 1.3), (4.35, 735, 1520, 1.28), (4.6, 740, 1520, 1.5), (V["t1"], 745, 1500, 1.4),
    (E("t1") + 0.3, 650, 1480, 1.2), (V["t2"] - 0.2, 560, 1420, 1.05), (V["t2"] + 0.8, 540, 1400, 1.0), (T_CHIP_END, 580, 1470, 1.12),
    (V["n3"], 620, 1470, 1.12), (TP - 0.5, 700, 1460, 1.28), (TP - 0.02, 740, 1450, 1.4),
    (TP + 0.45, 700, 1300, 1.35), (TP + 1.5, 640, 1180, 1.2), (TP + 3.2, 560, 1220, 1.05), (TP + 5.0, 640, 1100, 1.15),
    (TP + 7.0, 760, 800, 1.3), (TP + 8.4, 780, 760, 1.35), (TP + 9.6, 640, 1380, 1.12),
    (V["n6"] + 0.5, 600, 1440, 1.2), (V["c4"] - 0.3, 520, 1520, 1.45), (V["s4"] + 1.2, 540, 1500, 1.3), (V["n7"], 560, 1450, 1.1),
    (V["end"] - 0.2, 560, 1430, 1.0), (DUR, 560, 1400, 0.98),
]
def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 7 * math.sin(t * 0.8); cy += 5 * math.sin(t * 1.1 + 1)           # respiro della camera
    for kt in KNOCKS + [TP]:
        if kt <= t < kt + 0.28:
            k = (1 - (t - kt) / 0.28) * (16 if kt == TP else 3.5); cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    z = max(1.0, z); hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


# ------------------------------------------------------------------ audio -> parlato
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


# ------------------------------------------------------------------ personaggio
def cstate(name, t):
    x, y, mv = kf_pos(name, t)
    kind, ph, per = gait_info(name, t)
    hop = 0.0; rot = 0.0; sq = 1.0; lean = 0.0
    if kind == "walk":
        hop = (1 - abs(math.cos(2 * math.pi * ph))) * 20; rot = math.sin(2 * math.pi * ph) * 2.6; sq = 1 + 0.018 * math.cos(4 * math.pi * ph)
    elif kind == "run":
        hop = abs(math.sin(2 * math.pi * ph)) * 46; rot = math.sin(2 * math.pi * ph) * 3.5 - 3; sq = 1 + 0.03 * math.cos(4 * math.pi * ph)
    A, B, u = pose_state(name, t)
    for pose, t0 in ((e[1], e[0]) for e in EV[name]):                       # salti (conto, esultanza)
        if pose in ("salto", "afferra") and t0 - 0.05 <= t < t0 + 0.75:
            p = clamp((t - (t0 - 0.05)) / 0.8); hop += 4 * p * (1 - p) * (110 if pose == "salto" else 60)
            if t < t0 + 0.1: sq *= 1 - 0.07 * clamp((t - (t0 - 0.05)) / 0.15)
            elif p > 0.85: sq *= 1 - 0.06 * math.sin(math.pi * (p - 0.85) / 0.15)
    for pose, t0 in ((e[1], e[0]) for e in EV[name]):                       # arrivo/stop: rimbalzo
        if pose == "neutro" and t0 > 1.0: sq *= 1 + osc(t, t0 + 0.05, 0.05, 8, 24)
    if name == "mouse" and 4.4 <= t < 4.4 + 0.5:                            # spavento: si ritrae
        x -= 34 * math.sin(math.pi * clamp((t - 4.4) / 0.5)); sq *= 1 + 0.05 * math.exp(-6 * (t - 4.4)) * math.sin(30 * (t - 4.4))
    if EAT[name] + 0.5 <= t < EAT[name] + 2.0: sq *= 1 + 0.028 * math.sin((t - EAT[name]) * 24); rot += math.sin((t - EAT[name]) * 12) * 1.2
    tk = talk(name, t); sq *= 1 + 0.022 * tk; rot += math.sin(t * 11 + len(name)) * 1.3 * tk
    if A == B and A in ("tiene", "neutro", "saluta", "guarda_su", "indica", "sbircia"): sq *= 1 + 0.01 * math.sin(t * 3.2 + len(name) * 2)
    if A == "balla" or B == "balla" or A == "balla_m" or B == "balla_m":
        ph2 = ((t - (V["n7"] - 0.1)) / 0.46) % 1; hop += abs(math.sin(math.pi * ph2)) * 30; rot += math.sin(math.pi * 2 * ph2) * 3.5
    if A == "saluta" and t > V["end"]: rot += math.sin(t * 6 + len(name)) * 2
    return x, y, persp(y), hop, rot, sq


_shd = None
def shadow(img, x, y, w, k=1.0):
    global _shd
    if _shd is None:
        sh = Image.new("RGBA", (300, 90), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([25, 25, 275, 65], fill=(60, 30, 10, 130)); _shd = sh.filter(ImageFilter.GaussianBlur(9))
    s2 = _shd.resize((max(2, int(w * 1.35)), max(2, int(w * 1.35 * 90 / 300))), Image.BICUBIC)
    if k < 1: s2.putalpha(s2.getchannel("A").point(lambda v: int(v * k)))
    img.paste(s2, (int(x - s2.width / 2), int(y - s2.height / 2)), s2)


def dust(c, t):
    """nuvolette di polvere ai piedi: a ogni appoggio della corsa/camminata e agli atterraggi"""
    ev = []
    for (name, t0, t1, per, kind) in GAIT:
        q = per / 2 if kind == "run" else per / 2; k = 0
        while t0 + k * q < t1:
            ev.append((name, t0 + k * q + 0.02, 1.0 if kind == "run" else 0.55)); k += 1
    for name, evl in EV.items():
        for (te, pose, dur) in evl:
            if pose in ("salto", "afferra"): ev.append((name, te + 0.72, 1.3))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    for (name, te, amp) in ev:
        u = (t - te) / 0.5
        if not 0 <= u < 1 or t < APPEAR[name]: continue
        x, y, _ = kf_pos(name, te); s = persp(y)
        for j in range(3):
            dx = (j - 1) * 46 * s * amp + math.sin(j * 2.1) * 10; r = (14 + 46 * u) * s * amp * c.Z; a = int(110 * (1 - u) * amp)
            px, py = c.X(x + dx + (j - 1) * 40 * u), c.Y(y - 6 * s - 24 * u * s)
            ld.ellipse([px - r, py - r * 0.7, px + r, py + r * 0.7], fill=(246, 232, 210, min(150, a)))
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


# ------------------------------------------------------------------ frame
_bg = None
_motes = None
def frame(i):
    global _bg, _motes
    t = i / FPS; cx, cy, Z = camera(t)
    if _bg is None:
        _bg = Image.open(os.path.join(HERE, "assets", "amb", "cucina.png")).convert("RGB").resize((W, H), Image.BICUBIC)
        rng = np.random.default_rng(5); _motes = [(rng.uniform(560, 1050), rng.uniform(250, 1500), rng.uniform(0.3, 1.0), rng.uniform(0, 6.28)) for _ in range(46)]
    img = _bg.resize((W, H), Image.BICUBIC, box=(cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z))
    img = img.filter(ImageFilter.GaussianBlur(0.5 + 1.0 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    X, Y = c.X, c.Y

    # raggio di luce dalla finestra + pulviscolo
    sw = 12 * math.sin(t * 0.6)
    beam = [(X(620 + sw), Y(380)), (X(1000 + sw), Y(380)), (X(700 + sw), Y(1500)), (X(120 + sw), Y(1500))]
    c.gd.polygon(beam, fill=(13, 11, 4)); c.glow_used = True
    for (mx, my, sp, ph) in _motes:
        px = mx + math.sin(t * 0.5 * sp + ph) * 40 - (my - 250) * 0.18; py = (my - t * 18 * sp) % 1250 + 250
        r = (2.5 + 2.2 * sp) * Z; a = 0.5 + 0.5 * math.sin(t * 1.3 * sp + ph)
        c.gd.ellipse([X(px) - r, Y(py) - r, X(px) + r, Y(py) + r], fill=(int(120 * a), int(108 * a), int(64 * a)))

    if t >= V["n6"] + 0.6: rainbow(c, V["n6"] + 0.6)

    # barattolo: bagliore interno, tremore a ogni TOC, coperchio che salta
    jh = JAR_H * Z; wob = 0.0; lift = 0.0
    if t < TP:
        wob = 0.6 * math.sin(t * 17) * (0.25 + 0.75 * clamp((t - (TP - 3.0)) / 3.0))
        for kt in KNOCKS:
            wob += osc(t, kt, 9.0, 6.0, 36.0)
        if t > TP - 2.0: wob += math.sin(t * 40) * 3.5 * clamp((t - (TP - 2.0)) / 2.0)
        gl = 0.25 + 0.75 * clamp((t - 2.0) / (TP - 2.0)); gl *= 0.8 + 0.2 * math.sin(t * 9)
        gx, gy, gr = X(JAR[0]), Y(JAR[1] - JAR_H * 0.45), JAR_H * 0.55 * Z * (0.8 + 0.5 * gl)
        c.gd.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(int(70 * gl), int(46 * gl), int(14 * gl))); c.glow_used = True
        lift = (max(0.0, math.sin(t * 30) * wob * 0.5) + (clamp((t - (TP - 0.35)) / 0.35) ** 2) * 26) * Z
    jr, jw, jhh = jar_img(jh, lift, lid=(t < TP))
    jr = jr.rotate(wob, resample=Image.BICUBIC, center=(jw / 2, jhh))
    shadow(img, X(JAR[0] + 14), Y(JAR[1]), 250 * Z, 0.9)
    img.paste(jr, (int(X(JAR[0]) - jw / 2), int(Y(JAR[1]) - jhh)), jr)
    if t < TP:
        sparkles(c, JAR[0], JAR[1] - 220, 2.0, TP - 2.0, n=9, spread=80, rise=80, size=15, seed=3)
    else:
        u = t - TP
        if u < 1.2:
            lx = JAR[0] + 150 * u; ly = JAR[1] - JAR_H - (700 * u - 1100 * u * u)
            lr = lid_img(JAR_H * 0.22 * Z).rotate(-u * 520, resample=Image.BICUBIC, expand=True)
            img.paste(lr, (int(X(lx) - lr.width / 2), int(Y(ly) - lr.height / 2)), lr)
        sparkles(c, JAR[0], JAR[1] - 300, TP, 1.8, n=28, spread=220, rise=130, size=24, seed=5)
        if u < 0.35:                                  # onda d'urto luminosa
            rr = (60 + 700 * u) * Z; ga = 1 - u / 0.35
            c.gd.ellipse([X(JAR[0]) - rr, Y(JAR[1] - 300) - rr * 0.8, X(JAR[0]) + rr, Y(JAR[1] - 300) + rr * 0.8], outline=(int(190 * ga), int(170 * ga), int(100 * ga)), width=int(12 * Z)); c.glow_used = True

    # personaggi, dal più lontano
    vis = [n for n in CHARS if t >= APPEAR[n]]
    order = sorted(vis, key=lambda n: kf_pos(n, t)[1])
    poses = {}
    for n in order: poses[n] = draw_char(img, c, n, t)

    if t < TP:
        for kt in KNOCKS:
            if kt <= t < kt + 0.5 and 0.5 < kt < V["n3"]:
                pop_text(c, "TOC!" if (KNOCKS.index(kt) % 2 == 0) else "TOC TOC!", JAR[0] + 40, JAR[1] - 470 - 30 * (KNOCKS.index(kt) % 3), kt, 0.5, 100, (255, 232, 90), (170, 50, 40), rot=8 if KNOCKS.index(kt) % 2 else -8)

    # numeri del conto
    for key, nm, num, colr in (("t3", "mouse", "1", (255, 120, 120)), ("c3", "chip", "2", (255, 210, 80)), ("s3", "spike", "3", (120, 200, 255))):
        x, y, s, *_ = cstate(nm, V[key])
        pop_text(c, num, x, y - H_CH[nm] * s - 70, V[key] - 0.05, 0.85, 200, colr, (60, 40, 120), rot=-6, ow=14, margin=170)

    # onde del TOC sul barattolo
    for kt in KNOCKS:
        if kt <= t < kt + 0.45 and t < TP:
            u = (t - kt) / 0.45
            for q in range(2):
                rr = (60 + 230 * (u - 0.12 * q)) * Z
                if rr > 0: c.d.ellipse([X(JAR[0]) - rr, Y(JAR[1] - 170) - rr * 0.85, X(JAR[0]) + rr, Y(JAR[1] - 170) + rr * 0.85], outline=(255, 245, 200, int(190 * (1 - u))), width=max(2, int(7 * Z * (1 - u))))
    dust(c, t)
    # biscotto: vola dal barattolo e atterra nelle mani aperte (posa 'riceve'); poi è già dentro la posa
    # (tiene_biscotto / mangia / mangia2): niente più biscotto disegnato "a caso" davanti al personaggio
    ck = cookie_sprite()
    for k, n in enumerate(("spike", "chip", "mouse")):
        tl = LAND[n]; t0 = tl - 0.85
        if not (t0 <= t < tl + 0.25): continue
        x, y, s, hop, rot, sq = cstate(n, t)
        hx, hy = x + HAND[n][0] * s, y - hop * s - H_CH[n] * HAND[n][1] * s
        uu = clamp((t - t0) / 0.85)
        px, py = lerp(JAR[0], hx, ease(uu)), lerp(JAR[1] - 300, hy, ease(uu)) - 260 * math.sin(math.pi * uu)
        spin = uu * 540 * (1 - uu) * 2
        size = (104 + 6 * math.sin(t * 5 + k)) * (0.7 + 0.3 * s) * Z
        r = ck.resize((max(2, int(size)), max(2, int(size))), Image.LANCZOS).rotate(spin, resample=Image.BICUBIC)
        if t > tl: r.putalpha(r.getchannel("A").point(lambda v, f=1 - clamp((t - tl) / 0.25): int(v * f)))
        img.paste(r, (int(X(px) - size / 2), int(Y(py) - size / 2)), r)
    for n in ("spike", "chip", "mouse"):                                          # briciole a ogni boccone
        x, y, s, hop, rot, sq = cstate(n, t)
        for j in range(3):
            bt = t - (ET[n] + 0.62 + j * 0.8)
            if 0 <= bt < 0.5:
                mx_, my_ = x + MOUTH[n][0] * s, y - hop * s - H_CH[n] * MOUTH[n][1] * s
                for q in range(5):
                    c.d.ellipse([X(mx_ + (q - 2) * 12) - 4, Y(my_ + 30 + 210 * bt * bt + q * 6) - 4, X(mx_ + (q - 2) * 12) + 4, Y(my_ + 30 + 210 * bt * bt + q * 6) + 4], fill=(150, 98, 52, int(230 * (1 - bt / 0.5))))

    # farfalla magica con scia di brillantini
    if TP + 0.05 <= t < TP + 9.5:
        for j in range(16, 0, -1):
            bx, by = bf_pos(t - j * 0.05); f = 1 - j / 16
            col = tuple(int(v * f) for v in ((255, 220, 120), (255, 255, 255), (255, 170, 210))[j % 3]); star4(c.gd, X(bx), Y(by), (5 + 11 * f) * Z, col); c.glow_used = True
        bx, by = bf_pos(t); b2x, b2y = bf_pos(t + 0.06)
        ang = -math.degrees(math.atan2(b2x - bx, -(b2y - by) + 1e-6)) * 0.3
        sz = 120 * min(1, 0.3 + (t - TP) * 0.7) * (1 - 0.7 * clamp((t - (TP + 8.5)) / 1.0))
        butterfly_draw(c, X(bx), Y(by), sz, ang, (t - TP) * 24, ((255, 150, 60), (255, 220, 90)))

    # cuori, coriandoli
    if V["n7"] <= t < V["end"] + 1.0:
        for k in range(10):
            uu = ((t - V["n7"]) * 0.5 + k / 10) % 1.0; px = X(250 + k * 62 + math.sin(uu * 8 + k) * 40); py = Y(1300 - uu * 560)
            heart(c.d, px, py, 30 * Z * (0.6 + 0.4 * math.sin(math.pi * uu)), (255, 110, 150, int(235 * math.sin(math.pi * uu))))
    if t >= V["n7"]:
        for k in range(18):
            px = ((k * 113 + 40) % W) + math.sin(t * 3 + k) * 30; py = ((t - V["n7"]) * 250 + k * 150) % 1750 + 100
            col = ((255, 120, 150), (255, 220, 70), (120, 200, 255), (160, 230, 120))[k % 4]; c.d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=col)
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); c.img = img = ImageChops.add(ImageChops.add(img, c.glow), g2); c.d = ImageDraw.Draw(img, "RGBA")
    img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 246, 232))), 0.45)
    d = ImageDraw.Draw(img, "RGBA")

    # HOOK
    if t < 2.4:
        u = back(t / 0.35); a = int(255 * clamp((2.4 - t) / 0.4))
        text(d, "SHHH!", W / 2, 330 - 12 * math.sin(t * 6), int(210 * max(0.1, u)), (255, 240, 120, a), (190, 40, 70, a), 14)
        text(d, "Cosa si muove?", W / 2, 520, int(78 * max(0.1, back((t - 0.5) / 0.35))), (255, 255, 255, a), (60, 40, 120, a), 9)
    # sottotitoli
    for k, t0, who, txt, dur in VOICES:
        if t0 - 0.05 <= t <= t0 + dur + 0.3:
            u = ease((t - t0 + 0.05) / 0.18); f = ImageFont.truetype(FONT, 66 if who == "narr" else 78); lines = []; cur = ""
            for wd in txt.split():
                tl_ = (cur + " " + wd).strip(); bb = d.textbbox((0, 0), tl_, font=f, anchor="mm", stroke_width=6)
                if bb[2] - bb[0] > 930 and cur: lines.append(cur); cur = wd
                else: cur = tl_
            lines.append(cur); yy = (1660 if t < 2.4 else 280) - 41 * (len(lines) - 1) + (1 - u) * 14
            for ln in lines: text(d, ln, W / 2, yy, 66 if who == "narr" else 78, COL[who] + (int(255 * u),), (60, 40, 20, int(255 * u)), 7); yy += 84
            break
    subscribe_button(img, t, V["end"] + 0.9, cy=1810)
    return img.tobytes()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2), "TP", round(TP, 2)); print({k: round(v, 2) for k, v in V.items()})
    elif cmd == "prep":
        import time
        t0 = time.time(); ps = precompute(); print(len(ps), "transizioni")
        for n, (nm, a, b) in enumerate(ps):
            try: MO.transition(nm, a, b)
            except Exception as e: print("manca", nm, a, b, str(e)[:60])
        print("fatto in", round(time.time() - t0), "s")
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts) * FPS))).save(f"test_c3_{ts}.png")
    else:
        out = sys.argv[2]; N = int(DUR * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
