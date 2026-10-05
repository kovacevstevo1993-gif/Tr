from v3lib import *
from v3b3_10 import POP, new, lerp, fly, person_box
from v3b11_21 import crown, stop_sign, rail
from v4b2_10 import medicare_card, cal_card, eye, envelope, SRC, cliff_icon
from v4b11_20 import calculator, hourglass, ss_card, year_medal
import sys, math

SENT = {
 21: ["Reason number four hits people who stop working before sixty-five.", "Medicare is still years away, so you'll likely buy a marketplace health plan, and the price of that plan depends on your income too.", "In twenty twenty-six, the extra subsidies of the last few years have expired, and the old cliff at four hundred percent of the poverty line is back."],
 22: ["For one person, that cliff sits around sixty-two thousand six hundred dollars of income.", "One dollar above it can mean losing the entire premium tax credit, and if you already received it during the year, you may have to pay it back at tax time.", "So a big conversion at sixty-two can cost far more than the tax on the conversion itself."],
 23: ["These are the rules as of today, and lawmakers can change them, so always check the current numbers before you act.", "The point is simple: before you convert a single dollar, look at every line your income might cross.", "Medicare's, Social Security's, and your health insurance's."],
 24: ["Reason number five is about saving, not converting.", "Between sixty and sixty-three, the IRS lets workers in a four-oh-one-k add eleven thousand two hundred fifty dollars a year in catch-up contributions in twenty twenty-six, instead of the usual eight thousand.", "That's up to thirty-five thousand seven hundred fifty dollars in total, if the plan allows it.", "At sixty-one, you're inside that window, and it closes after sixty-three."],
 25: ["And here's a useful detail: money you put into a traditional four-oh-one-k comes out of your taxable income now.", "So while conversions push your income up, pre-tax contributions can push it down, which can help you stay under a line.", "The two tools work in opposite directions, and using them together is where planning gets powerful."],
 26: ["So here's where Frank and Mary end up.", "Frank did nothing at sixty-one and sixty-two, claimed Social Security early, and started converting at sixty-three.", "Mary treated those two years as a window: she checked her lines, converted a piece each year, and chose her Social Security date after running the numbers.", "At sixty-five, Frank opens a Medicare letter with a surcharge.", "Mary opens hers with the standard premium."],
 27: ["Let's recap the five reasons.", "One: Medicare reads your tax return from two years earlier.", "Two: the income lines are cliffs, not slopes.", "Three: a conversion can make your Social Security taxable.", "Four: before sixty-five, health insurance has a cliff of its own.", "Five: the catch-up window closes after sixty-three.", "Every one of them points to the same two years."],
 28: ["So here's what to do this year.", "One: find your modified adjusted gross income on your latest tax return and compare it with the Medicare lines.", "Two: write down the year you turn sixty-three, because that return is the one that counts.", "Three: before any Roth conversion, check three things: the Medicare line, the Social Security tax lines, and the health insurance cliff if you're under sixty-five."],
 29: ["Four: if your income has already dropped because you retired, cut your hours, or lost a pension, ask Social Security to reassess your Medicare premium using Form S-S-A forty-four.", "Five: get every number in writing from a tax professional or a fiduciary advisor before you convert, because the thresholds change every year and the numbers here are the twenty twenty-six ones."],
 30: ["What if you're already sixty-three or sixty-four?", "It's not too late.", "The surcharge is recalculated every year, so your next tax return still matters, and if your income drops because of a life event, the reassessment route is still open.", "The free years may be gone, but the smart years are not."],
 31: ["Sixty-one isn't a magic birthday.", "It's the last age when you still have two full years to act before Medicare starts reading your income.", "If this helped you plan ahead, hit subscribe so you don't miss the next one.", "And if you want to see what changes even earlier, at fifty-nine and a half, that video is linked right here."],
}
FRAMES = {21: 665, 22: 708, 23: 635, 24: 894, 25: 646, 26: 868, 27: 861, 28: 874, 29: 784, 30: 552, 31: 559}
GROUPS = {21: [[0], [1], [2]], 22: [[0], [1], [2]], 23: [[0], [1], [2]], 24: [[0], [1], [2, 3]], 25: [[0], [1], [2]], 26: [[0, 1], [2], [3, 4]], 27: [[0, 1, 2], [3, 4, 5], [6]], 28: [[0, 1], [2], [3]], 29: [[0], [1]], 30: [[0, 1], [2, 3]], 31: [[0, 1], [2, 3]]}

def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':') + text.count('—'))
def wpos(text, marker):
    i = text.index(marker); pre = text[:i]
    return len(pre) + 3 * (pre.count(',') + pre.count(':') + pre.count('—'))
TXT, DUR = {}, {}
for b in SENT:
    gw = [sum(len(SENT[b][i]) + 10 for i in g) for g in GROUPS[b]]
    T_ = sum(gw); fs = [round(w / T_ * FRAMES[b]) for w in gw]; fs[-1] = FRAMES[b] - sum(fs[:-1])
    DUR[b] = fs; TXT[b] = [' '.join(SENT[b][i] for i in g) for g in GROUPS[b]]
def tt(b, g, marker):
    return max(0.2, wpos(TXT[b][g], marker) / wtot(TXT[b][g]) * DUR[b][g] / 30 - 0.1)

def thumbs_up(C, cx, cy, s=1.0, alpha=255, col=gold):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 70 * s, cy - 10 * s, cx - 20 * s, cy + 70 * s], radius=int(8 * s), fill=A(col, alpha))
    d.rounded_rectangle([cx - 16 * s, cy - 10 * s, cx + 80 * s, cy + 70 * s], radius=int(16 * s), fill=A(col, alpha))
    d.rounded_rectangle([cx - 6 * s, cy - 70 * s, cx + 30 * s, cy + 0 * s], radius=int(14 * s), fill=A(col, alpha))

def magnifier(C, cx, cy, r=60, alpha=255):
    d = ImageDraw.Draw(C); d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=A(goldL, alpha), width=10); d.line([cx + r * 0.7, cy + r * 0.7, cx + r * 1.6, cy + r * 1.6], fill=A(goldL, alpha), width=14)

def thermo(C, cx, top, bot, level, col=gold, alpha=255):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 30, top, cx + 30, bot], radius=30, outline=A(goldL, alpha), width=6)
    h = (bot - top - 16) * level
    d.rounded_rectangle([cx - 20, bot - 8 - h, cx + 20, bot - 8], radius=18, fill=A(col, alpha))

def shield(C, cx, cy, s=1.0, alpha=255, col=green):
    d = ImageDraw.Draw(C)
    d.polygon([(cx, cy - 90 * s), (cx + 70 * s, cy - 60 * s), (cx + 64 * s, cy + 20 * s), (cx, cy + 90 * s), (cx - 64 * s, cy + 20 * s), (cx - 70 * s, cy - 60 * s)], fill=A(card, alpha), outline=A(col, alpha))
    d.line([(cx, cy - 90 * s), (cx + 70 * s, cy - 60 * s), (cx + 64 * s, cy + 20 * s), (cx, cy + 90 * s), (cx - 64 * s, cy + 20 * s), (cx - 70 * s, cy - 60 * s), (cx, cy - 90 * s)], fill=A(col, alpha), width=8)

