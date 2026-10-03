#!/usr/bin/env python3
"""Bambini Ciao Ciao - "Puliamo il parco!" - animazione 2D renderizzata a codice (9:16, 1080x1920)."""
import math, sys, subprocess
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, K = 1080, 1920, 24, 2
DUR = 36.0
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ---------------------------------------------------------------- helpers
def lerp(a, b, u): return a + (b - a) * u
def ease(u): u = max(0, min(1, u)); return u * u * (3 - 2 * u)
def clamp(v, a=0, b=1): return max(a, min(b, v))

class Cv:
    def __init__(s, img): s.im = img; s.d = ImageDraw.Draw(img, "RGBA")
    def e(s, cx, cy, rx, ry, fill, out=None, w=0):
        s.d.ellipse([(cx-rx)*K, (cy-ry)*K, (cx+rx)*K, (cy+ry)*K], fill=fill, outline=out, width=max(0, int(w*K)))
    def p(s, pts, fill, out=None, w=0):
        s.d.polygon([(x*K, y*K) for x, y in pts], fill=fill, outline=out if w else None)
    def r(s, x0, y0, x1, y1, rad, fill, out=None, w=0):
        s.d.rounded_rectangle([x0*K, y0*K, x1*K, y1*K], radius=rad*K, fill=fill, outline=out, width=max(0, int(w*K)))
    def l(s, pts, col, w):
        pp = [(x*K, y*K) for x, y in pts]
        s.d.line(pp, fill=col, width=max(1, int(w*K)), joint="curve")
        rr = w*K/2
        for x, y in (pp[0], pp[-1]):
            s.d.ellipse([x-rr, y-rr, x+rr, y+rr], fill=col)
    def pie(s, cx, cy, rx, ry, a0, a1, fill):
        s.d.pieslice([(cx-rx)*K, (cy-ry)*K, (cx+rx)*K, (cy+ry)*K], a0, a1, fill=fill)
    def t(s, txt, x, y, size, fill, out=None, ow=0, anchor="mm"):
        f = ImageFont.truetype(FONT, int(size*K))
        s.d.text((x*K, y*K), txt, font=f, fill=fill, anchor=anchor,
                 stroke_width=int(ow*K), stroke_fill=out)

def rot(pts, ang, cx, cy):
    c, s_ = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    return [(cx + (x-cx)*c - (y-cy)*s_, cy + (x-cx)*s_ + (y-cy)*c) for x, y in pts]

# ---------------------------------------------------------------- background
def make_bg():
    img = Image.new("RGB", (W*K, H*K))
    d = ImageDraw.Draw(img)
    for y in range(0, 1300*K):  # cielo
        u = y / (1300*K)
        d.line([(0, y), (W*K, y)], fill=(int(lerp(110, 215, u)), int(lerp(190, 240, u)), int(lerp(250, 255, u))))
    for y in range(1230*K, H*K):  # prato
        u = (y - 1230*K) / ((H-1230)*K)
        d.line([(0, y), (W*K, y)], fill=(int(lerp(120, 70, u)), int(lerp(205, 160, u)), int(lerp(90, 60, u))))
    c = Cv(img)
    c.e(880, 250, 130, 130, (255, 240, 150, 90)); c.e(880, 250, 95, 95, (255, 226, 80))
    for i in range(12):  # raggi
        a = i * math.pi / 6
        c.l([(880+math.cos(a)*115, 250+math.sin(a)*115), (880+math.cos(a)*150, 250+math.sin(a)*150)], (255, 226, 80), 10)
    # colline
    c.e(150, 1330, 520, 260, (130, 205, 110)); c.e(820, 1350, 600, 250, (105, 190, 100))
    c.e(480, 1400, 700, 200, (95, 180, 90))
    # alberi
    for tx, ty, sc in ((110, 1330, 1.0), (975, 1300, 0.85)):
        c.r(tx-26*sc, ty-300*sc, tx+26*sc, ty, 10, (140, 90, 55))
        for dx, dy, r_ in ((0, -380, 120), (-90, -320, 90), (90, -330, 95), (-10, -470, 85)):
            c.e(tx+dx*sc, ty+dy*sc, r_*sc, r_*sc, (60, 160, 70), (40, 125, 55), 4)
    # staccionata
    for fx in range(-20, W+40, 62):
        c.r(fx, 1240, fx+34, 1345, 8, (250, 235, 205), (205, 180, 140), 3)
    c.r(-10, 1262, W+10, 1282, 6, (240, 220, 185), (205, 180, 140), 3)
    c.r(-10, 1308, W+10, 1328, 6, (240, 220, 185), (205, 180, 140), 3)
    # fiori sparsi
    for fx, fy, col in ((90, 1480, (255, 120, 150)), (990, 1520, (255, 210, 60)), (45, 1800, (255, 255, 255)),
                        (1035, 1820, (255, 120, 150)), (500, 1850, (255, 210, 60))):
        flower(c, fx, fy, 0.8, col)
    return img.resize((W*K, H*K))

