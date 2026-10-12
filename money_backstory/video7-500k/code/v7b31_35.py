from v3lib import *
from v3b3_10 import POP, new
from v4b2_10 import cal_card
from v4b11_20 import calculator
from v5b1 import amb, sparks
from v5lib import arrow_r, paycheck, magnifier
from v6b1 import A_, E_, chip_src
import v7b6_15 as M
from v7b6_15 import fit, stage, card_, eq, P2, pill_last, sp, ring_, bars3
from v7b2_5 import tracker, numcard
from v7b21_30 import line_chart
import sys, math

SPEC = {31: [230, 230, 230], 32: [200, 200, 243], 33: [200, 200, 231], 34: [150, 160, 162], 35: [160, 160, 169]}
TOT = {31: 690, 32: 643, 33: 631, 34: 472, 35: 489}
for b in SPEC: assert sum(SPEC[b]) == TOT[b], b

def ic_levers2(C, cx, cy):
    d = ImageDraw.Draw(C)
    for k, p in enumerate([0.3, 0.7, 0.45, 0.8]):
        x = cx - 90 + k * 60; d.rounded_rectangle([x - 8, cy - 60, x + 8, cy + 60], radius=8, fill=A((80, 100, 130), 255))
        y = cy - 52 + p * 104; d.ellipse([x - 22, y - 16, x + 22, y + 16], fill=A(goldL, 255), outline=A(gold, 255), width=3)

# ============ 31 ============
def s31a(t):
    fr = stage(t, 'NEXT YEAR', 131); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 150, 270, 780, 600, red, 'FRANK NEEDS AGAIN', '$19,500', '+ INFLATION', 150, white); fr = P2(fr, C, (130, 250, 800, 620), t, T[0])
    if t > T[1]:
        L = new(); txt(L, 'FROM', BOLD(70), 380, goldL, 255 * E_(t, T[1]), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1140, 270, 1770, 600, blue, 'WHAT IS LEFT', '$384,400', 'AFTER THE 20% DROP', 130, white); fr = P2(fr, C, (1120, 250, 1790, 620), t, T[1])
    return frame(pill_last(fr, t, 'NEXT YEAR HE NEEDS ANOTHER $19,500, PLUS INFLATION', 760, red, (255, 255, 255), 42))

def s31b(t):
    fr = stage(t, 'A BIGGER SHARE OF WHAT IS LEFT', 132, 56); T = sp(4)
    fr = eq(fr, t, 230, [('c', 'WITHDRAWAL', '$19,500', None, red), ('o', '÷'), ('c', 'WHAT IS LEFT', '$384,400', None, blue), ('o', '='), ('c', 'THE SHARE', '5.07%', 'ABOUT', gold)], [T[0], T[1], T[2]], 250, 420, 150)
    if t > T[3]:
        C = new(); ring_(C, 960, 700, 100, 0.0507 * 6 * ease((t - T[3]) / 0.8), red, 36); txt(C, '5%+', BOLD(60), 668, white, 255, x=960); fr = P2(fr, C, (840, 590, 1080, 810), t, T[3])
    return frame(fr)

def s31c(t):
    fr = stage(t, 'A BAD MARKET EARLY HURTS THE MOST', 133, 56); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([160, 260, 960, 680], radius=34, fill=card + (255,), outline=red + (255,), width=6)
        line_chart(C, 220, 300, 900, 640, [(0.0, 0.2), (0.3, 0.3), (0.5, 0.8), (1.0, 0.9)], red, ease((t - T[0]) / 0.9), 14); txt(C, 'PRICES ARE LOW', BOLD(40), 280, white, 255, x=560)
        fr = P2(fr, C, (140, 240, 980, 700), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1020, 260, 1780, 460], radius=30, fill=card + (255,), outline=gold + (255,), width=6)
        money_bag(C, 1150, 380, 0.7); txt(C, 'WITHDRAWALS TAKE', BOLD(38), 310, white, 255, x=1470); txt(C, 'MONEY OUT', BOLD(56), 365, goldL, 255, x=1470)
        fr = P2(fr, C, (1000, 240, 1800, 480), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1020, 490, 1390, 680, green, 'ONE IDEA', 'FLEXIBILITY', None, 44, white); fr = P2(fr, C, (1000, 470, 1410, 700), t, T[2])
    if t > T[3]:
        C = new(); card_(C, 1410, 490, 1780, 680, blue, 'ANOTHER IDEA', 'CASH RESERVE', None, 44, white); fr = P2(fr, C, (1390, 470, 1800, 700), t, T[3])
    return frame(pill_last(fr, t, 'RESEARCHERS TALK ABOUT FLEXIBILITY AND A CASH RESERVE', 800, gold, navy, 42))

