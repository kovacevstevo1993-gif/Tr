import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes5 import *

# =====================================================================
# SHORT 6: CSFP, scatola di cibo mensile per over 60. Stesso motore di scenes5.
# uso: S6_OUT=cartella python3 scenes6.py <clip>
# =====================================================================
CARD_B = (196, 146, 78)
CARD_BD = (160, 112, 56)

def box_spr():
    def mk():
        c = Cv(520, 360)
        c.poly([(30, 70), (150, 6), (370, 6), (490, 70)], fill=CARD_BD)
        c.poly([(8, 70), (60, 20), (130, 70)], fill=(214, 164, 96))
        c.poly([(512, 70), (460, 20), (390, 70)], fill=(214, 164, 96))
        c.rrect((8, 66, 512, 350), 10, fill=CARD_B, outline=CARD_BD, width=5)
        c.rrect((8, 66, 512, 104), 6, fill=(214, 164, 96))
        c.rrect((196, 66, 324, 130), 6, fill=(226, 190, 130))
        c.rrect((70, 170, 450, 300), 18, fill=IVORY, outline=CARD_BD, width=4)
        c.text((260, 222), "CSFP", FONT_SANS, 74, DARK, track=6)
        c.text((260, 270), "MONTHLY FOOD BOX", FONT_SANS, 26, (70, 110, 90), track=3)
        return c.done()
    return cache("box6", mk)

def can_spr():
    def mk():
        c = Cv(110, 150)
        c.rrect((6, 14, 104, 140), 14, fill=(180, 190, 186), outline=(120, 132, 128), width=4)
        c.rrect((6, 50, 104, 108), 4, fill=CORAL)
        c.ell((34, 62, 76, 96), fill=IVORY)
        c.rrect((6, 8, 104, 26), 8, fill=(214, 220, 216))
        return c.done()
    return cache("can6", mk)

def cheese_spr():
    def mk():
        c = Cv(170, 120)
        c.poly([(8, 100), (30, 30), (160, 100)], fill=(240, 198, 80))
        c.rrect((8, 84, 160, 112), 8, fill=(226, 170, 52))
        for (x, y, r) in ((54, 80, 11), (96, 90, 8), (40, 56, 6)):
            c.ell((x - r, y - r, x + r, y + r), fill=(214, 158, 44))
        return c.done()
    return cache("cheese6", mk)

def juice_spr():
    def mk():
        c = Cv(100, 150)
        c.rrect((8, 20, 92, 144), 10, fill=(236, 140, 60), outline=(190, 100, 30), width=4)
        c.ell((26, 52, 74, 100), fill=(250, 190, 90))
        c.line([66, 20, 78, 0], IVORY, 7)
        c.line([78, 0, 92, 0], IVORY, 7)
        return c.done()
    return cache("juice6", mk)

def cereal_spr():
    def mk():
        c = Cv(110, 160)
        c.rrect((6, 8, 104, 154), 8, fill=(220, 90, 80), outline=(170, 60, 56), width=4)
        c.ell((24, 50, 86, 112), fill=IVORY)
        for (x, y) in ((40, 74), (58, 66), (52, 90), (68, 84)):
            c.ell((x - 6, y - 6, x + 6, y + 6), outline=(214, 160, 80), width=3)
        return c.done()
    return cache("cereal6", mk)

def rice_spr():
    def mk():
        c = Cv(120, 160)
        c.poly([(14, 14), (106, 14), (112, 150), (8, 150)], fill=IVORY)
        c.rrect((14, 8, 106, 28), 6, fill=(214, 208, 194))
        c.rrect((22, 60, 98, 110), 10, fill=SAGE)
        c.text((60, 86), "RICE", FONT_SANS, 28, DARK)
        return c.done()
    return cache("rice6", mk)

