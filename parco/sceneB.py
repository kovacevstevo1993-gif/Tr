"""Short B: 'Chip e il tamburo' - Chip cammina verso la camera, trova un tamburo, suona; finale col topolino in scena."""
import json, os, math
from PIL import Image, ImageDraw, ImageFilter
import engine_hooks as E
DUR = 14.8; AUDIO = "audioB"; SUBS = True; NO_BINS = True
HERE = os.path.dirname(os.path.abspath(__file__))
_D = json.load(open(os.path.join(HERE, AUDIO, "durate.json")))
_V = [("n1", 3.0, "narr", "Chip ha trovato un tamburo!"), ("b1", 6.2, "chip", "Tum, tum, tum!"), ("b2", 9.2, "chip", "Evviva!"),
      ("end", 10.7, "mouse", "Bambini Ciao Ciao! Iscrivetevi al canale!")]
VOICES = [(k, t, w, x, _D[k]) for k, t, w, x in _V]
SPK_COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 180), "spike": (200, 225, 255)}
SUB_Y = lambda t: 300
persp = lambda y: 0.40 + (y-1250)/510*0.74
CHARS = {"chip": 0, "mouse": 9.5}
KF = {"chip": [(0, 560, 1250), (3.0, 540, 1720), (60, 540, 1720)],
      "mouse": [(9.5, -160, 1700), (10.7, 250, 1700), (60, 250, 1700)]}
ITEMS = []
FORCE_MOUTH = [("chip", 3.35, 4.3, 1), ("chip", 5.0, 5.3, 1)]
BEATS = [6.35, 6.8, 7.25] + [8.0+0.444*k for k in range(0, 15)]
BOUNCE = [("chip", 7.867, 14.4, 0.03), ("mouse", 10.7, 14.8, 0.02)]
JUMP = [("chip", 9.2, 10.0)]
SHAKE = [(5.5, 5, 0.25)]
SHOTS = [(0.0, 3.0, (540, 1250, 1.0), (540, 1450, 1.3)), (3.0, 5.2, (540, 1500, 1.5), (540, 1500, 1.65)),
         (5.2, 6.0, (540, 1600, 2.2), (540, 1560, 2.3)), (6.0, 10.4, (540, 1480, 1.9), (540, 1450, 2.0)),
         (10.4, 14.8, (520, 1420, 1.55), (520, 1400, 1.65))]
TP = 5.45                      # Chip raccoglie il tamburo

def mouse_sprite(t, ml, b):
    return "assets/v/mouse_braccia_su.png" if t >= 12.5 else None

