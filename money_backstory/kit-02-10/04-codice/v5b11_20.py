from v5lib import *
import re, sys
sys.path.insert(0, '/home/claude/v5')
from blocks import B as BLK

def count(t, t0, dur, v): return v * ease((t - t0) / dur)
def sents(n): return re.split(r'(?<=[.?!]) ', BLK[n - 1])

class Bk(Blk):
    def T(s, g, m, off=0.0):
        try: return s.tt(g, m) + off
        except ValueError: print('MISSING marker', s.n, g, m); return 0.5

def mk(n, groups): return Bk(n, sents(n), groups)

def ring(C, cx, cy, r, frac, col, w=44, alpha=255):
    d = ImageDraw.Draw(C)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=A((60, 82, 124), alpha), width=w)
    if frac > 0.004: d.arc([cx - r, cy - r, cx + r, cy + r], -90, -90 + 360 * frac, fill=A(col, alpha), width=w)

def mcard(C, x0, y0, x1, y1, col, head, val, size=90, vcol=white, sub=None):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=A(card, 255), outline=A(col, 255), width=5)
    cx = (x0 + x1) / 2
    txt(C, head, BOLD(40), y0 + 20, col, 255, x=cx)
    txt(C, val, BOLD(size), y0 + 82, vcol, 255, x=cx)
    if sub: txt(C, sub, BOLD(38), y1 - 62, grey, 255, x=cx)

def bar(C, x, base_y, w, h, col, alpha=255):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([x, base_y - h, x + w, base_y], radius=14, fill=A(col, alpha), outline=A(goldL, min(alpha, 120)), width=3)
    d.rounded_rectangle([x + 10, base_y - h + 8, x + w - 10, base_y - h + 20], radius=6, fill=A((255, 255, 255), min(alpha, 60)))

def lay(fr, fn, box, t, t0, d=0.9):
    C = new(); fn(C); return appear(fr, C, box, t, t0, d)

# ======================= BLOCK 11 =======================
B11 = mk(11, [[0, 1], [2], [3]])
BX0, BX1, BY0, BY1 = 420, 1820, 260, 350
SEG = BX0 + (BX1 - BX0) * 1286 / 6000

def bar11(C, hl):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([BX0, BY0, BX1, BY1], radius=18, fill=A(card, 255), outline=A(grey, 255), width=3)
    if hl == 1: d.rounded_rectangle([BX0, BY0, SEG, BY1], radius=18, fill=A(gold, 255), outline=A(goldL, 255), width=4)
    else:
        d.rounded_rectangle([BX0, BY0, SEG, BY1], radius=18, fill=A((110, 90, 40), 255), outline=A(goldL, 255), width=3)
        d.rounded_rectangle([SEG + 4, BY0, BX1, BY1], radius=18, fill=A(blue, 255), outline=A((190, 215, 255), 255), width=4)
    txt(C, '$6,000 A MONTH', BOLD(40), BY0 - 60, white, 255, x=(BX0 + BX1) / 2)

def b11a(t):
    T = lambda m: B11.T(0, m)
    fr = base(t); fr = title(fr, "MARY'S $6,000 THROUGH THE FORMULA", t, 54)
    C = new(); person(C, 230, 520, green, 2.8); txt(C, 'MARY', BOLD(56), 695, green, 255, x=230); fr = appear(fr, C, (90, 300, 380, 740), t, 0.3, 0.9)
    fr = lay(fr, lambda C: bar11(C, 1), (BX0 - 10, BY0 - 70, BX1 + 10, BY1 + 10), t, 0.8, 1.0)
    fr = label(fr, 'FIRST $1,286', 380, 46, goldL, t, T('Ninety percent') - 0.4, BX0 + (SEG - BX0) / 2 + 60)
    tn = T('Ninety percent')
    fr = label(fr, '90%', 470, 190, goldL, t, tn, 1120)
    fr = label(fr, 'OF THE FIRST $1,286', 690, 64, white, t, tn + 0.5, 1120)
    L = new(); txt(L, money(count(t, tn + 1.5, 2.5, 1157.40), True), BOLD(150), 790, goldL, 255 * E(t, tn + 1.4, 0.7), x=1120); fr = Image.alpha_composite(fr, L)
    fr = lay(fr, lambda C: coin_stack(C, 1700, 900, 7, 70), (1600, 700, 1800, 940), t, tn + 1.5, 1.0)
    return frame(fr)

def b11b(t):
    T = lambda m: B11.T(1, m)
    fr = base(t); fr = title(fr, 'THE SECOND SLICE', t)
    C = new(); person(C, 230, 520, green, 2.8); txt(C, 'MARY', BOLD(56), 695, green, 255, x=230); fr = appear(fr, C, (90, 300, 380, 740), t, 0.0, 0.5)
    fr = lay(fr, lambda C: bar11(C, 2), (BX0 - 10, BY0 - 70, BX1 + 10, BY1 + 10), t, 0.0, 0.5)
    fr = label(fr, 'REMAINING $4,714', 380, 46, (190, 215, 255), t, 0.6, SEG + (BX1 - SEG) / 2)
    tn = T('thirty two percent')
    fr = label(fr, '32%', 470, 190, blue, t, tn, 1120)
    fr = label(fr, 'OF THE REMAINING $4,714', 690, 64, white, t, tn + 0.5, 1120)
    L = new(); txt(L, money(count(t, tn + 1.5, 2.5, 1508.48), True), BOLD(150), 790, blue, 255 * E(t, tn + 1.4, 0.7), x=1120); fr = Image.alpha_composite(fr, L)
    fr = lay(fr, lambda C: coin_stack(C, 1700, 900, 9, 70), (1600, 660, 1800, 940), t, tn + 1.5, 1.0)
    fr = chip(fr, 'FIRST SLICE: $1,157.40', 330, 880, t, 0.8, goldL, 34)
    return frame(fr)