def flower(c, x, y, s, col):
    c.l([(x, y), (x, y+38*s)], (60, 150, 60), 6*s)
    for i in range(5):
        a = i * 2*math.pi/5
        c.e(x+math.cos(a)*13*s, y+math.sin(a)*13*s, 11*s, 11*s, col)
    c.e(x, y, 8*s, 8*s, (255, 200, 40))

def cloud(c, x, y, s):
    for dx, dy, r_ in ((0, 0, 50), (55, -20, 60), (115, 0, 48), (60, 18, 55)):
        c.e(x+dx*s, y+dy*s, r_*s, r_*s*0.8, (255, 255, 255, 235))

# ---------------------------------------------------------------- bins & items
BINS = {"giallo": (600, (245, 200, 40), "PLASTICA"),
        "blu": (780, (60, 120, 220), "CARTA"),
        "marrone": (960, (140, 90, 55), "UMIDO")}
BIN_Y = 1425

def draw_bin(c, key, squish=0.0):
    x, col, lab = BINS[key]
    dk = tuple(int(v*0.7) for v in col)
    sx = 1 + squish*0.08; sy = 1 - squish*0.06
    w0, h0 = 78*sx, 190*sy
    top = BIN_Y - h0
    c.e(x, BIN_Y+4, w0+20, 14, (0, 0, 0, 60))
    c.p([(x-w0, top), (x+w0, top), (x+w0*0.86, BIN_Y), (x-w0*0.86, BIN_Y)], col, dk, 4)
    c.r(x-w0-8, top-24, x+w0+8, top+4, 10, dk)            # coperchio
    c.r(x-26, top-34, x+26, top-20, 6, dk)               # maniglia
    c.r(x-62, top+36, x+62, top+96, 12, (255, 255, 255, 235))
    c.t(lab, x, top+66, 24, dk)
    c.e(x-w0*0.7, BIN_Y, 14, 14, (50, 50, 55)); c.e(x+w0*0.7, BIN_Y, 14, 14, (50, 50, 55))

def draw_item(c, kind, x, y, ang=0, s=1.0):
    def R(pts): return rot([(x+px*s, y+py*s) for px, py in pts], ang, x, y)
    if kind == "bottle":
        c.p(R([(-20, -50), (20, -50), (20, 40), (-20, 40)]), (150, 215, 255, 235), (90, 160, 220), 3)
        c.p(R([(-10, -78), (10, -78), (14, -50), (-14, -50)]), (150, 215, 255, 235), (90, 160, 220), 3)
        c.p(R([(-11, -90), (11, -90), (11, -76), (-11, -76)]), (220, 50, 50))
        c.p(R([(-20, -10), (20, -10), (20, 14), (-20, 14)]), (255, 255, 255, 230))
    elif kind == "can":
        c.p(R([(-24, -36), (24, -36), (24, 36), (-24, 36)]), (200, 205, 215), (130, 135, 150), 3)
        c.p(R([(-24, -8), (24, -8), (24, 14), (-24, 14)]), (220, 60, 60))
    elif kind == "paper":
        pts = [(-34, -10), (-22, -34), (4, -38), (30, -26), (38, 4), (24, 32), (-6, 38), (-30, 24)]
        c.p(R(pts), (250, 250, 250), (170, 170, 180), 3)
        c.l(R([(-20, -12), (10, -4), (-6, 14)]), (180, 180, 195), 3)
    elif kind == "news":
        c.p(R([(-34, -26), (34, -26), (34, 26), (-34, 26)]), (235, 235, 225), (170, 170, 160), 3)
        for i in range(4): c.l(R([(-26, -14+i*10), (26, -14+i*10)]), (150, 150, 150), 3)
        c.p(R([(-28, -22), (-6, -22), (-6, -12), (-28, -12)]), (90, 90, 100))
    elif kind == "peel":
        for a in (-40, 0, 40):
            c.p(rot([(x, y+4), (x-14*s, y-34*s), (x, y-58*s), (x+14*s, y-34*s)], a+ang, x, y+4), (250, 215, 50), (190, 150, 20), 3)
        c.e(x, y+4, 8*s, 8*s, (120, 80, 30))
    elif kind == "core":
        c.e(x, y-20*s, 28*s, 22*s, (200, 70, 60)); c.e(x, y+20*s, 28*s, 22*s, (200, 70, 60))
        c.r(x-16*s, y-24*s, x+16*s, y+24*s, 8, (245, 235, 190), (190, 175, 120), 2)
        c.l([(x, y-40*s), (x+6*s, y-60*s)], (110, 70, 30), 5)

