from v3lib import *
from v3b3_10 import POP, new
from v4b2_10 import cal_card
from v5b1 import amb, sparks
from v5lib import arrow_r, paycheck
from v6b1 import A_, E_, chip_src
import v7b6_15 as M
from v7b6_15 import fit, stage, card_, eq, P2, pill_last, sp, ring_, bars3
from v7b2_5 import tracker
from v7b21_30 import line_chart, house
import sys, math

SPEC = {36: [230, 230, 224], 37: [170, 170, 173], 38: [155, 155, 154], 39: [167, 167, 167], 40: [105, 105, 106]}
TOT = {36: 684, 37: 513, 38: 464, 39: 501, 40: 316}
for b in SPEC: assert sum(SPEC[b]) == TOT[b], b

def insurer(C, cx, cy, s=1.0):
    building(C, cx, cy - 20 * s, 300 * s, 220 * s, blue)
    d = ImageDraw.Draw(C); txt(C, 'INSURANCE', BOLD(int(36 * s)), cy + 110 * s, white, 255, x=cx); txt(C, 'COMPANY', BOLD(int(36 * s)), cy + 110 * s + 42 * s, white, 255, x=cx)

# ============ 36 ============
def s36a(t):
    fr = stage(t, 'SECOND: AN IMMEDIATE ANNUITY', 151); T = sp(4)
    if t > T[0]:
        C = new(); money_bag(C, 330, 440, 1.4); coin_stack(C, 150, 600, 4, 50); txt(C, 'A LUMP SUM', BOLD(52), 650, white, 255, x=330); fr = P2(fr, C, (90, 260, 560, 720), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 560, 700, 470, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); insurer(C, 880, 470, 1.0); fr = P2(fr, C, (700, 280, 1060, 700), t, T[1])
    if t > T[2]:
        L = new(); arrow_r(L, 1060, 1200, 470, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); paycheck(C, 1210, 300, 1800, 640, green, '$ / MONTH', 'FOR LIFE', 'A CHECK', 90); fr = P2(fr, C, (1190, 280, 1820, 660), t, T[2])
    return frame(pill_last(fr, t, 'YOU GIVE THEM A LUMP SUM. THEY PAY YOU A CHECK FOR LIFE.', 790, gold, navy, 42))

def s36b(t):
    fr = stage(t, 'WHAT $500,000 BUYS AT AGE 65', 152); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 130, 280, 650, 600, blue, 'IN 2026, AT AGE 65', '$500,000', 'ONE LUMP SUM', 100, white); fr = P2(fr, C, (110, 260, 670, 620), t, T[0])
        L = new(); arrow_r(L, 660, 770, 440, goldL, 255 * E_(t, T[0] + 0.1)); fr = Image.alpha_composite(fr, L)
    if t > T[1]:
        C = new(); card_(C, 790, 280, 1260, 600, red, 'LOW QUOTE', '$2,300', 'A MONTH', 100, white); fr = P2(fr, C, (770, 260, 1280, 620), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1390, 280, 1860, 600, green, 'HIGH QUOTE', '$3,500', 'A MONTH', 100, white); fr = P2(fr, C, (1370, 260, 1880, 620), t, T[2])
        L = new(); txt(L, 'TO', BOLD(46), 400, goldL, 255 * E_(t, T[2]), x=1325); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'QUOTES RANGE FROM ABOUT $2,300 TO $3,500 A MONTH', 790, gold, navy, 44))

