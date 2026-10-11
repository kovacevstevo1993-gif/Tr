import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8b2_5 import *
from v3lib import up_arrow, check, padlock, tax_form, building, clock

EVT = []
def E(fr, C, box, t, t0):
    EVT.append(t0); return P2(fr, C, box, t, t0)

def chipE(fr, text, cx, y, t, t0, **kw):
    if t > t0: EVT.append(t0)
    return chip(fr, text, cx, y, t, t0, **kw)

GREYC = (120, 140, 170)
def dark(col): return tuple(int(c * 0.28 + n * 0.72) for c, n in zip(col, card))

def slab(C, k, y, col, label, x0=130, w=780):
    d = ImageDraw.Draw(C); oc = col if col else (150, 175, 215)
    d.rounded_rectangle([x0, y, x0 + w, y + 120], radius=26, fill=(dark(col) if col else (32, 52, 84)) + (255,), outline=oc + (255,), width=6)
    d.ellipse([x0 + 24, y + 20, x0 + 104, y + 100], fill=oc + (255,))
    txt(C, str(k), BOLD(56), y + 30, navy, 255, x=x0 + 64)
    lab = label if col else 'LAYER %d' % k
    txt(C, lab, fit(lab, w - 190, 44), y + 36, white, 255, x=x0 + 130 + (w - 170) / 2)

def vbar(C, x, base_y, w, h, col, label, u=1.0, lab_size=34):
    d = ImageDraw.Draw(C); hh = h * u
    d.rounded_rectangle([x, base_y - hh, x + w, base_y], radius=14, fill=col + (255,), outline=white + (255,), width=3)
    txt(C, label, fit(label, w + 80, lab_size), base_y + 14, white, 255, x=x + w / 2)

def chart_card(fr, t, t0, x0, x1, col, title, hs, y0=250, y1=670, base=585):
    if t > t0:
        C = new(); card_(C, x0, y0, x1, y1, col, title, None, None)
        u = ease((t - t0 - 0.2) / 0.9); bw, gap = 100, 40; tot = len(hs) * bw + (len(hs) - 1) * gap; sx = (x0 + x1) / 2 - tot / 2
        for i, h in enumerate(hs): vbar(C, sx + i * (bw + gap), base, bw, h, col, 'YEAR %d' % (i + 1), u, 28)
        fr = E(fr, C, (x0 - 20, y0 - 20, x1 + 20, y1 + 20), t, t0)
    return fr

def stack_slabs(fr, t, t0, states, step=0.15):
    ys = {1: 530, 2: 390, 3: 250}
    for i, k in enumerate((1, 2, 3)):
        col, lab = states[k]
        if t > t0 + step * i:
            C = new(); slab(C, k, ys[k], col, lab); fr = E(fr, C, (110, ys[k] - 20, 930, ys[k] + 140), t, t0 + step * i)
    return fr

# ================= BLOCCO 6 =================
def s6a(t):
    fr = stage_live(t, 'BILL NUMBER ONE: PROPERTY TAX', 101, 56)
    t1, t2 = tm('Bill', 0.4, 0.0), tm('property', 1.0, 0.5)
    t3a, t3, t4, t5 = tm('homeowners', LASTP() - 3.2, 1.8), tm('sixty', LASTP() - 2.4, 2.4), tm('biggest', LASTP() - 1.5, 3.0), tm('every year', LASTP() - 0.7, 3.8)
    if t > t1:
        C = new(); ring_(C, 300, 440, 150, ease((t - t1) / 0.8), gold, 36)
        txt(C, 'BILL', BOLD(44), 340, white, 255, x=300); txt(C, '#1', BOLD(120), 385, goldL, 255, x=300)
        fr = E(fr, C, (130, 270, 470, 610), t, t1)
    if t > t2:
        C = new(); card_(C, 560, 260, 1120, 640, gold, None, None, None); house(C, 840, 420, 1.5, gold)
        txt(C, 'PROPERTY TAX', BOLD(58), 565, white, 255, x=840)
        fr = E(fr, C, (540, 240, 1140, 660), t, t2)
    for tk, y, col, text in [(t3a, 250, green, 'HOMEOWNERS'), (t3, 375, blue, 'OVER 65'), (t4, 500, red, 'THE BIGGEST BILL'), (t5, 625, gold, 'EVERY YEAR')]:
        if t > tk:
            C = new(); card_(C, 1180, y, 1800, y + 105, col, None, text, None, 46, white)
            fr = E(fr, C, (1160, y - 20, 1820, y + 125), t, tk)
    return frame(pill_last(fr, t, 'THE BILL THAT KEEPS COMING', PILL_Y, gold, navy, 54))