# ============ 32 ============
def s32a(t):
    fr = stage(t, 'NUMBER FIVE', 134); T = sp(3)
    fr = numcard(fr, t, T[0], 560, 200, 1360, 770, 5, 'FOUR THINGS THAT', 'CHANGE THE ANSWER', 'WE TEST EACH ONE', ic_levers2, purple) if t > T[0] else fr
    return frame(pill_last(tracker(fr, t, {5}, 0.3, 965), t, 'NUMBER FIVE: FOUR THINGS THAT CAN CHANGE THE ANSWER', 810, purple, navy, 40))

def s32b(t):
    fr = stage(t, 'WE SHOW THE MATH', 135); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 150, 280, 880, 620, red, 'WE ARE NOT', 'RECOMMENDING', 'ANY OF THEM', 80, white); cross(C, 800, 570, 38, red); fr = P2(fr, C, (130, 260, 900, 640), t, T[0])
    if t > T[1]:
        C = new(); calculator(C, 1280, 470, 1.6); fr = P2(fr, C, (1060, 200, 1500, 740), t, T[1])
        L = new(); arrow_r(L, 890, 1090, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); card_(C, 1500, 330, 1830, 570, gold, 'TO SEE HOW', 'EACH ONE', 'MOVES THE NUMBERS', 56, goldL); fr = P2(fr, C, (1480, 310, 1850, 590), t, T[2])
    return frame(pill_last(fr, t, 'SEE HOW EACH ONE MOVES THE NUMBERS', 790, gold, navy, 46))

def s32c(t):
    fr = stage(t, 'MARY IS THE BASELINE', 136); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([130, 240, 700, 650], radius=34, fill=card + (255,), outline=pink + (255,), width=6)
        avatar(C, 290, 400, pink, 2.4); txt(C, 'MARY', BOLD(54), 540, pink, 255, x=290); txt(C, 'BASELINE', BOLD(36), 600, grey, 255, x=290)
        fr = P2(fr, C, (110, 220, 720, 670), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 760, 230, 1260, 440, blue, 'BEFORE MEDICARE', '$3,696', 'A MONTH', 70, white); fr = P2(fr, C, (740, 210, 1280, 460), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 760, 470, 1260, 680, green, 'AFTER PART B', '$3,493', 'A MONTH', 70, white); fr = P2(fr, C, (740, 450, 1280, 700), t, T[2])
    if t > T[3]:
        C = new(); card_(C, 1320, 240, 1790, 660, purple, 'FRANK', 'TESTS EACH ONE', None, 56, white); ic_levers2(C, 1555, 520); fr = P2(fr, C, (1300, 220, 1810, 680), t, T[3])
    return frame(pill_last(fr, t, 'MARY: $3,696 BEFORE MEDICARE, $3,493 AFTER PART B', 790, gold, navy, 42))

# ============ 33 ============
def s33a(t):
    fr = stage(t, 'FIRST: THE CLAIMING AGE', 137); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([130, 250, 700, 650], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        avatar(C, 290, 410, blue, 2.4); txt(C, 'FRANK', BOLD(54), 540, blue, 255, x=290); d.ellipse([440, 300, 640, 500], fill=gold + (255,)); txt(C, '67', BOLD(110), 330, navy, 255, x=540); txt(C, 'YEARS OLD', BOLD(24), 455, navy, 255, x=540)
        fr = P2(fr, C, (110, 230, 720, 670), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 780, 280, 1250, 600, gold, 'FULL RETIREMENT AGE', '67', None, 190, goldL); fr = P2(fr, C, (760, 260, 1270, 620), t, T[1])
        L = new(); arrow_r(L, 700, 770, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); paycheck(C, 1320, 280, 1800, 600, green, '$2,071', 'PER MONTH', 'HIS CHECK AT 67', 100); fr = P2(fr, C, (1300, 260, 1820, 620), t, T[2])
        L = new(); arrow_r(L, 1260, 1310, 450, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'AT 67 (FULL RETIREMENT AGE): $2,071 A MONTH', 780, gold, navy, 46))

