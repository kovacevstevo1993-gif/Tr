"""Video lungo 2 (SNAP over 60) - blocchi 11-15. Fine blocco (fotogrammi, dalla timeline): 7098 7722 8220 8642 9106.
Uso: OUT=cartella SA_TMP=/tmp/f python3 long2_b11_15.py <blocco 11-15> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import long2_b02_05 as L
from long2_b06_10 import *

FR2 = {11: 7098 - 6586, 12: 7722 - 7098, 13: 8220 - 7722, 14: 8642 - 8220, 15: 9106 - 8642}
L.BLOCK_FRAMES.update(FR2)


def bulb(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.el([cx - 55 * s, cy - 90 * s, cx + 55 * s, cy + 20 * s], GOLD)
    g.rr([cx - 28 * s, cy + 10 * s, cx + 28 * s, cy + 70 * s], int(8 * s), IVORY)
    for y in (30, 48): g.ln([(cx - 24 * s, cy + y * s), (cx + 24 * s, cy + y * s)], SAGE_D, int(5 * s))


def drop(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.pg([(cx, cy - 100 * s), (cx + 60 * s, cy - 10 * s), (cx - 60 * s, cy - 10 * s)], (110, 190, 230))
    g.el([cx - 60 * s, cy - 40 * s, cx + 60 * s, cy + 80 * s], (110, 190, 230))


def flame_icon(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.pg([(cx, cy - 100 * s), (cx + 55 * s, cy), (cx - 55 * s, cy)], RED)
    g.el([cx - 55 * s, cy - 40 * s, cx + 55 * s, cy + 70 * s], RED)
    g.el([cx - 28 * s, cy - 0 * s, cx + 28 * s, cy + 62 * s], GOLD)


def phone(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 45 * s, cy - 85 * s, cx + 45 * s, cy + 85 * s], int(16 * s), IVORY)
    g.rr([cx - 34 * s, cy - 65 * s, cx + 34 * s, cy + 45 * s], int(8 * s), GREEN_D)
    g.el([cx - 10 * s, cy + 52 * s, cx + 10 * s, cy + 72 * s], SAGE_D)


def key(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.el([cx - 70 * s, cy - 40 * s, cx + 10 * s, cy + 40 * s], None, GOLD, int(16 * s))
    g.ln([(cx + 10 * s, cy), (cx + 80 * s, cy)], GOLD, int(16 * s)); g.ln([(cx + 55 * s, cy), (cx + 55 * s, cy + 36 * s)], GOLD, int(14 * s)); g.ln([(cx + 78 * s, cy), (cx + 78 * s, cy + 28 * s)], GOLD, int(14 * s))


def taxbill(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 70 * s, cy - 90 * s, cx + 70 * s, cy + 90 * s], int(8 * s), IVORY)
    g.tx((cx, cy - 55 * s), "TAX", font(FONT_SANS, int(34 * s)), RED)
    for i in range(3): g.ln([(cx - 46 * s, cy - 10 * s + i * 28 * s), (cx + 46 * s, cy - 10 * s + i * 28 * s)], SAGE_D, int(5 * s))
    g.tx((cx, cy + 62 * s), "$", font(FONT_SERIF, int(40 * s)), GREEN_D)


def mortgage(rgb, mask, cx, cy, s=1.0):
    house(rgb, mask, cx, cy + 10 * s, .45 * s); g = D(rgb, mask)
    g.tx((cx + 50 * s, cy - 60 * s), "%", font(FONT_SANS, int(64 * s)), GOLD)


def plate(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.el([cx - 90 * s, cy - 90 * s, cx + 90 * s, cy + 90 * s], IVORY); g.el([cx - 60 * s, cy - 60 * s, cx + 60 * s, cy + 60 * s], None, SAGE, int(6 * s))
    g.el([cx - 36 * s, cy - 30 * s, cx + 10 * s, cy + 16 * s], SAGE); g.el([cx - 6 * s, cy - 6 * s, cx + 40 * s, cy + 40 * s], RED)


def clipboard(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 120 * s, cy - 150 * s, cx + 120 * s, cy + 150 * s], int(16 * s), BROWN)
    g.rr([cx - 100 * s, cy - 120 * s, cx + 100 * s, cy + 130 * s], int(8 * s), IVORY)
    g.rr([cx - 50 * s, cy - 165 * s, cx + 50 * s, cy - 125 * s], int(10 * s), SAGE_D)
    for i in range(4):
        g.ln([(cx - 70 * s, cy - 70 * s + i * 52 * s), (cx + 30 * s, cy - 70 * s + i * 52 * s)], SAGE_D, int(6 * s))
        g.el([cx + 48 * s, cy - 82 * s + i * 52 * s, cx + 72 * s, cy - 58 * s + i * 52 * s], SAGE)


def ledger(img, t, rows, x0=1160, y0=190):
    """nastro di calcolo a destra: rows = [(start, label, value, colore)]"""
    p0 = ease(seg(t, rows[0][0] - .3, .5))
    if p0 <= 0: return
    lay = new_layer(); g = D(*lay)
    g.rr([x0, y0, x0 + 660, y0 + 130 + 140 * len(rows)], 30, CARD, GOLD, 5)
    g.tx((x0 + 330, y0 + 55), "HER MATH", font(FONT_SANS, 36), GOLD)
    alpha_layer(img, lay, p0)
    for i, (st, lab, val, col) in enumerate(rows):
        p = ease(seg(t, st, .5))
        if p <= 0: continue
        lay = new_layer(); g = D(*lay); y = y0 + 150 + 140 * i + 20 * (1 - p)
        g.tx((x0 + 40, y), lab, font(FONT_SANS, 34), SAGE, "lm"); g.tx((x0 + 620, y + 40), val, font(FONT_SERIF, 76), col, "rm")
        alpha_layer(img, lay, p)


def interviewer(rgb, mask, cx, cy, s=1.0):
    D(rgb, mask).rr([cx - 230 * s, cy + 40 * s, cx + 230 * s, cy + 80 * s], 10, BROWN); person(rgb, mask, cx, cy - 40 * s, s * .9)


# ============ BLOCCO 11: cosa non conta + prove (512)
def b11a(img, t):
    title(img, t, "WHAT DOESN'T COUNT")
    show(img, t, .3, lambda r, m: insurance(r, m, 480, 430, 1.5), .7, angle=-3)
    show(img, t, 1.2, lambda r, m: (person(r, m, 1300, 460, 1.7), D(r, m).tx((1300, 740), "SOMEONE OUTSIDE", font(FONT_SANS, 40), IVORY), D(r, m).tx((1300, 790), "YOUR HOUSEHOLD", font(FONT_SANS, 40), IVORY)), .6)
    stamp(img, 480, 640, seg(t, 2.4, .5), "ALREADY PAID", RED, -8, 54)
    for k in range(4):
        pp = seg(t, 3.0 + k * .3, 1.4)
        if 0 < pp < 1:
            pop(img, lambda r, m: coin(r, m, 1300, 380, 32), 1.0, a=min(1, pp * 6) * (1 - ease(seg(pp, .7, .3))), dx=-760 * ease(pp), dy=60 * ease(pp))
    txt_in(img, t, 3.8, (480, 760), "INSURANCE PAID IT", 46, IVORY)
    txt_in(img, t, 4.6, (W // 2, 930), "NOT DEDUCTIBLE", 80, RED)


def b11b(img, t):
    title(img, t, "SPECIAL DIETS")
    show(img, t, .3, lambda r, m: plate(r, m, 960, 470, 2.4), .7, dy=math.sin(t * 2) * 5)
    xm = ease_back(seg(t, 1.3, .5))
    if xm > 0: pop(img, lambda r, m: xmark(r, m, 1160, 330, 2.4), xm, a=ease(seg(t, 1.3, .2)))
    txt_in(img, t, 1.0, (960, 810), "SPECIAL DIETS DON'T COUNT", 64, IVORY)


def b11c(img, t):
    title(img, t, "KEEP YOUR PROOF")
    items = [(380, lambda r, m, cx, cy: clipboard(r, m, cx, cy, 1.0), "RECEIPTS"), (960, lambda r, m, cx, cy: pills(r, m, cx, cy, 1.5), "PHARMACY PRINTOUTS"), (1540, lambda r, m, cx, cy: insurance(r, m, cx, cy, 1.0), "PREMIUM STATEMENTS")]
    for i, (cx, ic, lab) in enumerate(items):
        st = .4 + i * 1.0
        show(img, t, st, lambda r, m, cx=cx, ic=ic, lab=lab: (D(r, m).rr([cx - 250, 220, cx + 250, 700], 30, CARD, SAGE_D, 4), ic(r, m, cx, 440), D(r, m).tx((cx, 650), lab, font(FONT_SANS, 34), IVORY)), .6)
        glow_check(img, t, cx + 190, 270, st + .5)
    show(img, t, 4.4, lambda r, m: interviewer(r, m, 560, 880, 1.0), .6)
    txt_in(img, t, 5.2, (1300, 830), "BRING THEM", 70, GOLD)
    txt_in(img, t, 5.8, (1300, 920), "TO THE INTERVIEW", 70, IVORY)


# ============ BLOCCO 12: spesa abitativa (624)
def b12a(img, t):
    title(img, t, "A DEDUCTION ALMOST NOBODY MENTIONS")
    show(img, t, .3, lambda r, m: house(r, m, 700, 560, 2.6), .8)
    show(img, t, 2.0, lambda r, m: (D(r, m).rr([1260, 360, 1830, 640], 36, CARD, GOLD, 6), D(r, m).tx((1545, 450), "SHELTER", font(FONT_SANS, 90), GOLD), D(r, m).tx((1545, 560), "COSTS", font(FONT_SANS, 90), IVORY)), .7)
    sp = ease(seg(t, 3.4, .8))
    if sp > 0:
        lay = new_layer(); D(*lay).el([210, 190, 1190, 960], None, GOLD, 10); alpha_layer(img, lay, sp * (.4 + .3 * math.sin(t * 4)))


def b12b(img, t):
    title(img, t, "NOBODY IN THE HOME IS ELDERLY")
    show(img, t, .3, lambda r, m: house(r, m, 560, 600, 2.2), .7)
    show(img, t, 1.4, lambda r, m: (D(r, m).rr([150, 150, 970, 215], 14, RED), D(r, m).tx((560, 183), "CAP: $769", font(FONT_SANS, 42), IVORY)), .6, dy=math.sin(t * 3) * 3)
    show(img, t, 2.6, lambda r, m: (D(r, m).rr([1080, 330, 1790, 690], 40, CARD, RED, 6), D(r, m).tx((1435, 430), "MAXIMUM", font(FONT_SANS, 62), IVORY), D(r, m).tx((1435, 550), "$769", font(FONT_SERIF, 150), RED), D(r, m).tx((1435, 640), "SHELTER DEDUCTION", font(FONT_SANS_M, 34), SAGE)), .7)
    txt_in(img, t, 4.0, (W // 2, 960), "A HARD CEILING", 60, GOLD)


def b12c(img, t):
    title(img, t, "BUT WITH SOMEONE SIXTY OR OLDER")
    p = ease(seg(t, 1.6, 1.4))
    show(img, t, .3, lambda r, m: house(r, m, 560, 620, 2.0), .7)
    lay = new_layer(); g = D(*lay)
    g.rr([150 - 120 * p, 150 - 340 * p, 970 - 120 * p, 215 - 340 * p], 14, RED); alpha_layer(img, lay, 1 - ease(seg(t, 2.6, .4)))
    stamp(img, 560, 330, seg(t, 3.0, .6), "NO CAP", GOLD, -6, 84)
    # barra del reddito: meta' e oltre
    x0, y, tw = 1000, 380, 780
    pb = ease(seg(t, 3.8, 1.2))
    lay = new_layer(); g = D(*lay)
    g.rr([x0, y - 60, x0 + tw * pb, y + 60], 18, SAGE_D)
    if pb > .55: g.rr([x0 + tw * .5, y - 60, x0 + tw * pb, y + 60], 18, GOLD)
    alpha_layer(img, lay, min(1, pb * 3))
    txt_in(img, t, 4.6, (x0 + tw * .25, y + 110), "HALF OF INCOME", 36, SAGE)
    txt_in(img, t, 5.2, (x0 + tw * .75, y + 110), "ABOVE HALF", 36, GOLD)
    txt_in(img, t, 6.0, (1390, 640), "ALL SHELTER COSTS", 52, IVORY)
    txt_in(img, t, 6.6, (1390, 720), "ABOVE HALF CAN COME OFF", 52, GOLD)


# ============ BLOCCO 13: cosa e' spesa abitativa (498)
def b13a(img, t):
    title(img, t, "SHELTER MEANS MORE THAN RENT")
    tl = [(380, key, "RENT"), (960, mortgage, "MORTGAGE + INTEREST"), (1540, taxbill, "PROPERTY TAXES")]
    for i, (cx, ic, lab) in enumerate(tl):
        st = .5 + i * 1.3
        show(img, t, st, lambda r, m, cx=cx, ic=ic, lab=lab: tile(r, m, cx, 460, ic, lab), .6)
        glow_check(img, t, cx + 150, 330, st + .5)


def b13b(img, t):
    title(img, t, "UTILITIES TOO")
    tl = [(280, bulb, "ELECTRICITY"), (760, drop, "WATER"), (1240, flame_icon, "HEATING + COOKING FUEL"), (1680, phone, "BASIC PHONE FEE")]
    for i, (cx, ic, lab) in enumerate(tl):
        st = .4 + i * 1.0
        show(img, t, st, lambda r, m, cx=cx, ic=ic, lab=lab: (D(r, m).rr([cx - 200, 280, cx + 200, 700], 30, CARD, SAGE_D, 4), ic(r, m, cx, 460, 1.0), D(r, m).tx((cx, 640), lab, font(FONT_SANS, 28), IVORY)), .6)
        glow_check(img, t, cx + 150, 330, st + .5)


def b13c(img, t):
    title(img, t, "SOME STATES USE A SET AMOUNT")
    def state(r, m):
        g = D(r, m)
        g.rr([200, 230, 880, 800], 40, CARD, SAGE_D, 6)
        g.pg([(300, 380), (460, 340), (620, 370), (760, 440), (730, 600), (600, 700), (450, 710), (340, 620), (290, 500)], SAGE)
        g.el([480, 470, 560, 550], GOLD); g.tx((520, 510), "$", font(FONT_SERIF, 54), GREEN_D)
    show(img, t, .3, state, .7)
    txt_in(img, t, 1.2, (540, 880), "SET UTILITY AMOUNT", 52, GOLD)
    show(img, t, 2.4, lambda r, m: interviewer(r, m, 1400, 640, 1.2), .6)
    show(img, t, 3.4, lambda r, m: bubble(r, m, 1350, 300, 560, 170, "left") or D(r, m).tx((1350, 300), "ASK YOUR OFFICE", font(FONT_SANS, 42), GOLD), .5)


# ============ BLOCCO 14: la matematica, passo 1 (422)
LED1 = lambda: [(2.6, "SOCIAL SECURITY", "$1,800", IVORY), (5.4, "− STANDARD", "$217", RED), (7.0, "= SO FAR", "$1,583", GOLD)]


def b14a(img, t):
    title(img, t, "TIME FOR THE MATH")
    show(img, t, .3, lambda r, m: house(r, m, 380, 520, 1.5), .7)
    show(img, t, .9, lambda r, m: person(r, m, 380, 640, 0.8), .5)
    show(img, t, 1.8, lambda r, m: (D(r, m).rr([80, 830, 680, 930], 24, GOLD), D(r, m).tx((380, 880), "68 · LIVING ALONE", font(FONT_SANS, 44), GREEN_D)), .5)
    show(img, t, 3.0, lambda r, m: paycheck(r, m, 1420, 440, 1.3, "$1,800"), .7, angle=3, dy=math.sin(t * 2) * 5)
    txt_in(img, t, 4.0, (1420, 720), "IN SOCIAL SECURITY", 50, IVORY)


def b14b(img, t):
    title(img, t, "STEP ONE")
    show(img, t, .3, lambda r, m: price_tag(r, m, 500, 330, "STEP 1", 640, 240), .8, angle=-4)
    txt_in(img, t, 1.4, (500, 560), "STANDARD DEDUCTION", 50, IVORY)
    show(img, t, 2.0, lambda r, m: D(r, m).tx((500, 760), "$217", font(FONT_SERIF, 230), GOLD), .7)
    ledger(img, t, [(1.0, "SOCIAL SECURITY", "$1,800", IVORY), (3.0, "− STANDARD", "$217", RED), (5.0, "= SO FAR", "$1,583", GOLD)], 1160, 200)


# ============ BLOCCO 15: la matematica, passo 2 (464)
def b15a(img, t):
    title(img, t, "STEP TWO · MEDICAL")
    show(img, t, .3, lambda r, m: price_tag(r, m, 420, 300, "STEP 2", 560, 220), .8, angle=-4)
    show(img, t, 1.2, lambda r, m: insurance(r, m, 420, 640, 1.2), .7, angle=-3)
    show(img, t, 2.0, lambda r, m: pills(r, m, 880, 600, 1.4), .7)
    txt_in(img, t, 3.0, (650, 850), "HEALTH INSURANCE + PRESCRIPTIONS", 40, IVORY)
    show(img, t, 3.6, lambda r, m: D(r, m).tx((1450, 480), "$235", font(FONT_SERIF, 250), RED), .7)
    txt_in(img, t, 4.4, (1450, 680), "A MONTH", 60, IVORY)


def b15b(img, t):
    title(img, t, "SUBTRACT THIRTY FIVE")
    x0, y, tw = 220, 430, 1480
    p = ease(seg(t, .6, 1.4)); full = 235
    lay = new_layer(); g = D(*lay)
    g.rr([x0, y - 80, x0 + tw * (35 / full) * p, y + 80], 20, SAGE_D)
    if p > .2: g.rr([x0 + tw * (35 / full) * p, y - 80, x0 + tw * p, y + 80], 20, GOLD)
    alpha_layer(img, lay, min(1, p * 3))
    txt_in(img, t, 1.8, (x0 + 100, y + 150), "− $35", 56, SAGE)
    txt_in(img, t, 2.4, (x0 + 35 / full * tw + 600, y + 150), "$200", 110, GOLD)
    show(img, t, 3.2, lambda r, m: (D(r, m).rr([520, 740, 1400, 900], 30, CARD, GOLD, 6), D(r, m).tx((960, 820), "$200 IS DEDUCTIBLE", font(FONT_SANS, 62), IVORY)), .7)


def b15c(img, t):
    title(img, t, "HER MATH SO FAR")
    show(img, t, .3, lambda r, m: D(r, m).tx((560, 330), "$1,583", font(FONT_SERIF, 170), IVORY), .7)
    show(img, t, 1.4, lambda r, m: D(r, m).tx((560, 520), "− $200", font(FONT_SERIF, 150), RED), .6)
    ln = ease(seg(t, 2.4, .5))
    if ln > 0: ImageDraw.Draw(img).line([180, 640, 180 + 760 * ln, 640], fill=GOLD, width=10)
    show(img, t, 3.0, lambda r, m: D(r, m).tx((560, 790), "$1,383", font(FONT_SERIF, 190), GOLD), .8)
    ledger(img, t, [(0.8, "AFTER STANDARD", "$1,583", IVORY), (2.0, "− MEDICAL", "$200", RED), (3.4, "= SO FAR", "$1,383", GOLD)], 1160, 200)


L.BLOCKS.update({
    11: [("What doesn't count? Anything an insurance company or someone outside your household already paid.", b11a),
         ("And special diets don't count.", b11b),
         ("Also, you need proof, so keep your receipts, your pharmacy printouts and your premium statements. Bring them to the interview.", b11c)],
    12: [("Now a deduction almost nobody mentions. Shelter costs.", b12a),
         ("If nobody in your home is elderly or disabled, the shelter deduction is capped at seven hundred sixty nine dollars.", b12b),
         ("But with someone sixty or older, there's no cap. All your shelter costs above half of your income can come off.", b12c)],
    13: [("And shelter means more than rent. It includes your mortgage and interest, property taxes,", b13a),
         ("electricity, water, heating and cooking fuel, and the basic fee for one phone.", b13b),
         ("Some states even use a set amount for utilities, so ask your office.", b13c)],
    14: [("Time for the math. Take our woman, sixty eight, living alone, with eighteen hundred dollars in Social Security.", b14a),
         ("Step one: subtract the standard deduction, two hundred seventeen. She's at fifteen eighty three.", b14b)],
    15: [("Step two: medical. She pays two hundred thirty five dollars a month for health insurance and prescriptions.", b15a),
         ("Subtract thirty five, and two hundred is deductible.", b15b),
         ("Fifteen eighty three minus two hundred is thirteen eighty three.", b15c)],
})


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = L.split_frames(b)
    for i, ((s, fn), n) in enumerate(zip(L.BLOCKS[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide0{i}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
