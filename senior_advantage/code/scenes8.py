import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes7 import *

# =====================================================================
# SHORT 8: Bollette (correlato al video lungo 4). Stesso motore dello short 7.
# Durate (fotogrammi): 315 293 267 179 155 247 202. Ultimo elemento di ogni blocco entro l'80%.
# uso: S8_OUT=cartella python3 scenes8.py <clip>
# =====================================================================

def bill_spr(word, col=CORAL, amount="$$$"):
    def mk():
        c = Cv(360, 440)
        c.rrect((6, 6, 354, 434), 22, fill=IVORY, outline=(214, 208, 194), width=5)
        c.rrect((6, 6, 354, 96), 22, fill=col)
        c.rrect((6, 60, 354, 96), 2, fill=col)
        c.text((180, 52), word, FONT_SANS, 40, IVORY, track=4)
        for y in (150, 196, 242):
            c.rrect((40, y, 320, y + 16), 7, fill=(206, 202, 190))
        c.text((180, 340), amount, FONT_SANS, 84, DARK, track=6)
        c.text((180, 402), "DUE", FONT_SANS, 26, col, track=6)
        return c.done()
    return cache(("bill8", word, col, amount), mk)

def phone_spr():
    def mk():
        c = Cv(260, 440)
        c.rrect((6, 6, 254, 434), 38, fill=(20, 24, 24), outline=GOLD, width=7)
        c.rrect((26, 56, 234, 372), 12, fill=(22, 82, 64))
        c.text((130, 150), "PHONE", FONT_SANS, 40, IVORY, track=4)
        c.text((130, 230), "BILL", FONT_SANS, 62, GOLD, track=4)
        c.ell((100, 384, 160, 420), fill=(60, 66, 66))
        c.rrect((90, 26, 170, 38), 6, fill=(60, 66, 66))
        return c.done()
    return cache("phone8", mk)

def bus_spr():
    def mk():
        c = Cv(640, 380)
        c.rrect((10, 40, 630, 300), 46, fill=GOLD, outline=(190, 140, 60), width=7)
        for k in range(4):
            c.rrect((46 + k * 140, 76, 164 + k * 140, 170), 14, fill=(206, 232, 226), outline=DARK, width=4)
        c.rrect((10, 210, 630, 232), 2, fill=(190, 140, 60))
        c.rrect((26, 252, 150, 276), 8, fill=DARK)
        c.text((420, 191), "CITY BUS", FONT_SANS, 30, DARK, track=5)
        for x in (150, 470):
            c.ell((x - 56, 262, x + 56, 374), fill=(30, 30, 30), outline=IVORY, width=6)
            c.ell((x - 20, 298, x + 20, 338), fill=SAGE_D)
        return c.done()
    return cache("bus8", mk)

def house_spr():
    def mk():
        c = Cv(640, 560)
        c.poly([(320, 20), (620, 250), (20, 250)], fill=CORAL)
        c.line([320, 20, 620, 250, 20, 250, 320, 20], RED_D, 8)
        c.rrect((70, 240, 570, 540), 12, fill=IVORY, outline=(206, 200, 186), width=6)
        c.rrect((270, 340, 370, 540), 10, fill=(150, 110, 70), outline=(110, 74, 44), width=5)
        c.ell((345, 440, 360, 455), fill=GOLD)
        for x in (110, 410):
            c.rrect((x, 300, x + 100, 400), 8, fill=(206, 232, 226), outline=DARK, width=5)
            c.line([x + 50, 300, x + 50, 400], DARK, 4)
        c.rrect((470, 60, 530, 170), 6, fill=(150, 110, 70))
        return c.done()
    return cache("house8", mk)

def wrench_spr():
    def mk():
        c = Cv(300, 300)
        c.line([70, 230, 190, 110], SAGE, 36)
        c.ell((140, 40, 250, 150), fill=SAGE)
        c.ell((172, 64, 232, 112), fill=DARK)
        c.rrect((60, 90, 150, 270), 2, fill=None)
        c.ell((40, 200, 100, 260), fill=SAGE)
        return c.done()
    return cache("wrench8", mk)

