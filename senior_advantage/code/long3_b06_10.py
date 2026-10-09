"""Video lungo 3 (Costco) - blocchi 6-10 (punto 1: Member Prescription Program). 1920x1080, 30 fps.
Durate dalla timeline dell'utente (07/10/2026): B6 365, B7 354, B8 360, B9 376, B10 429 fotogrammi.
Uso: OUT=cartella python3 long3_b06_10.py <blocco 6..10> [fotogrammi]
     python3 long3_b06_10.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b02_05 import *

DUR.update({6: 365, 7: 354, 8: 360, 9: 376, 10: 429})
PHRASES.update({
    6: ["One.", "The Member Prescription Program.", "This is the biggest one for many seniors, so let's start here.",
        "It is not insurance.", "It is a free discount program on prescription drugs."],
    7: ["Costco says it can lower the price of some medications", "by up to eighty percent or more,",
        "depending on the drug.", "That is not a promise for every medication,", "so you have to check your own."],
    8: ["There is nothing to sign up for", "and no extra fee.", "You just show your Costco membership card at the pharmacy.",
        "You do not need insurance for it,", "and you do not need coupons."],
    9: ["And here is the part most people miss.", "The program does not only work at Costco.",
        "It also works at thousands of participating pharmacies,", "including chains like Walgreens and Kroger."],
    10: ["To use it, go to the Costco website,", "costco dot com slash c m p p,", "type the name of your medication,",
         "and compare prices before you go.", "Write down the price,", "and ask the pharmacist to confirm it."],
})

AMB = (222, 150, 64)

# ------------------------------------------------------------------ sprite comuni
def num_badge(n, S=380, fs=210):
    def mk():
        c = Cv(S, S)
        c.ell((6, 6, S - 6, S - 6), fill=GOLD)
        c.ell((S * 0.063, S * 0.063, S - S * 0.063, S - S * 0.063), outline=GREEN_D, width=max(3, S // 76))
        c.text((S / 2, S / 2 + S * 0.016), str(n), FONT_SERIF, fs, GREEN_D)
        return c.done()
    return cache(("nb", n, S, fs), mk)

def bottle(c, cx, cy, s=1.0):
    c.rrect((cx - 38 * s, cy - 34 * s, cx + 38 * s, cy + 56 * s), 14 * s, fill=AMB)
    c.rrect((cx - 44 * s, cy - 60 * s, cx + 44 * s, cy - 30 * s), 10 * s, fill=IVORY)
    c.rrect((cx - 28 * s, cy - 8 * s, cx + 28 * s, cy + 38 * s), 8 * s, fill=IVORY)
    c.rrect((cx - 6 * s, cy - 2 * s, cx + 6 * s, cy + 32 * s), 3, fill=CORAL)
    c.rrect((cx - 17 * s, cy + 9 * s, cx + 17 * s, cy + 21 * s), 3, fill=CORAL)

def cross_ic(c, cx, cy, r, col=IVORY, bg=None):
    if bg:
        c.ell((cx - r, cy - r, cx + r, cy + r), fill=bg)
    c.rrect((cx - r * .22, cy - r * .62, cx + r * .22, cy + r * .62), 3, fill=col)
    c.rrect((cx - r * .62, cy - r * .22, cx + r * .62, cy + r * .22), 3, fill=col)

def ins_card(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 36 * s, cx + 56 * s, cy + 36 * s), 10 * s, fill=IVORY)
    c.rrect((cx - 56 * s, cy - 36 * s, cx + 56 * s, cy - 14 * s), 10 * s, fill=(110, 170, 200))
    c.d.rectangle(c._b((cx - 56 * s, cy - 24 * s, cx + 56 * s, cy - 14 * s)), fill=(110, 170, 200))
    for k in range(2):
        c.rrect((cx - 42 * s, cy + (-2 + k * 18) * s, cx + (14 - k * 18) * s, cy + (6 + k * 18) * s), 3, fill=(180, 190, 184))
    cross_ic(c, cx + 36 * s, cy + 12 * s, 14 * s, IVORY, (110, 170, 200))

def common2(img, t, text):
    common(img, t, text)
    s, a, p = pop(t, 0.2, 0.4)
    put(img, num_badge(1, 120, 70), 96, 78, scale=s, alpha=a, shadow=5)

# ============================================================ BLOCCO 6
def chip6(kind):
    def mk():
        if kind == "not":
            w, h = 780, 230
            c = Cv(w, h)
            c.rrect((4, 4, w - 4, h - 4), 44, fill=PANEL_FILL, outline=CORAL, width=8)
            c.ell((34, 41, 188, 195), fill=GREEN_L)
            ins_card(c, 111, 118, 0.95)
            c.ell((46, 53, 176, 183), outline=CORAL, width=12)
            c.line([(64, 71), (158, 165)], CORAL, 12)
            c.text((232, 80), "THIS IS NOT", FONT_SANS, 42, SAGE, anchor="lm", track=2)
            c.text((232, 150), "INSURANCE", FONT_SANS, 82, CORAL, anchor="lm")
        else:
            w, h = 880, 230
            c = Cv(w, h)
            c.rrect((4, 4, w - 4, h - 4), 44, fill=GREEN_L, outline=SAGE, width=8)
            c.ell((34, 41, 188, 195), fill=GREEN_D)
            bottle(c, 111, 120, 0.85)
            c.text((216, 84), "FREE DISCOUNT PROGRAM", FONT_SANS, 40, IVORY, anchor="lm")
            c.text((216, 146), "ON PRESCRIPTION DRUGS", FONT_SANS, 38, GOLD, anchor="lm")
        return c.done()
    return cache(("chip6", kind), mk)

def draw6(img, t):
    ts = starts(6)
    common(img, t, "SAVING NUMBER 1")
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(1), 330, 330, scale=0.85 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 330, n=14, seed=3, rad=250)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("MEMBER PRESCRIPTION", FONT_SANS, 84, IVORY), 590, 280, 84, alpha=h1)
        put_left(img, tspr("PROGRAM", FONT_SANS, 104, GOLD), 590, 385, 104, alpha=h1)
    r = pop(t, ts[2], 0.45)
    if r[2] > 0:
        put(img, pill_spr("THE BIGGEST ONE FOR MANY SENIORS", 40, 900, 90, GOLD, GREEN_D), 590 + 450, 520, scale=r[0], alpha=r[1], shadow=8)
    n = pop(t, ts[3], 0.45)
    if n[2] > 0:
        put(img, chip6("not"), 500, 790, scale=n[0], alpha=n[1], shadow=12)
    f = pop(t, ts[4], 0.45)
    if f[2] > 0:
        put(img, chip6("free"), 1400, 790, scale=f[0], alpha=f[1], shadow=12)
        burst(img, t, ts[4] + 0.2, 1400, 790, n=10, seed=7, rad=220)

# ============================================================ BLOCCO 7
def price_panel():
    def mk():
        w, h = 800, 570
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 40, fill=PANEL_FILL, outline=SAGE_D, width=5)
        c.text((w / 2, 52), "THE SAME DRUG", FONT_SANS, 36, GOLD, track=4)
        c.line([(60, 480), (w - 60, 480)], SAGE_D, 5)
        c.text((250, 528), "REGULAR PRICE", FONT_SANS, 32, IVORY)
        c.text((560, 528), "MEMBER PRICE", FONT_SANS, 32, GOLD)
        return c.done()
    return cache("pp", mk)

def chip7(kind):
    def mk():
        if kind == "dep":
            w, h = 800, 150
            c = Cv(w, h)
            c.rrect((4, 4, w - 4, h - 4), 40, fill=GOLD, outline=(168, 118, 40), width=5)
            bottle(c, 90, 82, 0.62)
            c.text((160, h / 2 + 2), "DEPENDS ON THE DRUG", FONT_SANS, 50, GREEN_D, anchor="lm")
        else:
            w, h = 900, 180
            c = Cv(w, h)
            c.rrect((4, 4, w - 4, h - 4), 40, fill=PANEL_FILL, outline=CORAL, width=8)
            warn_tri(c, 92, h / 2 + 2, 0.95, CORAL, PANEL_FILL)
            c.text((176, 62), "NOT A PROMISE FOR", FONT_SANS, 48, IVORY, anchor="lm")
            c.text((176, 122), "EVERY MEDICATION", FONT_SANS, 52, CORAL, anchor="lm")
        return c.done()
    return cache(("chip7", kind), mk)

def draw7(img, t):
    ts = starts(7)
    common2(img, t, "HOW MUCH CAN YOU SAVE?")
    pn = pop(t, 0.3, 0.5)
    put(img, price_panel(), 500, 430, scale=pn[0], alpha=pn[1], shadow=18)
    d = ImageDraw.Draw(img)
    base = 430 - 285 + 480
    g1 = ease(seg(t, ts[0] + 0.3, 0.8)); g2 = ease(seg(t, ts[0] + 1.3, 0.9))
    if g1 > 0:
        h1 = 330 * g1
        d.rounded_rectangle([270, base - h1, 430, base], radius=16, fill=IVORY, outline=SAGE, width=3)
    if g2 > 0:
        h2 = (330 - 330 * 0.8 * g2)       # il prezzo scende fino al 20 percento
        d.rounded_rectangle([580, base - h2, 740, base], radius=16, fill=GOLD, outline=(168, 118, 40), width=3)
    ar = seg(t, ts[0] + 2.2, 0.5)
    if ar > 0:
        put(img, arrow_spr(), 505, 420, scale=1.15 * max(ease_back(ar), 0.01), rot=-48, alpha=min(1, ar * 3))
    u = fade(t, ts[1] + 0.2)
    if u > 0:
        put(img, tspr("UP TO", FONT_SANS, 70, SAGE, track=4), 1390, 215, alpha=u)
    p80 = pop(t, ts[1] + 0.2, 0.55)
    if p80[2] > 0:
        put(img, tspr("80%", FONT_SERIF, 320, GOLD), 1390, 410, scale=p80[0], alpha=p80[1])
        burst(img, t, ts[1] + 0.5, 1390, 410, n=14, seed=2, rad=260)
    om = fade(t, ts[1] + 0.9)
    if om > 0:
        put(img, tspr("OR MORE", FONT_SANS, 84, IVORY, track=4), 1390, 590, alpha=om)
    ck = pop(t, ts[4], 0.45)
    if ck[2] > 0:
        put(img, pill_spr("CHECK YOUR OWN", 46, 560, 96, IVORY, GREEN_D, GOLD), 1390, 725, scale=ck[0], alpha=ck[1], shadow=8)
    dp = pop(t, ts[2], 0.45)
    if dp[2] > 0:
        put(img, chip7("dep"), 500, 905, scale=dp[0], alpha=dp[1], shadow=10)
    nm = pop(t, ts[3], 0.45)
    if nm[2] > 0:
        put(img, chip7("not"), 1420, 905, scale=nm[0], alpha=nm[1], shadow=10)

# ============================================================ BLOCCO 8
def card8(i):
    def mk():
        w, h = 410, 420
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=SAGE_D, width=6)
        cx, cy = w / 2, 130
        c.ell((cx - 92, cy - 92, cx + 92, cy + 92), fill=GREEN_L)
        if i == 0:      # modulo
            c.rrect((cx - 42, cy - 58, cx + 42, cy + 58), 10, fill=IVORY)
            for k in range(4):
                c.rrect((cx - 28, cy - 38 + k * 22, cx + 28 - (k % 2) * 14, cy - 30 + k * 22), 3, fill=(176, 188, 180))
            c.line([(cx + 20, cy + 52), (cx + 62, cy + 6)], GOLD, 12)
        elif i == 1:    # moneta
            c.ell((cx - 52, cy - 52, cx + 52, cy + 52), fill=GOLD, outline=(168, 118, 40), width=5)
            c.text((cx, cy + 3), "$", FONT_SANS, 74, GREEN_D)
        elif i == 2:    # assicurazione
            ins_card(c, cx, cy, 1.1)
        else:           # coupon con forbici
            c.rrect((cx - 62, cy - 34, cx + 62, cy + 34), 10, fill=IVORY, outline=GOLD, width=4)
            for k in range(5):
                c.rrect((cx - 50 + k * 22, cy - 6, cx - 38 + k * 22, cy + 6), 2, fill=GOLD)
            c.line([(cx - 4, cy + 38), (cx + 40, cy + 62)], IVORY, 9); c.line([(cx - 4, cy + 62), (cx + 40, cy + 38)], IVORY, 9)
        c.ell((cx - 92, cy - 92, cx + 92, cy + 92), outline=CORAL, width=13)
        c.line([(cx - 65, cy - 65), (cx + 65, cy + 65)], CORAL, 13)
        l1, l2 = (("NO", "SIGN UP"), ("NO", "EXTRA FEE"), ("NO", "INSURANCE"), ("NO", "COUPONS"))[i]
        c.text((cx, 262), l1, FONT_SANS, 54, CORAL)
        c.text((cx, 330), l2, FONT_SANS, 56, GOLD)
        return c.done()
    return cache(("c8", i), mk)

def banner8():
    def mk():
        w, h = 1640, 190
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 60, fill=GOLD, outline=(168, 118, 40), width=5)
        card = card_spr()
        mini = card.resize((int(card.width * 0.3), int(card.height * 0.3)), Image.LANCZOS)
        im = c.done()
        im.paste(mini, (50, (h - mini.height) // 2), mini)
        c2 = Cv(w, h)
        c2.text((290, h / 2 + 2), "JUST SHOW YOUR CARD AT THE PHARMACY", FONT_SANS, 50, GREEN_D, anchor="lm")
        cross_ic(c2, w - 110, h / 2, 62, IVORY, GREEN_L)
        d = c2.done()
        im.paste(d, (0, 0), d)
        return im
    return cache("b8", mk)

def draw8(img, t):
    ts = starts(8)
    common2(img, t, "WHAT YOU NEED")
    for i, k in enumerate((0, 1, 3, 4)):
        s, a, pr = pop(t, ts[k], 0.45)
        if pr > 0:
            put(img, card8(i), 255 + i * 470, 355, scale=s, alpha=a, shadow=14)
    bn = pop(t, ts[2], 0.5)
    if bn[2] > 0:
        put(img, banner8(), 960, 850, scale=bn[0], alpha=bn[1], shadow=14)
        burst(img, t, ts[2] + 0.3, 960, 850, n=10, seed=6, rad=300)

# ============================================================ BLOCCO 9
def warehouse():
    def mk():
        w, h = 520, 400
        c = Cv(w, h)
        c.rrect((10, 110, w - 10, h - 10), 18, fill=IVORY, outline=SAGE_D, width=5)
        c.rrect((0, 60, w, 150), 12, fill=GREEN_D)
        c.text((w / 2, 106), "COSTCO", FONT_SANS, 70, IVORY, track=8)
        for k in range(3):
            x0 = 50 + k * 150
            c.rrect((x0, 230, x0 + 120, h - 10), 6, fill=(190, 200, 192))
            for yy in range(250, h - 20, 22):
                c.line([(x0 + 6, yy), (x0 + 114, yy)], (160, 172, 164), 3)
        c.poly([(0, 62), (w, 62), (w - 40, 20), (40, 20)], fill=GREEN_L)
        return c.done()
    return cache("wh", mk)

def storefront():
    def mk():
        w, h = 180, 170
        c = Cv(w, h)
        c.rrect((10, 50, w - 10, h - 6), 10, fill=CARD, outline=GOLD, width=4)
        for k in range(6):
            c.poly([(8 + k * 27, 14), (8 + (k + 1) * 27, 14), (12 + (k + 1) * 27, 56), (4 + k * 27, 56)],
                   fill=CORAL if k % 2 == 0 else IVORY)
        c.rrect((w / 2 - 20, 116, w / 2 + 20, h - 6), 5, fill=GREEN_L)
        cross_ic(c, w / 2, 84, 22, IVORY, GREEN_L)
        return c.done()
    return cache("sf", mk)

def draw9(img, t):
    ts = starts(9)
    common(img, t, "WHERE IT WORKS")
    a0 = fade(t, 0.4) * (1 - fade(t, ts[1] - 0.1, 0.35))
    if a0 > 0:
        put(img, tspr("THE PART", FONT_SANS, 130, IVORY), 960, 400 - 30 * (1 - a0), alpha=a0)
        put(img, tspr("MOST PEOPLE MISS", FONT_SANS, 130, GOLD), 960, 550 - 30 * (1 - a0), alpha=a0)
    w = pop(t, ts[1] + 0.1, 0.5)
    if w[2] > 0:
        put(img, warehouse(), 340, 400, scale=0.9 * w[0], alpha=w[1], shadow=16)
        put(img, pill_spr("WORKS AT COSTCO", 38, 470, 84, GREEN_L, IVORY, SAGE), 340, 640, scale=w[0], alpha=w[1], shadow=8)
    ar = seg(t, ts[1] + 1.6, 0.5)
    if ar > 0:
        put(img, arrow_spr(), 690, 400, scale=1.3 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    ph = ts[2]
    for i in range(12):
        s, a, pr = pop(t, ph + i * 0.2, 0.35)
        if pr > 0:
            col, row = i % 4, i // 4
            put(img, storefront(), 940 + col * 215, 245 + row * 185, scale=s, alpha=a, shadow=6)
    cp = fade(t, ph + 1.6)
    if cp > 0:
        put(img, pill_spr("THOUSANDS OF PARTICIPATING PHARMACIES", 40, 1200, 96, GOLD, GREEN_D), 1240, 790, alpha=cp)
    ic = pop(t, ts[3], 0.4)
    if ic[2] > 0:
        put(img, tspr("INCLUDING CHAINS LIKE", FONT_SANS_M, 42, SAGE, track=3), 440, 940, alpha=ic[1])
        put(img, pill_spr("WALGREENS", 48, 430, 100, IVORY, GREEN_D, GOLD), 1080, 940, scale=ic[0], alpha=ic[1], shadow=8)
    kr = pop(t, ts[3] + 0.5, 0.4)
    if kr[2] > 0:
        put(img, pill_spr("KROGER", 48, 360, 100, IVORY, GREEN_D, GOLD), 1500, 940, scale=kr[0], alpha=kr[1], shadow=8)

# ============================================================ BLOCCO 10
def browser10(url, stxt, results):
    def mk():
        w, h = 900, 580
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=IVORY, outline=SAGE_D, width=5)
        c.rrect((3, 3, w - 3, 78), 30, fill=(214, 224, 214))
        c.d.rectangle(c._b((3, 40, w - 3, 78)), fill=(214, 224, 214))
        for i, col in enumerate(((214, 108, 96), GOLD, (110, 190, 130))):
            c.ell((30 + i * 36, 28, 52 + i * 36, 50), fill=col)
        c.rrect((170, 18, w - 40, 62), 22, fill=IVORY)
        c.text((196, 41), url if url else "", FONT_SANS_M, 30, GREEN_D, anchor="lm")
        c.d.rectangle(c._b((3, 78, w - 3, 148)), fill=GREEN_D)
        c.text((40, 113), "MEMBER PRESCRIPTION PROGRAM", FONT_SANS, 32, IVORY, anchor="lm", track=2)
        c.rrect((40, 176, w - 40, 250), 18, fill=(238, 232, 214), outline=GOLD, width=4)
        magnifier(c, 82, 211, 14, GREEN_D, 6)
        if stxt:
            c.text((120, 213), stxt, FONT_SANS_M, 34, GREEN_D, anchor="lm")
        else:
            c.text((120, 213), "Medication name", FONT_SANS_M, 34, (160, 168, 160), anchor="lm")
        if results:
            names = ("PHARMACY A", "PHARMACY B", "PHARMACY C")
            lens = (600, 470, 330)
            for i, (nm, ln) in enumerate(zip(names, lens)):
                y = 292 + i * 80
                c.text((46, y + 26), nm, FONT_SANS, 28, GREEN_D, anchor="lm")
                best = i == 2
                c.rrect((300, y + 4, 300 + ln * 0.9, y + 48), 14, fill=GOLD if best else (196, 206, 198))
                if best:
                    check_ic(c, 300 + ln * 0.9 + 44, y + 26, 0.55, GREEN_L)
        return c.done()
    return cache(("b10", url, stxt, results), mk)

def step_row(n, l1, l2):
    def mk():
        w, h = 800, 130
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=CARD, outline=GOLD, width=5)
        c.ell((22, 19, 114, 111), fill=GOLD)
        c.text((68, 68), str(n), FONT_SERIF, 60, GREEN_D)
        c.text((144, 44), l1, FONT_SANS, 40, IVORY, anchor="lm")
        c.text((144, 90), l2, FONT_SANS, 40, GOLD, anchor="lm")
        return c.done()
    return cache(("row", n), mk)

def notepad():
    def mk():
        w, h = 340, 230
        c = Cv(w, h)
        c.rrect((6, 22, w - 6, h - 6), 18, fill=(250, 240, 190), outline=(200, 170, 80), width=4)
        for k in range(7):
            c.ell((30 + k * 42, 8, 50 + k * 42, 36), fill=GREEN_D)
        c.text((w / 2, 82), "PRICE", FONT_SANS, 54, GREEN_D)
        c.line([(46, 132), (w - 120, 134), (w - 90, 126)], CORAL_D, 6)
        for yy in (172, 204):
            c.line([(46, yy), (w - 46, yy)], (210, 190, 120), 3)
        return c.done()
    return cache("notepad", mk)

def pharmacist():
    def mk():
        S = 260
        c = Cv(S, S)
        c.ell((4, 4, S - 4, S - 4), fill=GREEN_L)
        c.ell((30, 180, S - 30, 380), fill=IVORY)
        c.poly([(104, 184), (130, 224), (156, 184)], fill=(214, 222, 214))
        c.rrect((118, 156, 142, 190), 8, fill=SKIN)
        c.ell((84, 62, 176, 170), fill=SKIN)
        c.d.pieslice(c._b((80, 52, 180, 150)), 180, 360, fill=(70, 52, 44))
        c.ell((106, 108, 118, 120), fill=GREEN_D); c.ell((142, 108, 154, 120), fill=GREEN_D)
        c.arc((106, 124, 154, 156), 20, 160, (160, 80, 70), 4)
        cross_ic(c, 172, 214, 18, IVORY, GREEN_D)
        im = c.done()
        mask = Image.new("L", (S * 2, S * 2), 0)
        ImageDraw.Draw(mask).ellipse((8, 8, S * 2 - 8, S * 2 - 8), fill=255)
        mask = mask.resize((S, S), Image.LANCZOS)
        im.putalpha(ImageChops.multiply(im.getchannel("A"), mask))
        ring = Cv(S, S)
        ring.ell((4, 4, S - 4, S - 4), outline=GOLD, width=10)
        r = ring.done()
        im.paste(r, (0, 0), r)
        return im
    return cache("pharm", mk)

STEPS = [("GO TO THE", "COSTCO WEBSITE"), ("TYPE THE NAME", "OF YOUR MEDICATION"),
         ("COMPARE PRICES", "BEFORE YOU GO"), ("WRITE DOWN", "THE PRICE"), ("ASK THE PHARMACIST", "TO CONFIRM IT")]

def draw10(img, t):
    ts = starts(10)
    common2(img, t, "HOW TO USE IT")
    # browser: indirizzo scritto con la frase 1, nome del farmaco con la frase 2, confronto con la frase 3
    full_url = "costco.com/cmpp"; full_s = "your medication"
    url = full_url[:int(len(full_url) * seg(t, ts[1] + 0.2, 1.3))]
    stxt = full_s[:int(len(full_s) * seg(t, ts[2] + 0.2, 1.4))]
    res = t >= ts[3] + 0.5
    bw = pop(t, ts[0] + 0.2, 0.5)
    put(img, browser10(url, stxt, res), 560, 440, scale=bw[0], alpha=bw[1], shadow=20)
    for i, k in enumerate((0, 2, 3, 4, 5)):
        s, a, pr = pop(t, ts[k], 0.4)
        if pr > 0:
            put(img, step_row(i + 1, *STEPS[i]), 1450, 235 + i * 150, scale=s, alpha=a, shadow=8)
    np_ = pop(t, ts[4], 0.45)
    if np_[2] > 0:
        put(img, notepad(), 330, 905, scale=np_[0], rot=-4, alpha=np_[1], shadow=10)
    ph = pop(t, ts[5], 0.45)
    if ph[2] > 0:
        put(img, pharmacist(), 610, 890, scale=0.78 * ph[0], alpha=ph[1], shadow=10)
        put(img, check_spr(), 708, 820, scale=ph[0], alpha=ph[1])
        burst(img, t, ts[5] + 0.3, 708, 820, n=8, seed=9, rad=140)
        put(img, pill_spr("CONFIRMED", 40, 300, 84, GOLD, GREEN_D), 880, 905, scale=ph[0], alpha=ph[1], shadow=8)

DRAW.update({6: draw6, 7: draw7, 8: draw8, 9: draw9, 10: draw10})

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
