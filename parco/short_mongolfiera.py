#!/usr/bin/env python3
"""Short 'La mongolfiera dei quattro amici' (9:16, 1080x1920, 30 fps): topolino, Spike, Chip ed elefantino.
Collina -> cielo sopra le nuvole -> mare -> tramonto. Novità del motore rispetto al castello:
  - pendolo fisico: il cesto oscilla sotto il pallone (secondaria + inerzia), ombra e luce coerenti
  - pallone deformabile (gonfia, si affloscia, si rigonfia), buco con getto d'aria, toppa
  - parallasse a più livelli: sfondo + campo di nuvole 3D a profondità diverse (sfocatura/foschia) + nuvole di passaggio
  - riflessi, spruzzi, acqua davanti al cesto, bloom, grana, gradazione colore per ambiente
    python3 short_mongolfiera.py info | prep | test 1.0 5.5 | render muto.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from scipy.interpolate import PchipInterpolator
import morph as MO

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
AUD = "audioH"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))


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
    at("n1", 0.4); at("t1", 0.2); at("n2", 0.3); at("c1", 0.2); at("n3", 1.3); at("s1", 0.05); at("n4", 0.35); at("t2", 0.1)
    at("c2", 0.15); at("n5", 0.2); at("e1", 0.25); at("n6", 0.2); at("n7", 0.9); at("s2", 0.2); at("t3", 0.1); at("end", 0.4)
    return t + 2.4
DUR = _seq()
SAY = {"n1": "narr", "t1": "mouse", "n2": "narr", "c1": "chip", "n3": "narr", "s1": "spike", "n4": "narr", "t2": "mouse", "c2": "chip",
       "n5": "narr", "e1": "ele", "n6": "narr", "n7": "narr", "s2": "spike", "t3": "mouse", "end": "mouse"}
TXT = {"n1": "Quattro amici vogliono volare! L'elefantino gonfia la mongolfiera.", "t1": "Si parte!",
       "n2": "Su, su, su, sempre più in alto, tra le nuvole!", "c1": "Che bello!",
       "n3": "Ma Spike salta di gioia... e Pop! La mongolfiera si buca!", "s1": "Ops!", "n4": "Scendono veloci verso il mare!",
       "t2": "Aiuto!", "c2": "Ci penso io!", "n5": "Chip si arrampica sulla corda e attacca una toppa.", "e1": "Tocca a me!",
       "n6": "L'elefantino soffia forte... e la mongolfiera torna a volare!", "n7": "Salvi! Al tramonto tornano a casa. Insieme è più bello!",
       "s2": "Evviva!", "t3": "Evviva!", "end": "Bambini Ciao Ciao! Iscrivetevi al canale!"}
COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 170), "ele": (200, 232, 255), "spike": (225, 255, 205)}
VOICES = [(k, V[k], SAY[k], TXT[k], D[k]) for k in V]
E = lambda k: V[k] + D[k]

# eventi
T_INF1 = 0.35                       # inizia a gonfiarsi (all'inizio è già a metà: hook)
T_FULL = V["n1"] + 3.9              # pallone pieno
T_BRD = {"chip": V["n1"] + 3.15, "spike": V["n1"] + 3.55, "mouse": V["n1"] + 3.95, "ele": T_FULL + 0.15}   # salto nel cesto
T_LIFT = V["t1"] + 0.55             # stacco da terra
T_W1 = V["n2"] + 1.55               # nuvole di passaggio (collina -> cielo)
T_POP = V["n3"] + 3.0               # "Pop!"
T_W2 = V["n4"] + 0.55               # caduta tra le nuvole (cielo -> mare)
T_DIP = V["t2"] - 0.15              # il cesto tocca l'acqua
T_CLIMB0 = V["c2"] + 0.35           # Chip comincia a salire
T_CLIMB1 = V["n5"] + 2.75           # arriva al buco
T_PATCH = V["n5"] + 3.0             # toppa attaccata
T_BLOW0 = V["n6"] + 0.45            # l'elefantino soffia
T_BLOW1 = V["n6"] + 3.1
T_UP = T_BLOW0 + 0.4                # si stacca dall'acqua
T_W3 = V["n7"] - 0.45               # nuvole di passaggio (mare -> tramonto)
SCENES = [("collina", 0.0), ("cielo", T_W1), ("mare", T_W2), ("cielo_tramonto", T_W3)]
WIPES = [(T_W1, +1), (T_W2, -1), (T_W3, +1)]          # (istante di copertura totale, direzione: +1 si sale, -1 si scende)

# ------------------------------------------------------------------ quota (altitudine) e fisica
ALT_PTS = [(0, 0), (T_LIFT, 0), (T_LIFT + 1.2, 260), (T_W1, 830), (T_W1 + 2.5, 1180), (T_POP, 1520), (T_POP + 1.0, 1380), (T_W2, 830),
           (T_W2 + 0.7, 330), (T_DIP, 12), (T_DIP + 0.5, 0), (T_UP, 0), (T_UP + 1.5, 330), (T_W3, 830), (T_W3 + 3.0, 1120), (DUR, 1500)]
_alt = PchipInterpolator([p[0] for p in ALT_PTS], [p[1] for p in ALT_PTS])
def alt(t): return float(_alt(t))

L_ROPE = 400.0
BASKET_TOP0 = 1410.0
P_LIE = (430.0, 1350.0)
P0X = 540.0


def fill_raw(t):
    """riempimento del pallone 0..1 (con piccoli 'soffi' mentre l'elefantino gonfia)"""
    if t < T_FULL:
        u = clamp((t - T_INF1) / (T_FULL - T_INF1))
        f = 0.34 + 0.66 * (1 - (1 - u) ** 1.7)
        f += 0.018 * math.sin(t * 14) * (1 - u)
        return f
    f = 1.0
    if t >= T_POP:
        u = clamp((t - T_POP - 0.1) / 2.6); f = 1.0 - 0.46 * u ** 1.5
        if t >= T_W2: f = lerp(f, 0.42, clamp((t - T_W2) / (T_DIP - T_W2)))
    if t >= T_BLOW0:
        u = clamp((t - T_BLOW0) / 2.9)
        f = lerp(0.42, 1.0, ease(u)) + 0.045 * math.sin(math.pi * clamp((u - 0.55) / 0.45)) + 0.014 * math.sin(t * 9) * (1 - u)
    return f


def fill(t):
    f = fill_raw(t)
    if t >= T_POP and t < T_BLOW0: f += 0.012 * math.sin(t * 7)           # vibra mentre perde aria
    return f


def kick(t):
    """urti esterni al cesto (accelerazione angolare)"""
    k = 0.0
    for tk, a in ((T_LIFT + 0.05, 0.9), (T_POP + 0.02, -2.4), (T_DIP, 3.0), (T_DIP + 0.5, -1.4), (T_UP, -1.2), (T_W2 - 0.6, 1.2)):
        if t >= tk: k += a * math.exp(-9 * (t - tk)) * 40
    return k


PX_AMP = [(0.9, 17.0, 0.0), (2.1, 9.0, 1.0), (0.37, 26.0, 2.0)]
def pivot_x(t):
    return P0X + sum(a * math.sin(w * t + p) for w, a, p in PX_AMP)


def _pend():
    """integra il pendolo (cesto appeso al pallone) a 240 Hz: stato = angolo del cesto rispetto alla verticale"""
    n = int((DUR + 1) * 240); dt = 1 / 240.0; th = np.zeros(n); w = 0.0; x = 0.0
    g = 1500.0
    px = [pivot_x(i * dt) for i in range(n)]
    for i in range(1, n):
        t = i * dt
        ax = (px[i] - 2 * px[i - 1] + px[i - 2]) / dt ** 2 if i >= 2 else 0.0
        wind = 0.06 * math.sin(0.7 * t + 0.5) + 0.03 * math.sin(1.9 * t)
        if t >= T_POP and t < T_W2 + 0.5: wind += 0.18 * math.sin(3.1 * t)                  # caduta: scossoni
        acc = -(g / L_ROPE) * math.sin(x) - 0.5 * w - ax / L_ROPE * math.cos(x) + wind + kick(t) * 0.02
        w += acc * dt; x += w * dt; th[i] = x
    return th
_TH = None
def theta(t):
    global _TH
    if _TH is None: _TH = _pend()
    i = t * 240.0; i0 = int(clamp(i, 0, len(_TH) - 2)); fr = i - i0
    return _TH[i0] * (1 - fr) + _TH[i0 + 1] * fr


def dip(t):
    """affondamento del cesto nell'acqua (px verso il basso)"""
    if t < T_DIP - 0.1 or t > T_UP + 1.6: return 0.0
    if t < T_DIP + 0.35: return 64 * back((t - (T_DIP - 0.1)) / 0.45, 2.2)
    if t < T_UP: return 64 + 7 * math.sin(t * 3.3) + 4 * math.sin(t * 7.1)
    return 64 * (1 - ease((t - T_UP) / 1.4))


def rig(t):
    """stato del pallone + cesto"""
    f = fill(t); th = theta(t)
    infl = clamp((t - T_INF1) / (T_FULL - T_INF1))
    Lc = 70 + (L_ROPE - 70) * ease(infl ** 0.8) if t < T_FULL + 0.2 else L_ROPE
    sag = clamp((1 - f) / 0.5)
    by = BASKET_TOP0 + dip(t) + 5 * math.sin(t * 1.3)
    if t >= T_LIFT: by += 0
    px = pivot_x(t); py = by - Lc * math.cos(th)
    e1 = ease(clamp((t - T_INF1) / (T_FULL - T_INF1)) ** 0.9)
    if t < T_FULL + 0.3:                                              # all'inizio il pallone è steso a terra, con la bocca verso l'elefantino
        px = lerp(P_LIE[0], px, e1); py = lerp(P_LIE[1], py, e1)
    px_b = pivot_x(t) + Lc * math.sin(th)
    # inclinazione del pallone: controbilancia il cesto + si piega quando è floscio
    tilt = -0.35 * math.degrees(th) + 4.0 * sag * math.sin(t * 1.9 + 1) + 84.0 * (1 - e1) ** 1.1 + 3.0 * (1 - infl) * math.sin(t * 5)
    sy = 0.16 + 0.84 * max(0.0, f) ** 1.15
    sx = 0.50 + 0.50 * max(0.0, f) ** 0.55
    bend = (1 - f) * 260 * (1 + 0.15 * math.sin(t * 2.3))
    return dict(f=f, th=th, px=px, py=py, bx=px_b, by=by, Lc=Lc, tilt=tilt, sx=sx, sy=sy, bend=bend, sag=sag, infl=infl)


# ------------------------------------------------------------------ oggetti
_obj = {}
def load(name):
    if name not in _obj: _obj[name] = Image.open(os.path.join(HERE, "assets", "obj", name + ".png")).convert("RGBA")
    return _obj[name]


def sized(name, w=None, h=None):
    im = load(name)
    if w is None: w = im.width * h / im.height
    if h is None: h = im.height * w / im.width
    return im.resize((max(2, int(w)), max(2, int(h))), Image.LANCZOS)


RW = 600.0
RH = RW * 884 / 677
BW, BH = 660.0, 290.0
RIMH = 0.24 * BH                       # altezza del bordo anteriore del cesto
FOOT = RIMH + 105                      # i piedi dei personaggi, sotto il bordo (dentro il cesto)
SLOT = {"chip": -215.0, "spike": -78.0, "mouse": 66.0, "ele": 208.0}
CHS = 0.74                            # scala dei personaggi
H_CH = {"mouse": 640 * CHS, "chip": 600 * CHS, "spike": 560 * CHS, "ele": 660 * CHS}
CHARS = ["spike", "chip", "mouse", "ele"]
HOLE = (-100.0, -225.0)                # buco sul pallone (coordinate locali dal perno, dritto)


class Ctx: pass


def star4(d, x, y, r, col):
    k = 0.2; d.polygon([(x, y - r), (x + r * k, y - r * k), (x + r, y), (x + r * k, y + r * k), (x, y + r), (x - r * k, y + r * k), (x - r, y), (x - r * k, y - r * k)], fill=col)


def text(d, s, x, y, size, fill, out, ow):
    d.text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)


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


