#!/usr/bin/env python3
"""Short 'Nascondino nel bosco d'autunno' (9:16, 1080x1920, 30 fps): la volpe (nuova amica), Spike, l'elefantino e il topolino (sorpresa finale).
Diverso dagli altri: UN solo ambiente esplorato dalla camera, gioco INTERATTIVO ('Lo vedi anche tu?' con pausa per cercare e indizi
che si muovono), foglie che cadono e che esplodono, finale a sorpresa (il topolino esce dal mucchio).
Riusa il motore di short_razzo.py (corpo vivo, pose con morph, bocca, luce): qui si cambiano solo copione, posizioni e regia.
    python3 short_nascondino.py info | prep | test 1.0 5.5 | renderpart a b out.mp4 | render muto.mp4
"""
import json, math, os, subprocess, sys
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import morph as MO
import short_razzo as R
from short_razzo import lerp, clamp, ease, back, osc, text, sparkles, glow_blob, paste_c, puff, subscribe_button, sized, Ctx

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
AUD = "audioK"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))
WD = json.load(open(os.path.join(HERE, AUD, "parole.json")))

V = {}
def _seq():
    t = 0.0
    def at(k, gap):
        nonlocal t
        V[k] = t + gap; t = V[k] + D[k]
    at("n1", 0.5); at("v1", 0.3); at("n2", 0.5); at("v2", 1.9); at("s1", 0.1); at("n3", 0.6); at("v3", 1.8); at("e1", 0.1)
    at("n4", 0.6); at("s2", 1.0); at("n5", 0.9); at("end", 1.1)
    return t + 2.8
DUR = _seq()
SAY = {"n1": "narr", "v1": "volpe", "n2": "narr", "v2": "volpe", "s1": "spike", "n3": "narr", "v3": "volpe", "e1": "ele",
       "n4": "narr", "s2": "spike", "n5": "narr", "end": "mouse"}
VOICES = [(k, V[k], SAY[k], D[k]) for k in V]
E = lambda k: V[k] + D[k]


def word(k, w, frac=0.5):
    for (ww, a, b) in WD.get(k, []):
        if w.lower() in ww.lower(): return V[k] + a
    return V[k] + D[k] * frac


# ------------------------------------------------------------------ eventi
T_HIDE_S = V["v1"] + 0.15                      # Spike si tuffa nel mucchio
T_HIDE_E0 = V["v1"] + 0.4; T_HIDE_E1 = T_HIDE_E0 + 1.6   # l'elefantino va dietro il cespuglio
T_LOOK1 = word("n2", "Lo") - 0.2               # indizi: il mucchio si muove
T_FOUND1 = V["v2"] + 0.05                       # Spike salta fuori
T_LOOK2 = word("n3", "dietro") - 0.6
T_FOUND2 = V["e1"] - 0.2                        # l'elefantino esce
T_JUMP = word("n4", "tutti") + 0.1              # tutti nel mucchio grande
T_BOOM = T_JUMP + 0.75                          # esplosione di foglie
T_MOUSE = word("n5", "sotto") + 0.35            # sorpresa: il topolino esce dal mucchio piccolo
WIDE = (540.0, 1300.0, 1.04)

# posizioni (mondo)
PILE1 = (250.0, 1660.0, 470.0)                  # mucchio piccolo (x, base, larghezza)
BUSH = (850.0, 1690.0, 640.0)
TREE = (860.0, 1650.0, 1250.0)
PILE2 = (560.0, 1560.0, 760.0)                  # mucchio grande dietro, al centro
POS0 = {"volpe": (560.0, 1840.0), "spike": (300.0, 1790.0), "ele": (820.0, 1800.0), "mouse": (560.0, 1600.0)}
POS_HID = {"spike": (250.0, 1655.0), "ele": (850.0, 1650.0)}
POS_OUT = {"spike": (330.0, 1800.0), "ele": (700.0, 1820.0), "volpe": (540.0, 1850.0)}


# ------------------------------------------------------------------ pose
def loop(t0, t1, seq, beat=0.5):
    ev = []; i = 0
    while t0 + i * beat < t1:
        ev.append((t0 + i * beat, seq[i % len(seq)], beat * 0.85)); i += 1
    return ev


