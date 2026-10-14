import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes8 import *

# =====================================================================
# SHORT 9: Aeroporto (correlato al video lungo 5). Stesso motore degli short 5-8, look un po' piu' pulito:
# intestazione a pillola con aereo + puntini di avanzamento (1-7), aerei leggeri sullo sfondo, disegni piu' grandi e semplici.
# Durate (fotogrammi): 256 197 206 259 216 210 202. Ultimo elemento di ogni blocco entro l'80%.
# Nelle slide compare SOLO cio' che la voce dice (nessuna casella vuota).
# uso: S9_OUT=cartella SA_TMP=/tmp/x python3 scenes9.py <clip>
# =====================================================================
SKY = (120, 176, 214)

# ------------------------------------------------------------------ sprite
def plane_draw(c, x, y, s=1.0, col=IVORY, outline=None):
    """aereo che guarda a destra, centro in (x, y), lunghezza ~200*s"""
    def P(pts, **k): c.poly([(x + px * s, y + py * s) for px, py in pts], **k)
    P([(-100, -6), (-82, -22), (70, -22), (100, -6), (100, 6), (70, 16), (-82, 16)], fill=col)
    P([(-10, -16), (30, -78), (52, -78), (30, -16)], fill=col)
    P([(-10, 10), (30, 72), (52, 72), (30, 10)], fill=col)
    P([(-96, -10), (-110, -58), (-86, -58), (-56, -16)], fill=col)
    for k in range(7):
        c.ell((x + (-60 + k * 20) * s - 4 * s, y - 14 * s, x + (-60 + k * 20) * s + 4 * s, y - 6 * s), fill=SKY)

def plane_spr(col=IVORY, w=300, h=190):
    def mk():
        c = Cv(w, h)
        plane_draw(c, w / 2, h / 2, w / 240.0, col)
        return c.done()
    return cache(("plane9", col, w, h), mk)