def b11c(t):
    T = lambda m: B11.T(2, m)
    fr = base(t); fr = title(fr, 'ADD THEM TOGETHER', t)
    fr = lay(fr, lambda C: mcard(C, 190, 200, 890, 400, gold, 'FIRST SLICE', '$1,157.40', 100, goldL), (180, 190, 900, 410), t, 0.3)
    fr = label(fr, '+', 240, 130, white, t, 1.0, 960)
    fr = lay(fr, lambda C: mcard(C, 1030, 200, 1730, 400, blue, 'SECOND SLICE', '$1,508.48', 100, (190, 215, 255)), (1020, 190, 1740, 410), t, 0.7)
    ta = T('Add them together'); tr = T('round down')
    fr = label(fr, '=', 420, 100, goldL, t, ta, 960)
    v = 2665.88 if t < tr + 0.3 else 2665.80
    C = new(); paycheck(C, 520, 540, 1400, 940, green, money(v, True) if t > ta + 0.4 else '', sub='PER MONTH', head='MARY: MONTHLY CHECK', size=140)
    fr = appear(fr, C, (510, 530, 1410, 950), t, ta + 0.3, 1.0)
    fr = chip(fr, 'ROUND DOWN', 1650, 560, t, tr, gold, 46)
    fr = lay(fr, lambda C: money_bag(C, 1650, 800, 1.0), (1530, 670, 1770, 930), t, ta + 1.2, 1.0)
    fr = lay(fr, lambda C: coin_stack(C, 260, 920, 8, 66), (170, 700, 350, 950), t, ta + 1.6, 1.0)
    return frame(fr)

# ======================= BLOCK 12 =======================
B12 = mk(12, [[0, 1], [2], [3], [4, 5]])

def b12a(t):
    T = lambda m: B12.T(0, m)
    fr = base(t); fr = title(fr, 'WHAT THE FORMULA DOES', t)
    fr = label(fr, 'NOTICE WHAT IT DOES', 230, 64, white, t, 0.5)
    ti = T('It is built')
    fr = label(fr, 'IT HELPS LOWER EARNERS MORE', 330, 72, goldL, t, ti)
    C = new(); person(C, 400, 640, blue, 3.3); coin_stack(C, 690, 800, 4, 62); txt(C, 'LOWER EARNER', BOLD(52), 850, blue, 255, x=480)
    fr = appear(fr, C, (250, 440, 800, 920), t, ti + 0.6, 1.0)
    C = new(); person(C, 1250, 640, purple, 3.3); coin_stack(C, 1550, 800, 10, 62); txt(C, 'HIGHER EARNER', BOLD(52), 850, purple, 255, x=1380)
    fr = appear(fr, C, (1100, 400, 1680, 920), t, ti + 1.6, 1.0)
    fr = lay(fr, lambda C: (up_arrow(C, 960, 620, 1.7, green), txt(C, 'HELPED MORE', BOLD(46), 780, green, 255, x=960)), (760, 480, 1160, 830), t, ti + 1.2, 0.9)
    return frame(fr)

def b12ring(t, g, who, col, amt, pct, extra, marker):
    T = lambda m: B12.T(g, m)
    fr = base(t); fr = title(fr, 'HOW MUCH COMES BACK', t)
    tm = T(marker)
    C = new(); person(C, 300, 560, col, 2.8); txt(C, who, BOLD(54), 730, col, 255, x=300); fr = appear(fr, C, (140, 340, 470, 780), t, 0.3, 0.9)
    fr = label(fr, 'AVERAGING ' + amt + ' A MONTH', 210, 62, white, t, 0.6, 1100)
    fr = lay(fr, lambda C: ring(C, 1100, 570, 230, 0, col), (850, 320, 1350, 820), t, 0.6, 0.8)
    frac = pct / 100 * ease((t - tm) / 2.4)
    C = new(); ring(C, 1100, 570, 230, frac, col); fr = Image.alpha_composite(fr, C) if t > tm else fr
    L = new(); txt(L, f'{int(round(frac * 100))}%', BOLD(150), 495, white, 255 * E(t, tm, 0.6), x=1100); fr = Image.alpha_composite(fr, L)
    fr = label(fr, extra, 860, 52, goldL, t, tm + 0.8, 1100)
    C = new(); wallet(C, 1650, 570, 1.3); fr = appear(fr, C, (1480, 470, 1820, 670), t, tm + 0.4, 0.9)
    return frame(fr)

def b12b(t): return b12ring(t, 1, 'SOMEONE', blue, '$3,000', 57, 'GETS BACK ABOUT 57%', 'gets back')
def b12c(t): return b12ring(t, 2, 'MARY', green, '$6,000', 44, 'GETS BACK ABOUT 44%', 'gets back')

def b12d(t):
    T = lambda m: B12.T(3, m)
    fr = base(t); fr = title(fr, 'THE MORE YOU EARN...', t)
    data = [(390, '$3,000', 57, blue, 0.4), (960, '$6,000', 44, green, 1.0), (1530, '$10,000', 36, purple, T('ten thousand') - 0.5)]
    for cx, amt, p, col, t0 in data:
        fr = label(fr, amt, 250, 62, white, t, t0, cx)
        C = new(); ring(C, cx, 520, 165, p / 100, col, 40); txt(C, f'{p}%', BOLD(100), 470, white, 255, x=cx); fr = appear(fr, C, (cx - 190, 330, cx + 190, 710), t, t0, 1.0)
    fr = label(fr, 'THE MORE YOU EARN,', 790, 66, white, t, T('The more you earn'))
    fr = label(fr, 'THE SMALLER THE SHARE', 880, 66, goldL, t, T('The more you earn') + 1.0)
    return frame(fr)