def s6b(t):
    fr = stage_live(t, 'EVEN AFTER THE MORTGAGE IS GONE', 102, 54)
    t1, t2, t3, t4 = tm('mortgage', 0.3, 0.0), tm('usually', LASTP() - 2.0, 1.5), tm('every time', LASTP() - 1.3, 2.2), tm('value', LASTP() - 0.7, 2.9)
    t0b = tm('gone', 1.2, 0.8)
    if t > t1:
        C = new(); card_(C, 130, 250, 660, 670, green, None, None, None); house(C, 395, 410, 1.3, green); check(C, 520, 345, 44, green)
        txt(C, 'MORTGAGE', BOLD(44), 548, white, 255, x=395); txt(C, 'PAID OFF', BOLD(54), 598, goldL, 255, x=395)
        fr = E(fr, C, (110, 230, 680, 690), t, t1)
    fr = chipE(fr, 'BALANCE: $0', 395, 690, t, t0b, col=green, size=40)
    fr = chart_card(fr, t, t2, 720, 1240, red, 'YOUR TAX BILL', [70, 120, 190])
    fr = chipE(fr, 'EVERY TIME', 1020, 690, t, t3, col=goldL, size=40)
    fr = chart_card(fr, t, t4, 1300, 1800, gold, 'HOME VALUE', [90, 150, 220])
    return frame(pill_last(fr, t, 'THE VALUE GOES UP, THE TAX GOES UP', PILL_Y, red, (255, 255, 255), 50))

# ================= BLOCCO 7 =================
def s7a(t):
    fr = stage_live(t, 'THREE BREAKS THAT STACK', 103)
    t1, t2, t3 = 0.0, tm('stack', LASTP() - 1.7, 1.2), tm('Layer', LASTP() - 0.9, 2.3)
    tc = tm('counties', 1.8, 1.2)
    fr = chipE(fr, 'STATES AND COUNTIES', 1380, 170, t, tc, col=goldL, size=36)
    fr = stack_slabs(fr, t, t1, {1: (None, ''), 2: (None, ''), 3: (None, '')}, 0.3)
    if t > t2:
        C = new(); up_arrow(C, 1100, 400, 2.2, goldL); txt(C, 'THEY STACK', BOLD(64), 345, white, 255, x=1480)
        fr = E(fr, C, (960, 230, 1800, 520), t, t2)
    if t > t3:
        C = new(); slab(C, 1, 530, gold, 'HOMESTEAD EXEMPTION'); fr = E(fr, C, (110, 510, 930, 670), t, t3)
        C = new(); card_(C, 960, 540, 1790, 680, gold, None, None, None); house(C, 1110, 612, 0.5, gold); txt(C, 'LAYER ONE', BOLD(60), 585, goldL, 255, x=1480)
        fr = E(fr, C, (940, 520, 1810, 700), t, t3)
    return frame(pill_last(fr, t, 'LAYER ONE: THE HOMESTEAD EXEMPTION', PILL_Y, gold, navy, 48))