# ---------------------------------------------------------------- personaggi
SK = (205, 205, 215); SKO = (140, 140, 158)

def limbs(c, Q, s, st, arm_col, sleeve_col, shoulder_y, shoulder_x):
    for side, a in ((-1, st["al"]), (1, st["ar"])):
        sh = Q(side*shoulder_x, shoulder_y)
        dx, dy = side*math.sin(math.radians(a)), math.cos(math.radians(a))
        L = 105*s
        hd = (sh[0]+dx*L, sh[1]+dy*L)
        c.l([sh, hd], arm_col, 30*s)
        c.l([sh, (sh[0]+dx*L*0.35, sh[1]+dy*L*0.35)], sleeve_col, 38*s)
        c.e(hd[0], hd[1], 24*s, 24*s, arm_col)
    return None

def hand_pos(x, y, s, st, side):
    a = st["ar"] if side > 0 else st["al"]
    sh = (x + side*92*s, y - st["bob"] - 285*s)
    return (sh[0] + side*math.sin(math.radians(a))*105*s, sh[1] + math.cos(math.radians(a))*105*s)

def face_common(c, Q, s, st, eye_y, eye_dx, eye_rx, eye_ry, mouth_y, sad):
    for sx in (-1, 1):
        if st["blink"]:
            c.l([Q(sx*eye_dx-16, eye_y), Q(sx*eye_dx+16, eye_y)], (35, 30, 45), 5*s)
        else:
            c.e(*Q(sx*eye_dx, eye_y), eye_rx*s, eye_ry*s, (35, 30, 45))
            c.e(*Q(sx*eye_dx-6, eye_y-10), 8*s, 8*s, (255, 255, 255))
    if sad:
        for sx in (-1, 1):
            c.l([Q(sx*eye_dx+sx*26, eye_y-40), Q(sx*eye_dx-sx*18, eye_y-56)], (90, 80, 100), 5*s)
    m = st["mouth"]
    if m > 0.12:
        c.e(*Q(0, mouth_y), 26*s, (8+22*m)*s, (150, 40, 60))
        c.e(*Q(0, mouth_y+(6+14*m)), 16*s, (5+7*m)*s, (255, 130, 150))
    elif sad:
        c.l([Q(-24+i*6, mouth_y+8-14*math.sin(i/8*math.pi)*-1) for i in range(9)], (90, 40, 60), 5*s)
    else:
        c.l([Q(-30+i*7.5, mouth_y-8+16*(1-((i-4)/4)**2)) for i in range(9)], (90, 40, 60), 5*s)

