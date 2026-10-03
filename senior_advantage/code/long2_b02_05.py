"""Video lungo 2 (SNAP over 60) - blocchi 2-5. Durate in fotogrammi dalla timeline utente.
Uso: OUT=cartella SA_TMP=/tmp/f python3 long2_b02_05.py <blocco> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long2_b01 import *
from long1_blocks import show, txt_in, bubble

BLOCK_FRAMES = {2: 609, 3: 675, 4: 580, 5: 638}


class D:
    def __init__(s, rgb, mask): s.d = ImageDraw.Draw(rgb); s.m = ImageDraw.Draw(mask)
    def rr(s, box, r, fill=None, outline=None, w=0):
        s.d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=w)
        s.m.rounded_rectangle(box, radius=r, fill=255 if fill is not None else None, outline=255 if outline else None, width=w)
    def el(s, box, fill=None, outline=None, w=0):
        s.d.ellipse(box, fill=fill, outline=outline, width=w)
        s.m.ellipse(box, fill=255 if fill is not None else None, outline=255 if outline else None, width=w)
    def pg(s, pts, fill=None, outline=None, w=0):
        s.d.polygon(pts, fill=fill, outline=outline); s.m.polygon(pts, fill=255)
    def ln(s, pts, fill, w):
        s.d.line(pts, fill=fill, width=w); s.m.line(pts, fill=255, width=w)
    def rc(s, box, fill):
        s.d.rectangle(box, fill=fill); s.m.rectangle(box, fill=255)
    def tx(s, xy, t, f, fill, anchor="mm"):
        s.d.text(xy, t, font=f, fill=fill, anchor=anchor); s.m.text(xy, t, font=f, fill=255, anchor=anchor)


BROWN = (150, 104, 62); PINK = (230, 150, 140)


def building(rgb, mask, cx, cy, s=1.0, label="USDA"):
    g = D(rgb, mask)
    g.pg([(cx - 230 * s, cy - 60 * s), (cx, cy - 190 * s), (cx + 230 * s, cy - 60 * s)], IVORY)
    g.tx((cx, cy - 92 * s), label, font(FONT_SANS, int(46 * s)), GREEN_D)
    g.rc([cx - 230 * s, cy - 50 * s, cx + 230 * s, cy - 20 * s], IVORY)
    for i in range(5):
        x = cx - 190 * s + i * 95 * s
        g.rc([x - 22 * s, cy - 15 * s, x + 22 * s, cy + 140 * s], SAGE)
    g.rc([cx - 250 * s, cy + 140 * s, cx + 250 * s, cy + 170 * s], IVORY)
    g.rc([cx - 280 * s, cy + 170 * s, cx + 280 * s, cy + 200 * s], SAGE)


def ebt_card(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask); w, h = 280 * s, 175 * s
    g.rr([cx - w, cy - h, cx + w, cy + h], int(36 * s), GREEN_L, GOLD, int(7 * s))
    g.rr([cx - w + 50 * s, cy - h + 70 * s, cx - w + 150 * s, cy - h + 140 * s], int(10 * s), GOLD)
    g.tx((cx + w - 40 * s, cy - h + 62 * s), "EBT", font(FONT_SANS, int(66 * s)), GOLD, "rm")
    g.tx((cx - w + 50 * s, cy + 60 * s), "SNAP BENEFITS", font(FONT_SANS, int(34 * s)), IVORY, "lm")
    for i in range(4):
        g.el([cx - w + (50 + i * 62) * s, cy + 100 * s, cx - w + (74 + i * 62) * s, cy + 124 * s], SAGE)


def calendar(rgb, mask, cx, cy, s=1.0, label="1"):
    g = D(rgb, mask)
    g.rr([cx - 110 * s, cy - 120 * s, cx + 110 * s, cy + 120 * s], int(18 * s), IVORY)
    g.rr([cx - 110 * s, cy - 120 * s, cx + 110 * s, cy - 60 * s], int(18 * s), RED); g.rc([cx - 110 * s, cy - 80 * s, cx + 110 * s, cy - 60 * s], RED)
    g.tx((cx, cy + 15 * s), label, font(FONT_SERIF, int(110 * s)), GREEN_D)
    for x in (-60, 60): g.rr([cx + (x - 8) * s, cy - 140 * s, cx + (x + 8) * s, cy - 95 * s], 6, SAGE_D)


def house(rgb, mask, cx, cy, s=1.0, roof=RED, body=IVORY):
    g = D(rgb, mask)
    g.rc([cx - 130 * s, cy - 40 * s, cx + 130 * s, cy + 130 * s], body)
    g.pg([(cx - 165 * s, cy - 35 * s), (cx, cy - 170 * s), (cx + 165 * s, cy - 35 * s)], roof)
    g.rr([cx - 28 * s, cy + 30 * s, cx + 28 * s, cy + 130 * s], 8, BROWN)
    for x in (-85, 57): g.rr([cx + x * s, cy - 10 * s, cx + (x + 38) * s, cy + 40 * s], 6, SAGE_D)
    g.rc([cx + 70 * s, cy - 150 * s, cx + 100 * s, cy - 80 * s], roof)


def piggy(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.el([cx - 120 * s, cy - 80 * s, cx + 120 * s, cy + 80 * s], PINK)
    g.pg([(cx + 60 * s, cy - 70 * s), (cx + 100 * s, cy - 120 * s), (cx + 110 * s, cy - 50 * s)], PINK)
    g.rr([cx + 95 * s, cy - 20 * s, cx + 150 * s, cy + 25 * s], int(14 * s), (240, 170, 160))
    g.el([cx + 75 * s, cy - 40 * s, cx + 90 * s, cy - 25 * s], GREEN_D)
    for x in (-70, 40): g.rr([cx + x * s, cy + 60 * s, cx + (x + 36) * s, cy + 115 * s], 8, PINK)
    g.rr([cx - 35 * s, cy - 78 * s, cx + 25 * s, cy - 66 * s], 5, GREEN_D)


def wallet(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 140 * s, cy - 90 * s, cx + 140 * s, cy + 90 * s], int(24 * s), BROWN)
    g.rr([cx - 140 * s, cy - 60 * s, cx + 140 * s, cy - 30 * s], 6, (120, 80, 45))
    g.rr([cx + 50 * s, cy - 20 * s, cx + 160 * s, cy + 40 * s], int(16 * s), GOLD)
    g.el([cx + 80 * s, cy - 2 * s, cx + 104 * s, cy + 22 * s], GREEN_D)


def cake(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 170 * s, cy + 20 * s, cx + 170 * s, cy + 150 * s], int(20 * s), SAGE)
    g.rr([cx - 120 * s, cy - 70 * s, cx + 120 * s, cy + 30 * s], int(18 * s), IVORY)
    g.rr([cx - 170 * s, cy + 15 * s, cx + 170 * s, cy + 45 * s], int(14 * s), GOLD)
    g.rr([cx - 120 * s, cy - 75 * s, cx + 120 * s, cy - 50 * s], int(12 * s), RED)
    for x in (-75, -25, 25, 75):
        g.rr([cx + (x - 7) * s, cy - 125 * s, cx + (x + 7) * s, cy - 72 * s], 4, GOLD)


def flame(img, cx, cy, t, s=1.0):
    k = 1 + .15 * math.sin(t * 14 + cx)
    lay = new_layer(); g = D(*lay)
    g.el([cx - 10 * s * k, cy - 34 * s * k, cx + 10 * s * k, cy + 4 * s], (255, 190, 70))
    alpha_layer(img, lay, .95)


def tick(rgb, mask, cx, cy, s=1.0, col=SAGE):
    g = D(rgb, mask); g.ln([(cx - 40 * s, cy), (cx - 10 * s, cy + 32 * s), (cx + 45 * s, cy - 36 * s)], col, int(16 * s))


def xmark(rgb, mask, cx, cy, s=1.0, col=RED):
    g = D(rgb, mask); g.ln([(cx - 36 * s, cy - 36 * s), (cx + 36 * s, cy + 36 * s)], col, int(16 * s)); g.ln([(cx - 36 * s, cy + 36 * s), (cx + 36 * s, cy - 36 * s)], col, int(16 * s))


def coupon(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 130 * s, cy - 70 * s, cx + 130 * s, cy + 70 * s], 6, IVORY, outline=SAGE_D, w=4)
    for i in range(9): g.ln([(cx - 120 * s + i * 30 * s, cy - 70 * s), (cx - 120 * s + i * 30 * s, cy - 60 * s)], SAGE_D, 4)
    g.tx((cx, cy - 12 * s), "COUPON", font(FONT_SANS, int(40 * s)), GREEN_D); g.tx((cx, cy + 32 * s), "CLIP & SAVE", font(FONT_SANS_M, int(26 * s)), RED)


def stamp(img, cx, cy, p, text="WRONG", col=RED, angle=-10, size=64):
    if p <= 0: return
    pop(img, lambda r, m: (D(r, m).rr([cx - max(190, len(text) * size * .36), cy - 50, cx + max(190, len(text) * size * .36), cy + 50], 14, None, col, 8), D(r, m).tx((cx, cy), text, font(FONT_SANS, size), col)),
        1.5 - .5 * ease_back(p), a=ease(seg(p, 0, .3)), angle=angle)


def gate(rgb, mask, cx, cy, s=1.0, col=SAGE, open_=0.0):
    g = D(rgb, mask)
    g.rr([cx - 150 * s, cy - 140 * s, cx - 120 * s, cy + 150 * s], 8, col); g.rr([cx + 120 * s, cy - 140 * s, cx + 150 * s, cy + 150 * s], 8, col)
    g.rr([cx - 150 * s, cy - 150 * s, cx + 150 * s, cy - 110 * s], 10, col)
    for i in range(5):
        x = cx - 100 * s + i * 50 * s
        g.rr([x - 6 * s, cy - 100 * s + open_ * -190 * s, x + 6 * s, cy + 100 * s + open_ * -190 * s], 4, col)


def paycheck(rgb, mask, cx, cy, s=1.0, amt="$1,800"):
    g = D(rgb, mask)
    g.rr([cx - 220 * s, cy - 110 * s, cx + 220 * s, cy + 110 * s], int(14 * s), IVORY, outline=SAGE_D, w=5)
    g.tx((cx - 190 * s, cy - 70 * s), "SOCIAL SECURITY", font(FONT_SANS, int(26 * s)), SAGE_D, "lm")
    g.tx((cx, cy + 10 * s), amt, font(FONT_SERIF, int(96 * s)), GREEN_D)
    g.ln([(cx - 190 * s, cy + 80 * s), (cx + 40 * s, cy + 80 * s)], SAGE_D, 4)


def fade_group(img, fn, t, a):
    if a <= 0: return
    tmp = img.copy(); fn(tmp, t)
    img.paste(Image.blend(img, tmp, min(1.0, a)))


def title(img, t, s):
    spaced(img, s, W // 2, 90, 44, a=ease(seg(t, 0, .5)))


# ================== BLOCCO 2: cos'e' snap (609)
def b2a(img, t):
    title(img, t, "WHAT IS SNAP?")
    show(img, t, .3, lambda r, m: building(r, m, 560, 540, 1.5), .8)
    txt_in(img, t, 1.2, (560, 960), "FEDERAL PROGRAM · U S D A", 48, IVORY)
    ar = ease(seg(t, 2.4, .6))
    if ar > 0:
        lay = new_layer(); g = D(*lay)
        g.pg([(950, 520), (1090, 520), (1090, 480), (1180, 560), (1090, 640), (1090, 600), (950, 600)], GOLD); alpha_layer(img, lay, ar)
    def state(r, m):
        g = D(r, m)
        g.rr([1240, 250, 1800, 780], 40, CARD, SAGE_D, 6)
        g.pg([(1330, 360), (1480, 330), (1600, 360), (1700, 420), (1680, 560), (1590, 690), (1450, 700), (1360, 620), (1320, 480)], SAGE)
        g.el([1500, 440, 1560, 500], RED); g.pg([(1500, 480), (1560, 480), (1530, 560)], RED); g.el([1518, 458, 1542, 482], IVORY)
    show(img, t, 3.0, state, .7)
    txt_in(img, t, 3.8, (1520, 860), "RUN BY YOUR STATE", 50, GOLD)
    show(img, t, 5.2, lambda r, m: grocery_bag(r, m, 1090, 830, .8), .6, dy=math.sin(t * 2.4) * 6)


def b2b(img, t):
    title(img, t, "YOUR E B T CARD")
    def part1(img, t):
        show(img, t, .3, lambda r, m: calendar(r, m, 330, 440, 1.5, "1st"), .7)
        txt_in(img, t, 1.0, (330, 740), "EVERY MONTH", 52, IVORY)
        for k in range(6):
            pp = seg(t, 1.6 + k * .35, 1.2)
            if 0 < pp < 1:
                pop(img, lambda r, m: coin(r, m, 330, 440, 36), 1.0, a=min(1, pp * 5) * (1 - ease(seg(pp, .8, .2))), dx=(780) * ease(pp), dy=-40 * math.sin(pp * math.pi))
        show(img, t, 1.4, lambda r, m: ebt_card(r, m, 1090, 440, 1.1), .7, angle=-5, dy=math.sin(t * 2) * 6)
        txt_in(img, t, 3.2, (1090, 740), "WORKS LIKE A DEBIT CARD", 48, GOLD)
    fade_group(img, part1, t, 1 - ease(seg(t, 4.6, .5)))
    st = 5.2
    if t > st:
        show(img, t, st, lambda r, m: (register(r, m, 520, 560), person(r, m, 1000, 500, 1.6)), .6)
        pop(img, lambda r, m: ebt_card(r, m, 720, 470, .3), 1.0, a=ease(seg(t, st + .8, .4)), dx=-60 * math.sin(seg(t, st + .8, 1.5) * 3))
        show(img, t, st + 1.8, lambda r, m: grocery_bag(r, m, 1500, 540, .9), .5)
        txt_in(img, t, st + 2.4, (W // 2, 930), "AUTHORIZED GROCERY STORES", 60, GOLD)


def b2c(img, t):
    title(img, t, "THAT'S IT")
    show(img, t, .3, lambda r, m: coupon(r, m, 560, 480, 1.6), .6, angle=-6)
    stamp(img, 560, 680, seg(t, 1.0, .6), "NO PAPER", RED, -8, 60)
    xs = ease(seg(t, 1.4, .4))
    if xs > 0:
        lay = new_layer(); xmark(lay[0], lay[1], 760, 340, 1.6); alpha_layer(img, lay, xs)
    show(img, t, 2.2, lambda r, m: ebt_card(r, m, 1340, 470, 1.1), .7, angle=4, dy=math.sin(t * 2.2) * 6)
    tk = ease_back(seg(t, 3.0, .5))
    if tk > 0:
        pop(img, lambda r, m: (D(r, m).el([1620, 190, 1740, 310], SAGE), tick(r, m, 1680, 250, 1.1, GREEN_D)), tk, a=ease(seg(t, 3.0, .2)))
    txt_in(img, t, 3.4, (W // 2, 900), "JUST A CARD", 100, GOLD)


# ================== BLOCCO 3: perche' non fanno domanda (675)
def b3a(img, t):
    title(img, t, "WHY DO SENIORS NEVER APPLY?")
    show(img, t, .3, lambda r, m: person(r, m, 520, 640, 2.2), .7)
    show(img, t, 1.2, lambda r, m: bubble(r, m, 1000, 330, 560, 250, "left") or D(r, m).tx((1000, 340), "?", font(FONT_SERIF, 200), GOLD), .6)
    for k, (x, y, sz) in enumerate(((1450, 250, 130), (1620, 470, 170), (1380, 600, 110))):
        show(img, t, 2.0 + k * .5, lambda r, m, x=x, y=y, sz=sz: D(r, m).tx((x, y), "?", font(FONT_SERIF, sz), IVORY), .5, dy=math.sin(t * 2 + k) * 8)
    txt_in(img, t, 3.6, (W // 2, 950), "THREE REASONS", 80, GOLD)


def b3b(img, t):
    title(img, t, "THREE REASONS")
    items = [(380, "ONE", "I MAKE TOO MUCH", lambda r, m, cx, cy: wallet(r, m, cx, cy, 1.0)),
             (960, "TWO", "I OWN MY HOME", lambda r, m, cx, cy: house(r, m, cx, cy + 10, 1.0)),
             (1540, "THREE", "I HAVE SOME SAVINGS", lambda r, m, cx, cy: piggy(r, m, cx, cy, 1.0))]
    for i, (cx, tag, lab, icon) in enumerate(items):
        st = .4 + i * 1.6
        p = ease_back(seg(t, st, .6)); a = ease(seg(t, st, .4))
        if a <= 0: continue
        lay = new_layer(); rgb, mask = lay; off = 80 * (1 - p)
        box = [cx - 280, 200 + off, cx + 280, 880 + off]
        D(rgb, mask).rr(box, 36, CARD, SAGE_D, 4)
        D(rgb, mask).rr([cx - 280, 200 + off, cx + 280, 280 + off], 36, GOLD); D(rgb, mask).rc([cx - 280, 240 + off, cx + 280, 280 + off], GOLD)
        D(rgb, mask).tx((cx, 242 + off), tag, font(FONT_SANS, 46), GREEN_D)
        icon(rgb, mask, cx, 520 + off)
        D(rgb, mask).tx((cx, 790 + off), lab, font(FONT_SANS, 38), IVORY)
        alpha_layer(img, lay, a)
        stamp(img, cx, 380, seg(t, st + 1.0, .5), "WORRY?", RED, -9, 54)


def b3c(img, t):
    title(img, t, "AFTER SIXTY THE RULES CHANGE")
    show(img, t, .3, lambda r, m: price_tag(r, m, 560, 330, "60+", 520, 300), .8, angle=-5, dy=math.sin(t * 2) * 6)
    # tre pietre di un sentiero
    for i, (x, lab) in enumerate(((1000, "1"), (1280, "2"), (1560, "3"))):
        st = 1.6 + i * 1.1
        show(img, t, st, lambda r, m, x=x, lab=lab: (D(r, m).el([x - 100, 300, x + 100, 500], GOLD), D(r, m).tx((x, 400), lab, font(FONT_SERIF, 130), GREEN_D)), .5)
        if i < 2:
            ar = ease(seg(t, st + .5, .4))
            if ar > 0:
                lay = new_layer(); D(*lay).pg([(x + 115, 385), (x + 165, 400), (x + 115, 415)], SAGE); alpha_layer(img, lay, ar)
    show(img, t, 5.2, lambda r, m: person(r, m, 560, 830, 1.6), .6)
    sx = 560 + 0
    pw = ease(seg(t, 5.2, 2.0))
    txt_in(img, t, 6.4, (1280, 700), "LET'S GO ONE BY ONE", 66, IVORY)
    txt_in(img, t, 7.4, (1280, 800), "DIFFERENT RULES", 60, GOLD)


# ================== BLOCCO 4: regola 1, 60 anni (580)
def b4a(img, t):
    title(img, t, "RULE NUMBER ONE")
    show(img, t, .3, lambda r, m: cake(r, m, 560, 560, 1.8), .8)
    for x in (-75, -25, 25, 75):
        if t > .9: flame(img, 560 + x * 1.8, 560 - 132 * 1.8, t, 1.6)
    show(img, t, 1.0, lambda r, m: D(r, m).tx((560, 520), "60", font(FONT_SERIF, 150), GREEN_D), .5)
    show(img, t, 2.0, lambda r, m: D(r, m).tx((1300, 330), "ELDERLY AT", font(FONT_SANS, 70), IVORY), .5)
    show(img, t, 2.5, lambda r, m: D(r, m).tx((1300, 560), "60", font(FONT_SERIF, 330), GOLD), .7)
    show(img, t, 4.4, lambda r, m: D(r, m).tx((1190, 840), "NOT 65", font(FONT_SANS, 110), RED), .5)
    g = ease(seg(t, 5.0, .5))
    if g > 0:
        ImageDraw.Draw(img).line([960, 850, 960 + 450 * g, 850], fill=RED, width=14)


def b4b(img, t):
    title(img, t, "THE WHOLE HOUSEHOLD")
    show(img, t, .3, lambda r, m: house(r, m, 560, 500, 2.2), .8)
    show(img, t, 1.0, lambda r, m: [person(r, m, 480 + i * 150, 930, .6) for i in range(3)], .6)
    p60 = ease_back(seg(t, 2.2, .6))
    pop(img, lambda r, m: price_tag(r, m, 880, 920, "60", 190, 110), p60, a=ease(seg(t, 2.2, .3)), angle=-8)
    gl = ease(seg(t, 3.2, .8))
    if gl > 0:
        lay = new_layer(); D(*lay).el([180, 150, 940, 1010], None, GOLD, 10); alpha_layer(img, lay, gl * (.5 + .4 * math.sin(t * 4)))
    show(img, t, 3.4, lambda r, m: (D(r, m).rr([1080, 330, 1790, 730], 40, CARD, GOLD, 6), D(r, m).tx((1435, 430), "SPECIAL", font(FONT_SANS, 90), GOLD), D(r, m).tx((1435, 540), "RULES", font(FONT_SANS, 120), IVORY), D(r, m).tx((1435, 650), "FOR EVERYONE", font(FONT_SANS_M, 46), SAGE)), .7)


def b4c(img, t):
    title(img, t, "YOU SKIP THE GROSS INCOME TEST")
    # percorso: cancello 1 saltato, cancello 2
    show(img, t, .3, lambda r, m: (gate(r, m, 600, 520, 1.5, RED), D(r, m).tx((600, 860), "GROSS INCOME TEST", font(FONT_SANS, 44), IVORY)), .7)
    show(img, t, 1.0, lambda r, m: gate(r, m, 1320, 520, 1.5, SAGE), .7)
    txt_in(img, t, 1.4, (1320, 860), "NET INCOME TEST", 44, IVORY)
    # persona che salta il primo cancello
    pp = ease(seg(t, 2.4, 2.6))
    x = 250 + 1000 * pp; y = 690 - 330 * math.sin(min(1, seg(t, 2.4, 1.6)) * math.pi) * (1 if seg(t, 2.4, 1.6) < 1 else 0)
    pop(img, lambda r, m: person(r, m, x, y, .8), 1.0, a=ease(seg(t, 2.2, .3)))
    xm = ease_back(seg(t, 3.2, .5))
    if xm > 0:
        pop(img, lambda r, m: xmark(r, m, 600, 330, 1.8), xm, a=ease(seg(t, 3.2, .2)))
    txt_in(img, t, 5.4, (W // 2, 975), "ONLY THE NET TEST COUNTS", 56, GOLD)


# ================== BLOCCO 5: lordo vs netto (638)
def b5a(img, t):
    title(img, t, "TEST 1 · GROSS INCOME")
    show(img, t, .3, lambda r, m: paycheck(r, m, 560, 480, 1.5, "$1,800"), .7, angle=-3, dy=math.sin(t * 2) * 5)
    txt_in(img, t, 1.2, (560, 790), "EVERYTHING YOU RECEIVE", 54, IVORY)
    txt_in(img, t, 1.9, (560, 860), "BEFORE ANY DEDUCTIONS", 54, GOLD)
    for i, (dx, dy) in enumerate(((1250, 330), (1480, 430), (1350, 590), (1620, 330), (1600, 600))):
        show(img, t, 2.6 + i * .35, lambda r, m, dx=dx, dy=dy: banknote(r, m, dx, dy, 330, 160, "GROSS", ""), .5, angle=(-1) ** i * 5, dy=math.sin(t * 2 + i) * 6)
    txt_in(img, t, 5.0, (1450, 800), "ALL OF IT COUNTS", 56, IVORY)


def scissors(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.ln([(cx - 70 * s, cy - 70 * s), (cx + 70 * s, cy + 70 * s)], IVORY, int(14 * s)); g.ln([(cx - 70 * s, cy + 70 * s), (cx + 70 * s, cy - 70 * s)], IVORY, int(14 * s))
    for y in (-1, 1): g.el([cx - 120 * s, cy + y * 85 * s - 28 * s, cx - 64 * s, cy + y * 85 * s + 28 * s], None, GOLD, int(10 * s))


def b5b(img, t):
    title(img, t, "TEST 2 · NET INCOME")
    show(img, t, .3, lambda r, m: paycheck(r, m, 400, 500, 1.1, "GROSS"), .6)
    ar1 = ease(seg(t, 1.2, .5))
    if ar1 > 0:
        lay = new_layer(); D(*lay).pg([(640, 480), (720, 480), (720, 450), (790, 510), (720, 570), (720, 540), (640, 540)], GOLD); alpha_layer(img, lay, ar1)
    show(img, t, 1.8, lambda r, m: (scissors(r, m, 960, 500, 1.3), D(r, m).tx((960, 700), "DEDUCTIONS", font(FONT_SANS, 46), GOLD)), .6, angle=0)
    ar2 = ease(seg(t, 3.0, .5))
    if ar2 > 0:
        lay = new_layer(); D(*lay).pg([(1130, 480), (1210, 480), (1210, 450), (1280, 510), (1210, 570), (1210, 540), (1130, 540)], GOLD); alpha_layer(img, lay, ar2)
    show(img, t, 3.6, lambda r, m: paycheck(r, m, 1530, 500, 1.1, "NET"), .6, angle=3)
    txt_in(img, t, 4.6, (W // 2, 930), "WHAT'S LEFT AFTER DEDUCTIONS", 66, IVORY)


def b5c(img, t):
    title(img, t, "AGE SIXTY OR OLDER")
    show(img, t, .3, lambda r, m: (gate(r, m, 560, 500, 1.5, RED), D(r, m).tx((560, 840), "GROSS TEST", font(FONT_SANS, 50), IVORY)), .7)
    xm = ease_back(seg(t, 1.3, .5))
    if xm > 0:
        pop(img, lambda r, m: xmark(r, m, 560, 300, 1.8), xm, a=ease(seg(t, 1.3, .2)))
    stamp(img, 560, 940, seg(t, 1.8, .5), "SKIPPED", RED, -6, 52)
    show(img, t, 2.8, lambda r, m: (gate(r, m, 1380, 500, 1.5, SAGE), D(r, m).tx((1380, 840), "NET TEST", font(FONT_SANS, 50), IVORY)), .7)
    pp = ease(seg(t, 3.6, 2.4))
    pop(img, lambda r, m: person(r, m, 900 + 480 * pp, 660, .8), 1.0, a=ease(seg(t, 3.4, .3)))
    show(img, t, 4.6, lambda r, m: price_tag(r, m, 1380, 290, "60+", 260, 130), .5, angle=-6)
    txt_in(img, t, 6.4, (1380, 940), "ONLY THE SECOND ONE", 44, GOLD)


BLOCKS = {
    2: [("First, what is snap? It's a federal food program from the U S D A, run by your state.", b2a),
        ("If you qualify, your benefits load every month onto an E B T card. It works like a debit card, and you use it at authorized grocery stores.", b2b),
        ("That's it. No paper coupons, just a card.", b2c)],
    3: [("So why do so many seniors never apply? Three reasons.", b3a),
        ("One: I make too much. Two: I own my home. Three: I have some savings.", b3b),
        ("Here's the surprise. For people over sixty, all three of those worries rest on rules that work differently. Let's go through them, one by one.", b3c)],
    4: [("Rule number one. In snap, you count as elderly at age sixty. Not sixty five. Sixty.", b4a),
        ("And the moment someone in your household turns sixty, the whole household gets special rules.", b4b),
        ("This is the first one, and it's big: you skip the gross income test.", b4c)],
    5: [("Here's what that means. Most households must pass two tests. The first is gross income, which is everything you receive before any deductions.", b5a),
        ("The second is net income, which is what's left after deductions.", b5b),
        ("But a household with someone sixty or older only has to pass the second one, the net test.", b5c)],
}


def split_frames(block):
    total = BLOCK_FRAMES[block]; w = [len(s) for s, _ in BLOCKS[block]]
    fr = [round(total * x / sum(w)) for x in w]; fr[-1] = total - sum(fr[:-1])
    return fr


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = split_frames(b)
    for i, ((s, fn), n) in enumerate(zip(BLOCKS[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide0{i}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
