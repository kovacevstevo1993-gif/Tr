"""Video lungo 9 (ALDI) - blocchi 11-20."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long9_kit import *
from long9_b01_10 import I, S, mini_icon_card, closed_card

def ic_plant(c, cx, cy, s):
    c.poly([(cx - 34 * s, cy + 6 * s), (cx + 34 * s, cy + 6 * s), (cx + 24 * s, cy + 52 * s), (cx - 24 * s, cy + 52 * s)], fill=(190, 110, 70))
    c.line([(cx, cy + 6 * s), (cx, cy - 36 * s)], OKG, 6 * s)
    c.ell((cx - 40 * s, cy - 40 * s, cx - 2 * s, cy - 8 * s), fill=OKG); c.ell((cx + 2 * s, cy - 58 * s, cx + 40 * s, cy - 22 * s), fill=(90, 180, 110))

def ic_paw(c, cx, cy, s, col=GOLD):
    c.ell((cx - 28 * s, cy - 2 * s, cx + 28 * s, cy + 44 * s), fill=col)
    for dx, dy in ((-40, -14), (-14, -38), (14, -38), (40, -14)):
        c.ell((cx + (dx - 12) * s, cy + (dy - 14) * s, cx + (dx + 12) * s, cy + (dy + 14) * s), fill=col)

def ic_steak(c, cx, cy, s):
    c.ell((cx - 60 * s, cy - 40 * s, cx + 60 * s, cy + 40 * s), fill=(190, 70, 64))
    c.ell((cx - 44 * s, cy - 28 * s, cx + 44 * s, cy + 28 * s), fill=(214, 108, 96))
    c.ell((cx + 6 * s, cy - 8 * s, cx + 28 * s, cy + 14 * s), fill=PAPER)

def ic_trowel(c, cx, cy, s):
    c.line([(cx - 40 * s, cy + 44 * s), (cx - 6 * s, cy + 6 * s)], (130, 90, 60), 12 * s)
    c.poly([(cx - 10 * s, cy + 10 * s), (cx + 20 * s, cy - 50 * s), (cx + 50 * s, cy - 10 * s), (cx + 8 * s, cy + 24 * s)], fill=(176, 184, 190))

def ic_warn2(c, cx, cy, s):
    c.poly([(cx, cy - 56 * s), (cx + 58 * s, cy + 44 * s), (cx - 58 * s, cy + 44 * s)], fill=AMBER)
    c.text((cx, cy + 14 * s), "!", FONT_SANS, 64 * s, GREEN_D)

def draw11(img, t):
    b = 11
    head9(img, t, 3, "WHAT ALDI DOESN'T HAVE")
    tb = T(b, "banks and pharmacies")
    show(img, t, T(b, "two things Aldi doesn't have"), pill9("TWO THINGS ALDI DOESN'T HAVE", 640, 64, fill=IVORY), 960, 235, mode="down", amp=2)
    show(img, t, tb, mini_icon_card("bk11", 480, 270, lambda c, x, y: (ic_bank(c, x, y, 1.0), ic_x(c, x + 50, y + 34, 0.6, CORAL, 14)), "NO BANKS", "CORPORATE PAGE", accent=CORAL), 330, 410, mode="up", amp=5)
    show(img, t, tb + 0.3, mini_icon_card("ph11", 480, 270, lambda c, x, y: (ic_pharmacy(c, x, y, 0.95), ic_x(c, x + 50, y + 34, 0.6, CORAL, 14)), "NO PHARMACIES", "CORPORATE PAGE", accent=CORAL), 840, 410, mode="up", amp=5, ph=1)
    show(img, t, T(b, "no delis"), mini_icon_card("dl11", 480, 270, lambda c, x, y: (ic_cheese(c, x, y, 0.9), ic_x(c, x + 50, y + 34, 0.6, CORAL, 14)), "NO DELIS", "HELP CENTER", accent=CORAL), 1350, 410, mode="up", amp=5, ph=2)
    show(img, t, T(b, "fresh meats and cheeses"), glass9("mc11", 700, 130, I(ic_cheese, 0.55), "BUT FRESH MEATS AND CHEESES", "IN THE DELI PRODUCTS SECTION", col=OKG, tsize=26, ssize=26), 1560, 640, mode="right", amp=3)
    show(img, t, T(b, "prescription medicine"), glass9("rx11", 760, 140, I(ic_bottle, 0.6), "PRESCRIPTION MEDICINE?", "YOU'LL STILL NEED YOUR OWN PHARMACY", col=GOLD, tsize=34, ssize=26), 450, 640, mode="left", amp=3)
    t1 = T(b, "one stop")
    def route(c):
        c.line([(110, 100), (360, 100), (610, 100), (860, 100)], (150, 215, 185), 6)
        for x, lab, ic in ((110, "HOME", lambda cc, x_, y_: ic_house(cc, x_, y_, 0.7)), (360, "ALDI", lambda cc, x_, y_: ic_storefront(cc, x_, y_, 0.9)), (610, "PHARMACY", lambda cc, x_, y_: ic_pharmacy(cc, x_, y_, 0.6)), (860, "HOME", lambda cc, x_, y_: ic_house(cc, x_, y_, 0.7))):
            c.ell((x - 52, 48, x + 52, 152), fill=(14, 62, 54), outline=GOLD, width=4)
            ic(c, x, 100)
            c.text((x, 182), lab, FONT_SANS, 24, IVORY, track=3)
    show(img, t, t1, mk("route11", 970, 220, route), 560, 860, mode="up", amp=4)
    show(img, t, t1 + 0.4, pill9("ALDI IS ONE STOP, NOT THE ONLY STOP", 700, 62, fill=GOLD), 1500, 860, mode="right", amp=3)
    show(img, t, T(b, "fresh produce is delivered daily"), glass9("fp11", 700, 110, I(ic_truck2, 0.55), "FRESH PRODUCE IS DELIVERED DAILY", None, col=SAGE_D, tsize=28), 1500, 975, mode="right", amp=3)

def draw12(img, t):
    b = 12
    head9(img, t, 4, "ALDI FINDS")
    show(img, t, T(b, "Aldi Finds"), bignum("af12", 360, 170, "ALDI FINDS", "NEW EVERY WEEK", GOLD, vsize=44), 1600, 300, amp=4)
    items = [("unique foods", "FOODS", lambda c, x, y: ic_apple(c, x, y, 1.2)), ("home goods", "HOME GOODS", lambda c, x, y: ic_house(c, x, y, 1.0)),
             ("gardening essentials", "GARDENING", lambda c, x, y: ic_plant(c, x, y, 1.2)), ("pet accessories", "PET ACCESSORIES", lambda c, x, y: ic_paw(c, x, y, 1.3))]
    for i, (k, lab, ic) in enumerate(items):
        show(img, t, T(b, k), mini_icon_card(("f12", i), 300, 300, ic, lab, "A FIND", accent=SAGE_D), 230 + i * 330, 340, mode="up", amp=6, ph=i)
    tl = T(b, "limited time")
    show(img, t, tl, glass9("lt12", 540, 120, I(ic_clock2, 0.4), "LIMITED TIME", "WHILE SUPPLIES LAST", col=AMBER, tsize=34, ssize=28), 1600, 520, mode="right", amp=3)
    show(img, t, T(b, "every week"), glass9("ew12", 520, 110, I(ic_repeat, 0.5), "THEY CHANGE EVERY WEEK", None, col=GOLD, tsize=28), 400, 590, mode="left", amp=3)
    ts = T(b, "stock varies by store")
    def stores(c):
        for k, f_ in enumerate((0.9, 0.3, 0.6)):
            x = 90 + k * 170
            ic_storefront(c, x, 70, 0.95)
            c.rrect((x - 56, 140, x + 56, 160), 8, fill=(30, 76, 66)); c.rrect((x - 56, 140, x - 56 + 112 * f_, 160), 8, fill=OKG)
        c.text((260, 196), "STOCK VARIES BY STORE", FONT_SANS, 24, IVORY, track=3)
    show(img, t, ts, mk("stk12", 520, 230, stores), 1040, 620, amp=5)
    show(img, t, T(b, "place holds"), stamp9("NO HOLDS", 280, 90, CORAL), 1480, 680, rot=-3, amp=3)
    show(img, t, T(b, "rain checks"), stamp9("NO RAIN CHECKS", 340, 90, CORAL), 1750, 780, rot=3, amp=3)
    tw_ = T(b, "Wednesdays")
    show(img, t, tw_, mk("wd12", 640, 190, lambda c: (vgrad(c, (3, 3, 637, 187), 24, (16, 68, 60), (8, 42, 36), outline=GOLD, width=4), ic_weekstrip(c, 320, 76, 1.9, 2), c.text((320, 160), "MOST STORES START NEW FINDS ON WEDNESDAYS", FONT_SANS, 20, IVORY, track=2))), 400, 860, mode="up", amp=4)
    show(img, t, T(b, "a week early"), glass9("we12", 640, 130, I(ic_web, 0.55), "POSTED ON ALDI'S WEBSITE", "A WEEK EARLY", col=SKY, tsize=30, ssize=30), 1100, 860, mode="up", amp=3)
    show(img, t, T(b, "as soon as possible"), glass9("go12", 560, 130, I(ic_clock2, 0.45), "WANT ONE? GO", "AS SOON AS POSSIBLE", col=OKG, tsize=30, ssize=30), 1640, 930, mode="up", amp=3)

def draw13(img, t):
    b = 13
    head9(img, t, 4, "WHAT FINDS ARE FOR")
    show(img, t, T(b, "test new products"), mini_icon_card("ts13", 330, 280, I(ic_flask, 1.2), "TEST NEW", "PRODUCTS"), 260, 340, mode="left", amp=5)
    show(img, t, T(b, "sells well"), arrow9(110, 52, GOLD), 520, 340, mode="fade", amp=2)
    show(img, t, T(b, "sells well"), mini_icon_card("sw13", 300, 280, I(ic_cart_big, 0.9), "SELLS WELL", None), 760, 340, mode="up", amp=5, ph=1)
    show(img, t, T(b, "come back during the year"), glass9("cb13", 760, 130, I(ic_repeat, 0.55), "COMES BACK DURING THE YEAR", None, col=OKG, tsize=30), 1440, 270, mode="right", amp=3)
    show(img, t, T(b, "everyday selection"), glass9("es13", 760, 130, I(ic_storefront, 0.6), "OR JOINS THE EVERYDAY SELECTION", None, col=OKG, tsize=28), 1440, 430, mode="right", amp=3)
    tw_ = T(b, "warning")
    show(img, t, tw_, mk("wr13", 150, 150, lambda c: ic_warn2(c, 75, 78, 1.1)), 140, 640, amp=4)
    show(img, t, T(b, "non food Finds"), glass9("nf13", 880, 130, I(ic_shield, 0.5, col=SAGE), "THE GUARANTEE LEAVES", "NON FOOD FINDS OUT", col=CORAL, tsize=34, ssize=34, scol=IVORY), 700, 640, mode="left", amp=3)
    tg = T(b, "gadget or a gardening tool")
    show(img, t, tg, mini_icon_card("gd13", 280, 250, lambda c, x, y: (ic_bolt(c, x, y, 1.6), ic_x(c, x + 50, y + 34, 0.55, CORAL, 14)), "A GADGET", None, accent=CORAL), 1330, 640, mode="up", amp=5)
    show(img, t, tg + 0.3, mini_icon_card("tl13", 280, 250, lambda c, x, y: (ic_trowel(c, x, y, 1.1), ic_x(c, x + 50, y + 34, 0.55, CORAL, 14)), "A GARDEN TOOL", None, accent=CORAL), 1650, 640, mode="up", amp=5, ph=1)
    show(img, t, T(b, "stuck with it"), pill9("YOU MAY BE STUCK WITH IT", 520, 62, fill=CORAL, ink=IVORY), 1490, 810, mode="up", amp=2)
    show(img, t, T(b, "impulse"), stamp9("THINK TWICE", 360, 100, GOLD), 330, 900, rot=-3, amp=3)
    show(img, t, T(b, "at the register"), say9("rg13", 900, 120, ["\"WOULD I STILL WANT IT AT THE REGISTER?\""], 30, tail="bl"), 1150, 920, mode="up", amp=3)

def flyer9():
    def fn(c):
        w, h = 420, 560
        c.rrect((3, 3, w - 3, h - 3), 14, fill=PAPER)
        c.rrect((3, 3, w - 3, 90), 14, fill=GOLD); c.d.rectangle(c._b((3, 60, w - 3, 90)), fill=GOLD)
        c.text((w / 2, 48), "WEEKLY AD", FONT_SANS, 44, GREEN_D, track=4)
        cols = [CORAL, OKG, SKY, AMBER, (176, 124, 200), (90, 180, 170)]
        for i in range(6):
            x = 30 + (i % 2) * 190; y = 112 + (i // 2) * 146
            c.rrect((x, y, x + 170, y + 126), 12, fill=(238, 234, 222))
            c.ell((x + 50, y + 18, x + 120, y + 88), fill=cols[i])
            c.rrect((x + 30, y + 98, x + 140, y + 110), 5, fill=(190, 186, 174))
    return mk("fly14", 420, 560, fn, blur=16, dy=12)

def draw14(img, t):
    b = 14
    head9(img, t, 5, "THE WEEKLY AD AND THE WEDNESDAY EMAIL")
    show(img, t, T(b, "weekly ad and the Wednesday"), flyer9(), 330, 610, mode="up", amp=5, rot=-3)
    te = T(b, "Wednesday email")
    show(img, t, te, mk("em14", 280, 220, lambda c: (ic_envelope(c, 140, 100, 2.0), c.rrect((40, 160, 240, 206), 16, fill=GOLD), c.text((140, 184), "WEDNESDAY", FONT_SANS, 26, GREEN_D, track=2))), 700, 420, mode="up", amp=6, ph=1)
    show(img, t, T(b, "Aldi has no coupons"), glass9("nc14", 760, 130, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "NO COUPONS, NO REWARDS CARD", None, col=CORAL, tsize=30), 1380, 330, mode="right", amp=3)
    show(img, t, T(b, "Weekly Specials"), arrow9(110, 120, GOLD, down=True), 1380, 440, mode="fade", amp=2)
    show(img, t, T(b, "Weekly Specials") + 0.2, glass9("ws14", 760, 130, I(ic_megaphone, 0.55), "...SO SEE THE WEEKLY SPECIALS", "TO SAVE MORE", col=OKG, tsize=30, ssize=28), 1380, 560, mode="right", amp=3)
    show(img, t, T(b, "goes out on a Wednesday"), mk("cal14", 520, 150, lambda c: (vgrad(c, (3, 3, 517, 147), 22, (16, 68, 60), (8, 42, 36), outline=GOLD, width=4), ic_weekstrip(c, 260, 60, 1.35, 2), c.text((260, 124), "EVERY WEEK: WEDNESDAY", FONT_SANS, 22, IVORY, track=2))), 900, 620, mode="up", amp=4)
    tw_ = T(b, "Aldi's website")
    show(img, t, tw_, glass9("wb14", 560, 120, I(ic_web, 0.5), "ALDI'S WEBSITE", None, col=SKY, tsize=32), 1240, 740, mode="up", amp=3)
    show(img, t, T(b, "store locator"), glass9("sl14", 560, 120, I(ic_pin8, 1.0), "YOUR STORE'S PAGE", "IN THE STORE LOCATOR", col=SKY, tsize=30, ssize=26), 1720, 740, mode="up", amp=3)
    tf = T(b, "Fresh Meat Specials")
    show(img, t, tf, mini_icon_card("fm14", 360, 250, I(ic_steak, 1.1), "FRESH MEAT", "SPECIALS", accent=CORAL), 1000, 900, mode="up", amp=5)
    show(img, t, T(b, "limited time, and while"), pill9("LIMITED TIME, WHILE SUPPLIES LAST", 700, 62, fill=AMBER), 1560, 920, mode="right", amp=3)

def draw15(img, t):
    b = 15
    head9(img, t, 5, "USE IT: A SHORT LIST")
    show(img, t, T(b, "open the ad"), mk("fl15", 320, 430, lambda c: (c.rrect((3, 3, 317, 427), 12, fill=PAPER), c.rrect((3, 3, 317, 70), 12, fill=GOLD), c.d.rectangle(c._b((3, 50, 317, 70)), fill=GOLD), c.text((160, 38), "WEEKLY AD", FONT_SANS, 34, GREEN_D, track=3),
        *[c.ell((30 + (i % 2) * 140, 92 + (i // 2) * 110, 130 + (i % 2) * 140 - 20, 182 + (i // 2) * 110 - 20), fill=[CORAL, OKG, SKY, AMBER][i]) for i in range(4)])), 280, 520, mode="left", amp=5, rot=-3)
    tl = T(b, "short list on paper")
    show(img, t, tl - 0.1, arrow9(120, 56, GOLD), 530, 520, mode="fade", amp=2)
    show(img, t, tl, mk("ls15", 400, 520, lambda c: (c.rrect((3, 3, 397, 517), 12, fill=PAPER), c.rrect((3, 3, 397, 70), 12, fill=OKG), c.d.rectangle(c._b((3, 50, 397, 70)), fill=OKG), c.text((200, 38), "MY LIST", FONT_SANS, 36, GREEN_D, track=4),
        *[c.rrect((60, 110 + i * 78, 340 - (i % 3) * 40, 124 + i * 78), 7, fill=(190, 186, 174)) for i in range(5)])), 800, 520, mode="up", amp=5, rot=2)
    for i in range(5):
        tk_ = tl + 0.5 + i * 0.5
        if t >= tk_:
            p = ease(seg(t, tk_, 0.3))
            put(img, mk(("tk15", i), 60, 60, lambda c: (c.ell((3, 3, 57, 57), outline=OKG, width=5), check_ic(c, 30, 31, 0.4, OKG)), shadow=False), 618, 330 + i * 78 + 24, scale=p, alpha=p)
    show(img, t, T(b, "Finds you really want"), pill9("+ THE FINDS YOU REALLY WANT", 540, 62, fill=GOLD), 800, 860, mode="up", amp=2)
    tx = T(b, "wandering the aisles")
    def zig(c):
        pts = [(40, 40), (240, 70), (90, 130), (280, 170), (60, 210), (260, 240)]
        c.line(pts, CORAL, 8)
        c.text((150, 285), "WANDERING THE AISLES", FONT_SANS, 20, IVORY, track=2)
    show(img, t, tx, mk("zz15", 320, 310, zig, shadow=False), 1310, 420, mode="right", amp=3)
    show(img, t, T(b, "grabbing extras"), xb(86), 1470, 330, amp=3)
    show(img, t, T(b, "not an Aldi rule"), stamp9("NOT AN ALDI RULE", 400, 90, GOLD), 1640, 520, rot=-3, amp=3)
    show(img, t, T(b, "just a habit"), stamp9("JUST A HABIT", 340, 90, OKG), 1640, 640, rot=3, amp=3)
    ts = T(b, "smart, fast and easy")
    for i, (lab, ic) in enumerate((("SMART", I(ic_pin8, 0.9)), ("FAST", I(ic_bolt, 1.0)), ("EASY", lambda c, x, y: check_ic(c, x, y, 0.7, OKG)))):
        show(img, t, ts + i * 0.25, mini_icon_card(("se15", i), 250, 190, ic, lab, None, accent=GOLD), 1180 + i * 280, 830, mode="up", amp=5, ph=i)
    show(img, t, T(b, "a list helps"), pill9("A LIST HELPS WITH ALL THREE", 600, 62, fill=IVORY), 1320, 975, mode="up", amp=2)

def paytile(label, col, ink=IVORY, sub=None):
    def fn(c):
        w, h = 320, 150
        vgrad(c, (3, 3, w - 3, h - 3), 20, tuple(min(255, v + 25) for v in col), col, outline=IVORY, width=3)
        c.rrect((3, 28, w - 3, 52), 1, fill=(20, 26, 30))
        s = 34
        while tw(label, s, 2) > w - 40 and s > 14:
            s -= 2
        c.text((w / 2, 100), label, FONT_SANS, s, ink, track=2)
        if sub:
            c.text((w / 2, 132), sub, FONT_SANS_M, 18, ink, track=1)
    return mk(("pt16", label), 320, 150, fn, blur=10, dy=7)

def draw16(img, t):
    b = 16
    head9(img, t, 6, "HOW YOU PAY")
    tiles = [("cash", "CASH", (40, 130, 84)), ("debit cards", "DEBIT", (60, 90, 150)), ("Visa", "VISA", (30, 60, 140)), ("Mastercard", "MASTERCARD", (190, 70, 50)), ("Discover", "DISCOVER", (220, 120, 40)),
             ("American Express", "AMEX", (40, 120, 170)), ("E B T", "E B T", (80, 100, 120)), ("snap", "SNAP", (60, 140, 90)), ("Link cards", "LINK", (100, 80, 150)), ("tap payments", "TAP TO PAY", (50, 56, 62))]
    for i, (k, lab, col) in enumerate(tiles):
        x = 230 + (i % 5) * 365; y = 330 + (i // 5) * 190
        sub = "APPLE PAY, GOOGLE PAY" if lab == "TAP TO PAY" else None
        show(img, t, T(b, k), paytile(lab, col, sub=sub), x, y, mode="pop", amp=4, ph=i * 0.7)
    tcb = T(b, "cash back of ten")
    show(img, t, tcb, pill9("CASH BACK WITH QUALIFYING CARDS", 600, 60, fill=GOLD), 400, 640, mode="left", amp=2)
    for i, v in enumerate(("$10", "$20", "$40", "$100")):
        show(img, t, tcb + 0.25 + i * 0.22, badge_ic(("cb16", v), 120, lambda c, x, y, s, v=v: c.text((x, y + 2), v, FONT_SANS, 34 if len(v) < 4 else 28, GOLD), GOLD), 900 + i * 150, 640, amp=4, ph=i)
    tc = T(b, "checks")
    show(img, t, tc, glass9("ck16", 560, 120, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "NO CHECKS", "AT THIS TIME", col=CORAL, tsize=34, ssize=26), 520, 820, mode="up", amp=3)
    show(img, t, T(b, "W I C"), glass9("wi16", 560, 120, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "NO W I C", "AT THIS TIME", col=CORAL, tsize=34, ssize=26), 1130, 820, mode="up", amp=3)
    show(img, t, T(b, "bring a card or some cash"), glass9("bc16", 760, 120, I(ic_paycard, 0.5, col=(60, 90, 150)), "BRING A CARD OR SOME CASH", None, col=GOLD, tsize=30), 1300, 975, mode="up", amp=3)

def draw17(img, t):
    b = 17
    head9(img, t, 6, "SNAP AT ALDI")
    show(img, t, T(b, "snap benefits"), mk("ebt17", 420, 270, lambda c: (ic_paycard(c, 210, 135, 2.9, (50, 140, 96), "E B T"), c.text((210, 118), "SNAP", FONT_SANS, 54, IVORY, track=3))), 330, 400, mode="left", amp=5, rot=-3)
    show(img, t, T(b, "all Aldi stores accept"), glass9("is17", 640, 130, I(ic_storefront, 0.6), "IN THE STORE: ALL ALDI STORES", None, col=OKG, tsize=30), 1130, 330, mode="right", amp=3)
    show(img, t, T(b, "all Aldi stores accept") + 0.2, okb(80), 1560, 330, amp=3)
    show(img, t, T(b, "online they work"), glass9("on17", 760, 130, I(ic_phone_app, 0.5), "ONLINE: PARTICIPATING PICKUP", "AND DELIVERY LOCATIONS", col=OKG, tsize=28, ssize=28), 1290, 490, mode="right", amp=3)
    show(img, t, T(b, "eligible food"), glass9("ef17", 640, 120, I(ic_apple, 0.6), "SNAP PAYS FOR ELIGIBLE FOOD", None, col=GOLD, tsize=28), 350, 640, mode="left", amp=3)
    tt = T(b, "tips or fees")
    show(img, t, tt, glass9("tf17", 640, 130, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "ONLINE: NOT FOR TIPS OR FEES", None, col=CORAL, tsize=28), 1130, 650, mode="right", amp=3)
    show(img, t, T(b, "debit or credit card"), glass9("dc17", 640, 130, I(ic_paycard, 0.5, col=(60, 90, 150)), "USE A DEBIT OR CREDIT CARD", "FOR THOSE", col=SKY, tsize=28, ssize=26), 1130, 800, mode="right", amp=3)
    tb = T(b, "blue badge")
    show(img, t, tb, mk("bb17", 330, 280, lambda c: (vgrad(c, (3, 3, 327, 277), 22, (240, 238, 228), (222, 218, 204), outline=(190, 186, 174), width=3), c.ell((100, 30, 230, 160), fill=(214, 108, 96)), c.rrect((100, 176, 230, 188), 6, fill=(190, 186, 174)), c.rrect((10, 10, 150, 46), 12, fill=(30, 110, 200)), c.text((80, 28), "SNAP", FONT_SANS, 22, IVORY, track=2), c.rrect((90, 214, 240, 232), 8, fill=(206, 202, 190)))), 350, 880, mode="up", amp=5, rot=-2)
    show(img, t, tb + 0.3, glass9("bd17", 520, 110, None, "ELIGIBLE PRODUCTS ON THE", "WEBSITE: A BLUE BADGE", col=SKY, tsize=24, ssize=24), 770, 880, mode="left", amp=3)
    tu = T(b, "U S D A")
    show(img, t, tu, glass9("us17", 800, 120, I(ic_seal, 0.8), "OFFICIAL LIST OF SNAP ELIGIBLE FOODS", "fns.usda.gov", col=GOLD, tsize=26, ssize=30), 1460, 985, mode="right", amp=3)

def draw18(img, t):
    b = 18
    head9(img, t, 7, "ALDI GIFT CARDS")
    ts = T(b, "five dollar steps")
    for i, (v, col) in enumerate((("$5", (70, 140, 200)), ("$10", (60, 160, 120)), ("$25", (210, 120, 60)), ("$50", (150, 90, 190)), ("$100", (200, 70, 80)))):
        show(img, t, ts + i * 0.2, mk(("gc18", v), 240, 160, lambda c, v=v, col=col: (ic_paycard(c, 120, 80, 1.8, col), c.text((120, 100), v, FONT_SANS, 44, IVORY))), 280 + i * 250, 360, amp=6, ph=i, rot=-6 + i * 3)
    show(img, t, T(b, "only in its stores"), glass9("os18", 520, 120, I(ic_storefront, 0.55), "ONLY IN ITS STORES", None, col=GOLD, tsize=32), 1560, 330, mode="right", amp=3)
    show(img, t, T(b, "no fees"), glass9("nf18", 520, 120, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "NO FEES", None, col=OKG, tsize=34), 1560, 480, mode="right", amp=3)
    show(img, t, T(b, "does not expire"), glass9("ne18", 600, 130, lambda c, x, y: (ic_calendar(c, x, y, 0.5), ic_x(c, x + 22, y + 22, 0.45, CORAL, 14)), "THE BALANCE DOES NOT EXPIRE", None, col=OKG, tsize=28), 400, 620, mode="left", amp=3)
    show(img, t, T(b, "part of the balance"), glass9("pb18", 640, 130, I(ic_gift2, 0.5), "USE PART OF THE BALANCE", None, col=SAGE_D, tsize=30), 1130, 620, mode="up", amp=3)
    show(img, t, T(b, "bottom of your receipt"), receipt9("rb18", 380, 340, [("YOUR ITEMS", ""), ("TOTAL", ""), ("GIFT CARD BALANCE", "")], hl=2, hlcol=GOLD), 1650, 700, mode="up", amp=4, rot=2)
    show(img, t, T(b, "online orders"), glass9("oo18", 640, 120, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "NOT FOR ONLINE ORDERS", None, col=CORAL, tsize=30), 400, 790, mode="left", amp=3)
    show(img, t, T(b, "lost or stolen"), glass9("ls18", 640, 130, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "LOST OR STOLEN CARD:", "NOT REPLACED", col=CORAL, tsize=28, ssize=34, scol=IVORY), 1130, 800, mode="up", amp=3)
    show(img, t, T(b, "like cash"), pill9("TREAT IT LIKE CASH", 440, 62, fill=GOLD), 760, 975, mode="up", amp=2)

def draw19(img, t):
    b = 19
    head9(img, t, 8, "ORDERING ONLINE: THE REAL COST")
    scr = lambda c, x0, y0, x1, y1: (c.rrect((x0 + 14, y0 + 6, x1 - 14, y0 + 56), 10, fill=GREEN_D), c.text(((x0 + x1) / 2, y0 + 31), "ALDI", FONT_SANS, 28, GOLD, track=4),
        *[(c.rrect((x0 + 14, y0 + 76 + i * 76, x1 - 14, y0 + 138 + i * 76), 10, fill=(226, 232, 226)), c.ell((x0 + 24, y0 + 84 + i * 76, x0 + 70, y0 + 130 + i * 76), fill=[CORAL, OKG, GOLD][i])) for i in range(3)],
        c.rrect((x0 + 14, y1 - 90, x1 - 14, y1 - 30), 14, fill=OKG), c.text(((x0 + x1) / 2, y1 - 60), "CHECKOUT", FONT_SANS, 24, GREEN_D, track=2))
    show(img, t, T(b, "Instacart"), phone9("o19", 300, 580, scr), 290, 590, mode="left", amp=5, rot=-3)
    show(img, t, T(b, "Instacart") + 0.3, pill9("RUNS THROUGH INSTACART", 460, 60, fill=IVORY), 290, 960, mode="up", amp=2)
    tm = T(b, "at least ten dollars")
    show(img, t, tm, bignum("min19", 360, 170, "$10", "MINIMUM ORDER", GOLD, vsize=82), 760, 330, amp=4)
    show(img, t, T(b, "one dollar and ninety nine"), bignum("pk19", 420, 170, "FROM $1.99", "PICKUP FEES", GOLD, vsize=60), 1190, 330, amp=4, ph=1)
    show(img, t, T(b, "delivery window"), glass9("dw19", 860, 140, I(ic_truck2, 0.55), "DELIVERY FEES DEPEND ON THE", "DELIVERY WINDOW AND THE ORDER TOTAL", col=SKY, tsize=28, ssize=28), 1440, 520, mode="right", amp=3)
    show(img, t, T(b, "Aldi account"), glass9("ac19", 600, 130, I(ic_person, 0.7), "AN ALDI ACCOUNT IS REQUIRED", None, col=GOLD, tsize=28), 1130, 700, mode="right", amp=3)
    show(img, t, T(b, "no guest ordering"), stamp9("NO GUEST ORDERING", 440, 92, CORAL, 28), 1650, 700, rot=-3, amp=3)
    show(img, t, T(b, "no fee"), pill9("ACCOUNT ITSELF: NO FEE", 440, 60, fill=OKG), 700, 700, mode="up", amp=2)
    show(img, t, T(b, "Bags are charged"), glass9("bg19", 620, 120, I(ic_tote, 0.55), "BAGS ARE CHARGED TOO", "A SMALL FEE, LIKE IN THE STORE", col=SAGE_D, tsize=28, ssize=24), 1050, 880, mode="up", amp=3)
    show(img, t, T(b, "tips aren't accepted"), glass9("tp19", 700, 120, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "CURBSIDE ORDERS: NO TIPS", None, col=CORAL, tsize=28), 1580, 900, mode="right", amp=3)

def draw20(img, t):
    b = 20
    head9(img, t, 8, "ONLINE PRICES ARE NOT THE SAME")
    tp = T(b, "prices online may vary")
    show(img, t, tp, mini_icon_card("is20", 380, 300, I(ic_storefront, 1.3), "IN THE STORE", None, accent=SAGE_D), 360, 380, mode="left", amp=5)
    show(img, t, tp + 0.3, mini_icon_card("on20", 380, 300, I(ic_phone_app, 1.0), "ONLINE", "MAY VARY SLIGHTLY", accent=SKY), 840, 380, mode="up", amp=5, ph=1)
    show(img, t, tp + 0.5, arrow9(110, 50, GOLD), 600, 380, mode="fade", amp=2)
    show(img, t, T(b, "promotions in the store"), glass9("pr20", 800, 130, lambda c, x, y: ic_x(c, x, y, 0.7, CORAL, 14), "SOME PROMOTIONS IN THE STORE", "MAY NOT APPLY ONLINE", col=CORAL, tsize=28, ssize=28, scol=IVORY), 1460, 330, mode="right", amp=3)
    show(img, t, T(b, "priced higher"), glass9("ph20", 800, 130, I(ic_cart_big, 0.5), "ONLINE ITEMS MAY BE PRICED HIGHER", "TO COVER SHOPPING OR DELIVERY", col=AMBER, tsize=26, ssize=26), 1460, 490, mode="right", amp=3)
    show(img, t, T(b, "not the same basket"), stamp9("NOT THE SAME BASKET", 520, 100, GOLD, 34), 600, 640, rot=-3, amp=3)
    show(img, t, T(b, "carrying groceries is hard"), glass9("ch20", 640, 130, I(ic_tote, 0.55, col=CORAL), "CARRYING GROCERIES IS HARD?", None, col=OKG, tsize=28), 1200, 650, mode="up", amp=3)
    show(img, t, T(b, "weather is bad"), glass9("wb20", 560, 130, I(ic_rain, 0.6), "BAD WEATHER?", None, col=OKG, tsize=30), 1710, 650, mode="up", amp=3)
    show(img, t, T(b, "extra cost"), pill9("CHOOSE IT KNOWING THE EXTRA COST", 680, 62, fill=GOLD), 560, 790, mode="up", amp=2)
    tl = T(b, "total before you pay")
    show(img, t, tl, mk("tot20", 760, 190, lambda c: (vgrad(c, (3, 3, 757, 187), 24, (240, 238, 228), (222, 218, 204), outline=GOLD, width=6), c.text((60, 60), "ORDER TOTAL", FONT_SANS, 34, INK, anchor="lm", track=3), c.rrect((460, 38, 720, 82), 10, fill=GOLD), c.text((590, 60), "LOOK HERE", FONT_SANS, 26, GREEN_D, track=2), c.rrect((60, 112, 480, 130), 8, fill=(190, 186, 174)), c.rrect((60, 146, 360, 160), 8, fill=(200, 196, 184)))), 960, 930, mode="up", amp=3)
    show(img, t, tl + 0.4, pill9("BEFORE YOU PAY", 380, 60, fill=OKG), 1500, 930, mode="right", amp=2)

DRAW_B = {i: globals()["draw%d" % i] for i in range(11, 21)}
