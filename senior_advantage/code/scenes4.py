import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes3 import *
from engine import panel

ICE = (170, 214, 232)

# =====================================================================
# SPRITE NUOVI (short 4: aiuto per le bollette di luce e riscaldamento)
# =====================================================================
def small_house(lit):
    def mk():
        c = Cv(120, 112)
        if lit:
            c.poly([(2, 52), (60, 4), (118, 52)], fill=(190, 140, 60))
            c.rrect((14, 46, 106, 106), 8, fill=(240, 205, 140), outline=(190, 140, 60), width=3)
            c.rrect((50, 66, 72, 106), 5, fill=DARK)
            c.rrect((22, 58, 44, 80), 4, fill=IVORY)
            c.rrect((80, 58, 100, 80), 4, fill=IVORY)
        else:
            c.poly([(2, 52), (60, 4), (118, 52)], fill=(52, 104, 84))
            c.rrect((14, 46, 106, 106), 8, fill=(22, 70, 56), outline=SAGE_D, width=3)
            c.rrect((50, 66, 72, 106), 5, fill=(9, 46, 36))
            c.rrect((22, 58, 44, 80), 4, outline=LINE, width=3)
            c.rrect((80, 58, 100, 80), 4, outline=LINE, width=3)
        return c.done()
    return cache(("shouse", lit), mk)

def bulb_spr():
    def mk():
        c = Cv(100, 150)
        c.ell((10, 4, 90, 84), fill=(255, 226, 140), outline=(190, 140, 60), width=4)
        c.rrect((30, 78, 70, 112), 6, fill=SAGE)
        c.rrect((34, 108, 66, 124), 6, fill=SAGE_D)
        c.ell((40, 122, 60, 140), fill=SAGE_D)
        c.line([40, 60, 50, 40, 60, 60], (190, 140, 60), 4)
        return c.done()
    return cache("bulb", mk)

def flame_spr():
    def mk():
        c = Cv(130, 180)
        c.poly([(66, 4), (104, 64), (120, 118), (64, 176), (10, 118), (26, 66), (44, 90)], fill=CORAL)
        c.ell((10, 88, 120, 176), fill=CORAL)
        c.ell((34, 104, 96, 176), fill=GOLD)
        c.ell((50, 132, 80, 176), fill=(255, 236, 170))
        return c.done()
    return cache("flame", mk)

def snow_spr():
    def mk():
        c = Cv(170, 170)
        cx = cy = 85
        for k in range(3):
            a = math.radians(90 + 60 * k)
            dx, dy = math.cos(a), math.sin(a)
            c.line([cx - dx * 74, cy - dy * 74, cx + dx * 74, cy + dy * 74], ICE, 9)
            for s in (1, -1):
                ex, ey = cx + s * dx * 74, cy + s * dy * 74
                bx, by = cx + s * dx * 50, cy + s * dy * 50
                for sg in (1, -1):
                    ang = a + sg * math.radians(40)
                    c.line([bx, by, bx + s * math.cos(ang) * 24, by + s * math.sin(ang) * 24], ICE, 7)
        c.ell((72, 72, 98, 98), fill=ICE)
        return c.done()
    return cache("snow", mk)

def crisis_spr():
    def mk():
        c = Cv(180, 160)
        c.poly([(90, 6), (172, 150), (8, 150)], fill=GOLD)
        c.poly([(90, 28), (150, 138), (30, 138)], fill=(255, 226, 150))
        c.poly([(98, 56), (64, 98), (88, 98), (78, 132), (116, 86), (92, 86)], fill=DARK)
        return c.done()
    return cache("crisis", mk)

