from v3lib import *
from v3b3_10 import POP, new
from v4b2_10 import cal_card
from v5b1 import amb, sparks
from v5lib import arrow_r, arrow_d, paycheck
from v6b1 import A_, E_, chip_src
import v7b6_15 as M
from v7b6_15 import fit, stage, card_, eq, P2, pill_last, sp, ring_, bars3
from v7b2_5 import tracker, ic_med
from v7b31_35 import ic_levers2
from v7b36_40 import insurer
from v6b2 import logo
import sys, math

SPEC = {46: [156, 156, 156, 157], 47: [187, 187, 186], 48: [153, 153, 154], 49: [185, 185], 50: [229, 229], 51: [222, 222, 223], 52: [232, 233], 53: [357]}
TOT = {46: 625, 47: 560, 48: 460, 49: 370, 50: 458, 51: 667, 52: 465, 53: 357}
for b in SPEC: assert sum(SPEC[b]) == TOT[b], b

def dashed(C, x0, y0, x1, y1, col=goldL, w=6, dash=28, gap=18):
    d = ImageDraw.Draw(C)
    for (xa, ya, xb, yb) in [(x0, y0, x1, y0), (x0, y1, x1, y1), (x0, y0, x0, y1), (x1, y0, x1, y1)]:
        L = math.hypot(xb - xa, yb - ya); n = int(L // (dash + gap)) + 1
        for k in range(n):
            s0 = k * (dash + gap); s1 = min(L, s0 + dash)
            d.line([xa + (xb - xa) * s0 / L, ya + (yb - ya) * s0 / L, xa + (xb - xa) * s1 / L, ya + (yb - ya) * s1 / L], fill=col + (255,), width=w)

def dashed_circle(C, cx, cy, r, col=goldL, w=6):
    d = ImageDraw.Draw(C)
    for k in range(18): d.arc([cx - r, cy - r, cx + r, cy + r], start=k * 20, end=k * 20 + 12, fill=col + (255,), width=w)

def warn(C, cx, cy, s=1.0, col=(255, 200, 40)):
    d = ImageDraw.Draw(C); d.polygon([(cx, cy - 60 * s), (cx - 60 * s, cy + 48 * s), (cx + 60 * s, cy + 48 * s)], fill=A(col, 255), outline=A(navy, 255)); txt(C, '!', BOLD(int(70 * s)), cy - 28 * s, navy, 255, x=cx)

def thumb(C, cx, cy, s=1.0, col=goldL):
    d = ImageDraw.Draw(C); d.rounded_rectangle([cx - 70 * s, cy - 10 * s, cx - 30 * s, cy + 60 * s], radius=int(8 * s), fill=A(col, 255))
    d.polygon([(cx - 22 * s, cy - 6 * s), (cx + 6 * s, cy - 70 * s), (cx + 30 * s, cy - 62 * s), (cx + 22 * s, cy - 14 * s), (cx + 74 * s, cy - 14 * s), (cx + 60 * s, cy + 56 * s), (cx - 22 * s, cy + 60 * s)], fill=A(col, 255))

# ============ 46 ============
def s46a(t):
    fr = stage(t, 'SPLITTING WITH AN ANNUITY', 191); T = sp(3)
    if t > T[0]:
        C = new(); insurer(C, 380, 450, 1.0); fr = P2(fr, C, (190, 230, 570, 650), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 600, 740, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 760, 250, 1500, 620, green, 'ADDS ABOUT', '+$725', 'A MONTH FROM SAVINGS', 190, white); up_arrow(C, 1420, 520, 0.6, green); fr = P2(fr, C, (740, 230, 1520, 640), t, T[1])
    return frame(pill_last(fr, t, 'SPLITTING WITH AN ANNUITY: ABOUT +$725 A MONTH', 790, green, navy, 46))

def s46b(t):
    fr = stage(t, 'SPENDING FLEXIBLY', 192); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 250, 250, 1090, 620, green, 'COULD ADD ABOUT', '+$750', 'A MONTH', 200, white); fr = P2(fr, C, (230, 230, 1110, 640), t, T[0])
    if t > T[1]:
        C = new(); warn(C, 1420, 380, 1.8); txt(C, 'MORE RISK', BOLD(64), 520, (255, 200, 40), 255, x=1420); fr = P2(fr, C, (1230, 250, 1620, 600), t, T[1])
    return frame(pill_last(fr, t, 'FLEXIBLE SPENDING: ABOUT +$750 A MONTH, WITH MORE RISK', 790, gold, navy, 44))

