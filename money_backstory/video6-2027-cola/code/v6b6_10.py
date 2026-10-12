from v3lib import *
from v3b3_10 import POP, new, lerp
from v4b11_20 import calculator
from v4b2_10 import cal_card
from v5b1 import amb
from v5lib import paycheck, arrow_r, arrow_d, magnifier
from v6b1 import A_, E_, chip_src
from v6b2 import chip
from v6b3 import badge
from v6b45 import Blk, head, months
import sys, math

def P(fr, text, y, t, t0, col=goldL, tcol=navy, size=50, cx=960): return pill_pop(fr, text, y, t, t0, col, tcol=tcol, size=size, cx=cx)
def base_(t, seed, title, size=62):
    fr = base(t); fr = amb(fr, t, seed, 6, 50); return head(fr, title, t, size)
def card_(C, x0, y0, x1, y1, col, fill=card): card_box(C, x0, y0, x1, y1, outline=col, fill=fill)
def house(C, cx, cy, s=1.0, col=goldL):
    d = ImageDraw.Draw(C); d.polygon([(cx - 90 * s, cy - 10 * s), (cx, cy - 90 * s), (cx + 90 * s, cy - 10 * s)], fill=A(red, 255)); d.rectangle([cx - 66 * s, cy - 10 * s, cx + 66 * s, cy + 70 * s], fill=A(col, 255)); d.rectangle([cx - 16 * s, cy + 20 * s, cx + 16 * s, cy + 70 * s], fill=A(navy, 255))
def car(C, cx, cy, s=1.0, col=blue):
    d = ImageDraw.Draw(C); d.rounded_rectangle([cx - 100 * s, cy - 10 * s, cx + 100 * s, cy + 50 * s], radius=int(20 * s), fill=A(col, 255)); d.polygon([(cx - 60 * s, cy - 10 * s), (cx - 35 * s, cy - 55 * s), (cx + 35 * s, cy - 55 * s), (cx + 65 * s, cy - 10 * s)], fill=A(col, 255))
    for x in (-55, 55): d.ellipse([cx + (x - 22) * s, cy + 30 * s, cx + (x + 22) * s, cy + 74 * s], fill=A(navy, 255), outline=A(goldL, 255), width=4)
def medcross(C, cx, cy, s=1.0):
    d = ImageDraw.Draw(C); d.rounded_rectangle([cx - 60 * s, cy - 60 * s, cx + 60 * s, cy + 60 * s], radius=int(16 * s), fill=(236, 240, 245, 255)); d.rectangle([cx - 12 * s, cy - 40 * s, cx + 12 * s, cy + 40 * s], fill=A(red, 255)); d.rectangle([cx - 40 * s, cy - 12 * s, cx + 40 * s, cy + 12 * s], fill=A(red, 255))
def worker(C, cx, cy, col, s=1.0):
    avatar(C, cx, cy, col, s); d = ImageDraw.Draw(C); d.rounded_rectangle([cx + 28 * s, cy + 18 * s, cx + 78 * s, cy + 52 * s], radius=6, fill=A((150, 100, 50), 255), outline=A(goldL, 255), width=3)

class Blk2(Blk):
    def tt(s, g, marker): return max(0.15, 0.55 * Blk.tt(s, g, marker))

# ============ BLOCCO 6 (702) ============
B6 = Blk2(["Let's check last year's raise.",
          "The average for the summer of twenty twenty five was three hundred seventeen point two six five.",
          "The summer before, it was three hundred eight point seven two nine.",
          "The difference is about two point eight percent, and that is exactly the raise retirees received in January of twenty twenty six.",
          "No guessing, no opinions, just two averages and a division."],
         [[0, 1], [2], [3], [4]], 702)
