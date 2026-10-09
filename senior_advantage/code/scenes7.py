import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes6 import *

# =====================================================================
# SHORT 7: Costco (correlato al video lungo Costco). Stesso motore degli short 5/6.
# Slide pulite: poche parole grandi, un'idea per blocco, tutto finito prima della frase dopo.
# uso: S7_OUT=cartella python3 scenes7.py <clip>
# =====================================================================
RED_D = (176, 70, 62)

# ------------------------------------------------------------------ sprite
def mcard_spr():
    """tessera generica (nessun logo reale)"""
    def mk():
        c = Cv(600, 380)
        c.rrect((4, 4, 596, 376), 36, fill=(16, 78, 62), outline=GOLD, width=6)
        c.rrect((4, 70, 596, 130), 2, fill=GOLD)
        c.text((46, 40), "MEMBERSHIP", FONT_SANS, 34, IVORY, anchor="lm", track=6)
        c.rrect((46, 168, 150, 236), 12, fill=(232, 200, 130), outline=(190, 140, 60), width=3)
        for y in (186, 202, 218):
            c.line([62, y, 134, y], (190, 140, 60), 3)
        c.text((46, 300), "CARD", FONT_SANS, 64, IVORY, anchor="lm", track=8)
        c.text((554, 330), "$65 A YEAR", FONT_SANS, 28, SAGE, anchor="rm", track=3)
        return c.done()
    return cache("mcard7", mk)

def counter_spr():
    """banco della farmacia"""
    def mk():
        c = Cv(720, 520)
        c.rrect((20, 150, 700, 480), 20, fill=(22, 82, 64), outline=SAGE_D, width=5)
        # tenda a strisce
        for k in range(8):
            col = IVORY if k % 2 == 0 else CORAL
            c.poly([(30 + k * 82, 60), (112 + k * 82, 60), (122 + k * 82, 150), (20 + k * 82, 150)], fill=col)
        c.rrect((30, 24, 690, 70), 14, fill=DARK, outline=GOLD, width=4)
        c.text((360, 48), "PHARMACY", FONT_SANS, 34, GOLD, track=14)
        # scaffale con flaconi
        c.rrect((60, 190, 660, 214), 6, fill=(60, 120, 100))
        for k, col in enumerate(((226, 150, 70), (236, 190, 90), (226, 150, 70), (214, 108, 96), (226, 150, 70), (236, 190, 90), (226, 150, 70))):
            x = 84 + k * 80
            c.rrect((x, 134 + 14, x + 52, 190), 8, fill=col)
            c.rrect((x + 4, 128 + 14, x + 48, 146 + 14), 5, fill=IVORY)
        # bancone
        c.rrect((40, 330, 680, 392), 14, fill=(236, 190, 120), outline=(190, 140, 60), width=4)
        # croce medica
        c.ell((300, 236, 420, 316), fill=IVORY)
        c.rrect((350, 244, 370, 308), 4, fill=CORAL)
        c.rrect((328, 266, 392, 286), 4, fill=CORAL)
        return c.done()
    return cache("counter7", mk)

def rx_spr():
    def mk():
        c = Cv(300, 380)
        c.rrect((6, 6, 294, 374), 20, fill=IVORY, outline=(214, 208, 194), width=4)
        c.text((60, 66), "Rx", FONT_SERIF, 76, CORAL, anchor="lm")
        for y in (150, 190, 230, 270):
            c.rrect((40, y, 260, y + 14), 6, fill=(206, 202, 190))
        c.ell((200, 296, 270, 366), fill=GOLD, outline=(190, 140, 60), width=4)
        c.line([218, 332, 232, 346, 256, 316], DARK, 8)
        return c.done()
    return cache("rx7", mk)