def hdr_spr(text, color):
    def mk():
        ts = tspr(text, FONT_SANS, 40, color, track=8)
        w, h = ts.width + 190, 104
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 52, fill=(10, 48, 38), outline=color, width=4)
        c.ell((20, 20, 84, 84), fill=color)
        plane_draw(c, 52, 52, 0.17, DARK)
        im = c.done()
        im.paste(ts, (100, (h - ts.height) // 2), ts)
        return im
    return cache(("hdr9", text, color), mk)

def hdr(img, t, text, y, color, k):
    a = seg(t, 0.0, 0.5)
    if a > 0:
        put(img, hdr_spr(text, color), W // 2, y - 36 * (1 - ease(a)), alpha=ease(a), shadow=6)
        for i in range(7):
            col = color if i == k - 1 else (60, 112, 92)
            put(img, dot_spr(col, 9 if i == k - 1 else 7), 540 + (i - 3) * 44, y + 84, alpha=ease(a))

def ambient9(img, t, n=3, seed=9, alpha=0.10):
    rnd = random.Random(seed)
    sp = plane_spr((190, 224, 210), 220, 140)
    for i in range(n):
        v = rnd.uniform(40, 70)
        y = rnd.uniform(520, 1700)
        off = rnd.uniform(0, W + 500)
        x = (off + t * v) % (W + 500) - 250
        put(img, sp, x, y + 10 * math.sin(t * 0.8 + i), scale=rnd.choice([0.6, 0.8]), alpha=alpha, rot=8)

def arch_spr():
    def mk():
        c = Cv(380, 520)
        for x0 in (20, 290):
            c.rrect((x0, 60, x0 + 70, 510), 14, fill=(26, 90, 72), outline=SAGE_D, width=5)
            c.rrect((x0 + 16, 120, x0 + 54, 420), 8, fill=(18, 70, 56))
        c.rrect((10, 14, 370, 104), 20, fill=(22, 82, 64), outline=GOLD, width=6)
        c.ell((166, 40, 214, 88), fill=(110, 220, 130), outline=DARK, width=4)
        c.text((190, 258), "", FONT_SANS, 20, IVORY)
        return c.done()
    return cache("arch9", mk)

def belt_spr():
    def mk():
        c = Cv(640, 320)
        c.rrect((130, 20, 510, 210), 30, fill=(22, 82, 64), outline=SAGE_D, width=6)
        for k in range(5):
            c.rrect((150 + k * 70, 40, 168 + k * 70, 190), 6, fill=(14, 58, 45))
        c.rrect((6, 200, 634, 262), 26, fill=(44, 48, 48), outline=(110, 116, 116), width=5)
        for k in range(9):
            c.ell((30 + k * 68, 276, 62 + k * 68, 308), fill=(70, 74, 74))
        c.rrect((60, 140, 200, 204), 12, fill=(120, 170, 190), outline=IVORY, width=4)
        c.rrect((420, 150, 560, 204), 12, fill=(214, 108, 96), outline=IVORY, width=4)
        c.line([450, 150, 450, 128, 530, 128, 530, 150], IVORY, 6)
        return c.done()
    return cache("belt9", mk)

def shoe_draw(c, x, y, flip=False, col=IVORY):
    sg = -1 if flip else 1
    def P(pts, **k):
        c.poly([(x + sg * px, y + py) for px, py in pts], **k)
    P([(0, 0), (0, -62), (8, -112), (62, -122), (92, -98), (150, -74), (214, -58), (256, -32), (270, -6), (270, 14), (0, 14)], fill=col)
    P([(0, -62), (8, -112), (62, -122), (70, -80), (30, -52)], fill=(0, 0, 0, 40))
    c.line([x + sg * 30, y - 22, x + sg * 120, y - 18, x + sg * 226, y - 22], CORAL, 9)
    for k in range(3):
        c.line([x + sg * (104 + k * 32), y - 92 + k * 10, x + sg * (130 + k * 32), y - 66 + k * 10], DARK, 6)
    xa, xb = sorted((x - sg * 6, x + sg * 278))
    c.rrect((xa, y + 8, xb, y + 44), 18, fill=(30, 40, 40), outline=SAGE_D, width=3)

def shoes_spr():
    def mk():
        c = Cv(640, 300)
        shoe_draw(c, 30, 170, False, IVORY)
        shoe_draw(c, 610, 190, True, SAGE)
        return c.done()
    return cache("shoes9", mk)

def flight_card_spr():
    def mk():
        c = Cv(640, 300)
        c.rrect((4, 4, 636, 296), 34, fill=CARD, outline=GOLD, width=6)
        c.rrect((4, 4, 636, 90), 34, fill=(22, 82, 64))
        c.rrect((4, 60, 636, 90), 2, fill=(22, 82, 64))
        c.text((320, 48), "YOUR FLIGHT", FONT_SANS, 40, IVORY, track=6)
        plane_draw(c, 320, 200, 0.9, IVORY)
        return c.done()
    return cache("fcard9", mk)

def wallet_spr():
    def mk():
        c = Cv(420, 320)
        for k, dx in enumerate((-30, 0, 30)):
            c.rrect((70 + dx, 14 + k * 8, 350 + dx, 110 + k * 8), 12, fill=(128, 196, 146), outline=(70, 130, 90), width=4)
        c.rrect((10, 70, 410, 300), 34, fill=(150, 110, 70), outline=(110, 74, 44), width=6)
        c.rrect((10, 70, 410, 170), 34, fill=(176, 132, 84), outline=(110, 74, 44), width=6)
        c.ell((180, 150, 240, 210), fill=GOLD, outline=CRUST_D, width=4)
        return c.done()
    return cache("wallet9", mk)

def bill9_spr():
    def mk():
        c = Cv(260, 130)
        c.rrect((4, 4, 256, 126), 14, fill=(128, 196, 146), outline=(70, 130, 90), width=5)
        c.ell((90, 22, 170, 108), fill=(176, 224, 188), outline=(70, 130, 90), width=4)
        c.text((130, 66), "$", FONT_SANS, 62, (40, 100, 66))
        return c.done()
    return cache("bill9", mk)

def counter9_spr():
    def mk():
        c = Cv(760, 420)
        c.rrect((20, 190, 740, 410), 20, fill=(22, 82, 64), outline=SAGE_D, width=5)
        c.rrect((8, 160, 752, 214), 16, fill=(236, 190, 120), outline=CRUST_D, width=4)
        c.rrect((190, 10, 570, 120), 20, fill=DARK, outline=GOLD, width=5)
        c.text((380, 66), "COUNTER", FONT_SANS, 46, GOLD, track=10)
        return c.done()
    return cache("counter9", mk)

def calendar_spr():
    def mk():
        c = Cv(640, 560)
        c.rrect((8, 50, 632, 550), 30, fill=IVORY, outline=(206, 200, 186), width=6)
        c.rrect((8, 50, 632, 150), 30, fill=CORAL)
        c.rrect((8, 110, 632, 150), 2, fill=CORAL)
        c.text((320, 102), "DAYS BEFORE", FONT_SANS, 42, IVORY, track=5)
        for x in (150, 490):
            c.rrect((x - 10, 14, x + 10, 84), 10, fill=DARK)
        for r in range(4):
            for q in range(7):
                x, y = 40 + q * 80, 176 + r * 90
                c.rrect((x, y, x + 66, y + 74), 12, fill=(228, 224, 210))
        for q in (1, 2, 3):   # giorni prima
            x, y = 40 + q * 80, 176 + 90
            c.rrect((x, y, x + 66, y + 74), 12, fill=GOLD, outline=CRUST_D, width=3)
        x, y = 40 + 5 * 80, 176 + 90
        c.rrect((x, y, x + 66, y + 74), 12, fill=DARK)
        plane_draw(c, x + 33, y + 38, 0.2, IVORY)
        return c.done()
    return cache("cal9", mk)

def phone9_spr():
    def mk():
        c = Cv(300, 520)
        c.rrect((8, 8, 292, 512), 52, fill=(20, 24, 24), outline=GOLD, width=7)
        c.rrect((28, 66, 272, 446), 14, fill=(22, 82, 64))
        c.text((150, 170), "CALL", FONT_SANS, 62, IVORY, track=4)
        c.ell((90, 250, 210, 370), fill=(96, 200, 120), outline=DARK, width=4)
        c.line([124, 326, 122, 296, 142, 280, 158, 280, 178, 296, 176, 326], DARK, 16)
        c.ell((110, 316, 138, 344), fill=DARK)
        c.ell((162, 316, 190, 344), fill=DARK)
        c.rrect((110, 26, 190, 38), 6, fill=(60, 66, 66))
        c.ell((120, 462, 180, 500), fill=(60, 66, 66))
        return c.done()
    return cache("phone9", mk)

def agebadge9_spr():
    def mk():
        c = Cv(300, 300)
        pts = []
        for i in range(28):
            ang = math.pi * 2 * i / 28 - math.pi / 2
            r = 144 if i % 2 == 0 else 124
            pts.append((150 + r * math.cos(ang), 150 + r * math.sin(ang)))
        c.poly(pts, fill=GOLD)
        c.ell((30, 30, 270, 270), outline=CRUST_D, width=5)
        c.text((150, 134), "?", FONT_SERIF, 150, DARK)
        c.text((150, 226), "AGE", FONT_SANS, 40, DARK, track=8)
        return c.done()
    return cache("agebadge9", mk)

def vcard9_spr():
    def mk():
        c = Cv(860, 560)
        c.rrect((4, 4, 856, 556), 44, fill=CARD, outline=GOLD, width=7)
        c.rrect((30, 30, 830, 360), 28, fill=(22, 82, 64))
        for k in range(15):
            c.line([30 + k * 60, 30, 30 + k * 60 - 90, 360], (28, 96, 76), 6)
        plane_draw(c, 640, 110, 0.55, IVORY)
        c.ell((330, 140, 530, 340), fill=GOLD, outline=CRUST_D, width=6)
        c.poly([(398, 184), (398, 296), (488, 240)], fill=DARK)
        c.text((430, 420), "8 THINGS", FONT_SANS, 84, GOLD, track=6)
        c.text((430, 494), "THE EXACT WORDS", FONT_SANS, 40, SAGE, track=5)
        return c.done()
    return cache("vcard9", mk)

def pill9_spr():
    def mk():
        c = Cv(960, 100)
        c.rrect((3, 3, 957, 97), 46, fill=CARD, outline=SAGE_D, width=4)
        tr = 4
        t1, t2 = "SUBSCRIBE", "THE SENIOR ADVANTAGE"
        d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
        f = font(FONT_SANS, 28)
        w1 = sum(d0.textlength(ch, font=f) + tr for ch in t1) - tr
        w2 = sum(d0.textlength(ch, font=f) + tr for ch in t2) - tr
        gap = 56
        x0 = 480 - (w1 + gap + w2) / 2
        c.text((x0, 50), t1, FONT_SANS, 28, GOLD, anchor="lm", track=tr)
        dx = x0 + w1 + gap / 2
        c.poly([(dx - 11, 50), (dx, 39), (dx + 11, 50), (dx, 61)], fill=SAGE)
        c.text((x0 + w1 + gap, 50), t2, FONT_SANS, 28, IVORY, anchor="lm", track=tr)
        return c.done()
    return cache("pill9", mk)

# ---------------------------------------------------------------- B1 (256 f = 8,5 s)
def c1(img, t):
    ambient9(img, t)
    hdr(img, t, "AT EVERY AIRPORT", 300, GOLD, 1)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, arch_spr(), 250, 810, scale=0.95 * s, alpha=al, shadow=12)
        put(img, belt_spr(), 745, 880, scale=0.85 * s, alpha=al, shadow=12)
        burst(img, t, 0.2, 540, 820, n=10, color=SAGE, dur=0.6, rad=380, seed=91)
    for i in range(5):
        s, al, a = pop(t, 1.4 + i * 0.16, 0.35)
        if a > 0:
            put(img, person_spr("off"), 170 + i * 185, 1150, scale=2.0 * s, alpha=al, shadow=8)
    s, al, a = pop(t, 3.2, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 1420, scale=1.2, alpha=0.3 * al)
        put(img, tspr("?", FONT_SANS, 300, GOLD), 540, 1410, scale=s, alpha=al, shadow=14, rot=-5 + 3 * math.sin(t * 4))
        burst(img, t, 3.2, 540, 1410, n=12, color=GOLD, dur=0.7, rad=320, seed=92)
    pop_text(img, t, 4.2, "ONE QUESTION", 1590, 84, IVORY, 8)
    pop_text(img, t, 5.8, "MOST PEOPLE OVER 60", 1680, 56, SAGE, 6, track=1)
    pop_text(img, t, 6.6, "NEVER ASK IT", 1780, 92, CORAL, 10)

# ---------------------------------------------------------------- B2 (197 f = 6,6 s)
def c2(img, t):
    ambient9(img, t, seed=11)
    hdr(img, t, "ABOUT YOUR SHOES", 300, SAGE, 2)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 700, scale=1.3, alpha=0.3 * al)
        put(img, shoes_spr(), 540, 700, scale=1.1 * s, alpha=al, shadow=14, rot=-3)
        burst(img, t, 0.2, 540, 700, n=12, color=GOLD, dur=0.7, rad=380, seed=93)
    s, al, a = pop(t, 1.1, 0.45)
    if a > 0:
        put(img, tag_spr("YOUR SHOES", 600, 120, GOLD, 64), 540, 940, scale=s, alpha=al, rot=-2, shadow=12)
    pop_text(img, t, 2.0, "ONLY SOME TRAVELERS", 1090, 62, IVORY, 8)
    for i in range(5):
        s, al, a = pop(t, 2.3 + i * 0.1, 0.35)
        if a > 0:
            put(img, person_spr("on" if i in (1, 3) else "off"), 200 + i * 170, 1220, scale=1.8 * s, alpha=al, shadow=8)
    s, al, a = pop(t, 3.1, 0.4)
    if a > 0:
        for i in (1, 3):
            put(img, check_spr(), 200 + i * 170, 1360, scale=0.45 * s, alpha=al)
    s, al, a = pop(t, 3.9, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1520, scale=1.0, alpha=0.3 * al)
        put(img, agebadge9_spr(), 540, 1530, scale=0.8 * s, alpha=al, shadow=12, rot=-6 * (1 - ease(a)))
        burst(img, t, 3.9, 540, 1510, n=12, color=GOLD, dur=0.7, rad=300, seed=94)
    pop_text(img, t, 4.5, "THE AGE THAT DECIDES IT", 1690, 50, IVORY, 6, track=1)
    pop_text(img, t, 5.1, "MIGHT SURPRISE YOU", 1780, 68, GOLD, 8)

# ---------------------------------------------------------------- B3 (206 f = 6,9 s)
def c3(img, t):
    ambient9(img, t, seed=13)
    hdr(img, t, "ONE OF EIGHT", 300, GOLD, 3)
    for n in range(8):
        r, q = divmod(n, 4)
        s, al, a = pop(t, 0.2 + n * 0.1, 0.35)
        if a > 0:
            kind = "on" if (n == 0 and t > 1.4) else "off"
            put(img, tile7(n + 1, kind), 218 + q * 215, 650 + r * 230, scale=1.5 * s, alpha=al, shadow=8)
    s, al, a = pop(t, 1.4, 0.4)
    if a > 0:
        burst(img, t, 1.4, 218, 650, n=10, color=GOLD, dur=0.6, rad=200, seed=95)
    pop_text(img, t, 1.5, "ONE OF 8 THINGS", 1190, 78, IVORY, 8)
    pop_text(img, t, 2.7, "TRAVELERS OVER 60", 1310, 66, SAGE, 8, track=1)
    pop_text(img, t, 3.7, "CAN ASK FOR AT THE AIRPORT", 1410, 46, IVORY, 6, track=1)
    s, al, a = pop(t, 5.2, 0.5)
    if a > 0:
        put(img, stamp_spr("ALMOST NOBODY ASKS", 860, 140, CORAL), 540, 1620, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 5.2, 540, 1620, n=12, color=CORAL, dur=0.7, rad=380, seed=96)

# ---------------------------------------------------------------- B4 (259 f = 8,6 s)
def c4(img, t):
    ambient9(img, t, seed=15)
    hdr(img, t, "CANCELLED FLIGHT", 300, CORAL, 4)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, flight_card_spr(), 540, 610, scale=0.85 * s, alpha=al, shadow=12)
    s, al, a = pop(t, 1.1, 0.45)
    if a > 0:
        put(img, stamp_spr("CANCELLED", 600, 120, CORAL), 540, 650, scale=s, alpha=al, rot=-8, shadow=14)
        burst(img, t, 1.1, 540, 650, n=12, color=CORAL, dur=0.7, rad=320, seed=97)
    s, al, a = pop(t, 2.2, 0.45)
    if a > 0:
        put(img, wallet_spr(), 540, 900, scale=0.8 * s, alpha=al, shadow=12)
    for k in range(4):
        u = seg(t, 2.6 + k * 0.22, 0.6)
        if u > 0:
            put(img, bill9_spr(), 540 + (k - 1.5) * 50, 760 + 130 * ease(u), scale=0.6 * (1 - 0.25 * ease(u)), alpha=1 - seg(t, 3.6 + k * 0.05, 0.3), rot=(k - 1.5) * 8)
    pop_text(img, t, 3.3, "REAL MONEY BACK", 1085, 74, GOLD, 8)
    s, al, a = pop(t, 4.7, 0.5)
    if a > 0:
        put(img, person_spr("off"), 800, 1330, scale=1.5 * s, alpha=al)
        put(img, counter9_spr(), 600, 1380, scale=0.66 * s, alpha=al, shadow=12)
        put(img, person_spr("on"), 230, 1430, scale=1.9 * s, alpha=al, shadow=8)
    s, al, a = pop(t, 5.3, 0.4)
    if a > 0:
        put(img, bubble_spr(250, 110, lines=["YES"], size=62), 280, 1250, scale=s, alpha=al, shadow=8)
    pop_text(img, t, 5.0, "MOST PEOPLE SAY YES", 1655, 60, IVORY, 8)
    pop_text(img, t, 6.6, "TO THE WRONG THING", 1755, 68, CORAL, 8)

