from v3lib import *
from v3b3_10 import POP, new
from v4b2_10 import cal_card
from v5b1 import amb, sparks
from v5lib import arrow_r, paycheck
from v6b1 import A_, E_, chip_src
import v7b6_15 as M
from v7b6_15 import fit, stage, card_, eq, P2, pill_last, sp, ring_, bars3
from v7b2_5 import tracker, ic_med
from v7b21_30 import line_chart
from v7b31_35 import ic_levers2
import sys, math

SPEC = {41: [169, 169, 169], 42: [196, 197], 43: [155, 155, 156], 44: [155, 154, 154], 45: [151, 151, 151]}
TOT = {41: 507, 42: 393, 43: 466, 44: 463, 45: 453}
for b in SPEC: assert sum(SPEC[b]) == TOT[b], b

def med_icon(C, cx, cy, s=1.0):
    d = ImageDraw.Draw(C); d.rounded_rectangle([cx - 55 * s, cy - 55 * s, cx + 55 * s, cy + 55 * s], radius=int(14 * s), fill=A((236, 240, 245), 255), outline=A(red, 255), width=5)
    d.rectangle([cx - 10 * s, cy - 36 * s, cx + 10 * s, cy + 36 * s], fill=A(red, 255)); d.rectangle([cx - 36 * s, cy - 10 * s, cx + 36 * s, cy + 10 * s], fill=A(red, 255))

def timeline(C, x0, x1, y, marks, spans=()):
    """marks: (x, label, col); spans: (xa, xb, col, label)"""
    d = ImageDraw.Draw(C); d.rounded_rectangle([x0, y, x1, y + 16], radius=8, fill=(60, 80, 110, 255))
    for xa, xb, col, lab in spans:
        d.rounded_rectangle([xa, y - 6, xb, y + 22], radius=12, fill=col + (255,))
        if lab: txt(C, lab, BOLD(36), y - 64, white, 255, x=(xa + xb) / 2)
    for x, lab, col in marks:
        d.ellipse([x - 20, y - 12, x + 20, y + 28], fill=col + (255,), outline=white + (255,), width=4); txt(C, lab, BOLD(44), y + 50, col, 255, x=x)