# ======================= BLOCK 13 =======================
B13 = mk(13, [[0, 1], [2], [3]])
CX0, CX1, CBASE, CPX = 260, 1660, 880, 3.0  # height px per $1000
def ceil_h(v): return v / 1000 * 2.4

def b13a(t):
    T = lambda m: B13.T(0, m)
    fr = base(t); fr = title(fr, 'THERE IS ALSO A CEILING', t)
    tc = T('In twenty twenty six')
    C = new(); d = ImageDraw.Draw(C)
    for k, v in enumerate([40, 70, 100, 140, 184.5]):
        bar(C, 320 + k * 190, CBASE, 130, ceil_h(v * 1000) * 0.85 * 1, gold if k < 4 else goldL)
    fr = appear(fr, C, (300, 300, 1300, 900), t, 0.6, 1.2)
    ly = CBASE - ceil_h(184500) * 0.85
    L = new(); d = ImageDraw.Draw(L)
    for x in range(260, 1400, 40): d.line([x, ly, x + 22, ly], fill=A(red, 255 * E(t, tc, 0.7)), width=8)
    fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'CEILING', 250, 66, red, t, tc, 1560)
    fr = label(fr, '$184,500', 330, 84, goldL, t, tc + 0.6, 1560)
    fr = label(fr, 'A YEAR IN 2026', 450, 46, white, t, tc + 1.0, 1560)
    C = new(); person(C, 1560, 780, purple, 2.0); fr = appear(fr, C, (1460, 640, 1660, 900), t, 1.0, 0.9)
    return frame(fr)

def b13b(t):
    T = lambda m: B13.T(1, m)
    fr = base(t); fr = title(fr, 'ABOVE THE CEILING', t)
    hh = ceil_h(300000) * 0.85; ch = ceil_h(184500) * 0.85
    C = new(); bar(C, 520, CBASE, 260, ch, gold); fr = appear(fr, C, (500, 300, 800, 900), t, 0.3, 1.0)
    ta = T('Anything above')
    C = new(); bar(C, 520, CBASE - ch, 260, hh - ch, (90, 100, 125), 200); fr = appear(fr, C, (500, 300, 800, CBASE - ch + 20), t, ta, 1.0)
    L = new(); ImageDraw.Draw(L).line([440, CBASE - ch, 1000, CBASE - ch], fill=A(red, 255), width=8); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'COUNTED', CBASE - ch / 2 - 30, 44, navy, t, 0.6, 650)
    fr = label(fr, 'NOT COUNTED', CBASE - ch - (hh - ch) / 2 - 30, 40, white, t, ta + 0.6, 650)
    fr = label(fr, 'ANYTHING ABOVE', 300, 64, white, t, ta, 1350); fr = label(fr, 'DOES NOT RAISE', 385, 64, white, t, ta + 0.5, 1350)
    fr = label(fr, 'YOUR BENEFIT', 470, 74, red, t, ta + 1.0, 1350)
    for k in range(3):
        C = new(); bill(C, 1200 + k * 150, 720, 220, 108, 0, 120, (110, 130, 120)); fr = appear(fr, C, (1080 + k * 150, 650, 1330 + k * 150, 790), t, ta + 0.8 + k * 0.3, 0.8)
    L = new(); cross(L, 1400, 720, 70, red, 255 * E(t, ta + 1.8, 0.6)); fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b13c(t):
    T = lambda m: B13.T(2, m)
    fr = base(t); fr = title(fr, 'THE MAXIMUM BENEFIT', t)
    tm = T('four thousand')
    fr = label(fr, 'EVEN THE HIGHEST EARNERS HIT A MAXIMUM', 220, 56, white, t, 0.4)
    C = new(); paycheck(C, 470, 340, 1450, 800, gold, money(count(t, tm, 2.0, 4152)) if t > tm - 0.3 else '$ ?', sub='PER MONTH', head='MAXIMUM AT FULL RETIREMENT AGE', size=170)
    fr = appear(fr, C, (460, 330, 1460, 810), t, 0.7, 1.0)
    C = new(); money_bag(C, 1660, 650, 1.1); fr = appear(fr, C, (1520, 490, 1800, 790), t, 1.5, 1.0)
    C = new(); coin_stack(C, 260, 800, 9, 68); fr = appear(fr, C, (170, 590, 350, 830), t, 1.8, 1.0)
    fr = chip(fr, 'AGE 67 · YEAR 2026', 960, 870, t, 2.5, goldL, 44)
    return frame(fr)

# ======================= BLOCK 14 =======================
B14 = mk(14, [[0, 1], [2], [3, 4, 5]])

def cal_icon(C, cx, cy, s, txt_, col=gold):
    d = ImageDraw.Draw(C); w = 150 * s
    d.rounded_rectangle([cx - w, cy - w * 0.9, cx + w, cy + w * 0.9], radius=int(26 * s), fill=A((236, 240, 245), 255), outline=A(col, 255), width=6)
    d.rounded_rectangle([cx - w, cy - w * 0.9, cx + w, cy - w * 0.4], radius=int(26 * s), fill=A(col, 255)); d.rectangle([cx - w, cy - w * 0.6, cx + w, cy - w * 0.4], fill=A(col, 255))
    for k in (-0.55, 0.55): d.rounded_rectangle([cx + k * w - 10 * s, cy - w * 1.05, cx + k * w + 10 * s, cy - w * 0.75], radius=6, fill=A(navy, 255))
    txt(C, txt_, BOLD(int(120 * s)), cy - w * 0.25, navy, 255, x=cx)

