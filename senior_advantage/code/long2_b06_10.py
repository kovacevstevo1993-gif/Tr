"""Video lungo 2 (SNAP over 60) - blocchi 6-10 e lancio di tutti i blocchi.
Uso: OUT=cartella SA_TMP=/tmp/f python3 long2_b06_10.py <blocco 1-10> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import long2_b02_05 as L
from long2_b02_05 import *

# fotogrammi dalla timeline dell'utente (fine blocco): 1022 1631 2306 2886 3524 4202 4868 5346 5915 6586
ENDS = [1022, 1631, 2306, 2886, 3524, 4202, 4868, 5346, 5915, 6586]
FR = {i + 1: e - (ENDS[i - 1] if i else 0) for i, e in enumerate(ENDS)}


def counter(img, t, st, xy, target, size, col, dur=1.4, prefix="$"):
    p = ease(seg(t, st, dur))
    if p <= 0: return
    lay = new_layer(); D(*lay).tx(xy, f"{prefix}{round(target * p):,}", font(FONT_SERIF, size), col, "lm"); alpha_layer(img, lay, min(1, p * 4))


def bar(img, t, st, x0, y, maxw, val, vmax, col, label, dur=1.4, h=90):
    p = ease(seg(t, st, dur))
    if p <= 0: return
    lay = new_layer(); g = D(*lay)
    g.rr([x0, y - h / 2, x0 + maxw * val / vmax * p, y + h / 2], 22, col)
    g.tx((x0 + 24, y), label, font(FONT_SANS, 40), GREEN_D, "lm")
    alpha_layer(img, lay, min(1, p * 4))


def tooth(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.pg([(cx - 70 * s, cy - 60 * s), (cx - 40 * s, cy - 85 * s), (cx, cy - 65 * s), (cx + 40 * s, cy - 85 * s), (cx + 70 * s, cy - 60 * s), (cx + 62 * s, cy + 10 * s), (cx + 40 * s, cy + 90 * s), (cx + 15 * s, cy + 90 * s), (cx + 5 * s, cy + 20 * s), (cx - 5 * s, cy + 20 * s), (cx - 15 * s, cy + 90 * s), (cx - 40 * s, cy + 90 * s), (cx - 62 * s, cy + 10 * s)], IVORY)


def pills(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 60 * s, cy - 40 * s, cx + 60 * s, cy + 90 * s], int(14 * s), GOLD)
    g.rr([cx - 70 * s, cy - 80 * s, cx + 70 * s, cy - 35 * s], int(10 * s), IVORY)
    g.rr([cx - 45 * s, cy + 0 * s, cx + 45 * s, cy + 60 * s], int(8 * s), IVORY)
    g.tx((cx, cy + 30 * s), "Rx", font(FONT_SERIF, int(46 * s)), RED)


def dentures(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.pg([(cx - 90 * s, cy - 40 * s), (cx + 90 * s, cy - 40 * s), (cx + 60 * s, cy + 40 * s), (cx - 60 * s, cy + 40 * s)], PINK)
    for i in range(7): g.rr([cx - 84 * s + i * 26 * s, cy - 36 * s, cx - 62 * s + i * 26 * s, cy + 14 * s], 5, IVORY)


def hospital(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 110 * s, cy - 70 * s, cx + 110 * s, cy + 90 * s], int(10 * s), IVORY)
    g.rr([cx - 30 * s, cy + 30 * s, cx + 30 * s, cy + 90 * s], 6, SAGE_D)
    g.rc([cx - 14 * s, cy - 60 * s, cx + 14 * s, cy - 10 * s], RED); g.rc([cx - 36 * s, cy - 42 * s, cx + 36 * s, cy - 28 * s], RED)
    for x in (-80, 50):
        for y in (-5, 35): g.rr([cx + x * s, cy + y * s, cx + (x + 30) * s, cy + (y + 25) * s], 4, SAGE_D)


def nurse(rgb, mask, cx, cy, s=1.0):
    person(rgb, mask, cx, cy, s * .8); cross(rgb, mask, cx, cy + 40 * s, int(30 * s))


def insurance(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 130 * s, cy - 80 * s, cx + 130 * s, cy + 80 * s], int(16 * s), IVORY, SAGE_D, 4)
    g.rr([cx - 130 * s, cy - 80 * s, cx + 130 * s, cy - 30 * s], int(16 * s), SAGE_D); g.rc([cx - 130 * s, cy - 50 * s, cx + 130 * s, cy - 30 * s], SAGE_D)
    g.tx((cx, cy - 52 * s), "HEALTH PLAN", font(FONT_SANS, int(26 * s)), IVORY)
    cross(rgb, mask, cx - 70 * s, cy + 25 * s, int(26 * s)); g.tx((cx + 30 * s, cy + 25 * s), "$ / MO", font(FONT_SANS, int(34 * s)), GREEN_D)


def car(rgb, mask, cx, cy, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 130 * s, cy - 10 * s, cx + 130 * s, cy + 60 * s], int(24 * s), IVORY)
    g.pg([(cx - 80 * s, cy - 10 * s), (cx - 50 * s, cy - 65 * s), (cx + 50 * s, cy - 65 * s), (cx + 85 * s, cy - 10 * s)], IVORY)
    g.pg([(cx - 62 * s, cy - 14 * s), (cx - 40 * s, cy - 55 * s), (cx + 40 * s, cy - 55 * s), (cx + 66 * s, cy - 14 * s)], SAGE_D)
    for x in (-80, 80): g.el([cx + (x - 28) * s, cy + 32 * s, cx + (x + 28) * s, cy + 88 * s], GREEN_D, IVORY, int(7 * s))
    cross(rgb, mask, cx, cy + 20 * s, int(22 * s))


def laptop(rgb, mask, cx, cy, s=1.0, lid=1.0):
    g = D(rgb, mask)
    g.rr([cx - 220 * s, cy + 100 * s, cx + 220 * s, cy + 130 * s], int(10 * s), SAGE)
    h = 220 * s * lid
    if h > 6:
        g.rr([cx - 190 * s, cy + 100 * s - h, cx + 190 * s, cy + 100 * s], int(14 * s), GREEN_D, SAGE, int(8 * s))


def tile(rgb, mask, cx, cy, icon, label, s=1.0):
    g = D(rgb, mask)
    g.rr([cx - 190, cy - 170, cx + 190, cy + 170], 30, CARD, SAGE_D, 4)
    icon(rgb, mask, cx, cy - 20, s)
    g.tx((cx, cy + 130), label, font(FONT_SANS, 36), IVORY)


def glow_check(img, t, cx, cy, st):
    p = ease_back(seg(t, st, .5))
    if p > 0: pop(img, lambda r, m: (D(r, m).el([cx - 36, cy - 36, cx + 36, cy + 36], SAGE), tick(r, m, cx, cy, .6, GREEN_D)), p, a=ease(seg(t, st, .2)))


# ============ BLOCCO 6: i limiti (678)
def b6a(img, t):
    title(img, t, "ONE PERSON · MONTHLY LIMITS")
    show(img, t, .3, lambda r, m: person(r, m, 330, 520, 2.0), .7)
    bar(img, t, 1.0, 640, 360, 1100, 1729, 1800, RED, "GROSS", 1.6, 110)
    counter(img, t, 1.0, (1000, 360), 1729, 80, GREEN_D, 1.6)
    bar(img, t, 3.4, 640, 560, 1100, 1330, 1800, GOLD, "NET", 1.6, 110)
    counter(img, t, 3.4, (1000, 560), 1330, 80, GREEN_D, 1.6)
    txt_in(img, t, 1.4, (1190, 250), "SEVENTEEN TWENTY NINE", 34, SAGE, sans_m=True)
    txt_in(img, t, 3.8, (1190, 455), "THIRTEEN THIRTY", 34, SAGE, sans_m=True)
    txt_in(img, t, 6.0, (W // 2, 860), "TWO DIFFERENT LIMITS", 70, IVORY)
    txt_in(img, t, 6.8, (W // 2, 950), "AT SIXTY, ONLY NET MATTERS", 50, GOLD)


def b6b(img, t):
    title(img, t, "TWO PEOPLE · MONTHLY LIMITS")
    show(img, t, .3, lambda r, m: (person(r, m, 250, 520, 1.8), person(r, m, 430, 520, 1.8)), .7)
    bar(img, t, 1.0, 640, 360, 1100, 2345, 2400, RED, "GROSS", 1.6, 110)
    counter(img, t, 1.0, (1000, 360), 2345, 80, GREEN_D, 1.6)
    bar(img, t, 3.0, 640, 560, 1100, 1804, 2400, GOLD, "NET", 1.6, 110)
    counter(img, t, 3.0, (1000, 560), 1804, 80, GREEN_D, 1.6)
    txt_in(img, t, 5.0, (W // 2, 900), "TWO PEOPLE: MORE ROOM", 64, IVORY)


def b6c(img, t):
    title(img, t, "OFFICIAL U S D A LIMITS")
    show(img, t, .3, lambda r, m: calendar(r, m, 400, 470, 1.9, "1"), .8)
    txt_in(img, t, 1.0, (400, 780), "OCTOBER 1, 2026", 56, GOLD)
    show(img, t, 1.8, lambda r, m: building(r, m, 1130, 440, .9), .7)
    def us(r, m):
        g = D(r, m)
        g.rr([1450, 300, 1830, 600], 30, CARD, SAGE_D, 5)
        g.pg([(1490, 380), (1560, 350), (1700, 360), (1790, 390), (1770, 480), (1700, 540), (1600, 560), (1520, 520), (1480, 450)], SAGE)
        g.tx((1640, 450), "48 + D.C.", font(FONT_SANS, 40), GREEN_D)
    show(img, t, 3.4, us, .6)
    txt_in(img, t, 4.0, (1640, 680), "48 STATES AND D.C.", 40, IVORY)
    stamp(img, 1130, 840, seg(t, 5.0, .6), "OFFICIAL", GOLD, -5, 62)


# ============ BLOCCO 7: la donna (666)
def b7a(img, t):
    title(img, t, "NOW PICTURE THIS")
    show(img, t, .3, lambda r, m: person(r, m, 430, 640, 2.4), .7)
    show(img, t, 1.4, lambda r, m: paycheck(r, m, 1230, 450, 1.35, "$1,800"), .7, angle=3, dy=math.sin(t * 2) * 5)
    txt_in(img, t, 2.8, (1230, 700), "SOCIAL SECURITY · PER MONTH", 44, IVORY)
    for k in range(5):
        pp = seg(t, 3.4 + k * .3, 1.4)
        if 0 < pp < 1:
            pop(img, lambda r, m: coin(r, m, 1230, 450, 34), 1.0, a=min(1, pp * 6) * (1 - ease(seg(pp, .7, .3))), dx=-540 * ease(pp), dy=120 * ease(pp))


def b7b(img, t):
    title(img, t, "SHE SEES THE LIMIT")
    show(img, t, .3, lambda r, m: person(r, m, 360, 660, 2.0), .6)
    show(img, t, .9, lambda r, m: (laptop(r, m, 1130, 400, 1.2), D(r, m).rr([960, 290, 1300, 480], 14, CARD), D(r, m).tx((1130, 340), "GROSS LIMIT", font(FONT_SANS, 34), SAGE), D(r, m).tx((1130, 420), "$1,729", font(FONT_SERIF, 78), GOLD)), .6)
    show(img, t, 2.0, lambda r, m: bubble(r, m, 560, 260, 520, 170, "left") or D(r, m).tx((560, 262), "I'M OVER.", font(FONT_SERIF, 76), GOLD), .5)
    # chiude il laptop
    lid = 1 - ease(seg(t, 4.2, .9))
    if t > 4.2:
        lay = new_layer(); g = D(*lay)
        g.rr([590, 215, 1030, 245], 6, GREEN_D)  # placeholder, coperta da overlay
    ov = ease(seg(t, 4.2, .9))
    if ov > 0:
        lay = new_layer(); g = D(*lay); g.rr([880, 250, 1380, 540], 40, GREEN_D); alpha_layer(img, lay, ov)
        lay = new_layer(); xmark(lay[0], lay[1], 1130, 400, 2.4); alpha_layer(img, lay, ov)
    txt_in(img, t, 5.2, (1130, 700), "SHE CLOSES THE PAGE", 56, IVORY)


def b7c(img, t):
    title(img, t, "BUT SHE IS SIXTY EIGHT")
    show(img, t, .3, lambda r, m: person(r, m, 380, 650, 2.2), .7)
    show(img, t, 1.0, lambda r, m: price_tag(r, m, 380, 330, "68", 300, 170), .6, angle=-6)
    show(img, t, 2.0, lambda r, m: (gate(r, m, 1150, 480, 1.5, RED), D(r, m).tx((1150, 790), "GROSS TEST", font(FONT_SANS, 50), IVORY)), .7)
    xm = ease_back(seg(t, 3.0, .5))
    if xm > 0: pop(img, lambda r, m: xmark(r, m, 1150, 290, 1.8), xm, a=ease(seg(t, 3.0, .2)))
    stamp(img, 1150, 900, seg(t, 3.4, .5), "DOES NOT APPLY", RED, -5, 46)
    # segnalibro "ricordala"
    sb = ease_back(seg(t, 6.0, .6))
    if sb > 0:
        pop(img, lambda r, m: (D(r, m).pg([(1560, 280), (1700, 280), (1700, 520), (1630, 460), (1560, 520)], GOLD), D(r, m).pg([(1630, 320), (1645, 358), (1685, 360), (1653, 384), (1665, 424), (1630, 400), (1595, 424), (1607, 384), (1575, 360), (1615, 358)], GREEN_D)), sb, a=ease(seg(t, 6.0, .3)))
    txt_in(img, t, 6.6, (1630, 600), "REMEMBER HER", 44, GOLD)


# ============ BLOCCO 8: dal lordo al netto, detrazione standard (478)
def b8a(img, t):
    title(img, t, "FROM GROSS TO NET")
    steps = [("GROSS", 380, RED), ("DEDUCTIONS", 960, SAGE_D), ("NET", 1540, GOLD)]
    for i, (lab, cx, col) in enumerate(steps):
        st = .4 + i * 1.2
        show(img, t, st, lambda r, m, cx=cx, lab=lab, col=col: (D(r, m).rr([cx - 230, 400, cx + 230, 580], 30, col), D(r, m).tx((cx, 490), lab, font(FONT_SANS, 56), GREEN_D)), .6)
        if i < 2:
            ar = ease(seg(t, st + .7, .4))
            if ar > 0:
                lay = new_layer(); x = cx + 250; D(*lay).pg([(x, 465), (x + 50, 465), (x + 50, 435), (x + 105, 490), (x + 50, 545), (x + 50, 515), (x, 515)], GOLD); alpha_layer(img, lay, ar)
    show(img, t, 3.6, lambda r, m: D(r, m).pg([(960, 150), (990, 215), (1060, 220), (1008, 265), (1024, 335), (960, 298), (896, 335), (912, 265), (860, 220), (930, 215)], GOLD), .6, dy=math.sin(t * 3) * 5)
    txt_in(img, t, 4.4, (W // 2, 760), "AND SENIORS HAVE AN EDGE", 78, GOLD)


def b8b(img, t):
    title(img, t, "STANDARD DEDUCTION")
    show(img, t, .3, lambda r, m: D(r, m).tx((560, 400), "$217", font(FONT_SERIF, 300), GOLD), .8)
    txt_in(img, t, 1.4, (560, 640), "1 TO 3 PEOPLE", 56, IVORY)
    txt_in(img, t, 2.4, (560, 740), "TAKEN OFF AUTOMATICALLY", 50, SAGE)
    show(img, t, 1.0, lambda r, m: paycheck(r, m, 1400, 330, 1.0, "$1,800"), .6, angle=2)
    show(img, t, 2.8, lambda r, m: D(r, m).tx((1400, 530), "− $217", font(FONT_SERIF, 96), RED), .5)
    show(img, t, 4.0, lambda r, m: D(r, m).tx((1400, 700), "= $1,583", font(FONT_SERIF, 110), IVORY), .6)
    txt_in(img, t, 5.0, (1400, 820), "NO PAPERWORK NEEDED", 42, GOLD)


# ============ BLOCCO 9: regola 2 (569)
def b9a(img, t):
    title(img, t, "THE ONE I PROMISED")
    show(img, t, .3, lambda r, m: price_tag(r, m, 560, 450, "RULE 2", 760, 300), .8, angle=-4, dy=math.sin(t * 2) * 6)
    show(img, t, 1.4, lambda r, m: cross(r, m, 1400, 450, 190), .8)
    txt_in(img, t, 2.4, (1400, 760), "MEDICAL COSTS", 66, IVORY)
    for k in range(6):
        pp = seg(t, 3.0 + k * .4, 1.8)
        if 0 < pp < 1:
            pop(img, lambda r, m: coin(r, m, 1400, 450, 32), 1.0, a=min(1, pp * 6) * (1 - ease(seg(pp, .7, .3))), dx=-360 * ease(pp) + 20 * math.sin(pp * 9), dy=-40 + 300 * ease(pp))
    txt_in(img, t, 4.4, (W // 2, 940), "THEY COME OFF YOUR INCOME", 56, GOLD)


def b9b(img, t):
    title(img, t, "COSTS YOU PAY YOURSELF")
    show(img, t, .3, lambda r, m: person(r, m, 330, 500, 1.5), .7)
    show(img, t, 1.2, lambda r, m: pills(r, m, 1000, 450, 1.8), .7)
    show(img, t, 2.0, lambda r, m: (D(r, m).rr([1250, 270, 1620, 640], 14, IVORY), D(r, m).tx((1435, 330), "RECEIPT", font(FONT_SANS, 38), GREEN_D), [D(r, m).ln([(1290, 400 + i * 50), (1580, 400 + i * 50)], SAGE_D, 6) for i in range(4)], D(r, m).tx((1435, 600), "$235", font(FONT_SERIF, 70), RED)), .6, angle=3)
    for k in range(5):
        pp = seg(t, 2.8 + k * .3, 1.5)
        if 0 < pp < 1:
            pop(img, lambda r, m: coin(r, m, 440, 520, 32), 1.0, a=min(1, pp * 6) * (1 - ease(seg(pp, .7, .3))), dx=560 * ease(pp), dy=-60 * math.sin(pp * math.pi))
    txt_in(img, t, 4.4, (W // 2, 960), "ABOVE $35 A MONTH", 76, GOLD)


def b9c(img, t):
    title(img, t, "ONLY THE PART OVER $35")
    x0, y, tw = 220, 430, 1480
    full = 235
    p = ease(seg(t, .6, 1.4))
    lay = new_layer(); g = D(*lay)
    g.rr([x0, y - 80, x0 + tw * (35 / full) * p, y + 80], 20, SAGE_D)
    if p > .2:
        g.rr([x0 + tw * (35 / full) * p, y - 80, x0 + tw * p, y + 80], 20, GOLD)
    alpha_layer(img, lay, min(1, p * 3))
    txt_in(img, t, 1.8, (x0 + 100, y + 150), "FIRST $35", 44, SAGE)
    txt_in(img, t, 1.8, (x0 + 90, y + 210), "NOT COUNTED", 36, SAGE, sans_m=True)
    txt_in(img, t, 2.6, (x0 + 35 / full * tw + 600, y + 150), "EVERYTHING ABOVE", 52, GOLD)
    txt_in(img, t, 2.6, (x0 + 35 / full * tw + 600, y + 215), "IS DEDUCTIBLE", 52, GOLD)
    show(img, t, 4.0, lambda r, m: (D(r, m).rr([560, 740, 1360, 900], 30, CARD, GOLD, 6), D(r, m).tx((960, 820), "$235 − $35 = $200 OFF", font(FONT_SANS, 56), IVORY)), .7)


# ============ BLOCCO 10: cosa conta (671)
def b10a(img, t):
    title(img, t, "WHAT COUNTS?")
    tiles = [(430, 330, cross, "DOCTOR BILLS", 1.0), (1000, 330, tooth, "DENTIST BILLS", 1.0), (1490, 330, pills, "PRESCRIPTIONS", .9)]
    for i, (cx, cy, ic, lab, s) in enumerate(tiles):
        st = .5 + i * 1.5
        show(img, t, st, lambda r, m, cx=cx, cy=cy, ic=ic, lab=lab, s=s: tile(r, m, cx, cy, (lambda rr, mm, x, y, ss: ic(rr, mm, x, y, 70 if ic is cross else s)), lab), .6)
        glow_check(img, t, cx + 150, cy - 130, st + .5)
    show(img, t, 5.2, lambda r, m: (D(r, m).rr([420, 600, 1500, 800], 36, CARD, GOLD, 6), D(r, m).tx((960, 700), "OVER THE COUNTER · WITH DOCTOR APPROVAL", font(FONT_SANS, 40), GOLD)), .6)


def b10b(img, t):
    title(img, t, "AND MORE")
    tiles = [(430, 420, dentures, "DENTURES"), (1000, 420, hospital, "HOSPITAL COSTS"), (1490, 420, nurse, "NURSING CARE")]
    for i, (cx, cy, ic, lab) in enumerate(tiles):
        st = .5 + i * 1.5
        show(img, t, st, lambda r, m, cx=cx, cy=cy, ic=ic, lab=lab: tile(r, m, cx, cy, ic, lab), .6)
        glow_check(img, t, cx + 150, cy - 130, st + .5)
    txt_in(img, t, 5.0, (W // 2, 830), "INPATIENT AND OUTPATIENT", 56, IVORY)


def b10c(img, t):
    title(img, t, "ALMOST NOBODY KNOWS")
    show(img, t, .3, lambda r, m: insurance(r, m, 560, 450, 1.7), .7, angle=-3)
    show(img, t, 2.4, lambda r, m: car(r, m, 1400, 450, 1.7), .7)
    txt_in(img, t, 1.2, (560, 700), "HEALTH INSURANCE PREMIUMS", 46, IVORY)
    txt_in(img, t, 3.2, (1400, 700), "MEDICAL TRANSPORTATION", 46, IVORY)
    for cx, st in ((560, 1.6), (1400, 3.6)):
        pop(img, lambda r, m, cx=cx: (D(r, m).el([cx + 190, 180, cx + 310, 300], GOLD), D(r, m).tx((cx + 250, 240), "✓" if False else "+", font(FONT_SANS, 110), GREEN_D)), ease_back(seg(t, st, .5)), a=ease(seg(t, st, .2)))
    txt_in(img, t, 4.8, (W // 2, 880), "THEY COUNT TOO", 90, GOLD)


L.BLOCKS.update({
    6: [("Look at the numbers. For one person, the gross limit is seventeen hundred twenty nine dollars a month. The net limit is thirteen hundred thirty.", b6a),
        ("For two people, gross is twenty three forty five, and net is eighteen hundred four.", b6b),
        ("Those are the U S D A limits from October first, twenty twenty six, in the forty eight states and D C.", b6c)],
    7: [("Now picture this. A woman gets eighteen hundred dollars a month in Social Security.", b7a),
        ("She sees the gross limit, seventeen twenty nine, and she says: I'm over. She closes the page.", b7b),
        ("But she's sixty eight. The gross test doesn't apply to her. She never even asked. Remember her, because we'll come back to her math.", b7c)],
    8: [("So how do you get from gross income down to net income? Deductions. And this is where seniors have an edge.", b8a),
        ("First, a standard deduction. For households of one to three people, it's two hundred seventeen dollars, taken off automatically.", b8b)],
    9: [("Rule number two. This is the one I promised. Medical costs.", b9a),
        ("If you're sixty or older, the medical expenses you pay yourself, above thirty five dollars a month, come off your income.", b9b),
        ("Only the amount over thirty five dollars counts. But everything above that is deductible.", b9c)],
    10: [("What counts? Doctor and dentist bills. Prescription drugs. Over the counter medicine, when a doctor approves it.", b10a),
         ("Dentures. Hospital costs, inpatient and outpatient. Nursing care.", b10b),
         ("And here's what almost nobody knows: health insurance premiums count too, and so do some medical transportation costs.", b10c)],
})
L.BLOCK_FRAMES.update(FR)


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    if b == 1:
        import long2_b01 as B1
        B1.DUR2[:] = [round(1022 * w / sum(B1._w)) for w in B1._w[:2]] + [0]; B1.DUR2[2] = 1022 - sum(B1.DUR2[:2])
        for k, fn in ((1, B1.c1), (2, B1.c2), (3, B1.c3)):
            if not only or k in only:
                render(fn, B1.DUR2[k - 1] / FPS, f"{OUT}/bloco01-slide0{k}.mp4"); print("ok blocco 1 clip", k, B1.DUR2[k - 1], flush=True)
    else:
        fr = L.split_frames(b)
        for i, ((s, fn), n) in enumerate(zip(L.BLOCKS[b], fr), 1):
            if only and i not in only: continue
            render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide0{i}.mp4")
            print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
