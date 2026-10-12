"""Video lungo 5 (AEROPORTO) - blocchi 6-15. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AEROPORTO.md.
Durate dalla timeline dell'utente (12/10/2026): B6 424, B7 279, B8 358, B9 281, B10 261, B11 413, B12 270, B13 402, B14 436, B15 472.
Uso: OUT=cartella python3 long5_b06_15.py <blocco> [fotogrammi]
     python3 long5_b06_15.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long5_b01_05 import *      # motore, icone, banner, txt, seq, slide_in, panel, stamp, license helpers

DUR = {6: 424, 7: 279, 8: 358, 9: 281, 10: 261, 11: 413, 12: 270, 13: 402, 14: 436, 15: 472}
PHRASES = {
    6: ["One more thing before we start.", "Everything in this video comes from official pages,", "T S A dot gov and the federal rules for airlines.",
        "No guesses, no rumors.", "Rules change, so confirm before you travel."],
    7: ["Number one.", "Your photo I D.", "Since May seventh, twenty twenty five,", "to fly inside the country,", "you need a Real I D, or a passport."],
    8: ["Look at your driver's license right now.", "A star in the corner,", "or the word Enhanced,", "means it counts.", "No star, and no passport,", "and you have a problem at the checkpoint."],
    9: ["The common mistake is thinking your old license is fine", "because it hasn't expired.", "The expiration date isn't the point.", "The star is."],
    10: ["T S A lists a forty five dollar fee", "for travelers who show up", "without an acceptable I D.", "It is much easier to check the card at home."],
    11: ["Who does this hit hardest?", "Older drivers who haven't renewed in years,", "and people who never needed a passport.",
         "You get a Real I D through your state's motor vehicle office,", "so don't wait until the week of your trip."],
    12: ["So here's your action.", "Take out your license tonight.", "Look for the star.", "If it's not there,", "call your state motor vehicle office."],
    13: ["Number two.", "Help getting through the airport.", "Federal rules say that if you have a disability,", "the airline must provide or arrange help",
         "moving from the terminal entrance to your gate,", "and from your gate back out."],
    14: ["That includes help making a connection between two gates.", "It includes a short stop at a restroom on the way,", "if you ask.",
         "And if you can't carry your bags because of your disability,", "the airline has to help with the luggage."],
    15: ["Now, here is the honest part.", "These rules are about disability,", "not about your birthday.", "Being over sixty is not enough by itself.",
         "But if walking far is hard,", "or standing for a long time is hard,", "this is for you."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

GREEN_OK = (110, 200, 130)
NAVY = (36, 66, 120)

# ------------------------------------------------------------------ sprite comuni
def badge(n):
    return sprite(("badge5", n), 120, 120, lambda c: (c.ell((4, 4, 116, 116), fill=GOLD, outline=(168, 118, 40), width=6), c.text((60, 64), str(n), FONT_SERIF, 76, GREEN_D)))

def show_badge(img, t, n):
    seq(img, t, 0.1, badge(n), 110, 130, shadow=6)

def chip(text, w, h, col, mark=None, size=40, fill=PANEL_FILL):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), h / 2, fill=fill, outline=col, width=6)
        off = 0
        if mark == "x":
            ic_x(c, 56, h / 2, 0.55, RED, 14); off = 40
        elif mark == "ok":
            check_ic(c, 56, h / 2, 0.8, GREEN_OK); off = 40
        c.text((w / 2 + off, h / 2 + 2), text, FONT_SANS, size, col if mark is None else IVORY, track=1)
    return sprite(("chip5", text, w, h, col, mark, size, fill), w, h, fn)

def license_spr(slot=False, w=760, h=470):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 26, fill=IVORY, outline=(206, 200, 186), width=5)
        c.rrect((4, 4, w - 4, 94), 26, fill=GREEN_L)
        c.d.rectangle(c._b((4, 60, w - 4, 94)), fill=GREEN_L)
        c.text((230, 50), "DRIVER LICENSE", FONT_SANS, 40, IVORY, track=3)
        c.rrect((40, 124, 250, 374), 14, fill=(214, 204, 192))
        c.ell((100, 158, 190, 248), fill=SKIN)
        c.d.pieslice(c._b((62, 236, 228, 400)), 180, 360, fill=SAGE_D)
        for k, wd in enumerate((330, 270, 300)):
            c.rrect((290, 130 + k * 46, 290 + wd, 150 + k * 46), 8, fill=(206, 212, 206))
        c.text((290, 312), "EXPIRES 11/2029", FONT_SANS, 34, GREEN_D, anchor="lm")
        c.rrect((290, 346, 560, 366), 8, fill=(206, 212, 206))
        if slot:
            for k in range(0, 360, 36):
                c.arc((w - 130, 14, w - 62, 82), k, k + 20, SAGE, 5)
    return sprite(("lic5", slot, w, h), w, h, fn)

def star_gold(r=34):
    return sprite(("stargold5", r), r * 2 + 8, r * 2 + 8, lambda c: star5(c, r + 4, r + 4, r, GOLD))

def passport_spr(w=360, h=250, dim=False):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 20, fill=NAVY if not dim else (40, 56, 80), outline=GOLD, width=5)
        c.ell((w / 2 - 50, 30, w / 2 + 50, 130), outline=GOLD, width=5)
        star5(c, w / 2, 80, 28, GOLD)
        c.text((w / 2, h - 50), "PASSPORT", FONT_SANS, 38, GOLD, track=3)
    return sprite(("pass5", w, h, dim), w, h, fn)

def realid_card(w=520, h=300):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 26, fill=IVORY, outline=GOLD, width=7)
        star5(c, w - 90, 80, 52, GOLD)
        c.text((40, h / 2 + 10), "REAL I D", FONT_SANS, 82, GREEN_D, anchor="lm")
        c.rrect((40, h - 62, 330, h - 42), 8, fill=(206, 212, 206))
    return sprite(("realid5", w, h), w, h, fn)

def cal_spr(w=300, h=340, top="MAY", day="7", yr="2025"):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 26, fill=IVORY, outline=(206, 200, 186), width=5)
        c.rrect((4, 4, w - 4, 90), 26, fill=CORAL)
        c.d.rectangle(c._b((4, 56, w - 4, 90)), fill=CORAL)
        c.text((w / 2, 50), top, FONT_SANS, 46, IVORY, track=4)
        c.text((w / 2, 195), day, FONT_SANS, 150, GREEN_D)
        c.text((w / 2, 290), yr, FONT_SANS, 50, CORAL_D, track=3)
    return sprite(("cal5", w, h, top, day, yr), w, h, fn)

def ic_door(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 66 * s, cx + 50 * s, cy + 62 * s), 8 * s, fill=(160, 112, 60), outline=GOLD, width=3)
    c.rrect((cx - 38 * s, cy - 54 * s, cx - 2 * s, cy + 62 * s), 4, fill=(190, 222, 232))
    c.rrect((cx + 2 * s, cy - 54 * s, cx + 38 * s, cy + 62 * s), 4, fill=(190, 222, 232))

def ic_gatesign(c, cx, cy, s, text="A12"):
    c.rrect((cx - 56 * s, cy - 48 * s, cx + 56 * s, cy + 48 * s), 10 * s, fill=GREEN_L, outline=GOLD, width=3)
    c.text((cx, cy - 18 * s), "GATE", FONT_SANS, 20 * s, IVORY, track=2)
    c.text((cx, cy + 16 * s), text, FONT_SANS, 40 * s, GOLD)

def ic_suitcase(c, cx, cy, s):
    c.rrect((cx - 12 * s, cy - 62 * s, cx + 12 * s, cy - 40 * s), 4, outline=SAGE, width=5)
    c.rrect((cx - 56 * s, cy - 44 * s, cx + 56 * s, cy + 52 * s), 14 * s, fill=CORAL, outline=CORAL_D, width=4)
    for dx in (-26, 26):
        c.rrect((cx + (dx - 6) * s, cy - 44 * s, cx + (dx + 6) * s, cy + 52 * s), 2, fill=CORAL_D)
    for dx in (-34, 34):
        c.ell((cx + (dx - 8) * s, cy + 52 * s, cx + (dx + 8) * s, cy + 68 * s), fill=GREEN_D)

def ic_wc(c, cx, cy, s):
    c.rrect((cx - 62 * s, cy - 62 * s, cx + 62 * s, cy + 62 * s), 14 * s, fill=NAVY, outline=IVORY, width=4)
    c.ell((cx - 32 * s, cy - 44 * s, cx - 12 * s, cy - 24 * s), fill=IVORY)
    c.rrect((cx - 40 * s, cy - 20 * s, cx - 4 * s, cy + 30 * s), 6 * s, fill=IVORY)
    c.ell((cx + 14 * s, cy - 44 * s, cx + 34 * s, cy - 24 * s), fill=IVORY)
    c.poly([(cx + 24 * s, cy - 20 * s), (cx + 46 * s, cy + 30 * s), (cx + 2 * s, cy + 30 * s)], fill=IVORY)
    c.rrect((cx - 14 * s, cy + 38 * s, cx - 6 * s, cy + 56 * s), 2, fill=IVORY)
    c.rrect((cx + 10 * s, cy + 38 * s, cx + 18 * s, cy + 56 * s), 2, fill=IVORY)

def ic_helper(c, cx, cy, s):
    c.ell((cx - 22 * s, cy - 58 * s, cx + 22 * s, cy - 14 * s), fill=SKIN)
    c.d.pieslice(c._b((cx - 44 * s, cy - 6 * s, cx + 44 * s, cy + 80 * s)), 180, 360, fill=GOLD)
    c.rrect((cx - 8 * s, cy + 10 * s, cx + 8 * s, cy + 38 * s), 2, fill=GREEN_D)
    c.rrect((cx - 20 * s, cy + 18 * s, cx + 20 * s, cy + 30 * s), 2, fill=GREEN_D)

def ic_scroll(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 62 * s, cx + 50 * s, cy + 62 * s), 8 * s, fill=IVORY, outline=(206, 200, 186), width=3)
    c.text((cx, cy - 36 * s), "14 CFR", FONT_SANS, 22 * s, GREEN_D)
    for k in range(4):
        c.rrect((cx - 34 * s, cy - 8 * s + k * 18 * s, cx + 34 * s - (k % 2) * 14 * s, cy + 2 * s + k * 18 * s), 3, fill=(206, 212, 206))

def ic_moon(c, cx, cy, s):
    c.ell((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), fill=GOLD)
    c.ell((cx - 16 * s, cy - 52 * s, cx + 56 * s, cy + 28 * s), fill=PANEL_FILL)
    star5(c, cx + 36 * s, cy - 26 * s, 10 * s, GOLD)

def ic_magnify(c, cx, cy, s):
    magnifier(c, cx - 14 * s, cy - 14 * s, 40 * s, GOLD, 10 * s)

def ic_cake(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 6 * s, cx + 50 * s, cy + 50 * s), 8 * s, fill=CORAL)
    c.rrect((cx - 50 * s, cy - 6 * s, cx + 50 * s, cy + 12 * s), 8 * s, fill=IVORY)
    for dx in (-26, 0, 26):
        c.rrect((cx + (dx - 4) * s, cy - 36 * s, cx + (dx + 4) * s, cy - 8 * s), 2, fill=GOLD)
        c.ell((cx + (dx - 8) * s, cy - 54 * s, cx + (dx + 8) * s, cy - 34 * s), fill=(246, 150, 60))

def card(w, h, border=SAGE_D):
    return panel(w, h, border=border)

def stage(img, t, ts, spr, cx, cy, **kw):
    seq(img, t, ts, spr, cx, cy, **kw)

# ============================================================ BLOCCO 6
def browser_spr(w=700, h=470):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 30, fill=(20, 56, 46), outline=SAGE_D, width=5)
        c.rrect((4, 4, w - 4, 76), 30, fill=(34, 78, 64))
        c.d.rectangle(c._b((4, 50, w - 4, 76)), fill=(34, 78, 64))
        for k, col in enumerate((CORAL, GOLD, GREEN_OK)):
            c.ell((34 + k * 36, 30, 54 + k * 36, 50), fill=col)
        c.rrect((170, 20, w - 40, 60), 20, fill=IVORY)
        c.text((190, 41), "tsa.gov", FONT_SANS, 30, GREEN_D, anchor="lm")
        c.ell((w / 2 - 90, 130, w / 2 + 90, 310), fill=GOLD, outline=(168, 118, 40), width=6)
        star5(c, w / 2, 220, 62, GREEN_D)
        c.text((w / 2, 370), "OFFICIAL PAGE", FONT_SANS, 40, IVORY, track=3)
        c.rrect((w / 2 - 140, 410, w / 2 + 140, 424), 6, fill=(60, 110, 92))
    return sprite(("browser5", w, h), w, h, fn)

def doc_spr(w=700, h=470):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 30, fill=(20, 56, 46), outline=SAGE_D, width=5)
        c.rrect((190, 34, w - 190, h - 34), 14, fill=IVORY, outline=(206, 200, 186), width=4)
        c.text((w / 2, 110), "14 CFR", FONT_SANS, 62, GREEN_D)
        c.text((w / 2, 172), "PART 382", FONT_SANS, 44, CORAL_D, track=2)
        for k in range(4):
            c.rrect((230, 220 + k * 34, w - 230 - (k % 2) * 40, 236 + k * 34), 6, fill=(206, 212, 206))
        c.ell((w - 280, h - 170, w - 170, h - 60), fill=GOLD, outline=(168, 118, 40), width=5)
        star5(c, w - 225, h - 115, 34, GREEN_D)
    return sprite(("doc5", w, h), w, h, fn)

def draw6(img, t):
    ts = starts(6)
    common(img, t, "WHERE THIS COMES FROM")
    seq(img, t, ts[0], txt("BEFORE WE START", 76, GOLD, 4), 960, 190, shadow=8)
    slide_in(img, t, ts[1], browser_spr(), 520, 520, dx=-80, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.5, txt("OFFICIAL PAGES", 44, SAGE, 3), 520, 810)
    slide_in(img, t, ts[2], doc_spr(), 1400, 520, dx=80, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.5, txt("FEDERAL AIRLINE RULES", 44, SAGE, 3), 1400, 810)
    seq(img, t, ts[3], chip("NO GUESSES", 560, 96, RED, "x"), 520, 905, shadow=8)
    seq(img, t, ts[3] + 0.5, chip("NO RUMORS", 560, 96, RED, "x"), 1400, 905, shadow=8)
    ban(img, t, ts[4], "RULES CHANGE. CONFIRM BEFORE YOU TRAVEL", cy=1010, w=1300, h=84, size=44)

# ============================================================ BLOCCO 7
def draw7(img, t):
    ts = starts(7)
    common(img, t, "PHOTO I D")
    show_badge(img, t, 1)
    seq(img, t, ts[1], sprite("idc7", 460, 320, lambda c: ic_idcard(c, 230, 160, 2.3)), 440, 330, shadow=10)
    seq(img, t, ts[1] + 0.4, txt("YOUR PHOTO I D", 46, IVORY, 2), 440, 510)
    seq(img, t, ts[2], cal_spr(), 960, 340, shadow=10)
    seq(img, t, ts[2] + 0.4, txt("SINCE THIS DATE", 40, SAGE, 2), 960, 540)
    seq(img, t, ts[3], sprite("pl7", 320, 220, lambda c: ic_plane(c, 160, 110, 1.9)), 1500, 330, shadow=10)
    seq(img, t, ts[3] + 0.4, txt("FLYING INSIDE THE COUNTRY", 38, SAGE, 1), 1500, 510)
    seq(img, t, ts[4], realid_card(), 620, 800, shadow=12)
    seq(img, t, ts[4] + 0.4, txt("OR", 80, GOLD, 2), 960, 800)
    seq(img, t, ts[4] + 0.7, passport_spr(), 1300, 800, shadow=12)
    ban(img, t, ts[4] + 0.9, "YOU NEED ONE OF THESE", cy=1010, w=1000, h=84, size=46)

# ============================================================ BLOCCO 8
def draw8(img, t):
    ts = starts(8)
    common(img, t, "THE STAR")
    show_badge(img, t, 1)
    slide_in(img, t, ts[0], license_spr(), 600, 520, dx=-100, dur=0.6, shadow=14)
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, star_gold(34), 884, 333, scale=s * 1.3, alpha=a)
        burst(img, t, ts[1], 884, 333, n=12, color=GOLD, rad=200, seed=7)
    seq(img, t, ts[1] + 0.4, txt("A STAR IN THE CORNER", 44, GOLD, 2), 600, 240)
    seq(img, t, ts[2], card(560, 260, GOLD), 1480, 400, shadow=12)
    seq(img, t, ts[2] + 0.3, txt("OR THE WORD", 42, IVORY, 3), 1480, 330)
    seq(img, t, ts[2] + 0.5, txt("ENHANCED", 80, GOLD, 3), 1480, 420)
    s, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, stamp("IT COUNTS", 520, 120, GREEN_OK, size=54), 1480, 600, scale=s, alpha=a, rot=-3, shadow=10)
    seq(img, t, ts[4], chip("NO STAR", 520, 90, RED, "x"), 1480, 740, shadow=8)
    seq(img, t, ts[4] + 0.5, chip("NO PASSPORT", 520, 90, RED, "x"), 1480, 845, shadow=8)
    ban(img, t, ts[5], "A PROBLEM AT THE CHECKPOINT", cy=1010, w=1100, h=84, size=46)

# ============================================================ BLOCCO 9
def draw9(img, t):
    ts = starts(9)
    common(img, t, "THE COMMON MISTAKE")
    show_badge(img, t, 1)
    slide_in(img, t, ts[0], license_spr(slot=True), 600, 520, dx=-100, dur=0.6, shadow=14)
    seq(img, t, ts[0] + 0.3, bubble_spr(760, 220, IVORY, ["MY OLD LICENSE", "IS FINE"], DARK, 56), 1450, 330, shadow=10)
    seq(img, t, ts[0] + 1.0, sprite("bigx9", 120, 120, lambda c: ic_x(c, 60, 60, 1.3, RED, 16)), 1760, 260)
    seq(img, t, ts[1], chip("NOT EXPIRED", 600, 100, GREEN_OK, "ok", 44), 1450, 590, shadow=8)
    seq(img, t, ts[2], chip("DATE: NOT THE POINT", 700, 100, GOLD, None, 40), 1450, 730, shadow=8)
    p = ease(seg(t, ts[2] + 0.2, 0.5))
    if p > 0:
        put(img, sprite("ring9", 340, 84, lambda c: c.rrect((4, 4, 336, 80), 20, outline=GOLD, width=6)), 645, 594, alpha=p)
    s, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, star_gold(34), 884, 333, scale=s * 1.3, alpha=a)
        burst(img, t, ts[3], 884, 333, n=14, color=GOLD, rad=220, seed=9)
    ban(img, t, ts[3] + 0.3, "THE STAR IS THE POINT", cy=1010, w=1000, h=84, size=48)

# ============================================================ BLOCCO 10
def feetag():
    def fn(c):
        w, h = 540, 290
        c.rrect((4, 4, w - 4, h - 4), 30, fill=GOLD, outline=(168, 118, 40), width=6)
        c.ell((40, h / 2 - 22, 84, h / 2 + 22), fill=GREEN_D)
        c.text((w / 2 + 40, h / 2 - 12), "$45", FONT_SANS, 150, GREEN_D)
        c.text((w / 2 + 40, h - 52), "T S A FEE", FONT_SANS, 40, GREEN_D, track=4)
    return sprite("feetag10", 540, 290, fn)

def draw10(img, t):
    ts = starts(10)
    common(img, t, "THE FEE")
    show_badge(img, t, 1)
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, feetag(), 440, 340, scale=s, alpha=a, shadow=14, rot=-4)
        burst(img, t, ts[0], 440, 340, n=12, color=GOLD, rad=240, seed=10)
    slide_in(img, t, ts[1], sprite("trav10", 360, 300, lambda c: (ic_person(c, 150, 150, 2.2, col=SAGE), ic_suitcase(c, 280, 230, 0.8))), 960, 340, dx=-60, dur=0.5, shadow=10)
    seq(img, t, ts[1] + 0.4, txt("TRAVELER AT THE CHECKPOINT", 36, SAGE, 1), 960, 520)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("noid10", 440, 280, lambda c: (c.rrect((6, 6, 434, 274), 26, fill=(10, 40, 32), outline=RED, width=6), ic_x(c, 220, 130, 2.0, RED, 14), c.text((220, 235), "NO ACCEPTABLE I D", FONT_SANS, 34, IVORY))), 1480, 340, scale=s, alpha=a, shadow=10)
    slide_in(img, t, ts[3], card(1560, 290, GOLD), 960, 790, dy=60, dur=0.5, shadow=14)
    seq(img, t, ts[3] + 0.3, sprite("home10", 280, 220, lambda c: ic_house(c, 140, 100, 1.9)), 420, 765, shadow=8)
    seq(img, t, ts[3] + 0.5, txt("AT HOME", 40, SAGE, 3), 420, 895)
    seq(img, t, ts[3] + 0.8, license_spr_small(), 960, 790, shadow=8)
    seq(img, t, ts[3] + 1.1, sprite("okbig10", 220, 220, lambda c: (c.ell((10, 10, 210, 210), fill=GREEN_OK), check_ic(c, 110, 116, 2.4, GREEN_D))), 1500, 790, shadow=8)
    ban(img, t, ts[3] + 1.2, "CHECK THE CARD AT HOME", cy=1010, w=1000, h=84, size=48)

def license_spr_small():
    def fn(c):
        w, h = 380, 235
        c.rrect((4, 4, w - 4, h - 4), 16, fill=IVORY, outline=GOLD, width=5)
        c.rrect((4, 4, w - 4, 52), 16, fill=GREEN_L)
        c.d.rectangle(c._b((4, 30, w - 4, 52)), fill=GREEN_L)
        star5(c, w - 50, 28, 17, GOLD)
        c.rrect((26, 70, 126, 200), 8, fill=(214, 204, 192))
        for k in range(3):
            c.rrect((146, 80 + k * 34, 340 - k * 24, 96 + k * 34), 6, fill=(206, 212, 206))
    return sprite("licsmall10", 380, 235, fn)

# ============================================================ BLOCCO 11
def week_strip():
    def fn(c):
        w, h = 700, 150
        for k in range(7):
            x = 14 + k * 96
            last = (k == 6)
            c.rrect((x, 30, x + 84, 130), 14, fill=(40, 70, 52) if not last else CORAL, outline=GOLD if last else SAGE_D, width=5)
            c.text((x + 42, 56), "MTWTFSS"[k], FONT_SANS, 26, IVORY if not last else IVORY)
        ic_plane(c, 14 + 6 * 96 + 42, 100, 0.42, col=IVORY)
        c.text((350, 12), "WEEK OF YOUR TRIP", FONT_SANS, 24, SAGE, track=3)
    return sprite("week11", 700, 150, fn)

def draw11(img, t):
    ts = starts(11)
    common(img, t, "THE REAL I D")
    show_badge(img, t, 1)
    seq(img, t, ts[0], txt("WHO GETS HIT HARDEST?", 66, GOLD, 3), 960, 175, shadow=8)
    seq(img, t, ts[1], card(760, 330, SAGE), 520, 420, shadow=12)
    seq(img, t, ts[1] + 0.2, txt("OLDER DRIVERS", 48, GOLD, 2), 520, 300)
    seq(img, t, ts[1] + 0.4, sprite("old11", 260, 220, lambda c: ic_person(c, 130, 110, 1.9, col=SAGE)), 330, 430)
    seq(img, t, ts[1] + 0.6, sprite("lic11", 300, 200, lambda c: ic_idcard(c, 150, 100, 1.6)), 650, 430)
    seq(img, t, ts[1] + 0.8, txt("NOT RENEWED IN YEARS", 30, SAGE, 1), 520, 545)
    seq(img, t, ts[2], card(760, 330, SAGE), 1400, 420, shadow=12)
    seq(img, t, ts[2] + 0.2, txt("NEVER NEEDED A PASSPORT", 38, GOLD, 1), 1400, 300)
    seq(img, t, ts[2] + 0.4, sprite("per11", 260, 220, lambda c: ic_person(c, 130, 110, 1.9, col=GOLD)), 1210, 430)
    p = pop(t, ts[2] + 0.6, 0.45)
    if p[2] > 0:
        put(img, passport_spr(240, 170, dim=True), 1550, 440, scale=p[0], alpha=p[1])
        put(img, sprite("x11", 90, 90, lambda c: (c.ell((4, 4, 86, 86), fill=PANEL_FILL, outline=RED, width=5), ic_x(c, 45, 45, 0.8, RED, 14))), 1650, 360, scale=p[0], alpha=p[1])
    seq(img, t, ts[3], card(760, 270, GOLD), 520, 800, shadow=12)
    seq(img, t, ts[3] + 0.2, txt("STATE MOTOR VEHICLE OFFICE", 34, SAGE, 1), 520, 700)
    seq(img, t, ts[3] + 0.4, sprite("bld11", 200, 200, lambda c: ic_building(c, 100, 100, 1.4)), 310, 810)
    seq(img, t, ts[3] + 0.6, sprite("arr11", 120, 100, lambda c: c.poly([(6, 34), (62, 34), (62, 8), (114, 50), (62, 92), (62, 66), (6, 66)], fill=GOLD)), 450, 810)
    seq(img, t, ts[3] + 0.8, sprite("rid11", 300, 190, lambda c: (c.rrect((4, 4, 296, 186), 16, fill=IVORY, outline=GOLD, width=5), star5(c, 240, 56, 34, GOLD), c.text((30, 130), "REAL I D", FONT_SANS, 46, GREEN_D, anchor="lm"))), 640, 810)
    seq(img, t, ts[4], card(760, 270, CORAL), 1400, 800, shadow=12)
    seq(img, t, ts[4] + 0.2, week_strip(), 1400, 810)
    ban(img, t, ts[4] + 0.5, "DON'T WAIT UNTIL TRIP WEEK", cy=1010, w=1100, h=84, size=48)

# ============================================================ BLOCCO 12
def step_card(n, w=540, h=560):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 36, fill=PANEL_FILL, outline=GOLD, width=6)
    return sprite(("step12", n, w, h), w, h, fn)

def draw12(img, t):
    ts = starts(12)
    common(img, t, "YOUR ACTION")
    show_badge(img, t, 1)
    seq(img, t, ts[0], txt("YOUR ACTION TONIGHT", 66, GOLD, 3), 960, 170, shadow=8)
    seq(img, t, ts[1], step_card(1), 340, 580, shadow=12)
    seq(img, t, ts[1] + 0.25, sprite("lic12", 340, 220, lambda c: ic_idcard(c, 170, 110, 1.9)), 340, 560)
    seq(img, t, ts[1] + 0.45, sprite("moon12", 120, 120, lambda c: ic_moon(c, 60, 60, 1.2)), 470, 440)
    seq(img, t, ts[1] + 0.6, txt("TAKE OUT", 46, IVORY, 2), 340, 720)
    seq(img, t, ts[1] + 0.7, txt("YOUR LICENSE", 46, GOLD, 2), 340, 780)
    seq(img, t, ts[2], step_card(2), 960, 580, shadow=12)
    seq(img, t, ts[2] + 0.25, sprite("lic12b", 340, 220, lambda c: ic_idcard(c, 170, 110, 1.9)), 960, 560)
    seq(img, t, ts[2] + 0.45, sprite("mag12", 160, 160, lambda c: ic_magnify(c, 80, 80, 1.6)), 1080, 610)
    seq(img, t, ts[2] + 0.6, txt("LOOK FOR", 46, IVORY, 2), 960, 720)
    seq(img, t, ts[2] + 0.7, txt("THE STAR", 46, GOLD, 2), 960, 780)
    seq(img, t, ts[3], step_card(3), 1580, 580, shadow=12)
    seq(img, t, ts[3] + 0.25, sprite("ph12", 160, 200, lambda c: ic_phone(c, 80, 100, 1.4)), 1580, 550)
    seq(img, t, ts[3] + 0.5, txt("NOT THERE?", 46, IVORY, 2), 1580, 720)
    seq(img, t, ts[4], txt("CALL YOUR STATE", 38, GOLD, 2), 1580, 775)
    seq(img, t, ts[4] + 0.2, txt("MOTOR VEHICLE OFFICE", 32, GOLD, 1), 1580, 830)

# ============================================================ BLOCCO 13
def draw13(img, t):
    ts = starts(13)
    common(img, t, "HELP AT THE AIRPORT")
    show_badge(img, t, 2)
    seq(img, t, ts[1], txt("HELP GETTING THROUGH THE AIRPORT", 56, GOLD, 2), 960, 175, shadow=8)
    seq(img, t, ts[2], card(780, 250, SAGE), 520, 380, shadow=12)
    seq(img, t, ts[2] + 0.2, sprite("scr13", 160, 200, lambda c: ic_scroll(c, 80, 100, 1.4)), 290, 380)
    seq(img, t, ts[2] + 0.4, txt("FEDERAL RULES", 40, GOLD, 2), 650, 340)
    seq(img, t, ts[2] + 0.6, txt("IF YOU HAVE A DISABILITY", 30, IVORY, 1), 650, 405)
    seq(img, t, ts[3], card(780, 250, GOLD), 1400, 380, shadow=12)
    seq(img, t, ts[3] + 0.2, sprite("hlp13", 160, 200, lambda c: ic_helper(c, 80, 100, 1.5)), 1130, 390)
    seq(img, t, ts[3] + 0.4, txt("THE AIRLINE MUST", 40, GOLD, 2), 1490, 340)
    seq(img, t, ts[3] + 0.6, txt("PROVIDE OR ARRANGE HELP", 30, IVORY, 1), 1490, 405)
    seq(img, t, ts[4], sprite("door13", 220, 220, lambda c: ic_door(c, 110, 110, 1.6)), 330, 760, shadow=8)
    seq(img, t, ts[4] + 0.2, txt("TERMINAL ENTRANCE", 32, SAGE, 1), 330, 905)
    seq(img, t, ts[4] + 0.4, sprite("gate13", 220, 220, lambda c: ic_gatesign(c, 110, 110, 1.6)), 1590, 760, shadow=8)
    seq(img, t, ts[4] + 0.6, txt("YOUR GATE", 32, SAGE, 1), 1590, 905)
    p = ease(seg(t, ts[4] + 0.5, 0.9))
    if p > 0:
        put(img, sprite("arrF13", 1000, 80, lambda c: (c.line([(10, 40), (900, 40)], GOLD, 14), c.poly([(900, 8), (990, 40), (900, 72)], fill=GOLD))), 960, 720, alpha=p)
    p = ease(seg(t, ts[5], 0.9))
    if p > 0:
        put(img, sprite("arrB13", 1000, 80, lambda c: (c.line([(990, 40), (100, 40)], SAGE, 14), c.poly([(100, 8), (10, 40), (100, 72)], fill=SAGE))), 960, 810, alpha=p)

# ============================================================ BLOCCO 14
def draw14(img, t):
    ts = starts(14)
    common(img, t, "WHAT IT INCLUDES")
    show_badge(img, t, 2)
    seq(img, t, ts[0], card(540, 600, GOLD), 360, 520, shadow=12)
    seq(img, t, ts[0] + 0.3, txt("CONNECTIONS", 44, GOLD, 2), 360, 290)
    seq(img, t, ts[0] + 0.5, sprite("gA14", 180, 180, lambda c: ic_gatesign(c, 90, 90, 1.3, "A12")), 250, 470)
    seq(img, t, ts[0] + 0.8, sprite("gB14", 180, 180, lambda c: ic_gatesign(c, 90, 90, 1.3, "B7")), 470, 470)
    seq(img, t, ts[0] + 1.0, sprite("gar14", 120, 60, lambda c: c.poly([(6, 22), (70, 22), (70, 6), (114, 30), (70, 54), (70, 38), (6, 38)], fill=GOLD)), 360, 600)
    seq(img, t, ts[0] + 1.2, txt("BETWEEN TWO GATES", 30, IVORY, 1), 360, 700)
    seq(img, t, ts[1], card(540, 600, SAGE), 960, 520, shadow=12)
    seq(img, t, ts[1] + 0.3, txt("A SHORT STOP", 44, GOLD, 2), 960, 290)
    seq(img, t, ts[1] + 0.5, sprite("wc14", 220, 220, lambda c: ic_wc(c, 110, 110, 1.6)), 960, 480)
    seq(img, t, ts[1] + 0.9, txt("AT A RESTROOM", 34, IVORY, 1), 960, 650)
    seq(img, t, ts[2], chip("IF YOU ASK", 360, 90, GOLD, None, 40), 960, 740, shadow=8)
    seq(img, t, ts[3], card(540, 600, CORAL), 1560, 520, shadow=12)
    seq(img, t, ts[3] + 0.3, txt("YOUR BAGS", 44, GOLD, 2), 1560, 290)
    seq(img, t, ts[3] + 0.5, sprite("bag14", 220, 220, lambda c: ic_suitcase(c, 110, 110, 1.5)), 1470, 480)
    seq(img, t, ts[4], sprite("hel14", 200, 220, lambda c: ic_helper(c, 100, 110, 1.6)), 1680, 480, shadow=8)
    seq(img, t, ts[4] + 0.3, txt("THE AIRLINE HELPS", 32, IVORY, 1), 1560, 650)
    ban(img, t, ts[4] + 0.6, "IF YOU CAN'T CARRY THEM BECAUSE OF A DISABILITY", cy=1010, w=1500, h=84, size=40)

# ============================================================ BLOCCO 15
def draw15(img, t):
    ts = starts(15)
    common(img, t, "THE HONEST PART")
    show_badge(img, t, 2)
    seq(img, t, ts[1], card(740, 330, GREEN_OK), 520, 355, shadow=12)
    seq(img, t, ts[1] + 0.2, txt("DISABILITY", 54, GREEN_OK, 3), 520, 245)
    seq(img, t, ts[1] + 0.4, sprite("cane15", 160, 200, lambda c: ic_cane(c, 70, 100, 1.3)), 400, 385)
    seq(img, t, ts[1] + 0.6, sprite("ok15", 160, 160, lambda c: (c.ell((10, 10, 150, 150), fill=GREEN_OK), check_ic(c, 80, 84, 1.8, GREEN_D))), 640, 385)
    seq(img, t, ts[2], card(740, 330, RED), 1400, 355, shadow=12)
    seq(img, t, ts[2] + 0.2, txt("YOUR BIRTHDAY", 54, RED, 3), 1400, 245)
    seq(img, t, ts[2] + 0.4, sprite("cake15", 200, 200, lambda c: ic_cake(c, 100, 110, 1.6)), 1280, 395)
    seq(img, t, ts[2] + 0.6, sprite("x15", 160, 160, lambda c: ic_x(c, 80, 80, 1.7, RED, 16)), 1520, 385)
    s, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, stamp("OVER SIXTY ALONE IS NOT ENOUGH", 1300, 96, RED, size=46), 960, 595, scale=s, alpha=a, shadow=10)
    seq(img, t, ts[4], card(740, 230, SAGE), 520, 790, shadow=12)
    seq(img, t, ts[4] + 0.3, sprite("walk15", 200, 160, lambda c: (ic_person(c, 60, 80, 1.1, col=SAGE), c.line([(110, 120), (190, 120)], SAGE_D, 8), c.poly([(184, 100), (200, 120), (184, 140)], fill=SAGE_D))), 370, 790)
    seq(img, t, ts[4] + 0.5, txt("WALKING FAR", 40, IVORY, 2), 650, 770)
    seq(img, t, ts[4] + 0.7, txt("IS HARD", 40, GOLD, 2), 650, 825)
    seq(img, t, ts[5], card(740, 230, SAGE), 1400, 790, shadow=12)
    seq(img, t, ts[5] + 0.3, sprite("stand15", 200, 160, lambda c: (ic_person(c, 70, 80, 1.1, col=GOLD), ic_clockface(c, 150, 100, 36, 0.4))), 1250, 790)
    seq(img, t, ts[5] + 0.5, txt("STANDING A LONG TIME", 28, IVORY, 1), 1548, 765)
    seq(img, t, ts[5] + 0.7, txt("IS HARD", 40, GOLD, 2), 1548, 825)
    ban(img, t, ts[6], "THIS IS FOR YOU", cy=1010, w=800, h=84, size=52)

DRAW = {6: draw6, 7: draw7, 8: draw8, 9: draw9, 10: draw10, 11: draw11, 12: draw12, 13: draw13, 14: draw14, 15: draw15}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/V5-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
