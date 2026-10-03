"""Video lungo 2 (SNAP over 60) - blocchi 16-20. Fine blocco (fotogrammi, dalla timeline): 9632 10124 10702 11373 12037.
Uso: OUT=cartella SA_TMP=/tmp/f python3 long2_b16_20.py <blocco 11-20> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import long2_b02_05 as L
from long2_b11_15 import *

ENDS2 = [9632, 10124, 10702, 11373, 12037]
FR3 = {16 + i: e - (9106 if i == 0 else ENDS2[i - 1]) for i, e in enumerate(ENDS2)}
L.BLOCK_FRAMES.update(FR3)


def barpair(img, t, st, x0, y, tw, parts, vmax, h=90, dur=1.2):
    """barra a segmenti [(valore, colore)] che cresce"""
    p = ease(seg(t, st, dur))
    if p <= 0: return
    lay = new_layer(); g = D(*lay); x = x0
    for val, col in parts:
        w = tw * val / vmax * p
        g.rr([x, y - h / 2, x + w, y + h / 2], 18, col); x += w
    alpha_layer(img, lay, min(1, p * 3))


# ============ BLOCCO 16: spesa abitativa e reddito netto (526)
def b16a(img, t):
    title(img, t, "STEP THREE · SHELTER")
    show(img, t, .3, lambda r, m: price_tag(r, m, 420, 290, "STEP 3", 560, 220), .8, angle=-4)
    show(img, t, 1.0, lambda r, m: house(r, m, 420, 680, 1.4), .7)
    for i, (ic, lab) in enumerate(((key, "RENT"), (bulb, "UTILITIES"))):
        show(img, t, 1.8 + i * .7, lambda r, m, ic=ic, lab=lab, i=i: (D(r, m).rr([830 + i * 340, 230, 1130 + i * 340, 540], 30, CARD, SAGE_D, 4), ic(r, m, 980 + i * 340, 370, 1.0), D(r, m).tx((980 + i * 340, 490), lab, font(FONT_SANS, 34), IVORY)), .6)
    show(img, t, 3.6, lambda r, m: D(r, m).tx((1150, 730), "$1,100", font(FONT_SERIF, 230), GOLD), .8)
    txt_in(img, t, 4.4, (1150, 900), "ADDED UP A MONTH", 50, IVORY)


def b16b(img, t):
    title(img, t, "HALF OF HER ADJUSTED INCOME")
    x0, tw, vmax = 220, 1480, 1400
    txt_in(img, t, .3, (x0 + 250, 260), "ADJUSTED INCOME  $1,383", 40, SAGE)
    barpair(img, t, .6, x0, 340, tw, [(1383, SAGE_D)], vmax, 80)
    mk = ease(seg(t, 1.8, .5))
    if mk > 0:
        mx = x0 + tw * 691.5 / vmax
        ImageDraw.Draw(img).line([mx, 270, mx, 640], fill=GOLD, width=8)
        txt_in(img, t, 2.0, (mx + 120, 225), "HALF  ≈ $691", 36, GOLD)
    txt_in(img, t, 3.0, (x0 + 290, 540), "SHELTER COSTS  $1,100", 40, SAGE)
    barpair(img, t, 3.2, x0, 620, tw, [(691.5, SAGE_D), (408.5, GOLD)], vmax, 80, 1.4)
    txt_in(img, t, 4.8, (x0 + tw * (691.5 + 204) / vmax, 740), "EXTRA ≈ $408", 56, GOLD)
    txt_in(img, t, 5.6, (W // 2, 900), "THE EXTRA COMES OFF", 70, IVORY)


def b16c(img, t):
    title(img, t, "HER NET INCOME")
    ledger(img, t, [(.6, "ADJUSTED INCOME", "$1,383", IVORY), (1.8, "− SHELTER EXTRA", "$408.50", RED), (3.2, "= NET INCOME", "$974.50", GOLD)], 150, 190)
    show(img, t, 3.6, lambda r, m: D(r, m).tx((1450, 480), "$974.50", font(FONT_SERIF, 190), GOLD), .8)
    txt_in(img, t, 4.4, (1450, 650), "NET INCOME PER MONTH", 48, IVORY)


# ============ BLOCCO 17: il test (492)
def b17a(img, t):
    title(img, t, "AND NOW THE TEST")
    x0, tw, vmax = 220, 1480, 1500
    txt_in(img, t, .3, (x0 + 260, 270), "NET LIMIT · ONE PERSON", 40, SAGE)
    barpair(img, t, .5, x0, 360, tw, [(1330, SAGE_D)], vmax, 80, 1.2)
    txt_in(img, t, 1.2, (x0 + tw * 1330 / vmax, 270), "$1,330", 70, IVORY)
    txt_in(img, t, 2.4, (x0 + 170, 540), "HER NET INCOME", 40, SAGE)
    barpair(img, t, 2.6, x0, 630, tw, [(974.5, GOLD)], vmax, 80, 1.4)
    txt_in(img, t, 3.6, (x0 + tw * 974.5 / vmax, 540), "$974.50", 70, GOLD)
    show(img, t, 4.8, lambda r, m: (D(r, m).el([W // 2 - 70, 790, W // 2 + 70, 930], SAGE), tick(r, m, W // 2, 862, 1.4, GREEN_D)), .6)


def b17b(img, t):
    title(img, t, "SHE PASSES")
    show(img, t, .3, lambda r, m: (gate(r, m, 560, 480, 1.5, RED), D(r, m).tx((560, 790), "GROSS $1,800", font(FONT_SANS, 46), IVORY)), .6)
    xm = ease_back(seg(t, 1.0, .5))
    if xm > 0: pop(img, lambda r, m: xmark(r, m, 560, 290, 1.6), xm, a=ease(seg(t, 1.0, .2)))
    txt_in(img, t, 1.4, (560, 860), "ABOVE THE LIMIT · DOESN'T MATTER", 34, SAGE, sans_m=True)
    op = ease(seg(t, 2.2, 1.2))
    show(img, t, 1.8, lambda r, m: gate(r, m, 1380, 480, 1.5, SAGE), .6)
    pp = ease(seg(t, 3.4, 2.2))
    pop(img, lambda r, m: person(r, m, 1020 + 360 * pp, 640, .8), 1.0, a=ease(seg(t, 3.2, .3)))
    txt_in(img, t, 2.2, (1380, 790), "NET $974.50", 46, GOLD)
    stamp(img, 1380, 900, seg(t, 5.0, .6), "APPROVED TEST", GOLD, -5, 54)


def b17c(img, t):
    title(img, t, "THE WOMAN WHO CLOSED THE PAGE")
    show(img, t, .3, lambda r, m: person(r, m, 420, 640, 2.2), .7)
    lid = ease(seg(t, 1.0, 1.0))
    show(img, t, .8, lambda r, m: laptop(r, m, 1180, 500, 1.5, 0.0), .5)
    pop(img, lambda r, m: (laptop(r, m, 1180, 500, 1.5, lid), D(r, m).tx((1180, 450), "SNAP", font(FONT_SANS, 90), GOLD) if lid > .9 else None), 1.0, a=ease(seg(t, 1.0, .3)))
    if t > 2.2:
        pop(img, lambda r, m: (D(r, m).el([1470, 190, 1590, 310], SAGE), tick(r, m, 1530, 250, 1.1, GREEN_D)), ease_back(seg(t, 2.2, .5)), a=ease(seg(t, 2.2, .2)))
    txt_in(img, t, 3.4, (1180, 800), "THE WHOLE REASON", 62, IVORY)
    txt_in(img, t, 4.0, (1180, 880), "THIS VIDEO EXISTS", 62, GOLD)


# ============ BLOCCO 18: la formula (578)
def b18a(img, t):
    title(img, t, "HOW MUCH WOULD SHE GET?")
    show(img, t, .3, lambda r, m: D(r, m).tx((960, 400), "HOW MUCH?", font(FONT_SERIF, 250), GOLD), .8)
    for k, (x, y) in enumerate(((330, 700), (620, 820), (960, 720), (1300, 830), (1590, 700))):
        show(img, t, 1.2 + k * .35, lambda r, m, x=x, y=y: coin(r, m, x, y, 60), .5, dy=math.sin(t * 2 + k) * 8)
    txt_in(img, t, 3.4, (W // 2, 960), "SNAP USES A SIMPLE FORMULA", 56, IVORY)


def b18b(img, t):
    title(img, t, "THE SNAP FORMULA")
    blocks = [(300, "NET INCOME", "× 30%", SAGE_D), (960, "ROUND UP", "", GOLD), (1620, "SUBTRACT FROM", "MAX", RED)]
    for i, (cx, l1, l2, col) in enumerate(blocks):
        st = .4 + i * 1.5
        show(img, t, st, lambda r, m, cx=cx, l1=l1, l2=l2, col=col: (D(r, m).rr([cx - 280, 300, cx + 280, 620], 36, col), D(r, m).tx((cx, 420), l1, font(FONT_SANS, 46), GREEN_D), D(r, m).tx((cx, 520), l2, font(FONT_SERIF, 90), GREEN_D) if l2 else None), .7)
        if i < 2:
            ar = ease(seg(t, st + .9, .4))
            if ar > 0:
                lay = new_layer(); x = cx + 300; D(*lay).pg([(x, 440), (x + 40, 440), (x + 40, 410), (x + 90, 460), (x + 40, 510), (x + 40, 480), (x, 480)], GOLD); alpha_layer(img, lay, ar)
    show(img, t, 5.0, lambda r, m: (D(r, m).rr([520, 740, 1400, 900], 30, CARD, GOLD, 6), D(r, m).tx((960, 820), "= YOUR MONTHLY SNAP", font(FONT_SANS, 56), GOLD)), .7)
    txt_in(img, t, 5.6, (W // 2, 970), "FOR YOUR HOUSEHOLD SIZE", 36, SAGE, sans_m=True)


def b18c(img, t):
    title(img, t, "MAXIMUM MONTHLY BENEFIT")
    cards = [(520, 1, "ONE PERSON", 306), (1400, 2, "TWO PEOPLE", 562)]
    for i, (cx, n, lab, val) in enumerate(cards):
        st = .4 + i * 2.0
        show(img, t, st, lambda r, m, cx=cx, n=n, lab=lab: (D(r, m).rr([cx - 330, 220, cx + 330, 880], 40, CARD, GOLD, 6), [person(r, m, cx - 70 + k * 140 - (n - 1) * 70 + 0, 440, 1.0 if n == 1 else .9) for k in range(n)], D(r, m).tx((cx, 790), lab, font(FONT_SANS, 46), IVORY)), .7)
        counter(img, t, st + .8, (cx - 190, 640), val, 130, GOLD, 1.4)


# ============ BLOCCO 19: il calcolo per lei (671)
def b19a(img, t):
    title(img, t, "HER BENEFIT")
    ledger(img, t, [(.6, "NET INCOME", "$974.50", IVORY), (2.0, "× 30%", "$292.35", SAGE), (3.6, "ROUNDED UP", "$293", GOLD)], 150, 190)
    ledger(img, t, [(6.0, "MAXIMUM", "$306", IVORY), (7.4, "− 30% OF NET", "$293", RED), (9.0, "= HER SNAP", "$13", GOLD)], 1110, 190)


def b19b(img, t):
    title(img, t, "THIRTEEN DOLLARS")
    show(img, t, .3, lambda r, m: D(r, m).tx((960, 430), "$13", font(FONT_SERIF, 420), GOLD), .9)
    txt_in(img, t, 1.4, (960, 720), "A MONTH", 80, IVORY)
    txt_in(img, t, 2.4, (960, 840), "NOT LIFE CHANGING · AN HONEST NUMBER", 46, SAGE)


def b19c(img, t):
    title(img, t, "EVERY DEDUCTION YOU DOCUMENT")
    labels = ["STANDARD", "+ MEDICAL", "+ SHELTER", "+ PROOF"]
    for i, lab in enumerate(labels):
        st = .5 + i * 1.3
        hh = 120 + i * 120
        p = ease(seg(t, st, .9))
        if p <= 0: continue
        lay = new_layer(); g = D(*lay); cx = 330 + i * 420
        g.rr([cx - 130, 840 - hh * p, cx + 130, 840], 20, [SAGE_D, SAGE, GOLD, GOLD][i]); g.tx((cx, 890), lab, font(FONT_SANS, 34), IVORY)
        alpha_layer(img, lay, min(1, p * 3))
    ar = ease(seg(t, 4.8, .8))
    if ar > 0:
        lay = new_layer(); D(*lay).pg([(1660, 330), (1760, 330), (1760, 230), (1860, 330), (1760, 330)], GOLD) if False else None
    txt_in(img, t, 5.0, (W // 2, 230), "THE NUMBER GOES UP", 80, GOLD)


# ============ BLOCCO 20: esempio USDA (664)
def b20a(img, t):
    title(img, t, "U S D A'S OWN EXAMPLE")
    show(img, t, .3, lambda r, m: building(r, m, 560, 480, 1.3), .8)
    txt_in(img, t, 1.2, (560, 860), "STRAIGHT FROM THEIR PAGE", 48, GOLD)
    show(img, t, 2.4, lambda r, m: (person(r, m, 1230, 500, 1.6), person(r, m, 1450, 500, 1.6)), .6)
    txt_in(img, t, 3.4, (1340, 740), "A COUPLE · BOTH ELDERLY", 44, IVORY)
    show(img, t, 4.6, lambda r, m: (D(r, m).rr([1000, 800, 1480, 920], 26, CARD, GOLD, 5), D(r, m).tx((1240, 860), "$1,200 INCOME", font(FONT_SANS, 44), GOLD)), .5)
    show(img, t, 6.0, lambda r, m: (D(r, m).rr([1510, 800, 1820, 920], 26, CARD, RED, 5), D(r, m).tx((1665, 860), "+$300 MEDICAL", font(FONT_SANS, 34), RED)), .5)


def b20b(img, t):
    title(img, t, "THEIR NET INCOME")
    ledger(img, t, [(.6, "INCOME", "$1,200", IVORY), (1.6, "− STANDARD", "$217", RED), (2.6, "− MEDICAL", "$300", RED), (3.6, "− SHELTER EXTRA", "$258.50", RED)], 150, 150)
    show(img, t, 5.0, lambda r, m: D(r, m).tx((1450, 380), "$424.50", font(FONT_SERIF, 200), GOLD), .8)
    txt_in(img, t, 5.8, (1450, 560), "NET INCOME", 56, IVORY)


def b20c(img, t):
    title(img, t, "THE POWER OF THE MEDICAL DEDUCTION")
    show(img, t, .3, lambda r, m: cross(r, m, 330, 420, 150), .8)
    show(img, t, 1.0, lambda r, m: D(r, m).tx((1050, 330), "$562 − $128", font(FONT_SANS, 90), IVORY), .6)
    show(img, t, 3.0, lambda r, m: D(r, m).tx((1050, 600), "$434", font(FONT_SERIF, 330), GOLD), .9)
    txt_in(img, t, 4.0, (1050, 830), "A MONTH FOR THE COUPLE", 56, IVORY)
    txt_in(img, t, 5.0, (330, 640), "MEDICAL", 50, GOLD)


L.BLOCKS.update({
    16: [("Step three: shelter. Her rent and utilities add up to eleven hundred dollars.", b16a),
         ("Half of her adjusted income is about six ninety one. The extra, about four hundred eight, comes off.", b16b),
         ("Her net income: nine hundred seventy four dollars and fifty cents.", b16c)],
    17: [("And now the test. The net limit for one person is thirteen thirty. She's at nine seventy four.", b17a),
         ("She passes, even though her gross was above the limit.", b17b),
         ("This is the woman who closed the page. That's the whole reason this video exists.", b17c)],
    18: [("How much would she get? Snap uses a simple formula.", b18a),
         ("Multiply your net income by thirty percent, round up, and subtract that from the maximum benefit for your household size.", b18b),
         ("For one person the maximum is three hundred six dollars a month. For two people, five sixty two.", b18c)],
    19: [("For her, thirty percent of nine seventy four fifty is two ninety three, rounded up. Three oh six minus two ninety three equals thirteen dollars.", b19a),
         ("Thirteen dollars. I won't pretend that's life changing.", b19b),
         ("But look what happens at lower incomes, or with higher medical bills. Every deduction you document pushes the number up.", b19c)],
    20: [("Here's the U S D A's own example, straight from their page. A couple, both elderly, with twelve hundred dollars a month in income and three hundred dollars in extra medical costs.", b20a),
         ("Their net income comes out to four twenty four fifty.", b20b),
         ("Their benefit: four hundred thirty four dollars a month. That's the power of the medical deduction.", b20c)],
})


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = L.split_frames(b)
    for i, ((s, fn), n) in enumerate(zip(L.BLOCKS[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide0{i}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