def flap(c, name, x, y, size, ang, phase, mirror=False, tint=None, alpha=1.0):
    im = load(name)
    w = max(16, min(int(size * c.Z), 900)); h = int(w * im.height / im.width)
    fl = 0.34 + 0.66 * abs(math.cos(phase))
    r = im.resize((max(4, int(w * fl)), h), Image.LANCZOS)
    if mirror: r = r.transpose(Image.FLIP_LEFT_RIGHT)
    r = r.rotate(ang, resample=Image.BICUBIC, expand=True)
    if tint is not None: r = tinted(r, tint)
    if alpha < 1: r.putalpha(r.getchannel("A").point(lambda v: int(v * alpha)))
    c.img.paste(r, (int(x - r.width / 2), int(y - r.height / 2)), r)


def tinted(im, tint):
    a = np.asarray(im).astype(np.float32); a[..., :3] = np.clip(a[..., :3] * np.array(tint, dtype=np.float32), 0, 255)
    return Image.fromarray(a.astype(np.uint8), "RGBA")


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


# ------------------------------------------------------------------ pose dei personaggi
def walk_free(): return []
def ride_loop(t0, t1, a, b, beat=0.5):
    ev = []; i = 0
    while t0 + i * beat < t1:
        ev.append((t0 + i * beat, a if i % 2 == 0 else b, beat * 0.9)); i += 1
    return ev


def climb_seq(t0, t1, per=0.34):
    ev = []; i = 0
    while t0 + i * per < t1:
        ev.append((t0 + i * per, "arrampica" if i % 2 == 0 else "arrampica_m", 0.05)); i += 1
    return ev