def s33b(t):
    fr = stage(t, 'EACH YEAR HE WAITS ADDS 8%', 138); T = sp(5)
    fr = bars3(fr, t, 720, [('AGE 67', '$2,071', 2071 / 2568, (90, 130, 190), white), ('AGE 68', '$2,237', 2237 / 2568, (90, 150, 190), white), ('AGE 69', '$2,402', 2402 / 2568, (90, 170, 170), white), ('AGE 70', '$2,568', 1.0, gold, goldL)], [T[0], T[1], T[2], T[3]], 440, 250, 110)
    L = new()
    for k in range(3):
        if t > T[k + 1]: txt(L, '+8%', BOLD(50), 580, green, 255 * E_(t, T[k + 1]), x=600 + k * 360)
    fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'EACH YEAR AFTER 67, UP TO AGE 70: +8%', 850, green, navy, 46))

def s33c(t):
    fr = stage(t, 'AT SEVENTY', 139); T = sp(4)
    fr = eq(fr, t, 230, [('c', 'CHECK AT 70', '$2,568', 'ABOUT', gold), ('o', '−'), ('c', 'CHECK AT 67', '$2,071', None, blue), ('o', '='), ('c', 'MORE EVERY MONTH', '+$497', 'ABOUT', green)], [T[0], T[1], T[2]], 250, 420, 150)
    if t > T[3]:
        C = new(); card_(C, 560, 560, 1360, 680, green, None, 'ALMOST $500 MORE EVERY MONTH', None, 56, white); fr = P2(fr, C, (540, 540, 1380, 700), t, T[3])
    return frame(fr)

# ============ 34 ============
def s34a(t):
    fr = stage(t, 'OUR VIDEO ON THE SAME IDEA', 140); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([420, 250, 1500, 690], radius=34, fill=card + (255,), outline=goldL + (255,), width=6)
        d.rounded_rectangle([480, 310, 960, 580], radius=18, fill=A((60, 90, 140), 255)); d.polygon([(680, 380), (680, 510), (790, 445)], fill=A(white, 255))
        txt(C, 'CLAIMING AT', BOLD(50), 330, white, 255, x=1230); txt(C, '62 VS 70', BOLD(110), 400, goldL, 255, x=1230); txt(C, 'THE $124,800 MISTAKE', BOLD(36), 540, grey, 255, x=1230)
        fr = P2(fr, C, (400, 230, 1520, 710), t, T[0])
    return frame(pill_last(fr, t, 'THE IDEA BEHIND OUR VIDEO: 62 VS 70', 790, gold, navy, 48))

def s34b(t):
    fr = stage(t, 'THE PRICE OF WAITING', 141); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 380, 1720, 480], radius=40, fill=(60, 80, 110, 255)); d.rounded_rectangle([200, 380, 200 + 760 * ease((t - T[0]) / 0.9), 480], radius=40, fill=red + (255,))
        txt(C, 'AGE 67', BOLD(44), 500, white, 255, x=200, anchor='l'); txt(C, 'AGE 70', BOLD(44), 500, goldL, 255, x=1720, anchor='r'); fr = P2(fr, C, (180, 360, 1740, 560), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 560, 240, 1360, 340, red, None, '3 YEARS WITHOUT HIS CHECKS', None, 52, white); fr = P2(fr, C, (540, 220, 1380, 360), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 560, 580, 1360, 740, gold, 'HE LIVES ON', 'HIS SAVINGS ALONE', None, 64, goldL); fr = P2(fr, C, (540, 560, 1380, 760), t, T[2])
    return frame(fr)

