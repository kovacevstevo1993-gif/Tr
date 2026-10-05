from v3lib import *
from v3b3_10 import POP, new
from v4b2_10 import cal_card
from v5b1 import amb, sparks
from v5lib import arrow_r, arrow_d, paycheck
from v6b1 import A_, E_, chip_src
import v7b6_15 as M
from v7b6_15 import fit, stage, card_, eq, P2, pill_last, sp, ring_, bars3, avatars
from v7b2_5 import tracker, ic_med
from v7b16_20 import ic_bed
import sys, math

SPEC = {21: [150, 200, 294], 22: [150, 130, 328], 23: [200, 140, 125], 24: [150, 245, 140], 25: [230, 150, 186],
        26: [250, 130, 222], 27: [130, 240, 166], 28: [190, 120, 238], 29: [230, 170, 202], 30: [150, 150, 177]}
TOT = {21: 644, 22: 608, 23: 465, 24: 535, 25: 566, 26: 602, 27: 536, 28: 548, 29: 602, 30: 477}
for b in SPEC: assert sum(SPEC[b]) == TOT[b], b
D = M.D

def house(C, cx, cy, s=1.0, col=gold):
    d = ImageDraw.Draw(C)
    d.polygon([(cx - 100 * s, cy), (cx, cy - 80 * s), (cx + 100 * s, cy)], fill=A(red, 255))
    d.rectangle([cx - 80 * s, cy, cx + 80 * s, cy + 90 * s], fill=A(col, 255)); d.rectangle([cx - 20 * s, cy + 30 * s, cx + 20 * s, cy + 90 * s], fill=A(navy, 255))

def line_chart(C, x0, y0, x1, y1, pts, col, prog, w=12):
    d = ImageDraw.Draw(C); P = [(x0 + (x1 - x0) * px, y0 + (y1 - y0) * py) for px, py in pts]
    n = max(2, int(len(P) * prog) + 1); d.line(P[:n], fill=A(col, 255), width=w, joint='curve')

# ============ BLOCCO 21 ============
def s21a(t):
    fr = stage(t, 'FRANK OWES NO FEDERAL INCOME TAX', 91, 58); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 150, 280, 780, 620, green, "FRANK'S TAXABLE INCOME", '$22,963', 'BELOW THE DEDUCTION', 130, white); fr = P2(fr, C, (130, 260, 800, 640), t, T[0])
    if t > T[1]:
        L = new(); txt(L, '<', BOLD(150), 380, goldL, 255 * E_(t, T[1]), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1140, 280, 1770, 620, gold, 'TOTAL DEDUCTIONS', '$24,150', 'STANDARD + SENIOR', 130, goldL); fr = P2(fr, C, (1120, 260, 1790, 640), t, T[1])
    if t > T[2]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([430, 650, 1490, 780], radius=40, fill=green + (255,)); txt(C, 'FEDERAL INCOME TAX: $0', BOLD(62), 680, navy, 255, x=900); check(C, 1380, 715, 36, navy)
        fr = P2(fr, C, (410, 630, 1510, 800), t, T[2])
    return frame(fr)

def s21b(t):
    fr = stage(t, 'MARY: HALF HER SAVINGS IN A ROTH', 92, 58); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([140, 260, 900, 650], radius=34, fill=card + (255,), outline=pink + (255,), width=6)
        avatar(C, 290, 430, pink, 2.4); txt(C, 'MARY', BOLD(54), 560, pink, 255, x=290)
        d.rounded_rectangle([430, 300, 870, 405], radius=18, fill=A((50, 130, 90), 255), outline=goldL + (255,), width=4); txt(C, 'ROTH', BOLD(36), 308, white, 255, x=650); txt(C, '$250,000', BOLD(52), 345, goldL, 255, x=650)
        d.rounded_rectangle([430, 420, 870, 525], radius=18, fill=A((60, 90, 140), 255), outline=grey + (255,), width=4); txt(C, 'TRADITIONAL', BOLD(36), 428, white, 255, x=650); txt(C, '$250,000', BOLD(52), 465, white, 255, x=650)
        fr = P2(fr, C, (120, 240, 920, 670), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 1060, 260, 1780, 460, green, 'ROTH WITHDRAWALS', 'NOT TAXABLE INCOME', None, 56, white); fr = P2(fr, C, (1040, 240, 1800, 480), t, T[1])
        L = new(); arrow_r(L, 910, 1050, 360, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); card_(C, 1060, 490, 1780, 650, blue, 'EVEN LESS TAXABLE INCOME', 'THAN FRANK', None, 52, white); fr = P2(fr, C, (1040, 470, 1800, 670), t, T[2])
    return frame(pill_last(fr, t, 'MARY OWES NONE EITHER', 780, green, navy, 54))