# ================= BLOCK 21 =================
def b21a(t):
    fr = base(t); fr = title_layer(fr, 'REASON #4', t, col=red)
    T = lambda m: tt(21, 0, m)
    a = T('hits people'); b = T('stop working'); c = T('before sixty-five')
    C = new(); door(C, 1150, 560, 200, 300, blue, 255, open_p=0.85); fr = POP(fr, C, (1000, 380, 1300, 750), back((t - 0.3) / 0.5))
    if t > a:
        u = ease((t - b) / 1.4) if t > b else 0; px = lerp(500, 1100, u)
        C = new(); avatar(C, px, 560, gold, 2.2, 255 * (1 - max(0, (u - 0.85) * 6))); briefcase(C, px - 110, 640, 0.8, 255 * (1 - max(0, (u - 0.85) * 6)))
        fr = Image.alpha_composite(fr, C) if t > b else POP(fr, C, (330, 400, 720, 720), back((t - a) / 0.45))
        if t <= b: pass
    if t > b: fr = pill_pop(fr, 'STOP WORKING', 800, t, b, gold, navy, size=40, cx=800)
    if t > c:
        C = new(); cal_card(C, 1440, 300, 1760, 580, 'BEFORE', '65', 130, red); fr = POP(fr, C, (1430, 290, 1770, 590), back((t - c) / 0.5))
    return frame(fr)

def b21b(t):
    fr = base(t); fr = title_layer(fr, 'BEFORE MEDICARE', t)
    T = lambda m: tt(21, 1, m)
    a = T('Medicare is still'); b = T("you'll likely buy"); c = T('the price of that plan')
    C = new(); medicare_card(C, 1540, 470, 0.9, 110); txt(C, 'YEARS AWAY', BOLD(36), 600, grey, 255, x=1540); fr = POP(fr, C, (1380, 360, 1700, 650), back((t - a) / 0.5))
    if t > b - 0.3:
        C = new(); card_box(C, 660, 330, 1100, 640, green, card, 255, 6); txt(C, 'MARKETPLACE', BOLD(46), 370, green, 255, x=880); txt(C, 'HEALTH PLAN', BOLD(46), 425, white, 255, x=880); d = ImageDraw.Draw(C); d.rectangle([840, 510, 920, 528], fill=A(red, 255)); d.rectangle([870, 480, 890, 560], fill=A(red, 255))
        fr = POP(fr, C, (650, 320, 1110, 650), back((t - b + 0.3) / 0.5))
    if t > c - 0.3:
        C = new(); lev = 0.25 + 0.55 * (0.5 + 0.5 * math.sin((t - c) * 1.8)); thermo(C, 330, 300, 760, lev, gold); txt(C, 'YOUR INCOME', BOLD(30), 790, white, 255, x=330); fr = POP(fr, C, (230, 280, 430, 840), back((t - c + 0.3) / 0.45))
        L = new(); d = ImageDraw.Draw(L); d.line([400, 530, 640, 530], fill=goldL + (255,), width=8); d.polygon([(660, 530), (626, 508), (626, 552)], fill=goldL + (255,)); fr = Image.alpha_composite(fr, L)
        price = 180 + 260 * (0.5 + 0.5 * math.sin((t - c) * 1.8))
        fr = pill_pop(fr, f'PRICE DEPENDS ON INCOME', 730, t, c + 0.3, gold, navy, size=38, cx=880)
    return frame(fr)

def b21c(t):
    fr = base(t); fr = title_layer(fr, 'THE SUBSIDY CLIFF IS BACK', t, size=56)
    T = lambda m: tt(21, 2, m)
    a = T('the extra subsidies'); b = T('have expired'); c = T('the old cliff'); d_ = T('four hundred percent'); e = T('is back')
    C = new(); shield(C, 460, 520, 1.8); coin_stack(C, 460, 580, 3, 46); txt(C, 'EXTRA SUBSIDIES', BOLD(34), 700, green, 255, x=460); fr = POP(fr, C, (250, 340, 670, 750), back((t - a + 0.3) / 0.5)) if t > a - 0.3 else fr
    if t > b: fr = stamp(fr, 'EXPIRED', 460, 500, -10, red, back((t - b) / 0.45), 64)
    if t > c:
        C = new(); cliff_icon(C, 1220, 520, 2.4, 255, red); fr = POP(fr, C, (1030, 380, 1420, 700), back((t - c) / 0.5))
    if t > d_:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - d_) / 0.7)
        for x in range(900, int(900 + 620 * u), 30): d.line([x, 450, x + 16, 450], fill=gold + (255,), width=6)
        txt(L, '400% OF THE POVERTY LINE', BOLD(38), 385, gold, 255 * u, x=1210); fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'THE OLD CLIFF IS BACK', 800, t, e, red, size=48, cx=1200)
    return frame(fr)

# ================= BLOCK 22 =================
def b22a(t):
    fr = base(t); fr = title_layer(fr, 'WHERE THE CLIFF SITS', t)
    T = lambda m: tt(22, 0, m)
    a = T('For one person'); b = T('sixty-two thousand')
    x0, x1, yb, yt = 300, 1620, 800, 350
    ax = lambda v: x0 + v / 80000 * (x1 - x0)
    L = new(); d = ImageDraw.Draw(L)
    d.line([x0, yb, x1, yb], fill=gold + (255,), width=3); d.line([x0, yb, x0, yt - 30], fill=gold + (255,), width=3)
    for v in range(0, 80001, 20000): d.line([ax(v), yb - 8, ax(v), yb + 8], fill=gold + (255,), width=3); txt(L, f'${v // 1000}k', BOLD(28), yb + 16, grey, 255, x=ax(v))
    txt(L, 'PREMIUM TAX CREDIT', BOLD(30), yt - 60, green, 255, x=x0 + 200, anchor='c')
    u = ease((t - 0.4) / 1.2); xe = ax(62600)
    d.line([x0, yt, x0 + (xe - x0) * u, yt], fill=green + (255,), width=12)
    if t > b:
        v = ease((t - b) / 0.6)
        d.line([xe, yt, xe, yt + (yb - yt) * v], fill=red + (255,), width=12); d.line([xe, yb, xe + (x1 - xe) * v, yb], fill=red + (255,), width=12)
        txt(L, '$62,600', BOLD(56), yt - 70, red, 255 * v, x=xe)
    fr = Image.alpha_composite(fr, L)
    if t > a: 
        C = new(); avatar(C, 1500, 520, blue, 1.6); txt(C, 'ONE PERSON', BOLD(30), 590, blue, 255, x=1500); fr = POP(fr, C, (1400, 420, 1600, 640), back((t - a) / 0.45))
    return frame(SRC(fr, 'Approximate 2026 figure for one person'))

def b22b(t):
    fr = base(t); fr = title_layer(fr, 'ONE DOLLAR TOO MANY', t)
    T = lambda m: tt(22, 1, m)
    a = T('One dollar above'); b = T('losing the entire'); c = T('already received'); d_ = T('pay it back')
    lost = ease((t - b) / 1.2) if t > b else 0
    C = new(); coin_stack(C, 380, 620, max(0, int(8 * (1 - lost))), 70); txt(C, 'PREMIUM TAX CREDIT', BOLD(30), 690, green, 255, x=380); fr = POP(fr, C, (130, 360, 640, 730), back((t - 0.3) / 0.5))
    if t > a:
        L = new(); d = ImageDraw.Draw(L); d.line([700, 300, 700, 800], fill=red + (255,), width=10); txt(L, '$62,600', BOLD(30), 270, red, 255, x=700); fr = Image.alpha_composite(fr, L)
        C = new(); bill(C, 830, 560, 200, 98, 10, 255); txt(C, '+ $1', BOLD(50), 630, red, 255, x=830); fr = POP(fr, C, (700, 470, 960, 700), back((t - a) / 0.45))
    if t > b:
        L = new(); s0 = b
        for k in range(8):
            fly(L, t, b + k * 0.1, 1.2, (380, 560), (200 - k * 10, 200), 120, 'coin', 255 * (1 - lost * 0.0), 0, 0.9)
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'ENTIRE CREDIT LOST', 830, t, b + 0.6, red, size=40, cx=400)
    if t > c - 0.3:
        C = new(); wallet(C, 1150, 500, 0.9); coin_stack(C, 1150, 470, 3, 34); fr = POP(fr, C, (1020, 400, 1290, 600), back((t - c + 0.3) / 0.45))
        txt_l = new(); txt(txt_l, 'ALREADY RECEIVED', BOLD(28), 620, gold, 255, x=1150); fr = Image.alpha_composite(fr, txt_l)
    if t > d_ - 0.3:
        C = new(); building(C, 1600, 500, 240, 190, red); txt(C, 'IRS', BOLD(40), 640, white, 255, x=1600); fr = POP(fr, C, (1450, 380, 1750, 680), back((t - d_ + 0.3) / 0.45))
        L = new(); s0 = d_
        while s0 < DUR[22][1] / 30 - 0.3:
            fly(L, t, s0, 1.0, (1250, 500), (1480, 500), 60, 'bill', 255, 0, 0.6); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'PAY IT BACK AT TAX TIME', 800, t, d_, red, size=38, cx=1330)
    return frame(fr)