def s34c(t):
    fr = stage(t, 'WHAT THE CHECKS WOULD HAVE PAID', 142, 56); T = sp(4)
    fr = eq(fr, t, 260, [('c', 'HIS CHECK', '$2,071', 'A MONTH', blue), ('o', '×'), ('c', 'MONTHS', '36', '3 YEARS', gold), ('o', '='), ('c', 'NOT RECEIVED', '$74,556', 'ABOUT', red)], [T[0], T[1], T[2]], 270, 420, 150)
    return frame(pill_last(fr, t, 'ABOUT $74,556 THE CHECKS WOULD HAVE PAID', 640, red, (255, 255, 255), 50))

# ============ 35 ============
def s35a(t):
    fr = stage(t, 'HOW LONG TO REPAY IT?', 143); T = sp(4)
    fr = eq(fr, t, 250, [('c', 'THE EXTRA', '$5,964', 'A YEAR', green), ('o', '÷'), ('c', 'TO REPAY', '$74,556', 'THE CHECKS NOT RECEIVED', red), ('o', '='), ('c', 'ABOUT', '12.5', 'YEARS', gold)], [T[0], T[1], T[2]], 270, 420, 150)
    return frame(pill_last(fr, t, 'ROUGHLY TWELVE AND A HALF YEARS TO REPAY IT', 640, gold, navy, 48))

def s35b(t):
    fr = stage(t, 'FROM AGE 70, ABOUT 12.5 YEARS LATER', 144, 56); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 400, 1720, 480], radius=36, fill=(60, 80, 110, 255)); d.rounded_rectangle([200, 400, 200 + 1520 * 0.66 * ease((t - T[0]) / 1.0), 480], radius=36, fill=green + (255,))
        for x, lab in ((200, 'AGE 70'), (200 + 1520 * 0.66, 'ABOUT 82')): txt(C, lab, BOLD(44), 500, white if x == 200 else goldL, 255, x=x if x > 200 else 290)
        fr = P2(fr, C, (180, 380, 1740, 560), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 560, 230, 1360, 350, gold, None, 'A SIMPLE ESTIMATE', None, 56, goldL); fr = P2(fr, C, (540, 210, 1380, 370), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 560, 590, 1360, 740, red, 'NOT INCLUDED', 'INVESTMENT GROWTH', None, 56, white); fr = P2(fr, C, (540, 570, 1380, 760), t, T[2])
    return frame(fr)

def s35c(t):
    fr = stage(t, 'SO THE CHOICE DEPENDS ON...', 145); T = sp(4)
    labs = [('HIS HEALTH', 'h'), ('OTHER INCOME', 'm'), ('HOW LONG HE', 'c')]
    for k, (lab, ic) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 270, x0 + 500, 610], radius=34, fill=card + (255,), outline=goldL + (255,), width=5)
            if ic == 'h': d.rounded_rectangle([x0 + 195, 330, x0 + 305, 440], radius=16, fill=A((236, 240, 245), 255), outline=A(red, 255), width=5); d.rectangle([x0 + 240, 350, x0 + 260, 420], fill=A(red, 255)); d.rectangle([x0 + 215, 375, x0 + 285, 395], fill=A(red, 255))
            elif ic == 'm': coin_stack(C, x0 + 250, 430, 5, 56)
            else: clock(C, x0 + 250, 385, 62, 1.5, goldL)
            if ic == 'c': txt(C, 'HOW LONG HE', BOLD(46), 480, white, 255, x=x0 + 250); txt(C, 'EXPECTS TO LIVE', BOLD(40), 535, goldL, 255, x=x0 + 250)
            else: txt(C, lab, BOLD(52), 490, white, 255, x=x0 + 250)
            fr = P2(fr, C, (x0 - 20, 250, x0 + 520, 630), t, T[k])
    return frame(pill_last(fr, t, 'HEALTH, OTHER INCOME, AND HOW LONG YOU EXPECT TO LIVE', 760, gold, navy, 42))

SLIDES = {31: [s31a, s31b, s31c], 32: [s32a, s32b, s32c], 33: [s33a, s33b, s33c], 34: [s34a, s34b, s34c], 35: [s35a, s35b, s35c]}

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
