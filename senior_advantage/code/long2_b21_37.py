"""Video lungo 2 (SNAP over 60) - blocchi 21-37. Fine blocco (fotogrammi, dalla timeline utente):
12572 13049 13723 14190 14960 15507 15913 16739 17351 17947 18488 19054 19655 20207 20925 21469 21955.
Uso: OUT=cartella SA_TMP=/tmp/f python3 long2_b21_37.py <blocco 21-37> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import long2_b02_05 as L
from long2_b16_20 import *

ENDS3 = [12572, 13049, 13723, 14190, 14960, 15507, 15913, 16739, 17351, 17947, 18488, 19054, 19655, 20207, 20925, 21469, 21955]
FR4 = {21 + i: e - (12037 if i == 0 else ENDS3[i - 1]) for i, e in enumerate(ENDS3)}
L.BLOCK_FRAMES.update(FR4)


def person2(rgb, mask, cx, cy, s=1.0, col=SAGE):
    g = D(rgb, mask)
    g.el([cx - 62 * s, cy - 150 * s, cx + 62 * s, cy - 26 * s], col)
    g.d.pieslice([cx - 125 * s, cy - 10 * s, cx + 125 * s, cy + 250 * s], 180, 360, fill=col); g.m.pieslice([cx - 125 * s, cy - 10 * s, cx + 125 * s, cy + 250 * s], 180, 360, fill=255)


def calendar2(rgb, mask, cx, cy, s=1.0, label="END", size=64):
    g = D(rgb, mask)
    g.rr([cx - 110 * s, cy - 120 * s, cx + 110 * s, cy + 120 * s], int(18 * s), IVORY)
    g.rr([cx - 110 * s, cy - 120 * s, cx + 110 * s, cy - 60 * s], int(18 * s), RED); g.rc([cx - 110 * s, cy - 80 * s, cx + 110 * s, cy - 60 * s], RED)
    g.tx((cx, cy + 15 * s), label, font(FONT_SANS, int(size * s)), GREEN_D)
    for x in (-60, 60): g.rr([cx + (x - 8) * s, cy - 140 * s, cx + (x + 8) * s, cy - 95 * s], 6, SAGE_D)


def stateshape(r, m, cx, cy, s=1.0, col=SAGE, label=None):
    g = D(r, m)
    pts = [(-110, -50), (-30, -80), (60, -65), (115, -10), (95, 60), (30, 90), (-60, 80), (-115, 20)]
    g.pg([(cx + x * s, cy + y * s) for x, y in pts], col)
    if label: g.tx((cx, cy), label, font(FONT_SANS, int(34 * s)), GREEN_D)


def thumb(r, m, cx, cy, s=1.0, col=GOLD):
    g = D(r, m)
    g.rr([cx - 130 * s, cy - 20 * s, cx - 60 * s, cy + 120 * s], int(14 * s), SAGE_D)
    g.rr([cx - 60 * s, cy - 20 * s, cx + 120 * s, cy + 120 * s], int(26 * s), col)
    g.rr([cx - 40 * s, cy - 110 * s, cx + 20 * s, cy], int(24 * s), col)
    for i in range(3): g.ln([(cx + 10 * s, cy + (10 + i * 36) * s), (cx + 100 * s, cy + (10 + i * 36) * s)], GREEN_D, int(5 * s))


def bell(r, m, cx, cy, s=1.0, col=GOLD):
    g = D(r, m)
    g.pieslice = None
    g.d.pieslice([cx - 70 * s, cy - 90 * s, cx + 70 * s, cy + 50 * s], 180, 360, fill=col); g.m.pieslice([cx - 70 * s, cy - 90 * s, cx + 70 * s, cy + 50 * s], 180, 360, fill=255)
    g.rc([cx - 70 * s, cy - 20 * s, cx + 70 * s, cy + 40 * s], col)
    g.rr([cx - 90 * s, cy + 30 * s, cx + 90 * s, cy + 55 * s], int(10 * s), col)
    g.el([cx - 16 * s, cy + 55 * s, cx + 16 * s, cy + 85 * s], col)
    g.el([cx - 12 * s, cy - 110 * s, cx + 12 * s, cy - 86 * s], col)


def paper(r, m, cx, cy, s=1.0, lab="", col=IVORY):
    g = D(r, m)
    g.rr([cx - 90 * s, cy - 115 * s, cx + 90 * s, cy + 115 * s], int(8 * s), col)
    for i in range(4): g.ln([(cx - 60 * s, cy - 55 * s + i * 36 * s), (cx + 60 * s, cy - 55 * s + i * 36 * s)], SAGE_D, int(5 * s))
    if lab: g.tx((cx, cy - 85 * s), lab, font(FONT_SANS, int(24 * s)), RED)


def office(r, m, cx, cy, s=1.0):
    building(r, m, cx, cy, s * .55, "OFFICE")


def stopsign(r, m, cx, cy, s=1.0):
    g = D(r, m); pts = [(cx + 100 * s * math.cos(math.pi / 8 + i * math.pi / 4), cy + 100 * s * math.sin(math.pi / 8 + i * math.pi / 4)) for i in range(8)]
    g.pg(pts, RED); g.tx((cx, cy), "STOP", font(FONT_SANS, int(44 * s)), IVORY)


def numcard(img, t, st, cx, cy, n, l1, l2, col=GOLD, w=520, h=300):
    show(img, t, st, lambda r, m: (D(r, m).rr([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], 34, CARD, col, 6), D(r, m).el([cx - w / 2 + 20, cy - h / 2 + 20, cx - w / 2 + 110, cy - h / 2 + 110], col), D(r, m).tx((cx - w / 2 + 65, cy - h / 2 + 65), str(n), font(FONT_SERIF, 64), GREEN_D), D(r, m).tx((cx + 40, cy - 10), l1, font(FONT_SANS, 40), IVORY), D(r, m).tx((cx + 40, cy + 50), l2, font(FONT_SANS, 40), col)), .6)


# ============ 21: regola 3, risparmi (535)
def b21a(img, t):
    title(img, t, "RULE NUMBER THREE")
    show(img, t, .3, lambda r, m: price_tag(r, m, 560, 390, "RULE 3", 700, 280), .8, angle=-4, dy=math.sin(t * 2) * 6)
    show(img, t, 1.2, lambda r, m: piggy(r, m, 1400, 440, 1.9), .8, dx=0, dy=math.sin(t * 6) * 5 if 2.0 < t < 3.5 else 0)
    txt_in(img, t, 2.2, (560, 640), "THE ONE THAT SCARES PEOPLE MOST", 44, IVORY)
    txt_in(img, t, 3.4, (W // 2, 900), "SAVINGS", 150, GOLD)


def jar(img, t, x0, y0, w, h, fill_to, col, label_val, limit_line=None):
    """barra verticale (salvadanaio-vaso) con riempimento e linea limite"""
    lay = new_layer(); g = D(*lay)
    g.rr([x0, y0, x0 + w, y0 + h], 40, CARD, SAGE_D, 6)
    fh = (h - 20) * fill_to
    if fh > 6: g.rr([x0 + 10, y0 + h - 10 - fh, x0 + w - 10, y0 + h - 10], 30, col)
    alpha_layer(img, lay, 1)


def b21b(img, t):
    title(img, t, "COUNTABLE RESOURCES")
    p = ease(seg(t, .8, 2.2))
    jar(img, t, 360, 260, 360, 640, .75 * p, SAGE_D, "")
    ImageDraw.Draw(img).line([320, 260 + 640 * (1 - .75), 760, 260 + 640 * (1 - .75)], fill=GOLD, width=8) if p > 0 else None
    for k in range(5):
        pp = seg(t, .4 + k * .4, 1.2)
        if 0 < pp < 1:
            pop(img, lambda r, m: coin(r, m, 540, 150, 40), 1.0, a=min(1, pp * 4) * (1 - ease(seg(pp, .8, .2))), dy=400 * ease(pp))
    show(img, t, 1.2, lambda r, m: D(r, m).tx((1250, 330), "$3,000", font(FONT_SERIF, 260), IVORY), .8)
    txt_in(img, t, 2.2, (1250, 560), "LIMIT FOR MOST HOUSEHOLDS", 46, SAGE)
    txt_in(img, t, 3.2, (1250, 650), "CASH · BANK ACCOUNTS", 40, GOLD)


def b21c(img, t):
    title(img, t, "BUT AT SIXTY OR OLDER")
    jar(img, t, 360, 260, 360, 640, 1.0, GOLD, "")
    ImageDraw.Draw(img).line([320, 260 + 640 * (1 - .75), 760, 260 + 640 * (1 - .75)], fill=SAGE, width=6)
    up = ease(seg(t, 1.2, 1.2))
    ImageDraw.Draw(img).line([320, 260 + 640 * (1 - .75) - 130 * up, 760, 260 + 640 * (1 - .75) - 130 * up], fill=GOLD, width=10)
    show(img, t, .3, lambda r, m: price_tag(r, m, 540, 190, "60+", 260, 110), .5)
    show(img, t, 2.0, lambda r, m: D(r, m).tx((1250, 360), "$4,750", font(FONT_SERIF, 270), GOLD), .9)
    txt_in(img, t, 3.0, (1250, 590), "THE LIMIT GOES UP", 54, IVORY)
    txt_in(img, t, 3.8, (1250, 680), "MORE ROOM TO KEEP YOUR SAVINGS", 36, SAGE)


# ============ 22: cosa non conta (477)
def b22a(img, t):
    title(img, t, "DOESN'T COUNT AT ALL")
    show(img, t, .3, lambda r, m: house(r, m, 560, 560, 2.4), .8)
    show(img, t, 1.4, lambda r, m: (D(r, m).rr([1000, 700, 1800, 800], 20, SAGE_D), D(r, m).tx((1400, 750), "YOUR HOME + THE LOT", font(FONT_SANS, 50), GREEN_D)), .6)
    stamp(img, 1400, 400, seg(t, 2.4, .6), "NOT COUNTED", GOLD, -6, 70)
    txt_in(img, t, 3.6, (W // 2, 950), "EVEN IF IT'S WORTH A LOT", 1 and 46, SAGE)


def b22b(img, t):
    title(img, t, "ALSO NOT COUNTED")
    items = [(500, lambda r, m, cx, cy: (D(r, m).rr([cx - 120, cy - 70, cx + 120, cy + 90], 20, BROWN), D(r, m).rr([cx - 50, cy - 110, cx + 50, cy - 70], 12, SAGE_D), D(r, m).tx((cx, cy + 10), "401", font(FONT_SERIF, 70), GOLD)), "RETIREMENT + PENSION PLANS"),
             (1420, lambda r, m, cx, cy: (D(r, m).rr([cx - 150, cy - 90, cx + 150, cy + 90], 20, IVORY), D(r, m).tx((cx, cy - 30), "S S I", font(FONT_SANS, 70), GREEN_D), D(r, m).tx((cx, cy + 40), "BENEFIT CARD", font(FONT_SANS_M, 30), SAGE_D)), "RESOURCES OF S S I RECEIVERS")]
    for i, (cx, ic, lab) in enumerate(items):
        st = .4 + i * 1.6
        show(img, t, st, lambda r, m, cx=cx, ic=ic, lab=lab: (D(r, m).rr([cx - 330, 230, cx + 330, 790], 40, CARD, SAGE_D, 4), ic(r, m, cx, 440), D(r, m).tx((cx, 700), lab, font(FONT_SANS, 34), IVORY)), .7)
        glow_check(img, t, cx + 270, 290, st + .6)
    txt_in(img, t, 4.2, (W // 2, 930), "MOST OF THEM", 60, GOLD)


def b22c(img, t):
    title(img, t, "OWNING YOUR HOUSE")
    show(img, t, .3, lambda r, m: house(r, m, 560, 580, 2.2), .8)
    tk = ease_back(seg(t, 1.2, .6))
    if tk > 0: pop(img, lambda r, m: (D(r, m).el([880, 230, 1040, 390], SAGE), tick(r, m, 960, 310, 1.8, GREEN_D)), tk, a=ease(seg(t, 1.2, .2)))
    show(img, t, 2.0, lambda r, m: D(r, m).tx((1380, 420), "NOT A REASON", font(FONT_SANS, 78), IVORY), .6)
    show(img, t, 2.6, lambda r, m: D(r, m).tx((1380, 530), "TO SKIP SNAP", font(FONT_SANS, 78), GOLD), .6)
    txt_in(img, t, 4.0, (1380, 700), "IT NEVER WAS", 90, RED)


# ============ 23: auto (674)
def b23a(img, t):
    title(img, t, "WHAT ABOUT YOUR CAR?")
    show(img, t, .3, lambda r, m: car(r, m, 560, 520, 2.8), .8, dx=0)
    show(img, t, 1.6, lambda r, m: D(r, m).tx((1330, 380), "?", font(FONT_SERIF, 360), GOLD), .7)
    show(img, t, 2.8, lambda r, m: (stateshape(r, m, 1500, 700, 1.1), D(r, m).tx((1500, 860), "RULES DEPEND ON YOUR STATE", font(FONT_SANS, 34), IVORY)), .6)
    txt_in(img, t, 3.6, (560, 900), "VEHICLES CAN COUNT", 56, IVORY)


def b23b(img, t):
    title(img, t, "WHEN A CAR IS NOT COUNTED")
    show(img, t, .3, lambda r, m: (D(r, m).rr([150, 220, 940, 880], 40, CARD, SAGE_D, 4), car(r, m, 545, 450, 2.0), D(r, m).tx((545, 760), "NEEDED FOR A DISABLED MEMBER", font(FONT_SANS, 34), IVORY)), .7)
    glow_check(img, t, 880, 270, 1.2)
    show(img, t, 2.6, lambda r, m: (D(r, m).rr([980, 220, 1770, 880], 40, CARD, SAGE_D, 4), car(r, m, 1375, 400, 1.5), price_tag(r, m, 1375, 600, "< $1,500", 400, 130), D(r, m).tx((1375, 760), "IF SELLING IT BRINGS LESS", font(FONT_SANS, 34), IVORY)), .7)
    glow_check(img, t, 1710, 270, 3.4)


def b23c(img, t):
    title(img, t, "ONE VEHICLE PER ADULT")
    for i in range(2):
        show(img, t, .4 + i * .8, lambda r, m, i=i: (person(r, m, 330 + i * 360, 480, 1.4), car(r, m, 330 + i * 360, 780, 1.0)), .6)
        glow_check(img, t, 470 + i * 360, 300, 1.0 + i * .8)
    txt_in(img, t, 2.6, (540, 960), "EXCLUDED FROM THE EQUITY TEST", 44, GOLD)
    show(img, t, 3.6, lambda r, m: (interviewer(r, m, 1500, 600, 1.4), bubble(r, m, 1420, 280, 600, 170, "left") or D(r, m).tx((1420, 282), "HOW DO YOU COUNT MINE?", font(FONT_SANS, 34), GOLD)), .6)
    txt_in(img, t, 5.0, (1500, 900), "ASK YOUR OFFICE", 56, IVORY)


# ============ 24: stati piu generosi (467)
def b24a(img, t):
    title(img, t, "SOME STATES ARE MORE GENEROUS")
    pos = [(380, 520), (700, 380), (1020, 560), (1340, 400), (1620, 600)]
    for i, (x, y) in enumerate(pos):
        gold = i in (1, 3, 4)
        show(img, t, .4 + i * .4, lambda r, m, x=x, y=y, gold=gold: stateshape(r, m, x, y, 1.5, GOLD if gold else SAGE_D), .6)
    txt_in(img, t, 3.2, (W // 2, 840), "BROAD BASED CATEGORICAL ELIGIBILITY", 58, IVORY)
    txt_in(img, t, 4.0, (W // 2, 930), "MOST STATES USE IT", 44, GOLD)


def b24b(img, t):
    title(img, t, "KEEP MORE IN SAVINGS")
    x0, tw = 260, 1400
    txt_in(img, t, .3, (x0 + 330, 290), "FEDERAL NUMBERS", 40, SAGE)
    barpair(img, t, .5, x0, 380, tw, [(4750, SAGE_D)], 9000, 90, 1.2)
    txt_in(img, t, 2.2, (x0 + 400, 560), "SOME STATES ALLOW MORE", 40, GOLD)
    barpair(img, t, 2.4, x0, 650, tw, [(4750, SAGE_D), (3500, GOLD)], 9000, 90, 1.6)
    txt_in(img, t, 4.2, (x0 + tw * 6500 / 9000, 790), "MORE ROOM", 60, GOLD)


def b24c(img, t):
    title(img, t, "BUT THE OTHER RULES STILL APPLY")
    for i, lab in enumerate(["INCOME LIMITS", "NON FINANCIAL RULES", "ASK YOUR STATE"]):
        st = .4 + i * 1.1
        show(img, t, st, lambda r, m, i=i, lab=lab: (D(r, m).rr([420, 250 + i * 190, 1500, 400 + i * 190], 34, CARD, SAGE_D if i < 2 else GOLD, 5), D(r, m).tx((960, 325 + i * 190), lab, font(FONT_SANS, 52), IVORY if i < 2 else GOLD)), .6)
        glow_check(img, t, 1420, 325 + i * 190, st + .5)
    txt_in(img, t, 4.2, (W // 2, 900), "IT COULD MATTER", 80, GOLD)


# ============ 25: nucleo familiare (770)
def b25a(img, t):
    title(img, t, "WHO'S IN YOUR HOUSEHOLD?")
    show(img, t, .3, lambda r, m: house(r, m, 560, 540, 2.3), .8)
    show(img, t, 1.2, lambda r, m: [person(r, m, 440 + i * 120, 900, .55) for i in range(4)], .6)
    for i, lab in enumerate(["LIVE TOGETHER", "BUY FOOD TOGETHER", "PREPARE IT TOGETHER"]):
        st = 2.0 + i * 1.3
        show(img, t, st, lambda r, m, i=i, lab=lab: (D(r, m).rr([1130, 250 + i * 190, 1800, 400 + i * 190], 30, CARD, GOLD, 5), D(r, m).tx((1465, 325 + i * 190), lab, font(FONT_SANS, 42), IVORY)), .6)
        glow_check(img, t, 1740, 280 + i * 190, st + .5)


def b25b(img, t):
    title(img, t, "THE SPOUSE IS ALWAYS INCLUDED")
    show(img, t, .3, lambda r, m: (person(r, m, 700, 470, 1.9), person(r, m, 1000, 470, 1.9)), .8)
    show(img, t, 1.4, lambda r, m: D(r, m).tx((850, 800), "SPOUSE", font(FONT_SANS, 60), GOLD), .5)
    stamp(img, 960, 940, seg(t, 2.6, .6), "THE TWIST", GOLD, -5, 70)


def b25c(img, t):
    title(img, t, "A SEPARATE HOUSEHOLD")
    show(img, t, .3, lambda r, m: house(r, m, 600, 450, 2.1), .7)
    show(img, t, 1.0, lambda r, m: [person(r, m, 380 + i * 110, 850, .6) for i in range(2)], .5)
    ov = ease(seg(t, 2.0, 1.0))
    if ov > 0:
        lay = new_layer(); D(*lay).el([310, 700, 650, 960], None, GOLD, 8); alpha_layer(img, lay, ov)
    txt_in(img, t, 2.6, (480, 990), "60+ AND SPOUSE", 38, GOLD)
    show(img, t, 3.6, lambda r, m: (D(r, m).rr([1120, 220, 1830, 560], 36, CARD, GOLD, 6), D(r, m).tx((1475, 330), "CAN'T PREPARE MEALS", font(FONT_SANS, 40), IVORY), D(r, m).tx((1475, 400), "SEPARATELY BECAUSE OF A", font(FONT_SANS, 40), IVORY), D(r, m).tx((1475, 470), "PERMANENT DISABILITY", font(FONT_SANS, 40), GOLD)), .7)
    show(img, t, 6.2, lambda r, m: (D(r, m).rr([1120, 640, 1830, 940], 36, CARD, SAGE, 6), D(r, m).tx((1475, 740), "OTHERS EARN AT MOST", font(FONT_SANS, 40), IVORY), D(r, m).tx((1475, 840), "165%", font(FONT_SERIF, 130), GOLD)), .7)
    txt_in(img, t, 7.2, (1475, 970), "OF THE POVERTY LEVEL", 36, SAGE)


# ============ 26: 32% (547)
def b26a(img, t):
    title(img, t, "WHY DOES THAT MATTER?")
    show(img, t, .3, lambda r, m: house(r, m, 480, 520, 2.0), .8)
    show(img, t, 1.2, lambda r, m: D(r, m).tx((1330, 420), "32%", font(FONT_SERIF, 400), GOLD), .9)
    txt_in(img, t, 2.4, (1330, 680), "OF ELIGIBLE SENIORS", 58, IVORY)
    txt_in(img, t, 3.1, (1330, 770), "WHO LIVE WITH OTHER PEOPLE", 46, IVORY)
    txt_in(img, t, 4.0, (1330, 880), "PARTICIPATE · U S D A DATA", 36, SAGE, sans_m=True)


def b26b(img, t):
    title(img, t, "ONE IN THREE")
    for i in range(3):
        person2(img_r := None, None, 0, 0) if False else None
    lay = new_layer(); g = D(*lay)
    for i in range(3):
        person2(lay[0], lay[1], 480 + i * 480, 560, 2.4, GOLD if i == 0 else SAGE_D)
    alpha_layer(img, lay, 1)
    txt_in(img, t, 0, (W // 2, 930), "ONE IN THREE", 90, GOLD)


def b26c(img, t):
    title(img, t, "THEY ASSUME THEY CAN'T QUALIFY")
    show(img, t, .3, lambda r, m: [person(r, m, 330, 640, 2.0), person2(r, m, 620, 700, 1.2, GOLD)], .7)
    show(img, t, 1.2, lambda r, m: bubble(r, m, 1150, 330, 700, 200, "left") or D(r, m).tx((1150, 332), "I CAN'T QUALIFY", font(FONT_SANS, 54), IVORY), .6)
    xm = ease_back(seg(t, 2.2, .5))
    if xm > 0: pop(img, lambda r, m: xmark(r, m, 1560, 330, 1.5), xm, a=ease(seg(t, 2.2, .2)))
    show(img, t, 4.2, lambda r, m: D(r, m).tx((1250, 720), "SOMETIMES THEY CAN", font(FONT_SANS, 82), GOLD), .7)


# ============ 27: lavoro (406)
def b27a(img, t):
    title(img, t, "WORRIED ABOUT WORK RULES?")
    def briefcase(r, m, cx, cy, s=1.0):
        g = D(r, m); g.rr([cx - 140 * s, cy - 80 * s, cx + 140 * s, cy + 90 * s], int(20 * s), BROWN); g.rr([cx - 50 * s, cy - 120 * s, cx + 50 * s, cy - 76 * s], int(10 * s), None, SAGE_D, int(10 * s)); g.rc([cx - 140 * s, cy - 10 * s, cx + 140 * s, cy + 6 * s], (110, 76, 44)); g.rr([cx - 20 * s, cy - 24 * s, cx + 20 * s, cy + 24 * s], 6, GOLD)
    show(img, t, .3, lambda r, m: briefcase(r, m, 560, 520, 2.4), .8)
    show(img, t, 1.4, lambda r, m: D(r, m).tx((1380, 400), "GOOD NEWS", font(FONT_SANS, 110), GOLD), .7)
    txt_in(img, t, 2.4, (1380, 560), "FOR ELDERLY HOUSEHOLDS", 52, IVORY)


def b27b(img, t):
    title(img, t, "NO WORK REQUIREMENTS")
    show(img, t, .3, lambda r, m: (house(r, m, 480, 590, 1.6), [person(r, m, 430 + i * 100, 930, .5) for i in range(2)]), .8)
    stamp(img, 480, 240, seg(t, 1.2, .5), "ELDERLY OR DISABLED", GOLD, -3, 40)
    for i, lab in enumerate(["NO JOB SEARCH", "NO HOURS TO LOG"]):
        st = 1.6 + i * 1.3
        show(img, t, st, lambda r, m, i=i, lab=lab: (D(r, m).rr([1000, 300 + i * 220, 1790, 470 + i * 220], 34, CARD, SAGE, 5), D(r, m).tx((1395, 385 + i * 220), lab, font(FONT_SANS, 56), IVORY)), .6)
        pop(img, lambda r, m, i=i: xmark(r, m, 1710, 385 + i * 220, .8), ease_back(seg(t, st + .5, .4)), a=ease(seg(t, st + .5, .2)))


# ============ 28: come fare domanda (826)
def b28a(img, t):
    title(img, t, "HOW TO APPLY · THREE STEPS")
    xs = [330, 960, 1590]; labs = ["FIND YOUR STATE", "SUBMIT THE APPLICATION", "THE INTERVIEW"]
    for i, (x, lab) in enumerate(zip(xs, labs)):
        st = .5 + i * 1.2
        show(img, t, st, lambda r, m, x=x, lab=lab, i=i: (D(r, m).el([x - 130, 300, x + 130, 560], GOLD), D(r, m).tx((x, 430), str(i + 1), font(FONT_SERIF, 200), GREEN_D), D(r, m).tx((x, 680), lab, font(FONT_SANS, 40), IVORY)), .7)
        if i < 2:
            ar = ease(seg(t, st + .6, .4))
            if ar > 0:
                lay = new_layer(); D(*lay).pg([(x + 170, 405), (x + 270, 405), (x + 270, 370), (x + 340, 430), (x + 270, 490), (x + 270, 455), (x + 170, 455)], SAGE); alpha_layer(img, lay, ar)
    txt_in(img, t, 4.6, (W // 2, 900), "YOU'VE SEEN THE RULES · NOW ACT", 60, GOLD)


def b28b(img, t):
    title(img, t, "STEP ONE · FIND YOUR STATE")
    show(img, t, .3, lambda r, m: price_tag(r, m, 420, 300, "STEP 1", 560, 220), .8, angle=-4)
    for i, (x, y) in enumerate(((900, 360), (1200, 520), (1500, 360), (1000, 700), (1350, 740))):
        show(img, t, 1.0 + i * .4, lambda r, m, x=x, y=y, i=i: (stateshape(r, m, x, y, 1.5, GOLD if i == 2 else SAGE_D), paper(r, m, x + 10, y + 5, .5, "", IVORY)), .5)
    txt_in(img, t, 3.6, (W // 2, 930), "EVERY STATE HAS ITS OWN FORM", 56, IVORY)


def b28c(img, t):
    title(img, t, "CALL THE SNAP INFORMATION LINE")
    show(img, t, .3, lambda r, m: phone(r, m, 480, 520, 4.0), .8, dy=math.sin(t * 9) * 4 if t < 2.0 else 0)
    show(img, t, 1.2, lambda r, m: D(r, m).tx((1260, 400), "1-800-221-5689", font(FONT_SERIF, 150), GOLD), .8)
    txt_in(img, t, 2.4, (1260, 580), "SNAP TOLL FREE INFORMATION NUMBER", 40, IVORY)
    txt_in(img, t, 3.4, (1260, 660), "U S D A", 44, SAGE)


def b28d(img, t):
    title(img, t, "OR GO ONLINE")
    def browser(r, m):
        g = D(r, m)
        g.rr([220, 220, 1700, 900], 30, CARD, SAGE_D, 6); g.rr([220, 220, 1700, 320], 30, SAGE_D); g.rc([220, 290, 1700, 320], SAGE_D)
        for i in range(3): g.el([260 + i * 50, 255, 290 + i * 50, 285], [RED, GOLD, SAGE][i])
        g.rr([440, 235, 1650, 305], 20, GREEN_D); g.tx((1045, 270), "fns.usda.gov/snap/state-directory", font(FONT_SANS, 40), GOLD)
    show(img, t, .3, browser, .7)
    show(img, t, 1.4, lambda r, m: building(r, m, 560, 560, 1.0), .7)
    for i in range(4):
        show(img, t, 2.2 + i * .35, lambda r, m, i=i: (D(r, m).rr([1000, 400 + i * 100, 1620, 480 + i * 100], 16, SAGE_D if i != 1 else GOLD), D(r, m).tx((1310, 440 + i * 100), ["ALABAMA", "YOUR STATE", "ALASKA", "ARIZONA"][i], font(FONT_SANS, 36), GREEN_D)), .4)
    txt_in(img, t, 4.4, (W // 2, 970), "U S D A STATE DIRECTORY", 44, IVORY)


# ============ 29: passo 2 (612)
def b29a(img, t):
    title(img, t, "STEP TWO · SUBMIT THE APPLICATION")
    show(img, t, .3, lambda r, m: price_tag(r, m, 420, 290, "STEP 2", 560, 220), .8, angle=-4)
    tl = [(400, office, "IN PERSON"), (960, lambda r, m, cx, cy, s: laptop(r, m, cx, cy - 20, .6), "ONLINE"), (1520, phone, "BY PHONE")]
    for i, (cx, ic, lab) in enumerate(tl):
        st = 1.0 + i * 1.2
        show(img, t, st, lambda r, m, cx=cx, ic=ic, lab=lab: (D(r, m).rr([cx - 250, 430, cx + 250, 860], 36, CARD, SAGE_D, 4), ic(r, m, cx, 620, 1.0), D(r, m).tx((cx, 800), lab, font(FONT_SANS, 44), IVORY)), .6)
    txt_in(img, t, 4.8, (1280, 300), "YOUR CHOICE", 60, GOLD)


def b29b(img, t):
    title(img, t, "HEAR THIS CAREFULLY")
    show(img, t, .3, lambda r, m: (calendar2(r, m, 1500, 480, 1.6, "DAY 1", 52), D(r, m).tx((1500, 760), "DATE YOU APPLIED", font(FONT_SANS, 40), IVORY)), .7)
    show(img, t, 1.2, lambda r, m: (calendar2(r, m, 420, 480, 1.6, "LATER", 52), D(r, m).tx((420, 760), "APPROVAL ARRIVES", font(FONT_SANS, 40), IVORY)), .7)
    ar = ease(seg(t, 2.4, 1.2))
    if ar > 0:
        lay = new_layer(); g = D(*lay); x1 = 1380 - 780 * ar
        g.ln([(1380, 470), (x1, 470)], GOLD, 24); g.pg([(x1, 410), (x1 - 80, 470), (x1, 530)], GOLD); alpha_layer(img, lay, 1)
    txt_in(img, t, 3.8, (960, 250), "BENEFITS GO BACK", 70, GOLD)
    txt_in(img, t, 5.0, (W // 2, 930), "TO THE DATE YOU APPLIED", 70, IVORY)


def b29c(img, t):
    title(img, t, "APPLY FIRST · FIX THE DETAILS LATER")
    for i in range(4):
        show(img, t, .3 + i * .3, lambda r, m, i=i: paper(r, m, 330 + i * 120, 480 + (i % 2) * 20, 1.3, "", IVORY), .5, angle=(-1) ** i * 6)
    show(img, t, 2.0, lambda r, m: D(r, m).tx((1300, 380), "DON'T WAIT", font(FONT_SANS, 100), RED), .7)
    show(img, t, 3.0, lambda r, m: D(r, m).tx((1300, 520), "FOR EVERY PAPER", font(FONT_SANS, 76), IVORY), .6)
    show(img, t, 4.2, lambda r, m: price_tag(r, m, 1300, 760, "APPLY FIRST", 700, 190), .7, angle=-3)


# ============ 30: colloquio (596)
def b30a(img, t):
    title(img, t, "STEP THREE · THE INTERVIEW")
    show(img, t, .3, lambda r, m: price_tag(r, m, 420, 290, "STEP 3", 560, 220), .8, angle=-4)
    show(img, t, 1.2, lambda r, m: (phone(r, m, 520, 700, 2.0)), .7, dy=math.sin(t * 8) * 4 if t < 2.4 else 0)
    show(img, t, 2.4, lambda r, m: (calendar(r, m, 1300, 500, 1.6, "30"), D(r, m).tx((1300, 780), "DAYS FOR A DECISION", font(FONT_SANS, 44), IVORY)), .7)
    txt_in(img, t, 1.8, (520, 930), "USUALLY BY PHONE", 44, GOLD)


def b30b(img, t):
    title(img, t, "BRING PROOF OF")
    tl = [(380, taxbill, "INCOME"), (860, key, "RENT"), (1340, bulb, "UTILITY BILLS"), (1700, cross, "MEDICAL COSTS")]
    tl = [(260, paycheck, "INCOME"), (700, key, "RENT"), (1140, bulb, "UTILITY BILLS"), (1580, cross, "MEDICAL COSTS")]
    for i, (cx, ic, lab) in enumerate(tl):
        st = .4 + i * 1.0
        def draw(r, m, cx=cx, ic=ic, lab=lab, i=i):
            D(r, m).rr([cx - 190, 260, cx + 190, 760], 34, CARD, GOLD if i == 3 else SAGE_D, 5)
            if ic is paycheck: paycheck(r, m, cx, 480, .7, "$$$")
            elif ic is cross: cross(r, m, cx, 470, 80)
            else: ic(r, m, cx, 480, 1.3)
            D(r, m).tx((cx, 690), lab, font(FONT_SANS, 30), IVORY)
        show(img, t, st, draw, .6)
        glow_check(img, t, cx + 150, 310, st + .5)
    txt_in(img, t, 4.8, (W // 2, 900), "YES · EVEN YOUR MEDICAL COSTS", 60, GOLD)


def b30c(img, t):
    title(img, t, "SAY IT OUT LOUD")
    show(img, t, .3, lambda r, m: person(r, m, 430, 640, 2.3), .7)
    show(img, t, 1.0, lambda r, m: bubble(r, m, 1130, 330, 760, 230, "left") or (D(r, m).tx((1130, 300), "I HAVE MEDICAL", font(FONT_SANS, 54), IVORY), D(r, m).tx((1130, 370), "EXPENSES", font(FONT_SANS, 54), GOLD)), .6)
    show(img, t, 2.2, lambda r, m: cross(r, m, 1560, 330, 70), .5)
    txt_in(img, t, 3.4, (1260, 700), "NOBODY CAN DEDUCT", 60, IVORY)
    txt_in(img, t, 4.2, (1260, 790), "WHAT THEY DON'T KNOW ABOUT", 52, GOLD)


# ============ 31: expedited (541)
def b31a(img, t):
    title(img, t, "NEED MONEY SOONER?")
    show(img, t, .3, lambda r, m: (D(r, m).el([220, 250, 520, 550], IVORY), D(r, m).ln([(370, 400), (370, 300)], GREEN_D, 14), D(r, m).ln([(370, 400), (450, 440)], GREEN_D, 14)), .7)
    show(img, t, 1.2, lambda r, m: (D(r, m).rr([680, 250, 1250, 560], 36, CARD, GOLD, 6), D(r, m).tx((965, 350), "LESS THAN", font(FONT_SANS, 40), SAGE), D(r, m).tx((965, 440), "$100", font(FONT_SERIF, 130), GOLD), D(r, m).tx((965, 525), "IN CASH", font(FONT_SANS, 36), IVORY)), .7)
    show(img, t, 2.6, lambda r, m: (D(r, m).rr([1330, 250, 1800, 560], 36, CARD, GOLD, 6), D(r, m).tx((1565, 350), "UNDER", font(FONT_SANS, 40), SAGE), D(r, m).tx((1565, 440), "$150", font(FONT_SERIF, 130), GOLD), D(r, m).tx((1565, 525), "MONTHLY INCOME", font(FONT_SANS, 30), IVORY)), .7)
    txt_in(img, t, 4.2, (W // 2, 800), "AND", 80, IVORY)


def b31b(img, t):
    title(img, t, "OR")
    show(img, t, .3, lambda r, m: (D(r, m).rr([250, 250, 900, 700], 40, CARD, SAGE_D, 5), D(r, m).tx((575, 380), "INCOME + CASH", font(FONT_SANS, 56), IVORY), coin(r, m, 575, 540, 90)), .7)
    show(img, t, 1.6, lambda r, m: D(r, m).tx((960, 480), "<", font(FONT_SERIF, 200), GOLD), .6)
    show(img, t, 2.4, lambda r, m: (D(r, m).rr([1020, 250, 1670, 700], 40, CARD, RED, 5), D(r, m).tx((1345, 380), "RENT + UTILITIES", font(FONT_SANS, 50), IVORY), house(r, m, 1345, 590, .8)), .7)
    txt_in(img, t, 3.8, (W // 2, 880), "LESS THAN WHAT YOU PAY TO LIVE", 56, GOLD)


def b31c(img, t):
    title(img, t, "BENEFITS WITHIN SEVEN DAYS")
    show(img, t, .3, lambda r, m: calendar(r, m, 520, 470, 2.0, "7"), .8)
    show(img, t, 1.4, lambda r, m: D(r, m).tx((520, 810), "DAYS", font(FONT_SANS, 70), GOLD), .5)
    show(img, t, 2.4, lambda r, m: (D(r, m).rr([1000, 330, 1800, 560], 36, CARD, GOLD, 6), D(r, m).tx((1400, 445), "ASK FOR IT BY NAME", font(FONT_SANS, 50), IVORY)), .7)
    stamp(img, 1400, 740, seg(t, 3.8, .6), "EXPEDITED", GOLD, -5, 96)


# ============ 32: rappresentante e ricertificazione (566)
def b32a(img, t):
    title(img, t, "CAN'T LEAVE THE HOUSE?")
    show(img, t, .3, lambda r, m: house(r, m, 420, 520, 2.0), .8)
    show(img, t, 1.4, lambda r, m: (person(r, m, 1100, 650, 1.8), D(r, m).rr([850, 210, 1350, 300], 24, GOLD), D(r, m).tx((1100, 255), "TRUSTED PERSON", font(FONT_SANS, 40), GREEN_D)), .7)
    ar = ease(seg(t, 2.6, 1.2))
    if ar > 0:
        lay = new_layer(); D(*lay).pg([(680, 600), (790, 600), (790, 560), (880, 640), (790, 720), (790, 680), (680, 680)], GOLD); alpha_layer(img, lay, ar)
    txt_in(img, t, 3.4, (W // 2, 930), "AUTHORIZED REPRESENTATIVE", 66, GOLD)


def b32b(img, t):
    title(img, t, "CHOOSE THEM IN WRITING")
    show(img, t, .3, lambda r, m: (paper(r, m, 700, 520, 2.6, "DESIGNATION", IVORY)), .8, angle=-3)
    sg = ease(seg(t, 1.6, 1.2))
    if sg > 0:
        lay = new_layer(); g = D(*lay); pts = [(580 + 22 * i, 700 - 30 * math.sin(i * .9)) for i in range(int(14 * sg) + 1)]
        if len(pts) > 1: g.ln(pts, GREEN_D, 8)
        alpha_layer(img, lay, 1)
    show(img, t, 2.6, lambda r, m: D(r, m).tx((1450, 420), "IN WRITING", font(FONT_SANS, 100), GOLD), .7)
    glow_check(img, t, 1450, 600, 3.4)


def b32c(img, t):
    title(img, t, "RECERTIFY BEFORE IT ENDS")
    show(img, t, .3, lambda r, m: (paper(r, m, 400, 470, 2.0, "NOTICE", IVORY), D(r, m).tx((400, 760), "CERTIFICATION PERIOD", font(FONT_SANS, 34), IVORY)), .7)
    show(img, t, 1.6, lambda r, m: calendar2(r, m, 1300, 470, 2.0, "END", 62), .8)
    ov = ease(seg(t, 3.0, .8))
    if ov > 0:
        lay = new_layer(); D(*lay).el([1050, 220, 1550, 720], None, RED, 12); alpha_layer(img, lay, ov)
    txt_in(img, t, 4.0, (1300, 800), "MARK THAT DATE", 70, GOLD)


# ============ 33: errori (601)
def b33a(img, t):
    title(img, t, "THE BIGGEST MISTAKES")
    numcard(img, t, .4, 560, 520, 1, "DECIDING YOU'RE", "OVER THE LIMIT", RED, 800, 360)
    show(img, t, 1.6, lambda r, m: stopsign(r, m, 1480, 440, 1.8), .7)
    txt_in(img, t, 3.0, (W // 2, 880), "LET THE STATE DECIDE", 80, GOLD)


def b33b(img, t):
    title(img, t, "MISTAKES TWO AND THREE")
    numcard(img, t, .4, 500, 480, 2, "FORGETTING MEDICAL", "COSTS + PREMIUMS", RED, 780, 360)
    numcard(img, t, 1.8, 1420, 480, 3, "SKIPPING THE", "INTERVIEW", RED, 780, 360)
    for cx, st in ((500, 1.2), (1420, 2.6)): pop(img, lambda r, m, cx=cx: xmark(r, m, cx + 330, 270, .8), ease_back(seg(t, st, .4)), a=ease(seg(t, st, .2)))


def b33c(img, t):
    title(img, t, "MISTAKE FOUR")
    numcard(img, t, .4, 560, 480, 4, "MISSING YOUR", "RECERTIFICATION DATE", RED, 840, 360)
    show(img, t, 1.4, lambda r, m: calendar(r, m, 1480, 480, 1.8, "!"), .7)
    stamp(img, W // 2, 880, seg(t, 2.8, .6), "ANY OF THESE CAN COST YOU", RED, -3, 56)


# ============ 34: nuova legge (552)
def b34a(img, t):
    title(img, t, "ONE MORE THING YOU SHOULD KNOW")
    show(img, t, .3, lambda r, m: (paper(r, m, 520, 480, 2.4, "NEW LAW", IVORY), D(r, m).tx((520, 880), "2025", font(FONT_SERIF, 110), GOLD)), .8, angle=-3)
    for i, lab in enumerate(["WORK REQUIREMENTS", "NON CITIZEN RULES"]):
        st = 1.8 + i * 1.4
        show(img, t, st, lambda r, m, i=i, lab=lab: (D(r, m).rr([1000, 300 + i * 200, 1800, 460 + i * 200], 34, CARD, GOLD, 5), D(r, m).tx((1400, 380 + i * 200), lab, font(FONT_SANS, 50), IVORY)), .6)
    txt_in(img, t, 5.0, (1400, 760), "CHANGED SOME RULES", 56, GOLD)


def b34b(img, t):
    title(img, t, "STILL UPDATING ITS PAGES")
    show(img, t, .3, lambda r, m: building(r, m, 480, 520, 1.2), .8)
    def page(r, m):
        g = D(r, m); g.rr([1000, 260, 1760, 820], 30, CARD, SAGE_D, 5)
        for i in range(5): g.ln([(1060, 360 + i * 70), (1700 - (i % 2) * 120, 360 + i * 70)], SAGE_D, 12)
    show(img, t, 1.0, page, .7)
    pg = ease(seg(t, 1.6, 2.4))
    lay = new_layer(); g = D(*lay); g.rr([1060, 740, 1700, 770], 14, SAGE_D); g.rr([1060, 740, 1060 + 640 * pg * .7, 770], 14, GOLD); alpha_layer(img, lay, 1)
    txt_in(img, t, 2.4, (1380, 300), "SNAP ELIGIBILITY", 44, IVORY)
    txt_in(img, t, 3.6, (W // 2, 930), "THE U S D A IS STILL UPDATING", 56, GOLD)


def b34c(img, t):
    title(img, t, "ALWAYS CONFIRM THE CURRENT RULES")
    show(img, t, .3, lambda r, m: phone(r, m, 480, 520, 3.4), .8)
    show(img, t, 1.2, lambda r, m: (office(r, m, 1300, 480, 1.7)), .8)
    txt_in(img, t, 2.4, (1300, 760), "YOUR STATE SNAP OFFICE", 56, GOLD)
    txt_in(img, t, 3.6, (W // 2, 930), "BEFORE YOU DECIDE", 70, IVORY)


# ============ 35: riepilogo (718)
def b35a(img, t):
    title(img, t, "LET'S RECAP")
    numcard(img, t, .4, 560, 440, 1, "AT SIXTY", "SKIP THE GROSS TEST", GOLD, 900, 360)
    show(img, t, 1.4, lambda r, m: (gate(r, m, 1500, 420, 1.5, RED), D(r, m).tx((1500, 760), "GROSS INCOME TEST", font(FONT_SANS, 44), IVORY)), .7)
    pop(img, lambda r, m: xmark(r, m, 1500, 240, 1.6), ease_back(seg(t, 2.6, .5)), a=ease(seg(t, 2.6, .2)))
    show(img, t, 3.4, lambda r, m: price_tag(r, m, 560, 780, "60+", 340, 150), .6)


def b35b(img, t):
    title(img, t, "LET'S RECAP")
    numcard(img, t, .4, 560, 440, 2, "MEDICAL COSTS OVER $35", "COME OFF YOUR INCOME", GOLD, 900, 360)
    show(img, t, 1.2, lambda r, m: cross(r, m, 1500, 380, 110), .7)
    show(img, t, 2.6, lambda r, m: (house(r, m, 560, 790, .75), D(r, m).tx((1050, 800), "SHELTER COSTS · NO CAP", font(FONT_SANS, 56), IVORY)), .7)


def b35c(img, t):
    title(img, t, "LET'S RECAP")
    numcard(img, t, .4, 560, 440, 3, "KEEP $4,750 IN SAVINGS", "YOUR HOME DOESN'T COUNT", GOLD, 900, 360)
    show(img, t, 1.2, lambda r, m: piggy(r, m, 1500, 420, 1.6), .7)
    show(img, t, 2.6, lambda r, m: house(r, m, 1500, 780, .7), .7)
    stamp(img, 560, 780, seg(t, 3.0, .6), "NOT COUNTED", GOLD, -5, 60)


def b35d(img, t):
    title(img, t, "THEN")
    xs = [330, 960, 1590]; labs = [("CALL", phone), ("APPLY", paper), ("LET YOUR STATE", None)]
    items = [("CALL", lambda r, m, cx, cy: phone(r, m, cx, cy, 1.5)), ("APPLY", lambda r, m, cx, cy: paper(r, m, cx, cy, 1.3, "", IVORY)), ("DECIDE", lambda r, m, cx, cy: building(r, m, cx, cy, .7, "STATE"))]
    for i, (x, (lab, ic)) in enumerate(zip(xs, items)):
        st = .4 + i * 1.5
        show(img, t, st, lambda r, m, x=x, lab=lab, ic=ic: (D(r, m).rr([x - 270, 240, x + 270, 800], 40, CARD, GOLD, 5), ic(r, m, x, 480), D(r, m).tx((x, 720), lab, font(FONT_SANS, 60), GOLD)), .7)
    txt_in(img, t, 5.2, (W // 2, 920), "AND LET YOUR STATE DECIDE", 70, IVORY)


# ============ 36: invito a like e iscrizione (544)
def b36a(img, t):
    title(img, t, "KNOW SOMEONE OVER SIXTY?")
    labs = ["A PARENT", "A NEIGHBOR", "A FRIEND"]
    for i, lab in enumerate(labs):
        st = .4 + i * 1.0
        show(img, t, st, lambda r, m, i=i, lab=lab: (D(r, m).rr([150 + i * 560, 230, 650 + i * 560, 840], 40, CARD, SAGE_D, 4), person2(r, m, 400 + i * 560, 520, 1.8, [SAGE, GOLD, SAGE][i]), D(r, m).tx((400 + i * 560, 760), lab, font(FONT_SANS, 46), IVORY)), .7)
    txt_in(img, t, 4.4, (W // 2, 930), "WHO ISN'T GETTING THIS?", 66, GOLD)


def b36b(img, t):
    title(img, t, "HIT THE LIKE BUTTON")
    p = 1 + .12 * math.sin(t * 5)
    show(img, t, .3, lambda r, m: thumb(r, m, 700, 520, 3.0), .8, dy=-20 * math.sin(t * 4))
    for k in range(7):
        pp = seg(t, 1.0 + k * .4, 1.6)
        if 0 < pp < 1:
            pop(img, lambda r, m, k=k: D(r, m).tx((560 + k * 70, 330), "+1", font(FONT_SANS, 60), RED), 1.0, a=min(1, pp * 5) * (1 - ease(seg(pp, .7, .3))), dy=-170 * ease(pp), dx=(k - 3) * 15)
    txt_in(img, t, 1.6, (1470, 400), "IT HELPS US", 80, IVORY)
    txt_in(img, t, 2.2, (1470, 520), "MORE THAN YOU IMAGINE", 40, GOLD)


def b36c(img, t):
    title(img, t, "THE SENIOR ADVANTAGE")
    show(img, t, .3, lambda r, m: (D(r, m).rr([420, 300, 1500, 520], 60, RED), D(r, m).tx((960, 410), "SUBSCRIBE", font(FONT_SANS, 120), IVORY)), .8, dy=0)
    if t > 2.2:
        lay = new_layer(); g = D(*lay); g.rr([420, 300, 1500, 520], 60, SAGE); g.tx((960, 410), "SUBSCRIBED", font(FONT_SANS, 120), GREEN_D); alpha_layer(img, lay, ease(seg(t, 2.2, .3)))
    cp = ease(seg(t, 1.4, .8))
    if cp > 0:
        lay = new_layer(); g = D(*lay); x = 1450 - 220 * cp; y = 600 - 170 * cp
        g.pg([(x, y), (x, y + 90), (x + 25, y + 66), (x + 48, y + 112), (x + 66, y + 104), (x + 44, y + 58), (x + 80, y + 54)], IVORY); alpha_layer(img, lay, 1 - ease(seg(t, 3.0, .4)))
    rot = math.sin(t * 12) * 12 if t > 2.8 else 0
    show(img, t, 2.8, lambda r, m: bell(r, m, 960, 720, 1.4), .6, angle=rot)
    txt_in(img, t, 5.0, (W // 2, 960), "SEE YOU IN THE NEXT ONE", 56, GOLD)


# ============ 37: finale e disclaimer (486)
def b37a(img, t):
    spaced(img, "BEFORE YOU GO", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .3, (590, 330), "ALWAYS CONFIRM", 112, IVORY)
    txt_in(img, t, .9, (590, 470), "BEFORE YOU RELY", 112, GOLD)
    show(img, t, 1.4, lambda r, m: (D(r, m).rr([100, 590, 1090, 990], 36, CARD, SAGE_D, 5)), .5)
    lines = [("General information, not financial or legal advice.", IVORY, 2.0), ("Rules, amounts and ages change", IVORY, 3.6), ("and differ by state.", IVORY, 4.2), ("Always confirm with your official state", GOLD, 5.8), ("SNAP office before you rely on them.", GOLD, 6.4)]
    for i, (s, col, st) in enumerate(lines):
        txt_in(img, t, st, (595, 650 + i * 70), s, 40, col)
    # riquadro schermata finale
    a = ease(seg(t, 2.0, .6))
    if a > 0:
        lay = new_layer(); g = D(*lay)
        for x in range(1170, 1800, 60): g.ln([(x, 250), (x + 34, 250)], GOLD, 5); g.ln([(x, 710), (x + 34, 710)], GOLD, 5)
        for y in range(250, 710, 60): g.ln([(1150, y), (1150, y + 34)], GOLD, 5); g.ln([(1830, y), (1830, y + 34)], GOLD, 5)
        alpha_layer(img, lay, a)
        txt_in(img, t, 2.4, (1490, 790), "WATCH NEXT", 54, GOLD)
    txt_in(img, t, 8.0, (1490, 880), "THANK YOU FOR WATCHING", 40, SAGE)


L.BLOCKS.update({
    21: [("Wait. Before you do anything, rule number three, and it's the one that scares people the most. Savings.", b21a),
         ("A household may have three thousand dollars in countable resources.", b21b),
         ("But if someone is sixty or older, the limit goes up to forty seven hundred fifty.", b21c)],
    22: [("And here's what doesn't count at all. Your home and the lot it sits on.", b22a),
         ("Most retirement and pension plans. And the resources of anyone who receives S S I.", b22b),
         ("So owning your house is not a reason to skip snap. It never was.", b22c)],
    23: [("What about your car? Vehicles can count, and the rules depend on your state.", b23a),
         ("In general, a vehicle isn't counted if it's needed to carry a disabled household member, or if selling it would bring in less than fifteen hundred dollars.", b23b),
         ("One vehicle per adult is also excluded from the equity test. Ask your office how they count yours.", b23c)],
    24: [("Some states are more generous. Most states use something called broad based categorical eligibility,", b24a),
         ("which can let you keep more in savings than the federal numbers.", b24b),
         ("You still have to pass the other rules, but ask your state about it. It could matter.", b24c)],
    25: [("Now, who's in your household? Snap counts everyone who lives together and buys and prepares food together.", b25a),
         ("Your spouse is always included. But here's the twist.", b25b),
         ("If you're sixty or older and can't prepare meals separately because of a permanent disability, you and your spouse can be a separate household, if the people you live with earn no more than one hundred sixty five percent of the poverty level.", b25c)],
    26: [("Why does that matter? That same U S D A data says that among eligible seniors who live with other people, participation is only about thirty two percent.", b26a),
         ("One in three.", b26b),
         ("A lot of seniors who live with family just assume they can't qualify. Sometimes they can.", b26c)],
    27: [("And here's good news if you were worried about work rules.", b27a),
         ("Households made up entirely of elderly or disabled members are not subject to the snap work requirements. No job search, no hours to log.", b27b)],
    28: [("Alright. You've seen the rules. Now, how to apply, in three steps.", b28a),
         ("Step one: find your state. You apply in the state where you live, because every state has its own form.", b28b),
         ("Call the snap information line: one, eight hundred, two two one, five six eight nine.", b28c),
         ("Or go to the U S D A state directory at f n s dot u s d a dot gov, slash snap, slash state directory.", b28d)],
    29: [("Step two: submit the application, in person at your local office, online if your state offers it, or by phone.", b29a),
         ("And hear this carefully. If you're approved, your benefits go back to the date you applied.", b29b),
         ("So don't wait until you've gathered every paper. Apply first. Fix the details later.", b29c)],
    30: [("Step three: the interview. Usually it's over the phone, and most of the time you get a decision within thirty days.", b30a),
         ("Bring proof of your income, your rent, your utility bills and, yes, your medical costs.", b30b),
         ("Mention your medical expenses out loud. Nobody can deduct what they don't know about.", b30c)],
    31: [("Need money sooner? If your household has less than one hundred dollars in cash and under one hundred fifty dollars in monthly income,", b31a),
         ("or if your income and cash are less than your rent and utilities,", b31b),
         ("you may get benefits within seven days. Ask for it by name: expedited.", b31c)],
    32: [("Can't leave the house? You can name an authorized representative, a trusted person who applies and does the interview for you.", b32a),
         ("You just have to choose them in writing.", b32b),
         ("And after you're approved, you'll get a notice with your certification period. Before it ends, you must recertify. Mark that date.", b32c)],
    33: [("Let me save you from the biggest mistakes. One: deciding by yourself that you're over the limit. Let the state decide.", b33a),
         ("Two: forgetting your medical costs and your insurance premiums. Three: skipping the interview.", b33b),
         ("Four: missing your recertification date. Any of these can cost you.", b33c)],
    34: [("One more thing you should know. In twenty twenty five, a new law changed some snap rules, especially work requirements and rules for non citizens,", b34a),
         ("and the U S D A is still updating its pages.", b34b),
         ("So always confirm the current rules with your state snap office before you decide.", b34c)],
    35: [("Let's recap. One: at sixty, you skip the gross income test.", b35a),
         ("Two: medical costs over thirty five dollars a month come off your income, and so do your shelter costs, with no cap.", b35b),
         ("Three: you can keep forty seven hundred fifty in savings, and your home doesn't count.", b35c),
         ("Then call, apply, and let your state decide.", b35d)],
    36: [("If this video helped you, or you know a parent, a neighbor or a friend over sixty who isn't getting this,", b36a),
         ("please hit the like button. It helps us more than you imagine.", b36b),
         ("And subscribe to The Senior Advantage, so the next video about money you're owed finds you first. See you there.", b36c)],
    37: [("This video is general information, not financial or legal advice. Rules, amounts and ages change and differ by state. Always confirm with your official state snap office before you rely on them. Thank you for watching.", b37a)],
})


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = L.split_frames(b)
    for i, ((s, fn), n) in enumerate(zip(L.BLOCKS[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide0{i}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
