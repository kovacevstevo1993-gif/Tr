from v6b6_10 import *
from v6b3 import medicare_card
from v6b11_15 import mini_check
import sys

def shield(C, cx, cy, s=1.0, col=green, mark='check'):
    d = ImageDraw.Draw(C); pts = [(cx - 90 * s, cy - 100 * s), (cx, cy - 125 * s), (cx + 90 * s, cy - 100 * s), (cx + 90 * s, cy + 10 * s), (cx, cy + 120 * s), (cx - 90 * s, cy + 10 * s)]
    d.polygon(pts, fill=col + (255,), outline=goldL + (255,))
    if mark == 'check': d.line([cx - 40 * s, cy - 5 * s, cx - 8 * s, cy + 35 * s, cx + 48 * s, cy - 45 * s], fill=(255, 255, 255, 255), width=int(16 * s), joint='curve')
    else: d.line([cx - 40 * s, cy - 45 * s, cx + 40 * s, cy + 35 * s], fill=(255, 255, 255, 255), width=int(16 * s)); d.line([cx - 40 * s, cy + 35 * s, cx + 40 * s, cy - 45 * s], fill=(255, 255, 255, 255), width=int(16 * s))
def taxbar(C, y, a, b, maxv, marks=None, lab=('NO TAX', 'UP TO 50%', 'UP TO 85%')):
    x0, x1 = 200, 1720; W_ = x1 - x0; X = lambda v: x0 + W_ * v / maxv; d = ImageDraw.Draw(C)
    d.rounded_rectangle([x0, y, X(a), y + 90], radius=20, fill=green + (255,)); d.rectangle([X(a) - 20, y, X(a), y + 90], fill=green + (255,))
    d.rectangle([X(a), y, X(b), y + 90], fill=gold + (255,)); d.rounded_rectangle([X(b), y, x1, y + 90], radius=20, fill=red + (255,)); d.rectangle([X(b), y, X(b) + 20, y + 90], fill=red + (255,))
    for xx, l in [((x0 + X(a)) / 2, lab[0]), ((X(a) + X(b)) / 2, lab[1]), ((X(b) + x1) / 2, lab[2])]: txt(C, l, BOLD(34), y + 24, navy, 255, x=xx)
    for v in (a, b): d.line([X(v), y - 20, X(v), y + 110], fill=white + (255,), width=6); txt(C, f'${v:,}', BOLD(46), y + 120, white, 255, x=X(v))
    return X

# ============ BLOCCO 16 (665) ============
B16 = Blk2(["Now, the part that surprises almost everyone.", "There is a rule called the hold harmless provision.",
            "It says that if you already receive Social Security, your Part B premium cannot go up by more than the dollar amount of your raise.",
            "In other words, a Medicare increase cannot make your Social Security deposit smaller.", "That protection is real, and it covers most people on Part B."],
           [[0, 1], [2], [3], [4]], 665)
def s16a(t):
    fr = base_(t, 141, 'THE SURPRISE'); T = lambda m: B16.tt(0, m)
    if t > 0.3:
        C = new(); shield(C, 420, 520, 1.9, green); fr = A_(fr, C, (200, 270, 640, 780), t, 0.3)
    t2 = T('hold harmless')
    if t > t2 - 0.3:
        C = new(); txt(C, 'THE', BOLD(70), 380, white, 255, x=1210); txt(C, 'HOLD HARMLESS', BOLD(110), 460, goldL, 255, x=1210); txt(C, 'RULE', BOLD(110), 590, goldL, 255, x=1210); fr = A_(fr, C, (620, 340, 1820, 740), t, t2 - 0.3)
    fr = P(fr, 'THE PART THAT SURPRISES ALMOST EVERYONE', 830, t, 0.9, red, (255, 255, 255), 46)
    return frame(fr)
