#!/usr/bin/env python3
"""Short 'Il barattolo misterioso' (9:16, 1080x1920, 24 fps).
Topolino, Chip e Spike nella cucina; usa le pose in assets/pose e le voci in audioC.
    python3 short_cucina.py test 1.0 5.5 12     # fotogrammi di controllo (test_cucina_<t>.png)
    python3 short_cucina.py render muto_cucina.mp4
"""
import json, math, os, subprocess, sys
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 24
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
D = json.load(open(os.path.join(HERE, "audioC", "durate.json")))
for _k, _v in {"n1": 5.9, "t1": .7, "n2": 2.9, "c1": .8, "s1": .8, "n3": 3.6, "c2": .7, "s2": .7, "t2": 1.3, "n4": 5.2, "end": 3.0}.items():
    D.setdefault(_k, _v)       # provvisorio finché la voce non esiste


def lerp(a, b, u): return a + (b - a) * u
def clamp(u): return max(0.0, min(1.0, u))
def ease(u): u = clamp(u); return u * u * (3 - 2 * u)
def back(u, k=1.7): u = clamp(u); return 1 + (k + 1) * (u - 1) ** 3 + k * (u - 1) ** 2


# ------------------------------------------------------------------ copione (tempi dalle voci)
V = {}
def _seq():
    t = 0.2
    def at(k, gap):
        nonlocal t
        V[k] = t + gap; t = V[k] + D[k]
    at("n1", 0); at("t1", 0.25); at("n2", 0.35); at("c1", 0.15); at("s1", 0.1); at("n3", 0.45)
    global TP; TP = t + 0.1                     # il coperchio salta
    at("c2", 0.55); at("s2", 0.1); at("t2", 0.15); at("n4", 0.5); at("end", 0.45)
    return t + 1.6
DUR = _seq()
END = lambda k: V[k] + D[k]
SAY = {"n1": "narr", "t1": "mouse", "n2": "narr", "c1": "chip", "s1": "spike", "n3": "narr", "c2": "chip",
       "s2": "spike", "t2": "mouse", "n4": "narr", "end": "mouse"}
TXT = {"n1": "Shhh... sentite anche voi? Qualcosa si muove, nella cucina!", "t1": "Cosa sarà?",
       "n2": "Chip e Spike corrono a vedere.", "c1": "Che curiosità!", "s1": "Cos'è, cos'è?",
       "n3": "Piano piano... aprono il barattolo dei biscotti.", "c2": "Wow!", "s2": "Evviva!",
       "t2": "Una farfalla magica!", "n4": "E i biscotti? Uno per ciascuno, perché condividere è bellissimo!",
       "end": "Bambini Ciao Ciao! Iscrivetevi al canale!"}
COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 170), "spike": (200, 225, 255)}
VOICES = [(k, V[k], SAY[k], TXT[k], D[k]) for k in V]

JAR = (905, 1640)                                # base del barattolo (coordinate mondo)
GY = 1650                                        # linea del pavimento dei personaggi
CH_H = {"mouse": 640, "chip": 600, "spike": 560}
GAP_N4 = END("n4") - 0.0

# posizioni (t, x, y)
KF = {
    "mouse": [(0, 560, GY), (END("s1") + 0.2, 560, GY), (END("s1") + 0.9, 690, GY), (999, 690, GY)],
    "chip": [(0, -260, GY + 20), (END("n2") - 1.6, -260, GY + 20), (END("c1") + 0.1, 250, GY + 20),
             (END("s1") + 0.2, 250, GY + 20), (END("s1") + 0.95, 460, GY + 20), (999, 460, GY + 20)],
    "spike": [(0, -480, GY + 10), (END("n2") - 1.9, -480, GY + 10), (END("c1") + 0.25, 70, GY + 10),
              (END("s1") + 0.2, 70, GY + 10), (END("s1") + 1.0, 235, GY + 10), (999, 235, GY + 10)],
}
CHARS = ["spike", "chip", "mouse"]


