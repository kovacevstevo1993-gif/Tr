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


def cal_icon(C, cx, cy, s, txt_, col=gold):
    d = ImageDraw.Draw(C); w = 150 * s
    d.rounded_rectangle([cx - w, cy - w * 0.9, cx + w, cy + w * 0.9], radius=int(26 * s), fill=A((236, 240, 245), 255), outline=A(col, 255), width=6)
    d.rounded_rectangle([cx - w, cy - w * 0.9, cx + w, cy - w * 0.4], radius=int(26 * s), fill=A(col, 255)); d.rectangle([cx - w, cy - w * 0.6, cx + w, cy - w * 0.4], fill=A(col, 255))
    for k in (-0.55, 0.55): d.rounded_rectangle([cx + k * w - 10 * s, cy - w * 1.05, cx + k * w + 10 * s, cy - w * 0.75], radius=6, fill=A(navy, 255))
    txt(C, txt_, BOLD(int(120 * s)), cy - w * 0.25, navy, 255, x=cx)

# ---------- extra icons ----------
def capitol(C, cx, cy, s=1.0, col=(236, 240, 245)):
    d = ImageDraw.Draw(C)
    d.polygon([(cx - 210 * s, cy - 60 * s), (cx, cy - 190 * s), (cx + 210 * s, cy - 60 * s)], fill=A(col, 255), outline=A(gold, 255))
    d.rectangle([cx - 230 * s, cy - 60 * s, cx + 230 * s, cy - 30 * s], fill=A(col, 255), outline=A(gold, 255), width=3)
    for k in range(5):
        x = cx - 180 * s + k * 90 * s
        d.rectangle([x - 18 * s, cy - 30 * s, x + 18 * s, cy + 130 * s], fill=A(col, 255), outline=A(grey, 255), width=2)
    d.rectangle([cx - 250 * s, cy + 130 * s, cx + 250 * s, cy + 165 * s], fill=A(col, 255), outline=A(gold, 255), width=3)
    d.rectangle([cx - 270 * s, cy + 165 * s, cx + 270 * s, cy + 195 * s], fill=A(col, 255), outline=A(gold, 255), width=3)

def shield(C, cx, cy, s=1.0, col=blue):
    d = ImageDraw.Draw(C)
    pts = [(cx - 130 * s, cy - 150 * s), (cx + 130 * s, cy - 150 * s), (cx + 130 * s, cy + 20 * s), (cx, cy + 170 * s), (cx - 130 * s, cy + 20 * s)]
    d.polygon(pts, fill=A(col, 255), outline=A(goldL, 255)); d.line(pts + [pts[0]], fill=A(goldL, 255), width=8)

def thumb(C, cx, cy, s=1.0, col=goldL):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 120 * s, cy - 10 * s, cx - 50 * s, cy + 110 * s], radius=int(14 * s), fill=A(col, 255))
    d.rounded_rectangle([cx - 40 * s, cy - 10 * s, cx + 130 * s, cy + 110 * s], radius=int(24 * s), fill=A(col, 255))
    d.rounded_rectangle([cx - 30 * s, cy - 110 * s, cx + 20 * s, cy + 10 * s], radius=int(22 * s), fill=A(col, 255))