def s46c(t):
    fr = stage(t, 'RETIRING EARLIER', 193); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 250, 250, 1090, 620, red, 'RETIRING EARLIER', 'REMOVES INCOME', 'INSTEAD OF ADDING IT', 74, white); fr = P2(fr, C, (230, 230, 1110, 640), t, T[0])
    if t > T[1]:
        C = new(); arrow_d(C, 1450, 260, 520, red, 255); down = ImageDraw.Draw(C); txt(C, 'LESS', BOLD(80), 560, red, 255, x=1450); fr = P2(fr, C, (1300, 240, 1600, 660), t, T[1])
    return frame(pill_last(fr, t, 'RETIRING EARLIER REMOVES INCOME INSTEAD OF ADDING IT', 790, red, (255, 255, 255), 42))

def s46d(t):
    fr = stage(t, 'AND THE GAP?', 194); T = sp(4)
    fr = bars3(fr, t, 690, [('MARY, AFTER PART B', '$3,493', 3493 / 5100, (90, 130, 190), white), ('AVERAGE HOUSEHOLD SPENDING', '$5,100', 1.0, red, white)], [T[0], T[1]], 430, 340, 260)
    if t > T[2]:
        C = new(); card_(C, 1460, 300, 1850, 460, gold, 'REMEMBER', 'THE GAP', None, 62, goldL); fr = P2(fr, C, (1440, 280, 1870, 480), t, T[2])
    return frame(pill_last(fr, t, 'THE AVERAGE HOUSEHOLD SPENDS ABOUT $5,100 A MONTH', 830, red, (255, 255, 255), 44))

# ============ 47 ============
def s47a(t):
    fr = stage(t, 'NO SINGLE CHOICE CLOSES THE GAP ALONE', 195, 56); T = sp(5)
    if t > T[0]:
        C = new(); card_(C, 130, 250, 640, 620, red, 'THE GAP', '$1,423', 'ABOUT, A MONTH', 150, white); fr = P2(fr, C, (110, 230, 660, 640), t, T[0])
    chips = [('AGE 70', '+$497', gold), ('ANNUITY', '+$725', blue), ('FLEXIBLE', '+$750', green)]
    for k, (a, b2, col) in enumerate(chips):
        if t > T[k + 1]:
            C = new(); card_(C, 720 + k * 370, 300, 1060 + k * 370 - 10, 560, col, a, b2, 'SMALLER THAN THE GAP', 80, white); fr = P2(fr, C, (700 + k * 370, 280, 1080 + k * 370, 580), t, T[k + 1])
    return frame(pill_last(fr, t, 'EACH ONE ALONE IS SMALLER THAN THE GAP', 780, gold, navy, 48))

def s47b(t):
    fr = stage(t, 'EVERY CHOICE HAS A TRADE-OFF', 196); T = sp(4)
    labs = [('A SMALLER', 'INHERITANCE', gold, 'b'), ('LESS', 'FLEXIBILITY', blue, 'l'), ('MORE', 'RISK', red, 'w')]
    for k, (a, b2, col, ic) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 260, x0 + 500, 620], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            if ic == 'b': money_bag(C, x0 + 250, 385, 0.75)
            elif ic == 'l': padlock(C, x0 + 250, 375, 0.9, blue)
            else: warn(C, x0 + 250, 375, 1.3)
            txt(C, a, BOLD(46), 510, white, 255, x=x0 + 250); txt(C, b2, fit(b2, 460, 52), 562, col, 255, x=x0 + 250); fr = P2(fr, C, (x0 - 20, 240, x0 + 520, 640), t, T[k])
    return frame(pill_last(fr, t, 'A SMALLER INHERITANCE, LESS FLEXIBILITY, OR MORE RISK', 790, gold, navy, 44))