_drum = None
def drum_sprite():
    global _drum
    if _drum is None:
        w, h, Sx = 420, 340, 3; cv = Image.new("RGBA", (w*Sx, h*Sx), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
        x0, x1 = 0.06*w*Sx, 0.94*w*Sx; ytop, ybot = 0.26*h*Sx, 0.80*h*Sx; ry = 0.17*h*Sx
        for xi in range(int(x0), int(x1)):                          # corpo cilindrico con gradiente
            u = (xi-x0)/(x1-x0); sh = 0.62+0.5*max(0.0, math.sin(math.pi*u))**0.7
            col = (min(255, int(190*sh)), min(255, int(120*sh)), min(255, int(62*sh)), 255); d.line([(xi, ytop), (xi, ybot)], fill=col)
        d.ellipse([x0, ybot-ry, x1, ybot+ry], fill=(150, 92, 48, 255))
        d.rectangle([x0, ytop, x1, ybot], fill=None)
        for xi in range(int(x0), int(x1)):
            u = (xi-x0)/(x1-x0); sh = 0.62+0.5*max(0.0, math.sin(math.pi*u))**0.7
            d.line([(xi, ytop), (xi, ybot)], fill=(min(255, int(190*sh)), min(255, int(120*sh)), min(255, int(62*sh)), 255))
        d.pieslice([x0, ybot-ry, x1, ybot+ry], 0, 180, fill=(170, 106, 56, 255))
        for k in range(9):                                          # corde rosse a zig-zag
            xa = x0+(x1-x0)*(k/8.0); xb = x0+(x1-x0)*((k+0.5)/8.0)
            d.line([(xa, ytop+ry*0.5), (xb, ybot)], fill=(205, 45, 45, 255), width=int(5*Sx)); d.line([(xb, ybot), (x0+(x1-x0)*((k+1)/8.0), ytop+ry*0.5)], fill=(205, 45, 45, 255), width=int(5*Sx))
        d.ellipse([x0-4*Sx, ytop-ry, x1+4*Sx, ytop+ry], fill=(120, 75, 40, 255))        # bordo
        d.ellipse([x0+8*Sx, ytop-ry+7*Sx, x1-8*Sx, ytop+ry-7*Sx], fill=(246, 232, 196, 255))   # pelle
        d.ellipse([x0+50*Sx, ytop-ry*0.6, x0+190*Sx, ytop-ry*0.1], fill=(255, 250, 225, 160))   # riflesso
        _drum = cv.resize((w, h), Image.LANCZOS)
    return _drum

def _stick(c, px, py, hit_h, ang, s):
    L = 150*s; x2 = px+math.sin(math.radians(ang))*L; y2 = py-math.cos(math.radians(ang))*L*hit_h
    c.d.line([(px, py), (x2, y2)], fill=(232, 205, 150), width=max(2, int(9*s)))
    c.d.ellipse([x2-7*s, y2-7*s, x2+7*s, y2+7*s], fill=(205, 70, 60))

def char_fx(c, name, x, y, h, hop, t):
    if name != "chip": return
    k = c.Z; cx0, cy0 = c.X(x - 0.05*h), c.Y(y - hop - 0.27*h)
    if t < TP-0.15:                         # tamburo a terra (scintilla)
        gx, gy = c.X(540), c.Y(1800); dw = 260*k; sp = drum_sprite().resize((int(dw), int(dw*340/420)), Image.LANCZOS)
        c.img.paste(sp, (int(gx-sp.width/2), int(gy-sp.height)), sp)
        E.sparkles(c, 540, 1740, 3.2, 2.2, n=10, spread=100, size=16, seed=4); return
    hit = 0.0; sq = 1.0
    for th in E.S.BEATS:
        if 0 <= t-th < 0.12: sq = 1+0.06*(1-(t-th)/0.12); hit = 1
    dw = 0.46*h*k*sq; sp = drum_sprite().resize((int(dw), int(dw*340/420)), Image.LANCZOS)
    pop = E.ease((t-(TP-0.1))/0.3)
    c.img.paste(sp, (int(cx0-sp.width/2), int(cy0-sp.height*0.5+(1-pop)*40*k)), sp)
    for i, sgn in enumerate((-1, 1)):                          # bacchette + zampette
        hits = E.S.BEATS[i::2]; up = 1.0; ang = sgn*28
        for th in hits:
            if -0.3 <= t-th <= 0.14:
                u = (t-th+0.3)/0.3 if t < th else 1-(t-th)/0.14*1.0
                up = 1 - 0.85*E.ease(min(1, max(0, u)))
        sx_ = cx0 + sgn*0.21*h*k; sy_ = cy0 - 0.02*h*k
        _stick(c, sx_, sy_, up*0.8+0.2, -sgn*22+sgn*10*(1-up), h*k/500)
        c.d.ellipse([sx_-0.03*h*k, sy_-0.03*h*k, sx_+0.03*h*k, sy_+0.03*h*k], fill=(205, 118, 58), outline=(150, 80, 35), width=max(1, int(3*k)))
    if t >= 6.0: E.notes(c, x, y-0.45*h, 6.0, 8.5, n=7, seed=3)

def front_fx(c):
    t = c.t
    if 5.3 <= t < 5.9: E.sparkles(c, 540, 1500, 5.3, 0.6, n=20, spread=160, size=22, seed=5)
    if 9.2 <= t: E.confetti(c, 9.2, 12)
    if 9.2 <= t < 10.2: E.sparkles(c, 540, 1500, 9.2, 1.0, n=24, spread=200, size=24, seed=6)

def overlay(img, t):
    E.subscribe_button(img, t, 12.4, cy=1450)