def dashed(C, x0, y0, x1, y1, col=goldL, w=8, dash=34, gap=22):
    d = ImageDraw.Draw(C)
    for (a, b, c, e) in ((x0, y0, x1, y0), (x0, y1, x1, y1), (x0, y0, x0, y1), (x1, y0, x1, y1)):
        L = ((c - a) ** 2 + (e - b) ** 2) ** 0.5; n = int(L // (dash + gap)) + 1
        for k in range(n):
            s0 = k * (dash + gap) / L; s1 = min(1, (k * (dash + gap) + dash) / L)
            d.line([a + (c - a) * s0, b + (e - b) * s0, a + (c - a) * s1, b + (e - b) * s1], fill=A(col, 255), width=w)

def pc(fr, box, t, t0, col, amount, head, sub='PER MONTH', size=110, d=1.0):
    C = new(); paycheck(C, *box, col, amount, sub=sub, head=head, size=size)
    return appear(fr, C, (box[0] - 10, box[1] - 10, box[2] + 10, box[3] + 10), t, t0, d)

def pair(C, cx, cy, c1=blue, c2=purple, s=2.2):
    person(C, cx - 90 * s / 2.2, cy, c1, s); person(C, cx + 90 * s / 2.2, cy, c2, s)

# ======================= BLOCK 21 =======================
B21 = mk(21, [[0, 1], [2], [3, 4]])

def b21a(t):
    T = lambda m: B21.T(0, m)
    fr = base(t); fr = title(fr, 'IS THE MONEY GONE FOREVER?', t, 56)
    C = new(); money_bag(C, 560, 600, 2.4); fr = appear(fr, C, (250, 300, 880, 900), t, 0.3, 1.0)
    fr = label(fr, 'GONE FOREVER?', 470, 100, red, t, 0.9, 1370)
    tn = T('It is not')
    C = new(); strike(C, 1010, 1730, 512, red, 255, 12); fr = appear(fr, C, (1000, 490, 1740, 535), t, tn, 0.5)
    fr = label(fr, 'NOT GONE!', 640, 130, green, t, tn + 0.3, 1370)
    C = new(); check(C, 1370, 900, 60, green); fr = appear(fr, C, (1290, 830, 1450, 970), t, tn + 0.9, 0.6)
    return frame(fr)

def b21b(t):
    T = lambda m: B21.T(1, m)
    fr = base(t); fr = title(fr, 'AT FULL RETIREMENT AGE', t, 56)
    C = new(); cal_icon(C, 420, 560, 1.3, 'FRA'); fr = appear(fr, C, (200, 380, 640, 760), t, 0.4, 1.0)
    tw = T('credit for the months')
    fr = label(fr, 'WITHHELD MONTHS', 250, 56, red, t, 0.9, 1150)
    for k in range(6):
        x = 720 + k * 190
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([x, 330, x + 165, 470], radius=20, fill=A(card, 255), outline=A(red, 255), width=4)
        txt(C, 'MONTH', BOLD(32), 345, grey, 255, x=x + 82); txt(C, str(k + 1), BOLD(70), 385, white, 255, x=x + 82)
        fr = appear(fr, C, (x - 6, 324, x + 172, 476), t, 0.9 + k * 0.12, 0.6)
    fr = label(fr, 'SOCIAL SECURITY RECALCULATES', 560, 60, white, t, 2.4, 1150)
    C = new(); arrow_d(C, 1150, 640, 760, goldL, 255, 14); fr = appear(fr, C, (1100, 630, 1200, 770), t, tw, 0.6)
    fr = label(fr, 'CREDIT FOR EVERY MONTH', 790, 76, green, t, tw + 0.3, 1150)
    return frame(fr)

def b21c(t):
    T = lambda m: B21.T(2, m)
    fr = base(t); fr = title(fr, 'IT COMES BACK', t, 58)
    C = new(); check(C, 300, 380, 80, green); fr = appear(fr, C, (200, 280, 400, 480), t, 0.3, 0.7)
    fr = label(fr, 'NOT LOST', 500, 80, green, t, 0.5, 300)
    tc = T('It comes back')
    fr = pc(fr, (620, 260, 1600, 700), t, tc, green, 'HIGHER', 'HIGHER MONTHLY CHECK', sub='', size=130)
    C = new(); up_arrow(C, 1720, 500, 1.4, green); fr = appear(fr, C, (1630, 350, 1810, 640), t, tc + 0.6, 0.8)
    tl = T('for the rest')
    fr = label(fr, 'FOR THE REST OF YOUR LIFE', 810, 76, goldL, t, tl, 1100)
    C = new(); coin_stack(C, 260, 900, 7, 64); fr = appear(fr, C, (170, 700, 350, 930), t, tl, 0.8)
    return frame(fr)

# ======================= BLOCK 22 =======================
B22 = mk(22, [[0, 1], [2], [3, 4]])

def b22a(t):
    T = lambda m: B22.T(0, m)
    fr = base(t); fr = title(fr, 'THE YEAR YOU REACH FULL RETIREMENT AGE', t, 50)
    C = new(); cal_icon(C, 330, 520, 1.2, 'FRA'); fr = appear(fr, C, (140, 360, 520, 700), t, 0.3, 1.0)
    tl = T('the limit jumps')
    fr = label(fr, 'THE LIMIT JUMPS TO', 250, 60, white, t, 0.8, 1180)
    L = new(); txt(L, '$65,160', BOLD(190), 320, goldL, 255 * E(t, tl, 0.8), x=1180); fr = Image.alpha_composite(fr, L)
    to = T('only one dollar')
    fr = label(fr, 'ABOVE THE LIMIT:', 570, 60, white, t, to, 1180)
    C = new(); ImageDraw.Draw(C).rounded_rectangle([560, 680, 1800, 920], radius=26, fill=A(card, 255), outline=A(red, 255), width=5)
    for k in range(3): coin(C, 660 + k * 110, 800, 44)
    txt(C, 'YOU EARN $3', BOLD(56), 770, white, 255, x=1120); txt(C, '$1 WITHHELD', BOLD(60), 770, red, 255, x=1560)
    fr = appear(fr, C, (550, 670, 1810, 930), t, to + 0.6, 0.9)
    return frame(fr)

def b22b(t):
    T = lambda m: B22.T(1, m)
    fr = base(t); fr = title(fr, 'AFTER FULL RETIREMENT AGE', t, 56)
    C = new(); padlock(C, 520, 560, 2.2, green, 255, True); fr = appear(fr, C, (300, 300, 740, 860), t, 0.5, 1.0)
    fr = label(fr, 'NO LIMIT AT ALL', 380, 120, green, t, 1.0, 1300)
    fr = label(fr, 'EARN AS MUCH AS YOU WANT', 600, 64, white, t, 2.0, 1300)
    C = new(); coin_stack(C, 1130, 900, 6, 60); coin_stack(C, 1300, 900, 9, 60); coin_stack(C, 1470, 900, 12, 60)
    fr = appear(fr, C, (1030, 620, 1580, 930), t, 2.6, 1.0)
    return frame(fr)

def b22c(t):
    T = lambda m: B22.T(2, m)
    fr = base(t); fr = title(fr, 'WHAT COUNTS AS EARNINGS', t, 56)
    fr = label(fr, 'COUNTS', 220, 60, green, t, 0.4, 480); fr = label(fr, 'DOES NOT COUNT', 220, 60, red, t, T('Pensions'), 1440)
    ys = [320, 480]
    for k, (nm, ic) in enumerate((('PAYCHECKS', 'p'), ('SELF EMPLOYMENT', 'b'))):
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([120, ys[k], 840, ys[k] + 130], radius=26, fill=A(card, 255), outline=A(green, 255), width=5)
        txt(C, nm, BOLD(50), ys[k] + 38, white, 255, x=520); check(C, 190, ys[k] + 65, 34, green)
        fr = appear(fr, C, (110, ys[k] - 10, 850, ys[k] + 140), t, 0.6 + k * 0.6, 0.8)
    C = new(); briefcase(C, 480, 800, 1.7); fr = appear(fr, C, (250, 640, 720, 960), t, 1.6, 0.9)
    tp = T('Pensions'); ti = T('investment income'); tf = T('four oh one')
    for k, (nm, tt_) in enumerate((('PENSIONS', tp), ('INVESTMENT INCOME', ti), ('401(k) WITHDRAWALS', tf))):
        y = 300 + k * 160
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([1000, y, 1800, y + 130], radius=26, fill=A(card, 255), outline=A(red, 255), width=5)
        txt(C, nm, BOLD(50), y + 38, white, 255, x=1420 + 30); cross(C, 1070, y + 65, 30, red)
        fr = appear(fr, C, (990, y - 10, 1810, y + 140), t, tt_ - 0.2, 0.8)
    return frame(fr)

# ======================= BLOCK 23 =======================
B23 = mk(23, [[0, 1], [2], [3]])

def b23a(t):
    T = lambda m: B23.T(0, m)
    fr = base(t); fr = title(fr, 'NUMBER FIVE: YOUR SPOUSE', t, 56)
    C = new(); cal_icon(C, 300, 560, 1.2, '5'); fr = appear(fr, C, (110, 400, 500, 730), t, 0.3, 1.0)
    C = new(); person(C, 850, 600, blue, 3.2); txt(C, 'YOU', BOLD(52), 780, blue, 255, x=850); fr = appear(fr, C, (700, 380, 1000, 830), t, 0.8, 0.9)
    C = new(); person(C, 1450, 600, purple, 3.2); txt(C, 'YOUR SPOUSE', BOLD(52), 780, purple, 255, x=1450); fr = appear(fr, C, (1230, 380, 1670, 830), t, 1.3, 0.9)
    ti = T('may be able')
    C = new(); arrow_r(C, 1030, 1300, 600, goldL, 255, 14); fr = appear(fr, C, (1020, 560, 1310, 640), t, ti, 0.7)
    fr = label(fr, "BENEFIT ON YOUR RECORD", 870, 60, goldL, t, ti + 0.5, 1150)
    return frame(fr)

def b23b(t):
    T = lambda m: B23.T(1, m)
    fr = base(t); fr = title(fr, 'THE SPOUSE BENEFIT', t, 58)
    tp = T('fifty percent')
    fr = label(fr, 'AT THEIR OWN FULL RETIREMENT AGE', 220, 54, white, t, 0.4, 1150)
    C = new(); ring(C, 600, 600, 220, 0.5, gold); fr = appear(fr, C, (330, 330, 870, 870), t, 0.5, 0.8)
    fr = label(fr, 'UP TO', 500, 50, white, t, tp - 0.2, 600); fr = label(fr, '50%', 560, 110, goldL, t, tp - 0.2, 600)
    fr = label(fr, 'OF YOUR FULL BENEFIT', 400, 60, white, t, tp + 0.4, 1420)
    tf = T('only after')
    fr = chip(fr, 'ONLY AFTER YOU FILED', 1420, 560, t, tf, red, 48)
    C = new(); check(C, 1130, 760, 50, green); txt(C, 'YOU FILE FIRST', BOLD(60), 725, green, 255, x=1500); fr = appear(fr, C, (1060, 690, 1800, 820), t, tf + 0.8, 0.8)
    return frame(fr)

def b23c(t):
    T = lambda m: B23.T(2, m)
    fr = base(t); fr = title(fr, "WITH MARY'S FULL BENEFIT", t, 58)
    fr = pc(fr, (150, 260, 800, 560), t, 0.4, green, '$2,665.80', "MARY'S FULL BENEFIT", sub='', size=86)
    C = new(); txt(C, '× 50%', BOLD(90), 340, goldL, 255, x=960); fr = appear(fr, C, (830, 300, 1090, 470), t, 1.0, 0.8)
    C = new(); person(C, 280, 780, purple, 1.8); txt(C, 'SPOUSE WITH LITTLE WORK HISTORY', BOLD(46), 730, white, 255, x=800); fr = appear(fr, C, (150, 660, 1500, 900), t, 1.6, 0.9)
    tu = T('up to about')
    fr = pc(fr, (1100, 260, 1780, 560), t, tu - 0.3, gold, '$1,333', 'SPOUSE: UP TO ABOUT', sub='PER MONTH', size=100)
    C = new(); coin_stack(C, 1660, 930, 6, 56); fr = appear(fr, C, (1580, 750, 1760, 950), t, tu + 0.8, 0.8)
    return frame(fr)

# ======================= BLOCK 24 =======================
B24 = mk(24, [[0, 1], [2], [3]])

def b24a(t):
    T = lambda m: B24.T(0, m)
    fr = base(t); fr = title(fr, 'TIMING MATTERS FOR SPOUSES TOO', t, 54)
    C = new(); cal_icon(C, 330, 520, 1.15, '-3'); txt(C, 'YEARS EARLY', BOLD(44), 750, red, 255, x=330); fr = appear(fr, C, (130, 350, 530, 800), t, 0.5, 1.0)
    te = T('drops to')
    base_y = 900; BW = 260
    C = new(); bar(C, 800, base_y, BW, 500, gold); txt(C, '50%', BOLD(80), base_y - 400, navy, 255, x=800 + BW / 2)
    fr = appear(fr, C, (780, 380, 1080, 930), t, 1.4, 0.9)
    fr = label(fr, 'AT FULL AGE', 940, 46, grey, t, 1.6, 930)
    C = new(); bar(C, 1250, base_y, BW, 375, red); txt(C, '37.5%', BOLD(80), base_y - 300, white, 255, x=1250 + BW / 2)
    fr = appear(fr, C, (1230, 500, 1550, 930), t, te, 0.9)
    fr = label(fr, 'CLAIMS EARLY', 940, 46, grey, t, te + 0.2, 1380)
    return frame(fr)

def b24b(t):
    T = lambda m: B24.T(1, m)
    fr = base(t); fr = title(fr, 'NO GROWTH AFTER FULL AGE', t, 56)
    fr = pc(fr, (520, 260, 1400, 640), t, 0.4, gold, '$1,333', 'SPOUSAL BENEFIT', sub='FIXED AMOUNT', size=110)
    tw = T('does not grow')
    C = new(); up_arrow(C, 1650, 470, 1.5, green); fr = appear(fr, C, (1560, 320, 1740, 620), t, 0.9, 0.7)
    C = new(); cross(C, 1650, 470, 130, red); fr = appear(fr, C, (1500, 320, 1800, 620), t, tw, 0.5)
    fr = label(fr, 'DOES NOT GROW IF YOU WAIT', 760, 72, red, t, tw + 0.3)
    fr = label(fr, 'PAST FULL RETIREMENT AGE', 860, 60, white, t, tw + 0.8)
    return frame(fr)

def b24c(t):
    T = lambda m: B24.T(2, m)
    fr = base(t); fr = title(fr, 'IF YOU ARE DIVORCED', t, 58)
    C = new(); person(C, 520, 560, blue, 3.0); person(C, 860, 560, purple, 3.0); fr = appear(fr, C, (380, 360, 1000, 800), t, 0.4, 0.9)
    C = new(); cal_icon(C, 1450, 520, 1.6, '10+'); fr = appear(fr, C, (1170, 240, 1730, 800), t, 0.9, 1.0)
    fr = label(fr, 'YEARS OF MARRIAGE', 830, 64, goldL, t, 1.3, 1450)
    tq = T('may still qualify')
    fr = label(fr, 'YOU MAY STILL QUALIFY', 250, 66, green, t, tq, 700)
    C = new(); check(C, 700, 880, 50, green); fr = appear(fr, C, (630, 820, 780, 940), t, tq + 0.6, 0.6)
    return frame(fr)

# ======================= BLOCK 25 =======================
B25 = mk(25, [[0, 1], [2], [3, 4]])

def b25a(t):
    T = lambda m: B25.T(0, m)
    fr = base(t); fr = title(fr, 'SURVIVOR BENEFITS', t, 60)
    C = new(); person(C, 600, 520, blue, 3.3); person(C, 1000, 520, purple, 3.3); fr = appear(fr, C, (440, 300, 1160, 720), t, 0.4, 0.9)
    C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1240, 300, 1780, 700], radius=30, fill=A(card, 255), outline=A(gold, 255), width=5)
    txt(C, 'ONE SPOUSE', BOLD(54), 400, white, 255, x=1510); txt(C, 'DIES', BOLD(120), 490, red, 255, x=1510)
    tw = T('When one spouse dies')
    fr = appear(fr, C, (1230, 290, 1790, 710), t, tw, 0.9)
    C = new(); person(C, 1000, 520, grey, 3.3, 140); fr = appear(fr, C, (900, 300, 1100, 720), t, tw + 0.6, 0.8)
    fr = label(fr, 'DOES NOT KEEP BOTH CHECKS', 860, 68, goldL, t, T('does not keep both'), 960)
    return frame(fr)

