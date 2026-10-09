from v3lib import *
from v3b3_10 import POP, new
from v4b2_10 import cal_card
from v5b1 import amb, sparks
from v5lib import arrow_r, paycheck
from v6b1 import A_, E_, chip_src
import v7b6_15 as M
from v7b6_15 import fit, stage, card_, eq, P2, pill_last, sp, ring_, bars3, avatars
from v7b2_5 import tracker, ic_med, ic_coins
import sys, math

SPEC = {16: [150, 150, 159], 17: [75, 165, 105, 215], 18: [115, 260, 203], 19: [186, 159, 85, 177], 20: [190, 110, 164]}
TOT = {16: 459, 17: 560, 18: 578, 19: 607, 20: 464}
for b in SPEC: assert sum(SPEC[b]) == TOT[b], b
D = M.D

def ic_bed(C, cx, cy, s=1.0):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 120 * s, cy + 10 * s, cx + 120 * s, cy + 50 * s], radius=int(10 * s), fill=A(blue, 255))
    d.rounded_rectangle([cx - 120 * s, cy - 40 * s, cx - 90 * s, cy + 70 * s], radius=int(8 * s), fill=A((70, 100, 160), 255))
    d.rounded_rectangle([cx - 85 * s, cy - 15 * s, cx - 25 * s, cy + 10 * s], radius=int(10 * s), fill=A((236, 240, 245), 255))
    d.rectangle([cx + 112 * s, cy + 50 * s, cx + 120 * s, cy + 70 * s], fill=A((70, 100, 160), 255))

def vs_cards(fr, t, t0, items, y=280, h=330):
    pass

# ======================= BLOCCO 16 =======================
def s16a(t):
    fr = stage(t, 'FIDELITY ESTIMATES', 71); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 130, 260, 700, 640, blue, 'FIDELITY INVESTMENTS', 'RETIREE HEALTH', 'CARE COST ESTIMATE', 70, white); fr = P2(fr, C, (110, 240, 720, 660), t, T[0])
    if t > T[1]:
        C = new(); avatar(C, 960, 470, gold, 2.8); txt(C, 'A 65-YEAR-OLD', BOLD(44), 600, white, 255, x=960); txt(C, 'RETIRING IN 2026', BOLD(44), 650, goldL, 255, x=960)
        L = new(); arrow_r(L, 720, 800, 450, goldL, 255 * E_(t, T[1] - 0.2)); C = Image.alpha_composite(C, L) if False else C
        fr = P2(fr, C, (740, 280, 1200, 700), t, T[1])
        L = new(); arrow_r(L, 715, 790, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); cal_card(C, 1380, 290, 1760, 640, 'RETIRING IN', '2026', 120, blue); fr = P2(fr, C, (1360, 270, 1780, 660), t, T[2])
        L = new(); arrow_r(L, 1215, 1370, 450, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'FIDELITY ESTIMATES HEALTH COSTS FOR A 65-YEAR-OLD', 830, blue, navy, 44))

def s16b(t):
    fr = stage(t, 'HEALTH CARE OVER THE REST OF THEIR LIFE', 72, 56); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 520, 1720, 600], radius=40, fill=(60, 80, 110, 255))
        d.rounded_rectangle([200, 520, 1720 * 0 + 200 + 1520 * ease((t - T[0]) / 1.0), 600], radius=40, fill=gold + (255,))
        txt(C, 'AGE 65', BOLD(44), 620, white, 255, x=200, anchor='l'); txt(C, 'THE REST OF THEIR LIFE', BOLD(44), 620, goldL, 255, x=1720, anchor='r')
        fr = P2(fr, C, (180, 500, 1740, 690), t, T[0])
    if t > T[1]:
        v = 185500 * ease((t - T[1]) / 1.0)
        C = new(); card_(C, 560, 250, 1360, 480, gold, 'AN AVERAGE OF', '$' + f'{int(v):,}', None, 150, goldL); fr = P2(fr, C, (540, 230, 1380, 500), t, T[1])
    return frame(pill_last(fr, t, 'ABOUT $185,500 ON HEALTH CARE, PER PERSON', 780, gold, navy, 46))