def rule8_spr():
    def mk():
        c = Cv(560, 400)
        c.rrect((8, 8, 552, 392), 30, fill=IVORY, outline=(206, 200, 186), width=6)
        c.text((280, 76), "THE RULE", FONT_SANS, 60, DARK, track=6)
        c.text((280, 260), "?", FONT_SANS, 240, (214, 160, 70))
        return c.done()
    return cache("rule8", mk)

def vcard8_spr():
    def mk():
        c = Cv(860, 560)
        c.rrect((4, 4, 856, 556), 44, fill=CARD, outline=GOLD, width=7)
        c.rrect((30, 30, 830, 360), 28, fill=(22, 82, 64))
        for k in range(15):
            c.line([30 + k * 60, 30, 30 + k * 60 - 90, 360], (28, 96, 76), 6)
        c.text((430, 100), "BILLS BEFORE WINTER", FONT_SANS, 46, IVORY, track=4)
        c.ell((330, 140, 530, 340), fill=GOLD, outline=(190, 140, 60), width=6)
        c.poly([(398, 184), (398, 296), (488, 240)], fill=DARK)
        c.text((430, 420), "7 BILLS", FONT_SANS, 84, GOLD, track=6)
        c.text((430, 494), "THE RIGHT ORDER", FONT_SANS, 40, SAGE, track=5)
        return c.done()
    return cache("vcard8", mk)

# ---------------------------------------------------------------- B1 (315 f = 10,5 s)
def c1(img, t):
    ambient_food(img, t, n=6, seed=101)
    label(img, t, "BILLS YOU MAY PAY IN FULL", 300, GOLD)
    kinds = (("HEAT", CORAL), ("POWER", GOLD), ("PHONE", SAGE), ("FOOD", CORAL), ("BOX", GOLD), ("BUS", SAGE), ("REPAIR", CORAL))
    for i, (w, col) in enumerate(kinds):
        s, al, a = pop(t, 0.2 + i * 0.22, 0.4)
        if a > 0:
            r, q = (0, i) if i < 4 else (1, i - 4)
            x = 180 + q * 240 if r == 0 else 300 + q * 240
            y = 640 + r * 340
            put(img, bill_spr(w, col), x, y, scale=0.56 * s, alpha=al, shadow=10, rot=-4 + 8 * ((i * 37) % 5) / 4)
    s, al, a = pop(t, 2.3, 0.5)
    if a > 0:
        put(img, tag_spr("7 BILLS", 560, 140, GOLD, 84), 540, 1260, scale=s, alpha=al, rot=-2, shadow=12)
        burst(img, t, 2.3, 540, 1260, n=12, color=GOLD, dur=0.7, rad=360, seed=102)
    s, al, a = pop(t, 4.4, 0.45)
    if a > 0:
        put(img, stamp_spr("A PROGRAM FOR EACH", 860, 130, SAGE), 540, 1440, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 4.4, 540, 1440, n=12, color=SAGE, dur=0.7, rad=360, seed=103)
    for i in range(7):
        s, al, a = pop(t, 6.3 + i * 0.1, 0.35)
        if a > 0:
            put(img, person_spr("off"), 130 + i * 137, 1640 + 4 * math.sin(t * 3 + i), scale=0.8 * s, alpha=al * 0.9)
    pop_text(img, t, 8.2, "NOBODY OVER 60 MAKES THE CALL", 1790, 46, CORAL, 6, track=1)