def b14a(t):
    T = lambda m: B14.T(0, m)
    fr = base(t); fr = title(fr, 'NUMBER THREE', t)
    C = new(); cal_icon(C, 560, 560, 1.7, '3'); fr = appear(fr, C, (280, 250, 840, 870), t, 0.4, 1.0)
    fr = label(fr, 'YOUR', 380, 90, white, t, 0.9, 1360); fr = label(fr, 'CLAIMING AGE', 500, 110, goldL, t, 1.4, 1360)
    te = T('Everything we just')
    C = new(); paycheck(C, 1080, 690, 1720, 930, green, '$2,665.80', sub='', head='FULL BENEFIT', size=86); fr = appear(fr, C, (1070, 680, 1730, 940), t, te, 1.0)
    return frame(fr)

def b14b(t):
    T = lambda m: B14.T(1, m)
    fr = base(t); fr = title(fr, 'FULL RETIREMENT AGE', t)
    fr = label(fr, 'BORN IN 1960 OR LATER', 240, 66, white, t, 0.5)
    tm = T('sixty seven')
    C = new(); cal_icon(C, 660, 620, 1.9, '67'); fr = appear(fr, C, (330, 260, 990, 960), t, 0.8, 1.0)
    fr = label(fr, 'FULL', 470, 96, white, t, 1.6, 1420); fr = label(fr, 'RETIREMENT AGE', 590, 96, goldL, t, 2.0, 1420)
    fr = chip(fr, '100% OF YOUR BENEFIT', 1420, 760, t, max(tm, 3.0), green, 48)
    return frame(fr)

def b14c(t):
    T = lambda m: B14.T(2, m)
    fr = base(t); fr = title(fr, 'EARLIER OR LATER', t)
    te = T('Claim earlier'); tl = T('Claim later'); tp = T('the change is')
    C = new(); mcard(C, 130, 400, 640, 700, red, 'CLAIM EARLIER', 'SMALLER', 80, red, 'THE CHECK SHRINKS'); fr = appear(fr, C, (120, 390, 650, 710), t, te, 1.0)
    fr = lay(fr, lambda C: arrow_d(C, 385, 250, 380, red), (300, 240, 470, 390), t, te + 0.4, 0.9)
    C = new(); mcard(C, 1280, 400, 1790, 700, green, 'CLAIM LATER', 'BIGGER', 80, green, 'THE CHECK GROWS'); fr = appear(fr, C, (1270, 390, 1800, 710), t, tl, 1.0)
    fr = lay(fr, lambda C: up_arrow(C, 1535, 320, 1.8, green), (1420, 200, 1650, 390), t, tl + 0.4, 0.9)
    C = new(); padlock(C, 960, 540, 1.9, goldL); fr = appear(fr, C, (830, 400, 1090, 700), t, tp, 1.0)
    fr = label(fr, 'THE CHANGE IS PERMANENT', 830, 76, goldL, t, tp + 0.6)
    return frame(fr)

# ======================= BLOCK 15 =======================
B15 = mk(15, [[0, 1, 2], [3, 4, 5], [6]])
AGES = [(62, 70, red), (63, 75, (235, 130, 70)), (64, 80, (235, 175, 70)), (65, 87, (215, 205, 80)), (66, 93, (150, 210, 90)), (67, 100, green)]

def draw_bars15(t, fr, starts, dim_first=0):
    for k, (age, p, col) in enumerate(AGES):
        st = starts[k]
        if t < st: continue
        e = ease((t - st) / 1.2); x = 200 + k * 270; hgt = p * 5.0
        C = new(); bar(C, x, 860, 200, hgt * e, col)
        L = C
        txt(L, f'{p}%', BOLD(70), 860 - hgt * e - 90, white, 255 * e, x=x + 100)
        txt(L, f'AGE {age}', BOLD(48), 880, goldL if age == 67 else white, 255, x=x + 100)
        fr = Image.alpha_composite(fr, L)
    return fr

def b15a(t):
    T = lambda m: B15.T(0, m)
    fr = base(t); fr = title(fr, 'CLAIMING EARLY', t)
    st = [T('At sixty two'), T('At sixty three'), T('At sixty four'), 99, 99, 99]
    fr = draw_bars15(t, fr, st)
    fr = label(fr, 'PERCENT OF YOUR FULL AMOUNT', 220, 52, grey, t, 0.5)
    return frame(fr)

def b15b(t):
    T = lambda m: B15.T(1, m)
    fr = base(t); fr = title(fr, 'CLAIMING EARLY', t)
    st = [0.0, 0.0, 0.0, T('At sixty five'), T('At sixty six'), T('And at sixty seven')]
    fr = draw_bars15(t, fr, st)
    fr = label(fr, 'PERCENT OF YOUR FULL AMOUNT', 220, 52, grey, t, 0.2)
    return frame(fr)