def pricetag_spr(word, col, strike=False):
    def mk():
        c = Cv(440, 220)
        c.poly([(8, 110), (96, 6), (432, 6), (432, 214), (96, 214)], fill=CARD)
        c.line([8, 110, 96, 6, 432, 6, 432, 214, 96, 214, 8, 110], col, 7)
        c.ell((70, 94, 102, 126), fill=DARK, outline=col, width=5)
        c.text((270, 70), word, FONT_SANS, 40, IVORY, track=3)
        c.text((270, 152), "$ $ $" if strike else "$", FONT_SANS, 70, col, track=10)
        if strike:
            c.line([150, 160, 392, 142], CORAL, 11)
        return c.done()
    return cache(("ptag7", word, strike), mk)

def ear_spr():
    def mk():
        c = Cv(360, 440)
        c.ell((40, 30, 320, 410), fill=(236, 194, 154), outline=(196, 150, 110), width=6)
        c.ell((100, 90, 262, 330), outline=(196, 150, 110), width=8)
        c.ell((140, 150, 226, 262), outline=(196, 150, 110), width=7)
        c.ell((150, 300, 230, 396), fill=(236, 194, 154), outline=(196, 150, 110), width=6)
        return c.done()
    return cache("ear7", mk)

def waves7(img, t, cx, cy, col=GOLD):
    for k in range(3):
        ph = (t * 1.4 - k * 0.33) % 1.0
        r = 120 + 190 * ph
        a = (1 - ph) * 0.9
        w = max(8, int(r * 1.3))
        sp = Image.new("RGBA", (w + 20, w + 20), (0, 0, 0, 0))
        d = ImageDraw.Draw(sp)
        d.arc([10, 10, w + 10, w + 10], -50, 50, fill=col + (int(255 * a),), width=12)
        put(img, sp, cx, cy)

def tile7(n, kind):
    """kind: on (oro), off (spenta), warn (corallo)"""
    def mk():
        c = Cv(130, 130)
        if kind == "on":
            c.rrect((4, 4, 126, 126), 26, fill=GOLD, outline=(190, 140, 60), width=5)
            col = DARK
        elif kind == "warn":
            c.rrect((4, 4, 126, 126), 26, fill=CORAL, outline=RED_D, width=5)
            col = IVORY
        else:
            c.rrect((4, 4, 126, 126), 26, fill=(14, 58, 45), outline=SAGE_D, width=4)
            col = SAGE_D
        c.text((65, 68), str(n), FONT_SERIF, 66, col)
        return c.done()
    return cache(("tile7", n, kind), mk)

def sign_spr():
    def mk():
        c = Cv(560, 330)
        c.rrect((16, 16, 544, 250), 20, fill=IVORY, outline=(206, 200, 186), width=6)
        c.rrect((262, 246, 298, 322), 6, fill=(150, 110, 70))
        c.text((280, 76), "SENIOR", FONT_SANS, 54, DARK, track=6)
        c.text((280, 138), "PERKS", FONT_SANS, 54, DARK, track=6)
        for y in (190, 216):
            c.rrect((90, y, 470, y + 12), 5, fill=(206, 202, 190))
        return c.done()
    return cache("sign7", mk)

def wallet_spr():
    def mk():
        c = Cv(360, 260)
        c.rrect((10, 40, 350, 250), 34, fill=(150, 104, 62), outline=(110, 74, 44), width=6)
        c.rrect((10, 40, 350, 112), 30, fill=(176, 126, 80), outline=(110, 74, 44), width=6)
        c.rrect((246, 130, 350, 190), 28, fill=(110, 74, 44))
        c.ell((284, 146, 316, 176), fill=GOLD)
        return c.done()
    return cache("wallet7", mk)

def thumb_spr():
    def mk():
        c = Cv(300, 320)
        c.rrect((8, 130, 90, 308), 16, fill=GOLD, outline=(190, 140, 60), width=6)
        c.poly([(104, 142), (176, 20), (214, 26), (196, 122), (284, 122), (294, 150), (278, 290), (250, 308), (104, 308)], fill=GOLD)
        c.line([104, 142, 176, 20, 214, 26, 196, 122, 284, 122, 294, 150, 278, 290, 250, 308, 104, 308, 104, 142], (190, 140, 60), 6)
        for y in (178, 220, 262):
            c.line([128, y, 252, y], (190, 140, 60), 4)
        return c.done()
    return cache("thumb7", mk)