# ---------------------------------------------------------------- B2 (293 f = 9,8 s)
def c2(img, t):
    ambient_food(img, t, n=6, seed=103)
    label(img, t, "TWO OF THE SEVEN", 300, SAGE)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, glow_spr(), 300, 760, scale=1.0, alpha=0.3 * al)
        put(img, phone_spr(), 300, 760, scale=1.0 * s, alpha=al, shadow=14, rot=-4)
        burst(img, t, 0.2, 300, 760, n=10, color=GOLD, dur=0.6, rad=260, seed=104)
    s, al, a = pop(t, 1.4, 0.45)
    if a > 0:
        put(img, tag_spr("PHONE", 420, 120, GOLD, 64), 300, 1090, scale=s, alpha=al, rot=-2, shadow=12)
    s, al, a = pop(t, 2.9, 0.5)
    if a > 0:
        put(img, glow_spr(), 780, 760, scale=1.0, alpha=0.3 * al)
        put(img, bus_spr(), 780, 760, scale=0.62 * s, alpha=al, shadow=14, rot=3)
        burst(img, t, 2.9, 780, 760, n=10, color=GOLD, dur=0.6, rad=240, seed=105)
    s, al, a = pop(t, 3.9, 0.45)
    if a > 0:
        put(img, tag_spr("HALF PRICE", 460, 120, GOLD, 56), 780, 960, scale=s, alpha=al, rot=2, shadow=12)
    s, al, a = pop(t, 5.4, 0.5)
    if a > 0:
        put(img, stamp_spr("BUT THERE'S A CATCH", 860, 130, CORAL), 540, 1360, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 5.4, 540, 1360, n=12, color=CORAL, dur=0.7, rad=360, seed=106)
    a = seg(t, 6.5, 0.4)
    if a > 0:
        put(img, tspr("?", FONT_SANS, 260, GOLD), 540, 1640 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10, rot=-6 + 4 * math.sin(t * 4))
    pop_text(img, t, 7.8, "MOST PEOPLE MISS IT", 1790, 56, IVORY, 6, track=1)

# ---------------------------------------------------------------- B3 (267 f = 8,9 s)
def c3(img, t):
    ambient_food(img, t, n=6, seed=105)
    label(img, t, "THE BIGGEST ONE", 300, CORAL)
    s, al, a = pop(t, 0.2, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 760, scale=1.3, alpha=0.3 * al)
        put(img, house_spr(), 540, 760, scale=1.05 * s, alpha=al, shadow=16)
        burst(img, t, 0.2, 540, 760, n=12, color=GOLD, dur=0.7, rad=420, seed=107)
    pop_text(img, t, 2.4, "NOT A MONTHLY BILL", 1130, 66, IVORY, 8, track=1)
    pop_text(img, t, 3.1, "A REPAIR BILL", 1250, 92, CORAL, 10)
    s, al, a = pop(t, 4.3, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1470, scale=1.2, alpha=0.3 * al)
        put(img, tag_spr("UP TO $10,000", 860, 150, GOLD, 80), 540, 1470, scale=s, alpha=al, rot=-2, shadow=14)
        burst(img, t, 4.3, 540, 1470, n=14, color=GOLD, dur=0.7, rad=440, seed=108)
    for k in range(5):
        u = seg(t, 5.0 + k * 0.15, 0.8)
        if u > 0:
            put(img, coin_spr(), 300 + k * 120, 1320 - 90 * ease(u) + 14 * math.sin(u * 6), scale=0.7, alpha=1 - seg(t, 6.2, 0.4))
    s, al, a = pop(t, 7.1, 0.45)
    if a > 0:
        put(img, stamp_spr("NOT A LOAN", 640, 130, SAGE), 540, 1640, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 7.1, 540, 1640, n=12, color=SAGE, dur=0.7, rad=220, seed=109)

# ---------------------------------------------------------------- B4 (179 f = 6,0 s)
def c4(img, t):
    ambient_food(img, t, n=6, seed=107)
    label(img, t, "WHO QUALIFIES?", 300, GOLD)
    for i in range(6):
        s, al, a = pop(t, 0.2 + i * 0.12, 0.35)
        if a > 0:
            put(img, person_spr("off" if i not in (1, 4) else "on") if False else person_spr("off"), 170 + i * 148, 700, scale=1.0 * s, alpha=al, shadow=8)
    s, al, a = pop(t, 1.3, 0.45)
    if a > 0:
        for i in (1, 4):
            put(img, check_spr(), 170 + i * 148, 880, scale=0.5 * s, alpha=al)
        for i in (0, 2, 3, 5):
            put(img, bigx_spr(), 170 + i * 148, 880, scale=0.3 * s, alpha=al)
    pop_text(img, t, 2.0, "ONLY SOME PEOPLE QUALIFY", 1060, 58, IVORY, 8)
    s, al, a = pop(t, 3.0, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1330, scale=1.2, alpha=0.3 * al)
        put(img, rule8_spr(), 540, 1340, scale=1.0 * s, alpha=al, shadow=14, rot=-2)
    pop_text(img, t, 4.8, "THE RULE NOBODY CHECKS", 1650, 56, CORAL, 8, track=1)