def s21c(t):
    fr = stage(t, 'WITHOUT THE TEMPORARY SENIOR DEDUCTION', 93, 54); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 150, 270, 780, 560, red, 'FRANK WOULD OWE', '$481', 'ABOUT, A YEAR', 150, white); fr = P2(fr, C, (130, 250, 800, 580), t, T[0])
    if t > T[1]:
        L = new(); txt(L, 'VS', BOLD(100), 360, goldL, 255 * E_(t, T[1]), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1140, 270, 1770, 560, green, 'MARY WOULD STILL OWE', '$0', None, 170, white); fr = P2(fr, C, (1120, 250, 1790, 580), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 410, 600, 1510, 790, gold, 'FRANK: ($22,963 - $18,150) × 10%', '$481.30', None, 80, goldL); fr = P2(fr, C, (390, 580, 1530, 810), t, T[2])
    return frame(pill_last(fr, t, 'WITHOUT THE EXTRA DEDUCTION: FRANK ABOUT $481, MARY $0', 860, red, (255, 255, 255), 40))

# ============ BLOCCO 22 ============
def s22a(t):
    fr = stage(t, 'SAME SAVINGS, A DIFFERENT TYPE OF ACCOUNT', 94, 54); T = sp(3)
    for k, (nm, col, acc, tx, x0) in enumerate([('FRANK', blue, 'TRADITIONAL 401(k)', '$0 TAX', 150), ('MARY', pink, 'HALF ROTH', '$0 TAX', 1020)]):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([x0, 270, x0 + 750, 650], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            avatar(C, x0 + 140, 430, col, 2.4); txt(C, nm, BOLD(54), 560, col, 255, x=x0 + 140)
            txt(C, '$500,000', BOLD(80), 340, goldL, 255, x=x0 + 480); txt(C, acc, BOLD(46), 450, white, 255, x=x0 + 480)
            txt(C, 'WITH THE SENIOR DEDUCTION', BOLD(30), 570, grey, 255, x=x0 + 480)
            fr = P2(fr, C, (x0 - 20, 250, x0 + 770, 670), t, T[k])
    if t > T[2]: fr = chip(fr, 'DIFFERENT ACCOUNT, DIFFERENT RESULT WITHOUT THE EXTRA DEDUCTION', 960, 700, t, T[2], goldL, 38) if False else fr
    return frame(pill_last(fr, t, 'SAME SAVINGS, A DIFFERENT TYPE OF ACCOUNT, A DIFFERENT RESULT', 790, gold, navy, 38))

def s22b(t):
    fr = stage(t, 'YOUR STATE MAY HAVE ITS OWN RULES', 95, 56); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([420, 250, 1500, 640], radius=34, fill=card + (255,), outline=red + (255,), width=6)
        cal_card(C, 480, 310, 780, 590, 'STATE', 'TAX', 100, red)
        txt(C, 'NOT COUNTED HERE:', BOLD(46), 340, grey, 255, x=1150); txt(C, 'STATE INCOME TAX', BOLD(70), 420, white, 255, x=1150); txt(C, 'CHECK YOUR OWN STATE RULES', BOLD(40), 530, goldL, 255, x=1150)
        fr = P2(fr, C, (400, 230, 1520, 660), t, T[0])
    return frame(pill_last(fr, t, 'THESE NUMBERS ARE FEDERAL ONLY', 780, red, (255, 255, 255), 52))

def s22c(t):
    fr = stage(t, 'WHAT LANDS IN THE BANK', 96); T = sp(4)
    fr = eq(fr, t, 230, [('c', 'FROM SAVINGS', '$1,625', 'A MONTH', gold), ('o', '+'), ('c', 'SOCIAL SECURITY', '$1,868.10', 'AFTER PART B', blue), ('o', '='), ('c', 'IN THE BANK', '$3,493.10', 'A MONTH', green)], [T[0], T[1], T[2]], 250, 420, 150)
    if t > T[3]:
        C = new(); building(C, 960, 620, 380, 220, blue); txt(C, 'EVERY MONTH', BOLD(50), 745, white, 255, x=960); fr = P2(fr, C, (740, 480, 1180, 820), t, T[3])
    return frame(fr)

# ============ BLOCCO 23 ============
def s23a(t):
    fr = stage(t, 'THE MONTHLY DEPOSIT', 97); T = sp(3)
    if t > T[0]:
        C = new(); paycheck(C, 500, 250, 1420, 640, green, '$3,493.10', 'A MONTH', 'IN THE BANK', 180); fr = P2(fr, C, (480, 230, 1440, 660), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 560, 680, 1360, 790, gold, None, 'LITTLE OR NO FEDERAL TAX', None, 54, goldL); fr = P2(fr, C, (540, 660, 1380, 810), t, T[1])
    return frame(fr)

def s23b(t):
    fr = stage(t, 'OVER A WHOLE YEAR', 98); T = sp(3)
    fr = eq(fr, t, 280, [('c', 'EVERY MONTH', '$3,493.10', None, green), ('o', '×'), ('c', 'MONTHS', '12', 'IN A YEAR', gold), ('o', '='), ('c', 'EVERY YEAR', '$41,917', 'ABOUT', goldL)], [T[0], T[1], T[2]], 260, 420, 150)
    return frame(pill_last(fr, t, 'ABOUT $41,917 A YEAR', 640, green, navy, 56))

def s23c(t):
    fr = stage(t, 'REMEMBER THAT FIGURE', 99); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 150, 300, 800, 620, green, 'WHAT ARRIVES', '$41,917', 'A YEAR', 140, white); fr = P2(fr, C, (130, 280, 820, 640), t, T[0])
        L = new(); arrow_r(L, 810, 1100, 460, goldL, 255 * E_(t, T[0] + 0.3)); fr = Image.alpha_composite(fr, L)
    if t > T[1]:
        C = new(); card_(C, 1120, 300, 1770, 620, red, 'NOW IT MEETS', 'REALITY', 'THE GAP IS NEXT', 110, white); fr = P2(fr, C, (1100, 280, 1790, 640), t, T[1])
    return frame(pill_last(tracker(fr, t, {4}, 0.3, 965), t, 'NOW IT MEETS REALITY', 800, red, (255, 255, 255), 50))

