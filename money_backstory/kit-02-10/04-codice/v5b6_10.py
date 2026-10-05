from v5lib import *

def count(t, t0, dur, v): return v * ease((t - t0) / dur)

# ======================= BLOCK 6 =======================
S6 = ["Let's see what that does to Frank and Mary.", "Say both earn the equivalent of about seventy two thousand dollars a year in today's wages.",
      "Mary has thirty five years, so her average is six thousand dollars a month.",
      "Frank has only thirty years, so five zero years pull his average down to about five thousand one hundred forty three dollars a month."]
B6 = Blk(6, S6, [[0, 1], [2], [3]])

def b6a(t):
    T = lambda m: B6.tt(0, m)
    fr = base(t); fr = title(fr, 'FRANK AND MARY', t)
    for nm, cx, col, t0 in [('FRANK', 520, blue, 0.4), ('MARY', 1400, green, 0.9)]:
        C = new(); person(C, cx, 470, col, 3.0); txt(C, nm, BOLD(60), 640, col, 255, x=cx); fr = appear(fr, C, (cx - 190, 280, cx + 190, 720), t, t0, 1.0)
    te = T('both earn'); tn = T('seventy two')
    fr = label(fr, '=', 380, 190, goldL, t, te, 960)
    for cx in (520, 1400):
        L = new(); txt(L, '$72,000', BOLD(110), 735, goldL, 255 * E(t, tn, 1.0), x=cx); txt(L, "A YEAR IN TODAY'S WAGES", BOLD(40), 860, white, 255 * E(t, tn + 0.4, 1.0), x=cx)
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b6b(t):
    fr = base(t); fr = title(fr, 'MARY: 35 YEARS OF WORK', t)
    C = new(); person(C, 290, 520, green, 2.8); txt(C, 'MARY', BOLD(56), 695, green, 255, x=290); fr = appear(fr, C, (120, 300, 460, 720), t, 0.2, 0.8)
    C = new(); tile(C, 480, 430, 200, gold, '35'); txt(C, 'YEARS', BOLD(50), 660, goldL, 255, x=580); fr = appear(fr, C, (465, 420, 700, 720), t, 0.6, 0.8)
    L = new(); arrow_r(L, 720, 900, 540, goldL, 255 * E(t, 1.1, 0.6)); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'HER AVERAGE', 290, 54, grey, t, 1.1, 1420)
    L = new(); txt(L, money(count(t, 1.3, 2.2, 6000)), BOLD(200), 370, goldL, 255 * E(t, 1.3, 0.6), x=1420); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'A MONTH', 610, 72, white, t, 1.6, 1420)
    return frame(fr)

def b6c(t):
    T = lambda m: B6.tt(2, m)
    fr = base(t); fr = title(fr, 'FRANK: 30 YEARS + 5 ZERO YEARS', t, 54)
    C = new(); person(C, 250, 520, blue, 2.6); txt(C, 'FRANK', BOLD(56), 650, blue, 255, x=250); fr = appear(fr, C, (90, 300, 420, 720), t, 0.2, 0.8)
    C = new(); tile(C, 410, 440, 160, gold, '30'); txt(C, 'YEARS', BOLD(44), 620, goldL, 255, x=490); fr = appear(fr, C, (395, 430, 590, 690), t, 0.6, 0.8)
    fr = label(fr, '+', 470, 100, goldL, t, 1.0, 640)
    tz = T('five zero years')
    for k in range(5):
        st = tz + k * 0.35
        x = 700 + k * 82
        if t > st:
            C = new(); tile(C, x, 470, 72, red, '0', fill=red, outline=(255, 150, 150)); fr = appear(fr, C, (x - 6, 460, x + 80, 560), t, st, 0.5)
    fr = label(fr, '5 ZERO YEARS', 590, 40, red, t, tz + 0.3, 905)
    L = new(); txt(L, '$6,000', BOLD(90), 240, grey, 170 * E(t, 0.6, 0.8), x=1470)
    if t > tz + 0.5: strike(L, 1250, 1690, 292, red, 255 * E(t, tz + 0.5, 0.6), 10)
    fr = Image.alpha_composite(fr, L)
    td = T('pull his average')
    v = 6000 - 857 * ease((t - td) / 2.0)
    L = new(); txt(L, money(v), BOLD(190), 380, red, 255 * E(t, td - 0.2, 0.6), x=1470); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'A MONTH', 610, 72, white, t, td + 0.3, 1470)
    return frame(fr)