# ---------------------------------------------------------------- B5 (216 f = 7,2 s)
def c5(img, t):
    ambient9(img, t, seed=17)
    hdr(img, t, "ANOTHER ONE", 300, SAGE, 5)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, glow_spr(), 270, 800, scale=1.0, alpha=0.3 * al)
        put(img, phone9_spr(), 270, 800, scale=0.95 * s, alpha=al, shadow=14, rot=-4)
        burst(img, t, 0.2, 270, 800, n=10, color=GOLD, dur=0.6, rad=260, seed=98)
    s, al, a = pop(t, 1.7, 0.5)
    if a > 0:
        put(img, calendar_spr(), 730, 800, scale=0.7 * s, alpha=al, shadow=12, rot=3)
    pop_text(img, t, 2.7, "DAYS BEFORE YOU FLY", 1170, 62, IVORY, 8)
    s, al, a = pop(t, 4.0, 0.45)
    if a > 0:
        put(img, tag_spr("AIRPORT", 520, 120, SAGE, 66), 540, 1340, scale=s, alpha=al, rot=-2, shadow=12)
    pop_text(img, t, 4.2, "WAIT UNTIL THE AIRPORT", 1470, 52, IVORY, 6, track=1)
    s, al, a = pop(t, 5.3, 0.5)
    if a > 0:
        put(img, stamp_spr("TOO LATE", 700, 150, CORAL), 540, 1640, scale=s, alpha=al, rot=-4, shadow=14)
        burst(img, t, 5.3, 540, 1640, n=12, color=CORAL, dur=0.7, rad=340, seed=99)