# ============ BLOCCO 24 ============
def s24a(t):
    fr = stage(t, 'NUMBER FOUR: THE GAP', 101); T = sp(3)
    from v7b2_5 import numcard, ic_time
    fr = numcard(fr, t, T[0], 560, 200, 1360, 770, 4, 'THE GAP', 'BETWEEN INCOME', 'AND WHAT PEOPLE SPEND', ic_time, green) if t > T[0] else fr
    return frame(pill_last(tracker(fr, t, {4}, 0.3, 965), t, 'NUMBER FOUR: THE GAP', 810, green, navy, 52))

def s24b(t):
    fr = stage(t, 'WHAT HOUSEHOLDS OVER 65 SPENT', 102, 56); T = sp(4)
    if t > T[0]:
        C = new(); building(C, 380, 450, 400, 330, blue); txt(C, 'BUREAU OF', BOLD(44), 640, white, 255, x=380); txt(C, 'LABOR STATISTICS', BOLD(44), 690, white, 255, x=380); fr = P2(fr, C, (130, 230, 640, 740), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 760, 270, 1320, 560, gold, 'AGE 65 OR OLDER', 'IN 2024', None, 80, goldL); cal_card(C, 790, 330, 1040, 540, '', '2024', 90, gold) if False else None; fr = P2(fr, C, (740, 250, 1340, 580), t, T[1])
        L = new(); arrow_r(L, 650, 750, 420, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        v = 61432 * ease((t - T[2]) / 0.9)
        C = new(); card_(C, 1400, 270, 1800, 560, red, 'AVERAGE SPENDING', '$' + f'{int(v):,}', 'A YEAR', 80, white); fr = P2(fr, C, (1380, 250, 1820, 580), t, T[2])
        L = new(); arrow_r(L, 1330, 1390, 420, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'AVERAGE: $61,432 A YEAR IN 2024', 800, red, (255, 255, 255), 52))