def pasta_spr():
    def mk():
        c = Cv(150, 130)
        c.ell((6, 40, 144, 122), fill=IVORY, outline=(214, 208, 194), width=4)
        for k in range(7):
            x = 24 + k * 16
            c.line([x, 52, x + 12, 70], (240, 200, 90), 6)
            c.line([x + 12, 70, x - 4, 88], (240, 200, 90), 6)
        return c.done()
    return cache("pasta6", mk)

def pb_spr():
    def mk():
        c = Cv(120, 140)
        c.rrect((10, 6, 110, 30), 8, fill=CORAL)
        c.rrect((16, 28, 104, 136), 18, fill=(196, 140, 70), outline=(150, 100, 44), width=4)
        c.rrect((28, 62, 92, 108), 8, fill=IVORY)
        c.text((60, 86), "PB", FONT_SANS, 30, DARK)
        return c.done()
    return cache("pb6", mk)

def beans_spr():
    def mk():
        c = Cv(130, 140)
        c.rrect((12, 8, 118, 32), 8, fill=(190, 140, 60))
        c.rrect((16, 30, 114, 134), 20, fill=(154, 200, 170, 90), outline=SAGE, width=4)
        rnd = random.Random(6)
        for _ in range(16):
            x, y = rnd.randint(30, 98), rnd.randint(54, 120)
            c.ell((x - 9, y - 6, x + 9, y + 6), fill=(150, 70, 56))
        return c.done()
    return cache("beans6", mk)

def carrot_spr():
    def mk():
        c = Cv(100, 160)
        c.poly([(18, 40), (82, 40), (52, 154)], fill=(240, 130, 50))
        for y in (66, 88, 110):
            c.line([34, y, 52, y + 6], (200, 96, 30), 4)
        c.poly([(34, 40), (40, 6), (52, 36)], fill=LEAF)
        c.poly([(50, 40), (62, 2), (68, 40)], fill=(90, 150, 100))
        return c.done()
    return cache("carrot6", mk)

def month_cal_spr():
    def mk():
        c = Cv(330, 350)
        c.rrect((0, 22, 330, 346), 28, fill=IVORY)
        c.rrect((0, 22, 330, 112), 28, fill=SAGE_D)
        c.rrect((0, 74, 330, 112), 2, fill=SAGE_D)
        c.rrect((78, 0, 100, 56), 8, fill=DARK)
        c.rrect((230, 0, 252, 56), 8, fill=DARK)
        c.text((165, 70), "MONTHLY", FONT_SANS, 46, IVORY, track=3)
        for r in range(4):
            for q in range(5):
                c.rrect((24 + q * 58, 130 + r * 52, 24 + q * 58 + 40, 130 + r * 52 + 36), 8, fill=(214, 208, 194))
        c.rrect((24 + 2 * 58, 130 + 1 * 52, 24 + 2 * 58 + 40, 130 + 1 * 52 + 36), 8, fill=GOLD)
        c.line([90 + 58, 148 + 52, 100 + 58, 160 + 52, 118 + 58, 140 + 52], DARK, 6)
        return c.done()
    return cache("mcal6", mk)

def unclaimed_spr():
    def mk():
        c = Cv(300, 130)
        c.rrect((4, 4, 296, 126), 26, fill=CARD, outline=SAGE_D, width=5)
        c.ell((24, 28, 92, 96), fill=GOLD)
        c.text((58, 64), "?", FONT_SERIF, 54, DARK)
        c.text((200, 52), "BENEFIT", FONT_SANS, 34, IVORY, track=3)
        c.text((200, 88), "UNCLAIMED", FONT_SANS, 24, CORAL, track=3)
        return c.done()
    return cache("unclaimed6", mk)

def url_bar_spr(txt, size=44, w=940):
    def mk():
        c = Cv(w, 190)
        c.rrect((3, 3, w - 3, 187), 30, fill=CARD, outline=SAGE_D, width=5)
        for i, col in enumerate((CORAL, GOLD, SAGE)):
            c.ell((30 + i * 34, 22, 52 + i * 34, 44), fill=col)
        c.rrect((30, 66, w - 30, 164), 44, fill=IVORY)
        return c.done()
    return cache(("urlbar", w), mk)

