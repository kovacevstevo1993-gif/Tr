#!/usr/bin/env python3
"""Short 'La festa a sorpresa' (9:16, 1080x1920, 30 fps): compleanno del topolino con Chip, Spike e l'elefantino.
Diverso dagli altri: tutto in una stanza, gioco di LUCI (buio con la luce della porta -> luci accese di colpo con coriandoli ->
luci da discoteca), conto INTERATTIVO per soffiare le candeline, panna che vola anche sullo 'schermo', palloncini dal regalo.
Riusa il motore di short_razzo.py (corpo vivo, pose con morph, bocca, luce).
    python3 short_festa.py info | prep | test 1.0 5.5 | renderpart a b out.mp4 | render muto.mp4
"""
import json, math, os, subprocess, sys
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import morph as MO
import short_razzo as R
from short_razzo import lerp, clamp, ease, back, osc, text, sparkles, glow_blob, paste_c, puff, subscribe_button, sized, Ctx, star4

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
AUD = "audioL"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))
WD = json.load(open(os.path.join(HERE, AUD, "parole.json")))

V = {}
def _seq():
    t = 0.0
    def at(k, gap):
        nonlocal t
        V[k] = t + gap; t = V[k] + D[k]
    at("n1", 0.5); at("c1", 0.2); at("n2", 0.5); at("t1", 0.2); at("x1", 0.4)
    V["x2"] = V["x1"] + 0.05; V["x3"] = V["x1"] + 0.1; t = max(E_(k) for k in ("x1", "x2", "x3"))
    at("n3", 0.9); at("n4", 0.7); at("e1", 0.15); at("n5", 0.3); at("s1", 0.4); at("n6", 0.5); at("end", 0.5)
    return t + 2.8
def E_(k): return V[k] + D[k]
DUR = _seq()
SAY = {"n1": "narr", "c1": "chip", "n2": "narr", "t1": "mouse", "x1": "chip", "x2": "spike", "x3": "ele", "n3": "narr", "n4": "narr",
       "e1": "ele", "n5": "narr", "s1": "spike", "n6": "narr", "end": "mouse"}
VOICES = [(k, V[k], SAY[k], D[k]) for k in V]
E = E_


def word(k, w, frac=0.5):
    import re
    for (ww, a, b) in WD.get(k, []):
        if re.sub(r"[^\wàèéìòù']", "", ww.lower()) == w.lower(): return V[k] + a
    for (ww, a, b) in WD.get(k, []):
        if w.lower() in ww.lower(): return V[k] + a
    return V[k] + D[k] * frac


# ------------------------------------------------------------------ eventi
T_OFF = E("c1") + 0.15                         # luci spente
T_ENTER0 = V["n2"] + 0.1; T_ENTER1 = T_ENTER0 + 2.0      # il topolino entra dalla porta (destra)
T_ON = V["x1"] - 0.05                           # SORPRESA: luci accese
T_CNT = [word("n3", "uno"), word("n3", "due"), word("n3", "tre"), word("n3", "soffia")]
T_PUFF = T_CNT[3] + 0.1                          # il topolino soffia (le candeline restano accese)
T_BLOW = V["n5"] + 0.6                           # l'elefantino soffia
T_SPLAT = word("n5", "panna") - 0.1              # panna dappertutto
T_GIFT = word("n6", "regalo") + 0.2              # il regalo si apre
T_BALL = word("n6", "palloncini") - 0.1
T_DISCO = word("n6", "compleanno") - 0.2

CAKE = (600.0, 1330.0, 360.0)                    # torta sul tavolino (x, base, larghezza)
GIFT = (560.0, 1800.0, 230.0)
POS = {"chip": (140.0, 1610.0), "spike": (930.0, 1600.0), "mouse": (370.0, 1830.0), "ele": (820.0, 1820.0)}
DOOR = (1080.0, 1650.0)


def loop(t0, t1, seq, beat=0.5):
    ev = []; i = 0
    while t0 + i * beat < t1:
        ev.append((t0 + i * beat, seq[i % len(seq)], beat * 0.85)); i += 1
    return ev


