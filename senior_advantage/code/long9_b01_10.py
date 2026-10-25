"""Video lungo 9 (ALDI) - blocchi 1-10. Voce: COPIONE-VIDEO-ALDI.md. Durate dalla timeline dell'utente (25/10/2026)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long9_kit import *

def I(fn, s=1.0, **kw):
    return lambda c, x, y: fn(c, x, y, s, **kw)

def S(img, t, b, key, spr, x, y, n=1, **kw):
    return show(img, t, T(b, key, n), spr, x, y, **kw)

def donut_spr(frac, size=360, width=34, col=GOLD):
    q = int(round(frac * 100))
    def build():
        ss = 2; N = size * ss
        im = Image.new("RGBA", (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        m = 14 * ss
        d.ellipse([m, m, N - m, N - m], outline=(22, 70, 60, 255), width=width * ss)
        if q > 0:
            d.arc([m, m, N - m, N - m], -90, -90 + 360 * q / 100.0, fill=col + (255,), width=width * ss)
        return bake(im.resize((size, size), Image.LANCZOS), 12, 8, 0.4)
    return cache(("dn9", q, size, width, col), build)

def thumb_video():
    def fn(c):
        w, h = 250, 150
        vgrad(c, (2, 2, w - 2, h - 2), 14, (70, 80, 84), (34, 40, 44), outline=(150, 160, 156), width=3)
        c.poly([(w / 2 - 14, 34), (w / 2 + 22, 56), (w / 2 - 14, 78)], fill=IVORY)
        c.text((w / 2, 104), "HIDDEN ALDI", FONT_SANS, 20, GOLD, track=2)
        c.text((w / 2, 128), "SENIOR DISCOUNTS?", FONT_SANS, 17, IVORY, track=1)
    return mk("thumbv", 250, 150, fn, blur=8, dy=6)

def helppage():
    def fn(c):
        w, h = 860, 560
        c.rrect((3, 3, w - 3, h - 3), 22, fill=PAPER, outline=(150, 164, 156), width=4)
        c.rrect((3, 3, w - 3, 64), 22, fill=(206, 218, 210)); c.d.rectangle(c._b((3, 44, w - 3, 64)), fill=(206, 218, 210))
        for k in range(3):
            c.ell((28 + k * 28, 24, 44 + k * 28, 40), fill=(CORAL, AMBER, OKG)[k])
        c.rrect((130, 16, w - 40, 50), 17, fill=PAPER)
        c.text((152, 33), "help.aldi.us", FONT_SANS_M, 22, (90, 100, 94), anchor="lm")
        c.rrect((3, 64, w - 3, 150), 0, fill=GREEN_D)
        c.text((40, 107), "ALDI HELP CENTER", FONT_SANS, 40, IVORY, anchor="lm", track=4)
        for i, wd in enumerate((620, 700, 540)):
            c.rrect((40, 190 + i * 34, 40 + wd, 208 + i * 34), 8, fill=(206, 210, 202))
        for i, wd in enumerate((500, 420)):
            c.rrect((40, 420 + i * 34, 40 + wd, 438 + i * 34), 8, fill=(206, 210, 202))
    return mk("helppg9", 860, 560, fn, blur=18, dy=12)

def hl_bar():
    return mk("hlbar9", 790, 120, lambda c: (c.rrect((2, 2, 788, 118), 14, fill=GOLD), c.rrect((20, 28, 620, 46), 8, fill=(190, 140, 50)), c.rrect((20, 70, 450, 88), 8, fill=(190, 140, 50))), shadow=False)

# ============================================================ 1
def draw1(img, t):
    b = 1
    head9(img, t, 0, "THE SENIOR DISCOUNT QUESTION")
    show(img, t, 0.25, helppage(), 520, 560, mode="left", amp=4, dur=0.7)
    t1 = T(b, "In plain words")
    show(img, t, t1 - 0.1, hl_bar(), 520, 585, mode="fade", fl=False, dur=0.5)
    show(img, t, t1, quote9("q1", 800, 250, ["DOES NOT OFFER DISCOUNTS", "AT ITS STORE LOCATIONS"], 40), 1400, 330, mode="right", amp=4)
    show(img, t, t1 + 0.7, pill9("LOWEST POSSIBLE PRICES", 380, 58, fill=SAGE), 1210, 505, mode="up", amp=3)
    show(img, t, t1 + 1.1, pill9("MOSTLY EXCLUSIVE BRANDS", 390, 58, fill=SAGE), 1600, 505, mode="up", amp=3)
    t2 = T(b, "No senior day")
    show(img, t, t2, stamp9("NO SENIOR DAY", 380, 96, CORAL), 1210, 640, rot=-2, amp=3)
    show(img, t, t2 + 0.4, stamp9("NO AGE DISCOUNT", 380, 96, CORAL), 1610, 640, rot=2, amp=3)
    t3 = T(b, "some videos promise"); t4 = T(b, "ten real things")
    for k in range(3):
        show(img, t, t3 + k * 0.18, thumb_video(), 1160 + k * 270, 835, amp=5, ph=k, t_out=t4 - 0.2)
    show(img, t, t3 + 0.2, pill9("HIDDEN SENIOR DISCOUNTS?", 440, 58, fill=IVORY), 1430, 950, mode="up", amp=2, t_out=t4 - 0.2)
    show(img, t, t4, bignum("n10", 440, 230, "10", "REAL THINGS", GOLD, vsize=130), 1230, 840, amp=4)
    t5 = T(b, "Not one of them")
    show(img, t, t5, okb(96), 1600, 800, amp=3)
    show(img, t, t5 + 0.2, pill9("NOT ONE IS A TRICK", 400, 62, fill=OKG), 1600, 905, mode="up", amp=2)

# ============================================================ 2
def card5(key, w, h, icon, l1, l2, accent=GOLD):
    return paper9(key, w, h, l1, [(l2, INK)], accent=accent, size=28, tsize=28, align="center", icon=None)

def mini_icon_card(key, w, h, icon, top, bottom, accent=SAGE_D, glow=False):
    def fn(c):
        vgrad(c, (3, 3, w - 3, h - 3), 28, (16, 68, 54), (8, 42, 34), outline=GOLD if glow else accent, width=6 if glow else 4)
        icon(c, w / 2, h * 0.34)
        s = 30
        while tw(top, s, 3) > w - 30 and s > 14:
            s -= 2
        c.text((w / 2, h * 0.66), top, FONT_SANS, s, GOLD if glow else IVORY, track=3)
        if bottom:
            s = 24
            while tw(bottom, s, 2) > w - 30 and s > 12:
                s -= 2
            c.text((w / 2, h * 0.82), bottom, FONT_SANS_M, s, SAGE, track=2)
    return mk(("mic9", key, w, h), w, h, fn)

def draw2(img, t):
    b = 2
    head9(img, t, 0, "WHAT'S COMING: TEN THINGS")
    show(img, t, 0.2, bignum("n10b", 360, 190, "10", "THINGS", GOLD, vsize=104), 330, 290, amp=3)
    show(img, t, T(b, "all from Aldi's own pages"), pill9("ALL FROM ALDI'S OWN PAGES", 560, 70, fill=IVORY), 1090, 290, mode="left", amp=2)
    xs = [260, 620, 980, 1340, 1700]
    cards = [("coin", "SMALL COIN", "THAT COMES BACK", lambda c, x, y: ic_coin25(c, x, y, 1.05), "small coin"),
             ("day", "A DAY OF THE WEEK", "NEW ITEMS SHOW UP", lambda c, x, y: ic_weekstrip(c, x, y + 4, 1.12, 2), "day of the week"),
             ("rcp", "A RECEIPT RULE", "CAN COST YOU A REFUND", lambda c, x, y: ic_receipt(c, x, y, 1.15), "rule about your receipt"),
             ("onl", "ORDERING ONLINE", "THE REAL COST", lambda c, x, y: ic_phone_app(c, x, y, 0.95), "real cost of ordering online")]
    for i, (k, a, bb, ic, key) in enumerate(cards):
        show(img, t, T(b, key), mini_icon_card(("c2", k), 320, 400, ic, a, bb), xs[i], 600, mode="up", amp=6, ph=i)
    tt = T(b, "number ten")
    show(img, t, tt, mini_icon_card(("c2", "ten"), 340, 430, I(ic_shield, 1.0, mark=lambda c, x, y, s: check_ic(c, x, y + 2, s * 0.62, GOLD)), "NUMBER TEN", "ALDI'S STRONGEST PROMISE", glow=True), xs[4], 600, amp=6, ph=4)
    show(img, t, tt + 0.6, pill9("ONE SIMPLE THING BEFORE YOU LEAVE", 720, 66, fill=GOLD), 1330, 880, mode="up", amp=3)
    show(img, t, T(b, "Stay for that one"), pill9("STAY FOR NUMBER TEN", 460, 66, fill=OKG), 1330, 975, mode="up", amp=3)

# ============================================================ 3
def draw3(img, t):
    b = 3
    head9(img, t, 0, "IS THIS ONLY FOR SENIORS?")
    show(img, t, T(b, "Is this video only"), paper9("q3", 520, 190, "ONLY FOR SENIORS?", [("THE HONEST ANSWER:", INK)], GOLD, 34, 32, "center"), 380, 330, mode="left", amp=4)
    show(img, t, T(b, "No, and I want"), stamp9("NO", 190, 110, OKG, 60), 600, 440, rot=-6, amp=3)
    show(img, t, T(b, "Nothing on Aldi's pages"), glass9("age3", 520, 150, lambda c, x, y: (ic_person(c, x, y + 6, 0.8, GOLD), ic_x(c, x + 30, y + 30, 0.55, CORAL, 14)),
        "NOTHING DEPENDS", "ON YOUR AGE", col=GOLD, tsize=36, ssize=30), 380, 560, mode="left", amp=4)
    t_o = T(b, "if you're over sixty")
    show(img, t, t_o, pill9("IF YOU'RE OVER SIXTY, THESE MATTER MORE", 900, 66, fill=GOLD), 1290, 290, mode="down", amp=2)
    trio = [("avoid a wasted trip", I(ic_pin8, 1.3), "AVOID A", "WASTED TRIP"), ("carry less", I(ic_tote, 0.9), "CARRY", "LESS"), ("get your money back", I(ic_receipt, 1.0), "MONEY BACK,", "NO ARGUMENT")]
    for i, (k, ic, a, bb) in enumerate(trio):
        show(img, t, T(b, k), mini_icon_card(("t3", i), 360, 330, ic, a, bb), 970 + i * 400 - 100 + 0, 520, mode="up", amp=6, ph=i)
    ts = T(b, "Everything here comes from")
    show(img, t, ts, glass9("s3a", 400, 120, I(ic_doc, 0.55), "ALDI HELP CENTER", None, col=SAGE_D, tsize=28), 260, 830, mode="up", amp=3)
    show(img, t, ts + 0.3, glass9("s3b", 400, 120, I(ic_building, 0.55), "CORPORATE PAGES", None, col=SAGE_D, tsize=28), 680, 830, mode="up", amp=3)
    td = T(b, "doesn't date")
    show(img, t, td, glass9("d3", 420, 120, lambda c, x, y: (ic_calendar(c, x, y, 0.5), ic_x(c, x + 22, y + 22, 0.45, CORAL, 14)), "NO DATE ON", "THESE PAGES", col=CORAL, tsize=26, ssize=26), 1110, 830, mode="up", amp=3)
    show(img, t, T(b, "checkout screen"), glass9("f3", 520, 120, I(ic_register, 0.45), "CHECKOUT SCREEN =", "YOUR FINAL ANSWER", col=OKG, tsize=26, ssize=28), 1600, 830, mode="up", amp=3)
    show(img, t, LAST(b), pill9("FROM ALDI'S OWN PAGES, EVERY TIME", 640, 62, fill=IVORY), 960, 975, mode="up", amp=2)

# ============================================================ 4
def draw4(img, t):
    b = 4
    head9(img, t, 0, "TWO THINGS YOU MIGHT BE THINKING")
    show(img, t, T(b, "some of you are thinking"), say9("b4a", 760, 150, ["\"I DON'T SHOP AT", "ALDI MUCH\""], 44), 470, 290, mode="left", amp=4)
    show(img, t, T(b, "Fair enough"), glass9("f4", 700, 130, I(ic_pin8, 1.0), "WORTH KNOWING BEFORE", "YOUR FIRST TRIP", col=OKG, tsize=34, ssize=34), 470, 560, mode="left", amp=4)
    show(img, t, T(b, "busy week"), glass9("w4", 700, 130, I(ic_calendar, 0.5), "...AND BEFORE", "A BUSY WEEK", col=OKG, tsize=34, ssize=34), 470, 730, mode="left", amp=4)
    show(img, t, T(b, "Others are thinking"), say9("b4b", 760, 150, ["\"I DON'T USE APPS,", "I JUST WALK IN\""], 44, tail="br"), 1440, 290, mode="right", amp=4)
    show(img, t, T(b, "I don't use apps"), mk("noapp4", 200, 230, lambda c: (ic_phone_app(c, 100, 115, 1.5), ic_x(c, 100, 115, 1.0, CORAL, 22))), 1150, 500, amp=5)
    show(img, t, T(b, "Stay anyway"), stamp9("STAY ANYWAY", 380, 100, GOLD), 1500, 480, rot=-3, amp=3)
    t6 = T(b, "no phone at all")
    show(img, t, t6, glass9("np4", 700, 130, I(ic_storefront, 0.6), "MOST OF THIS LIST:", "NO PHONE AT ALL", col=OKG, tsize=34, ssize=34), 1440, 720, mode="right", amp=4)
    t8 = T(b, "number eight")
    show(img, t, t8, badge_ic(("n8", 4), 130, lambda c, x, y, s: c.text((x, y + 2), "8", FONT_SANS, 76, GOLD), GOLD), 1130, 900, amp=4)
    show(img, t, t8 + 0.25, glass9("on4", 560, 130, I(ic_phone_app, 0.45), "ONLY NUMBER EIGHT:", "ORDERING ONLINE", col=GOLD, tsize=30, ssize=34), 1560, 900, mode="right", amp=4)
    show(img, t, T(b, "what it costs"), pill9("I'LL TELL YOU WHAT IT COSTS", 600, 62, fill=GOLD), 470, 940, mode="up", amp=2)

# ============================================================ 5
def draw5(img, t):
    b = 5
    head9(img, t, 0, "BEFORE WE START")
    rc = receipt9("r5", 420, 640, [("EXCLUSIVE BRANDS", ""), ("CART QUARTER", ""), ("ALDI FINDS", ""), ("THE ITEM YOU RETURN", ""), ("TOTAL", "")], hl=3, foot="KEEP IT", hlcol=GOLD)
    show(img, t, T(b, "Keep your receipt"), rc, 360, 600, mode="up", amp=4, rot=-2)
    show(img, t, T(b, "Keep your receipt") + 0.5, stamp9("KEEP IT", 240, 90, OKG, 40), 540, 870, rot=-6, amp=3)
    t9 = T(b, "number nine and number ten")
    show(img, t, t9, badge_ic(("n9", 5), 110, lambda c, x, y, s: c.text((x, y + 2), "9", FONT_SANS, 64, GOLD)), 640, 380, amp=4)
    show(img, t, t9 + 0.3, badge_ic(("n10", 5), 110, lambda c, x, y, s: c.text((x, y + 2), "10", FONT_SANS, 52, GOLD)), 640, 520, amp=4, ph=1)
    tc = T(b, "fluctuate from city to city")
    for k in range(3):
        show(img, t, tc + k * 0.25, mk(("st5", k), 220, 200, lambda c, k=k: (ic_storefront(c, 110, 100, 1.2), c.rrect((20 + k * 20, 168, 200 - k * 20, 198), 8, fill=GOLD), c.text((110, 183), "PRICE", FONT_SANS, 20, GREEN_D, track=2))), 1010 + k * 290, 400, amp=6, ph=k)
    show(img, t, tc + 0.3, pill9("PRICES CAN VARY FROM CITY TO CITY", 760, 62, fill=SAGE), 1290, 560, mode="up", amp=2)
    ts = T(b, "single product price")
    show(img, t, ts, mk("nopr5", 300, 200, lambda c: (ic_box8(c, 150, 100, 1.0), c.rrect((90, 70, 210, 130), 10, fill=GOLD), c.text((150, 100), "$ ?", FONT_SANS, 40, GREEN_D), c.line([(70, 30), (230, 170)], CORAL, 14))), 1000, 740, amp=5)
    show(img, t, ts + 0.3, pill9("NOT A SINGLE PRODUCT PRICE", 560, 62, fill=CORAL, ink=IVORY), 1000, 900, mode="up", amp=2)
    tr = T(b, "rules, fees and policies")
    show(img, t, tr, checklist9("c5", 520, ["RULES", "FEES", "POLICIES"], 36, 70), 1560, 760, mode="right", amp=3)
    show(img, t, T(b, "things you can check"), pill9("THINGS YOU CAN CHECK", 480, 62, fill=OKG), 1560, 900, mode="up", amp=2)

# ============================================================ 6
def productbox(key, label, col, w=260, h=250):
    def fn(c):
        c.poly([(24, 60), (w - 24, 60), (w - 10, h - 30), (10, h - 30)], fill=col)
        c.rrect((10, 40, w - 10, 80), 6, fill=tuple(min(255, v + 30) for v in col))
        c.rrect((40, 100, w - 40, h - 70), 10, fill=PAPER)
        c.text((w / 2, 150), label, FONT_SANS, 24, INK, track=2)
        c.rrect((54, 176, w - 54, 190), 6, fill=(190, 186, 174))
    return mk(("pbox9", key, w, h), w, h, fn, blur=12, dy=8)

def bar6(label, frac, col):
    def fn(c):
        w, h = 760, 120
        c.text((0, 26), label, FONT_SANS, 26, IVORY, anchor="lm", track=3)
        c.rrect((0, 52, (w - 40) * frac, 108), 16, fill=col)
        c.rrect((0, 52, (w - 40) * frac, 70), 16, fill=tuple(min(255, v + 40) for v in col))
    return mk(("bar6", label, frac), 760, 120, fn, shadow=False)

def draw6(img, t):
    b = 6
    head9(img, t, 1, "EXCLUSIVE BRANDS")
    t1 = T(b, "more than ninety percent")
    f = ease(seg(t, t1, 1.4)) * 0.9
    if t >= t1 - 0.2:
        put(img, donut_spr(f), 360, 470)
        pc = int(round(f * 100))
        put(img, tspr("%d%%+" % pc if pc >= 90 else "%d%%" % pc, FONT_SANS, 76, GOLD), 360, 462)
    show(img, t, t1 + 0.5, glass9("g6", 560, 130, None, "ALDI EXCLUSIVE BRANDS", "OF ITS PRODUCT SELECTION", col=GOLD, tsize=30, ssize=28), 360, 740, mode="up", amp=3)
    tg = T(b, "as good as or better")
    show(img, t, tg, productbox("nb", "NAME BRAND", (110, 120, 128)), 900, 340, amp=5)
    show(img, t, tg + 0.2, mk("ge6", 120, 120, lambda c: c.text((60, 58), "≥", FONT_SANS, 100, GOLD), shadow=False), 1130, 340, amp=2)
    show(img, t, tg + 0.4, productbox("ab", "ALDI BRAND", (70, 140, 100)), 1380, 340, amp=5, ph=1)
    show(img, t, tg + 0.7, pill9("AS GOOD AS OR BETTER THAN NAME BRANDS", 760, 58, fill=IVORY), 1140, 510, mode="up", amp=2)
    tf = T(b, "up to fifty percent")
    grow_x(img, t, tf - 0.2, bar6("NATIONAL BRAND", 1.0, (150, 160, 156)), 760, 600, dur=0.8)
    grow_x(img, t, tf + 0.4, bar6("ALDI EXCLUSIVE BRAND", 0.5, OKG), 760, 730, dur=0.9)
    show(img, t, tf + 1.0, bignum("l50", 330, 150, "UP TO 50%", "LESS", GOLD, vsize=46), 1700, 665, amp=3)
    show(img, t, T(b, "footnote"), pill9("* BASED ON PRICE COMPARISONS", 560, 54, fill=SAGE), 1140, 830, mode="up", amp=2)
    show(img, t, T(b, "That's Aldi's claim"), stamp9("ALDI'S CLAIM, NOT MINE", 520, 96, CORAL, 34), 560, 930, rot=-3, amp=3)
    tt = T(b, "test it yourself")
    show(img, t, tt, badge_ic(("mg6", 1), 120, lambda c, x, y, s: magnifier(c, x - 6, y - 6, 26, GOLD, 8)), 1150, 930, amp=4)
    show(img, t, tt + 0.3, pill9("COMPARE THE TWO ON THE SHELF", 620, 62, fill=GOLD), 1600, 930, mode="up", amp=2)

# ============================================================ 7
def coupon9(key, label, w=300, h=170, col=GOLD):
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 16, fill=col)
        for y in range(18, h - 12, 22):
            c.line([(w - 90, y), (w - 90, y + 11)], GREEN_D, 3)
        c.text((100, h / 2 - 14), "COUPON", FONT_SANS, 34, GREEN_D, track=3)
        s = 20
        while tw(label, s, 2) > w - 190 and s > 12:
            s -= 2
        c.text((100, h / 2 + 24), label, FONT_SANS_M, s, GREEN_D)
        c.text((w - 46, h / 2), "%", FONT_SANS, 52, GREEN_D)
    return mk(("cp9", key, w, h), w, h, fn, blur=10, dy=7)

def draw7(img, t):
    b = 7
    head9(img, t, 1, "NO COUPONS, NO REWARDS CARD")
    show(img, t, T(b, "other savings tools"), pill9("THE OTHER SAVINGS TOOLS DON'T WORK HERE", 920, 64, fill=IVORY), 960, 250, mode="down", amp=2)
    tm = T(b, "manufacturer coupons")
    show(img, t, tm, coupon9("m7", "MANUFACTURER", col=GOLD), 330, 450, amp=5)
    show(img, t, tm + 0.5, xb(96), 470, 390, amp=3)
    show(img, t, T(b, "negotiates the best price"), glass9("n7", 560, 140, I(ic_building, 0.55), "BEST PRICE ALREADY", "NEGOTIATED WITH SUPPLIERS", col=SAGE_D, tsize=28, ssize=26), 330, 640, mode="up", amp=3)
    tr = T(b, "rewards cards")
    show(img, t, tr, mk("rw7", 300, 180, lambda c: ic_paycard(c, 150, 90, 1.5, (120, 150, 90), "REWARDS")), 960, 450, amp=5, ph=1)
    show(img, t, tr + 0.5, xb(96), 1100, 380, amp=3)
    show(img, t, tr + 0.7, pill9("NO REWARDS CARDS", 340, 56, fill=CORAL, ink=IVORY), 960, 600, mode="up", amp=2)
    ta = T(b, "Aldi coupons are printed")
    show(img, t, ta, coupon9("a7", "ALDI", col=OKG), 1590, 430, amp=5, ph=2)
    show(img, t, ta + 0.3, glass9("p7", 560, 100, I(ic_building, 0.45), "PRINTED AND HANDED OUT IN STORES", None, col=OKG, tsize=22), 1590, 590, mode="up", amp=3)
    show(img, t, T(b, "mailed to you"), glass9("e7", 560, 100, I(ic_envelope, 0.6), "OR MAILED TO YOU", None, col=OKG, tsize=28), 1590, 710, mode="up", amp=3)
    to = T(b, "online or on social media")
    show(img, t, to, mk("soc7", 220, 240, lambda c: (ic_phone_app(c, 110, 120, 1.5), c.text((110, 98), "%", FONT_SANS, 70, GOLD))), 330, 850, amp=5)
    show(img, t, to + 0.3, glass9("o7", 560, 130, None, "COUPON FOUND ONLINE OR", "ON SOCIAL MEDIA", col=CORAL, tsize=26, ssize=28, scol=IVORY), 800, 850, mode="up", amp=3)
    show(img, t, T(b, "not a real Aldi coupon"), stamp9("NOT A REAL ALDI COUPON", 560, 100, CORAL, 30), 1420, 850, rot=-3, amp=3)
    td = T(b, "don't print anything")
    show(img, t, td, pill9("DON'T PRINT ANYTHING", 430, 60, fill=GOLD), 1000, 975, mode="up", amp=2)
    show(img, t, T(b, "shelf price"), glass9("sh7", 560, 100, I(ic_pin8, 0.7), "LOOK AT THE SHELF PRICE", None, col=GOLD, tsize=30), 1590, 975, mode="up", amp=3)

# ============================================================ 8
def cartcoin(img, t, t0):
    pass

def draw8(img, t):
    b = 8
    head9(img, t, 2, "A QUARTER AND A BAG")
    tu = T(b, "unlock a cart")
    show(img, t, tu, mk("cart8", 400, 300, lambda c: ic_cart_big(c, 200, 150, 2.2)), 420, 520, mode="left", amp=5)
    tq = T(b, "insert a quarter")
    show(img, t, tq, mk("coin8", 200, 200, lambda c: ic_coin25(c, 100, 100, 1.5)), 520, 340, mode="down", amp=6, ph=1)
    show(img, t, tq + 0.4, pill9("A 25 CENT DEPOSIT", 400, 60, fill=GOLD), 420, 760, mode="up", amp=3)
    tg = T(b, "get it back")
    show(img, t, tg, glass9("rt8", 760, 130, I(ic_repeat, 0.6), "RETURN THE CART TO THE CORRAL", "AND THE QUARTER COMES BACK", col=OKG, tsize=30, ssize=30), 520, 880, mode="up", amp=3)
    te = T(b, "extra staff")
    show(img, t, te, glass9("es8", 640, 140, lambda c, x, y: (ic_person(c, x, y + 4, 0.75, SAGE), ic_x(c, x + 26, y + 26, 0.5, CORAL, 14)), "NO EXTRA STAFF NEEDED", "TO COLLECT CARTS", col=SAGE_D, tsize=28, ssize=28), 1400, 290, mode="right", amp=3)
    tb = T(b, "bags")
    show(img, t, tb, pill9("THEN THERE ARE BAGS", 460, 62, fill=IVORY), 1400, 440, mode="down", amp=2)
    ty = T(b, "bring your own")
    show(img, t, ty, mini_icon_card("tote8", 340, 330, I(ic_tote, 1.0), "BRING YOUR OWN", "SHOPPING BAGS"), 1180, 640, mode="up", amp=6)
    tr = T(b, "reusable Aldi bag")
    show(img, t, tr, mini_icon_card("pbag8", 340, 330, I(ic_paperbag, 1.2), "OR BUY A", "REUSABLE ALDI BAG"), 1570, 640, mode="up", amp=6, ph=1)
    tk = T(b, "a few quarters")
    show(img, t, tk, glass9("kq8", 460, 110, None, "KEEP A FEW QUARTERS...", None, col=GOLD, tsize=26), 1130, 960, mode="up", amp=3)
    show(img, t, T(b, "by the door"), glass9("bd8", 460, 110, None, "...BAGS BY THE DOOR", None, col=GOLD, tsize=26), 1620, 960, mode="up", amp=3)

# ============================================================ 9
def conveyor9():
    def fn(c):
        w, h = 1100, 120
        c.rrect((0, 30, w, 100), 30, fill=(48, 58, 62))
        for k in range(0, w, 60):
            c.line([(k + 10, 40), (k + 40, 90)], (74, 86, 69), 6)
        c.rrect((0, 24, w, 40), 10, fill=(96, 108, 86))
    return mk("conv9", 1100, 120, fn, blur=10, dy=8)

def groceryitem(k):
    def fn(c):
        col = [CORAL, OKG, GOLD, SKY][k % 4]
        c.rrect((6, 6, 74, 84), 12, fill=col)
        c.rrect((6, 30, 74, 52), 1, fill=PAPER)
    return mk(("gi9", k), 80, 90, fn, blur=6, dy=4)

def draw9(img, t):
    b = 9
    head9(img, t, 2, "PACK YOUR OWN BAGS")
    tp = T(b, "pack their own groceries")
    show(img, t, tp - 0.1, conveyor9(), 620, 380, mode="left", amp=0, dur=0.6)
    if t >= tp:
        tm_ = min(t, END[0] - 0.95)
        fade = min(1.0, (t - tp) / 0.6)
        for k in range(8):
            x = 100 + ((tm_ - tp) * 90 + k * 130) % 1000
            put(img, groceryitem(k), x + 60, 322, alpha=fade)
    show(img, t, tp + 0.2, mini_icon_card("pk9", 300, 300, I(ic_tote, 1.0), "SHOPPERS PACK", "THEIR OWN GROCERIES"), 1500, 400, mode="right", amp=5)
    tl = T(b, "lines moving faster")
    show(img, t, tl, glass9("lm9", 640, 130, I(ic_clock2, 0.5), "KEEPS THE LINES", "MOVING FASTER", col=OKG, tsize=32, ssize=32), 470, 590, mode="left", amp=3)
    tm = T(b, "a minute or two")
    show(img, t, tm, mk("sw9", 200, 200, lambda c: ic_clock2(c, 100, 100, 1.5, 70)), 1050, 600, amp=5, ph=1)
    show(img, t, tm + 0.3, pill9("A MINUTE OR TWO", 380, 58, fill=GOLD), 1050, 740, mode="up", amp=2)
    to = T(b, "bags open and ready")
    show(img, t, to, glass9("bo9", 600, 130, I(ic_tote, 0.55), "BAGS OPEN AND READY", None, col=GOLD, tsize=32), 1560, 625, mode="right", amp=3)
    tq = T(b, "a quarter in your pocket")
    show(img, t, tq, glass9("qp9", 640, 130, None, "A QUARTER IN YOUR POCKET", "FOR THE NEXT CART", col=GOLD, tsize=30, ssize=28), 470, 790, mode="left", amp=3)
    th = T(b, "lifting heavy bags")
    show(img, t, th, glass9("hv9", 600, 120, I(ic_warn, 0.7), "HEAVY BAGS HARD TO LIFT?", None, col=CORAL, tsize=28), 1560, 790, mode="right", amp=3)
    t8 = T(b, "number eight")
    show(img, t, t8, arrow9(120, 60, GOLD, down=True), 1560, 880, mode="fade", amp=3)
    show(img, t, t8 + 0.2, glass9("n8b", 700, 110, I(ic_phone_app, 0.4), "NUMBER EIGHT: ORDERING ONLINE", None, col=GOLD, tsize=26), 1480, 985, mode="up", amp=3)
    show(img, t, T(b, "has a cost"), pill9("IT HAS A COST", 330, 56, fill=CORAL, ink=IVORY), 780, 985, mode="up", amp=2)

# ============================================================ 10
def closed_card(key, name, w=380, h=230, col=CORAL):
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 22, fill=PAPER)
        c.rrect((3, 3, w - 3, 66), 22, fill=col); c.d.rectangle(c._b((3, 46, w - 3, 66)), fill=col)
        for k in (0, 1):
            c.ell((22 + k * (w - 64), 22, 42 + k * (w - 64), 42), fill=PAPER)
        c.text((w / 2, 38), "CLOSED", FONT_SANS, 30, IVORY, track=6)
        s = 34
        while tw(name, s, 2) > w - 40 and s > 14:
            s -= 2
        c.text((w / 2, 140), name, FONT_SANS, s, INK, track=2)
    return mk(("cl10", key, w, h), w, h, fn)

def limited_card(key, name, w=330, h=190):
    def fn(c):
        vgrad(c, (3, 3, w - 3, h - 3), 22, (16, 68, 54), (8, 42, 34), outline=AMBER, width=4)
        c.ell((w - 84, 20, w - 24, 80), fill=IVORY)
        c.d.pieslice(c._b((w - 84, 20, w - 24, 80)), -90, 90, fill=AMBER)
        c.text((w / 2 - 28, 56), "LIMITED", FONT_SANS_M, 22, AMBER, track=2)
        s = 30
        while tw(name, s, 2) > w - 36 and s > 12:
            s -= 2
        c.text((w / 2, 130), name, FONT_SANS, s, IVORY, track=1)
    return mk(("lm10", key, w, h), w, h, fn)

def draw10(img, t):
    b = 10
    head9(img, t, 3, "KNOW WHEN ALDI IS CLOSED")
    tc = T(b, "closed on")
    names = [("New Year's Day", "NEW YEAR'S DAY"), ("Easter Sunday", "EASTER SUNDAY"), ("Thanksgiving Day", "THANKSGIVING DAY"), ("Christmas Day", "CHRISTMAS DAY")]
    for i, (k, nm) in enumerate(names):
        show(img, t, T(b, k), closed_card(("c", i), nm), 270 + i * 460, 330, mode="down", amp=6, ph=i)
    tl = T(b, "limited hours")
    show(img, t, tl - 0.1, pill9("LIMITED HOURS", 340, 56, fill=AMBER), 960, 500, mode="fade", amp=2)
    lim = [("Memorial Day", "MEMORIAL DAY"), ("Independence Day", "INDEPENDENCE DAY"), ("Labor Day", "LABOR DAY"), ("Christmas Eve", "CHRISTMAS EVE"), ("New Year's Eve", "NEW YEAR'S EVE")]
    for i, (k, nm) in enumerate(lim):
        show(img, t, T(b, k), limited_card(("l", i), nm), 220 + i * 370, 650, mode="up", amp=6, ph=i + 1)
    ts = T(b, "store locator")
    show(img, t, ts, glass9("sl10", 1020, 130, I(ic_pin8, 1.0), "ALDI'S STORE LOCATOR", "HOURS · SERVICES · PAYMENT OPTIONS · WEEKLY AD", col=GOLD, tsize=34, ssize=26), 600, 880, mode="up", amp=3)
    tw_ = T(b, "wasted trip")
    show(img, t, tw_, glass9("wt10", 700, 130, I(ic_car, 0.8), "A WASTED TRIP COSTS", "GAS AND TIME", col=CORAL, tsize=32, ssize=34, scol=IVORY), 1470, 880, mode="right", amp=3)

DRAW_A = {i: globals()["draw%d" % i] for i in range(1, 11)}