def s16c(t):
    fr = stage(t, 'WHAT THE ESTIMATE COVERS', 73); T = sp(4)
    labs = [('MEDICARE', 'PREMIUMS', red, 'm'), ('DRUG', 'COVERAGE', blue, 'p'), ('OUT-OF-POCKET', 'COSTS', gold, 'w')]
    for k, (a, b2, col, ic) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 270, x0 + 500, 610], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            if ic == 'm': d.rounded_rectangle([x0 + 195, 330, x0 + 305, 440], radius=16, fill=A((236, 240, 245), 255), outline=A(red, 255), width=5), d.rectangle([x0 + 240, 350, x0 + 260, 420], fill=A(red, 255)), d.rectangle([x0 + 215, 375, x0 + 285, 395], fill=A(red, 255))
            elif ic == 'p': d.rounded_rectangle([x0 + 190, 340, x0 + 310, 440], radius=40, fill=col + (255,)); d.line([x0 + 250, 340, x0 + 250, 440], fill=white + (255,), width=6)
            else: wallet(C, x0 + 250, 395, 1.1)
            txt(C, a, fit(a, 470, 52), 480, white, 255, x=x0 + 250); txt(C, b2, BOLD(52), 540, col, 255, x=x0 + 250); fr = P2(fr, C, (x0 - 20, 250, x0 + 520, 630), t, T[k])
    fr = chip_src(fr, 'SOURCE: FIDELITY, 2026 RETIREE HEALTH CARE COST ESTIMATE', 700, t, T[3])
    return frame(pill_last(fr, t, 'IT COVERS MEDICARE PREMIUMS, DRUGS AND OUT-OF-POCKET COSTS', 790, red, (255, 255, 255), 40))

# ======================= BLOCCO 17 =======================
def s17a(t):
    fr = stage(t, 'WHAT IT DOES NOT INCLUDE', 74); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([560, 250, 1360, 640], radius=34, fill=card + (255,), outline=red + (255,), width=6)
        ic_bed(C, 960, 420, 1.5); cross(C, 1230, 330, 50, red); txt(C, 'LONG-TERM CARE', BOLD(60), 540, white, 255, x=960); fr = P2(fr, C, (540, 230, 1380, 660), t, T[0])
    return frame(pill_last(fr, t, 'NOT INCLUDED: LONG-TERM CARE', 780, red, (255, 255, 255), 52))

def s17b(t):
    fr = stage(t, 'SPREAD OVER TWENTY YEARS', 75); T = sp(5)
    fr = eq(fr, t, 250, [('c', 'HEALTH CARE COST', '$185,500', 'PER PERSON', gold), ('o', '÷'), ('c', 'YEARS', '20', 'OF RETIREMENT', blue), ('o', '='), ('c', 'EVERY YEAR', '$9,275', 'ABOUT', green)], [T[0], T[1], T[2]], 270, 420, 150)
    if t > T[3]:
        C = new(); d = ImageDraw.Draw(C)
        for k in range(20): d.rounded_rectangle([280 + k * 68, 620, 280 + k * 68 + 56, 690], radius=10, fill=(green if k < int(20 * ease((t - T[3]) / 1.0)) else (60, 80, 110)) + (255,))
        txt(C, 'YEAR 1', BOLD(34), 710, grey, 255, x=300); txt(C, 'YEAR 20', BOLD(34), 710, grey, 255, x=1620)
        fr = P2(fr, C, (200, 600, 1720, 760), t, T[3])
    return frame(pill_last(fr, t, 'ABOUT $9,275 A YEAR, OVER TWENTY YEARS', 790, green, navy, 46))

def s17c(t):
    fr = stage(t, 'NOW, TAXES', 76); T = sp(3)
    if t > T[0]:
        C = new(); tax_form(C, 700, 250, 240, 330, 255, 'TAX'); d = ImageDraw.Draw(C)
        d.ellipse([1030, 380, 1230, 580], fill=A(gold, 255)); txt(C, '$', BOLD(150), 400, navy, 255, x=1130)
        fr = P2(fr, C, (680, 230, 1260, 600), t, T[0])
        L = new(); arrow_r(L, 960, 1020, 480, goldL, 255 * E_(t, T[0] + 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[1]:
        L = new(); txt(L, '?', BOLD(150), 300, red, 255 * E_(t, T[1]), x=1450); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'THE PART THAT SURPRISES PEOPLE', 780, red, (255, 255, 255), 52))