def walk(t0, t1, per=0.62):
    pl = ["cammina_dx_m", "passa_dx_m", "cammina_dx", "passa_dx_m"]; q = per / 4
    return [(t0 + i * q, pl[i % 4], q) for i in range(int((t1 - t0) / q))]


EV = {
    "mouse": [(0.0, "neutro", 0.01)] + walk(T_ENTER0, T_ENTER1) + [(T_ENTER1, "guarda_su", 0.15), (V["t1"] - 0.1, "sorpreso", 0.15),
              (T_ON + 0.05, "fuggi", 0.1), (T_ON + 0.7, "sorpreso", 0.15), (E("x3") + 0.3, "ride", 0.2), (V["n3"] + 1.2, "indica", 0.2),
              (T_CNT[0] - 0.2, "tiene", 0.2), (T_PUFF - 0.1, "sorpreso", 0.12), (V["n4"] + 0.3, "triste", 0.2), (T_BLOW - 0.2, "guarda_su", 0.2),
              (T_SPLAT + 0.1, "sorpreso", 0.1), (V["s1"] + 0.2, "ride", 0.2), (T_GIFT - 0.3, "indica", 0.15), (T_BALL + 0.2, "salto", 0.12)]
             + loop(T_DISCO, DUR + 1, ["balla", "salto", "balla_m", "saluta2", "ride", "saluta2_m"], 0.5),
    "chip": [(0.0, "tiene", 0.01), (V["n1"] + 2.4, "ride", 0.2), (V["c1"] - 0.1, "sbircia", 0.15), (T_ON, "salto", 0.12), (T_ON + 0.75, "ride", 0.2),
             (V["n3"] + 1.4, "guarda_su", 0.2), (T_PUFF, "sorpreso", 0.15), (T_SPLAT + 0.1, "sorpreso", 0.1), (T_SPLAT + 0.9, "ride", 0.2),
             (T_BALL + 0.3, "salto", 0.12)] + loop(T_DISCO + 0.1, DUR + 1, ["balla_m", "ride", "salto", "saluta2", "balla"], 0.5),
    "spike": [(0.0, "tiene", 0.01), (V["n1"] + 2.6, "ride", 0.2), (V["c1"], "sbircia", 0.15), (T_ON + 0.05, "salto", 0.12), (T_ON + 0.8, "ride", 0.2),
              (V["n3"] + 1.5, "guarda_su", 0.2), (T_PUFF, "sorpreso", 0.15), (T_SPLAT + 0.1, "ops", 0.1), (V["s1"] - 0.1, "mangia", 0.2),
              (E("s1") + 0.4, "ride", 0.2), (T_BALL + 0.25, "salto", 0.12)] + loop(T_DISCO + 0.2, DUR + 1, ["balla", "salto", "ride", "balla_m", "saluta2"], 0.5),
    "ele": [(0.0, "saluta2", 0.01), (V["n1"] + 2.5, "ride", 0.2), (V["c1"] + 0.1, "sorpreso", 0.15), (T_ON + 0.1, "salto", 0.12), (T_ON + 0.85, "ride", 0.2),
            (V["n3"] + 1.6, "guarda_su", 0.2), (T_PUFF, "sorpreso", 0.15), (V["e1"] - 0.15, "indica", 0.15), (T_BLOW - 0.15, "soffia_m", 0.12),
            (T_SPLAT + 0.9, "sorpreso", 0.15), (V["s1"] + 0.4, "ride", 0.2), (T_BALL + 0.2, "salto", 0.12)]
           + loop(T_DISCO + 0.15, DUR + 1, ["balla", "ride", "saluta2", "salto", "balla"], 0.52),
}
for _n in EV: EV[_n].sort(key=lambda e: e[0])
JUMPS = {"mouse": [(T_ON + 0.05, 0.5, 120)], "chip": [(T_ON, 0.6, 240)], "spike": [(T_ON + 0.05, 0.6, 240)], "ele": [(T_ON + 0.1, 0.6, 220)]}

