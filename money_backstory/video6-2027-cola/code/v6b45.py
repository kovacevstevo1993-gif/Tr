from v3lib import *
from v3b3_10 import POP, new, lerp
from v4b11_20 import calculator
from v4b2_10 import cal_card
from v5b1 import amb, sparks, shake
from v5lib import paycheck, arrow_r, arrow_d, magnifier
from v6b1 import A_, E_, chip_src
from v6b2 import chip
from v6b3 import badge
import sys, math

def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':'))
class Blk:
    def __init__(s, S, groups, tot):
        s.S = S; s.G = groups; s.tot = tot
        gw = [sum(len(S[i]) + 10 for i in g) for g in groups]
        fs = [round(w / sum(gw) * tot) for w in gw]; fs[-1] = tot - sum(fs[:-1]); s.FS = fs
        s.TXT = [' '.join(S[i] for i in g) for g in groups]
    def tt(s, g, marker):
        x = s.TXT[g]; i = x.index(marker)
        return max(0.2, wtot(x[:i]) / wtot(x) * s.FS[g] / 30 - 0.1)

def head(fr, text, t, size=62): return title_layer(fr, text, t, size=size)

# ================= BLOCCO 4 (773 fotogrammi) =================
B4 = Blk(["Number one: what Cola is.", "Cola is short for cost of living adjustment.",
          "It is the yearly raise that keeps Social Security checks from losing value as prices go up.",
          "It has been automatic since nineteen seventy five, which means nobody votes on it.",
          "The number comes from a formula, and that formula uses one inflation measure, the Consumer Price Index for Wage Earners, known as C P I W."],
         [[0, 1], [2], [3], [4]], 773)

def d4a(t):
    fr = base(t); fr = amb(fr, t, 21, 6, 50); fr = head(fr, 'NUMBER ONE: WHAT COLA IS', t, 60)
    T = lambda m: B4.tt(0, m)
    if t > 0.3:
        C = new(); badge(C, 330, 420, 1, gold, 70); txt(C, 'COLA', BOLD(200), 330, goldL, 255, x=960)
        fr = A_(fr, C, (240, 300, 1700, 600), t, 0.3)
    t2 = T('Cola is short')
    words = [('C', 'OST'), ('O', 'F'), ('L', 'IVING'), ('A', 'DJUSTMENT')]
    ws = [190 + 34 * len(b_) for (_, b_) in words]; gap = 50; x_ = (1920 - (sum(ws) + gap * 3)) / 2; xs = []
    for w_ in ws: xs.append(x_ + w_ / 2); x_ += w_ + gap
    for k, (a, b) in enumerate(words):
        t0 = t2 + 0.2 + 0.45 * k
        if t > t0:
            C = new(); d = ImageDraw.Draw(C); w = 190 + 34 * len(b)
            cx = xs[k]
            d.rounded_rectangle([cx - w / 2, 640, cx + w / 2, 800], radius=26, fill=card + (255,), outline=gold + (255,), width=5)
            f1 = BOLD(110); f2 = BOLD(60); b1 = d.textbbox((0, 0), a, font=f1); b2 = d.textbbox((0, 0), b, font=f2)
            tw = (b1[2] - b1[0]) + (b2[2] - b2[0]) + 4; x0 = cx - tw / 2
            d.text((x0 - b1[0], 660 - b1[1]), a, font=f1, fill=gold + (255,))
            d.text((x0 + (b1[2] - b1[0]) + 4 - b2[0], 660 + 110 * 0.72 - b2[3]), b, font=f2, fill=white + (255,))
            fr = A_(fr, C, (cx - w / 2 - 15, 625, cx + w / 2 + 15, 815), t, t0, 0.5)
    if t > t2 + 2.0: fr = pill_pop(fr, 'COST OF LIVING ADJUSTMENT', 860, t, t2 + 2.0, goldL, tcol=navy, size=50, cx=960)
    return frame(fr)