def b25b(t):
    T = lambda m: B25.T(1, m)
    fr = base(t); fr = title(fr, 'THE SURVIVOR KEEPS THE LARGER', t, 56)
    fr = pc(fr, (170, 280, 880, 640), t, 0.3, green, 'LARGER', 'LARGER CHECK', sub='', size=120)
    tk = T('keeps the larger')
    C = new(); check(C, 525, 740, 60, green); fr = appear(fr, C, (450, 670, 600, 810), t, tk, 0.6)
    fr = label(fr, 'KEPT', 840, 70, green, t, tk + 0.2, 525)
    fr = pc(fr, (1040, 280, 1750, 640), t, 0.7, red, 'SMALLER', 'SMALLER CHECK', sub='', size=120)
    ts = T('smaller one disappears')
    L = new(); dd = ImageDraw.Draw(L); e = ease((t - ts) / 0.6)
    if e > 0:
        dd.rounded_rectangle([1040, 280, 1750, 640], radius=30, fill=A((20, 25, 45), 190 * e), outline=A(red, 255 * e), width=6)
        dd.line([1080, 320, 1710, 600], fill=A(red, 255 * e), width=14); dd.line([1710, 320, 1080, 600], fill=A(red, 255 * e), width=14)
    fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'DISAPPEARS', 740, 70, red, t, ts + 0.3, 1395)
    return frame(fr)