def b15c(t):
    T = lambda m: B15.T(2, m)
    fr = base(t); fr = title(fr, 'THE REDUCTION', t)
    tj = min(T('just over half'), 1.0); tl = max(T('a little less'), tj + 5.0)
    fr = label(fr, 'JUST OVER', 210, 60, white, t, tj, 960)
    fr = label(fr, '0.5%', 280, 170, red, t, tj + 0.3, 960)
    fr = label(fr, 'FOR EVERY MONTH YOU CLAIM EARLY', 490, 54, white, t, tj + 0.8)
    for k in range(36):
        st = tj + 2.0 + k * 0.07
        x = 200 + (k % 12) * 125; y = 690 + (k // 12) * 100
        C = new(); tile(C, x, y, 84, red, None, fill=(150, 50, 60), outline=(255, 150, 150)); txt(C, str(k + 1), BOLD(38), y + 18, white, 255, x=x + 42)
        fr = appear(fr, C, (x - 6, y - 6, x + 92, y + 98), t, st, 0.4)
    fr = label(fr, 'FIRST 3 YEARS', 590, 46, goldL, t, tj + 2.0, 480)
    fr = chip(fr, 'A LITTLE LESS AFTER THAT', 1450, 570, t, tl, goldL, 40)
    return frame(fr)

# ======================= BLOCK 16 =======================
B16 = mk(16, [[0, 1], [2], [3]])

def b16a(t):
    T = lambda m: B16.T(0, m)
    fr = base(t); fr = title(fr, 'THE OTHER DIRECTION', t)
    tw = T('Wait past')
    C = new(); cal_icon(C, 420, 560, 1.4, '67'); fr = appear(fr, C, (200, 300, 640, 820), t, 0.4, 1.0)
    fr = label(fr, 'WAIT PAST 67...', 220, 70, white, t, 0.8, 1300)
    te = max(T('eight percent') - 1.2, 1.5)
    fr = label(fr, '+8%', 340, 250, green, t, te, 1300)
    fr = label(fr, 'DELAYED RETIREMENT CREDITS', 620, 52, white, t, te + 0.6, 1300)
    fr = label(fr, 'EVERY YEAR YOU WAIT', 710, 60, goldL, t, te + 1.2, 1300)
    for k, h in enumerate([3, 5, 7]):
        C = new(); coin_stack(C, 1050 + k * 200, 940, h, 60); fr = appear(fr, C, (960 + k * 200, 940 - h * 20 - 60, 1140 + k * 200, 970), t, te + 0.8 + k * 0.4, 0.9)
    return frame(fr)

def b16b(t):
    T = lambda m: B16.T(1, m)
    fr = base(t); fr = title(fr, 'WAITING PAYS', t)
    data = [(67, 100, gold, 0.3), (68, 108, (170, 210, 90), T('at sixty eight')), (69, 116, (110, 210, 110), T('at sixty nine')), (70, 124, green, T('at seventy'))]
    for k, (age, p, col, st) in enumerate(data):
        if t < st: continue
        e = ease((t - st) / 1.2); x = 260 + k * 380; h = p * 4.2
        C = new(); bar(C, x, 870, 260, h * e, col); txt(C, f'{p}%', BOLD(84), 870 - h * e - 105, white, 255 * e, x=x + 130); txt(C, f'AGE {age}', BOLD(52), 895, goldL if age == 70 else white, 255, x=x + 130)
        fr = Image.alpha_composite(fr, C)
    fr = label(fr, 'PERCENT OF YOUR FULL AMOUNT', 175, 46, grey, t, 0.5)
    return frame(fr)

def b16c(t):
    T = lambda m: B16.T(2, m)
    fr = base(t); fr = title(fr, 'AFTER AGE 70', t)
    tm = T('After seventy')
    fr = label(fr, 'WAITING ADDS', 300, 80, white, t, 0.4, 1200)
    tn = T('nothing')
    fr = label(fr, 'NOTHING', 420, 190, red, t, tn, 1200)
    C = new(); padlock(C, 480, 560, 2.4, red); fr = appear(fr, C, (300, 350, 660, 820), t, 0.6, 1.0)
    L = new(); ImageDraw.Draw(L).line([760, 800, 1660, 800], fill=A(grey, 255 * E(t, tn + 0.8, 0.8)), width=10); fr = Image.alpha_composite(fr, L)
    fr = label(fr, '+0%', 680, 70, red, t, tn + 0.8, 1200)
    fr = chip(fr, 'NO REASON TO DELAY BEYOND 70', 1200, 860, t, T('so there is no reason'), goldL, 44)
    return frame(fr)

# ======================= BLOCK 17 =======================
B17 = mk(17, [[0, 1], [2], [3], [4]])

def b17a(t):
    T = lambda m: B17.T(0, m)
    fr = base(t); fr = title(fr, "PUT DOLLARS ON IT", t)
    C = new(); person(C, 260, 540, green, 2.8); txt(C, 'MARY', BOLD(56), 715, green, 255, x=260); fr = appear(fr, C, (100, 320, 430, 760), t, 0.3, 0.9)
    tm = T("Mary's full benefit")
    C = new(); paycheck(C, 560, 250, 1520, 780, green, (money(count(t, tm + 0.6, 2.6, 2665.80), True) if t > tm + 0.6 else '$ ?'), sub='PER MONTH', head='MARY: FULL BENEFIT AT 67', size=150)
    fr = appear(fr, C, (550, 240, 1530, 790), t, 0.6, 1.0)
    fr = lay(fr, lambda C: coin_stack(C, 1720, 780, 8, 66), (1630, 560, 1810, 800), t, tm + 1.0, 1.0)
    return frame(fr)

def b17b(t):
    T = lambda m: B17.T(1, m)
    fr = base(t); fr = title(fr, 'IF SHE CLAIMS AT 62', t)
    C = new(); person(C, 260, 540, green, 2.8); txt(C, 'MARY', BOLD(56), 715, green, 255, x=260); fr = appear(fr, C, (100, 320, 430, 760), t, 0.0, 0.5)
    C = new(); cal_icon(C, 700, 300, 0.75, '62', red); fr = appear(fr, C, (570, 170, 830, 430), t, 0.4, 0.9)
    tm = T('about one thousand')
    C = new(); paycheck(C, 900, 250, 1780, 780, red, money(count(t, tm, 2.4, 1866)), sub='PER MONTH', head='AT AGE 62', size=150)
    fr = appear(fr, C, (890, 240, 1790, 790), t, tm - 0.3, 1.0)
    fr = chip(fr, 'FULL BENEFIT: $2,665.80', 960, 850, t, 0.9, green, 44)
    return frame(fr)

def b17c(t):
    T = lambda m: B17.T(2, m)
    fr = base(t); fr = title(fr, 'IF SHE WAITS UNTIL 70', t)
    C = new(); person(C, 260, 540, green, 2.8); txt(C, 'MARY', BOLD(56), 715, green, 255, x=260); fr = appear(fr, C, (100, 320, 430, 760), t, 0.0, 0.5)
    C = new(); cal_icon(C, 700, 300, 0.75, '70', green); fr = appear(fr, C, (570, 170, 830, 430), t, 0.4, 0.9)
    tm = T('about three thousand')
    C = new(); paycheck(C, 900, 250, 1780, 780, green, money(count(t, tm, 2.6, 3306)), sub='PER MONTH', head='AT AGE 70', size=150)
    fr = appear(fr, C, (890, 240, 1790, 790), t, tm - 0.3, 1.0)
    fr = chip(fr, 'AT 62 IT WAS ONLY $1,866', 1340, 850, t, 1.2, red, 42)
    for k, h in enumerate([5, 8, 11]):
        C = new(); coin_stack(C, 630 + k * 110, 960, h, 46); fr = appear(fr, C, (570 + k * 110, 960 - h * 20 - 40, 690 + k * 110, 980), t, tm + 0.6 + k * 0.4, 0.9)
    return frame(fr)

def b17d(t):
    T = lambda m: B17.T(3, m)
    fr = base(t); fr = title(fr, 'THE DIFFERENCE', t)
    tm = T('seventeen thousand')
    L = new(); txt(L, '$' + f'{int(count(t, tm - 0.2, 2.4, 17280)):,}', BOLD(230), 250, green, 255 * E(t, tm - 0.4, 0.7), x=960); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'MORE EVERY YEAR', 520, 90, white, t, tm + 0.6)
    fr = label(fr, 'FOR THE SAME CAREER', 650, 62, goldL, t, T('for the same career'))
    for k in range(5):
        C = new(); bill(C, 380 + k * 290, 860, 230, 112, (-1) ** k * 4, 255); fr = appear(fr, C, (250 + k * 290, 780, 510 + k * 290, 940), t, tm + 1.0 + k * 0.4, 0.8)
    return frame(fr)