# ============ 41 ============
def s41a(t):
    fr = stage(t, 'THIRD: FLEXIBILITY', 171); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 140, 260, 760, 620, blue, 'THE 3.9% RATE ASSUMES', 'THE SAME AMOUNT', 'EVERY YEAR, NO MATTER WHAT', 76, white); fr = P2(fr, C, (120, 240, 780, 640), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([860, 260, 1780, 620], radius=34, fill=card + (255,), outline=gold + (255,), width=6)
        txt(C, 'SPENDING EACH YEAR', BOLD(40), 285, white, 255, x=1320)
        for k in range(7): d.rounded_rectangle([920 + k * 120, 480 - 40 - k * 6, 920 + k * 120 + 90, 560], radius=10, fill=A(gold, 255))
        txt(C, 'INFLATION ADJUSTED', BOLD(34), 575, goldL, 255, x=1320); fr = P2(fr, C, (840, 240, 1800, 640), t, T[1])
    return frame(pill_last(fr, t, 'THE SAME INFLATION-ADJUSTED AMOUNT, EVERY YEAR', 770, blue, navy, 44))

def s41b(t):
    fr = stage(t, 'WILLING TO CUT AFTER BAD MARKET YEARS', 172, 56); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([160, 260, 960, 660], radius=34, fill=card + (255,), outline=red + (255,), width=6)
        line_chart(C, 220, 300, 900, 620, [(0, 0.2), (0.3, 0.3), (0.5, 0.8), (1, 0.9)], red, ease((t - T[0]) / 0.9), 14); txt(C, 'A BAD MARKET YEAR', BOLD(42), 280, white, 255, x=560); fr = P2(fr, C, (140, 240, 980, 680), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 980, 1090, 460, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1100, 260, 1780, 660, green, 'THE RETIREE CHOOSES TO', 'CUT SPENDING', None, 68, white)
        for k in range(4): ImageDraw.Draw(C).rounded_rectangle([1180 + k * 140, 560 - (4 - k) * 0 - (30 if k > 0 else 80) , 1180 + k * 140 + 100, 630], radius=10, fill=A(green if k else gold, 255))
        fr = P2(fr, C, (1080, 240, 1800, 680), t, T[1])
    return frame(pill_last(fr, t, 'WILLING TO CUT SPENDING AFTER BAD MARKET YEARS', 800, green, navy, 44))

def s41c(t):
    fr = stage(t, 'THEY CAN START HIGHER', 173); T = sp(5)
    fr = bars3(fr, t, 700, [('FIXED SPENDING', '3.9%', 3.9 / 5.7, (90, 130, 190), white), ('FLEXIBLE SPENDING', '5.7%', 1.0, green, white)], [T[0], T[1]], 440, 340, 220)
    if t > T[2]:
        C = new(); card_(C, 1420, 280, 1830, 440, gold, 'UP TO', 'AT 5.7%', None, 70, goldL); fr = P2(fr, C, (1400, 260, 1850, 460), t, T[2])
    fr = chip_src(fr, 'SOURCE: MORNINGSTAR RESEARCH', 780, t, T[3])
    return frame(pill_last(fr, t, 'RETIREES WHO CAN CUT SPENDING MAY START AT UP TO 5.7%', 860, green, navy, 40))

# ============ 42 ============
def s42a(t):
    fr = stage(t, 'FIVE POINT SEVEN PERCENT OF $500,000', 174, 56); T = sp(4)
    fr = eq(fr, t, 250, [('c', 'YOUR SAVINGS', '$500,000', None, gold), ('o', '×'), ('c', 'THE RATE', '5.7%', 'FLEXIBLE', green), ('o', '='), ('c', 'EVERY YEAR', '$28,500', None, goldL)], [T[0], T[1], T[2]], 270, 420, 150)
    return frame(pill_last(fr, t, '$28,500 A YEAR', 650, green, navy, 56))

def s42b(t):
    fr = stage(t, 'A MONTH, AND THE TRADE-OFF', 175); T = sp(5)
    fr = eq(fr, t, 200, [('c', 'EVERY YEAR', '$28,500', None, gold), ('o', '÷'), ('c', 'MONTHS', '12', None, blue), ('o', '='), ('c', 'EVERY MONTH', '$2,375', None, green)], [T[0], T[1], T[2]], 250, 420, 150)
    if t > T[3]:
        C = new(); d = ImageDraw.Draw(C); d.polygon([(960, 560), (900, 640), (1020, 640)], fill=A((120, 130, 150), 255)); d.rectangle([450, 520, 1470, 534], fill=A((120, 130, 150), 255))
        card_(C, 330, 450, 800, 570, green, 'MORE INCOME NOW', None, None, 40, white); card_(C, 1120, 470, 1590, 590, red, 'LESS CERTAINTY LATER', None, None, 40, white); fr = P2(fr, C, (310, 430, 1610, 650), t, T[3])
    return frame(pill_last(fr, t, 'MORE INCOME NOW, LESS CERTAINTY LATER', 780, gold, navy, 48))

# ============ 43 ============
def s43a(t):
    fr = stage(t, 'FOURTH: THE RETIREMENT DATE', 176); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 140, 260, 760, 640, gold, 'EVERYTHING SO FAR ASSUMED', 'AGE 67', None, 130, goldL); fr = P2(fr, C, (120, 240, 780, 660), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([860, 260, 1780, 640], radius=34, fill=card + (255,), outline=red + (255,), width=6); med_icon(C, 1060, 450, 1.5); check(C, 1180, 380, 38, green)
        txt(C, 'MEDICARE', BOLD(60), 340, white, 255, x=1480); txt(C, 'ALREADY ACTIVE', BOLD(48), 420, green, 255, x=1480); fr = P2(fr, C, (840, 240, 1800, 660), t, T[1])
    return frame(pill_last(tracker(fr, t, {5}, 0.3, 965), t, 'EVERYTHING SO FAR: AGE 67, WITH MEDICARE ACTIVE', 810, gold, navy, 42))

def s43b(t):
    fr = stage(t, 'RETIRE AT 60 AND THE PICTURE CHANGES', 177, 56); T = sp(5)
    if t > T[0]:
        C = new(); timeline(C, 260, 1660, 520, [(300, '60', red)], []); fr = P2(fr, C, (240, 420, 1700, 620), t, T[0])
    if t > T[1]:
        C = new(); timeline(C, 260, 1660, 520, [(300, '60', red), (1060, '65', blue)], [(300, 1060, red, '5 YEARS')]); fr = P2(fr, C, (240, 420, 1700, 620), t, T[1])
    if t > T[2]:
        C = new(); med_icon(C, 1060, 300, 1.0); txt(C, 'MEDICARE STARTS', BOLD(44), 380, white, 255, x=1060); fr = P2(fr, C, (840, 220, 1280, 440), t, T[2])
    if t > T[3]:
        C = new(); timeline(C, 260, 1660, 520, [(300, '60', red), (1060, '65', blue), (1500, '67', gold)], [(300, 1060, red, '5 YEARS')]); fr = P2(fr, C, (240, 420, 1700, 620), t, T[3])
    return frame(pill_last(fr, t, 'MEDICARE STARTS AT 65', 800, red, (255, 255, 255), 52))

def s43c(t):
    fr = stage(t, 'FIVE YEARS OF HEALTH INSURANCE TO PAY FOR', 178, 54); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 140, 260, 700, 640, red, 'AGE 60 TO 65', '5 YEARS', 'BEFORE MEDICARE', 120, white); fr = P2(fr, C, (120, 240, 720, 660), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 710, 810, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([830, 260, 1780, 640], radius=34, fill=card + (255,), outline=gold + (255,), width=6)
        for k in range(5): d.rounded_rectangle([880 + k * 175, 330, 880 + k * 175 + 150, 480], radius=18, fill=(236, 240, 245, 255), outline=red + (255,), width=5); txt(C, 'YEAR ' + str(k + 1), BOLD(34), 360, (30, 40, 70), 255, x=955 + k * 175); med_icon(C, 955 + k * 175, 440, 0.4)
        txt(C, 'A HEALTH INSURANCE BILL EVERY YEAR', BOLD(42), 540, goldL, 255, x=1300); fr = P2(fr, C, (810, 240, 1800, 660), t, T[1])
    return frame(pill_last(fr, t, 'FIVE YEARS OF HEALTH INSURANCE TO PAY FOR', 800, red, (255, 255, 255), 46))

# ============ 44 ============
def s44a(t):
    fr = stage(t, 'SOCIAL SECURITY CAN START AT 62', 179); T = sp(4)
    fr = bars3(fr, t, 700, [('START AT 62', 'REDUCED', 0.72, red, white), ('FULL AGE 67', 'FULL CHECK', 1.0, green, white)], [T[0], T[1]], 440, 340, 220)
    if t > T[2]:
        C = new(); card_(C, 1420, 300, 1840, 470, red, 'THE REDUCTION IS', 'PERMANENT', None, 60, white); fr = P2(fr, C, (1400, 280, 1860, 490), t, T[2])
    return frame(pill_last(fr, t, 'AT 62, BUT WITH A PERMANENT REDUCTION', 830, red, (255, 255, 255), 46))

def s44b(t):
    fr = stage(t, 'THE SAME SAVINGS, FIVE YEARS LONGER', 180, 56); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 300, 200 + 1000 * ease((t - T[0]) / 0.7), 380], radius=30, fill=A(blue, 255)); txt(C, 'RETIRE AT 67', BOLD(40), 400, white, 255, x=200, anchor='l'); fr = P2(fr, C, (180, 280, 1700, 440), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 500, 200 + 1000 * ease((t - T[1]) / 0.7), 580], radius=30, fill=A(gold, 255)); d.rounded_rectangle([1200, 500, 1200 + 400 * ease((t - T[1] - 0.4) / 0.6), 580], radius=30, fill=A(red, 255)) if t > T[1] + 0.4 else None
        txt(C, 'RETIRE AT 60', BOLD(40), 600, white, 255, x=200, anchor='l'); fr = P2(fr, C, (180, 480, 1760, 650), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1250, 280, 1700, 440, red, '+5 YEARS', 'THE MONEY MUST LAST', None, 60, white); fr = P2(fr, C, (1230, 260, 1720, 460), t, T[2])
    return frame(pill_last(fr, t, 'THE SAME SAVINGS HAVE TO LAST FIVE YEARS LONGER', 790, red, (255, 255, 255), 42))