def draw_mouse(c, x, y, s, st):
    yb = y - st["bob"]
    Q = lambda dx, dy: (x+dx*s, yb+dy*s)
    pts = [Q(-80-120*u/10, -105+34*math.sin(u/10*3+st["tail"])) for u in range(11)]
    c.l(pts, (230, 165, 175), 13*s)
    for sx in (-1, 1):
        c.r(*Q(sx*70-(0 if sx > 0 else 0)-34 if False else (sx*8 if sx > 0 else -78), -150), *Q(78 if sx > 0 else -8, -28), 26, (250, 205, 60), (200, 150, 20), 3)
    c.e(x-42*s, y-14*s-st["lift_l"]*s, 40*s, 20*s, SK, SKO, 3)
    c.e(x+42*s, y-14*s-st["lift_r"]*s, 40*s, 20*s, SK, SKO, 3)
    c.e(*Q(0, -235), 98*s, 112*s, (70, 190, 190), (40, 140, 150), 3)
    for yy in range(-330, -140, 34):
        half = 98*math.sqrt(max(0, 1-((yy+235)/112)**2))
        c.l([Q(-half+6, yy), Q(half-6, yy)], (40, 150, 160), 14*s)
    c.e(*Q(0, -150), 100*s, 78*s, (250, 205, 60), (200, 150, 20), 3)
    c.r(*Q(-64, -262), *Q(64, -150), 22*s, (250, 205, 60), (200, 150, 20), 3)
    c.l([Q(-46, -262), Q(-74, -318)], (250, 205, 60), 17*s); c.l([Q(46, -262), Q(74, -318)], (250, 205, 60), 17*s)
    c.e(*Q(-46, -262), 7*s, 7*s, (150, 90, 40)); c.e(*Q(46, -262), 7*s, 7*s, (150, 90, 40))
    c.r(*Q(-26, -236), *Q(26, -190), 8*s, (225, 60, 50), (170, 30, 30), 2)
    limbs(c, Q, s, st, SK, (70, 190, 190), -285, 92)
    for sx in (-1, 1):  # orecchie
        c.e(*Q(sx*108, -488), 68*s, 68*s, SK, SKO, 4)
        c.e(*Q(sx*108, -488), 42*s, 42*s, (255, 170, 190))
    c.e(*Q(0, -395), 128*s, 118*s, SK, SKO, 4)
    c.e(*Q(0, -356), 72*s, 56*s, (238, 234, 242))
    for sx in (-1, 1):
        c.e(*Q(sx*86, -358), 22*s, 15*s, (255, 150, 170, 150))
        for dy in (-8, 8):
            c.l([Q(sx*60, -358+dy*0.5), Q(sx*128, -366+dy*2.2)], (130, 130, 145), 3*s)
    face_common(c, Q, s, st, -408, 46, 22, 29, -338, st["sad"])
    c.e(*Q(0, -382), 19*s, 14*s, (255, 130, 155), (210, 90, 115), 2)

def draw_chip(c, x, y, s, st):
    yb = y - st["bob"]
    Q = lambda dx, dy: (x+dx*s, yb+dy*s)
    FUR = (205, 115, 55); FO = (150, 80, 35); CR = (250, 226, 188)
    sw = math.sin(st["tail"])*10
    for dx, dy, rx, ry in ((-125+sw, -180, 70, 105), (-140+sw*1.5, -320, 82, 95), (-100+sw*2, -440, 62, 70)):
        c.e(*Q(dx, dy), rx*s, ry*s, FUR, FO, 4)
    c.e(*Q(-130+sw*1.4, -320), 40*s, 60*s, (235, 150, 85))
    c.e(x-40*s, y-14*s-st["lift_l"]*s, 38*s, 20*s, FUR, FO, 3)
    c.e(x+40*s, y-14*s-st["lift_r"]*s, 38*s, 20*s, FUR, FO, 3)
    c.e(*Q(0, -200), 90*s, 112*s, FUR, FO, 4)
    c.e(*Q(0, -185), 58*s, 82*s, CR)
    limbs(c, Q, s, st, FUR, FUR, -270, 84)
    for sx in (-1, 1):
        c.e(*Q(sx*80, -488), 36*s, 50*s, FUR, FO, 4); c.e(*Q(sx*80, -484), 20*s, 30*s, (255, 190, 170))
        c.l([Q(sx*80, -532), Q(sx*88, -562)], FO, 5*s)
    c.e(*Q(0, -392), 120*s, 108*s, FUR, FO, 4)
    c.e(*Q(0, -352), 66*s, 50*s, CR)
    for sx in (-1, 1): c.e(*Q(sx*84, -356), 20*s, 14*s, (255, 160, 140, 150))
    face_common(c, Q, s, st, -405, 44, 21, 28, -322, st["sad"])
    c.e(*Q(0, -374), 17*s, 13*s, (90, 50, 30))
    c.r(*Q(-11, -362), *Q(0, -340), 3*s, (255, 255, 255), (160, 150, 140), 2)
    c.r(*Q(0, -362), *Q(11, -340), 3*s, (255, 255, 255), (160, 150, 140), 2)
    c.e(*Q(0, -300), 90*s, 30*s, (160, 220, 60), (110, 170, 30), 3)  # sciarpa
    c.r(*Q(22, -300), *Q(66, -212), 12*s, (160, 220, 60), (110, 170, 30), 3)
    for i in range(3): c.l([Q(24, -280+i*24), Q(64, -280+i*24)], (110, 170, 30), 5*s)