def s36c(t):
    fr = stage(t, 'THE QUOTE DEPENDS ON...', 153); T = sp(4)
    labs = [('THE COMPANY', 'b'), ("THE BUYER'S SEX", 'p'), ('THE PAYOUT OPTION', 'c')]
    for k, (lab, ic) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 270, x0 + 500, 610], radius=34, fill=card + (255,), outline=goldL + (255,), width=5)
            if ic == 'b': building(C, x0 + 250, 400, 190, 150, blue)
            elif ic == 'p': avatar(C, x0 + 190, 405, blue, 1.7); avatar(C, x0 + 310, 405, pink, 1.7)
            else: paycheck(C, x0 + 150, 310, x0 + 350, 470, gold, '$', '', 'CHOICE', 60)
            txt(C, lab, fit(lab, 460, 46), 520, white, 255, x=x0 + 250); fr = P2(fr, C, (x0 - 20, 250, x0 + 520, 630), t, T[k])
    return frame(pill_last(fr, t, 'COMPANY, BUYER\'S SEX AND PAYOUT OPTION', 760, gold, navy, 46))

# ============ 37 ============
def s37a(t):
    fr = stage(t, 'A TYPICAL SINGLE LIFE QUOTE', 154); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 460, 260, 1460, 620, gold, 'ON $500,000 AT AGE 65', '$3,000', 'A MONTH, FOR LIFE', 220, goldL); fr = P2(fr, C, (440, 240, 1480, 640), t, T[0])
    return frame(pill_last(fr, t, 'A TYPICAL SINGLE LIFE QUOTE: NEAR $3,000 A MONTH', 770, gold, navy, 46))

def s37b(t):
    fr = stage(t, 'ALMOST DOUBLE', 155); T = sp(4)
    fr = bars3(fr, t, 720, [('WITHDRAWAL RULE', '$1,625', 1625 / 3000, (90, 130, 190), white), ('ANNUITY QUOTE', '$3,000', 1.0, gold, goldL)], [T[0], T[1]], 440, 340, 220)
    if t > T[2]:
        L = new(); txt(L, 'ALMOST', BOLD(72), 330, green, 255 * E_(t, T[2]), x=1630); txt(L, 'DOUBLE', BOLD(90), 410, green, 255 * E_(t, T[2]), x=1630); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'ALMOST DOUBLE THE $1,625 FROM THE WITHDRAWAL RULE', 830, green, navy, 42))