def s47c(t):
    fr = stage(t, 'THE HONEST ANSWER', 197); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 460, 240, 1460, 400, gold, 'CAN YOU RETIRE WITH', '$500,000?', None, 90, goldL); fr = P2(fr, C, (440, 220, 1480, 420), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 260, 470, 960, 650, green, 'IT DEPENDS ON', 'YOUR EXPENSES', None, 80, white); fr = P2(fr, C, (240, 450, 980, 670), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1000, 470, 1660, 650, red, 'NOT ON', 'THE NUMBER', None, 80, white); cross(C, 1600, 500, 36, red); fr = P2(fr, C, (980, 450, 1680, 670), t, T[2])
    return frame(pill_last(fr, t, 'IT DEPENDS ON YOUR EXPENSES, NOT ON THE NUMBER', 810, gold, navy, 46))

# ============ 48 ============
def source_cards(fr, t, T, items):
    for k, (head, sub, ic) in enumerate(items):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 260, x0 + 500, 640], radius=34, fill=card + (255,), outline=goldL + (255,), width=6)
            if ic == 'b': building(C, x0 + 250, 400, 190, 150, blue)
            elif ic == 'm': ic_med(C, x0 + 250, 400)
            else: tax_form(C, x0 + 190, 330, 120, 150, 255, 'TAX')
            txt(C, head, fit(head, 460, 54), 500, goldL, 255, x=x0 + 250); txt(C, sub, fit(sub, 460, 40), 570, white, 255, x=x0 + 250); fr = P2(fr, C, (x0 - 20, 240, x0 + 520, 660), t, T[k])
    return fr

def s48a(t):
    fr = stage(t, 'A WORD ABOUT SOURCES', 198); T = sp(3)
    fr = source_cards(fr, t, [T[0], 99, 99], [('SOCIAL SECURITY', 'ADMINISTRATION: THE SS NUMBERS', 'b')])
    return frame(pill_last(fr, t, 'SOCIAL SECURITY NUMBERS: SOCIAL SECURITY ADMINISTRATION', 790, gold, navy, 42))

def s48b(t):
    fr = stage(t, 'A WORD ABOUT SOURCES', 199); T = sp(3)
    fr = source_cards(fr, t, [0.1, T[0], 99], [('SOCIAL SECURITY', 'ADMINISTRATION: THE SS NUMBERS', 'b'), ('MEDICARE & MEDICAID', 'SERVICES: THE PREMIUM', 'm')])
    return frame(pill_last(fr, t, 'MEDICARE PREMIUM: CENTERS FOR MEDICARE AND MEDICAID SERVICES', 790, red, (255, 255, 255), 40))

def s48c(t):
    fr = stage(t, 'A WORD ABOUT SOURCES', 200); T = sp(3)
    fr = source_cards(fr, t, [0.1, 0.15, T[0]], [('SOCIAL SECURITY', 'ADMINISTRATION: THE SS NUMBERS', 'b'), ('MEDICARE & MEDICAID', 'SERVICES: THE PREMIUM', 'm'), ('IRS', 'INTERNAL REVENUE SERVICE: TAXES', 't')])
    return frame(pill_last(fr, t, 'TAX NUMBERS: INTERNAL REVENUE SERVICE', 790, gold, navy, 48))

# ============ 49 ============
def s49a(t):
    fr = stage(t, 'MORE SOURCES', 201); T = sp(4)
    labs = [('BUREAU OF LABOR', 'STATISTICS: SPENDING', 'b'), ('FEDERAL RESERVE:', 'THE SAVINGS DATA', 'f'), ('MORNINGSTAR:', 'THE WITHDRAWAL ESTIMATE', 'm')]
    for k, (a, b2, ic) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 260, x0 + 500, 640], radius=34, fill=card + (255,), outline=goldL + (255,), width=6)
            if ic == 'b': building(C, x0 + 250, 400, 190, 150, blue)
            elif ic == 'f': coin_stack(C, x0 + 250, 450, 5, 56)
            else: ring_(C, x0 + 250, 400, 70, 0.039 * 8, gold, 30); txt(C, '3.9%', BOLD(44), 378, goldL, 255, x=x0 + 250)
            txt(C, a, fit(a, 460, 46), 500, goldL, 255, x=x0 + 250); txt(C, b2, fit(b2, 460, 36), 565, white, 255, x=x0 + 250); fr = P2(fr, C, (x0 - 20, 240, x0 + 520, 660), t, T[k])
    return frame(pill_last(fr, t, 'SPENDING, SAVINGS AND THE WITHDRAWAL ESTIMATE', 790, gold, navy, 46))