def s44c(t):
    fr = stage(t, 'ENOUGH AT 67, NOT AT 60?', 181); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 140, 260, 880, 620, green, 'RETIRE AT 67', '$500,000', 'MAY FEEL LIKE ENOUGH', 100, white); check(C, 800, 330, 44, green); fr = P2(fr, C, (120, 240, 900, 640), t, T[0])
    if t > T[1]:
        L = new(); txt(L, 'VS', BOLD(90), 400, goldL, 255 * E_(t, T[1]), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1040, 260, 1780, 620, red, 'RETIRE AT 60', '$500,000', 'MAY NOT BE ENOUGH', 100, white); cross(C, 1700, 330, 44, red); fr = P2(fr, C, (1020, 240, 1800, 640), t, T[1])
    return frame(pill_last(fr, t, 'ENOUGH AT SIXTY SEVEN. NOT ENOUGH AT SIXTY.', 780, gold, navy, 46))

# ============ 45 ============
def s45a(t):
    fr = stage(t, "LET'S PUT IT ALL TOGETHER", 182); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([140, 250, 640, 660], radius=34, fill=card + (255,), outline=pink + (255,), width=6); avatar(C, 290, 410, pink, 2.4); txt(C, 'MARY', BOLD(54), 540, pink, 255, x=290); txt(C, 'BASELINE', BOLD(34), 600, grey, 255, x=290); fr = P2(fr, C, (120, 230, 660, 680), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 650, 760, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); paycheck(C, 780, 270, 1360, 640, green, '$3,493', 'A MONTH', 'AFTER PART B', 130); fr = P2(fr, C, (760, 250, 1380, 660), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1420, 270, 1830, 640, purple, "FRANK'S", '4 TESTS', None, 90, white); ic_levers2(C, 1625, 560); fr = P2(fr, C, (1400, 250, 1850, 660), t, T[2])
    return frame(pill_last(fr, t, 'MARY: $3,493 A MONTH AFTER PART B', 790, pink, navy, 46))