def video_card_spr():
    def mk():
        c = Cv(860, 560)
        c.rrect((4, 4, 856, 556), 44, fill=CARD, outline=GOLD, width=7)
        c.rrect((30, 30, 830, 360), 28, fill=(22, 82, 64))
        for k in range(15):
            c.line([30 + k * 60, 30, 30 + k * 60 - 90, 360], (28, 96, 76), 6)
        c.text((430, 100), "COSTCO FOR SENIORS", FONT_SANS, 46, IVORY, track=5)
        c.ell((330, 140, 530, 340), fill=GOLD, outline=(190, 140, 60), width=6)
        c.poly([(398, 184), (398, 296), (488, 240)], fill=DARK)
        c.text((430, 420), "14 THINGS", FONT_SANS, 76, GOLD, track=6)
        c.text((430, 494), "THE EXACT STEPS", FONT_SANS, 38, SAGE, track=5)
        return c.done()
    return cache("vcard7", mk)

def pop_text(img, t, t0, s, y, size, col, shadow=8, track=0):
    a = seg(t, t0, 0.4)
    if a > 0:
        put(img, tspr(s, FONT_SANS, size, col, track=track), 540, y + 22 * (1 - ease(a)), alpha=ease(a), shadow=shadow)

# ---------------------------------------------------------------- clip 1 (305 f = 10,2 s): gancio
def c1(img, t):
    ambient_food(img, t, n=6, seed=81)
    label(img, t, "COSTCO AND SENIORS", 300, GOLD)
    # tessera + NO SENIOR DISCOUNT
    s, al, a = pop(t, 0.15, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 640, scale=1.2, alpha=0.25 * al)
        put(img, mcard_spr(), 540, 640, scale=0.9 * s, alpha=al, shadow=14, rot=-3 + 2 * math.sin(t * 2.5))
    s, al, a = pop(t, 1.2, 0.45)
    if a > 0:
        put(img, stamp_spr("NO SENIOR DISCOUNT", 820, 130, CORAL), 540, 640, scale=s, alpha=al, rot=-6, shadow=14)
        burst(img, t, 1.2, 540, 640, n=12, color=CORAL, dur=0.7, rad=360, seed=82)
    pop_text(img, t, 2.5, "NOT ONE.", 900, 120, IVORY, 10)
    # banco farmacia
    s, al, a = pop(t, 3.7, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1230, scale=1.2, alpha=0.3 * al)
        put(img, counter_spr(), 540, 1230, scale=0.9 * s, alpha=al, shadow=14)
        burst(img, t, 3.7, 540, 1230, n=12, color=GOLD, dur=0.7, rad=380, seed=83)
    s, al, a = pop(t, 5.9, 0.45)
    if a > 0:
        put(img, tag_spr("NO CARD NEEDED", 760, 120, GOLD, 58), 540, 1555, scale=s, alpha=al, rot=-2, shadow=12)
    for i in range(7):
        s, al, a = pop(t, 8.3 + i * 0.07, 0.35)
        if a > 0:
            put(img, person_spr("off"), 130 + i * 137, 1680 + 4 * math.sin(t * 3 + i), scale=0.8 * s, alpha=al * 0.9)
    pop_text(img, t, 8.9, "ALMOST NOBODY OVER 60 USES IT", 1790, 44, CORAL, 6, track=1)

# ---------------------------------------------------------------- clip 2 (167 f = 5,6 s): la farmacia
def c2(img, t):
    ambient_food(img, t, n=6, seed=83)
    label(img, t, "THE PHARMACY", 300, SAGE)
    s, al, a = pop(t, 0.1, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 760, scale=1.3, alpha=0.3 * al)
        put(img, counter_spr(), 540, 760, scale=1.2 * s, alpha=al, shadow=16)
        burst(img, t, 0.1, 540, 760, n=12, color=GOLD, dur=0.7, rad=420, seed=84)
    s, al, a = pop(t, 1.7, 0.5)
    if a > 0:
        put(img, mcard_spr(), 330, 1290, scale=0.5 * s, alpha=al, shadow=10, rot=-6)
        put(img, bigx_spr(), 330, 1290, scale=0.55 * s, alpha=al)
    s, al, a = pop(t, 2.2, 0.5)
    if a > 0:
        put(img, rx_spr(), 760, 1290, scale=0.62 * s, alpha=al, shadow=10, rot=5)
    s, al, a = pop(t, 2.9, 0.45)
    if a > 0:
        put(img, stamp_spr("NO MEMBERSHIP NEEDED", 880, 130, GOLD), 540, 1580, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 2.9, 540, 1580, n=12, color=GOLD, dur=0.7, rad=250, seed=85)
    pop_text(img, t, 4.1, "FILL YOUR PRESCRIPTIONS", 1760, 50, IVORY, 6, track=1)