def b25c(t):
    T = lambda m: B25.T(2, m)
    fr = base(t); fr = title(fr, 'HOW MUCH THE SURVIVOR GETS', t, 56)
    ta = T('as early as sixty'); tf = T('full retirement age')
    fr = label(fr, 'FROM AGE 60', 220, 56, white, t, 0.4, 560)
    C = new(); ring(C, 560, 560, 200, 0, gold); fr = appear(fr, C, (330, 330, 790, 790), t, 0.4, 0.7)
    frac = 0.715 * ease((t - ta) / 2.0)
    C = new(); ring(C, 560, 560, 200, frac, gold); fr = Image.alpha_composite(fr, C) if t > ta else fr
    L = new(); txt(L, '71.5%', BOLD(96), 515, white, 255 * E(t, ta, 0.6), x=560); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'OF THE DECEASED\'S BENEFIT', 830, 44, goldL, t, ta + 0.6, 560)
    fr = label(fr, 'AT FULL RETIREMENT AGE', 220, 56, white, t, tf - 0.2, 1360)
    C = new(); ring(C, 1360, 560, 200, 0, green); fr = appear(fr, C, (1130, 330, 1590, 790), t, tf - 0.2, 0.7)
    frac = 1.0 * ease((t - tf) / 2.0)
    C = new(); ring(C, 1360, 560, 200, frac, green); fr = Image.alpha_composite(fr, C) if t > tf else fr
    L = new(); txt(L, '100%', BOLD(96), 515, white, 255 * E(t, tf, 0.6), x=1360); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'OF THE DECEASED\'S BENEFIT', 830, 44, green, t, tf + 0.6, 1360)
    return frame(fr)