EV = {
    "mouse": [(0.0, "saluta2", 0.01), (V["n1"] + 1.8, "indica", 0.2), (T_BRD["mouse"] - 0.1, "salto", 0.15),
              (T_BRD["mouse"] + 0.75, "neutro", 0.2), (V["t1"] - 0.15, "indica", 0.2), (E("t1") + 0.1, "saluta2", 0.2)]
             + [(V["c1"] - 0.2, "ride", 0.2), (V["n3"] + 0.2, "neutro", 0.25), (V["n3"] + 2.0, "guarda_su", 0.2),
                (T_POP + 0.1, "sorpreso", 0.1), (V["n4"], "sorpreso", 0.2), (V["t2"] - 0.1, "fuggi", 0.1), (E("t2") + 0.5, "sorpreso", 0.2),
                (V["c2"] + 0.1, "indica", 0.2), (T_PATCH + 0.3, "ride", 0.2), (V["e1"] - 0.1, "indica", 0.2), (E("e1") + 0.2, "neutro", 0.3),
                (T_BLOW0 + 0.2, "guarda_su", 0.2), (T_UP + 1.3, "ride", 0.2), (T_W3 + 0.3, "saluta2", 0.2), (V["n7"] + 1.0, "neutro", 0.3),
                (V["n7"] + 3.3, "ride", 0.2), (V["s2"], "saluta2", 0.2), (V["t3"] - 0.1, "ride", 0.2), (V["end"] - 0.2, "saluta2", 0.2)],
    "spike": [(0.0, "tiene", 0.01), (V["n1"] + 1.5, "ride", 0.2), (T_BRD["spike"] - 0.1, "salto", 0.15), (T_BRD["spike"] + 0.75, "neutro", 0.2),
              (V["t1"] + 0.1, "saluta2", 0.2), (V["c1"] - 0.1, "guarda_su", 0.2), (V["n3"] + 0.2, "ride", 0.2),
              (T_POP - 0.375, "salto", 0.12), (T_POP + 0.45, "sorpreso", 0.1), (V["s1"] - 0.05, "ops", 0.12), (E("s1") + 0.4, "sorpreso", 0.15),
              (V["t2"] + 0.4, "ops", 0.15), (V["c2"] + 0.6, "sorpreso", 0.15), (T_PATCH + 0.3, "ride", 0.2), (T_BLOW0 + 0.3, "guarda_su", 0.2),
              (T_UP + 1.2, "ride", 0.2), (T_W3 + 0.3, "saluta2", 0.2), (V["n7"] + 1.0, "neutro", 0.3), (V["n7"] + 3.2, "ride", 0.2),
              (V["s2"] - 0.1, "salto", 0.12), (V["s2"] + 0.8, "ride", 0.2), (V["end"] - 0.2, "saluta2", 0.2)],
    "chip": [(0.0, "saluta2", 0.01), (V["n1"] + 1.3, "corre", 0.15), (T_BRD["chip"] - 0.1, "salto", 0.15), (T_BRD["chip"] + 0.75, "neutro", 0.2),
             (V["t1"] + 0.1, "saluta2", 0.2), (V["c1"] - 0.15, "ride", 0.2), (V["n3"] + 0.2, "guarda_su", 0.2),
             (T_POP + 0.1, "sorpreso", 0.1), (V["t2"] - 0.1, "sorpreso", 0.2), (V["c2"] - 0.1, "afferra", 0.15)]
            + climb_seq(T_CLIMB0, T_CLIMB1)
            + [(T_CLIMB1, "afferra", 0.1), (T_PATCH + 0.2, "salto", 0.12), (T_PATCH + 1.1, "ride", 0.2), (T_UP + 1.0, "neutro", 0.3),
               (T_W3 + 0.3, "saluta2", 0.2), (V["n7"] + 1.0, "neutro", 0.3), (V["n7"] + 3.2, "ride", 0.2), (V["s2"], "saluta2", 0.2),
               (V["t3"] - 0.1, "ride", 0.2), (V["end"] - 0.2, "saluta2", 0.2)],
    "ele": [(0.0, "soffia", 0.01), (T_FULL - 0.05, "neutro", 0.2), (T_BRD["ele"] - 0.1, "salto", 0.15), (T_BRD["ele"] + 0.85, "neutro", 0.2),
            (V["t1"] + 0.15, "saluta2", 0.2), (V["c1"] - 0.2, "ride", 0.2), (V["n3"] + 0.2, "guarda_su", 0.2), (T_POP + 0.1, "sorpreso", 0.1),
            (V["t2"] - 0.1, "sorpreso", 0.2), (V["c2"] + 0.5, "guarda_su", 0.2), (T_PATCH + 0.3, "ride", 0.2),
            (V["e1"] - 0.15, "soffia_m", 0.2), (E("e1") + 0.1, "neutro", 0.2), (T_BLOW0 - 0.1, "soffia_m", 0.15), (T_BLOW1, "neutro", 0.25),
            (T_UP + 1.3, "ride", 0.2), (T_W3 + 0.3, "saluta2", 0.2), (V["n7"] + 1.0, "neutro", 0.3), (V["n7"] + 3.2, "ride", 0.2),
            (V["s2"] + 0.2, "saluta2", 0.2), (V["end"] - 0.2, "saluta2", 0.2)],
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
HAS_MOUTH = {"mouse": ("parla_a", "parla_o"), "chip": ("parla_a", "parla_o"), "spike": ("parla_a", "parla_o"), "ele": ("parla_a",)}
ALIAS = {"ele": {"salto": "ride", "indica": "saluta2", "corre": "sorpreso", "parla_o": "parla_a", "afferra": "sorpreso", "ops": "sorpreso"},
         "mouse": {}, "spike": {"corre": "corre", "indica": "indica"}, "chip": {}}


def rp(name, pose):
    al = ALIAS.get(name, {}); m = pose.endswith("_m"); b = pose[:-2] if m else pose
    b = al.get(b, b); return b + ("_m" if m else "")


_iou = {}
def pair_dur(name, A, B, dur):
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
        for p in ("parla_a", "parla_o"):                              # bocca: neutro <-> parla
            pass
    return sorted(pairs)


# ------------------------------------------------------------------ parlato
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


# ------------------------------------------------------------------ posizione dei personaggi
GROUND = {"ele": (150.0, 1765.0), "spike": (935.0, 1735.0), "chip": (790.0, 1830.0), "mouse": (390.0, 1860.0)}


def basket_pt(r, lx, ly):
    """punto del cesto (coordinate locali: x dal centro, y dal bordo superiore) in coordinate mondo"""
    a = r["th"]; ca, sa = math.cos(a), math.sin(a)
    return r["bx"] + lx * ca - ly * sa, r["by"] + lx * sa + ly * ca


def char_place(name, t, r):
    """-> (x, y, rot_gradi, layer) layer: 'ground' | 'basket' | 'climb'"""
    tb = T_BRD[name]; sx = SLOT[name]
    if name == "chip" and T_CLIMB0 - 0.2 <= t <= T_CLIMB1 + 0.45:
        return climb_pos(t, r)
    if t >= tb + 0.7:
        x, y = basket_pt(r, sx, FOOT); return x, y, math.degrees(r["th"]), "basket"
    if t >= tb - 0.15:
        u = clamp((t - (tb - 0.15)) / 0.85)
        gx, gy = GROUND[name]; x1, y1 = basket_pt(r, sx, FOOT)
        x = lerp(gx, x1, ease(u)); y = lerp(gy, y1, ease(u)) - 4 * 235 * u * (1 - u)
        return x, y, math.degrees(r["th"]) * u + 6 * math.sin(u * 6.28) * (1 - u), ("basket" if u > 0.55 else "ground")
    gx, gy = GROUND[name]; return gx, gy, 0.0, "ground"


def climb_pos(t, r):
    """Chip sale da un angolo del cesto lungo la corda sinistra fino al perno e poi sul pallone fino al buco"""
    u = clamp((t - T_CLIMB0) / (T_CLIMB1 - T_CLIMB0))
    c0 = basket_pt(r, -BW * 0.44, 4)
    ring = (r["px"] - 70, r["py"] - 12)
    ca, sa = math.cos(math.radians(r["tilt"])), math.sin(math.radians(r["tilt"]))
    hx = r["px"] + (HOLE[0] * r["sx"]) * ca - (HOLE[1] * r["sy"]) * sa
    hy = r["py"] + (HOLE[0] * r["sx"]) * sa + (HOLE[1] * r["sy"]) * ca
    if t < T_CLIMB0:                                                 # salta sul bordo
        x, y = c0; return x, y + 20, 0.0, "climb"
    if u < 0.62:
        v = ease(u / 0.62) ** 0.9; x = lerp(c0[0], ring[0], v); y = lerp(c0[1], ring[1], v)
    else:
        v = (u - 0.62) / 0.38; x = lerp(ring[0], hx - 8, ease(v)); y = lerp(ring[1], hy + 70, ease(v))
    ang = math.degrees(math.atan2(-(ring[0] - c0[0]), (c0[1] - ring[1]))) * 0.5 if u < 0.62 else 0
    return x, y, ang + math.sin(t * 18) * 2.2, "climb"


# ------------------------------------------------------------------ luce
SUN = {"collina": (1.0, 0.33), "cielo": (1.0, 0.30), "mare": (1.0, 0.31), "cielo_tramonto": (0.0, -0.35)}
TINT = {"collina": (1.0, 1.0, 1.0), "cielo": (1.02, 1.0, 0.95), "mare": (0.98, 1.01, 1.02), "cielo_tramonto": (1.0, 0.78, 0.66)}
RIM = {"collina": ((255, 244, 214), 0.20), "cielo": ((255, 236, 190), 0.34), "mare": ((255, 248, 226), 0.22), "cielo_tramonto": ((255, 150, 70), 0.62)}
RIMDIR = {"collina": (-1, -1), "cielo": (1, -1), "mare": (-1, -1), "cielo_tramonto": (0, -1)}


def cast_shadow(c, r, nw, nh, x, y, sc):
    shx, k = SUN[c.sid]
    al = np.asarray(r.getchannel("A")).astype(np.float32) / 255
    fy = nh * (MO.AY / MO.CH); fx = nw * (MO.AX / MO.CW); ext = int(nh * 0.45)
    M = np.float32([[1, -shx * 0.9, shx * 0.9 * fy], [0, k, fy * (1 - k)]]) if k > 0 else np.float32([[1, 0, 0], [0, k, fy * (1 - k)]])
    sh = cv2.warpAffine(al, M, (nw + int(abs(shx) * nh * 0.6) + 40, nh + ext), flags=cv2.INTER_LINEAR)
    sh = cv2.GaussianBlur(sh, (0, 0), max(4.0, 11 * c.Z * sc))
    a = (sh * 0.30 * 255).astype(np.uint8)
    lay = Image.new("RGBA", (sh.shape[1], sh.shape[0]), (20, 22, 40, 0)); lay.putalpha(Image.fromarray(a))
    c.img.paste(lay, (int(c.X(x) - fx), int(c.Y(y) - fy)), lay)


def draw_char(c, name, t, x, y, rot, layer, hop=0.0, sc=CHS, aux_rot=0.0):
    cv, pose = char_canvas(name, t)
    im = Image.fromarray(np.ascontiguousarray(cv), "RGBA")
    A, B, u = pose_state(name, t)
    sq = 1.0; wob = 0.0
    tk = talk(name, t); sq *= 1 + 0.022 * tk; wob += math.sin(t * 11 + len(name)) * 1.3 * tk
    if A == B and A in ("neutro", "saluta2", "saluta2_m", "guarda_su", "sorpreso", "tiene", "soffia", "soffia_m", "ops", "indica"):
        sq *= 1 + 0.012 * math.sin(t * 3.2 + len(name) * 2)
    if A == B and A in ("ride", "salto"): sq *= 1 + 0.03 * math.sin(t * 13 + len(name)); wob += 2.2 * math.sin(t * 9 + len(name))
    for pose_, t0 in ((e[1], e[0]) for e in EV[name]):
        if pose_ == "salto" and t0 - 0.05 <= t < t0 + 0.8 and layer == "basket":
            p = clamp((t - (t0 - 0.05)) / 0.85); hop += 4 * p * (1 - p) * (390 if name == "spike" and abs(t0 - (T_POP - 0.375)) < 0.1 else 120)
            if t < t0 + 0.1: sq *= 1 - 0.07 * clamp((t - (t0 - 0.05)) / 0.15)
            elif p > 0.85: sq *= 1 - 0.06 * math.sin(math.pi * (p - 0.85) / 0.15)
        if pose_ == "neutro" and t0 > 1.0: sq *= 1 + osc(t, t0 + 0.05, 0.05, 8, 24)
    # dondolio degli amici nel cesto: seguono l'inerzia
    rot = rot + wob + aux_rot
    if rot: im = im.rotate(rot, resample=Image.BILINEAR, center=(MO.AX, MO.AY))
    f = c.Z * sc
    nw, nh = max(2, int(MO.CW * f / math.sqrt(sq))), max(2, int(MO.CH * f * sq))
    rr = im.resize((nw, nh), Image.LANCZOS if f < 1 else Image.BICUBIC)
    px, py = c.X(x) - MO.AX * nw / MO.CW, c.Y(y - hop) - MO.AY * nh / MO.CH
    sid = c.sid
    if layer == "ground":
        cast_shadow(c, rr, nw, nh, x, y, sc)
        wsh = H_CH[name] * 0.45 * c.Z
        ell = Image.new("RGBA", (int(wsh * 2.4), int(wsh * 0.7)), (0, 0, 0, 0)); ImageDraw.Draw(ell).ellipse([wsh * 0.2, wsh * 0.12, wsh * 2.2, wsh * 0.58], fill=(15, 15, 30, 95))
        ell = ell.filter(ImageFilter.GaussianBlur(max(3, 6 * c.Z))); c.img.paste(ell, (int(c.X(x) - ell.width / 2), int(c.Y(y) - ell.height * 0.5)), ell)
    arr = np.asarray(rr).astype(np.float32); a = arr[..., 3] / 255.0
    rgb = arr[..., :3] * np.array(TINT[sid], dtype=np.float32)
    rimc, rimk = RIM[sid]; dx, dy = RIMDIR[sid]
    sg = max(3.0, 8 * f)
    Lb = cv2.GaussianBlur(a, (0, 0), sg)
    Ls = cv2.warpAffine(Lb, np.float32([[1, 0, -dx * sg * 1.1], [0, 1, -dy * sg * 1.1]]), (nw, nh))
    rim = np.clip(a * (1 - Ls * 1.25), 0, 1) ** 1.3
    rgb = rgb + rim[..., None] * np.array(rimc, dtype=np.float32) * rimk
    if layer in ("basket", "climb"):                               # ombra del pallone dall'alto + ombra interna del cesto in basso
        gy = np.linspace(0, 1, nh, dtype=np.float32)[:, None, None]
        top_sh = 1 - 0.20 * np.clip(1 - gy * 2.2, 0, 1) ** 1.3
        low_sh = 1 - 0.22 * np.clip((gy - 0.55) / 0.45, 0, 1)
        rgb = rgb * top_sh * low_sh
    else:
        rgb = rgb * np.linspace(1.02, 0.90, nh, dtype=np.float32)[:, None, None]
    out = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), arr[..., 3]]).astype(np.uint8), "RGBA")
    c.img.paste(out, (int(px), int(py)), out)
    return pose