def s7b(t):
    fr = stage_live(t, 'A SMALLER NUMBER TO TAX', 104)
    t1, t2, t2b = 0.0, tm('part', 1.0, 0.6), tm('part', 1.1, 0.7)
    t3, t3b, t4 = tm('county', LASTP() - 1.9, 2.2), tm('calculates', LASTP() - 1.3, 2.7), tm('smaller', LASTP() - 0.7, 3.2)
    if t > t1:
        C = new(); d = ImageDraw.Draw(C); base, x, w = 650, 200, 200
        d.rounded_rectangle([x, base - 270, x + w, base], radius=14, fill=(green if t > t4 else blue) + (255,), outline=white + (255,), width=3)
        s_ = ease((t - t2) / 0.8) * 270 if t > t2 else 0
        d.rounded_rectangle([x + s_, 250, x + w + s_, 380], radius=14, fill=(red if t > t2 else blue) + (255,), outline=white + (255,), width=3)
        if t > t2 + 0.5: txt(C, 'EXEMPTION', fit('EXEMPTION', 176, 32), 305, white, 255, x=x + w / 2 + s_)
        lab = 'TAXABLE VALUE' if t > t4 else 'HOME VALUE'; txt(C, lab, fit(lab, 300, 38), base + 14, white, 255, x=x + w / 2)
        fr = E(fr, C, (90, 220, 740, 720), t, t1)
    fr = chipE(fr, 'PART OF THE VALUE', 480, 170, t, t2b, col=red, size=34)
    if t > t3:
        C = new(); building(C, 1500, 430, 300, 240, gold); txt(C, 'COUNTY', BOLD(52), 575, white, 255, x=1500)
        fr = E(fr, C, (1340, 250, 1700, 640), t, t3)
    if t > t3b:
        C = new(); arrow_r(C, 1010, 1290, 450, goldL); txt(C, 'CALCULATES', BOLD(34), 395, white, 255, x=1150)
        fr = E(fr, C, (980, 370, 1320, 490), t, t3b)
    fr = chipE(fr, 'A SMALLER NUMBER', 690, 520, t, t4, col=green, size=36)
    return frame(pill_last(fr, t, 'PAY TAX ON A SMALLER NUMBER', PILL_Y, green, navy, 54))

# ================= BLOCCO 8 =================
def s8a(t):
    fr = stage_live(t, 'THE PART PEOPLE GET WRONG', 105)
    t1, t2, t3 = tm('Here', 0.3, 0.0), tm('places', LASTP() - 1.0, 1.0), tm('homestead', LASTP() - 0.5, 1.6)
    t0b = tm('part', 1.2, 0.8)
    if t > t1:
        C = new(); card_(C, 130, 250, 650, 680, gold, None, None, None); d = ImageDraw.Draw(C)
        d.polygon([(390, 300), (270, 510), (510, 510)], fill=gold + (255,), outline=white + (255,)); txt(C, '!', BOLD(130), 370, navy, 255, x=390)
        txt(C, 'COMMON', BOLD(46), 560, white, 255, x=390); txt(C, 'MISTAKE', BOLD(46), 612, white, 255, x=390)
        fr = E(fr, C, (110, 230, 670, 700), t, t1)
    fr = chipE(fr, 'ASSUMING IT IS AUTOMATIC', 390, 700, t, t0b, col=goldL, size=34)
    if t > t2:
        C = new(); card_(C, 700, 250, 1220, 680, blue, None, None, None); building(C, 960, 430, 260, 200, blue)
        txt(C, 'IN MOST', BOLD(46), 560, white, 255, x=960); txt(C, 'PLACES', BOLD(46), 612, white, 255, x=960)
        fr = E(fr, C, (680, 230, 1240, 700), t, t2)
    if t > t3:
        C = new(); card_(C, 1270, 250, 1790, 680, gold, None, None, None); house(C, 1530, 420, 1.2, gold)
        txt(C, 'HOMESTEAD', BOLD(46), 560, white, 255, x=1530); txt(C, 'EXEMPTION', BOLD(46), 612, white, 255, x=1530)
        fr = E(fr, C, (1250, 230, 1810, 700), t, t3)
    if t > LASTP():
        C = new(); cross(C, 1700, 300, 62, red); fr = P2(fr, C, (1600, 200, 1800, 400), t, LASTP())
    return frame(pill_last(fr, t, 'NOT AUTOMATIC', PILL_Y, red, (255, 255, 255), 56))

def s8b(t):
    fr = stage_live(t, 'FILE A SHORT FORM WITH YOUR COUNTY', 106, 50)
    t1, t2, t3 = tm('to file', 0.3, 0.0), tm('county', LASTP() - 1.6, 1.2), tm('deadline', LASTP() - 0.7, 2.0)
    t0b = tm('short', 1.1, 0.7)
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 680, gold, None, None, None); tax_form(C, 265, 280, 240, 300, 255, 'FORM'); d = ImageDraw.Draw(C)
        for k in range(4):
            fk = ease((t - t1 - 0.25 * k) / 0.7)
            if fk > 0: d.rounded_rectangle([285, 345 + k * 42, 285 + fk * 200, 361 + k * 42], radius=7, fill=gold + (255,))
        txt(C, 'FILE IT', BOLD(46), 610, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 700), t, t1)
    fr = chipE(fr, 'A SHORT FORM', 385, 700, t, t0b, col=goldL, size=36)
    if t > t2:
        C = new(); card_(C, 740, 250, 1250, 680, blue, None, None, None); building(C, 995, 430, 280, 210, blue); txt(C, 'YOUR COUNTY', BOLD(46), 600, white, 255, x=995)
        arrow_r(C, 645, 735, 440, goldL)
        fr = E(fr, C, (630, 230, 1270, 700), t, t2)
    if t > t3:
        C = new(); cal_card(C, 1350, 260, 1790, 640, 'DEADLINE', 'SPRING', 90, red); fr = E(fr, C, (1330, 240, 1810, 660), t, t3)
    return frame(pill_last(fr, t, 'FILE BY THE SPRING DEADLINE', PILL_Y, gold, navy, 52))