# ======================= BLOCK 18 =======================
B18 = mk(18, [[0, 1], [2], [3, 4], [5, 6]])

def b18a(t):
    T = lambda m: B18.T(0, m)
    fr = base(t); fr = title(fr, 'AND THERE IS A BONUS', t)
    tc = T('Every year')
    fr = label(fr, 'EVERY YEAR', 280, 90, white, t, tc, 1230)
    fr = label(fr, 'A COST OF LIVING', 400, 80, goldL, t, tc + 0.8, 1230)
    fr = label(fr, 'INCREASE', 500, 110, goldL, t, tc + 1.2, 1230)
    C = new(); up_arrow(C, 460, 560, 3.0, green); fr = appear(fr, C, (250, 300, 680, 760), t, 0.5, 1.0)
    for k, h in enumerate([3, 5, 7]):
        C = new(); coin_stack(C, 1000 + k * 200, 900, h, 60); fr = appear(fr, C, (910 + k * 200, 900 - h * 20 - 60, 1090 + k * 200, 930), t, tc + 1.8 + k * 0.5, 0.9)
    return frame(fr)

def b18b(t):
    T = lambda m: B18.T(1, m)
    fr = base(t); fr = title(fr, 'THE 2026 INCREASE', t)
    tm = T('two point eight')
    L = new(); txt(L, '+' + f'{count(t, tm, 1.8, 2.8):.1f}' + '%', BOLD(260), 260, green, 255 * E(t, tm - 0.3, 0.7), x=650); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'IN 2026', 560, 66, white, t, tm + 0.4, 650)
    ta = T('two thousand seventy one')
    C = new(); paycheck(C, 1090, 300, 1800, 740, gold, '$2,071', sub='PER MONTH', head='AVERAGE RETIREE CHECK', size=130); fr = appear(fr, C, (1080, 290, 1810, 750), t, ta - 0.3, 1.0)
    C = new(); coin_stack(C, 300, 900, 7, 66); coin_stack(C, 460, 900, 4, 66); fr = appear(fr, C, (200, 720, 560, 930), t, 1.5, 0.9)
    return frame(fr)