# ======================= BLOCK 26 =======================
B26 = mk(26, [[0], [1], [2, 3]])

def b26a(t):
    T = lambda m: B26.T(0, m)
    fr = base(t); fr = title(fr, 'WHY THE HIGHER EARNER MATTERS', t, 54)
    C = new(); person(C, 560, 560, purple, 3.6); txt(C, 'HIGHER EARNER', BOLD(52), 800, purple, 255, x=560); fr = appear(fr, C, (300, 330, 820, 860), t, 0.4, 0.9)
    C = new(); person(C, 1360, 560, blue, 3.6); txt(C, 'SPOUSE', BOLD(52), 800, blue, 255, x=1360); fr = appear(fr, C, (1140, 330, 1580, 860), t, 1.0, 0.9)
    tc = T('claiming age')
    C = new(); cal_icon(C, 960, 500, 1.0, 'AGE'); fr = appear(fr, C, (790, 360, 1130, 640), t, tc, 0.9)
    fr = label(fr, 'CLAIMING AGE', 700, 56, goldL, t, tc + 0.4, 960)
    return frame(fr)

def b26b(t):
    T = lambda m: B26.T(0, m)
    T = lambda m: B26.T(1, m)
    fr = base(t); fr = title(fr, 'IF MARY WAITS UNTIL 70', t, 58)
    C = new(); cal_icon(C, 330, 470, 1.15, '70'); fr = appear(fr, C, (140, 320, 520, 640), t, 0.3, 0.9)
    fr = label(fr, 'MARY', 660, 60, green, t, 0.6, 330)
    tc = T('her check')
    fr = pc(fr, (700, 260, 1500, 620), t, tc, green, '$3,306', 'MARY AT 70', sub='PER MONTH', size=130)
    C = new(); coin_stack(C, 1700, 620, 9, 60); fr = appear(fr, C, (1610, 420, 1790, 650), t, tc + 0.8, 0.8)
    ts = T('surviving spouse')
    C = new(); arrow_d(C, 1100, 650, 760, goldL, 255, 14); fr = appear(fr, C, (1050, 640, 1150, 780), t, ts - 0.3, 0.6)
    fr = label(fr, 'SURVIVING SPOUSE KEEPS IT FOR LIFE', 810, 62, goldL, t, ts, 1100)
    return frame(fr)

def b26c(t):
    T = lambda m: B26.T(2, m)
    fr = base(t); fr = title(fr, 'THE DELAY IS INSURANCE', t, 58)
    C = new(); shield(C, 960, 430, 1.7, blue); check(C, 960, 430, 90, green); fr = appear(fr, C, (700, 200, 1220, 740), t, 0.4, 1.0)
    C = new(); person(C, 480, 560, purple, 3.0); person(C, 1440, 560, blue, 3.0); fr = appear(fr, C, (300, 350, 1620, 760), t, 1.0, 0.9)
    ti = T('It is insurance')
    fr = label(fr, 'NOT ONLY FOR HER', 810, 66, white, t, 0.6)
    fr = label(fr, 'FOR WHOEVER LIVES LONGER', 910, 70, goldL, t, ti)
    return frame(fr)

