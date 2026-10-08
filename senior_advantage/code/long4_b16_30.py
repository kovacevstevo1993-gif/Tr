"""Video lungo 4 (BOLLETTE) - blocchi 16-30. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-BOLLETTE.md.
Durate (timeline utente 08/10/2026): B16 292, B17 396, B18 416, B19 407, B20 358, B21 453, B22 219, B23 375, B24 333, B25 350, B26 338, B27 264, B28 312, B29 417, B30 362.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long4_b16_30.py <blocco>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b11_15 import *

DUR = {16: 292, 17: 396, 18: 416, 19: 407, 20: 358, 21: 453, 22: 219, 23: 375, 24: 333, 25: 350, 26: 338, 27: 264, 28: 312, 29: 417, 30: 362}
PHRASES = {
    16: ["It's called the Weatherization Assistance Program,", "run by the U S Department of Energy.", "A crew comes to your home", "and fixes what makes it lose heat."],
    17: ["First, a professional energy auditor checks your whole house.", "Your bills, your heating equipment, the attic, the basement.", "They even run a test that measures how much cold air is leaking in."],
    18: ["Then they recommend the work that saves the most energy,", "and a local crew does it.", "According to the Department of Energy,", "households save on average three hundred seventy two dollars or more,", "every single year."],
    19: ["And here's what surprises people.", "Older adults get priority here too.", "And you don't need to own your home.", "Renters can apply.", "The provider simply works with your landlord to get permission first."],
    20: ["To qualify, your household income must be at or below twice the federal poverty level,", "or you receive S S I.", "Some states use the same limit as L I H E A P instead."],
    21: ["The mistake?", "Thinking it's only for falling down houses.", "It's not.", "And because there is often a waiting list,", "the sooner you get your name on it, the better.", "Your state agency is listed on the Department of Energy website."],
    22: ["Bill number three is smaller,", "but I'm not skipping it,", "because it comes every month and it adds up.", "Your phone bill."],
    23: ["There's a federal program called Lifeline.", "It lowers the monthly cost of your phone or internet service", "by up to nine dollars and twenty five cents a month.", "That's over one hundred dollars a year."],
    24: ["You can use it on a phone plan, on internet, or on a bundle.", "And on qualifying Tribal lands,", "the discount goes up to thirty four dollars and twenty five cents a month."],
    25: ["Now pay attention to how you qualify,", "because this is where the order I promised starts to matter.", "You can qualify through your income,", "or simply because you already get certain benefits."],
    26: ["If you get snap, Medicaid, S S I, federal public housing help, or a Veterans Pension,", "you can qualify for Lifeline.", "You don't have to prove your income all over again."],
    27: ["Or you qualify by income.", "For one person in twenty twenty six,", "that's up to twenty one thousand five hundred forty six dollars a year."],
    28: ["Who does this help most?", "Anyone who already gets snap or Medicaid", "and still pays full price for a phone.", "Many people qualify for years and never ask."],
    29: ["You apply on lifeline support dot org,", "then you contact a participating phone or internet company.", "If you need help, call one, eight hundred, two three four, nine four seven three.", "They answer seven days a week."],
    30: ["So that's three bills.", "Heat, energy, phone.", "Now we get to the bills most people never connect to a program at all.", "And one of them is about the food in your fridge."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

# ------------------------------------------------------------------ sprite nuovi
def ic_hat_person(c, cx, cy, s, col=GOLD):
    ic_person(c, cx, cy, s, col=col)
    c.d.pieslice(c._b((cx - 26 * s, cy - 62 * s, cx + 26 * s, cy - 12 * s)), 180, 360, fill=GOLD)
    c.rrect((cx - 32 * s, cy - 38 * s, cx + 32 * s, cy - 30 * s), 3, fill=(190, 140, 60))

def ic_wifi(c, cx, cy, s, col=GOLD):
    for r in (62, 42, 22):
        c.arc((cx - r * s, cy - r * s + 20 * s, cx + r * s, cy + r * s + 20 * s), 215, 325, col, 10 * s)
    c.ell((cx - 8 * s, cy + 18 * s, cx + 8 * s, cy + 34 * s), fill=col)

def ic_clip(c, cx, cy, s):
    c.rrect((cx - 54 * s, cy - 68 * s, cx + 54 * s, cy + 68 * s), 10 * s, fill=(190, 150, 100), outline=(130, 90, 50), width=4)
    c.rrect((cx - 42 * s, cy - 54 * s, cx + 42 * s, cy + 58 * s), 5 * s, fill=IVORY)
    c.rrect((cx - 22 * s, cy - 78 * s, cx + 22 * s, cy - 56 * s), 6 * s, fill=(110, 110, 110))
    for k in range(3):
        c.line([(cx - 32 * s, cy - 24 * s + k * 28 * s), (cx - 22 * s, cy - 14 * s + k * 28 * s), (cx - 8 * s, cy - 34 * s + k * 28 * s)], GREEN_L, 5 * s)
        c.rrect((cx + 2 * s, cy - 28 * s + k * 28 * s, cx + 36 * s, cy - 20 * s + k * 28 * s), 3, fill=(206, 202, 190))

def ic_fan(c, cx, cy, s, ang=0.0):
    c.ell((cx - 60 * s, cy - 60 * s, cx + 60 * s, cy + 60 * s), fill=(24, 60, 48), outline=ICE, width=6)
    for k in range(4):
        a = ang + k * math.pi / 2
        pts = [(cx, cy), (cx + math.cos(a - 0.35) * 52 * s, cy + math.sin(a - 0.35) * 52 * s), (cx + math.cos(a + 0.35) * 52 * s, cy + math.sin(a + 0.35) * 52 * s)]
        c.poly(pts, fill=ICE)
    c.ell((cx - 9 * s, cy - 9 * s, cx + 9 * s, cy + 9 * s), fill=GREEN_D)

def ic_fridge(c, cx, cy, s):
    c.rrect((cx - 56 * s, cy - 90 * s, cx + 56 * s, cy + 90 * s), 14 * s, fill=(226, 232, 234), outline=(160, 172, 176), width=4)
    c.line([(cx - 56 * s, cy - 24 * s), (cx + 56 * s, cy - 24 * s)], (160, 172, 176), 4)
    c.rrect((cx + 34 * s, cy - 70 * s, cx + 42 * s, cy - 38 * s), 3, fill=(120, 130, 134))
    c.rrect((cx + 34 * s, cy - 14 * s, cx + 42 * s, cy + 40 * s), 3, fill=(120, 130, 134))

def card(w, h, icon, top, bottom, col, tsz=40, bsz=32):
    def fn(c):
        c.rrect((5, 5, w - 5, h - 5), 36, fill=PANEL_FILL, outline=col, width=7)
        icon(c, w / 2, h * 0.38, 1.4)
        c.text((w / 2, h * 0.72), top, FONT_SANS, tsz, col, track=2)
        if bottom:
            c.text((w / 2, h * 0.88), bottom, FONT_SANS, bsz, IVORY, track=1)
    return sprite(("card4b", w, h, top, bottom, col), w, h, fn)

def typed(img, t, t0, t1, text, size, col, cx, cy, track=3):
    if t < t0:
        return
    k = max(1, int(len(text) * min(1.0, (t - t0) / max(0.1, t1 - t0))))
    full = txt(text, size, col, track); sp = txt(text[:k], size, col, track)
    img.paste(sp, (int(cx - full.width / 2), int(cy - sp.height / 2)), sp)

def counter(img, t, t0, dur, prefix, final, suffix, size, col, cx, cy, fmt="{:,}"):
    if t < t0:
        return
    v = int(final * ease(seg(t, t0, dur)))
    sp = txt(prefix + fmt.format(v) + suffix, size, col, 3)
    full = txt(prefix + fmt.format(final) + suffix, size, col, 3)
    img.paste(sp, (int(cx - full.width / 2), int(cy - sp.height / 2)), sp)

def ic_coin(c, cx, cy, r):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=GOLD, outline=(168, 118, 40), width=max(2, r * 0.08))
    c.text((cx, cy + 2), '$', FONT_SANS, r * 1.1, GREEN_D)

def check_at(img, t, t0, cx, cy, sc=1.0):
    s, a, p = pop(t, t0, 0.4)
    if p > 0:
        put(img, check_spr(), cx, cy, scale=sc * s, alpha=a)

# ============================================================ BLOCCO 16
def draw16(img, t):
    ts = starts(16)
    common(img, t, "THE PROGRAM")
    seq(img, t, ts[0], txt("WEATHERIZATION", 124, GOLD, 4), 960, 210, shadow=10)
    seq(img, t, ts[0] + 0.5, txt("ASSISTANCE PROGRAM", 54, IVORY, 4), 960, 310)
    # Department of Energy
    slide_in(img, t, ts[1], panel(560, 420, border=SAGE), 440, 640, dx=-80, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, sprite("gov16", 260, 200, lambda c: ic_gov(c, 130, 100, 1.6)), 440, 560, shadow=8)
    seq(img, t, ts[1] + 0.6, txt("U S DEPARTMENT", 38, SAGE, 3), 440, 700)
    seq(img, t, ts[1] + 0.75, txt("OF ENERGY", 52, IVORY, 3), 440, 760)
    # casa che perde calore
    hs = lambda c: (ic_house(c, 200, 200, 3.2, col=IVORY))
    seq(img, t, ts[2] - 0.6, sprite("hl16", 400, 400, hs), 1000, 620, shadow=12, scale=1.05)
    leak = 1.0 - ease(seg(t, ts[3] + 0.6, 0.5))
    if t >= ts[2] - 0.4 and leak > 0:
        for k, (dx, dy) in enumerate(((-210, -90), (-230, 40), (230, -80), (240, 50))):
            ph = (t * 1.6 + k * 0.25) % 1.0
            put(img, rarrow(FLAME, 120, 70), 1000 + dx * (1 + 0.5 * ph), 620 + dy, alpha=leak * (1 - ph), rot=0 if dx > 0 else 180, scale=0.8)
    # squadra
    for k, x in enumerate((1440, 1560, 1680)):
        s, a, p = pop(t, ts[2] + 0.2 + k * 0.25, 0.4)
        if p > 0:
            put(img, sprite(("crew16", k), 200, 240, lambda c: ic_hat_person(c, 100, 140, 1.5, col=[(70, 120, 176), GOLD, SAGE][k])), x, 640, scale=s, alpha=a, shadow=8)
    seq(img, t, ts[2] + 0.9, txt("A LOCAL CREW", 38, GOLD, 3), 1560, 790)
    # fix: scudo con spunta sulla casa
    s, a, p = pop(t, ts[3] + 0.5, 0.45)
    if p > 0:
        put(img, check_spr(), 1130, 480, scale=1.5 * s, alpha=a)
        burst(img, t, ts[3] + 0.5, 1130, 480, n=10, rad=170, seed=16)
    ban(img, t, ts[3] + 0.6, "FIXES WHAT MAKES YOUR HOME LOSE HEAT", cy=975, w=1280)

# ============================================================ BLOCCO 17
def xsec():
    def fn(c):
        w, h = 760, 640
        c.poly([(40, 170), (380, 14), (720, 170)], fill=CORAL)
        c.rrect((70, 160, 690, 260), 4, fill=(236, 226, 206))            # soffitta
        c.rrect((70, 270, 690, 450), 4, fill=IVORY)                       # piano
        c.rrect((70, 460, 690, 610), 4, fill=(120, 96, 76))               # cantina
        c.rrect((340, 330, 420, 450), 4, fill=(160, 112, 60))
        c.rrect((110, 300, 220, 380), 6, fill=(190, 222, 232)); c.rrect((540, 300, 650, 380), 6, fill=(190, 222, 232))
    return sprite("xsec17", 760, 640, fn)

def draw17(img, t):
    ts = starts(17)
    common(img, t, "THE ENERGY AUDIT")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, sprite("aud17", 260, 300, lambda c: (ic_hat_person(c, 130, 170, 1.9, col=(70, 120, 176)), ic_clip(c, 200, 230, 0.7))), 260, 500, scale=s, alpha=a, shadow=12)
    seq(img, t, ts[0] + 0.5, txt("ENERGY AUDITOR", 36, GOLD, 3), 260, 680)
    seq(img, t, ts[0] + 0.7, txt("WHOLE HOUSE", 30, SAGE, 3), 260, 730)
    slide_in(img, t, ts[0] + 0.3, xsec(), 820, 520, dx=0, dy=-60, dur=0.6, shadow=16, scale=0.85)
    # quattro segnalini
    tags = [("YOUR BILLS", 330, 310, ic_bolt), ("ATTIC", 820, 215, None), ("HEATING EQUIPMENT", 830, 880, ic_flame), ("BASEMENT", 1220, 790, None)]
    for k, (name, x, y, ic) in enumerate(tags):
        s, a, p = pop(t, ts[1] + 0.2 + k * 0.7, 0.4)
        if p > 0:
            put(img, banner(name, w=int(120 + len(name) * 24), h=70, size=32), x, y, scale=s, alpha=a, shadow=8)
            if ic:
                put(img, sprite(("t17", name), 100, 100, lambda c, ic=ic: ic(c, 50, 52, 0.7)), x - (60 + len(name) * 12) - 40, y, scale=s, alpha=a)
    # test della porta soffiante
    slide_in(img, t, ts[2], panel(520, 520, border=ICE), 1620, 520, dx=30, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.3, txt("BLOWER DOOR TEST", 34, ICE, 3), 1620, 330)
    if t >= ts[2] + 0.3:
        cv = Cv(240, 240); ic_fan(cv, 120, 120, 1.7, ang=(t - ts[2]) * 4.0)
        put(img, cv.done(), 1620, 500, alpha=ease(seg(t, ts[2] + 0.3, 0.4)))
    for k in range(3):
        ph = (t * 1.2 - k * 0.3) % 1.0
        if t >= ts[2] + 0.8:
            put(img, rarrow(ICE, 110, 60), 1440 - 90 * ph + 100, 660 + k * 36 - 30, alpha=(1 - ph) * 0.9, rot=180, scale=0.7)
    seq(img, t, ts[2] + 1.4, txt("COLD AIR LEAKING IN", 32, IVORY, 2), 1620, 740)

# ============================================================ BLOCCO 18
def draw18(img, t):
    ts = starts(18)
    common(img, t, "THE WORK AND THE SAVINGS")
    slide_in(img, t, ts[0], panel(520, 620, border=GOLD), 360, 560, dx=-80, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.3, sprite("clip18", 220, 240, lambda c: ic_clip(c, 110, 120, 1.6)), 360, 450, shadow=8)
    seq(img, t, ts[0] + 0.7, txt("BEST SAVINGS", 44, GOLD, 3), 360, 640)
    seq(img, t, ts[0] + 0.85, txt("FIRST", 56, IVORY, 4), 360, 705)
    for k, x in enumerate((880, 1000, 1120)):
        s, a, p = pop(t, ts[1] + 0.2 + k * 0.25, 0.4)
        if p > 0:
            put(img, sprite(("crew18", k), 200, 240, lambda c: ic_hat_person(c, 100, 140, 1.5, col=[(70, 120, 176), GOLD, SAGE][k])), x, 560, scale=s, alpha=a, shadow=8)
    seq(img, t, ts[1] + 0.9, txt("A LOCAL CREW DOES IT", 38, IVORY, 3), 1000, 720)
    # numero
    slide_in(img, t, ts[2], panel(520, 620, border=SAGE), 1560, 560, dx=80, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.2, sprite("gov18", 200, 160, lambda c: ic_gov(c, 100, 80, 0.9)), 1560, 320, shadow=6)
    seq(img, t, ts[2] + 0.5, txt("DEPARTMENT OF ENERGY", 26, SAGE, 2), 1560, 420)
    seq(img, t, ts[3] - 0.1, txt("ON AVERAGE", 36, SAGE, 4), 1560, 480)
    counter(img, t, ts[3] + 0.1, 1.4, "$", 372, "", 150, GOLD, 1560, 600, fmt="{}")
    seq(img, t, ts[3] + 0.8, txt("OR MORE", 54, IVORY, 5), 1560, 710)
    seq(img, t, ts[4], txt("EVERY SINGLE YEAR", 40, GOLD, 3), 1560, 790)
    ban(img, t, ts[4] + 0.2, "SAVED ON ENERGY, YEAR AFTER YEAR", cy=975, w=1100)

# ============================================================ BLOCCO 19
def draw19(img, t):
    ts = starts(19)
    common(img, t, "WHAT SURPRISES PEOPLE")
    seq(img, t, ts[0], stamp("SURPRISE", 460, 110, GOLD, size=56), 960, 200, shadow=12, rot=-2)
    # priorita
    slide_in(img, t, ts[1], panel(520, 520, border=GOLD), 370, 590, dx=-70, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, person_q(GOLD, ring=GOLD), 370, 520, scale=1.7, shadow=10)
    seq(img, t, ts[1] + 0.6, star_spr(), 460, 400, scale=1.0)
    seq(img, t, ts[1] + 0.8, txt("OLDER ADULTS", 40, IVORY, 3), 370, 680)
    seq(img, t, ts[1] + 0.95, txt("GET PRIORITY", 52, GOLD, 3), 370, 745)
    # non serve possedere casa
    slide_in(img, t, ts[2], panel(520, 520, border=SAGE), 960, 590, dy=60, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.3, sprite("own19", 280, 240, lambda c: (ic_house(c, 140, 120, 2.0, col=IVORY), ic_x(c, 200, 190, 1.2, RED, 14))), 960, 490, shadow=8)
    seq(img, t, ts[2] + 0.7, txt("NO NEED TO OWN", 40, IVORY, 3), 960, 680)
    seq(img, t, ts[2] + 0.85, txt("YOUR HOME", 52, GOLD, 3), 960, 745)
    p = seq(img, t, ts[3], stamp("RENTERS CAN APPLY", 460, 100, SAGE, size=36), 960, 905, shadow=8, rot=-2)
    # locatore
    slide_in(img, t, ts[4], panel(520, 520, border=GOLD), 1550, 590, dx=70, dur=0.55, shadow=14)
    seq(img, t, ts[4] + 0.3, sprite("prov19", 200, 220, lambda c: ic_hat_person(c, 100, 130, 1.5, col=(70, 120, 176))), 1400, 520, shadow=8)
    seq(img, t, ts[4] + 0.6, sprite("land19", 200, 220, lambda c: ic_person(c, 100, 130, 1.4, col=GOLD)), 1700, 520, shadow=8)
    seq(img, t, ts[4] + 1.0, sprite("doc19", 200, 150, lambda c: (c.rrect((40, 10, 160, 140), 10, fill=IVORY), c.line([(70, 70), (92, 96), (134, 44)], GREEN_L, 10))), 1550, 640)
    seq(img, t, ts[4] + 1.4, txt("PERMISSION FIRST", 36, GOLD, 3), 1550, 760)

# ============================================================ BLOCCO 20
def draw20(img, t):
    ts = starts(20)
    common(img, t, "WHO QUALIFIES")
    seq(img, t, ts[0], txt("HOUSEHOLD INCOME", 60, IVORY, 4), 960, 190, shadow=8)
    # barre
    p1 = ease(seg(t, ts[0] + 0.5, 0.6))
    if p1 > 0:
        put(img, sprite("b1_20", 520, 90, lambda c: c.rrect((2, 2, 518, 88), 20, fill=SAGE_D)), 650, 340, alpha=p1)
        put(img, txt("FEDERAL POVERTY LEVEL", 34, IVORY, 2), 600, 340, alpha=1) if False else None
    sp = txt("FEDERAL POVERTY LEVEL", 32, IVORY, 2)
    if p1 > 0:
        img.paste(sp, (int(650 - sp.width / 2), 322), sp)
    p2 = ease(seg(t, ts[0] + 1.3, 0.8))
    if p2 > 0:
        w2 = int(1040 * p2)
        put(img, sprite(("b2_20", w2), max(8, w2), 90, lambda c: c.rrect((2, 2, max(8, w2) - 2, 88), 20, fill=GOLD)), 390 + w2 / 2, 470)
    if p2 >= 1:
        sp2 = txt("TWICE THE POVERTY LEVEL", 34, GREEN_D, 2)
        img.paste(sp2, (int(910 - sp2.width / 2), 452), sp2)
        seq(img, t, ts[0] + 2.4, stamp("2 x", 160, 100, GOLD, size=60), 1540, 470, shadow=8)
    seq(img, t, ts[0] + 3.0, txt("AT OR BELOW", 44, GOLD, 4), 960, 590)
    # SSI
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, card(560, 300, lambda c, x, y, sc: c.text((x, y), "S S I", FONT_SANS, 90, GOLD, track=4), "OR YOU RECEIVE", "SUPPLEMENTAL SECURITY INCOME", GOLD, 40, 22), 560, 800, scale=s, alpha=a, shadow=12)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, card(700, 300, lambda c, x, y, sc: ic_flame(c, x, y, 1.0), "SOME STATES", "USE THE L I H E A P LIMIT", FLAME, 40, 26), 1360, 800, scale=s, alpha=a, shadow=12)

# ============================================================ BLOCCO 21
def ruin_house():
    def fn(c):
        ic_house(c, 160, 160, 3.0, col=(170, 160, 140), roof=(120, 90, 80))
        c.line([(80, 140), (130, 190), (110, 230)], (90, 70, 60), 6)
        c.rrect((196, 150, 240, 190), 3, fill=(60, 50, 44))
    return sprite("ruin21", 320, 320, fn)

def wlist(show_me):
    def fn(c):
        w, h = 460, 520
        c.rrect((4, 4, w - 4, h - 4), 30, fill=IVORY, outline=(206, 200, 186), width=5)
        c.rrect((4, 4, w - 4, 90), 30, fill=GREEN_L); c.d.rectangle(c._b((4, 56, w - 4, 90)), fill=GREEN_L)
        c.text((w / 2, 48), "WAITING LIST", FONT_SANS, 38, IVORY, track=3)
        for k in range(5):
            y = 120 + k * 76
            c.ell((30, y, 70, y + 40), fill=(190, 196, 188))
            c.rrect((86, y + 8, 86 + (260 if k % 2 == 0 else 200), y + 30), 6, fill=(206, 212, 206))
        if show_me:
            c.rrect((14, 106, w - 14, 176), 14, fill=(246, 222, 150), outline=GOLD, width=5)
            c.ell((30, 120, 70, 160), fill=GOLD)
            c.text((96, 142), "YOUR NAME", FONT_SANS, 34, GREEN_D, anchor="lm", track=2)
    return sprite(("wlist21", show_me), 460, 520, fn)

def draw21(img, t):
    ts = starts(21)
    common(img, t, "THE MISTAKE")
    seq(img, t, ts[0], stamp("THE MISTAKE", 560, 120, RED, size=56), 960, 205, shadow=12, rot=-2)
    slide_in(img, t, ts[1], ruin_house(), 400, 560, dy=-80, dur=0.55, shadow=14, scale=1.1)
    seq(img, t, ts[1] + 0.8, txt("ONLY FALLING DOWN HOUSES?", 32, SAGE, 2), 400, 780)
    s, a, p = pop(t, ts[2], 0.45)
    if p > 0:
        put(img, sprite("x21", 300, 300, lambda c: ic_x(c, 150, 150, 3.2, RED, 16)), 400, 560, scale=s, alpha=a)
        put(img, stamp("IT'S NOT", 300, 90, GOLD, size=44), 400, 850, scale=s, alpha=a, rot=-3, shadow=8)
    slide_in(img, t, ts[3], wlist(False), 960, 600, dy=60, dur=0.55, shadow=16, scale=0.95)
    if t >= ts[4]:
        s, a, p = pop(t, ts[4] + 0.1, 0.45)
        put(img, wlist(True), 960, 600, scale=0.95, alpha=a, shadow=0)
        put(img, sprite("pen21", 100, 100, lambda c: (c.line([(14, 86), (74, 26)], GOLD, 16), c.poly([(10, 90), (20, 70), (30, 80)], fill=GREEN_D))), 1150 + 40 * (1 - ease(seg(t, ts[4] + 0.1, 0.5))), 450, alpha=1 - seg(t, ts[4] + 1.2, 0.4))
    seq(img, t, ts[4] + 0.6, txt("SOONER IS BETTER", 36, GOLD, 3), 960, 925)
    slide_in(img, t, ts[5], browser_gov(), 1560, 560, dx=30, dur=0.55, shadow=16, scale=0.72)
    seq(img, t, ts[5] + 0.5, txt("STATE AGENCY LIST", 32, IVORY, 3), 1560, 820)
    seq(img, t, ts[5] + 0.7, txt("ON THE DEPARTMENT OF ENERGY SITE", 24, SAGE, 2), 1560, 865)

# ============================================================ BLOCCO 22
def draw22(img, t):
    ts = starts(22)
    common(img, t, "BILL NUMBER THREE")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(3, 400), 360, 330, scale=s, alpha=a, shadow=18)
        burst(img, t, ts[0], 360, 330, n=14, color=GOLD, rad=300, seed=22)
    seq(img, t, ts[3] - 0.3, panel(1080, 400, border=SAGE), 1230, 330, shadow=14)
    seq(img, t, ts[3] - 0.1, sprite("ph22", 240, 330, lambda c: ic_phone(c, 120, 165, 2.3)), 880, 330)
    seq(img, t, ts[3] + 0.1, txt("YOUR", 64, SAGE, 5), 1360, 250)
    seq(img, t, ts[3] + 0.25, txt("PHONE BILL", 92, IVORY, 3), 1360, 360)
    # piccolo ma ogni mese
    seq(img, t, ts[1], txt("SMALLER, BUT NOT SKIPPED", 44, GOLD, 3), 960, 640)
    for k in range(12):
        s, a, p = pop(t, ts[2] + 0.1 + k * 0.1, 0.3)
        if p > 0:
            x = 360 + k * 108
            put(img, sprite(("mon22", k), 90, 110, lambda c, k=k: (c.rrect((2, 2, 88, 108), 14, fill=PANEL_FILL, outline=SAGE_D, width=4), c.text((45, 34), "JFMAMJJASOND"[k], FONT_SANS, 34, SAGE), ic_coin(c, 45, 74, 22))), x, 780, scale=s, alpha=a)
    ban(img, t, ts[2] + 0.7, "EVERY MONTH IT ADDS UP", cy=975, w=860)

# ============================================================ BLOCCO 23
def draw23(img, t):
    ts = starts(23)
    common(img, t, "FEDERAL PROGRAM")
    seq(img, t, ts[0], txt("LIFELINE", 150, GOLD, 8), 960, 230, shadow=12)
    slide_in(img, t, ts[1], panel(560, 440, border=SAGE), 500, 640, dx=-70, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, sprite("ph23", 200, 260, lambda c: ic_phone(c, 100, 130, 1.8)), 410, 640, shadow=8)
    seq(img, t, ts[1] + 0.5, sprite("wf23", 200, 200, lambda c: ic_wifi(c, 100, 100, 1.5)), 620, 640)
    seq(img, t, ts[1] + 0.8, txt("PHONE OR INTERNET", 34, IVORY, 2), 500, 800)
    slide_in(img, t, ts[2], panel(760, 440, border=GOLD), 1330, 640, dx=70, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.2, txt("UP TO", 48, SAGE, 5), 1330, 530)
    counter(img, t, ts[2] + 0.3, 1.0, "$", 925, "", 150, GOLD, 1330, 650, fmt="{:.0f}") if False else None
    v = ease(seg(t, ts[2] + 0.3, 1.0));
    if t >= ts[2] + 0.3:
        sp = txt("$%.2f" % (9.25 * v), 150, GOLD, 3); full = txt("$9.25", 150, GOLD, 3)
        img.paste(sp, (int(1330 - full.width / 2), int(650 - sp.height / 2)), sp)
    seq(img, t, ts[2] + 1.0, txt("A MONTH", 54, IVORY, 4), 1330, 760)
    ban(img, t, ts[3] + 0.1, "OVER $100 A YEAR", cy=960, w=820, size=60)

# ============================================================ BLOCCO 24
def draw24(img, t):
    ts = starts(24)
    common(img, t, "WHERE YOU CAN USE IT")
    items = [(lambda c, x, y, s: ic_phone(c, x, y, s * 0.95), "PHONE PLAN"), (lambda c, x, y, s: ic_wifi(c, x, y - 10, s * 1.1), "INTERNET"),
             (lambda c, x, y, s: (ic_phone(c, x - 50, y, s * 0.7), ic_wifi(c, x + 54, y - 8, s * 0.9)), "A BUNDLE")]
    for k, (ic, name) in enumerate(items):
        s, a, p = pop(t, ts[0] + 0.2 + k * 0.55, 0.45)
        if p > 0:
            put(img, card(460, 340, ic, name, None, [SAGE, GOLD, ICE][k], 44), 360 + k * 600, 400, scale=s, alpha=a, shadow=12)
    slide_in(img, t, ts[1], panel(1640, 330, border=GOLD), 960, 800, dy=60, dur=0.6, shadow=16)
    seq(img, t, ts[1] + 0.3, sprite("pin24", 200, 240, lambda c: ic_pin(c, 100, 110, 2.2)), 330, 800, shadow=8)
    seq(img, t, ts[1] + 0.6, txt("QUALIFYING", 44, SAGE, 4), 700, 760)
    seq(img, t, ts[1] + 0.75, txt("TRIBAL LANDS", 64, IVORY, 3), 700, 840)
    seq(img, t, ts[2] - 0.1, txt("UP TO", 38, SAGE, 4), 1330, 735)
    if t >= ts[2] + 0.1:
        v = ease(seg(t, ts[2] + 0.1, 1.2))
        sp = txt("$%.2f" % (34.25 * v), 120, GOLD, 3); full = txt("$34.25", 120, GOLD, 3)
        img.paste(sp, (int(1330 - full.width / 2), int(810 - sp.height / 2)), sp)
    seq(img, t, ts[2] + 1.0, txt("A MONTH", 40, IVORY, 4), 1330, 890)

# ============================================================ BLOCCO 25
def draw25(img, t):
    ts = starts(25)
    common(img, t, "HOW YOU QUALIFY")
    seq(img, t, ts[0], stamp("HOW YOU QUALIFY", 760, 120, GOLD, size=52), 960, 200, shadow=12)
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, sprite("hub25", 260, 260, lambda c: (c.ell((6, 6, 254, 254), fill=PANEL_FILL, outline=GOLD, width=8), ic_phone(c, 130, 128, 1.5))), 960, 450, scale=s, alpha=a, shadow=12)
    seq(img, t, ts[1] + 0.5, txt("LIFELINE", 40, GOLD, 4), 960, 620)
    seq(img, t, ts[1] + 0.8, sprite("lk25", 150, 170, lambda c: (c.d.arc(c._b((38, 8, 112, 90)), 180, 360, fill=GOLD, width=22), c.rrect((20, 70, 130, 160), 16, fill=GOLD), c.ell((62, 96, 88, 122), fill=GREEN_D), c.rrect((70, 112, 80, 140), 3, fill=GREEN_D))), 1580, 440, scale=0.9)
    seq(img, t, ts[1] + 1.1, txt("THE ORDER MATTERS", 34, SAGE, 3), 1580, 550)
    p = ease(seg(t, ts[2], 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 700, 600, alpha=p, rot=-135 if False else 235, scale=0.9)
    slide_in(img, t, ts[2], card(560, 330, lambda c, x, y, s: [ic_coin(c, x - 40 + k * 40, y + (k % 2) * 6, 34) for k in range(3)], "INCOME", "LOW ENOUGH", GOLD, 54, 32), 520, 800, dy=40, dur=0.5, shadow=12)
    p = ease(seg(t, ts[3], 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 1220, 600, alpha=p, rot=-45, scale=0.9)
    slide_in(img, t, ts[3], card(700, 330, lambda c, x, y, s: [c.rrect((x - 70 + k * 36, y - 40 + k * 8, x + 6 + k * 36, y + 16 + k * 8), 8, fill=[SAGE, GOLD, CORAL][k], outline=GREEN_D, width=3) for k in range(3)], "BENEFITS", "YOU ALREADY GET", SAGE, 54, 32), 1400, 800, dy=40, dur=0.5, shadow=12)

# ============================================================ BLOCCO 26
CHIPS26 = ["SNAP", "MEDICAID", "S S I", "PUBLIC HOUSING", "VETERANS PENSION"]
def draw26(img, t):
    ts = starts(26)
    common(img, t, "BENEFITS THAT QUALIFY YOU")
    pos = [(480, 270), (960, 270), (1440, 270), (670, 420), (1250, 420)]
    for k, name in enumerate(CHIPS26):
        s, a, p = pop(t, ts[0] + 0.15 + k * 0.5, 0.4)
        if p > 0:
            x, y = pos[k]
            put(img, pill_spr(name, 40, (540 if k == 4 else 440) if k > 2 else 380, 110, PANEL_FILL, GOLD, border=GOLD, track=2), x, y, scale=s, alpha=a, shadow=8)
    p = ease(seg(t, ts[1], 0.5))
    if p > 0:
        put(img, sprite("dn26", 120, 160, lambda c: (c.rrect((40, 6, 80, 90), 8, fill=GOLD), c.poly([(8, 84), (112, 84), (60, 150)], fill=GOLD))), 960, 590, alpha=p)
    s, a, pp = pop(t, ts[1] + 0.2, 0.5)
    if pp > 0:
        put(img, sprite("lf26", 520, 200, lambda c: (c.rrect((5, 5, 515, 195), 40, fill=PANEL_FILL, outline=GOLD, width=8), ic_phone(c, 90, 100, 1.0), c.text((330, 100), "LIFELINE", FONT_SANS, 62, GOLD, track=4))), 960, 770, scale=s, alpha=a, shadow=12)
        check_at(img, t, ts[1] + 0.8, 1280, 700, 1.1)
    # niente prova del reddito
    s, a, pp = pop(t, ts[2], 0.5)
    if pp > 0:
        put(img, sprite("pay26", 200, 240, lambda c: (c.rrect((20, 10, 180, 230), 12, fill=IVORY, outline=(206, 200, 186), width=4), c.text((100, 56), "PAY", FONT_SANS, 34, GREEN_L), [c.rrect((44, 90 + k * 36, 156, 106 + k * 36), 5, fill=(206, 212, 206)) for k in range(3)], ic_x(c, 100, 130, 2.4, RED, 14))), 1620, 700, scale=0.9 * s, alpha=a, shadow=8)
    seq(img, t, ts[2] + 0.5, txt("NO NEW PROOF", 32, RED, 3), 1620, 850)
    seq(img, t, ts[2] + 0.65, txt("OF INCOME", 32, RED, 3), 1620, 890)

# ============================================================ BLOCCO 27
def draw27(img, t):
    ts = starts(27)
    common(img, t, "OR BY INCOME")
    seq(img, t, ts[0], stamp("BY INCOME", 480, 120, GOLD, size=60), 960, 205, shadow=12, rot=-2)
    slide_in(img, t, ts[1], panel(560, 560, border=SAGE), 460, 600, dx=-70, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, sprite("one27", 240, 280, lambda c: ic_person(c, 120, 150, 2.2, col=GOLD)), 460, 560, shadow=10)
    seq(img, t, ts[1] + 0.7, txt("1 PERSON", 56, IVORY, 4), 460, 770)
    seq(img, t, ts[1] + 0.9, txt("YEAR 2026", 36, SAGE, 4), 460, 830)
    slide_in(img, t, ts[2], panel(940, 560, border=GOLD), 1330, 600, dx=70, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.1, txt("UP TO", 54, SAGE, 6), 1330, 470)
    counter(img, t, ts[2] + 0.3, 1.6, "$", 21546, "", 150, GOLD, 1330, 620)
    seq(img, t, ts[2] + 1.0, txt("A YEAR", 60, IVORY, 6), 1330, 760)

# ============================================================ BLOCCO 28
def draw28(img, t):
    ts = starts(28)
    common(img, t, "WHO IT HELPS MOST")
    seq(img, t, ts[0], stamp("WHO IT HELPS MOST", 760, 120, GOLD, size=52), 960, 200, shadow=12)
    seq(img, t, ts[1], sprite("pe28", 260, 300, lambda c: ic_person(c, 130, 160, 2.2, col=GOLD)), 400, 520, shadow=10)
    seq(img, t, ts[1] + 0.4, pill_spr("SNAP", 40, 230, 90, PANEL_FILL, SAGE, border=SAGE, track=2), 290, 720, shadow=6)
    seq(img, t, ts[1] + 0.8, pill_spr("MEDICAID", 40, 300, 90, PANEL_FILL, SAGE, border=SAGE, track=2), 540, 720, shadow=6)
    slide_in(img, t, ts[2], sprite("fp28", 500, 460, lambda c: (c.rrect((5, 5, 495, 455), 36, fill=PANEL_FILL, outline=RED, width=7), ic_phone(c, 150, 190, 2.0), c.text((340, 140), "PHONE BILL", FONT_SANS, 36, IVORY, track=2), c.text((340, 220), "$$$", FONT_SANS, 80, RED, track=6))), 1100, 540, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.7, stamp("FULL PRICE", 380, 100, RED, size=46), 1100, 800, rot=-4, shadow=10)
    for k in range(4):
        s, a, p = pop(t, ts[3] + 0.1 + k * 0.4, 0.4)
        if p > 0:
            put(img, sprite(("yr28", k), 130, 150, lambda c, k=k: (c.rrect((3, 3, 127, 147), 20, fill=IVORY, outline=(206, 200, 186), width=4), c.rrect((3, 3, 127, 50), 20, fill=SAGE_D), c.text((65, 28), "YEAR", FONT_SANS, 26, IVORY, track=2), c.text((65, 100), str(k + 1), FONT_SERIF, 60, GREEN_D))), 1560 + (k % 2) * 150 - 70, 440 + (k // 2) * 180, scale=s, alpha=a, shadow=6)
    seq(img, t, ts[3] + 1.8, stamp("NEVER ASKED", 400, 100, RED, size=46), 1560, 780, rot=-3, shadow=10)

# ============================================================ BLOCCO 29
def draw29(img, t):
    ts = starts(29)
    common(img, t, "HOW TO GET IT")
    # passo 1
    slide_in(img, t, ts[0], panel(860, 330, border=GOLD), 520, 330, dx=-70, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.2, numbadge(1, 130), 190, 330, shadow=8)
    seq(img, t, ts[0] + 0.3, txt("APPLY", 44, SAGE, 5), 600, 250)
    seq(img, t, ts[0] + 0.5, sprite("web29", 640, 100, lambda c: (c.rrect((4, 4, 636, 96), 46, fill=IVORY, outline=GOLD, width=7), c.ell((26, 20, 78, 72), outline=GREEN_D, width=6), c.line([(26, 46), (78, 46)], GREEN_D, 5), c.text((360, 52), "lifelinesupport.org", FONT_SANS_M, 40, GREEN_D))), 600, 380, shadow=8)
    # passo 2
    slide_in(img, t, ts[1], panel(860, 330, border=GOLD), 1440, 330, dx=30, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.2, numbadge(2, 130), 1110, 330, shadow=8)
    seq(img, t, ts[1] + 0.3, txt("CONTACT A PARTICIPATING", 36, SAGE, 3), 1500, 260)
    seq(img, t, ts[1] + 0.45, txt("PHONE OR INTERNET COMPANY", 36, IVORY, 3), 1500, 320)
    seq(img, t, ts[1] + 0.7, sprite("co29", 360, 150, lambda c: (ic_phone(c, 80, 76, 0.9), ic_wifi(c, 190, 70, 1.0), c.rrect((250, 30, 330, 120), 8, fill=SAGE_D))), 1500, 410)
    # aiuto
    slide_in(img, t, ts[2], panel(1000, 330, border=SAGE), 650, 770, dy=60, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.2, sprite("hp29", 150, 200, lambda c: ic_phone(c, 75, 100, 1.4)), 210, 770)
    seq(img, t, ts[2] + 0.3, txt("NEED HELP? CALL", 36, SAGE, 3), 700, 700)
    typed(img, t, ts[2] + 0.5, ts[3] - 0.3, "1-800-234-9473", 92, GOLD, 700, 790)
    # 7 giorni
    for k, d in enumerate("MTWTFSS"):
        s, a, p = pop(t, ts[3] + 0.1 + k * 0.12, 0.35)
        if p > 0:
            put(img, sprite(("d29", k), 100, 100, lambda c, k=k, d=d: (c.ell((4, 4, 96, 96), fill=GOLD, outline=(168, 118, 40), width=5), c.text((50, 52), d, FONT_SANS, 48, GREEN_D))), 1300 + k * 92, 770, scale=0.85 * s, alpha=a, shadow=6)
    seq(img, t, ts[3] + 1.0, txt("SEVEN DAYS A WEEK", 40, GOLD, 4), 1570, 860)

# ============================================================ BLOCCO 30
def draw30(img, t):
    ts = starts(30)
    common(img, t, "THREE BILLS DONE")
    seq(img, t, ts[0], txt("3 BILLS", 110, GOLD, 6), 960, 190, shadow=10)
    for k, (fn, name, x) in enumerate(((ic_flame, "HEAT", 560), (ic_bolt, "ENERGY", 960), (ic_phone, "PHONE", 1360))):
        s, a, p = pop(t, ts[1] + 0.15 + k * 0.5, 0.45)
        if p > 0:
            put(img, sprite(("b30", k), 240, 240, lambda c, fn=fn: (c.ell((6, 6, 234, 234), fill=PANEL_FILL, outline=GOLD, width=7), fn(c, 120, 118, 1.2))), x, 390, scale=s, alpha=a, shadow=10)
            put(img, txt(name, 40, IVORY, 3), x, 560, alpha=a)
            check_at(img, t, ts[1] + 0.5 + k * 0.5, x + 100, 300, 0.9)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("q30", 560, 320, lambda c: (c.rrect((6, 6, 554, 314), 40, fill=PANEL_FILL, outline=RED, width=7), c.text((280, 120), "?", FONT_SERIF, 150, RED), c.text((280, 250), "NO PROGRAM CONNECTED", FONT_SANS, 32, IVORY, track=2))), 560, 800, scale=s, alpha=a, shadow=12)
    seq(img, t, ts[2] + 0.6, txt("BILLS MOST PEOPLE NEVER LINK", 32, SAGE, 3), 560, 985) if False else None
    p = ease(seg(t, ts[3], 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 160, 110), 960, 800, alpha=p)
    s, a, p = pop(t, ts[3] + 0.2, 0.5)
    if p > 0:
        put(img, sprite("fr30", 560, 320, lambda c: (c.rrect((6, 6, 554, 314), 40, fill=PANEL_FILL, outline=GOLD, width=7), ic_fridge(c, 120, 160, 1.4), ic_bag(c, 300, 170, 1.0), c.text((440, 270), "FOOD", FONT_SANS, 40, GOLD, track=3))), 1360, 800, scale=s, alpha=a, shadow=12)
    seq(img, t, ts[3] + 0.9, txt("YOUR FRIDGE", 40, IVORY, 3), 1360, 985) if False else None

DRAW = {16: draw16, 17: draw17, 18: draw18, 19: draw19, 20: draw20, 21: draw21, 22: draw22, 23: draw23, 24: draw24, 25: draw25, 26: draw26, 27: draw27, 28: draw28, 29: draw29, 30: draw30}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/bollette-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