# ---------------------------------------------------------------- clip 3 (298 f = 9,9 s): programma farmaci
def c3(img, t):
    ambient_food(img, t, n=6, seed=85)
    label(img, t, "IF YOU ARE A MEMBER", 300, GOLD)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, mcard_spr(), 330, 640, scale=0.6 * s, alpha=al, shadow=12, rot=-5)
        put(img, check_spr(), 560, 740, scale=0.5 * ease_back(seg(t, 0.8, 0.4)), alpha=al)
    s, al, a = pop(t, 0.5, 0.5)
    if a > 0:
        put(img, pill_bottle_spr(), 800, 650, scale=0.78 * s, alpha=al, shadow=12, rot=6)
    # prezzo normale -> prezzo membro
    s, al, a = pop(t, 2.2, 0.5)
    if a > 0:
        put(img, pricetag_spr("REGULAR", CORAL, True), 300, 1020, scale=0.85 * s, alpha=al, shadow=10, rot=-3)
    a = seg(t, 3.2, 0.5)
    if a > 0:
        put(img, arrow_down7(), 540, 1020, scale=0.55, alpha=ease(a))
    s, al, a = pop(t, 3.7, 0.5)
    if a > 0:
        put(img, pricetag_spr("MEMBER", GOLD, False), 780, 1020, scale=0.85 * s, alpha=al, shadow=10, rot=3)
        burst(img, t, 3.7, 780, 1020, n=10, color=GOLD, dur=0.6, rad=240, seed=86)
    a = seg(t, 4.6, 0.5)
    if a > 0:
        put(img, tspr("LOWER PRICE ON MANY DRUGS", FONT_SANS, 46, IVORY, track=1), 540, 1230 + 20 * (1 - ease(a)), alpha=ease(a), shadow=6)
    s, al, a = pop(t, 5.9, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1440, scale=1.3, alpha=0.3 * al)
        put(img, tag_spr("MEMBER PRESCRIPTION", 860, 120, GOLD, 54), 540, 1410, scale=s, alpha=al, rot=-2, shadow=12)
        put(img, tag_spr("PROGRAM", 520, 120, GOLD, 64), 540, 1540, scale=s, alpha=al, rot=-2, shadow=12)
        burst(img, t, 5.9, 540, 1480, n=12, color=GOLD, dur=0.7, rad=420, seed=87)
    s, al, a = pop(t, 8.0, 0.45)
    if a > 0:
        put(img, stamp_spr("NOT INSURANCE", 700, 130, CORAL), 540, 1700, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 8.0, 540, 1700, n=12, color=CORAL, dur=0.7, rad=200, seed=88)

def arrow_down7():
    def mk():
        c = Cv(200, 240)
        c.rrect((70, 6, 130, 130), 8, fill=GOLD)
        c.poly([(16, 120), (184, 120), (100, 232)], fill=GOLD)
        return c.done()
    return cache("adown7", mk)