def s37c(t):
    fr = stage(t, 'SO WHY DOES NOT EVERYONE DO IT?', 156, 56); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 150, 250, 760, 460, red, 'BECAUSE OF', 'THE TRADE-OFFS', None, 70, white); fr = P2(fr, C, (130, 230, 780, 480), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([860, 250, 1780, 640], radius=34, fill=card + (255,), outline=gold + (255,), width=6)
        line_chart(C, 920, 300, 1720, 580, [(0, 0.5), (1, 0.5)], blue, ease((t - T[1]) / 0.7), 12); line_chart(C, 920, 300, 1720, 580, [(0, 0.5), (0.3, 0.42), (0.6, 0.25), (1, 0.05)], red, ease((t - T[1] - 0.3) / 0.9), 12)
        txt(C, 'THE CHECK STAYS FLAT', BOLD(40), 280, blue, 255, x=1320); txt(C, 'PRICES KEEP RISING', BOLD(40), 590, red, 255, x=1320); fr = P2(fr, C, (840, 230, 1800, 660), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 150, 490, 760, 640, gold, None, 'NO RAISE FOR INFLATION', None, 46, goldL); fr = P2(fr, C, (130, 470, 780, 660), t, T[2])
    return frame(pill_last(fr, t, 'MOST BASIC ANNUITIES DO NOT RISE WITH INFLATION', 790, red, (255, 255, 255), 44))

# ============ 38 ============
def s38a(t):
    fr = stage(t, 'THE MONEY IS NO LONGER YOURS', 157); T = sp(4)
    if t > T[0]:
        C = new(); money_bag(C, 460, 460, 1.7); fr = P2(fr, C, (250, 240, 680, 700), t, T[0])
        L = new(); arrow_r(L, 700, 900, 470, red, 255 * E_(t, T[0] + 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[1]:
        C = new(); insurer(C, 1060, 430, 0.9); fr = P2(fr, C, (880, 240, 1240, 700), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1290, 270, 1810, 640, red, 'NOTHING LEFT FOR', 'AN EMERGENCY', 'OR FOR HEIRS', 62, white); fr = P2(fr, C, (1280, 250, 1820, 660), t, T[2])
    return frame(pill_last(fr, t, 'NOTHING LEFT FOR AN EMERGENCY OR FOR HEIRS', 790, red, (255, 255, 255), 46))

def s38b(t):
    fr = stage(t, 'EXTRA FEATURES COST A LITTLE EXTRA', 158, 56); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 140, 270, 770, 600, green, 'EXTRA FEATURES', 'HEIRS, INFLATION', 'YOU CAN PAY FOR THEM', 56, white); fr = P2(fr, C, (120, 250, 790, 620), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 790, 930, 430, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); paycheck(C, 950, 280, 1500, 600, blue, 'LOWER', 'PER MONTH', 'THE CHECK', 100); fr = P2(fr, C, (930, 260, 1520, 620), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1560, 300, 1840, 560, red, 'THE PRICE IS', 'LESS', 'MONTHLY INCOME', 64, white); fr = P2(fr, C, (1540, 280, 1860, 580), t, T[2])
    return frame(pill_last(fr, t, 'EXTRA FEATURES LOWER THE CHECK', 790, gold, navy, 50))

def s38c(t):
    fr = stage(t, 'THE GUARANTEE HAS A LIMIT', 159); T = sp(4)
    if t > T[0]:
        C = new(); insurer(C, 460, 400, 1.0); fr = P2(fr, C, (240, 200, 680, 640), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 700, 900, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 920, 250, 1780, 560, gold, 'THE GUARANTEE IS ONLY AS STRONG AS', 'THE INSURANCE COMPANY', 'BEHIND IT', 70, goldL); fr = P2(fr, C, (900, 230, 1800, 580), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 560, 620, 1360, 740, blue, None, "NOW, A PARTIAL VERSION", None, 50, white); fr = P2(fr, C, (540, 600, 1380, 760), t, T[2])
    return frame(fr)

# ============ 39 ============
def s39a(t):
    fr = stage(t, 'FRANK PUTS HALF IN AN ANNUITY', 160); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([140, 250, 640, 660], radius=34, fill=card + (255,), outline=blue + (255,), width=6); avatar(C, 290, 420, blue, 2.2); txt(C, 'FRANK', BOLD(50), 560, blue, 255, x=290); money_bag(C, 500, 450, 0.9); fr = P2(fr, C, (120, 230, 660, 680), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 650, 780, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 800, 280, 1230, 600, gold, 'INTO AN ANNUITY', '$250,000', 'HALF OF $500,000', 90, goldL); fr = P2(fr, C, (780, 260, 1250, 620), t, T[1])
    if t > T[2]:
        L = new(); arrow_r(L, 1240, 1340, 450, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); paycheck(C, 1360, 280, 1830, 600, green, '$1,537.50', 'A MONTH', 'THE ANNUITY PAYS', 80); fr = P2(fr, C, (1340, 260, 1850, 620), t, T[2])
    return frame(pill_last(fr, t, '$250,000 IN AN ANNUITY PAYS $1,537.50 A MONTH', 790, gold, navy, 44))

def s39b(t):
    fr = stage(t, 'THE OTHER HALF STAYS INVESTED', 161); T = sp(4)
    if t > T[0]:
        C = new(); money_bag(C, 360, 430, 1.5); card_(C, 190, 630, 530, 730, blue, None, '$250,000', None, 50, white); fr = P2(fr, C, (140, 240, 580, 750), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 590, 700, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 720, 290, 1150, 590, blue, 'HE WITHDRAWS', '3.9%', 'FROM THE $250,000', 160, white); fr = P2(fr, C, (700, 270, 1170, 610), t, T[1])
    if t > T[2]:
        L = new(); arrow_r(L, 1160, 1260, 450, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); paycheck(C, 1280, 280, 1830, 600, blue, '$812.50', 'A MONTH', 'FROM SAVINGS', 100); fr = P2(fr, C, (1260, 260, 1850, 620), t, T[2])
    return frame(pill_last(fr, t, 'THE OTHER $250,000 AT 3.9%: $812.50 A MONTH', 790, blue, navy, 46))

def s39c(t):
    fr = stage(t, 'THE PARTIAL VERSION: TWO PIECES', 162); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 260, 940, 660], radius=34, fill=card + (255,), outline=gold + (255,), width=6)
        d.rounded_rectangle([240, 300, 590, 520], radius=22, fill=A(gold, 255)); txt(C, 'ANNUITY', BOLD(40), 320, navy, 255, x=415); txt(C, '$250,000', BOLD(50), 380, navy, 255, x=415); txt(C, '$1,537.50', BOLD(44), 450, (60, 40, 10), 255, x=415)
        d.rounded_rectangle([610, 300, 900, 520], radius=22, fill=A((90, 130, 190), 255)); txt(C, 'INVESTED', BOLD(36), 320, white, 255, x=755); txt(C, '$250,000', BOLD(44), 380, white, 255, x=755); txt(C, '$812.50', BOLD(44), 450, white, 255, x=755)
        txt(C, 'HIS $500,000, SPLIT IN TWO', BOLD(36), 585, goldL, 255, x=570); fr = P2(fr, C, (180, 240, 960, 680), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 1040, 260, 1780, 660, green, 'EACH MONTH, FROM SAVINGS', '$2,350', 'BOTH PIECES TOGETHER', 160, white); fr = P2(fr, C, (1020, 240, 1800, 680), t, T[1])
        L = new(); arrow_r(L, 950, 1030, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'TWO PIECES, ONE PLAN', 790, gold, navy, 52))

