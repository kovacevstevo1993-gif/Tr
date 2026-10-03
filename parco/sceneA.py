"""Short A: 'La magia dei cestini' - 3 cicli azione -> magia -> reazione, finale col topolino che saluta in scena."""
import json, os, math
from PIL import Image
import engine_hooks as E            # funzioni effetto (importate in modo lazy da engine)
DUR = 27.8; AUDIO = "audioA"; SUBS = True
HERE = os.path.dirname(os.path.abspath(__file__))
_D = json.load(open(os.path.join(HERE, AUDIO, "durate.json")))
_V = [("n1", 0.15, "narr", "La bottiglia di plastica va nel cestino giallo... e succede la magia!"),
      ("w1", 6.65, "chip", "Wow!"),
      ("n2", 7.95, "narr", "La carta va nel cestino blu... e succede la magia!"),
      ("w2", 13.5, "spike", "Oooh!"),
      ("n3", 15.0, "narr", "La buccia di banana va nel cestino marrone... ed ecco la magia!"),
      ("w3", 19.3, "chip", "Evviva!"), ("w4", 20.2, "spike", "Evviva!"),
      ("end", 22.9, "mouse", "Bambini Ciao Ciao! Iscrivetevi al canale!")]
VOICES = [(k, t, w, x, _D[k]) for k, t, w, x in _V]
SPK_COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 180), "spike": (200, 225, 255)}
SUB_Y = lambda t: 300
CHARS = {"mouse": 0, "chip": 0, "spike": 0}
KF = {"mouse": [(0, -140, 1700), (2.2, 300, 1706), (2.35, 300, 1706), (2.9, 300, 1706), (3.9, 300, 1500), (5.0, 300, 1500), (5.8, 330, 1580),
                (20.6, 330, 1580), (21.4, 540, 1660), (60, 540, 1660)],
      "chip": [(0, 620, 1700), (8.3, 620, 1700), (9.2, 560, 1790), (9.7, 560, 1790), (10.8, 560, 1500), (12.0, 560, 1500), (12.8, 600, 1680),
               (19.0, 600, 1680), (20.4, 310, 1700), (60, 310, 1700)],
      "spike": [(0, 880, 1740), (15.4, 880, 1740), (16.0, 840, 1750), (16.5, 840, 1750), (18.0, 800, 1500), (19.4, 800, 1500),
                (20.8, 780, 1720), (60, 780, 1720)]}
ITEMS = [("bottle", 300, 1706, "mouse", 2.6, 4.3, "giallo"), ("news", 560, 1790, "chip", 9.8, 10.9, "blu"), ("peel", 840, 1750, "spike", 16.3, 18.45, "marrone")]
JUMP = [("all", 19.1, 22.4), ("chip", 22.4, 27.8), ("spike", 22.4, 27.8)]
BOUNCE = [("mouse", 22.4, 27.8, 0.025)]
FORCE_MOUTH = [("chip", 6.4, 6.65, 2), ("spike", 13.3, 13.5, 2)]
SHAKE = [(4.85, 7, 0.3), (11.45, 6, 0.3), (19.0, 8, 0.35)]
SHOTS = [(0.0, 1.9, (300, 1640, 2.8), (300, 1630, 3.1)), (1.9, 3.9, (330, 1600, 1.4), (300, 1520, 1.5)),
         (3.9, 5.0, (300, 1330, 1.55), (300, 1330, 1.7)), (5.0, 6.6, (540, 1100, 1.0), (540, 1150, 1.08)),
         (6.6, 7.9, (620, 1450, 2.2), (620, 1440, 2.3)), (7.9, 9.6, (560, 1730, 2.8), (560, 1730, 3.1)),
         (9.6, 11.5, (560, 1600, 1.5), (560, 1540, 1.6)), (11.5, 13.4, (540, 1050, 1.0), (540, 1100, 1.05)),
         (13.4, 14.9, (860, 1450, 2.2), (850, 1440, 2.3)), (14.9, 16.3, (840, 1700, 2.8), (840, 1700, 3.1)),
         (16.3, 18.0, (840, 1620, 1.5), (800, 1520, 1.5)), (18.0, 19.1, (800, 1350, 1.6), (800, 1350, 1.7)),
         (19.1, 21.2, (540, 1350, 1.0), (540, 1400, 1.06)), (21.2, 22.4, (540, 1450, 1.15), (540, 1450, 1.2)),
         (22.4, 27.8, (540, 1330, 1.35), (540, 1300, 1.5))]