# ======================= BLOCK 7 =======================
S7 = ["That gap looks small, but watch the final check.", "Mary's full benefit comes out to two thousand six hundred sixty five dollars and eighty cents a month.",
      "Frank's is only two thousand three hundred ninety one dollars and fifty cents.",
      "That is two hundred seventy four dollars less every month, about three thousand two hundred ninety two dollars a year.",
      "Over twenty years, before any raises, that is more than sixty five thousand dollars."]
B7 = Blk(7, S7, [[0, 1], [2], [3], [4]])

def b7a(t):
    T = lambda m: B7.tt(0, m)
    fr = base(t); fr = title(fr, "MARY'S FULL BENEFIT", t)
    C = new(); person(C, 250, 520, green, 2.6); txt(C, 'MARY', BOLD(56), 695, green, 255, x=250); fr = appear(fr, C, (90, 300, 420, 720), t, 0.2, 0.8)
    tm = T("Mary's full benefit")
    v = count(t, tm + 0.7, 3.0, 2665.80)
    C = new(); paycheck(C, 520, 250, 1480, 780, green, money(v, True) if t > tm + 0.5 else '$ ?', sub='PER MONTH', head='MARY: MONTHLY CHECK', size=150)
    fr = appear(fr, C, (510, 240, 1490, 790), t, 0.4, 0.9)
    C = new(); coin_stack(C, 1680, 760, 8, 72); fr = appear(fr, C, (1590, 520, 1780, 800), t, tm + 0.4, 1.0)
    return frame(fr)

def b7b(t):
    fr = base(t); fr = title(fr, "FRANK'S FULL BENEFIT", t)
    C = new(); person(C, 250, 500, blue, 2.6); txt(C, 'FRANK', BOLD(56), 630, blue, 255, x=250); fr = appear(fr, C, (90, 290, 420, 700), t, 0.2, 0.8)
    v = count(t, 0.6, 2.4, 2391.50)
    C = new(); paycheck(C, 520, 230, 1480, 740, blue, money(v, True), sub='PER MONTH', head='FRANK: MONTHLY CHECK', size=150)
    fr = appear(fr, C, (510, 220, 1490, 750), t, 0.4, 0.9)
    fr = chip(fr, "MARY: $2,665.80", 960, 810, t, 3.0, green, 46)
    return frame(fr)

def b7c(t):
    T = lambda m: B7.tt(2, m)
    fr = base(t); fr = title(fr, 'THE DIFFERENCE', t)
    ta = T('two hundred seventy four'); tb = T('about three thousand')
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    for m in range(12):
        st = ta + 0.6 + m * 0.22
        if t < st: continue
        x = 120 + (m % 4) * 240; y = 260 + (m // 4) * 210
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([x, y, x + 210, y + 180], radius=22, fill=A(card, 255), outline=A(red, 255), width=4)
        txt(C, months[m], BOLD(40), y + 20, white, 255, x=x + 105); txt(C, '-$274', BOLD(52), y + 90, red, 255, x=x + 105)
        fr = appear(fr, C, (x - 6, y - 6, x + 216, y + 186), t, st, 0.5)
    L = new(); txt(L, '-$274', BOLD(190), 250, red, 255 * E(t, ta, 0.9), x=1440); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'EVERY MONTH', 450, 58, white, t, ta + 0.3, 1440)
    L = new(); txt(L, '-$3,292', BOLD(170), 560, red, 255 * E(t, tb, 0.9), x=1440); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'A YEAR', 760, 66, goldL, t, tb + 0.3, 1440)
    return frame(fr)