def tip_world(name, pose, x, y, rot, sc):
    """punta della proboscide (pixel più a destra/sinistra della posa) in coordinate mondo"""
    a = MO.aligned(name, pose)[..., 3] > 128; ys, xs = np.nonzero(a)
    i = xs.argmax() if not pose.endswith("_m") else xs.argmin()
    dx, up = (xs[i] - MO.AX) * sc, (MO.AY - ys[i]) * sc
    ca, sa = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    return x + dx * ca - (-up) * sa * -1 * 0 + (dx * 0), y - up


# ------------------------------------------------------------------ pallone (deformabile)
_ENV = {}
def env_src():
    if "e" not in _ENV:
        im = load("balloon"); _ENV["e"] = np.asarray(im).astype(np.float32); _ENV["e"][..., :3] *= _ENV["e"][..., 3:4] / 255.0
    return _ENV["e"]


def draw_envelope(c, r, t):
    """pallone: scala, si piega quando è floscio, ondeggia come tessuto, con ombre e riflesso. Restituisce la trasformazione."""
    Z = c.Z; src = env_src(); sh_, sw_ = src.shape[:2]
    px, py = c.X(r["px"]), c.Y(r["py"])
    cw, ch = int(RW * 1.45 * Z), int(RH * 1.12 * Z)
    x0, y0 = int(px - cw / 2), int(py - ch * 0.93)
    xs, ys = np.meshgrid(np.arange(cw, dtype=np.float32), np.arange(ch, dtype=np.float32))
    lx = (xs + x0 - px) / Z; ly = (ys + y0 - py) / Z
    tl = math.radians(r["tilt"]); ca, sa = math.cos(tl), math.sin(tl)
    rx = lx * ca + ly * sa; ry = -lx * sa + ly * ca                      # ruota di -tilt
    u = -ry / (RH * r["sy"])
    wobv = 1 + 0.012 * np.sin(t * 3.1 + u * 7.0) + 0.02 * (1 - r["f"]) * np.sin(t * 6 + u * 11)
    bend = r["bend"] * (u ** 2.0) * (1 if True else -1)
    halfw = RW * 0.5 * r["sx"] * wobv
    ux = (rx - bend) / np.maximum(halfw, 1e-3)                            # -1..1
    mapx = (sw_ / 2.0 + ux * sw_ / 2.0).astype(np.float32); mapy = ((1 - u) * (sh_ - 1)).astype(np.float32)
    out = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    al = np.clip(out[..., 3:4], 1, 255)
    rgb = out[..., :3] / al * 255.0
    # volume: più scuro a destra/in basso, riflesso morbido in alto a sinistra, pieghe quando è floscio
    shade = 1 - 0.20 * np.clip((ux + 0.15) / 1.15, 0, 1) ** 1.6 - 0.08 * np.clip(1 - u, 0, 1)
    hl = 0.20 * np.exp(-(((ux + 0.42) / 0.20) ** 2 + ((u - 0.62) / 0.20) ** 2)) * r["f"]
    fold = 1 - 0.20 * (1 - r["f"]) * (0.5 + 0.5 * np.sin(rx * 0.085 + u * 9 + t * 0.7))
    rgb = rgb * (shade * fold)[..., None] * np.array(TINT[c.sid], dtype=np.float32) + 255 * hl[..., None]
    if c.sid == "cielo_tramonto":                                          # luce calda da dietro: bordo arancio
        rim = np.clip(1 - np.abs(ux) * 1.0, 0, 1) ** 8 * 0 + np.exp(-(((np.abs(ux) - 0.97) / 0.07) ** 2)) * 0.55
        rgb = rgb + rim[..., None] * np.array([255, 140, 60], dtype=np.float32) * 0.5
    arr = np.dstack([np.clip(rgb, 0, 255), out[..., 3]]).astype(np.uint8)
    im = Image.fromarray(arr, "RGBA")
    c.img.paste(im, (x0, y0), im)
    return ca, sa


def env_pt(r, lx, ly):
    """punto sul pallone (locale dritto, dal perno; ly<0 = sopra) -> mondo, con scala, piegatura e inclinazione"""
    u = clamp(-ly / RH); ys = ly * r["sy"]; xs = lx * r["sx"] + r["bend"] * u ** 2
    tl = math.radians(r["tilt"]); ca, sa = math.cos(tl), math.sin(tl)
    return r["px"] + xs * ca - ys * sa, r["py"] + xs * sa + ys * ca