# ---------------------------------------------------------------- B6 (210 f = 7,0 s)
def c6(img, t):
    ambient9(img, t, seed=19)
    hdr(img, t, "THE FULL VIDEO", 300, GOLD, 6)
    s, al, a = pop(t, 0.2, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 760, scale=1.5, alpha=0.3 * al)
        put(img, vcard9_spr(), 540, 760, scale=1.0 * s * (1 + 0.012 * math.sin(t * 6)), alpha=al, shadow=18, rot=-2 * (1 - ease(a)))
        burst(img, t, 0.3, 540, 760, n=12, color=GOLD, dur=0.7, rad=460, seed=100)
    pop_text(img, t, 1.4, "ALL EIGHT, ONE VIDEO", 1150, 72, IVORY, 8)
    pop_text(img, t, 2.8, "THE EXACT WORDS TO SAY", 1255, 54, SAGE, 6, track=1)
    pop_text(img, t, 3.9, "RIGHT BELOW", 1375, 100, GOLD, 12)
    pop_text(img, t, 5.2, "TAP IT NOW", 1495, 84, IVORY, 10)
    for k in range(3):
        a = seg(t, 4.0 + k * 0.1, 0.3)
        if a > 0:
            ph = (t * 2.2 - k * 0.22) % 1.0
            put(img, chevron_spr(), 540, 1615 + k * 46 + 18 * math.sin(ph * 6.28), alpha=ease(a) * (0.5 + 0.5 * math.sin(ph * 6.28) ** 2), scale=0.7)