def b7d(t):
    T = lambda m: B7.tt(3, m)
    fr = base(t); fr = title(fr, 'OVER TWENTY YEARS', t)
    for k in range(5):
        st = 0.3 + k * 0.5
        if t < st: continue
        C = new(); coin_stack(C, 190 + k * 130, 800, 3 + 2 * k, 50); fr = appear(fr, C, (110 + k * 130, 800 - (3 + 2 * k) * 20 - 60, 270 + k * 130, 830), t, st, 0.7)
    tm = T('more than sixty five')
    L = new(); txt(L, '$' + f'{int(count(t, tm, 1.8, 65000)):,}' + ('+' if t > tm + 1.8 else ''), BOLD(200), 300, red, 255 * E(t, tm - 0.2, 0.6), x=1340); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'LESS IN 20 YEARS', 540, 62, white, t, tm + 0.3, 1340)
    fr = chip(fr, 'BEFORE ANY RAISES', 1340, 680, t, T('before any raises'), gold, 50)
    return frame(fr)

# ======================= BLOCK 8 =======================
S8 = ["So what can you do about it?", "If you are still working and you have fewer than thirty five years, every extra year of work replaces one of those zeros.",
      "Even a modest year is better than a zero.", "And you can check your own record for free, inside your my Social Security account at ssa dot gov.",
      "Look for missing years, because mistakes do happen."]
