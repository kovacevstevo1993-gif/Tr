import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8b1 import *
from v6b2 import logo

def two_line(C, x, y, a, b, size, col=white):
    txt(C, a, fit(a, 640, size), y, col, 255, x=x); txt(C, b, fit(b, 640, size), y + size + 14, col, 255, x=x)

def initials(C, cx, cy, letter, r=62, col=gold):
    d = ImageDraw.Draw(C); d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (255,), outline=white + (255,), width=4)
    txt(C, letter, BOLD(int(r * 1.15)), cy - r * 0.62, navy, 255, x=cx)

def house(C, cx, cy, s=1.0, col=gold):
    d = ImageDraw.Draw(C)
    d.polygon([(cx - 100 * s, cy), (cx, cy - 90 * s), (cx + 100 * s, cy)], fill=col + (255,), outline=white + (255,))
    d.rectangle([cx - 78 * s, cy, cx + 78 * s, cy + 90 * s], fill=(236, 240, 245, 255), outline=col + (255,), width=4)
    d.rectangle([cx - 20 * s, cy + 25 * s, cx + 20 * s, cy + 90 * s], fill=col + (255,))
    d.rectangle([cx + 40 * s, cy + 20 * s, cx + 70 * s, cy + 50 * s], fill=blue + (255,))

BN = ['PROPERTY TAX', 'TAX ON SOCIAL SECURITY', 'INCOME TAX', 'MEDICARE PART B']

# ======================= BLOCCO 2 =======================
def s2a(t):
    fr = stage_live(t, 'TWO COMMON ASSUMPTIONS', 91, 58)
    t1, t2 = tm('struggling', LASTP() - 1.8), tm('wealthy', LASTP() - 0.9)
    for (x0, x1, tk, col, head, a, b, ic) in [(130, 900, t1, red, 'ASSUMPTION 1', 'ONLY FOR PEOPLE', 'WHO STRUGGLE', 'w'), (1020, 1790, t2, gold, 'ASSUMPTION 2', 'ONLY FOR THE WEALTHY', 'WITH LAWYERS', 'b')]:
        if t > tk:
            C = new(); card_(C, x0, 250, x1, 700, col, head, None, None); cx = (x0 + x1) / 2
            if ic == 'w': wallet(C, cx, 400, 1.3)
            else: building(C, cx, 410, 260, 210, gold)
            two_line(C, cx, 530, a, b, 48)
            fr = P2(fr, C, (x0 - 20, 230, x1 + 20, 720), t, tk)
    return frame(pill_last(fr, t, 'TWO REASONS TO TUNE OUT', PILL_Y, red, (255, 255, 255), 54))

def s2b(t):
    fr = stage_live(t, 'BOTH GROUPS ARE WRONG', 92, 60)
    t1, t2, t3 = tm('wrong', LASTP() - 3.0), tm('wrong', LASTP() - 2.7), tm('thousand', LASTP() - 0.9)
    for x0, x1, lab, tk in [(200, 900, 'STRUGGLING', t1), (1020, 1720, 'WEALTHY', t2)]:
        if t > tk:
            C = new(); card_(C, x0, 240, x1, 400, grey, None, lab, None, 64, (170, 185, 205)); cross(C, (x0 + x1) / 2 + 280, 270, 52, red)
            fr = P2(fr, C, (x0 - 20, 220, x1 + 20, 420), t, tk)
    if t > t3:
        C = new(); card_(C, 380, 460, 1540, 740, gold, 'A COUPLE ON SOCIAL SECURITY + A MODEST IRA', '$1,000+', 'SAVED EVERY YEAR', 120, goldL)
        fr = P2(fr, C, (360, 440, 1560, 760), t, t3)
    return frame(pill_last(fr, t, 'THE EXACT MATH IS COMING', PILL_Y, gold, navy, 54))