def s8c(t):
    fr = stage_live(t, 'FILE ONCE, KEEP IT', 107)
    t1, t2, t3 = tm('File it once', 0.3, 0.0), tm('stays', LASTP() - 1.7, 1.4), tm('own', LASTP() - 0.8, 2.2)
    t0b = tm('many', 1.2, 0.8)
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 680, green, None, None, None); check(C, 385, 400, 100, green); txt(C, 'FILE IT ONCE', BOLD(52), 560, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 700), t, t1)
    fr = chipE(fr, 'IN MANY STATES', 385, 700, t, t0b, col=goldL, size=36)
    if t > t2:
        C = new(); card_(C, 700, 250, 1210, 680, blue, None, None, None); padlock(C, 955, 410, 1.6, blue); txt(C, 'STAYS IN PLACE', BOLD(48), 600, white, 255, x=955)
        fr = E(fr, C, (680, 230, 1230, 700), t, t2)
    if t > t3:
        C = new(); card_(C, 1270, 250, 1790, 680, gold, None, None, None); house(C, 1530, 400, 1.2, gold)
        txt(C, 'AS LONG AS YOU', BOLD(44), 545, white, 255, x=1530); txt(C, 'OWN THE HOME', BOLD(44), 597, white, 255, x=1530)
        fr = E(fr, C, (1250, 230, 1810, 700), t, t3)
    return frame(pill_last(fr, t, 'ONE FORM, IT STAYS IN PLACE', PILL_Y, green, navy, 52))

# ================= BLOCCO 9 =================
def s9a(t):
    fr = stage_live(t, 'LAYER TWO: THE SENIOR EXEMPTION', 108, 54)
    t1, t2, t3 = tm('Layer', 0.4, 0.0), tm('sixty', LASTP() - 1.6, 1.4), tm('extra', LASTP() - 0.8, 2.3)
    tmany = tm('many', 2.2, 1.5)
    fr = stack_slabs(fr, t, t1, {1: (gold, 'HOMESTEAD'), 2: (green, 'SENIOR EXEMPTION'), 3: (None, '')})
    fr = chipE(fr, 'IN MANY PLACES', 1150, 610, t, tmany, col=goldL, size=36)
    if t > t2:
        C = new(); ring_(C, 1150, 420, 140, ease((t - t2) / 0.8), gold, 34); txt(C, 'AGE', BOLD(44), 345, white, 255, x=1150); txt(C, '65', BOLD(110), 385, goldL, 255, x=1150)
        fr = E(fr, C, (980, 260, 1320, 600), t, t2)
    if t > t3:
        C = new(); d = ImageDraw.Draw(C); base, x, w = 650, 1360, 200
        d.rounded_rectangle([x, base - 300, x + w, base], radius=14, fill=blue + (255,), outline=white + (255,), width=3)
        s_ = ease((t - t3 - 0.3) / 0.7) * 220
        d.rounded_rectangle([x + s_, base - 420, x + w + s_, base - 300], radius=14, fill=red + (255,), outline=white + (255,), width=3)
        txt(C, 'EXTRA', BOLD(38), base - 395, white, 255, x=x + w / 2 + s_); txt(C, 'PIECE', BOLD(38), base - 350, white, 255, x=x + w / 2 + s_)
        txt(C, 'HOME VALUE', BOLD(36), base + 14, white, 255, x=x + w / 2)
        fr = E(fr, C, (1330, 210, 1820, 710), t, t3)
    return frame(pill_last(fr, t, 'AN EXTRA PIECE REMOVED', PILL_Y, green, navy, 54))