def s24c(t):
    fr = stage(t, 'WHAT THAT INCLUDES', 103); T = sp(4)
    labs = [('HOUSING', 'h'), ('FOOD', 'c'), ('TRANSPORT', 't'), ('HEALTH CARE', 'm')]
    for k, (lab, ic) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); cx = 330 + k * 420; d.rounded_rectangle([cx - 190, 260, cx + 190, 560], radius=30, fill=card + (255,), outline=goldL + (255,), width=4); cy = 380
            if ic == 'h': house(C, cx, cy - 20, 1.1)
            elif ic == 'c': cart(C, cx + 20, cy, 0.8, 255, green)
            elif ic == 't':
                d.rounded_rectangle([cx - 85, cy - 25, cx + 85, cy + 30], radius=18, fill=A(blue, 255)); d.polygon([(cx - 50, cy - 25), (cx - 30, cy - 62), (cx + 30, cy - 62), (cx + 55, cy - 25)], fill=A(blue, 255))
                d.ellipse([cx - 70, cy + 12, cx - 30, cy + 52], fill=A(navy, 255), outline=A(white, 255), width=5); d.ellipse([cx + 30, cy + 12, cx + 70, cy + 52], fill=A(navy, 255), outline=A(white, 255), width=5)
            else:
                d.rounded_rectangle([cx - 55, cy - 55, cx + 55, cy + 55], radius=14, fill=A((236, 240, 245), 255), outline=A(red, 255), width=5); d.rectangle([cx - 10, cy - 36, cx + 10, cy + 36], fill=A(red, 255)); d.rectangle([cx - 36, cy - 10, cx + 36, cy + 10], fill=A(red, 255))
            txt(C, lab, fit(lab, 350, 44), 490, white, 255, x=cx); fr = P2(fr, C, (cx - 210, 240, cx + 210, 580), t, T[k])
    return frame(pill_last(fr, t, 'HOUSING, FOOD, TRANSPORTATION AND HEALTH CARE', 700, gold, navy, 46))

# ============ BLOCCO 25 ============
def s25a(t):
    fr = stage(t, 'INCOME VS AVERAGE SPENDING', 104); T = sp(4)
    fr = bars3(fr, t, 690, [('FRANK AND MARY', '$44,352', 44352 / 61432, (90, 130, 190), white), ('AVERAGE SPENDING', '$61,432', 1.0, red, white)], [T[0], T[1]], 440, 340, 220)
    if t > T[2]:
        C = new(); card_(C, 1420, 300, 1810, 450, red, 'THE DIFFERENCE', '$17,080', None, 64, white); fr = P2(fr, C, (1400, 280, 1830, 470), t, T[2])
    return frame(pill_last(fr, t, 'DIFFERENCE: $17,080 A YEAR', 800, red, (255, 255, 255), 52))

def s25b(t):
    fr = stage(t, 'THE GAP, MONTH BY MONTH', 105); T = sp(3)
    fr = eq(fr, t, 280, [('c', 'THE GAP', '$17,080', 'A YEAR', red), ('o', '÷'), ('c', 'MONTHS', '12', None, gold), ('o', '='), ('c', 'EVERY MONTH', '$1,423', 'ABOUT', goldL)], [T[0], T[1], T[2]], 260, 420, 150)
    return frame(pill_last(fr, t, 'ABOUT $1,423 EVERY MONTH', 640, red, (255, 255, 255), 54))