def draw_spike(c, x, y, s, st):
    yb = y - st["bob"]
    Q = lambda dx, dy: (x+dx*s, yb+dy*s)
    DK = (110, 70, 40); LT = (150, 100, 60); TAN = (192, 152, 102); CR = (245, 222, 188)
    cx, cy = Q(0, -250)
    for i in range(-9, 10):  # aculei
        a = math.radians(-90 + i*11)
        r0, r1 = 105*s, 175*s + (i % 2)*18*s
        a1, a2 = a-0.11, a+0.11
        c.p([(cx+math.cos(a1)*r0*0.95, cy+math.sin(a1)*r0*1.1), (cx+math.cos(a)*r1, cy+math.sin(a)*r1*1.05),
             (cx+math.cos(a2)*r0*0.95, cy+math.sin(a2)*r0*1.1)], DK, (70, 40, 20), 2)
    c.e(x-40*s, y-14*s-st["lift_l"]*s, 38*s, 20*s, TAN, DK, 3)
    c.e(x+40*s, y-14*s-st["lift_r"]*s, 38*s, 20*s, TAN, DK, 3)
    c.e(*Q(0, -205), 92*s, 112*s, TAN, DK, 4)
    c.e(*Q(0, -190), 60*s, 82*s, CR)
    limbs(c, Q, s, st, TAN, TAN, -270, 86)
    for sx in (-1, 1): c.e(*Q(sx*96, -450), 32*s, 32*s, LT, DK, 3)
    c.e(*Q(0, -390), 118*s, 104*s, (238, 208, 168), DK, 4)
    c.e(*Q(0, -360), 56*s, 44*s, CR)
    c.pie(*Q(6, -432), 124*s, 78*s, 180, 360, (50, 110, 220))
    c.e(*Q(6, -432), 124*s, 6*s, (35, 85, 180))
    c.e(*Q(60, -428), 82*s, 15*s, (35, 85, 180)); c.e(*Q(8, -508), 12*s, 12*s, (255, 220, 60))
    for sx in (-1, 1): c.e(*Q(sx*80, -360), 18*s, 13*s, (255, 160, 150, 140))
    face_common(c, Q, s, st, -395, 42, 19, 26, -318, st["sad"])
    c.e(*Q(0, -370), 22*s, 17*s, (60, 40, 35))
    c.e(*Q(-6, -376), 6*s, 5*s, (255, 255, 255, 200))

DRAW = {"mouse": draw_mouse, "chip": draw_chip, "spike": draw_spike}
SCALE = {"mouse": 0.92, "chip": 0.88, "spike": 0.86}

# ---------------------------------------------------------------- storia
# keyframes (t, x, y) per personaggio; fra due keyframe diversi il personaggio cammina
KF = {
 "mouse": [(0, -170, 1620), (2.0, 300, 1620), (12.0, 300, 1620), (13.6, 215, 1690), (13.9, 215, 1690),
           (16.3, 540, 1555), (17.4, 540, 1555), (22.6, 690, 1700), (23.0, 690, 1700),
           (24.4, 560, 1555), (25.0, 560, 1555), (27.2, 540, 1650), (40, 540, 1650)],
 "chip":  [(6.8, 1250, 1690), (8.8, 690, 1690), (13.0, 690, 1690), (15.6, 440, 1765), (15.9, 440, 1765),
           (18.3, 760, 1600), (19.2, 760, 1600), (21.6, 860, 1750), (21.9, 860, 1750),
           (24.9, 790, 1600), (25.6, 790, 1600), (27.2, 330, 1665), (40, 330, 1665)],
 "spike": [(7.8, 1250, 1735), (9.6, 890, 1735), (14.0, 890, 1735), (18.0, 330, 1655), (18.3, 330, 1655),
           (20.9, 935, 1600), (21.8, 935, 1600), (23.4, 585, 1660), (23.7, 585, 1660),
           (25.8, 925, 1600), (26.6, 925, 1600), (28.0, 760, 1665), (40, 760, 1665)],
}
# oggetti: (tipo, x, y, personaggio, t_raccolta, t_lancio, cestino)
ITEMS = [
 ("bottle", 190, 1700, "mouse", 13.9, 16.5, "giallo"),
 ("news",   440, 1775, "chip",  15.9, 18.6, "blu"),
 ("peel",   330, 1655, "spike", 18.3, 21.1, "marrone"),
 ("can",    690, 1710, "mouse", 23.0, 24.5, "giallo"),
 ("paper",  860, 1765, "chip",  21.9, 25.3, "blu"),
 ("core",   585, 1665, "spike", 23.7, 26.1, "marrone"),
 ("paper",  820, 1860, "spike", -1, -1, None),   # decorativi sparsi, raccolti insieme agli altri
]
ITEMS = ITEMS[:6]
FLY = 0.55