def b18c(t):
    T = lambda m: B18.T(2, m)
    fr = base(t); fr = title(fr, 'A RAISE IS A PERCENTAGE', t)
    fr = label(fr, 'OF YOUR CHECK', 215, 60, white, t, T('But a raise'), 960)
    tm = T('fifty two')
    C = new(); paycheck(C, 200, 320, 940, 780, red, '$1,866', sub='CLAIMED AT 62', head='THE SMALLER EARLY CHECK', size=130); fr = appear(fr, C, (190, 310, 950, 790), t, 0.6, 1.0)
    L = new(); txt(L, '+$52', BOLD(150), 810, green, 255 * E(t, tm, 0.8), x=570); fr = Image.alpha_composite(fr, L)
    fr = lay(fr, lambda C: (ImageDraw.Draw(C).rounded_rectangle([1000, 320, 1720, 780], radius=30, outline=A(grey, 255), width=4)), (990, 310, 1730, 790), t, 0.6, 1.0)
    fr = label(fr, '2.8% RAISE', 480, 84, goldL, t, T('it is about') - 0.8, 1360)
    fr = label(fr, 'ABOUT $52', 620, 100, green, t, tm, 1360)
    return frame(fr)

def b18d(t):
    T = lambda m: B18.T(3, m)
    fr = base(t); fr = title(fr, 'THE GAP KEEPS GROWING', t)
    C = new(); paycheck(C, 130, 320, 830, 740, red, '$1,866', sub='EARLY', head='CLAIMED AT 62', size=120); fr = appear(fr, C, (120, 310, 840, 750), t, 0.0, 0.5)
    L = new(); txt(L, '+$52', BOLD(110), 770, green, 255, x=480); fr = Image.alpha_composite(fr, L)
    tm = T('ninety three')
    C = new(); paycheck(C, 1010, 240, 1790, 740, green, '$3,306', sub='LATE', head='CLAIMED AT 70', size=140); fr = appear(fr, C, (1000, 230, 1800, 750), t, 0.4, 1.0)
    L = new(); txt(L, '+$93', BOLD(110), 770, green, 255 * E(t, tm, 0.8), x=1400); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'THE BIGGER CHECK GETS MORE', 920, 50, goldL, t, T('The gap keeps growing') - 0.6)
    return frame(fr)

# ======================= BLOCK 19 =======================
B19 = mk(19, [[0, 1], [2, 3], [4]])

def b19a(t):
    T = lambda m: B19.T(0, m)
    fr = base(t); fr = title(fr, 'NUMBER FOUR', t)
    fr = label(fr, 'THE ONE THAT SURPRISES YOU', 240, 64, goldL, t, 0.5)
    C = new(); person(C, 480, 640, blue, 3.0); briefcase(C, 730, 740, 1.4); fr = appear(fr, C, (300, 400, 860, 860), t, 0.9, 1.0)
    tw = T('What if')
    fr = label(fr, 'CLAIM EARLY...', 420, 86, white, t, tw, 1330)
    fr = label(fr, 'BUT STILL WORKING?', 560, 86, red, t, T('but you are still'), 1330)
    C = new(); bill(C, 1240, 780, 240, 118, -6); bill(C, 1470, 800, 240, 118, 5); fr = appear(fr, C, (1080, 700, 1640, 900), t, T('but you are still') + 0.3, 1.0)
    return frame(fr)

def b19b(t):
    T = lambda m: B19.T(1, m)
    fr = base(t); fr = title(fr, 'THE EARNINGS LIMIT', t)
    fr = label(fr, 'BEFORE FULL RETIREMENT AGE', 230, 62, white, t, 0.4)
    tl = T('In twenty twenty six')
    fr = lay(fr, lambda C: ImageDraw.Draw(C).rounded_rectangle([220, 420, 1700, 520], radius=22, fill=A(card, 255), outline=A(grey, 255), width=3), (210, 410, 1710, 530), t, 0.4, 0.8)
    C = new(); ImageDraw.Draw(C).rounded_rectangle([220, 420, 1000, 520], radius=22, fill=A(gold, 255), outline=A(goldL, 255), width=4); fr = appear(fr, C, (210, 410, 1010, 530), t, tl, 1.2)
    L = new(); ImageDraw.Draw(L).line([1000, 380, 1000, 560], fill=A(red, 255 * E(t, tl + 0.6, 0.6)), width=10); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'LIMIT', 600, 60, red, t, tl + 0.6, 1000)
    L = new(); txt(L, '$24,480', BOLD(200), 690, goldL, 255 * E(t, tl + 1.0, 0.8), x=960); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'A YEAR', 920, 54, white, t, tl + 1.4)
    fr = lay(fr, lambda C: coin_stack(C, 300, 330, 5, 50), (230, 200, 370, 350), t, tl + 0.4, 0.9)
    return frame(fr)

def b19c(t):
    T = lambda m: B19.T(2, m)
    fr = base(t); fr = title(fr, 'EVERY TWO DOLLARS...', t)
    fr = label(fr, 'ABOVE THE LIMIT', 220, 60, white, t, 0.4)
    C = new(); bill(C, 400, 500, 260, 128, -4); bill(C, 400, 660, 260, 128, 4); txt(C, '$2 EARNED', BOLD(58), 780, white, 255, x=400); fr = appear(fr, C, (240, 400, 580, 850), t, 0.8, 1.0)
    fr = lay(fr, lambda C: arrow_r(C, 700, 1000, 580, goldL), (690, 530, 1010, 630), t, 1.6, 0.9)
    tw = T('withhold')
    C = new(); bill(C, 1330, 580, 300, 148, 0, 255, (120, 130, 150)); fr = appear(fr, C, (1150, 480, 1510, 680), t, tw - 0.6, 1.0)
    L = new(); cross(L, 1330, 580, 100, red, 255 * E(t, tw + 0.2, 0.7)); txt(L, '$1 WITHHELD', BOLD(66), 730, red, 255 * E(t, tw, 0.8), x=1330); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'HALF OF IT DOES NOT ARRIVE', 880, 56, goldL, t, tw + 1.0)
    return frame(fr)