# ======================= BLOCK 27 =======================
B27 = mk(27, [[0, 1], [2], [3, 4]])

def b27a(t):
    fr = base(t); fr = title(fr, 'THE QUESTION EVERYONE ASKS', t, 56)
    C = new(); money_bag(C, 620, 600, 2.5); fr = appear(fr, C, (300, 300, 940, 900), t, 0.3, 1.0)
    L = new(); txt(L, '?', BOLD(300), 660, red, 255 * E(t, 1.2, 0.8), x=1370); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'WILL SOCIAL SECURITY', 400, 76, white, t, 0.9, 1370)
    fr = label(fr, 'EVEN BE THERE?', 510, 96, goldL, t, 1.6, 1370)
    return frame(fr)

def b27b(t):
    T = lambda m: B27.T(1, m)
    fr = base(t); fr = title(fr, 'THE 2026 TRUSTEES REPORT', t, 56)
    C = new(); capitol(C, 450, 520, 1.1); fr = appear(fr, C, (150, 300, 750, 780), t, 0.3, 1.0)
    fr = label(fr, 'RELEASED IN JUNE 2026', 830, 46, grey, t, 0.8, 450)
    tp = T('can pay full')
    fr = label(fr, 'RETIREMENT TRUST FUND', 260, 60, white, t, 0.6, 1290)
    fr = label(fr, 'PAYS FULL BENEFITS UNTIL', 380, 58, goldL, t, tp, 1290)
    tq = T('last quarter')
    C = new(); mcard(C, 950, 520, 1650, 800, gold, 'LAST QUARTER OF', '2032', 150, goldL); fr = appear(fr, C, (940, 510, 1660, 810), t, tq - 0.2, 1.0)
    return frame(fr)

def b27c(t):
    T = lambda m: B27.T(2, m)
    fr = base(t); fr = title(fr, 'BOTH TRUST FUNDS COMBINED', t, 56)
    tb = T('Both trust funds'); 
    x0, x1, y = 260, 1660, 620; X32 = 1230
    C = new(); d = ImageDraw.Draw(C); d.line([x0, y, x1, y], fill=A(grey, 255), width=10)
    for yr, x in ((2026, x0), (2032, X32), (2034, x1)):
        d.line([x, y - 24, x, y + 24], fill=A(white, 255), width=8); txt(C, str(yr), BOLD(52), y + 40, white, 255, x=x)
    fr = appear(fr, C, (200, 540, 1720, 720), t, 0.3, 0.8)
    C = new(); coin_stack(C, X32, y - 30, 6, 52); fr = appear(fr, C, (1130, 400, 1330, 630), t, 0.9, 0.8)
    fr = label(fr, 'RETIREMENT FUND', 220, 44, gold, t, 0.9, X32)
    fr = label(fr, '2032', 280, 70, goldL, t, 0.9, X32)
    C = new(); coin_stack(C, x1, y - 30, 8, 52); fr = appear(fr, C, (1560, 380, 1760, 630), t, tb + 0.4, 0.8)
    fr = label(fr, 'BOTH COMBINED', 220, 44, blue, t, tb + 0.4, x1); fr = label(fr, '2034', 280, 70, (190, 215, 255), t, tb + 0.4, x1)
    to = T('official projections')
    fr = chip(fr, 'OFFICIAL PROJECTIONS', 960, 830, t, to, goldL, 56)
    return frame(fr)

# ======================= BLOCK 28 =======================
B28 = mk(28, [[0, 1, 2], [3], [4]])

def b28a(t):
    T = lambda m: B28.T(0, m)
    fr = base(t); fr = title(fr, 'BUT NOTICE WHAT THEY DID NOT SAY', t, 54)
    tn = T('After that date')
    C = new(); money_bag(C, 420, 480, 1.9); fr = appear(fr, C, (170, 250, 670, 720), t, 0.3, 1.0)
    fr = label(fr, 'AFTER THAT DATE:', 270, 60, white, t, tn - 0.2, 1240)
    L = new(); txt(L, 'NOT ZERO', BOLD(190), 350, green, 255 * E(t, tn + 0.4, 0.8), x=1240); fr = Image.alpha_composite(fr, L)
    tp = T('Payroll taxes')
    C = new(); 
    for k in range(4): bill(C, 380 + k * 380, 750, 260, 125, 0)
    fr = appear(fr, C, (200, 640, 1780, 880), t, tp, 1.0)
    fr = label(fr, 'PAYROLL TAXES KEEP COMING IN', 930, 62, goldL, t, tp + 0.4)
    return frame(fr)