# ---------------------------------------------------------------- clip 4 (194 f = 6,5 s): 2 di 14
def c4(img, t):
    ambient_food(img, t, n=6, seed=87)
    label(img, t, "COSTCO FOR SENIORS", 300, GOLD)
    for i in range(14):
        r, q = i // 7, i % 7
        x, y = 150 + q * 130, 700 + r * 150
        s, al, a = pop(t, 0.2 + i * 0.07, 0.35)
        if a > 0:
            kind = "on" if (i < 2 and t > 1.6) else "off"
            put(img, tile7(i + 1, kind), x, y, scale=0.98 * s, alpha=al, shadow=6)
    s, al, a = pop(t, 1.6, 0.5)
    if a > 0:
        burst(img, t, 1.6, 280, 700, n=10, color=GOLD, dur=0.7, rad=220, seed=89)
        put(img, tag_spr("ONLY 2 OF 14", 760, 130, GOLD, 70), 540, 1060, scale=s, alpha=al, rot=-2, shadow=12)
    # cartello con X
    s, al, a = pop(t, 3.1, 0.5)
    if a > 0:
        put(img, sign_spr(), 540, 1400, scale=0.9 * s, alpha=al, shadow=14, rot=-2)
    s, al, a = pop(t, 3.7, 0.45)
    if a > 0:
        put(img, bigx_spr(), 540, 1380, scale=0.55 * s, alpha=al)
    pop_text(img, t, 4.4, "MOST ARE NOT ON ANY SIGN", 1690, 52, IVORY, 6, track=1)

# ---------------------------------------------------------------- clip 5 (136 f = 4,5 s): test dell'udito
def c5(img, t):
    ambient_food(img, t, n=6, seed=89)
    label(img, t, "HEARING TEST", 300, SAGE)
    s, al, a = pop(t, 0.1, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 800, scale=1.3, alpha=0.3 * al)
        put(img, ear_spr(), 540, 800, scale=1.15 * s, alpha=al, shadow=14)
        waves7(img, t, 760, 760)
    pop_text(img, t, 0.9, "A HEARING TEST", 1180, 84, GOLD, 10)
    s, al, a = pop(t, 2.2, 0.45)
    if a > 0:
        put(img, stamp_spr("NO NEED TO BUY", 780, 130, CORAL), 540, 1400, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 2.2, 540, 1400, n=12, color=CORAL, dur=0.7, rad=360, seed=90)
    s, al, a = pop(t, 3.0, 0.4)
    if a > 0:
        put(img, check_spr(), 540, 1640, scale=0.9 * s, alpha=al)

# ---------------------------------------------------------------- clip 6 (131 f = 4,4 s): quello che costa
def c6(img, t):
    ambient_food(img, t, n=6, seed=91)
    label(img, t, "ONE OF THE FOURTEEN", 300, CORAL)
    for i in range(14):
        r, q = i // 7, i % 7
        x, y = 150 + q * 130, 600 + r * 150
        s, al, a = pop(t, 0.1 + i * 0.04, 0.3)
        if a > 0:
            kind = "warn" if (i == 9 and t > 1.0) else "off"
            put(img, tile7("?" if kind == "warn" else i + 1, kind), x, y, scale=0.98 * s, alpha=al, shadow=6)
    s, al, a = pop(t, 1.0, 0.45)
    if a > 0:
        burst(img, t, 1.0, 150 + 2 * 130, 750, n=10, color=CORAL, dur=0.6, rad=200, seed=91)
    s, al, a = pop(t, 1.3, 0.5)
    if a > 0:
        put(img, wallet_spr(), 540, 1180, scale=0.95 * s, alpha=al, shadow=12)
    for k in range(5):
        u = seg(t, 1.7 + k * 0.2, 0.7)
        if u > 0:
            put(img, coin_spr(), 560 + k * 70 - 140 + 18 * math.sin(u * 6), 1130 - 170 * ease(u) * (1 if u < 1 else 1), scale=0.8, alpha=1 - seg(t, 2.6, 0.5))
    pop_text(img, t, 1.9, "CAN QUIETLY COST YOU MONEY", 1500, 50, CORAL, 8, track=1)
    pop_text(img, t, 2.8, "KNOW THE RULE", 1650, 100, GOLD, 10)