def s25c(t):
    fr = stage(t, 'AN AVERAGE HIDES A LOT', 106); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 270, 760, 660], radius=34, fill=card + (255,), outline=green + (255,), width=6)
        house(C, 480, 420, 1.5, gold); txt(C, 'SOME HAVE PAID', BOLD(44), 560, white, 255, x=480); txt(C, 'OFF THEIR HOMES', BOLD(44), 610, green, 255, x=480); fr = P2(fr, C, (180, 250, 780, 680), t, T[0])
    if t > T[1]:
        L = new(); txt(L, 'BUT...', BOLD(80), 420, goldL, 255 * E_(t, T[1]), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1160, 270, 1720, 660, red, 'OTHERS', 'SPEND MORE', 'AVERAGES HIDE A LOT', 80, white); fr = P2(fr, C, (1140, 250, 1740, 680), t, T[1])
    return frame(pill_last(fr, t, 'AN AVERAGE HIDES A LOT', 780, gold, navy, 52))

# ============ BLOCCO 26 ============
def s26a(t):
    fr = stage(t, 'EVERYONE IS DIFFERENT', 107); T = sp(4)
    items = [('A PENSION', 'EXTRA INCOME', gold), ("A SPOUSE'S INCOME", 'MORE COMING IN', blue), ('LOWER COSTS', 'SPEND LESS', green), ('SPEND MORE', 'COSTS ARE HIGHER', red)]
    for k, (a, b2, col) in enumerate(items):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 150 + k * 430; d.rounded_rectangle([x0, 280, x0 + 380, 620], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            avatar(C, x0 + 190, 390, col, 2.0); txt(C, a, fit(a, 350, 40), 510, white, 255, x=x0 + 190); txt(C, b2, fit(b2, 350, 32), 565, col, 255, x=x0 + 190)
            fr = P2(fr, C, (x0 - 20, 260, x0 + 400, 640), t, T[k])
    return frame(pill_last(fr, t, 'SOME HAVE PENSIONS OR LOWER COSTS. OTHERS SPEND FAR MORE.', 760, gold, navy, 40))

def s26b(t):
    fr = stage(t, 'THE POINT', 108); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 250, 280, 960, 620, red, 'IT IS NOT THAT', '$500,000 FAILS', None, 70, white); cross(C, 600, 560, 40, red); fr = P2(fr, C, (230, 260, 980, 640), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 1000, 280, 1700, 620, gold, 'IT COVERS A', 'SMALLER LIFESTYLE', 'THAN MANY EXPECT', 70, goldL); fr = P2(fr, C, (980, 260, 1720, 640), t, T[1])
    return frame(pill_last(fr, t, 'A SMALLER LIFESTYLE THAN MANY PEOPLE EXPECT', 760, gold, navy, 46))