# ============ 40 ============
def s40a(t):
    fr = stage(t, 'BOTH PIECES TOGETHER', 163); T = sp(4)
    fr = eq(fr, t, 250, [('c', 'ANNUITY', '$1,537.50', 'A MONTH', gold), ('o', '+'), ('c', 'INVESTED HALF', '$812.50', 'A MONTH', blue), ('o', '='), ('c', 'FROM SAVINGS', '$2,350', 'A MONTH', green)], [T[0], T[1], T[2]], 270, 420, 150)
    return frame(pill_last(fr, t, 'TOGETHER: $2,350 A MONTH FROM SAVINGS', 650, green, navy, 52))

def s40b(t):
    fr = stage(t, 'COMPARED WITH THE FIRST PLAN', 164); T = sp(4)
    fr = bars3(fr, t, 720, [('ALL INVESTED, 3.9%', '$1,625', 1625 / 2350, (90, 130, 190), white), ('HALF IN AN ANNUITY', '$2,350', 1.0, green, white)], [T[0], T[1]], 440, 340, 220)
    if t > T[2]:
        C = new(); card_(C, 1440, 330, 1830, 500, gold, 'THE DIFFERENCE', '+$725', None, 76, goldL); fr = P2(fr, C, (1420, 310, 1850, 520), t, T[2])
    return frame(pill_last(fr, t, 'INSTEAD OF $1,625: $2,350 A MONTH', 830, green, navy, 46))

def s40c(t):
    fr = stage(t, 'THIS IS A HYPOTHETICAL', 165); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 360, 270, 1560, 650, gold, 'A HYPOTHETICAL EXAMPLE', 'USING AN AVERAGE QUOTE', 'YOUR OWN QUOTE WILL BE DIFFERENT', 80, goldL); fr = P2(fr, C, (340, 250, 1580, 670), t, T[0])
    return frame(pill_last(fr, t, 'HYPOTHETICAL: AN AVERAGE QUOTE, NOT A PROMISE', 770, gold, navy, 46))

SLIDES = {36: [s36a, s36b, s36c], 37: [s37a, s37b, s37c], 38: [s38a, s38b, s38c], 39: [s39a, s39b, s39c], 40: [s40a, s40b, s40c]}

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