B8 = Blk(8, S8, [[0, 1, 2], [3, 4]])
G8X, G8Y, G8S, G8P = 150, 250, 92, 108
def g8(i): return G8X + (i % 7) * G8P, G8Y + (i // 7) * G8P

def b8a(t):
    T = lambda m: B8.tt(0, m)
    fr = base(t); fr = title(fr, 'WHAT CAN YOU DO ABOUT IT?', t)
    C = new()
    for i in range(30):
        x, y = g8(i); tile(C, x, y, G8S, gold, str(i + 1))
    fr = appear(fr, C, (G8X - 10, G8Y - 10, G8X + 6 * G8P + G8S + 10, G8Y + 4 * G8P + G8S + 20), t, 0.3, 1.0)
    tc = T('every extra year')
    for k in range(5):
        x, y = g8(30 + k); st = tc + 0.3 + k * 1.0
        C = new()
        if t > st: tile(C, x, y, G8S, gold, str(31 + k)); fr = appear(fr, C, (x - 8, y - 8, x + G8S + 8, y + G8S + 16), t, st, 0.6)
        else: tile(C, x, y, G8S, red, '0', fill=red, outline=(255, 150, 150)); fr = appear(fr, C, (x - 8, y - 8, x + G8S + 8, y + G8S + 16), t, 0.6, 0.9)
    fr = label(fr, 'STILL WORKING?', 260, 66, white, t, T('still working'), 1400)
    fr = label(fr, 'FEWER THAN 35 YEARS?', 350, 54, goldL, t, T('fewer than thirty five'), 1400)
    fr = label(fr, 'EVERY EXTRA YEAR', 480, 62, white, t, tc, 1400); fr = label(fr, 'REPLACES A ZERO', 560, 62, green, t, tc + 0.4, 1400)
    fr = label(fr, 'EVEN A SMALL YEAR', 710, 56, goldL, t, T('Even a modest'), 1400); fr = label(fr, 'BEATS A ZERO', 785, 56, goldL, t, T('Even a modest') + 0.3, 1400)
    return frame(fr)

def b8b(t):
    T = lambda m: B8.tt(1, m)
    fr = base(t); fr = title(fr, "CHECK YOUR RECORD. IT'S FREE.", t, 56)
    X0, Y0, X1, Y1 = 260, 230, 1660, 850
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([X0, Y0, X1, Y1], radius=26, fill=(236, 240, 245, 255), outline=A(goldL, 255), width=5)
    d.rounded_rectangle([X0, Y0, X1, Y0 + 80], radius=26, fill=(40, 52, 74, 255)); d.rectangle([X0, Y0 + 50, X1, Y0 + 80], fill=(40, 52, 74, 255))
    for k, cc in enumerate([red, gold, green]): d.ellipse([X0 + 30 + k * 36, Y0 + 30, X0 + 50 + k * 36, Y0 + 50], fill=A(cc, 255))
    d.rounded_rectangle([X0 + 170, Y0 + 14, X0 + 600, Y0 + 66], radius=26, fill=(90, 104, 130, 255)); txt(C, 'ssa.gov', BOLD(36), Y0 + 22, (255, 255, 255), 255, x=X0 + 200, anchor='l')
    d.rectangle([X0, Y0 + 80, X1, Y0 + 165], fill=A(blue, 255)); txt(C, 'my Social Security', BOLD(56), Y0 + 96, (255, 255, 255), 255, x=(X0 + X1) / 2)
    txt(C, 'EXAMPLE OF AN EARNINGS RECORD', BOLD(38), Y0 + 185, (70, 84, 108), 255, x=(X0 + X1) / 2)
    fr = appear(fr, C, (X0 - 10, Y0 - 10, X1 + 10, Y1 + 10), t, 0.3, 0.9)
    tr = T('check your own record'); tm = T('Look for missing')
    rows = [('2019', '$61,200'), ('2020', '$62,900'), ('2021', 'NOTHING SHOWN'), ('2022', '$65,700'), ('2023', '$67,100')]
    for i, (yr, amt) in enumerate(rows):
        st = tr + 0.3 + i * 0.5
        if t < st: continue
        y = Y0 + 260 + i * 68
        C = new(); d = ImageDraw.Draw(C)
        miss = (i == 2)
        if miss and t > tm: d.rounded_rectangle([X0 + 60, y - 8, X1 - 60, y + 58], radius=14, fill=(255, 215, 215, 255), outline=A(red, 255), width=4)
        txt(C, yr, BOLD(46), y, navy, 255, x=X0 + 130, anchor='l'); txt(C, amt, BOLD(46), y, red if miss and t > tm else navy, 255, x=X0 + 500, anchor='l')
        if not miss: check(C, X1 - 160, y + 26, 24, green)
        fr = appear(fr, C, (X0 + 40, y - 14, X1 - 40, y + 64), t, st, 0.5)
    if t > tm:
        C = new(); magnifier(C, 1250, 640, 60, goldL); fr = appear(fr, C, (1160, 560, 1440, 800), t, tm, 0.8)
    fr = chip(fr, 'MISTAKES DO HAPPEN', 960, 875, t, T('mistakes'), red, 44, filled=red, tcol=(255, 255, 255))
    return frame(fr)

# ======================= BLOCK 9 =======================
S9 = ["Number two: the formula.", "Once Social Security has your best thirty five years, it adds them up and divides by four hundred twenty months.",
      "That gives what it calls your average indexed monthly earnings.",
      "Then it runs that number through a formula with three slices, and this is where things get interesting."]
B9 = Blk(9, S9, [[0, 1], [2], [3]])

def b9a(t):
    T = lambda m: B9.tt(0, m)
    fr = base(t); fr = title(fr, 'NUMBER TWO: THE FORMULA', t)
    C = new()
    for i in range(35): tile(C, 130 + (i % 7) * 76, 330 + (i // 7) * 76, 64, gold)
    fr = appear(fr, C, (120, 320, 670, 700), t, 0.4, 1.0)
    fr = label(fr, 'YOUR BEST 35 YEARS', 245, 46, goldL, t, 0.6, 400)
    ta = T('adds them up'); td = T('divides by')
    L = new(); arrow_r(L, 700, 870, 520, goldL, 255 * E(t, ta, 0.7)); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'ADD THEM UP', 430, 36, goldL, t, ta, 835)
    C = new(); calculator(C, 1090, 500, 1.5); fr = appear(fr, C, (930, 300, 1250, 700), t, td, 0.9)
    fr = label(fr, 'DIVIDE BY', 300, 48, grey, t, td + 0.3, 1560)
    L = new(); txt(L, '420', BOLD(200), 350, goldL, 255 * E(t, td + 0.5, 0.9), x=1560); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'MONTHS', 590, 60, white, t, td + 0.8, 1560)
    fr = label(fr, '35 YEARS x 12 MONTHS', 690, 40, grey, t, td + 1.2, 1560, bold=False)
    return frame(fr)

def b9b(t):
    T = lambda m: B9.tt(1, m)
    fr = base(t); fr = title(fr, 'THE RESULT', t)
    fr = label(fr, 'YOUR AVERAGE', 230, 120, goldL, t, T('your average'), 860)
    fr = label(fr, 'INDEXED', 380, 120, white, t, T('indexed'), 860)
    fr = label(fr, 'MONTHLY EARNINGS', 530, 104, goldL, t, T('monthly earnings'), 860)
    fr = label(fr, 'of your best 35 years, in today\'s wages', 720, 46, grey, t, T('monthly earnings') + 0.6, 860, bold=False)
    C = new(); wallet(C, 1610, 520, 1.5); fr = appear(fr, C, (1400, 360, 1820, 700), t, T('monthly earnings') + 0.3, 1.0)
    return frame(fr)

def b9c(t):
    T = lambda m: B9.tt(2, m)
    fr = base(t); fr = title(fr, 'A FORMULA WITH THREE SLICES', t, 56)
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([130, 350, 560, 670], radius=30, fill=A(card, 255), outline=A(goldL, 255), width=5)
    txt(C, 'YOUR AVERAGE', BOLD(44), 385, white, 255, x=345); txt(C, '$6,000', BOLD(96), 460, goldL, 255, x=345); txt(C, 'MARY', BOLD(44), 590, green, 255, x=345)
    fr = appear(fr, C, (120, 340, 570, 680), t, 0.3, 0.9)
    L = new(); arrow_r(L, 580, 700, 510, goldL, 255 * E(t, 0.9, 0.6)); fr = Image.alpha_composite(fr, L)
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([720, 290, 1200, 740], radius=30, fill=A(card, 255), outline=A(gold, 255), width=6)
    txt(C, 'THE FORMULA', BOLD(50), 315, goldL, 255, x=960)
    for k in range(3): d.rounded_rectangle([760, 400 + k * 105, 1160, 485 + k * 105], radius=18, outline=A((80, 100, 130), 255), width=3)
    fr = appear(fr, C, (710, 280, 1210, 750), t, 1.3, 0.9)
    ts = T('three slices'); cols = [gold, blue, purple]
    for k in range(3):
        st = ts + k * 0.9
        if t > st:
            C = new(); d = ImageDraw.Draw(C)
            d.rounded_rectangle([760, 400 + k * 105, 1160, 485 + k * 105], radius=18, fill=A(cols[k], 255)); txt(C, f'SLICE {k + 1}', BOLD(50), 415 + k * 105, navy, 255, x=960)
            fr = appear(fr, C, (750, 390 + k * 105, 1170, 495 + k * 105), t, st, 0.6)
    L = new(); arrow_r(L, 1220, 1340, 510, goldL, 255 * E(t, 2.0, 0.6)); fr = Image.alpha_composite(fr, L)
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([1360, 350, 1790, 670], radius=30, fill=A(card, 255), outline=A(green, 255), width=5)
    txt(C, 'YOUR CHECK', BOLD(44), 385, white, 255, x=1575); txt(C, '$ ?', BOLD(120), 470, green, 255, x=1575)
    fr = appear(fr, C, (1350, 340, 1800, 680), t, 2.2, 0.9)
    return frame(fr)

# ======================= BLOCK 10 =======================
S10 = ["For people turning sixty two in twenty twenty six, the formula works like this.", "You get ninety percent of the first one thousand two hundred eighty six dollars.",
       "Then thirty two percent of everything between one thousand two hundred eighty six and seven thousand seven hundred forty nine dollars.",
       "And only fifteen percent of anything above that."]
B10 = Blk(10, S10, [[0, 1], [2, 3]])

def b10a(t):
    T = lambda m: B10.tt(0, m)
    fr = base(t); fr = title(fr, 'THE FORMULA FOR 2026', t)
    fr = label(fr, 'FOR PEOPLE TURNING 62', 165, 50, grey, t, 0.5)
    ty = T('You get ninety')
    L = new(); txt(L, '90%', BOLD(210), 275, goldL, 255 * E(t, ty, 1.0), x=960); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'OF THE FIRST $1,286', 470, 60, white, t, ty + 0.6, 960)
    C = new()
    for k in range(10):
        cx = 429 + k * 118
        if k < 9: coin(C, cx, 610, 50)
        else:
            d = ImageDraw.Draw(C); d.ellipse([cx - 50, 560, cx + 50, 660], outline=A((120, 130, 150), 255), width=5)
    fr = appear(fr, C, (360, 540, 1560, 680), t, ty + 1.2, 1.0)
    fr = label(fr, '90 CENTS OF EVERY DOLLAR', 700, 46, goldL, t, ty + 1.8, 960)
    tf = T('first one thousand')
    L = new(); d = ImageDraw.Draw(L); a = E(t, ty + 2.4, 0.9)
    d.line([200, 840, 1720, 840], fill=A(grey, 255 * a), width=4)
    d.rounded_rectangle([200, 815, 417, 865], radius=12, fill=A(gold, 255 * a))
    txt(L, '$0', BOLD(40), 878, white, 255 * a, x=200); txt(L, '$1,286', BOLD(40), 878, goldL, 255 * a, x=417)
    fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b10b(t):
    T = lambda m: B10.tt(1, m)
    fr = base(t); fr = title(fr, 'THE THREE SLICES', t)
    base_y = 760
    specs = [(420, gold, '90%', 420, 'FIRST $1,286', 0.3), (960, blue, '32%', 150, '$1,286 TO $7,749', T('thirty two percent')), (1500, purple, '15%', 70, 'ABOVE $7,749', T('fifteen percent'))]
    L = new(); ImageDraw.Draw(L).line([150, base_y, 1770, base_y], fill=A(goldL, 255), width=4); fr = Image.alpha_composite(fr, L)
    for cx, col, pct, h, rng, t0 in specs:
        u = ease((t - t0) / 1.6)
        if u <= 0: continue
        L = new(); d = ImageDraw.Draw(L); hh = h * u
        d.rounded_rectangle([cx - 150, base_y - hh, cx + 150, base_y], radius=20, fill=A(col, 255))
        if u > 0.9:
            a = E(t, t0 + 1.4, 0.7)
            txt(L, pct, BOLD(120), base_y - h - 150, col, 255 * a, x=cx)
        txt(L, rng, BOLD(44), base_y + 30, col, 255 * E(t, t0 + 0.4, 0.7), x=cx)
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

SL = {6: [b6a, b6b, b6c], 7: [b7a, b7b, b7c, b7d], 8: [b8a, b8b], 9: [b9a, b9b, b9c], 10: [b10a, b10b]}
FSD = {6: B6.FS, 7: B7.FS, 8: B8.FS, 9: B9.FS, 10: B10.FS}

if __name__ == '__main__':
    run_cli('b6_10', SL, FSD, None)
