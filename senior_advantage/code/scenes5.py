import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes4 import *

# =====================================================================
# SHORT 5: SNAP per over 60 (3 regole). Stesso motore, piu' movimento e piu' oggetti.
# uso: S5_OUT=cartella python3 scenes5.py <clip>
# =====================================================================
LEAF = (110, 176, 124)
CRUST = (214, 160, 80)
CRUST_D = (190, 140, 60)

# ---------------------------------------------------------------- sprite nuovi
def person_spr(kind):
    """kind: on (oro), off (vuota), no (vuota corallo)"""
    def mk():
        c = Cv(70, 90)
        if kind == "on":
            c.rrect((6, 42, 64, 88), 22, fill=GOLD, outline=CRUST_D, width=3)
            c.ell((19, 4, 51, 38), fill=(236, 194, 154))
            c.ell((17, 2, 53, 20), fill=(240, 240, 236))
            c.ell((16, 14, 26, 30), fill=(240, 240, 236))
            c.ell((44, 14, 54, 30), fill=(240, 240, 236))
        else:
            col = SAGE_D if kind == "off" else CORAL
            c.rrect((6, 42, 64, 88), 22, fill=(16, 64, 50), outline=col, width=4)
            c.ell((19, 4, 51, 38), fill=(16, 64, 50), outline=col, width=4)
        return c.done()
    return cache(("person", kind), mk)

def apple_spr():
    def mk():
        c = Cv(110, 124)
        c.ell((4, 24, 58, 118), fill=CORAL)
        c.ell((50, 24, 106, 118), fill=CORAL)
        c.ell((22, 36, 88, 118), fill=CORAL)
        c.line([55, 34, 60, 8], (120, 78, 52), 6)
        c.poly([(62, 22), (96, 4), (92, 34)], fill=LEAF)
        c.arc((18, 44, 52, 90), 200, 270, (255, 190, 176), 7)
        return c.done()
    return cache("apple5", mk)

def bread_spr():
    def mk():
        c = Cv(170, 104)
        c.rrect((4, 20, 166, 100), 42, fill=CRUST, outline=CRUST_D, width=4)
        for x in (48, 84, 120):
            c.line([x, 36, x + 16, 62], CRUST_D, 7)
        return c.done()
    return cache("bread5", mk)

def milk_spr():
    def mk():
        c = Cv(92, 160)
        c.poly([(8, 46), (46, 6), (84, 46)], fill=(226, 220, 204))
        c.rrect((8, 42, 84, 154), 8, fill=IVORY)
        c.rrect((52, 42, 84, 154), 8, fill=(226, 220, 204))
        c.rrect((20, 78, 60, 122), 8, fill=SAGE)
        c.ell((30, 90, 50, 110), fill=IVORY)
        return c.done()
    return cache("milk5", mk)

def basket_spr():
    def mk():
        c = Cv(300, 250)
        c.arc((46, 4, 254, 190), 180, 360, CRUST_D, 14)
        c.poly([(8, 96), (292, 96), (252, 240), (48, 240)], fill=CRUST)
        c.line([8, 96, 292, 96], CRUST_D, 12)
        c.line([48, 240, 252, 240], CRUST_D, 10)
        for x in (70, 110, 150, 190, 230):
            c.line([x, 104, x - (150 - x) * 0.0 + (x - 150) * 0.28, 236], CRUST_D, 5)
        for y in (140, 184):
            c.line([20 + (y - 96) * 0.28, y, 280 - (y - 96) * 0.28, y], CRUST_D, 5)
        return c.done()
    return cache("basket5", mk)

FOODS = None
def food_list():
    return [apple_spr(), bread_spr(), milk_spr()]

def ambient_food(img, t, n=7, seed=5, alpha=0.13):
    """cibo che sale piano sullo sfondo (al posto di $ e %)"""
    rnd = random.Random(seed)
    sp_l = food_list()
    for i in range(n):
        sp = sp_l[i % 3]
        x0 = rnd.uniform(110, W - 110)
        v = rnd.uniform(24, 52)
        ph = rnd.uniform(0, 6.28)
        sc = rnd.choice([0.55, 0.7, 0.85])
        off = rnd.uniform(0, H + 260)
        y = (off - t * v) % (H + 260) - 130
        x = x0 + math.sin(t * 0.7 + ph) * 26
        put(img, sp, x, y, scale=sc, alpha=alpha, rot=math.sin(t * 0.9 + ph) * 18)