# voci: (chiave, start, personaggio, testo, durata)
VOICES = [
 ("m1", 0.6, "mouse", "Oh no! Quanti rifiuti nel parco!", 2.58),
 ("m2", 3.6, "mouse", "Chiamiamo gli amici! Chip! Spike!", 2.95),
 ("c1", 7.6, "chip", "Eccomi!", 0.83),
 ("s1", 8.6, "spike", "Siamo qui!", 1.04),
 ("m3", 10.2, "mouse", "Puliamo tutto insieme!", 1.7),
 ("m4", 14.5, "mouse", "La bottiglia va nel giallo!", 2.03),
 ("c2", 17.0, "chip", "La carta va nel blu!", 1.64),
 ("s2", 19.1, "spike", "La buccia va nel marrone!", 1.97),
 ("m5", 22.0, "mouse", "Bravissimi! Ancora un po'!", 2.2),
 ("m6", 27.7, "mouse", "Il parco è pulito!", 1.55),
 ("c3", 29.6, "chip", "Evviva!", 0.85),
 ("s3", 30.4, "spike", "Grazie amici!", 1.28),
 ("m7", 32.0, "mouse", "Ciao ciao bambini!", 1.53),
]
SPK_COL = {"mouse": (255, 200, 60), "chip": (255, 150, 90), "spike": (120, 180, 255)}

def interp(kf, t):
    if t <= kf[0][0]: return kf[0][1], kf[0][2], False, 1
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        if t0 <= t <= t1:
            u = ease((t-t0)/(t1-t0)) if (x0, y0) != (x1, y1) else 0
            mv = (x0, y0) != (x1, y1)
            return lerp(x0, x1, u), lerp(y0, y1, u), mv, (1 if x1 >= x0 else -1)
    return kf[-1][1], kf[-1][2], False, 1

def char_state(name, t):
    x, y, walking, dirn = interp(KF[name], t)
    st = dict(al=12, ar=12, mouth=0, blink=False, sad=False, bob=0, lift_l=0, lift_r=0, tail=t*3, dir=dirn)
    ph = t * 11
    if walking:
        st["bob"] = abs(math.sin(ph)) * 14
        st["lift_l"] = max(0, math.sin(ph)) * 22; st["lift_r"] = max(0, -math.sin(ph)) * 22
        st["al"] = 18 + math.sin(ph) * 22; st["ar"] = 18 - math.sin(ph) * 22
    else:
        st["bob"] = (math.sin(t*3 + hash(name) % 7) + 1) * 3
    if (t*0.77 + hash(name) % 5) % 3.3 < 0.12: st["blink"] = True
    for k, t0, who, txt, dur in VOICES:
        if who == name and t0 <= t <= t0 + dur:
            st["mouth"] = 0.5 + 0.5 * math.sin(t*16 + 1) if math.sin(t*16) > -0.2 else 0.05
    # pose speciali
    if name == "mouse":
        if t < 3.3 and t > 2.2: st["sad"] = True; st["al"] = st["ar"] = 100
        if 3.8 <= t <= 6.8: st["ar"] = 150; st["al"] = 150
    if 10.2 <= t <= 12 and name == "mouse": st["ar"] = 125
    if t >= 27.5 and not walking:
        w = math.sin(t*7 + (0 if name == "mouse" else 2 if name == "chip" else 4))
        st["al"] = 155 + w*12; st["ar"] = 155 - w*12
        st["bob"] = abs(math.sin(t*5 + hash(name) % 3)) * 24
    return x, y, st