def s16b(t):
    fr = base_(t, 142, 'THE RULE'); T = lambda m: B16.tt(1, m)
    if t > 0.3:
        C = new(); C.alpha_composite(bar(330, green, 260), (260, 760 - 330)); txt(C, '+$72', BOLD(90), 330, green, 255, x=390); txt(C, 'YOUR RAISE', BOLD(46), 780, white, 255, x=390); fr = A_(fr, C, (230, 280, 560, 840), t, 0.3)
    t2 = T('Part B premium') - 0.1
    if t > t2:
        C = new(); C.alpha_composite(bar(32, red, 260), (1100, 760 - 32)); txt(C, '+$6.60', BOLD(90), 560, red, 255, x=1230); txt(C, 'PART B INCREASE', BOLD(46), 780, white, 255, x=1230); fr = A_(fr, C, (940, 480, 1520, 840), t, t2)
        C = new(); txt(C, '<=', BOLD(150), 450, goldL, 255, x=800); fr = A_(fr, C, (640, 380, 960, 620), t, t2 + 0.2)
    t3 = T('cannot go up')
    if t > t3: C = new(); txt(C, 'CANNOT BE MORE', BOLD(54), 330, goldL, 255, x=1500); txt(C, 'THAN THE RAISE', BOLD(54), 400, goldL, 255, x=1500); fr = A_(fr, C, (1260, 300, 1800, 480), t, t3)
    return frame(fr)
def s16c(t):
    fr = base_(t, 143, 'THE DEPOSIT'); T = lambda m: B16.tt(2, m)
    if t > 0.3:
        C = new(); mini_check(C, 160, 290, 760, 640, green, '$1,868.10', 'DEPOSIT TODAY', 'IN THE BANK', 100); fr = A_(fr, C, (140, 270, 780, 660), t, 0.3)
    t2 = T('cannot make')
    if t > t2 - 0.3:
        L = new(); arrow_r(L, 800, 960, 460, goldL, 255 * E_(t, t2 - 0.3)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1000, 300, 1780, 640, green); txt(C, 'NEVER SMALLER', BOLD(64), 340, green, 255, x=1390); up_arrow(C, 1180, 500, 0.7, green); txt(C, 'DEPOSIT', BOLD(60), 440, white, 255, x=1470); txt(C, 'CANNOT SHRINK', BOLD(50), 520, white, 255, x=1470); fr = A_(fr, C, (980, 280, 1800, 660), t, t2 - 0.3)
    fr = P(fr, 'A MEDICARE INCREASE CANNOT SHRINK IT', 790, t, 1.0, goldL, navy, 50)
    return frame(fr)
def s16d(t):
    fr = base_(t, 144, 'A REAL PROTECTION'); T = lambda m: B16.tt(3, m)
    if t > 0.3:
        C = new(); shield(C, 360, 480, 1.6, green); txt(C, 'REAL', BOLD(70), 660, green, 255, x=360); fr = A_(fr, C, (160, 280, 560, 740), t, 0.3)
    t2 = T('most people')
    if t > t2 - 0.3:
        C = new(); cols = [green] * 7 + [grey] * 3
        for k in range(10): avatar(C, 800 + k * 100, 470, cols[k], 1.3)
        txt(C, 'MOST PEOPLE ON PART B', BOLD(62), 620, white, 255, x=1280); fr = A_(fr, C, (740, 330, 1840, 700), t, t2 - 0.3)
    fr = P(fr, 'IT COVERS MOST PEOPLE ON PART B', 810, t, 1.0, green, navy, 50)
    return frame(fr)

# ============ BLOCCO 17 (965) ============
B17 = Blk2(["But some people do not get that protection.",
            "First, people who are new to Medicare, or who were not receiving Social Security checks in both November and December of the year before.",
            "Second, people who do not have Part B taken out of their Social Security check, because they pay the bill directly.",
            "And third, higher earners who pay the income related surcharge called IRMAA, which we explained in an earlier video.",
            "For these groups, the whole premium increase can come out of their own pocket."],
           [[0, 1], [2], [3], [4]], 965)