def b22c(t):
    fr = base(t); fr = title_layer(fr, 'THE REAL COST OF A BIG CONVERSION', t, size=54)
    T = lambda m: tt(22, 2, m)
    a = T('a big conversion'); b = T('far more'); c = T('the tax on the conversion')
    C = new(); vault(C, 400, 520, 120, t, 0.3); txt(C, 'BIG CONVERSION', BOLD(34), 680, gold, 255, x=400); fr = POP(fr, C, (240, 360, 560, 730), back((t - a) / 0.5)) if t > a - 0.2 else fr
    base_y = 820
    L = new(); d = ImageDraw.Draw(L); d.line([760, base_y, 1660, base_y], fill=gold + (255,), width=3)
    if t > b:
        u = ease((t - b) / 0.9); d.rounded_rectangle([800, base_y - 460 * u, 1000, base_y], radius=14, fill=red + (255,)); txt(L, 'LOST SUBSIDY', BOLD(32), base_y + 14, red, 255, x=900)
    if t > c:
        u = ease((t - c) / 0.7); d.rounded_rectangle([1200, base_y - 160 * u, 1400, base_y], radius=14, fill=gold + (255,)); txt(L, 'TAX ON THE CONVERSION', BOLD(28), base_y + 14, gold, 255, x=1300)
    fr = Image.alpha_composite(fr, L)
    if t > c + 0.6: fr = pill_pop(fr, 'FAR MORE THAN THE TAX', 220, t, c + 0.6, red, size=44)
    return frame(fr)

# ================= BLOCK 23 =================
def b23a(t):
    fr = base(t); fr = title_layer(fr, 'RULES AS OF TODAY', t)
    T = lambda m: tt(23, 0, m)
    a = T('as of today'); b = T('lawmakers can change'); c = T('always check')
    C = new(); cal_card(C, 220, 300, 560, 620, 'TODAY', '2026', 100, blue); fr = POP(fr, C, (210, 290, 570, 630), back((t - a + 0.4) / 0.5)) if t > a - 0.4 else fr
    if t > b - 0.3:
        C = new(); building(C, 960, 470, 300, 230, gold); txt(C, 'LAWMAKERS', BOLD(40), 620, gold, 255, x=960); fr = POP(fr, C, (780, 340, 1140, 690), back((t - b + 0.3) / 0.5))
        vals = ['$109,000', '$62,600', '25,000', '$218,000']
        L = new(); k = int((t - b) * 2.2) % 4
        txt(L, vals[k] if vals[k][0] == '$' else '$' + vals[k], BOLD(70), 720, red, 255, x=960); fr = Image.alpha_composite(fr, L)
    if t > c:
        C = new(); magnifier(C, 1500, 470, 80); fr = POP(fr, C, (1400, 370, 1680, 660), back((t - c) / 0.45))
        fr = pill_pop(fr, 'CHECK THE CURRENT NUMBERS', 820, t, c + 0.2, gold, navy, size=44)
    return frame(fr)

def b23b(t):
    fr = base(t); fr = title_layer(fr, 'BEFORE YOU CONVERT', t)
    T = lambda m: tt(23, 1, m)
    a = T('before you convert'); b = T('look at every line')
    C = new(); bill(C, 450, 500, 340, 166, 6, 255); vault(C, 450, 720, 60, t, 0.3); fr = POP(fr, C, (250, 380, 650, 800), back((t - a + 0.4) / 0.5)) if t > a - 0.4 else fr
    if t > a: fr = pill_pop(fr, 'A SINGLE DOLLAR', 260, t, a, gold, navy, size=40, cx=450)
    if t > b - 0.2:
        C = new(); eye(C, 1000, 320, 1.3, 255, t); fr = POP(fr, C, (860, 240, 1140, 400), back((t - b + 0.2) / 0.45))
        L = new(); d = ImageDraw.Draw(L)
        for k, (lab, col) in enumerate([('MEDICARE', red), ('SOCIAL SECURITY', gold), ('HEALTH INSURANCE', purple)]):
            st = b + k * 0.6
            if t < st: continue
            u = ease((t - st) / 0.6); y = 470 + k * 130
            for x in range(800, int(800 + 780 * u), 30): d.line([x, y, x + 16, y], fill=col + (255,), width=6)
            txt(L, lab, BOLD(36), y - 56, col, 255 * u, x=1190)
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b23c(t):
    fr = base(t); fr = title_layer(fr, 'THREE LINES', t)
    T = lambda m: tt(23, 2, m)
    a = T('Medicare'); b = T('Social Security'); c = T('your health insurance')
    C = new(); medicare_card(C, 420, 520, 0.95); fr = POP(fr, C, (240, 400, 600, 640), back((t - a) / 0.5))
    if t > b - 0.1:
        C = new(); ss_card(C, 960, 520, 0.95); fr = POP(fr, C, (780, 400, 1140, 640), back((t - b + 0.1) / 0.5))
    if t > c - 0.1:
        C = new(); card_box(C, 1330, 420, 1690, 620, green, card, 255, 6); txt(C, 'HEALTH', BOLD(38), 450, green, 255, x=1510); txt(C, 'INSURANCE', BOLD(38), 500, white, 255, x=1510); d = ImageDraw.Draw(C); d.rectangle([1480, 570, 1540, 582], fill=A(red, 255)); d.rectangle([1504, 546, 1516, 606], fill=A(red, 255))
        fr = POP(fr, C, (1320, 410, 1700, 630), back((t - c + 0.1) / 0.5))
    L = new(); d = ImageDraw.Draw(L)
    for k, (x, col) in enumerate([(420, red), (960, gold), (1510, purple)]):
        d.line([x - 160, 720, x + 160, 720], fill=col + (255,), width=8)
        if t > [a, b, c][k] + 0.4: txt(L, 'LINE', BOLD(34), 740, col, 255, x=x)
    fr = Image.alpha_composite(fr, L)
    return frame(fr)

# ================= BLOCK 24 =================
def b24a(t):
    fr = base(t); fr = title_layer(fr, 'REASON #5', t, col=gold)
    T = lambda m: tt(24, 0, m)
    a = T('about saving'); b = T('not converting')
    C = new(); d = ImageDraw.Draw(C); d.ellipse([200, 340, 500, 640], fill=gold + (255,)); txt(C, '5', BOLD(240), 360, navy, 255, x=350); fr = POP(fr, C, (190, 330, 510, 650), back((t - 0.3) / 0.5))
    if t > a - 0.2:
        C = new(); vault(C, 1000, 500, 100, t, 0.3); txt(C, 'SAVING', BOLD(50), 640, green, 255, x=1000); fr = POP(fr, C, (830, 380, 1170, 700), back((t - a + 0.2) / 0.45))
        L = new(); s0 = a
        while s0 < DUR[24][0] / 30 - 0.2:
            fly(L, t, s0, 0.9, (700, 480), (930, 500), 40, 'coin', 255, 0, 0.9); s0 += 0.35
        fr = Image.alpha_composite(fr, L)
    if t > b:
        C = new(); d = ImageDraw.Draw(C); txt(C, 'CONVERTING', BOLD(44), 600, grey, 255, x=1560); d.ellipse([1400, 440, 1720, 560], outline=red + (255,), width=10); d.line([1420, 545, 1700, 455], fill=red + (255,), width=10)
        fr = POP(fr, C, (1380, 400, 1740, 660), back((t - b) / 0.45))
    return frame(fr)

