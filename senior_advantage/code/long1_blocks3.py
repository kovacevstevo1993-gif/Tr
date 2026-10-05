"""Video lungo 1 - blocchi 12-20. Durate dalla timeline CapCut (screenshot dell'utente: riga bianca + righello).
Uso: python3 long1_blocks3.py <blocco> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long1_blocks2 import *  # show, txt_in, footer, bubble, tiles_row, month_strip, calendar, chip, check_receipt, aarp_card, ...

BLOCK_FRAMES3 = {12: 603, 13: 540, 14: 715, 15: 317, 16: 464, 17: 864, 18: 678, 19: 597, 20: 435}


def ring(img, t, cx, cy, rr, pct, big, small, st=1.0):
    """anello che si riempie con percentuale al centro"""
    a = ease(seg(t, st, .5))
    if a <= 0: return
    d = ImageDraw.Draw(img)
    lay = new_layer(); L, M = lay; dd, dm = ImageDraw.Draw(L), ImageDraw.Draw(M)
    for dr, c in ((dd, CARD), (dm, 255)): dr.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c)
    dd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=SAGE_D, width=6); alpha_layer(img, lay, a)
    d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, 270, fill=(30, 80, 64), width=28)
    d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, -90 + 360 * pct * ease(seg(t, st + .4, 1.0)), fill=GOLD, width=28)
    show(img, t, st + .2, lambda r, m: T(r, m, (cx, cy - 10), big, font(FONT_SERIF, int(rr * .7)), IVORY), .5)
    if small: txt_in(img, t, st + .8, (cx, cy + rr * .5), small, 34, SAGE)


def pill(rgb, mask, cx, cy, s, size=44, fill=GOLD, fg=GREEN_D, pad=40):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    f = font(FONT_SANS, size); w = d.textlength(s, font=f) + 2 * pad; h = size + 40
    for dr, c in ((d, fill), (dm, 255)): dr.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=h // 2, fill=c)
    d.text((cx, cy), s, font=f, fill=fg, anchor="mm"); dm.text((cx, cy), s, font=f, fill=255, anchor="mm")


def id_card(r, m, cx, cy, w=520, h=320, label="PHOTO ID"):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    dm.rounded_rectangle(box, radius=26, fill=255); d.rounded_rectangle(box, radius=26, fill=(246, 241, 229))
    d.rectangle([box[0], box[1], box[2], box[1] + 60], fill=GREEN_L); T(r, m, (cx, box[1] + 30), label, font(FONT_SANS, 34), IVORY)
    d.rounded_rectangle([box[0] + 36, box[1] + 90, box[0] + 176, box[3] - 36], radius=12, fill=SAGE)
    for i in range(3): d.rounded_rectangle([box[0] + 210, box[1] + 100 + i * 52, box[2] - 40 - (i % 2) * 60, box[1] + 124 + i * 52], radius=8, fill=(190, 184, 160))


def coupon(r, m, cx, cy, s, w=380, h=190, fill=GOLD, fg=GREEN_D, size=64):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    dm.rounded_rectangle(box, radius=22, fill=255); d.rounded_rectangle(box, radius=22, fill=fill)
    for k in range(7): d.line([(box[0] + 30 + k * ((w - 60) / 6), box[1] + 14), (box[0] + 30 + k * ((w - 60) / 6) + 10, box[1] + 14)], fill=fg, width=4)
    T(r, m, (cx, cy), s, font(FONT_SANS, size), fg)


def bigx(img, t, st, cx, cy, size=80):
    stamp_x(img, cx, cy, seg(t, st, .5))


# ============================== BLOCCO 12: Kohl's ==============================
def b12c1(img, t):
    spaced(img, "NUMBER FOUR  ·  KOHL'S", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    d = ImageDraw.Draw(img)
    for i, dn in enumerate(days):
        x = 150 + i * 120
        on = ease(seg(t, .8, .5)) if i == 2 else 0
        col = tuple(int(CARD[k] + (GOLD[k] - CARD[k]) * on) for k in range(3))
        d.rounded_rectangle([x, 330, x + 105, 560], radius=22, fill=col, outline=SAGE_D, width=3)
        d.text((x + 52, 390), dn, font=font(FONT_SANS, 30), fill=GREEN_D if on > .5 else IVORY, anchor="mm")
    txt_in(img, t, 1.4, (490, 640), "EVERY WEDNESDAY", 46, GOLD)
    ring(img, t, 1330, 440, 230, .15, "15%", "OFF", st=1.8)
    show(img, t, 3.2, lambda r, m: price_tag(r, m, 1330, 780, "60+", 300, 170), .5, angle=-7)
    show(img, t, 4.4, lambda r, m: pill(r, m, 490, 800, "IN THE STORE ONLY", 44), .5)
    footer(img, t)


def b12c2(img, t):
    spaced(img, "NUMBER FOUR  ·  KOHL'S", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: id_card(r, m, 620, 520), .6, angle=-3)
    show(img, t, 1.6, lambda r, m: pill(r, m, 1400, 400, "ONE PER CUSTOMER", 50), .5)
    show(img, t, 2.4, lambda r, m: person(r, m, 1400, 700, 1.0), .5)
    txt_in(img, t, 3.0, (W // 2, 930), "YOU NEED AN ID", 62, IVORY)
    footer(img, t)


def b12c3(img, t):
    spaced(img, "NUMBER FOUR  ·  KOHL'S", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: coupon(r, m, 560, 480, "% OFF", fill=GOLD, size=84), .5, angle=-5)
    show(img, t, 1.2, lambda r, m: T(r, m, (960, 480), "+", font(FONT_SANS, 130), SAGE), .4)
    show(img, t, 1.8, lambda r, m: coupon(r, m, 1360, 480, "% OFF", fill=SAGE, size=84), .5, angle=5)
    bigx(img, t, 3.0, 960, 480)
    txt_in(img, t, 3.6, (W // 2, 760), "NOT WITH OTHER PERCENT-OFF COUPONS", 54, RED)
    footer(img, t, 4.4)


def b12c4(img, t):
    spaced(img, "NUMBER FOUR  ·  KOHL'S", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: coupon(r, m, 520, 460, "$10 OFF", w=420, size=64), .5, angle=-4)
    show(img, t, 1.2, lambda r, m: coupon(r, m, 1000, 460, "KOHL'S CASH", w=460, fill=SAGE, size=44), .5, angle=3)
    show(img, t, 2.4, lambda r, m: T(r, m, (1380, 460), "➜", font(FONT_SANS, 120), GOLD), .5)
    show(img, t, 3.0, lambda r, m: coupon(r, m, 1620, 460, "15%", w=240, h=170, size=70), .5, angle=4)
    txt_in(img, t, 3.8, (760, 650), "APPLIED FIRST", 70, GOLD)
    txt_in(img, t, 4.6, (W // 2, 880), "YOU CAN STILL USE THOSE", 54, IVORY)
    footer(img, t, 5.0)


# ============================== BLOCCO 13: thrift ==============================
def b13c1(img, t):
    spaced(img, "NUMBER FIVE  ·  THRIFT STORES", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    tiles_row(img, t, ["shirt", "hanger"], ["", ""], 420, 330, 250, .4)
    txt_in(img, t, 1.0, (460, 620), "SAVERS: SENIOR TUESDAY", 46, GOLD)
    ring(img, t, 1300, 440, 230, .30, "30%", "OFF", st=1.4)
    show(img, t, 3.0, lambda r, m: price_tag(r, m, 1000, 800, "55+", 300, 170), .5, angle=-6)
    def red_tag(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        pts = [(1400, 770), (1470, 720), (1700, 720), (1700, 850), (1470, 850)]
        dm.polygon(pts, fill=255); d.polygon(pts, fill=RED); d.ellipse([1468, 776, 1488, 796], fill=GREEN_D); T(r, m, (1590, 785), "NEW", font(FONT_SANS, 44), IVORY)
    show(img, t, 4.4, red_tag, .5)
    bigx(img, t, 5.0, 1700, 720)
    txt_in(img, t, 5.4, (1560, 910), "NOT NEW MERCHANDISE", 40, SAGE)
    footer(img, t)


def b13c2(img, t):
    spaced(img, "NUMBER FIVE  ·  THRIFT STORES", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .2, (W // 2, 200), "GOODWILL IS DIFFERENT", 62, IVORY)
    d = ImageDraw.Draw(img)
    on = {1, 4, 6}
    for i in range(8):
        cx, cy = 330 + (i % 4) * 420, 450 + (i // 4) * 260
        lit = ease(seg(t, 1.2 + (i % 4) * .2, .5)) if i in on else 0
        show(img, t, .5 + i * .12, lambda r, m, cx=cx, cy=cy, lit=lit: (ImageDraw.Draw(m).rounded_rectangle([cx - 150, cy - 90, cx + 150, cy + 90], radius=24, fill=255), ImageDraw.Draw(r).rounded_rectangle([cx - 150, cy - 90, cx + 150, cy + 90], radius=24, fill=GOLD if lit > .5 else CARD, outline=SAGE_D, width=4), T(r, m, (cx, cy), "SENIOR DAY" if lit > .5 else "STORE", font(FONT_SANS, 34), GREEN_D if lit > .5 else SAGE)), .4)
    txt_in(img, t, 3.0, (W // 2, 820), "NO NATIONAL RULE", 58, RED)
    txt_in(img, t, 4.2, (W // 2, 930), "SOME LOCAL STORES DO  ·  ASK AT YOURS", 54, GOLD)
    footer(img, t, 4.6)


# ============================== BLOCCO 14: Michaels ==============================
def b14c1(img, t):
    spaced(img, "NUMBER SIX  ·  MICHAELS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: tile_icon("craft", r, m, 330, 420), .5)
    txt_in(img, t, 1.0, (330, 580), "CRAFTS & HOBBIES", 40, SAGE)
    ring(img, t, 960, 430, 230, .10, "10%", "OFF", st=1.4)
    show(img, t, 3.0, lambda r, m: pill(r, m, 960, 760, "EVEN SALE ITEMS", 50), .5)
    show(img, t, 3.6, lambda r, m: price_tag(r, m, 1560, 420, "55+", 300, 170), .5, angle=-6)
    d = ImageDraw.Draw(img)
    for i, dn in enumerate(["M", "T", "W", "T", "F", "S", "S"]):
        on = ease(seg(t, 4.2 + i * .15, .3)); x = 1370 + (i % 4) * 100; y = 650 + (i // 4) * 100
        col = tuple(int(CARD[k] + (GOLD[k] - CARD[k]) * on) for k in range(3))
        d.ellipse([x - 40, y - 40, x + 40, y + 40], fill=col, outline=SAGE_D, width=3); d.text((x, y), dn, font=font(FONT_SANS, 34), fill=GREEN_D if on > .5 else SAGE, anchor="mm")
    txt_in(img, t, 5.4, (1530, 880), "ANY DAY OF THE WEEK", 42, GOLD)
    footer(img, t)


def b14c2(img, t):
    spaced(img, "NUMBER SIX  ·  MICHAELS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: id_card(r, m, 520, 480), .6, angle=-3)
    txt_in(img, t, 1.2, (520, 700), "SHOW YOUR ID AT CHECKOUT", 44, IVORY)
    show(img, t, 2.6, lambda r, m: T(r, m, (960, 480), "OR", font(FONT_SANS, 70), SAGE), .4)
    def rc(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        box = [1100, 330, 1720, 650]
        dm.rounded_rectangle(box, radius=32, fill=255); d.rounded_rectangle(box, radius=32, fill=GOLD)
        T(r, m, (1410, 420), "REWARDS", font(FONT_SANS, 60), GREEN_D); T(r, m, (1410, 520), "FREE ACCOUNT", font(FONT_SANS_M, 48), GREEN_D)
        d.rounded_rectangle([1160, 580, 1660, 610], radius=8, fill=GREEN_D)
    show(img, t, 3.0, rc, .6, angle=4)
    txt_in(img, t, 3.8, (1410, 700), "ADD IT TO YOUR ACCOUNT", 44, IVORY)
    footer(img, t)


def b14c3(img, t):
    spaced(img, "NUMBER SIX  ·  MICHAELS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .2, (W // 2, 200), "A FEW THINGS ARE EXCLUDED", 62, IVORY)
    for i, lab in enumerate(["CLEARANCE", "CUSTOM FRAMING", "BOOKS"]):
        cx = 360 + i * 600
        show(img, t, .7 + i * .8, lambda r, m, cx=cx, lab=lab: (ImageDraw.Draw(m).rounded_rectangle([cx - 270, 330, cx + 270, 600], radius=34, fill=255), ImageDraw.Draw(r).rounded_rectangle([cx - 270, 330, cx + 270, 600], radius=34, fill=CARD, outline=SAGE_D, width=5), T(r, m, (cx, 465), lab, font(FONT_SANS, 46), IVORY)), .5)
        stamp_x(img, cx + 230, 350, seg(t, 1.3 + i * .8, .5))
    show(img, t, 3.6, lambda r, m: pill(r, m, W // 2, 760, "ONE SENIOR DISCOUNT PER DAY", 54), .5)
    footer(img, t, 4.2)


# ============================== BLOCCO 15: meta' ==============================
def b15c1(img, t):
    spaced(img, "WE'RE HALFWAY THERE", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    d = ImageDraw.Draw(img)
    for i in range(12):
        on = ease(seg(t, .5 + i * .12, .3)) if i < 6 else 0
        x = 330 + i * 110
        col = tuple(int(CARD[k] + (GOLD[k] - CARD[k]) * on) for k in range(3))
        d.ellipse([x - 38, 420, x + 38, 496], fill=col, outline=SAGE_D, width=4); d.text((x, 458), str(i + 1), font=font(FONT_SANS, 34), fill=GREEN_D if on > .5 else SAGE, anchor="mm")
    show(img, t, 2.4, lambda r, m: T(r, m, (960, 640), "6 OF 12", font(FONT_SERIF, 150), IVORY), .5)
    txt_in(img, t, 3.6, (W // 2, 860), "THE NEXT ONE DOESN'T COME FROM A STORE", 54, GOLD)


def b15c2(img, t):
    spaced(img, "YOUR OWN PHONE BILL", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: check_receipt(r, m, 220, 200, 760, 760, "PHONE BILL", [("Plan", "$40.00"), ("Taxes", "$6.00")], hl=("55+ PLAN", "SAVES"), total="MONTHLY"), .6, angle=-3)
    month_strip(img, t, 1.5, 300, x0=840, w=78, h=90, lab_size=20)
    month_strip(img, t, 1.5, 420, x0=860, w=96, h=90, lab_size=22) if False else None
    txt_in(img, t, 3.4, (1330, 560), "EVERY SINGLE MONTH", 52, GOLD)
    d = ImageDraw.Draw(img)
    a = ease(seg(t, 4.2, .5))
    if a > 0:
        lay = new_layer(); T(lay[0], lay[1], (1330, 700), "NOT JUST ONE TUESDAY", font(FONT_SANS, 46), SAGE); alpha_layer(img, lay, a)


# ============================== BLOCCO 16: pausa ==============================
def b16c1(img, t):
    spaced(img, "QUICK PAUSE", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    tiles_row(img, t, ["plate", "pharmacy", "shirt", "hanger", "craft"], ["RESTAURANTS", "DRUGSTORE", "CLOTHES", "THRIFT", "CRAFTS"], 450, 360, 300, .5, lsz=30)
    def chk(r, m, x):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, GOLD), (dm, 255)): dr.ellipse([x + 40, 360, x + 90, 410], fill=c)
        d.line([(x + 52, 386), (x + 62, 398), (x + 80, 372)], fill=GREEN_D, width=7)
    for i in range(5):
        show(img, t, 2.8 + i * .4, lambda r, m, x=360 + i * 300: chk(r, m, x), .3)
    txt_in(img, t, 5.0, (W // 2, 860), "KEEPING SCORE", 66, GOLD)


def b16c2(img, t):
    spaced(img, "TELL ME IN THE COMMENTS", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    def b(r, m):
        bubble(r, m, 760, 440, 1000, 380, tail="left")
        T(r, m, (760, 380), "Which one", font(FONT_SERIF, 84), IVORY); T(r, m, (760, 490), "didn't you know about?", font(FONT_SERIF, 84), GOLD)
    show(img, t, .5, b, .6)
    show(img, t, 1.4, lambda r, m: person(r, m, 1560, 640, 1.3), .5)
    def heart(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, RED), (dm, 255)):
            dr.ellipse([1420, 340, 1500, 420], fill=c); dr.ellipse([1490, 340, 1570, 420], fill=c); dr.polygon([(1420, 395), (1570, 395), (1495, 480)], fill=c)
    show(img, t, 3.0, heart, .5)
    txt_in(img, t, 4.4, (W // 2, 900), "I READ THEM  ·  YOUR ANSWER HELPS OTHERS FIND THIS LIST", 46, SAGE)


# ============================== BLOCCO 17: telefono ==============================
def phone_icon(r, m, cx, cy, s=1.0, label="55+"):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - 120 * s, cy - 220 * s, cx + 120 * s, cy + 220 * s]
    dm.rounded_rectangle(box, radius=int(40 * s), fill=255); d.rounded_rectangle(box, radius=int(40 * s), fill=(230, 230, 225))
    d.rounded_rectangle([cx - 100 * s, cy - 180 * s, cx + 100 * s, cy + 170 * s], radius=int(24 * s), fill=GREEN_D)
    T(r, m, (cx, cy - 20 * s), label, font(FONT_SANS, int(80 * s)), GOLD); T(r, m, (cx, cy + 70 * s), "PLAN", font(FONT_SANS_M, int(36 * s)), SAGE)


def b17c1(img, t):
    spaced(img, "NUMBER SEVEN  ·  YOUR PHONE PLAN", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: phone_icon(r, m, 400, 520, 1.1), .6, angle=-4)
    txt_in(img, t, 1.2, (400, 830), "AT&T 55+ PLAN", 46, GOLD)
    show(img, t, 2.6, lambda r, m: chip(r, m, 960, 400, "$40", 100, w=380, h=190), .5)
    txt_in(img, t, 3.0, (960, 540), "ONE LINE / MONTH", 34, SAGE)
    show(img, t, 5.2, lambda r, m: chip(r, m, 1480, 400, "$35", 100, w=380, h=190), .5)
    txt_in(img, t, 5.6, (1480, 540), "PER LINE, TWO LINES", 34, SAGE)
    show(img, t, 8.0, lambda r, m: id_card(r, m, 1200, 760, 420, 250), .5, angle=-3)
    txt_in(img, t, 8.4, (1200, 920), "PROVE YOUR AGE WITH AN ID", 40, IVORY)


def b17c2(img, t):
    spaced(img, "NUMBER SEVEN  ·  YOUR PHONE PLAN", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .2, (W // 2, 200), "T-MOBILE: THREE 55+ PLANS", 60, GOLD)
    for i, n in enumerate(["PLAN 1", "PLAN 2", "PLAN 3"]):
        cx = 400 + i * 560
        show(img, t, .7 + i * .7, lambda r, m, cx=cx, n=n: (ImageDraw.Draw(m).rounded_rectangle([cx - 230, 300, cx + 230, 700], radius=34, fill=255), ImageDraw.Draw(r).rounded_rectangle([cx - 230, 300, cx + 230, 700], radius=34, fill=CARD, outline=GOLD, width=5), T(r, m, (cx, 400), "55+", font(FONT_SERIF, 140), GOLD), T(r, m, (cx, 560), n, font(FONT_SANS, 54), IVORY), T(r, m, (cx, 640), "UNLIMITED", font(FONT_SANS_M, 34), SAGE)), .5)
    show(img, t, 3.4, lambda r, m: pill(r, m, W // 2, 820, "STARTING AT $30 PER LINE, TWO LINES", 46), .5)
    footer(img, t, 4.0, "Prices change · check the company's page")


def florida(r, m, cx, cy, s=1.0):
    pts = [(-150, -230), (60, -230), (90, -200), (130, -120), (110, -40), (140, 40), (170, 140), (150, 240), (100, 260), (60, 170), (30, 90), (-20, 20), (-70, -60), (-150, -80)]
    P = [(cx + x * s, cy + y * s) for x, y in pts]
    ImageDraw.Draw(m).polygon(P, fill=255); ImageDraw.Draw(r).polygon(P, fill=GOLD, outline=IVORY)


def b17c3(img, t):
    spaced(img, "NUMBER SEVEN  ·  YOUR PHONE PLAN", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: florida(r, m, 560, 520, 1.15), .6)
    txt_in(img, t, 1.4, (560, 900), "FLORIDA", 70, GOLD)
    show(img, t, 2.0, lambda r, m: phone_icon(r, m, 1300, 520, 1.0), .6, angle=4)
    txt_in(img, t, 3.0, (1300, 830), "VERIZON 55+ PLAN", 46, IVORY)
    show(img, t, 3.8, lambda r, m: pill(r, m, 1300, 920, "ONLY FOR FLORIDA RESIDENTS", 40, fill=RED, fg=IVORY), .5)


def b17c4(img, t):
    spaced(img, "PRICES CHANGE", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    for i, s in enumerate(["$40", "$35", "$30"]):
        show(img, t, .4 + i * .5, lambda r, m, i=i, s=s: price_tag(r, m, 420 + i * 420, 480, s, 320, 190), .5, angle=-8 + i * 8)
    def mag(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, IVORY), (dm, 255)):
            dr.ellipse([1500, 330, 1760, 590], outline=c, width=22); dr.line([(1735, 565), (1850, 680)], fill=c, width=34)
    show(img, t, 2.4, mag, .6)
    txt_in(img, t, 3.4, (W // 2, 800), "CHECK THE COMPANY'S PAGE", 64, GOLD)
    txt_in(img, t, 4.4, (W // 2, 910), "BEFORE YOU SWITCH", 54, IVORY)
    footer(img, t, 4.8, "Prices change · check the company's page")


# ============================== BLOCCO 18: cinema ==============================
def ticket(r, m, cx, cy, s, w=560, h=250, fill=GOLD):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    dm.rounded_rectangle(box, radius=26, fill=255); d.rounded_rectangle(box, radius=26, fill=fill)
    for dr, c in ((d, CARD), (dm, 0)): dr.ellipse([box[0] - 34, cy - 34, box[0] + 34, cy + 34], fill=c); dr.ellipse([box[2] - 34, cy - 34, box[2] + 34, cy + 34], fill=c)
    T(r, m, (cx, cy), s, font(FONT_SANS, 64), GREEN_D)


def b18c1(img, t):
    spaced(img, "NUMBER EIGHT  ·  THE MOVIES", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: ticket(r, m, 560, 450, "SENIOR"), .6, angle=-5)
    show(img, t, 1.4, lambda r, m: price_tag(r, m, 560, 700, "60+", 300, 170), .5, angle=4)
    cx, cy, rr = 1330, 470, 230
    d = ImageDraw.Draw(img)
    a = ease(seg(t, 2.2, .5))
    if a > 0:
        lay = new_layer(); L, M = lay; dd, dm = ImageDraw.Draw(L), ImageDraw.Draw(M)
        for dr, c in ((dd, CARD), (dm, 255)): dr.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c)
        dd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=SAGE_D, width=6); alpha_layer(img, lay, a)
        for k in range(12):
            ang = k * math.pi / 6; d.line([cx + (rr - 30) * math.sin(ang), cy - (rr - 30) * math.cos(ang), cx + (rr - 12) * math.sin(ang), cy - (rr - 12) * math.cos(ang)], fill=SAGE, width=5)
        ha = (t - 2.4) * 2.0; d.line([cx, cy, cx + 120 * math.sin(ha), cy - 120 * math.cos(ha)], fill=GOLD, width=12); d.line([cx, cy, cx + 170 * math.sin(ha * 6), cy - 170 * math.cos(ha * 6)], fill=IVORY, width=6)
    txt_in(img, t, 3.0, (cx, 790), "ALL DAY, EVERY DAY", 54, GOLD)


def b18c2(img, t):
    spaced(img, "WHEN YOU BUY ONLINE", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .2, (W // 2, 200), "CHOOSE THE TICKET AT CHECKOUT", 56, IVORY)
    for i, n in enumerate(["ADULT", "CHILD", "SENIOR"]):
        cx = 400 + i * 560; sel = i == 2
        show(img, t, .7 + i * .5, lambda r, m, cx=cx, n=n, sel=sel: (ImageDraw.Draw(m).rounded_rectangle([cx - 230, 330, cx + 230, 650], radius=34, fill=255), ImageDraw.Draw(r).rounded_rectangle([cx - 230, 330, cx + 230, 650], radius=34, fill=GOLD if sel else CARD, outline=GOLD if sel else SAGE_D, width=6), T(r, m, (cx, 490), n, font(FONT_SANS, 62), GREEN_D if sel else SAGE)), .5)
    a = ease(seg(t, 3.0, .5))
    if a > 0:
        d = ImageDraw.Draw(img); d.polygon([(1520, 720), (1560, 770), (1600, 720)], fill=GOLD)
    txt_in(img, t, 3.6, (1520, 840), "SENIOR", 54, GOLD)


def b18c3(img, t):
    spaced(img, "THE PRICE DEPENDS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    for i, (n, p) in enumerate((("THEATER A", "$9"), ("THEATER B", "$12"), ("THEATER C", "$8"))):
        cx = 360 + i * 600
        show(img, t, .5 + i * .6, lambda r, m, cx=cx, n=n, p=p: (ImageDraw.Draw(m).rounded_rectangle([cx - 240, 260, cx + 240, 560], radius=34, fill=255), ImageDraw.Draw(r).rounded_rectangle([cx - 240, 260, cx + 240, 560], radius=34, fill=CARD, outline=SAGE_D, width=5), T(r, m, (cx, 330), n, font(FONT_SANS, 44), SAGE), T(r, m, (cx, 450), p, font(FONT_SERIF, 130), IVORY)), .5)
    txt_in(img, t, 2.6, (W // 2, 660), "THEATER  ·  SHOWTIME", 54, IVORY)
    def clk(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, GOLD), (dm, 255)): dr.ellipse([300, 760, 440, 900], fill=c)
        d.line([370, 830, 370, 780], fill=GREEN_D, width=8); d.line([370, 830, 410, 830], fill=GREEN_D, width=8)
    show(img, t, 4.2, clk, .5)
    txt_in(img, t, 4.6, (1000, 830), "DISCOUNTED MATINEES BEFORE 4 P.M.", 52, GOLD)
    footer(img, t, 5.2, "Prices vary · compare for your theater")


# ============================== BLOCCO 19: treno ==============================
def train_big(r, m, cx, cy):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    for dr, c in ((d, IVORY), (dm, 255)):
        dr.rounded_rectangle([cx - 330, cy - 130, cx + 330, cy + 100], radius=60, fill=c)
    d.rounded_rectangle([cx - 290, cy - 90, cx + 290, cy - 10], radius=24, fill=GREEN_D)
    for k in range(4): d.rounded_rectangle([cx - 270 + k * 140, cy - 80, cx - 150 + k * 140, cy - 20], radius=10, fill=GREEN_L)
    d.rectangle([cx - 330, cy + 20, cx + 330, cy + 50], fill=RED)
    for x in (-220, 220):
        d.ellipse([cx + x - 34, cy + 80, cx + x + 34, cy + 148], fill=SAGE_D)
    d.line([cx - 380, cy + 160, cx + 380, cy + 160], fill=SAGE, width=8)


def b19c1(img, t):
    spaced(img, "NOW WE MOVE TO TRAVEL", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .2, (W // 2, 220), "THIS IS WHERE THE AGE CHANGES", 62, IVORY)
    ages = [(480, "55"), (960, "60"), (1440, "65")]
    for i, (x, a_) in enumerate(ages):
        show(img, t, .8 + i * .6, lambda r, m, x=x, a_=a_: (ImageDraw.Draw(m).ellipse([x - 150, 380, x + 150, 680], fill=255), ImageDraw.Draw(r).ellipse([x - 150, 380, x + 150, 680], fill=CARD, outline=GOLD if a_ == "65" else SAGE_D, width=8), T(r, m, (x, 530), a_, font(FONT_SERIF, 150), GOLD if a_ == "65" else IVORY)), .5)
    for x in (720, 1200):
        a = ease(seg(t, 1.6 if x == 720 else 2.2, .4))
        if a > 0: ImageDraw.Draw(img).polygon([(x, 510), (x + 50, 530), (x, 550)], fill=SAGE_D)
    txt_in(img, t, 3.2, (W // 2, 820), "TRAVEL DISCOUNTS START LATER", 56, GOLD)


def b19c2(img, t):
    spaced(img, "NUMBER NINE  ·  TRAINS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: train_big(r, m, 600, 560), .7, rise=0)
    ring(img, t, 1450, 440, 230, .10, "10%", "OFF MOST FARES", st=1.4)
    show(img, t, 3.0, lambda r, m: price_tag(r, m, 1450, 800, "65+", 300, 170), .5, angle=-6)
    txt_in(img, t, 1.0, (600, 860), "AMTRAK", 60, GOLD)


def b19c3(img, t):
    spaced(img, "NUMBER NINE  ·  TRAINS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    def us_ca(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, GREEN_L), (dm, 255)): dr.rounded_rectangle([400, 520, 1520, 880], radius=40, fill=c)
        for dr, c in ((d, CARD), (dm, 255)): dr.rounded_rectangle([400, 260, 1520, 500], radius=40, fill=c)
        d.rounded_rectangle([400, 260, 1520, 880], radius=40, outline=SAGE_D, width=5)
        T(r, m, (960, 380), "CANADA", font(FONT_SANS, 60), SAGE); T(r, m, (960, 700), "UNITED STATES", font(FONT_SANS, 60), IVORY)
    show(img, t, .4, us_ca, .6)
    d = ImageDraw.Draw(img)
    a = ease(seg(t, 1.6, .8))
    if a > 0:
        for i in range(9):
            x = 700 + i * 60 * a; d.ellipse([x - 10, 500 - 10, x + 10, 500 + 10], fill=GOLD)
    show(img, t, 2.4, lambda r, m: pill(r, m, 960, 500, "VIA RAIL CANADA ROUTES", 44), .5)
    show(img, t, 3.4, lambda r, m: price_tag(r, m, 1700, 500, "60+", 280, 160), .5, angle=-7)
    txt_in(img, t, 4.2, (W // 2, 960), "ON SHARED ROUTES IT STARTS AT SIXTY", 54, GOLD)


def b19c4(img, t):
    spaced(img, "PROOF OF AGE", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: id_card(r, m, 560, 480, 560, 330), .6, angle=-3)
    txt_in(img, t, 1.0, (560, 730), "WHEN YOU BOOK", 56, IVORY)
    show(img, t, 2.2, lambda r, m: T(r, m, (960, 480), "+", font(FONT_SANS, 130), SAGE), .4)
    show(img, t, 2.8, lambda r, m: id_card(r, m, 1360, 480, 560, 330), .6, angle=3)
    txt_in(img, t, 3.4, (1360, 730), "AND ON BOARD", 56, IVORY)


# ============================== BLOCCO 20: la pecca ==============================
def bed(r, m, cx, cy):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    for dr, c in ((d, SAGE), (dm, 255)):
        dr.rounded_rectangle([cx - 230, cy - 20, cx + 230, cy + 110], radius=24, fill=c); dr.rounded_rectangle([cx - 230, cy - 110, cx - 150, cy + 110], radius=20, fill=c)
    d.rounded_rectangle([cx - 140, cy - 80, cx - 20, cy - 10], radius=20, fill=IVORY)


def b20c1(img, t):
    spaced(img, "ONE CATCH WITH AMTRAK", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: bed(r, m, 620, 520), .6)
    bigx(img, t, 1.6, 880, 400)
    txt_in(img, t, 2.0, (620, 740), "SLEEPING ACCOMMODATIONS", 52, IVORY)
    txt_in(img, t, 2.6, (620, 810), "NOT INCLUDED", 54, RED)
    show(img, t, 3.6, lambda r, m: train_big(r, m, 1400, 560), .6, rise=0)
    show(img, t, 4.4, lambda r, m: ring_small(r, m), .5)


def ring_small(r, m):
    pill(r, m, 1400, 800, "SEATS: 10% OFF", 44)


def b20c2(img, t):
    spaced(img, "ONE CATCH WITH AMTRAK", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: coupon(r, m, 520, 480, "10% SENIOR", w=520, size=52), .5, angle=-4)
    show(img, t, 1.3, lambda r, m: T(r, m, (960, 480), "+", font(FONT_SANS, 130), SAGE), .4)
    show(img, t, 1.9, lambda r, m: coupon(r, m, 1400, 480, "OTHER OFFER", w=520, fill=SAGE, size=52), .5, angle=4)
    bigx(img, t, 3.0, 960, 480)
    txt_in(img, t, 3.6, (W // 2, 760), "CAN'T BE COMBINED", 66, RED)


def b20c3(img, t):
    spaced(img, "BEFORE YOU BOOK", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    def scales(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, GOLD), (dm, 255)):
            dr.rectangle([940, 300, 980, 700], fill=c); dr.rectangle([780, 700, 1140, 740], fill=c); dr.rectangle([560, 320, 1360, 350], fill=c)
            dr.polygon([(560, 350), (700, 350), (630, 480)], fill=c); dr.polygon([(1220, 350), (1360, 350), (1290, 480)], fill=c)
        d.ellipse([560, 460, 700, 520], fill=SAGE); d.ellipse([1220, 460, 1360, 520], fill=SAGE)
    show(img, t, .4, scales, .6)
    txt_in(img, t, 1.4, (630, 580), "COMPARE", 50, IVORY); txt_in(img, t, 1.8, (1290, 580), "BOOK", 50, IVORY)
    txt_in(img, t, 3.0, (W // 2, 840), "BUT ON A LONG TRIP", 58, IVORY)
    show(img, t, 4.4, lambda r, m: pill(r, m, W // 2, 940, "TEN PERCENT IS REAL MONEY", 52), .5)


BLOCKS3 = {
    12: [("Number four: Kohl's. Fifteen percent off every Wednesday for customers sixty and older, in the store only.", b12c1),
         ("You need an ID, it's one per customer,", b12c2),
         ("and it can't be used with other percent-off coupons.", b12c3),
         ("But dollar-off coupons and Kohl's Cash are applied first, so you can still use those.", b12c4)],
    13: [("Number five: thrift stores. Savers has Senior Tuesday: thirty percent off for customers fifty-five and older, except on new merchandise.", b13c1),
         ("Goodwill is different. There's no national rule, but some local Goodwill stores run a senior day, so ask at yours.", b13c2)],
    14: [("Number six: Michaels, for crafts and hobbies. Ten percent off your entire purchase, even sale items, for customers fifty-five and older, any day of the week.", b14c1),
         ("Show your ID at checkout or add it to your free Rewards account.", b14c2),
         ("A few things are excluded, like clearance, custom framing and books, and it's one senior discount per day.", b14c3)],
    15: [("We're halfway there, and the next one doesn't come from a store.", b15c1),
         ("It comes from your own phone bill. And unlike a Tuesday discount, it saves you money every single month.", b15c2)],
    16: [("Quick pause. If you've been keeping score, you already have restaurants, a drugstore, clothes, thrift stores and crafts.", b16c1),
         ("Tell me in the comments which one you didn't know about. I read them, and your answer helps other people find this list.", b16c2)],
    17: [("Number seven: your phone plan. AT&T has a fifty-five-plus plan: forty dollars a month for one line, or thirty-five dollars per line for two, and you prove your age with an ID.", b17c1),
         ("T-Mobile has three fifty-five-plus plans, starting at thirty dollars per line for two lines.", b17c2),
         ("Verizon's fifty-five-plus plan is only for Florida residents.", b17c3),
         ("Prices change, so check the company's page before you switch.", b17c4)],
    18: [("Number eight: the movies. AMC offers senior pricing to guests sixty and older, all day, every day.", b18c1),
         ("When you buy online, you choose the senior ticket at checkout.", b18c2),
         ("The price depends on the theater and the showtime, and AMC also has discounted matinees before four p.m., so compare the prices for your theater.", b18c3)],
    19: [("Now we move to travel, and this is where the age changes.", b19c1),
         ("Number nine: trains. Amtrak takes ten percent off most rail fares for travelers sixty-five and older.", b19c2),
         ("On routes shared with VIA Rail Canada, it starts at sixty.", b19c3),
         ("You show proof of age when you book and again on board.", b19c4)],
    20: [("One catch with Amtrak: sleeping accommodations are not included,", b20c1),
         ("and the discount can't be combined with other offers.", b20c2),
         ("So it's worth comparing before you book. But on a long trip, ten percent is real money.", b20c3)],
}


def split_frames3(block):
    total = BLOCK_FRAMES3[block]; w = [len(s) for s, _ in BLOCKS3[block]]
    fr = [round(total * x / sum(w)) for x in w]; fr[-1] = total - sum(fr[:-1])
    return fr


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = split_frames3(b)
    for i, ((s, fn), n) in enumerate(zip(BLOCKS3[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide{i:02d}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