def numcard(fr, t, t0, n, l1, l2, col=red, dy=0):
    C = new(); card_(C, 140, 270 + dy, 1780, 400 + dy, col); badge(C, 230, 335 + dy, n, col, 50); txt(C, l1, BOLD(58), 305 + dy, white, 255, x=1010)
    return A_(fr, C, (120, 250 + dy, 1800, 420 + dy), t, t0)
def s17a(t):
    fr = base_(t, 151, 'NOT EVERYONE IS PROTECTED'); T = lambda m: B17.tt(0, m)
    if t > 0.3:
        C = new(); txt(C, 'NOT PROTECTED', BOLD(96), 215, red, 255, x=960); fr = A_(fr, C, (300, 190, 1620, 340), t, 0.3)
    t1 = T('First')
    if t > t1:
        fr = numcard(fr, t, t1, 1, 'NEW TO MEDICARE', '', dy=100)
    t2 = T('or who were not')
    if t > t2 - 0.2:
        C = new(); card_(C, 140, 560, 1780, 860, red); txt(C, 'NOT RECEIVING SOCIAL SECURITY IN BOTH', BOLD(54), 585, white, 255, x=960)
        for k, m in enumerate(['NOVEMBER', 'DECEMBER']): ImageDraw.Draw(C).rounded_rectangle([420 + k * 560, 670, 800 + k * 560, 810], radius=20, fill=card + (255,), outline=goldL + (255,), width=5); txt(C, m, BOLD(60), 710, goldL, 255, x=610 + k * 560)
        fr = A_(fr, C, (120, 540, 1800, 880), t, t2 - 0.2)
    return frame(fr)
def s17b(t):
    fr = base_(t, 152, 'PAYING PART B DIRECTLY'); T = lambda m: B17.tt(1, m)
    if t > 0.3: fr = numcard(fr, t, 0.3, 2, 'PAY PART B DIRECTLY', '')
    t2 = T('taken out')
    if t > t2 - 0.3:
        C = new(); mini_check(C, 140, 460, 640, 760, blue, '$2,071', 'FULL CHECK', 'SOCIAL SECURITY', 100); txt(C, 'NOTHING TAKEN OUT', BOLD(40), 790, goldL, 255, x=390); fr = A_(fr, C, (120, 440, 660, 840), t, t2 - 0.3)
    t3 = T('they pay the bill')
    if t > t3 - 0.3:
        L = new(); arrow_r(L, 700, 960, 610, red, 255 * E_(t, t3 - 0.3)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1000, 460, 1780, 780, red); medicare_card(C, 1390, 600, 0.9); txt(C, 'THEY PAY THE BILL', BOLD(50), 720, red, 255, x=1390); fr = A_(fr, C, (980, 440, 1800, 800), t, t3 - 0.3)
    return frame(fr)
def s17c(t):
    fr = base_(t, 153, 'THE IRMAA SURCHARGE'); T = lambda m: B17.tt(2, m)
    if t > 0.3: fr = numcard(fr, t, 0.3, 3, 'HIGHER EARNERS: IRMAA', '')
    t2 = T('income related') - 0.1
    if t > t2:
        C = new(); card_(C, 140, 460, 880, 780, blue); medicare_card(C, 510, 600, 0.9); txt(C, 'STANDARD PART B', BOLD(50), 720, white, 255, x=510); fr = A_(fr, C, (120, 440, 900, 800), t, t2)
        C = new(); txt(C, '+', BOLD(150), 560, goldL, 255, x=960); fr = A_(fr, C, (900, 480, 1020, 700), t, t2 + 0.2)
    t3 = T('IRMAA')
    if t > t3 - 0.2:
        C = new(); card_(C, 1040, 460, 1780, 780, red); txt(C, 'SURCHARGE', BOLD(70), 520, red, 255, x=1410); txt(C, 'IRMAA', BOLD(120), 610, white, 255, x=1410); fr = A_(fr, C, (1020, 440, 1800, 800), t, t3 - 0.2)
    t4 = T('earlier video')
    if t > t4 - 0.2: fr = P(fr, 'EXPLAINED IN AN EARLIER VIDEO', 850, t, t4 - 0.2, goldL, navy, 46)
    return frame(fr)