def mouse_sprite(t, ml, b):
    if 19.1 <= t < 22.4 or t >= 25.3: return "assets/v/mouse_braccia_su.png"
    return None

BF_COL = [((255, 140, 200), (255, 230, 120)), ((120, 190, 255), (255, 255, 255)), ((255, 190, 70), (255, 120, 90)),
          ((190, 140, 255), (255, 210, 240)), ((120, 220, 150), (255, 250, 150)), ((255, 120, 120), (255, 220, 160))]
FLOWERS = [(120, 1660, (255, 110, 150), 52), (230, 1560, (255, 220, 70), 46), (340, 1840, (190, 140, 255), 58), (440, 1690, (255, 255, 255), 50),
           (610, 1775, (255, 110, 150), 56), (700, 1565, (255, 220, 70), 46), (770, 1860, (190, 140, 255), 54), (905, 1690, (255, 255, 255), 52),
           (1005, 1810, (255, 110, 150), 58), (70, 1860, (255, 220, 70), 50), (490, 1560, (190, 140, 255), 44), (595, 1625, (255, 220, 70), 44),
           (180, 1740, (255, 255, 255), 50), (960, 1580, (255, 110, 150), 44), (390, 1585, (255, 110, 150), 42), (820, 1620, (190, 140, 255), 46)]

def back_fx0(c):
    E.rainbow(c, 4.85)

def back_fx1(c):
    for k, (x, y, col, sz) in enumerate(FLOWERS):
        delay = 19.0 + 0.1 + math.hypot(x-810, y-1340)/1000*1.0
        E.flower(c, x, y, sz, (c.t-delay)/0.7, col, sway=math.sin(c.t*2+k))

def front_fx(c):
    t = c.t
    E.sparkles(c, 300, 1700, 0.1, 1.8, n=9, spread=70, size=14, seed=1); E.sparkles(c, 560, 1790, 7.9, 1.7, n=9, spread=70, size=14, seed=2)
    E.sparkles(c, 840, 1750, 14.9, 1.4, n=9, spread=70, size=14, seed=3)
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        ti = tl + E.FLY; E.sparkles(c, E.BIN_X[b], E.BIN_Y-E.BIN_H, ti, 1.0, n=28, spread=190, rise=90, size=28, seed=ti)
    E.sparkles(c, 540, 760, 5.0, 3.2, n=30, spread=430, rise=-40, size=18, seed=9)
    # farfalle dal cestino blu
    if t >= 11.45:
        for k in range(6):
            tk = 11.45 + k*0.28
            if t < tk: continue
            u = t - tk; ang = k*1.05; r = min(60+u*95, 380)
            bx = 540 + math.cos(ang+u*0.9)*r*(1.1 if k % 2 else 0.9); by = 940 - min(u*90, 330) + math.sin(u*2.3+k)*45
            if k == 0:
                bump = max(0, 1-abs(t-13.9)/1.1); bx = bx*(1-bump) + (815+math.sin(t*3)*25)*bump; by = by*(1-bump) + (1330+math.sin(t*4)*20)*bump
            E.butterfly(c, c.X(bx), c.Y(by), 70*(1.0 if k else 1.1), math.sin(t*3+k)*14, t*16+k, BF_COL[k])
            E.sparkles(c, bx, by, tk, 6, n=3, spread=40, size=9, seed=k+20)
    E.confetti(c, 19.2)

def overlay(img, t):
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        ti = tl + E.FLY
        if 0 <= t-ti < 0.16:
            img = Image.blend(img, Image.new("RGB", img.size, (255, 250, 225)), 0.32*(1-(t-ti)/0.16))
    E.subscribe_button(img, t, 24.2, cy=1440)
    return img