def s45b(t):
    fr = stage(t, "FRANK'S FOUR TESTS", 183); T = sp(5)
    labs = [('1', 'CLAIM AT 70', gold), ('2', 'ANNUITY', blue), ('3', 'FLEXIBILITY', green), ('4', 'RETIRE EARLY', red)]
    for k, (n, lab, col) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 130 + k * 440; d.rounded_rectangle([x0, 280, x0 + 400, 600], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            d.ellipse([x0 + 150, 310, x0 + 250, 410], fill=col + (255,)); txt(C, n, BOLD(70), 322, navy, 255, x=x0 + 200); txt(C, lab, fit(lab, 370, 48), 470, white, 255, x=x0 + 200); fr = P2(fr, C, (x0 - 20, 260, x0 + 420, 620), t, T[k])
    return frame(pill_last(fr, t, 'FOUR TESTS: CLAIMING AGE, ANNUITY, FLEXIBILITY, RETIREMENT DATE', 760, purple, navy, 38))

def s45c(t):
    fr = stage(t, 'TEST ONE: WAIT UNTIL SEVENTY', 184); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 140, 260, 680, 640, blue, 'FULL AGE 67', '$2,071', 'A MONTH', 110, white); fr = P2(fr, C, (120, 240, 700, 660), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 690, 790, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 800, 260, 1340, 640, gold, 'AT AGE 70', '$2,568', 'A MONTH', 110, goldL); fr = P2(fr, C, (780, 240, 1360, 660), t, T[1])
    if t > T[2]:
        C = new(); card_(C, 1400, 300, 1840, 600, green, 'ABOUT', '+$497', 'A MONTH MORE', 100, white); fr = P2(fr, C, (1380, 280, 1860, 620), t, T[2])
    return frame(pill_last(fr, t, 'WAITING UNTIL 70 ADDS ABOUT $497 A MONTH', 790, green, navy, 46))

SLIDES = {41: [s41a, s41b, s41c], 42: [s42a, s42b], 43: [s43a, s43b, s43c], 44: [s44a, s44b, s44c], 45: [s45a, s45b, s45c]}

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
