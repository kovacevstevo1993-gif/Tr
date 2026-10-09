"""Video lungo 3 (Costco) - blocchi 26-30 (Concierge: numero, nota, dati da avere; punto 6 secondo anno di garanzia).
Durate dalla timeline dell'utente (07/10/2026): B26 338, B27 306, B28 344, B29 380, B30 362 fotogrammi.
Uso: OUT=cartella python3 long3_b26_30.py <blocco 26..30> [fotogrammi]
     python3 long3_b26_30.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b21_25 import *

DUR.update({26: 338, 27: 306, 28: 344, 29: 380, 30: 362})
PHRASES.update({
    26: ["The number is", "one, eight six six, eight six one, zero four five zero.", "They are open every day,",
         "from five in the morning until eight at night,", "Pacific time."],
    27: ["Write that number on a sticky note,", "and stick it on the back of the television,", "or save it in your phone right now.",
         "You will not remember it when the screen goes black."],
    28: ["Have this information next to you when you call:", "your name,", "your membership number,",
         "the item number from your receipt,", "the description and model number,", "the serial number,", "and the date you bought it."],
    29: ["Six.", "A second year of warranty.", "On televisions, projectors, computers and major appliances,",
         "Costco extends the manufacturer's warranty", "to two years from the date of purchase."],
    30: ["Major appliances means", "refrigerators above ten cubic feet,", "freezers, ranges, cooktops,",
         "over the range microwaves, dishwashers,", "water heaters, washers and dryers."],
})

# ------------------------------------------------------------------ icone nuove
def ic_sun(c, cx, cy, s=1.0):
    c.ell((cx - 30 * s, cy - 30 * s, cx + 30 * s, cy + 30 * s), fill=GOLD)
    for k in range(8):
        a = k * math.pi / 4
        c.line([(cx + math.cos(a) * 42 * s, cy + math.sin(a) * 42 * s), (cx + math.cos(a) * 58 * s, cy + math.sin(a) * 58 * s)], GOLD, 8 * s)

def ic_moon(c, cx, cy, s=1.0):
    c.ell((cx - 44 * s, cy - 44 * s, cx + 44 * s, cy + 44 * s), fill=IVORY)
    c.ell((cx - 14 * s, cy - 58 * s, cx + 66 * s, cy + 22 * s), fill=GREEN_D)
    c.ell((cx + 30 * s, cy - 40 * s, cx + 40 * s, cy - 30 * s), fill=GOLD)

def ic_sticky(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 56 * s, cx + 56 * s, cy + 56 * s), 6 * s, fill=(250, 235, 120))
    c.poly([(cx + 30 * s, cy + 56 * s), (cx + 56 * s, cy + 30 * s), (cx + 56 * s, cy + 56 * s)], fill=(220, 200, 90))
    for k, w_ in enumerate((34, 40, 26)):
        c.line([(cx - 38 * s, cy + (-26 + k * 24) * s), (cx - 38 * s + w_ * s, cy + (-30 + k * 24) * s), (cx - 38 * s + w_ * 1.6 * s, cy + (-26 + k * 24) * s)], CORAL_D, 5 * s)

def ic_tv_back(c, cx, cy, s=1.0):
    c.rrect((cx - 70 * s, cy - 50 * s, cx + 70 * s, cy + 40 * s), 10 * s, fill=(70, 78, 76), outline=IVORY, width=6 * s)
    for k in range(4):
        c.line([(cx - 60 * s, cy - 36 * s + k * 12 * s), (cx - 14 * s, cy - 36 * s + k * 12 * s)], (110, 120, 116), 4 * s)
    c.rrect((cx - 2 * s, cy - 30 * s, cx + 50 * s, cy + 24 * s), 4 * s, fill=(250, 235, 120))
    for k in range(3):
        c.line([(cx + 8 * s, cy - 16 * s + k * 12 * s), (cx + 40 * s, cy - 16 * s + k * 12 * s)], CORAL_D, 4 * s)
    c.rrect((cx - 30 * s, cy + 44 * s, cx + 30 * s, cy + 56 * s), 4 * s, fill=IVORY)

def ic_phone_contact(c, cx, cy, s=1.0):
    c.rrect((cx - 42 * s, cy - 64 * s, cx + 42 * s, cy + 64 * s), 12 * s, fill=GREEN_D, outline=IVORY, width=6 * s)
    c.rrect((cx - 32 * s, cy - 52 * s, cx + 32 * s, cy + 46 * s), 4 * s, fill=BLUE)
    c.ell((cx - 12 * s, cy - 40 * s, cx + 12 * s, cy - 16 * s), fill=IVORY)
    c.rrect((cx - 22 * s, cy - 8 * s, cx + 22 * s, cy + 6 * s), 4 * s, fill=IVORY)
    c.rrect((cx - 22 * s, cy + 14 * s, cx + 8 * s, cy + 26 * s), 4 * s, fill=IVORY)
    c.ell((cx + 10 * s, cy + 26 * s, cx + 40 * s, cy + 56 * s), fill=GOLD)
    check_ic(c, cx + 25 * s, cy + 41 * s, 0.4 * s, GREEN_D)

def ic_tv_off(c, cx, cy, s=1.0):
    c.rrect((cx - 70 * s, cy - 46 * s, cx + 70 * s, cy + 34 * s), 10 * s, fill=GREEN_D, outline=IVORY, width=7 * s)
    c.rrect((cx - 56 * s, cy - 34 * s, cx + 56 * s, cy + 22 * s), 4 * s, fill=(8, 12, 10))
    c.text((cx, cy - 8 * s), "?", FONT_SANS, 46 * s, GOLD)
    c.line([(cx, cy + 34 * s), (cx, cy + 52 * s)], IVORY, 8 * s)
    c.line([(cx - 30 * s, cy + 54 * s), (cx + 30 * s, cy + 54 * s)], IVORY, 9 * s)

def ic_person(c, cx, cy, s=1.0):
    person_ic(c, cx, cy + 8 * s, 1.4 * s, IVORY)

def ic_receipt(c, cx, cy, s=1.0):
    c.poly([(cx - 42 * s, cy - 62 * s), (cx + 42 * s, cy - 62 * s), (cx + 42 * s, cy + 56 * s), (cx + 28 * s, cy + 46 * s), (cx + 14 * s, cy + 56 * s),
            (cx, cy + 46 * s), (cx - 14 * s, cy + 56 * s), (cx - 28 * s, cy + 46 * s), (cx - 42 * s, cy + 56 * s)], fill=IVORY)
    for k in range(4):
        c.line([(cx - 28 * s, cy - 38 * s + k * 18 * s), (cx + 28 * s - (k % 2) * 14 * s, cy - 38 * s + k * 18 * s)], (150, 160, 152), 4 * s)

def ic_barcode(c, cx, cy, s=1.0):
    c.rrect((cx - 64 * s, cy - 42 * s, cx + 64 * s, cy + 42 * s), 8 * s, fill=IVORY)
    x = cx - 50 * s
    for w_ in (5, 3, 7, 3, 4, 8, 3, 5, 3, 6, 4):
        c.d.rectangle(c._b((x, cy - 28 * s, x + w_ * s, cy + 28 * s)), fill=GREEN_D)
        x += (w_ + 4) * s

def ic_cardm(c, cx, cy, s=1.0):
    c.rrect((cx - 66 * s, cy - 42 * s, cx + 66 * s, cy + 42 * s), 10 * s, fill=(236, 188, 108))
    c.rrect((cx - 66 * s, cy - 24 * s, cx + 66 * s, cy - 6 * s), 0, fill=(150, 105, 40))
    c.rrect((cx - 46 * s, cy + 8 * s, cx - 12 * s, cy + 30 * s), 4 * s, fill=(210, 160, 80))

def ic_box(c, cx, cy, s=1.0):
    c.rrect((cx - 58 * s, cy - 42 * s, cx + 58 * s, cy + 50 * s), 8 * s, fill=(196, 150, 98))
    c.line([(cx, cy - 42 * s), (cx, cy - 10 * s)], (160, 118, 72), 8 * s)
    c.rrect((cx - 34 * s, cy - 6 * s, cx + 34 * s, cy + 30 * s), 4 * s, fill=IVORY)
    c.line([(cx - 24 * s, cy + 6 * s), (cx + 24 * s, cy + 6 * s)], (150, 160, 152), 4 * s)
    c.line([(cx - 24 * s, cy + 18 * s), (cx + 10 * s, cy + 18 * s)], (150, 160, 152), 4 * s)

def ic_freezer(c, cx, cy, s=1.0):
    c.rrect((cx - 72 * s, cy - 18 * s, cx + 72 * s, cy + 54 * s), 8 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    c.rrect((cx - 76 * s, cy - 36 * s, cx + 76 * s, cy - 14 * s), 8 * s, fill=(214, 222, 214), outline=SAGE_D, width=4 * s)
    c.rrect((cx - 20 * s, cy - 32 * s, cx + 20 * s, cy - 22 * s), 4 * s, fill=GREEN_D)
    for k in range(3):
        a = k * math.pi / 3
        c.line([(cx - math.cos(a) * 20 * s, cy + 18 * s - math.sin(a) * 20 * s), (cx + math.cos(a) * 20 * s, cy + 18 * s + math.sin(a) * 20 * s)], BLUE, 5 * s)

def ic_range(c, cx, cy, s=1.0):
    c.rrect((cx - 62 * s, cy - 56 * s, cx + 62 * s, cy + 58 * s), 8 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    for sx in (-30, 30):
        for sy in (-34, -22):
            pass
    for sx in (-32, 32):
        c.ell((cx + sx * s - 16 * s, cy - 44 * s, cx + sx * s + 16 * s, cy - 26 * s), fill=GREEN_D)
    for k in range(4):
        c.ell((cx - 40 * s + k * 26 * s, cy - 16 * s, cx - 30 * s + k * 26 * s, cy - 6 * s), fill=GREEN_D)
    c.rrect((cx - 44 * s, cy + 2 * s, cx + 44 * s, cy + 46 * s), 6 * s, fill=BLUE)
    c.line([(cx - 38 * s, cy + 8 * s), (cx + 38 * s, cy + 8 * s)], IVORY, 4 * s)

def ic_cooktop(c, cx, cy, s=1.0):
    c.rrect((cx - 72 * s, cy - 40 * s, cx + 72 * s, cy + 40 * s), 10 * s, fill=GREEN_D, outline=IVORY, width=6 * s)
    for i, (dx, dy) in enumerate(((-34, -16), (34, -16), (-34, 18), (34, 18))):
        col = CORAL if i == 1 else GOLD
        c.ell((cx + (dx - 22) * s, cy + (dy - 14) * s, cx + (dx + 22) * s, cy + (dy + 14) * s), outline=col, width=5 * s)
        c.ell((cx + (dx - 8) * s, cy + (dy - 6) * s, cx + (dx + 8) * s, cy + (dy + 6) * s), outline=col, width=4 * s)

def ic_micro(c, cx, cy, s=1.0):
    c.rrect((cx - 76 * s, cy - 58 * s, cx + 76 * s, cy - 36 * s), 6 * s, fill=SAGE_D)
    c.rrect((cx - 72 * s, cy - 32 * s, cx + 72 * s, cy + 34 * s), 8 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    c.rrect((cx - 58 * s, cy - 22 * s, cx + 18 * s, cy + 24 * s), 4 * s, fill=BLUE)
    c.rrect((cx + 30 * s, cy - 22 * s, cx + 62 * s, cy - 6 * s), 3 * s, fill=GREEN_D)
    for k in range(3):
        c.ell((cx + 38 * s, cy + (2 + k * 9) * s, cx + 46 * s, cy + (10 + k * 9) * s), fill=GOLD)
    c.rrect((cx - 72 * s, cy + 40 * s, cx + 72 * s, cy + 58 * s), 6 * s, fill=GREEN_D, outline=IVORY, width=3 * s)

def ic_dishwasher(c, cx, cy, s=1.0):
    c.rrect((cx - 60 * s, cy - 62 * s, cx + 60 * s, cy + 62 * s), 8 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    c.rrect((cx - 60 * s, cy - 62 * s, cx + 60 * s, cy - 36 * s), 8 * s, fill=(214, 222, 214))
    for k in range(3):
        c.ell((cx - 40 * s + k * 20 * s, cy - 54 * s, cx - 32 * s + k * 20 * s, cy - 46 * s), fill=GREEN_D)
    c.rrect((cx - 46 * s, cy - 24 * s, cx + 46 * s, cy + 40 * s), 6 * s, fill=BLUE)
    for k in range(3):
        c.line([(cx - 40 * s, cy - 8 * s + k * 18 * s), (cx + 40 * s, cy - 8 * s + k * 18 * s)], IVORY, 3 * s)
    c.rrect((cx - 30 * s, cy + 46 * s, cx + 30 * s, cy + 54 * s), 3 * s, fill=GREEN_D)

def ic_heater(c, cx, cy, s=1.0):
    c.rrect((cx - 44 * s, cy - 56 * s, cx + 44 * s, cy + 62 * s), 22 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    c.rrect((cx - 30 * s, cy - 70 * s, cx - 18 * s, cy - 52 * s), 3 * s, fill=(190, 140, 66))
    c.rrect((cx + 18 * s, cy - 70 * s, cx + 30 * s, cy - 52 * s), 3 * s, fill=(110, 170, 200))
    c.rrect((cx - 44 * s, cy - 10 * s, cx + 44 * s, cy + 10 * s), 0, fill=CORAL)
    c.ell((cx - 16 * s, cy + 22 * s, cx + 16 * s, cy + 54 * s), fill=GREEN_D)
    c.line([(cx, cy + 38 * s), (cx + 10 * s, cy + 28 * s)], GOLD, 4 * s)

def ic_washer(c, cx, cy, s=1.0):
    c.rrect((cx - 60 * s, cy - 62 * s, cx + 60 * s, cy + 62 * s), 8 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    for k in range(3):
        c.ell((cx - 44 * s + k * 18 * s, cy - 54 * s, cx - 36 * s + k * 18 * s, cy - 46 * s), fill=GREEN_D)
    c.ell((cx - 40 * s, cy - 36 * s, cx + 40 * s, cy + 44 * s), fill=BLUE, outline=SAGE_D, width=7 * s)
    c.arc((cx - 26 * s, cy - 22 * s, cx + 26 * s, cy + 30 * s), 190, 330, IVORY, 6 * s)

def ic_dryer(c, cx, cy, s=1.0):
    c.rrect((cx - 60 * s, cy - 62 * s, cx + 60 * s, cy + 62 * s), 8 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    for k in range(3):
        c.ell((cx - 44 * s + k * 18 * s, cy - 54 * s, cx - 36 * s + k * 18 * s, cy - 46 * s), fill=GREEN_D)
    c.ell((cx - 40 * s, cy - 36 * s, cx + 40 * s, cy + 44 * s), fill=(236, 206, 150), outline=SAGE_D, width=7 * s)
    for k in range(3):
        c.line([(cx - 20 * s, cy - 8 * s + k * 14 * s), (cx - 6 * s, cy - 14 * s + k * 14 * s), (cx + 8 * s, cy - 8 * s + k * 14 * s), (cx + 22 * s, cy - 14 * s + k * 14 * s)], CORAL, 4 * s)

# ============================================================ BLOCCO 26
def card26():
    def mk():
        w, h = 1500, 290
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 50, fill=CARD, outline=GOLD, width=9)
        c.ell((40, h / 2 - 90, 220, h / 2 + 90), fill=GREEN_D)
        c.text((260, 62), "CONCIERGE  ·  FREE TECH HELP", FONT_SANS, 34, SAGE, anchor="lm", track=4)
        im = c.done()
        paste_c(im, mini(ic_headset, 0.85), 130, h / 2)
        return im
    return cache("card26", mk)

def day_tile(name):
    def mk():
        w, h = 200, 110
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 24, fill=GOLD, outline=(168, 118, 40), width=4)
        c.text((w / 2, h / 2 + 2), name, FONT_SANS, 46, GREEN_D)
        return c.done()
    return cache(("day", name), mk)

def draw26(img, t):
    ts = starts(26)
    common4(img, t, "THE CONCIERGE NUMBER", 5)
    show(img, t, ts[0] + 0.1, card26(), 960, 290, sh=14, dur=0.5)
    full = "1-866-861-0450"
    dim = fade(t, ts[0] + 0.3)
    if dim > 0:
        put_left(img, tspr(full, FONT_SANS, 120, SAGE_D), 470, 340, 120, alpha=0.35 * dim)
    steps = [("1-", 0.1), ("1-866-", 0.8), ("1-866-861-", 1.9), (full, 3.0)]
    cur = None
    for txt, off in steps:
        if t >= ts[1] + off:
            cur = txt
    if cur:
        put_left(img, tspr(cur, FONT_SANS, 120, GOLD), 470, 340, 120)
    days = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
    for i, d in enumerate(days):
        show(img, t, ts[2] + 0.1 + i * 0.17, day_tile(d), 960 + (i - 3) * 214, 560, sh=6, dur=0.35)
    show(img, t, ts[3] + 0.1, chipx("c26a", 560, 170, GREEN_L, GOLD, ic_sun, 0.72, ("FROM", "5 AM"), (38, 64), (SAGE, GOLD)), 560, 790)
    ar = seg(t, ts[3] + 0.8, 0.35)
    if ar > 0:
        put(img, arrow_spr(), 960, 790, scale=0.9 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[3] + 1.2, chipx("c26b", 560, 170, GREEN_L, GOLD, ic_moon, 0.72, ("UNTIL", "8 PM"), (38, 64), (SAGE, GOLD)), 1360, 790)
    show(img, t, ts[4], pill_spr("PACIFIC TIME", 52, 700, 100, GOLD, GREEN_D), 960, 975, sh=10)

# ============================================================ BLOCCO 27
def draw27(img, t):
    ts = starts(27)
    common4(img, t, "KEEP IT WHERE YOU CAN FIND IT", 5)
    xs = (330, 960, 1590)
    specs = ((ic_sticky, "c27a", ("WRITE IT ON", "A STICKY NOTE")), (ic_tv_back, "c27b", ("STICK IT ON THE", "BACK OF THE TV")), (ic_phone_contact, "c27c", ("OR SAVE IT IN", "YOUR PHONE")))
    for i, (fn, key, ls) in enumerate(specs):
        show(img, t, ts[i], card_big(key, 540, 420, GOLD, fn, 1.0, ls[0], ls[1], 38, 44, cy=140, r=100), xs[i], 365, sh=12)
    show(img, t, ts[2] + 1.3, pill_spr("SAVE IT RIGHT NOW", 40, 560, 76, GOLD, GREEN_D), 1590, 640, sh=6)
    show(img, t, ts[3], chipx("c27d", 1700, 150, PANEL_FILL, CORAL, ic_tv_off, 0.5, ("YOU WILL NOT REMEMBER IT WHEN THE SCREEN GOES BLACK",), (40,), (CORAL,)), 960, 850, sh=12)

# ============================================================ BLOCCO 28
ROWS28 = [(ic_person, "YOUR NAME"), (ic_cardm, "YOUR MEMBERSHIP NUMBER"), (ic_receipt, "ITEM NUMBER FROM YOUR RECEIPT"),
          (ic_box, "DESCRIPTION AND MODEL NUMBER"), (ic_barcode, "SERIAL NUMBER"), (calendar, "DATE YOU BOUGHT IT")]

def draw28(img, t):
    ts = starts(28)
    common4(img, t, "BEFORE YOU CALL", 5)
    show(img, t, ts[0] + 0.1, chipx("c28h", 1500, 110, GOLD, (168, 118, 40), ic_headset, 0.36, ("HAVE THIS NEXT TO YOU WHEN YOU CALL",), (48,), (GREEN_D,)), 960, 195, sh=8)
    for i, (fn, txt) in enumerate(ROWS28):
        y = 345 + i * 115
        p = show(img, t, ts[i + 1], chipx(("c28", i), 1500, 100, CARD, GOLD, fn, 0.36, (txt,), (44,), (IVORY,)), 960, y, sh=6, dur=0.4)
        ck = pop(t, ts[i + 1] + 0.45, 0.3)
        if ck[2] > 0:
            put(img, check_spr(), 1640, y, scale=0.8 * ck[0], alpha=ck[1])

# ============================================================ BLOCCO 29
def bar29():
    def mk():
        w, h = 1500, 140
        c = Cv(w, h)
        c.rrect((3, 3, 745, h - 3), 30, fill=IVORY, outline=SAGE_D, width=5)
        c.rrect((755, 3, w - 3, h - 3), 30, fill=GOLD, outline=(168, 118, 40), width=5)
        c.text((374, 50), "YEAR 1", FONT_SANS, 46, GREEN_D)
        c.text((374, 100), "MANUFACTURER'S WARRANTY", FONT_SANS, 30, GREEN_D)
        c.text((1127, 50), "YEAR 2", FONT_SANS, 46, GREEN_D)
        c.text((1127, 100), "COSTCO EXTENDS IT", FONT_SANS, 30, GREEN_D)
        return c.done()
    return cache("bar29", mk)

def bar29_half(k):
    def mk():
        im = bar29()
        w, h = im.size
        out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        box = (0, 0, 750, h) if k == 1 else (750, 0, w, h)
        part = im.crop(box)
        out.paste(part, (box[0], 0), part)
        return out
    return cache(("bar29h", k), mk)

def draw29(img, t):
    ts = starts(29)
    common4(img, t, "SAVING NUMBER 6")
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(6), 330, 300, scale=0.8 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 300, n=14, seed=3, rad=240)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("A SECOND YEAR", FONT_SANS, 100, IVORY), 590, 255, 100, alpha=h1)
        put_left(img, tspr("OF WARRANTY", FONT_SANS, 100, GOLD), 590, 370, 100, alpha=h1)
    for k, di in enumerate((0, 1, 2, 8)):
        show(img, t, ts[2] + 0.2 + k * 0.45, tile24(di), 615 + k * 230, 630, sh=6, dur=0.4)
    show(img, t, ts[3], bar29_half(1), 960, 870, sh=8)
    show(img, t, ts[3] + 1.0, bar29_half(2), 960, 870, sh=8)
    show(img, t, ts[4], pill_spr("TWO YEARS FROM THE DATE OF PURCHASE", 44, 1100, 90, PANEL_FILL, GOLD, GOLD), 960, 995, sh=8)

# ============================================================ BLOCCO 30
APPS = [(ic_fridge, "REFRIGERATORS", "ABOVE 10 CUBIC FEET"), (ic_freezer, "FREEZERS", ""), (ic_range, "RANGES", ""), (ic_cooktop, "COOKTOPS", ""),
        (ic_micro, "OVER THE RANGE", "MICROWAVES"), (ic_dishwasher, "DISHWASHERS", ""), (ic_heater, "WATER HEATERS", ""),
        (ic_washer, "WASHERS", ""), (ic_dryer, "DRYERS", "")]

def tile30(i):
    def mk():
        w, h = 330, 250
        fn, l1, l2 = APPS[i]
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=CARD, outline=GOLD, width=5)
        if l2:
            c.text((w / 2, 190), l1, FONT_SANS, 30 if len(l1) < 14 else 28, IVORY)
            c.text((w / 2, 224), l2, FONT_SANS, 24, GOLD)
        else:
            c.text((w / 2, 205), l1, FONT_SANS, 34, GOLD)
        im = c.done()
        paste_c(im, mini(fn, 0.84), w / 2, 94)
        return im
    return cache(("t30", i), mk)

def draw30(img, t):
    ts = starts(30)
    common4(img, t, "WHAT COUNTS AS MAJOR", 6)
    h1 = pop(t, 0.3, 0.5)
    put(img, tspr("MAJOR APPLIANCES", FONT_SANS, 100, GOLD), 960, 215, scale=h1[0], alpha=h1[1])
    pos1 = [(260 + i * 350, 440) for i in range(5)]
    pos2 = [(435 + i * 350, 735) for i in range(4)]
    pos = pos1 + pos2
    st = [ts[1] + 0.1, ts[2] + 0.1, ts[2] + 0.8, ts[2] + 1.5, ts[3] + 0.1, ts[3] + 1.5, ts[4] + 0.1, ts[4] + 0.8, ts[4] + 1.5]
    for i in range(9):
        show(img, t, st[i], tile30(i), pos[i][0], pos[i][1], sh=8, dur=0.4)

DRAW.update({26: draw26, 27: draw27, 28: draw28, 29: draw29, 30: draw30})

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/costco-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