def d4b(t):
    fr = base(t); fr = amb(fr, t, 22, 6, 50); fr = head(fr, 'THE YEARLY RAISE', t, 62)
    T = lambda m: B4.tt(0, m)
    # note: group index 1 (S2)
    Tb = lambda m: B4.tt(1, m)
    if t > 0.3:
        C = new(); card_box(C, 130, 280, 900, 760, outline=red, fill=card)
        cart(C, 380, 520, 1.7, 255, gold)
        txt(C, 'PRICES GO UP', BOLD(62), 330, red, 255, x=515)
        up_arrow(C, 720, 520, 1.0, red)
        for k, (p, y) in enumerate([('$100', 650), ('$103', 700)]):
            pass
        txt(C, '$100  >  $103', BOLD(60), 660, white, 255, x=515)
        fr = A_(fr, C, (110, 260, 920, 780), t, 0.3)
    tr = Tb('keeps')
    if t > tr:
        C = new(); paycheck(C, 1010, 300, 1790, 650, green, '$2,071', 'KEEPS ITS VALUE', 'SOCIAL SECURITY CHECK', 130)
        shield = ImageDraw.Draw(C); shield.polygon([(1720, 250), (1780, 270), (1780, 320), (1720, 360), (1660, 320), (1660, 270)], fill=green + (255,))
        shield.line([1690, 305, 1715, 330, 1752, 285], fill=(255, 255, 255, 255), width=10)
        fr = A_(fr, C, (990, 230, 1810, 680), t, tr)
        L = new(); arrow_r(L, 910, 1000, 470, goldL, 255 * E_(t, tr)); fr = Image.alpha_composite(fr, L)
    if t > Tb('prices go up') - 0.2:
        fr = pill_pop(fr, 'THE RAISE KEEPS UP WITH PRICES', 820, t, Tb('prices go up') - 0.2, green, tcol=navy, size=50, cx=960)
    return frame(fr)

def d4c(t):
    fr = base(t); fr = amb(fr, t, 23, 6, 50); fr = head(fr, 'AUTOMATIC SINCE 1975', t, 62)
    Tc = lambda m: B4.tt(2, m)
    if t > 0.3:
        C = new(); cal_card(C, 140, 300, 640, 700, 'SINCE', '1975', bigsize=150, headcol=gold)
        fr = A_(fr, C, (120, 280, 660, 720), t, 0.3)
    ta = Tc('which means')
    L = new(); arrow_r(L, 690, 800, 500, goldL, 255 * E_(t, 0.8)); fr = Image.alpha_composite(fr, L)
    if t > 0.8:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([830, 330, 1170, 680], radius=30, fill=card + (255,), outline=goldL + (255,), width=6)
        txt(C, 'AUTOMATIC', BOLD(52), 400, goldL, 255, x=1000); txt(C, 'EVERY YEAR', BOLD(52), 470, white, 255, x=1000)
        clock(C, 1000, 600, 55, t * 1.2)
        fr = A_(fr, C, (810, 310, 1190, 700), t, 0.8)
    if t > ta:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([1280, 330, 1780, 680], radius=30, fill=card + (255,), outline=red + (255,), width=6)
        d.rectangle([1430, 420, 1630, 560], fill=(236, 240, 245, 255), outline=goldL + (255,), width=5)
        d.rectangle([1500, 396, 1560, 424], fill=goldL + (255,))
        txt(C, 'VOTE', BOLD(54), 470, navy, 255, x=1530)
        cross(C, 1620, 420, 44, red)
        txt(C, 'NOBODY VOTES', BOLD(52), 590, red, 255, x=1530)
        fr = A_(fr, C, (1260, 310, 1800, 700), t, ta)
    fr = chip_src(fr, 'SOURCE: SSA.GOV', 900, t, 1.5)
    return frame(fr)