# ---------------------------------------------------------------- clip 1: gancio (12,5 s)
def c1(img, t):
    ambient_food(img, t, n=7, seed=61)
    label(img, t, "ONCE A MONTH", 300, GOLD)
    # calendario che entra, poi la scatola cade
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, glow_spr(), 330, 760, scale=1.0, alpha=0.25 * al)
        put(img, month_cal_spr(), 330, 760, scale=0.82 * s, alpha=al, shadow=14, rot=-5 + 2 * math.sin(t * 2.5))
    u = seg(t, 1.5, 0.6)
    if u > 0:
        fy = -420 * (1 - ease_back(u)) * (1 if u < 1 else 0)
        put(img, glow_spr(), 740, 800, scale=1.2, alpha=0.3 * min(1.0, u * 2))
        put(img, box_spr(), 740, 800 + fy, scale=0.82, alpha=min(1.0, u * 3), shadow=16, rot=3 * math.sin(t * 2))
        burst(img, t, 2.0, 740, 800, n=14, color=GOLD, dur=0.8, rad=330, seed=62)
    for k, (fn, dx, dy, sc, r0) in enumerate(((apple_spr, -150, -150, 0.52, -14), (bread_spr, 20, -170, 0.5, 8), (milk_spr, 160, -140, 0.5, 12), (can_spr, -60, -190, 0.9, -6))):
        s, al, a = pop(t, 2.3 + k * 0.18, 0.45)
        if a > 0:
            put(img, fn(), 740 + dx, 800 + dy + 8 * math.sin(t * 4 + k), scale=sc * s, alpha=al, rot=r0 + 6 * math.sin(t * 3 + k), shadow=6)
    a = seg(t, 1.2, 0.5)
    if a > 0:
        put(img, tspr("A BOX OF FOOD", FONT_SANS, 82, IVORY), 540, 1130 + 22 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 2.2, 0.5)
    if a > 0:
        put(img, tspr("FROM THE GOVERNMENT", FONT_SANS, 54, SAGE, track=2), 540, 1220 + 22 * (1 - ease(a)), alpha=ease(a), shadow=6)
    # quasi nessuno lo sa: anziani spenti con punto interrogativo
    for i in range(7):
        s, al, a = pop(t, 4.8 + i * 0.12, 0.4)
        if a > 0:
            put(img, person_spr("off"), 150 + i * 130, 1390 + 5 * math.sin(t * 3 + i), scale=0.95 * s, alpha=al * 0.9)
    a = seg(t, 5.4, 0.5)
    if a > 0:
        put(img, tspr("NEARLY NO ONE OVER 60", FONT_SANS, 56, CORAL), 540, 1500 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 6.0, 0.5)
    if a > 0:
        put(img, tspr("KNOWS IT EXISTS", FONT_SANS, 70, GOLD), 540, 1590 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)
    # tease finale: dove controllare
    s, al, a = pop(t, 8.6, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1740, scale=1.1, alpha=0.3 * al)
        put(img, tag_spr("STAY TO THE END", 760, 130, GOLD, 64), 540, 1740, scale=s, alpha=al, rot=-2, shadow=12)
        burst(img, t, 8.6, 540, 1740, n=12, color=GOLD, dur=0.7, rad=380, seed=63)
    a = seg(t, 10.0, 0.5)
    if a > 0:
        put(img, magnifier_spr(), 930 - 30 * math.sin(t * 2), 1580 + 14 * math.sin(t * 3), scale=0.6, alpha=ease(a), rot=-10)