def s26c(t):
    fr = stage(t, 'WRITE DOWN YOUR OWN EXPENSES', 109, 56); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([560, 240, 1360, 740], radius=26, fill=(250, 244, 220, 255), outline=goldL + (255,), width=6)
        txt(C, 'MY MONTHLY EXPENSES', BOLD(46), 270, (60, 50, 30), 255, x=960)
        for k, lab in enumerate(['HOUSING', 'FOOD', 'TRANSPORT', 'HEALTH CARE']):
            y = 360 + k * 85; d.line([620, y + 62, 1300, y + 62], fill=(180, 170, 140, 255), width=3); txt(C, lab, BOLD(38), y, (60, 50, 30), 255, x=630, anchor='l'); txt(C, '$ ____', BOLD(38), y, (60, 50, 30), 255, x=1290, anchor='r')
        fr = P2(fr, C, (540, 220, 1380, 760), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.line([1480, 380, 1620, 240], fill=A(goldL, 255), width=26); d.polygon([(1470, 392), (1500, 410), (1450, 440)], fill=A(white, 255)); fr = P2(fr, C, (1430, 220, 1660, 460), t, T[1])
    return frame(pill_last(fr, t, 'THE ONLY WAY TO KNOW YOURS: WRITE IT DOWN', 790, gold, navy, 46))

# ============ BLOCCO 27 ============
def s27a(t):
    fr = stage(t, 'THE SECOND PART OF NUMBER FOUR: TIME', 111, 54); T = sp(3)
    if t > T[0]:
        C = new(); clock(C, 960, 470, 190, t * 1.3, goldL); fr = P2(fr, C, (740, 250, 1180, 700), t, T[0])
    return frame(pill_last(tracker(fr, t, {4}, 0.3, 965), t, 'TIME: HOW LONG DOES THE MONEY HAVE TO LAST?', 800, gold, navy, 46))

def s27b(t):
    fr = stage(t, 'HOW LONG DOES A 65-YEAR-OLD LIVE?', 112, 56); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([140, 260, 900, 650], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        avatar(C, 290, 395, blue, 2.0); txt(C, 'A MAN', BOLD(46), 520, blue, 255, x=290); txt(C, 'AGE 65 TODAY', BOLD(30), 585, grey, 255, x=290)
        txt(C, '50% CHANCE', BOLD(40), 330, white, 255, x=650); txt(C, 'OF REACHING', BOLD(40), 380, white, 255, x=650); txt(C, '84', BOLD(150), 430, goldL, 255, x=650)
        fr = P2(fr, C, (120, 240, 920, 670), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1020, 260, 1780, 650], radius=34, fill=card + (255,), outline=pink + (255,), width=6)
        avatar(C, 1170, 395, pink, 2.0); txt(C, 'A WOMAN', BOLD(46), 520, pink, 255, x=1170); txt(C, 'AGE 65 TODAY', BOLD(30), 585, grey, 255, x=1170)
        txt(C, '50% CHANCE', BOLD(40), 330, white, 255, x=1530); txt(C, 'OF REACHING', BOLD(40), 380, white, 255, x=1530); txt(C, '87', BOLD(150), 430, goldL, 255, x=1530)
        fr = P2(fr, C, (1000, 240, 1800, 670), t, T[1])
    fr = chip_src(fr, 'SOURCE: SOCIAL SECURITY ADMINISTRATION', 700, t, T[2]) if t > T[2] else fr
    return frame(pill_last(fr, t, 'A 50% CHANCE OF REACHING 84 (MEN) AND 87 (WOMEN)', 790, gold, navy, 44))

def s27c(t):
    fr = stage(t, 'ABOUT ONE IN FOUR WILL LIVE PAST NINETY', 113, 54); T = sp(5)
    C = new()
    for k in range(4):
        u = back((t - T[0] - 0.25 * k) / 0.35)
        if u <= 0: continue
        hl = (k == 3 and t > T[3])
        avatar(C, 420 + k * 360, 440, goldL if hl else (110, 128, 156), 2.6 * min(1, u))
    fr = Image.alpha_composite(fr, C)
    if t > T[3]:
        C = new(); txt(C, '90+', BOLD(80), 190, goldL, 255, x=1500); fr = P2(fr, C, (1380, 160, 1620, 290), t, T[3])
    if t > T[2]:
        v = 25 * ease((t - T[2]) / 0.8)
        C = new(); card_(C, 560, 640, 1360, 770, gold, None, '1 IN 4  =  ' + str(int(v)) + '%', None, 70, goldL); fr = P2(fr, C, (540, 620, 1380, 790), t, T[2])
    return frame(fr)

# ============ BLOCCO 28 ============
def s28a(t):
    fr = stage(t, 'HOW LONG MUST IT WORK?', 114); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 300, 1720, 420], radius=40, fill=(60, 80, 110, 255)); d.rounded_rectangle([200, 300, 200 + 1520 * 0.33 * ease((t - T[0]) / 0.5), 420], radius=40, fill=red + (255,))
        d.rounded_rectangle([200, 300, 200 + 1520 * ease((t - T[0] - 0.4) / 1.0), 420], radius=40, fill=gold + (255,)) if t > T[0] + 0.4 else None
        txt(C, 'YEAR 1', BOLD(40), 440, white, 255, x=200, anchor='l'); txt(C, 'YEAR 25-30', BOLD(40), 440, goldL, 255, x=1720, anchor='r'); fr = P2(fr, C, (180, 280, 1740, 500), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 400, 560, 960, 740, red, 'NOT TEN YEARS', '10', None, 80, white); fr = P2(fr, C, (380, 540, 980, 760), t, T[1])
        C = new(); card_(C, 980, 560, 1540, 740, gold, 'BUT 25 TO 30 YEARS', '25-30', None, 80, goldL); fr = P2(fr, C, (960, 540, 1560, 760), t, T[1] + 0.2)
    return frame(fr)