def d4d(t):
    fr = base(t); fr = amb(fr, t, 24, 6, 50); fr = head(fr, 'THE FORMULA USES ONE MEASURE', t, 58)
    Td = lambda m: B4.tt(3, m)
    if t > 0.3:
        C = new(); calculator(C, 270, 480, 1.45); txt(C, 'FORMULA', BOLD(60), 690, goldL, 255, x=270)
        fr = A_(fr, C, (110, 290, 440, 760), t, 0.3)
    t2 = Td('one inflation')
    L = new(); arrow_r(L, 460, 600, 480, goldL, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([640, 300, 1280, 700], radius=34, fill=card + (255,), outline=blue + (255,), width=7)
        txt(C, 'C P I - W', BOLD(130), 340, blue, 255, x=960)
        txt(C, 'CONSUMER PRICE INDEX', BOLD(44), 500, white, 255, x=960); txt(C, 'FOR WAGE EARNERS', BOLD(44), 556, white, 255, x=960)
        txt(C, 'ONE INFLATION MEASURE', BOLD(40), 630, goldL, 255, x=960)
        fr = A_(fr, C, (620, 280, 1300, 720), t, t2)
    t3 = Td('known as')
    L = new(); arrow_r(L, 1320, 1450, 480, goldL, 255 * E_(t, t3)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); d = ImageDraw.Draw(C)
        d.ellipse([1480, 340, 1800, 660], fill=gold + (255,), outline=goldL + (255,), width=8)
        txt(C, '%', BOLD(190), 380, navy, 255, x=1640); txt(C, 'RAISE', BOLD(54), 585, navy, 255, x=1640)
        fr = A_(fr, C, (1460, 320, 1820, 680), t, t3)
    fr = chip_src(fr, 'CPI-W: BUREAU OF LABOR STATISTICS (BLS.GOV)', 880, t, t2 + 0.8)
    return frame(fr)

# ================= BLOCCO 5 (853 fotogrammi) =================
B5 = Blk(["Here is how the formula works.", "The Bureau of Labor Statistics measures prices every month.",
          "Social Security takes only three of those months, July, August and September, and averages them.",
          "Then it compares that average with the same three months of the year before.",
          "If prices went up, the percentage increase, rounded to the nearest tenth of one percent, becomes your raise.",
          "That is why the number can only be announced after the September prices come out."],
         [[0, 1], [2], [3], [4], [5]], 853)
MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

def months(fr, t, y, t0, hl=(), dim=False, step=0.06, size=62, hlt=None):
    for i, m in enumerate(MONTHS):
        a0 = t0 + i * step
        if t < a0: continue
        C = new(); d = ImageDraw.Draw(C); x = 190 + i * 128; on = i in hl
        hot = on and (hlt is None or t > hlt[hl.index(i)])
        fillc = gold if hot else card; ol = goldL if hot else (80, 100, 130)
        al = 255 if (hot or not dim) else 120
        d.rounded_rectangle([x, y, x + 116, y + 150], radius=18, fill=fillc + (al,), outline=ol + (al,), width=4)
        txt(C, m, BOLD(40), y + 20, navy if hot else (200, 210, 225), al, x=x + 58)
        txt(C, str(i + 1), BOLD(64), y + 70, navy if hot else (200, 210, 225), al, x=x + 58)
        fr = A_(fr, C, (x - 10, y - 10, x + 126, y + 160), t, a0, 0.4)
    return fr

def d5a(t):
    fr = base(t); fr = amb(fr, t, 31, 6, 50); fr = head(fr, 'HOW THE FORMULA WORKS', t, 62)
    T = lambda m: B5.tt(0, m)
    if t > T('The Bureau') - 0.2:
        C = new(); building(C, 420, 400, 280, 230, gold)
        txt(C, 'BUREAU OF', BOLD(50), 540, white, 255, x=420); txt(C, 'LABOR STATISTICS', BOLD(50), 600, white, 255, x=420)
        fr = A_(fr, C, (120, 250, 760, 680), t, T('The Bureau') - 0.2)
    t2 = T('measures prices')
    if t > t2:
        C = new(); cart(C, 1230, 400, 1.4, 255, gold); magnifier(C, 1450, 350, 70)
        txt(C, 'MEASURES PRICES', BOLD(54), 560, goldL, 255, x=1330)
        fr = A_(fr, C, (1000, 220, 1700, 640), t, t2)
    t3 = T('every month')
    fr = months(fr, t, 700, t3, step=0.1)
    if t > t3 + 1.4: fr = pill_pop(fr, 'EVERY SINGLE MONTH', 890, t, t3 + 1.4, goldL, tcol=navy, size=46, cx=960)
    return frame(fr)

def d5b(t):
    fr = base(t); fr = amb(fr, t, 32, 6, 50); fr = head(fr, 'ONLY THREE MONTHS COUNT', t, 62)
    T = lambda m: B5.tt(1, m)
    ts = [T('July') - 0.1, T('August') - 0.1, T('September') - 0.1]
    fr = months(fr, t, 340, 0.2, hl=(6, 7, 8), dim=True, step=0.04, hlt=ts)
    if t > ts[2] + 0.3:
        C = new(); d = ImageDraw.Draw(C)
        d.polygon([(190 + 6 * 128 + 58, 520), (190 + 8 * 128 + 58, 520), (190 + 7 * 128 + 58, 580)], fill=gold + (255,))
        d.line([190 + 6 * 128 + 58, 520, 190 + 8 * 128 + 58, 520], fill=gold + (255,), width=8)
        fr = A_(fr, C, (400, 500, 1200, 600), t, ts[2] + 0.3)
    t4 = T('averages them')
    if t > t4:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([560, 620, 1360, 840], radius=34, fill=card + (255,), outline=gold + (255,), width=7)
        txt(C, 'JUL + AUG + SEP', BOLD(56), 650, white, 255, x=960); txt(C, '= THE AVERAGE', BOLD(80), 725, goldL, 255, x=960)
        fr = A_(fr, C, (540, 600, 1380, 860), t, t4)
    return frame(fr)

def d5c(t):
    fr = base(t); fr = amb(fr, t, 33, 6, 50); fr = head(fr, 'THIS YEAR VS LAST YEAR', t, 62)
    T = lambda m: B5.tt(2, m)
    if t > 0.3:
        C = new(); card_box(C, 140, 270, 880, 760, outline=gold, fill=card)
        txt(C, 'THIS YEAR', BOLD(60), 300, goldL, 255, x=510); txt(C, 'JUL  AUG  SEP', BOLD(54), 380, white, 255, x=510)
        for k, h_ in enumerate([250, 260, 275]): C.alpha_composite(bar(h_, gold, 120), (310 + k * 150, 750 - h_))
        fr = A_(fr, C, (120, 250, 900, 780), t, 0.3)
    t2 = T('the same three months')
    if t > t2:
        C = new(); card_box(C, 1040, 270, 1780, 760, outline=blue, fill=card)
        txt(C, 'LAST YEAR', BOLD(60), 300, blue, 255, x=1410); txt(C, 'JUL  AUG  SEP', BOLD(54), 380, white, 255, x=1410)
        for k, h_ in enumerate([225, 235, 245]): C.alpha_composite(bar(h_, blue, 120), (1210 + k * 150, 750 - h_))
        fr = A_(fr, C, (1020, 250, 1800, 780), t, t2)
        L = new(); txt(L, 'VS', BOLD(84), 480, goldL, 255 * E_(t, t2 + 0.2), x=960); fr = Image.alpha_composite(fr, L)
    if t > t2 + 0.6: fr = pill_pop(fr, 'COMPARE THE TWO AVERAGES', 850, t, t2 + 0.6, goldL, tcol=navy, size=50, cx=960)
    return frame(fr)

def d5d(t):
    fr = base(t); fr = amb(fr, t, 34, 6, 50); fr = head(fr, 'FROM PRICES TO YOUR RAISE', t, 60)
    T = lambda m: B5.tt(3, m)
    if t > 0.3:
        C = new(); up_arrow(C, 250, 470, 1.5, red); txt(C, 'PRICES', BOLD(56), 640, red, 255, x=260); txt(C, 'WENT UP', BOLD(56), 700, red, 255, x=260)
        fr = A_(fr, C, (40, 330, 580, 780), t, 0.3)
    t2 = T('the percentage increase')
    L = new(); arrow_r(L, 580, 690, 480, goldL, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([710, 320, 1130, 640], radius=30, fill=card + (255,), outline=goldL + (255,), width=6)
        txt(C, '2.76%', BOLD(130), 380, white, 255, x=920); txt(C, 'EXAMPLE', BOLD(40), 540, grey, 255, x=920)
        fr = A_(fr, C, (690, 300, 1150, 660), t, t2)
    t3 = T('rounded to')
    L = new(); arrow_r(L, 1150, 1260, 480, goldL, 255 * E_(t, t3)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); d = ImageDraw.Draw(C)
        d.ellipse([1280, 330, 1600, 650], fill=gold + (255,), outline=goldL + (255,), width=8)
        txt(C, '2.8%', BOLD(120), 420, navy, 255, x=1440); txt(C, 'RAISE', BOLD(50), 560, navy, 255, x=1440)
        fr = A_(fr, C, (1260, 310, 1620, 670), t, t3)
        fr = pill_pop(fr, 'ROUNDED TO THE NEAREST TENTH', 740, t, t3 + 0.3, goldL, tcol=navy, size=44, cx=1200)
    return frame(fr)

def d5e(t):
    fr = base(t); fr = amb(fr, t, 35, 6, 50); fr = head(fr, 'WHY THE WAIT?', t, 64)
    T = lambda m: B5.tt(4, m)
    fr = months(fr, t, 300, 0.2, hl=(8,), dim=True, step=0.04, hlt=[T('September') - 0.2])
    t2 = T('prices come out')
    fr = chip(fr, 'WAIT FOR SEPTEMBER PRICES', 560, 600, t, 0.9, goldL, 46)
    fr = chip(fr, 'THEN THE RAISE IS ANNOUNCED', 560, 720, t, t2 - 0.3, red, 46, fillc=red, tcol=(255, 255, 255))
    if t > t2 - 0.3:
        C = new(); cal_card(C, 1040, 580, 1540, 900, 'ANNOUNCED', '14', bigsize=130, headcol=red)
        txt(C, 'OCTOBER', BOLD(52), 825, (70, 84, 108), 255, x=1290)
        fr = A_(fr, C, (1020, 560, 1560, 920), t, t2 - 0.3)
        L = new(); arrow_d(L, 1272, 470, 560, gold, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    return frame(fr)

FNS = {4: [d4a, d4b, d4c, d4d], 5: [d5a, d5b, d5c, d5d, d5e]}
BLK = {4: B4, 5: B5}
if __name__ == '__main__':
    mode = sys.argv[1]; b = int(sys.argv[2]); fns = FNS[b]; FS = BLK[b].FS
    sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, len(fns) + 1))
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.25, 0.6, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}pv{b}_{i}_{int(fq*100)}.png')
        print(FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b{b}-0{i}.mp4'); print('done', b, i, f, flush=True)