# ---------------------------------------------------------------- clip 2: nome del programma (5,7 s)
def c2(img, t):
    ambient_food(img, t, n=7, seed=63)
    label(img, t, "THE PROGRAM", 300, SAGE)
    for k, ch in enumerate("CSFP"):
        s, al, a = pop(t, 0.2 + k * 0.2, 0.45)
        if a > 0:
            put(img, glow_spr(), 270 + k * 180, 760, scale=0.5, alpha=0.2 * al)
            put(img, tspr(ch, FONT_SERIF, 300, GOLD), 190 + k * 233 - 20, 760 + 8 * math.sin(t * 4 + k), scale=s, alpha=al, shadow=14)
            burst(img, t, 0.2 + k * 0.2, 190 + k * 233 - 20, 760, n=8, color=GOLD, dur=0.6, rad=200, seed=64 + k)
    a = seg(t, 1.5, 0.5)
    if a > 0:
        put(img, tspr("COMMODITY SUPPLEMENTAL", FONT_SANS, 50, IVORY, track=1), 540, 1000 + 20 * (1 - ease(a)), alpha=ease(a), shadow=6)
    a = seg(t, 2.0, 0.5)
    if a > 0:
        put(img, tspr("FOOD PROGRAM", FONT_SANS, 90, IVORY), 540, 1100 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 3.5, 0.6)
    if a > 0:
        put(img, building_spr(), 540 - 260 * (1 - ease(a)), 1420, scale=0.62, alpha=ease(a), shadow=12)
    s, al, a = pop(t, 4.0, 0.45)
    if a > 0:
        put(img, stamp_spr("RUN BY THE USDA", 640, 130, GOLD), 540, 1640, scale=s, alpha=al, rot=-4, shadow=12)
        burst(img, t, 4.0, 540, 1640, n=12, color=GOLD, dur=0.7, rad=320, seed=69)

# ---------------------------------------------------------------- clip 3: requisiti (5,3 s)
def c3(img, t):
    ambient_food(img, t, n=7, seed=65)
    label(img, t, "THE RULE", 300, GOLD)
    s, al, a = pop(t, 0.1, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 760, scale=1.2, alpha=0.28 * al)
        put(img, elder_spr(), 400, 760, scale=0.95 * s, alpha=al, shadow=14, rot=2 * math.sin(t * 3))
    s, al, a = pop(t, 0.6, 0.5)
    if a > 0:
        put(img, age_badge(), 700, 820, scale=0.95 * s, alpha=al, shadow=12, rot=-8 + 5 * math.sin(t * 4))
        burst(img, t, 0.6, 700, 820, n=12, color=GOLD, dur=0.7, rad=250, seed=66)
    a = seg(t, 1.2, 0.5)
    if a > 0:
        put(img, test_card("AT LEAST 60", "AGE", SAGE, "paper"), 540 - 300 * (1 - ease(a)), 1180, alpha=ease(a), shadow=12)
        put(img, check_spr(), 910, 1110, scale=0.55 * ease_back(seg(t, 1.6, 0.4)), alpha=ease(a))
    a = seg(t, 2.6, 0.5)
    if a > 0:
        put(img, test_card("LOW INCOME", "INCOME", SAGE, "bills"), 540 + 300 * (1 - ease(a)), 1430, alpha=ease(a), shadow=12)
        put(img, check_spr(), 910, 1360, scale=0.55 * ease_back(seg(t, 3.0, 0.4)), alpha=ease(a))
    for k, (fn, x, y, sc, r0) in enumerate(((apple_spr, 130, 1700, 0.8, -12), (bread_spr, 400, 1760, 0.7, 6), (milk_spr, 700, 1720, 0.7, -8), (can_spr, 940, 1750, 1.1, 10))):
        s2, al2, a2 = pop(t, 3.2 + k * 0.15, 0.45)
        if a2 > 0:
            put(img, fn(), x, y + 6 * math.sin(t * 4 + k), scale=sc * s2, alpha=al2, rot=r0 + 5 * math.sin(t * 3 + k), shadow=6)
    a = seg(t, 3.8, 0.5)
    if a > 0:
        put(img, tspr("THAT'S IT", FONT_SANS, 84, GOLD), 540, 1640 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)