def sumcard(C, x0, x1, yr, val, col):
    card_(C, x0, 270, x1, 760, col); cx = (x0 + x1) / 2
    txt(C, 'SUMMER ' + yr, BOLD(62), 300, col, 255, x=cx)
    for k, m in enumerate(['JUL', 'AUG', 'SEP']):
        xx = cx - 190 + k * 135; ImageDraw.Draw(C).rounded_rectangle([xx, 400, xx + 115, 480], radius=14, fill=A(col, 255)); txt(C, m, BOLD(44), 415, navy, 255, x=xx + 58)
    txt(C, val, BOLD(124), 520, white, 255, x=cx); txt(C, 'CPI-W AVERAGE', BOLD(46), 670, grey, 255, x=cx)
def s6a(t):
    fr = base_(t, 41, "LAST YEAR'S RAISE"); T = lambda m: B6.tt(0, m)
    if t > 0.3:
        C = new(); magnifier(C, 1320, 420, 120); txt(C, 'LET US CHECK IT', BOLD(60), 640, goldL, 255, x=1420)
        fr = A_(fr, C, (1000, 230, 1800, 760), t, 0.3)
    t1 = T('The average')
    if t > t1:
        C = new(); sumcard(C, 130, 850, '2025', '317.265', gold); fr = A_(fr, C, (110, 250, 870, 780), t, t1)
    fr = P(fr, 'WE CHECK THE 2026 RAISE', 850, t, 0.9, goldL, navy, 50)
    return frame(fr)
def s6b(t):
    fr = base_(t, 42, 'TWO SUMMERS, TWO AVERAGES'); T = lambda m: B6.tt(1, m)
    C = new(); sumcard(C, 130, 850, '2025', '317.265', gold); fr = Image.alpha_composite(fr, C)
    t1 = 0.4
    if t > t1:
        C = new(); sumcard(C, 1070, 1790, '2024', '308.729', blue); fr = A_(fr, C, (1050, 250, 1810, 780), t, t1)
        L = new(); txt(L, 'VS', BOLD(84), 480, goldL, 255 * E_(t, t1 + 0.2), x=960); fr = Image.alpha_composite(fr, L)
    fr = P(fr, 'TWO AVERAGES TO COMPARE', 850, t, 0.9, goldL, navy, 50)
    return frame(fr)
def s6c(t):
    fr = base_(t, 43, 'THE DIVISION'); T = lambda m: B6.tt(2, m)
    t1 = 0.3
    if t > t1:
        C = new(); txt(C, '317.265 - 308.729 = 8.536', BOLD(90), 270, white, 255, x=960); fr = A_(fr, C, (140, 250, 1780, 400), t, t1)
        t2 = t1 + 1.2
        if t > t2:
            C = new(); txt(C, '8.536 / 308.729 = 2.8%', BOLD(90), 410, goldL, 255, x=960); fr = A_(fr, C, (140, 390, 1780, 540), t, t2)
    t3 = T('is about two point eight')
    if t > t3:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([260, 580, 560, 880], fill=gold + (255,), outline=goldL + (255,), width=8)
        txt(C, '2.8%', BOLD(120), 690, navy, 255, x=410); txt(C, 'RAISE', BOLD(50), 810, navy, 255, x=410)
        fr = A_(fr, C, (240, 560, 580, 900), t, t3)
    t4 = T('received in January')
    if t > t4:
        L = new(); arrow_r(L, 620, 800, 730, goldL, 255 * E_(t, t4)); fr = Image.alpha_composite(fr, L)
        C = new(); cal_card(C, 840, 580, 1280, 900, 'JANUARY', '2026', bigsize=120, headcol=gold); fr = A_(fr, C, (820, 560, 1300, 920), t, t4)
        fr = P(fr, 'EXACTLY THE RAISE RETIREES GOT', 700, t, t4 + 0.3, green, navy, 40, 1560) if False else fr
        C = new(); txt(C, 'RETIREES', BOLD(52), 640, white, 255, x=1560); txt(C, 'GOT EXACTLY', BOLD(52), 710, white, 255, x=1560); txt(C, 'THIS RAISE', BOLD(52), 780, green, 255, x=1560); fr = A_(fr, C, (1340, 620, 1800, 860), t, t4 + 0.3)
    return frame(fr)