# ---------------------------------------------------------------- clip 7 (208 f = 6,9 s): vai al video
def c7(img, t):
    ambient_food(img, t, n=6, seed=93)
    label(img, t, "THE FULL VIDEO", 300, GOLD)
    s, al, a = pop(t, 0.2, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 820, scale=1.5, alpha=0.3 * al)
        put(img, video_card_spr(), 540, 820, scale=1.0 * s * (1 + 0.012 * math.sin(t * 6)), alpha=al, shadow=18, rot=-2 * (1 - ease(a)))
        burst(img, t, 0.3, 540, 820, n=12, color=GOLD, dur=0.7, rad=460, seed=94)
    pop_text(img, t, 2.5, "ALL 14, ONE VIDEO", 1230, 80, IVORY, 8)
    pop_text(img, t, 3.7, "WITH THE EXACT STEPS", 1340, 56, SAGE, 6, track=1)
    pop_text(img, t, 5.0, "RIGHT BELOW", 1440, 100, GOLD, 12)
    pop_text(img, t, 6.0, "TAP IT NOW", 1550, 80, IVORY, 10)
    for k in range(3):
        a = seg(t, 5.1 + k * 0.1, 0.3)
        if a > 0:
            ph = (t * 2.2 - k * 0.22) % 1.0
            put(img, chevron_spr(), 540, 1640 + k * 50 + 18 * math.sin(ph * 6.28), alpha=ease(a) * (0.5 + 0.5 * math.sin(ph * 6.28) ** 2), scale=0.7)

# ---------------------------------------------------------------- clip 8 (202 f = 6,7 s): like e iscriviti
def c8(img, t):
    ambient_food(img, t, n=6, seed=95)
    label(img, t, "THE SENIOR ADVANTAGE", 300, SAGE)
    pop_text(img, t, 0.1, "BEFORE YOU GO", 560, 96, IVORY, 10)
    s, al, a = pop(t, 1.3, 0.5)
    if a > 0:
        put(img, glow_spr(), 270, 900, scale=1.1, alpha=0.3 * al)
        put(img, thumb_spr(), 270, 900, scale=1.15 * s, alpha=al, shadow=14, rot=-8 + 3 * math.sin(t * 5))
        burst(img, t, 1.3, 270, 900, n=10, color=GOLD, dur=0.6, rad=200, seed=96)
    s, al, a = pop(t, 1.6, 0.45)
    if a > 0:
        put(img, tag_spr("LIKE", 340, 130, GOLD, 80), 270, 1190, scale=s, alpha=al, rot=-3, shadow=12)
    s, al, a = pop(t, 3.2, 0.5)
    if a > 0:
        sw = 10 * math.sin((t - 3.5) * 18) * max(0.0, 1 - (t - 3.5) / 1.2) if t > 3.5 else 0
        put(img, glow_spr(), 780, 900, scale=1.1, alpha=0.3 * al)
        put(img, bell_spr(), 780, 900, scale=1.5 * s, alpha=al, rot=sw, shadow=14)
        burst(img, t, 3.2, 780, 900, n=10, color=GOLD, dur=0.6, rad=180, seed=97)
    s, al, a = pop(t, 3.5, 0.45)
    if a > 0:
        put(img, tag_spr("SUBSCRIBE", 470, 130, GOLD, 60), 770, 1190, scale=s, alpha=al, rot=3, shadow=12)
    pop_text(img, t, 4.9, "SO YOU DON'T MISS", 1410, 84, IVORY, 8)
    pop_text(img, t, 5.5, "THE NEXT ONE", 1540, 110, GOLD, 10)
    a = seg(t, 5.9, 0.4)
    if a > 0:
        put(img, subpill_spr(), 540, 1700 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)

SCENES7 = {1: (c1, 305), 2: (c2, 167), 3: (c3, 298), 4: (c4, 194), 5: (c5, 136), 6: (c6, 131), 7: (c7, 208), 8: (c8, 202)}
DRAW = {k: v[0] for k, v in SCENES7.items()}
DUR = {k: v[1] for k, v in SCENES7.items()}

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES7)
    out_dir = os.environ.get("S7_OUT", "short7")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        fn, nf = SCENES7[k]
        render_seq(zoomed(fn), nf, f"{out_dir}/short7-clip{k:02d}.mp4")