def s28b(t):
    fr = stage(t, 'AND PRICES DO NOT STAND STILL', 115); T = sp(3)
    if t > T[0]:
        C = new(); cart(C, 480, 480, 1.7, 255, gold); txt(C, 'PRICES', BOLD(54), 640, white, 255, x=480); fr = P2(fr, C, (240, 300, 740, 720), t, T[0])
        L = new(); arrow_r(L, 760, 900, 480, goldL, 255 * E_(t, T[0] + 0.1)); fr = Image.alpha_composite(fr, L)
    if t > T[1]:
        C = new(); card_(C, 920, 300, 1620, 640, red, 'EXAMPLE ONLY', '+3%', 'A YEAR', 200, white); fr = P2(fr, C, (900, 280, 1640, 660), t, T[1])
    return frame(pill_last(fr, t, 'EXAMPLE: PRICES RISE 3% A YEAR', 780, red, (255, 255, 255), 52))

def s28c(t):
    fr = stage(t, 'AFTER TWENTY YEARS', 116); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C)
        for k in range(21):
            h = 360 * (1.03 ** k) / 1.806
            d.rounded_rectangle([260 + k * 70, 650 - h * ease((t - T[0] - 0.03 * k) / 0.5), 260 + k * 70 + 56, 650], radius=8, fill=(gold if k == 20 else (90, 130, 190)) + (255,))
        txt(C, 'TODAY', BOLD(34), 670, grey, 255, x=288); txt(C, '20 YEARS', BOLD(34), 670, goldL, 255, x=1640); fr = P2(fr, C, (220, 240, 1760, 720), t, T[0])
    if t > T[2]:
        v = 81 * ease((t - T[2]) / 0.7)
        C = new(); card_(C, 300, 215, 900, 365, red, 'PRICES ARE ABOUT', '+' + str(int(v)) + '% HIGHER', None, 66, white); fr = P2(fr, C, (280, 195, 920, 385), t, T[2])
    return frame(pill_last(fr, t, 'AFTER 20 YEARS PRICES ARE ABOUT 81% HIGHER', 800, red, (255, 255, 255), 44))

# ============ BLOCCO 29 ============
def s29a(t):
    fr = stage(t, 'A LIFESTYLE THAT COSTS $3,500 TODAY', 117, 56); T = sp(4)
    if t > T[0]:
        C = new(); paycheck(C, 150, 280, 790, 640, blue, '$3,500', 'PER MONTH', 'TODAY', 150); fr = P2(fr, C, (130, 260, 810, 660), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 810, 1110, 460, goldL, 255 * E_(t, T[1])); txt(L, 'IN 20 YEARS', BOLD(40), 380, goldL, 255 * E_(t, T[1]), x=960); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); paycheck(C, 1130, 280, 1770, 640, red, '$6,300', 'PER MONTH', 'IN 20 YEARS', 150); fr = P2(fr, C, (1110, 260, 1790, 660), t, T[2])
    return frame(pill_last(fr, t, 'ABOUT $6,300 A MONTH IN TWENTY YEARS', 790, red, (255, 255, 255), 48))

def s29b(t):
    fr = stage(t, 'SOCIAL SECURITY HELPS WITH PART OF IT', 118, 54); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 150, 290, 880, 610, blue, 'SOCIAL SECURITY', 'YEARLY RAISE', 'HELPS WITH PART OF IT', 80, white); up_arrow(C, 810, 540, 0.6, green); fr = P2(fr, C, (130, 270, 900, 630), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 1040, 290, 1770, 610, gold, 'THE WITHDRAWALS', 'FROM SAVINGS', 'HAVE TO KEEP UP TOO', 80, goldL); up_arrow(C, 1700, 540, 0.6, green); fr = P2(fr, C, (1020, 270, 1790, 630), t, T[1])
    return frame(pill_last(fr, t, 'THE WITHDRAWALS HAVE TO KEEP UP TOO', 760, gold, navy, 48))