def zoomed(fn):
    """spinta lenta in avanti su tutta la clip (piu' movimento)"""
    def draw(img, t):
        fn(img, t)
        z = 1.0 + 0.0085 * t
        cw, ch = W / z, H / z
        x0, y0 = (W - cw) / 2, (H - ch) / 2
        crop = img.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
        img.paste(crop, (0, 0))
    return draw

# ---------------------------------------------------------------- scene
GX0, GY0, GST = 540 - 4.5 * 84, 520, 88

def pos(i):
    return GX0 + (i % 10) * 84, GY0 + (i // 10) * GST

def s1(img, t):
    ambient_food(img, t, n=7, seed=71)
    if t < 0.95:
        sw, al, aw = pop(t, 0.0, 0.35)
        fade = 1.0 - seg(t, 0.6, 0.3)
        shake = 7 * math.sin(t * 38) * (1 - seg(t, 0.0, 0.7))
        put(img, glow_spr(), 540, 880, scale=1.3, alpha=0.3 * fade)
        put(img, tspr("WAIT...", FONT_SERIF, 230, CORAL), 540 + shake, 880, scale=sw, alpha=al * fade, rot=-4, shadow=16)
    else:
        label(img, t, "SNAP FOR SENIORS", 300, SAGE, t0=0.95)
    # 100 persone: onda iniziale, poi 55 si accendono d'oro
    n_on = 0
    for i in range(100):
        x, y = pos(i)
        t_in = 0.55 + i * 0.0035
        s, al, a = pop(t, t_in, 0.3)
        if a <= 0:
            continue
        t_on = 1.05 + i * 0.022
        if i < 55 and t >= t_on:
            n_on += 1
            u = seg(t, t_on, 0.3)
            put(img, person_spr("on"), x, y - 10 * math.sin(u * 3.14), scale=0.74 * (1 + 0.3 * math.sin(u * 3.14)), alpha=1.0, shadow=4)
        elif i >= 55 and t > 2.4:
            u = seg(t, 2.4 + (i - 55) * 0.006, 0.4)
            put(img, person_spr("no"), x, y, scale=0.74 * (0.86 + 0.14 * ease_back(u)), alpha=0.55 + 0.25 * math.sin(t * 5 + i * 0.5))
        else:
            put(img, person_spr("off"), x, y, scale=0.74 * s, alpha=al)
    # contatore
    u = seg(t, 1.05, 1.3)
    if u > 0:
        n = int(round(55 * ease(u)))
        put(img, glow_spr(), 300, 1440, scale=0.9, alpha=0.25 * min(1.0, u * 3))
        put(img, tspr(str(n), FONT_SERIF, 300, GOLD), 300, 1440, shadow=16, scale=1.0 + 0.05 * max(0.0, math.sin(min(1.0, u) * 3.14 * 2)))
    if u >= 1.0:
        burst(img, t, 2.3, 300, 1440, n=12, color=GOLD, dur=0.7, rad=250, seed=72)
    a = seg(t, 2.2, 0.45)
    if a > 0:
        put(img, tspr("OUT OF 100", FONT_SANS, 62, IVORY), 730, 1385 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 2.55, 0.45)
    if a > 0:
        put(img, tspr("ELIGIBLE SENIORS", FONT_SANS, 44, SAGE, track=4), 730, 1465 + 20 * (1 - ease(a)), alpha=ease(a))
    # finale: GET SNAP + cestino con cibo
    s, al, a = pop(t, 3.55, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1685, scale=1.2, alpha=0.3 * al)
        put(img, tag_spr("GET SNAP", 620, 150, GOLD, 86), 560, 1685, scale=s, alpha=al, rot=-2, shadow=14)
        burst(img, t, 3.55, 560, 1685, n=14, color=GOLD, dur=0.7, rad=360, seed=73)
    s, al, a = pop(t, 3.7, 0.5)
    if a > 0:
        bob = 5 * math.sin((t - 3.7) * 6)
        put(img, basket_spr(), 125, 1670 + bob, scale=0.55 * s, alpha=al, shadow=10, rot=-4)
        put(img, apple_spr(), 108, 1612 + bob, scale=0.5 * s, alpha=al, rot=-10)
        put(img, bread_spr(), 158, 1616 + bob, scale=0.42 * s, alpha=al, rot=14)
    s, al, a = pop(t, 3.95, 0.5)
    if a > 0:
        put(img, milk_spr(), 960, 1670 + 6 * math.sin((t - 3.95) * 5), scale=0.7 * s, alpha=al, shadow=8, rot=8)


# ---------------------------------------------------------------- sprite clip 2-8
def rules_doc_spr():
    def mk():
        c = Cv(440, 540)
        c.rrect((0, 0, 440, 540), 22, fill=IVORY)
        c.poly([(360, 0), (440, 80), (360, 80)], fill=(214, 208, 194))
        c.rrect((0, 0, 440, 96), 22, fill=SAGE)
        c.d.rectangle([0, 60 * c.ss, 440 * c.ss, 96 * c.ss], fill=SAGE)
        c.text((30, 50), "SNAP RULES", FONT_SANS, 42, DARK, anchor="lm", track=4)
        for i in range(3):
            y = 138 + i * 112
            c.ell((30, y, 90, y + 60), fill=(214, 208, 194))
            c.rrect((112, y + 4, 400 - i * 36, y + 24), 8, fill=(198, 196, 186))
            c.rrect((112, y + 36, 330 - i * 30, y + 52), 8, fill=(214, 212, 202))
        c.text((220, 500), "FINE PRINT", FONT_SANS, 26, (120, 130, 120), track=6)
        return c.done()
    return cache("rules_doc", mk)

def num_badge(n):
    def mk():
        c = Cv(190, 190)
        c.ell((6, 6, 184, 184), fill=GOLD, outline=CRUST_D, width=8)
        c.ell((22, 22, 168, 168), outline=CRUST_D, width=3)
        c.text((95, 100), str(n), FONT_SERIF, 118, DARK)
        return c.done()
    return cache(("numbadge", n), mk)

def age_badge():
    def mk():
        c = Cv(250, 250)
        pts = []
        for i in range(24):
            ang = math.pi * 2 * i / 24 - math.pi / 2
            r = 120 if i % 2 == 0 else 104
            pts.append((125 + r * math.cos(ang), 125 + r * math.sin(ang)))
        c.poly(pts, fill=GOLD)
        c.ell((26, 26, 224, 224), outline=CRUST_D, width=5)
        c.text((125, 118), "60", FONT_SERIF, 112, DARK)
        c.text((125, 184), "YEARS", FONT_SANS, 28, DARK, track=4)
        return c.done()
    return cache("age_badge", mk)

def test_card(txt, sub, col, icon):
    def mk():
        c = Cv(900, 210)
        c.rrect((4, 4, 896, 206), 46, fill=CARD, outline=col, width=6)
        c.ell((34, 34, 176, 176), fill=(16, 64, 50), outline=col, width=4)
        if icon == "bills":
            for k, dx in enumerate((-14, 0, 14)):
                c.rrect((60 + dx, 70 - dx * 0.6, 150 + dx, 128 - dx * 0.6), 8, fill=(232, 200, 130) if k == 2 else (196, 160, 90), outline=CRUST_D, width=3)
            c.ell((92, 82, 118, 108), outline=CRUST_D, width=4)
        else:
            c.rrect((58, 66, 152, 132), 10, fill=IVORY)
            c.rrect((58, 66, 152, 86), 10, fill=SAGE)
            for y in (100, 116):
                c.rrect((70, y, 140, y + 8), 4, fill=(198, 196, 186))
            c.ell((120, 118, 160, 158), fill=GOLD, outline=CRUST_D, width=3)
        c.text((206, 80), txt, FONT_SANS, 54, IVORY, anchor="lm")
        c.text((208, 140), sub, FONT_SANS, 30, SAGE, anchor="lm", track=4)
        return c.done()
    return cache(("tcard", txt, sub, col), mk)

def check_spr():
    def mk():
        c = Cv(180, 180)
        c.ell((6, 6, 174, 174), fill=GOLD, outline=CRUST_D, width=6)
        c.line([46, 94, 78, 128, 136, 56], DARK, 18)
        return c.done()
    return cache("check5", mk)

def pill_bottle_spr():
    def mk():
        c = Cv(170, 250)
        c.rrect((22, 4, 148, 70), 14, fill=IVORY, outline=(214, 208, 194), width=3)
        for x in (44, 66, 88, 110, 130):
            c.line([x, 14, x, 62], (214, 208, 194), 4)
        c.rrect((12, 62, 158, 244), 22, fill=(226, 150, 70), outline=(190, 110, 40), width=4)
        c.rrect((24, 100, 146, 210), 14, fill=IVORY)
        c.rrect((74, 114, 96, 196), 4, fill=CORAL)
        c.rrect((38, 144, 132, 166), 4, fill=CORAL)
        return c.done()
    return cache("pillbottle", mk)

def med_cross_spr():
    def mk():
        c = Cv(220, 220)
        c.ell((6, 6, 214, 214), fill=CARD, outline=CORAL, width=7)
        c.rrect((84, 40, 136, 180), 12, fill=CORAL)
        c.rrect((40, 84, 180, 136), 12, fill=CORAL)
        return c.done()
    return cache("medcross", mk)

def receipt_spr():
    def mk():
        c = Cv(250, 330)
        pts = [(0, 0), (250, 0), (250, 316)]
        for k in range(10):
            pts.append((250 - (k + 0.5) * 25, 330 if k % 2 == 0 else 316))
        pts += [(0, 316)]
        c.poly(pts, fill=IVORY)
        c.text((125, 44), "RECEIPT", FONT_SANS, 32, (110, 120, 110), track=4)
        for i in range(4):
            c.rrect((26, 84 + i * 36, 224 - (i % 2) * 50, 98 + i * 36), 6, fill=(198, 196, 186))
        c.line([26, 238, 224, 238], (170, 170, 158), 3)
        c.text((125, 282), "$35+", FONT_SANS, 58, CORAL)
        return c.done()
    return cache("receipt5", mk)

def savings_jar_spr():
    def mk():
        c = Cv(400, 540)
        c.rrect((40, 100, 360, 520), 80, fill=(154, 200, 170, 45), outline=SAGE, width=6)
        c.rrect((78, 44, 322, 112), 20, fill=GOLD, outline=CRUST_D, width=5)
        c.rrect((140, 68, 260, 84), 8, fill=DARK)
        c.rrect((92, 150, 308, 274), 18, fill=IVORY)
        c.text((200, 204), "SAVINGS", FONT_SANS, 46, DARK, track=2)
        c.text((200, 248), "ACCOUNT", FONT_SANS, 26, (70, 110, 90), track=5)
        return c.done()
    return cache("sjar", mk)

def stamp_spr(txt, w, h, col):
    def mk():
        c = Cv(w, h)
        c.rrect((6, 6, w - 6, h - 6), 24, fill=(7, 38, 30, 225), outline=col, width=8)
        c.rrect((20, 20, w - 20, h - 20), 14, outline=col, width=3)
        c.text((w / 2, h / 2), txt, FONT_SANS, int(h * 0.38), col, track=3)
        return c.done()
    return cache(("stamp", txt, w, h, col), mk)

def link_pill_spr(txt):
    def mk():
        c = Cv(760, 120)
        c.rrect((3, 3, 757, 117), 58, fill=CARD, outline=SAGE_D, width=5)
        c.ell((28, 30, 88, 90), fill=GOLD)
        c.poly([(50, 44), (50, 76), (76, 60)], fill=DARK)
        c.text((420, 62), txt, FONT_SANS, 46, IVORY)
        return c.done()
    return cache(("lpill", txt), mk)

def play_card_spr():
    def mk():
        c = Cv(780, 470)
        c.rrect((4, 4, 776, 466), 44, fill=CARD, outline=GOLD, width=7)
        c.rrect((30, 30, 750, 350), 28, fill=(22, 82, 64))
        for k in range(14):
            c.line([30 + k * 60, 30, 30 + k * 60 - 90, 350], (28, 96, 76), 6)
        mask = Image.new("L", c.im.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([60, 60, 1500, 700], radius=56, fill=255)
        c.ell((290, 60, 490, 260), fill=GOLD, outline=CRUST_D, width=6)
        c.poly([(358, 104), (358, 216), (448, 160)], fill=DARK)
        c.text((390, 300), "SNAP FOR SENIORS", FONT_SANS, 34, IVORY, track=5)
        c.text((390, 408), "WATCH NOW", FONT_SANS, 62, GOLD, track=4)
        return c.done()
    return cache("playcard", mk)

def chevron_spr():
    def mk():
        c = Cv(260, 140)
        c.poly([(10, 20), (70, 20), (130, 78), (190, 20), (250, 20), (130, 134)], fill=GOLD)
        return c.done()
    return cache("chev", mk)

def pin_tag(img, t, t0, bx, by, col, txt):
    a = seg(t, t0, 0.45)
    if a > 0:
        put(img, pin_spr(col), bx, by - 60 - 220 * (1 - ease_back(a)), alpha=min(1.0, a * 3))
        put(img, tag_spr(txt, 150, 76, col, 44), bx, by - 190 - 220 * (1 - ease_back(a)) * 0.2, alpha=ease(a), shadow=6)

# ---------------------------------------------------------------- clip 2: "Three rules nobody explains."
def s2(img, t):
    ambient_food(img, t, n=7, seed=81)
    label(img, t, "3 RULES", 300, GOLD)
    s, al, a = pop(t, 0.05, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 800, scale=1.3, alpha=0.3 * al)
        put(img, rules_doc_spr(), 540, 800, scale=1.15 * s, alpha=al, shadow=18, rot=-3 * (1 - ease(a)) + 2 * math.sin(t * 2))
    u = seg(t, 0.4, 1.3)
    if u > 0:
        put(img, magnifier_spr(), 380 + 330 * ease(u), 700 + 180 * math.sin(u * 6.3) * 0.5 + 60 * u, alpha=min(1.0, u * 4), rot=-8, shadow=10)
    for k, (x, t0) in enumerate(((290, 0.55), (540, 0.85), (790, 1.15))):
        s, al, a = pop(t, t0, 0.4)
        if a > 0:
            put(img, num_badge(k + 1), x, 1230 + 6 * math.sin(t * 5 + k), scale=0.95 * s, alpha=al, shadow=10)
            burst(img, t, t0, x, 1230, n=8, color=GOLD, dur=0.6, rad=170, seed=82 + k)
    a = seg(t, 1.0, 0.4)
    if a > 0:
        put(img, tspr("NOBODY", FONT_SANS, 92, IVORY), 540, 1440 + 22 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 1.45, 0.4)
    if a > 0:
        put(img, tspr("EXPLAINS THEM", FONT_SANS, 76, GOLD), 540, 1550 + 22 * (1 - ease(a)), alpha=ease(a), shadow=8)

# ---------------------------------------------------------------- clip 3: regola 1, a 60 anni si salta il test sul reddito lordo
def s3(img, t):
    ambient_food(img, t, n=7, seed=83)
    label(img, t, "RULE 1", 300, GOLD)
    s, al, a = pop(t, 0.1, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 800, scale=1.2, alpha=0.28 * al)
        put(img, elder_spr(), 480, 800, scale=0.95 * s, alpha=al, shadow=14, rot=2 * math.sin(t * 3))
    s, al, a = pop(t, 0.75, 0.5)
    if a > 0:
        put(img, age_badge(), 720, 900, scale=0.95 * s, alpha=al, shadow=12, rot=-8 + 5 * math.sin(t * 4))
        burst(img, t, 0.75, 720, 900, n=12, color=GOLD, dur=0.7, rad=250, seed=84)
    # carta del test lordo: entra, poi viene barrata
    a = seg(t, 1.6, 0.5)
    if a > 0:
        x = 540 - 300 * (1 - ease(a))
        dim = 1.0 - 0.55 * seg(t, 2.5, 0.4)
        put(img, test_card("GROSS INCOME", "THE FIRST TEST", CORAL, "bills"), x, 1240, alpha=ease(a) * dim, shadow=12, rot=-2 * seg(t, 2.5, 0.4))
    s, al, a = pop(t, 2.5, 0.4)
    if a > 0:
        put(img, bigx_spr(), 560, 1240, scale=0.62 * s, alpha=al, rot=-4)
        burst(img, t, 2.5, 560, 1240, n=10, color=CORAL, dur=0.6, rad=240, seed=85)
    s, al, a = pop(t, 2.9, 0.4)
    if a > 0:
        put(img, tag_spr("SKIPPED", 380, 110, CORAL, 56), 760, 1110, scale=s, alpha=al, rot=6, shadow=10)
    a = seg(t, 3.2, 0.5)
    if a > 0:
        put(img, test_card("NET INCOME", "STILL APPLIES", SAGE, "paper"), 540 + 300 * (1 - ease(a)), 1480, alpha=ease(a), shadow=12)
        put(img, check_spr(), 910, 1410, scale=0.55 * ease_back(seg(t, 3.5, 0.4)), alpha=ease(a))

# ---------------------------------------------------------------- clip 4: regola 2, spese mediche sopra 35$ al mese
def s4(img, t):
    ambient_food(img, t, n=7, seed=85)
    label(img, t, "RULE 2", 300, GOLD)
    for (x, t0, fn, sc, rot0) in ((250, 0.4, pill_bottle_spr, 1.0, -8), (540, 0.65, med_cross_spr, 0.95, 0), (830, 0.9, receipt_spr, 0.95, 8)):
        s, al, a = pop(t, t0, 0.45)
        if a > 0:
            put(img, fn(), x, 640 + 8 * math.sin(t * 3 + x), scale=sc * s, alpha=al, rot=rot0 + 3 * math.sin(t * 2.5 + x), shadow=14)
            burst(img, t, t0, x, 640, n=7, color=GOLD, dur=0.55, rad=170, seed=int(86 + x))
    a = seg(t, 1.1, 0.5)
    if a > 0:
        put(img, tspr("MEDICAL COSTS YOU PAY", FONT_SANS, 50, IVORY), 540, 850 + 20 * (1 - ease(a)), alpha=ease(a), shadow=6)
    s, al, a = pop(t, 2.3, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1010, scale=1.2, alpha=0.3 * al)
        put(img, tspr("$35+", FONT_SERIF, 270, GOLD), 540, 1010, scale=s, alpha=al, shadow=16)
        burst(img, t, 2.3, 540, 1010, n=14, color=GOLD, dur=0.7, rad=330, seed=87)
    a = seg(t, 2.9, 0.5)
    if a > 0:
        put(img, tspr("A MONTH", FONT_SANS, 62, SAGE, track=6), 540, 1160 + 20 * (1 - ease(a)), alpha=ease(a))
    # barra del reddito che si accorcia
    a = seg(t, 3.5, 0.4)
    if a > 0:
        put(img, tspr("COUNTED INCOME", FONT_SANS, 32, SAGE, track=7), 540, 1295, alpha=ease(a))
        d = ImageDraw.Draw(img)
        x0, y0, x1, y1 = 140, 1340, 940, 1420
        d.rounded_rectangle([x0 - 8, y0 - 8, x1 + 8, y1 + 8], radius=44, fill=(9, 46, 36), outline=SAGE_D, width=3)
        u = ease(seg(t, 4.4, 0.8))
        full = x1 - x0
        keep = int(full * (1 - 0.32 * u))
        d.rounded_rectangle([x0, y0, x0 + int(full * ease(a)) if u == 0 else x0 + keep, y1], radius=36, fill=GOLD)
        if u > 0:
            cut = full - keep
            if cut > 20:
                fy = 120 * u * u
                put(img, tag_spr("-$35", 220, 84, CORAL, 50), x0 + keep + cut / 2, y0 + 40 + fy, alpha=1 - 0.8 * u, rot=18 * u, shadow=6)
    a = seg(t, 4.6, 0.5)
    if a > 0:
        put(img, tspr("COMES OFF YOUR INCOME", FONT_SANS, 54, GOLD), 540, 1570 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)

# ---------------------------------------------------------------- clip 5: regola 3, risparmi 4.750$ e la casa non conta
def s5(img, t):
    ambient_food(img, t, n=7, seed=89)
    label(img, t, "RULE 3", 300, GOLD)
    mv = ease(seg(t, 3.0, 0.6))
    jx = 540 - 260 * mv
    s, al, a = pop(t, 0.1, 0.5)
    if a > 0:
        put(img, glow_spr(), jx, 780, scale=1.1, alpha=0.25 * al)
        put(img, savings_jar_spr(), jx, 790, scale=(0.85 - 0.12 * mv) * s, alpha=al, shadow=16)
    # monete che cadono nel barattolo
    for k in range(9):
        t0 = 0.5 + k * 0.18
        u = seg(t, t0, 0.45)
        if 0 < u < 1:
            put(img, coin_spr(), jx + (k % 3 - 1) * 34, 520 + (730 - 520) * u * u * (1.0 + 0.0 * k), scale=0.9, alpha=min(1.0, u * 4), rot=u * 360)
        elif u >= 1:
            put(img, coin_spr(), jx + (k % 3 - 1) * 46, 962 - (k // 3) * 34 - (k % 2) * 6, scale=0.85 * (1 - 0.12 * mv))
    # cifra che sale
    u = seg(t, 0.7, 1.6)
    if u > 0:
        n = int(round(4750 * ease(u)))
        put(img, tspr("$" + format(n, ","), FONT_SERIF, 220, GOLD), 540, 1230, shadow=14, scale=1.0 + 0.04 * max(0.0, math.sin(min(1.0, u) * 6.28)))
    if u >= 1.0:
        burst(img, t, 2.3, 540, 1230, n=14, color=GOLD, dur=0.7, rad=350, seed=90)
    a = seg(t, 2.35, 0.45)
    if a > 0:
        put(img, tspr("SAVINGS LIMIT", FONT_SANS, 46, SAGE, track=7), 540, 1405 + 20 * (1 - ease(a)), alpha=ease(a))
    # la casa non conta
    a = seg(t, 3.1, 0.55)
    if a > 0:
        hx = 790 + 300 * (1 - ease_back(a))
        put(img, glow_spr(), 790, 790, scale=0.9, alpha=0.22 * ease(a))
        put(img, house_spr(), hx, 790, scale=0.72, alpha=ease(a), shadow=14)
        put(img, tspr("YOUR HOME", FONT_SANS, 44, IVORY, track=4), 790, 990, alpha=ease(a))
    s, al, a = pop(t, 3.9, 0.45)
    if a > 0:
        put(img, stamp_spr("NOT COUNTED", 470, 118, CORAL), 790, 830, scale=s, alpha=al, rot=-12, shadow=12)
        burst(img, t, 3.9, 790, 850, n=12, color=CORAL, dur=0.6, rad=260, seed=91)
    a = seg(t, 4.3, 0.5)
    if a > 0:
        put(img, tspr("HOME DOESN'T COUNT", FONT_SANS, 62, GOLD), 540, 1580 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)

# ---------------------------------------------------------------- clip 6: varia per Stato + numero SNAP
NUM5 = "1-800-221-5689"
def num5_cuts():
    d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
    f = font(FONT_SANS, 104, True)
    pad = int(104 * 0.35)
    return pad, [pad + d0.textlength(NUM5[:k], font=f) for k in (2, 6, 10, 14)]

def s6(img, t):
    ambient_food(img, t, n=7, seed=93)
    if t < 2.0:
        label(img, t, "RULES VARY BY STATE", 300, SAGE)
    else:
        label(img, t, "SNAP INFO LINE", 300, GOLD, t0=2.0)
    # fase A: mappa con pin
    mp = 1.0 - seg(t, 2.1, 0.5)
    if mp > 0:
        s, al, a = pop(t, 0.0, 0.5)
        put(img, map_spr(), 540, 720 - 40 * (1 - mp), scale=1.1 * s, alpha=al * mp, shadow=16)
        for (px, py, col, t0, txt) in ((-250, -60, GOLD, 0.3, "TX"), (50, 60, SAGE, 0.55, "NY"), (290, -40, IVORY, 0.8, "CA"), (-80, 90, CORAL, 1.05, "FL")):
            if mp > 0.05:
                a2 = seg(t, t0, 0.45)
                if a2 > 0:
                    bx, by = 540 + px * 1.1, 720 + py * 1.1
                    put(img, pin_spr(col), bx, by - 60 - 220 * (1 - ease_back(a2)), alpha=min(1.0, a2 * 3) * mp)
                    put(img, tag_spr(txt, 150, 76, col, 44), bx, by - 190 - 220 * (1 - ease_back(a2)) * 0.2, alpha=ease(a2) * mp, shadow=6)
        u = seg(t, 1.0, 1.0)
        if u > 0:
            put(img, magnifier_spr(), 300 + 480 * ease(u), 660 + 40 * math.sin(u * 6.3), alpha=min(1.0, u * 4) * mp, rot=-8, shadow=10)
        a = seg(t, 0.8, 0.5)
        put(img, tspr("EVERY STATE", FONT_SANS, 92, GOLD), 540, 1100 + 24 * (1 - ease(a)), alpha=ease(a) * mp, shadow=8)
        a = seg(t, 1.2, 0.5)
        put(img, tspr("HAS ITS OWN RULES", FONT_SANS, 62, IVORY), 540, 1220 + 24 * (1 - ease(a)), alpha=ease(a) * mp, shadow=8)
    # fase B: telefono + numero
    s, al, a = pop(t, 2.45, 0.5)
    if a > 0:
        rings(img, t, 540, 610)
        put(img, handset_spr(), 540, 610, scale=0.85 * s, alpha=al, rot=5 * math.sin(t * 13), shadow=14)
    s, al, a = pop(t, 2.8, 0.45)
    if a > 0:
        put(img, numpanel_spr(), 540, 960, scale=s, alpha=al, shadow=14)
    pad, cuts = num5_cuts()
    sp = tspr(NUM5, FONT_SANS, 104, GOLD)
    w, h = sp.size
    marks = [(3.2, 0.4), (3.7, 0.9), (4.7, 1.0), (5.8, 1.4)]
    edges = [pad] + cuts
    upto = pad
    for k, (t0, d) in enumerate(marks):
        if t >= t0:
            upto = edges[k] + (edges[k + 1] - edges[k]) * ease(seg(t, t0, d))
    if upto > pad + 2:
        crop = sp.crop((0, 0, int(upto), h))
        img.paste(crop, (int(540 - w / 2), int(960 - h / 2)), crop)
    a = seg(t, 3.2, 0.5)
    if a > 0:
        put(img, tspr("USDA SNAP INFORMATION LINE", FONT_SANS, 30, SAGE, track=3), 540, 1090, alpha=ease(a))
    s, al, a = pop(t, 3.7, 0.45)
    if a > 0:
        put(img, tag_spr("TOLL-FREE", 400, 100, GOLD, 52), 540, 1230, scale=s, alpha=al, rot=-3, shadow=10)
    a = seg(t, 4.6, 0.5)
    if a > 0:
        put(img, tspr("TO APPLY: YOUR STATE SNAP OFFICE", FONT_SANS, 38, IVORY, track=2), 540, 1390 + 20 * (1 - ease(a)), alpha=ease(a))
    s, al, a = pop(t, 5.1, 0.5)
    if a > 0:
        put(img, link_pill_spr("fns.usda.gov/snap"), 540, 1540, scale=s, alpha=al, shadow=14)
        if t > 5.6:
            u = seg(t, 5.6, 0.6)
            put(img, cursor_spr(), 760 + 90 * (1 - ease(u)), 1590 + 70 * (1 - ease(u)), alpha=ease(u), shadow=6)

# ---------------------------------------------------------------- clip 7: "Want the full video? Click below!"
def s7(img, t):
    ambient_food(img, t, n=7, seed=95)
    label(img, t, "WANT MORE?", 300, GOLD)
    s, al, a = pop(t, 0.05, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 760, scale=1.5, alpha=0.3 * al)
        put(img, play_card_spr(), 540, 760, scale=1.12 * s * (1 + 0.015 * math.sin(t * 6)), alpha=al, shadow=18, rot=-2 * (1 - ease(a)))
        burst(img, t, 0.1, 540, 760, n=12, color=GOLD, dur=0.7, rad=420, seed=96)
    a = seg(t, 0.3, 0.4)
    if a > 0:
        put(img, tspr("THE FULL VIDEO", FONT_SANS, 84, IVORY), 540, 1130 + 22 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 0.95, 0.4)
    if a > 0:
        put(img, tspr("CLICK BELOW", FONT_SANS, 120, GOLD), 540, 1300 + 22 * (1 - ease(a)), alpha=ease(a), shadow=12)
    for k in range(3):
        a = seg(t, 1.0 + k * 0.12, 0.3)
        if a > 0:
            ph = (t * 2.2 - k * 0.22) % 1.0
            put(img, chevron_spr(), 540, 1490 + k * 80 + 34 * math.sin(ph * 6.28), alpha=ease(a) * (0.5 + 0.5 * math.sin(ph * 6.28) ** 2), scale=1.0)

# ---------------------------------------------------------------- clip 8: follow
def s8(img, t):
    ambient_food(img, t, n=7, seed=97)
    label(img, t, "THE SENIOR ADVANTAGE", 300, SAGE)
    s, al, a = pop(t, 0.03, 0.4)
    if a > 0:
        sw = 10 * math.sin((t - 0.3) * 18) * max(0.0, 1 - (t - 0.3) / 1.2)
        put(img, glow_spr(), 540, 640, scale=1.2, alpha=0.3 * al)
        put(img, bell_spr(), 540, 640, scale=1.5 * s, alpha=al, rot=sw, shadow=16)
        burst(img, t, 0.08, 540, 640, n=10, color=GOLD, dur=0.6, rad=280, seed=98)
    s, al, a = pop(t, 0.3, 0.4)
    if a > 0:
        put(img, tag_spr("FOLLOW", 640, 170, GOLD, 92), 540, 960, scale=s, alpha=al, shadow=14)
    a = seg(t, 0.65, 0.35)
    if a > 0:
        put(img, tspr("SO YOU DON'T", FONT_SANS, 88, IVORY), 540, 1190 + 22 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 0.95, 0.35)
    if a > 0:
        put(img, tspr("MISS IT", FONT_SANS, 130, GOLD), 540, 1340 + 22 * (1 - ease(a)), alpha=ease(a), shadow=10)
    a = seg(t, 1.25, 0.35)
    if a > 0:
        put(img, subpill_spr(), 540, 1590 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)

# durate in fotogrammi (dalla timeline CapCut, dalla fine del clip precedente)
SCENES5 = {1: (s1, 147), 2: (s2, 73), 3: (s3, 129), 4: (s4, 180), 5: (s5, 170), 6: (s6, 221), 7: (s7, 69), 8: (s8, 61)}

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES5)
    out_dir = os.environ.get("S5_OUT", "short5")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        fn, nf = SCENES5[k]
        render_seq(zoomed(fn), nf, f"{out_dir}/short5-clip{k:02d}.mp4")