def walk(t0, t1, per=0.6):
    pl = ["cammina_dx", "passa_dx", "cammina_dx_m", "passa_dx"]; q = per / 4
    return [(t0 + i * q, pl[i % 4], q) for i in range(int((t1 - t0) / q))]


EV = {
    "volpe": [(0.0, "salto", 0.01)] + loop(V["v1"], E("v1"), ["salto_m", "salto"], 0.6) + [(E("v1"), "salto", 0.1), (T_FOUND1 - 0.6, "salto_m", 0.1),
              (T_FOUND1 + 0.4, "salto", 0.1), (T_FOUND2 - 0.6, "salto_m", 0.1), (T_FOUND2 + 0.4, "salto", 0.1)] + loop(T_MOUSE + 1.0, DUR + 1, ["salto", "salto_m"], 0.7),
    "spike": [(0.0, "saluta2", 0.01), (V["n1"] + 1.4, "ride", 0.2), (T_HIDE_S - 0.15, "salto", 0.12), (T_HIDE_S + 0.6, "sbircia", 0.2),
              (T_FOUND1, "salto", 0.12), (T_FOUND1 + 0.75, "ops", 0.15), (E("s1") + 0.3, "ride", 0.2), (T_FOUND2 + 0.3, "ride", 0.2),
              (T_JUMP - 0.2, "salto", 0.12), (T_BOOM + 0.1, "ride", 0.2), (V["s2"] - 0.1, "salto", 0.12), (E("s2") + 0.3, "ride", 0.2),
              (T_MOUSE - 0.1, "sorpreso", 0.12)] + loop(T_MOUSE + 1.0, DUR + 1, ["saluta2", "ride", "saluta2_m", "balla"], 0.6),
    "ele": [(0.0, "saluta2", 0.01), (V["n1"] + 1.6, "ride", 0.2)] + walk(T_HIDE_E0, T_HIDE_E1)
           + [(T_HIDE_E1, "sorpreso", 0.15), (T_LOOK2, "ride", 0.2), (T_FOUND2, "salto", 0.12), (T_FOUND2 + 0.7, "ride", 0.2), (E("e1") + 0.2, "saluta2", 0.2),
              (T_JUMP - 0.15, "salto", 0.12), (T_BOOM + 0.1, "ride", 0.2), (T_MOUSE - 0.1, "sorpreso", 0.12)]
           + loop(T_MOUSE + 1.1, DUR + 1, ["ride", "saluta2", "balla", "saluta2"], 0.62),
    "mouse": [(0.0, "salto", 0.01), (T_MOUSE + 0.75, "ride", 0.2), (V["end"] - 0.1, "saluta2", 0.2)]
             + loop(V["end"] + 1.0, DUR + 1, ["saluta2_m", "balla", "saluta2", "ride"], 0.6),
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
JUMPS = {   # (inizio, durata, altezza): saltelli continui della volpe + salti di gioco
    "volpe": [(V["n1"] + 0.1 + 0.62 * i, 0.6, 60) for i in range(5)] + [(T_FOUND1 - 0.55, 0.6, 200), (T_FOUND2 - 0.5, 0.6, 200)]
             + [(T_BOOM + 0.05, 0.6, 260)] + [(T_MOUSE + 1.0 + 0.7 * i, 0.65, 90) for i in range(9)],
    "spike": [], "ele": [], "mouse": [(T_MOUSE, 0.75, 330)],
}

R.AUD = AUD; R.VOICES = VOICES; R.EV = EV; R.JUMPS = JUMPS
R.H_CH = {"mouse": 640.0, "spike": 560.0, "ele": 660.0, "volpe": 600.0}
SID = "bosco_autunno"
R.TINT[SID] = (1.04, 0.98, 0.92); R.RIM[SID] = ((255, 200, 120), 0.45); R.RIMDIR[SID] = (1, -1); R.SHCOL[SID] = (60, 30, 10)
R.SUN[SID] = (0.6, 0.3)
R.HAS_MOUTH = {"mouse": 1, "spike": 1, "ele": 1, "volpe": 0}


def precompute():
    pairs = set()
    for name, ev in EV.items():
        for a, b in zip(ev, ev[1:]):
            if a[1] != b[1]: pairs.add((name, a[1], b[1]))
        if name != "volpe":
            for p in ("parla_a", "parla_o"): pairs.add((name, "neutro", p)); pairs.add((name, p, "neutro"))
    return sorted(pairs)


# ------------------------------------------------------------------ ambiente
_bg = None
def bg_arr():
    global _bg
    if _bg is None:
        _bg = np.asarray(Image.open(os.path.join(HERE, "assets", "amb", SID + ".png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)
    return _bg


_grid = None
def background(t):
    global _grid
    if _grid is None: _grid = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    xs, ys = _grid
    dx = 4 * np.sin(0.7 * t + ys * 0.006 + xs * 0.002) * np.clip((1100 - ys) / 900, 0, 1)        # chiome nel vento
    return cv2.remap(bg_arr(), (xs + dx).astype(np.float32), ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT).astype(np.uint8)


_tree = None
def autumn_tree(h):
    global _tree
    if _tree is None:
        im = R.load("tree"); a = np.asarray(im).copy()
        hsv = cv2.cvtColor(a[..., :3], cv2.COLOR_RGB2HSV).astype(np.float32)
        m = ((hsv[..., 0] > 25) & (hsv[..., 0] < 95)).astype(np.float32)
        hsv[..., 0] = hsv[..., 0] * (1 - m) + (10 + (hsv[..., 0] - 25) / 70 * 14) * m
        a[..., :3] = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)
        _tree = Image.fromarray(a, "RGBA")
    return _tree.resize((int(_tree.width * h / _tree.height), int(h)), Image.LANCZOS)


_bush = {}
def autumn_bush(w):
    k = int(w)
    if k not in _bush:
        im = sized("bush", w=w); a = np.asarray(im).copy()
        hsv = cv2.cvtColor(a[..., :3], cv2.COLOR_RGB2HSV).astype(np.float32)
        m = ((hsv[..., 0] > 25) & (hsv[..., 0] < 95)).astype(np.float32)
        hsv[..., 0] = hsv[..., 0] * (1 - m) + (8 + (hsv[..., 0] - 25) / 70 * 16) * m
        hsv[..., 1] = hsv[..., 1] * (1 - 0.15 * m)
        a[..., :3] = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)
        _bush[k] = Image.fromarray(a, "RGBA")
        if len(_bush) > 30: _bush.pop(next(iter(_bush)))
    return _bush[k]


LEAF_COL = [(235, 120, 30), (220, 70, 30), (245, 180, 40), (200, 90, 20), (250, 150, 50)]


def leaf(c, x, y, s, ang, col, flip=1.0, a=255):
    s *= c.Z; ca, sa = math.cos(ang), math.sin(ang)
    pts = []
    for i in range(10):
        u = i / 10 * 6.283; px = math.cos(u) * s; py = math.sin(u) * s * 0.55 * flip
        pts.append((c.X(x) + px * ca - py * sa, c.Y(y) + px * sa + py * ca))
    c.d.polygon(pts, fill=col + (a,))
    c.d.line([(c.X(x) - s * ca, c.Y(y) - s * sa), (c.X(x) + s * ca, c.Y(y) + s * sa)], fill=(120, 50, 10, a // 2), width=max(1, int(s * 0.12)))


_lr = np.random.default_rng(13)
FALL = [(float(_lr.uniform(-100, 1180)), float(_lr.uniform(0, 2100)), float(_lr.choice([0.5, 0.8, 1.2, 1.8], p=[.35, .35, .2, .1])), float(_lr.uniform(0, 6.28)), int(_lr.integers(0, 5))) for _ in range(70)]


def falling_leaves(c, t, front):
    for (x0, y0, d, ph, ci) in FALL:
        if (d > 1.5) != front: continue
        y = (y0 + t * 70 * d) % 2100 - 100; x = x0 + 70 * math.sin(t * 0.8 + ph) * d
        leaf(c, x, y, 13 * d, t * 1.6 + ph, LEAF_COL[ci], math.cos(t * 2.4 + ph), 235)


def pile(c, x, ybase, wdt, t, wig=0.0, alpha=1.0, squash=1.0):
    im = sized("leaves_pile", w=wdt * c.Z)
    if squash != 1.0 or wig:
        im = im.resize((int(im.width * (1 + 0.04 * wig)), max(2, int(im.height * squash * (1 - 0.03 * wig)))), Image.LANCZOS)
    if alpha < 1: im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * alpha)))
    R.contact(c, x, ybase, wdt * 0.42, 90)
    c.img.paste(im, (int(c.X(x) - im.width / 2 + wig * 6 * math.sin(t * 40)), int(c.Y(ybase) - im.height + 8 * c.Z)), im)


def burst(c, x, y, t, t0, n=60, spread=520, dur=1.8, seed=3):
    """esplosione di foglie che volano in aria e ricadono ondeggiando"""
    if not (t0 <= t < t0 + dur): return
    u = t - t0; rng = np.random.default_rng(seed)
    for k in range(n):
        a = rng.uniform(math.pi * 1.05, math.pi * 1.95); v = rng.uniform(0.4, 1.0) * spread * 2.2
        px = x + math.cos(a) * v * u * 0.8 + 30 * math.sin(u * 4 + k); py = y + math.sin(a) * v * u + 420 * u * u
        py = min(py, y + 60)
        fade = clamp((t0 + dur - t) / 0.5)
        leaf(c, px, py, rng.uniform(12, 26), u * rng.uniform(3, 8) + k, LEAF_COL[k % 5], math.cos(u * 6 + k), int(255 * fade))


# ------------------------------------------------------------------ chi è dove
END_OFF = {"volpe": (-60.0, 170.0, 1830.0), "spike": (-160.0, 370.0, 1800.0), "ele": (170.0, 900.0, 1800.0)}


def pos(n, t):
    """(x, y, scala, visibile, hop extra); dopo l'esplosione ognuno ricade al suo posto con un arco"""
    if n in END_OFF and T_BOOM <= t < T_BOOM + 0.6:
        dx, fx, fy = END_OFF[n]; p = ease((t - T_BOOM) / 0.6)
        return (lerp(PILE2[0] + dx, fx, p), lerp(PILE2[1] - 40, fy, p), 1.0, True)
    return _pos(n, t)


def _pos(n, t):
    if n == "volpe":
        if t < E("v1"): return POS0["volpe"] + (1.0, True)
        if t < T_FOUND1 - 0.55:
            p = ease((t - E("v1")) / 0.8); return (lerp(560, 600, p), 1850.0, 1.0, True)
        if t < T_FOUND2 - 0.5:
            p = ease((t - T_FOUND1 + 0.55) / 0.6); return (lerp(600, 520, p), 1850.0, 1.0, True)
        if t < T_LOOK2 + 0.6:
            p = ease((t - T_FOUND1 - 0.05) / 0.8); return (lerp(520, 560, p), 1850.0, 1.0, True)
        if t < T_JUMP:
            p = ease((t - T_FOUND2 + 0.5) / 0.6); return (lerp(560, 600, p), 1850.0, 1.0, True)
        if t < T_BOOM:
            p = (t - T_JUMP) / (T_BOOM - T_JUMP); return (lerp(600, PILE2[0] - 60, p), lerp(1850, PILE2[1] - 40, p), 1.0, p < 0.92)
        return (170.0, 1830.0, 1.0, True)
    if n == "spike":
        if t < T_HIDE_S: return POS0["spike"] + (1.0, True)
        if t < T_HIDE_S + 0.6:
            p = (t - T_HIDE_S) / 0.6; return (lerp(300, POS_HID["spike"][0], p), lerp(1790, POS_HID["spike"][1], p) - 4 * p * (1 - p) * 260, 1.0, True)
        if t < T_FOUND1: return POS_HID["spike"] + (1.0, True)
        if t < T_JUMP:
            p = ease((t - T_FOUND1) / 0.75); return (lerp(POS_HID["spike"][0], POS_OUT["spike"][0], p), lerp(POS_HID["spike"][1], POS_OUT["spike"][1], p) - 4 * p * (1 - p) * 300 if p < 1 else POS_OUT["spike"][1], 1.0, True)
        if t < T_BOOM:
            p = (t - T_JUMP) / (T_BOOM - T_JUMP); return (lerp(330, PILE2[0] - 160, p), lerp(1800, PILE2[1] - 40, p), 1.0, p < 0.92)
        return (370.0, 1800.0, 1.0, True)
    if n == "ele":
        if t < T_HIDE_E0: return POS0["ele"] + (1.0, True)
        if t < T_HIDE_E1:
            p = (t - T_HIDE_E0) / (T_HIDE_E1 - T_HIDE_E0); return (lerp(820, POS_HID["ele"][0], p), lerp(1800, POS_HID["ele"][1], p), 1.0, True)
        if t < T_FOUND2: return POS_HID["ele"] + (1.0, True)
        if t < T_JUMP:
            p = ease((t - T_FOUND2) / 0.7); return (lerp(POS_HID["ele"][0], POS_OUT["ele"][0], p), lerp(POS_HID["ele"][1], POS_OUT["ele"][1], p), 1.0, True)
        if t < T_BOOM:
            p = (t - T_JUMP) / (T_BOOM - T_JUMP); return (lerp(700, PILE2[0] + 170, p), lerp(1820, PILE2[1] - 40, p), 1.0, p < 0.92)
        return (900.0, 1800.0, 1.0, True)
    # topolino: nascosto nel mucchio grande, esce alla fine
    if t < T_MOUSE + 0.75: return (560.0, 1640.0, 1.0, t >= T_MOUSE)
    p = ease((t - T_MOUSE - 0.75) / 0.6); return (lerp(560, 620, p), lerp(1640, 1840, p), 1.0, True)


def _fox_after(t):
    return None


def jump_into(n, t):
    """salto ad arco verso il mucchio grande"""
    if T_JUMP <= t < T_BOOM:
        p = (t - T_JUMP) / (T_BOOM - T_JUMP); return 4 * p * (1 - p) * 420
    if n != "volpe" and T_BOOM <= t < T_BOOM + 0.6:                              # ricadono fuori dall'esplosione
        p = (t - T_BOOM) / 0.6; return 4 * p * (1 - p) * 300 * (1 - p)
    return 0.0


def draw_clipped(c, n, t, x, y, ymax, hop=0.0):
    """disegna il personaggio su un livello a parte e taglia tutto ciò che sta sotto ymax (nascosto dal mucchio/cespuglio)"""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    c2 = Ctx(); c2.img = lay; c2.d = ImageDraw.Draw(lay, "RGBA"); c2.t = c.t; c2.Z = c.Z; c2.sid = c.sid; c2.X = c.X; c2.Y = c.Y
    R.draw_char(c2, n, t, x, y, hop=hop)
    yy = int(clamp(c.Y(ymax), 0, H))
    a = np.asarray(lay).copy(); a[yy:, :, 3] = 0
    lay = Image.fromarray(a, "RGBA"); c.img.paste(lay, (0, 0), lay)


def draw_scene(c, t):
    falling_leaves(c, t, False)
    # albero dietro al cespuglio
    # mucchio grande (al centro, dietro): esplode a T_BOOM, poi ne resta un mucchietto da cui esce il topolino
    if t < T_BOOM:
        k = 0.0
        if T_JUMP + 0.6 <= t < T_BOOM: k = (t - T_JUMP - 0.6) / (T_BOOM - T_JUMP - 0.6)
        pile(c, PILE2[0], PILE2[1], PILE2[2], t, wig=k * 2, squash=1 - 0.15 * k)
    else:
        u = clamp((t - T_BOOM) / 0.35)
        small = 0.55 * PILE2[2]
        wig = 1.0 if (T_MOUSE - 1.6 <= t < T_MOUSE) else 0.0
        if t < T_MOUSE + 0.1: pile(c, PILE2[0], PILE2[1], lerp(PILE2[2], small, u), t, wig=wig, squash=lerp(0.5, 1, u))
    # chi sta dietro (in ordine di profondità)
    items = []
    for n in ("volpe", "spike", "ele", "mouse"):
        x, y, sc, vis = pos(n, t)
        if vis: items.append((y, n, x))
    items.append((PILE1[1], "pile1", None)); items.append((BUSH[1], "bush", None))
    for y, n, x in sorted(items, key=lambda q: q[0]):
        if n == "pile1":
            wig = 1.0 if (T_LOOK1 <= t < T_FOUND1) and int(t * 1.6) % 2 == 0 else 0.0
            sq = 1.0 if t < T_FOUND1 else 1 - 0.25 * clamp((t - T_FOUND1) / 0.3)
            pile(c, PILE1[0], PILE1[1], PILE1[2], t, wig=wig, squash=sq)
            if T_FOUND1 <= t: burst(c, PILE1[0], PILE1[1] - 120, t, T_FOUND1, n=36, spread=320, dur=1.5, seed=5)
        elif n == "bush":
            wig = 1.0 if (T_LOOK2 <= t < T_FOUND2) and int(t * 1.5) % 2 == 0 else 0.0
            im = sized("leaves_pile", w=BUSH[2] * c.Z)
            R.contact(c, BUSH[0], BUSH[1], BUSH[2] * 0.42, 100)
            c.img.paste(im, (int(c.X(BUSH[0]) - im.width / 2 + wig * 5 * math.sin(t * 38)), int(c.Y(BUSH[1]) - im.height)), im)
            if T_FOUND2 <= t < T_FOUND2 + 1.2: burst(c, BUSH[0], BUSH[1] - 250, t, T_FOUND2, n=22, spread=260, dur=1.2, seed=8)
        else:
            hop = jump_into(n, t)
            clip = None
            if n == "spike" and T_HIDE_S + 0.45 <= t < T_FOUND1 + 0.3: clip = PILE1[1] - 30
            if n == "ele" and T_HIDE_E1 - 0.3 <= t < T_FOUND2 + 0.2: clip = BUSH[1] - 40
            if clip is not None:
                sink = 0.0
                if n == "spike":
                    sink = 235 * clamp((t - T_HIDE_S - 0.45) / 0.3) * (1 - clamp((t - T_FOUND1) / 0.25))
                    sink -= 45 * max(0.0, math.sin(t * 6)) if T_LOOK1 <= t < T_FOUND1 else 0          # sbuca un poco: indizio
                if n == "ele": sink = 215 * clamp((t - T_HIDE_E1 + 0.3) / 0.3) * (1 - clamp((t - T_FOUND2) / 0.25)) - (35 * max(0.0, math.sin(t * 5)) if T_LOOK2 <= t < T_FOUND2 else 0)
                draw_clipped(c, n, t, x, y + sink, clip, hop)
                continue
            if n == "mouse":
                R.draw_char(c, "mouse", t, x, y, hop=0)
                if T_MOUSE <= t < T_MOUSE + 1.4: burst(c, x, y - 120, t, T_MOUSE, n=40, spread=380, dur=1.4, seed=21)
            else:
                rot = 0.0
                if T_JUMP <= t < T_BOOM: rot = -25 * math.sin(math.pi * (t - T_JUMP) / (T_BOOM - T_JUMP)) * (1 if n == "ele" else -1)
                R.draw_char(c, n, t, x, y, hop=hop, rot=rot)
    if T_BOOM <= t < T_BOOM + 2.4:
        burst(c, PILE2[0], PILE2[1] - 150, t, T_BOOM, n=110, spread=640, dur=2.4, seed=11)
        if t < T_BOOM + 1.0: sparkles(c, PILE2[0], PILE2[1] - 300, T_BOOM, 1.0, n=20, spread=420, rise=50, size=20, seed=4)
    # indizi per i bambini: cerchio che pulsa sul nascondiglio
    for (t0, t1, x, y, r) in ((T_LOOK1, T_FOUND1, PILE1[0], PILE1[1] - 150, 230), (T_LOOK2, T_FOUND2, BUSH[0], BUSH[1] - 330, 300)):
        if t0 + 0.6 <= t < t1:
            u = (t - t0 - 0.6) % 0.9 / 0.9; rr = r * (0.8 + 0.4 * u) * c.Z
            c.d.ellipse([c.X(x) - rr, c.Y(y) - rr, c.X(x) + rr, c.Y(y) + rr], outline=(255, 255, 255, int(200 * (1 - u))), width=max(4, int(9 * c.Z)))
    for (tf, txt, x, y) in ((T_FOUND1, "TROVATO!", 540, 760), (V["v3"], "TI VEDO!", 540, 760)):
        if tf <= t < tf + 0.9:
            u = (t - tf) / 0.9; a = int(255 * clamp((1 - u) * 3))
            text(c.d, txt, x, y - 30 * u, int(150 * back(clamp(u / 0.25))), (255, 235, 90, a), (190, 60, 20, a), 13)
    falling_leaves(c, t, True)


# ------------------------------------------------------------------ camera
CAM = [(0.0, 540, 1350, 1.12), (V["n1"] + 1.5, 540, 1330, 1.06), (V["v1"], 540, 1330, 1.04), (E("v1") + 0.1, 540, 1330, 1.04),
       (T_LOOK1 - 0.3, 420, 1450, 1.3), (T_FOUND1 + 0.3, 420, 1450, 1.28), (E("s1") + 0.2, 480, 1380, 1.15),
       (T_LOOK2 - 0.4, 780, 1380, 1.35), (T_FOUND2 + 0.4, 760, 1400, 1.3), (E("e1") + 0.2, 560, 1350, 1.08),
       (T_JUMP, 560, 1300, 1.04), (T_BOOM, 560, 1250, 1.0), (T_BOOM + 1.2, 560, 1320, 1.08), (T_MOUSE - 0.3, 560, 1380, 1.25),
       (T_MOUSE + 0.8, 560, 1350, 1.18), (V["end"] + 0.8, 560, 1300, 1.06), (DUR, 560, 1300, 1.06)]
SHAKES = [(T_FOUND1, 10), (T_FOUND2, 10), (T_BOOM, 22), (T_MOUSE, 12)]


def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 5 * math.sin(t * 0.8) + 3 * math.sin(t * 2.3); cy += 4 * math.sin(t * 1.1 + 1)
    for kt, amp in SHAKES:
        if kt <= t < kt + 0.45:
            k = (1 - (t - kt) / 0.45) * amp; cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    z = max(1.0, z); hx, hy = 540 / z, 960 / z
    return min(max(cx, hx), W - hx), min(max(cy, hy), H - hy), z


_VIG = None
def frame(i):
    global _VIG
    if _VIG is None: _VIG = R.vignette()
    t = i / FPS; cx, cy, Z = camera(t)
    arr = background(t)
    box = (cx - 540 / Z, cy - 960 / Z, cx + 540 / Z, cy + 960 / Z)
    img = Image.fromarray(arr).resize((W, H), Image.BICUBIC, box=box).filter(ImageFilter.GaussianBlur(0.3 + 0.8 * max(0, Z - 1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z; c.sid = SID
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    glow_blob(c, 560, 250, 520, (70, 55, 25), 0.8 + 0.2 * math.sin(t * 0.9))                      # sole tra gli alberi
    draw_scene(c, t)
    img = c.img
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); img = ImageChops.add(ImageChops.add(img, c.glow), g2)
    a = np.asarray(img).astype(np.float32)
    a = a + cv2.resize(cv2.GaussianBlur(cv2.resize(np.clip(a - 215, 0, 255) * 3.0, (W // 4, H // 4), interpolation=cv2.INTER_AREA), (0, 0), 3.5), (W, H)) * 0.18
    a = a + np.random.default_rng(i).normal(0, 2.0, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    img = Image.fromarray(np.clip(a * _VIG, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img, "RGBA")
    if t < 2.3:
        u = back(t / 0.35); al = int(255 * clamp((2.3 - t) / 0.4))
        text(d, "DOVE SONO?", W / 2, 260 - 10 * math.sin(t * 6), int(140 * clamp(max(0.6, u), 0, 1.0)), (255, 235, 90, al), (190, 60, 20, al), 13)
    subscribe_button(img, t, V["end"] + 0.9)
    return img.tobytes()


def _prep(p):
    try: MO.transition(*p); return None
    except Exception as e: return (p, str(e)[:80])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2)); print({k: round(v, 2) for k, v in V.items()})
        print({k: round(v, 2) for k, v in dict(T_HIDE_S=T_HIDE_S, T_LOOK1=T_LOOK1, T_FOUND1=T_FOUND1, T_LOOK2=T_LOOK2, T_FOUND2=T_FOUND2, T_JUMP=T_JUMP, T_BOOM=T_BOOM, T_MOUSE=T_MOUSE).items()})
    elif cmd == "prep":
        ps = precompute(); print(len(ps), "transizioni")
        with Pool(4) as pool:
            for r in pool.imap_unordered(_prep, ps):
                if r: print("manca", r)
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