# ---------------------------------------------------------------- clip 4: cosa c'e' nella scatola (10,8 s)
ITEMS6 = [(1.3, "MILK", milk_spr, 0.9), (2.0, "CHEESE", cheese_spr, 1.5), (2.65, "JUICE", juice_spr, 1.6), (3.3, "CEREAL", cereal_spr, 1.5),
          (4.0, "RICE", rice_spr, 1.5), (4.65, "PASTA", pasta_spr, 1.7), (5.3, "PEANUT BUTTER", pb_spr, 1.7), (6.3, "DRY BEANS", beans_spr, 1.7),
          (7.5, "CANNED MEAT", can_spr, 1.8), (8.6, "FRUIT", apple_spr, 1.2), (9.4, "VEGETABLES", carrot_spr, 1.5)]

def c4(img, t):
    ambient_food(img, t, n=7, seed=67)
    label(img, t, "INSIDE THE BOX", 300, GOLD)
    bx, by = 540, 1530
    # oggetti gia' caduti: spuntano dalla scatola
    drops = [it for it in ITEMS6 if t >= it[0] + 0.85]
    for k, (t0, name, fn, sc) in enumerate(drops):
        sl = k % 6
        put(img, fn(), 250 + sl * 116, 1360 - (k // 6) * 50 + 4 * math.sin(t * 4 + k), scale=1.0, rot=(-12 + sl * 5), alpha=1.0)
    bounce = 0.0
    for (t0, name, fn, sc) in ITEMS6:
        if t0 + 0.8 < t < t0 + 1.1:
            bounce = 14 * math.sin((t - t0 - 0.8) / 0.3 * 3.14)
    put(img, glow_spr(), bx, by, scale=1.2, alpha=0.2)
    put(img, box_spr(), bx, by + bounce, scale=1.45, shadow=16)
    for (t0, name, fn, sc) in ITEMS6:
        u = seg(t, t0, 0.35)
        if u <= 0 or t > t0 + 1.2:
            continue
        v = seg(t, t0 + 0.55, 0.3)
        s = ease_back(u)
        y = 850 + (1380 - 850) * v * v
        scl = 2.3 - 1.2 * v
        al = 1.0 - 0.6 * v
        put(img, fn(), 540 + 10 * math.sin(t * 6), y, scale=max(0.05, scl * s), alpha=al, rot=8 * math.sin(t * 5) * (1 - v), shadow=10)
        if u < 1:
            burst(img, t, t0, 540, 850, n=8, color=GOLD, dur=0.5, rad=240, seed=int(t0 * 10) + 70)
        if t < t0 + 0.9:
            put(img, tspr(name, FONT_SANS, 92, GOLD), 540, 1090 + 14 * (1 - ease(seg(t, t0 + 0.05, 0.25))), alpha=ease(seg(t, t0 + 0.05, 0.25)) * (1 - seg(t, t0 + 0.8, 0.12)), shadow=10)
    a = seg(t, 8.2, 0.5)
    if a > 0:
        put(img, tspr("PLUS", FONT_SANS, 38, SAGE, track=8), 540, 660 + 12 * (1 - ease(a)), alpha=ease(a) * (1 if t < 10.4 else 1 - seg(t, 10.4, 0.3)))

# ---------------------------------------------------------------- clip 5: il trucco (8,2 s)
def c5(img, t):
    ambient_food(img, t, n=7, seed=69)
    label(img, t, "THE CATCH", 300, CORAL)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, map_spr(), 540, 760, scale=1.1 * s, alpha=al, shadow=16)
    pins = ((-250, -60, GOLD, 1.9, "TX"), (50, 60, SAGE, 2.3, "NY"), (290, -40, IVORY, 2.7, "CA"), (-80, 90, CORAL, 3.1, "FL"))
    for (px, py, col, t0, txt) in pins:
        a2 = seg(t, t0, 0.45)
        if a2 > 0:
            bx, by = 540 + px * 1.1, 760 + py * 1.1
            put(img, pin_spr(col), bx, by - 60 - 220 * (1 - ease_back(a2)), alpha=min(1.0, a2 * 3))
            put(img, tag_spr(txt, 150, 76, col, 44), bx, by - 190 - 220 * (1 - ease_back(a2)) * 0.2, alpha=ease(a2), shadow=6)
    a = seg(t, 1.6, 0.5)
    if a > 0:
        put(img, tspr("EVERY STATE SETS ITS OWN", FONT_SANS, 46, IVORY, track=1), 540, 1130 + 20 * (1 - ease(a)), alpha=ease(a), shadow=6)
    a = seg(t, 2.1, 0.5)
    if a > 0:
        put(img, tspr("INCOME LIMIT", FONT_SANS, 100, GOLD), 540, 1250 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)
    # seconda parte: non in tutte le zone
    for (px, py, t0) in ((-250, -60, 5.0), (290, -40, 5.6)):
        s, al, a = pop(t, t0, 0.4)
        if a > 0:
            put(img, bigx_spr(), 540 + px * 1.1, 760 + py * 1.1 + 10, scale=0.45 * s, alpha=al, rot=-6)
    s, al, a = pop(t, 5.0, 0.5)
    if a > 0:
        put(img, stamp_spr("NOT IN EVERY AREA", 700, 120, CORAL), 540, 1480, scale=s, alpha=al, rot=-4, shadow=12)
        burst(img, t, 5.0, 540, 1480, n=12, color=CORAL, dur=0.7, rad=320, seed=75)
    a = seg(t, 5.9, 0.5)
    if a > 0:
        put(img, tspr("ASK WHERE YOU LIVE", FONT_SANS, 58, IVORY), 540, 1640 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)

# ---------------------------------------------------------------- clip 6: dove controllare (11,5 s)
URL6 = "fns.usda.gov/csfp/program-contacts"
def c6(img, t):
    ambient_food(img, t, n=7, seed=71)
    label(img, t, "CONTACT YOUR STATE", 300, GOLD)
    s, al, a = pop(t, 0.1, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 760, scale=1.2, alpha=0.28 * al)
        put(img, office_spr(), 540, 760, scale=1.05 * s, alpha=al, shadow=14)
        put(img, tspr("YOUR STATE AGENCY", FONT_SANS, 48, IVORY, track=2), 540, 990, alpha=ease(seg(t, 0.5, 0.5)), shadow=8)
    a = seg(t, 2.4, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1250, scale=1.3, alpha=0.2 * ease(a))
        put(img, url_bar_spr(URL6), 540, 1250 + 30 * (1 - ease(a)), alpha=ease(a), shadow=12)
        put(img, tspr("USDA WEBSITE", FONT_SANS, 34, SAGE, track=6), 540, 1130, alpha=ease(a))
        # indirizzo che si scrive in sync con la voce: dominio fino a 8.3, poi il resto
        n = len(URL6)
        if t < 2.9:
            k = 0
        elif t < 8.3:
            k = int(round(14 * ease(seg(t, 2.9, 4.8))))
        else:
            k = 14 + int(round((n - 14) * ease(seg(t, 8.3, 2.8))))
        if k > 0:
            sp = tspr(URL6[:k], FONT_SANS, 40, DARK)
            img.paste(sp, (int(540 - 470 + 72), int(1250 - 7) - sp.height // 2 + 15), sp)
    if t > 3.2:
        u = seg(t, 3.2, 0.6)
        put(img, cursor_spr(), 820 + 90 * (1 - ease(u)) - 40 * seg(t, 8.3, 2.5), 1330 + 60 * (1 - ease(u)), alpha=ease(u), shadow=6)
    s, al, a = pop(t, 9.0, 0.5)
    if a > 0:
        put(img, tag_spr("PROGRAM CONTACTS", 700, 110, GOLD, 52), 540, 1530, scale=s, alpha=al, rot=-2, shadow=12)
        burst(img, t, 9.0, 540, 1530, n=12, color=GOLD, dur=0.7, rad=360, seed=76)
    a = seg(t, 9.8, 0.5)
    if a > 0:
        put(img, tspr("OFFICIAL .GOV LIST", FONT_SANS, 44, IVORY, track=3), 540, 1670 + 20 * (1 - ease(a)), alpha=ease(a))

# ---------------------------------------------------------------- clip 7: un altro beneficio -> short SNAP (9,3 s)
def c7(img, t):
    ambient_food(img, t, n=7, seed=73)
    label(img, t, "MORE BENEFITS", 300, GOLD)
    for k in range(5):
        s, al, a = pop(t, 0.2 + k * 0.45, 0.45)
        if a > 0:
            x = 540 + (-1) ** k * 200 * (1 if k % 2 else -1) * 0.0 + (k % 2 * 2 - 1) * 190
            y = 560 + k * 128
            fade = 1.0 - 0.7 * seg(t, 3.6, 0.4)
            put(img, unclaimed_spr(), x, y, scale=0.9 * s, alpha=al * fade, rot=(-5 if k % 2 else 5), shadow=8)
    a = seg(t, 2.6, 0.5)
    if a > 0:
        fade = 1.0 - seg(t, 3.7, 0.4)
        put(img, tspr("MOST SENIORS", FONT_SANS, 62, IVORY), 540, 1290, alpha=ease(a) * fade, shadow=8)
        put(img, tspr("NEVER CLAIM THEM", FONT_SANS, 62, CORAL), 540, 1380, alpha=ease(a) * fade, shadow=8)
    s, al, a = pop(t, 3.8, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 800, scale=1.5, alpha=0.3 * al)
        put(img, play_card_spr(), 540, 800, scale=1.0 * s * (1 + 0.015 * math.sin(t * 6)), alpha=al, shadow=18, rot=-2 * (1 - ease(a)))
        burst(img, t, 3.9, 540, 800, n=12, color=GOLD, dur=0.7, rad=420, seed=77)
    a = seg(t, 4.2, 0.5)
    if a > 0:
        put(img, tspr("WANT ANOTHER ONE?", FONT_SANS, 74, IVORY), 540, 1170 + 22 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 5.6, 0.4)
    if a > 0:
        put(img, tspr("3 SNAP RULES", FONT_SANS, 100, GOLD), 540, 1300 + 22 * (1 - ease(a)), alpha=ease(a), shadow=10)
    a = seg(t, 8.0, 0.4)
    if a > 0:
        put(img, tspr("CLICK BELOW", FONT_SANS, 110, GOLD), 540, 1460 + 22 * (1 - ease(a)), alpha=ease(a), shadow=12)
    for k in range(3):
        a = seg(t, 8.1 + k * 0.1, 0.3)
        if a > 0:
            ph = (t * 2.2 - k * 0.22) % 1.0
            put(img, chevron_spr(), 540, 1610 + k * 70 + 30 * math.sin(ph * 6.28), alpha=ease(a) * (0.5 + 0.5 * math.sin(ph * 6.28) ** 2), scale=0.9)

# durate in fotogrammi (dalla timeline CapCut, dalla fine del clip precedente)
SCENES6 = {1: (c1, 375), 2: (c2, 170), 3: (c3, 160), 4: (c4, 324), 5: (c5, 246), 6: (c6, 345), 7: (c7, 279), 8: (s8, 112)}

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES6)
    out_dir = os.environ.get("S6_OUT", "short6")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        fn, nf = SCENES6[k]
        render_seq(zoomed(fn), nf, f"{out_dir}/short6-clip{k:02d}.mp4")