def s17d(t):
    fr = base_(t, 154, 'OUT OF THEIR OWN POCKET'); T = lambda m: B17.tt(3, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 880, 700, red); txt(C, 'THESE GROUPS', BOLD(64), 330, red, 255, x=510); avatar(C, 330, 560, red, 1.8); avatar(C, 510, 560, red, 1.8); avatar(C, 690, 560, red, 1.8); fr = A_(fr, C, (120, 270, 900, 720), t, 0.3)
    t2 = T('whole premium')
    if t > t2 - 0.3:
        L = new(); arrow_r(L, 910, 1030, 500, red, 255 * E_(t, t2 - 0.3)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1060, 290, 1780, 700, red); wallet(C, 1420, 470, 1.4); txt(C, 'WHOLE INCREASE', BOLD(52), 590, white, 255, x=1420); txt(C, 'FROM THEIR POCKET', BOLD(46), 650, red, 255, x=1420); fr = A_(fr, C, (1040, 270, 1800, 720), t, t2 - 0.3)
    fr = P(fr, 'NO HOLD HARMLESS PROTECTION', 800, t, 1.0, red, (255, 255, 255), 54)
    return frame(fr)

# ============ BLOCCO 18 (1019) ============
B18 = Blk2(["Number four: taxes.", "Many people believe Social Security is tax free.", "It is not always.", "The Internal Revenue Service looks at something called combined income.",
            "That is your other income, plus any tax exempt interest, plus half of your Social Security.",
            "For a single person, above twenty five thousand dollars, up to fifty percent of your benefits can become taxable.", "Above thirty four thousand, up to eighty five percent.",
            "For couples filing together, the lines are thirty two thousand and forty four thousand."],
           [[0, 1, 2], [3, 4], [5, 6], [7]], 1019)
def s18a(t):
    fr = base_(t, 161, 'NUMBER FOUR: TAXES'); T = lambda m: B18.tt(0, m)
    if t > 0.3:
        C = new(); badge(C, 260, 340, 4, red, 70); txt(C, 'IS SOCIAL SECURITY', BOLD(76), 290, white, 255, x=1090); txt(C, 'TAX FREE?', BOLD(110), 380, goldL, 255, x=1090); fr = A_(fr, C, (120, 230, 1800, 520), t, 0.3)
    t2 = T('Many people')
    if t > t2:
        C = new(); card_(C, 200, 580, 940, 800, grey); txt(C, 'MANY PEOPLE THINK:', BOLD(44), 610, white, 255, x=570); txt(C, 'YES, TAX FREE', BOLD(66), 680, grey, 255, x=570); fr = A_(fr, C, (180, 560, 960, 820), t, t2)
    t3 = T('not always')
    if t > t3:
        C = new(); card_(C, 980, 580, 1720, 800, red); txt(C, 'THE TRUTH:', BOLD(44), 610, white, 255, x=1350); txt(C, 'NOT ALWAYS', BOLD(76), 670, red, 255, x=1350); fr = A_(fr, C, (960, 560, 1740, 820), t, t3)
    return frame(fr)