def s6d(t):
    fr = base_(t, 44, 'JUST MATH'); T = lambda m: B6.tt(3, m)
    items = [('No guessing', 'NO GUESSING', red, 'x'), ('no opinions', 'NO OPINIONS', red, 'x'), ('just two', 'TWO AVERAGES', green, 'c')]
    for k, (m, lab, col, kind) in enumerate(items):
        t0 = max(0.3, T(m) - 0.1)
        if t < t0: continue
        cx = 360 + k * 600; C = new(); card_(C, cx - 270, 300, cx + 270, 720, col)
        (cross if kind == 'x' else check)(C, cx, 450, 90, col)
        txt(C, lab, BOLD(56), 580, white, 255, x=cx)
        if k == 2: txt(C, '+ A DIVISION', BOLD(52), 650, goldL, 255, x=cx)
        fr = A_(fr, C, (cx - 290, 280, cx + 290, 740), t, t0)
    fr = P(fr, 'NO GUESSING. JUST MATH.', 820, t, 0.9, goldL, navy, 50)
    return frame(fr)

# ============ BLOCCO 7 (789) ============
B7 = Blk2(["And this year?",
          "On October fourteenth, the Bureau of Labor Statistics releases the September prices, and the Social Security Administration announces the result the same morning.",
          "Private estimates from The Senior Citizens League and from AARP sit between three point five and three point six percent.",
          "Remember, those are estimates, not the official number.",
          "In this video, we will use three point five percent, so you can follow the math."],
         [[0, 1], [2], [3], [4]], 789)
def s7a(t):
    fr = base_(t, 51, 'ANNOUNCEMENT DAY'); T = lambda m: B7.tt(0, m)
    t1 = T('On October')
    if t > t1:
        C = new(); cal_card(C, 120, 300, 560, 700, 'OCTOBER', '14', bigsize=200, headcol=red); fr = A_(fr, C, (100, 280, 580, 720), t, t1)
    t2 = T('Bureau of Labor')
    if t > t2:
        L = new(); arrow_r(L, 590, 690, 500, goldL, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
        C = new(); building(C, 940, 430, 240, 200, gold); txt(C, 'BLS RELEASES', BOLD(48), 580, white, 255, x=940); txt(C, 'SEPTEMBER PRICES', BOLD(48), 640, goldL, 255, x=940)
        fr = A_(fr, C, (700, 280, 1200, 700), t, t2)
    t3 = T('Social Security Administration')
    if t > t3:
        L = new(); arrow_r(L, 1230, 1320, 500, goldL, 255 * E_(t, t3)); fr = Image.alpha_composite(fr, L)
        C = new(); building(C, 1560, 430, 240, 200, blue); txt(C, 'SSA ANNOUNCES', BOLD(48), 580, white, 255, x=1560); txt(C, 'THE RESULT', BOLD(48), 640, blue, 255, x=1560)
        fr = A_(fr, C, (1330, 280, 1820, 700), t, t3)
    t4 = T('the same morning')
    if t > t4: fr = P(fr, 'THE SAME MORNING', 790, t, t4, goldL, navy, 54)
    return frame(fr)
def s7b(t):
    fr = base_(t, 52, 'PRIVATE ESTIMATES'); T = lambda m: B7.tt(1, m)
    t1 = T('Senior Citizens')
    if t > t1 - 0.1:
        C = new(); card_(C, 130, 280, 880, 700, gold); txt(C, 'THE SENIOR', BOLD(54), 310, white, 255, x=505); txt(C, 'CITIZENS LEAGUE', BOLD(54), 372, white, 255, x=505); txt(C, '3.5%', BOLD(170), 470, goldL, 255, x=505)
        fr = A_(fr, C, (110, 260, 900, 720), t, t1 - 0.1)
    t2 = T('AARP')
    if t > t2 - 0.1:
        C = new(); card_(C, 1040, 280, 1790, 700, blue); txt(C, 'AARP', BOLD(70), 340, white, 255, x=1415); txt(C, '3.6%', BOLD(170), 470, blue, 255, x=1415)
        fr = A_(fr, C, (1020, 260, 1810, 720), t, t2 - 0.1)
    t3 = T('between')
    if t > t3:
        fr = P(fr, 'BETWEEN 3.5% AND 3.6%', 800, t, t3, goldL, navy, 56)
    return frame(fr)
def s7c(t):
    fr = base_(t, 53, 'ESTIMATE OR OFFICIAL?'); T = lambda m: B7.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 900, 730, gold); txt(C, 'ESTIMATES', BOLD(70), 330, goldL, 255, x=520); txt(C, '3.5%  -  3.6%', BOLD(100), 470, white, 255, x=520); txt(C, 'FROM PRIVATE GROUPS', BOLD(44), 620, grey, 255, x=520)
        fr = A_(fr, C, (120, 270, 920, 750), t, 0.3)
    t2 = T('not the official')
    if t > t2:
        C = new(); card_(C, 1020, 290, 1780, 730, red); txt(C, 'OFFICIAL NUMBER', BOLD(60), 330, white, 255, x=1400); txt(C, '?', BOLD(210), 380, red, 255, x=1400); txt(C, 'OCTOBER 14', BOLD(44), 690, grey, 255, x=1400)
        fr = A_(fr, C, (1000, 270, 1800, 750), t, t2)
        fr = stamp(fr, 'NOT YET', 1400, 640, -10, red, back((t - t2 - 0.4) / 0.4), 56)
    fr = P(fr, 'ESTIMATE, NOT OFFICIAL', 830, t, 0.9, red, (255, 255, 255), 50)
    return frame(fr)