def seg(name, t):
    """posizione, se si muove, direzione e distanza percorsa"""
    kf = KF[name]; cum = 0.0
    if t <= kf[0][0]: return kf[0][1], kf[0][2], False, 1, 0.0
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        L = math.hypot(x1 - x0, y1 - y0)
        if t0 <= t <= t1:
            mv = L > 0; u = ease((t - t0) / (t1 - t0)) if mv else 0
            return lerp(x0, x1, u), lerp(y0, y1, u), mv, (1 if x1 >= x0 else -1), cum + L * u
        cum += L
    return kf[-1][1], kf[-1][2], False, 1, cum


def pose_of(name, t):
    x, y, mv, dirn, cum = seg(name, t)
    if mv: return ("cammina_sx" if int(cum / 70) % 2 == 0 else "cammina_dx")
    if name == "mouse":
        if t < V["t1"]: return "sorpreso"
        if t < END("n2"): return "tiene"
        if t < END("n3") - 1.2: return "tiene"
        if t < TP: return "china"
        if t < V["t2"]: return "sorpreso"
        if t < V["n4"]: return "saluta"
        if t < V["end"]: return "tiene"
        return "ride"
    if name == "chip":
        if t < V["c1"]: return "tiene"
        if t < END("c1") + 0.1: return "sorpreso"
        if t < END("n3") - 1.2: return "tiene"
        if t < TP: return "china"
        if t < V["n4"] - 0.2: return "ride"
        if t < V["end"]: return "tiene"
        return "saluta"
    if t < V["s1"]: return "tiene"                       # spike
    if t < END("s1") + 0.1: return "sorpreso"
    if t < END("n3") - 1.2: return "tiene"
    if t < TP: return "china"
    if t < V["n4"] - 0.2: return "ride"
    if t < V["end"]: return "tiene"
    return "saluta"


# ------------------------------------------------------------------ sprite
_poses = {}
_ref_h = {}
def pose_img(chi, pose):
    key = (chi, pose)
    if key not in _poses:
        im = Image.open(os.path.join(HERE, "assets", "pose", f"{'topo' if chi == 'mouse' else chi}_{pose}.png")).convert("RGBA")
        a = im.getchannel("A").point(lambda v: 255 if v > 150 else 0).filter(ImageFilter.MinFilter(5))  # toglie la frangia chiara
        im.putalpha(a.filter(ImageFilter.GaussianBlur(0.8)))
        al = np.asarray(a) > 0; ys, xs = np.nonzero(al)
        top, bot = ys.min(), ys.max(); h = bot - top
        tor = al[int(top + h * 0.35):int(top + h * 0.7)]; cx = np.nonzero(tor)[1].mean() if tor.any() else xs.mean()
        _poses[key] = (im, float(cx), float(bot), int(h))
    return _poses[key]


def ref_scale(chi):
    if chi not in _ref_h: _ref_h[chi] = CH_H[chi] / pose_img(chi, "tiene")[3]
    return _ref_h[chi]


def draw_char(img, chi, pose, x, y, s=1.0, rot=0.0, sq=1.0, flip=False):
    im, ax, ay, _ = pose_img(chi, pose)
    sc = ref_scale(chi) * s
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT); ax = im.width - ax
    nw, nh = max(1, int(im.width * sc / sq)), max(1, int(im.height * sc * sq))
    r = im.resize((nw, nh), Image.LANCZOS if sc < 1 else Image.BICUBIC)
    px, py = ax * nw / im.width, ay * nh / im.height
    if rot:
        r = r.rotate(rot, resample=Image.BICUBIC, center=(px, py))
    img.paste(r, (int(x - px), int(y - py)), r)