def s18b(t):
    fr = base_(t, 162, 'COMBINED INCOME'); T = lambda m: B18.tt(1, m)
    if t > 0.3:
        C = new(); txt(C, 'COMBINED INCOME', BOLD(96), 270, goldL, 255, x=960); txt(C, 'USED BY THE IRS', BOLD(46), 380, grey, 255, x=960); fr = A_(fr, C, (240, 250, 1700, 450), t, 0.3)
    items = [('OTHER INCOME', blue, 'your other income'), ('TAX-EXEMPT INTEREST', gold, 'tax exempt interest'), ('HALF OF YOUR SOCIAL SECURITY', green, 'half of your Social Security')]
    xs = [340, 960, 1580]
    for k, (lab, col, m) in enumerate(items):
        t0 = max(0.5, T(m) - 0.2)
        if t < t0: continue
        C = new(); card_(C, xs[k] - 245, 520, xs[k] + 245, 740, col); l = lab.split(' ', 1) if k != 1 else ['TAX-EXEMPT', 'INTEREST']
        if k == 0: l = ['OTHER', 'INCOME']
        if k == 2: l = ['HALF OF YOUR', 'SOCIAL SECURITY']
        txt(C, l[0], BOLD(54), 575, white, 255, x=xs[k]); txt(C, l[1], BOLD(54), 640, col, 255, x=xs[k]); fr = A_(fr, C, (xs[k] - 265, 500, xs[k] + 265, 760), t, t0)
        if k < 2:
            L = new(); txt(L, '+', BOLD(110), 580, goldL, 255 * E_(t, t0 + 0.3), x=xs[k] + 310); fr = Image.alpha_composite(fr, L)
    return frame(fr)
def s18c(t):
    fr = base_(t, 163, 'A SINGLE PERSON'); T = lambda m: B18.tt(2, m)
    if t > 0.3:
        C = new(); avatar(C, 260, 320, blue, 1.6); txt(C, 'SINGLE PERSON', BOLD(70), 290, white, 255, x=1000); fr = A_(fr, C, (140, 200, 1500, 420), t, 0.3)
    if t > 0.7:
        C = new(); taxbar(C, 520, 25000, 34000, 50000); fr = A_(fr, C, (160, 480, 1780, 760), t, 0.7)
    t2 = T('fifty percent')
    if t > t2: fr = P(fr, 'ABOVE $25,000: UP TO 50%', 820, t, t2 - 0.2, gold, navy, 46, 540)
    t3 = T('eighty five')
    if t > t3 - 0.2: fr = P(fr, 'ABOVE $34,000: UP TO 85%', 820, t, t3 - 0.2, red, (255, 255, 255), 46, 1380)
    return frame(fr)
def s18d(t):
    fr = base_(t, 164, 'COUPLES FILING TOGETHER'); T = lambda m: B18.tt(3, m)
    if t > 0.3:
        C = new(); avatar(C, 250, 320, blue, 1.6); avatar(C, 360, 320, pink, 1.6); txt(C, 'COUPLES FILING TOGETHER', BOLD(66), 290, white, 255, x=1090); fr = A_(fr, C, (140, 200, 1800, 420), t, 0.3)
    if t > 0.7:
        C = new(); taxbar(C, 520, 32000, 44000, 60000); fr = A_(fr, C, (160, 480, 1780, 760), t, 0.7)
    fr = P(fr, 'THE LINES: $32,000 AND $44,000', 850, t, 1.5, goldL, navy, 52)
    return frame(fr)

# ============ BLOCCO 19 (758) ============
B19 = Blk2(["Here is the detail that matters for a raise.", "Those lines were set in the nineteen eighties and nineties, and they have never been adjusted for inflation.",
            "So every raise pushes a little more of each check toward the taxable zone, and each year more retirees cross the line.",
            "Notice that taxable does not mean taxed.", "Only part of your benefit is counted, and whether that creates a tax bill depends on your deductions."],
           [[0, 1], [2], [3, 4]], 758)
def s19a(t):
    fr = base_(t, 171, 'FROZEN LINES'); T = lambda m: B19.tt(0, m)
    t1 = T('Those lines') - 0.1
    for k, (yr, val, col) in enumerate([('1984', '$25,000', gold), ('1993', '$34,000', red)]):
        t0 = max(0.4, t1 + 0.9 * k)
        if t < t0: continue
        C = new(); card_(C, 220 + k * 760, 290, 900 + k * 760, 560, col); txt(C, 'SET IN ' + yr, BOLD(60), 320, white, 255, x=560 + k * 760); txt(C, val, BOLD(130), 410, col, 255, x=560 + k * 760); fr = A_(fr, C, (200 + k * 760, 270, 920 + k * 760, 580), t, t0)
    t3 = T('never been adjusted')
    if t > t3 - 0.3:
        C = new(); padlock(C, 520, 720, 1.0, red); txt(C, 'NEVER ADJUSTED FOR INFLATION', BOLD(66), 720, red, 255, x=1230); fr = A_(fr, C, (360, 580, 1800, 860), t, t3 - 0.3)
    return frame(fr)