def b24b(t):
    fr = base(t); fr = title_layer(fr, 'THE CATCH-UP BONUS', t)
    T = lambda m: tt(24, 1, m)
    a = T('Between sixty'); b = T('add eleven thousand'); c = T('instead of the usual')
    for i, age in enumerate([60, 61, 62, 63]):
        fr = year_medal(fr, t, 340 + i * 170, 300, age, a + i * 0.25, green, 62) if t > a - 0.1 else fr
    base_y = 860; sc = 400 / 11250
    L = new(); d = ImageDraw.Draw(L); d.line([900, base_y, 1700, base_y], fill=gold + (255,), width=3)
    if t > b:
        u = ease((t - b) / 1.0); d.rounded_rectangle([1250, base_y - 11250 * sc * u, 1450, base_y], radius=14, fill=green + (255,)); txt(L, '$11,250', BOLD(60), base_y - 11250 * sc * u - 80, green, 255 * u, x=1350); txt(L, 'AGES 60-63', BOLD(30), base_y + 14, green, 255, x=1350)
    if t > c:
        u = ease((t - c) / 0.8); d.rounded_rectangle([950, base_y - 8000 * sc * u, 1150, base_y], radius=14, fill=gold + (255,)); txt(L, '$8,000', BOLD(60), base_y - 8000 * sc * u - 80, gold, 255 * u, x=1050); txt(L, 'THE USUAL', BOLD(30), base_y + 14, gold, 255, x=1050)
    fr = Image.alpha_composite(fr, L)
    C = new(); vault(C, 400, 620, 110, t, 0.3); txt(C, '401(k)', BOLD(50), 780, gold, 255, x=400); fr = POP(fr, C, (250, 480, 560, 830), back((t - 0.5) / 0.5))
    if t > b:
        L = new(); s0 = b
        while s0 < DUR[24][1] / 30 - 0.3:
            fly(L, t, s0, 1.0, (820, 640), (540, 620), 40, 'bill', 255, 0, 0.6); s0 += 0.45
        fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: IRS Notice 2025-67'))

def b24c(t):
    fr = base(t); fr = title_layer(fr, 'THE 61 WINDOW', t)
    T = lambda m: tt(24, 2, m)
    a = T('up to thirty-five'); b = T('if the plan allows'); c = T("At sixty-one"); d_ = T('it closes after')
    base_y = 830; sc = 360 / 35750
    L = new(); d = ImageDraw.Draw(L); u = ease((t - 0.3) / 1.0)
    d.rounded_rectangle([300, base_y - 24500 * sc * u, 480, base_y], radius=14, fill=gold + (255,)); d.rounded_rectangle([300, base_y - 35750 * sc * u, 480, base_y - 24500 * sc * u], radius=14, fill=green + (255,)); d.line([260, base_y, 520, base_y], fill=gold + (255,), width=3)
    v = 35750 * ease((t - a + 0.3) / 1.4) if t > a - 0.3 else 0
    txt(L, f'${int(v // 50 * 50):,}', BOLD(110), 420, green, 255 * ease((t - a + 0.3) / 0.3), x=880) if t > a - 0.3 else None
    txt(L, 'UP TO', BOLD(36), 370, white, 255 * ease((t - a + 0.3) / 0.3), x=880) if t > a - 0.3 else None
    fr = Image.alpha_composite(fr, L)
    if t > b: fr = pill_pop(fr, 'IF THE PLAN ALLOWS IT', 600, t, b, gold, navy, size=38, cx=880)
    if t > c - 0.3:
        for i, age in enumerate([60, 61, 62, 63]):
            fr = year_medal(fr, t, 1200 + i * 150, 350, age, c - 0.3 + i * 0.2, gold if age == 61 else green, 58)
        C = new(); crown(C, 1350, 250, 1.0); fr = POP(fr, C, (1290, 190, 1410, 260), back((t - c - 0.4) / 0.45)) if t > c else fr
    if t > d_ - 0.6:
        C = new(); door(C, 1500, 700, 180, 260, red, 255, open_p=max(0, 0.9 - (t - d_ + 0.6) * 0.8)); padlock(C, 1500, 700, 0.55, red, 255) if t > d_ + 0.4 else None
        txt(C, 'CLOSES AFTER 63', BOLD(34), 850, red, 255, x=1500); fr = POP(fr, C, (1330, 560, 1680, 890), back((t - d_ + 0.6) / 0.45))
    return frame(SRC(fr, 'Source: IRS Notice 2025-67'))

# ================= BLOCK 25 =================
def b25a(t):
    fr = base(t); fr = title_layer(fr, 'PRE-TAX CONTRIBUTIONS', t)
    T = lambda m: tt(25, 0, m)
    a = T('money you put'); b = T('a traditional four-oh-one-k'); c = T('comes out of your taxable')
    C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([240, 340, 640, 640], radius=18, fill=(236, 240, 245, 255)); txt(C, 'PAYCHECK', BOLD(40), 365, navy, 255, x=440); d.rectangle([290, 450, 590, 466], fill=(150, 165, 190, 255)); d.rectangle([290, 500, 520, 516], fill=(150, 165, 190, 255)); txt(C, '$$$', BOLD(60), 545, green, 255, x=440)
    fr = POP(fr, C, (230, 330, 650, 650), back((t - 0.3) / 0.5))
    if t > b - 0.3:
        C = new(); vault(C, 1000, 500, 100, t, 0.3); txt(C, 'TRADITIONAL 401(k)', BOLD(34), 640, gold, 255, x=1000); fr = POP(fr, C, (800, 380, 1200, 700), back((t - b + 0.3) / 0.45))
    L = new(); s0 = a
    while s0 < DUR[25][0] / 30 - 0.3:
        fly(L, t, s0, 1.2, (660, 480), (920, 500), 60, 'bill', 255, 0, 0.6); s0 += 0.45
    fr = Image.alpha_composite(fr, L)
    if t > c - 0.3:
        C = new(); lev = 0.8 - 0.45 * ease((t - c) / 1.2); thermo(C, 1560, 300, 760, lev, gold); txt(C, 'TAXABLE', BOLD(30), 790, white, 255, x=1560); txt(C, 'INCOME', BOLD(30), 826, white, 255, x=1560)
        fr = POP(fr, C, (1440, 280, 1680, 870), back((t - c + 0.3) / 0.45))
        L = new(); d = ImageDraw.Draw(L); u = ease((t - c) / 0.8); d.line([1440, 420, 1440, 420 + 160 * u], fill=green + (255,), width=10); d.polygon([(1440, 600), (1420, 570), (1460, 570)], fill=green + (255,)) if u > 0.9 else None; fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b25b(t):
    fr = base(t); fr = title_layer(fr, 'PUSH UP, PULL DOWN', t)
    T = lambda m: tt(25, 1, m)
    a = T('conversions push'); b = T('pre-tax contributions'); c = T('stay under a line')
    L = new(); d = ImageDraw.Draw(L)
    lev = 0.5
    if t > a: lev = 0.5 + 0.42 * ease((t - a) / 0.8)
    if t > b: lev = 0.92 - 0.55 * ease((t - b) / 0.9)
    thermo(L, 960, 280, 820, lev, red if lev > 0.72 else gold)
    d.line([800, 420, 1120, 420], fill=red + (255,), width=8); txt(L, 'THE LINE', BOLD(30), 380, red, 255, x=1230)
    fr = Image.alpha_composite(fr, L)
    if t > a - 0.2:
        C = new(); up_arrow(C, 500, 520, 1.1, red, 255); txt(C, 'CONVERSIONS', BOLD(40), 680, red, 255, x=500); fr = POP(fr, C, (330, 400, 670, 730), back((t - a + 0.2) / 0.45))
    if t > b - 0.2:
        C = new(); d = ImageDraw.Draw(C); d.polygon([(1440, 640), (1510, 560), (1468, 560), (1468, 460), (1412, 460), (1412, 560), (1370, 560)], fill=green + (255,)); txt(C, 'PRE-TAX', BOLD(40), 680, green, 255, x=1440); txt(C, 'CONTRIBUTIONS', BOLD(32), 730, green, 255, x=1440); fr = POP(fr, C, (1250, 430, 1650, 780), back((t - b + 0.2) / 0.45))
    if t > c:
        C = new(); check(C, 1120, 500, 40, green); fr = POP(fr, C, (1060, 440, 1180, 560), back((t - c) / 0.4))
        fr = pill_pop(fr, 'UNDER THE LINE', 200, t, c, green, navy, size=42)
    return frame(fr)

