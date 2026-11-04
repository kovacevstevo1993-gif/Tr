"""Video lungo 10 (BLACK FRIDAY) - blocchi 1-10. Voce: COPIONE-VIDEO-BLACK-FRIDAY.md. Durate: screenshot CapCut 04/11/2026."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bf10_kit import *

def S(img, t, b, key, spr, x, y, n=1, dt=0.0, **kw):
    return show(img, t, T(b, key, n) + dt, spr, x, y, **kw)

def I(fn, s=1.0, **kw):
    return lambda c, x, y: fn(c, x, y, s, **kw)

def calendar_spr(w=560, h=600, hi=None, marks=()):
    """pagina di calendario con anelli: numeri 1-30 (nessuna casella vuota)"""
    def fn(c):
        c.rrect((3, 28, w - 3, h - 3), 24, fill=PAPER, outline=(196, 190, 170), width=3)
        c.rrect((3, 28, w - 3, 118), 24, fill=GOLD)
        c.d.rectangle(c._b((3, 90, w - 3, 118)), fill=GOLD)
        for k in range(6):
            x = 70 + k * (w - 140) / 5
            c.rrect((x - 9, 6, x + 9, 56), 8, fill=(30, 40, 38), outline=(120, 130, 126), width=2)
        c.text((w / 2, 76), "RETURN DEADLINE", FONT_SANS, 40, GREEN_D, track=4)
        cw, ch = (w - 60) / 7, (h - 170) / 5
        for i in range(30):
            r, q = divmod(i, 7)
            x = 30 + q * cw + cw / 2; y = 150 + r * ch + ch / 2
            c.text((x, y), str(i + 1), FONT_SANS_M, 30, (70, 96, 84))
    return mk(("cal10", w, h), w, h, fn)

def cal_cell(i, w=560, h=600, x0=500, y0=600):
    cw, ch = (w - 60) / 7, (h - 170) / 5
    r, q = divmod(i, 7)
    return (x0 - w / 2 + 30 + q * cw + cw / 2, y0 - h / 2 + 150 + r * ch + ch / 2)

def ring_spr(S=84, col=GOLD):
    return mk(("ring10", S, col), S, S, lambda c: c.ell((5, 5, S - 5, S - 5), outline=col, width=8), blur=6, dy=3, alpha=0.4)

def qdisc(S=92):
    return mk(("qd10", S), S, S, lambda c: (c.ell((4, 4, S - 4, S - 4), fill=GOLD, outline=IVORY, width=4), c.text((S / 2, S / 2 + 3), "?", FONT_SANS, int(S * 0.62), GREEN_D)), blur=8, dy=5)

def plate(key, w, h, name, tabs=("RETURNS", "PRICE MATCHING")):
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 22, fill=PAPER, outline=(196, 190, 170), width=3)
        c.rrect((3, 3, 26, h - 3), 12, fill=GOLD); c.d.rectangle(c._b((16, 3, 26, h - 3)), fill=GOLD)
        c.text((52, 44), name, FONT_SANS, 40, GREEN_D, anchor="lm", track=3)
        ic_doc(c, w - 56, 44, 0.42)
        x = 52
        for tname in tabs:
            tw_ = tw(tname, 20, 2) + 30
            c.rrect((x, h - 56, x + tw_, h - 18), 16, fill=(214, 226, 218), outline=(150, 176, 160), width=2)
            c.text((x + tw_ / 2, h - 36), tname, FONT_SANS, 20, (40, 84, 66), track=2)
            x += tw_ + 12
    return mk(("plate10", key, w, h), w, h, fn)

# ============================================================ 1
def draw1(img, t):
    b = 1
    head10(img, t, "BLACK FRIDAY FINE PRINT", None, "RETURNS AND PRICE MATCHING")
    S(img, t, b, "Here is a question", banner10("bf", 480, 84, "BLACK FRIDAY", GOLD, GREEN_D, 44), 400, 245, mode="left", amp=3)
    S(img, t, b, "Here is a question", calendar_spr(), 500, 600, mode="up", amp=4, dt=0.25)
    # il cerchio salta tra le date finche la voce dice "Not roughly"; poi si ferma sul punto interrogativo
    t_hop = T(b, "Do you know the exact day"); t_stop = T(b, "Not roughly") + 0.5
    if t > t_hop:
        order = [11, 19, 6, 24, 13, 27, 8, 22]
        k = min(int((t - t_hop) / 0.55), len(order) - 1)
        i = order[k] if t < t_stop else 24
        x, y = cal_cell(i, x0=500, y0=600)
        put(img, ring_spr(78), x, y, alpha=min(1.0, (t - t_hop) * 3))
        if t >= t_stop:
            show(img, t, t_stop, qdisc(66), x, y, mode="zoom", dur=0.3, fl=False)
    S(img, t, b, "Do you know the exact day", pill9("THE EXACT DAY YOU COULD STILL RETURN IT?", 700, 62, fill=IVORY, size=26), 500, 960, mode="up", amp=2)
    S(img, t, b, "Not roughly", stampbox("nr", 300, 88, "NOT ROUGHLY", CORAL, 30), 790, 250, mode="pop", rot=-5, amp=3)
    # negozi
    xs, ys = 1330, [330, 520, 710]
    for i, nm in enumerate(STORES):
        S(img, t, b, "Walmart, Target and Costco", plate(("p1", nm), 720, 150, nm), xs, ys[i], mode="right", amp=4, ph=i, dt=0.28 * i)
    S(img, t, b, "policy pages", pill9("THEIR OWN POLICY PAGES", 520, 58, fill=SAGE, size=25), 1330, 225, mode="down", amp=2)
    S(img, t, b, "Black Friday exception", banner10("exc", 560, 78, "ONE BLACK FRIDAY EXCEPTION", GOLD, GREEN_D, 28), 1330, 880, mode="up", amp=3)
    S(img, t, b, "Black Friday exception", mk(("ex1", 1), 74, 74, lambda c: (c.ell((3, 3, 71, 71), fill=GOLD, outline=IVORY, width=4), c.text((37, 40), "!", FONT_SANS, 46, GREEN_D)), blur=8, dy=5), 1655, 280, mode="pop", amp=3, dt=0.3)
    S(img, t, b, "And the dates", pill9("DIFFERENT DATES AT EVERY STORE", 620, 62, fill=GOLD, size=28), 1330, 985, mode="up", amp=2)
    for i in range(3):
        S(img, t, b, "And the dates", qdisc(70), 1760, ys[i], mode="pop", amp=3, ph=i, dt=0.2 * i)

# ============================================================ 2
def browser(key, w, h, url, title, rows=4):
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 20, fill=PAPER, outline=(176, 190, 180), width=4)
        c.rrect((3, 3, w - 3, 62), 20, fill=(206, 218, 210)); c.d.rectangle(c._b((3, 44, w - 3, 62)), fill=(206, 218, 210))
        for k in range(3):
            c.ell((26 + k * 26, 24, 42 + k * 26, 40), fill=(CORAL, GOLD, OKG)[k])
        c.rrect((118, 14, w - 22, 50), 17, fill=PAPER)
        s = 21
        while tw(url, s, 1) > w - 190 and s > 12:
            s -= 1
        c.text((136, 32), url, FONT_SANS_M, s, (70, 96, 84), anchor="lm")
        c.rrect((3, 62, w - 3, 128), 0, fill=FOREST)
        ts = 28
        while tw(title, ts, 3) > w - 60 and ts > 14:
            ts -= 1
        c.text((28, 96), title, FONT_SANS, ts, IVORY, anchor="lm", track=3)
        for i in range(rows):
            wd = (w - 120) * (0.9 - 0.14 * (i % 3))
            c.rrect((28, 156 + i * 30, 28 + wd, 170 + i * 30), 6, fill=(206, 210, 202))
    return mk(("brw10", key, w, h), w, h, fn, blur=16, dy=12)

def seal(text="OFFICIAL", S_=118, col=GOLD):
    def fn(c):
        for k in range(18):
            a = math.radians(k * 20)
            c.ell((S_ / 2 + (S_ / 2 - 12) * math.cos(a) - 9, S_ / 2 + (S_ / 2 - 12) * math.sin(a) - 9, S_ / 2 + (S_ / 2 - 12) * math.cos(a) + 9, S_ / 2 + (S_ / 2 - 12) * math.sin(a) + 9), fill=col)
        c.ell((10, 10, S_ - 10, S_ - 10), fill=col)
        c.ell((20, 20, S_ - 20, S_ - 20), outline=GREEN_D, width=3)
        c.text((S_ / 2, S_ / 2 + 1), text, FONT_SANS, int(S_ * 0.112) if len(text) > 4 else int(S_ * 0.22), GREEN_D, track=1)
    return mk(("seal10", text, S_, col), S_, S_, fn, blur=8, dy=5)

def draw2(img, t):
    b = 2
    head10(img, t, "WHERE THE FACTS COME FROM", None, "OFFICIAL POLICY PAGES ONLY")
    sites = [("walmart", "corporate.walmart.com/policies", "WALMART POLICIES"), ("target", "target.com/help", "TARGET HELP"), ("costco", "customerservice.costco.com", "COSTCO CUSTOMER SERVICE")]
    xs = [330, 960, 1590]
    for i, (k, u, ti) in enumerate(sites):
        S(img, t, b, "First, where this comes from", browser(k, 560, 330, u, ti), xs[i], 350, mode="up", amp=4, ph=i, dt=0.3 * i)
        S(img, t, b, "official policy pages", seal("OFFICIAL"), xs[i] + 200, 440, mode="pop", amp=3, ph=i, dt=0.25 * i)
        S(img, t, b, "date on each page", pill9("DATE ON THE PAGE", 330, 52, fill=GOLD, size=22), xs[i], 560, mode="up", amp=2, dt=0.2 * i)
    t3 = T(b, "I did not use blogs")
    for i, (txt_, x) in enumerate((("BLOGS", 420), ("COUPON SITES", 880))):
        show(img, t, t3 + 0.3 * i, strip10(("nb", txt_), 360, 74, txt_, size=28), x, 700, mode="up", amp=3, ph=i)
        show(img, t, t3 + 0.55 + 0.3 * i, xcircle(70), x + 190, 700, mode="pop", amp=2, ph=i)
    t4 = T(b, "not about a senior discount")
    show(img, t, t4, strip10("sd", 420, 74, "SENIOR DISCOUNT", size=28), 1470, 700, mode="up", amp=3)
    show(img, t, t4 + 0.5, stampbox("nt", 330, 80, "NOT THIS VIDEO", CORAL, 26), 1610, 780, mode="pop", rot=-4, amp=2)
    S(img, t, b, "two things that protect", pill9("TWO THINGS THAT PROTECT YOUR MONEY", 820, 60, fill=IVORY, size=28), 960, 800, mode="up", amp=2, dt=-0.1)
    S(img, t, b, "how long you have to return", dossier("c2a", 760, 150, "HOW LONG TO RETURN", [("THE TIME YOU HAVE TO BRING IT BACK", INK)], GOLD, 26, 30, ic_hourglass), 520, 930, mode="left", amp=3)
    S(img, t, b, "what happens if the price", dossier("c2b", 760, 150, "IF THE PRICE DROPS", [("WHAT HAPPENS AFTER YOU BUY", INK)], GOLD, 26, 30, ic_pricetag), 1400, 930, mode="right", amp=3)

# ============================================================ 3
def draw3(img, t):
    b = 3
    head10(img, t, "WHY THESE TWO MATTER", None, "ON BLACK FRIDAY")
    tl = TL(D(11, 20), D(12, 31), 130, 1790)
    S(img, t, b, "Why do these two things matter", axis_spr(tl), (tl.x0 + tl.x1) / 2, 400, mode="left", amp=0, dt=0.1, fl=False)
    xb_, xe_ = tl.x(D(11, 27)), tl.xe(D(12, 25))
    tb = T(b, "Because a gift bought")
    show(img, t, tb, mk(("po3", 1), 14, 120, lambda c: c.line([(7, 0), (7, 120)], GOLD, 5), shadow=False), xb_, 505, mode="fade", fl=False)
    show(img, t, tb, flag10("BLACK FRIDAY", None, GOLD), xb_ + 72, 580, mode="down", amp=3)
    show(img, t, tb, badge_ic(("gift3",), 118, ic_gift, scale=0.9), xb_, 262, mode="pop", amp=4)
    show(img, t, tb, pill9("A GIFT BOUGHT", 270, 48, fill=SAGE, size=20), xb_, 345, mode="up", amp=2)
    tc = T(b, "Christmas morning")
    show(img, t, tc, mk(("po3", 2), 14, 120, lambda c: c.line([(7, 0), (7, 120)], IVORY, 5), shadow=False), xe_, 505, mode="fade", fl=False)
    show(img, t, tc, flag10("CHRISTMAS MORNING", None, IVORY, GREEN_D), xe_ - 40, 580, mode="down", amp=3)
    show(img, t, tc, badge_ic(("tree3",), 118, ic_tree, scale=0.9), xe_, 262, mode="pop", amp=4)
    show(img, t, tc, pill9("OPENED", 200, 48, fill=SAGE, size=20), xe_, 345, mode="up", amp=2)
    if t > tc:
        p = ease(seg(t, tc, 0.8))
        d = ImageDraw.Draw(img)
        xs0 = xb_ + 70; xs1 = xs0 + (xe_ - 70 - xs0) * p
        for x in range(int(xs0), int(xs1), 28):
            d.line([(x, 262), (min(x + 14, xs1), 262)], fill=GOLD, width=4)
    t30 = T(b, "thirty day return window")
    grow_bar(img, t, t30, xb_, tl.xe(D(12, 26)), 690, "30 DAY RETURN WINDOW", GOLD, GREEN_D, 70, 26)
    ta = T(b, "almost gone")
    if t > ta:
        p = ease(seg(t, ta, 0.9))
        used = int((xe_ - xb_) * p)
        ov = Image.new("RGBA", (max(2, used), 70), (10, 44, 36, 165))
        put(img, ov, xb_ + used / 2, 690)
        show(img, t, ta + 0.7, stampbox("ag", 330, 80, "ALMOST GONE", CORAL, 30), xb_ + (xe_ - xb_) / 2, 640 + 140, mode="pop", rot=-3, amp=2)
    tp = T(b, "Prices can also change")
    show(img, t, tp, hangtag(("pt3",), 250, 280, "PRICE", "CAN CHANGE", bsize=46), 330, 880, mode="up", amp=5, rot=-3)
    show(img, t, tp + 0.25, mk(("ar3d", 1), 60, 90, lambda c: (c.line([(30, 6), (30, 60)], CORAL, 12), c.poly([(8, 56), (52, 56), (30, 88)], fill=CORAL)), blur=6, dy=4), 150, 880, mode="down", amp=3)
    show(img, t, tp + 0.5, mk(("ar3u", 1), 60, 90, lambda c: (c.line([(30, 34), (30, 88)], OKG, 12), c.poly([(8, 38), (52, 38), (30, 6)], fill=OKG)), blur=6, dy=4), 510, 880, mode="up", amp=3)
    S(img, t, b, "price match can matter", stampbox("pm3", 420, 100, "PRICE MATCH", GOLD, 34), 1000, 880, mode="pop", rot=2, amp=3)
    t5 = T(b, "Every store handles both")
    show(img, t, t5 - 0.1, pill9("EACH IN ITS OWN WAY", 400, 52, fill=SAGE, size=22), 1560, 790, mode="up", amp=2)
    for i, nm in enumerate(STORES):
        show(img, t, t5 + 0.2 * i, navchip_spr(nm, 0), 1560, 865 + i * 76, mode="right", amp=3, ph=i)
    t6 = T(b, "starting with Walmart")
    show(img, t, t6, navchip_spr("WALMART", 1), 1560, 865, mode="zoom", dur=0.3, fl=False)

# ============================================================ 4
def ic_card_g(c, x, y, s):
    ic_card(c, x, y, s, (60, 150, 100))

def draw4(img, t):
    b = 4
    head10(img, t, "WALMART: RETURNS", 0, "HOW LONG YOU HAVE")
    dial_show(img, t, T(b, "ninety days"), "d4", 380, "90", "DAYS", 330, 400, GOLD, vsize=150)
    S(img, t, b, "ninety days", strip10("fp", 500, 72, "FROM THE PURCHASE", size=28), 330, 640, mode="up", amp=3, dt=0.5)
    S(img, t, b, "from when you receive it", strip10("fr", 500, 72, "OR FROM WHEN YOU RECEIVE IT", size=25), 330, 725, mode="up", amp=3)
    S(img, t, b, "unless it is listed", pill9("UNLESS LISTED IN THE EXCEPTIONS", 520, 56, fill=SAGE, size=21), 330, 815, mode="up", amp=2)
    S(img, t, b, "store receipt", tile("rc4", 250, 300, ic_receipt, "STORE\nRECEIPT", "IN THE STORE", GOLD, 1.0, 28, 20), 800, 430, mode="up", amp=5)
    S(img, t, b, "order number", tile("on4", 250, 300, ic_box8, "ONLINE\nORDER NUMBER", "FOR AN ONLINE BUY", GOLD, 1.0, 26, 19), 1080, 430, mode="up", amp=5, ph=1)
    S(img, t, b, "sends your money back", arrow9(80, 100, GOLD, down=True), 940, 640, mode="fade", amp=0, fl=False)
    S(img, t, b, "sends your money back", dossier("mb4", 560, 190, "MONEY BACK", [("THE SAME WAY YOU PAID", INK)], GOLD, 30, 30, ic_card_g), 940, 790, mode="up", amp=3)
    labels = [("in the store", "IN THE STORE", ic_storefront, 1450, 400), ("curbside", "CURBSIDE", ic_car2, 1700, 400),
              ("free by mail", "FREE BY MAIL", ic_box8, 1450, 730), ("FedEx", "FEDEX PICKUP", lambda c, x, y, s: ic_truck2(c, x, y, s, GOLD), 1700, 730)]
    for i, (k, tt, ic, x, y) in enumerate(labels):
        S(img, t, b, k, tile(("rm4", i), 230, 290, ic, tt, None, GOLD, 1.0, 24, 18, dark=True), x, y, mode="up", amp=5, ph=i)
    S(img, t, b, "You can return", pill9("RETURN IT ANY OF THESE WAYS", 520, 52, fill=GOLD, size=21), 1575, 225, mode="down", amp=2)
    source10(img, t, T(b, "The page I read"), "WALMART · UPDATED OCT 9, 2026", 1500, 1036)

# ============================================================ 5
def ic_two(a, b_):
    def f(c, x, y, s):
        a(c, x - 26 * s, y, s * 0.6); b_(c, x + 28 * s, y + 4 * s, s * 0.6)
    return f

def draw5(img, t):
    b = 5
    head10(img, t, "WALMART: LOST RECEIPT + HOLIDAY RULE", 0, "EXTENDED HOLIDAY RETURNS")
    S(img, t, b, "What if you lost the receipt", tile("lr5", 240, 250, ic_norcpt, "LOST THE\nRECEIPT?", None, CORAL, 0.9, 26, 18), 210, 310, mode="left", amp=4)
    S(img, t, b, "debit or credit card", dossier("l1", 700, 112, "STORE PURCHASES", [("LOOKED UP WITH A DEBIT OR CREDIT CARD", INK)], GOLD, 22, 26, ic_card_g), 760, 262, mode="up", amp=3)
    S(img, t, b, "phone number or email", dossier("l2", 700, 112, "ONLINE ORDERS", [("LOOKED UP WITH A PHONE NUMBER OR EMAIL", INK)], GOLD, 22, 26, ic_phone_app), 760, 392, mode="up", amp=3)
    S(img, t, b, "attempt to look up", dossier("lk5", 560, 210, "WALMART CAN ATTEMPT", [("TO LOOK IT UP", INK)], OKG, 34, 28, ic_magnify), 1490, 330, mode="right", amp=3, dt=-0.1)
    tl = TL(D(10, 1), D(1, 31, 2027), 110, 1810)
    t0 = T(b, "Now the holiday rule")
    show(img, t, t0 - 0.2, axis_spr(tl), (tl.x0 + tl.x1) / 2, 555, mode="left", amp=0, fl=False)
    S(img, t, b, "Extended Holiday Returns", banner10("eh5", 560, 70, "EXTENDED HOLIDAY RETURNS", GOLD, GREEN_D, 26), 420, 480, mode="up", amp=2)
    grow_bar(img, t, T(b, "October first"), tl.x(D(10, 1)), tl.xe(D(12, 31)), 660, "BOUGHT OCT 1 – DEC 31", GOLD, GREEN_D, 62, 26, dur=1.0)
    tj = T(b, "January thirty first")
    show(img, t, tj, mk(("po5", 1), 14, 130, lambda c: c.line([(7, 0), (7, 130)], IVORY, 5), shadow=False), tl.xe(D(1, 31, 2027)) - 6, 630, mode="fade", fl=False)
    show(img, t, tj, flag10("RETURNABLE UNTIL JAN 31", None, IVORY, GREEN_D), tl.xe(D(1, 31, 2027)) - 230, 742, mode="down", amp=2)
    S(img, t, b, "some exceptions may apply", pill9("SOME EXCEPTIONS MAY APPLY", 480, 54, fill=CORAL, ink=IVORY, size=21), 330, 905, mode="up", amp=2)
    ex = [("wireless phones", "WIRELESS\nPHONES", ic_phone_app), ("protection plans", "PROTECTION\nPLANS", lambda c, x, y, s: ic_shield(c, x, y, s * 0.8, GOLD, lambda cc, xx, yy, ss: check_ic(cc, xx, yy + 2, ss * 0.7, GOLD))),
          ("major appliances", "MAJOR\nAPPLIANCES", ic_fridge), ("Dyson products", "DYSON\nPRODUCTS", ic_vacuum), ("seasonal and luxury", "SEASONAL AND\nLUXURY GOODS", ic_two(ic_tree, ic_gem))]
    for i, (k, tt, ic) in enumerate(ex):
        S(img, t, b, k, tile(("ex5", i), 235, 220, ic, tt, None, CORAL, 0.9, 20, 16, dark=True), 740 + i * 255, 900, mode="up", amp=4, ph=i)

# ============================================================ 6
def draw6(img, t):
    b = 6
    head10(img, t, "WALMART: SHORTER WINDOWS", 0, "CHECK YOUR ITEM")
    S(img, t, b, "Now the shorter windows", banner10("sw6", 560, 64, "SHORTER WINDOWS", GOLD, GREEN_D, 28), 360, 215, mode="left", amp=2)
    X0, PPD = 780, 11.5
    rows = [("major appliances", "MAJOR APPLIANCES", ic_fridge, 2, "2 DAYS", 300), ("wireless phones", "MOST WIRELESS PHONES", ic_phone_app, 14, "14 DAYS", 440),
            ("Consumer electronics", "ELECTRONICS AND PCS", ic_tv, 30, "30 DAYS", 570), ("Hearing aids", "HEARING AIDS, GLASSES, LENSES", ic_hearing, 60, "60 DAYS", 700)]
    for i, (k, lab, ic, days, dl, y) in enumerate(rows):
        t0 = T(b, k)
        show(img, t, t0, strip10(("rw6", i), 600, 88, lab, size=26, icon=ic), 410, y, mode="left", amp=3, ph=i)
        grow_bar(img, t, t0 + 0.3, X0, X0 + days * PPD, y, "", GOLD, GREEN_D, 54, dur=0.8)
        show(img, t, t0 + 0.9, pill9(dl, 190, 54, fill=IVORY, size=24), X0 + days * PPD + 125, y, mode="pop", amp=2, ph=i)
    S(img, t, b, "thirty days for unopened", pill9("UP TO 30 DAYS: UNOPENED, UNINSTALLED, FACTORY SEALED", 780, 46, fill=SAGE, size=19), 1170, 360, mode="up", amp=2)
    S(img, t, b, "doesn't spell out", dossier("hr6", 800, 120, "HOLIDAY RULE", [("NOT SPELLED OUT FOR EACH ITEM", INK)], CORAL, 26, 26), 560, 880, mode="left", amp=3)
    S(img, t, b, "ask a Walmart associate", say9("as6", 860, 120, ["ASK A WALMART ASSOCIATE", "BEFORE YOU BUY"], 34, tail="bl"), 1370, 855, mode="right", amp=3)

# ============================================================ 7
def draw7(img, t):
    b = 7
    head10(img, t, "WALMART: PRICE MATCHING", 0, "A DIFFERENT SECTION")
    S(img, t, b, "Next, Walmart price matching", browser("pm7", 720, 470, "corporate.walmart.com/policies", "PRICE MATCH POLICY", 5), 480, 460, mode="left", amp=4)
    S(img, t, b, "its own section", pill9("ITS OWN SECTION", 290, 46, fill=SAGE, size=19), 690, 322, mode="down", amp=2, dt=0.3)
    tj = T(b, "June eighth")
    show(img, t, tj, stampbox("jn7", 440, 100, "UPDATED JUNE 8, 2023", GOLD, 28), 480, 640, mode="pop", rot=-3, amp=3)
    show(img, t, T(b, "keep that date in mind"), mk(("rg7", 1), 520, 150, lambda c: c.ell((6, 6, 514, 144), outline=CORAL, width=7), blur=6, dy=3, alpha=0.4), 480, 640, mode="zoom", fl=False, dur=0.5)
    S(img, t, b, "keep that date in mind", pill9("KEEP THAT DATE IN MIND", 460, 56, fill=CORAL, ink=IVORY, size=22), 480, 790, mode="up", amp=2)
    t1 = T(b, "For an item you buy in a Walmart store")
    show(img, t, t1, hangtag("st7", 250, 300, "IN A", "WALMART STORE", bsize=44), 1150, 380, mode="up", amp=4, rot=-3)
    S(img, t, b, "identical item advertised", mk(("eq7", 1), 100, 100, lambda c: (c.rrect((10, 24, 90, 40), 6, fill=GOLD), c.rrect((10, 60, 90, 76), 6, fill=GOLD)), blur=6, dy=4), 1350, 380, mode="pop", amp=2)
    S(img, t, b, "identical item advertised", browser("wc7", 380, 300, "walmart.com", "SAME ITEM", 3), 1610, 380, mode="right", amp=4)
    S(img, t, b, "tell the associate", strip10("a7", 780, 84, "TELL THE ASSOCIATE THE PRICE AT CHECKOUT", size=24, icon=ic_chat), 1380, 640, mode="right", amp=3)
    S(img, t, b, "the identical item must be", strip10("b7", 780, 84, "THE IDENTICAL ITEM", size=26, icon=ic_barcode), 1380, 745, mode="right", amp=3)
    S(img, t, b, "in stock", strip10("c7", 780, 84, "IN STOCK AND AVAILABLE ON WALMART.COM NOW", size=22, icon=ic_cart2), 1380, 850, mode="right", amp=3)

# ============================================================ 8
def draw8(img, t):
    b = 8
    head10(img, t, "WALMART: THE BLACK FRIDAY EXCEPTION", 0, "WHAT THE PAGE SAYS IT DOES NOT MATCH")
    S(img, t, b, "Now the part about Black Friday", banner10("dn8", 780, 80, "WALMART DOES NOT MATCH", CORAL, IVORY, 34), 520, 245, mode="left", amp=2)
    S(img, t, b, "walmart dot com prices on special events", pill9("WALMART.COM PRICES ON SPECIAL EVENTS", 700, 50, fill=SAGE, size=22), 520, 320, mode="up", amp=2)
    items = [("clearance", "CLEARANCE", 400, False), ("Rollback", "ROLLBACK", 485, False), ("Black Friday or Cyber Monday deals", "BLACK FRIDAY OR CYBER MONDAY DEALS", 580, True), ("limited time promotions", "OTHER LIMITED TIME PROMOTIONS", 675, False)]
    for i, (k, tt, y, hot) in enumerate(items):
        t0 = T(b, k)
        show(img, t, t0, strip10(("it8", i), 740, 80, tt, fill=(40, 70, 44) if hot else (10, 50, 40), border=GOLD if hot else SAGE_D, size=26 if not hot else 25, bold=hot), 490, y, mode="left", amp=3, ph=i)
        show(img, t, t0 + 0.35, xcircle(66), 940, y, mode="pop", amp=2, ph=i)
    S(img, t, b, "competitor prices", strip10("cp8", 740, 80, "COMPETITOR PRICES", size=26), 490, 800, mode="left", amp=3, dt=-0.2)
    S(img, t, b, "competitor prices", xcircle(66), 940, 800, mode="pop", amp=2, dt=0.15)
    S(img, t, b, "store manager", dossier("mg8", 640, 200, "STORE MANAGER ON DUTY", [("HAS THE FINAL DECISION", INK)], GOLD, 30, 28, I(ic_person, 0.5, col=GOLD) if False else lambda c, x, y, s: ic_person(c, x, y + 6, s * 1.9, GOLD_D)), 1450, 400, mode="right", amp=3)
    S(img, t, b, "purchases made on walmart dot com", dossier("wc8", 700, 190, "ON WALMART.COM", [("NO PRICE MATCHING", CORAL)], CORAL, 30, 34, ic_pricetag), 1430, 690, mode="right", amp=3)
    S(img, t, b, "dropped after you bought", stampbox("dr8", 700, 110, "EVEN IF THE PRICE DROPPED AFTER YOU BOUGHT", CORAL, 25), 1430, 870, mode="pop", rot=-2, amp=3)

# ============================================================ 9
def draw9(img, t):
    b = 9
    head10(img, t, "TARGET: HOLIDAY RETURNS", 1, "ELECTRONICS AND ENTERTAINMENT")
    tl = TL(D(11, 1), D(1, 31, 2027), 110, 1810)
    t0 = T(b, "Now Target")
    show(img, t, t0 + 0.1, axis_spr(tl), (tl.x0 + tl.x1) / 2, 250, mode="left", amp=0, fl=False)
    grow_bar(img, t, T(b, "November first"), tl.x(D(11, 1)), tl.xe(D(12, 24)), 360, "BOUGHT NOV 1 – DEC 24", GOLD, GREEN_D, 62, 26, dur=1.0)
    t26 = T(b, "December twenty sixth")
    show(img, t, t26, mk(("po9", 1), 14, 150, lambda c: c.line([(7, 0), (7, 150)], IVORY, 5), shadow=False), tl.x(D(12, 26)), 340, mode="fade", fl=False)
    show(img, t, t26, flag10("RETURN WINDOW BEGINS DEC 26", None, IVORY, GREEN_D), tl.x(D(12, 26)) - 150, 440, mode="down", amp=2)
    # corsia 1
    t30 = T(b, "Those items, except")
    show(img, t, t30, dossier("l9a", 900, 150, "ELECTRONICS + ENTERTAINMENT", [("EXCEPT APPLE AND BEATS", INK)], GOLD, 28, 30, ic_tv), 560, 590, mode="left", amp=3)
    grow_bar(img, t, T(b, "thirty days from then"), tl.x(D(12, 26)), tl.xe(D(1, 24, 2027)), 590, "30 DAYS", GOLD, GREEN_D, 66, 28, dur=0.9)
    tj = T(b, "January twenty fourth")
    show(img, t, tj, flag10("JAN 24, 2027", None, GOLD, GREEN_D), tl.xe(D(1, 24, 2027)) - 10, 675, mode="down", amp=2)
    # corsia 2
    t14 = T(b, "Apple and Beats products")
    show(img, t, t14, dossier("l9b", 900, 150, "APPLE, BEATS AND PHONES", [("UNLOCKED OR PREPAID MOBILE PHONES", INK)], CORAL, 26, 30, ic_phone_app), 560, 790, mode="left", amp=3)
    grow_bar(img, t, T(b, "fourteen days"), tl.x(D(12, 26)), tl.xe(D(1, 8, 2027)), 790, "14 DAYS", CORAL, IVORY, 66, 28, dur=0.8)
    tj8 = T(b, "January eighth")
    show(img, t, tj8, flag10("JAN 8", None, CORAL, IVORY), tl.xe(D(1, 8, 2027)) - 10, 875, mode="down", amp=2)

# ============================================================ 10
def draw10(img, t):
    b = 10
    head10(img, t, "TARGET: EVERYTHING ELSE", 1, "THE NORMAL POLICY")
    S(img, t, b, "normal Target policy", banner10("np10", 520, 66, "THE NORMAL TARGET POLICY", GOLD, GREEN_D, 26), 380, 215, mode="left", amp=2)
    dial_show(img, t, T(b, "ninety days"), "d10", 360, "90", "DAYS", 330, 470, GOLD, vsize=140)
    S(img, t, b, "most unopened items", strip10("u10", 520, 72, "MOST UNOPENED ITEMS", size=26), 330, 710, mode="up", amp=3)
    S(img, t, b, "in new condition", strip10("n10", 520, 72, "IN NEW CONDITION", size=26), 330, 795, mode="up", amp=3)
    S(img, t, b, "refund or exchange", banner10("re10", 520, 84, "REFUND OR EXCHANGE", OKG, GREEN_D, 30), 330, 915, mode="up", amp=3)
    S(img, t, b, "opened, damaged or without", pill9("MAY BE DENIED A REFUND OR EXCHANGE", 700, 54, fill=CORAL, ink=IVORY, size=22), 920, 300, mode="down", amp=2)
    den = [("opened", "OPENED", ic_openbox, 700), ("damaged", "DAMAGED", ic_crack, 920), ("without a receipt", "NO RECEIPT", ic_norcpt, 1140)]
    for i, (k, tt, ic, x) in enumerate(den):
        S(img, t, b, k, tile(("dn10", i), 200, 270, ic, tt, None, CORAL, 0.9, 22, 17, dark=True), x, 480, mode="up", amp=4, ph=i)
    S(img, t, b, "Target Circle Card holders", dossier("c1", 560, 150, "CIRCLE CARD HOLDERS", [("EXTENDED RETURN WINDOWS", INK)], GOLD, 24, 28, ic_cardring), 1560, 350, mode="right", amp=3)
    S(img, t, b, "Target Circle three sixty", dossier("c2", 560, 150, "CIRCLE 360 MEMBERS", [("EXTENDED RETURN WINDOWS", INK)], GOLD, 24, 28, ic_cardring), 1560, 525, mode="right", amp=3)
    S(img, t, b, "doesn't list the days", dossier("dl10", 1040, 150, "THE DAYS ARE NOT LISTED ON THIS PAGE", [("CHECK THE RETURN POLICY PAGE", INK)], CORAL, 28, 32, ic_note2), 1170, 780, mode="up", amp=3)