# ---------------------------------------------------------------- B5 (155 f = 5,2 s)
def c5(img, t):
    ambient_food(img, t, n=6, seed=109)
    label(img, t, "THE ORDER MATTERS", 300, CORAL)
    order = (3, 1, 4, 2, 5)
    for i, n in enumerate(order):
        s, al, a = pop(t, 0.2 + i * 0.18, 0.35)
        if a > 0:
            put(img, tile7(n, "warn" if t > 2.0 else "off"), 180 + i * 180, 720, scale=1.15 * s, alpha=al, shadow=8)
    for i in range(4):
        a = seg(t, 1.2 + i * 0.12, 0.3)
        if a > 0:
            put(img, tspr(">", FONT_SANS, 80, IVORY), 270 + i * 180, 720, alpha=ease(a) * 0.9)
    s, al, a = pop(t, 2.2, 0.5)
    if a > 0:
        put(img, stamp_spr("WRONG ORDER", 700, 140, CORAL), 540, 1020, scale=s, alpha=al, rot=-4, shadow=14)
        burst(img, t, 2.2, 540, 1020, n=12, color=CORAL, dur=0.7, rad=340, seed=110)
    pop_text(img, t, 3.0, "YOU CAN MISS", 1230, 80, IVORY, 8)
    s, al, a = pop(t, 4.1, 0.5)
    if a > 0:
        put(img, tag_spr("HELP YOU QUALIFIED FOR", 860, 130, GOLD, 46), 540, 1400, scale=s, alpha=al, rot=-2, shadow=12)
        burst(img, t, 4.1, 540, 1400, n=12, color=GOLD, dur=0.7, rad=380, seed=111)

# ---------------------------------------------------------------- B6 (247 f = 8,2 s)
def c6(img, t):
    ambient_food(img, t, n=6, seed=111)
    label(img, t, "THE FULL VIDEO", 300, GOLD)
    s, al, a = pop(t, 0.2, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 760, scale=1.5, alpha=0.3 * al)
        put(img, vcard8_spr(), 540, 760, scale=1.0 * s * (1 + 0.012 * math.sin(t * 6)), alpha=al, shadow=18, rot=-2 * (1 - ease(a)))
        burst(img, t, 0.3, 540, 760, n=12, color=GOLD, dur=0.7, rad=460, seed=112)
    pop_text(img, t, 2.0, "ALL SEVEN, ONE VIDEO", 1150, 72, IVORY, 8)
    pop_text(img, t, 3.6, "THE RIGHT ORDER", 1255, 62, SAGE, 6, track=1)
    pop_text(img, t, 5.0, "RIGHT BELOW", 1370, 100, GOLD, 12)
    pop_text(img, t, 6.4, "TAP IT NOW", 1490, 84, IVORY, 10)
    for k in range(3):
        a = seg(t, 5.1 + k * 0.1, 0.3)
        if a > 0:
            ph = (t * 2.2 - k * 0.22) % 1.0
            put(img, chevron_spr(), 540, 1610 + k * 46 + 18 * math.sin(ph * 6.28), alpha=ease(a) * (0.5 + 0.5 * math.sin(ph * 6.28) ** 2), scale=0.7)

# ---------------------------------------------------------------- B7 (202 f = 6,7 s)
def c7(img, t):
    ambient_food(img, t, n=6, seed=113)
    label(img, t, "THE SENIOR ADVANTAGE", 300, SAGE)
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
        put(img, subpill_spr(), 540, 1700 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)

SCENES8 = {1: (c1, 315), 2: (c2, 293), 3: (c3, 267), 4: (c4, 179), 5: (c5, 155), 6: (c6, 247), 7: (c7, 202)}
DRAW = {k: v[0] for k, v in SCENES8.items()}
DUR = {k: v[1] for k, v in SCENES8.items()}

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES8)
    out_dir = os.environ.get("S8_OUT", "short8")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        fn, nf = SCENES8[k]
        render_seq(zoomed(fn), nf, f"{out_dir}/short8-blocco{k:02d}.mp4")