# ======================= BLOCCO 3 =======================
def s3a(t):
    fr = stage_live(t, 'FIVE BILLS AFTER 65', 93)
    t1 = tm('five', 3.0)
    if t > t1:
        C = new(); ring_(C, 520, 450, 190, 1.0 * ease((t - t1) / 0.8), gold, 40)
        txt(C, '5', BOLD(230), 340, goldL, 255, x=520); txt(C, 'BILLS', BOLD(60), 662, white, 255, x=520)
        fr = P2(fr, C, (300, 230, 740, 740), t, t1)
    rows = [('STOP', red, tm('stop', LASTP() - 1.7)), ('LOWER', green, tm('lower', LASTP() - 1.1)), ('FREEZE', blue, tm('freeze', LASTP() - 0.5))]
    for k, (nm, col, tk) in enumerate(rows):
        if t > tk:
            C = new(); y = 250 + k * 170; d = ImageDraw.Draw(C)
            d.rounded_rectangle([900, y, 1790, y + 140], radius=30, fill=card + (255,), outline=col + (255,), width=6)
            if k == 0: cross(C, 1010, y + 70, 48, red)
            elif k == 1: arrow_d(C, 1010, y + 30, y + 112, green, 255, 14)
            else: padlock(C, 1010, y + 70, 0.62, blue)
            txt(C, nm, BOLD(76), y + 28, white, 255, x=1400)
            fr = P2(fr, C, (880, y - 20, 1810, y + 160), t, tk)
    return frame(pill_last(fr, t, 'STOP, LOWER, OR FREEZE', PILL_Y, gold, navy, 54))

def s3b(t):
    fr = stage_live(t, 'STAY FOR NUMBER FIVE', 94)
    ts = [0.35 + 0.28 * k for k in range(5)]
    for k in range(5):
        if t > ts[k] and k < 4:
            C = new(); cx = 330 + k * 290; d = ImageDraw.Draw(C)
            d.ellipse([cx - 75, 290, cx + 75, 440], fill=card + (255,), outline=(120, 140, 170, 255), width=6); txt(C, str(k + 1), BOLD(86), 312, (150, 165, 190), 255, x=cx)
            fr = P2(fr, C, (cx - 90, 270, cx + 90, 460), t, ts[k])
    t5 = tm('number five', LASTP() - 1.5)
    if t > t5:
        C = new(); cx = 1490; d = ImageDraw.Draw(C)
        d.ellipse([cx - 120, 250, cx + 120, 490], fill=gold + (255,), outline=white + (255,), width=6); txt(C, '5', BOLD(170), 280, navy, 255, x=cx)
        txt(C, 'THE BIGGEST ONE', BOLD(44), 520, goldL, 255, x=cx)
        fr = P2(fr, C, (cx - 300, 230, cx + 300, 580), t, t5)
    tp = tm('single phone call', LASTP() - 0.7)
    if t > tp:
        C = new(); phone(C, 380, 650, 0.95, 255, t - tp, True)
        txt(C, 'ONE PHONE CALL', BOLD(64), 620, white, 255, x=900, anchor='c')
        fr = P2(fr, C, (200, 500, 1200, 790), t, tp)
    return frame(pill_last(fr, t, 'THE BIGGEST ONE ON THE LIST', PILL_Y, gold, navy, 54))

# ======================= BLOCCO 4 =======================
def s4a(t):
    fr = stage_live(t, 'THE MONEY BACKSTORY', 95)
    t1 = tm('Welcome', 1.2)
    if t > t1:
        C = new(); logo(C, 520, 470, 200); fr = P2(fr, C, (290, 230, 750, 710), t, t1)
    for k, (tx, key, lim) in enumerate([('RETIREMENT', 'retirement', 1.9), ('FOR AMERICANS OVER 50', 'Americans', 1.3), ('OFFICIAL NUMBERS', 'official', 0.7)]):
        tk = tm(key, LASTP() - lim)
        if t > tk:
            C = new(); y = 270 + k * 150; card_(C, 960, y, 1790, y + 120, gold if k < 2 else green, None, tx, None, 56, white)
            fr = P2(fr, C, (940, y - 20, 1810, y + 140), t, tk)
    return frame(pill_last(fr, t, 'EXPLAINED WITH OFFICIAL NUMBERS', PILL_Y, green, navy, 52))