def b25c(t):
    fr = base(t); fr = title_layer(fr, 'TWO TOOLS, ONE PLAN', t)
    T = lambda m: tt(25, 2, m)
    a = T('opposite directions'); b = T('using them together'); c = T('powerful')
    C = new(); d = ImageDraw.Draw(C); d.ellipse([260, 340, 560, 640], outline=red + (255,), width=10); d.polygon([(410, 380), (500, 480), (450, 480), (450, 600), (370, 600), (370, 480), (320, 480)], fill=red + (255,)); txt(C, 'CONVERSION', BOLD(38), 670, red, 255, x=410)
    fr = POP(fr, C, (250, 330, 570, 720), back((t - 0.3) / 0.5))
    if t > a - 0.3:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([1360, 340, 1660, 640], outline=green + (255,), width=10); d.polygon([(1510, 600), (1600, 500), (1550, 500), (1550, 380), (1470, 380), (1470, 500), (1420, 500)], fill=green + (255,)); txt(C, 'CONTRIBUTION', BOLD(38), 670, green, 255, x=1510)
        fr = POP(fr, C, (1350, 330, 1670, 720), back((t - a + 0.3) / 0.5))
    if t > b:
        C = new(); shield(C, 960, 500, 2.0, 255, gold); txt(C, '+', BOLD(110), 450, gold, 255, x=960); fr = POP(fr, C, (800, 310, 1120, 700), back((t - b) / 0.5))
        L = new(); rot_a = t * 60
        for k in range(8):
            a2 = math.radians(rot_a + k * 45); coin(L, 960 + 300 * math.cos(a2), 500 + 300 * math.sin(a2), 20, 255, squash=abs(math.cos(t * 4 + k)) * 0.6 + 0.4)
        fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'WHERE PLANNING GETS POWERFUL', 840, t, c - 0.2, gold, navy, size=44)
    return frame(fr)

# ================= BLOCK 26 =================
def tl_axis(fr, x0, x1, ya, ages, ax):
    L = new(); d = ImageDraw.Draw(L); d.line([x0, ya, x1, ya], fill=gold + (255,), width=3)
    for a in ages: d.line([ax(a), ya - 8, ax(a), ya + 8], fill=gold + (255,), width=3); txt(L, str(a), BOLD(30), ya + 16, grey, 255, x=ax(a))
    return Image.alpha_composite(fr, L)

def b26a(t):
    fr = base(t); fr = title_layer(fr, 'WHERE THEY END UP', t)
    T = lambda m: tt(26, 0, m)
    ax = lambda a: 330 + (a - 61) / 4 * 1300
    fr = person_box(fr, 'FRANK', 190, 470, blue, t, 0.2, 1.7) if False else fr
    C = new(); avatar(C, 200, 520, blue, 1.6); txt(C, 'FRANK', BOLD(40), 610, blue, 255, x=200); fr = POP(fr, C, (110, 420, 300, 670), back((t - 0.3) / 0.5))
    fr = tl_axis(fr, 330, 1630, 780, [61, 62, 63, 64, 65], ax)
    a = T('did nothing'); b = T('claimed Social Security'); c = T('started converting')
    if t > a:
        C = new(); txt(C, 'zzz', BOLD(70), 540, grey, 255, x=(ax(61) + ax(62)) / 2); txt(C, 'NOTHING', BOLD(36), 620, grey, 255, x=(ax(61) + ax(62)) / 2); fr = POP(fr, C, (ax(61) - 20, 500, ax(62) + 20, 670), back((t - a) / 0.45))
    if t > b:
        C = new(); ss_card(C, ax(62), 610, 0.6); txt(C, 'CLAIMS EARLY', BOLD(30), 700, blue, 255, x=ax(62)); fr = POP(fr, C, (ax(62) - 130, 520, ax(62) + 130, 730), back((t - b) / 0.45))
    if t > c:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - c) / 0.9); d.rounded_rectangle([ax(63) - 60, 770 - 300 * u, ax(63) + 60, 770], radius=14, fill=red + (255,)); txt(L, 'CONVERTS', BOLD(32), 470, red, 255 * u, x=ax(63)); fr = Image.alpha_composite(fr, L)
        L = new(); s0 = c
        while s0 < DUR[26][0] / 30 - 0.2:
            fly(L, t, s0, 0.9, (ax(63) - 200, 500), (ax(63), 600), 40, 'bill', 255, 0, 0.6); s0 += 0.35
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b26b(t):
    fr = base(t); fr = title_layer(fr, "MARY'S WINDOW", t)
    T = lambda m: tt(26, 0, m) if False else tt(26, 1, m)
    ax = lambda a: 330 + (a - 61) / 4 * 1300
    C = new(); avatar(C, 200, 520, green, 1.6); txt(C, 'MARY', BOLD(40), 610, green, 255, x=200); fr = POP(fr, C, (110, 420, 300, 670), back((t - 0.3) / 0.5))
    fr = tl_axis(fr, 330, 1630, 780, [61, 62, 63, 64, 65], ax)
    a = T('as a window'); b = T('checked her lines'); c = T('converted a piece'); d_ = T('chose her Social Security'); e = T('running the numbers')
    if t > a - 0.3:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - a + 0.3) / 0.6); d.rounded_rectangle([ax(61) - 40, 300, ax(62) + 40, 780], radius=30, outline=green + (255,), width=8); txt(L, 'THE WINDOW', BOLD(38), 250, green, 255 * u, x=(ax(61) + ax(62)) / 2); fr = Image.alpha_composite(fr, L)
    if t > b:
        C = new(); magnifier(C, ax(61), 480, 46); fr = POP(fr, C, (ax(61) - 70, 400, ax(61) + 150, 640), back((t - b) / 0.45))
    if t > c:
        for i, age in enumerate([61, 62]):
            st = c + i * 0.8
            if t > st:
                L = new(); d = ImageDraw.Draw(L); u = ease((t - st) / 0.6); d.rounded_rectangle([ax(age) + 40, 770 - 140 * u, ax(age) + 120, 770], radius=12, fill=green + (255,)); fr = Image.alpha_composite(fr, L)
        txt_l = new(); txt(txt_l, 'A PIECE EACH YEAR', BOLD(30), 560, green, 255, x=(ax(61) + ax(62)) / 2 + 60); fr = Image.alpha_composite(fr, txt_l)
    if t > e - 0.4:
        C = new(); calculator(C, ax(63) - 20, 500, 0.6); fr = POP(fr, C, (ax(63) - 90, 380, ax(63) + 60, 630), back((t - e + 0.4) / 0.45))
    if t > d_:
        C = new(); ss_card(C, ax(64) + 60, 560, 0.6); txt(C, 'CHOSEN DATE', BOLD(28), 650, blue, 255, x=ax(64) + 60); fr = POP(fr, C, (ax(64) - 70, 470, ax(64) + 190, 690), back((t - d_) / 0.45))
    return frame(fr)