def b28b(t):
    T = lambda m: B28.T(1, m)
    fr = base(t); fr = title(fr, 'WHAT COULD STILL BE PAID', t, 56)
    tr = T('retirement fund'); tc = T('combined funds')
    for (cx, col, pct, tm, nm) in ((520, gold, 78, tr, 'RETIREMENT FUND'), (1400, blue, 83, tc, 'COMBINED FUNDS')):
        fr = label(fr, nm, 220, 54, white, t, tm - 0.3, cx)
        C = new(); ring(C, cx, 580, 210, 0, col); fr = appear(fr, C, (cx - 240, 350, cx + 240, 810), t, tm - 0.3, 0.7)
        frac = pct / 100 * ease((t - tm) / 2.0)
        C = new(); ring(C, cx, 580, 210, frac, col); fr = Image.alpha_composite(fr, C) if t > tm else fr
        L = new(); txt(L, f'{int(round(frac * 100))}%', BOLD(110), 525, white, 255 * E(t, tm, 0.6), x=cx); fr = Image.alpha_composite(fr, L)
        fr = label(fr, 'OF SCHEDULED BENEFITS', 850, 44, goldL, t, tm + 1.0, cx)
    return frame(fr)

def b28c(t):
    T = lambda m: B28.T(2, m)
    fr = base(t); fr = title(fr, "MARY'S CHECK AFTER THAT DATE", t, 54)
    fr = pc(fr, (130, 300, 850, 620), t, 0.4, green, '$2,665', 'TODAY', sub='PER MONTH', size=130)
    tb = T('would become')
    C = new(); arrow_r(C, 880, 1060, 460, goldL, 255, 14); fr = appear(fr, C, (870, 420, 1070, 500), t, tb - 0.2, 0.6)
    fr = pc(fr, (1090, 300, 1810, 620), t, tb, gold, '$2,079', 'ABOUT', sub='PER MONTH', size=130)
    fr = chip(fr, 'ABOUT 78% OF THE FULL CHECK', 960, 760, t, tb + 1.2, goldL, 54)
    return frame(fr)

# ======================= BLOCK 29 =======================
B29 = mk(29, [[0, 1, 2], [3], [4]])

def b29a(t):
    T = lambda m: B29.T(0, m)
    fr = base(t); fr = title(fr, 'COULD CONGRESS FIX IT?', t, 58)
    C = new(); capitol(C, 600, 560, 1.5); fr = appear(fr, C, (250, 260, 950, 860), t, 0.3, 1.0)
    th = T('It has before')
    fr = label(fr, 'IT HAS BEFORE', 300, 88, goldL, t, th, 1370)
    ty = T('In nineteen eighty three')
    C = new(); cal_icon(C, 1370, 600, 1.2, '1983'); fr = appear(fr, C, (1150, 440, 1590, 780), t, ty, 0.9)
    fr = label(fr, 'RULES CHANGED', 850, 60, white, t, ty + 0.6, 1370)
    return frame(fr)

def b29b(t):
    fr = base(t); fr = title(fr, 'NO PROMISES', t, 60)
    C = new(); shield(C, 520, 540, 1.7, blue); txt(C, 'i', BOLD(220), 400, white, 255, x=520); fr = appear(fr, C, (280, 240, 760, 860), t, 0.3, 1.0)
    fr = label(fr, 'NOBODY CAN PROMISE', 330, 72, white, t, 0.8, 1340)
    fr = label(fr, 'THIS VIDEO IS', 500, 60, white, t, 1.8, 1340)
    fr = label(fr, 'EDUCATION,', 610, 96, goldL, t, 2.2, 1340)
    fr = label(fr, 'NOT ADVICE', 730, 96, goldL, t, 2.6, 1340)
    return frame(fr)

def b29c(t):
    T = lambda m: B29.T(2, m)
    fr = base(t); fr = title(fr, 'A SMART WAY TO PLAN', t, 58)
    C = new(); magnifier(C, 300, 500, 100); fr = appear(fr, C, (160, 360, 520, 720), t, 0.3, 0.9)
    fr = label(fr, 'LOOK AT YOUR OWN NUMBER', 250, 56, white, t, 0.6, 1150)
    fr = pc(fr, (560, 320, 1240, 620), t, 0.9, green, '$ ?', 'YOUR BENEFIT', sub='', size=130)
    tt_ = T('test what happens')
    C = new(); arrow_r(C, 1265, 1395, 470, goldL, 255, 14); fr = appear(fr, C, (1255, 430, 1405, 510), t, tt_, 0.6)
    fr = pc(fr, (1420, 320, 1810, 620), t, tt_ + 0.3, red, '-20%', 'TEST', sub='', size=120)
    fr = label(fr, 'ABOUT A FIFTH SMALLER', 760, 76, red, t, T('a fifth') , 1150)
    return frame(fr)

# ======================= BLOCK 30 =======================
B30 = mk(30, [[0, 1, 2], [3, 4], [5]])

def card5(C, n, txt1, txt2, col, y, icon=None):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([140, y, 1780, y + 290], radius=30, fill=A(card, 255), outline=A(col, 255), width=6)
    d.ellipse([190, y + 75, 340, y + 225], fill=A(col, 255)); txt(C, str(n), BOLD(110), y + 92, navy, 255, x=265)
    txt(C, txt1, BOLD(66), y + 60, white, 255, x=1010); txt(C, txt2, BOLD(54), y + 165, goldL, 255, x=1010)
    if icon: icon(C, 1650, y + 145)