def wave_arm(name, st, t):
    """Braccio che porta/lancia un oggetto."""
    for it in ITEMS:
        if it[3] != name: continue
        _, _, _, _, tp, tl, _ = it
        if tp - 0.3 <= t < tp:                                    # si china a prendere
            st["ar"] = 40 + 60*ease((t-(tp-0.3))/0.3); st["bob"] -= 8
        elif tp <= t < tl - 0.25:
            st["ar"] = 70; st["al"] = max(st["al"]*0.5, 14)       # porta in mano
        elif tl - 0.25 <= t < tl:
            st["ar"] = lerp(70, 150, ease((t-(tl-0.25))/0.25))    # carica il lancio
        elif tl <= t < tl + 0.3:
            st["ar"] = lerp(150, 20, ease((t-tl)/0.3))

def bin_squish(t):
    out = {}
    for k in BINS:
        v = 0
        for it in ITEMS:
            if it[6] == k:
                tl = it[5] + FLY
                if tl <= t < tl + 0.45: v = max(v, math.sin((t-tl)/0.45*math.pi) * (1-(t-tl)/0.45))
        out[k] = v
    return out

# ---------------------------------------------------------------- frame
BG = None
def get_bg():
    global BG
    if BG is None: BG = make_bg()
    return BG

SPARK = []