def s9b(t):
    fr = stage_live(t, 'THE COUNTY WILL NOT TELL YOU', 109, 56)
    t1, t2, t3 = tm('The county', 0.3, 0.0), tm('ask', LASTP() - 1.5, 1.8), tm('name', LASTP() - 0.7, 2.6)
    t0b = tm('almost', 1.2, 0.8)
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 680, red, None, None, None); building(C, 385, 410, 280, 210, red); cross(C, 540, 300, 46, red)
        txt(C, 'NEVER TELLS', BOLD(44), 560, white, 255, x=385); txt(C, 'YOU', BOLD(44), 610, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 700), t, t1)
    fr = chipE(fr, 'ALMOST NEVER', 385, 700, t, t0b, col=red, size=36)
    if t > t2:
        C = new(); card_(C, 700, 250, 1210, 680, blue, None, None, None); phone(C, 955, 440, 1.2, 255, t - t2, True); txt(C, 'YOU ASK', BOLD(52), 600, white, 255, x=955)
        fr = E(fr, C, (680, 230, 1230, 700), t, t2)
    if t > t3:
        C = new(); card_(C, 1270, 250, 1790, 680, gold, 'BY NAME', 'SENIOR EXEMPTION', None, 60, goldL); check(C, 1530, 520, 70, green)
        fr = E(fr, C, (1250, 230, 1810, 700), t, t3)
    return frame(pill_last(fr, t, 'YOU MUST ASK FOR IT', PILL_Y, red, (255, 255, 255), 54))

def s9c(t):
    fr = stage_live(t, 'THE AMOUNT DEPENDS', 110)
    t1, t2, t3 = tm('amount', 0.3, 0.0), tm('state', LASTP() - 1.1, 0.8), tm('sometimes', LASTP() - 0.6, 1.4)
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 680, green, None, None, None); coin_stack(C, 385, 520, 5, 62); txt(C, 'THE AMOUNT', BOLD(50), 580, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 700), t, t1)
    if t > t2:
        C = new(); card_(C, 700, 250, 1210, 680, blue, None, None, None); building(C, 955, 420, 280, 210, blue); txt(C, 'YOUR STATE', BOLD(50), 580, white, 255, x=955)
        fr = E(fr, C, (680, 230, 1230, 700), t, t2)
    if t > t3:
        C = new(); card_(C, 1270, 250, 1790, 680, gold, None, None, None); wallet(C, 1530, 410, 1.5); txt(C, 'SOMETIMES', BOLD(46), 545, white, 255, x=1530); txt(C, 'YOUR INCOME', BOLD(46), 597, white, 255, x=1530)
        fr = E(fr, C, (1250, 230, 1810, 700), t, t3)
    return frame(pill_last(fr, t, 'THE AMOUNT VARIES', PILL_Y, gold, navy, 54))

# ================= BLOCCO 10 =================
def s10a(t):
    fr = stage_live(t, 'LAYER THREE: THE SENIOR FREEZE', 111, 54)
    t1, t2, t2b = tm('Layer', 0.3, 0.0), tm('matters', LASTP() - 1.3, 1.0), tm('over time', LASTP() - 0.6, 1.8)
    fr = stack_slabs(fr, t, t1, {1: (gold, 'HOMESTEAD'), 2: (green, 'SENIOR EXEMPTION'), 3: (blue, 'SENIOR FREEZE')})
    if t > t2:
        C = new(); card_(C, 970, 280, 1800, 620, gold, None, None, None); clock(C, 1130, 450, 95, t - t2, goldL, 255)
        txt(C, 'MATTERS MOST', BOLD(50), 400, white, 255, x=1545); txt(C, 'OVER TIME', BOLD(50), 465, goldL, 255, x=1545)
        fr = E(fr, C, (950, 260, 1820, 640), t, t2)
    fr = chipE(fr, 'OVER TIME', 1385, 670, t, t2b, col=goldL, size=36)
    return frame(pill_last(fr, t, 'THE SENIOR FREEZE', PILL_Y, blue, (255, 255, 255), 56))