def s19b(t):
    fr = base_(t, 172, 'EVERY RAISE PUSHES A LITTLE'); T = lambda m: B19.tt(1, m)
    if t > 0.3:
        C = new(); X = taxbar(C, 380, 25000, 34000, 50000); fr = A_(fr, C, (160, 340, 1780, 620), t, 0.3)
    u = ease((t - 0.8) / 2.0)
    C = new(); d = ImageDraw.Draw(C); xv = 360 + 760 * u
    bill(C, xv, 300, 200, 98, 0, 255); txt(C, 'YOUR CHECK + RAISE', BOLD(44), 220, goldL, 255, x=xv)
    fr = Image.alpha_composite(fr, C)
    t2 = T('cross the line')
    if t > t2 - 0.4:
        C = new(); [avatar(C, 1100 + k * 120, 760, [blue, pink, gold][k % 3], 1.3) for k in range(5)]; txt(C, 'MORE RETIREES CROSS THE LINE', BOLD(54), 860, goldL, 255, x=1300); fr = A_(fr, C, (780, 660, 1840, 940), t, t2 - 0.4)
    return frame(fr)
def s19c(t):
    fr = base_(t, 173, 'TAXABLE IS NOT TAXED'); T = lambda m: B19.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 900, 700, gold); tax_form(C, 220, 360, 150, 200, 255, 'COUNTED'); txt(C, 'TAXABLE', BOLD(80), 340, goldL, 255, x=640); txt(C, 'PART OF YOUR', BOLD(48), 450, white, 255, x=640); txt(C, 'BENEFIT IS COUNTED', BOLD(48), 510, white, 255, x=640); fr = A_(fr, C, (120, 270, 920, 720), t, 0.3)
    t2 = T('Only part')
    if t > t2 - 0.2:
        L = new(); txt(L, '=/=', BOLD(80), 470, red, 255 * E_(t, t2 - 0.2), x=960); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1020, 290, 1780, 700, red); txt(C, 'TAXED', BOLD(80), 340, red, 255, x=1400); txt(C, 'DEPENDS ON', BOLD(48), 450, white, 255, x=1400); txt(C, 'YOUR DEDUCTIONS', BOLD(48), 510, white, 255, x=1400); fr = A_(fr, C, (1000, 270, 1800, 720), t, t2)
    fr = P(fr, 'TAXABLE DOES NOT MEAN TAXED', 810, t, 0.9, goldL, navy, 56)
    return frame(fr)

# ============ BLOCCO 20 (912) ============
B20 = Blk2(["Let's test it on Frank and Mary.", "Mary has no other income, so her combined income is only about twelve thousand four hundred dollars, far below the line.",
            "None of her Social Security is taxable, and the raise does not change that.", "Frank has a pension of twenty thousand dollars a year.",
            "His combined income is about thirty two thousand four hundred dollars, so he is in the fifty percent zone.",
            "After a three point five percent raise, about two hundred sixteen dollars more of his benefit would become taxable."],
           [[0, 1, 2], [3, 4], [5]], 912)
def marker(C, X, v, y, col, lab):
    d = ImageDraw.Draw(C); x = X(v); d.polygon([(x, y), (x - 30, y - 60), (x + 30, y - 60)], fill=col + (255,)); txt(C, lab, BOLD(50), y - 130, col, 255, x=x)