def cat_badge(kind, ring):
    def mk():
        c = Cv(230, 230)
        c.ell((6, 6, 224, 224), fill=CARD, outline=ring, width=6)
        c.ell((20, 20, 210, 210), outline=LINE, width=2)
        im = c.done()
        ic = {"heat": flame_spr, "cool": snow_spr, "crisis": crisis_spr}[kind]()
        sc = 0.95 if kind != "heat" else 0.9
        ic = ic.resize((int(ic.width * sc), int(ic.height * sc)), Image.LANCZOS)
        im.alpha_composite(ic, ((230 - ic.width) // 2, (230 - ic.height) // 2 + 4))
        return im
    return cache(("cbadge", kind), mk)

def building_spr():
    def mk():
        c = Cv(660, 430)
        c.poly([(20, 128), (330, 22), (640, 128)], fill=IVORY)
        c.poly([(70, 120), (330, 44), (590, 120)], fill=(226, 220, 204))
        c.ell((300, 58, 360, 118), fill=GOLD, outline=(190, 140, 60), width=4)
        c.rrect((40, 128, 620, 160), 6, fill=(214, 208, 194))
        for k in range(6):
            x = 68 + k * 100
            c.rrect((x, 166, x + 48, 336), 6, fill=IVORY)
            c.rrect((x + 30, 166, x + 48, 336), 6, fill=(214, 208, 194))
            c.rrect((x - 6, 160, x + 54, 176), 4, fill=(226, 220, 204))
            c.rrect((x - 6, 330, x + 54, 346), 4, fill=(226, 220, 204))
        c.rrect((26, 346, 634, 376), 6, fill=(190, 184, 170))
        c.rrect((8, 376, 652, 408), 6, fill=(168, 162, 148))
        return c.done()
    return cache("liheap_bld", mk)

def elder_spr():
    def mk():
        c = Cv(300, 300)
        c.ell((6, 6, 294, 294), fill=(26, 92, 71))
        c.ell((40, 206, 260, 400), fill=SAGE_D)
        c.poly([(120, 206), (180, 206), (150, 262)], fill=IVORY)
        c.rrect((130, 176, 170, 222), 14, fill=(214, 170, 130))
        c.ell((86, 52, 214, 150), fill=(240, 240, 236))
        c.ell((98, 78, 202, 196), fill=(236, 194, 154))
        c.ell((80, 100, 112, 160), fill=(240, 240, 236))
        c.ell((188, 100, 220, 160), fill=(240, 240, 236))
        c.ell((92, 118, 112, 148), fill=(236, 194, 154))
        c.ell((188, 118, 208, 148), fill=(236, 194, 154))
        c.ell((98, 84, 202, 112), fill=(240, 240, 236))
        c.line([112, 112, 136, 108], (220, 220, 214), 5)
        c.line([164, 108, 188, 112], (220, 220, 214), 5)
        c.ell((110, 122, 146, 156), outline=GOLD, width=5)
        c.ell((154, 122, 190, 156), outline=GOLD, width=5)
        c.line([146, 138, 154, 138], GOLD, 4)
        c.ell((124, 135, 134, 145), fill=DARK)
        c.ell((166, 135, 176, 145), fill=DARK)
        c.arc((124, 150, 176, 184), 20, 160, (170, 90, 80), 5)
        mask = Image.new("L", c.im.size, 0)
        ImageDraw.Draw(mask).ellipse([6 * 2, 6 * 2, 294 * 2, 294 * 2], fill=255)
        c.im.putalpha(ImageChops.multiply(c.im.getchannel("A"), mask))
        c.ell((6, 6, 294, 294), outline=GOLD, width=8)
        return c.done()
    return cache("elder", mk)

def magnifier_spr():
    def mk():
        c = Cv(230, 230)
        c.line([132, 132, 214, 214], (190, 140, 60), 30)
        c.line([132, 132, 214, 214], GOLD, 22)
        c.ell((10, 10, 150, 150), fill=(154, 200, 170, 55))
        c.ell((10, 10, 150, 150), outline=GOLD, width=14)
        return c.done()
    return cache("magn", mk)

def clock_spr():
    def mk():
        c = Cv(290, 310)
        c.ell((22, 8, 112, 92), fill=GOLD, outline=(190, 140, 60), width=4)
        c.ell((178, 8, 268, 92), fill=GOLD, outline=(190, 140, 60), width=4)
        c.line([70, 252, 44, 296], (190, 140, 60), 14)
        c.line([220, 252, 246, 296], (190, 140, 60), 14)
        c.ell((26, 40, 264, 278), fill=IVORY, outline=GOLD, width=12)
        c.ell((48, 62, 242, 256), outline=(214, 208, 194), width=3)
        for k in range(12):
            a = math.radians(k * 30)
            r1, r2 = 84, 98
            c.line([145 + math.sin(a) * r1, 159 - math.cos(a) * r1, 145 + math.sin(a) * r2, 159 - math.cos(a) * r2], DARK, 5)
        c.line([145, 159, 145, 92], DARK, 9)
        c.line([145, 159, 192, 182], CORAL, 9)
        c.ell((133, 147, 157, 171), fill=DARK)
        return c.done()
    return cache("clock", mk)

def calendar_spr():
    def mk():
        c = Cv(330, 350)
        c.rrect((0, 22, 330, 346), 28, fill=IVORY)
        c.rrect((0, 22, 330, 112), 28, fill=CORAL)
        c.rrect((0, 74, 330, 112), 2, fill=CORAL)
        c.rrect((78, 0, 100, 56), 8, fill=DARK)
        c.rrect((230, 0, 252, 56), 8, fill=DARK)
        c.text((165, 70), "EARLY", FONT_SANS, 50, IVORY, track=4)
        for r in range(4):
            for q in range(5):
                c.rrect((24 + q * 58, 130 + r * 52, 24 + q * 58 + 40, 130 + r * 52 + 36), 8, fill=(214, 208, 194))
        c.ell((50, 118, 106, 176), outline=GOLD, width=8)
        c.rrect((24, 130, 24 + 40, 166), 8, fill=GOLD)
        return c.done()
    return cache("cal", mk)

def bell_spr():
    def mk():
        c = Cv(210, 230)
        c.ell((90, 2, 120, 32), fill=(190, 140, 60))
        c.ell((30, 18, 180, 170), fill=GOLD, outline=(190, 140, 60), width=5)
        c.poly([(30, 96), (180, 96), (200, 174), (10, 174)], fill=GOLD)
        c.line([30, 96, 10, 174], (190, 140, 60), 5)
        c.line([180, 96, 200, 174], (190, 140, 60), 5)
        c.rrect((8, 166, 202, 188), 10, fill=(214, 160, 80), outline=(190, 140, 60), width=4)
        c.ell((84, 182, 126, 224), fill=(190, 140, 60))
        c.arc((54, 46, 110, 120), 200, 260, (255, 236, 170), 8)
        return c.done()
    return cache("bell", mk)

def browser_spr():
    def mk():
        c = Cv(900, 190)
        c.rrect((3, 3, 897, 187), 30, fill=CARD, outline=SAGE_D, width=5)
        for i, col in enumerate((CORAL, GOLD, SAGE)):
            c.ell((30 + i * 34, 22, 52 + i * 34, 44), fill=col)
        c.rrect((30, 66, 870, 164), 44, fill=IVORY)
        c.text((450, 117), "energyhelp.us", FONT_SANS, 62, DARK, track=1)
        return c.done()
    return cache("browser", mk)

def cursor_spr():
    def mk():
        c = Cv(80, 100)
        c.poly([(8, 4), (8, 76), (28, 58), (42, 92), (56, 86), (42, 54), (68, 54)], fill=IVORY)
        c.poly([(14, 18), (14, 62), (28, 50), (40, 80), (44, 78), (32, 46), (50, 46)], fill=DARK)
        return c.done()
    return cache("cursor", mk)

def day_chip(letter, on):
    def mk():
        c = Cv(124, 124)
        if on:
            c.ell((4, 4, 120, 120), fill=GOLD, outline=(190, 140, 60), width=5)
            c.text((62, 64), letter, FONT_SANS, 58, DARK)
        else:
            c.ell((4, 4, 120, 120), fill=CARD, outline=SAGE_D, width=5)
            c.text((62, 64), letter, FONT_SANS, 58, SAGE_D)
        return c.done()
    return cache(("day", letter, on), mk)

def fin(a):
    return ease(seg(a, 0, 1))

# =====================================================================
# SCENE
# =====================================================================
def n1(img, t):
    ambient(img, t, "$%", n=8, seed=51)
    if t < 2.0:
        label(img, t, "WAIT...", 300, CORAL)
    else:
        label(img, t, "ENERGY BILLS", 300, SAGE, t0=2.0)
    lit_i = 6
    for i in range(8):
        x = 540 + (i % 4 - 1.5) * 232
        y = 600 + (i // 4) * 250
        s, al, a = pop(t, 0.15 + 0.12 * i, 0.4)
        if a > 0:
            lit = (i == lit_i and t > 2.0)
            if lit:
                u = seg(t, 2.0, 0.5)
                put(img, glow_spr(), x, y, scale=1.0, alpha=0.5 * ease(u))
                put(img, small_house(True), x, y - 4 * math.sin((t - 2.0) * 6), scale=1.7 * s * (1 + 0.08 * ease(u)), alpha=al, shadow=10)
            else:
                put(img, small_house(False), x, y, scale=1.6 * s, alpha=al * (0.9 if t < 2.0 else 0.6), shadow=6)
    x6, y6 = 540 + (6 % 4 - 1.5) * 232, 600 + 250
    s, al, a = pop(t, 2.2, 0.5)
    if a > 0:
        put(img, bulb_spr(), x6, y6 - 190 - 6 * math.sin(t * 4), scale=s * 0.9, alpha=al)
        burst(img, t, 2.2, x6, y6, n=10, color=GOLD, dur=0.7, rad=230, seed=52)
    s, al, a = pop(t, 2.0, 0.5)
    if a > 0:
        put(img, tspr("1 IN 8", FONT_SERIF, 250, GOLD), 540, 1150, scale=s, alpha=al, shadow=14)
    a = seg(t, 2.8, 0.5)
    if a > 0:
        put(img, tspr("HOMES THAT QUALIFY", FONT_SANS, 44, SAGE, track=6), 540, 1300, alpha=ease(a))
    a = seg(t, 4.0, 0.5)
    if a > 0:
        put(img, tspr("GET HELP", FONT_SANS, 92, IVORY), 540, 1425 + 24 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 4.6, 0.5)
    if a > 0:
        put(img, tspr("WITH ENERGY BILLS", FONT_SANS, 58, GOLD), 540, 1530 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)

def n2(img, t):
    ambient(img, t, "$", n=7, seed=53)
    label(img, t, "FEDERAL PROGRAM", 300, SAGE)
    s, al, a = pop(t, 0.05, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 680, scale=1.3, alpha=0.25 * al)
        put(img, building_spr(), 540, 690, scale=1.28 * s, alpha=al, shadow=18)
    s, al, a = pop(t, 0.95, 0.5)
    if a > 0:
        put(img, tspr("LIHEAP", FONT_SERIF, 260, IVORY), 540, 1140, scale=s, alpha=al, shadow=16)
        burst(img, t, 0.95, 540, 1140, n=12, color=GOLD, dur=0.7, rad=330, seed=54)
    a = seg(t, 1.5, 0.5)
    if a > 0:
        put(img, tspr("LOW INCOME HOME", FONT_SANS, 40, SAGE, track=5), 540, 1330, alpha=ease(a))
        put(img, tspr("ENERGY ASSISTANCE PROGRAM", FONT_SANS, 40, SAGE, track=5), 540, 1390, alpha=ease(a))

def n3(img, t):
    ambient(img, t, "%$", n=8, seed=55)
    label(img, t, "IT CAN HELP WITH", 300, SAGE)
    cols = [(220, "heat", "HEATING", GOLD, 0.8, GOLD),
            (540, "cool", "COOLING", ICE, 1.7, ICE),
            (860, "crisis", "CRISIS HELP", CORAL, 3.0, CORAL)]
    for (x, kind, txt, col, t0, bc) in cols:
        s, al, a = pop(t, t0, 0.5)
        if a > 0:
            put(img, glow_spr(), x, 760, scale=0.9, alpha=0.28 * al)
            wob = 0
            if kind == "heat":
                wob = 4 * math.sin(t * 9)
            if kind == "cool":
                wob = 6 * math.sin(t * 4)
            put(img, cat_badge(kind, col), x, 760 + (wob if kind == "heat" else 0), scale=1.15 * s, alpha=al,
                rot=(wob if kind == "cool" else 0), shadow=14)
            put(img, tspr(txt, FONT_SANS, 40 if kind != "crisis" else 36, IVORY, track=3), x, 960, alpha=al)
            burst(img, t, t0, x, 760, n=9, color=bc, dur=0.6, rad=190, seed=60 + x)
    # casa al centro che reagisce
    s, al, a = pop(t, 0.2, 0.55)
    if a > 0:
        put(img, house_spr(), 540, 1330, scale=1.2 * s, alpha=al, shadow=16)
    if t > 0.9:
        warm = seg(t, 0.9, 0.6) * (1 - seg(t, 1.8, 0.5))
        if warm > 0:
            put(img, glow_spr(), 540, 1360, scale=1.3, alpha=0.35 * warm)
        cold = seg(t, 1.8, 0.6) * (1 - seg(t, 3.0, 0.5))
        if cold > 0:
            for k in range(5):
                put(img, snow_spr(), 330 + k * 105, 1160 + 40 * math.sin(t * 3 + k) + ((t * 60 + k * 70) % 120),
                    scale=0.35, alpha=0.8 * cold, rot=t * 90 + k * 30)
    a = seg(t, 3.3, 0.5)
    if a > 0:
        put(img, tspr("EVEN IN A CRISIS", FONT_SANS, 60, GOLD), 540, 1640 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)

def n4(img, t):
    ambient(img, t, "$%", n=8, seed=56)
    if t < 2.5:
        label(img, t, "OLDER ADULT AT HOME?", 300, SAGE)
    else:
        label(img, t, "PRIORITY GROUP", 300, GOLD, t0=2.5)
    s, al, a = pop(t, 0.05, 0.55)
    if a > 0:
        put(img, house_spr(), 540, 800, scale=1.55 * s, alpha=al, shadow=18)
    s, al, a = pop(t, 0.7, 0.5)
    if a > 0:
        put(img, elder_spr(), 540, 840, scale=0.85 * s, alpha=al, shadow=14, rot=2 * math.sin(t * 3))
    a = seg(t, 1.3, 0.4)
    if a > 0 and t < 2.6:
        put(img, tspr("?", FONT_SERIF, 180, GOLD), 790 + 8 * math.sin(t * 5), 560 + 10 * math.sin(t * 4), alpha=ease(a), rot=12, shadow=8)
    s, al, a = pop(t, 2.6, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1330, scale=1.3, alpha=0.3 * al)
        put(img, tag_spr("PRIORITY", 720, 190, GOLD, 100), 540, 1330, scale=s, alpha=al, rot=-3, shadow=14)
        burst(img, t, 2.6, 540, 1330, n=14, color=GOLD, dur=0.7, rad=360, seed=57)
    a = seg(t, 3.2, 0.5)
    if a > 0:
        put(img, tspr("OLDER ADULTS COUNT", FONT_SANS, 52, IVORY), 540, 1490 + 20 * (1 - ease(a)), alpha=ease(a), shadow=8)

def n5(img, t):
    ambient(img, t, "$%", n=8, seed=58)
    label(img, t, "YOUR STATE", 300, SAGE)
    s, al, a = pop(t, 0.0, 0.5)
    if a > 0:
        put(img, map_spr(), 540, 700, scale=1.1 * s, alpha=al, shadow=16)
    for (px, py, col, t0, txt) in [(-250, -60, GOLD, 0.35, "$"), (50, 60, SAGE, 0.6, "$$"), (290, -40, IVORY, 0.85, "$$$")]:
        a = seg(t, t0, 0.45)
        if a > 0:
            bx, by = 540 + px * 1.1, 700 + py * 1.1
            put(img, pin_spr(col), bx, by - 60 - 220 * (1 - ease_back(a)), alpha=min(1.0, a * 3))
            put(img, tag_spr(txt, 150, 76, col, 44), bx, by - 190 - 220 * (1 - ease_back(a)) * 0.2, alpha=ease(a), shadow=6)
    u = seg(t, 1.3, 1.4)
    if u > 0:
        mx = 300 + 480 * ease(u)
        my = 640 + 40 * math.sin(u * 6.3)
        put(img, magnifier_spr(), mx, my, alpha=min(1.0, u * 4), rot=-8, shadow=10)
    a = seg(t, 0.9, 0.5)
    if a > 0:
        put(img, tspr("INCOME LIMITS", FONT_SANS, 92, GOLD), 540, 1060 + 24 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 1.3, 0.5)
    if a > 0:
        put(img, tspr("DEPEND ON YOUR STATE", FONT_SANS, 58, IVORY), 540, 1180 + 24 * (1 - ease(a)), alpha=ease(a), shadow=8)
    s, al, a = pop(t, 2.0, 0.45)
    if a > 0:
        put(img, tag_spr("CHECK YOURS", 560, 120, SAGE, 54), 540, 1380, scale=s, alpha=al, shadow=10)

NUM = "1-866-674-6327"
def num_cuts():
    d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
    f = font(FONT_SANS, 104, True)
    pad = int(104 * 0.35)
    return pad, [pad + d0.textlength(NUM[:k], font=f) for k in (2, 6, 10, 14)]

def n6(img, t):
    ambient(img, t, "$%", n=8, seed=59)
    label(img, t, "HOW TO APPLY", 300, GOLD)
    s, al, a = pop(t, 0.0, 0.5)
    if a > 0:
        rings(img, t, 540, 610)
        put(img, handset_spr(), 540, 610, scale=0.85 * s, alpha=al, rot=5 * math.sin(t * 13), shadow=14)
    s, al, a = pop(t, 0.3, 0.45)
    if a > 0:
        put(img, numpanel_spr(), 540, 960, scale=s, alpha=al, shadow=14)
    pad, cuts = num_cuts()
    sp = tspr(NUM, FONT_SANS, 104, GOLD)
    w, h = sp.size
    marks = [(0.55, 0.4), (1.05, 0.8), (2.25, 0.8), (3.45, 1.2)]
    edges = [pad] + cuts
    upto = pad
    for k, (t0, d) in enumerate(marks):
        if t >= t0:
            upto = edges[k] + (edges[k + 1] - edges[k]) * ease(seg(t, t0, d))
    if upto > pad + 2:
        crop = sp.crop((0, 0, int(upto), h))
        img.paste(crop, (int(540 - w / 2), int(960 - h / 2)), crop)
    a = seg(t, 0.8, 0.5)
    if a > 0:
        put(img, tspr("NATIONAL ENERGY ASSISTANCE REFERRAL", FONT_SANS, 28, SAGE, track=3), 540, 1090, alpha=ease(a))
    # giorni feriali
    for i, L in enumerate("MTWTF"):
        s, al, a = pop(t, 5.1 + 0.12 * i, 0.4)
        if a > 0:
            put(img, day_chip(L, True), 540 + (i - 2) * 150, 1230, scale=0.95 * s, alpha=al, shadow=8)
    a = seg(t, 5.7, 0.5)
    if a > 0:
        put(img, tspr("WEEKDAYS  9AM TO 7PM ET", FONT_SANS, 40, IVORY, track=3), 540, 1340, alpha=ease(a))
    a = seg(t, 6.3, 0.5)
    if a > 0:
        put(img, tspr("OR GO ONLINE", FONT_SANS, 46, SAGE, track=7), 540, 1450, alpha=ease(a))
    s, al, a = pop(t, 6.7, 0.5)
    if a > 0:
        put(img, browser_spr(), 540, 1610, scale=s, alpha=al, shadow=14)
        if t > 7.4:
            u = seg(t, 7.4, 0.7)
            put(img, cursor_spr(), 760 + 120 * (1 - ease(u)), 1700 + 90 * (1 - ease(u)), alpha=ease(u), shadow=6)
            burst(img, t, 8.3, 640, 1620, n=8, color=GOLD, dur=0.5, rad=170, seed=61)

def n7(img, t):
    ambient(img, t, "$%", n=8, seed=62)
    label(img, t, "FUNDING IS LIMITED", 300, CORAL)
    # misuratore del fondo che si svuota
    bx = (110, 640, 970, 790)
    s, al, a = pop(t, 0.0, 0.4)
    if a > 0:
        panel(img, bx, radius=44, fill=CARD, border=GOLD, bw=5)
        d = ImageDraw.Draw(img)
        frac = 1.0 - 0.84 * ease(seg(t, 0.35, 1.7))
        x0, y0, x1, y1 = 140, 670, 940, 760
        d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=(9, 46, 36))
        fw = int((x1 - x0) * frac)
        if fw > 24:
            col = GOLD if frac > 0.4 else CORAL
            d.rounded_rectangle([x0, y0, x0 + fw, y1], radius=30, fill=col)
        put(img, tspr("FUNDING", FONT_SANS, 34, SAGE, track=8), 540, 610, alpha=al)
    s, al, a = pop(t, 1.9, 0.5)
    if a > 0:
        shake = 6 * math.sin(t * 40) * (1.0 if t < 3.0 else 0.0)
        put(img, clock_spr(), 340 + shake, 1120, scale=1.0 * s, alpha=al, shadow=14, rot=shake)
        for k in range(3):
            put(img, tspr("(", FONT_SANS, 70, GOLD), 190 - k * 20, 1010 + 6 * math.sin(t * 20 + k), alpha=al * 0.5, rot=20)
    s, al, a = pop(t, 2.45, 0.5)
    if a > 0:
        put(img, calendar_spr(), 760, 1130, scale=0.95 * s, alpha=al, shadow=14, rot=4 * (1 - ease(a)))
        burst(img, t, 2.5, 760, 1130, n=10, color=GOLD, dur=0.6, rad=230, seed=63)
    a = seg(t, 2.6, 0.5)
    if a > 0:
        put(img, tspr("APPLY EARLY", FONT_SERIF, 140, GOLD), 540, 1500 + 24 * (1 - ease(a)), alpha=ease(a), shadow=12)

def n8(img, t):
    ambient(img, t, "$%", n=8, seed=64)
    label(img, t, "THE SENIOR ADVANTAGE", 300, SAGE)
    s, al, a = pop(t, 0.05, 0.5)
    if a > 0:
        sw = 10 * math.sin((t - 0.4) * 18) * max(0.0, 1 - (t - 0.4) / 1.6)
        put(img, glow_spr(), 540, 640, scale=1.2, alpha=0.3 * al)
        put(img, bell_spr(), 540, 640, scale=1.5 * s, alpha=al, rot=sw, shadow=16)
        burst(img, t, 0.1, 540, 640, n=10, color=GOLD, dur=0.6, rad=280, seed=65)
    s, al, a = pop(t, 0.5, 0.45)
    if a > 0:
        put(img, tag_spr("FOLLOW", 640, 170, GOLD, 92), 540, 960, scale=s, alpha=al, shadow=14)
    a = seg(t, 1.0, 0.5)
    if a > 0:
        put(img, tspr("FOR MORE HELP", FONT_SANS, 74, IVORY), 540, 1160 + 24 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 1.5, 0.5)
    if a > 0:
        put(img, tspr("MOST SENIORS", FONT_SANS, 90, IVORY), 540, 1290 + 24 * (1 - ease(a)), alpha=ease(a), shadow=8)
    a = seg(t, 2.0, 0.5)
    if a > 0:
        put(img, tspr("NEVER CLAIM", FONT_SANS, 110, GOLD), 540, 1430 + 24 * (1 - ease(a)), alpha=ease(a), shadow=10)
    a = seg(t, 2.3, 0.5)
    if a > 0:
        put(img, subpill_spr(), 540, 1620 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)

# durate in fotogrammi (dagli screenshot della timeline CapCut, partendo dalla fine del clip precedente)
SCENES4 = {1: (n1, 186), 2: (n2, 78), 3: (n3, 146), 4: (n4, 139), 5: (n5, 101), 6: (n6, 292), 7: (n7, 109), 8: (n8, 94)}

if __name__ == "__main__":
    k = int(sys.argv[1])
    out_dir = os.environ.get("S4_OUT", "short4")
    os.makedirs(out_dir, exist_ok=True)
    fn, nf = SCENES4[k]
    render_seq(fn, nf, f"{out_dir}/short4-clip{k:02d}.mp4")