def s29c(t):
    fr = stage(t, 'THE RISK THAT SURPRISES MOST PEOPLE', 119, 56); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 270, 1720, 680], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        pts = [(0.03, 0.55), (0.18, 0.40), (0.30, 0.62), (0.42, 0.30), (0.55, 0.45), (0.68, 0.25), (0.82, 0.38), (0.97, 0.15)]
        line_chart(C, 260, 300, 1660, 640, pts, green, ease((t - T[0]) / 1.2)); txt(C, 'THE MARKET, YEAR BY YEAR', BOLD(40), 280, white, 255, x=960)
        fr = P2(fr, C, (180, 250, 1740, 700), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([250, 320, 620, 660], radius=30, outline=red + (255,), width=8); txt(C, 'THE FIRST YEARS', BOLD(36), 700, red, 255, x=435); fr = P2(fr, C, (230, 300, 640, 750), t, T[1])
    return frame(pill_last(fr, t, 'THE ORDER OF RETURNS', 800, red, (255, 255, 255), 56))

# ============ BLOCCO 30 ============
def s30a(t):
    fr = stage(t, 'THE MARKET FALLS 20% IN YEAR ONE', 120, 56); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 270, 1100, 700], radius=34, fill=card + (255,), outline=red + (255,), width=6)
        line_chart(C, 260, 310, 1040, 660, [(0.0, 0.2), (0.35, 0.25), (0.6, 0.8), (1.0, 0.95)], red, ease((t - T[0]) / 1.0), 14); txt(C, 'YEAR ONE', BOLD(40), 290, white, 255, x=650)
        fr = P2(fr, C, (180, 250, 1120, 720), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 1200, 330, 1720, 600, red, 'THE MARKET', '-20%', 'IN THE FIRST YEAR', 160, white); fr = P2(fr, C, (1180, 310, 1740, 620), t, T[1])
    return frame(pill_last(fr, t, 'SUPPOSE THE MARKET FALLS 20% IN THE FIRST YEAR', 790, red, (255, 255, 255), 44))

def s30b(t):
    fr = stage(t, 'FRANK WITHDRAWS FIRST', 121); T = sp(3)
    fr = eq(fr, t, 280, [('c', 'SAVINGS', '$500,000', 'AT THE START', gold), ('o', '−'), ('c', 'WITHDRAWAL', '$19,500', 'YEAR ONE', red), ('o', '='), ('c', 'LEFT', '$480,500', None, green)], [T[0], T[1], T[2]], 260, 420, 150)
    return frame(pill_last(fr, t, 'HE WITHDRAWS $19,500 AND $480,500 IS LEFT', 640, gold, navy, 46))

def s30c(t):
    fr = stage(t, 'THEN THE 20% DROP', 122); T = sp(4)
    fr = bars3(fr, t, 700, [('AFTER HIS WITHDRAWAL', '$480,500', 480500 / 500000.0, (90, 130, 190), white), ('AFTER THE 20% DROP', '$384,400', 384400 / 500000.0, red, white)], [T[0], T[1]], 440, 340, 220)
    if t > T[2]:
        L = new(); arrow_r(L, 880, 1050, 470, red, 255 * E_(t, T[2])); txt(L, '-20%', BOLD(80), 360, red, 255 * E_(t, T[2]), x=965); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'AFTER A 20% DROP: $384,400', 810, red, (255, 255, 255), 50))

SLIDES = {21: [s21a, s21b, s21c], 22: [s22a, s22b, s22c], 23: [s23a, s23b, s23c], 24: [s24a, s24b, s24c], 25: [s25a, s25b, s25c],
          26: [s26a, s26b, s26c], 27: [s27a, s27b, s27c], 28: [s28a, s28b, s28c], 29: [s29a, s29b, s29c], 30: [s30a, s30b, s30c]}

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