SHD = None
def shadow(img, x, y, w, k=1.0):
    global SHD
    if SHD is None:
        sh = Image.new("RGBA", (300, 90), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([25, 25, 275, 65], fill=(60, 30, 10, 130)); SHD = sh.filter(ImageFilter.GaussianBlur(9))
    s2 = SHD.resize((max(2, int(w * 1.35)), max(2, int(w * 1.35 * 90 / 300))), Image.BICUBIC)
    if k < 1: s2.putalpha(s2.getchannel("A").point(lambda v: int(v * k)))
    img.paste(s2, (int(x - s2.width / 2), int(y - s2.height / 2)), s2)


# ------------------------------------------------------------------ oggetti disegnati
_obj = {}
def jar_sprite():
    if "jar" not in _obj:
        S = 3; w, h = 260, 340; cv = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
        d.rounded_rectangle([20 * S, 70 * S, 240 * S, 335 * S], radius=46 * S, fill=(205, 232, 245, 150), outline=(255, 255, 255, 235), width=5 * S)
        for k, (cx, cy) in enumerate([(70, 300), (130, 305), (190, 298), (100, 258), (160, 262), (130, 214)]):
            r = 44 * S / 2 * 1.35; d.ellipse([(cx - 33) * S, (cy - 33) * S, (cx + 33) * S, (cy + 33) * S], fill=(196, 130, 66, 255), outline=(140, 84, 38, 255), width=3 * S)
            for dx, dy in ((-11, -9), (9, -12), (2, 8), (-14, 10), (14, 6)):
                d.ellipse([(cx + dx - 4) * S, (cy + dy - 4) * S, (cx + dx + 4) * S, (cy + dy + 4) * S], fill=(88, 50, 28, 255))
        d.rounded_rectangle([52 * S, 82 * S, 74 * S, 320 * S], radius=10 * S, fill=(255, 255, 255, 90))      # riflesso
        d.rounded_rectangle([40 * S, 56 * S, 220 * S, 80 * S], radius=8 * S, fill=(236, 236, 240, 255), outline=(255, 255, 255, 255), width=3 * S)  # collo
        _obj["jar"] = cv.resize((w, h), Image.LANCZOS)
        S = 3; cv = Image.new("RGBA", (w * S, 70 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
        d.rounded_rectangle([30 * S, 18 * S, 230 * S, 62 * S], radius=14 * S, fill=(222, 56, 56, 255), outline=(150, 28, 28, 255), width=4 * S)
        d.rounded_rectangle([90 * S, 2 * S, 170 * S, 24 * S], radius=10 * S, fill=(255, 190, 70, 255), outline=(170, 110, 30, 255), width=3 * S)
        d.rounded_rectangle([44 * S, 26 * S, 216 * S, 36 * S], radius=5 * S, fill=(255, 255, 255, 80))
        _obj["lid"] = cv.resize((w, 70), Image.LANCZOS)
    return _obj["jar"], _obj["lid"]


def cookie_sprite():
    if "ck" not in _obj:
        S = 4; n = 120; cv = Image.new("RGBA", (n * S, n * S), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
        d.ellipse([6 * S, 6 * S, 114 * S, 114 * S], fill=(210, 140, 70, 255), outline=(145, 88, 38, 255), width=5 * S)
        d.ellipse([16 * S, 14 * S, 80 * S, 60 * S], fill=(228, 166, 96, 160))
        for dx, dy in ((-26, -22), (22, -30), (4, 4), (-30, 24), (32, 18), (-4, 36), (30, -4)):
            d.ellipse([(60 + dx - 9) * S, (60 + dy - 8) * S, (60 + dx + 9) * S, (60 + dy + 8) * S], fill=(80, 46, 26, 255))
        _obj["ck"] = cv.resize((n, n), Image.LANCZOS)
    return _obj["ck"]


def heart(d, x, y, r, col):
    pts = []
    for i in range(40):
        a = i / 40 * 2 * math.pi
        pts.append((x + r * 16 * math.sin(a) ** 3 / 16, y - r * (13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)) / 16))
    d.polygon(pts, fill=col)


def star4(d, x, y, r, col):
    k = 0.2; d.polygon([(x, y - r), (x + r * k, y - r * k), (x + r, y), (x + r * k, y + r * k), (x, y + r), (x - r * k, y + r * k), (x - r, y), (x - r * k, y - r * k)], fill=col)


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
def rainbow(c, t0, cx=540, cy=1330, R=560, band=34):
    if c.t < t0: return
    p = ease((c.t - t0) / 1.4); a = min(1, (c.t - t0) / 0.5) * 0.55
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i, col in enumerate(RB):
        r = (R - i * band) * c.Z; d.arc([c.X(cx) - r, c.Y(cy) - r, c.X(cx) + r, c.Y(cy) + r], 180, 180 + 180 * p, fill=col + (int(255 * a),), width=int(band * c.Z) + 1)
    lay = lay.filter(ImageFilter.GaussianBlur(1.6)); c.img.paste(lay, (0, 0), lay)


def butterfly(c, x, y, size, ang, phase, cols):
    Ssz = 3; w = max(20, min(int(size * c.Z * 2.6), 600)); cv = Image.new("RGBA", (w * Ssz, w * Ssz), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
    ox, oy = w * Ssz / 2, w * Ssz / 2; u = w * Ssz * 0.30; fl = abs(math.cos(phase)) * 0.82 + 0.18
    fore = [(0, 0), (0.95, -0.95), (1.45, -0.55), (1.2, 0.1), (0.15, 0.1)]; hind = [(0, 0.05), (1.0, 0.18), (1.05, 0.85), (0.5, 1.0), (0.1, 0.5)]
    for sg in (-1, 1):
        for poly, col, col2 in ((fore, cols[0], cols[1]), (hind, cols[1], cols[0])):
            pts = [(ox + sg * px * fl * u, oy + py * u) for px, py in poly]; d.polygon(pts, fill=col + (255,), outline=(60, 40, 70, 255))
            cxp = sum(p[0] for p in pts) / len(pts); cyp = sum(p[1] for p in pts) / len(pts); r_ = u * 0.28
            d.ellipse([cxp - r_, cyp - r_, cxp + r_, cyp + r_], fill=col2 + (255,))
    d.ellipse([ox - u * 0.07, oy - u * 0.55, ox + u * 0.07, oy + u * 0.55], fill=(60, 40, 60, 255))
    cv = cv.resize((w, w), Image.LANCZOS).rotate(ang, resample=Image.BICUBIC); c.img.paste(cv, (int(x - w / 2), int(y - w / 2)), cv)


def confetti(c, t0, n=16):
    if c.t < t0: return
    for k in range(n):
        px = ((k * 113 + 40) % W) + math.sin(c.t * 3 + k) * 30; py = ((c.t - t0) * 240 + k * 160) % 1700 + 120
        col = ((255, 120, 150), (255, 220, 70), (120, 200, 255), (160, 230, 120))[k % 4]; c.d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=col)


def subscribe_button(img, t, t0, cy=1500):
    if t < t0: return
    u = back((t - t0) / 0.45); s = max(0.05, u) * (1 + 0.03 * math.sin((t - t0) * 6))
    w, h = 520, 130; Sx = 2; cv = Image.new("RGBA", (w * Sx, h * Sx + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
    d.rounded_rectangle([6 * Sx, 10 * Sx, (w - 6) * Sx, (h - 6) * Sx], radius=34 * Sx, fill=(0, 0, 0, 70))
    d.rounded_rectangle([0, 0, (w - 12) * Sx, (h - 16) * Sx], radius=34 * Sx, fill=(232, 36, 36, 255), outline=(255, 255, 255, 255), width=4 * Sx)
    f = ImageFont.truetype(FONT, 54 * Sx); d.text((((w - 12) / 2 + 34) * Sx, (h - 16) / 2 * Sx), "ISCRIVITI", font=f, fill=(255, 255, 255, 255), anchor="mm")
    bell = Image.new("RGBA", (90 * Sx, 90 * Sx), (0, 0, 0, 0)); bd = ImageDraw.Draw(bell)
    bd.pieslice([20 * Sx, 12 * Sx, 70 * Sx, 62 * Sx], 180, 360, fill=(255, 255, 255, 255)); bd.polygon([(20 * Sx, 38 * Sx), (70 * Sx, 38 * Sx), (78 * Sx, 62 * Sx), (12 * Sx, 62 * Sx)], fill=(255, 255, 255, 255))
    bd.ellipse([36 * Sx, 62 * Sx, 54 * Sx, 78 * Sx], fill=(255, 255, 255, 255)); bd.ellipse([40 * Sx, 4 * Sx, 50 * Sx, 14 * Sx], fill=(255, 255, 255, 255))
    bell = bell.rotate(math.sin((t - t0) * 14) * 16 * max(0, 1 - (t - t0) / 1.8), resample=Image.BICUBIC, center=(45 * Sx, 14 * Sx))
    cv.paste(bell, (24 * Sx, int(((h - 16) / 2 - 45) * Sx)), bell)
    cv = cv.resize((int(w * s), int((h + 10) * s)), Image.LANCZOS); img.paste(cv, (int(W / 2 - cv.width / 2), int(cy - cv.height / 2)), cv)


def text(d, s, x, y, size, fill, out, ow):
    d.text((x, y), s, font=ImageFont.truetype(FONT, size), fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)


# ------------------------------------------------------------------ camera
SHOTS = [  # (t0, t1, (cx, cy, z) inizio, (cx, cy, z) fine)
    (0.0, END("t1") + 0.2, (700, 1480, 1.25), (680, 1450, 1.45)),
    (END("t1") + 0.2, END("s1") + 0.2, (540, 1380, 1.0), (500, 1420, 1.12)),
    (END("s1") + 0.2, TP - 0.05, (560, 1450, 1.15), (640, 1440, 1.35)),
    (TP - 0.05, V["t2"] + 0.2, (820, 1400, 1.6), (600, 1340, 1.2)),
    (V["t2"] + 0.2, V["n4"] - 0.1, (580, 1380, 1.05), (580, 1400, 1.0)),
    (V["n4"] - 0.1, V["end"] - 0.1, (580, 1450, 1.2), (580, 1470, 1.12)),
    (V["end"] - 0.1, 999, (560, 1420, 1.0), (560, 1400, 1.0)),
]
def camera(t):
    for (t0, t1, a, b) in SHOTS:
        if t0 <= t < t1:
            u = ease((t - t0) / (t1 - t0)) if t1 < 900 else (t - t0) / 6; cx, cy, z = [lerp(a[i], b[i], min(1, u)) for i in range(3)]; break
    else: cx, cy, z = SHOTS[-1][3]
    if TP <= t < TP + 0.3:
        k = (1 - (t - TP) / 0.3) * 14; cx += math.sin(t * 90) * k; cy += math.cos(t * 77) * k
    hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


# ------------------------------------------------------------------ frame
_bg = None
_env = {}
def env(k):
    import wave
    if k not in _env:
        if not os.path.exists(os.path.join(HERE, "audioC", f"{k}.wav")): _env[k] = np.zeros(400); return _env[k]
        with wave.open(os.path.join(HERE, "audioC", f"{k}.wav")) as w:
            a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
        win = 44100 // (FPS * 2); n = len(a) // win + 1
        e = np.array([np.sqrt(np.mean(a[i * win:(i + 1) * win] ** 2) + 1e-12) for i in range(n)]); _env[k] = e / (np.percentile(e, 95) + 1e-9)
    return _env[k]


def talk(who, t):
    """0..1 : quanto sta parlando il personaggio in questo istante (dalla voce)."""
    for k, t0, w, tx, d in VOICES:
        if w == who and t0 <= t <= t0 + d:
            e = env(k); return min(1.0, e[min(len(e) - 1, int((t - t0) * FPS * 2))])
    return 0.0


def cstate(name, t):
    x, y, mv, dirn, cum = seg(name, t)
    s = (0.80 + (y - 1300) / 1000 * 0.45) / 0.96 * 0.96 + 0.0
    hop = 0.0; rot = 0.0; sq = 1.0
    if mv:
        k = abs(math.sin(cum / 70 * math.pi)); hop = k ** 0.8 * 22; sq = 1 - 0.04 * (1 - min(1, k * 3)); rot = math.sin(cum / 70 * math.pi) * 2.2
    p = pose_of(name, t)
    tk = talk(name, t); sq *= 1 + 0.025 * tk; rot += math.sin(t * 9 + len(name)) * 1.2 * tk
    if p == "ride" or (name != "mouse" and TP <= t < V["n4"] - 0.2):          # esultanza: saltelli
        ph = ((t - TP) / 0.7 + {"mouse": 0, "chip": 0.3, "spike": 0.6}[name]) % 1; air = 4 * ph * (1 - ph); hop += air * 70; rot += math.sin(2 * math.pi * ph) * 3
    elif p in ("tiene", "saluta", "sorpreso"): sq *= 1 + 0.008 * math.sin(t * 3 + len(name) * 2)    # respiro
    if p == "sorpreso":
        ts = {"mouse": V["t1"] - 0.6 if t < V["t1"] + 1 else V["t2"], "chip": V["c1"], "spike": V["s1"]}[name]
        if 0 <= t - ts < 0.5: sq *= 1 + 0.06 * math.exp(-8 * (t - ts)) * math.sin(30 * (t - ts))
    return x, y, s, hop, rot, sq, dirn, mv, p


def frame(i):
    global _bg
    t = i / FPS; cx, cy, Z = camera(t)
    if _bg is None: _bg = Image.open(os.path.join(HERE, "assets", "amb", "cucina.png")).convert("RGB").resize((W, H), Image.BICUBIC)
    img = _bg.resize((W, H), Image.BICUBIC, box=(cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z))
    img = img.filter(ImageFilter.GaussianBlur(0.6 + 1.2 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    X, Y = c.X, c.Y

    if t >= TP + 0.2: rainbow(c, TP + 0.2)

    # barattolo che si agita
    jar, lid = jar_sprite(); jh = 330 * Z; jw = jar.width * jh / jar.height
    amp = 0.0
    if t < TP: amp = (1.0 + 7 * clamp((t - 0.0) / (TP)) ) * (0.55 + 0.45 * abs(math.sin(t * 2.3))) * (1 if (t % 1.6) < 1.0 else 0.25)
    wob = math.sin(t * 34) * amp
    jr = jar.resize((int(jw), int(jh)), Image.LANCZOS).rotate(wob, resample=Image.BICUBIC, center=(jw / 2, jh))
    shadow(img, X(JAR[0] + 14), Y(JAR[1]), 250 * Z, 0.9)
    img.paste(jr, (int(X(JAR[0]) - jw / 2), int(Y(JAR[1]) - jh)), jr)
    if t < TP:
        lh = 70 * jh / 340; lw = lid.width * lh / lid.height; lr = lid.resize((int(lw), int(lh)), Image.LANCZOS)
        lift = max(0, math.sin(t * 34 + 1) * amp * 0.25) * 4
        img.paste(lr, (int(X(JAR[0]) - lw / 2), int(Y(JAR[1]) - jh * 0.99 - lift * Z)), lr)
        sparkles(c, JAR[0], JAR[1] - 200, 0.0, TP, n=7, spread=70, rise=70, size=14, seed=3)
    else:
        u = t - TP; ly = 180 * (u * 3.2 - 5 * u * u * 3.2 * 1.6) if u < 0.9 else None
        if u < 1.1:
            lx = JAR[0] + 130 * u; ly = JAR[1] - 330 - (520 * u - 900 * u * u)
            lh = 70 * Z; lw = lid.width * lh / lid.height
            lr = lid.resize((int(lw), int(lh)), Image.LANCZOS).rotate(-u * 420, resample=Image.BICUBIC, expand=True)
            img.paste(lr, (int(X(lx) - lr.width / 2), int(Y(ly) - lr.height / 2)), lr)
        sparkles(c, JAR[0], JAR[1] - 300, TP, 1.6, n=26, spread=200, rise=120, size=24, seed=5)

    # personaggi, dal più lontano
    states = sorted([cstate(n, t) + (n,) for n in CHARS], key=lambda q: q[1])
    for (x, y, s, hop, rot, sq, dirn, mv, p, n) in states:
        shadow(img, X(x + 20), Y(y), CH_H[n] * 0.5 * Z * s, max(0.5, 1 - hop / 120))
        sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw_char(sub, n, p, X(x), Y(y - hop), s * Z, rot, sq, flip=False)
        img.paste(sub, (0, 0), sub)

    # biscotti: volano dal barattolo e vengono tenuti in mano
    if t >= V["n4"]:
        ck = cookie_sprite()
        for k, n in enumerate(("spike", "chip", "mouse")):
            t0 = V["n4"] + 0.25 + k * 0.28; u = (t - t0) / 0.75
            if u < 0: continue
            x, y, s, hop, rot, sq, dirn, mv, p = cstate(n, t)
            tx, ty = x + 0.03 * CH_H[n], y - hop - CH_H[n] * 0.30 * s
            u = clamp(u); px, py = lerp(JAR[0], tx, ease(u)), lerp(JAR[1] - 280, ty, ease(u)) - 260 * math.sin(math.pi * u)
            ch = (95 + 15 * math.sin(t * 5 + k)) * Z; r = ck.resize((int(ch), int(ch)), Image.LANCZOS).rotate(u * 360 * (1 - u) * 2, resample=Image.BICUBIC)
            img.paste(r, (int(X(px) - ch / 2), int(Y(py) - ch / 2)), r)
    # farfalla magica
    if TP + 0.1 <= t < V["end"] + 3:
        u = t - TP - 0.1; bx = JAR[0] - 40 + 150 * math.sin(u * 1.9) - 180 * clamp(u / 3); by = JAR[1] - 330 - 330 * ease(u / 2.2) + 70 * math.sin(u * 3.3)
        butterfly(c, X(bx), Y(by), 120 * min(1, 0.4 + u), math.sin(u * 1.9) * 25, u * 22, ((255, 150, 60), (255, 220, 90)))
    # cuori durante la condivisione
    if V["n4"] + 0.9 <= t < V["end"]:
        for k in range(9):
            uu = ((t - V["n4"]) * 0.45 + k / 9) % 1.0; px = X(300 + k * 55 + math.sin(uu * 8 + k) * 40); py = Y(1250 - uu * 520)
            heart(c.d, px, py, 30 * Z * (0.6 + 0.4 * math.sin(math.pi * uu)), (255, 110, 150, int(240 * math.sin(math.pi * uu))))
    if t >= V["t2"]: confetti(c, V["t2"], 14)
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(9)); c.img = img = ImageChops.add(ImageChops.add(img, c.glow), g2); c.d = ImageDraw.Draw(img, "RGBA")
    img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 246, 232))), 0.5)
    d = ImageDraw.Draw(img, "RGBA")

    # HOOK: SHHH! + punto interrogativo nei primi secondi
    if t < 2.7:
        u = back(t / 0.35); a = int(255 * clamp(min(1, (2.7 - t) / 0.4)))
        text(d, "SHHH!", W / 2, 330 - 12 * math.sin(t * 6), int(210 * max(0.1, u)), (255, 240, 120, a), (190, 40, 70, a), 14)
        text(d, "Cosa si muove?", W / 2, 520, int(78 * max(0.1, back((t - 0.6) / 0.35))), (255, 255, 255, a), (60, 40, 120, a), 9)
    # sottotitoli
    for k, t0, who, txt, dur in VOICES:
        if t0 - 0.05 <= t <= t0 + dur + 0.3:
            u = ease((t - t0 + 0.05) / 0.18); f = ImageFont.truetype(FONT, 66); lines = []; cur = ""
            for wd in txt.split():
                tl_ = (cur + " " + wd).strip(); bb = d.textbbox((0, 0), tl_, font=f, anchor="mm", stroke_width=6)
                if bb[2] - bb[0] > 930 and cur: lines.append(cur); cur = wd
                else: cur = tl_
            lines.append(cur); yy = 300 + (150 if t < 2.7 else 0) - 41 * (len(lines) - 1) + (1 - u) * 14
            if t < 2.7: yy = 1660 - 41 * (len(lines) - 1)
            for ln in lines: text(d, ln, W / 2, yy, 66, COL[who] + (int(255 * u),), (60, 40, 20, int(255 * u)), 7); yy += 82
            break
    subscribe_button(img, t, V["end"] + 0.7, cy=1810)
    return img.tobytes()


if __name__ == "__main__":
    if sys.argv[1] == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts) * FPS))).save(f"test_cucina_{ts}.png")
    elif sys.argv[1] == "info":
        print("DUR", round(DUR, 2), {k: round(v, 2) for k, v in V.items()}, "TP", round(TP, 2))
    else:
        out = sys.argv[2]; N = int(DUR * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