# ------------------------------------------------------------------ corde, cesto, buco
def rope(c, p0, p1, sag, col=(120, 82, 44), w=5):
    pts = []
    n = 14
    for i in range(n + 1):
        u = i / n; x = lerp(p0[0], p1[0], u); y = lerp(p0[1], p1[1], u) + sag * 4 * u * (1 - u)
        pts.append((c.X(x), c.Y(y)))
    wid = max(2, int(w * c.Z))
    c.d.line(pts, fill=(60, 40, 22, 255), width=wid + 2)
    c.d.line(pts, fill=col + (255,), width=wid)
    c.d.line([(x + 1, y - 1) for x, y in pts], fill=(200, 160, 100, 140), width=max(1, wid // 3))


_bk = {}
def basket_imgs(Z):
    key = round(Z, 2)
    if key not in _bk:
        im = load("basket"); full = im.resize((int(BW * Z), int(BH * Z)), Image.LANCZOS)
        fr = full.copy(); a = np.asarray(fr).copy(); cut = int(RIMH * Z)
        ramp = np.clip((np.arange(a.shape[0]) - cut) / (10 * Z), 0, 1)[:, None]
        a[..., 3] = (a[..., 3] * ramp).astype(np.uint8)
        _bk[key] = (full, Image.fromarray(a, "RGBA"))
        if len(_bk) > 40: _bk.pop(next(iter(_bk)))
    return _bk[key]


def paste_rot(c, im, ax, ay, wx, wy, ang):
    """incolla im ruotata (antiorario, gradi) attorno al suo punto (ax, ay), che va in (wx, wy) mondo"""
    a = np.asarray(im); h, w = a.shape[:2]
    M = cv2.getRotationMatrix2D((float(ax), float(ay)), float(ang), 1.0)
    cr = cv2.transform(np.float32([[[0, 0], [w, 0], [w, h], [0, h]]]), M)[0]
    x0, y0 = np.floor(cr.min(0)).astype(int) - 2; x1, y1 = np.ceil(cr.max(0)).astype(int) + 2
    M[0, 2] -= x0; M[1, 2] -= y0
    out = cv2.warpAffine(a, M, (int(x1 - x0), int(y1 - y0)), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
    o = Image.fromarray(out, "RGBA")
    c.img.paste(o, (int(c.X(wx) - (ax - x0)), int(c.Y(wy) - (ay - y0))), o)


def draw_basket(c, r, part):
    full, front = basket_imgs(c.Z)
    im = full if part == "back" else front
    tintv = TINT[c.sid]
    if part == "back" or True:
        key = (id(im), c.sid)
        im = tinted(im, tuple(v * (0.82 if part == "back" else 1.0) for v in tintv))
    paste_rot(c, im, im.width / 2, 0, r["bx"], r["by"], math.degrees(r["th"]))


def draw_ropes(c, r, front):
    th = r["th"]
    ringL = (r["px"] - 70, r["py"] - 14); ringR = (r["px"] + 70, r["py"] - 14)
    cL = basket_pt(r, -BW * 0.44, 6); cR = basket_pt(r, BW * 0.44, 6)
    slack = (1 - r["infl"]) * 120
    if front:
        rope(c, ringL, cL, slack, w=6); rope(c, ringR, cR, slack, w=6)
    else:
        bL = basket_pt(r, -BW * 0.30, -6); bR = basket_pt(r, BW * 0.30, -6)
        rope(c, (ringL[0] + 38, ringL[1]), bL, slack * 0.8, col=(95, 66, 36), w=4); rope(c, (ringR[0] - 38, ringR[1]), bR, slack * 0.8, col=(95, 66, 36), w=4)


def draw_hole(c, r, t):
    if t < T_POP: return
    hx, hy = env_pt(r, HOLE[0], HOLE[1]); X, Y, Z = c.X, c.Y, c.Z
    u = clamp((t - T_POP) / 0.12)
    if t < T_PATCH:
        rr = (26 + 6 * math.sin(t * 25)) * Z * back(u) * (0.7 + 0.3 * r["sx"])
        c.d.ellipse([X(hx) - rr, Y(hy) - rr * 0.85, X(hx) + rr, Y(hy) + rr * 0.85], fill=(36, 20, 20, 255), outline=(255, 245, 230, 255), width=max(2, int(5 * Z)))
        for k in range(7):                                                      # lembi strappati
            a = k * 0.9 + 0.3; c.d.polygon([(X(hx) + math.cos(a) * rr * 0.9, Y(hy) + math.sin(a) * rr * 0.8),
                                           (X(hx) + math.cos(a + 0.18) * rr * 1.5, Y(hy) + math.sin(a + 0.18) * rr * 1.3),
                                           (X(hx) + math.cos(a + 0.38) * rr * 0.9, Y(hy) + math.sin(a + 0.38) * rr * 0.8)], fill=(255, 238, 220, 255))
    else:
        s = 130 * (0.6 + 0.4 * r["sx"]) * back((t - T_PATCH) / 0.35, 1.8)
        tp = sized("toppa", w=max(4, s * Z))
        a = (math.sin(t * 2) * 2 - r["tilt"] * 0.4)
        tp = tp.rotate(a, resample=Image.BICUBIC, expand=True)
        c.img.paste(tp, (int(X(hx) - tp.width / 2), int(Y(hy) - tp.height / 2)), tp)
        if t < T_PATCH + 1.0: sparkles(c, hx, hy, T_PATCH, 1.0, n=12, spread=90, rise=30, size=14, seed=3)


def leak_jet(c, r, t):
    """getto d'aria dal buco: nuvolette bianche e linee di velocità che si disperdono"""
    if not (T_POP <= t < T_PATCH): return
    hx, hy = env_pt(r, HOLE[0], HOLE[1]); lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    dirx, diry = -0.85, -0.55
    for k in range(26):
        ph = (t * 3.2 + k * 0.173) % 1.0; d_ = ph * 330
        x = hx + dirx * d_ + math.sin(k * 3.7 + t * 9) * 22 * ph; y = hy + diry * d_ * 0.8 + 60 * ph * ph + math.cos(k * 2.3) * 16 * ph
        rr = (10 + 44 * ph) * c.Z; a = int(170 * (1 - ph))
        ld.ellipse([c.X(x) - rr, c.Y(y) - rr, c.X(x) + rr, c.Y(y) + rr], fill=(250, 252, 255, a))
    lay = lay.filter(ImageFilter.GaussianBlur(3)); c.img.paste(lay, (0, 0), lay)
    for k in range(6):                                                    # linee 'pssss'
        ph = (t * 4 + k * 0.17) % 1.0; d0 = 30 + ph * 210
        c.d.line([(c.X(hx + dirx * d0 - k * 4), c.Y(hy + diry * d0 * 0.8 + 6 * k - 15)), (c.X(hx + dirx * (d0 + 70) - k * 4), c.Y(hy + diry * (d0 + 70) * 0.8 + 6 * k - 15))],
                 fill=(255, 255, 255, int(220 * (1 - ph))), width=max(2, int(5 * c.Z)))


def pop_burst(c, r, t):
    if not (T_POP <= t < T_POP + 0.5): return
    u = (t - T_POP) / 0.5; hx, hy = env_pt(r, HOLE[0], HOLE[1])
    for k in range(10):
        a = k / 10 * 6.283 + 0.3; rr = (30 + 190 * u) * c.Z
        star4(c.d, c.X(hx) + math.cos(a) * rr, c.Y(hy) + math.sin(a) * rr, (30 - 22 * u) * c.Z, (255, 240 - int(60 * u), 100, int(255 * (1 - u))))
    rr = (30 + 220 * u) * c.Z
    c.d.ellipse([c.X(hx) - rr, c.Y(hy) - rr, c.X(hx) + rr, c.Y(hy) + rr], outline=(255, 255, 255, int(255 * (1 - u))), width=max(3, int(10 * (1 - u) * c.Z)))
    if u < 0.55:
        text(c.d, "POP!", c.X(hx) - 40 * c.Z, c.Y(hy) - 150 * c.Z, int(150 * c.Z * back(u / 0.3)), (255, 240, 90, 255), (200, 40, 60, 255), int(12 * c.Z))


def blow_stream(c, r, t, ele_pos):
    """soffio dell'elefantino verso il pallone: scia d'aria con righe e volute"""
    if not (T_BLOW0 <= t < T_BLOW1 or (T_INF1 <= t < T_FULL)): return
    tx, ty = ele_pos
    if t < T_FULL: tgt = (r["px"], r["py"] - 50)
    else: tgt = (r["px"] + 10, r["py"] - 20)
    d_ = 0.0
    for k in range(16):
        ph = (t * 2.4 + k * 0.0625) % 1.0
        x = lerp(tx, tgt[0], ph) + math.sin(k * 5.1 + t * 7) * 12 * (1 - ph) * 0; y = lerp(ty, tgt[1], ph) - 90 * math.sin(math.pi * ph) * (1 if t >= T_FULL else 0.3)
        rr = (8 + 24 * ph) * c.Z
        x += math.sin(ph * 12 + k) * 14
        c.d.ellipse([c.X(x) - rr, c.Y(y) - rr * 0.8, c.X(x) + rr, c.Y(y) + rr * 0.8], fill=(255, 255, 255, int(150 * math.sin(math.pi * ph))))
    for k in range(5):
        ph = (t * 3.0 + k * 0.2) % 1.0
        a0 = lerp(tx, tgt[0], ph * 0.9); b0 = lerp(ty, tgt[1], ph * 0.9) - 50 * math.sin(math.pi * ph)
        c.d.line([(c.X(a0 - 40), c.Y(b0 + k * 9 - 18)), (c.X(a0 + 24), c.Y(b0 + k * 9 - 18 - 6))], fill=(255, 255, 255, int(200 * math.sin(math.pi * ph))), width=max(2, int(4 * c.Z)))


# ------------------------------------------------------------------ sfondi, parallasse, nuvole
_bg = {}
def bg_arr(sid):
    if sid not in _bg:
        _bg[sid] = np.asarray(Image.open(os.path.join(HERE, "assets", "amb", sid + ".png")).convert("RGB").resize((W, H), Image.BICUBIC))
    return _bg[sid]


_grid = None
def parallax(sid, t):
    """sfondo con parallasse verticale (le cose lontane si spostano meno) + animazioni dell'ambiente"""
    global _grid
    if _grid is None: _grid = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    xs, ys = _grid; arr = bg_arr(sid); a = alt(t)
    if sid == "collina":
        s = np.clip((ys - 500) / 1100.0, 0, 1); s = s * s * (3 - 2 * s)
        dy = a * (0.42 + 0.58 * s)
        gust = 0.0
        for g0, g1 in ((T_INF1, T_FULL), (T_BLOW0, T_BLOW1)):
            if g0 <= t <= g1: gust = 1.0
        ground = np.clip((ys - 1100) / 400.0, 0, 1)
        sw = (5 + 9 * gust) * np.sin(2 * math.pi * 0.6 * t + xs * 0.012 + ys * 0.02) * ground * (1 + 0.5 * gust * np.sin(t * 5 - xs * 0.01))
        dx = sw + 6 * np.sin(0.3 * t + xs * 0.002) * np.clip(1 - ys / 900, 0, 1)
        sy_ = ys - dy
    elif sid == "mare":
        dy = a * 0.40 + 0.0
        wat = np.clip((ys - 840 - dy * 0) / 120.0, 0, 1)
        near = np.clip((ys - 840) / 900.0, 0, 1)
        dx = wat * (3 + 12 * near) * np.sin(2 * math.pi * 0.35 * t + ys * 0.03 + xs * 0.005)
        sy_ = ys - dy + wat * (1.5 + 7 * near) * np.sin(2 * math.pi * 0.5 * t + xs * 0.017 + ys * 0.02)
        sy_ = sy_ + (a - 0) * 0.0
    else:
        dy = (a - 900.0) * 0.17 if sid == "cielo" else (a - 900.0) * 0.14
        dx = 8 * np.sin(0.3 * t + xs * 0.002 + ys * 0.003)
        sy_ = ys - dy
    return cv2.remap(arr, (xs + dx).astype(np.float32), sy_.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


# campo di nuvole 3D: (quota, x, profondità, sprite, gonfiore)
_rng = np.random.default_rng(11)
CLOUDS = []
for _i in range(44):
    _d = float(_rng.choice([0.38, 0.5, 0.65, 0.85, 1.0, 1.3], p=[.22, .24, .22, .2, .12, 0.0]))
    CLOUDS.append((_rng.uniform(950, 3500), _rng.uniform(-200, 1280), _d, "nuvola_a" if _rng.random() < 0.55 else "nuvola_b", _rng.uniform(0.85, 1.15), _rng.uniform(0, 6.28)))
CLOUDS.sort(key=lambda q: q[2])
CLOUD_W = {"nuvola_a": 520, "nuvola_b": 380}
CLOUD_TINT = {"collina": (1, 1, 1), "cielo": (1, 1, 1), "mare": (1, 1, 1), "cielo_tramonto": (1.0, 0.74, 0.80)}
_cl = {}
def cloud_sprite(name, w, tint, blur, alpha):
    key = (name, int(w // 12), tint, round(blur, 1), round(alpha, 1))
    if key not in _cl:
        im = sized(name, w=w)
        a = np.asarray(im).astype(np.float32)
        al = cv2.erode(a[..., 3], np.ones((5, 5), np.uint8)); al = cv2.GaussianBlur(al, (0, 0), 3.0 + blur) / 255.0
        pm = a[..., :3] * (a[..., 3:4] / 255.0)
        pb = cv2.GaussianBlur(pm, (0, 0), 7 + blur); ab = cv2.GaussianBlur(a[..., 3] / 255.0, (0, 0), 7 + blur)[..., None]
        clean = pb / np.maximum(ab, 1e-3)
        rgb = np.where((al > 0.97)[..., None], a[..., :3], clean * 0.5 + a[..., :3] * 0.5)
        rgb = rgb * 0.82 + 255 * 0.18                                  # nuvole più bianche e luminose
        rgb = np.clip(rgb * np.array(tint, dtype=np.float32), 0, 255)
        if blur > 0.3: rgb = cv2.GaussianBlur(rgb, (0, 0), blur)
        out = np.dstack([rgb, al * 255 * alpha]).astype(np.uint8)
        _cl[key] = Image.fromarray(out, "RGBA")
        if len(_cl) > 160: _cl.pop(next(iter(_cl)))
    return _cl[key]


def cloud_field(c, t, front):
    a = alt(t); sid = c.sid
    if sid == "mare" and a < 150: lim = 0.55
    for (ca_, cx_, d, name, sc, ph) in CLOUDS:
        if (d >= 1.2) != front: continue
        y = 960 - (ca_ - a) * d * 1.05
        wd = CLOUD_W[name] * d * sc
        if y < -wd * 0.6 or y > H + wd * 0.4: continue
        x = (cx_ + t * 14 * d + 40 * math.sin(t * 0.3 + ph)) % 1500 - 200
        blur = max(0.0, (0.8 - d)) * 5 + max(0.0, d - 1.1) * 9
        alpha = 0.50 + 0.45 * min(1.0, d / 0.9)
        if front: alpha *= 0.55
        spr = cloud_sprite(name, wd * c.Z, CLOUD_TINT[sid], blur, alpha)
        c.img.paste(spr, (int(c.X(x) - spr.width / 2), int(c.Y(y) - spr.height / 2)), spr)


def wipe(c, t):
    """nuvole di passaggio: coprono tutto lo schermo per un istante (cambio ambiente)"""
    for tw, dirn in WIPES:
        if abs(t - tw) > 0.85: continue
        u = t - tw
        cover = ease(1 - abs(u) / 0.8) if abs(u) < 0.8 else 0.0
        rng = np.random.default_rng(int(tw * 10))
        sp = 1500 * dirn
        for k in range(34):
            gx = rng.uniform(-150, 1230); gy0 = rng.uniform(-100, 2000); name = "nuvola_a" if k % 2 == 0 else "nuvola_b"
            wd = rng.uniform(1000, 1700) * (0.55 + 0.45 * (k % 3) / 2)
            y = gy0 + (-u * sp * (0.7 + 0.5 * ((k * 37) % 10) / 10)) * -1 * 0 + (u * sp * (0.7 + 0.5 * ((k * 37) % 10) / 10)) * (-1)
            spr = cloud_sprite(name, wd * c.Z, (1, 1, 1), 1.0 if k % 2 else 0.0, 1.0)
            if cover < 1: spr = spr.copy(); spr.putalpha(spr.getchannel("A").point(lambda v: int(v * clamp(cover * 1.25))))
            c.img.paste(spr, (int(c.X(gx) - spr.width / 2), int(c.Y(y) - spr.height / 2)), spr)
        if cover > 0.55:
            wash = Image.new("RGBA", (W, H), (244, 247, 255, int(175 * clamp((cover - 0.55) / 0.4))))
            if c.sid == "cielo_tramonto" or (tw == T_W3 and u > 0): wash = Image.new("RGBA", (W, H), (255, 218, 220, int(175 * clamp((cover - 0.55) / 0.4))))
            c.img.paste(wash, (0, 0), wash)


def sea_front(c, r, t):
    """acqua davanti al cesto (quando lo sfiora): onda traslucida con schiuma, spruzzi e scia"""
    d_ = dip(t)
    if d_ < 3 or c.sid != "mare": return
    Z = c.Z; top = 1648 + 10 * math.sin(t * 2.1)
    pts_t = []; pts_f = []
    for x in range(-60, 1160, 30):
        yy = top + 12 * math.sin(t * 2.6 + x * 0.018) + 6 * math.sin(t * 4.1 + x * 0.045) - d_ * 0.0
        pts_t.append((c.X(x), c.Y(yy)))
    bot = [(c.X(1160), c.Y(2100)), (c.X(-60), c.Y(2100))]
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.polygon(pts_t + bot, fill=(40, 176, 200, 190))
    for i, (x, y) in enumerate(pts_t):                                        # schiuma
        ld.ellipse([x - 22 * Z, y - 12 * Z, x + 22 * Z, y + 12 * Z], fill=(255, 255, 255, 170))
    lay = lay.filter(ImageFilter.GaussianBlur(2.2)); alpha = clamp(d_ / 30)
    lay.putalpha(lay.getchannel("A").point(lambda v: int(v * alpha))); c.img.paste(lay, (0, 0), lay)
    for k in range(34):                                                       # spruzzi continui sul cesto
        ph = (t * 1.6 + k * 0.0297) % 1.0; side = -1 if k % 2 else 1
        x = r["bx"] + side * (BW * 0.5 - 20 + 90 * ph) * (0.6 + 0.5 * ((k * 7) % 5) / 5)
        y = top - 330 * math.sin(math.pi * ph) * (0.4 + 0.6 * ((k * 13) % 7) / 7)
        rr = (4 + 6 * ((k * 5) % 4) / 4) * Z * (1 - 0.4 * ph)
        c.d.ellipse([c.X(x) - rr, c.Y(y) - rr * 1.2, c.X(x) + rr, c.Y(y) + rr * 1.2], fill=(200, 238, 255, int(210 * (1 - ph))))


def sea_reflection(c, r, t):
    """riflesso del pallone e del cesto nell'acqua quando è basso"""
    if c.sid != "mare": return
    a = alt(t)
    if a > 400: return
    k = clamp(1 - a / 400.0) * 0.28
    # riflesso semplice del pallone: rettangolo sfumato colorato specchiato sotto la linea d'acqua
    hx = c.X(r["px"]); hy = c.Y(1700 + dip(t))
    ref = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(ref)
    for i in range(8):
        col = [(230, 50, 50), (255, 210, 60), (255, 150, 40), (60, 120, 230)][i % 4]
        rd.ellipse([hx - 190 * c.Z + i * 48 * c.Z, hy + 10 * c.Z, hx - 190 * c.Z + (i + 1) * 48 * c.Z, hy + 300 * c.Z], fill=col + (int(255 * k),))
    ref = ref.filter(ImageFilter.GaussianBlur(14 * c.Z)); c.img.paste(ref, (0, 0), ref)


# ------------------------------------------------------------------ uccelli, vento, particelle
def birds(c, t):
    sid = c.sid
    plan = {"cielo": [(V["c1"] - 0.2, 520, 1, 140), (V["n3"] + 0.4, 700, -1, 120)], "mare": [(T_DIP + 1.0, 430, 1, 170), (T_CLIMB0, 520, -1, 150), (T_BLOW0, 380, 1, 160)],
            "cielo_tramonto": [(V["n7"] + 0.5, 520, -1, 110), (V["n7"] + 2.0, 700, 1, 100)], "collina": [(1.5, 420, 1, 120)]}.get(sid, [])
    for k, (t0, yy, d_, sz) in enumerate(plan):
        u = (t - t0) / 6.0
        if 0 <= u <= 1:
            px = lerp(-200, 1280, u) if d_ > 0 else lerp(1280, -200, u); py = yy + 44 * math.sin(u * 8 + k)
            nm = "seagull" if sid != "collina" and sid != "cielo_tramonto" else "bird"
            tint = (1, 0.8, 0.75) if sid == "cielo_tramonto" else None
            flap(c, nm, c.X(px), c.Y(py), sz * (1.0 if nm == "seagull" else 0.8) * c.Z / c.Z * 1.0 * c.Z, -6 * math.sin(t * 2 + k), t * 9 + k, mirror=(d_ < 0), tint=tint)


def petals(c, t):
    """petali e foglie portati dal vento dell'elefantino"""
    g = 0.0
    for g0, g1 in ((T_INF1, T_FULL), ):
        if g0 <= t <= g1: g = 1.0
    if not g: return
    cols = [(255, 140, 170), (255, 220, 90), (255, 255, 255), (170, 130, 255)]
    for k in range(28):
        ph = (t * 0.9 + k * 0.0357) % 1.0
        x = 120 + ph * 1000 + 20 * math.sin(k + t * 3); y = 1500 + 200 * ((k * 53) % 10) / 10 - 140 * ph + 80 * math.sin(ph * 6 + k)
        rr = (7 + 5 * (k % 3)) * c.Z; ang = t * 4 + k
        c.d.ellipse([c.X(x) - rr, c.Y(y) - rr * 0.55, c.X(x) + rr, c.Y(y) + rr * 0.55], fill=cols[k % 4] + (int(230 * math.sin(math.pi * ph)),))


def speed_lines(c, t):
    """linee di caduta quando precipitano"""
    u = 0.0
    if T_POP + 0.6 < t < T_W2 + 0.9: u = ease((t - T_POP - 0.6) / 0.8) * (1 - ease((t - T_W2 - 0.2) / 0.7))
    if u <= 0: return
    rng = np.random.default_rng(5)
    for k in range(34):
        x = rng.uniform(0, W); sp = rng.uniform(1400, 2600); ph = (t * sp / 2400 + rng.uniform(0, 1)) % 1.0; y = ph * 2300 - 200
        ln = rng.uniform(120, 300)
        c.d.line([(x, y), (x, y + ln)], fill=(255, 255, 255, int(120 * u)), width=int(rng.uniform(2, 5)))


def stars(c, t):
    if c.sid != "cielo_tramonto": return
    rng = np.random.default_rng(9)
    for k in range(34):
        x = rng.uniform(20, 1060); y = rng.uniform(20, 560); ph = rng.uniform(0, 6.28); sp = rng.uniform(1.0, 2.4)
        a = 0.35 + 0.65 * max(0.0, math.sin(t * sp + ph)) ** 2
        r = (3 + 4 * rng.random()) * c.Z * (0.6 + a)
        star4(c.gd, c.X(x), c.Y(y), r, tuple(int(235 * a) for _ in range(3))); c.glow_used = True


def god_rays(c, t):
    if c.sid not in ("cielo", "cielo_tramonto"): return
    sx, sy = (800, 560) if c.sid == "cielo" else (540, 1040)
    for k in range(7):
        a0 = 0.5 + 0.5 * math.sin(t * 0.55 + k * 1.2); ang = -math.pi / 2 + (k - 3) * 0.26 + (0.2 if c.sid == "cielo" else 0)
        x1, y1 = sx + math.cos(ang) * 1700, sy + math.sin(ang) * 1700
        col = (int(18 * a0), int(14 * a0), int(7 * a0)) if c.sid == "cielo" else (int(20 * a0), int(10 * a0), int(4 * a0))
        c.gd.polygon([(c.X(sx), c.Y(sy)), (c.X(x1 - 90), c.Y(y1)), (c.X(x1 + 90), c.Y(y1))], fill=col)
    c.glow_used = True
    g = 0.85 + 0.15 * math.sin(t * 1.1)
    glow_blob(c, sx, sy, 520, (90, 78, 40) if c.sid == "cielo" else (130, 70, 25), g)


# ------------------------------------------------------------------ camera
CAM = [  # (t, cx, cy, z)
    (0.0, 540, 1480, 1.0), (1.6, 540, 1460, 1.04), (V["n1"] + 2.6, 540, 1400, 1.08), (T_BRD["mouse"] + 0.5, 540, 1300, 1.0),
    (V["t1"] - 0.1, 540, 1280, 1.38), (T_LIFT + 0.6, 540, 1180, 1.12), (T_W1 - 0.2, 540, 1000, 1.0), (V["c1"] - 0.45, 540, 1000, 1.05), (V["c1"] - 0.05, 540, 1240, 1.4),
    (V["c1"] + 0.9, 540, 1000, 1.05), (V["n3"] + 1.0, 540, 1000, 1.08), (T_POP - 0.3, 520, 1180, 1.28), (T_POP + 0.5, 520, 1000, 1.18),
    (V["s1"], 470, 1250, 1.6), (V["n4"] - 0.1, 540, 1000, 1.05), (T_W2, 540, 1000, 1.0), (V["t2"] - 0.2, 540, 1250, 1.3),
    (E("t2"), 540, 1350, 1.2), (V["c2"] - 0.1, 400, 1220, 1.55), (T_CLIMB0 + 0.6, 440, 1130, 1.28), (T_CLIMB1, 480, 1000, 1.45),
    (T_PATCH + 0.7, 520, 1180, 1.25), (V["e1"] - 0.1, 650, 1280, 1.62), (T_BLOW0 + 0.2, 560, 1120, 1.3), (T_UP + 1.2, 540, 1000, 1.05),
    (T_W3, 540, 1000, 1.0), (V["n7"] + 0.6, 540, 1000, 1.05), (V["n7"] + 3.2, 540, 1180, 1.22), (V["s2"] - 0.2, 540, 1250, 1.27),
    (V["t3"] - 0.1, 540, 1250, 1.27), (V["end"] - 0.1, 540, 1240, 1.29), (DUR, 540, 1210, 1.24),
]
SHAKES = [(T_LIFT, 8), (T_POP, 30), (T_POP + 0.3, 14), (T_DIP, 26), (T_DIP + 0.45, 10), (T_UP, 10), (T_PATCH, 8), (T_W2 - 0.3, 10)]
def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 6 * math.sin(t * 0.8) + 3 * math.sin(t * 2.3); cy += 5 * math.sin(t * 1.1 + 1)
    for kt, amp in SHAKES:
        if kt <= t < kt + 0.4:
            k = (1 - (t - kt) / 0.4) * amp; cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    if T_POP + 0.6 < t < T_W2 + 0.6: cx += 5 * math.sin(t * 40); cy += 5 * math.cos(t * 37)
    z = max(1.0, z); hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


# ------------------------------------------------------------------ fotogramma
def scene_at(t):
    cur = SCENES[0][0]
    for sid, t0 in SCENES:
        if t >= t0: cur = sid
    return cur


GRADE = {"collina": (1.0, 1.0, 1.0), "cielo": (1.0, 0.99, 0.95), "mare": (1.0, 1.0, 1.0), "cielo_tramonto": (1.0, 0.93, 0.88)}


def scene_img(sid, t, cx, cy, Z):
    arr = parallax(sid, t)
    box = (cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z)
    base = Image.fromarray(arr).resize((W, H), Image.BICUBIC, box=box)
    img = base.filter(ImageFilter.GaussianBlur(0.4 + 0.9 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z; c.sid = sid; c.cx = cx; c.cy = cy
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    r = rig(t)
    god_rays(c, t); stars(c, t)
    cloud_field(c, t, front=False)
    birds(c, t)
    petals(c, t)
    sea_reflection(c, r, t)
    # personaggi a terra (davanti al cesto, finché non salgono)
    places = {n: char_place(n, t, r) for n in CHARS}
    # pallone, corde, cesto
    draw_envelope(c, r, t)
    draw_hole(c, r, t); leak_jet(c, r, t); pop_burst(c, r, t)
    draw_ropes(c, r, front=False)
    draw_basket(c, r, "back")
    for n in sorted(CHARS, key=lambda n: SLOT[n]):
        x, y, rot, layer = places[n]
        if layer == "basket": draw_char(c, n, t, x, y, rot, "basket")
    draw_basket(c, r, "front")
    draw_ropes(c, r, front=True)
    for n in sorted(CHARS, key=lambda n: places[n][1]):
        x, y, rot, layer = places[n]
        if layer == "ground" and sid == "collina": draw_char(c, n, t, x, y, rot, "ground")
    ch = places["chip"]
    if ch[3] == "climb": draw_char(c, "chip", t, ch[0], ch[1], ch[2], "climb", sc=CHS * 0.82)
    for n in CHARS:
        x, y, rot, layer = places[n]
        if n == "ele" and (T_INF1 <= t < T_FULL):
            tipx, tipy = tip_world_simple('ele', 'soffia', x, y, CHS)
            blow_stream(c, r, t, (tipx, tipy))
        if n == "ele" and layer == "basket" and (T_BLOW0 <= t < T_BLOW1):
            tx, ty = tip_world_simple("ele", "soffia_m", x, y, CHS)
            blow_stream(c, r, t, (tx, ty))
    for n in sorted(CHARS, key=lambda n: places[n][1]):
        x, y, rot, layer = places[n]
        if layer == "ground" and sid != "collina": pass
    sea_front(c, r, t)
    speed_lines(c, t)
    cloud_field(c, t, front=True)
    wipe(c, t)
    if sid == "collina":                                                 # corde tenute a terra prima del decollo
        pass
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); img = ImageChops.add(ImageChops.add(img, c.glow), g2)
    gcol = GRADE[sid]
    if gcol != (1.0, 1.0, 1.0): img = ImageChops.multiply(img, Image.new("RGB", (W, H), tuple(int(255 * v) for v in gcol))) if False else Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), tuple(int(255 * v) for v in gcol))), 0.5)
    return img


def tip_world_simple(name, pose, x, y, sc):
    a = MO.aligned(name, pose)[..., 3] > 128; ys, xs = np.nonzero(a)
    i = xs.argmax() if not pose.endswith("_m") else xs.argmin()
    return x + (xs[i] - MO.AX) * sc, y - (MO.AY - ys[i]) * sc


def vignette():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.70)) ** 2)
    return np.clip(1 - 0.28 * np.clip(r - 0.45, 0, 1) ** 1.6, 0.6, 1)[..., None].astype(np.float32)