def s17d(t):
    fr = stage(t, "FRANK'S TRADITIONAL 401(k)", 77); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([140, 250, 900, 700], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        avatar(C, 290, 400, blue, 2.4); txt(C, 'FRANK', BOLD(54), 570, blue, 255, x=290)
        d.rounded_rectangle([430, 320, 870, 600], radius=22, fill=A((60, 90, 140), 255), outline=goldL + (255,), width=4)
        txt(C, 'TRADITIONAL', BOLD(40), 345, white, 255, x=650); txt(C, '401(k)', BOLD(76), 400, goldL, 255, x=650); txt(C, '$500,000', BOLD(52), 500, white, 255, x=650)
        fr = P2(fr, C, (120, 230, 920, 720), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 920, 1030, 470, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1040, 290, 1790, 650, gold, 'EVERY DOLLAR HE WITHDRAWS', 'COUNTS AS', None, 84, white)
        txt(C, 'INCOME', BOLD(130), 470, goldL, 255, x=1415); fr = P2(fr, C, (1020, 270, 1810, 670), t, T[1])
    return frame(pill_last(fr, t, 'EVERY DOLLAR HE WITHDRAWS COUNTS AS INCOME', 790, gold, navy, 46))

# ======================= BLOCCO 18 =======================
def s18a(t):
    fr = stage(t, "FRANK'S WITHDRAWALS", 78); T = sp(3)
    if t > T[0]:
        C = new(); money_bag(C, 400, 470, 1.7); coin_stack(C, 210, 640, 5, 60); fr = P2(fr, C, (110, 270, 620, 760), t, T[0])
    if t > T[1]:
        v = 19500 * ease((t - T[1]) / 0.9)
        C = new(); card_(C, 760, 290, 1700, 600, gold, 'FROM HIS 401(k), EVERY YEAR', '$' + f'{int(v):,}', None, 190, goldL); fr = P2(fr, C, (740, 270, 1720, 620), t, T[1])
        L = new(); arrow_r(L, 620, 740, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'HIS WITHDRAWALS: $19,500 A YEAR', 780, gold, navy, 52))