def b26c(t):
    fr = base(t); fr = title_layer(fr, 'AT AGE 65', t)
    T = lambda m: tt(26, 2, m)
    a = T('Frank opens'); b = T('Mary opens')
    C = new(); medicare_card(C, 500, 520, 1.3); txt(C, 'FRANK', BOLD(44), 700, blue, 255, x=500); txt(C, '$284.10', BOLD(80), 780, red, 255, x=500); fr = POP(fr, C, (250, 380, 750, 860), back((t - a + 0.3) / 0.5)) if t > a - 0.3 else fr
    if t > a:
        fr = pill_pop(fr, '+ SURCHARGE', 230, t, a + 0.3, red, size=42, cx=500)
        L = new(); s0 = a + 0.3
        while s0 < b:
            fly(L, t, s0, 1.0, (500, 600), (760, 420), 60, 'bill', 255, 0, 0.6); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
    if t > b - 0.3:
        C = new(); medicare_card(C, 1420, 520, 1.3); txt(C, 'MARY', BOLD(44), 700, green, 255, x=1420); txt(C, '$202.90', BOLD(80), 780, green, 255, x=1420); check(C, 1600, 400, 30, green); fr = POP(fr, C, (1170, 380, 1680, 860), back((t - b + 0.3) / 0.5))
        fr = pill_pop(fr, 'STANDARD PREMIUM', 230, t, b + 0.3, green, navy, size=42, cx=1420)
        L = new(); rain(L, t, b + 0.3, 1200, 1640, 400, n=6, seed=131, r=20, dur=2.5); fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: CMS, 2026 Part B premiums'))

# ================= BLOCK 27 =================
NODES = [('TWO-YEAR', 'RULE', 'cal'), ('INCOME', 'CLIFFS', 'cliff'), ('SOCIAL SECURITY', 'TAX', 'ss'), ('HEALTH', 'CLIFF', 'cross'), ('CATCH-UP', 'WINDOW', 'coins')]
def recap(fr, t, shown_at, hi=False, pulse=False):
    cx, cy, R = 960, 560, 300
    L = new(); d = ImageDraw.Draw(L)
    for k in range(5):
        if t < shown_at[k]: continue
        ang = math.radians(-90 + k * 72); x = cx + R * math.cos(ang) * 1.35; y = cy + R * math.sin(ang)
        col = red if k in (1, 3) else gold
        d.line([x, y, cx, cy], fill=A(col, 255 if not pulse else 160 + 95 * math.sin(t * 6)), width=6)
    fr = Image.alpha_composite(fr, L)
    C = new(); d = ImageDraw.Draw(C); r = 110 + (10 * math.sin(t * 5) if pulse else 0)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=gold + (255,)); txt(C, '61' if not hi else '61+62', BOLD(110 if not hi else 70), cy - (60 if not hi else 40), navy, 255, x=cx)
    fr = Image.alpha_composite(fr, C)
    for k in range(5):
        if t < shown_at[k]: continue
        ang = math.radians(-90 + k * 72); x = cx + R * math.cos(ang) * 1.35; y = cy + R * math.sin(ang)
        col = red if k in (1, 3) else gold
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([x - 150, y - 60, x + 150, y + 60], radius=20, fill=A(card, 255), outline=A(col, 255), width=4)
        d.ellipse([x - 140, y - 24, x - 92, y + 24], fill=A(col, 255)); txt(C, str(k + 1), BOLD(34), y - 20, navy, 255, x=x - 116)
        txt(C, NODES[k][0], BOLD(24), y - 34, white, 255, x=x + 30); txt(C, NODES[k][1], BOLD(30), y + 2, col, 255, x=x + 30)
        fr = POP(fr, C, (x - 160, y - 70, x + 160, y + 70), back((t - shown_at[k]) / 0.4))
    return fr

def b27a(t):
    fr = base(t); fr = title_layer(fr, 'THE 5 REASONS', t)
    T = lambda m: tt(27, 0, m)
    sh = [T('One:'), T('Two:'), 1e9, 1e9, 1e9]
    return frame(recap(fr, t, sh))

def b27b(t):
    fr = base(t); fr = title_layer(fr, 'THE 5 REASONS', t)
    T = lambda m: tt(27, 1, m)
    sh = [0.0, 0.0, T('Three:'), T('Four:'), T('Five:')]
    return frame(recap(fr, t, sh))

def b27c(t):
    fr = base(t); fr = title_layer(fr, 'ONE SHARED WINDOW', t)
    sh = [0.0] * 5
    fr = recap(fr, t, sh, hi=t > 0.6, pulse=True)
    fr = pill_pop(fr, 'THE SAME TWO YEARS', 900, t, 0.6, gold, navy, size=40)
    return frame(fr)

# ================= BLOCK 28 =================
def b28a(t):
    fr = base(t); fr = title_layer(fr, 'WHAT TO DO THIS YEAR', t)
    T = lambda m: tt(28, 0, m)
    a = T('One:'); b = T('find your modified'); c = T('compare it with')
    if t > a - 0.2:
        C = new(); tax_form(C, 300, 300, 420, 500, 255, 'TAX'); d = ImageDraw.Draw(C); d.rounded_rectangle([340, 520, 680, 580], radius=10, outline=gold + (255,), width=6); txt(C, 'MAGI', BOLD(40), 528, gold, 255, x=510) if t > b else None
        fr = POP(fr, C, (290, 290, 730, 810), back((t - a + 0.2) / 0.5))
    if t > b:
        C = new(); magnifier(C, 700, 560, 60); fr = POP(fr, C, (620, 470, 860, 700), back((t - b) / 0.45))
    if t > c - 0.3:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - c + 0.3) / 0.7)
        for k, (lab, col) in enumerate([('SINGLE: $109,000', blue), ('MARRIED: $218,000', gold)]):
            y = 420 + k * 170
            for x in range(1000, int(1000 + 620 * u), 30): d.line([x, y, x + 16, y], fill=col + (255,), width=6)
            txt(L, lab, BOLD(36), y - 56, col, 255 * u, x=1310)
        fr = Image.alpha_composite(fr, L)
        C = new(); medicare_card(C, 1310, 760, 0.5); fr = POP(fr, C, (1230, 700, 1400, 810), back((t - c) / 0.45))
    return frame(rail(fr, 1, t))

def b28b(t):
    fr = base(t); fr = title_layer(fr, 'MARK THE YEAR', t)
    T = lambda m: tt(28, 1, m)
    a = T('write down'); b = T('sixty-three'); c = T('the one that counts')
    C = new(); cal_card(C, 300, 260, 780, 700, 'THE YEAR YOU TURN', '63', 220, gold); fr = POP(fr, C, (290, 250, 790, 710), back((t - b + 0.4) / 0.5)) if t > b - 0.4 else fr
    if t > a - 0.3:
        C = new(); d = ImageDraw.Draw(C); d.polygon([(1150, 560), (1270, 440), (1310, 480), (1190, 600)], fill=gold + (255,)); d.polygon([(1150, 560), (1190, 600), (1130, 620)], fill=white + (255,))
        d.line([1000, 650, 1300, 650], fill=white + (255,), width=6); txt(C, 'WRITE IT DOWN', BOLD(50), 700, gold, 255, x=1150)
        fr = POP(fr, C, (960, 400, 1360, 780), back((t - a + 0.3) / 0.45))
    if t > c:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - c) / 0.6); d.ellipse([260, 220, 820, 740], outline=A(red, 255 * u), width=10); fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'THAT RETURN COUNTS', 820, t, c + 0.2, red, size=42, cx=540)
    return frame(rail(fr, 2, t))

