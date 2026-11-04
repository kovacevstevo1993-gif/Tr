"""Video lungo 10 (BLACK FRIDAY) - blocchi 11-20. Voce: COPIONE-VIDEO-BLACK-FRIDAY.md. Durate: screenshot CapCut 04/11/2026."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bf10_kit import *
from bf10_b01_10 import S, I, ic_card_g, ic_two, browser, seal, plate, qdisc
from long8_b21_32 import endbox, disc_panel

def rowcard(key, w, h, lines, accent=GOLD, size=26, icon=None):
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 18, fill=PAPER, outline=(196, 190, 170), width=3)
        c.rrect((3, 3, 22, h - 3), 12, fill=accent); c.d.rectangle(c._b((12, 3, 22, h - 3)), fill=accent)
        n = len(lines)
        x0 = 44
        if icon:
            icon(c, 58, h / 2, 0.5); x0 = 108
        for i, ln in enumerate(lines):
            col = INK
            if isinstance(ln, tuple):
                ln, col = ln
            s = size
            while tw(ln, s, 2) > w - x0 - 16 and s > 12:
                s -= 1
            c.text((x0, h / 2 + (i - (n - 1) / 2) * (size + 8)), ln, FONT_SANS_M if i else FONT_SANS, s, col, anchor="lm", track=1)
    return mk(("rowc10", key, w, h), w, h, fn)

def ic_pair(a, b_, sa=0.6, sb=0.6):
    def f(c, x, y, s):
        a(c, x - 28 * s, y, s * sa); b_(c, x + 30 * s, y + 4 * s, s * sb)
    return f

# ============================================================ 11
def draw11(img, t):
    b = 11
    head10(img, t, "TARGET: THE HOLIDAY PRICE MATCH", 1, "ASK AT PURCHASE OR WITHIN 14 DAYS")
    tl = TL(D(11, 1), D(12, 31), 110, 1810)
    S(img, t, b, "Target also has a holiday price match", axis_spr(tl), (tl.x0 + tl.x1) / 2, 235, mode="left", amp=0, fl=False)
    grow_bar(img, t, T(b, "starting November first"), tl.x(D(11, 1)), tl.xe(D(12, 24)), 345, "PRICE GOES LOWER AT TARGET ON OR BEFORE DEC 24", GOLD, GREEN_D, 62, 25, dur=1.0)
    S(img, t, b, "you can request a price match", banner10("rq11", 540, 76, "YOU CAN REQUEST A PRICE MATCH", GOLD, GREEN_D, 26), 410, 470, mode="left", amp=2)
    S(img, t, b, "at the time of purchase", pill9("AT THE TIME OF PURCHASE", 420, 56, fill=IVORY, size=23), 1010, 470, mode="up", amp=2)
    S(img, t, b, "within fourteen days", pill9("OR WITHIN 14 DAYS AFTER", 420, 56, fill=IVORY, size=23), 1470, 470, mode="up", amp=2)
    S(img, t, b, "In a store", pill9("IN A STORE", 360, 50, fill=SAGE, size=22), 470, 590, mode="down", amp=2)
    S(img, t, b, "proof of the lower price", tile("pf11", 240, 290, lambda c, x, y, s: ic_pricetag(c, x, y, s), "PROOF OF THE\nLOWER PRICE", None, GOLD, 1.0, 20, 15, dark=True), 330, 770, mode="up", amp=4)
    S(img, t, b, "Guest Services", tile("gs11", 240, 290, ic_desk, "GUEST\nSERVICES", "IN THE STORE", GOLD, 1.0, 22, 16, dark=True), 640, 770, mode="up", amp=4, ph=1)
    S(img, t, b, "Guest Services", arrow9(70, 50, GOLD), 485, 770, mode="fade", fl=False, dt=0.3)
    S(img, t, b, "Target dot com or app", pill9("TARGET.COM OR APP", 420, 50, fill=SAGE, size=22), 1330, 590, mode="down", amp=2)
    S(img, t, b, "chat online", tile("ch11", 240, 290, ic_chat, "CHAT\nONLINE", None, GOLD, 1.0, 24, 16, dark=True), 1210, 770, mode="up", amp=4, ph=2)
    S(img, t, b, "call Guest Services", tile("cl11", 240, 290, ic_handset, "CALL GUEST\nSERVICES", None, GOLD, 1.0, 22, 16, dark=True), 1480, 770, mode="up", amp=4, ph=3)
    S(img, t, b, "Original receipts", tile("rp11", 240, 290, ic_receipt, "RECEIPTS OR\nPACKING SLIPS", "REQUIRED", CORAL, 1.0, 20, 18), 1740, 770, mode="up", amp=4, ph=4)

# ============================================================ 12
def draw12(img, t):
    b = 12
    head10(img, t, "TARGET: THE LIMITS", 1, "READ THEM TOO")
    S(img, t, b, "identical", banner10("id12", 520, 70, "THE ITEM MUST BE IDENTICAL", GOLD, GREEN_D, 25), 360, 235, mode="left", amp=2)
    for i, (k, tt) in enumerate((("same brand", "BRAND"), ("size", "SIZE"), ("color", "COLOR"), ("quantity", "QUANTITY"), ("model number", "MODEL NUMBER"))):
        t0 = T(b, k)
        show(img, t, t0, strip10(("at12", i), 480, 70, tt, size=26), 360, 335 + i * 84, mode="left", amp=2, ph=i)
        show(img, t, t0 + 0.3, okcircle(52), 570, 335 + i * 84, mode="pop", amp=1, ph=i)
    S(img, t, b, "cannot be combined", banner10("cb12", 540, 70, "CANNOT BE COMBINED WITH", CORAL, IVORY, 25), 1010, 235, mode="up", amp=2)
    for i, (k, tt, ic, y) in enumerate((("Target Circle bonuses", "TARGET CIRCLE BONUSES", ic_cardring, 335), ("gift card offers", "GIFT CARD OFFERS", ic_giftcard, 425), ("Target coupons", "TARGET COUPONS", ic_coupon, 515))):
        t0 = T(b, k)
        show(img, t, t0, strip10(("cm12", i), 520, 76, tt, size=24, icon=ic), 1010, y, mode="up", amp=2, ph=i)
        show(img, t, t0 + 0.3, xcircle(56), 1220, y, mode="pop", amp=1, ph=i)
    S(img, t, b, "limit quantities per guest", dossier("lq12", 540, 130, "LIMIT PER GUEST", [("TARGET CAN LIMIT QUANTITIES", INK)], GOLD, 24, 26, ic_stack), 1010, 650, mode="up", amp=3)
    S(img, t, b, "It excludes", banner10("ex12", 460, 70, "EXCLUDED", CORAL, IVORY, 28), 1600, 235, mode="right", amp=2)
    for i, (k, tt) in enumerate((("clearance", "CLEARANCE"), ("closeout", "CLOSEOUT"), ("open package", "OPEN PACKAGE"), ("refurbished", "REFURBISHED"), ("minimum purchase", "MINIMUM-PURCHASE DEALS"))):
        t0 = T(b, k)
        show(img, t, t0, strip10(("xc12", i), 440, 66, tt, size=22), 1600, 335 + i * 80, mode="right", amp=2, ph=i)
        show(img, t, t0 + 0.3, xcircle(48), 1790, 335 + i * 80, mode="pop", amp=1, ph=i)
    S(img, t, b, "Alaska and Hawaii", dossier("ah12", 1500, 150, "TARGET.COM AND THE APP", [("PRICE MATCHING NOT AVAILABLE IN ALASKA AND HAWAII", INK)], CORAL, 28, 30, ic_island), 960, 880, mode="up", amp=3)

# ============================================================ 13
def draw13(img, t):
    b = 13
    head10(img, t, "COSTCO: RETURNS", 2, "THE SATISFACTION GUARANTEE")
    S(img, t, b, "Now Costco", seal("100%", 250, GOLD), 330, 360, mode="pop", amp=4)
    S(img, t, b, "Risk Free", banner10("rf13", 560, 70, "RISK FREE SATISFACTION GUARANTEE", GOLD, GREEN_D, 22), 330, 540, mode="up", amp=2)
    S(img, t, b, "October twenty twenty five", pill9("PAGE PUBLISHED OCT 2025", 440, 50, fill=SAGE, size=21), 330, 620, mode="up", amp=2)
    dial_show(img, t, T(b, "Electronics have their own rule"), "d13", 300, "90", "DAYS", 330, 810, GOLD, vsize=116)
    S(img, t, b, "from the date you received", pill9("FROM THE DATE YOU RECEIVED IT", 520, 52, fill=IVORY, size=21), 330, 985, mode="up", amp=1)
    items = [("televisions", "TVS", ic_tv), ("projectors", "PROJECTORS", ic_projector), ("major appliances", "MAJOR\nAPPLIANCES", ic_fridge), ("computers", "COMPUTERS", ic_laptop),
             ("tablets", "TABLETS", ic_tablet), ("smart wearable", "SMART\nWEARABLES", ic_watch), ("cameras", "CAMERAS", ic_camera), ("drones", "DRONES", ic_drone),
             ("camcorders", "CAMCORDERS", ic_camcorder), ("M P three players", "MP3\nPLAYERS", ic_mp3), ("cellular phones", "CELL\nPHONES", ic_phone_app)]
    for i, (k, tt, ic) in enumerate(items):
        r_, q = divmod(i, 5)
        S(img, t, b, k, tile(("it13", i), 196, 200, ic, tt, None, GOLD, 1.0, 17, 14), 900 + q * 210, 340 + r_ * 220, mode="up", amp=3, ph=i)
    S(img, t, b, "carrier service contract", dossier("ph13", 700, 180, "PHONES", [("RETURN DETAILS VARY BY CARRIER CONTRACT", INK)], CORAL, 28, 30, ic_phone_app), 1470, 800, mode="up", amp=3)

# ============================================================ 14
def draw14(img, t):
    b = 14
    head10(img, t, "COSTCO: WHAT IT WILL NOT REFUND", 2, "AND WHAT TO ASK ABOUT")
    S(img, t, b, "Costco also lists items", banner10("nr14", 680, 76, "ITEMS COSTCO WILL NOT REFUND", CORAL, IVORY, 28), 470, 235, mode="left", amp=2)
    tiles = [("airline and live performance", "AIRLINE AND LIVE\nEVENT ITEMS", ic_ticket, 220), ("precious metals", "PRECIOUS\nMETALS", ic_goldbar, 480),
             ("Shop Cards", "SHOP\nCARDS", ic_card_g, 740), ("gift cards", "GIFT\nCARDS", ic_giftcard, 1000)]
    for i, (k, tt, ic, x) in enumerate(tiles):
        S(img, t, b, k, tile(("nr14", i), 240, 300, ic, tt, None, CORAL, 1.0, 21, 15), x, 470, mode="up", amp=4, ph=i)
    S(img, t, b, "Custom special order", dossier("cs14", 1040, 200, "CUSTOM SPECIAL ORDER ITEMS", [("NO RETURNS OR REFUNDS, EXCEPT FOR", INK), ("WARRANTY REPAIR OR REPLACEMENT", (150, 100, 20))], GOLD, 24, 28, ic_wrench), 610, 800, mode="left", amp=3)
    S(img, t, b, "hearing aids", dossier("ha14", 620, 250, "HEARING AIDS", [("CONTACT THE HEARING AID CENTER", INK), ("AT YOUR COSTCO WAREHOUSE", INK)], GOLD, 26, 28, ic_hearing), 1530, 420, mode="right", amp=3)
    S(img, t, b, "limited useful life", dossier("tb14", 620, 190, "TIRES AND BATTERIES", [("PRODUCTS WITH A LIMITED USEFUL LIFE", INK)], GOLD, 24, 26, ic_pair(ic_tire, ic_battery, 0.8, 0.8)), 1530, 680, mode="right", amp=3)
    S(img, t, b, "product specific limited warranty", banner10("pw14", 620, 76, "PRODUCT-SPECIFIC LIMITED WARRANTY", GOLD, GREEN_D, 22), 1530, 850, mode="up", amp=2)

# ============================================================ 15
def draw15(img, t):
    b = 15
    head10(img, t, "COSTCO: THE PRICE MATCH", 2, "SALE DATES AND 30 DAYS")
    S(img, t, b, "specific sale dates", banner10("sd15", 800, 76, "ITEMS WITH SPECIFIC SALE DATES", GOLD, GREEN_D, 28), 520, 235, mode="left", amp=2)
    S(img, t, b, "holiday savings promotions", pill9("SUCH AS HOLIDAY SAVINGS PROMOTIONS", 640, 50, fill=SAGE, size=22), 1380, 235, mode="right", amp=2)
    t_p = T(b, "active promotional dates")
    grow_bar(img, t, t_p, 190, 1230, 370, "ACTIVE PROMOTIONAL DATES", GOLD, GREEN_D, 70, 26, dur=0.9, left=40)
    t_d = T(b, "thirty days of the purchase date")
    grow_bar(img, t, t_d, 760, 1560, 480, "30 DAYS FROM THE PURCHASE DATE", IVORY, GREEN_D, 70, 24, dur=0.9, left=36)
    show(img, t, t_p + 0.3, mk(("po15", 1), 14, 190, lambda c: c.line([(7, 0), (7, 190)], IVORY, 5), shadow=False), 760, 440, mode="fade", fl=False)
    show(img, t, t_d + 0.8, flag10("PURCHASE DATE", None, IVORY, GREEN_D), 760, 570, mode="down", amp=2)
    ov = Image.new("RGBA", (1230 - 760, 230), (110, 200, 130, 60))
    if t > t_d + 0.7:
        put(img, ov, 995, 425, alpha=ease(seg(t, t_d + 0.7, 0.5)))
        show(img, t, t_d + 1.2, pill9("REQUEST WITHIN BOTH", 380, 54, fill=OKG, size=22), 1030, 620, mode="up", amp=2)
    t_a = T(b, "after the promotion has ended")
    grow_bar(img, t, t_a, 1230, 1740, 370, "AFTER IT ENDS: MAY BE DENIED", CORAL, IVORY, 70, 22, dur=0.7, hatch=True)
    S(img, t, b, "For other purchases", dossier("op15", 820, 190, "OTHER PURCHASES", [("A PRICE DROP WITHIN 30 DAYS OF YOUR", INK), ("PURCHASE IS ELIGIBLE", INK)], GOLD, 26, 28, ic_pricetag), 520, 830, mode="left", amp=3)
    S(img, t, b, "does not price match", dossier("ot15", 820, 190, "OTHER BUSINESSES OR RETAILERS", [("COSTCO DOES NOT PRICE MATCH WITH THEM", (160, 60, 50))], CORAL, 24, 28, ic_storefront), 1400, 830, mode="right", amp=3)
    source10(img, t, T(b, "May twenty twenty six"), "COSTCO · PUBLISHED MAY 2026", 1560, 1030)

# ============================================================ 16
def draw16(img, t):
    b = 16
    head10(img, t, "COSTCO: MORE DETAILS", 2, "ONLINE ORDERS AND WAREHOUSES")
    S(img, t, b, "A few more details", pill9("A FEW MORE DETAILS FROM THAT PAGE", 640, 52, fill=SAGE, size=22), 960, 215, mode="down", amp=2)
    S(img, t, b, "Costco dot com orders", tile("cc16", 300, 340, ic_laptop, "COSTCO.COM\nORDERS", "THAT PAGE IS FOR", GOLD, 1.0, 24, 17, dark=True), 300, 450, mode="left", amp=4)
    S(img, t, b, "five to ten business days", arrow9(100, 60, GOLD), 520, 450, mode="fade", fl=False)
    dial_show(img, t, T(b, "five to ten business days"), "d16", 330, "5–10", "BUSINESS DAYS", 770, 450, GOLD, vsize=96, sub="TYPICALLY")
    S(img, t, b, "original form of payment", pill9("CREDIT TO YOUR ORIGINAL FORM OF PAYMENT", 640, 52, fill=IVORY, size=20), 770, 670, mode="up", amp=2)
    S(img, t, b, "warehouse purchase", tile("wh16", 300, 340, ic_storefront, "WAREHOUSE\nPURCHASE", None, GOLD, 1.0, 22, 17, dark=True), 1250, 450, mode="right", amp=4)
    S(img, t, b, "Returns counter", arrow9(100, 60, GOLD), 1450, 450, mode="fade", fl=False)
    S(img, t, b, "Returns counter", tile("rc16", 300, 340, ic_desk, "ASK AT THE\nRETURNS COUNTER", "WHERE YOU BOUGHT IT", GOLD, 1.0, 20, 15, dark=True), 1650, 450, mode="right", amp=4, ph=1)
    S(img, t, b, "sole discretion", dossier("sd16", 820, 200, "CAN DENY A REQUEST", [("AT ITS SOLE DISCRETION", INK)], CORAL, 28, 32, ic_stamp if False else ic_note2), 500, 860, mode="left", amp=3)
    S(img, t, b, "restrict its price match policy", dossier("rs16", 900, 150, "MAY RESTRICT ITS POLICY IN THE FUTURE", [("IN THE FUTURE, IF IT DECIDES TO", INK)], GOLD, 26, 26, ic_hourglass), 1400, 830, mode="right", amp=3)
    S(img, t, b, "point of purchase", banner10("pp16", 760, 72, "RESTRICTIONS SHOWN AT THE POINT OF PURCHASE", GOLD, GREEN_D, 22), 1400, 950, mode="up", amp=2)

# ============================================================ 17
def draw17(img, t):
    b = 17
    head10(img, t, "RECAP: STORE BY STORE", None, "THE SHORT VERSION")
    S(img, t, b, "Let's recap", banner10("rc17", 520, 66, "LET'S RECAP", GOLD, GREEN_D, 30), 960, 205, mode="down", amp=2)
    cols = [("WALMART", 360, [("ninety days for most items", ["90 DAYS FOR", "MOST ITEMS"]), ("holiday rule", ["HOLIDAY RULE", "TO JAN 31"]), ("shorter windows for some items", ["SHORTER WINDOWS", "FOR SOME ITEMS"]),
                              ("price match policy that excludes", ["NO PRICE MATCH ON WALMART.COM", "BLACK FRIDAY / CYBER MONDAY DEALS"])]),
            ("TARGET", 960, [("extended returns for electronics", ["EXTENDED RETURNS FOR", "ELECTRONICS: NOV 1 – DEC 24"]), ("price match request within fourteen days", ["PRICE MATCH REQUEST", "WITHIN 14 DAYS"]), ("with receipts", ["RECEIPTS", "REQUIRED"])]),
            ("COSTCO", 1560, [("ninety days for electronics", ["90 DAYS FOR", "ELECTRONICS"]), ("price matches within thirty days", ["PRICE MATCH WITHIN", "30 DAYS"]), ("the sale dates", ["AND WITHIN THE", "SALE DATES"])])]
    for ci, (nm, x, rows) in enumerate(cols):
        t0 = T(b, nm.capitalize() + ":")
        show(img, t, t0, plate(("rc17", nm), 540, 100, nm, ()), x, 330, mode="up", amp=3, ph=ci)
        for ri, (k, lines) in enumerate(rows):
            tk = T(b, k)
            show(img, t, tk, rowcard(("r17", nm, ri), 520, 128, lines, GOLD if nm != "TARGET" else GOLD, 24), x, 470 + ri * 150, mode="up", amp=3, ph=ri + ci)

# ============================================================ 18
def draw18(img, t):
    b = 18
    head10(img, t, "A SIMPLE PLAN", None, "BEFORE YOU BUY")
    steps = [("Keep every receipt", ["KEEP EVERY RECEIPT", "ONLINE ORDERS: KEEP THE ORDER NUMBER"], ic_receipt), ("write the return deadline", ["WRITE THE RETURN DEADLINE", "ON THE RECEIPT"], ic_calendar),
             ("dates on that store's own page", ["USE THE DATES ON", "THAT STORE'S OWN PAGE"], ic_doc), ("shorter list", ["ON A SHORTER LIST? PHONES, APPLIANCES,", "HEARING AIDS: ASK AT THE COUNTER FIRST"], ic_hearing),
             ("if you want a price match", ["WANT A PRICE MATCH?", "ASK BEFORE YOU LEAVE THE STORE"], ic_pricetag)]
    for i, (k, lines, ic) in enumerate(steps):
        t0 = T(b, k)
        y = 300 + i * 128
        show(img, t, t0, numdisc(i + 1, 84), 150, y, mode="pop", amp=2, ph=i)
        show(img, t, t0 + 0.1, rowcard(("s18", i), 880, 108, lines, GOLD, 26, icon=(lambda c, x, y_, s, f=ic: f(c, x, y_, s * 0.9) if f not in (ic_calendar,) else ic_calendar(c, x, y_, s * 0.9, GOLD, "31"))), 650, y, mode="left", amp=2, ph=i)
    tr = T(b, "write the return deadline")
    S(img, t, b, "Keep every receipt", mk(("rcp18", 1), 440, 640, lambda c: (
        c.rrect((0, 10, 440, 630), 8, fill=PAPER),
        [c.poly([(k, 12), (k + 14, 0), (k + 28, 12)], fill=PAPER) for k in range(0, 440, 28)],
        [c.poly([(k, 628), (k + 14, 640), (k + 28, 628)], fill=PAPER) for k in range(0, 440, 28)],
        c.text((220, 70), "RECEIPT", FONT_SANS, 40, INK, track=8),
        [c.line([(k, 112), (k + 8, 112)], (170, 166, 154), 3) for k in range(28, 412, 16)],
        [c.rrect((36, 160 + i * 54, 36 + (300 - (i % 3) * 60), 178 + i * 54), 5, fill=(206, 206, 194)) for i in range(5)],
        c.rrect((36, 470, 404, 590), 14, outline=GOLD_D, width=4),
        c.text((220, 506), "RETURN BY", FONT_SANS, 28, GOLD_D, track=4))), 1590, 540, mode="right", amp=3)
    if t > tr + 0.3:
        # calligrafia: la penna scrive la data sulla riga RETURN BY
        p = ease(seg(t, tr + 0.3, 1.6))
        d = ImageDraw.Draw(img)
        pts = []
        N = int(60 * p)
        for k in range(N + 1):
            u = k / 60.0
            x = 1440 + 300 * u
            y = 772 + 14 * math.sin(u * 40) * (0.5 + 0.5 * math.sin(u * 9)) - 6 * u
            pts.append((x, y))
        if len(pts) > 1:
            d.line(pts, fill=INK, width=5, joint="curve")
        if p < 1 and pts:
            put(img, mk(("pen18", 1), 90, 90, lambda c: (c.line([(70, 20), (30, 70)], GOLD_D, 14), c.poly([(24, 64), (38, 78), (20, 86)], fill=INK)), blur=5, dy=3), pts[-1][0] + 26, pts[-1][1] - 26)
    show(img, t, T(b, "dates on that store's own page"), flag10("FROM THE STORE'S OWN PAGE", None, GOLD, GREEN_D), 1590, 905, mode="up", amp=2)
    S(img, t, b, "Target and Costco give you", pill9("TARGET AND COSTCO: A LIMITED NUMBER OF DAYS", 820, 52, fill=SAGE, size=21), 560, 960, mode="up", amp=2)
    S(img, t, b, "Walmart does not match", pill9("WALMART: NO MATCH ON WALMART.COM BLACK FRIDAY DEALS", 880, 52, fill=CORAL, ink=IVORY, size=19), 1440, 960, mode="up", amp=2)

# ============================================================ 19
def draw19(img, t):
    b = 19
    head10(img, t, "ONE HONEST NOTE", None, "PAGES CAN CHANGE")
    S(img, t, b, "These pages can change", tile("pc19", 300, 300, ic_hourglass, "PAGES CAN\nCHANGE", None, CORAL, 1.0, 23, 16), 250, 360, mode="up", amp=4)
    S(img, t, b, "early November", tile("en19", 300, 300, lambda c, x, y, s: ic_calendar(c, x, y, s, GOLD, "NOV"), "READ IN EARLY\nNOVEMBER", None, GOLD, 1.0, 20, 16), 590, 360, mode="up", amp=4, ph=1)
    S(img, t, b, "price match page is dated", tile("pm19", 300, 300, ic_doc, "WALMART PRICE\nMATCH PAGE: 2023", None, GOLD, 1.0, 19, 16), 930, 360, mode="up", amp=4, ph=2)
    S(img, t, b, "check your store", dossier("ck19", 1020, 130, "CHECK YOUR STORE OR ITS WEBSITE", [("BEFORE YOU RELY ON ANY DETAIL", INK)], OKG, 26, 28, ic_storefront), 590, 610, mode="left", amp=3)
    S(img, t, b, "If you know someone", tile("sh19", 300, 290, ic_share, "SEND IT TO\nSOMEONE", "WHO SHOPS THE SALES", GOLD, 1.0, 22, 15, dark=True), 250, 850, mode="up", amp=4)
    S(img, t, b, "Tell me in the comments", say9("cm19", 700, 150, ["\"WHICH OF THESE RULES", "DID YOU NOT KNOW?\""], 36, tail="bl"), 850, 840, mode="up", amp=3)
    S(img, t, b, "like the video", strip10("lk19", 560, 110, "LIKE THE VIDEO", fill=(40, 100, 64), border=OKG, size=34, icon=ic_thumb, bold=True), 1560, 330, mode="right", amp=3)
    S(img, t, b, "subscribe to The Senior Advantage", strip10("sb19", 560, 110, "SUBSCRIBE", fill=(70, 56, 24), border=GOLD, size=34, icon=ic_bell, bold=True), 1560, 470, mode="right", amp=3)
    S(img, t, b, "subscribe to The Senior Advantage", pill9("THE SENIOR ADVANTAGE", 560, 60, fill=GOLD, size=26), 1560, 570, mode="up", amp=2, dt=0.2)
    S(img, t, b, "don't miss the next one", dossier("nx19", 560, 160, "SO YOU DON'T MISS", [("THE NEXT ONE", INK)], GOLD, 26, 34, ic_bell_dark), 1560, 760, mode="up", amp=3)

def ic_bell_dark(c, cx, cy, s):
    ic_bell(c, cx, cy, s * 1.1, GOLD_D)

# ============================================================ 20
DLINES = [("Return windows", "Return windows, price match rules", INK), ("and dates change", "and dates change, and they can", INK), ("they can differ", "differ by store and by item.", INK),
          ("Always confirm", "Always confirm with the official source", (150, 100, 20)), ("before you rely", "before you rely on them.", (150, 100, 20)),
          ("general information", "General information,", (70, 100, 84)), ("not financial advice", "not financial advice.", (70, 100, 84)),
          ("not affiliated", "This channel is not affiliated with Walmart,", INK), ("Costco or any", "Target, Costco or any government agency.", INK)]

def draw20(img, t):
    b = 20
    te = DUR[b] / FPS - 20.0          # schermata finale di YouTube = ultimi 20 secondi: il riquadro compare li, non prima
    ap(img, t, 0.3, txt("BEFORE", 120, IVORY, 6), 470, 400, pop_=False, dy=30, dur=0.6, t_out=te - 0.4)
    ap(img, t, 0.5, txt("YOU GO", 120, GOLD, 6), 470, 540, pop_=False, dy=30, dur=0.6, t_out=te - 0.4)
    ap(img, t, te, endbox(), 470, 470, pop_=False, dur=0.4)
    ap(img, t, te + 0.1, txt("WATCH NEXT", 54, GOLD, 3), 470, 780, pop_=False, dur=0.4)
    ap(img, t, 0.2, disc_panel(), 1380, 500, pop_=False, dy=40, dur=0.6, shadow=14)
    for i, (key, s_, col) in enumerate(DLINES):
        ap(img, t, T(b, key) if i else 0.6, tspr(s_, FONT_SANS_M, 32, col), 1380, 350 + i * 50, pop_=False, dy=14, dur=0.5)
    ap(img, t, LAST(b), txt("THANKS FOR WATCHING", 40, IVORY, 4), 960, 950)
