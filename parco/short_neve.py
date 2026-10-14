#!/usr/bin/env python3
"""Short 'Il pupazzo di neve' (9:16, 1080x1920, 30 fps): topolino, Spike ed elefantino.
Collina innevata -> discesa in slitta tra i pini -> villaggio innevato di sera.
Motore derivato da short_mongolfiera.py (pose con morph, bocca, luce di bordo, ombre, camera, bloom, grana) con in più:
  - neve che cade a 3 profondità (dietro / tra / davanti ai personaggi), sbuffi e spruzzi di neve
  - palla di neve che rotola davvero (grumi in proiezione sferica che girano con la palla, luce fissa) e cresce, con il solco nella neve
  - lanci balistici (testa, cappello, carota) con schiacciamento all'atterraggio
  - pupazzo vivo: faccia di carbone, naso-carota, occhiolino, dondolio
  - discesa: parallasse a più livelli di pini che sfrecciano, slitta che rimbalza, scia di neve, linee di velocità
  - villaggio: finestre e lucine che tremolano, luna con alone, stelle
    python3 short_neve.py info | prep | test 1.0 5.5 | renderpart a b out.mp4 | render muto.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import morph as MO

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
AUD = "audioI"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))
WD = json.load(open(os.path.join(HERE, AUD, "parole.json"))) if os.path.exists(os.path.join(HERE, AUD, "parole.json")) else {}


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
    at("n1", 0.5); at("t1", 0.25); at("n2", 0.3); at("s1", 0.15); at("n3", 0.3); at("e1", 0.25); at("n4", 0.4); at("t2", 0.25)
    at("n5", 1.0); at("e2", 0.2); at("n6", 1.0); at("s2", 0.2); at("n7", 0.3); at("t3", 0.2); at("end", 0.5)
    return t + 2.6
DUR = _seq()
SAY = {"n1": "narr", "t1": "mouse", "n2": "narr", "s1": "spike", "n3": "narr", "e1": "ele", "n4": "narr", "t2": "mouse",
       "n5": "narr", "e2": "ele", "n6": "narr", "s2": "spike", "n7": "narr", "t3": "mouse", "end": "mouse"}
TXT = {"n1": "Nevica! Il topolino fa una palla di neve, sempre più grande!", "t1": "Che grande!",
       "n2": "Spike lancia una palla più piccola: ecco la testa!", "s1": "Oplà!",
       "n3": "L'elefantino mette il naso di carota.", "e1": "Ecco!",
       "n4": "Ma Spike starnutisce... Ecciù! La testa rotola giù!", "t2": "Presto, la slitta!",
       "n5": "Giù veloci tra gli alberi! La palla diventa enorme!", "e2": "Più veloce!",
       "n6": "Si ferma al villaggio. Spike lancia una testa nuova, il topolino il cappello!", "s2": "Che bello!",
       "n7": "Ecco il pupazzo gigante! E fa l'occhiolino!", "t3": "Evviva!", "end": "Bambini Ciao Ciao! Iscrivetevi al canale!"}
COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "ele": (200, 232, 255), "spike": (225, 255, 205)}
VOICES = [(k, V[k], SAY[k], TXT[k], D[k]) for k in V]
E = lambda k: V[k] + D[k]


def word(k, w, frac):
    """istante (assoluto) in cui la voce k pronuncia la parola w (da parole.json, Whisper); se manca, frazione della battuta"""
    for (ww, a, b) in WD.get(k, []):
        if w.lower() in ww.lower(): return V[k] + a
    return V[k] + D[k] * frac


# ------------------------------------------------------------------ eventi
# S1 collina
T_R0 = V["n1"] + 0.9; T_R1 = word("n1", "grande", 0.85) + 0.15        # il topolino fa rotolare la palla
BODY = (620.0, 1760.0)                                                  # base della palla grande
R_B0, R_B1 = 46.0, 168.0
X_B0 = 430.0
T_THROW = word("n2", "lancia", 0.25) + 0.05                             # Spike lancia la testa
T_HEAD = T_THROW + 0.75
R_H = 108.0
T_E0 = V["n3"] - 0.4; T_E1 = word("n3", "naso", 0.6) - 0.35            # l'elefantino arriva
ELE1 = (150.0, 1715.0)
T_CAR0 = T_E1 + 0.5; T_NOSE = T_CAR0 + 0.45                            # carota dalla proboscide al naso
T_SNZ = word("n4", "ciù", 0.45) - 0.15                                      # starnuto
T_FALL = T_SNZ + 0.12
T_ROLLOUT = T_FALL + 0.65
T_W1 = E("t2") + 0.55                                                   # cambio scena (sbuffo di neve)
# S2 discesa
T_BUMP = V["n5"] + 1.1
T_BIG = word("n5", "enorme", 0.8)
T_W2 = E("e2") + 0.9
# S3 villaggio
T_STOP = T_W2 + 0.9
BODY3 = (585.0, 1580.0); R3 = 235.0; R3H = 142.0
T_THROW2 = word("n6", "Spike", 0.4) + 0.15; T_HEAD2 = T_THROW2 + 0.85
T_HAT0 = word("n6", "topolino", 0.75) + 0.1; T_HAT1 = T_HAT0 + 0.8
T_CAR3 = V["n7"] - 0.15; T_NOSE3 = T_CAR3 + 0.6
T_FACE = V["n7"] + 0.25
T_WINK = word("n7", "occhiolino", 0.8) + 0.05
T_DANCE = V["t3"] - 0.15
SCENES = [("neve_collina", 0.0), ("neve_discesa", T_W1), ("neve_sera", T_W2)]
WIPES = [T_W1, T_W2]


# ------------------------------------------------------------------ oggetti
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
        if len(_sz) > 300: _sz.pop(next(iter(_sz)))
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
    """incolla im centrata nel punto mondo (x, y), ruotata di ang gradi"""
    if ang: im = im.rotate(ang, resample=Image.BICUBIC, expand=True)
    c.img.paste(im, (int(c.X(x) - im.width / 2), int(c.Y(y) - im.height / 2)), im)


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
GAIT = []
FLIP_WALK = ["cammina_dx", "passa_dx", "cammina_dx_m", "passa_dx_m"]


def walk(name, t0, t1, period=0.60):
    GAIT.append((name, t0, t1, period))
    q = period / 4; ev = []; i = 0
    while t0 + i * q < t1 - 1e-6:
        ev.append((t0 + i * q, FLIP_WALK[i % 4], q)); i += 1
    return ev


def loop(t0, t1, seq, beat=0.5):
    ev = []; i = 0
    while t0 + i * beat < t1:
        ev.append((t0 + i * beat, seq[i % len(seq)], beat * 0.85)); i += 1
    return ev


EV = {
    "mouse": [(0.0, "guarda_su", 0.01), (1.6, "guarda_su_m", 0.2), (T_R0 - 0.35, "neutro", 0.2)] + walk("mouse", T_R0, T_R1)
             + [(T_R1, "ride", 0.2), (V["t1"] + 0.1, "indica", 0.2), (E("t1") + 0.3, "neutro", 0.25), (T_THROW + 0.2, "guarda_su", 0.2),
                (T_HEAD + 0.1, "ride", 0.2), (V["n3"] + 0.4, "neutro", 0.25), (T_NOSE + 0.1, "ride", 0.2), (V["n4"] + 0.2, "neutro", 0.25),
                (T_FALL + 0.05, "fuggi", 0.1), (T_FALL + 0.7, "sorpreso", 0.15), (V["t2"] - 0.1, "indica", 0.15),
                # S2 sulla slitta
                (T_W1 - 0.1, "indica", 0.01), (V["n5"] + 0.3, "ride", 0.2), (T_BUMP - 0.05, "salto", 0.12), (T_BUMP + 0.6, "indica", 0.2),
                (T_BIG, "sorpreso", 0.15), (V["e2"] + 0.3, "ride", 0.2),
                # S3 villaggio
                (T_W2 - 0.1, "sorpreso", 0.01), (T_STOP + 0.2, "ride", 0.2), (T_THROW2 + 0.2, "guarda_su_m", 0.2),
                (T_HAT0 - 0.45, "lancia", 0.15), (T_HAT0 + 0.25, "guarda_su_m", 0.2), (T_HAT1 + 0.1, "ride", 0.2), (V["n7"], "guarda_su_m", 0.2),
                (T_WINK - 0.1, "sorpreso", 0.15), (T_WINK + 0.6, "ride", 0.2)]
             + loop(T_DANCE, V["end"] - 0.25, ["salto", "balla", "ride", "balla_m"], 0.5) + loop(V["end"] - 0.25, DUR + 1, ["saluta2", "saluta2_m"], 0.62),
    "spike": [(0.0, "sorpreso", 0.01), (1.2, "ride", 0.2), (T_R0 + 0.4, "neutro", 0.25), (V["n2"] - 0.2, "tiene", 0.2),
              (T_THROW - 0.3, "lancia", 0.12), (T_HEAD + 0.05, "salto", 0.12), (T_HEAD + 0.75, "ride", 0.2), (V["n3"] + 0.5, "neutro", 0.25),
              (T_NOSE + 0.1, "ride", 0.2), (V["n4"] + 0.1, "neutro", 0.25), (T_SNZ - 0.65, "ops", 0.15), (T_SNZ - 0.02, "sorpreso", 0.08),
              (T_FALL + 0.5, "ops", 0.15),
              (T_W1 - 0.1, "sorpreso", 0.01), (V["n5"] + 0.4, "ride", 0.2), (T_BUMP - 0.05, "salto", 0.12), (T_BUMP + 0.6, "ride", 0.2),
              (T_BIG, "sorpreso", 0.15), (V["e2"] + 0.2, "ride", 0.2),
              (T_W2 - 0.1, "sorpreso", 0.01), (T_STOP + 0.2, "neutro", 0.25), (T_THROW2 - 0.55, "tiene", 0.2), (T_THROW2 - 0.25, "lancia", 0.12),
              (T_HEAD2 + 0.05, "salto", 0.12), (T_HEAD2 + 0.75, "ride", 0.2), (T_HAT0 + 0.3, "guarda_su", 0.2), (V["s2"] - 0.1, "ride", 0.2),
              (V["n7"] + 0.3, "guarda_su", 0.2), (T_WINK + 0.5, "ride", 0.2)]
             + loop(T_DANCE + 0.1, V["end"] - 0.2, ["ride", "balla", "salto", "balla_m"], 0.5) + loop(V["end"] - 0.2, DUR + 1, ["saluta2_m", "ride", "saluta2", "balla"], 0.6),
    "ele": [(0.0, "neutro", 0.01)] + walk("ele", T_E0, T_E1)
           + [(T_E1, "neutro", 0.2), (T_E1 + 0.12, "soffia", 0.12), (T_NOSE + 0.35, "ride", 0.2), (E("e1") + 0.2, "neutro", 0.25),
              (T_FALL + 0.05, "sorpreso", 0.12),
              (T_W1 - 0.1, "ride", 0.01), (V["n5"] + 0.6, "saluta2", 0.2), (T_BUMP - 0.05, "salto", 0.12), (T_BUMP + 0.6, "ride", 0.2),
              (V["e2"] - 0.15, "indica", 0.15), (E("e2") + 0.2, "ride", 0.2),
              (T_W2 - 0.1, "sorpreso", 0.01), (T_STOP + 0.3, "ride", 0.2), (T_THROW2 + 0.3, "guarda_su", 0.2), (T_HAT1 + 0.2, "ride", 0.2),
              (T_CAR3 - 0.35, "soffia", 0.12), (T_NOSE3 + 0.25, "guarda_su", 0.2), (T_WINK + 0.5, "ride", 0.2)]
           + loop(T_DANCE + 0.2, V["end"] - 0.15, ["balla", "ride", "salto", "saluta2"], 0.5) + loop(V["end"] - 0.15, DUR + 1, ["saluta2", "balla_m", "saluta2_m", "ride"], 0.66),
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
HAS_MOUTH = {"mouse": ("parla_a", "parla_o"), "spike": ("parla_a", "parla_o"), "ele": ("parla_a",)}
ALIAS = {"ele": {"parla_o": "parla_a", "lancia": "saluta2", "fuggi": "sorpreso", "ops": "sorpreso"},
         "spike": {"passa_dx": "cammina_dx", "fuggi": "sorpreso"}, "mouse": {}}
CHS = 0.74
H_CH = {"mouse": 640 * CHS, "spike": 560 * CHS, "ele": 660 * CHS}
CHARS = ["mouse", "spike", "ele"]


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
    if rp(name, prev) != rp(name, pose):
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


# ------------------------------------------------------------------ dove stanno i personaggi
KF = {   # (t, x, y)   S1 collina / S3 villaggio (S2 = sulla slitta, calcolato a parte)
    "mouse": [(0, 274, 1850), (999, 342, 1850)],
    "spike": [(0, 880, 1800), (999, 880, 1800)],
    "ele": [(0, -260, 1715), (T_E0, -260, 1715), (T_E1, ELE1[0], ELE1[1]), (999, ELE1[0], ELE1[1])],
}
POS3 = {"ele": (175.0, 1760.0), "spike": (380.0, 1800.0), "mouse": (905.0, 1785.0)}


def ball1(t):
    """palla grande della S1: (x, raggio, angolo di rotolamento)"""
    u = clamp((t - T_R0) / (T_R1 - T_R0)); v = ease(u) * 0.35 + u * 0.65
    x = lerp(X_B0, BODY[0], v); r = lerp(R_B0, R_B1, v ** 0.8)
    if t > T_R1: r *= 1 + osc(t, T_R1, 0.04, 9, 20)
    return x, r, (x - X_B0) / max(40.0, r) if t >= T_R0 else 0.0


def gait_on(name, t):
    for (n, t0, t1, per) in GAIT:
        if n == name and t0 <= t < t1: return ((t - t0) / per) % 1.0
    return None


def kf_pos(name, t):
    if name == "mouse" and T_R0 <= t <= T_R1 + 0.4:                   # spinge la palla: sempre dietro di lei
        bx, r, _ = ball1(min(t, T_R1)); return bx - r - 110, 1850.0
    kf = KF[name]
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        if t0 <= t <= t1:
            u = (t - t0) / (t1 - t0) if gait_on(name, t) is not None else ease((t - t0) / (t1 - t0))
            return lerp(x0, x1, u), lerp(y0, y1, u)
    return kf[-1][1], kf[-1][2]


# ------------------------------------------------------------------ luce
SUN = {"neve_collina": (0.9, 0.30), "neve_discesa": (0.9, 0.30), "neve_sera": (-0.5, 0.26)}
TINT = {"neve_collina": (1.0, 1.0, 1.02), "neve_discesa": (1.0, 1.0, 1.03), "neve_sera": (0.80, 0.84, 1.02)}
RIM = {"neve_collina": ((255, 248, 230), 0.26), "neve_discesa": ((255, 250, 235), 0.30), "neve_sera": ((255, 190, 110), 0.55)}
RIMDIR = {"neve_collina": (-1, -1), "neve_discesa": (-1, -1), "neve_sera": (1, -1)}
SHCOL = {"neve_collina": (60, 90, 160), "neve_discesa": (60, 90, 160), "neve_sera": (20, 25, 70)}


def cast_shadow(c, r, nw, nh, x, y, sc, k_alpha=0.30):
    shx, k = SUN[c.sid]
    al = np.asarray(r.getchannel("A")).astype(np.float32) / 255
    fy = nh * (MO.AY / MO.CH); fx = nw * (MO.AX / MO.CW); ext = int(nh * 0.45); pad = int(abs(shx) * nh * 0.6) + 40
    M = np.float32([[1, -shx * 0.9, shx * 0.9 * fy + (pad if shx < 0 else 0)], [0, k, fy * (1 - k)]])
    sh = cv2.warpAffine(al, M, (nw + pad, nh + ext), flags=cv2.INTER_LINEAR)
    sh = cv2.GaussianBlur(sh, (0, 0), max(4.0, 11 * c.Z * sc))
    a = (sh * k_alpha * 255).astype(np.uint8)
    lay = Image.new("RGBA", (sh.shape[1], sh.shape[0]), SHCOL[c.sid] + (0,)); lay.putalpha(Image.fromarray(a))
    c.img.paste(lay, (int(c.X(x) - fx - (pad if shx < 0 else 0)), int(c.Y(y) - fy)), lay)


def contact(c, x, y, wsh):
    wsh *= c.Z
    ell = Image.new("RGBA", (int(wsh * 2.4) + 2, int(wsh * 0.7) + 2), (0, 0, 0, 0))
    ImageDraw.Draw(ell).ellipse([wsh * 0.2, wsh * 0.12, wsh * 2.2, wsh * 0.58], fill=SHCOL[c.sid] + (110,))
    ell = ell.filter(ImageFilter.GaussianBlur(max(3, 6 * c.Z))); c.img.paste(ell, (int(c.X(x) - ell.width / 2), int(c.Y(y) - ell.height * 0.5)), ell)


def draw_char(c, name, t, x, y, rot=0.0, layer="ground", sc=CHS, hop=0.0):
    cv, pose = char_canvas(name, t)
    im = Image.fromarray(np.ascontiguousarray(cv), "RGBA")
    A, B, u = pose_state(name, t)
    sq = 1.0; wob = 0.0
    tk = talk(name, t); sq *= 1 + 0.022 * tk; wob += math.sin(t * 11 + len(name)) * 1.3 * tk
    if A == B and A in ("neutro", "guarda_su", "guarda_su_m", "sorpreso", "tiene", "soffia", "ops", "indica", "saluta2"):
        sq *= 1 + 0.012 * math.sin(t * 3.2 + len(name) * 2)
    if A == B and A in ("ride", "balla", "balla_m"): sq *= 1 + 0.03 * math.sin(t * 13 + len(name)); wob += 2.2 * math.sin(t * 9 + len(name))
    g = gait_on(name, t)
    if g is not None:                                                  # passo: rimbalzo e dondolio
        hop += 14 * abs(math.sin(math.pi * 2 * g)); wob += 3.0 * math.sin(math.pi * 2 * g)
    for pose_, t0 in ((e[1], e[0]) for e in EV[name]):
        if pose_ == "salto" and t0 - 0.05 <= t < t0 + 0.6:
            p = clamp((t - (t0 - 0.05)) / 0.62); hop += 4 * p * (1 - p) * 110
            if t < t0 + 0.08: sq *= 1 - 0.07 * clamp((t - (t0 - 0.05)) / 0.13)
            elif p > 0.85: sq *= 1 - 0.06 * math.sin(math.pi * (p - 0.85) / 0.15)
        if pose_ == "fuggi" and t0 - 0.02 <= t < t0 + 0.5:
            p = clamp((t - t0 + 0.02) / 0.52); hop += 4 * p * (1 - p) * 70
        if pose_ in ("neutro", "ride") and t0 > 1.0: sq *= 1 + osc(t, t0 + 0.05, 0.04, 8, 24)
    if name == "spike" and T_SNZ - 0.02 <= t < T_SNZ + 0.5:            # starnuto: scatto all'indietro
        p = clamp((t - T_SNZ) / 0.5); wob += -9 * math.sin(math.pi * p) * (1 - p) * 2; sq *= 1 + 0.06 * math.sin(math.pi * clamp(p * 3))
    rot = rot + wob
    if rot: im = im.rotate(rot, resample=Image.BILINEAR, center=(MO.AX, MO.AY))
    f = c.Z * sc
    nw, nh = max(2, int(MO.CW * f / math.sqrt(sq))), max(2, int(MO.CH * f * sq))
    rr = im.resize((nw, nh), Image.LANCZOS if f < 1 else Image.BICUBIC)
    px, py = c.X(x) - MO.AX * nw / MO.CW, c.Y(y - hop) - MO.AY * nh / MO.CH
    sid = c.sid
    if layer == "ground":
        cast_shadow(c, rr, nw, nh, x, y, sc, 0.26 * clamp(1 - hop / 260))
        contact(c, x, y, H_CH[name] * 0.42 * clamp(1 - hop / 300, 0.4, 1))
    arr = np.asarray(rr).astype(np.float32); a = arr[..., 3] / 255.0
    rgb = arr[..., :3] * np.array(TINT[sid], dtype=np.float32)
    rimc, rimk = RIM[sid]; dx, dy = RIMDIR[sid]
    sg = max(3.0, 8 * f)
    Lb = cv2.GaussianBlur(a, (0, 0), sg)
    Ls = cv2.warpAffine(Lb, np.float32([[1, 0, -dx * sg * 1.1], [0, 1, -dy * sg * 1.1]]), (nw, nh))
    rim = np.clip(a * (1 - Ls * 1.25), 0, 1) ** 1.3
    rgb = rgb + rim[..., None] * np.array(rimc, dtype=np.float32) * rimk
    gy = np.linspace(0, 1, nh, dtype=np.float32)[:, None, None]
    rgb = rgb * (1.03 - 0.10 * gy) + 22 * np.clip((gy - 0.78) / 0.22, 0, 1) * np.array([0.6, 0.8, 1.0], dtype=np.float32)   # luce riflessa dalla neve sui piedi
    out = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), arr[..., 3]]).astype(np.uint8), "RGBA")
    c.img.paste(out, (int(px), int(py)), out)
    return pose


def tip(name, pose, x, y, sc=CHS):
    """punta della proboscide (pixel più a destra della posa 'soffia') in coordinate mondo"""
    a = MO.aligned(name, pose)[..., 3] > 128; ys, xs = np.nonzero(a); i = xs.argmax()
    return x + (xs[i] - MO.AX) * sc, y - (MO.AY - ys[i]) * sc


# ------------------------------------------------------------------ palle di neve, pupazzo, oggetti in volo
_rng = np.random.default_rng(3)
LUMPS = [(float(_rng.uniform(0, 6.283)), float(_rng.uniform(-1.2, 1.2)), float(_rng.uniform(0.05, 0.11))) for _ in range(26)]


def snowball(c, x, ybase, r, ang, tint, squash=1.0, shadow=True):
    """palla di neve 3D: sprite con luce fissa + grumi che girano con la palla (proiezione sferica)"""
    if r < 3: return
    ry = r * squash; rx = r / math.sqrt(squash); cy = ybase - ry
    if shadow:
        contact(c, x + r * 0.15, ybase, r * 0.75)
    spr = sized("snowball", w=2 * rx * c.Z * 1.04, h=2 * ry * c.Z * 1.04)
    spr = tinted(spr, tint) if tint != (1.0, 1.0, 1.0) else spr
    c.img.paste(spr, (int(c.X(x) - spr.width / 2), int(c.Y(cy) - spr.height / 2)), spr)
    for (lon, lat, sz) in LUMPS:                                      # grumi sulla superficie
        ph = lon + ang; cz = math.cos(ph) * math.cos(lat)
        if cz < 0.15: continue
        px = x + rx * 0.92 * math.sin(ph) * math.cos(lat); py = cy - ry * 0.92 * math.sin(lat)
        s = r * sz * c.Z; sh = 0.55 + 0.45 * cz
        lt = 1.0 - 0.18 * (math.sin(ph) * 0.6 + 0.4)
        col = tuple(int(v * lt * t_) for v, t_ in zip((236, 243, 255), tint))
        c.d.ellipse([c.X(px) - s * sh, c.Y(py) - s * 0.8, c.X(px) + s * sh, c.Y(py) + s * 0.8], fill=col + (200,))
        c.d.ellipse([c.X(px) - s * sh * 0.8, c.Y(py) + s * 0.2, c.X(px) + s * sh * 0.8, c.Y(py) + s * 0.75], fill=tuple(int(v * 0.86) for v in col) + (120,))


def coal(c, x, y, r):
    c.d.ellipse([c.X(x) - r * c.Z, c.Y(y) - r * c.Z, c.X(x) + r * c.Z, c.Y(y) + r * c.Z], fill=(34, 32, 40, 255))
    c.d.ellipse([c.X(x - r * 0.35) - r * 0.28 * c.Z, c.Y(y - r * 0.35) - r * 0.28 * c.Z, c.X(x - r * 0.35) + r * 0.28 * c.Z, c.Y(y - r * 0.35) + r * 0.28 * c.Z], fill=(200, 200, 220, 255))


def face(c, x, cy, r, t, t_face, t_wink=None, nose_t=None, nose_from=None, look=0.0, smile=1.0):
    """occhi di carbone, sorriso, naso-carota (che può arrivare in volo)"""
    if t >= t_face:
        k = back(clamp((t - t_face) / 0.3))
        er = r * 0.10 * k; ey = cy - r * 0.22; ex = r * 0.34
        blink = t_wink is not None and t_wink <= t < t_wink + 0.5
        for s in (-1, 1):
            exx = x + s * ex + look * r * 0.05
            if blink and s == 1:                                         # occhiolino: occhio destro chiuso ad arco
                c.d.arc([c.X(exx) - er * 1.3 * c.Z, c.Y(ey) - er * 0.9 * c.Z, c.X(exx) + er * 1.3 * c.Z, c.Y(ey) + er * 1.1 * c.Z], 200, 340,
                        fill=(34, 32, 40, 255), width=max(3, int(er * 0.55 * c.Z)))
            else: coal(c, exx, ey, er)
        for j in range(5):                                               # sorriso di carbone
            a = math.radians(205 + j * 32.5) if False else math.radians(160 - j * 35)
            sx = x + math.cos(a) * r * 0.46; sy = cy + r * 0.12 + math.sin(a) * r * 0.30 * smile
            coal(c, sx, sy, r * 0.055 * k)
    if nose_t is not None and t >= nose_t[0]:
        t0, t1 = nose_t; nx, ny = x + r * 0.02, cy - r * 0.02
        w = r * 0.62
        if t < t1 and nose_from is not None:
            u = clamp((t - t0) / (t1 - t0)); fx, fy = nose_from
            px = lerp(fx, nx, u); py = lerp(fy, ny, u) - 4 * u * (1 - u) * 70; ang = -40 * (1 - u) + 360 * (1 - u) * (1 if nose_from[0] < nx else -1)
        else:
            px, py, ang = nx, ny, 0
            w *= 1 + osc(t, t1, 0.25, 9, 26)
        car = sized("carrot", w=w * c.Z)
        car = tinted(car, TINT[c.sid]) if c.sid == "neve_sera" else car
        paste_c(c, car, px + w * 0.36, py, ang - 8)                     # la punta verso destra, la base sul viso
        if t1 <= t < t1 + 0.6: sparkles(c, nx + w * 0.5, ny, t1, 0.6, n=10, spread=70, rise=20, size=12, seed=4)


def arc_pos(p0, p1, u, h):
    return lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u) - 4 * u * (1 - u) * h


def puff(c, x, y, t0, dur=0.9, n=18, spread=150, size=26, seed=1, col=(250, 252, 255)):
    """sbuffo di neve (atterraggi, starnuto, frenata)"""
    t = c.t
    if not (t0 <= t < t0 + dur): return
    u = (t - t0) / dur
    for k in range(n):
        a = (k * 2.399 + seed) % 6.283; sp = spread * (0.5 + 0.5 * ((k * 0.37 + seed * 0.1) % 1.0))
        px = x + math.cos(a) * sp * (1 - (1 - u) ** 2) * 1.2; py = y - abs(math.sin(a)) * sp * 0.6 * (1 - (1 - u) ** 2) + 120 * u * u
        rr = size * (0.6 + 0.6 * ((k * 0.61) % 1.0)) * (1 + u) * c.Z
        c.d.ellipse([c.X(px) - rr, c.Y(py) - rr, c.X(px) + rr, c.Y(py) + rr], fill=col + (int(210 * (1 - u) ** 1.2),))


def sneeze(c, x, y, t):
    if not (T_SNZ <= t < T_SNZ + 0.7): return
    u = (t - T_SNZ) / 0.7
    for k in range(7):                                                   # linee dello starnuto verso il pupazzo (a sinistra)
        a = math.radians(180 + (k - 3) * 9); d0 = 60 + 260 * u; d1 = d0 + 110
        c.d.line([(c.X(x + math.cos(a) * d0), c.Y(y + math.sin(a) * d0)), (c.X(x + math.cos(a) * d1), c.Y(y + math.sin(a) * d1))],
                 fill=(255, 255, 255, int(240 * (1 - u))), width=max(3, int(7 * c.Z)))
    puff(c, x - 120, y, T_SNZ, 0.7, n=12, spread=160, size=18, seed=7)
    if u < 0.6:
        text(c.d, "ECCIÙ!", c.X(x + 20), c.Y(y - 330), int(120 * c.Z * back(u / 0.25)), (255, 255, 255, 255), (60, 110, 200, 255), int(10 * c.Z))


def head1_state(t):
    """testa della S1: (x, ybase, r, ang, squash) o None"""
    top = BODY[1] - 2 * R_B1 * 0.97
    h0 = (BODY[0], top + 10)
    if t < T_THROW: return None
    if t < T_HEAD:                                                       # in volo dalle mani di Spike
        u = (t - T_THROW) / (T_HEAD - T_THROW); hand = (KF["spike"][0][1] - 20, KF["spike"][0][2] - 330)
        x, y = arc_pos(hand, h0, u, 330); return x, y + R_H, R_H * lerp(0.75, 1, u), -u * 6, 1.0
    if t < T_FALL:
        sq = 1 - 0.18 * math.exp(-10 * (t - T_HEAD)) * math.cos(22 * (t - T_HEAD))
        wob = 0.0
        if t >= T_SNZ: wob = 14 * math.sin(clamp((t - T_SNZ) / 0.12) * math.pi / 2)
        return h0[0] + wob, h0[1], R_H, 0.0, sq
    # cade di lato e rotola via a destra (giù dalla collina), crescendo
    u = t - T_FALL
    if u < 0.45:
        p = u / 0.45; x = lerp(h0[0] + 14, BODY[0] + R_B1 + R_H + 30, p); y = lerp(h0[1], BODY[1], p ** 2)
        return x, y, R_H, p * 2.0, 1.0
    p = u - 0.45; x = BODY[0] + R_B1 + R_H + 30 + 520 * p + 380 * p * p; r = R_H * (1 + 0.25 * p)
    return x, BODY[1] - 6 * abs(math.sin(p * 9)) * math.exp(-p * 2), r, 2.0 + (x - BODY[0]) / r, 1.0


def draw_track(c, t):
    """solco lasciato dalla palla che rotola"""
    if t < T_R0: return
    x1, r, _ = ball1(t)
    pts = []
    for k in range(40):
        u = k / 39; x = lerp(X_B0, x1, u); rr = lerp(R_B0, r, u)
        pts.append((x, rr))
    for x, rr in pts:
        w = rr * 0.55
        c.d.ellipse([c.X(x) - w * c.Z, c.Y(BODY[1] - 6) - 7 * c.Z, c.X(x) + w * c.Z, c.Y(BODY[1] + 8) + 7 * c.Z], fill=(176, 196, 232, 70))


def snowman1(c, t):
    bx, r, ang = ball1(t)
    snowball(c, bx, BODY[1], r, ang, TINT[c.sid])
    if t >= T_HEAD:                                                       # bottoni
        for j in range(3): coal(c, BODY[0] + 2, BODY[1] - r * (1.55 - 0.32 * j), r * 0.07 * back(clamp((t - T_HEAD) / 0.3)))
    hs = head1_state(t)
    if hs:
        x, yb, rh, a, sq = hs
        snowball(c, x, yb, rh, a, TINT[c.sid], sq, shadow=(t >= T_FALL + 0.3))
        if T_HEAD <= t < T_HEAD + 0.8: puff(c, x, yb, T_HEAD, 0.8, n=14, spread=120, size=20, seed=2)
        if t < T_FALL:
            el = ELE1
            face(c, x, yb - rh * sq, rh, t, T_HEAD + 0.15, None, (T_CAR0, T_NOSE), tip("ele", "soffia", el[0], el[1]))
        elif t < T_FALL + 0.45:
            face(c, x, yb - rh, rh, t, T_HEAD + 0.15, None, (T_CAR0, T_NOSE), None)
    if T_FALL + 0.35 <= t < T_FALL + 1.2: puff(c, BODY[0] + R_B1 + 120, BODY[1], T_FALL + 0.35, 0.85, n=16, spread=160, size=22, seed=5)


def carrot_in_trunk(c, t, x, y, t0, t1):
    """carota tenuta in punta alla proboscide prima del lancio"""
    if t0 - 0.25 <= t < t0:
        tx, ty = tip("ele", "soffia", x, y); w = R_H * 0.62
        car = sized("carrot", w=w * c.Z * back(clamp((t - t0 + 0.25) / 0.2)))
        paste_c(c, car, tx + w * 0.30, ty + 6, -8)


def snowman3(c, t):
    """S3: la palla enorme arriva rotolando e si ferma; poi testa nuova, cappello, carota, faccia, occhiolino"""
    tint = TINT[c.sid]
    u = clamp((t - T_W2 + 0.4) / (T_STOP - T_W2 + 0.4))
    x = lerp(-320, BODY3[0], 1 - (1 - u) ** 2.2)
    r = R3 * (1 + osc(t, T_STOP, 0.05, 7, 18))
    alive = 0.0 if t < T_FACE else 1.0
    sway = alive * 3.5 * math.sin((t - T_FACE) * 2.4) * clamp((t - T_FACE) / 0.5)
    snowball(c, x, BODY3[1], r, (x + 320) / R3, tint, 1.0)
    if T_STOP <= t < T_STOP + 0.9: puff(c, x + R3 * 0.8, BODY3[1], T_STOP, 0.9, n=20, spread=200, size=28, seed=8)
    if t >= T_HEAD2 - 0.02 and t >= T_FACE:
        for j in range(3): coal(c, BODY3[0] + sway * 0.5, BODY3[1] - R3 * (1.55 - 0.33 * j), R3 * 0.07 * back(clamp((t - T_FACE) / 0.3)))
    top = BODY3[1] - 2 * R3 * 0.97 + 12
    if t >= T_THROW2:
        if t < T_HEAD2:
            p = (t - T_THROW2) / (T_HEAD2 - T_THROW2); hand = (POS3["spike"][0] + 10, POS3["spike"][1] - 330)
            hx, hy = arc_pos(hand, (BODY3[0], top), p, 520); sq = 1.0; rh = R3H * lerp(0.7, 1, p)
        else:
            hx, hy, rh = BODY3[0] + sway, top, R3H; sq = 1 - 0.18 * math.exp(-10 * (t - T_HEAD2)) * math.cos(22 * (t - T_HEAD2))
        snowball(c, hx, hy + rh * (1 if t < T_HEAD2 else 0), rh, -(t - T_THROW2) * 3 if t < T_HEAD2 else 0, tint, sq, shadow=False)
        if t >= T_HEAD2:
            if t < T_HEAD2 + 0.8: puff(c, hx, hy, T_HEAD2, 0.8, n=14, spread=140, size=22, seed=3)
            cy = hy - R3H * sq
            el = POS3["ele"]
            face(c, hx, cy, R3H, t, T_FACE, T_WINK, (T_CAR3, T_NOSE3), tip("ele", "soffia", el[0], el[1]), smile=1.0)
            if t >= T_HAT0: hat(c, t, hx, cy - R3H * 0.82, sway)
    if T_FACE <= t < T_FACE + 1.4: sparkles(c, BODY3[0], BODY3[1] - R3 * 2.2, T_FACE, 1.4, n=26, spread=330, rise=60, size=22, seed=6)
    if T_WINK <= t < T_WINK + 0.8: sparkles(c, BODY3[0] + R3H * 0.6, top - R3H * 1.2, T_WINK, 0.8, n=8, spread=60, rise=20, size=26, seed=9)


def hat(c, t, hx, hy, sway):
    """secchiello-cappello lanciato dal topolino"""
    w = R3H * 1.25
    if t < T_HAT1:
        p = (t - T_HAT0) / (T_HAT1 - T_HAT0); hand = (POS3["mouse"][0] - 40, POS3["mouse"][1] - 420)
        x, y = arc_pos(hand, (hx, hy), p, 380); ang = 180 + 540 * (1 - p) if False else 360 * 1.5 * (1 - ease(p)) + 180
    else:
        x, y = hx, hy; ang = 180 + osc(t, T_HAT1, 12, 8, 20) - sway
    im = sized("bucket", w=w * c.Z)
    im = tinted(im, TINT[c.sid]) if c.sid == "neve_sera" else im
    paste_c(c, im, x, y - w * 0.18, ang)                                   # capovolto: il secchiello diventa un cappello
    if T_HAT1 <= t < T_HAT1 + 0.7: sparkles(c, hx, hy - 40, T_HAT1, 0.7, n=10, spread=90, rise=30, size=14, seed=11)


# ------------------------------------------------------------------ discesa (S2)
SLED = (470.0, 1560.0); SLED_W = 860.0
SLOPE = -7.0                                                              # gradi (scende verso destra)
SEAT = {"ele": -255.0, "spike": -45.0, "mouse": 175.0}


def sled_state(t):
    bump = 0.0
    if T_BUMP - 0.1 <= t < T_BUMP + 0.75:
        p = (t - T_BUMP + 0.1) / 0.85; bump = 4 * p * (1 - p) * 120
    jit = 6 * math.sin(t * 17) + 4 * math.sin(t * 29 + 1)
    y = SLED[1] - bump + jit * (0.3 if bump else 1)
    x = SLED[0] + 18 * math.sin(t * 1.3)
    ang = SLOPE + 2.2 * math.sin(t * 6.1) + (7 * math.sin(math.pi * clamp((t - T_BUMP + 0.1) / 0.85)) if bump else 0)
    return x, y, ang, bump


def sled_pt(st, lx, ly):
    x, y, ang, _ = st; a = math.radians(-ang); ca, sa = math.cos(a), math.sin(a)
    return x + lx * ca - ly * sa, y + lx * sa + ly * ca


def pine_layer(c, t, depth, n, ybase, scale, speed, blur, seed, front=False):
    rng = np.random.default_rng(seed); span = 1700
    for k in range(n):
        x0 = rng.uniform(0, span); s = scale * rng.uniform(0.8, 1.2)
        x = (x0 - (t - T_W1) * speed) % span - 300
        y = ybase + rng.uniform(-30, 30) + (x - 540) * math.tan(math.radians(-SLOPE)) * depth
        h_ = 900 * s
        im = sized("pine", h=h_ * c.Z)
        if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
        tint = (0.93, 0.97, 1.05) if not front else (0.75, 0.80, 0.95)
        im = tinted(im, tint)
        if not front:                                                    # foschia in lontananza
            a = np.asarray(im).astype(np.float32); hz = 1 - depth
            a[..., :3] = a[..., :3] * (1 - 0.35 * hz) + np.array([215, 230, 250], np.float32) * 0.35 * hz
            im = Image.fromarray(a.astype(np.uint8), "RGBA")
        c.img.paste(im, (int(c.X(x) - im.width / 2), int(c.Y(y) - im.height)), im)


def slope_snow(c, t):
    """pista innevata in primo piano (inclinata) che scorre"""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    def yl(x): return 1600 + (x - 540) * math.tan(math.radians(-SLOPE))
    ld.polygon([(c.X(-100), c.Y(yl(-100))), (c.X(1200), c.Y(yl(1200))), (c.X(1200), c.Y(2300)), (c.X(-100), c.Y(2300))], fill=(240, 246, 255, 255))
    for k in range(14):                                                  # gobbe e righe della pista che scorrono
        x = (k * 160 - (t - T_W1) * 1500) % 1800 - 300; yy = yl(x) + 70 + (k % 4) * 60
        ld.ellipse([c.X(x) - 180 * c.Z, c.Y(yy) - 14 * c.Z, c.X(x) + 180 * c.Z, c.Y(yy) + 14 * c.Z], fill=(200, 218, 245, 160))
    lay = lay.filter(ImageFilter.GaussianBlur(3)); c.img.paste(lay, (0, 0), lay)


def spray(c, t, st):
    """scia di neve dietro la slitta"""
    bx, by = sled_pt(st, -SLED_W * 0.48, 40)
    for k in range(40):
        ph = (t * 2.2 + k * 0.025) % 1.0
        x = bx - 700 * ph - 60 * ((k * 7) % 5) / 5; y = by - 260 * math.sin(math.pi * ph * 0.8) * (0.4 + 0.6 * ((k * 13) % 7) / 7) + 60 * ph
        rr = (6 + 20 * ph) * c.Z * (0.6 + 0.4 * ((k * 3) % 4) / 4)
        c.d.ellipse([c.X(x) - rr, c.Y(y) - rr, c.X(x) + rr, c.Y(y) + rr], fill=(255, 255, 255, int(220 * (1 - ph))))


def speed_lines(c, t, amt):
    if amt <= 0: return
    rng = np.random.default_rng(5)
    for k in range(30):
        y = rng.uniform(100, 1800); sp = rng.uniform(1800, 3200); ph = (t * sp / 2600 + rng.uniform(0, 1)) % 1.0; x = 1300 - ph * 1700
        ln = rng.uniform(140, 320)
        c.d.line([(x, y), (x + ln, y - ln * 0.12)], fill=(255, 255, 255, int(110 * amt)), width=int(rng.uniform(2, 5)))


def ball2(t):
    """la testa che rotola davanti alla slitta e diventa enorme"""
    g = clamp((t - V["n5"]) / max(0.5, T_BIG + 0.6 - V["n5"]))
    r = lerp(R_H * 1.5, 235, ease(g) ** 1.2) * (1 + osc(t, T_BIG, 0.06, 6, 16))
    x = 1010 - 120 * ease(g) + 20 * math.sin(t * 2.0)
    y = 1600 + (x - 540) * math.tan(math.radians(-SLOPE)) + 30 - 18 * abs(math.sin(t * 5.3))
    return x, y, r, t * 9.0


# ------------------------------------------------------------------ neve che cade
_fr = np.random.default_rng(21)
FLAKES = [(float(_fr.uniform(0, 1200)), float(_fr.uniform(0, 2100)), float(_fr.choice([0.35, 0.6, 1.0, 1.7], p=[.4, .3, .2, .1])), float(_fr.uniform(0, 6.28))) for _ in range(240)]


def snowfall(c, t, layer):
    """layer 0: lontana, 1: media, 2: davanti (grande e sfocata)"""
    sid = c.sid; wind = 0.0 if sid != "neve_discesa" else 1.0
    lay = None
    for (x0, y0, d, ph) in FLAKES:
        L = 0 if d < 0.5 else (1 if d < 1.2 else 2)
        if L != layer: continue
        if sid == "neve_sera" and L == 2 and ((x0 * 7) % 3) < 1.5: continue
        sp = 90 + 110 * d
        y = (y0 + t * sp) % 2100 - 90
        x = (x0 + 40 * math.sin(t * 0.9 + ph) * d - wind * t * 900 * d) % 1200 - 60
        rr = (2.4 + 3.6 * d) * (1.4 if L == 2 else 1.0)
        if L == 2:
            if lay is None: lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
            ld.ellipse([x - rr * 1.8, y - rr * 1.8, x + rr * 1.8, y + rr * 1.8], fill=(255, 255, 255, 150))
        else:
            a = int(170 + 70 * d / 1.2)
            if wind: c.d.line([(x, y), (x + 26 * d, y - 4 * d)], fill=(255, 255, 255, a), width=max(2, int(rr * 0.9)))
            else: c.d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(255, 255, 255, a))
    if lay is not None:
        lay = lay.filter(ImageFilter.GaussianBlur(3.5)); c.img.paste(lay, (0, 0), lay)


# ------------------------------------------------------------------ sfondi
_bg = {}
def bg_arr(sid):
    if sid not in _bg:
        _bg[sid] = np.asarray(Image.open(os.path.join(HERE, "assets", "amb", sid + ".png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.8))).astype(np.float32)
    return _bg[sid]


_warm = {}
def warm_mask():
    """finestre e lucine del villaggio (pixel caldi e luminosi) -> tremolano"""
    if "m" not in _warm:
        a = bg_arr("neve_sera"); r, g, b = a[..., 0], a[..., 1], a[..., 2]
        m = np.clip((r - b - 40) / 80, 0, 1) * np.clip((r + g - 300) / 120, 0, 1) * (np.arange(H)[:, None] < 1250)
        m = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 2.0)
        _warm["m"] = m; _warm["blob"] = cv2.GaussianBlur(m, (0, 0), 18)
        ys, xs = np.nonzero(m > 0.6); _warm["pts"] = list(zip(xs[::97], ys[::97]))
    return _warm


_grid = None
def background(sid, t):
    global _grid
    if _grid is None: _grid = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    xs, ys = _grid; arr = bg_arr(sid)
    if sid == "neve_collina":
        dx = 4 * np.sin(0.4 * t + ys * 0.004) * np.clip(1 - ys / 900, 0, 1)            # nuvole e fumo del comignolo che si muovono
        out = cv2.remap(arr, (xs + dx).astype(np.float32), ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    elif sid == "neve_discesa":
        z = 1.0 + 0.05 * clamp((t - T_W1) / (T_W2 - T_W1))                              # si avvicina alla valle
        out = cv2.remap(arr, ((xs - 540) / z + 540).astype(np.float32), ((ys - 700) / z + 700).astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    else:
        wm = warm_mask(); fl = 1 + 0.18 * np.sin(t * 3.1 + xs * 0.05) * np.sin(t * 1.7 + ys * 0.03)
        out = arr * (1 + (fl - 1)[..., None] * wm["m"][..., None] * 1.5)
        out = out + wm["blob"][..., None] * np.array([90, 50, 10], np.float32) * (0.75 + 0.25 * math.sin(t * 2.3))
    return np.clip(out, 0, 255).astype(np.uint8)


def wipe(c, t):
    """sbuffo di neve che copre tutto lo schermo per un istante (cambio ambiente)"""
    for tw in WIPES:
        if abs(t - tw) > 0.8: continue
        u = t - tw; cover = ease(1 - abs(u) / 0.75) if abs(u) < 0.75 else 0.0
        rng = np.random.default_rng(int(tw * 10))
        for k in range(36):
            gx = rng.uniform(-150, 1230); gy = rng.uniform(-100, 2000); rr = rng.uniform(170, 330)
            x = gx + u * 1400 * (0.7 + 0.5 * ((k * 37) % 10) / 10)
            a = int(255 * clamp(cover * 1.3))
            c.d.ellipse([x - rr, gy - rr * 0.8, x + rr, gy + rr * 0.8], fill=(246, 250, 255, a))
        if cover > 0.5:
            wash = Image.new("RGBA", (W, H), (244, 248, 255, int(235 * clamp((cover - 0.5) / 0.4)))); c.img.paste(wash, (0, 0), wash)


def moon_glow(c, t):
    if c.sid != "neve_sera": return
    glow_blob(c, 540, 300, 320, (60, 60, 80), 0.8 + 0.2 * math.sin(t * 1.2))
    rng = np.random.default_rng(9)
    for k in range(30):
        x = rng.uniform(20, 1060); y = rng.uniform(20, 700); ph = rng.uniform(0, 6.28); sp = rng.uniform(1.0, 2.4)
        a = 0.3 + 0.7 * max(0.0, math.sin(t * sp + ph)) ** 2
        star4(c.gd, c.X(x), c.Y(y), (3 + 4 * rng.random()) * c.Z * (0.6 + a), tuple(int(230 * a) for _ in range(3))); c.glow_used = True
    wm = warm_mask()
    for k, (x, y) in enumerate(wm["pts"][:40]):                         # lucine che pulsano
        a = 0.5 + 0.5 * math.sin(t * 2.6 + k * 1.3)
        if a > 0.6: star4(c.gd, c.X(x), c.Y(y), 7 * c.Z * a, (int(120 * a), int(90 * a), int(30 * a))); c.glow_used = True


def sun_glow(c, t):
    if c.sid != "neve_collina": return
    glow_blob(c, 860, 180, 360, (70, 64, 40), 0.85 + 0.15 * math.sin(t * 1.1))
    for k in range(18):                                                  # neve che luccica al sole
        rng = np.random.default_rng(100 + k); x = rng.uniform(40, 1040); y = rng.uniform(1300, 1900)
        a = max(0.0, math.sin(t * rng.uniform(2, 4) + k)) ** 6
        if a > 0.05: star4(c.gd, c.X(x), c.Y(y), 9 * c.Z * a, (int(255 * a), int(255 * a), int(255 * a))); c.glow_used = True


# ------------------------------------------------------------------ camera
CAM = [  # (t, cx, cy, z)
    (0.0, 545, 1420, 1.1), (1.0, 550, 1400, 1.08), (T_R0, 555, 1360, 1.05), (T_R1, 540, 1330, 1.0), (V["t1"] + 0.4, 420, 1480, 1.25),
    (V["n2"] + 0.3, 600, 1300, 1.04), (T_HEAD + 0.3, 600, 1350, 1.08), (V["n3"] + 0.2, 470, 1350, 1.05), (T_NOSE, 420, 1380, 1.22),
    (E("e1") + 0.2, 560, 1300, 1.05), (T_SNZ - 0.2, 760, 1420, 1.3), (T_FALL + 0.3, 760, 1380, 1.15), (V["t2"] - 0.1, 560, 1300, 1.02),
    (T_W1 - 0.01, 560, 1300, 1.0), (T_W1, 540, 1250, 1.05), (V["n5"] + 1.0, 560, 1300, 1.0), (T_BIG, 700, 1350, 1.08),
    (V["e2"] - 0.1, 400, 1380, 1.18), (T_W2 - 0.01, 540, 1300, 1.05),
    (T_W2, 540, 1300, 1.0), (T_STOP + 0.4, 540, 1300, 1.0), (T_THROW2 + 0.2, 560, 1280, 1.02), (T_HAT1 + 0.4, 600, 1180, 1.12),
    (T_FACE, 600, 1150, 1.2), (T_WINK + 0.6, 600, 1180, 1.25), (V["t3"] + 0.9, 540, 1300, 1.0), (DUR, 540, 1300, 1.0),
]
SHAKES = [(T_HEAD, 8), (T_FALL + 0.4, 12), (T_BUMP + 0.6, 16), (T_STOP, 18), (T_HEAD2, 8)]


def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 5 * math.sin(t * 0.8) + 3 * math.sin(t * 2.3); cy += 4 * math.sin(t * 1.1 + 1)
    for kt, amp in SHAKES:
        if kt <= t < kt + 0.4:
            k = (1 - (t - kt) / 0.4) * amp; cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    if T_W1 < t < T_W2: cx += 3 * math.sin(t * 31); cy += 3 * math.cos(t * 27)
    z = max(1.0, z); hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


# ------------------------------------------------------------------ fotogramma
def scene_at(t):
    cur = SCENES[0][0]
    for sid, t0 in SCENES:
        if t >= t0: cur = sid
    return cur


def scene_img(sid, t, cx, cy, Z):
    arr = background(sid, t)
    box = (cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z)
    img = Image.fromarray(arr).resize((W, H), Image.BICUBIC, box=box).filter(ImageFilter.GaussianBlur(0.4 + 0.8 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z; c.sid = sid
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    sun_glow(c, t); moon_glow(c, t)
    snowfall(c, t, 0)
    if sid == "neve_collina":
        draw_track(c, t)
        items = []
        for n in CHARS:
            x, y = kf_pos(n, t)
            if -400 < x < 1500: items.append((y, "char", n, x))
        items.append((BODY[1] - 1, "snowman", None, None))
        if t >= V["t2"] + 0.1: items.append((1745, "sled", None, None))
        for y, kind, n, x in sorted(items, key=lambda q: q[0]):
            if kind == "snowman": snowman1(c, t)
            elif kind == "sled":                                               # la slitta arriva scivolando
                p = clamp((t - V["t2"] - 0.1) / 0.8); sx_ = lerp(-420, 470, 1 - (1 - p) ** 2.5)
                contact(c, sx_, 1830, SLED_W * 0.28)
                paste_c(c, sized("sled", w=SLED_W * 0.6 * c.Z), sx_, 1745, osc(t, V["t2"] + 0.9, 4, 6, 14))
                if p < 1: puff(c, sx_ - 260, 1820, V["t2"] + 0.1, 0.9, n=12, spread=110, size=18, seed=12)
            else:
                draw_char(c, n, t, x, y)
                if n == "ele": carrot_in_trunk(c, t, x, y, T_CAR0, T_NOSE)
        sneeze(c, KF["spike"][0][1] - 60, KF["spike"][0][2] - 300, t)
        snowfall(c, t, 1)
    elif sid == "neve_discesa":
        pine_layer(c, t, 0.35, 9, 1180, 0.38, 420, 2.0, 1)
        pine_layer(c, t, 0.6, 7, 1330, 0.62, 900, 1.0, 2)
        slope_snow(c, t)
        snowfall(c, t, 1)
        st = sled_state(t)
        x2, y2, r2, a2 = ball2(t)
        snowball(c, x2, y2, r2, a2, TINT[sid])
        puff(c, x2 - r2 * 0.6, y2, math.floor(t * 2.5) / 2.5, 0.4, n=8, spread=90, size=16, seed=int(t * 2.5))
        spray(c, t, st)
        sx, sy, ang, bump = st
        contact(c, sx, 1600 + (sx - 540) * math.tan(math.radians(-SLOPE)) + 50, SLED_W * 0.45 * clamp(1 - bump / 250, 0.5, 1))
        for n in ("ele", "spike", "mouse"):
            px, py = sled_pt(st, SEAT[n], 78)
            draw_char(c, n, t, px, py, rot=-ang * 0.6, layer="sled")
        sl = sized("sled", w=SLED_W * c.Z)
        paste_c(c, sl, *sled_pt(st, 0, 60), ang)
        speed_lines(c, t, clamp((t - T_W1) / 0.6) * clamp((T_W2 - t) / 0.6))
    else:
        items = [(BODY3[1] - 1, "snowman", None)] + [(POS3[n][1], "char", n) for n in CHARS]
        for y, kind, n in sorted(items, key=lambda q: q[0]):
            if kind == "snowman": snowman3(c, t)
            else:
                x, yy = POS3[n]
                if t < T_STOP + 0.3:                                       # scendono dalla slitta e si sistemano
                    p = clamp((t - T_W2 + 0.2) / (T_STOP + 0.3 - T_W2 + 0.2)); x = lerp(x - 260, x, ease(p))
                draw_char(c, n, t, x, yy)
                if n == "ele": carrot_in_trunk(c, t, x, yy, T_CAR3, T_NOSE3)
        snowfall(c, t, 1)
    snowfall(c, t, 2)
    wipe(c, t)
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); img = ImageChops.add(ImageChops.add(c.img, c.glow), g2)
    else: img = c.img
    return img


def vignette():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.70)) ** 2)
    return np.clip(1 - 0.26 * np.clip(r - 0.45, 0, 1) ** 1.6, 0.6, 1)[..., None].astype(np.float32)
_VIG = None
GRADE = {"neve_collina": (255, 250, 244), "neve_discesa": (250, 252, 255), "neve_sera": (236, 238, 255)}


def frame(i):
    global _VIG
    if _VIG is None: _VIG = vignette()
    t = i / FPS; cx, cy, Z = camera(t)
    sid = scene_at(t)
    img = scene_img(sid, t, cx, cy, Z)
    arr = np.asarray(img).astype(np.float32)
    bright = np.clip(arr - 220, 0, 255) * 3.0                              # bloom leggero + grana di pellicola
    arr = arr + cv2.resize(cv2.GaussianBlur(cv2.resize(bright, (W // 4, H // 4), interpolation=cv2.INTER_AREA), (0, 0), 3.5), (W, H)) * 0.18
    arr = arr * 0.70 + np.asarray(ImageChops.multiply(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)), Image.new("RGB", (W, H), GRADE[sid]))).astype(np.float32) * 0.30
    rng = np.random.default_rng(i)
    arr = arr + rng.normal(0, 2.0, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    img = Image.fromarray(np.clip(arr * _VIG, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img, "RGBA")
    if t < 2.4:                                                          # HOOK
        u = back(t / 0.35); a = int(255 * clamp((2.4 - t) / 0.4))
        text(d, "NEVICA!", W / 2, 240 - 10 * math.sin(t * 6), int(190 * clamp(max(0.6, u), 0, 1.0)), (255, 255, 255, a), (40, 90, 190, a), 14)
    for k, t0, who, txt, dur in VOICES:                                  # sottotitoli
        if t0 - 0.05 <= t <= t0 + dur + 0.3:
            u = ease((t - t0 + 0.05) / 0.18); size = 66 if who == "narr" else 78; f = ImageFont.truetype(FONT, size); lines = []; cur = ""
            for wd in txt.split():
                tl_ = (cur + " " + wd).strip(); bb = d.textbbox((0, 0), tl_, font=f, anchor="mm", stroke_width=6)
                if bb[2] - bb[0] > 930 and cur: lines.append(cur); cur = wd
                else: cur = tl_
            lines.append(cur); yy = (330 if k == "end" else (560 if t >= T_W2 else 1850 - 84 * (len(lines) - 1))) + (1 - u) * 14
            for ln in lines: text(d, ln, W / 2, yy, size, COL[who] + (int(255 * u),), (30, 40, 70, int(255 * u)), 7); yy += 84
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
        print({k: round(v, 2) for k, v in dict(T_R0=T_R0, T_R1=T_R1, T_THROW=T_THROW, T_E1=T_E1, T_NOSE=T_NOSE, T_SNZ=T_SNZ, T_W1=T_W1, T_BUMP=T_BUMP,
                                                     T_BIG=T_BIG, T_W2=T_W2, T_STOP=T_STOP, T_THROW2=T_THROW2, T_HAT0=T_HAT0, T_CAR3=T_CAR3, T_FACE=T_FACE, T_WINK=T_WINK).items()})
    elif cmd == "prep":
        import time
        t0 = time.time(); ps = precompute(); print(len(ps), "transizioni")
        with Pool(4) as pool:
            for r in pool.imap_unordered(_prep, ps):
                if r: print("manca", r)
        print("fatto in", round(time.time() - t0), "s")
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(round(float(ts) * FPS)))).save(f"/tmp/claude-0/prova/test_n_{ts}.png")
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