def s7d(t):
    fr = base_(t, 54, 'OUR EXAMPLE'); T = lambda m: B7.tt(3, m)
    if t > 0.3:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([260, 300, 660, 700], fill=gold + (255,), outline=goldL + (255,), width=10); txt(C, '3.5%', BOLD(150), 400, navy, 255, x=460); txt(C, 'USED HERE', BOLD(52), 560, navy, 255, x=460)
        fr = A_(fr, C, (240, 280, 680, 720), t, 0.3)
    t2 = T('follow the math')
    if t > t2 - 0.5:
        L = new(); arrow_r(L, 720, 880, 500, goldL, 255 * E_(t, t2 - 0.5)); fr = Image.alpha_composite(fr, L)
        C = new(); calculator(C, 1100, 500, 1.6); fr = A_(fr, C, (880, 280, 1330, 760), t, t2 - 0.5)
        C = new(); txt(C, 'FOLLOW', BOLD(64), 420, white, 255, x=1560); txt(C, 'THE MATH', BOLD(64), 500, goldL, 255, x=1560); fr = A_(fr, C, (1340, 380, 1800, 600), t, t2 - 0.3)
    fr = P(fr, 'WE USE 3.5% IN THIS VIDEO', 830, t, 0.9, goldL, navy, 50)
    return frame(fr)

# ============ BLOCCO 8 (876) ============
B8 = Blk2(["To see the pattern, look at the last four raises.", "Twenty twenty three, eight point seven percent.", "Twenty twenty four, three point two.",
          "Twenty twenty five, two point five.", "Twenty twenty six, two point eight.",
          "And in three different years, twenty ten, twenty eleven and twenty sixteen, the raise was zero.",
          "A big raise is not always good news, because the formula is simply following prices, and a big raise means prices rose a lot."],
         [[0, 1, 2], [3, 4], [5], [6]], 876)