# ---------------------------------------------------------------- B7 (202 f = 6,7 s)
def c7(img, t):
    ambient9(img, t, seed=21)
    hdr(img, t, "THE SENIOR ADVANTAGE", 300, SAGE, 7)
    pop_text(img, t, 0.1, "BEFORE YOU GO", 560, 96, IVORY, 10)
    s, al, a = pop(t, 1.0, 0.5)
    if a > 0:
        put(img, glow_spr(), 270, 900, scale=1.1, alpha=0.3 * al)
        put(img, thumb_spr(), 270, 900, scale=1.15 * s, alpha=al, shadow=14, rot=-8 + 3 * math.sin(t * 5))
        burst(img, t, 1.0, 270, 900, n=10, color=GOLD, dur=0.6, rad=200, seed=114)
    s, al, a = pop(t, 1.3, 0.45)
    if a > 0:
        put(img, tag_spr("LIKE", 340, 130, GOLD, 80), 270, 1190, scale=s, alpha=al, rot=-3, shadow=12)
    s, al, a = pop(t, 2.8, 0.5)
    if a > 0:
        sw = 10 * math.sin((t - 3.1) * 18) * max(0.0, 1 - (t - 3.1) / 1.2) if t > 3.1 else 0
        put(img, glow_spr(), 780, 900, scale=1.1, alpha=0.3 * al)
        put(img, bell_spr(), 780, 900, scale=1.5 * s, alpha=al, rot=sw, shadow=14)
        burst(img, t, 2.8, 780, 900, n=10, color=GOLD, dur=0.6, rad=180, seed=115)
    s, al, a = pop(t, 3.1, 0.45)
    if a > 0:
        put(img, tag_spr("SUBSCRIBE", 470, 130, GOLD, 60), 770, 1190, scale=s, alpha=al, rot=3, shadow=12)
    pop_text(img, t, 4.1, "SO YOU DON'T MISS", 1410, 84, IVORY, 8)
    pop_text(img, t, 4.7, "THE NEXT ONE", 1540, 110, GOLD, 10)
    a = seg(t, 5.3, 0.4)
    if a > 0:
        put(img, pill9_spr(), 540, 1700 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)

SCENES9 = {1: (c1, 256), 2: (c2, 197), 3: (c3, 206), 4: (c4, 259), 5: (c5, 216), 6: (c6, 210), 7: (c7, 202)}
DRAW = {k: v[0] for k, v in SCENES9.items()}
DUR = {k: v[1] for k, v in SCENES9.items()}

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES9)
    out_dir = os.environ.get("S9_OUT", "short9")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        fn, nf = SCENES9[k]
        render_seq(zoomed(fn), nf, f"{out_dir}/short9-blocco{k:02d}.mp4")