def b28c(t):
    fr = base(t); fr = title_layer(fr, 'BEFORE ANY ROTH CONVERSION', t, size=54)
    T = lambda m: tt(28, 2, m)
    a = T('the Medicare line'); b = T('the Social Security tax'); c = T('the health insurance cliff')
    items = [(a, 'MEDICARE', 'LINE', red, 'med'), (b, 'SOCIAL SECURITY', 'TAX LINES', gold, 'ss'), (c, 'HEALTH INSURANCE', 'CLIFF', purple, 'cross')]
    for k, (st, l1, l2, col, ic) in enumerate(items):
        if t < st - 0.2: continue
        cx = 420 + k * 540; C = new(); d = ImageDraw.Draw(C)
        card_box(C, cx - 230, 280, cx + 230, 700, col, card, 255, 5)
        if ic == 'med': medicare_card(C, cx, 430, 0.6)
        elif ic == 'ss': ss_card(C, cx, 430, 0.6)
        else: d.rectangle([cx - 44, 424, cx + 44, 452], fill=A(red, 255)); d.rectangle([cx - 14, 394, cx + 14, 484], fill=A(red, 255))
        txt(C, l1, BOLD(34), 540, white, 255, x=cx); txt(C, l2, BOLD(38), 590, col, 255, x=cx)
        if t > st + 0.7: check(C, cx, 660, 28, green)
        fr = POP(fr, C, (cx - 240, 270, cx + 240, 710), back((t - st + 0.2) / 0.45))
    return frame(rail(fr, 3, t))

# ================= BLOCK 29 =================
def b29a(t):
    fr = base(t); fr = title_layer(fr, 'IF YOUR INCOME ALREADY DROPPED', t, size=54)
    T = lambda m: tt(29, 0, m)
    a = T('has already dropped'); e1 = T('you retired'); e2 = T('cut your hours'); e3 = T('lost a pension'); f = T('ask Social Security'); g = T('Form S-S-A')
    L = new(); d = ImageDraw.Draw(L); x0, x1, yb, yt = 260, 900, 700, 330
    d.line([x0, yb, x1, yb], fill=gold + (255,), width=3); d.line([x0, yb, x0, yt - 20], fill=gold + (255,), width=3)
    u = ease((t - a + 0.2) / 1.6) if t > a - 0.2 else 0
    pts = [(x0 + (x1 - x0) * i / 30, yt + 20 + (yb - yt - 60) * (i / 30) ** 1.5) for i in range(int(30 * u) + 1)]
    if len(pts) > 1: d.line(pts, fill=red + (255,), width=10, joint='curve')
    txt(L, 'YOUR INCOME', BOLD(32), yt - 50, white, 255 * ease((t - a + 0.2) / 0.4), x=580) if t > a - 0.2 else None
    fr = Image.alpha_composite(fr, L)
    for k, (st, lab) in enumerate([(e1, 'RETIRED'), (e2, 'CUT HOURS'), (e3, 'LOST PENSION')]):
        if t > st:
            C = new(); x = 330 + k * 230
            if k == 0: avatar(C, x, 800, gold, 0.9)
            elif k == 1: clock(C, x, 790, 40, t, goldL, 255)
            else: money_bag(C, x, 790, 0.5); cross(C, x + 40, 760, 22, red)
            txt(C, lab, BOLD(24), 850, white, 255, x=x); fr = POP(fr, C, (x - 90, 700, x + 90, 890), back((t - st) / 0.4))
    if t > f - 0.2:
        C = new(); ss_card(C, 1240, 440, 1.0); fr = POP(fr, C, (1060, 320, 1420, 560), back((t - f + 0.2) / 0.5))
        L = new(); d = ImageDraw.Draw(L); d.line([1000, 480, 1060, 480], fill=goldL + (255,), width=8); fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'ASK TO REASSESS', 620, t, f, gold, navy, size=40, cx=1240)
    if t > g - 0.2:
        C = new(); tax_form(C, 1520, 330, 200, 250, 255, 'SSA-44'); fr = POP(fr, C, (1510, 320, 1730, 600), back((t - g + 0.2) / 0.45))
    return frame(rail(fr, 4, t))

def b29b(t):
    fr = base(t); fr = title_layer(fr, 'GET IT IN WRITING', t)
    T = lambda m: tt(29, 1, m)
    a = T('get every number'); b = T('from a tax professional'); c = T('fiduciary advisor'); d_ = T('before you convert'); e = T('change every year'); f = T('twenty-six ones')
    if t > a - 0.3:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([260, 300, 640, 780], radius=16, fill=(236, 240, 245, 255), outline=gold + (255,), width=5)
        u = ease((t - a) / 1.4)
        for k in range(6):
            if u > k / 6: d.rectangle([300, 350 + k * 60, 300 + 300 * min(1, (u - k / 6) * 6), 368 + k * 60], fill=(120, 135, 160, 255))
        txt(C, 'IN WRITING', BOLD(36), 730, navy, 255, x=450) if u > 0.9 else None
        fr = POP(fr, C, (250, 290, 650, 800), back((t - a + 0.3) / 0.45))
    if t > b - 0.2:
        C = new(); avatar(C, 860, 470, gold, 1.5); txt(C, 'TAX PROFESSIONAL', BOLD(26), 540, gold, 255, x=860); fr = POP(fr, C, (720, 380, 1000, 580), back((t - b + 0.2) / 0.45))
    if t > c - 0.2:
        C = new(); avatar(C, 1160, 470, blue, 1.5); txt(C, 'FIDUCIARY ADVISOR', BOLD(26), 540, blue, 255, x=1160); fr = POP(fr, C, (1010, 380, 1310, 580), back((t - c + 0.2) / 0.45))
    if t > d_:
        C = new(); vault(C, 1560, 470, 70, t, 0.3); txt(C, 'BEFORE YOU CONVERT', BOLD(24), 570, gold, 255, x=1560); fr = POP(fr, C, (1420, 380, 1700, 600), back((t - d_) / 0.45))
        L = new(); d = ImageDraw.Draw(L); d.line([1330, 470, 1440, 470], fill=goldL + (255,), width=8); d.polygon([(1456, 470), (1430, 452), (1430, 488)], fill=goldL + (255,)); fr = Image.alpha_composite(fr, L)
    if t > e - 0.2:
        C = new(); cal_card(C, 800, 640, 1120, 800, 'EVERY YEAR', 'NEW', 60, red); fr = POP(fr, C, (790, 630, 1130, 810), back((t - e + 0.2) / 0.45))
        L = new(); vals = ['$109,000', '$113,000', '$117,000']; k = int((t - e) * 2) % 3; txt(L, vals[k] + '?', BOLD(44), 690, red, 255, x=1400); fr = Image.alpha_composite(fr, L)
    if t > f: fr = stamp(fr, 'THESE ARE THE 2026 NUMBERS', 960, 760, -4, gold, back((t - f) / 0.45), 40) if False else stamp(fr, '2026 NUMBERS', 1500, 780, -6, gold, back((t - f) / 0.45), 46)
    return frame(rail(fr, 5, t))