BARS = [('2023', 8.7), ('2024', 3.2), ('2025', 2.5), ('2026', 2.8)]
def bars_(fr, t, shown, starts):
    C0 = new(); ImageDraw.Draw(C0).line([180, 790, 1740, 790], fill=goldL + (200,), width=5); txt(C0, 'RAISE EACH YEAR (COLA)', BOLD(50), 250, white, 255 * E_(t, 0.3), x=960); fr = Image.alpha_composite(fr, C0)
    for k, (yr, v) in enumerate(BARS):
        st = starts.get(k)
        if st is None: continue
        if t < st: continue
        u = ease((t - st) / 0.8) if st > 0.35 else 1.0
        h_ = max(6, 40 * v * u); cx = 380 + k * 400
        C = new(); C.alpha_composite(bar(h_, red if k == 0 else gold, 220), (int(cx - 110), int(790 - h_)))
        txt(C, f'{v}%', BOLD(76), 790 - h_ - 95, white, 255 * min(1, u * 2), x=cx); txt(C, yr, BOLD(60), 810, goldL, 255, x=cx)
        fr = Image.alpha_composite(fr, C)
    return fr
def s8a(t):
    fr = base_(t, 61, 'THE LAST FOUR RAISES'); T = lambda m: B8.tt(0, m)
    fr = bars_(fr, t, 2, {0: T('Twenty twenty three') - 0.1, 1: T('Twenty twenty four') - 0.1})
    return frame(fr)
def s8b(t):
    fr = base_(t, 62, 'THE LAST FOUR RAISES'); T = lambda m: B8.tt(1, m)
    fr = bars_(fr, t, 4, {0: 0.0, 1: 0.0, 2: T('Twenty twenty five') - 0.1, 3: T('Twenty twenty six') - 0.1})
    return frame(fr)
def s8c(t):
    fr = base_(t, 63, 'THREE YEARS WITH NO RAISE'); T = lambda m: B8.tt(2, m)
    for k, (yr, m) in enumerate([('2010', 'twenty ten'), ('2011', 'twenty eleven'), ('2016', 'twenty sixteen')]):
        t0 = max(0.3, T(m) - 0.1)
        if t < t0: continue
        cx = 360 + k * 600; C = new(); card_(C, cx - 250, 300, cx + 250, 700, goldL)
        txt(C, yr, BOLD(90), 330, goldL, 255, x=cx); txt(C, '0.0%', BOLD(130), 450, white, 255, x=cx)
        ImageDraw.Draw(C).line([cx - 150, 640, cx + 150, 640], fill=red + (255,), width=10)
        fr = A_(fr, C, (cx - 270, 280, cx + 270, 720), t, t0)
    if t > T('the raise was zero') - 0.2: fr = P(fr, 'THE RAISE WAS ZERO', 800, t, T('the raise was zero') - 0.2, red, (255, 255, 255), 56)
    return frame(fr)
def s8d(t):
    fr = base_(t, 64, 'BIG RAISE = BIG PRICE JUMP'); T = lambda m: B8.tt(3, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 880, 730, red); cart(C, 420, 520, 1.6, 255, gold); up_arrow(C, 700, 520, 1.1, red); txt(C, 'PRICES ROSE A LOT', BOLD(56), 330, white, 255, x=510)
        fr = A_(fr, C, (120, 270, 900, 750), t, 0.3)
    t2 = T('a big raise means')
    if t > t2 - 1.0:
        L = new(); arrow_r(L, 920, 1030, 510, goldL, 255 * E_(t, t2 - 1.0)); fr = Image.alpha_composite(fr, L)
        C = new(); d = ImageDraw.Draw(C); d.ellipse([1070, 330, 1470, 730], fill=gold + (255,), outline=goldL + (255,), width=10); txt(C, '%', BOLD(220), 390, navy, 255, x=1270); txt(C, 'BIG RAISE', BOLD(54), 610, navy, 255, x=1270)
        fr = A_(fr, C, (1050, 310, 1490, 750), t, t2 - 1.0)
    t3 = T('not always good news')
    if t > t3: fr = chip(fr, 'NOT ALWAYS GOOD NEWS', 1640, 460, t, t3, red, 46, fillc=red, tcol=(255, 255, 255)) if False else P(fr, 'NOT ALWAYS GOOD NEWS', 820, t, t3, red, (255, 255, 255), 54)
    return frame(fr)