def s20a(t):
    fr = base_(t, 181, 'MARY'); T = lambda m: B20.tt(0, m)
    if t > 0.3:
        C = new(); avatar(C, 260, 330, pink, 1.8); txt(C, 'MARY: NO OTHER INCOME', BOLD(66), 300, white, 255, x=1090); fr = A_(fr, C, (140, 200, 1800, 440), t, 0.3)
    if t > 0.7:
        C = new(); X = taxbar(C, 590, 25000, 34000, 50000); fr = A_(fr, C, (160, 480, 1780, 780), t, 0.7)
        C = new(); marker(C, X, 12400, 585, pink, '$12,400'); fr = Image.alpha_composite(fr, C) if t > 1.2 else fr
    t3 = T('None of her')
    if t > t3 - 0.3: fr = P(fr, 'NONE OF HER BENEFIT IS TAXABLE', 850, t, t3 - 0.3, green, navy, 56)
    return frame(fr)
def s20b(t):
    fr = base_(t, 182, 'FRANK'); T = lambda m: B20.tt(1, m)
    if t > 0.3:
        C = new(); avatar(C, 260, 330, blue, 1.8); txt(C, 'FRANK: PENSION $20,000', BOLD(66), 300, white, 255, x=1090); fr = A_(fr, C, (140, 200, 1800, 440), t, 0.3)
    if t > 0.7:
        C = new(); X = taxbar(C, 590, 25000, 34000, 50000); fr = A_(fr, C, (160, 480, 1780, 780), t, 0.7)
    t2 = T('His combined')
    if t > t2:
        C = new(); X = lambda v: 200 + 1520 * v / 50000; marker(C, X, 32400, 585, blue, '$32,400'); fr = A_(fr, C, (900, 330, 1400, 600), t, t2)
    t3 = T('fifty percent zone')
    if t > t3 - 0.3: fr = P(fr, 'FRANK IS IN THE 50% ZONE', 850, t, t3 - 0.3, gold, navy, 56)
    return frame(fr)
def s20c(t):
    fr = base_(t, 183, 'AFTER THE RAISE'); T = lambda m: B20.tt(2, m)
    if t > 0.3:
        C = new(); avatar(C, 330, 440, blue, 2.2); txt(C, 'FRANK', BOLD(60), 560, blue, 255, x=330); fr = A_(fr, C, (160, 300, 520, 640), t, 0.3)
    t2 = T('about two hundred')
    if t > 0.8:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([620, 330, 900, 610], fill=gold + (255,), outline=goldL + (255,), width=8); txt(C, '3.5%', BOLD(90), 410, navy, 255, x=760); txt(C, 'RAISE', BOLD(46), 510, navy, 255, x=760); fr = A_(fr, C, (600, 310, 920, 630), t, 0.8)
        L = new(); arrow_r(L, 930, 1060, 470, goldL, 255 * E_(t, 1.2)); fr = Image.alpha_composite(fr, L)
    if t > t2 - 0.3:
        C = new(); card_(C, 1090, 300, 1790, 650, red); up_arrow(C, 1250, 480, 0.7, red); txt(C, '+$216', BOLD(130), 360, red, 255, x=1560); txt(C, 'MORE TAXABLE', BOLD(54), 520, white, 255, x=1560); fr = A_(fr, C, (1070, 280, 1810, 670), t, t2 - 0.3)
    fr = P(fr, 'ABOUT $216 MORE OF HIS BENEFIT TAXABLE', 800, t, 1.2, goldL, navy, 46)
    return frame(fr)

FNS3 = {16: [s16a, s16b, s16c, s16d], 17: [s17a, s17b, s17c, s17d], 18: [s18a, s18b, s18c, s18d], 19: [s19a, s19b, s19c], 20: [s20a, s20b, s20c]}
BLK3 = {16: B16, 17: B17, 18: B18, 19: B19, 20: B20}
if __name__ == '__main__':
    mode = sys.argv[1]; b = int(sys.argv[2]); fns = FNS3[b]; FS = BLK3[b].FS
    sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, len(fns) + 1))
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.35, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}py{b}_{i}_{int(fq*100)}.png')
        print(b, FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b{b}-0{i}.mp4'); print('done', b, i, f, flush=True)
