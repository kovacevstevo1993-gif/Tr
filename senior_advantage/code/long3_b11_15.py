"""Video lungo 3 (Costco) - blocchi 11-15 (fine punto 1, punti 2 e 3). 1920x1080, 30 fps.
Durate dalla timeline dell'utente (07/10/2026): B11 767, B12 332, B13 533, B14 261, B15 337 fotogrammi.
Uso: OUT=cartella python3 long3_b11_15.py <blocco 11..15> [fotogrammi]
     python3 long3_b11_15.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b06_10 import *

DUR.update({11: 767, 12: 332, 13: 533, 14: 261, 15: 337})
PHRASES.update({
    11: ["Here is a simple way to do it.", "Make a list of every medication you take.", "Look up each one on that page.",
         "Then ask your pharmacist two questions:", "what is my price with my insurance,",
         "and what is my price with the Member Prescription Program?", "Choose the lower one,",
         "and ask them to explain the difference.", "Remember, the result depends on each drug,",
         "so check them one by one."],
    12: ["Two.", "The Costco pharmacy itself needs no membership.", "You can fill a prescription at a Costco pharmacy,",
         "online or in the warehouse,", "without being a member."],
    13: ["Members get the discounted member pricing.", "Non members pay the cash price,",
         "and they can pay with cash, a debit card, a Costco shop card or a Visa card.",
         "So if you are helping a parent or a friend who does not have a card,", "this is a door that is open to them."],
    14: ["The pharmacy also works online.", "If walking through a big warehouse is hard for you,",
         "you can order your prescription online,", "from home."],
    15: ["Three.", "The hearing aid center.", "If your hearing is changing, start here.",
         "The hearing test is free for members,", "it is done in a sound booth, and it takes about an hour."],
})

def common3(img, t, text, n=None):
    common(img, t, text)
    if n:
        s, a, p = pop(t, 0.2, 0.4)
        put(img, num_badge(n, 120, 70), 96, 78, scale=s, alpha=a, shadow=5)

def intro(img, t, l1, l2, until, y=(400, 550), size=130):
    a0 = fade(t, 0.4) * (1 - fade(t, until - 0.1, 0.35))
    if a0 > 0:
        put(img, tspr(l1, FONT_SANS, size, IVORY), 960, y[0] - 30 * (1 - a0), alpha=a0)
        put(img, tspr(l2, FONT_SANS, size, GOLD), 960, y[1] - 30 * (1 - a0), alpha=a0)

# ------------------------------------------------------------------ icone nuove
def laptop(c, cx, cy, s=1.0, screen=GREEN_D):
    c.rrect((cx - 100 * s, cy - 70 * s, cx + 100 * s, cy + 50 * s), 14 * s, fill=screen, outline=IVORY, width=8 * s)
    c.poly([(cx - 130 * s, cy + 62 * s), (cx + 130 * s, cy + 62 * s), (cx + 106 * s, cy + 86 * s), (cx - 106 * s, cy + 86 * s)], fill=IVORY)

def house(c, cx, cy, s=1.0):
    c.poly([(cx - 78 * s, cy - 6 * s), (cx, cy - 66 * s), (cx + 78 * s, cy - 6 * s)], fill=CORAL)
    c.rrect((cx - 60 * s, cy - 8 * s, cx + 60 * s, cy + 62 * s), 6 * s, fill=IVORY)
    c.rrect((cx - 14 * s, cy + 14 * s, cx + 14 * s, cy + 62 * s), 4 * s, fill=GREEN_L)
    c.rrect((cx + 26 * s, cy + 6 * s, cx + 50 * s, cy + 30 * s), 3 * s, fill=(150, 190, 215))

def door(c, cx, cy, s=1.0):
    c.rrect((cx - 70 * s, cy - 100 * s, cx + 70 * s, cy + 100 * s), 8 * s, fill=GOLD)
    c.rrect((cx - 56 * s, cy - 88 * s, cx + 56 * s, cy + 100 * s), 4 * s, fill=(255, 244, 205))
    c.poly([(cx - 56 * s, cy - 88 * s), (cx - 6 * s, cy - 70 * s), (cx - 6 * s, cy + 100 * s), (cx - 56 * s, cy + 100 * s)], fill=(24, 78, 62))
    c.ell((cx - 20 * s, cy + 6 * s, cx - 8 * s, cy + 18 * s), fill=GOLD)

def clock(c, cx, cy, r):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=IVORY, outline=GOLD, width=r * 0.14)
    c.line([(cx, cy), (cx, cy - r * 0.62)], GREEN_D, r * 0.12)
    c.line([(cx, cy), (cx + r * 0.46, cy + r * 0.12)], GREEN_D, r * 0.12)
    c.ell((cx - r * 0.1, cy - r * 0.1, cx + r * 0.1, cy + r * 0.1), fill=GREEN_D)

def sound_booth(c, cx, cy, s=1.0):
    c.rrect((cx - 54 * s, cy - 66 * s, cx + 54 * s, cy + 66 * s), 10 * s, fill=GREEN_D, outline=IVORY, width=7 * s)
    c.rrect((cx - 36 * s, cy - 48 * s, cx + 36 * s, cy + 22 * s), 6 * s, fill=(110, 170, 200))
    c.ell((cx - 15 * s, cy - 30 * s, cx + 15 * s, cy + 4 * s), fill=SKIN)
    c.arc((cx - 22 * s, cy - 40 * s, cx + 22 * s, cy + 6 * s), 180, 360, GOLD, 6 * s)
    c.ell((cx - 26 * s, cy - 20 * s, cx - 14 * s, cy - 4 * s), fill=GOLD); c.ell((cx + 14 * s, cy - 20 * s, cx + 26 * s, cy - 4 * s), fill=GOLD)

def chip_icon(w, h, fill, border, icon_fn, l1, l2, s1=40, s2=56, c1=IVORY, c2=GOLD, extra=None, tx=216):
    c = Cv(w, h)
    c.rrect((4, 4, w - 4, h - 4), 44, fill=fill, outline=border, width=8)
    c.ell((34, h / 2 - 77, 188, h / 2 + 77), fill=GREEN_D)
    icon_fn(c, 111, h / 2)
    c.text((tx, h / 2 - 34), l1, FONT_SANS, s1, c1, anchor="lm")
    c.text((tx, h / 2 + 28), l2, FONT_SANS, s2, c2, anchor="lm")
    if extra:
        extra(c, w, h)
    return c.done()

# ============================================================ BLOCCO 11
def panel11(i):
    def mk():
        w, h = 860, 320
        titles = ("MAKE A LIST", "LOOK IT UP", "ASK YOUR PHARMACIST", "CHOOSE THE LOWER ONE")
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=GOLD, width=5)
        c.ell((18, 14, 90, 86), fill=GOLD)
        c.text((54, 52), str(i + 1), FONT_SERIF, 46, GREEN_D)
        c.text((112, 52), titles[i], FONT_SANS, 40, IVORY, anchor="lm")
        if i == 0:
            c.text((40, 158), "EVERY MEDICATION", FONT_SANS, 36, IVORY, anchor="lm")
            c.text((40, 206), "YOU TAKE", FONT_SANS, 40, GOLD, anchor="lm")
            c.rrect((450, 98, 820, 304), 20, fill=IVORY)
            c.rrect((580, 86, 690, 112), 8, fill=GOLD)
            for k in range(3):
                y = 152 + k * 56
                bottle(c, 488, y, 0.3)
                c.rrect((528, y - 9, 730, y + 9), 8, fill=(190, 200, 192))
                check_ic(c, 770, y, 0.55, GREEN_L)
        elif i == 1:
            c.text((40, 158), "EACH ONE, ON", FONT_SANS, 36, IVORY, anchor="lm")
            c.text((40, 206), "THAT PAGE", FONT_SANS, 40, GOLD, anchor="lm")
            c.rrect((450, 98, 830, 304), 18, fill=IVORY, outline=SAGE_D, width=4)
            c.rrect((450, 98, 830, 138), 18, fill=(214, 224, 214))
            c.d.rectangle(c._b((450, 118, 830, 138)), fill=(214, 224, 214))
            c.text((476, 118), "costco.com/cmpp", FONT_SANS_M, 22, GREEN_D, anchor="lm")
            c.rrect((470, 154, 810, 204), 14, fill=(238, 232, 214), outline=GOLD, width=3)
            magnifier(c, 500, 179, 10, GREEN_D, 4)
            c.text((528, 180), "medication name", FONT_SANS_M, 24, GREEN_D, anchor="lm")
            for k in range(2):
                c.rrect((470, 226 + k * 38, 780 - k * 90, 242 + k * 38), 7, fill=(196, 206, 198))
        elif i == 2:
            ph = pharmacist().resize((170, 170), Image.LANCZOS)
            im = c.done()
            im.paste(ph, (40, 110), ph)
            return im
        else:
            c.rrect((40, 100, 640, 160), 18, fill=(196, 206, 198))
            c.text((62, 130), "INSURANCE", FONT_SANS, 30, GREEN_D, anchor="lm")
            c.rrect((40, 176, 460, 236), 18, fill=GOLD)
            c.text((62, 206), "MEMBER PROGRAM", FONT_SANS, 30, GREEN_D, anchor="lm")
        return c.done()
    return cache(("p11", i), mk)

def bubble11(text, w, fill=IVORY, ink=GREEN_D, size=28):
    def mk():
        h = 84
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=fill)
        c.text((w / 2, h / 2 + 2), text, FONT_SANS, size, ink)
        return c.done()
    return cache(("bub11", text, w, size), mk)

def strip11():
    def mk():
        w, h = 1700, 110
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 55, fill=PANEL_FILL, outline=CORAL, width=7)
        warn_tri(c, 86, h / 2 + 2, 0.7, CORAL, PANEL_FILL)
        c.text((156, h / 2 + 2), "EVERY DRUG IS DIFFERENT:", FONT_SANS, 44, IVORY, anchor="lm")
        c.text((156 + 700, h / 2 + 2), "CHECK THEM ONE BY ONE", FONT_SANS, 44, CORAL, anchor="lm")
        return c.done()
    return cache("s11", mk)

def draw11(img, t):
    ts = starts(11)
    common3(img, t, "A SIMPLE WAY TO DO IT", 1)
    intro(img, t, "HERE IS A", "SIMPLE WAY", ts[1], size=140)
    pos = ((500, 300), (1420, 300), (500, 640), (1420, 640))
    for i, k in enumerate((1, 2, 3, 6)):
        s, a, pr = pop(t, ts[k], 0.5)
        if pr > 0:
            put(img, panel11(i), pos[i][0], pos[i][1], scale=s, alpha=a, shadow=14)
    # domande al farmacista
    pa = pop(t, ts[4], 0.4)
    if pa[2] > 0:
        put(img, bubble11("PRICE WITH MY INSURANCE?", 590), 595, 610, scale=pa[0], alpha=pa[1], shadow=6)
    pb = pop(t, ts[5], 0.4)
    if pb[2] > 0:
        put(img, bubble11("PRICE WITH THE MEMBER PROGRAM?", 590, GOLD), 595, 712, scale=pb[0], alpha=pb[1], shadow=6)
    # scelta del prezzo piu basso
    ck = pop(t, ts[6] + 1.0, 0.4)
    if ck[2] > 0:
        put(img, check_spr(), 1990 - 500, 682, scale=0.9 * ck[0], alpha=ck[1])
        burst(img, t, ts[6] + 1.2, 1490, 682, n=8, seed=3, rad=130)
    ex = pop(t, ts[7], 0.45)
    if ex[2] > 0:
        put(img, pill_spr("ASK THEM TO EXPLAIN THE DIFFERENCE", 30, 790, 56, IVORY, GREEN_D, GOLD), 1420, 754, scale=ex[0], alpha=ex[1], shadow=6)
    sp = pop(t, ts[8], 0.5)
    if sp[2] > 0:
        put(img, strip11(), 960, 915, scale=sp[0], alpha=sp[1], shadow=10)

# ============================================================ BLOCCO 12
def draw12(img, t):
    ts = starts(12)
    common(img, t, "SAVING NUMBER 2")
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(2), 330, 330, scale=0.85 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 330, n=14, seed=3, rad=250)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("THE COSTCO PHARMACY", FONT_SANS, 84, IVORY), 590, 280, 84, alpha=h1)
        put_left(img, tspr("NEEDS NO MEMBERSHIP", FONT_SANS, 84, GOLD), 590, 385, 84, alpha=h1)
    r = pop(t, ts[2], 0.45)
    if r[2] > 0:
        put(img, pill_spr("FILL A PRESCRIPTION THERE", 40, 800, 90, GOLD, GREEN_D), 590 + 400, 520, scale=r[0], alpha=r[1], shadow=8)
    on = pop(t, ts[3], 0.45)
    if on[2] > 0:
        put(img, cache("c12on", lambda: chip_icon(840, 230, GREEN_L, SAGE, lambda c, x, y: laptop(c, x, y + 4, 0.5),
                                                   "FILL IT", "ONLINE", 40, 66)), 480, 690, scale=on[0], alpha=on[1], shadow=12)
    wh = pop(t, ts[3] + 0.6, 0.45)
    if wh[2] > 0:
        def wh_icon(c, x, y):
            c.rrect((x - 44, y - 8, x + 44, y + 44), 6, fill=IVORY)
            c.rrect((x - 52, y - 40, x + 52, y - 2), 6, fill=GOLD)
            for k in range(3):
                c.rrect((x - 36 + k * 26, y + 6, x - 16 + k * 26, y + 44), 3, fill=(170, 182, 174))
        put(img, cache("c12wh", lambda: chip_icon(840, 230, GREEN_L, SAGE, wh_icon, "FILL IT IN", "THE WAREHOUSE", 40, 56)),
            1440, 690, scale=wh[0], alpha=wh[1], shadow=12)
    nm = pop(t, ts[4], 0.5)
    if nm[2] > 0:
        def nm_icon(c, x, y):
            c.rrect((x - 44, y - 28, x + 44, y + 28), 8, fill=GOLD)
            c.rrect((x - 44, y - 14, x + 44, y - 4), 0, fill=(196, 146, 72))
            c.ell((x - 70, y - 70, x + 70, y + 70), outline=CORAL, width=10)
            c.line([(x - 50, y - 50), (x + 50, y + 50)], CORAL, 10)
        put(img, cache("c12nm", lambda: chip_icon(1300, 170, PANEL_FILL, CORAL, nm_icon, "WITHOUT BEING", "A MEMBER", 40, 62, c2=CORAL)),
            960, 930, scale=nm[0], alpha=nm[1], shadow=12)

# ============================================================ BLOCCO 13
def who_panel(kind):
    def mk():
        w, h = 840, 270
        c = Cv(w, h)
        if kind == "mem":
            c.rrect((4, 4, w - 4, h - 4), 44, fill=GREEN_L, outline=GOLD, width=8)
            card = card_spr()
            mini = card.resize((int(card.width * 0.36), int(card.height * 0.36)), Image.LANCZOS)
            im = c.done()
            im.paste(mini, (44, (h - mini.height) // 2), mini)
            c2 = Cv(w, h)
            c2.text((290, 84), "MEMBERS", FONT_SANS, 44, SAGE, anchor="lm", track=3)
            c2.text((290, 160), "MEMBER", FONT_SANS, 70, GOLD, anchor="lm")
            c2.text((290, 220), "PRICING", FONT_SANS, 56, IVORY, anchor="lm")
            d = c2.done()
            im.paste(d, (0, 0), d)
            return im
        c.rrect((4, 4, w - 4, h - 4), 44, fill=PANEL_FILL, outline=SAGE_D, width=8)
        c.ell((44, 50, 244, 220), fill=GREEN_L)
        person_ic(c, 144, 134, 1.2, SAGE_D)
        c.text((290, 84), "NON MEMBERS", FONT_SANS, 44, SAGE, anchor="lm", track=3)
        c.text((290, 160), "CASH", FONT_SANS, 70, IVORY, anchor="lm")
        c.text((290, 220), "PRICE", FONT_SANS, 56, GOLD, anchor="lm")
        return c.done()
    return cache(("who", kind), mk)

def pay_tile(i):
    def mk():
        w, h = 400, 210
        names = ("CASH", "DEBIT CARD", "SHOP CARD", "VISA CARD")
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=CARD, outline=GOLD, width=5)
        cx, cy = w / 2, 88
        if i == 0:
            c.rrect((cx - 90, cy - 44, cx + 90, cy + 44), 10, fill=(120, 190, 140), outline=(70, 140, 96), width=4)
            c.ell((cx - 28, cy - 28, cx + 28, cy + 28), fill=(210, 240, 214))
            c.text((cx, cy + 2), "$", FONT_SANS, 44, (50, 110, 70))
        else:
            fill = ((210, 218, 214), (236, 188, 108), (50, 90, 140))[i - 1]
            c.rrect((cx - 82, cy - 52, cx + 82, cy + 52), 14, fill=fill)
            c.rrect((cx - 82, cy - 28, cx + 82, cy - 8), 0, fill=GREEN_D if i == 1 else (150, 105, 40) if i == 2 else (20, 40, 80))
            c.rrect((cx - 62, cy + 6, cx - 24, cy + 32), 5, fill=(220, 170, 80))
            if i == 3:
                c.text((cx + 34, cy + 26), "VISA CARD", FONT_SANS_M, 16, IVORY)
        c.text((cx, 172), names[i], FONT_SANS, 38, IVORY)
        return c.done()
    return cache(("pay", i), mk)

def draw13(img, t):
    ts = starts(13)
    common3(img, t, "WHO PAYS WHAT", 2)
    m = pop(t, ts[0], 0.5)
    if m[2] > 0:
        put(img, who_panel("mem"), 500, 280, scale=m[0], alpha=m[1], shadow=14)
    n = pop(t, ts[1], 0.5)
    if n[2] > 0:
        put(img, who_panel("non"), 1420, 280, scale=n[0], alpha=n[1], shadow=14)
    for i in range(4):
        s, a, pr = pop(t, ts[2] + 0.25 + i * 0.7, 0.4)
        if pr > 0:
            put(img, pay_tile(i), 270 + i * 460, 560, scale=s, alpha=a, shadow=8)
    hp = pop(t, ts[3], 0.5)
    if hp[2] > 0:
        def hp_icon(c, x, y):
            person_ic(c, x - 30, y + 8, 0.8, (190, 140, 66))
            person_ic(c, x + 34, y + 20, 0.62, SAGE, head=(226, 190, 160))
        put(img, cache("c13hp", lambda: chip_icon(800, 220, PANEL_FILL, SAGE_D, hp_icon, "HELPING A PARENT", "OR A FRIEND", 38, 52)),
            470, 880, scale=hp[0], alpha=hp[1], shadow=10)
    dr = pop(t, ts[4], 0.5)
    if dr[2] > 0:
        put(img, cache("c13dr", lambda: chip_icon(900, 220, GREEN_L, GOLD, lambda c, x, y: door(c, x, y + 2, 0.5),
                                                  "THIS DOOR IS", "OPEN TO THEM", 40, 62)),
            1380, 880, scale=dr[0], alpha=dr[1], shadow=10)
        burst(img, t, ts[4] + 0.3, 1380, 880, n=10, seed=4, rad=260)

# ============================================================ BLOCCO 14
def scene14(kind):
    def mk():
        w, h = (820, 560) if kind == "walk" else (860, 560)
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 44, fill=CARD, outline=SAGE_D if kind == "walk" else GOLD, width=6)
        if kind == "walk":
            wh = warehouse().resize((380, 292), Image.LANCZOS)
            im = c.done()
            im.paste(wh, (390, 80), wh)
            bd = senior_badge().resize((190, 190), Image.LANCZOS)
            im.paste(bd, (60, 130), bd)
            c2 = Cv(w, h)
            for k in range(5):
                c2.ell((262 + k * 22, 268, 274 + k * 22, 280), fill=GOLD)
            c2.text((w / 2, 424), "BIG WAREHOUSE,", FONT_SANS, 46, IVORY)
            c2.text((w / 2, 486), "HARD TO WALK?", FONT_SANS, 58, CORAL)
            d = c2.done()
            im.paste(d, (0, 0), d)
            return im
        laptop(c, w / 2, 190, 1.55, GREEN_D)
        cx, cy = w / 2, 150
        bottle(c, cx - 110, cy + 2, 0.7)
        c.rrect((cx - 40, cy - 40, cx + 150, cy - 10), 8, fill=(196, 206, 198))
        c.rrect((cx - 40, cy + 6, cx + 120, cy + 30), 8, fill=(150, 160, 152))
        c.rrect((cx - 20, cy + 52, cx + 130, cy + 98), 22, fill=GOLD)
        c.text((cx + 55, cy + 76), "ORDER", FONT_SANS, 30, GREEN_D)
        return c.done()
    return cache(("sc14", kind), mk)

def draw14(img, t):
    ts = starts(14)
    common(img, t, "ORDER FROM HOME")
    h1 = pop(t, 0.3, 0.5)
    put(img, tspr("THE PHARMACY", FONT_SANS, 96, IVORY), 960, 190, scale=h1[0], alpha=h1[1])
    put(img, tspr("ALSO WORKS ONLINE", FONT_SANS, 96, GOLD), 960, 300, scale=h1[0], alpha=h1[1])
    w = pop(t, ts[1], 0.5)
    if w[2] > 0:
        put(img, scene14("walk"), 480, 700, scale=w[0], alpha=w[1], shadow=14)
    l = pop(t, ts[2], 0.5)
    if l[2] > 0:
        put(img, scene14("online"), 1420, 700, scale=l[0], alpha=l[1], shadow=14)
        ar = seg(t, ts[2] - 0.1, 0.4)
        put(img, arrow_spr(), 940, 700, scale=0.9 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    hm = pop(t, ts[3], 0.45)
    if hm[2] > 0:
        def hs():
            c = Cv(190, 160); house(c, 95, 84, 1.0); return c.done()
        put(img, cache("hs14", hs), 1180, 868, scale=hm[0], alpha=hm[1], shadow=8)
        put(img, pill_spr("FROM HOME", 52, 520, 104, GOLD, GREEN_D), 1560, 875, scale=hm[0], alpha=hm[1], shadow=8)
        burst(img, t, ts[3] + 0.2, 1560, 875, n=10, seed=2, rad=200)

# ============================================================ BLOCCO 15
def draw15(img, t):
    ts = starts(15)
    common(img, t, "SAVING NUMBER 3")
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(3), 330, 330, scale=0.85 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 330, n=14, seed=3, rad=250)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("THE HEARING", FONT_SANS, 100, IVORY), 590, 280, 100, alpha=h1)
        put_left(img, tspr("AID CENTER", FONT_SANS, 100, GOLD), 590, 395, 100, alpha=h1)
    r = pop(t, ts[2], 0.45)
    if r[2] > 0:
        put(img, pill_spr("HEARING CHANGING? START HERE", 40, 960, 92, GOLD, GREEN_D), 590 + 480, 540, scale=r[0], alpha=r[1], shadow=8)
    f = pop(t, ts[3], 0.45)
    if f[2] > 0:
        put(img, cache("c15f", lambda: chip_icon(780, 230, GREEN_L, SAGE, ic_hear, "HEARING TEST", "FREE FOR MEMBERS", 44, 44)),
            500, 800, scale=f[0], alpha=f[1], shadow=12)
        burst(img, t, ts[3] + 0.2, 500, 800, n=10, seed=7, rad=220)
    bo = pop(t, ts[4], 0.45)
    if bo[2] > 0:
        def bo_extra(c, w, h):
            clock(c, w - 100, h / 2, 50)
        put(img, cache("c15b", lambda: chip_icon(880, 230, GREEN_L, SAGE, lambda c, x, y: sound_booth(c, x, y, 0.85),
                                                  "DONE IN A SOUND BOOTH", "ABOUT AN HOUR", 34, 52, extra=bo_extra)),
            1400, 800, scale=bo[0], alpha=bo[1], shadow=12)

DRAW.update({11: draw11, 12: draw12, 13: draw13, 14: draw14, 15: draw15})

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