def s18b(t):
    fr = stage(t, 'THE I R S COUNTS HALF OF HIS SOCIAL SECURITY', 79, 54); T = sp(5)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 220, 1720, 330], radius=30, fill=card + (255,), outline=blue + (255,), width=5)
        d.rounded_rectangle([210, 230, 965, 320], radius=24, fill=A((90, 130, 190), 255)); d.rounded_rectangle([965, 230, 1710, 320], radius=24, fill=A((60, 80, 110), 255))
        txt(C, 'SOCIAL SECURITY: $24,852 A YEAR', BOLD(44), 247, white, 255, x=960); fr = P2(fr, C, (180, 200, 1740, 350), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.line([965, 335, 965, 400], fill=goldL + (255,), width=6); txt(C, 'HALF', BOLD(48), 410, goldL, 255, x=965); fr = P2(fr, C, (880, 330, 1050, 470), t, T[1])
    fr = eq(fr, t, 500, [('c', 'SOCIAL SECURITY', '$24,852', 'A YEAR', blue), ('o', '÷'), ('c', 'HALF', '2', None, gold), ('o', '='), ('c', 'THE I R S COUNTS', '$12,426', 'A YEAR', green)], [T[2], T[3], T[4]], 250, 420, 150)
    return frame(pill_last(fr, t, 'THE I R S COUNTS $12,426 OF IT', 810, green, navy, 50))

def s18c(t):
    fr = stage(t, 'FRANK\'S COMBINED INCOME', 80); T = sp(4)
    fr = eq(fr, t, 215, [('c', 'HIS WITHDRAWALS', '$19,500', None, gold), ('o', '+'), ('c', 'HALF HIS SS', '$12,426', None, blue), ('o', '='), ('c', 'COMBINED INCOME', '$31,926', None, green)], [T[0], T[1], T[2]], 210, 420, 150)
    if t > T[3]:
        C = new(); d = ImageDraw.Draw(C); x0, x1, y = 260, 1660, 640; u = lambda v: x0 + (x1 - x0) * v / 45000.0
        d.rounded_rectangle([u(0), y, u(25000), y + 60], radius=10, fill=A((70, 110, 90), 255)); d.rectangle([u(25000), y, u(34000), y + 60], fill=A(gold, 255)); d.rounded_rectangle([u(34000), y, u(45000), y + 60], radius=10, fill=A(red, 255))
        txt(C, '0%', BOLD(34), y + 12, white, 255, x=(u(0) + u(25000)) / 2); txt(C, 'UP TO 50%', BOLD(34), y + 12, navy, 255, x=(u(25000) + u(34000)) / 2); txt(C, 'UP TO 85%', BOLD(34), y + 12, white, 255, x=(u(34000) + u(45000)) / 2)
        for v, lab in ((25000, '$25,000'), (34000, '$34,000')): txt(C, lab, BOLD(32), y + 72, grey, 255, x=u(v))
        d.polygon([(u(31926), y - 6), (u(31926) - 24, y - 50), (u(31926) + 24, y - 50)], fill=A(white, 255)); txt(C, 'FRANK  $31,926', BOLD(40), y - 100, goldL, 255, x=u(31926))
        fr = P2(fr, C, (240, y - 120, 1700, y + 130), t, T[3])
    return frame(pill_last(fr, t, 'INSIDE THE 50% ZONE', 815, gold, navy, 50))

# ======================= BLOCCO 19 =======================
def s19a(t):
    fr = stage(t, "PART OF FRANK'S SOCIAL SECURITY BECOMES TAXABLE", 81, 50); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([200, 300, 1720, 430], radius=36, fill=card + (255,), outline=blue + (255,), width=5)
        w = 1500 * 3463 / 24852.0
        d.rounded_rectangle([210, 310, 1710 - w - 6, 420], radius=28, fill=A((90, 130, 190), 255))
        txt(C, 'SOCIAL SECURITY: $24,852 A YEAR', BOLD(44), 340, white, 255, x=(210 + 1710 - w) / 2); fr = P2(fr, C, (180, 280, 1740, 450), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); w = 1500 * 3463 / 24852.0
        d.rounded_rectangle([1710 - w, 310, 1710, 420], radius=28, fill=A(red, 255)); fr = P2(fr, C, (1400, 290, 1730, 440), t, T[1])
        L = new(); txt(L, '$3,463', BOLD(60), 460, red, 255 * E_(t, T[1]), x=1555); txt(L, 'TAXABLE', BOLD(40), 525, white, 255 * E_(t, T[1]), x=1555); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        v = 3463 * ease((t - T[2]) / 0.9)
        C = new(); card_(C, 500, 580, 1420, 760, red, 'ABOUT THIS MUCH OF HIS SOCIAL SECURITY', '$' + f'{int(v):,}', None, 100, white); fr = P2(fr, C, (480, 560, 1440, 780), t, T[2])
    return frame(fr if t < T[3] else chip_src(fr, 'COMBINED INCOME $31,926 - $25,000, TIMES 50%', 880, t, T[3]))

def s19b(t):
    fr = stage(t, 'HIS TAXABLE INCOME', 82); T = sp(4)
    fr = eq(fr, t, 260, [('c', 'HIS WITHDRAWALS', '$19,500', None, gold), ('o', '+'), ('c', 'TAXABLE SS', '$3,463', None, red), ('o', '='), ('c', 'TAXABLE INCOME', '$22,963', None, green)], [T[0], T[1], T[2]], 250, 420, 150)
    return frame(pill_last(fr, t, 'HIS TAXABLE INCOME: $22,963', 640, green, navy, 56))

def s19c(t):
    fr = stage(t, 'NOW COMPARE IT WITH THE STANDARD DEDUCTION', 83, 54); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 200, 280, 840, 640, green, "FRANK'S TAXABLE INCOME", '$22,963', 'COMPARE WITH...', 130, white); fr = P2(fr, C, (180, 260, 860, 660), t, T[0])
    if t > T[1]:
        L = new(); txt(L, 'VS', BOLD(110), 410, goldL, 255 * E_(t, T[1]), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1080, 280, 1720, 640, gold, 'THE STANDARD DEDUCTION', '$ ?', 'FOR A SINGLE PERSON 65+', 150, goldL); fr = P2(fr, C, (1060, 260, 1740, 660), t, T[1])
    return frame(fr)

