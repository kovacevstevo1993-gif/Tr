"""Video lungo 2 (SNAP over 60) - blocco 1 (gancio). Uso: L2_FRAMES=<fotogrammi timeline> OUT=cartella python3 long2_b01.py [1 2 3]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long1_b01 import *
from long1_blocks import show, txt_in

TOTAL2 = int(os.environ.get("L2_FRAMES", 1030))
SENT2 = [("Wait… out of every one hundred seniors who qualify for snap, only fifty five ever sign up, according to U S D A data. The other forty five walk past money for groceries, month after month, and most of them never find out."),
         ("In this video you'll learn the three rules that change everything after sixty. You'll watch me run the exact math, step by step."),
         ("And you'll see how one deduction can turn zero dollars into real money. Stay until the end, because that one is rule number two.")]
_w = [len(s) for s in SENT2]
DUR2 = [round(TOTAL2 * _w[0] / sum(_w)), round(TOTAL2 * _w[1] / sum(_w))]; DUR2.append(TOTAL2 - sum(DUR2))


def senior(rgb, mask, cx, cy, s=1.0, col=SAGE, cane=False):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, col), (dm, 255)):
        dr.ellipse([cx - 13 * s, cy - 34 * s, cx + 13 * s, cy - 8 * s], fill=c)
        dr.pieslice([cx - 24 * s, cy - 2 * s, cx + 24 * s, cy + 52 * s], 180, 360, fill=c)
        if cane: dr.line([(cx + 26 * s, cy + 10 * s), (cx + 28 * s, cy + 30 * s)], fill=c, width=max(2, int(3 * s)))


def cross(rgb, mask, cx, cy, r=60, col=RED):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, IVORY), (dm, 255)):
        dr.rounded_rectangle([cx - r, cy - r, cx + r, cy + r], radius=int(r * .28), fill=c)
    d.rectangle([cx - r * .22, cy - r * .66, cx + r * .22, cy + r * .66], fill=col)
    d.rectangle([cx - r * .66, cy - r * .22, cx + r * .66, cy + r * .22], fill=col)


def coin(rgb, mask, cx, cy, r=40, label="$"):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, GOLD), (dm, 255)):
        dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    d.ellipse([cx - r * .78, cy - r * .78, cx + r * .78, cy + r * .78], outline=GREEN_D, width=max(2, int(r * .08)))
    d.text((cx, cy), label, font=font(FONT_SERIF, int(r * 1.1)), fill=GREEN_D, anchor="mm")


def grocery_bag(rgb, mask, cx, cy, s=1.0):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, (196, 150, 98)), (dm, 255)):
        dr.polygon([(cx - 90 * s, cy - 60 * s), (cx + 90 * s, cy - 60 * s), (cx + 76 * s, cy + 110 * s), (cx - 76 * s, cy + 110 * s)], fill=c)
    d.line([(cx - 90 * s, cy - 60 * s), (cx - 76 * s, cy + 110 * s)], fill=(160, 118, 72), width=int(5 * s))
    for dx, col in ((-40, RED), (10, SAGE), (50, GOLD)):
        for dr, c in ((d, col), (dm, 255)):
            dr.ellipse([cx + (dx - 22) * s, cy - 110 * s, cx + (dx + 22) * s, cy - 62 * s], fill=c)
    for dr, c in ((d, IVORY), (dm, 255)):
        dr.rectangle([cx - 20 * s, cy - 132 * s, cx + 62 * s, cy - 70 * s], fill=c)
    d.text((cx, cy + 25 * s), "SNAP", font=font(FONT_SANS, int(30 * s)), fill=GREEN_D, anchor="mm")


# ---------------- SLIDE 1: 55 su 100
def c1(img, t):
    d = ImageDraw.Draw(img)
    spaced(img, "SNAP FOR SENIORS", W // 2, 90, 44, a=ease(seg(t, 0, .5)))
    gx0, gy0, dx, dy = 150, 215, 66, 76  # griglia 10x10 a sinistra
    for i in range(100):
        r_, c_ = divmod(i, 10)
        st = .3 + i * .018
        p = ease_back(seg(t, st, .35))
        if p <= 0: continue
        x, y = gx0 + c_ * dx, gy0 + r_ * dy
        lit = i < 55
        sw = 0 if t < 4.2 else ease(seg(t, 4.2 + (i - 55) * .02, .4))  # i 45 si spengono / diventano rossi
        col = GOLD if lit else tuple(int(SAGE_D[k] + (RED[k] - SAGE_D[k]) * sw) for k in range(3))
        if not lit and t > 4.2:
            col = tuple(int(SAGE_D[k] + (RED[k] - SAGE_D[k]) * sw) for k in range(3))
        elif not lit:
            col = SAGE_D
        pop(img, lambda r, m, x=x, y=y, col=col, i=i: senior(r, m, x, y - 10, 1.05, col), p, a=ease(seg(t, st, .2)))
    # grande 55 / 100
    pop(img, lambda r, m: T(r, m, (1330, 360), "55", font(FONT_SERIF, 360), GOLD), ease_back(seg(t, 1.6, .7)), a=ease(seg(t, 1.6, .3)))
    txt_in(img, t, 2.0, (1330, 560), "OUT OF 100 SENIORS", 54, IVORY)
    txt_in(img, t, 2.4, (1330, 635), "WHO QUALIFY GET SNAP", 54, IVORY)
    # i 45 che non lo prendono
    pop(img, lambda r, m: T(r, m, (1330, 810), "45", font(FONT_SERIF, 230), RED), ease_back(seg(t, 4.4, .7)), a=ease(seg(t, 4.4, .3)))
    txt_in(img, t, 4.9, (1330, 940), "WALK PAST THE MONEY", 56, RED)
    # moneta che scivola via
    for k in range(5):
        st = 5.4 + k * .5
        pp = seg(t, st, 3.0)
        if 0 < pp < 1:
            pop(img, lambda r, m: coin(r, m, 1700, 760, 34), 1.0, a=min(1, pp * 5) * (1 - ease(seg(pp, .7, .3))), dx=-80 * pp, dy=240 * pp * pp)
    txt_in(img, t, 8.0, (W // 2, 1030), "SOURCE: USDA FNS", 26, SAGE, sans_m=True)


# ---------------- SLIDE 2: tre regole + calcolo
def c2(img, t):
    d = ImageDraw.Draw(img)
    spaced(img, "THREE RULES AFTER SIXTY", W // 2, 90, 44, a=ease(seg(t, 0, .5)))
    cards = [(330, "RULE 1", "SKIP THE GROSS", "INCOME TEST", lambda r, m, cx, cy: (price_tag(r, m, cx, cy, "60", 260, 150), None)),
             (960, "RULE 2", "MEDICAL COSTS", "COME OFF INCOME", lambda r, m, cx, cy: cross(r, m, cx, cy, 80)),
             (1590, "RULE 3", "SAVINGS UP TO $4,750", "HOME DOESN'T COUNT", lambda r, m, cx, cy: (coin(r, m, cx - 70, cy + 10, 56), coin(r, m, cx + 10, cy - 20, 56), coin(r, m, cx + 70, cy + 30, 56)))]
    for i, (cx, tag, l1, l2, icon) in enumerate(cards):
        st = .5 + i * .9
        p = ease_back(seg(t, st, .6)); a = ease(seg(t, st, .4))
        if a <= 0: continue
        lay = new_layer(); rgb, mask = lay
        off = 70 * (1 - p)
        box = [cx - 285, 190 + off, cx + 285, 640 + off]
        ImageDraw.Draw(mask).rounded_rectangle(box, radius=34, fill=255)
        dd = ImageDraw.Draw(rgb); dd.rounded_rectangle(box, radius=34, fill=CARD, outline=SAGE_D, width=4)
        dd.rounded_rectangle([box[0], box[1], box[2], box[1] + 70], radius=34, fill=GOLD)
        dd.rectangle([box[0], box[1] + 40, box[2], box[1] + 70], fill=GOLD)
        T(rgb, mask, (cx, box[1] + 36), tag, font(FONT_SANS, 40), GREEN_D)
        icon(rgb, mask, cx, 410 + off)
        T(rgb, mask, (cx, 545 + off), l1, font(FONT_SANS, 31), IVORY)
        T(rgb, mask, (cx, 595 + off), l2, font(FONT_SANS, 31), GOLD)
        alpha_layer(img, lay, a)
    # calcolatrice con scritta "THE EXACT MATH"
    st = 4.2
    p = ease_back(seg(t, st, .7))
    def calc(r, m):
        bx = [640, 700, 1280, 1010]
        ImageDraw.Draw(m).rounded_rectangle(bx, radius=30, fill=255)
        dr = ImageDraw.Draw(r); dr.rounded_rectangle(bx, radius=30, fill=GOLD)
        dr.rounded_rectangle([bx[0] + 25, bx[1] + 25, bx[2] - 25, bx[1] + 105], radius=14, fill=GREEN_D)
        for rr in range(2):
            for cc in range(5):
                x = bx[0] + 55 + cc * 105; y = bx[1] + 150 + rr * 70
                dr.rounded_rectangle([x, y, x + 80, y + 50], radius=10, fill=(190, 140, 66) if cc < 4 else GREEN_L)
        T(r, m, (bx[2] - 60, bx[1] + 65), "= ?", font(FONT_SANS, 56), GOLD, anchor="rm")
    pop(img, calc, .6 + .4 * p, a=ease(seg(t, st, .4)), dy=math.sin(t * 2) * 4 if t > st + .8 else 0, angle=-3)
    txt_in(img, t, 5.0, (W // 2, 1052), "STEP BY STEP · THE EXACT MATH", 36, GOLD)


# ---------------- SLIDE 3: da $0 a soldi veri + regola 2
def c3(img, t):
    d = ImageDraw.Draw(img)
    spaced(img, "ONE DEDUCTION CHANGES THE NUMBER", W // 2, 90, 44, a=ease(seg(t, 0, .5)))
    # display "$0" -> "$$$"
    def disp(r, m):
        bx = [160, 230, 900, 640]
        ImageDraw.Draw(m).rounded_rectangle(bx, radius=36, fill=255)
        dr = ImageDraw.Draw(r); dr.rounded_rectangle(bx, radius=36, fill=CARD, outline=GOLD, width=6)
        T(r, m, ((bx[0] + bx[2]) / 2, 290), "MONTHLY SNAP", font(FONT_SANS, 40), SAGE)
    show(img, t, .3, disp, .6)
    amt = "$0" if t < 3.2 else "$$"
    a1 = ease(seg(t, .8, .4)) * (1 - ease(seg(t, 3.0, .3)))
    if a1 > 0:
        lay = new_layer(); T(lay[0], lay[1], (530, 450), "$0", font(FONT_SERIF, 220), IVORY); alpha_layer(img, lay, a1)
    if t > 3.2:
        p = ease_back(seg(t, 3.2, .7))
        pop(img, lambda r, m: T(r, m, (530, 450), "REAL $", font(FONT_SERIF, 170), GOLD), p, a=ease(seg(t, 3.2, .3)))
        for k in range(6):
            pp = seg(t, 3.6 + k * .3, 1.6)
            if 0 < pp < 1:
                pop(img, lambda r, m, k=k: coin(r, m, 230 + k * 120, 700, 34), 1.0, a=min(1, pp * 6) * (1 - ease(seg(pp, .7, .3))), dy=-150 * pp)
    # freccia + croce medica
    ar = ease(seg(t, 2.0, .6))
    if ar > 0:
        lay = new_layer(); rgb, mask = lay
        for dr, c in ((ImageDraw.Draw(rgb), GOLD), (ImageDraw.Draw(mask), 255)):
            dr.polygon([(960, 405 + 0), (1080, 405 - 0), (1080, 380), (1160, 440), (1080, 500), (1080, 475), (960, 475)], fill=c)
        alpha_layer(img, lay, ar)
    show(img, t, 1.4, lambda r, m: cross(r, m, 1440, 400, 150), .7, angle=0, dy=math.sin(t * 2.4) * 6)
    txt_in(img, t, 2.2, (1440, 640), "MEDICAL DEDUCTION", 50, IVORY)
    # RULE NUMBER 2 + stay till the end
    st = 5.2
    pop(img, lambda r, m: (price_tag(r, m, 960, 860, "RULE 2", 560, 190)), .6 + .4 * ease_back(seg(t, st, .6)), a=ease(seg(t, st, .3)), angle=-3)
    txt_in(img, t, 6.0, (W // 2, 1005), "STAY UNTIL THE END", 52, GOLD)
    # lancetta di avanzamento
    pg = ease(seg(t, 6.2, 3.5))
    d.rounded_rectangle([560, 1050, 1360, 1060], radius=5, fill=SAGE_D)
    d.rounded_rectangle([560, 1050, 560 + 800 * pg, 1060], radius=5, fill=GOLD)


if __name__ == "__main__":
    which = sys.argv[1:] or ["1", "2", "3"]
    for k, fn in (("1", c1), ("2", c2), ("3", c3)):
        if k in which:
            render(fn, DUR2[int(k) - 1] / FPS, f"{OUT}/bloco01-slide0{k}.mp4")
            print("ok", k, DUR2[int(k) - 1], "fotogrammi", flush=True)