def ic_cal(C, x, y): cal_icon(C, x, y, 0.55, '35')
def ic_coins(C, x, y): coin_stack(C, x, y + 90, 6, 44)
def ic_pct(C, x, y): txt(C, '124%', BOLD(60), y - 40, green, 255, x=x)
def ic_up(C, x, y): up_arrow(C, x, y, 0.9, green)
def ic_pair(C, x, y): person(C, x - 45, y + 20, blue, 1.8); person(C, x + 45, y + 20, purple, 1.8)

def b30a(t):
    T = lambda m: B30.T(0, m)
    fr = base(t); fr = title(fr, 'THE FIVE THINGS', t, 60)
    C = new(); card5(C, 1, 'BEST 35 YEARS COUNT', 'MISSING YEARS ARE ZEROS', gold, 230, ic_cal); fr = appear(fr, C, (130, 220, 1790, 530), t, T('One'), 0.9)
    C = new(); card5(C, 2, 'BIGGER SLICE IF YOU EARN LESS', 'THE FORMULA GIVES BACK MORE', blue, 590, ic_coins); fr = appear(fr, C, (130, 580, 1790, 890), t, T('Two'), 0.9)
    return frame(fr)

def b30b(t):
    T = lambda m: B30.T(1, m)
    fr = base(t); fr = title(fr, 'THE FIVE THINGS', t, 60)
    C = new(); card5(C, 3, '62 = 70%   ·   70 = 124%', 'WHEN YOU CLAIM CHANGES THE CHECK', green, 230, ic_up); fr = appear(fr, C, (130, 220, 1790, 530), t, 0.4, 0.9)
    C = new(); card5(C, 4, 'EARNINGS WITHHELD', 'THEY COME BACK LATER', red, 590, ic_up); fr = appear(fr, C, (130, 580, 1790, 890), t, T('Four'), 0.9)
    return frame(fr)

def b30c(t):
    fr = base(t); fr = title(fr, 'THE FIVE THINGS', t, 60)
    C = new(); card5(C, 5, 'SPOUSES AND SURVIVORS', 'HAVE THEIR OWN RULES', purple, 230, ic_pair); fr = appear(fr, C, (130, 220, 1790, 530), t, 0.4, 0.9)
    for k in range(5):
        C = new(); check(C, 480 + k * 240, 720, 70, green); txt(C, str(k + 1), BOLD(64), 810, white, 255, x=480 + k * 240)
        fr = appear(fr, C, (390 + k * 240, 630, 570 + k * 240, 900), t, 1.0 + k * 0.3, 0.6)
    return frame(fr)

# ======================= BLOCK 31 =======================
B31 = mk(31, [[0], [1, 2]])

def b31a(t):
    fr = base(t); fr = title(fr, 'THE MONEY BACKSTORY', t, 60)
    C = new(); thumb(C, 560, 480, 2.4); fr = appear(fr, C, (270, 300, 860, 780), t, 0.3, 0.9)
    fr = label(fr, 'LIKE', 810, 84, goldL, t, 0.6, 560)
    C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1130, 430, 1770, 590], radius=40, fill=A(red, 255), outline=A((255, 200, 200), 255), width=5)
    txt(C, 'SUBSCRIBE', BOLD(80), 462, white, 255, x=1450); fr = appear(fr, C, (1120, 420, 1780, 600), t, 1.0, 0.9)
    fr = label(fr, 'DO NOT MISS THE NEXT ONE', 720, 48, white, t, 1.6, 1440)
    return frame(fr)

def b31b(t):
    T = lambda m: B31.T(1, m)
    fr = base(t); fr = title(fr, 'THE EXACT MATH', t, 60)
    fr = label(fr, 'CLAIMING AT', 300, 60, white, t, 0.3, 560)
    fr = label(fr, '62 vs 70', 400, 170, goldL, t, 0.6, 560)
    C = new(); coin_stack(C, 300, 900, 5, 56); coin_stack(C, 820, 900, 10, 56); fr = appear(fr, C, (200, 620, 900, 930), t, 1.2, 0.9)
    C = new(); dashed(C, 1040, 290, 1800, 718); fr = appear(fr, C, (1020, 270, 1820, 740), t, 0.4, 0.8)
    L = new(); txt(L, 'WATCH NEXT', BOLD(70), 470, goldL, 255 * E(t, 0.9, 0.8), x=1420); Image.alpha_composite(fr, L); fr = Image.alpha_composite(fr, L)
    C = new(); arrow_d(C, 1420, 780, 900, goldL, 255, 14); fr = appear(fr, C, (1370, 770, 1470, 910), t, 1.6, 0.6)
    return frame(fr)

SL = {21: [b21a, b21b, b21c], 22: [b22a, b22b, b22c], 23: [b23a, b23b, b23c], 24: [b24a, b24b, b24c], 25: [b25a, b25b, b25c],
      26: [b26a, b26b, b26c], 27: [b27a, b27b, b27c], 28: [b28a, b28b, b28c], 29: [b29a, b29b, b29c], 30: [b30a, b30b, b30c], 31: [b31a, b31b]}
FSD = {21: B21.FS, 22: B22.FS, 23: B23.FS, 24: B24.FS, 25: B25.FS, 26: B26.FS, 27: B27.FS, 28: B28.FS, 29: B29.FS, 30: B30.FS, 31: B31.FS}

if __name__ == '__main__':
    run_cli('b21_31', SL, FSD, None)