def s49b(t):
    fr = stage(t, 'EVERY SOURCE IS IN THE DESCRIPTION', 202, 58); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([260, 240, 900, 660], radius=26, fill=(236, 240, 245, 255), outline=goldL + (255,), width=6)
        txt(C, 'DESCRIPTION', BOLD(46), 262, (30, 40, 70), 255, x=580)
        for k, lab in enumerate(['SSA.GOV', 'CMS.GOV', 'IRS.GOV', 'BLS.GOV', 'FEDERAL RESERVE', 'MORNINGSTAR']): d.rectangle([310, 345 + k * 52, 330, 365 + k * 52], fill=green + (255,)); txt(C, lab, BOLD(32), 340 + k * 52, (50, 64, 90), 255, x=360, anchor='l')
        fr = P2(fr, C, (240, 220, 920, 680), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 980, 300, 1740, 600, red, 'YOUR OWN NUMBERS', 'MAY BE DIFFERENT', 'CHECK THE OFFICIAL SOURCE', 64, white); fr = P2(fr, C, (960, 280, 1760, 620), t, T[1])
    return frame(pill_last(fr, t, 'YOUR OWN NUMBERS MAY BE DIFFERENT', 790, red, (255, 255, 255), 50))

# ============ 50 ============
def s50a(t):
    fr = stage(t, 'RECAP: THE FIVE NUMBERS', 203); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 140, 250, 900, 640, gold, 'NUMBER ONE: A SAFE STARTING WITHDRAWAL', '3.9% TO 4%', 'ABOUT $1,625 A MONTH', 150, goldL); ic_coins2(C, 780, 560); fr = P2(fr, C, (120, 230, 920, 660), t, T[0])
    if t > T[1]:
        C = new(); ring_(C, 1400, 440, 170, 0.04 * 6, gold, 50); txt(C, '4%', BOLD(120), 380, goldL, 255, x=1400); fr = P2(fr, C, (1200, 240, 1600, 660), t, T[1])
    return frame(pill_last(tracker(fr, t, {1}, 0.3, 965), t, 'ONE: A SAFE START NEAR 4%, ABOUT $1,625 A MONTH', 810, gold, navy, 44))

def ic_coins2(C, cx, cy): coin_stack(C, cx, cy, 3, 40)

def s50b(t):
    fr = stage(t, 'RECAP: THE FIVE NUMBERS', 204); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 140, 250, 900, 640, blue, 'NUMBER TWO: SOCIAL SECURITY ADDS', '$2,071', 'THE AVERAGE CHECK, A MONTH', 190, white); fr = P2(fr, C, (120, 230, 920, 660), t, T[0])
    if t > T[1]:
        C = new(); building(C, 1400, 450, 380, 300, blue); fr = P2(fr, C, (1160, 230, 1640, 700), t, T[1])
    return frame(pill_last(tracker(fr, t, {1, 2}, 0.3, 965), t, 'TWO: SOCIAL SECURITY ADDS THE AVERAGE $2,071', 810, blue, navy, 44))

# ============ 51 ============
def s51a(t):
    fr = stage(t, 'RECAP: NUMBER THREE', 205); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 140, 250, 800, 640, red, 'MEDICARE PART B TAKES', '$202.90', 'A MONTH, FROM THE CHECK', 150, white); fr = P2(fr, C, (120, 230, 820, 660), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 880, 250, 1780, 640, green, 'FEDERAL INCOME TAX', '$0', 'IN THIS EXAMPLE, OR CLOSE TO IT', 200, white); check(C, 1700, 330, 40, green); fr = P2(fr, C, (860, 230, 1800, 660), t, T[1])
    return frame(pill_last(tracker(fr, t, {1, 2, 3}, 0.3, 965), t, 'THREE: PART B TAKES $202.90. FEDERAL TAX: ZERO OR CLOSE.', 810, red, (255, 255, 255), 42))