# ============ BLOCCO 9 (674) ============
B9 = Blk2(["Number two: why the raise can feel smaller than your bills.",
          "The formula tracks the prices paid by urban wage earners, people who are still on the job.",
          "Retirees spend their money differently.", "They usually spend more on healthcare and housing, and less on commuting.",
          "So the formula and your own budget do not always move together."],
         [[0], [1], [2, 3], [4]], 674)
def s9a(t):
    fr = base_(t, 71, 'NUMBER TWO'); T = lambda m: B9.tt(0, m)
    if t > 0.3:
        C = new(); badge(C, 240, 330, 2, gold, 70); txt(C, 'WHY THE RAISE FEELS', BOLD(70), 290, white, 255, x=1060); txt(C, 'SMALLER THAN YOUR BILLS', BOLD(70), 370, goldL, 255, x=1060)
        fr = A_(fr, C, (140, 240, 1800, 460), t, 0.3)
    t2 = T('smaller')
    if t > t2:
        C = new(); card_(C, 200, 520, 780, 860, green); bill(C, 490, 640, 230, 112, 0, 255); txt(C, '+ THE RAISE', BOLD(56), 740, green, 255, x=490); fr = A_(fr, C, (180, 500, 800, 880), t, t2)
        C = new(); card_(C, 1100, 520, 1760, 860, red); wallet(C, 1430, 630, 1.0); txt(C, 'BILLS KEEP GROWING', BOLD(44), 740, red, 255, x=1430); fr = A_(fr, C, (1120, 500, 1740, 880), t, t2 + 0.3)
    return frame(fr)
def s9b(t):
    fr = base_(t, 72, 'WHO THE FORMULA TRACKS'); T = lambda m: B9.tt(1, m)
    t1 = T('urban wage earners')
    if t > 0.3:
        C = new(); card_(C, 140, 290, 900, 740, blue); [worker(C, 270 + k * 235, 560, [blue, pink, gold][k], 1.9) for k in range(3)]; txt(C, 'URBAN WAGE EARNERS', BOLD(54), 320, white, 255, x=520)
        fr = A_(fr, C, (120, 270, 920, 760), t, 0.3)
    t2 = T('still on the job')
    if t > t2 - 0.3:
        L = new(); arrow_r(L, 930, 1030, 520, goldL, 255 * E_(t, t2 - 0.3)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1050, 290, 1790, 740, gold); briefcase(C, 1420, 470, 1.8); txt(C, 'STILL ON', BOLD(70), 590, white, 255, x=1420); txt(C, 'THE JOB', BOLD(70), 665, goldL, 255, x=1420)
        fr = A_(fr, C, (1030, 270, 1810, 760), t, t2 - 0.3)
    fr = P(fr, 'THE FORMULA TRACKS WORKERS', 830, t, 0.9, goldL, navy, 50)
    return frame(fr)
def s9c(t):
    fr = base_(t, 73, 'RETIREES SPEND DIFFERENTLY'); T = lambda m: B9.tt(2, m)
    cols = [('healthcare', 'HEALTHCARE', 'up', red, medcross), ('housing', 'HOUSING', 'up', red, house), ('commuting', 'COMMUTING', 'down', green, car)]
    for k, (m, lab, dr, col, icon) in enumerate(cols):
        t0 = max(0.3, T(m) - 0.2)
        if t < t0: continue
        cx = 360 + k * 600; C = new(); card_(C, cx - 260, 290, cx + 260, 740, col)
        icon(C, cx, 450, 1.6) if icon is not car else car(C, cx, 450, 1.5)
        txt(C, lab, BOLD(56), 590, white, 255, x=cx)
        (up_arrow(C, cx + 190, 380, 0.6, col) if dr == 'up' else arrow_d(C, cx + 190, 320, 460, col))
        txt(C, 'MORE' if dr == 'up' else 'LESS', BOLD(54), 660, col, 255, x=cx)
        fr = A_(fr, C, (cx - 280, 270, cx + 280, 760), t, t0)
    fr = P(fr, 'MORE ON HEALTH AND HOUSING', 830, t, 0.9, goldL, navy, 50)
    return frame(fr)
