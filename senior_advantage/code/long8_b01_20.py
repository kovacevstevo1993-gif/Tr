"""Video lungo 8 (WALMART OVER 60) - blocchi 1-20. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-WALMART.md (versione finale).
Durate dalla timeline dell'utente (23/10/2026, fine di ogni blocco: 888, 1817, 2726, 3643, 4562, 5563, 6562, 7587, 8489, 9369,
10344, 11198, 12106, 13060, 13978, 14939, 15855, 16799, 17710, 18626).
Uso: OUT=cartella python3 long8_b01_20.py <blocco>      anteprima: python3 long8_b01_20.py frame <blocco> <secondi> <file.png>"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long8_kit import *

ENDS = [888, 1817, 2726, 3643, 4562, 5563, 6562, 7587, 8489, 9369, 10344, 11198, 12106, 13060, 13978, 14939, 15855, 16799, 17710, 18626]
for _i, _e in enumerate(ENDS):
    DUR[_i + 1] = _e - (ENDS[_i - 1] if _i else 0)

def A(img, t, b, key, spr, x, y, n=1, **kw):
    return ap(img, t, T(b, key, n), spr, x, y, **kw)

# ============================================================ BLOCCO 1 - la domanda alla cassa
def register_scene():
    def fn(c):
        w, h = 640, 420
        c.rrect((0, 250, w, h), 18, fill=(150, 106, 70))            # bancone
        c.rrect((0, 236, w, 262), 10, fill=(176, 128, 88))
        c.rrect((0, 300, w, 312), 2, fill=(120, 82, 52))
        ic_register(c, 210, 190, 1.9)
        # cassiera
        c.ell((430, 70, 520, 160), fill=SKIN)
        c.d.pieslice(c._b((424, 56, 526, 150)), 180, 360, fill=(120, 80, 50))
        c.rrect((404, 158, 546, 250), 34, fill=(70, 120, 180))
        c.rrect((448, 170, 502, 196), 6, fill=PAPER)
        # cliente anziano di spalle
        c.ell((540, 120, 620, 200), fill=HAIR)
        c.rrect((520, 196, 640, 300), 30, fill=(190, 140, 66))
    return sprite("reg8", 640, 420, fn)

def search_win():
    def fn(c):
        w, h = 760, 420
        c.rrect((3, 3, w - 3, h - 3), 24, fill=PAPER, outline=SAGE_D, width=5)
        c.rrect((3, 3, w - 3, 70), 24, fill=(200, 214, 204)); c.d.rectangle(c._b((3, 50, w - 3, 70)), fill=(200, 214, 204))
        for k in range(3):
            c.ell((26 + k * 30, 26, 44 + k * 30, 44), fill=(150, 150, 146))
        c.rrect((40, 110, w - 40, 190), 40, fill=IVORY, outline=(170, 166, 154), width=4)
        magnifier(c, 92, 148, 18, (110, 110, 106), 6)
        c.text((140, 150), "senior discount", FONT_SANS_M, 40, INK, anchor="lm")
        for k in range(3):
            c.rrect((60, 240 + k * 50, w - 120 - k * 90, 266 + k * 50), 8, fill=(222, 226, 220))
    return sprite("srch8", 760, 420, fn)

def ten_receipt():
    def fn(c):
        w, h = 520, 560
        c.rrect((0, 10, w, h), 10, fill=PAPER)
        for k in range(0, w, 26):
            c.poly([(k, 12), (k + 13, 0), (k + 26, 12)], fill=PAPER)
            c.poly([(k, h - 2), (k + 13, h + 12), (k + 26, h - 2)], fill=PAPER)
        c.text((w / 2, 74), "10 THINGS", FONT_SANS, 64, INK, track=4)
        c.text((w / 2, 132), "IF YOU KNOW HOW TO ASK", FONT_SANS, 26, (170, 120, 30), track=3)
        for i in range(10):
            y = 180 + i * 34
            c.text((40, y), "#%d" % (i + 1), FONT_SANS, 24, INK, anchor="lm")
            c.rrect((100, y - 7, 340 - (i % 3) * 50, y + 7), 6, fill=(206, 202, 190))
            c.text((w - 40, y), "ASK", FONT_SANS, 22, OKG if i % 2 == 0 else SAGE_D, anchor="rm", track=2)
    return sprite("ten8", 520, 572, fn)

def draw1(img, t):
    b = 1
    head(img, t, 0, "THE QUESTION AT THE REGISTER")
    ap(img, t, 0.2, register_scene(), 380, 700, pop_=False, dx=-80, dur=0.7, shadow=14)
    A(img, t, b, "Do you", bubble("q1", 620, 170, ["DO YOU HAVE A", "SENIOR DISCOUNT?"], 46), 400, 290, shadow=10)
    A(img, t, b, "Maybe", chip("AT THE REGISTER", 420, 62, fill=IVORY), 380, 960, shadow=6)
    tw_ = T(b, "But that's")
    A(img, t, b, "I searched", search_win(), 1340, 420, pop_=False, dx=80, dur=0.6, shadow=12, t_out=tw_ + 0.6)
    A(img, t, b, "couldn't find", stamp("NOT FOUND", 420, 120, CORAL, 52), 1380, 520, rot=-6, shadow=8, t_out=tw_ + 0.6)
    A(img, t, b, "wrong question", chip("THE WRONG QUESTION", 520, 70, fill=CORAL, ink=IVORY), 400, 455, shadow=8)
    A(img, t, b, "ten things", ten_receipt(), 1180, 560, pop_=False, dy=60, dur=0.6, shadow=14)
    A(img, t, b, "worth more", shelf_tag("worth", 380, 230, "WORTH", "MORE THAN A DISCOUNT", big_size=70), 1680, 470, rot=5, shadow=10)
    t0 = LAST(b)
    for k, (ic, lab) in enumerate(((lambda c, x, y: ic_register(c, x, y, 0.55), "COUNTERS"), (lambda c, x, y: ic_web(c, x, y, 0.55), "PAGES"), (lambda c, x, y: ic_idcard(c, x, y, 0.5), "PROGRAMS"))):
        ap(img, t, t0 + k * 0.12, label_card(("sp1", lab), 320, 110, ic, lab, None, col=GOLD, tsize=30), [1020, 1360, 1700][k], 940, pop_=False, dy=40, dur=0.45, shadow=8)

# ============================================================ BLOCCO 2 - la mappa dei dieci
def road_spr():
    def fn(c):
        w, h = 1800, 200
        c.rrect((0, 80, w, 120), 20, fill=(60, 70, 80))
        for k in range(0, w, 70):
            c.rrect((k + 10, 97, k + 44, 103), 2, fill=GOLD)
    return sprite("road8", 1800, 200, fn)

STOP_X = [150 + i * 180 for i in range(10)]

def draw2(img, t):
    b = 2
    head(img, t, 0, "WHAT'S COMING: ALL TEN")
    ap(img, t, 0.2, road_spr(), 960, 610, pop_=False, dx=-100, dur=0.7)
    t_all = T(b, "All ten")
    for i in range(10):
        ap(img, t, t_all + i * 0.08, numdisc(i + 1, 100, fill=PANEL_FILL, ink=IVORY), STOP_X[i], 610, shadow=6)
    # 1: regola alla cassa
    t1 = T(b, "a rule at the checkout")
    ap(img, t, t1, numdisc(1, 100), STOP_X[0], 610)
    ap(img, t, t1 + 0.2, label_card("c2a", 440, 150, lambda c, x, y: ic_register(c, x, y, 0.5), "AT CHECKOUT", "SPEAK UP", col=GOLD, tsize=36), 300, 390, pop_=False, dy=40, shadow=10)
    # 2: scadenza di stagione
    t2 = T(b, "a deadline")
    ap(img, t, t2, numdisc(2, 100), STOP_X[1], 610)
    ap(img, t, t2 + 0.2, label_card("c2b", 440, 150, lambda c, x, y: ic_calendar(c, x, y, 0.5), "A DEADLINE", "THIS SEASON", col=GOLD, tsize=36), 520, 830, pop_=False, dy=-40, shadow=10)
    # 6-7-8: un pacchetto a meta prezzo
    t3 = T(b, "Three of them")
    for k in (5, 6, 7):
        ap(img, t, t3 + (k - 5) * 0.1, numdisc(k + 1, 100), STOP_X[k], 610)
    if t >= t3 + 0.3:
        p = ease(seg(t, t3 + 0.3, 0.5)); d = ImageDraw.Draw(img)
        x0, x1 = STOP_X[5] - 60, STOP_X[7] + 60
        d.rounded_rectangle([x0, 540, x0 + (x1 - x0) * p, 680], radius=30, outline=GOLD, width=6)
    ap(img, t, T(b, "one package"), label_card("c2c", 470, 150, lambda c, x, y: ic_box8(c, x, y, 0.55), "ONE PACKAGE", "HALF THE PRICE", col=GOLD, tsize=38), STOP_X[6], 390, pop_=False, dy=40, shadow=10)
    # 9-10: medicina, venti anni
    t4 = T(b, "numbers nine and ten")
    for k in (8, 9):
        ap(img, t, t4 + (k - 8) * 0.1, numdisc(k + 1, 100), STOP_X[k], 610)
    ap(img, t, t4 + 0.2, label_card("c2d", 600, 150, lambda c, x, y: ic_bottle(c, x, y, 0.6), "YOUR MEDICINE", "A PROGRAM FROM 20 YEARS AGO", col=GOLD, tsize=38, ssize=26), 1500, 830, pop_=False, dy=-40, shadow=10)
    ap(img, t, LAST(b), chip("IF YOU TAKE MEDICINE EVERY MONTH", 760, 70, fill=GOLD), 960, 1000, shadow=8)

# ============================================================ BLOCCO 3 - due obiezioni
def draw3(img, t):
    b = 3
    head(img, t, 0, "TWO THINGS YOU MIGHT BE THINKING")
    # sinistra: niente app
    A(img, t, b, "I don't use apps", bubble("o1", 760, 150, ["\"I DON'T USE APPS\""], 52, tail="bl"), 520, 270, shadow=10)
    A(img, t, b, "I don't use apps", sprite("noapp", 220, 220, lambda c: (ic_phone_app(c, 110, 110, 1.3), ic_x(c, 110, 110, 1.0, CORAL, 22))), 240, 520, shadow=8)
    A(img, t, b, "register", label_card("o1a", 560, 120, lambda c, x, y: ic_register(c, x, y, 0.5), "AT THE REGISTER", None, col=OKG), 640, 470, pop_=False, dx=-60, shadow=8)
    A(img, t, b, "pharmacy counter", label_card("o1b", 560, 120, lambda c, x, y: ic_bottle(c, x, y, 0.55), "AT THE PHARMACY", None, col=OKG), 640, 610, pop_=False, dx=-60, shadow=8)
    A(img, t, b, "no phone", chip("NO PHONE NEEDED", 440, 70, fill=OKG), 520, 735, shadow=6)
    # destra: non compro molto da Walmart
    A(img, t, b, "Others are thinking", bubble("o2", 760, 150, ["\"I DON'T SHOP AT", "WALMART THAT MUCH\""], 44, tail="br"), 1400, 270, shadow=10)
    A(img, t, b, "Stay too", label_card("o2a", 640, 150, lambda c, x, y: ic_bottle(c, x, y, 0.65), "THE PHARMACY PART", "EVEN IF YOU SHOP ELSEWHERE", col=GOLD, ssize=26), 1400, 540, pop_=False, dx=60, shadow=8)
    # sotto: numero sei
    t6 = T(b, "number six")
    ap(img, t, t6, numdisc(6, 130), 560, 920, shadow=8)
    ap(img, t, t6 + 0.2, chip("PAY CLOSE ATTENTION", 470, 70, fill=IVORY), 880, 920, shadow=6)
    tl = LAST(b)
    for k, lab in enumerate(("SNAP", "MEDICAID", "SSI")):
        ap(img, t, tl + k * 0.12, chip(lab, 230, 70, fill=GOLD), 1260 + k * 250, 920, shadow=6)

# ============================================================ BLOCCO 4 - le fonti
def draw4(img, t):
    b = 4
    head(img, t, 0, "WHERE EVERYTHING COMES FROM")
    docs = [("policy page", "POLICY PAGE", lambda c, x, y: ic_doc(c, x, y, 0.8)),
            ("news releases", "NEWS RELEASES", lambda c, x, y: ic_doc(c, x, y, 0.8, col=(236, 242, 236))),
            ("price guide", "PRICE GUIDE", lambda c, x, y: ic_bottle(c, x, y, 0.8)),
            ("check eligibility", "ELIGIBILITY CHECK", lambda c, x, y: ic_idcard(c, x, y, 0.6))]
    for k, (key, lab, ic) in enumerate(docs):
        A(img, t, b, key, card(("src4", lab), 370, 300, ic, ["WALMART", lab], GOLD, 30, ih=0.5, ink=SAGE, ink2=IVORY), 230 + k * 400, 330, shadow=12)
    A(img, t, b, "For snap", sprite("usda8", 200, 200, lambda c: ic_seal(c, 100, 100, 1.4)), 1760, 330, shadow=10)
    A(img, t, b, "For snap", chip("SNAP: USDA", 260, 60, fill=IVORY), 1760, 470, shadow=6)
    A(img, t, b, "exceptions", label_card("ex4", 760, 130, lambda c, x, y: ic_warn(c, x, y, 0.7), "EXCEPTIONS: I'LL TELL YOU", None, col=OKG), 520, 640, pop_=False, dx=-60, shadow=8)
    A(img, t, b, "your state or your plan", label_card("st4", 760, 130, lambda c, x, y: ic_pin8(c, x, y + 10, 1.2), "DEPENDS ON STATE OR PLAN", None, col=OKG), 520, 800, pop_=False, dx=-60, shadow=8)
    A(img, t, b, "could not confirm", receipt("rum4", 620, 300, "OTHER VIDEOS", [("UNCONFIRMED CLAIMS", "OUT")], size=34), 1380, 720, pop_=False, dx=60, shadow=12)
    ap(img, t, LAST(b), stamp("NOT IN THIS VIDEO", 500, 110, CORAL, 40), 1380, 930, rot=-5, shadow=8)

# ============================================================ BLOCCO 5 - #1 Walmart si allinea al proprio sito
def compare_bars():
    def fn(c):
        w, h = 760, 380
        c.rrect((0, 0, w, h), 26, fill=PANEL_FILL, outline=SAGE_D, width=5)
        c.text((40, 70), "IN THE STORE", FONT_SANS, 34, IVORY, anchor="lm", track=3)
        c.rrect((40, 100, 700, 160), 14, fill=CORAL)
        c.text((40, 230), "ON WALMART.COM", FONT_SANS, 34, IVORY, anchor="lm", track=3)
        c.rrect((40, 260, 470, 320), 14, fill=OKG)
        c.text((500, 290), "CHEAPER", FONT_SANS, 34, OKG, anchor="lm", track=3)
    return sprite("cmp5", 760, 380, fn)

def draw5(img, t):
    b = 5
    head(img, t, 1, "WALMART WILL MATCH ITS OWN WEBSITE")
    A(img, t, b, "If you're in a Walmart store", sprite("store5", 300, 240, lambda c: ic_storefront(c, 150, 130, 1.8)), 230, 330, shadow=10)
    A(img, t, b, "exact same item", compare_bars(), 760, 380, pop_=False, dx=-60, shadow=12)
    A(img, t, b, "will match that price", stamp("STORE MATCHES IT", 470, 110, GOLD, 40), 1500, 300, rot=-4, shadow=8)
    for k, w_ in enumerate(("SIZE", "BRAND", "MODEL", "COLOR")):
        A(img, t, b, ["Same size", "same brand", "same model", "same color"][k], shelf_tag(("same", w_), 230, 150, w_, "SAME", big_size=40), 1270 + (k % 2) * 260, 500 + (k // 2) * 190, shadow=8)
    A(img, t, b, "in stock", chip("IT HAS TO BE IN STOCK", 460, 70, fill=OKG), 1400, 860, shadow=6)
    A(img, t, b, "You have to tell", bubble("tell5", 820, 160, ["TELL THE CASHIER THE PRICE", "WHEN YOU CHECK OUT"], 42), 620, 760, shadow=12)
    A(img, t, b, "You have to tell", sprite("reg5", 220, 200, lambda c: ic_register(c, 110, 110, 1.4)), 170, 900, shadow=8)
    ap(img, t, LAST(b), chip("THAT STEP IS ON YOU", 520, 76, fill=GOLD), 1400, 975, shadow=8)

# ============================================================ BLOCCO 6 - le eccezioni
def draw6(img, t):
    b = 6
    head(img, t, 1, "THE FINE PRINT: WHEN IT CAN BE REFUSED")
    rows = [("other stores", "OTHER STORES", "TARGET, ALDI..."), ("clearance", "CLEARANCE OR ROLLBACK", "WEBSITE PRICES"),
            ("other sellers", "OTHER SELLERS", "ON WALMART.COM"), ("different Walmart", "ANOTHER WALMART", "ACROSS TOWN")]
    for k, (key, a, s_) in enumerate(rows):
        y = 280 + k * 165
        A(img, t, b, key, label_card(("no6", a), 860, 140, lambda c, x, y_: ic_x(c, x, y_, 0.8, CORAL, 16), a, s_, col=CORAL, tsize=40, ssize=28), 520, y, pop_=False, dx=-70, shadow=8)
        ap(img, t, T(b, key) + 0.3, chip("NO MATCH", 240, 60, fill=CORAL, ink=IVORY), 1060, y, shadow=6)
    ap(img, t, T(b, "only items sold by Walmart"), chip("ONLY SOLD BY WALMART", 470, 64, fill=OKG), 1500, 610, shadow=6)
    tb = T(b, "So before you go")
    steps = [("look up the item", "LOOK UP THE ITEM", lambda c, x, y: magnifier(c, x - 6, y - 6, 22, GOLD, 7)),
             ("check who sells it", "CHECK WHO SELLS IT", lambda c, x, y: ic_storefront(c, x, y, 0.5)),
             ("ready to show", "HAVE THE PRICE READY", lambda c, x, y: ic_phone_app(c, x, y, 0.55))]
    ap(img, t, tb, receipt("bef6", 560, 560, "BEFORE YOU GO", [], size=34), 1530, 500, pop_=False, dx=70, shadow=12, t_out=None)
    for k, (key, lab, ic) in enumerate(steps):
        tk = T(b, key) if k < 2 else LAST(b)
        ap(img, t, tk, label_card(("st6", lab), 480, 110, ic, lab, None, col=GOLD, tsize=30), 1530, 400 + k * 135, pop_=False, dx=40, shadow=6)

# ============================================================ BLOCCO 7 - #2 resi: la regola delle feste
def months_spr():
    def fn(c):
        w, h = 1640, 300
        names = ["OCT", "NOV", "DEC", "JAN"]
        for k, n in enumerate(names):
            x = 20 + k * 400
            fill = GOLD if k < 3 else PAPER
            c.rrect((x, 40, x + 380, 260), 22, fill=fill, outline=IVORY, width=4)
            c.text((x + 190, 110), n, FONT_SANS, 72, GREEN_D if k < 3 else INK, track=6)
        c.text((20 + 190, 210), "OCT 1", FONT_SANS, 36, GREEN_D)
        c.text((20 + 2 * 400 + 190, 210), "DEC 31", FONT_SANS, 36, GREEN_D)
        c.text((20 + 3 * 400 + 190, 210), "JAN 31", FONT_SANS, 36, CORAL)
    return sprite("mon7", 1640, 300, fn)

def draw7(img, t):
    b = 7
    head(img, t, 2, "MORE TIME TO CHANGE YOUR MIND")
    A(img, t, b, "ninety days", shelf_tag("90d", 380, 230, "90 DAYS", "MOST ITEMS"), 300, 330, shadow=10)
    A(img, t, b, "much less time", shelf_tag("less", 380, 230, "LESS", "SOME THINGS", col=CORAL, ink=IVORY), 760, 330, shadow=10)
    A(img, t, b, "holiday rule", chip("THE HOLIDAY RULE", 520, 76, fill=IVORY), 1420, 255, shadow=8)
    tb = T(b, "Most items bought between")
    ap(img, t, tb, months_spr(), 960, 590, pop_=False, dy=50, dur=0.6, shadow=12)
    ap(img, t, T(b, "until January"), chip("RETURN UNTIL JAN 31", 480, 70, fill=CORAL, ink=IVORY), 1420, 360, shadow=6)
    A(img, t, b, "even a gift", sprite("gift7", 200, 200, lambda c: ic_gift(c, 100, 110, 1.4)), 260, 880, shadow=10)
    A(img, t, b, "even a gift", label_card("g7", 760, 130, lambda c, x, y: ic_calendar(c, x, y, 0.45), "SHORT WINDOW? STILL COVERED", "UNTIL THE HOLIDAYS ARE OVER", col=GOLD, tsize=34, ssize=26), 760, 880, pop_=False, dx=-50, shadow=8)
    ap(img, t, LAST(b), stamp("WALMART RETURN POLICY", 560, 110, GOLD, 34), 1520, 880, rot=-3, shadow=8)

# ============================================================ BLOCCO 8 - le finestre piu corte
def hbar(key, frac, col, w=900, h=78):
    return sprite(("hb8", key), w, h, lambda c: c.rrect((0, 0, max(30, w * frac), h), h / 2, fill=col))

def draw8(img, t):
    b = 8
    head(img, t, 2, "THE SHORTER WINDOWS")
    rows = [("wireless phones", "PHONES", 14, CORAL), ("Electronics", "ELECTRONICS, VACUUMS, HEATING", 30, GOLD),
            ("Prescription glasses", "GLASSES, CONTACTS, HEARING AIDS", 60, SAGE), ("Major appliances", "MAJOR APPLIANCES", 2, CORAL)]
    for k, (key, lab, days, col) in enumerate(rows):
        y = 270 + k * 145; tk = T(b, key)
        ap(img, t, tk, txt(lab, 34, IVORY, 3), 60 + tw(lab, 34, 3) / 2 + 30, y - 46, pop_=False, dx=-40)
        if t >= tk:
            grow(img, t, tk + 0.1, hbar(lab, days / 90.0, col), 60 + 450, y + 10)
            ap(img, t, tk + 0.4, txt("%d DAYS" % days, 44, col, 2), 60 + 900 * max(30 / 900, days / 90.0) + 130, y + 10)
    A(img, t, b, "may not get the holiday extension", receipt("exc8", 620, 440, "MAY NOT GET THE EXTENSION", ["PHONES", "PROTECTION PLANS", "DYSON PRODUCTS", "SOME SEASONAL & LUXURY"], size=34, title_size=34), 1520, 420, pop_=False, dx=70, shadow=12)
    A(img, t, b, "heater", sprite("heat8", 200, 200, lambda c: ic_heater(c, 100, 100, 1.4)), 1150, 870, shadow=10)
    ap(img, t, LAST(b), label_card("heat8b", 560, 130, lambda c, x, y: ic_receipt(c, x, y, 0.8), "CHECK THE RECEIPT", "HEATING: 30 DAYS, NOT 90", col=GOLD, tsize=34, ssize=28), 1540, 870, pop_=False, dx=50, shadow=8)

# ============================================================ BLOCCO 9 - scontrino perso
def draw9(img, t):
    b = 9
    head(img, t, 2, "LOST THE RECEIPT?")
    A(img, t, b, "lost the receipt", sprite("rc9", 240, 260, lambda c: (ic_receipt(c, 120, 130, 1.8), ic_x(c, 120, 130, 1.0, CORAL, 20))), 240, 340, shadow=10)
    A(img, t, b, "don't give up", chip("DON'T GIVE UP", 360, 66, fill=GOLD), 240, 520, shadow=6)
    A(img, t, b, "purchases made in the store", label_card("st9", 840, 170, lambda c, x, y: ic_card(c, x, y, 0.75), "IN THE STORE", "LOOK UP WITH YOUR DEBIT OR CREDIT CARD", col=GOLD, tsize=40, ssize=28), 900, 290, pop_=False, dx=60, shadow=10)
    A(img, t, b, "online orders", label_card("on9", 840, 170, lambda c, x, y: ic_envelope(c, x, y, 0.75), "ONLINE ORDERS", "PHONE NUMBER OR EMAIL", col=GOLD, tsize=40, ssize=28), 900, 480, pop_=False, dx=60, shadow=10)
    A(img, t, b, "service desk", sprite("desk9", 240, 220, lambda c: ic_register(c, 120, 120, 1.5)), 1620, 380, shadow=8)
    A(img, t, b, "I don't have", bubble("say9", 1100, 200, ["\"I DON'T HAVE THE RECEIPT,", "CAN YOU LOOK IT UP WITH MY CARD?\""], 46, tail="br"), 1150, 710, shadow=12)
    A(img, t, b, "pay cash", sprite("cash9", 200, 160, lambda c: (c.rrect((20, 30, 180, 130), 12, fill=OKG, outline=IVORY, width=4), c.text((100, 80), "$", FONT_SANS, 60, GREEN_D))), 200, 930, shadow=8)
    ap(img, t, LAST(b), label_card("keep9", 760, 130, lambda c, x, y: ic_envelope(c, x, y, 0.7), "PAY CASH? KEEP RECEIPTS TOGETHER", None, col=OKG, tsize=34), 720, 930, pop_=False, dx=-50, shadow=8)

# ============================================================ BLOCCO 10 - #3 ritiro gratis al marciapiede
def draw10(img, t):
    b = 10
    head(img, t, 3, "FREE PICKUP AT THE CURB")
    steps = [("Walmart app", "ORDER", "APP OR WALMART.COM", lambda c, x, y: ic_phone_app(c, x, y, 0.75)),
             ("reserve the time", "RESERVE", "TIME AND STORE", lambda c, x, y: ic_clock(c, x, y, 50, 1.2)),
             ("drive up", "DRIVE UP", "COLLECT AT THE CURB", lambda c, x, y: ic_car(c, x, y + 6, 1.2))]
    for k, (key, a, s_, ic) in enumerate(steps):
        x = 330 + k * 630
        A(img, t, b, key, card(("pk10", a), 440, 340, ic, [a, s_], GOLD, 40, ih=0.5, ink=IVORY, ink2=GOLD), x, 400, shadow=12)
        if k < 2:
            A(img, t, b, steps[k + 1][0], arrow_spr(150, 56), x + 315, 400, pop_=False, dx=-30)
    A(img, t, b, "without going inside", chip("NO NEED TO GO INSIDE", 520, 70, fill=OKG), 1590, 620, shadow=6)
    A(img, t, b, "this pickup is free", shelf_tag("free10", 420, 240, "FREE", "WALMART HAS SAID"), 360, 830, rot=-4, shadow=10)
    A(img, t, b, "thirty five dollar order minimum", shelf_tag("min10", 420, 240, "$35", "ORDER MINIMUM", col=PAPER, ink=INK), 860, 830, rot=3, shadow=10)
    A(img, t, b, "plan your order", label_card("plan10", 620, 130, lambda c, x, y: ic_cart2(c, x, y, 0.6), "PLAN TO REACH $35", None, col=GOLD, tsize=36), 1500, 790, pop_=False, dx=50, shadow=8)
    ap(img, t, LAST(b), label_card("heavy10", 620, 130, lambda c, x, y: ic_water(c, x, y, 0.6), "ADD THE HEAVY THINGS", "YOU NEED ANYWAY", col=GOLD, tsize=34, ssize=28), 1500, 950, pop_=False, dx=50, shadow=8)

# ============================================================ BLOCCO 11 - perche conta dopo i 60
def draw11(img, t):
    b = 11
    head(img, t, 3, "WHY IT MATTERS AFTER SIXTY")
    items = [("the walking", "THE WALKING", lambda c, x, y: ic_person(c, x, y + 4, 0.9, GOLD)), ("heavy cart", "THE HEAVY CART", lambda c, x, y: ic_cart2(c, x, y, 0.6)),
             ("cases of water", "CASES OF WATER", lambda c, x, y: ic_water(c, x, y, 0.6)), ("bags in the rain", "BAGS IN THE RAIN", lambda c, x, y: ic_rain(c, x, y, 0.6))]
    tskip = T(b, "skip all of that")
    for k, (key, lab, ic) in enumerate(items):
        x = 260 + k * 466
        A(img, t, b, key, card(("w11", lab), 400, 280, ic, [lab], CORAL, 34, ih=0.55), x, 330, shadow=10)
        ap(img, t, tskip + k * 0.12, xmark_spr(90), x + 150, 230, shadow=6)
    ap(img, t, tskip, chip("CURBSIDE PICKUP: SKIP ALL OF THAT", 760, 74, fill=OKG), 960, 530, shadow=8)
    A(img, t, b, "icy days", label_card("ice11", 820, 150, lambda c, x, y: ic_ice(c, x, y, 0.65), "ICY DAYS THIS WINTER", "FEWER STEPS ON A SLIPPERY LOT", col=GOLD, tsize=38, ssize=28), 500, 720, pop_=False, dx=-60, shadow=10)
    A(img, t, b, "someone in your family", label_card("fam11", 820, 150, lambda c, x, y: ic_couple(c, x, y + 6, 0.8), "A BREAK FOR BOTH OF YOU", "IF FAMILY DRIVES YOU", col=GOLD, tsize=38, ssize=28), 500, 900, pop_=False, dx=-60, shadow=10)
    tl = LAST(b)
    ap(img, t, tl, numdisc(5, 170), 1300, 810, shadow=10)
    ap(img, t, tl + 0.15, bubble("snap11", 520, 150, ["GET SNAP?", "NUMBER FIVE IS NEXT"], 40, tail="bl"), 1640, 790, shadow=10)

# ============================================================ BLOCCO 12 - #4 il vaccino antinfluenzale
def map_dots():
    def fn(c):
        pts = [map_xy(lo, la) for lo, la in us_map()]
        c.poly(pts, fill=(34, 92, 72)); c.line(pts + [pts[0]], SAGE_D, 4)
        rnd = random.Random(8)
        for _ in range(140):
            lo, la = rnd.uniform(-122, -72), rnd.uniform(27, 47)
            x, y = map_xy(lo, la)
            c.ell((x - 4, y - 4, x + 4, y + 4), fill=GOLD)
    return sprite("mapd12", 560, 310, fn)

def draw12(img, t):
    b = 12
    head(img, t, 4, "A FLU SHOT, OFTEN AT NO CHARGE")
    A(img, t, b, "flu shot", sprite("syr12", 260, 260, lambda c: ic_syringe(c, 130, 130, 1.6)), 260, 380, shadow=10)
    A(img, t, b, "Walmart has said its flu shots", receipt("cost12", 760, 360, "WALMART HAS SAID", [("GIVEN BY", "PHARMACY STAFF"), ("OUT-OF-POCKET COST", "NONE"), ("ON", "MOST MAJOR PLANS")], size=34), 860, 400, pop_=False, dy=50, shadow=12)
    A(img, t, b, "book a time online", label_card("book12", 560, 130, lambda c, x, y: ic_calendar(c, x, y, 0.45), "BOOK ONLINE", None, col=GOLD), 1550, 300, pop_=False, dx=60, shadow=8)
    A(img, t, b, "walk ins", label_card("walk12", 560, 130, lambda c, x, y: ic_person(c, x, y + 4, 0.8, GOLD), "WALK-INS WELCOME", None, col=GOLD), 1550, 460, pop_=False, dx=60, shadow=8)
    A(img, t, b, "nearly four thousand", map_dots(), 420, 800, pop_=False, dy=40, shadow=10)
    A(img, t, b, "nearly four thousand", shelf_tag("4600", 460, 230, "4,600", "NEARLY: WALMART PHARMACIES"), 980, 800, shadow=10)
    ap(img, t, LAST(b), label_card("gro12", 560, 130, lambda c, x, y: ic_cart2(c, x, y, 0.55), "WHILE YOU SHOP", "FOR GROCERIES", col=OKG, tsize=36), 1540, 800, pop_=False, dx=50, shadow=8)

# ============================================================ BLOCCO 13 - la domanda prima dell'iniezione
def draw13(img, t):
    b = 13
    head(img, t, 4, "ASK ONE QUESTION FIRST")
    A(img, t, b, "Ask one question", sprite("q13", 220, 220, lambda c: ic_question(c, 110, 110, 1.9)), 200, 400, shadow=10)
    A(img, t, b, "Is this covered", bubble("q13b", 1100, 210, ["\"IS THIS COVERED BY MY PLAN?", "WILL I PAY ANYTHING TODAY?\""], 50), 900, 360, shadow=12)
    A(img, t, b, "Coverage depends", label_card("dep13", 700, 130, lambda c, x, y: ic_pin8(c, x, y + 10, 1.1), "DEPENDS ON PLAN AND VACCINE", None, col=GOLD, tsize=32), 480, 640, pop_=False, dx=-50, shadow=8)
    A(img, t, b, "before, not after", chip("ASK BEFORE, NOT AFTER", 520, 70, fill=GOLD), 480, 780, shadow=6)
    A(img, t, b, "insurance card", sprite("ins13", 440, 300, lambda c: (ic_card(c, 220, 150, 2.8, (90, 140, 120)), c.text((220, 92), "INSURANCE", FONT_SANS, 34, IVORY))), 1460, 620, shadow=10)
    A(img, t, b, "more than one vaccine", label_card("due13", 760, 150, lambda c, x, y: ic_syringe(c, x, y, 0.5), "MORE THAN ONE?", "WHICH ARE YOU DUE FOR?", col=GOLD, tsize=38, ssize=30), 1420, 870, pop_=False, dx=50, shadow=8)
    ap(img, t, LAST(b), stamp("NO SURPRISE BILL", 460, 110, OKG, 40), 480, 930, rot=-4, shadow=8)

# ============================================================ BLOCCO 14 - #5 snap online
def checkout_spr(sel):
    def fn(c):
        w, h = 520, 640
        c.rrect((0, 0, w, h), 50, fill=(30, 34, 40))
        c.rrect((22, 40, w - 22, h - 30), 26, fill=PAPER)
        c.text((w / 2, 100), "CHECKOUT", FONT_SANS, 40, INK, track=4)
        c.text((50, 170), "PAYMENT", FONT_SANS, 28, (120, 120, 116), anchor="lm", track=3)
        opts = ["CREDIT CARD", "EBT CARD", "GIFT CARD"]
        for k, o in enumerate(opts):
            y = 230 + k * 100
            on = sel and k == 1
            c.rrect((46, y - 36, w - 46, y + 36), 16, fill=(232, 244, 232) if on else IVORY, outline=OKG if on else (200, 200, 196), width=5 if on else 3)
            c.ell((70, y - 16, 102, y + 16), outline=OKG if on else (170, 170, 166), width=4)
            if on:
                c.ell((78, y - 8, 94, y + 8), fill=OKG)
            c.text((130, y), o, FONT_SANS, 30, INK, anchor="lm", track=2)
        c.rrect((60, h - 140, w - 60, h - 70), 20, fill=GOLD)
        c.text((w / 2, h - 105), "PLACE ORDER", FONT_SANS, 30, GREEN_D, track=3)
    return sprite(("co14", sel), 520, 640, fn)

def draw14(img, t):
    b = 14
    head(img, t, 5, "SNAP, WITHOUT GOING INSIDE")
    A(img, t, b, "U S D A says", sprite("usda14", 200, 200, lambda c: ic_seal(c, 100, 100, 1.4)), 200, 330, shadow=10)
    A(img, t, b, "all fifty states", shelf_tag("50", 360, 220, "50 STATES", "SNAP ONLINE"), 520, 330, shadow=10)
    A(img, t, b, "one of the first stores", label_card("first14", 640, 130, lambda c, x, y: ic_storefront(c, x, y, 0.5), "WALMART: ONE OF THE FIRST", None, col=GOLD, tsize=34), 400, 520, pop_=False, dx=-50, shadow=8)
    tp = T(b, "When you order")
    ap(img, t, tp, checkout_spr(False), 1060, 600, pop_=False, dy=60, dur=0.6, shadow=14)
    if t >= T(b, "E B T card option"):
        ap(img, t, T(b, "E B T card option"), checkout_spr(True), 1060, 600, pop_=False, dur=0.3)
    A(img, t, b, "for pickup", label_card("pu14", 460, 120, lambda c, x, y: ic_car(c, x, y + 6, 0.8), "PICKUP", None, col=OKG), 1590, 330, pop_=False, dx=50, shadow=8)
    A(img, t, b, "for delivery", label_card("de14", 460, 120, lambda c, x, y: ic_van(c, x, y, 0.6), "DELIVERY", "WHERE AVAILABLE", col=OKG), 1590, 470, pop_=False, dx=50, shadow=8)
    A(img, t, b, "pin number", sprite("kp14", 200, 220, lambda c: ic_keypad(c, 100, 110, 1.5)), 260, 820, shadow=10)
    A(img, t, b, "pin number", chip("ENTER YOUR PIN", 400, 66, fill=IVORY), 560, 820, shadow=6)
    ap(img, t, LAST(b), label_card("chk14", 460, 130, lambda c, x, y: ic_web(c, x, y, 0.5), "DELIVERY TO YOU?", "CHECK WALMART'S WEBSITE", col=GOLD, tsize=34, ssize=26), 1590, 760, pop_=False, dx=50, shadow=8)

# ============================================================ BLOCCO 15 - tre regole USDA
def draw15(img, t):
    b = 15
    head(img, t, 5, "THREE RULES AT CHECKOUT")
    A(img, t, b, "These come from", sprite("usda15", 200, 200, lambda c: ic_seal(c, 100, 100, 1.4)), 200, 300, shadow=10)
    A(img, t, b, "every store", chip("USDA RULES, EVERY STORE", 560, 70, fill=IVORY), 620, 300, shadow=6)
    rules = [("Only eligible food", "ELIGIBLE FOOD ONLY", OKG), ("Delivery fees", "NO DELIVERY OR SERVICE FEES", CORAL), ("the rest of your order", "PAY THE REST ANOTHER WAY", GOLD)]
    for k, (key, lab, col) in enumerate(rules):
        x = 330 + k * 630
        A(img, t, b, key, numdisc(k + 1, 120, fill=col), x, 470, shadow=8)
        A(img, t, b, key, panel(560, 210, border=col), x, 620, pop_=False, dy=40, shadow=10)
        A(img, t, b, key, fit(lab, 40, 500), x, 640, pop_=False, dy=40)
    A(img, t, b, "remember the thirty five", shelf_tag("35b", 420, 230, "$35", "MINIMUM FOR FREE PICKUP", col=PAPER, ink=INK), 600, 880, rot=-3, shadow=10)
    ap(img, t, LAST(b), label_card("card15", 760, 140, lambda c, x, y: ic_card(c, x, y, 0.65), "KEEP A SECOND CARD READY", "FOR WHAT SNAP DOESN'T COVER", col=GOLD, tsize=34, ssize=26), 1340, 890, pop_=False, dx=50, shadow=8)

# ============================================================ BLOCCO 16 - il pacchetto Walmart+
def package_spr():
    def fn(c):
        w, h = 760, 520
        c.poly([(80, 200), (380, 120), (680, 200), (380, 280)], fill=(226, 196, 140))
        c.poly([(80, 200), (380, 280), (380, 500), (80, 420)], fill=(190, 140, 86))
        c.poly([(680, 200), (380, 280), (380, 500), (680, 420)], fill=(160, 112, 66))
        c.poly([(80, 200), (20, 110), (330, 40), (380, 120)], fill=(236, 210, 160))
        c.poly([(680, 200), (740, 110), (430, 40), (380, 120)], fill=(236, 210, 160))
        c.rrect((180, 300, 330, 380), 14, fill=GOLD)
        c.text((255, 342), "PLUS", FONT_SANS, 34, GREEN_D, track=3)
    return sprite("pkg16", 760, 520, fn)

def draw16(img, t):
    b = 16
    head(img, t, 6, "NUMBERS SIX, SEVEN AND EIGHT: ONE PACKAGE")
    A(img, t, b, "one package", package_spr(), 520, 560, pop_=False, dy=60, dur=0.6, shadow=14)
    tn = T(b, "Now numbers six")
    for k in range(3):
        ap(img, t, tn + 0.2 + k * 0.15, numdisc(6 + k, 110), 400 + k * 130, 330, shadow=8)
    A(img, t, b, "called Walmart Plus", chip("WALMART PLUS", 400, 74, fill=IVORY), 520, 900, shadow=6)
    A(img, t, b, "ninety eight dollars", shelf_tag("98", 420, 250, "$98", "A YEAR: REGULAR PRICE", col=PAPER, ink=INK), 1200, 400, rot=-3, shadow=10)
    A(img, t, b, "If you don't use it much", label_card("nw16", 620, 140, lambda c, x, y: ic_x(c, x, y, 0.8, CORAL, 16), "NOT WORTH IT", "IF YOU DON'T USE IT MUCH", col=CORAL, tsize=38, ssize=28), 1450, 610, pop_=False, dx=50, shadow=8)
    A(img, t, b, "another version", label_card("ver16", 620, 140, lambda c, x, y: ic_box8(c, x, y, 0.45), "ANOTHER VERSION", "MUCH LOWER PRICE", col=GOLD, tsize=38, ssize=30), 1450, 770, pop_=False, dx=50, shadow=8)
    ap(img, t, LAST(b), label_card("math16", 620, 130, lambda c, x, y: c.text((x, y + 2), "=", FONT_SANS, 70, GOLD), "WE'LL DO THE MATH", None, col=GOLD, tsize=36), 1450, 930, pop_=False, dx=50, shadow=8)

# ============================================================ BLOCCO 17 - #6 Walmart+ Assist
def draw17(img, t):
    b = 17
    head(img, t, 6, "WALMART PLUS ASSIST")
    A(img, t, b, "fifty percent off", shelf_tag("98b", 360, 230, "$98", "REGULAR", col=PAPER, ink=INK), 230, 380, shadow=8)
    if t >= T(b, "fifty percent off") + 0.3:
        strike(img, t, T(b, "fifty percent off") + 0.3, 100, 360, 380)
    A(img, t, b, "fifty percent off", stamp("50% OFF", 320, 120, CORAL, 56), 230, 590, rot=-8, shadow=8)
    A(img, t, b, "Forty nine dollars", shelf_tag("49", 460, 300, "$49", "A YEAR"), 650, 430, shadow=12)
    A(img, t, b, "six dollars and forty seven", shelf_tag("647", 380, 240, "$6.47", "A MONTH"), 1090, 430, shadow=10)
    A(img, t, b, "Who can get it", label_card("who17", 600, 150, lambda c, x, y: ic_gov(c, x, y, 0.6), "WHO CAN GET IT?", "CERTAIN GOVERNMENT HELP", col=GOLD, tsize=38, ssize=28), 1580, 320, pop_=False, dx=-50, shadow=8)
    progs = [("snap, Medicaid", "SNAP"), ("Medicaid, S S I", "MEDICAID"), ("S S I, and", "SSI"), ("L I H E A P", "LIHEAP")]
    for k, (key, lab) in enumerate(progs):
        A(img, t, b, key, chip(lab, 270, 78, fill=GOLD), [1430, 1730, 1430, 1730][k], [500, 500, 600, 600][k], shadow=6)
    A(img, t, b, "plus a few others", chip("+ OTHERS FOR FAMILIES", 580, 70, fill=IVORY), 1580, 710, shadow=6)
    ap(img, t, LAST(b), label_card("list17", 960, 130, lambda c, x, y: ic_doc(c, x, y, 0.5), "FULL LIST ON THE SIGN-UP PAGE", "CHECK IT BEFORE YOU PAY FULL PRICE", col=GOLD, tsize=34, ssize=26), 960, 920, pop_=False, dy=40, shadow=8)

# ============================================================ BLOCCO 18 - come si ottiene
def draw18(img, t):
    b = 18
    head(img, t, 6, "HOW TO GET IT")
    steps = [("walmart dot com slash plus", "GO TO", "WALMART.COM/PLUS/ASSIST", lambda c, x, y: ic_web(c, x, y, 0.8)),
             ("Sheer I D", "VERIFY", "THROUGH SHEERID", lambda c, x, y: ic_idcard(c, x, y, 0.7)),
             ("sign up at the lower price", "SIGN UP", "AT THE LOWER PRICE", lambda c, x, y: c.text((x, y + 4), "$49", FONT_SANS, 56, GOLD))]
    for k, (key, a, s_, ic) in enumerate(steps):
        x = 330 + k * 630
        A(img, t, b, key, card(("h18", a), 460, 330, ic, [a, s_], GOLD, 34, ih=0.5, ink=IVORY, ink2=GOLD), x, 420, shadow=12)
        A(img, t, b, key, numdisc(k + 1, 96), x - 200, 270, shadow=6)
    ta = T(b, "already pay full price")
    ap(img, t, ta, receipt("sw18", 900, 400, "ALREADY PAYING FULL PRICE?", [("SWITCH", "IF YOU QUALIFY"), ("NEW PRICE", "RIGHT AWAY"), ("REFUND", "PRORATED")], size=36, title_size=40), 620, 820, pop_=False, dy=50, shadow=12)
    ap(img, t, LAST(b), stamp("WORTH CHECKING TODAY", 640, 120, GOLD, 36), 1480, 820, rot=-4, shadow=8)

# ============================================================ BLOCCO 19 - #7 consegna dei farmaci
def route_spr():
    def fn(c):
        w, h = 900, 380
        c.rrect((0, 0, w, h), 30, fill=PANEL_FILL, outline=SAGE_D, width=5)
        for k in range(0, w, 60):
            c.line([(k, 0), (k, h)], (20, 60, 46), 2)
        for k in range(0, h, 60):
            c.line([(0, k), (w, k)], (20, 60, 46), 2)
        pts = [(140, 290), (300, 290), (300, 160), (560, 160), (560, 250), (760, 250)]
        c.line(pts, GOLD, 10)
        ic_storefront(c, 140, 230, 0.8)
        ic_house(c, 770, 190, 0.9)
    return sprite("route19", 900, 380, fn)

def draw19(img, t):
    b = 19
    head(img, t, 7, "PRESCRIPTION DELIVERY")
    A(img, t, b, "Prescription delivery", route_spr(), 520, 400, pop_=False, dy=50, shadow=12)
    if t >= T(b, "Prescription delivery") + 0.4:
        p = ease(seg(t, T(b, "Prescription delivery") + 0.4, 2.0))
        pts = [(140, 290), (300, 290), (300, 160), (560, 160), (560, 250), (760, 250)]
        L = [math.dist(pts[i], pts[i + 1]) for i in range(5)]; d_ = p * sum(L); i = 0
        while i < 4 and d_ > L[i]:
            d_ -= L[i]; i += 1
        f = min(1, d_ / L[i]); x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f; y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f
        put(img, sprite("van19", 180, 120, lambda c: ic_van(c, 90, 60, 1.1)), 520 - 450 + x, 400 - 190 + y - 30, shadow=6)
    A(img, t, b, "members get pharmacy delivery for free", label_card("m19", 760, 150, lambda c, x, y: c.text((x, y + 2), "+", FONT_SANS, 80, GOLD), "WALMART PLUS MEMBERS: FREE", "WHERE DELIVERY IS AVAILABLE", col=OKG, tsize=36, ssize=26), 1440, 300, pop_=False, dx=50, shadow=8)
    A(img, t, b, "without the membership", label_card("n19", 760, 150, lambda c, x, y: c.text((x, y + 2), "$", FONT_SANS, 70, CORAL), "WITHOUT MEMBERSHIP: A FEE", "DEPENDS ON THE DELIVERY OPTION", col=CORAL, tsize=36, ssize=26), 1440, 480, pop_=False, dx=50, shadow=8)
    A(img, t, b, "forty nine states", shelf_tag("49s", 420, 240, "49 STATES", "SAME-DAY PHARMACY DELIVERY"), 400, 850, rot=-3, shadow=10)
    A(img, t, b, "with your groceries", label_card("g19", 620, 140, lambda c, x, y: ic_cart2(c, x, y, 0.55), "WITH YOUR GROCERIES", None, col=GOLD, tsize=36), 1000, 850, pop_=False, dy=40, shadow=8)
    ap(img, t, LAST(b), label_card("d19", 560, 140, lambda c, x, y: ic_car(c, x, y + 6, 0.8), "DON'T DRIVE?", "THIS IS A BIG ONE", col=GOLD, tsize=36, ssize=28), 1600, 850, pop_=False, dx=50, shadow=8)

# ============================================================ BLOCCO 20 - due cose da sapere
def bottles_spr():
    def fn(c):
        cols = [(232, 150, 60), (214, 108, 96), (110, 170, 210)]
        for k, col in enumerate(cols):
            ic_bottle(c, 90 + k * 150, 120, 1.2, col)
    return sprite("bot20", 420, 220, fn)

def draw20(img, t):
    b = 20
    head(img, t, 7, "TWO THINGS TO KNOW")
    A(img, t, b, "Not every medicine", label_card("ne20", 760, 160, lambda c, x, y: ic_bottle(c, x, y, 0.7), "NOT EVERY MEDICINE", "CAN BE DELIVERED", col=CORAL, tsize=42, ssize=32), 470, 290, pop_=False, dx=-50, shadow=10)
    A(img, t, b, "controlled substances", stamp("EXCEPTION: CONTROLLED SUBSTANCES", 760, 110, CORAL, 30), 470, 450, rot=-2, shadow=8)
    A(img, t, b, "Can this one", bubble("ask20", 860, 190, ["\"CAN THIS ONE BE", "DELIVERED TO MY HOME?\""], 46, tail="bl"), 1390, 300, shadow=12)
    A(img, t, b, "several medicines", bottles_spr(), 1140, 610, shadow=10)
    tq = T(b, "ask about each one")
    for k in range(3):
        ap(img, t, tq + k * 0.15, sprite("q20", 80, 80, lambda c: ic_question(c, 40, 40, 0.7)), 1140 - 150 + k * 150, 500, shadow=6)
    A(img, t, b, "ask about each one", chip("ASK ABOUT EACH ONE", 460, 70, fill=GOLD), 1620, 610, shadow=6)
    A(img, t, b, "insurance is applied", label_card("ins20", 820, 150, lambda c, x, y: ic_card(c, x, y, 0.6, (90, 140, 120)), "INSURANCE: SAME AS PICKUP", "WALMART HAS SAID", col=OKG, tsize=36, ssize=28), 520, 680, pop_=False, dx=-50, shadow=8)
    ap(img, t, LAST(b), label_card("home20", 820, 150, lambda c, x, y: ic_house(c, x, y, 0.75), "CHOOSE A TIME YOU'RE HOME", None, col=GOLD, tsize=36), 960, 920, pop_=False, dy=40, shadow=8)

DRAW = {i: globals()["draw%d" % i] for i in range(1, 21)}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background8(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render8(DRAW[b], n, f"{out}/V8-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