def s51b(t):
    fr = stage(t, 'RECAP: NUMBER FOUR', 206); T = sp(4)
    labs = [('THE AVERAGE', 'HOUSEHOLD SPENDS MORE', red, 'h'), ('INFLATION', 'RAISES PRICES', gold, 'c'), ('A BAD EARLY', 'MARKET HURTS', blue, 'm')]
    for k, (a, b2, col, ic) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 260, x0 + 500, 620], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            if ic == 'h': house(C, x0 + 250, 380, 1.2, gold)
            elif ic == 'c': cart(C, x0 + 270, 410, 1.2, 255, gold)
            else: line_chart(C, x0 + 70, 320, x0 + 430, 460, [(0, 0.1), (0.4, 0.2), (0.6, 0.9), (1, 1.0)], red, 1.0, 12)
            txt(C, a, BOLD(46), 500, white, 255, x=x0 + 250); txt(C, b2, fit(b2, 460, 40), 555, col, 255, x=x0 + 250); fr = P2(fr, C, (x0 - 20, 240, x0 + 520, 640), t, T[k])
    return frame(pill_last(tracker(fr, t, {1, 2, 3, 4}, 0.3, 965), t, 'FOUR: THE GAP, INFLATION AND A BAD EARLY MARKET', 810, red, (255, 255, 255), 42))

def s51c(t):
    fr = stage(t, 'RECAP: NUMBER FIVE', 207); T = sp(6)
    labs = [('CLAIMING', 'AGE', gold), ('AN', 'ANNUITY', blue), ('FLEXIBILITY', '', green), ('THE RETIREMENT', 'DATE', red)]
    for k, (a, b2, col) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 130 + k * 440; d.rounded_rectangle([x0, 280, x0 + 400, 600], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            d.ellipse([x0 + 150, 310, x0 + 250, 410], fill=col + (255,)); txt(C, str(k + 1), BOLD(70), 322, navy, 255, x=x0 + 200); txt(C, a, fit(a, 340, 40), 450, white, 255, x=x0 + 200)
            if b2: txt(C, b2, BOLD(40), 505, white, 255, x=x0 + 200)
            fr = P2(fr, C, (x0 - 20, 260, x0 + 420, 620), t, T[k])
    return frame(pill_last(tracker(fr, t, {1, 2, 3, 4, 5}, 0.3, 965), t, 'FIVE: FOUR THINGS CAN CHANGE THE ANSWER', 790, purple, navy, 46))

def house(C, cx, cy, s=1.0, col=gold):
    d = ImageDraw.Draw(C); d.polygon([(cx - 100 * s, cy), (cx, cy - 80 * s), (cx + 100 * s, cy)], fill=A(red, 255)); d.rectangle([cx - 80 * s, cy, cx + 80 * s, cy + 90 * s], fill=A(col, 255)); d.rectangle([cx - 20 * s, cy + 30 * s, cx + 20 * s, cy + 90 * s], fill=A(navy, 255))

def line_chart(C, x0, y0, x1, y1, pts, col, prog, w=12):
    d = ImageDraw.Draw(C); P = [(x0 + (x1 - x0) * px, y0 + (y1 - y0) * py) for px, py in pts]; n = max(2, int(len(P) * prog) + 1); d.line(P[:n], fill=A(col, 255), width=w, joint='curve')

# ============ 52 ============
def s52a(t):
    fr = stage(t, 'IF THIS HELPED', 208); T = sp(4)
    if t > T[0]:
        C = new(); thumb(C, 480, 430, 2.4); txt(C, 'LIKE', BOLD(70), 600, goldL, 255, x=480); fr = P2(fr, C, (260, 240, 700, 680), t, T[0])
    if t > T[1]:
        L = new(); txt(L, '+', BOLD(130), 400, goldL, 255 * E_(t, T[1]), x=860); fr = Image.alpha_composite(fr, L)
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1000, 360, 1700, 500], radius=70, fill=red + (255,)); txt(C, 'SUBSCRIBE', BOLD(70), 390, white, 255, x=1350); logo(C, 1120, 640, 80); txt(C, 'THE MONEY', SER(44), 600, goldL, 255, x=1480); txt(C, 'BACKSTORY', SER(44), 655, goldL, 255, x=1480); fr = P2(fr, C, (980, 240, 1720, 760), t, T[1])
    return frame(pill_last(fr, t, 'TAP LIKE AND SUBSCRIBE TO THE MONEY BACKSTORY', 810, red, (255, 255, 255), 44))