def s9d(t):
    fr = base_(t, 74, 'TWO LINES, TWO DIRECTIONS'); T = lambda m: B9.tt(3, m)
    C = new(); card_(C, 200, 270, 1720, 800, (80, 100, 130)); d = ImageDraw.Draw(C)
    for k in range(5): d.line([260, 330 + k * 100, 1660, 330 + k * 100], fill=(60, 80, 110, 255), width=2)
    fr = Image.alpha_composite(fr, C)
    u = ease((t - 0.4) / 2.2)
    n = 40
    for pts_col, f, lab, ly in [(gold, lambda x: 700 - 120 * x, 'THE FORMULA', 660), (red, lambda x: 700 - 330 * x ** 1.6, 'YOUR BUDGET', 285)]:
        L = new(); d = ImageDraw.Draw(L); pts = [(300 + 1300 * (i / n), f(i / n)) for i in range(int(n * u) + 1)]
        if len(pts) > 1: d.line(pts, fill=pts_col + (255,), width=12, joint='curve')
        fr = Image.alpha_composite(fr, L)
        if u > 0.95: C = new(); txt(C, lab, BOLD(54), ly, pts_col, 255, x=1450); fr = Image.alpha_composite(fr, C)
    t2 = T('do not always')
    if t > t2: fr = P(fr, 'THEY DO NOT ALWAYS MOVE TOGETHER', 850, t, t2, goldL, navy, 50)
    return frame(fr)

# ============ BLOCCO 10 (740) ============
B10 = Blk2(["The Senior Citizens League, an advocacy group for older Americans, studied this in twenty twenty six.",
           "It estimates that Social Security checks now buy about thirteen point seven percent less than they did in twenty sixteen.",
           "That is an estimate from an advocacy group, not an official government number, and economists debate how to measure it.",
           "But it helps explain why a raise can still feel small at the grocery store."],
          [[0], [1], [2], [3]], 740)
def s10a(t):
    fr = base_(t, 81, 'A 2026 STUDY'); T = lambda m: B10.tt(0, m)
    if t > 0.3:
        C = new(); card_(C, 140, 280, 1100, 740, gold); building(C, 360, 460, 220, 190, goldL); txt(C, 'THE SENIOR', BOLD(60), 340, white, 255, x=790); txt(C, 'CITIZENS LEAGUE', BOLD(60), 410, goldL, 255, x=790); txt(C, 'ADVOCACY GROUP', BOLD(46), 520, grey, 255, x=790); txt(C, 'FOR OLDER AMERICANS', BOLD(46), 580, grey, 255, x=790)
        fr = A_(fr, C, (120, 260, 1120, 760), t, 0.3)
    t2 = T('studied this')
    if t > t2 - 0.3:
        C = new(); magnifier(C, 1400, 450, 100); txt(C, '2026 STUDY', BOLD(70), 650, goldL, 255, x=1470); fr = A_(fr, C, (1180, 300, 1800, 740), t, t2 - 0.3)
    fr = P(fr, 'AN ADVOCACY GROUP, NOT THE GOVERNMENT', 830, t, 0.9, goldL, navy, 46)
    return frame(fr)