R.AUD = AUD; R.VOICES = VOICES; R.EV = EV; R.JUMPS = JUMPS
R.H_CH = {"mouse": 640.0, "chip": 600.0, "spike": 560.0, "ele": 660.0}
ALIAS = {"ele": {"ops": "sorpreso"}}
for sid, tint, rim, rd, sh in (("festa", (1.03, 1.0, 0.97), ((255, 210, 150), 0.35), (1, -1), (50, 25, 20)),
                               ("buio", (0.30, 0.34, 0.55), ((120, 150, 255), 0.30), (1, -1), (5, 5, 15))):
    R.TINT[sid] = tint; R.RIM[sid] = rim; R.RIMDIR[sid] = rd; R.SHCOL[sid] = sh; R.SUN[sid] = (0.5, 0.3)


def precompute():
    pairs = set()
    for name, ev in EV.items():
        for a, b in zip(ev, ev[1:]):
            if a[1] != b[1]: pairs.add((name, a[1], b[1]))
        for p in ("parla_a", "parla_o"): pairs.add((name, "neutro", p)); pairs.add((name, p, "neutro"))
    return sorted(pairs)


# ------------------------------------------------------------------ luce della stanza
def light(t):
    """0 = buio, 1 = luci accese"""
    if t < T_OFF: return 0.85 + 0.15 * clamp(t / 1.0)
    if t < T_ON: return max(0.0, 1 - (t - T_OFF) / 0.25) * 0.85
    return clamp((t - T_ON) / 0.08)