def s52b(t):
    fr = stage(t, 'WATCH NEXT', 209); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([140, 240, 1050, 640], radius=34, fill=card + (255,), outline=goldL + (255,), width=6)
        d.rounded_rectangle([190, 300, 560, 560], radius=18, fill=A((60, 90, 140), 255)); d.polygon([(330, 360), (330, 500), (440, 430)], fill=A(white, 255))
        txt(C, 'CLAIMING AT', BOLD(40), 320, white, 255, x=810); txt(C, '62 VS 70', BOLD(80), 375, goldL, 255, x=810); txt(C, 'THE $124,800', BOLD(34), 485, grey, 255, x=810); txt(C, 'MISTAKE', BOLD(34), 525, grey, 255, x=810); fr = P2(fr, C, (120, 220, 1070, 660), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 1060, 1180, 440, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1200, 270, 1790, 610, gold, 'THE AGE YOU CLAIM CHANGES', 'LIFETIME INCOME', 'BY MORE THAN $124,800', 50, goldL); fr = P2(fr, C, (1180, 250, 1810, 630), t, T[1])
    return frame(pill_last(fr, t, 'THAT VIDEO IS RIGHT ON YOUR SCREEN NOW', 800, gold, navy, 48))

# ============ 53 ============
def s53a(t):
    fr = base(t); fr = amb(fr, t, 211, 7, 55); fr = title_layer(fr, 'IMPORTANT', t, size=64); D = 357 / 30
    lines = [('Rules, amounts and ages change', white, 250), ('and differ by location and plan.', white, 315), ('Always confirm with the official', goldL, 410), ('source before you rely on them.', goldL, 475), ('General information,', white, 570), ('not financial advice.', white, 635)]
    for k, (tx, cl, yy) in enumerate([lines[0:2], lines[2:4], lines[4:6]][0:3] and []):
        pass
    groups = [lines[0:2], lines[2:4], lines[4:6]]; tg = [0.3, 0.3 + (0.6 * D - 0.3) / 2, 0.6 * D]
    for g, ts in zip(groups, tg):
        if t > ts:
            C = new()
            for tx, cl, yy in g: txt(C, tx, BOLD(52), yy, cl, 255, x=650)
            fr = A_(fr, C, (140, 240, 1160, 770), t, ts)
    if t > 0.68 * D:
        C = new(); dashed(C, 1220, 280, 1780, 640); txt(C, 'WATCH NEXT', BOLD(56), 430, goldL, 255, x=1500); fr = A_(fr, C, (1200, 260, 1800, 660), t, 0.68 * D)
    if t > 0.8 * D - 0.4:
        C = new(); dashed_circle(C, 260, 860, 85); txt(C, 'SUBSCRIBE', BOLD(44), 835, goldL, 255, x=560); fr = A_(fr, C, (160, 760, 760, 960), t, 0.8 * D - 0.4)
    return frame(fr)

SLIDES = {46: [s46a, s46b, s46c, s46d], 47: [s47a, s47b, s47c], 48: [s48a, s48b, s48c], 49: [s49a, s49b], 50: [s50a, s50b], 51: [s51a, s51b, s51c], 52: [s52a, s52b], 53: [s53a]}

if __name__ == '__main__':
    mode = sys.argv[1]; blk = int(sys.argv[2]); sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
    OUT = '/tmp/claude-0/-home-user-Tr/ca75d3ba-ecb8-59f6-9dcd-864234e0ec2e/scratchpad/w7/out/'
    for i, (fn, f) in enumerate(zip(SLIDES[blk], SPEC[blk]), 1):
        if sel and i not in sel: continue
        M.CUR['D'] = f / 30
        if mode == 'preview':
            for fq in [0.25, 0.5, 0.78, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((960, 540)).save(f'{OUT}pv{blk}_{i}_{int(fq*100)}.png')
        else:
            render_fast(fn, f, f'{OUT}v7-b{blk}-0{i}.mp4'); print('done', blk, i, f, flush=True)
    if mode == 'preview': print(blk, SPEC[blk], sum(SPEC[blk]))