def s10b(t):
    fr = base_(t, 82, 'WHAT $100 BUYS'); T = lambda m: B10.tt(1, m)
    if t > 0.3:
        C = new(); card_(C, 140, 280, 740, 760, gold); coin_stack(C, 440, 650, 10, 80); txt(C, '2016', BOLD(80), 310, goldL, 255, x=440); txt(C, 'ABOUT $100', BOLD(54), 690, white, 255, x=440); fr = A_(fr, C, (120, 260, 760, 780), t, 0.3)
    t2 = T('thirteen point seven')
    if t > t2:
        C = new(); card_(C, 1180, 280, 1780, 760, red); coin_stack(C, 1480, 650, 8, 80); txt(C, 'NOW', BOLD(80), 310, red, 255, x=1480); txt(C, 'ABOUT $86', BOLD(54), 690, white, 255, x=1480); fr = A_(fr, C, (1160, 260, 1800, 780), t, t2)
        C = new(); txt(C, '-13.7%', BOLD(86), 480, red, 255, x=960); fr = A_(fr, C, (740, 430, 1180, 600), t, t2 + 0.3)
    fr = P(fr, 'THE SAME MONEY BUYS LESS', 830, t, 0.9, goldL, navy, 50)
    return frame(fr)
def s10c(t):
    fr = base_(t, 83, 'ESTIMATE, NOT OFFICIAL'); T = lambda m: B10.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 880, 700, gold); txt(C, 'ESTIMATE FROM', BOLD(58), 340, white, 255, x=510); txt(C, 'AN ADVOCACY GROUP', BOLD(58), 410, goldL, 255, x=510); txt(C, '-13.7%', BOLD(130), 510, white, 255, x=510)
        fr = A_(fr, C, (120, 270, 900, 720), t, 0.3)
    t2 = T('not an official')
    if t > t2:
        C = new(); card_(C, 1040, 290, 1780, 700, red); txt(C, 'NOT AN OFFICIAL', BOLD(58), 360, white, 255, x=1410); txt(C, 'GOVERNMENT NUMBER', BOLD(58), 430, red, 255, x=1410); building(C, 1410, 590, 200, 190, grey)
        fr = A_(fr, C, (1020, 270, 1800, 720), t, t2)
    t3 = T('economists debate')
    if t > t3:
        C = new(); avatar(C, 520, 840, blue, 1.0); avatar(C, 1400, 840, pink, 1.0); bubble(C, 600, 740, 1300, 900, 'ECONOMISTS DEBATE\nHOW TO MEASURE IT', size=44); fr = A_(fr, C, (460, 720, 1500, 920), t, t3)
    return frame(fr)
def s10d(t):
    fr = base_(t, 84, 'THE GROCERY STORE'); T = lambda m: B10.tt(3, m)
    if t > 0.3:
        C = new(); card_(C, 140, 280, 960, 740, gold); cart(C, 450, 620, 1.7, 255, gold); txt(C, 'FEELS SMALL', BOLD(58), 320, white, 255, x=550); txt(C, 'AT THE STORE', BOLD(58), 390, goldL, 255, x=550)
        fr = A_(fr, C, (120, 260, 980, 760), t, 0.3)
    t2 = T('a raise can still')
    if t > t2 - 0.4:
        C = new(); card_(C, 1060, 280, 1780, 740, green); bill(C, 1420, 470, 240, 116, 0, 255); txt(C, 'THE RAISE', BOLD(60), 600, green, 255, x=1420); txt(C, 'STILL FEELS SMALL', BOLD(46), 670, white, 255, x=1420)
        fr = A_(fr, C, (1040, 260, 1800, 760), t, t2 - 0.4)
    fr = P(fr, 'WHY IT FEELS SMALL AT THE STORE', 830, t, 0.9, goldL, navy, 46)
    return frame(fr)

FNS = {6: [s6a, s6b, s6c, s6d], 7: [s7a, s7b, s7c, s7d], 8: [s8a, s8b, s8c, s8d], 9: [s9a, s9b, s9c, s9d], 10: [s10a, s10b, s10c, s10d]}
BLK = {6: B6, 7: B7, 8: B8, 9: B9, 10: B10}
if __name__ == '__main__':
    mode = sys.argv[1]; b = int(sys.argv[2]); fns = FNS[b]; FS = BLK[b].FS
    sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, len(fns) + 1))
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.3, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}pw{b}_{i}_{int(fq*100)}.png')
        print(b, FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b{b}-0{i}.mp4'); print('done', b, i, f, flush=True)