_bg = None
def bg_arr():
    global _bg
    if _bg is None:
        _bg = np.asarray(Image.open(os.path.join(HERE, "assets", "amb", "festa_buio.png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)
    return _bg


_grid = None
def background(t):
    global _grid
    if _grid is None: _grid = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    xs, ys = _grid
    a = bg_arr(); L = light(t)
    dark = a * np.array([0.12, 0.14, 0.26], np.float32)
    out = dark * (1 - L) + a * L
    if T_OFF + 0.2 < t < T_ON:                                                 # luce dalla porta aperta (destra) mentre entra
        k = clamp((t - T_ENTER0 + 0.4) / 0.5)
        cone = np.clip(1 - np.abs((ys - 1500) - (xs - 1080) * 0.55) / (180 + (1080 - xs) * 0.55), 0, 1) * np.clip((xs - 300) / 700, 0, 1)
        out = out + (a * 0.9 + 40) * cone[..., None] * 0.55 * k
    if t >= T_DISCO:                                                           # luci da discoteca
        for k, col in enumerate(((255, 60, 120), (60, 160, 255), (255, 220, 60), (120, 255, 120))):
            cx = 540 + 420 * math.sin(t * (0.9 + 0.2 * k) + k * 1.7); cy = 1100 + 500 * math.cos(t * (0.7 + 0.15 * k) + k)
            m = np.exp(-(((xs - cx) / 260) ** 2 + ((ys - cy) / 260) ** 2))
            out = out + m[..., None] * np.array(col, np.float32) * 0.28 * clamp((t - T_DISCO) / 0.5)
    return np.clip(out, 0, 255).astype(np.uint8)


# ------------------------------------------------------------------ oggetti di scena
def candles(c, t, x, top, wdt):
    """5 candeline disegnate sulla torta: fiamme che tremano, piegate dal soffio, spente con fumino"""
    n = 5; out_t = T_BLOW + 0.35
    for i in range(n):
        u = (i - 2) / 2.0; cx = x + u * wdt * 0.26; cy = top + wdt * 0.035 * abs(u) - wdt * 0.02
        hgt = wdt * 0.17; cw = wdt * 0.035
        col = [(255, 120, 160), (120, 200, 255), (255, 230, 90), (150, 240, 140), (200, 150, 255)][i]
        c.d.rounded_rectangle([c.X(cx - cw / 2), c.Y(cy - hgt), c.X(cx + cw / 2), c.Y(cy)], radius=int(cw * 0.3 * c.Z), fill=col + (255,))
        for s in range(3):
            yy = cy - hgt + (s + 0.5) * hgt / 3
            c.d.line([(c.X(cx - cw / 2), c.Y(yy)), (c.X(cx + cw / 2), c.Y(yy - cw * 0.5))], fill=(255, 255, 255, 200), width=max(2, int(cw * 0.25 * c.Z)))
        fy = cy - hgt - 4
        if t < out_t:
            bend = 0.0
            if T_PUFF <= t < T_PUFF + 0.9: bend = 0.9 * math.sin(math.pi * (t - T_PUFF) / 0.9)          # il topolino: si piegano ma restano
            if T_BLOW <= t: bend = 1.6 * clamp((t - T_BLOW) / 0.3)
            fl = 1 + 0.12 * math.sin(t * 23 + i * 2) + 0.08 * math.sin(t * 37 + i)
            fh = wdt * 0.075 * fl * (1 - 0.3 * min(1, bend)); fw = wdt * 0.028
            tipx = cx - bend * fh * 0.9; tipy = fy - fh * (1 - 0.4 * min(1, bend))
            for k, (cc, sc) in enumerate((((255, 150, 40), 1.0), ((255, 230, 120), 0.65), ((255, 255, 230), 0.35))):
                pts = [(c.X(cx - fw * sc), c.Y(fy)), (c.X(lerp(cx, tipx, 0.5) - fw * sc * 0.8), c.Y(lerp(fy, tipy, 0.5))), (c.X(tipx), c.Y(tipy)),
                       (c.X(lerp(cx, tipx, 0.5) + fw * sc * 0.8), c.Y(lerp(fy, tipy, 0.5))), (c.X(cx + fw * sc), c.Y(fy))]
                c.d.polygon(pts, fill=cc + (240,))
            glow_blob(c, cx, fy - fh * 0.4, wdt * 0.12, (110, 70, 20), 0.9 if light(t) < 0.5 else 0.5, 5)
        elif t < out_t + 2.0:                                                       # fumino
            u2 = (t - out_t) / 2.0
            for k in range(4):
                sy = fy - 30 * k - 160 * u2; sx = cx + 18 * math.sin(t * 3 + k + i)
                rr = (8 + 10 * k * u2) * c.Z
                c.d.ellipse([c.X(sx) - rr, c.Y(sy) - rr, c.X(sx) + rr, c.Y(sy) + rr], fill=(220, 220, 230, int(150 * (1 - u2))))


def cake(c, t):
    x, yb, wdt = CAKE
    im = sized("cake_off", w=wdt * c.Z)
    if light(t) < 0.99: im = R.tinted(im, tuple(lerp(v, 1.0, light(t)) for v in (0.25, 0.28, 0.45)))
    R.contact(c, x, yb, wdt * 0.42, 90)
    sq = 1 + osc(t, T_SPLAT - 0.1, 0.08, 9, 24)
    im2 = im.resize((int(im.width / math.sqrt(sq)), int(im.height * sq)), Image.LANCZOS) if sq != 1 else im
    c.img.paste(im2, (int(c.X(x) - im2.width / 2), int(c.Y(yb) - im2.height)), im2)
    top = yb - wdt * (im.height / im.width) * 0.86
    if t >= T_SPLAT:                                                                 # la panna si è svuotata un po': cratere
        rr = wdt * 0.22 * c.Z
        c.d.ellipse([c.X(x) - rr, c.Y(top + wdt * 0.04) - rr * 0.35, c.X(x) + rr, c.Y(top + wdt * 0.04) + rr * 0.35], fill=(235, 120, 170, 220))
    else:
        candles(c, t, x, top + wdt * 0.06, wdt)
    if T_BLOW <= t < T_SPLAT + 0.3: candles(c, t, x, top + wdt * 0.06, wdt)


SPLATS = {"mouse": [(-0.10, 0.80, 34), (0.14, 0.62, 22), (0.05, 0.92, 18)], "chip": [(0.08, 0.78, 30), (-0.12, 0.6, 20)],
          "spike": [(-0.05, 0.75, 30), (0.12, 0.88, 18)], "ele": [(0.15, 0.82, 28), (-0.2, 0.7, 22), (0.0, 0.95, 16)]}


def cream_fly(c, t):
    """schizzi di panna che volano dalla torta ai musi degli amici"""
    if not (T_SPLAT - 0.35 <= t < T_SPLAT + 0.05): return
    p = clamp((t - T_SPLAT + 0.35) / 0.4)
    x0, y0 = CAKE[0], CAKE[1] - CAKE[2] * 0.7
    for n, lst in SPLATS.items():
        px, py = POS[n]
        for (dx, hy, r) in lst:
            tx, ty = px + dx * R.H_CH[n], py - hy * R.H_CH[n]
            x = lerp(x0, tx, p); y = lerp(y0, ty, p) - 4 * p * (1 - p) * 200
            rr = r * c.Z * (0.6 + 0.4 * p)
            c.d.ellipse([c.X(x) - rr, c.Y(y) - rr, c.X(x) + rr, c.Y(y) + rr], fill=(255, 180, 210, 255))


def cream_on(c, t, n, x, y, hop):
    if t < T_SPLAT + 0.02 or t > T_DISCO + 0.3: return
    a = int(255 * clamp((T_DISCO + 0.3 - t) / 0.4))
    for (dx, hy, r) in SPLATS[n]:
        cx, cy = x + dx * R.H_CH[n], y - hop - hy * R.H_CH[n]
        rr = r * c.Z * (1 + osc(t, T_SPLAT, 0.4, 10, 20))
        c.d.ellipse([c.X(cx) - rr, c.Y(cy) - rr * 0.85, c.X(cx) + rr, c.Y(cy) + rr * 0.85], fill=(255, 190, 215, a))
        c.d.ellipse([c.X(cx - r * 0.3) - rr * 0.35, c.Y(cy - r * 0.3) - rr * 0.25, c.X(cx - r * 0.3) + rr * 0.35, c.Y(cy - r * 0.3) + rr * 0.25], fill=(255, 245, 250, a))


def gift(c, t):
    x, yb, wdt = GIFT
    im = sized("gift", w=wdt * c.Z)
    if light(t) < 0.99: im = R.tinted(im, tuple(lerp(v, 1.0, light(t)) for v in (0.25, 0.28, 0.45)))
    R.contact(c, x, yb, wdt * 0.45, 100)
    shake = 4 * math.sin(t * 40) if T_GIFT - 0.8 <= t < T_GIFT else 0
    if t < T_GIFT:
        c.img.paste(im, (int(c.X(x) - im.width / 2 + shake), int(c.Y(yb) - im.height)), im)
    else:
        cut = int(im.height * 0.30)
        body = im.crop((0, cut, im.width, im.height)); lid = im.crop((0, 0, im.width, cut))
        c.img.paste(body, (int(c.X(x) - im.width / 2), int(c.Y(yb) - im.height + cut)), body)
        u = clamp((t - T_GIFT) / 0.7); lx = x + 220 * u; ly = yb - wdt * im.height / im.width + cut / c.Z - 380 * u + 520 * u * u
        lid2 = lid.rotate(-140 * u, resample=Image.BICUBIC, expand=True); paste_c(c, lid2, lx, ly - cut / c.Z / 2)
        if t < T_GIFT + 1.0: sparkles(c, x, yb - 200, T_GIFT, 1.0, n=18, spread=180, rise=60, size=18, seed=6)


def balloons(c, t):
    if t < T_BALL: return
    u = t - T_BALL
    for k in range(3):
        bx = GIFT[0] + (k - 1) * 230 + 40 * math.sin(t * 1.3 + k * 2)
        by = GIFT[1] - 250 - 260 * u - 120 * k + 18 * math.sin(t * 2 + k)
        by = max(by, 520 + 180 * k)
        im = sized("balloons", w=(330 - 40 * k) * c.Z)
        paste_c(c, im, bx, by, 6 * math.sin(t * 1.7 + k))


def confetti(c, t, t0, n=120, dur=3.2):
    if not (t0 <= t < t0 + dur): return
    rng = np.random.default_rng(4); u = t - t0
    cols = [(255, 80, 120), (80, 180, 255), (255, 220, 60), (120, 230, 120), (200, 120, 255), (255, 150, 60)]
    for k in range(n):
        x0 = rng.uniform(0, W); vx = rng.uniform(-200, 200); vy = rng.uniform(-1600, -800)
        x = x0 + vx * u + 40 * math.sin(u * 5 + k); y = H + 50 + vy * u + 900 * u * u
        if y > H + 60: continue
        s = rng.uniform(8, 16); ang = u * rng.uniform(4, 10) + k; fl = abs(math.cos(u * 7 + k))
        ca, sa = math.cos(ang), math.sin(ang)
        pts = [(x + (-s) * ca - (-s * 0.5 * fl) * sa, y + (-s) * sa + (-s * 0.5 * fl) * ca), (x + s * ca - (-s * 0.5 * fl) * sa, y + s * sa + (-s * 0.5 * fl) * ca),
               (x + s * ca - (s * 0.5 * fl) * sa, y + s * sa + (s * 0.5 * fl) * ca), (x + (-s) * ca - (s * 0.5 * fl) * sa, y + (-s) * sa + (s * 0.5 * fl) * ca)]
        c.d.polygon(pts, fill=cols[k % 6] + (255,))


def screen_splats(img, t):
    """panna sullo 'schermo' (verso chi guarda) che poi scivola giù e sparisce"""
    if not (T_SPLAT <= t < T_SPLAT + 2.2): return img
    u = (t - T_SPLAT) / 2.2
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for (x, y, r) in ((210, 520, 120), (880, 380, 90), (760, 1180, 70), (300, 1350, 60)):
        yy = y + 260 * u * u; a = int(235 * clamp((1 - u) * 2.5))
        rr = r * back(clamp(u * 8), 2.0)
        d.ellipse([x - rr, yy - rr * 0.9, x + rr, yy + rr * 0.9], fill=(255, 190, 215, a))
        for k in range(6):
            ang = k * 1.05 + r; d.ellipse([x + math.cos(ang) * rr * 1.1 - rr * 0.25, yy + math.sin(ang) * rr - rr * 0.25, x + math.cos(ang) * rr * 1.1 + rr * 0.25, yy + math.sin(ang) * rr + rr * 0.25], fill=(255, 190, 215, a))
        d.ellipse([x - rr * 0.45, yy - rr * 0.5, x - rr * 0.05, yy - rr * 0.2], fill=(255, 250, 252, a))
        d.rounded_rectangle([x - rr * 0.18, yy, x + rr * 0.18, yy + rr * (0.9 + 1.5 * u)], radius=int(rr * 0.18), fill=(255, 190, 215, a))
    lay = lay.filter(ImageFilter.GaussianBlur(1.5)); img.paste(lay, (0, 0), lay)
    return img


def blow_wind(c, t, x0, y0, x1, y1, t0, dur, strength=1.0):
    if not (t0 <= t < t0 + dur): return
    for k in range(14):
        ph = (t * 2.6 + k / 14) % 1.0
        x = lerp(x0, x1, ph); y = lerp(y0, y1, ph) - 40 * math.sin(math.pi * ph) + 14 * math.sin(k * 3 + t * 9)
        rr = (8 + 22 * ph) * c.Z * strength
        c.d.ellipse([c.X(x) - rr, c.Y(y) - rr * 0.7, c.X(x) + rr, c.Y(y) + rr * 0.7], fill=(255, 255, 255, int(160 * math.sin(math.pi * ph))))


# ------------------------------------------------------------------ posizioni
def mouse_x(t):
    if t < T_ENTER0: return None
    if t < T_ENTER1: return lerp(DOOR[0] + 80, POS["mouse"][0], ease((t - T_ENTER0) / (T_ENTER1 - T_ENTER0)) * 0.3 + 0.7 * (t - T_ENTER0) / (T_ENTER1 - T_ENTER0))
    return POS["mouse"][0]


def hidden(n, t):
    """gli amici nel buio si accucciano dietro la torta/divano: affondano verso il basso (solo sagome)"""
    if n == "mouse": return 0.0
    if T_OFF + 0.2 <= t < T_ON: return 260 * clamp((t - T_OFF - 0.2) / 0.4)
    if T_ON <= t < T_ON + 0.25: return 260 * (1 - (t - T_ON) / 0.25)
    return 0.0


def draw_scene(c, t):
    L = light(t)
    c.sid = "festa" if L > 0.5 else "buio"
    items = [(CAKE[1], "cake"), (GIFT[1], "gift")] + [(POS[n][1], n) for n in ("chip", "spike", "mouse", "ele")]
    for _, k in sorted(items):
        if k == "cake": cake(c, t)
        elif k == "gift": gift(c, t)
        else:
            x, y = POS[k]
            if k == "mouse":
                mx = mouse_x(t)
                if mx is None: continue
                x = mx
            sink = hidden(k, t)
            hop = R.jump_state(k, t)[0]
            if sink > 0:
                lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                c2 = Ctx(); c2.img = lay; c2.d = ImageDraw.Draw(lay, "RGBA"); c2.t = t; c2.Z = c.Z; c2.sid = c.sid; c2.X = c.X; c2.Y = c.Y
                R.draw_char(c2, k, t, x, y + sink)
                a = np.asarray(lay).copy(); yy = int(clamp(c.Y(y - 120), 0, H)); a[yy:, :, 3] = 0
                lay = Image.fromarray(a, "RGBA"); c.img.paste(lay, (0, 0), lay)
            else:
                R.draw_char(c, k, t, x, y)
            cream_on(c, t, k, x, y, hop)
    # soffi
    mx = POS["mouse"][0]
    blow_wind(c, t, mx + 90, POS["mouse"][1] - 470, CAKE[0] - 60, CAKE[1] - 300, T_PUFF, 0.9, 0.7)
    if T_BLOW <= t < T_SPLAT + 0.2:
        tx, ty = POS["ele"][0] - 250, POS["ele"][1] - 500
        blow_wind(c, t, tx, ty, CAKE[0] + 40, CAKE[1] - 280, T_BLOW, T_SPLAT + 0.2 - T_BLOW, 1.8)
    cream_fly(c, t)
    balloons(c, t)
    if T_ON <= t < T_ON + 3.2: confetti(c, t, T_ON)
    if T_DISCO <= t: confetti(c, t, T_DISCO, n=80, dur=3.2)
    if T_ON <= t < T_ON + 1.2:
        u = (t - T_ON) / 1.2; a = int(255 * clamp((1 - u) * 3))
        text(c.d, "SORPRESA!", W / 2, 560 - 20 * u, int(170 * back(clamp(u / 0.2))), (255, 235, 90, a), (220, 40, 120, a), 15)
    for i, tc in enumerate(T_CNT):
        nxt = T_CNT[i + 1] if i < 3 else tc + 0.8
        if tc - 0.05 <= t < min(tc + 0.6, nxt - 0.03):
            u = (t - tc + 0.05) / 0.6; a = int(255 * clamp((1 - u) * 3)); s = back(clamp(u / 0.3))
            text(c.d, ["1", "2", "3", "SOFFIA!"][i], W / 2, 600, int((380 if i < 3 else 170) * s), (255, 255, 255, a), (230, 60, 140, a), 15)
    if T_DISCO <= t:                                                                  # palla da discoteca
        u = clamp((t - T_DISCO) / 0.6); bx, by = 540, -60 + 300 * ease(u)
        c.d.line([(c.X(bx), c.Y(-200)), (c.X(bx), c.Y(by - 70))], fill=(200, 200, 210, 255), width=4)
        rr = 80 * c.Z
        c.d.ellipse([c.X(bx) - rr, c.Y(by) - rr, c.X(bx) + rr, c.Y(by) + rr], fill=(170, 175, 195, 255))
        for k in range(26):
            a1 = k * 0.7 + t * 2; px = bx + math.cos(a1) * 55 * abs(math.sin(k * 1.3)); py = by + math.sin(k * 2.1) * 60
            bright = 0.5 + 0.5 * math.sin(t * 8 + k)
            c.d.rectangle([c.X(px) - 7, c.Y(py) - 7, c.X(px) + 7, c.Y(py) + 7], fill=tuple(int(120 + 135 * bright) for _ in range(3)) + (255,))
            if bright > 0.85: star4(c.gd, c.X(px), c.Y(py), 14, (255, 255, 255)); c.glow_used = True


CAM = [(0.0, 560, 1300, 1.08), (V["n1"] + 2.5, 560, 1330, 1.04), (T_OFF, 560, 1330, 1.04), (T_ENTER0, 700, 1400, 1.12), (V["t1"], 520, 1450, 1.22),
       (T_ON, 560, 1330, 1.0), (E("x3") + 0.3, 560, 1300, 1.04), (V["n3"] + 1.0, 600, 1250, 1.35), (T_PUFF + 0.6, 600, 1250, 1.38),
       (V["e1"], 680, 1400, 1.2), (T_SPLAT - 0.1, 600, 1350, 1.1), (T_SPLAT + 1.0, 560, 1330, 1.04), (V["s1"] + 0.3, 760, 1400, 1.3),
       (T_GIFT - 0.3, 560, 1450, 1.15), (T_BALL + 0.6, 560, 1250, 1.02), (DUR, 560, 1300, 1.04)]
SHAKES = [(T_ON, 18), (T_SPLAT, 22), (T_GIFT, 8)]


def camera(t):
    for (t0, ax, ay, az), (t1, bx, by, bz) in zip(CAM, CAM[1:]):
        if t0 <= t < t1:
            u = ease((t - t0) / max(1e-6, t1 - t0)); cx, cy, z = lerp(ax, bx, u), lerp(ay, by, u), lerp(az, bz, u); break
    else: cx, cy, z = CAM[-1][1:]
    cx += 5 * math.sin(t * 0.8) + 3 * math.sin(t * 2.3); cy += 4 * math.sin(t * 1.1 + 1)
    for kt, amp in SHAKES:
        if kt <= t < kt + 0.45:
            k = (1 - (t - kt) / 0.45) * amp; cx += math.sin(t * 95) * k; cy += math.cos(t * 83) * k
    if T_DISCO <= t: cy += 6 * math.sin(t * 6.3)
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
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z; c.sid = "festa"
    c.X = lambda x: (x - cx) * Z + W / 2; c.Y = lambda y: (y - cy) * Z + H / 2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    draw_scene(c, t)
    img = c.img
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(10)); img = ImageChops.add(ImageChops.add(img, c.glow), g2)
    if T_ON <= t < T_ON + 0.25:                                                   # lampo delle luci
        f = Image.new("RGB", (W, H), (255, 250, 235)); img = Image.blend(img, f, 0.6 * (1 - (t - T_ON) / 0.25))
    img = screen_splats(img, t)
    a = np.asarray(img).astype(np.float32)
    a = a + cv2.resize(cv2.GaussianBlur(cv2.resize(np.clip(a - 215, 0, 255) * 3.0, (W // 4, H // 4), interpolation=cv2.INTER_AREA), (0, 0), 3.5), (W, H)) * 0.18
    a = a + np.random.default_rng(i).normal(0, 2.0, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    img = Image.fromarray(np.clip(a * _VIG, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img, "RGBA")
    if t < 2.3:
        u = back(t / 0.35); al = int(255 * clamp((2.3 - t) / 0.4))
        text(d, "UNA SORPRESA?", W / 2, 250 - 10 * math.sin(t * 6), int(120 * clamp(max(0.6, u), 0, 1.0)), (255, 235, 90, al), (220, 40, 120, al), 13)
    subscribe_button(img, t, V["end"] + 0.9)
    return img.tobytes()


def _prep(p):
    try: MO.transition(*p); return None
    except Exception as e: return (p, str(e)[:80])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2)); print({k: round(v, 2) for k, v in V.items()})
        print({k: round(v, 2) for k, v in dict(T_OFF=T_OFF, T_ENTER0=T_ENTER0, T_ON=T_ON, T_PUFF=T_PUFF, T_BLOW=T_BLOW, T_SPLAT=T_SPLAT, T_GIFT=T_GIFT, T_BALL=T_BALL, T_DISCO=T_DISCO).items()})
    elif cmd == "prep":
        ps = precompute(); print(len(ps), "transizioni")
        with Pool(4) as pool:
            for r in pool.imap_unordered(_prep, ps):
                if r: print("manca", r)
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(round(float(ts) * FPS)))).save(f"/tmp/claude-0/prova/test_f_{ts}.png")
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