def s10b(t):
    fr = stage_live(t, 'WHEN THE COUNTY LOCKS IT', 112)
    t1, t2, t3 = tm('states', 0.3, 0.0), tm('when', 1.1, 0.7), tm('apply', 2.8, 1.8)
    t4, t5 = tm('locks', LASTP() - 1.8, 3.2), tm('taxable', LASTP() - 1.0, 3.8)
    for tk, y, col, text in [(t1, 250, blue, 'IN SOME STATES'), (t2, 410, gold, 'WHEN YOU TURN 65'), (t3, 570, green, 'AND YOU APPLY')]:
        if t > tk:
            C = new(); card_(C, 130, y, 640, y + 130, col, None, None, None, 52, white); txt(C, text, fit(text, 400 if text == 'AND YOU APPLY' else 470, 50), y + 40, white, 255, x=(355 if text == 'AND YOU APPLY' else 385))
            if text == 'AND YOU APPLY': check(C, 585, y + 65, 28, green)
            fr = E(fr, C, (110, y - 20, 660, y + 150), t, tk)
    if t > t4:
        C = new(); card_(C, 690, 250, 1110, 700, blue, None, None, None); padlock(C, 900, 430, 1.7, gold, 255, t < t4 + 0.6); txt(C, 'LOCKED', BOLD(56), 630, white, 255, x=900)
        fr = E(fr, C, (670, 230, 1130, 720), t, t4)
    if t > t5:
        C = new(); card_(C, 1160, 250, 1800, 700, gold, None, None, None); d = ImageDraw.Draw(C); u = ease((t - t5 - 0.3) / 1.2)
        d.line([1200, 650, 1760, 650], fill=GREYC + (255,), width=4); d.line([1260, 300, 1260, 650], fill=GREYC + (255,), width=3)
        txt(C, 'AGE 65', BOLD(32), 270, goldL, 255, x=1260)
        xe = 1260 + u * 500; d.line([1260, 560, xe, 560 - (xe - 1260) / 500 * 250], fill=gold + (255,), width=9); d.line([1260, 560, xe, 560], fill=green + (255,), width=9)
        txt(C, 'HOME VALUE', BOLD(34), 335, goldL, 255, x=1440); txt(C, 'TAX LOCKED', BOLD(34), 600, green, 255, x=1560)
        fr = E(fr, C, (1140, 230, 1820, 720), t, t5)
    return frame(pill_last(fr, t, "LOCKED AT THAT YEAR'S LEVEL", PILL_Y, gold, navy, 50))

def spec(b, cuts_):
    j = V.j[str(b)]; D = round((j['end'] - j['start']) * 30)
    c = [0] + [round(V.at(b, p) * 30) for p in cuts_] + [D]
    return [c[i + 1] - c[i] for i in range(len(c) - 1)]

SLIDES = {6: [frozen(s6a), frozen(s6b)], 7: [frozen(s7a), frozen(s7b)], 8: [frozen(s8a), frozen(s8b), frozen(s8c)],
          9: [frozen(s9a), frozen(s9b), frozen(s9c)], 10: [frozen(s10a), frozen(s10b)]}
RAW = {6: [s6a, s6b], 7: [s7a, s7b], 8: [s8a, s8b, s8c], 9: [s9a, s9b, s9c], 10: [s10a, s10b]}
SPEC = {6: spec(6, ['even after']), 7: spec(7, ['It removes']), 8: spec(8, ['You have to file', 'File it once']),
        9: spec(9, ['The county will', 'and the amount']), 10: spec(10, ['In some states'])}
DUR = {6: 448, 7: 381, 8: 477, 9: 484, 10: 405}
for b in SPEC: assert sum(SPEC[b]) == DUR[b], (b, SPEC[b])

if __name__ == '__main__':
    if sys.argv[1] == 'spec': print(SPEC)
    elif sys.argv[1] == 'evt':
        for b in SPEC:
            for i, (fn, f) in enumerate(zip(RAW[b], SPEC[b]), 1):
                CUE['blk'] = b; CUE['t0'] = sum(SPEC[b][:i - 1]) / 30; CUR['D'] = f / 30; EVT.clear(); LIVE['t'] = 0.97 * f / 30; fn(0.97 * f / 30)
                ev = sorted(EVT); print([round(x_,2) for x_ in ev]); print(b, i, f, 'primo elemento %.2fs' % ev[0], 'secondo %.2fs' % (ev[1] if len(ev) > 1 else -1), 'n.elementi', len(ev), 'ultimo %.2fs' % ev[-1], 'pill %.2fs' % LASTP(), 'gap max %.1fs' % max([b_ - a_ for a_, b_ in zip(ev, ev[1:] + [LASTP()])]), 'OK' if ev[0] <= 0.45 and (len(ev) < 2 or ev[1] <= 1.35) else 'TROPPO TARDI')
    else: run(SPEC, SLIDES, 'v8', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