# ======================= BLOCK 20 =======================
B20 = mk(20, [[0], [1, 2], [3]])

def b20a(t):
    T = lambda m: B20.T(0, m)
    fr = base(t); fr = title(fr, "FRANK CLAIMS AT 62", t)
    C = new(); person(C, 400, 560, blue, 3.2); txt(C, 'FRANK', BOLD(58), 750, blue, 255, x=400); fr = appear(fr, C, (220, 340, 590, 810), t, 0.4, 1.0)
    C = new(); briefcase(C, 700, 700, 1.5); fr = appear(fr, C, (540, 600, 860, 800), t, T('keeps a job'), 1.0)
    tj = T('forty thousand')
    L = new(); txt(L, '$' + f'{int(count(t, tj - 0.5, 1.2, 40000)):,}', BOLD(220), 320, goldL, 255 * E(t, tj - 0.2, 0.7), x=1290); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'A YEAR FROM HIS JOB', 570, 64, white, t, tj + 0.6, 1290)
    C = new(); bill(C, 1150, 800, 240, 118, -5); bill(C, 1400, 820, 240, 118, 6); fr = appear(fr, C, (990, 720, 1560, 900), t, tj + 0.5, 1.0)
    return frame(fr)

def b20b(t):
    T = lambda m: B20.T(1, m)
    fr = base(t); fr = title(fr, 'ABOVE THE LIMIT', t)
    x0, x1 = 200, 1720; sx = x0 + (x1 - x0) * 24480 / 40000
    fr = lay(fr, lambda C: (ImageDraw.Draw(C).rounded_rectangle([x0, 300, x1, 400], radius=22, fill=A(gold, 255), outline=A(goldL, 255), width=4), txt(C, '$40,000 JOB', BOLD(46), 322, navy, 255, x=(x0 + sx) / 2 - 60)), (190, 290, 1730, 410), t, 0.3, 0.9)
    ta = T('fifteen thousand five')
    C = new(); ImageDraw.Draw(C).rounded_rectangle([sx, 300, x1, 400], radius=22, fill=A(red, 255), outline=A((255, 150, 150), 255), width=4); fr = appear(fr, C, (sx - 10, 290, x1 + 10, 410), t, ta, 1.0)
    L = new(); ImageDraw.Draw(L).line([sx, 260, sx, 440], fill=A(white, 255), width=8); txt(L, 'LIMIT $24,480', BOLD(40), 210, white, 255, x=sx); fr = Image.alpha_composite(fr, L)
    fr = label(fr, '$15,520 ABOVE THE LIMIT', 500, 80, red, t, ta + 0.2)
    th = T('Half of it')
    fr = label(fr, 'HALF OF IT WITHHELD', 650, 66, white, t, th)
    L = new(); txt(L, '$' + f'{int(count(t, th + 0.8, 2.0, 7760)):,}', BOLD(210), 750, red, 255 * E(t, th + 0.6, 0.8), x=960); fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b20c(t):
    T = lambda m: B20.T(2, m)
    fr = base(t); fr = title(fr, 'CHECKS THAT DO NOT ARRIVE', t)
    tb = T('At his benefit')
    fr = label(fr, 'FRANK: $1,674 A MONTH', 220, 62, blue, t, 0.4)
    tc = T('more than four')
    for k in range(12):
        x = 120 + (k % 6) * 290; y = 330 + (k // 6) * 200
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([x, y, x + 250, y + 160], radius=22, fill=A(card, 255), outline=A(gold, 255), width=4)
        txt(C, f'MONTH {k + 1}', BOLD(38), y + 20, white, 255, x=x + 125); txt(C, '$1,674', BOLD(56), y + 82, goldL, 255, x=x + 125)
        fr = appear(fr, C, (x - 6, y - 6, x + 256, y + 166), t, 0.5 + k * 0.08, 0.6)
        if k < 5:
            st = tc + 0.3 + k * 0.6
            if t > st:
                e = ease((t - st) / 0.5); L = new(); dd = ImageDraw.Draw(L)
                fillc = A((60, 20, 30), 200 * e) if k < 4 else A((60, 20, 30), 90 * e)
                dd.rounded_rectangle([x, y, x + 250, y + 160], radius=22, fill=fillc, outline=A(red, 255 * e), width=6)
                if k < 4:
                    dd.line([x + 20, y + 20, x + 230, y + 140], fill=A(red, 255 * e), width=10); dd.line([x + 230, y + 20, x + 20, y + 140], fill=A(red, 255 * e), width=10)
                else:
                    dd.line([x + 20, y + 20, x + 125, y + 80], fill=A(red, 255 * e), width=10)
                fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'MORE THAN 4 MONTHS OF CHECKS', 800, 66, red, t, tc + 2.6)
    fr = label(fr, 'SIMPLY DO NOT ARRIVE', 890, 66, red, t, tc + 3.0)
    return frame(fr)

SL = {11: [b11a, b11b, b11c], 12: [b12a, b12b, b12c, b12d], 13: [b13a, b13b, b13c], 14: [b14a, b14b, b14c], 15: [b15a, b15b, b15c],
      16: [b16a, b16b, b16c], 17: [b17a, b17b, b17c, b17d], 18: [b18a, b18b, b18c, b18d], 19: [b19a, b19b, b19c], 20: [b20a, b20b, b20c]}
FSD = {11: B11.FS, 12: B12.FS, 13: B13.FS, 14: B14.FS, 15: B15.FS, 16: B16.FS, 17: B17.FS, 18: B18.FS, 19: B19.FS, 20: B20.FS}

if __name__ == '__main__':
    run_cli('b11_20', SL, FSD, None)