def s4b(t):
    fr = stage_live(t, 'MEET FRANK AND MARY', 96)
    for k, (nm, key, lim) in enumerate([('FRANK', 'Frank', 3.6), ('MARY', 'Mary', 3.0)]):
        tk = tm(key, LASTP() - lim)
        if t > tk:
            C = new(); y = 250 + k * 200; card_(C, 130, y, 880, y + 170, blue if k == 0 else pink, None, None, None)
            initials(C, 250, y + 85, nm[0]); txt(C, nm, BOLD(70), y + 22, white, 255, x=520)
            fr = P2(fr, C, (110, y - 20, 900, y + 190), t, tk)
    ta = tm('Both', LASTP() - 2.4)
    if t > ta:
        C = new()
        for k in range(2): txt(C, 'AGE 66', BOLD(54), 250 + k * 200 + 95, goldL, 255, x=520)
        fr = P2(fr, C, (300, 330, 760, 690), t, ta)
    tt_ = tm('Together', LASTP() - 0.9)
    if t > tt_:
        C = new(); paycheck(C, 1000, 250, 1790, 640, blue, '$3,600', 'PER MONTH, TOGETHER', 'SOCIAL SECURITY', 130)
        fr = P2(fr, C, (980, 230, 1810, 660), t, tt_)
    return frame(pill_last(fr, t, 'A MARRIED COUPLE, BOTH 66', PILL_Y, gold, navy, 54))

# ======================= BLOCCO 5 =======================
def s5a(t):
    fr = stage_live(t, 'THEIR INCOME AND HOME', 97)
    t1, t2 = tm('forty', LASTP() - 1.6), tm('own', LASTP() - 0.8)
    if t > t1:
        C = new(); card_(C, 130, 260, 900, 640, gold, "FRANK'S TRADITIONAL IRA", '$40,000', 'TAKEN EACH YEAR', 130, goldL)
        fr = P2(fr, C, (110, 240, 920, 660), t, t1)
    if t > t1 + 0.2:
        L = new(); txt(L, '+', BOLD(120), 380, goldL, 255 * E_(t, t1 + 0.2, 0.3), x=960); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); card_(C, 1020, 260, 1790, 640, green, None, None, None); house(C, 1405, 355, 1.3, green); txt(C, 'THEY OWN', BOLD(46), 490, goldL, 255, x=1405); txt(C, 'THEIR HOME', BOLD(62), 545, white, 255, x=1405)
        fr = P2(fr, C, (1000, 240, 1810, 660), t, t2)
    return frame(pill_last(fr, t, 'AN IRA AND THEIR OWN HOME', PILL_Y, gold, navy, 54))

def s5b(t):
    fr = stage_live(t, 'A VERY NORMAL RETIRED COUPLE', 98, 56)
    t1, t2 = tm('Nothing', 3.2), tm('bills', LASTP() - 1.6)
    if t > t1:
        C = new(); card_(C, 130, 250, 760, 520, blue, None, None, None); two_line(C, 445, 290, 'NOTHING', 'SPECIAL', 84)
        initials(C, 330, 590, 'F', 56, blue); initials(C, 560, 590, 'M', 56, pink)
        fr = P2(fr, C, (110, 230, 780, 680), t, t1)
    if t > t2:
        C = new(); magnifier(C, 880, 420, 90, goldL); fr = P2(fr, C, (760, 300, 1100, 640), t, t2)
    for k, nm in enumerate(BN):
        tk = t2 + 0.2 + 0.3 * k
        if t > tk:
            C = new(); y = 250 + k * 130; d = ImageDraw.Draw(C)
            d.rounded_rectangle([1100, y, 1800, y + 108], radius=26, fill=card + (255,), outline=gold + (255,), width=5)
            txt(C, nm, fit(nm, 470, 42), y + 30, white, 255, x=1365); d.ellipse([1715, y + 24, 1775, y + 84], fill=red + (255,)); txt(C, '?', BOLD(48), y + 32, white, 255, x=1745)
            fr = P2(fr, C, (1080, y - 20, 1820, y + 128), t, tk)
    return frame(pill_last(fr, t, 'WHICH BILLS DO THEY PAY?', PILL_Y, red, (255, 255, 255), 54))

SLIDES = {2: [frozen(s2a), frozen(s2b)], 3: [frozen(s3a), frozen(s3b)], 4: [frozen(s4a), frozen(s4b)], 5: [frozen(s5a), frozen(s5b)]}
if __name__ == '__main__':
    SPEC = {b: V.plan(b, 2) for b in SLIDES}
    if sys.argv[1] == 'spec': print(SPEC, {b: sum(v) for b, v in SPEC.items()})
    else: run(SPEC, SLIDES, 'v8', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
