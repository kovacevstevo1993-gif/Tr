"""Video lungo 4 (BOLLETTE) - blocchi 36-50 (snap fine, CSFP, bus). 1920x1080, 30 fps.
Durate (timeline utente 08/10/2026): B36 295, B37 343, B38 252, B39 325, B40 198, B41 340, B42 299, B43 301, B44 270, B45 351, B46 210, B47 285, B48 221, B49 411, B50 323.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long4_b36_50.py <blocco>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b31_35 import *

DUR = {36: 295, 37: 343, 38: 252, 39: 325, 40: 198, 41: 340, 42: 299, 43: 301, 44: 270, 45: 351, 46: 210, 47: 285, 48: 221, 49: 411, 50: 323}
PHRASES = {
    36: ["And savings?", "A household with someone sixty or older can have up to four thousand seven hundred fifty dollars.", "And your home doesn't count at all."],
    37: ["The mistake is deciding by yourself that you earn too much.", "Don't decide.", "Apply, and let your state snap office do the math.", "They must decide within thirty days."],
    38: ["Who does snap help most?", "Seniors with high medical bills or high rent.", "Those two deductions can turn a no into a yes."],
    39: ["And remember the order I promised.", "If snap says yes, that same yes can open the door to Lifeline, bill number three.", "One approval, two bills lower."],
    40: ["Bill number five is still about food,", "but it's a program almost no one over sixty has ever heard of."],
    41: ["It's called C S F P, the Commodity Supplemental Food Program, run by the U S D A.", "If you're at least sixty and your income is low,", "you can get a box of food every month."],
    42: ["Inside, you can find milk, cheese, juice, cereal, rice, pasta, peanut butter and dry beans.", "Plus canned meat, fruit and vegetables."],
    43: ["But here's the catch.", "Every state sets its own income limit,", "and the program is not available in every area.", "So you have to ask where you live."],
    44: ["The list of state agencies is on the U S D A website.", "Look up C S F P program contacts,", "and call the one for your state."],
    45: ["Who does this help most?", "People over sixty living alone on a small fixed income,", "who skip meals at the end of the month.", "If that's you, or your neighbor, make that call."],
    46: ["Bill number six.", "And this one is so simple, it almost feels like a secret.", "The bus."],
    47: ["Under federal law, transit agencies that receive a certain kind of federal funding", "must offer reduced fares to older riders outside of rush hour."],
    48: ["How much?", "During off peak hours, your fare can be no more than half of the regular peak fare.", "Half.", "Every ride."],
    49: ["The minimum age is sixty five,", "and some agencies start earlier, at sixty two.", "It covers regular buses, trains and ferries.", "And you can also qualify by showing your Medicare card."],
    50: ["The mistake?", "Paying full price for years because nobody asked for the card.", "Most agencies give you a special reduced fare I D,", "and you have to apply for it."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def ic_jar(c, cx, cy, s):
    c.rrect((cx - 52 * s, cy - 62 * s, cx + 52 * s, cy + 64 * s), 22 * s, fill=(190, 222, 232, 110), outline=SAGE, width=5)
    c.rrect((cx - 60 * s, cy - 78 * s, cx + 60 * s, cy - 56 * s), 8 * s, fill=GOLD)
    for k, dy in enumerate((40, 10, -20)):
        c.ell((cx - 34 * s, cy + dy * s, cx + 34 * s, cy + (dy + 26) * s), fill=GOLD, outline=(168, 118, 40), width=3)

def ic_box(c, cx, cy, s):
    c.poly([(cx - 66 * s, cy - 20 * s), (cx - 34 * s, cy - 56 * s), (cx + 34 * s, cy - 56 * s), (cx + 66 * s, cy - 20 * s)], fill=(160, 112, 56))
    c.rrect((cx - 66 * s, cy - 24 * s, cx + 66 * s, cy + 56 * s), 6 * s, fill=(196, 146, 78), outline=(160, 112, 56), width=4)
    c.rrect((cx - 20 * s, cy - 24 * s, cx + 20 * s, cy + 6 * s), 4, fill=(226, 190, 130))

def ic_cal(c, cx, cy, s, txt_="30"):
    c.rrect((cx - 56 * s, cy - 56 * s, cx + 56 * s, cy + 60 * s), 12 * s, fill=IVORY, outline=(206, 200, 186), width=4)
    c.rrect((cx - 56 * s, cy - 56 * s, cx + 56 * s, cy - 18 * s), 12 * s, fill=RED)
    c.text((cx, cy + 14 * s), txt_, FONT_SANS, 52 * s, GREEN_D)

def ic_cross(c, cx, cy, r, col=CORAL):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=PANEL_FILL, outline=col, width=r * 0.08)
    c.rrect((cx - r * 0.2, cy - r * 0.62, cx + r * 0.2, cy + r * 0.62), 6, fill=col)
    c.rrect((cx - r * 0.62, cy - r * 0.2, cx + r * 0.62, cy + r * 0.2), 6, fill=col)

def ic_train(c, cx, cy, s):
    c.rrect((cx - 54 * s, cy - 60 * s, cx + 54 * s, cy + 40 * s), 20 * s, fill=(70, 120, 176), outline=(36, 76, 128), width=3)
    c.rrect((cx - 40 * s, cy - 44 * s, cx + 40 * s, cy - 6 * s), 6 * s, fill=(190, 222, 232))
    c.ell((cx - 36 * s, cy + 6 * s, cx - 20 * s, cy + 22 * s), fill=GOLD); c.ell((cx + 20 * s, cy + 6 * s, cx + 36 * s, cy + 22 * s), fill=GOLD)
    c.line([(cx - 40 * s, cy + 60 * s), (cx - 14 * s, cy + 40 * s)], SAGE_D, 6 * s); c.line([(cx + 40 * s, cy + 60 * s), (cx + 14 * s, cy + 40 * s)], SAGE_D, 6 * s)

def ic_ferry(c, cx, cy, s):
    c.poly([(cx - 70 * s, cy + 6 * s), (cx + 70 * s, cy + 6 * s), (cx + 50 * s, cy + 46 * s), (cx - 50 * s, cy + 46 * s)], fill=(70, 120, 176))
    c.rrect((cx - 40 * s, cy - 30 * s, cx + 40 * s, cy + 6 * s), 5 * s, fill=IVORY)
    c.rrect((cx - 16 * s, cy - 56 * s, cx + 16 * s, cy - 30 * s), 4 * s, fill=CORAL)
    for k in range(4):
        c.arc((cx - 70 * s + k * 36 * s, cy + 46 * s, cx - 40 * s + k * 36 * s, cy + 66 * s), 0, 180, ICE, 5 * s)

def ic_card_id(c, cx, cy, s, txt_="REDUCED FARE", col=GOLD):
    c.rrect((cx - 100 * s, cy - 62 * s, cx + 100 * s, cy + 62 * s), 12 * s, fill=IVORY, outline=col, width=5)
    c.rrect((cx - 100 * s, cy - 62 * s, cx + 100 * s, cy - 22 * s), 12 * s, fill=col)
    c.text((cx, cy - 40 * s), txt_, FONT_SANS, 22 * s, GREEN_D, track=2)
    ic_person(c, cx - 46 * s, cy + 22 * s, 0.55 * s, col=GREEN_L)
    for k in range(3):
        c.rrect((cx - 4 * s, cy - 6 * s + k * 20 * s, cx + 80 * s, cy + 2 * s + k * 20 * s), 3, fill=(206, 202, 190))

def food_chip(name, col=GOLD, w=None):
    w = w or int(90 + len(name) * 30)
    return pill_spr(name, 42, w, 110, PANEL_FILL, col, border=col, track=2)

def pin_map():
    def fn(c):
        w, h = 760, 440
        c.rrect((6, 6, w - 6, h - 6), 36, fill=(30, 74, 58), outline=SAGE_D, width=6)
        c.poly([(80, 120), (220, 70), (380, 100), (520, 60), (690, 130), (650, 300), (520, 380), (360, 340), (200, 390), (90, 300)], fill=(54, 108, 86), )
        c.line([(80, 120), (220, 70), (380, 100), (520, 60), (690, 130), (650, 300), (520, 380), (360, 340), (200, 390), (90, 300), (80, 120)], SAGE, 5)
    return sprite("map43", 760, 440, fn)

# ============================================================ BLOCCO 36
def draw36(img, t):
    ts = starts(36)
    common(img, t, "SAVINGS")
    seq(img, t, ts[0], stamp("AND SAVINGS?", 560, 120, GOLD, size=56), 960, 200, shadow=12, rot=-2)
    slide_in(img, t, ts[1], panel(760, 560, border=GOLD), 500, 600, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.2, sprite("jar36", 260, 300, lambda c: ic_jar(c, 130, 150, 2.0)), 500, 520, shadow=8)
    seq(img, t, ts[1] + 0.5, txt("UP TO", 40, SAGE, 5), 500, 710)
    counter(img, t, ts[1] + 0.7, 1.8, "$", 4750, "", 96, GOLD, 500, 790)
    seq(img, t, ts[1] + 0.2, txt("60+ HOUSEHOLD", 34, IVORY, 3), 500, 380)
    slide_in(img, t, ts[2], panel(760, 560, border=SAGE), 1400, 600, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.2, sprite("house36", 340, 300, lambda c: ic_house(c, 170, 160, 3.0, col=IVORY)), 1400, 520, shadow=8)
    s, a, p = pop(t, ts[2] + 0.6, 0.45)
    if p > 0:
        put(img, stamp("DOESN'T COUNT", 520, 110, SAGE, size=46), 1400, 760, scale=s, alpha=a, rot=-3, shadow=10)
        put(img, sprite("x36", 300, 300, lambda c: ic_x(c, 150, 150, 3.0, RED, 14)), 1400, 520, scale=0.75 * s, alpha=a * 0.9)

# ============================================================ BLOCCO 37
def draw37(img, t):
    ts = starts(37)
    common(img, t, "THE MISTAKE")
    seq(img, t, ts[0] - 0.05, stamp("THE MISTAKE", 560, 120, RED, size=56), 960, 200, shadow=12, rot=-2)
    seq(img, t, ts[0] + 0.3, sprite("pe37", 220, 260, lambda c: ic_person(c, 110, 140, 2.0, col=GOLD)), 260, 520, shadow=10)
    seq(img, t, ts[0] + 0.8, bubble_sp("I EARN TOO MUCH", RED), 640, 440, shadow=8)
    seq(img, t, ts[1], stamp("DON'T DECIDE", 480, 100, GOLD, size=46), 640, 640, rot=-3, shadow=10)
    p = ease(seg(t, ts[2], 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 160, 110), 1080, 440, alpha=p)
    slide_in(img, t, ts[2], sprite("form37", 300, 380, lambda c: (c.rrect((6, 6, 294, 374), 20, fill=IVORY, outline=(206, 200, 186), width=5), c.rrect((6, 6, 294, 80), 20, fill=GREEN_L), c.text((150, 44), "APPLY", FONT_SANS, 42, IVORY, track=4), [c.rrect((40, 112 + k * 52, 260, 126 + k * 52), 6, fill=(206, 212, 206)) for k in range(4)], c.ell((190, 280, 270, 360), fill=GOLD), c.line([(208, 322), (226, 340), (254, 300)], GREEN_D, 10))), 1300, 460, dx=40, dur=0.5, shadow=14)
    seq(img, t, ts[2] + 0.6, sprite("snapoff37", 360, 250, lambda c: (ic_gov(c, 180, 100, 1.6), c.rrect((40, 190, 320, 236), 12, fill=GOLD), c.text((180, 214), "STATE snap OFFICE", FONT_SANS_M, 24, GREEN_D, track=1))), 1700, 440, shadow=8, scale=0.9)
    seq(img, t, ts[2] + 1.1, txt("THEY DO THE MATH", 40, GOLD, 3), 1500, 690)
    seq(img, t, ts[3], sprite("cal37", 240, 240, lambda c: ic_cal(c, 120, 120, 1.8, "30")), 700, 880, shadow=10, scale=0.8)
    seq(img, t, ts[3] + 0.3, txt("DAYS", 56, GOLD, 5), 930, 890)
    ban(img, t, ts[3] + 0.5, "THEY MUST DECIDE WITHIN THIRTY DAYS", cy=985, w=1320, size=48)

def bubble_sp(text, col):
    def fn(c):
        w, h = 620, 150
        c.rrect((6, 6, w - 6, h - 20), 50, fill=PANEL_FILL, outline=col, width=7)
        c.poly([(80, h - 24), (130, h - 24), (60, h - 2)], fill=PANEL_FILL)
        c.text((w / 2, 64), text, FONT_SANS, 46, col, track=2)
    return sprite(("bub37", text), 620, 150, fn)

# ============================================================ BLOCCO 38
def draw38(img, t):
    ts = starts(38)
    common(img, t, "WHO IT HELPS MOST")
    seq(img, t, ts[0], stamp("WHO IT HELPS MOST", 760, 120, GOLD, size=52), 960, 200, shadow=12)
    seq(img, t, ts[1], sprite("pe38", 220, 260, lambda c: ic_person(c, 110, 140, 2.0, col=GOLD)), 960, 460, shadow=10)
    slide_in(img, t, ts[1] + 0.2, sprite("med38", 560, 420, lambda c: (c.rrect((5, 5, 555, 415), 36, fill=PANEL_FILL, outline=CORAL, width=7), ic_cross(c, 280, 150, 100), c.text((280, 320), "HIGH MEDICAL", FONT_SANS, 42, IVORY, track=2), c.text((280, 372), "BILLS", FONT_SANS, 42, CORAL, track=3))), 440, 640, dx=-60, dur=0.55, shadow=14)
    slide_in(img, t, ts[1] + 0.8, sprite("rent38", 560, 420, lambda c: (c.rrect((5, 5, 555, 415), 36, fill=PANEL_FILL, outline=SAGE, width=7), ic_building(c, 280, 150, 1.5), c.text((280, 320), "HIGH", FONT_SANS, 42, IVORY, track=2), c.text((280, 372), "RENT", FONT_SANS, 42, SAGE, track=3))), 1480, 640, dx=60, dur=0.55, shadow=14)
    # no -> yes
    s, a, p = pop(t, ts[2], 0.45)
    if p > 0:
        put(img, stamp("NO", 200, 100, RED, size=54), 800, 860, scale=s, alpha=a, rot=-4, shadow=8)
    pa = ease(seg(t, ts[2] + 0.5, 0.5))
    if pa > 0:
        put(img, rarrow(GOLD, 150, 100), 1000, 860, alpha=pa)
    s, a, p = pop(t, ts[2] + 0.9, 0.5)
    if p > 0:
        put(img, stamp("YES", 220, 100, GOLD, size=54), 1230, 860, scale=s, alpha=a, rot=3, shadow=8)
        burst(img, t, ts[2] + 0.9, 1230, 860, n=12, color=GOLD, rad=200, seed=38)
    seq(img, t, ts[2] + 0.2, txt("TWO DEDUCTIONS", 38, SAGE, 4), 960, 770)

# ============================================================ BLOCCO 39
def draw39(img, t):
    ts = starts(39)
    common(img, t, "THE ORDER I PROMISED")
    seq(img, t, ts[0], stamp("THE ORDER I PROMISED", 880, 120, GOLD, size=48), 960, 200, shadow=12)
    slide_in(img, t, ts[1], ebt(), 400, 560, dx=-60, dur=0.55, shadow=16, scale=0.85)
    check_at(img, t, ts[1] + 0.9, 600, 440, 1.3)
    seq(img, t, ts[1] + 0.9, stamp("YES", 200, 90, GOLD, size=48), 400, 760, rot=-3, shadow=8)
    p = ease(seg(t, ts[1] + 1.4, 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 170, 110), 900, 560, alpha=p)
    s, a, p = pop(t, ts[1] + 1.8, 0.5)
    if p > 0:
        put(img, sprite("life39", 520, 340, lambda c: (c.rrect((5, 5, 515, 335), 40, fill=PANEL_FILL, outline=GOLD, width=8), ic_phone(c, 130, 170, 1.6), c.text((350, 140), "LIFELINE", FONT_SANS, 58, GOLD, track=3), c.text((350, 210), "BILL NUMBER THREE", FONT_SANS_M, 28, SAGE, track=3))), 1300, 560, scale=s, alpha=a, shadow=14)
        burst(img, t, ts[1] + 1.8, 1300, 560, n=12, color=GOLD, rad=240, seed=39)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, numbadge(1, 170), 700, 900, scale=s, alpha=a, shadow=10)
    seq(img, t, ts[2] + 0.1, txt("APPROVAL", 50, IVORY, 4), 940, 900)
    seq(img, t, ts[2] + 0.5, txt("=", 70, GOLD, 0), 1180, 900)
    seq(img, t, ts[2] + 0.7, numbadge(2, 170), 1360, 900, shadow=10)
    seq(img, t, ts[2] + 0.9, txt("BILLS LOWER", 50, GOLD, 4), 1660, 900)

# ============================================================ BLOCCO 40
def draw40(img, t):
    ts = starts(40)
    common(img, t, "BILL NUMBER FIVE")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(5, 400), 360, 330, scale=s, alpha=a, shadow=18)
        burst(img, t, ts[0], 360, 330, n=14, color=GOLD, rad=300, seed=40)
    seq(img, t, ts[0] + 0.4, panel(1080, 400, border=GOLD), 1230, 330, shadow=14)
    seq(img, t, ts[0] + 0.6, sprite("box40", 340, 340, lambda c: ic_box(c, 170, 170, 2.2)), 880, 340)
    seq(img, t, ts[0] + 0.8, txt("YOUR", 64, SAGE, 5), 1360, 250)
    seq(img, t, ts[0] + 0.95, txt("FOOD BOX", 92, IVORY, 3), 1360, 360)
    for i in range(7):
        s, a, p = pop(t, ts[1] + 0.2 + i * 0.09, 0.35)
        if p > 0:
            put(img, person_q(SAGE_D), 360 + i * 200, 800, scale=1.0 * s, alpha=a * 0.9)
            put(img, sprite(("qm40", i), 80, 80, lambda c: c.text((40, 44), "?", FONT_SERIF, 70, GOLD)), 360 + i * 200, 700, scale=s, alpha=a)
    ban(img, t, ts[1] + 0.9, "ALMOST NO ONE OVER 60 HAS HEARD OF IT", cy=975, w=1340, size=48)

# ============================================================ BLOCCO 41
def draw41(img, t):
    ts = starts(41)
    common(img, t, "THE PROGRAM")
    for k, ch in enumerate("CSFP"):
        s, a, p = pop(t, ts[0] + 0.1 + k * 0.25, 0.4)
        if p > 0:
            put(img, tspr(ch, FONT_SERIF, 210, GOLD), 780 + k * 120, 230, scale=s, alpha=a, shadow=12)
    seq(img, t, ts[0] + 1.3, txt("COMMODITY SUPPLEMENTAL FOOD PROGRAM", 44, IVORY, 2), 960, 370, shadow=6)
    seq(img, t, ts[0] + 2.2, stamp("RUN BY THE U S D A", 640, 100, SAGE, size=42), 960, 470, rot=-1, shadow=8)
    slide_in(img, t, ts[1], sprite("age41", 520, 340, lambda c: (c.rrect((5, 5, 515, 335), 36, fill=PANEL_FILL, outline=GOLD, width=7), c.text((260, 130), "60+", FONT_SERIF, 130, GOLD), c.text((260, 240), "AT LEAST SIXTY", FONT_SANS, 36, IVORY, track=2), c.text((260, 288), "LOW INCOME", FONT_SANS, 32, SAGE, track=3))), 560, 760, dx=-60, dur=0.55, shadow=14)
    p = ease(seg(t, ts[2] - 0.3, 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 960, 760, alpha=p)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("mbox41", 520, 340, lambda c: (c.rrect((5, 5, 515, 335), 36, fill=PANEL_FILL, outline=SAGE, width=7), ic_box(c, 140, 160, 1.9), ic_cal(c, 370, 150, 1.3, "1"), c.text((260, 292), "EVERY MONTH", FONT_SANS, 34, GOLD, track=3))), 1360, 760, scale=s, alpha=a, shadow=14)

# ============================================================ BLOCCO 42
FOODS = ["MILK", "CHEESE", "JUICE", "CEREAL", "RICE", "PASTA", "PEANUT BUTTER", "DRY BEANS"]
def draw42(img, t):
    ts = starts(42)
    common(img, t, "INSIDE THE BOX")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, sprite("bigbox42", 400, 340, lambda c: ic_box(c, 200, 170, 2.9)), 230, 440, scale=s, alpha=a, shadow=16)
    pos = [(780, 250), (1180, 250), (1580, 250), (780, 400), (1180, 400), (1580, 400), (920, 550), (1520, 550)]
    for k, name in enumerate(FOODS):
        s, a, p = pop(t, ts[0] + 0.5 + k * 0.38, 0.35)
        if p > 0:
            put(img, food_chip(name, col=[GOLD, SAGE][k % 2]), pos[k][0], pos[k][1], scale=s, alpha=a, shadow=6)
    seq(img, t, ts[1] - 0.1, txt("PLUS", 46, SAGE, 8), 960, 700)
    for k, name in enumerate(("CANNED MEAT", "FRUIT", "VEGETABLES")):
        s, a, p = pop(t, ts[1] + 0.2 + k * 0.35, 0.35)
        if p > 0:
            put(img, food_chip(name, col=CORAL), 420 + k * 540, 850, scale=s, alpha=a, shadow=6)

# ============================================================ BLOCCO 43
def draw43(img, t):
    ts = starts(43)
    common(img, t, "THE CATCH")
    s, a, p = pop(t, ts[0], 0.45)
    if p > 0:
        put(img, sprite("warn43", 200, 190, lambda c: warn_tri(c, 100, 100, 1.5)), 400, 210, scale=s, alpha=a)
    seq(img, t, ts[0] + 0.3, txt("THE CATCH", 90, GOLD, 4), 840, 210, shadow=10)
    seq(img, t, ts[1], pin_map(), 560, 600, shadow=14)
    cols = [GOLD, SAGE, CORAL, IVORY]
    for k, (dx, dy, st) in enumerate(((-200, -80, "TX"), (0, 40, "NY"), (190, -60, "CA"), (-70, 130, "FL"))):
        s, a, p = pop(t, ts[1] + 0.4 + k * 0.35, 0.4)
        if p > 0:
            put(img, sprite(("pin43", k), 90, 130, lambda c, k=k: ic_pin(c, 45, 55, 1.0, col=cols[k])), 560 + dx, 600 + dy, scale=s, alpha=a)
            put(img, tag_spr_small(st, cols[k]), 560 + dx, 600 + dy - 80, scale=s, alpha=a)
    seq(img, t, ts[1] + 1.8, txt("OWN INCOME LIMIT", 44, IVORY, 3), 560, 880)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("map43b", 760, 440, lambda c: (c.rrect((6, 6, 754, 434), 36, fill=(30, 74, 58), outline=RED, width=6), c.rrect((120, 80, 360, 360), 30, fill=(54, 108, 86)), c.rrect((420, 80, 650, 360), 30, fill=(54, 108, 86)), ic_x(c, 240, 220, 2.4, RED, 14), c.text((380, 400), "NOT IN EVERY AREA", FONT_SANS, 34, RED, track=3))), 1440, 600, scale=s, alpha=a, shadow=14)
    seq(img, t, ts[3], stamp("ASK WHERE YOU LIVE", 760, 110, GOLD, size=46), 1440, 910, rot=-2, shadow=10)

def tag_spr_small(text, col):
    def fn(c):
        c.rrect((4, 4, 116, 56), 14, fill=PANEL_FILL, outline=col, width=4)
        c.text((60, 31), text, FONT_SANS, 28, col, track=2)
    return sprite(("tg43", text, col), 120, 60, fn)

# ============================================================ BLOCCO 44
def draw44(img, t):
    ts = starts(44)
    common(img, t, "STATE AGENCIES")
    slide_in(img, t, ts[0], browser_gov(), 560, 520, dx=-60, dur=0.55, shadow=18)
    seq(img, t, ts[0] + 0.5, txt("U S D A WEBSITE", 36, SAGE, 4), 560, 840)
    seq(img, t, ts[1], sprite("search44", 760, 130, lambda c: (c.rrect((4, 4, 756, 126), 60, fill=IVORY, outline=GOLD, width=7), magnifier(c, 82, 64, 26, GREEN_D, 9), c.text((420, 66), "CSFP PROGRAM CONTACTS", FONT_SANS_M, 36, GREEN_D))), 1400, 330, shadow=10)
    s, a, p = pop(t, ts[1] + 0.6, 0.45)
    if p > 0:
        put(img, sprite("list44", 560, 300, lambda c: (c.rrect((5, 5, 555, 295), 30, fill=IVORY, outline=(206, 200, 186), width=5), [(c.ell((36, 36 + k * 60, 66, 66 + k * 60), fill=GOLD), c.rrect((90, 44 + k * 60, 90 + (320 if k % 2 == 0 else 250), 58 + k * 60), 6, fill=(206, 212, 206))) for k in range(4)])), 1400, 560, scale=s, alpha=a, shadow=12)
    seq(img, t, ts[2], sprite("call44", 560, 200, lambda c: (c.rrect((5, 5, 555, 195), 36, fill=PANEL_FILL, outline=SAGE, width=7), ic_phone(c, 100, 100, 1.2), c.text((340, 82), "CALL THE ONE", FONT_SANS, 40, IVORY, track=2), c.text((340, 132), "FOR YOUR STATE", FONT_SANS, 40, GOLD, track=2))), 1400, 850, shadow=12)

# ============================================================ BLOCCO 45
def draw45(img, t):
    ts = starts(45)
    common(img, t, "WHO IT HELPS MOST")
    seq(img, t, ts[0], stamp("WHO IT HELPS MOST", 760, 120, GOLD, size=52), 960, 200, shadow=12)
    seq(img, t, ts[1], sprite("alone45", 300, 340, lambda c: ic_person(c, 150, 190, 2.8, col=GOLD)), 400, 520, shadow=12)
    seq(img, t, ts[1] + 0.5, txt("LIVING ALONE", 40, IVORY, 3), 400, 730)
    seq(img, t, ts[1] + 0.8, txt("SMALL FIXED INCOME", 30, SAGE, 3), 400, 780)
    # calendario fine mese + piatto vuoto
    seq(img, t, ts[2], sprite("cal45", 300, 300, lambda c: ic_cal(c, 150, 150, 2.4, "30")), 960, 520, shadow=12)
    seq(img, t, ts[2] + 0.4, txt("END OF THE MONTH", 34, SAGE, 3), 960, 710)
    seq(img, t, ts[2] + 0.7, sprite("plate45", 300, 300, lambda c: (c.ell((20, 20, 280, 280), fill=IVORY, outline=(206, 200, 186), width=6), c.ell((70, 70, 230, 230), outline=(214, 208, 194), width=5))), 1480, 520, shadow=12)
    seq(img, t, ts[2] + 1.0, stamp("SKIPPED MEALS", 460, 100, RED, size=40), 1480, 740, rot=-3, shadow=8)
    ban(img, t, ts[3] + 0.3, "IF THAT'S YOU, OR YOUR NEIGHBOR, MAKE THE CALL", cy=985, w=1500, size=44)

# ============================================================ BLOCCO 46
def draw46(img, t):
    ts = starts(46)
    common(img, t, "BILL NUMBER SIX")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(6, 400), 360, 330, scale=s, alpha=a, shadow=18)
        burst(img, t, ts[0], 360, 330, n=14, color=GOLD, rad=300, seed=46)
    seq(img, t, ts[0] + 0.8, panel(1080, 400, border=GOLD), 1230, 330, shadow=14)
    seq(img, t, ts[0] + 1.0, sprite("bus46", 360, 300, lambda c: ic_bus(c, 180, 150, 2.2)), 880, 330)
    seq(img, t, ts[0] + 1.2, txt("YOUR", 64, SAGE, 5), 1360, 250)
    seq(img, t, ts[0] + 1.35, txt("BUS FARE", 92, IVORY, 3), 1360, 360)
    seq(img, t, ts[1], stamp("SO SIMPLE", 460, 110, GOLD, size=52), 640, 760, rot=-3, shadow=10)
    seq(img, t, ts[1] + 0.8, sprite("key46", 200, 200, lambda c: (c.ell((20, 40, 100, 120), outline=GOLD, width=14), c.line([(100, 80), (180, 80)], GOLD, 14), c.line([(150, 80), (150, 112)], GOLD, 12), c.line([(176, 80), (176, 106)], GOLD, 12))), 980, 760, shadow=8, scale=0.85)
    seq(img, t, ts[1] + 1.1, txt("ALMOST A SECRET", 44, SAGE, 4), 1340, 760)

# ============================================================ BLOCCO 47
def draw47(img, t):
    ts = starts(47)
    common(img, t, "UNDER FEDERAL LAW")
    slide_in(img, t, ts[0], panel(560, 520, border=SAGE), 380, 540, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.3, sprite("gov47", 300, 240, lambda c: ic_gov(c, 150, 120, 2.0)), 380, 450, shadow=8)
    seq(img, t, ts[0] + 0.8, txt("FEDERAL FUNDING", 38, IVORY, 3), 380, 610)
    seq(img, t, ts[0] + 1.0, txt("FOR TRANSIT AGENCIES", 28, SAGE, 3), 380, 660)
    p = ease(seg(t, ts[0] + 1.5, 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 760, 540, alpha=p)
    slide_in(img, t, ts[1], panel(940, 520, border=GOLD), 1330, 540, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.2, sprite("bus47", 300, 220, lambda c: ic_bus(c, 150, 110, 1.9)), 1130, 480, shadow=8)
    seq(img, t, ts[1] + 0.5, sprite("elder47", 200, 240, lambda c: ic_person(c, 100, 130, 1.7, col=GOLD)), 1500, 480, shadow=8)
    seq(img, t, ts[1] + 0.8, txt("REDUCED FARES", 52, GOLD, 4), 1330, 650)
    seq(img, t, ts[1] + 1.0, txt("FOR OLDER RIDERS", 36, IVORY, 3), 1330, 705)
    seq(img, t, ts[1] + 1.6, sprite("rush47", 440, 140, lambda c: (c.rrect((4, 4, 436, 136), 36, fill=PANEL_FILL, outline=CORAL, width=6), ic_clock(c, 80, 70, 44, 0.9), ic_x(c, 80, 70, 1.0, RED, 8), c.text((290, 70), "OUTSIDE RUSH HOUR", FONT_SANS, 24, CORAL, track=1))), 960, 905, shadow=8, scale=1.5)

# ============================================================ BLOCCO 48
def draw48(img, t):
    ts = starts(48)
    common(img, t, "HOW MUCH?")
    seq(img, t, ts[0], stamp("HOW MUCH?", 480, 120, GOLD, size=60), 960, 200, shadow=12)
    slide_in(img, t, ts[1], panel(1500, 440, border=SAGE), 960, 520, dy=50, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, txt("REGULAR PEAK FARE", 38, IVORY, 3), 560, 400)
    p = ease(seg(t, ts[1] + 0.5, 0.7))
    if p > 0:
        w = int(1100 * p)
        put(img, sprite(("f48", w), max(8, w), 70, lambda c: c.rrect((2, 2, max(8, w) - 2, 68), 16, fill=SAGE_D)), 350 + w / 2, 460)
    seq(img, t, ts[1] + 1.2, txt("OFF PEAK FARE", 38, GOLD, 3), 500, 580)
    p = ease(seg(t, ts[1] + 1.4, 0.7))
    if p > 0:
        w = int(550 * p)
        put(img, sprite(("h48", w), max(8, w), 70, lambda c: c.rrect((2, 2, max(8, w) - 2, 68), 16, fill=GOLD)), 350 + w / 2, 640)
    seq(img, t, ts[1] + 2.2, txt("NO MORE THAN HALF", 44, GOLD, 3), 1180, 640)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("half48", 260, 200, lambda c: c.text((130, 100), "1/2", FONT_SANS, 130, GOLD, track=2)), 960, 860, scale=s, alpha=a, shadow=10)
        burst(img, t, ts[2], 960, 860, n=12, color=GOLD, rad=220, seed=48)
    seq(img, t, ts[3], txt("EVERY RIDE", 54, IVORY, 5), 1500, 860, shadow=8)

# ============================================================ BLOCCO 49
def draw49(img, t):
    ts = starts(49)
    common(img, t, "WHO QUALIFIES")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, star60("65"), 400, 360, scale=1.05 * s, alpha=a, shadow=14)
    seq(img, t, ts[0] + 0.4, txt("MINIMUM AGE", 40, IVORY, 4), 400, 560)
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, star60("62"), 860, 360, scale=0.85 * s, alpha=a, shadow=14)
    seq(img, t, ts[1] + 0.4, txt("SOME START EARLIER", 34, SAGE, 3), 860, 540)
    for k, (fn, name, x) in enumerate(((ic_bus, "BUSES", 1300), (ic_train, "TRAINS", 1560), (ic_ferry, "FERRIES", 1810))):
        s, a, p = pop(t, ts[2] + 0.15 + k * 0.45, 0.4)
        if p > 0:
            put(img, sprite(("md49", k), 220, 280, lambda c, fn=fn, name=name: (c.rrect((4, 4, 216, 276), 30, fill=PANEL_FILL, outline=SAGE, width=6), fn(c, 110, 120, 1.0), c.text((110, 236), name, FONT_SANS, 30, GOLD, track=2))), x - 130, 380, scale=0.95 * s, alpha=a, shadow=8)
    slide_in(img, t, ts[3], sprite("mc49", 620, 300, lambda c: (c.rrect((5, 5, 615, 295), 30, fill=IVORY, outline=(70, 120, 176), width=8), c.rrect((5, 5, 615, 80), 30, fill=(70, 120, 176)), c.text((310, 44), "MEDICARE", FONT_SANS, 44, IVORY, track=4), c.rrect((40, 120, 330, 142), 6, fill=(206, 212, 206)), c.rrect((40, 170, 260, 190), 6, fill=(206, 212, 206)), c.rrect((460, 120, 590, 250), 12, fill=(214, 224, 214)))), 640, 800, dy=60, dur=0.55, shadow=14)
    check_at(img, t, ts[3] + 0.7, 1000, 690, 1.3)
    seq(img, t, ts[3] + 0.5, txt("OR SHOW YOUR", 40, SAGE, 4), 1450, 760)
    seq(img, t, ts[3] + 0.7, txt("MEDICARE CARD", 70, GOLD, 4), 1450, 850)

# ============================================================ BLOCCO 50
def draw50(img, t):
    ts = starts(50)
    common(img, t, "THE MISTAKE")
    seq(img, t, ts[0], stamp("THE MISTAKE", 560, 120, RED, size=56), 960, 200, shadow=12, rot=-2)
    seq(img, t, ts[1], sprite("full50", 520, 280, lambda c: (c.rrect((5, 5, 515, 275), 36, fill=PANEL_FILL, outline=RED, width=7), ic_bus(c, 130, 130, 1.5), c.text((350, 100), "FULL PRICE", FONT_SANS, 40, RED, track=2), c.text((350, 170), "FOR YEARS", FONT_SANS, 36, IVORY, track=3))), 480, 470, shadow=14)
    seq(img, t, ts[1] + 0.8, sprite("nobody50", 340, 250, lambda c: (ic_person(c, 100, 130, 1.8, col=SAGE_D), c.text((250, 90), "?", FONT_SERIF, 140, GOLD))), 1100, 460, shadow=8)
    seq(img, t, ts[1] + 1.3, txt("NOBODY ASKED FOR THE CARD", 34, SAGE, 3), 1100, 640)
    p = ease(seg(t, ts[2], 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 560, 810, alpha=p, scale=0.8)
    slide_in(img, t, ts[2], sprite("idc50", 420, 260, lambda c: ic_card_id(c, 210, 130, 2.0, "SENIOR FARE")), 940, 810, dy=40, dur=0.55, shadow=14, scale=0.75)
    seq(img, t, ts[3], stamp("YOU HAVE TO APPLY", 640, 110, GOLD, size=48), 1500, 760, rot=-3, shadow=10)
    ban(img, t, ts[3] + 0.5, "AGENCIES GIVE IT, BUT ONLY IF YOU APPLY", cy=985, cx=1180, w=1300, size=44)

DRAW = {36: draw36, 37: draw37, 38: draw38, 39: draw39, 40: draw40, 41: draw41, 42: draw42, 43: draw43, 44: draw44, 45: draw45, 46: draw46, 47: draw47, 48: draw48, 49: draw49, 50: draw50}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/bollette-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