def frame(i):
    t = i / FPS
    img = get_bg().copy()
    c = Cv(img)
    # nuvole che scorrono
    for cx, cy, sp, sc in ((100, 230, 14, 1.0), (520, 420, 9, 0.8), (800, 130, 11, 0.7)):
        cloud(c, (cx + t*sp) % (W+400) - 200, cy, sc)
    # cestini
    sq = bin_squish(t)
    for k in BINS: draw_bin(c, k, sq[k])
    # oggetti a terra
    for kind, x, y, who, tp, tl, b in ITEMS:
        if t < tp:
            if t < 12.5 or True:
                draw_item(c, kind, x, y, ang=(x*7) % 50 - 25)
    # personaggi, ordinati per y
    chars = []
    for name in ("mouse", "chip", "spike"):
        if name == "chip" and t < 6.5: continue
        if name == "spike" and t < 7.5: continue
        x, y, st = char_state(name, t)
        wave_arm(name, st, t)
        chars.append((y, name, x, st))
    for y, name, x, st in sorted(chars):
        s = SCALE[name]
        c.e(x, y+2, 70*s, 16*s, (0, 0, 0, 55))
        DRAW[name](c, x, y, s, st)
        # oggetto in mano
        for kind, ix, iy, who, tp, tl, b in ITEMS:
            if who == name and tp <= t < tl:
                hx, hy = hand_pos(x, y, s, st, 1)
                draw_item(c, kind, hx+10, hy-22, ang=math.sin(t*9)*8, s=0.8)
    # oggetti in volo
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if tl <= t < tl + FLY:
            x, y, st = char_state(who, tl)
            s = SCALE[who]
            hx, hy = hand_pos(x, y, s, st, 1)
            bx, by = BINS[b][0], BIN_Y - 215
            u = (t - tl) / FLY
            px, py = lerp(hx, bx, u), lerp(hy, by, u) - 240*math.sin(u*math.pi)
            draw_item(c, kind, px, py, ang=u*540, s=0.8*(1-0.3*u))
        if tl + FLY <= t < tl + FLY + 0.5:  # stelline
            u = (t-tl-FLY)/0.5
            bx = BINS[b][0]
            for k in range(6):
                a = k*math.pi/3 + 0.4
                c.e(bx+math.cos(a)*(30+90*u), BIN_Y-230+math.sin(a)*(30+90*u)-40*u, 10*(1-u)+2, 10*(1-u)+2, (255, 235, 90, int(255*(1-u))))
    # fine: fiori e farfalle
    if t > 26.2:
        g = ease((t-26.2)/2.0)
        for k, (fx, fy, col) in enumerate(((140, 1640, (255, 110, 150)), (300, 1800, (255, 220, 70)), (460, 1700, (255, 255, 255)),
                                           (640, 1790, (190, 140, 255)), (800, 1660, (255, 110, 150)), (980, 1760, (255, 220, 70)),
                                           (80, 1850, (190, 140, 255)), (560, 1880, (255, 110, 150)))):
            flower(c, fx, fy - 20, 1.3*g, col)
        for k in range(4):
            bx = 200 + k*220 + math.sin(t*1.7 + k)*70
            by = 1000 + k*60 + math.cos(t*2.3 + k)*50
            wv = abs(math.sin(t*14 + k))
            col = ((255, 140, 200), (255, 190, 70), (140, 200, 255), (200, 160, 255))[k]
            c.e(bx-18*wv-4, by, 20*wv+4, 26, col); c.e(bx+18*wv+4, by, 20*wv+4, 26, col)
            c.l([(bx, by-12), (bx, by+14)], (80, 60, 70), 5)
        for k in range(10):  # coriandoli
            cx_ = (k*113 + 40) % W; cy_ = ((t-27.2)*260 + k*170) % 1500 + 200
            if t > 27.2:
                c.e(cx_ + math.sin(t*3+k)*30, cy_, 9, 9, ((255, 120, 150), (255, 220, 70), (120, 200, 255), (160, 230, 120))[k % 4])
    # sottotitolo
    for k, t0, who, txt, dur in VOICES:
        if t0 - 0.05 <= t <= t0 + dur + 0.35:
            a = int(255 * min(1, (t-t0+0.05)/0.15))
            f = ImageFont.truetype(FONT, 72*K)
            bb = c.d.textbbox((0, 0), txt, font=f, anchor="mm", stroke_width=6*K)
            tw = (bb[2]-bb[0]) / K
            if tw > 960:  # va a capo
                words = txt.split(); half = len(words)//2
                lines = [" ".join(words[:half]), " ".join(words[half:])]
            else: lines = [txt]
            yy = 360 if len(lines) == 1 else 320
            for ln in lines:
                c.t(ln, W/2, yy, 72, (255, 255, 255, a), (60, 40, 20, a), 7)
                yy += 90
            c.e(W/2, 215, 24, 24, SPK_COL[who], (60, 40, 20), 4)
            break
    # titolo iniziale
    if t < 3:
        a = int(255 * min(1, (3-t)/0.6))
        c.t("PULIAMO IL PARCO!", W/2, 140, 70, (255, 255, 255, a), (230, 90, 60, a), 10)
    # schermata finale
    if t > 33.2:
        u = ease((t-33.2)/0.6)
        ov = Image.new("RGBA", (W*K, H*K), (255, 245, 210, int(235*u)))
        img = Image.alpha_composite(img.convert("RGBA"), ov); c = Cv(img)
        by = 700 + (1-u)*60
        c.t("Ricicla anche tu!", W/2, by, 86, (60, 160, 70), (255, 255, 255), 8)
        for j, (k, col) in enumerate((("giallo", BINS["giallo"][1]), ("blu", BINS["blu"][1]), ("marrone", BINS["marrone"][1]))):
            c.e(240+j*300, by+170, 70, 70, col, (255, 255, 255), 6)
        c.t("Plastica  ·  Carta  ·  Umido", W/2, by+330, 52, (90, 70, 50))
        c.t("Bambini Ciao Ciao", W/2, by+520, 92, (230, 90, 60), (255, 255, 255), 8)
        c.t("Un nuovo video ogni settimana!", W/2, by+620, 46, (110, 90, 70))
        draw_mouse(c, W/2, 1650, 1.05, dict(al=150, ar=150+math.sin(t*8)*10, mouth=0, blink=False, sad=False,
                                            bob=abs(math.sin(t*5))*18, lift_l=0, lift_r=0, tail=t*3))
    out = img.convert("RGB").resize((W, H), Image.LANCZOS)
    return out.tobytes()

if __name__ == "__main__":
    if sys.argv[1] == "test":
        for ts in sys.argv[2:]:
            i = int(float(ts)*FPS)
            Image.frombytes("RGB", (W, H), frame(i)).save(f"test_{ts}.png")
    else:
        N = int(DUR*FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                               "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17",
                               "-preset", "medium", "video_muto.mp4"], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
