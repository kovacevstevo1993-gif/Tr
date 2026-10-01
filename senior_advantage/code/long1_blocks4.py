"""Video lungo 1 - blocchi 21-36. Durate dalla timeline CapCut (screenshot dell'utente: riga bianca + righello).
Uso: python3 long1_blocks4.py <blocco> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long1_blocks3 import *  # show, txt_in, pill, chip, id_card, coupon, ring, ticket, train_big, phone_icon, aarp_card, bubble, ...

BLOCK_FRAMES4 = {21: 862, 22: 507, 23: 505, 24: 505, 25: 543, 26: 455, 27: 709, 28: 459, 29: 433, 30: 416,
                 31: 553, 32: 782, 33: 534, 34: 353, 35: 319, 36: 594}


def hdr(img, t, s):
    spaced(img, s, W // 2, 90, 42, a=ease(seg(t, 0, .5)))


def sh(r, m, fn, col):
    fn(ImageDraw.Draw(r), col); fn(ImageDraw.Draw(m), 255)


def phone2(r, m, cx, cy, s, label, lsize=44):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - 120 * s, cy - 220 * s, cx + 120 * s, cy + 220 * s]
    dm.rounded_rectangle(box, radius=int(40 * s), fill=255); d.rounded_rectangle(box, radius=int(40 * s), fill=(230, 230, 225))
    d.rounded_rectangle([cx - 100 * s, cy - 180 * s, cx + 100 * s, cy + 170 * s], radius=int(24 * s), fill=GREEN_D)
    T(r, m, (cx, cy), label, font(FONT_SANS, int(lsize * s)), GOLD)


def bus(r, m, cx, cy):
    sh(r, m, lambda d, c: d.rounded_rectangle([cx - 270, cy - 150, cx + 270, cy + 100], radius=50, fill=c), IVORY)
    d = ImageDraw.Draw(r)
    for k in range(4): d.rounded_rectangle([cx - 240 + k * 118, cy - 110, cx - 150 + k * 118, cy - 20], radius=12, fill=GREEN_L)
    d.rounded_rectangle([cx + 100, cy - 110, cx + 245, cy + 40], radius=12, fill=GREEN_D)
    d.rectangle([cx - 270, cy + 30, cx + 270, cy + 58], fill=GOLD)
    for x in (-170, 170): d.ellipse([cx + x - 42, cy + 62, cx + x + 42, cy + 146], fill=GREEN_D, outline=SAGE_D, width=8)


def magnifier(r, m, cx, cy, s=1.0):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    for dr, c in ((d, SAGE), (dm, 255)):
        dr.ellipse([cx - 70 * s, cy - 70 * s, cx + 70 * s, cy + 70 * s], outline=c, width=int(18 * s))
        dr.line([cx + 50 * s, cy + 50 * s, cx + 120 * s, cy + 120 * s], fill=c, width=int(24 * s))


def mountain_pass(r, m, cx, cy, w=640, h=380, label="SENIOR PASS"):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    dm.rounded_rectangle(box, radius=34, fill=255); d.rounded_rectangle(box, radius=34, fill=IVORY)
    d.rounded_rectangle([box[0] + 18, box[1] + 18, box[2] - 18, box[1] + 18 + h * .56], radius=22, fill=(150, 205, 210))
    d.ellipse([cx + 150, box[1] + 50, cx + 220, box[1] + 120], fill=GOLD)
    d.polygon([(box[0] + 18, box[1] + 18 + h * .56), (cx - 130, box[1] + 90), (cx - 20, box[1] + 18 + h * .56)], fill=GREEN_L)
    d.polygon([(cx - 90, box[1] + 18 + h * .56), (cx + 60, box[1] + 60), (box[2] - 18, box[1] + 18 + h * .56)], fill=GREEN_D)
    T(r, m, (cx, box[3] - 80), "INTERAGENCY", font(FONT_SANS, 34), GREEN_D); T(r, m, (cx, box[3] - 38), label, font(FONT_SANS, 40), GREEN_L)


def search_bar(r, m, cx, cy, s, w=900, h=130):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    dm.rounded_rectangle(box, radius=h // 2, fill=255); d.rounded_rectangle(box, radius=h // 2, fill=IVORY)
    d.text((box[0] + 60, cy), s, font=font(FONT_SANS_M, 54), fill=GREEN_D, anchor="lm")
    d.ellipse([box[2] - 120, cy - 28, box[2] - 70, cy + 22], outline=GREEN_L, width=8); d.line([box[2] - 76, cy + 18, box[2] - 52, cy + 42], fill=GREEN_L, width=10)


# ============================== BLOCCO 21: bus e metro ==============================
def b21c1(img, t):
    hdr(img, t, "NUMBER TEN  ·  BUS & SUBWAY")
    show(img, t, .4, lambda r, m: bus(r, m, 520, 470), .7, rise=0)
    ring(img, t, 1380, 420, 230, .5, "50%", "OF PEAK FARE", st=1.4)
    show(img, t, 3.0, lambda r, m: pill(r, m, 1380, 760, "OFF-PEAK HOURS", 50), .5)
    show(img, t, 4.4, lambda r, m: price_tag(r, m, 520, 800, "65+", 300, 170), .5, angle=-6)
    txt_in(img, t, 5.4, (W // 2, 970), "FEDERAL RULE FOR SYSTEMS USING FEDERAL FUNDS", 40, SAGE, sans_m=True)


def b21c2(img, t):
    hdr(img, t, "REDUCED FARES FROM 65")
    cities = ["NEW YORK", "BOSTON", "WASHINGTON", "CHICAGO"]
    for i, c_ in enumerate(cities):
        x, y = 520 + (i % 2) * 880, 360 + (i // 2) * 300
        show(img, t, .5 + i * .8, lambda r, m, x=x, y=y, c_=c_: chip(r, m, x, y, c_, size=64, w=700, h=200), .5)
        show(img, t, 1.0 + i * .8, lambda r, m, x=x, y=y: price_tag(r, m, x + 300, y + 90, "65+", 220, 110), .4, angle=-8)
    txt_in(img, t, 4.6, (W // 2, 900), "ALL OFFER REDUCED FARES FOR RIDERS 65 AND OLDER", 48, GOLD)


def b21c3(img, t):
    hdr(img, t, "BEFORE YOU RIDE")
    show(img, t, .4, lambda r, m: search_bar(r, m, 960, 330, "reduced fare", 1000), .6)
    txt_in(img, t, 1.2, (W // 2, 470), "SEARCH YOUR CITY'S TRANSIT WEBSITE", 46, SAGE)
    show(img, t, 2.4, lambda r, m: id_card(r, m, 960, 730, 560, 330), .6, angle=-3)
    txt_in(img, t, 3.0, (W // 2, 950), "AND BRING AN ID", 62, GOLD)


# ============================== BLOCCO 22: Senior Pass ==============================
def b22c1(img, t):
    hdr(img, t, "THE ONE I PROMISED  ·  NUMBER ELEVEN")
    show(img, t, .4, lambda r, m: mountain_pass(r, m, 700, 520, 760, 450), .7, angle=-3)
    txt_in(img, t, 1.4, (1440, 400), "NATIONAL", 70, IVORY); txt_in(img, t, 1.7, (1440, 490), "PARKS", 90, GOLD)
    show(img, t, 2.8, lambda r, m: pill(r, m, 1440, 650, "INTERAGENCY SENIOR PASS", 40), .5)


def b22c2(img, t):
    hdr(img, t, "INTERAGENCY SENIOR PASS")
    show(img, t, .4, lambda r, m: price_tag(r, m, 560, 330, "62+", 380, 200), .5, angle=-5)
    txt_in(img, t, 1.1, (560, 520), "U.S. CITIZEN OR RESIDENT", 40, SAGE, sans_m=True)
    show(img, t, 1.8, lambda r, m: T(r, m, (1300, 380), "$80", font(FONT_SERIF, 280), GOLD), .6)
    txt_in(img, t, 2.8, (1300, 570), "LIFETIME PASS", 56, IVORY)
    show(img, t, 3.8, lambda r, m: pill(r, m, 960, 800, "ONCE", 90, pad=90), .5)
    txt_in(img, t, 5.2, (960, 960), "NOT EVERY YEAR  ·  ONCE", 54, GOLD)


# ============================== BLOCCO 23 ==============================
def b23c1(img, t):
    hdr(img, t, "WHAT IT COVERS")
    show(img, t, .4, lambda r, m: mountain_pass(r, m, 520, 500, 640, 380), .6, angle=-3)
    items = ["ENTRANCE FEES", "STANDARD DAY-USE FEES", "FEDERAL RECREATION SITES"]
    for i, s in enumerate(items):
        show(img, t, 1.0 + i * .9, lambda r, m, s=s, y=380 + i * 140: pill(r, m, 1300, y, s, 40, fill=CARD, fg=IVORY, pad=44), .5)


def b23c2(img, t):
    hdr(img, t, "DISCOUNTS ON SOME EXTRAS")
    opts = ["CAMPING", "SWIMMING", "BOAT LAUNCHES", "GUIDED TOURS"]
    for i, s in enumerate(opts):
        x, y = 520 + (i % 2) * 880, 400 + (i // 2) * 280
        show(img, t, .5 + i * .8, lambda r, m, x=x, y=y, s=s: chip(r, m, x, y, s, size=58, w=700, h=190), .5)
    show(img, t, 4.2, lambda r, m: pill(r, m, 960, 900, "DISCOUNT ON SOME EXTRAS", 46), .5)


def b23c3(img, t):
    hdr(img, t, "WHERE TO GET IT")
    show(img, t, .4, lambda r, m: T(r, m, (520, 400), "1,000+", font(FONT_SERIF, 190), GOLD), .6)
    txt_in(img, t, 1.2, (520, 560), "FEDERAL SITES, IN PERSON", 46, IVORY)
    show(img, t, 2.2, lambda r, m: T(r, m, (960, 480), "OR", font(FONT_SANS, 70), SAGE), .4)
    def laptop(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, IVORY), (dm, 255)):
            dr.rounded_rectangle([1200, 300, 1700, 580], radius=24, fill=c); dr.rounded_rectangle([1140, 580, 1760, 620], radius=18, fill=c)
        d.rounded_rectangle([1224, 322, 1676, 558], radius=12, fill=GREEN_D); T(r, m, (1450, 440), "ONLINE", font(FONT_SANS, 60), GOLD)
    show(img, t, 2.6, laptop, .6)
    txt_in(img, t, 3.4, (1450, 700), "OR ONLINE", 46, IVORY)


# ============================== BLOCCO 24 ==============================
def b24c1(img, t):
    hdr(img, t, "A CHEAPER WAY TO START")
    show(img, t, .4, lambda r, m: coupon(r, m, 960, 430, "$20", w=620, h=300, size=170), .6, angle=-3)
    txt_in(img, t, 1.4, (960, 680), "ANNUAL PASS", 70, IVORY)
    txt_in(img, t, 2.4, (960, 800), "EVERY YEAR", 46, SAGE)


def b24c2(img, t):
    hdr(img, t, "DO THE MATH")
    show(img, t, .4, lambda r, m: T(r, m, (960, 250), "$80  ÷  $20  =  4", font(FONT_SERIF, 150), GOLD), .6)
    for i in range(6):
        x = 330 + i * 250
        on = i < 4
        show(img, t, 1.6 + i * .35, lambda r, m, x=x, on=on, i=i: chip(r, m, x, 520, f"${20}" if on else "FREE", size=54, w=220, h=170, fill=GOLD if on else CARD, fg=GREEN_D if on else IVORY, outline=SAGE_D), .4)
        txt_in(img, t, 1.8 + i * .35, (x, 650), f"YEAR {i + 1}", 34, SAGE)
    show(img, t, 4.2, lambda r, m: pill(r, m, 960, 790, "MORE THAN 4 YEARS: LIFETIME WINS", 52), .5)
    txt_in(img, t, 6.6, (W // 2, 930), "THAT'S THE ONE I WOULD PICK FIRST", 56, IVORY)


# ============================== BLOCCO 25 ==============================
def b25c1(img, t):
    hdr(img, t, "NO WAITING FOR A CARD")
    show(img, t, .4, lambda r, m: phone2(r, m, 560, 540, 1.5, "PASS"), .6)
    show(img, t, 1.4, lambda r, m: pill(r, m, 1300, 380, "RECREATION.GOV", 56), .5)
    txt_in(img, t, 2.2, (1300, 520), "DIGITAL PASS", 80, GOLD)
    txt_in(img, t, 3.0, (1300, 640), "IMMEDIATE ACCESS", 54, IVORY)


def b25c2(img, t):
    hdr(img, t, "ORDER ONLINE, GET IT BY MAIL")
    def env(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, IVORY), (dm, 255)): dr.rounded_rectangle([400, 330, 880, 640], radius=24, fill=c)
        d.line([(400, 340), (640, 520), (880, 340)], fill=SAGE_D, width=8)
    show(img, t, .4, env, .6, angle=-3)
    ring(img, t, 1320, 480, 220, .75, "3", "WEEKS", st=1.4)
    txt_in(img, t, 3.4, (W // 2, 880), "CAN TAKE UP TO THREE WEEKS", 56, GOLD)


def b25c3(img, t):
    hdr(img, t, "READY FOR THE NEXT TRIP")
    show(img, t, .4, lambda r, m: phone2(r, m, 600, 520, 1.4, "PASS"), .6)
    show(img, t, 1.6, lambda r, m: T(r, m, (960, 520), "OR", font(FONT_SANS, 70), SAGE), .4)
    show(img, t, 2.0, lambda r, m: id_card(r, m, 1340, 520, 560, 330, "SENIOR PASS"), .6, angle=3)
    txt_in(img, t, 1.0, (600, 920), "ON YOUR PHONE", 48, IVORY); txt_in(img, t, 2.6, (1340, 920), "IN YOUR WALLET", 48, IVORY)


# ============================== BLOCCO 26-27: AARP ==============================
def b26c1(img, t):
    hdr(img, t, "NUMBER TWELVE  ·  AARP")
    show(img, t, .4, lambda r, m: aarp_card(r, m, 600, 500, 640, 360), .7, angle=-4)
    txt_in(img, t, 1.4, (1380, 380), "OPENS THE MOST", 60, IVORY); txt_in(img, t, 1.8, (1380, 470), "DOORS AT ONCE", 68, GOLD)
    show(img, t, 3.6, lambda r, m: price_tag(r, m, 1380, 680, "JOIN AT 50", 480, 170), .5, angle=-5)
    txt_in(img, t, 4.8, (W // 2, 930), "NOT SIXTY-FIVE", 56, SAGE)


def b26c2(img, t):
    hdr(img, t, "WHAT MEMBERSHIP COSTS")
    show(img, t, .4, lambda r, m: coupon(r, m, 560, 470, "$20", w=620, h=300, size=170), .6, angle=-3)
    txt_in(img, t, 1.2, (560, 690), "REGULAR YEAR", 56, IVORY)
    show(img, t, 2.4, lambda r, m: coupon(r, m, 1360, 470, "$15", w=620, h=300, fill=SAGE, size=170), .6, angle=3)
    txt_in(img, t, 3.2, (1360, 690), "FIRST YEAR", 56, IVORY)
    txt_in(img, t, 3.8, (1360, 760), "WITH AUTOMATIC RENEWAL", 38, SAGE, sans_m=True)


def b27c1(img, t):
    hdr(img, t, "CAR RENTALS  ·  AVIS & BUDGET")
    show(img, t, .4, lambda r, m: chip(r, m, 520, 380, "AVIS", size=84, w=520, h=180), .5)
    show(img, t, .8, lambda r, m: chip(r, m, 520, 590, "BUDGET", size=84, w=520, h=180), .5)
    show(img, t, 2.0, lambda r, m: price_tag(r, m, 1300, 380, "UP TO 35%", 520, 180), .5, angle=-5)
    txt_in(img, t, 2.6, (1300, 510), "OFF BASE RATES · PAY AT BOOKING", 38, IVORY)
    show(img, t, 5.0, lambda r, m: price_tag(r, m, 1300, 680, "UP TO 30%", 520, 180), .5, angle=4)
    txt_in(img, t, 5.6, (1300, 810), "WHEN YOU PAY LATER", 38, IVORY)


def b27c2(img, t):
    hdr(img, t, "HOTELS & RESTAURANTS")
    names = [("BEST WESTERN", 360), ("CHOICE HOTELS", 360), ("DENNY'S", 700)]
    show(img, t, .4, lambda r, m: chip(r, m, 520, 360, "BEST WESTERN", size=56, w=700, h=170), .5)
    show(img, t, 1.4, lambda r, m: chip(r, m, 1400, 360, "CHOICE HOTELS", size=56, w=700, h=170), .5)
    show(img, t, 2.6, lambda r, m: chip(r, m, 960, 660, "DENNY'S", size=70, w=700, h=190), .5)
    txt_in(img, t, 1.0, (520, 480), "HOTEL DISCOUNTS", 38, SAGE); txt_in(img, t, 3.2, (960, 800), "RESTAURANT SAVINGS", 42, SAGE)


def b27c3(img, t):
    hdr(img, t, "BEFORE YOU BOOK")
    show(img, t, .4, lambda r, m: aarp_card(r, m, 560, 480, 560, 320), .6, angle=-3)
    ImageDraw.Draw(img).polygon([(920, 450), (1000, 450), (1000, 420), (1060, 480), (1000, 540), (1000, 510), (920, 510)], fill=SAGE) if ease(seg(t, 1.4, .4)) > .9 else None
    show(img, t, 2.0, lambda r, m: chip(r, m, 1440, 480, "WHAT WOULD IT SAVE?", size=44, w=620, h=230), .5)
    txt_in(img, t, 3.4, (W // 2, 830), "CHECK WHAT A MEMBERSHIP WOULD SAVE YOU", 52, GOLD)


# ============================== BLOCCO 28: trucco hotel ==============================
def b28c1(img, t):
    hdr(img, t, "A SMALL TRICK FOR HOTELS")
    show(img, t, .4, lambda r, m: bed(r, m, 420, 700), .6)
    show(img, t, 1.2, lambda r, m: person(r, m, 1260, 650, 1.6), .5)
    show(img, t, 2.2, lambda r, m: bubble(r, m, 1000, 250, 880, 200, "right"), .5)
    txt_in(img, t, 2.7, (1000, 220), "\"BEST AVAILABLE RATE", 44, IVORY); txt_in(img, t, 3.0, (1000, 280), "FOR MY AGE, PLEASE?\"", 44, GOLD)
    txt_in(img, t, 4.8, (W // 2, 930), "AT CHECK-IN  ·  OR WHEN YOU BOOK BY PHONE", 46, SAGE)


def b28c2(img, t):
    hdr(img, t, "NO MEMBERSHIP NEEDED TO ASK")
    show(img, t, .4, lambda r, m: pill(r, m, 960, 300, "NO MEMBERSHIP NEEDED", 60), .5)
    show(img, t, 1.6, lambda r, m: chip(r, m, 560, 600, "NO", size=130, w=500, h=250), .5)
    txt_in(img, t, 2.2, (560, 790), "THE WORST ANSWER", 44, SAGE)
    show(img, t, 3.6, lambda r, m: chip(r, m, 1360, 600, "LOWER PRICE", size=70, w=620, h=250, outline=GOLD), .5)
    txt_in(img, t, 4.2, (1360, 790), "SOMETIMES THE ANSWER", 44, SAGE)


# ============================== BLOCCO 29-31: errori ==============================
def b29c1(img, t):
    hdr(img, t, "BEFORE THE RECAP  ·  THREE MISTAKES")
    for i, s in enumerate(["ONE", "TWO", "THREE"]):
        show(img, t, .5 + i * .7, lambda r, m, i=i, s=s: chip(r, m, 460 + i * 500, 400, s, size=90, w=400, h=220, outline=GOLD if i == 0 else SAGE_D, fg=GOLD if i == 0 else IVORY), .5)
    txt_in(img, t, 3.0, (960, 700), "MISTAKE ONE: ASKING AFTER PAYING", 62, IVORY)
    show(img, t, 4.2, lambda r, m: pill(r, m, 960, 830, "AFTER PAYING IS TOO LATE", 50), .5)


def b29c2(img, t):
    hdr(img, t, "MISTAKE ONE  ·  ASKING AFTER PAYING")
    show(img, t, .4, lambda r, m: register(r, m, 480, 480), .5)
    show(img, t, 1.2, lambda r, m: pill(r, m, 480, 700, "PAID", 56, fill=RED, fg=IVORY), .4)
    stamp_x(img, 640, 380, seg(t, 2.0, .5))
    txt_in(img, t, 2.4, (480, 800), "MOST STORES WON'T REVERSE IT", 36, SAGE, sans_m=True)
    show(img, t, 3.6, lambda r, m: chip(r, m, 1300, 380, "1  ASK", size=78, w=520, h=190, outline=GOLD, fg=GOLD), .5)
    show(img, t, 4.4, lambda r, m: chip(r, m, 1300, 620, "2  PAY", size=78, w=520, h=190), .5)
    txt_in(img, t, 5.2, (1300, 820), "THE QUESTION COMES FIRST", 40, IVORY)


def b30c1(img, t):
    hdr(img, t, "MISTAKE TWO  ·  TRUSTING AN OLD LIST")
    def paper(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, IVORY), (dm, 255)): dr.rounded_rectangle([420, 230, 940, 820], radius=18, fill=c)
        T(r, m, (680, 300), "SENIOR LIST", font(FONT_SANS, 44), GREEN_D); T(r, m, (680, 365), "2 YEARS AGO", font(FONT_SANS_M, 34), RED)
        for i in range(5): d.rounded_rectangle([480, 430 + i * 64, 880 - (i % 3) * 60, 460 + i * 64], radius=8, fill=(190, 184, 160))
    show(img, t, .4, paper, .6, angle=-3)
    stamp_x(img, 920, 260, seg(t, 2.0, .5))
    ring(img, t, 1440, 480, 220, .5, "?", "TRUE TODAY?", st=2.4)
    txt_in(img, t, 4.4, (W // 2, 930), "AGES AND RULES CHANGE", 56, GOLD)


def b30c2(img, t):
    hdr(img, t, "CHECK BEFORE YOU RELY ON IT")
    show(img, t, .4, lambda r, m: search_bar(r, m, 960, 300, "store website", 900, 120), .6)
    txt_in(img, t, 1.2, (960, 410), "CHECK THE STORE'S WEBSITE", 44, IVORY)
    show(img, t, 2.2, lambda r, m: T(r, m, (960, 540), "OR", font(FONT_SANS, 60), SAGE), .4)
    show(img, t, 2.8, lambda r, m: bubble(r, m, 960, 690, 760, 130, "left"), .5)
    txt_in(img, t, 3.3, (960, 690), "ASK THE CASHIER", 56, IVORY)
    show(img, t, 4.4, lambda r, m: pill(r, m, 960, 920, "LOOK AT THE DATE ON WHAT YOU READ", 46), .5)


def b31c1(img, t):
    hdr(img, t, "MISTAKE THREE  ·  ASSUMING DISCOUNTS ADD UP")
    show(img, t, .4, lambda r, m: coupon(r, m, 520, 450, "SENIOR 10%", w=560, size=50), .5, angle=-4)
    show(img, t, 1.3, lambda r, m: T(r, m, (960, 450), "+", font(FONT_SANS, 130), SAGE), .4)
    show(img, t, 1.9, lambda r, m: coupon(r, m, 1400, 450, "OTHER OFFER", w=560, fill=SAGE, size=50), .5, angle=4)
    stamp_x(img, 960, 450, seg(t, 3.2, .5))
    txt_in(img, t, 4.0, (W // 2, 740), "MANY CAN'T BE COMBINED", 62, RED)
    txt_in(img, t, 5.0, (W // 2, 840), "LIKE THE AMTRAK DISCOUNT, OR WITH SALE PRICES", 40, SAGE, sans_m=True)


def b31c2(img, t):
    hdr(img, t, "ASK WHICH ONE IS BETTER FOR YOU")
    show(img, t, .4, lambda r, m: coupon(r, m, 520, 430, "SALE PRICE", w=600, size=52, fill=SAGE), .5, angle=-3)
    show(img, t, 1.0, lambda r, m: T(r, m, (960, 430), "VS", font(FONT_SANS, 90), GOLD), .4)
    show(img, t, 1.4, lambda r, m: coupon(r, m, 1400, 430, "SENIOR 10%", w=600, size=52), .5, angle=3)
    txt_in(img, t, 2.8, (520, 620), "SOMETIMES A SALE BEATS IT", 40, IVORY)
    txt_in(img, t, 4.2, (1400, 620), "SOMETIMES SENIOR WINS", 40, IVORY)
    show(img, t, 5.6, lambda r, m: pill(r, m, 960, 860, "ASK WHICH ONE IS BETTER", 56), .5)


# ============================== BLOCCO 32: ricapitolazione ==============================
RECAP = [("50", ["AARP"]), ("55", ["WALGREENS", "ROSS", "SAVERS", "MICHAELS", "DENNY'S & IHOP", "PHONE PLAN"]),
         ("60", ["KOHL'S", "AMC"]), ("62", ["PARKS PASS"]), ("65", ["AMTRAK", "HALF-FARE TRANSIT"])]


def recap_card(img, t, x, y, age, items, st, w=330, fs=29, step=62, af=78):
    def card(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        h = 60 + af + step * max(len(items), 1)
        box = [x - w / 2, y, x + w / 2, y + h]
        dm.rounded_rectangle(box, radius=28, fill=255); d.rounded_rectangle(box, radius=28, fill=CARD, outline=GOLD if age == "55" else SAGE_D, width=5)
        T(r, m, (x, y + 20 + af * .6), age + "+", font(FONT_SERIF, af), GOLD)
    show(img, t, st, card, .5)
    for i, s in enumerate(items):
        txt_in(img, t, st + .5 + i * .45, (x, y + 60 + af + step * (i + .5)), s, fs, IVORY, sans_m=True)


def b32c1(img, t):
    hdr(img, t, "PUTTING IT ALL TOGETHER")
    recap_card(img, t, 960, 170, "55", RECAP[1][1], .5, w=800, fs=50, step=96, af=130)


def b32c2(img, t):
    hdr(img, t, "PUTTING IT ALL TOGETHER")
    k = dict(fs=38, step=84, af=110)
    recap_card(img, t, 260, 260, "60", RECAP[2][1], .4, w=420, **k)
    recap_card(img, t, 730, 260, "62", RECAP[3][1], 2.6, w=420, **k)
    recap_card(img, t, 1230, 260, "65", RECAP[4][1], 4.4, w=500, **dict(k, fs=34))
    recap_card(img, t, 1690, 260, "50", RECAP[0][1], 6.6, w=360, **k)


def b32c3(img, t):
    hdr(img, t, "SEE THE PATTERN?")
    xs = [330, 650, 970, 1290, 1610]
    ImageDraw.Draw(img).line([200, 450, 1720, 450], fill=SAGE_D, width=8)
    for i, ((age, _), x) in enumerate(zip([RECAP[0], RECAP[1], RECAP[2], RECAP[3], RECAP[4]], xs)):
        show(img, t, .4 + i * .4, lambda r, m, x=x, age=age: (ImageDraw.Draw(m).ellipse([x - 90, 360, x + 90, 540], fill=255), ImageDraw.Draw(r).ellipse([x - 90, 360, x + 90, 540], fill=CARD, outline=GOLD, width=7), T(r, m, (x, 450), age, font(FONT_SERIF, 90), IVORY)), .4)
    show(img, t, 2.8, lambda r, m: pill(r, m, 1000, 700, "ALMOST ALL OF IT STARTS BEFORE 65", 56), .5)


# ============================== BLOCCO 33-34: piano d'azione ==============================
def b33c1(img, t):
    hdr(img, t, "WHAT TO DO THIS WEEK")
    for i in range(3):
        show(img, t, .5 + i * .7, lambda r, m, i=i: chip(r, m, 460 + i * 500, 380, f"PLACE {i + 1}", size=62, w=420, h=200), .5)
    txt_in(img, t, 2.8, (960, 560), "PICK THREE PLACES WHERE YOU ALREADY SPEND MONEY", 46, IVORY)
    show(img, t, 4.4, lambda r, m: pill(r, m, 960, 760, "ASK THE QUESTION BEFORE YOU PAY", 54), .5)


def b33c2(img, t):
    hdr(img, t, "BUILD YOUR LIST")
    show(img, t, .4, lambda r, m: chip(r, m, 520, 330, "AGE  +  DAY", size=62, w=700, h=180), .5)
    txt_in(img, t, 1.0, (520, 450), "WRITE THEM DOWN", 40, SAGE)
    for i, (lab, n) in enumerate([("WEEK 1", "3"), ("WEEK 2", "6"), ("WEEK 3", "9"), ("WEEK 4", "12")]):
        x = 360 + i * 400
        show(img, t, 2.4 + i * .9, lambda r, m, x=x, n=n: chip(r, m, x, 690, n, size=110, w=300, h=200, outline=GOLD if n == "12" else SAGE_D, fg=GOLD if n == "12" else IVORY), .4)
        txt_in(img, t, 2.6 + i * .9, (x, 830), lab, 36, SAGE)
    txt_in(img, t, 6.6, (W // 2, 960), "A LIST THAT WORKS FOR YOU EVERY YEAR", 52, GOLD)


def b34c1(img, t):
    hdr(img, t, "ONE MORE TIP")
    def phone(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, (230, 230, 225)), (dm, 255)): dr.rounded_rectangle([700, 170, 1220, 1000], radius=70, fill=c)
        d.rounded_rectangle([724, 200, 1196, 970], radius=44, fill=(250, 245, 220))
        T(r, m, (960, 270), "NOTES", font(FONT_SANS, 46), (170, 130, 40))
        for i, (a, b) in enumerate([("Walgreens", "55 · 1st Tue"), ("Kohl's", "60 · Wed"), ("Michaels", "55 · any day")]):
            y = 400 + i * 150
            d.text((770, y), a, font=font(FONT_SANS, 40), fill=GREEN_D, anchor="lm"); d.text((770, y + 52), b, font=font(FONT_SANS_M, 32), fill=GREEN_L, anchor="lm")
            d.line([770, y + 95, 1150, y + 95], fill=(210, 200, 170), width=3)
    show(img, t, .4, phone, .7, rise=0)
    for i, s in enumerate(["THE PLACE", "THE AGE", "THE DAY"]):
        show(img, t, 1.6 + i * .8, lambda r, m, s=s, y=420 + i * 150: pill(r, m, 330, y, s, 44), .5)
    txt_in(img, t, 4.4, (1560, 600), "NOTES APP", 54, GOLD)


def b34c2(img, t):
    hdr(img, t, "ALWAYS WITH YOU")
    show(img, t, .4, lambda r, m: phone2(r, m, 560, 520, 1.5, "LIST"), .6)
    show(img, t, 1.6, lambda r, m: pill(r, m, 1300, 420, "RIGHT WHERE YOU NEED IT", 54), .5)
    txt_in(img, t, 2.6, (1300, 570), "THE LIST IS ALWAYS WITH YOU", 44, IVORY)


# ============================== BLOCCO 35: iscriviti ==============================
def b35c1(img, t):
    hdr(img, t, "IF THIS HELPED YOU")
    def thumb(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, IVORY), (dm, 255)):
            dr.rounded_rectangle([420, 520, 560, 760], radius=14, fill=c)
            dr.polygon([(600, 520), (700, 360), (760, 340), (790, 400), (740, 520), (900, 520), (930, 580), (900, 740), (860, 760), (600, 760)], fill=c)
    show(img, t, .4, thumb, .6)
    txt_in(img, t, 1.0, (660, 860), "LIKE", 64, IVORY)
    show(img, t, 1.8, lambda r, m: pill(r, m, 1340, 560, "SUBSCRIBE", 80, fill=RED, fg=IVORY, pad=80), .6)
    txt_in(img, t, 2.8, (1340, 720), "THE SENIOR ADVANTAGE", 46, GOLD)


def b35c2(img, t):
    hdr(img, t, "SAVE EVEN MORE")
    txt_in(img, t, .4, (560, 330), "ANOTHER VIDEO", 80, IVORY); txt_in(img, t, .8, (560, 440), "THAT CAN HELP", 80, GOLD)
    txt_in(img, t, 1.4, (560, 580), "IS ON YOUR SCREEN RIGHT NOW", 44, SAGE)
    bx0, by0, bx1, by1 = 1150, 250, 1830, 710
    a = ease(seg(t, 1.0, .5))
    if a > 0:
        d = ImageDraw.Draw(img)
        for x in range(bx0 + 20, bx1 - 20, 40): d.line([x, by0, x + 20, by0], fill=GOLD, width=4); d.line([x, by1, x + 20, by1], fill=GOLD, width=4)
        for y in range(by0 + 20, by1 - 20, 40): d.line([bx0, y, bx0, y + 20], fill=GOLD, width=4); d.line([bx1, y, bx1, y + 20], fill=GOLD, width=4)
        d.text(((bx0 + bx1) / 2, by1 + 50), "WATCH NEXT", font=font(FONT_SANS, 40), fill=GOLD, anchor="mm")
    ImageDraw.Draw(img).polygon([(900, 450), (1020, 450), (1020, 410), (1100, 480), (1020, 550), (1020, 510), (900, 510)], fill=SAGE) if ease(seg(t, 2.0, .4)) > .9 else None


# ============================== BLOCCO 36: disclaimer finale ==============================
def b36(img, t):
    spaced(img, "BEFORE YOU GO", W // 2, 120, 44, a=ease(seg(t, 0, .6)))
    txt_in(img, t, .3, (560, 330), "ALWAYS ASK", 110, IVORY)
    txt_in(img, t, .9, (560, 470), "BEFORE YOU PAY", 90, GOLD)
    pa = ease(seg(t, 1.6, .6))
    if pa > 0:
        panel(img, [100, 600, 1020, 1010], radius=34, border=SAGE_D, bw=4)
    lines = ["Discounts, ages and prices change", "and differ by location and plan.", "Always confirm with the business", "or the official source before you rely on them.", "General information, not financial advice.", "Not affiliated with any company mentioned."]
    for i, l in enumerate(lines):
        txt_in(img, t, 2.0 + i * .5, (560, 650 + i * 58), l, 36, IVORY if i < 4 else SAGE, sans_m=True)
    bx0, by0, bx1, by1 = 1150, 250, 1830, 710
    d = ImageDraw.Draw(img)
    for x in range(bx0 + 20, bx1 - 20, 40): d.line([x, by0, x + 20, by0], fill=GOLD, width=4); d.line([x, by1, x + 20, by1], fill=GOLD, width=4)
    for y in range(by0 + 20, by1 - 20, 40): d.line([bx0, y, bx0, y + 20], fill=GOLD, width=4); d.line([bx1, y, bx1, y + 20], fill=GOLD, width=4)
    d.text(((bx0 + bx1) / 2, by1 + 50), "WATCH NEXT", font=font(FONT_SANS, 40), fill=GOLD, anchor="mm")


BLOCKS4 = {
    21: [("Number ten: your local bus or subway. Federal rules say that transit systems using federal funds can't charge older riders more than half of the regular peak fare during off-peak hours, and the rule counts everyone sixty-five and older.", b21c1),
         ("Big systems in New York, Boston, Washington and Chicago all offer reduced fares from sixty-five.", b21c2),
         ("Search your city's transit website for reduced fare, and bring an ID.", b21c3)],
    22: [("Here comes the one I promised. Number eleven: the Interagency Senior Pass for national parks.", b22c1),
         ("If you're a United States citizen or resident, sixty-two or older, a lifetime pass costs eighty dollars. Once. Not every year. Once.", b22c2)],
    23: [("It covers entrance fees and standard day-use fees at federal recreation sites,", b23c1),
         ("and it can give you a discount on some extras, like camping, swimming, boat launches and guided tours.", b23c2),
         ("You can buy it in person at more than a thousand federal sites, or online.", b23c3)],
    24: [("And there's a cheaper way to start: an annual pass costs twenty dollars.", b24c1),
         ("But do the math. Eighty divided by twenty is four. If you plan to use it for more than four years, the lifetime pass is the smarter buy. That's the one I would pick first.", b24c2)],
    25: [("And if you don't want to wait for a card in the mail, there's a digital pass through Recreation dot gov, with immediate access.", b25c1),
         ("You can also order online and have it mailed, but that can take up to three weeks.", b25c2),
         ("Keep it on your phone or in your wallet, and you're ready for the next trip.", b25c3)],
    26: [("Number twelve is the one that opens the most doors at once: AARP. And you can join at fifty, not sixty-five.", b26c1),
         ("A regular year costs twenty dollars, and the first year can be fifteen with automatic renewal.", b26c2)],
    27: [("Members can save up to thirty-five percent off base rates on Avis and Budget rentals when they pay at booking, or up to thirty percent when they pay later.", b27c1),
         ("AARP also lists hotel discounts, like Best Western and Choice Hotels, and restaurant savings at places like Denny's.", b27c2),
         ("So before you book your next trip, check what a membership would save you.", b27c3)],
    28: [("And here's a small trick for hotels. When you check in, or when you book by phone, ask for the best available rate for your age.", b28c1),
         ("You don't need a membership to ask. The worst answer is no, and sometimes the answer is a lower price.", b28c2)],
    29: [("Before the recap, three mistakes that cost people their discount. Mistake one: asking after paying.", b29c1),
         ("Once the payment is done, most stores won't reverse it, so the question comes first, every time.", b29c2)],
    30: [("Mistake two: trusting an old list. Ages and rules change, and a list that was true two years ago may not be true today.", b30c1),
         ("Check the store's website, or ask the cashier, and look at the date on whatever you read.", b30c2)],
    31: [("Mistake three: assuming discounts add up. Many can't be combined with other offers, like the Amtrak discount, or with sale prices.", b31c1),
         ("So ask which one is better for you. Sometimes a sale beats the senior discount. Sometimes the senior discount wins.", b31c2)],
    32: [("Let's put it all together. Fifty-five: Walgreens, Ross, Savers, Michaels, the Denny's and IHOP senior menus, and your phone plan.", b32c1),
         ("Sixty: Kohl's and AMC. Sixty-two: the national parks pass. Sixty-five: Amtrak and half-fare transit. And fifty for AARP.", b32c2),
         ("See the pattern? Almost all of it starts before sixty-five.", b32c3)],
    33: [("So here's what to do this week. Pick three places where you already spend money. Ask the question before you pay.", b33c1),
         ("Write down the age and the day. Next week, add three more. Do that for a month, and you'll have a list that works for you every year.", b33c2)],
    34: [("And one more tip. Put the three best ones for you in the notes app on your phone: the place, the age and the day of the week.", b34c1),
         ("Now the list is always with you, right where you need it.", b34c2)],
    35: [("If this helped you, hit like and subscribe to The Senior Advantage.", b35c1),
         ("And if you want to save even more, another video that can help is on your screen right now.", b35c2)],
    36: [("One last thing. Discounts, ages and prices change and differ by location and plan. Always confirm with the business or the official source before you rely on them. This video is general information, not financial advice, and this channel is not affiliated with any company mentioned.", b36)],
}


def split_frames4(block):
    total = BLOCK_FRAMES4[block]; w = [len(s) for s, _ in BLOCKS4[block]]
    fr = [round(total * x / sum(w)) for x in w]; fr[-1] = total - sum(fr[:-1])
    return fr


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = split_frames4(b)
    for i, ((s, fn), n) in enumerate(zip(BLOCKS4[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide{i:02d}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