_VIG = None
_GRAIN = None


def frame(i):
    global _VIG, _GRAIN
    if _VIG is None: _VIG = vignette()
    t = i / FPS; cx, cy, Z = camera(t)
    sid = scene_at(t)
    img = scene_img(sid, t, cx, cy, Z)
    arr = np.asarray(img).astype(np.float32)
    # bloom leggero sulle alte luci + grana di pellicola
    bright = np.clip(arr - 215, 0, 255) * 3.0
    bl = cv2.GaussianBlur(bright, (0, 0), 14)
    arr = arr + bl * 0.22
    arr = arr * 0.64 + np.asarray(ImageChops.multiply(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)), Image.new("RGB", (W, H), (255, 246, 232)))).astype(np.float32) * 0.36
    rng = np.random.default_rng(i)
    arr = arr + rng.normal(0, 2.2, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    img = Image.fromarray(np.clip(arr * _VIG, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img, "RGBA")
    if t < 2.5:                                                       # HOOK
        u = back(t / 0.35); a = int(255 * clamp((2.5 - t) / 0.4))
        text(d, "SI VOLA!", W / 2, 215 - 10 * math.sin(t * 6), int(176 * clamp(max(0.62, u), 0, 1.0)), (255, 240, 120, a), (190, 40, 70, a), 13)
    for k, t0, who, txt, dur in VOICES:                              # sottotitoli
        if t0 - 0.05 <= t <= t0 + dur + 0.3:
            u = ease((t - t0 + 0.05) / 0.18); f = ImageFont.truetype(FONT, 66 if who == "narr" else 78); lines = []; cur = ""
            for wd in txt.split():
                tl_ = (cur + " " + wd).strip(); bb = d.textbbox((0, 0), tl_, font=f, anchor="mm", stroke_width=6)
                if bb[2] - bb[0] > 930 and cur: lines.append(cur); cur = wd
                else: cur = tl_
            lines.append(cur); yy = (330 if k == "end" else 1850 - 84 * (len(lines) - 1)) + (1 - u) * 14
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
        print({k: round(v, 2) for k, v in dict(T_FULL=T_FULL, T_LIFT=T_LIFT, T_W1=T_W1, T_POP=T_POP, T_W2=T_W2, T_DIP=T_DIP, T_CLIMB0=T_CLIMB0, T_PATCH=T_PATCH, T_BLOW0=T_BLOW0, T_UP=T_UP, T_W3=T_W3).items()})
    elif cmd == "prep":
        import time
        t0 = time.time(); ps = precompute(); print(len(ps), "transizioni")
        with Pool(4) as pool:
            for r in pool.imap_unordered(_prep, ps):
                if r: print("manca", r)
        print("fatto in", round(time.time() - t0), "s")
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts) * FPS))).save(f"test_m_{ts}.png")
    elif cmd == "renderpart":
        a, b, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; b = min(b, int(DUR * FPS))
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(a, b), chunksize=4)): ff.stdin.write(fr)
        ff.stdin.close(); ff.wait()
    else:
        out = sys.argv[2]; N = int(DUR * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 60 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
