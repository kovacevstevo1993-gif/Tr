"""Video lungo 8 (WALMART) - blocchi 21-32. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-WALMART.md (versione finale).
Durate dalla timeline dell'utente (23/10/2026, fine di ogni blocco: 19595, 20595, 21493, 22498, 23328, 24245, 25157, 26290,
27126, 28033, 28804, 29534; fine blocco 20 = 18626).
Uso: OUT=cartella python3 long8_b21_32.py <blocco>      anteprima: python3 long8_b21_32.py frame <blocco> <secondi> <file.png>"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long8_kit import *
from long7_b11_29 import ic_thumb, ic_bell, ic_scale

ENDS = {20: 18626, 21: 19595, 22: 20595, 23: 21493, 24: 22498, 25: 23328, 26: 24245, 27: 25157, 28: 26290,
        29: 27126, 30: 28033, 31: 28804, 32: 29534}
for _b in range(21, 33):
    DUR[_b] = ENDS[_b] - ENDS[_b - 1]

def A(img, t, b, key, spr, x, y, n=1, **kw):
    return ap(img, t, T(b, key, n), spr, x, y, **kw)

# ============================================================ BLOCCO 21 - #8 sconto sulla benzina
def board_spr():
    def fn(c):
        w, h = 560, 420
        c.rrect((250, 300, 310, 420), 6, fill=(60, 66, 74))
        c.rrect((0, 0, w, 320), 26, fill=PAPER, outline=GOLD, width=8)
        c.rrect((0, 0, w, 80), 26, fill=GREEN_D)
        c.rrect((0, 50, w, 80), 0, fill=GREEN_D)
        c.text((w / 2, 42), "WALMART PLUS", FONT_SANS, 38, GOLD, track=4)
        c.text((w / 2, 165), "10 CENTS", FONT_SANS, 96, INK, track=2)
        c.text((w / 2, 255), "OFF A GALLON", FONT_SANS, 44, CORAL, track=4)
    return sprite("board21", 560, 420, fn)

def draw21(img, t):
    b = 21
    head(img, t, 8, "MONEY OFF YOUR GAS")
    A(img, t, b, "Money off your gas", sprite("pump21", 220, 300, lambda c: ic_pump(c, 100, 150, 2.1)), 900, 470, shadow=12)
    A(img, t, b, "save ten cents a gallon", board_spr(), 420, 480, pop_=False, dy=60, dur=0.6, shadow=14)
    A(img, t, b, "participating stations", chip("AT PARTICIPATING STATIONS", 620, 70, fill=IVORY), 420, 760, shadow=6)
    A(img, t, b, "In September", label_card("sep21", 700, 140, lambda c, x, y: ic_calendar(c, x, y + 4, 0.55), "SEPTEMBER: CITGO ADDED", None, col=GOLD, tsize=36), 1460, 290, pop_=False, dx=-50, shadow=8)
    A(img, t, b, "seventeen thousand", shelf_tag("17k", 520, 230, "17,000+", "STATIONS ACROSS THE COUNTRY"), 1460, 500, rot=-2, shadow=10)
    brands = [("Walmart, Murphy", "WALMART"), ("Murphy, Exxon", "MURPHY"), ("Exxon, Mobil", "EXXON"), ("Mobil and Citgo", "MOBIL"), ("Citgo stations", "CITGO")]
    for k, (key, lab) in enumerate(brands):
        A(img, t, b, key, chip(lab, 176, 64, fill=GOLD, size=26), 1050 + k * 182, 700, shadow=6)
    A(img, t, b, "ask the cashier", bubble("cash21", 760, 150, ["NOT SURE HOW TO USE IT?", "ASK THE CASHIER THERE"], 40, tail="bl"), 520, 900, shadow=10)
    ap(img, t, LAST(b), stamp("KEEPS PAYING YOU BACK", 640, 110, GOLD, 40), 1460, 900, rot=-3, shadow=8)

# ============================================================ BLOCCO 22 - i conti onesti
def bar_spr(key, length, col):
    return sprite(("bar22", key), length, 70, lambda c: c.rrect((0, 0, length, 70), 18, fill=col))

def draw22(img, t):
    b = 22
    head(img, t, 8, "THE HONEST MATH")
    A(img, t, b, "ten gallons", card("g22", 380, 210, lambda c, x, y: ic_pump(c, x, y, 0.7), ["10 GALLONS", "EVERY WEEK"], GOLD, 34, ih=0.42, ink=IVORY, ink2=GOLD), 270, 330, shadow=10)
    A(img, t, b, "At ten cents", txt("X", 70, GOLD), 500, 330)
    A(img, t, b, "At ten cents", card("c22", 380, 210, lambda c, x, y: c.text((x, y), "10 CENTS", FONT_SANS, 44, GOLD, track=2), ["A GALLON"], GOLD, 34, ih=0.42, ink=IVORY), 730, 330, shadow=10)
    A(img, t, b, "one dollar a week", txt("=", 70, GOLD), 960, 330)
    A(img, t, b, "one dollar a week", shelf_tag("1w", 320, 190, "$1", "A WEEK"), 1170, 320, shadow=10)
    A(img, t, b, "Over a year", sprite("ar22", 160, 60, lambda c: (c.rrect((0, 20, 110, 40), 8, fill=GOLD), c.poly([(100, 2), (156, 30), (100, 58)], fill=GOLD))), 1395, 330)
    A(img, t, b, "Over a year", shelf_tag("52y", 380, 190, "ABOUT $52", "A YEAR IN GAS"), 1650, 320, rot=-2, shadow=10)
    x0 = 560
    rows = [("Now look at number six", "GAS SAVINGS", "ABOUT $52", 531, OKG, 590),
            ("forty nine dollars for the year", "PLUS ASSIST", "$49", 500, GOLD, 710),
            ("At the full ninety eight", "FULL PRICE", "$98", 1000, CORAL, 830)]
    for key, lab, val, ln, col, y in rows:
        tk = T(b, key)
        ap(img, t, tk, fit(lab, 36, 330, IVORY, 3), 330, y)
        grow(img, t, tk + 0.2, bar_spr(lab, ln, col), x0 + ln / 2, y, dur=0.7, shadow=6)
        vs = txt(val, 34, GREEN_D if col != CORAL else IVORY, 2)
        ap(img, t, tk + 0.9, vs, x0 + ln - vs.width / 2 - 6, y)
    tg = T(b, "the gas savings alone")
    ap(img, t, tg, ok_spr(80), x0 + 531 + 64, 590, shadow=6)
    ap(img, t, tg + 0.2, chip("GAS ALONE CAN COVER ASSIST", 600, 70, fill=OKG), 1500, 650, shadow=6)
    ap(img, t, LAST(b), chip("FULL PRICE: NEED MORE DRIVING OR DELIVERIES", 1000, 76, fill=IVORY, size=30), 960, 970, shadow=8)

# ============================================================ BLOCCO 23 - #9 la lista da 4 dollari
def timeline_spr():
    def fn(c):
        w, h = 760, 160
        c.rrect((60, 74, 700, 86), 6, fill=GOLD)
        c.ell((10, 30, 110, 130), fill=GOLD, outline=IVORY, width=4)
        c.text((60, 82), "2006", FONT_SANS, 28, GREEN_D)
        c.ell((650, 30, 750, 130), fill=PAPER, outline=GOLD, width=4)
        c.text((700, 82), "NOW", FONT_SANS, 28, INK)
    return sprite("tl23", 760, 160, fn)

def draw23(img, t):
    b = 23
    head(img, t, 9, "THE FOUR DOLLAR LIST")
    A(img, t, b, "Twenty years ago", timeline_spr(), 480, 300, pop_=False, dx=-40, shadow=8)
    A(img, t, b, "two thousand six", chip("20 YEARS", 260, 60, fill=IVORY), 480, 220, shadow=6)
    A(img, t, b, "a month of certain generic", shelf_tag("4m", 440, 260, "$4", "A MONTH: CERTAIN GENERICS"), 480, 560, shadow=12)
    A(img, t, b, "It's called", label_card("wpp23", 820, 130, lambda c, x, y: ic_pills(c, x, y, 0.6), "WALMART PRESCRIPTION PROGRAM", None, col=GOLD, tsize=34), 480, 820, pop_=False, dy=40, shadow=8)
    A(img, t, b, "most recent price guide", receipt("pg23", 760, 430, "MOST RECENT PRICE GUIDE", [("BLOOD PRESSURE", "$4"), ("THYROID", "$4"), ("AND MORE", "$4"), ("UP TO 30 DAYS", "")], size=36, title_size=40), 1400, 470, pop_=False, dx=60, shadow=12)
    A(img, t, b, "the step that matters", chip("THE STEP THAT MATTERS", 520, 64, fill=GOLD), 1400, 735, shadow=6)
    A(img, t, b, "Ask the pharmacist", bubble("ask23", 840, 160, ["\"IS MY MEDICINE ON THAT LIST,", "AT MY DOSE?\""], 40, tail="br"), 1400, 880, shadow=10)

# ============================================================ BLOCCO 24 - non solo il prezzo del titolo
def draw24(img, t):
    b = 24
    head(img, t, 9, "BEYOND THE HEADLINE PRICE")
    A(img, t, b, "Not every medicine", shelf_tag("n4", 280, 190, "$4", "NOT EVERY ONE"), 190, 780, shadow=10)
    A(img, t, b, "nine dollars for thirty days", shelf_tag("9_30", 280, 190, "$9", "30 DAYS"), 470, 670, shadow=10)
    A(img, t, b, "twenty four for ninety", shelf_tag("24_90", 280, 190, "$24", "90 DAYS"), 750, 560, shadow=10)
    A(img, t, b, "Higher doses", label_card("dose24", 680, 120, lambda c, x, y: c.poly([(x, y - 36), (x + 30, y + 10), (x + 10, y + 10), (x + 10, y + 36), (x - 10, y + 36), (x - 10, y + 10), (x - 30, y + 10)], fill=CORAL), "HIGHER DOSES COST MORE", None, col=CORAL, tsize=34), 470, 330, pop_=False, dx=-50, shadow=8)
    A(img, t, b, "higher in some states", label_card("st24", 760, 120, lambda c, x, y: ic_pin8(c, x, y + 8, 1.0), "SOME STATES CAN BE HIGHER", None, col=GOLD, tsize=34), 1420, 280, pop_=False, dx=50, shadow=8)
    A(img, t, b, "California", chip("CALIFORNIA", 330, 64, fill=GOLD), 1240, 400, shadow=6)
    A(img, t, b, "Minnesota", chip("MINNESOTA", 330, 64, fill=GOLD), 1600, 400, shadow=6)
    A(img, t, b, "North Dakota", stamp("NORTH DAKOTA: NOT OFFERED", 700, 100, CORAL, 36), 1420, 530, rot=-3, shadow=8)
    A(img, t, b, "first fill", label_card("ff24", 760, 120, lambda c, x, y: ic_person(c, x, y + 4, 0.7, GOLD), "FIRST FILL: IN PERSON", None, col=OKG, tsize=34), 1420, 690, pop_=False, dx=50, shadow=8)
    A(img, t, b, "refills are picked up", label_card("rf24", 760, 120, lambda c, x, y: ic_storefront(c, x, y, 0.5), "REFILLS: PICKED UP IN STORE", None, col=OKG, tsize=34), 1420, 830, pop_=False, dx=50, shadow=8)
    ap(img, t, LAST(b), label_card("wd24", 820, 110, lambda c, x, y: ic_doc(c, x, y, 0.45), "WRITE DOWN: MEDICINE AND DOSE", None, col=GOLD, tsize=32), 560, 980, pop_=False, dy=30, shadow=8)

# ============================================================ BLOCCO 25 - il piano o il programma?
def draw25(img, t):
    b = 25
    head(img, t, 9, "YOUR PLAN OR THE PROGRAM?")
    A(img, t, b, "don't assume", chip("YOUR PLAN IS NOT ALWAYS THE CHEAPER WAY", 900, 70, fill=IVORY, size=30), 960, 215, shadow=6)
    A(img, t, b, "program rules say", card("pp25", 620, 300, lambda c, x, y: ic_pills(c, x, y, 0.9), ["PROGRAM PRICE"], GOLD, 40, ih=0.45, ink=IVORY), 520, 470, pop_=False, dx=-60, shadow=12)
    A(img, t, b, "you may pay", card("pl25", 620, 300, lambda c, x, y: ic_card(c, x, y, 0.9, (90, 140, 120)), ["PRICE WITH YOUR PLAN"], GOLD, 40, ih=0.45, ink=IVORY), 1400, 470, pop_=False, dx=60, shadow=12)
    A(img, t, b, "less or more", chip("YOU MAY PAY LESS OR MORE", 560, 64, fill=GOLD), 1400, 670, shadow=6)
    A(img, t, b, "worth comparing", sprite("sc25", 200, 200, lambda c: (c.ell((4, 4, 196, 196), fill=PANEL_FILL, outline=GOLD, width=5), ic_scale(c, 100, 100, 1.1))), 960, 470, shadow=10)
    A(img, t, b, "The pharmacist can look", label_card("ph25", 760, 140, lambda c, x, y: ic_doctor(c, x, y + 4, 0.75), "THE PHARMACIST CHECKS BOTH", None, col=GOLD, tsize=34), 520, 800, pop_=False, dy=40, shadow=8)
    A(img, t, b, "choose the lower one", stamp("CHOOSE THE LOWER ONE", 620, 110, OKG, 42), 1400, 800, rot=-3, shadow=8)
    ap(img, t, LAST(b), label_card("min25", 880, 110, lambda c, x, y: ic_clock(c, x, y, 34, 1.2), "ABOUT A MINUTE, ONCE PER MEDICINE", None, col=GOLD, tsize=32), 960, 965, pop_=False, dy=30, shadow=8)

# ============================================================ BLOCCO 26 - #10 la versione da 90 giorni
def cals_spr():
    def fn(c):
        for k in range(3):
            ic_calendar(c, 90 + k * 190, 90, 1.2, top=GOLD)
            c.text((90 + k * 190, 112), "M" + str(k + 1), FONT_SANS, 34, INK)
    return sprite("cal26", 560, 180, fn)

def trips_spr():
    def fn(c):
        for k in range(3):
            ic_storefront(c, 110 + k * 200, 70, 0.9)
        for k in (1, 2):
            x = 110 + k * 200
            c.line([(x - 60, 20), (x + 60, 120)], CORAL, 12); c.line([(x + 60, 20), (x - 60, 120)], CORAL, 12)
        c.text((310, 170), "ONE TRIP INSTEAD OF THREE", FONT_SANS, 32, IVORY, track=2)
    return sprite("trip26", 620, 200, fn)

def draw26(img, t):
    b = 26
    head(img, t, 10, "THE NINETY DAY VERSION")
    A(img, t, b, "ninety day supply", cals_spr(), 420, 300, pop_=False, dx=-40, shadow=8)
    A(img, t, b, "for ten dollars", shelf_tag("10_90", 440, 220, "$10", "90 DAYS: SOME GENERICS"), 420, 520, shadow=12)
    A(img, t, b, "two and a half months", chip("SAME AS 2.5 MONTHS AT $4", 620, 70, fill=IVORY), 420, 710, shadow=6)
    A(img, t, b, "one trip", trips_spr(), 420, 880, shadow=8)
    A(img, t, b, "two catches", stamp("TWO CATCHES", 460, 110, CORAL, 46), 1420, 290, rot=-3, shadow=8)
    A(img, t, b, "Not every drug", label_card("c1_26", 820, 160, lambda c, x, y: ic_pills(c, x, y, 0.6), "NOT EVERY $4 DRUG", "IS ON THE $10 LIST", col=CORAL, tsize=38, ssize=30), 1420, 480, pop_=False, dx=50, shadow=8)
    A(img, t, b, "your doctor", label_card("c2_26", 820, 160, lambda c, x, y: ic_doctor(c, x, y + 4, 0.75), "YOUR DOCTOR MAY NEED", "TO CHANGE 30 DAYS TO 90", col=CORAL, tsize=38, ssize=30), 1420, 680, pop_=False, dx=50, shadow=8)
    ap(img, t, LAST(b), chip("30 DAYS", 220, 70, fill=IVORY), 1240, 870, shadow=6)
    ap(img, t, LAST(b), arrow_spr(140, 56), 1420, 870)
    ap(img, t, LAST(b), chip("90 DAYS", 220, 70, fill=GOLD), 1600, 870, shadow=6)

# ============================================================ BLOCCO 27 - chiedere prima + la frase
def index_card():
    def fn(c):
        w, h = 1500, 300
        c.rrect((0, 0, w, h), 18, fill=PAPER, outline=GOLD, width=6)
        c.line([(40, 70), (w - 40, 70)], CORAL, 4)
        for y in (140, 205, 270):
            c.line([(40, y), (w - 40, y)], (196, 214, 230), 3)
        lines = ["\"IS MY MEDICINE ON YOUR $4 OR $10 LIST,", "AND WOULD THE CASH PRICE BE LOWER", "THAN WHAT I PAY WITH MY PLAN?\""]
        for i, ln in enumerate(lines):
            c.text((w / 2, 118 + i * 64), ln, FONT_SANS, 46, INK, track=1)
    return sprite("idx27", 1500, 300, fn)

def draw27(img, t):
    b = 27
    head(img, t, 10, "ONE MORE RULE, AND THE SENTENCE")
    A(img, t, b, "Some plans", label_card("sp27", 860, 150, lambda c, x, y: ic_warn(c, x, y, 0.7), "SOME PLANS MAY NOT COVER", "A 90-DAY SUPPLY", col=CORAL, tsize=38, ssize=30), 520, 300, pop_=False, dx=-50, shadow=8)
    A(img, t, b, "government funded", label_card("gf27", 860, 110, lambda c, x, y: ic_gov(c, x, y, 0.5), "INCLUDING GOVERNMENT-FUNDED PROGRAMS", None, col=GOLD, tsize=30), 520, 445, pop_=False, dx=-50, shadow=8)
    A(img, t, b, "ask first", chip("THROUGH YOUR PLAN? ASK FIRST", 680, 70, fill=GOLD), 520, 560, shadow=6)
    tn = T(b, "numbers nine and ten")
    ap(img, t, tn, numdisc(9, 120), 1300, 310, shadow=8)
    ap(img, t, tn + 0.15, txt("+", 70, GOLD), 1420, 310)
    ap(img, t, tn + 0.3, numdisc(10, 120), 1540, 310, shadow=8)
    A(img, t, b, "word for word", chip("SAY IT WORD FOR WORD", 520, 66, fill=IVORY), 1420, 450, shadow=6)
    A(img, t, b, "Is my medicine", index_card(), 960, 770, pop_=False, dy=60, dur=0.6, shadow=14)
    ap(img, t, LAST(b), chip("WRITE IT ON A CARD. KEEP IT IN YOUR WALLET.", 960, 66, fill=GOLD, size=28), 960, 990, shadow=6)

# ============================================================ BLOCCO 28 - riepilogo dei dieci
ALL10 = [("One, ask", "MATCH ITS OWN WEBSITE", "AT CHECKOUT"), ("Two, use", "HOLIDAY RETURNS", "UNTIL JANUARY 31"),
         ("Three, use", "FREE CURBSIDE PICKUP", None), ("Four, ask", "FLU SHOT", "ASK AT THE PHARMACY"),
         ("Five, use", "SNAP ONLINE", None), ("Six, check", "WALMART PLUS AT HALF PRICE", "IF YOU QUALIFY"),
         ("Seven, get", "PRESCRIPTIONS DELIVERED", None), ("Eight, save", "SAVE ON GAS", None),
         ("Nine, ask", "THE $4 LIST", "ASK ABOUT IT"), ("Ten, ask", "90 DAYS FOR $10", "ASK ABOUT IT")]

def draw28(img, t):
    b = 28
    head(img, t, 0, "ALL TEN IN ONE PLACE")
    for k, (key, a, s_) in enumerate(ALL10):
        col, row = k // 5, k % 5
        x, y = 520 + col * 900, 270 + row * 170
        tk = T(b, key)
        ap(img, t, tk, numdisc(k + 1, 110), x - 370, y, shadow=8)
        ap(img, t, tk + 0.1, label_card(("all28", k), 640, 130, None, a, s_, col=GOLD, tsize=34, ssize=26), x + 40, y, pop_=False, dx=40, shadow=8)

# ============================================================ BLOCCO 29 - cosa fare questa settimana
def notepad_spr():
    def fn(c):
        w, h = 1080, 760
        c.rrect((0, 30, w, h), 20, fill=PAPER, outline=GOLD, width=6)
        for k in range(12):
            x = 70 + k * 85
            c.ell((x - 14, 10, x + 14, 52), outline=(150, 150, 150), width=6)
        c.text((w / 2, 110), "THIS WEEK", FONT_SANS, 48, INK, track=6)
        c.line([(60, 150), (w - 60, 150)], CORAL, 4)
    return sprite("note29", 1080, 760, fn)

def todo_spr(key, l1, l2):
    def fn(c):
        c.rrect((0, 10, 70, 80), 10, fill=IVORY, outline=GREEN_D, width=5)
        c.text((100, 30), l1, FONT_SANS, 34, INK, anchor="lm", track=1)
        c.text((100, 74), l2, FONT_SANS, 28, (150, 110, 40), anchor="lm", track=1)
    return sprite(("todo29", key), 960, 100, fn)

def draw29(img, t):
    b = 29
    head(img, t, 0, "WHAT I'D DO THIS WEEK")
    ap(img, t, 0.3, notepad_spr(), 640, 600, pop_=False, dy=50, dur=0.6, shadow=14)
    todos = [("Write down every medicine", "WRITE DOWN EVERY MEDICINE", "WITH THE DOSE"),
             ("Take that list", "TAKE IT TO THE WALMART PHARMACY", "WITH THE SENTENCE FROM NUMBER TEN"),
             ("If you get government help", "SNAP OR MEDICAID? CHECK THE ASSIST PAGE", "BEFORE YOU PAY FULL PRICE"),
             ("from now until the end", "KEEP EVERY WALMART RECEIPT", "IN ONE ENVELOPE, UNTIL END OF DECEMBER")]
    for k, (key, l1, l2) in enumerate(todos):
        tk = T(b, key)
        y = 420 + k * 150
        ap(img, t, tk, todo_spr(k, l1, l2), 610, y, pop_=False, dx=-30)
        ap(img, t, tk + 0.6, sprite("tick29", 70, 70, lambda c: check_ic(c, 35, 38, 0.9, OKG)), 165, y - 5)
    A(img, t, b, "end of December", sprite("dec29", 220, 220, lambda c: ic_calendar(c, 110, 110, 1.6, txt_="DEC")), 1560, 330, shadow=10)
    A(img, t, b, "one envelope", sprite("env29", 300, 220, lambda c: ic_envelope(c, 150, 110, 2.0)), 1560, 600, shadow=10)
    A(img, t, b, "because of number two", chip("BECAUSE OF NUMBER TWO", 520, 64, fill=GOLD), 1560, 760, shadow=6)
    ap(img, t, LAST(b), label_card("free29", 560, 130, None, "NONE OF THIS COSTS", "ANYTHING TO CHECK", col=OKG, tsize=34, ssize=30), 1560, 920, pop_=False, dy=30, shadow=8)

# ============================================================ BLOCCO 30 - un avvertimento onesto
def fakecard_spr():
    def fn(c):
        w, h = 560, 330
        c.rrect((0, 0, w, h), 26, fill=(70, 120, 180), outline=IVORY, width=6)
        c.rrect((40, 60, 130, 130), 12, fill=GOLD)
        c.text((w / 2 + 40, 95), "SENIOR CARD", FONT_SANS, 46, IVORY, track=3)
        c.text((w / 2, 230), "?", FONT_SANS, 130, GOLD)
    return sprite("fake30", 560, 330, fn)

def draw30(img, t):
    b = 30
    head(img, t, 0, "ONE HONEST WARNING")
    for k, (key, lab) in enumerate((("programs", "PROGRAMS"), ("prices and", "PRICES"), ("partners", "PARTNERS"))):
        A(img, t, b, key, shelf_tag(("chg30", lab), 280, 160, lab, "CAN CHANGE", big_size=40), 230 + k * 310, 300, shadow=8)
    for k, (key, lab) in enumerate((("your state", "STATE"), ("your store", "STORE"), ("your plan", "PLAN"))):
        A(img, t, b, key, label_card(("dep30", lab), 280, 100, lambda c, x, y: ic_pin8(c, x, y + 6, 0.7), lab, None, col=GOLD, tsize=32), 230 + k * 310, 520, pop_=False, dy=30, shadow=6)
    A(img, t, b, "That's why", receipt("ntv30", 900, 300, "IN THIS VIDEO", [("A SENIOR DISCOUNT PROMISED", "NO"), ("\"FREE\" WITHOUT WALMART IN WRITING", "NO")], accent=CORAL, size=32, title_size=40), 540, 820, pop_=False, dy=50, shadow=12)
    A(img, t, b, "secret Walmart senior card", fakecard_spr(), 1460, 380, rot=-4, shadow=14)
    A(img, t, b, "look for it", label_card("lk30", 760, 130, lambda c, x, y: ic_web(c, x, y, 0.5), "LOOK ON WALMART'S WEBSITE FIRST", None, col=GOLD, tsize=32), 1460, 660, pop_=False, dx=50, shadow=8)
    ap(img, t, LAST(b), stamp("NOT THERE? BE CAREFUL", 620, 110, CORAL, 42), 1460, 850, rot=-3, shadow=8)

# ============================================================ BLOCCO 31 - condividi, commenta, iscriviti
def draw31(img, t):
    b = 31
    head(img, t, 0, "SHARE IT, TELL ME, SUBSCRIBE")
    A(img, t, b, "send them this video", label_card("sh31", 760, 160, lambda c, x, y: ic_phone(c, x, y, 0.6), "SEND IT TO SOMEONE OVER 60", "WHO SHOPS AT WALMART EVERY WEEK", col=GOLD, tsize=34, ssize=24), 460, 300, pop_=False, dx=-50, shadow=8)
    A(img, t, b, "It might save them", chip("IT MIGHT SAVE THEM MORE THAN YOU", 720, 64, fill=IVORY, size=28), 460, 440, shadow=6)
    A(img, t, b, "tell me in the comments", bubble("cm31", 860, 180, ["WHICH OF THESE TEN", "DID YOU NOT KNOW ABOUT?"], 44, tail="bl"), 1400, 300, shadow=10)
    tw_ = T(b, "which one of these ten")
    for k in range(10):
        ap(img, t, tw_ + 0.4 + k * 0.08, numdisc(k + 1, 70), 1022 + k * 84, 470, dur=0.35)
    tl = T(b, "like the video")
    ap(img, t, tl, sprite("th31", 220, 220, lambda c: ic_thumb(c, 110, 100, 1.7)), 260, 690, shadow=10)
    ap(img, t, tl + 0.3, txt("LIKE", 56, GOLD, 4), 260, 830)
    ts = T(b, "subscribe")
    ap(img, t, ts, sprite("sub31", 460, 120, lambda c: (c.rrect((4, 4, 456, 116), 58, fill=RED, outline=(255, 255, 255), width=6), c.text((230, 62), "SUBSCRIBE", FONT_SANS, 54, (255, 255, 255), track=3))), 760, 690, shadow=12)
    ap(img, t, ts + 0.3, txt("THE SENIOR ADVANTAGE", 40, IVORY, 3), 760, 810)
    A(img, t, b, "don't miss the next", sprite("bell31", 150, 150, lambda c: ic_bell(c, 75, 72, 1.5)), 1200, 690, shadow=8)
    A(img, t, b, "don't miss the next", chip("SO YOU DON'T MISS THE NEXT ONE", 560, 66, fill=GOLD, size=26), 1600, 690, shadow=6)
    ap(img, t, LAST(b), chip("WHAT PEOPLE OVER 60 CAN CLAIM, AND EXACTLY HOW TO ASK", 1500, 84, fill=IVORY, size=32), 960, 950, shadow=8)

# ============================================================ BLOCCO 32 - slide finale col disclaimer
def endbox():
    def fn(c):
        w, h = 700, 480
        for x in range(10, w - 30, 60):
            c.line([(x, 3), (x + 34, 3)], GOLD, 5); c.line([(x, h - 3), (x + 34, h - 3)], GOLD, 5)
        for y in range(10, h - 30, 60):
            c.line([(3, y), (3, y + 34)], GOLD, 5); c.line([(w - 3, y), (w - 3, y + 34)], GOLD, 5)
    return sprite("end32", 700, 480, fn)

def disc_panel():
    def fn(c):
        w, h = 900, 640
        c.rrect((0, 10, w, h - 10), 12, fill=PAPER)
        for k in range(0, w, 30):
            c.poly([(k, 12), (k + 15, 0), (k + 30, 12)], fill=PAPER)
            c.poly([(k, h - 12), (k + 15, h), (k + 30, h - 12)], fill=PAPER)
        c.text((w / 2, 80), "BEFORE YOU GO", FONT_SANS, 46, INK, track=6)
        for k in range(40, w - 40, 18):
            c.line([(k, 128), (k + 9, 128)], (170, 166, 154), 3)
    return sprite("dp32", 900, 640, fn)

DLINES = [("Rules, prices", "Rules, prices and programs change", INK), ("they differ", "and differ by state, store and plan.", INK),
          ("Always confirm", "Always confirm with Walmart, your pharmacist", (150, 100, 20)), ("before you rely", "or your plan before you rely on them.", (150, 100, 20)),
          ("general information", "General information,", (70, 100, 84)), ("not financial", "not financial or medical advice.", (70, 100, 84)),
          ("not affiliated", "This channel is not affiliated with Walmart.", INK)]

def draw32(img, t):
    b = 32
    te = DUR[b] / FPS - 20.0          # schermata finale di YouTube = ultimi 20 secondi: il riquadro compare li, non prima
    ap(img, t, 0.3, txt("BEFORE", 120, IVORY, 6), 470, 400, pop_=False, dy=30, dur=0.6, t_out=te - 0.4)
    ap(img, t, 0.5, txt("YOU GO", 120, GOLD, 6), 470, 540, pop_=False, dy=30, dur=0.6, t_out=te - 0.4)
    ap(img, t, te, endbox(), 470, 470, pop_=False, dur=0.4)
    ap(img, t, te + 0.1, txt("WATCH NEXT", 54, GOLD, 3), 470, 780, pop_=False, dur=0.4)
    ap(img, t, 0.2, disc_panel(), 1380, 500, pop_=False, dy=40, dur=0.6, shadow=14)
    for i, (key, s_, col) in enumerate(DLINES):
        ap(img, t, T(b, key) if i else 0.6, tspr(s_, FONT_SANS_M, 34, col), 1380, 360 + i * 62, pop_=False, dy=14, dur=0.5)
    ap(img, t, LAST(b), txt("THANKS FOR WATCHING", 40, IVORY, 4), 960, 950)

DRAW = {i: globals()["draw%d" % i] for i in range(21, 33)}

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