def s19d(t):
    fr = stage(t, 'THE 2026 STANDARD DEDUCTION', 84); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 500, 240, 1420, 520, gold, 'SINGLE, AGE 65 OR OLDER, 2026', '$18,150', None, 190, goldL); fr = P2(fr, C, (480, 220, 1440, 540), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 380, 580, 940, 770, blue, None, '$16,100', 'BASE DEDUCTION', 70, white); fr = P2(fr, C, (360, 560, 960, 790), t, T[1])
    if t > T[2]:
        L = new(); txt(L, '+', BOLD(110), 600, goldL, 255 * E_(t, T[2]), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 980, 580, 1540, 770, green, None, '$2,050', 'EXTRA FOR AGE 65+', 70, white); fr = P2(fr, C, (960, 560, 1560, 790), t, T[2])
    fr = chip_src(fr, 'SOURCE: IRS, TAX FOUNDATION 2026', 820, t, T[3]) if t > T[3] else fr
    return frame(pill_last(fr, t, 'STANDARD DEDUCTION: $18,150', 920, gold, navy, 40))

# ======================= BLOCCO 20 =======================
def s20a(t):
    fr = stage(t, 'AN EXTRA SENIOR DEDUCTION', 85); T = sp(4)
    if t > T[0]:
        C = new(); cal_card(C, 140, 270, 560, 640, '2025 TO', '2028', 130, blue); fr = P2(fr, C, (120, 250, 580, 660), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 700, 270, 1500, 640, gold, 'AN EXTRA DEDUCTION, UP TO', '$6,000', 'FOR EACH PERSON 65+', 200, goldL); fr = P2(fr, C, (680, 250, 1520, 660), t, T[1])
        L = new(); arrow_r(L, 580, 690, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); avatar(C, 1680, 480, goldL, 2.3); txt(C, '65+', BOLD(60), 580, white, 255, x=1680); fr = P2(fr, C, (1590, 340, 1780, 660), t, T[2])
    return frame(pill_last(fr, t, 'A TEMPORARY SENIOR DEDUCTION: UP TO $6,000', 790, gold, navy, 48))

def s20b(t):
    fr = stage(t, 'ALL TOGETHER', 86); T = sp(4)
    fr = eq(fr, t, 260, [('c', 'STANDARD DEDUCTION', '$18,150', '2026, SINGLE 65+', blue), ('o', '+'), ('c', 'SENIOR DEDUCTION', '$6,000', 'UP TO', green), ('o', '='), ('c', 'TOTAL', '$24,150', None, gold)], [T[0], T[1], T[2]], 250, 420, 150)
    return frame(pill_last(fr, t, 'TOGETHER: $24,150', 640, gold, navy, 56))

def s20c(t):
    fr = stage(t, 'INCOME VS DEDUCTION', 87); T = sp(4)
    fr = bars3(fr, t, 690, [("FRANK'S TAXABLE INCOME", '$22,963', 0.95, green, white), ('TOTAL DEDUCTIONS', '$24,150', 1.0, gold, goldL)], [T[0], T[1]], 440, 340, 220)
    if t > T[2]:
        C = new(); check(C, 960, 330, 80, green); fr = P2(fr, C, (840, 230, 1080, 430), t, T[2])
    return frame(pill_last(fr, t, '$22,963 IS BELOW $24,150', 800, green, navy, 56))

SLIDES = {16: [s16a, s16b, s16c], 17: [s17a, s17b, s17c, s17d], 18: [s18a, s18b, s18c], 19: [s19a, s19b, s19c, s19d], 20: [s20a, s20b, s20c]}

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