# ================= BLOCK 30 =================
def b30a(t):
    fr = base(t); fr = title_layer(fr, 'ALREADY 63 OR 64?', t)
    T = lambda m: tt(30, 0, m)
    a = T("It's not too late")
    for i, age in enumerate([63, 64]):
        fr = year_medal(fr, t, 700 + i * 520, 470, age, 0.3 + i * 0.3, gold, 120)
    C = new(); txt(C, '?', BOLD(150), 340, red, 255, x=960); fr = POP(fr, C, (900, 300, 1020, 500), back((t - 1.0) / 0.4)) if t < a else fr
    if t > a:
        C = new(); check(C, 960, 470, 70, green); fr = POP(fr, C, (860, 380, 1060, 560), back((t - a) / 0.4))
        fr = pill_pop(fr, "IT'S NOT TOO LATE", 760, t, a, green, navy, size=54)
    return frame(fr)

def b30b(t):
    fr = base(t); fr = title_layer(fr, 'STILL TIME TO ACT', t)
    T = lambda m: tt(30, 1, m)
    a = T('recalculated every year'); b = T('your next tax return'); c = T('if your income drops'); d_ = T('The free years'); e = T('smart years')
    if t > a - 0.3:
        yrs = ['2027', '2028', '2029', '2030']
        L = new(); k = int((t - a + 0.3) * 1.6) % 4
        C = new(); cal_card(C, 300, 300, 680, 640, 'RECALCULATED', yrs[k], 120, blue); fr = POP(fr, C, (290, 290, 690, 650), back((t - a + 0.3) / 0.45))
    if t > b:
        C = new(); tax_form(C, 820, 360, 200, 250, 255, 'TAX'); fr = POP(fr, C, (810, 350, 1030, 620), back((t - b) / 0.45))
    if t > c - 0.2:
        C = new(); door(C, 1300, 500, 160, 240, gold, 255, open_p=0.8); txt(C, 'REASSESSMENT ROUTE', BOLD(28), 660, gold, 255, x=1300); txt(C, 'STILL OPEN', BOLD(34), 700, green, 255, x=1300); fr = POP(fr, C, (1130, 350, 1480, 740), back((t - c + 0.2) / 0.45))
    if t > d_:
        C = new(); padlock(C, 1650, 470, 0.6, red, 255); txt(C, 'FREE YEARS', BOLD(24), 550, red, 255, x=1650); fr = POP(fr, C, (1560, 360, 1760, 590), back((t - d_) / 0.45))
    if t > e:
        C = new(); bulb(C, 960, 800, 0.9); fr = POP(fr, C, (860, 700, 1060, 880), back((t - e) / 0.45))
        fr = pill_pop(fr, 'THE SMART YEARS ARE NOT GONE', 900, t, e + 0.2, gold, navy, size=36, cx=1300)
    return frame(fr)

# ================= BLOCK 31 =================
def b31a(t):
    fr = base(t); fr = title_layer(fr, "61 ISN'T A MAGIC BIRTHDAY", t, size=54)
    T = lambda m: tt(31, 0, m)
    a = T('last age'); b = T('two full years'); c = T('starts reading')
    C = new(); d = ImageDraw.Draw(C); d.ellipse([260, 340, 560, 640], fill=gold + (255,)); txt(C, '61', BOLD(170), 400, navy, 255, x=410); fr = POP(fr, C, (250, 330, 570, 650), back((t - 0.3) / 0.5))
    C = new(); d = ImageDraw.Draw(C); d.line([300, 340, 520, 600], fill=red + (255,), width=14); d.line([520, 340, 300, 600], fill=red + (255,), width=14); fr = POP(fr, C, (280, 320, 540, 620), back((t - 1.0) / 0.4)) if t > 1.0 else fr
    if t > a:
        ax = lambda x: 700 + (x - 61) / 3 * 900
        L = new(); d = ImageDraw.Draw(L); d.line([700, 700, 1600, 700], fill=gold + (255,), width=3)
        for age in [61, 62, 63]: d.ellipse([ax(age) - 18, 682, ax(age) + 18, 718], fill=(gold if age < 63 else red) + (255,)); txt(L, str(age), BOLD(34), 730, gold if age < 63 else red, 255, x=ax(age))
        fr = Image.alpha_composite(fr, L)
    if t > b:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - b) / 0.8); d.rounded_rectangle([700, 630, 700 + 600 * u, 660], radius=14, fill=green + (255,)); txt(L, '2 FULL YEARS TO ACT', BOLD(40), 560, green, 255 * u, x=1000); fr = Image.alpha_composite(fr, L)
    if t > c:
        C = new(); eye(C, 1600, 540, 1.0, 255, t); medicare_card(C, 1600, 400, 0.4); fr = POP(fr, C, (1480, 320, 1720, 610), back((t - c) / 0.45))
    return frame(fr)

def b31b(t):
    fr = base(t); fr = title_layer(fr, 'THANK YOU FOR WATCHING', t, size=54)
    T = lambda m: tt(31, 1, m)
    a = T('If this helped'); b = T('hit subscribe'); c = T('And if you want'); d_ = T('fifty-nine and a half')
    if t > a - 0.2:
        C = new(); thumbs_up(C, 330, 470, 1.6); fr = POP(fr, C, (190, 330, 470, 620), back((t - a + 0.2) / 0.45))
        fr = pill_pop(fr, 'IF THIS HELPED YOU', 250, t, a, gold, navy, size=38, cx=420)
    if t > b:
        fr = pill_pop(fr, 'HIT SUBSCRIBE', 690, t, b, red, size=42, cx=420) if False else pill_pop(fr, 'HIT SUBSCRIBE', 640, t, b, red, size=42, cx=470)
    # dashed video box (end screen slot)
    xa, ya_, xb, yb = 1080, 290, 1740, 661
    L = new(); d = ImageDraw.Draw(L)
    for i in range(0, 66):
        x = xa + i * 10
        if i % 2 == 0: d.line([x, ya_, min(x + 6, xb), ya_], fill=goldL + (255,), width=5); d.line([x, yb, min(x + 6, xb), yb], fill=goldL + (255,), width=5)
    for j in range(0, 38):
        y = ya_ + j * 10
        if j % 2 == 0: d.line([xa, y, xa, min(y + 6, yb)], fill=goldL + (255,), width=5); d.line([xb, y, xb, min(y + 6, yb)], fill=goldL + (255,), width=5)
    txt(L, 'WHAT CHANGES AT 59\u00bd', SER(46), 450, (110, 130, 160), 255, x=(xa + xb) / 2)
    fr = Image.alpha_composite(fr, L) if t > c - 0.6 else fr
    if t > c - 0.2:
        L = new(); pulse = 6 * math.sin(t * 4); txt(L, 'WATCH NEXT', BOLD(56), 720, gold, 255 * ease((t - c + 0.2) / 0.4), x=(xa + xb) / 2)
        d = ImageDraw.Draw(L); d.polygon([(1410, 800 + pulse), (1370, 770 + pulse), (1450, 770 + pulse)], fill=A(gold, 255 * ease((t - c + 0.2) / 0.4)))
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

SLIDES = {21: [b21a, b21b, b21c], 22: [b22a, b22b, b22c], 23: [b23a, b23b, b23c], 24: [b24a, b24b, b24c], 25: [b25a, b25b, b25c], 26: [b26a, b26b, b26c], 27: [b27a, b27b, b27c], 28: [b28a, b28b, b28c], 29: [b29a, b29b], 30: [b30a, b30b], 31: [b31a, b31b]}

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'preview':
        sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(SLIDES)
        fq = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                fn(DUR[b][i] / 30 * fq).convert('RGB').save(f'/home/claude/pz_{b}_{i}.png')
        print({b: DUR[b] for b in sel}, 'ok')
    else:
        sel = [int(x) for x in sys.argv[2].split(',')]
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                render_fast(fn, DUR[b][i], f'/mnt/user-data/outputs/v4-b{b}-0{i + 1}.mp4')
                print('done', b, i + 1, DUR[b][i], flush=True)
