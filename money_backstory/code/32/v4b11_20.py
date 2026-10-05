from v3lib import *
from v3b3_10 import POP, new, lerp, fly, person_box
from v3b11_21 import crown, stop_sign
from v4b2_10 import medicare_card, cal_card, eye, envelope, SRC, badge61, cliff_icon
import sys, math

SENT = {
 11: ["So why sixty-one?", "Because the return for the year you turn sixty-three is the first one Medicare will read.", "That means the years you turn sixty-one and sixty-two are the last two years when extra income can't touch your Medicare premiums, assuming you enroll at sixty-five.", "Two free years, and then the door closes."],
 12: ["How do people use those two free years?", "The most common tool is a Roth conversion.", "You move money from a traditional IRA or four-oh-one-k into a Roth, and you pay income tax on that amount now.", "In exchange, the money grows tax-free, and qualified withdrawals later don't push your income up."],
 13: ["Here's the catch.", "A conversion counts as income in the year you do it.", "Convert at sixty-one or sixty-two, and Medicare never sees it.", "Convert at sixty-three, and two years later it can show up on your Medicare bill.", "Same conversion, same tax bill today, different Medicare price."],
 14: ["Picture it with Frank and Mary.", "Mary decides to move a piece of her traditional savings into a Roth in each of the next two years.", "Frank waits.", "At sixty-three he panics and converts a big amount in a single year.", "Two years later, at sixty-five, his first Medicare letter carries a surcharge that Mary's doesn't."],
 15: ["Now, a conversion is not always the right move.", "It costs real tax today, and for some people paying that tax now is worse than paying it later.", "This video isn't telling you to convert.", "It's telling you to know every line your income might cross before you decide."],
 16: ["Here's a simple way to think about it once you're sixty-three or older.", "Take the Medicare line, subtract the income you already expect, and what's left is your room.", "If the line is one hundred nine thousand dollars and your other income is forty thousand, your room is sixty-nine thousand.", "Stay inside it, and the conversion doesn't touch your premium."],
 17: ["Now for reason number three, the one that surprises almost everyone: a Roth conversion can make your Social Security taxable.", "Your benefit isn't reduced.", "But the government adds half of your benefit to your other income, and if the total crosses a line, part of your benefit becomes taxable income."],
 18: ["For a single filer, the lines are twenty-five thousand and thirty-four thousand dollars.", "For a married couple, thirty-two thousand and forty-four thousand.", "Between the lines, up to fifty percent of your benefit can be counted as taxable income.", "Above the second line, up to eighty-five percent."],
 19: ["That doesn't mean an eighty-five percent tax rate.", "It means up to eighty-five percent of your benefit is added to your taxable income and then taxed at your normal rate.", "And these lines have never been adjusted for inflation, because they were set in the nineteen eighties and nineties."],
 20: ["That's why timing matters at sixty-one.", "If you claim Social Security at sixty-two and convert in the same years, both land on the same tax return.", "If you convert first, before your benefits start, your conversion years stay cleaner.", "It isn't a reason to delay for everyone.", "It's a reason to run the numbers first."],
}
FRAMES = {11: 633, 12: 614, 13: 583, 14: 688, 15: 582, 16: 695, 17: 596, 18: 634, 19: 488, 20: 643}
GROUPS = {11: [[0, 1], [2, 3]], 12: [[0, 1], [2], [3]], 13: [[0, 1], [2, 3], [4]], 14: [[0, 1], [2, 3], [4]], 15: [[0, 1], [2, 3]], 16: [[0, 1], [2, 3]], 17: [[0], [1, 2]], 18: [[0, 1], [2, 3]], 19: [[0, 1], [2]], 20: [[0, 1], [2, 3, 4]]}

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

# ---------- icons ----------
def toolbox(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C)
    d.arc([cx - 60 * s, cy - 110 * s, cx + 60 * s, cy - 20 * s], start=180, end=360, fill=A(goldL, alpha), width=max(3, int(12 * s)))
    d.rounded_rectangle([cx - 130 * s, cy - 60 * s, cx + 130 * s, cy + 80 * s], radius=int(16 * s), fill=A(red, alpha), outline=A(goldL, alpha), width=4)
    d.rectangle([cx - 130 * s, cy - 10 * s, cx + 130 * s, cy + 6 * s], fill=A((120, 30, 30), alpha))
    d.rounded_rectangle([cx - 24 * s, cy - 24 * s, cx + 24 * s, cy + 30 * s], radius=int(6 * s), fill=A(gold, alpha))

def calculator(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 90 * s, cy - 120 * s, cx + 90 * s, cy + 120 * s], radius=int(18 * s), fill=A((40, 52, 74), alpha), outline=A(goldL, alpha), width=4)
    d.rounded_rectangle([cx - 70 * s, cy - 100 * s, cx + 70 * s, cy - 50 * s], radius=int(8 * s), fill=A(green, alpha))
    for r in range(3):
        for c in range(3):
            d.ellipse([cx - 62 * s + c * 50 * s, cy - 24 * s + r * 50 * s, cx - 30 * s + c * 50 * s, cy + 8 * s + r * 50 * s], fill=A(gold if (r + c) % 2 == 0 else grey, alpha))

def hourglass(C, cx, cy, s=1.0, alpha=255, p=0.0):
    d = ImageDraw.Draw(C)
    d.polygon([(cx - 60 * s, cy - 100 * s), (cx + 60 * s, cy - 100 * s), (cx + 6 * s, cy), (cx + 60 * s, cy + 100 * s), (cx - 60 * s, cy + 100 * s), (cx - 6 * s, cy)], outline=A(goldL, alpha), width=max(3, int(8 * s)))
    top = 70 * s * (1 - p); d.polygon([(cx - 45 * s, cy - 92 * s + (70 * s - top)), (cx + 45 * s, cy - 92 * s + (70 * s - top)), (cx, cy - 12 * s)], fill=A(gold, alpha)) if top > 4 else None
    bot = 80 * s * p; d.polygon([(cx - 52 * s, cy + 92 * s), (cx + 52 * s, cy + 92 * s), (cx, cy + 92 * s - bot)], fill=A(gold, alpha)) if bot > 4 else None

def scale_icon(C, cx, cy, tilt, alpha=255):
    d = ImageDraw.Draw(C)
    d.rectangle([cx - 8, cy - 20, cx + 8, cy + 220], fill=A(goldL, alpha)); d.rectangle([cx - 90, cy + 214, cx + 90, cy + 236], fill=A(goldL, alpha))
    a = math.radians(tilt); dx = math.cos(a) * 300; dy = math.sin(a) * 300
    d.line([cx - dx, cy - dy, cx + dx, cy + dy], fill=A(goldL, alpha), width=12)
    for sgn in (-1, 1):
        px = cx + sgn * dx; py = cy + sgn * dy
        d.line([px, py, px - 70, py + 150], fill=A(goldL, alpha), width=5); d.line([px, py, px + 70, py + 150], fill=A(goldL, alpha), width=5)
        d.pieslice([px - 100, py + 110, px + 100, py + 190], 0, 180, fill=A((60, 80, 110), alpha), outline=A(goldL, alpha), width=4)
    return (cx - dx, cy - dy), (cx + dx, cy + dy)

def ss_card(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C); w = 320 * s; h = 200 * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(18 * s), fill=A((236, 240, 245), alpha), outline=A(blue, alpha), width=5)
    txt(C, 'SOCIAL', BOLD(int(34 * s)), cy - h / 2 + 22 * s, blue, alpha, x=cx); txt(C, 'SECURITY', BOLD(int(34 * s)), cy - h / 2 + 62 * s, blue, alpha, x=cx)
    d.rectangle([cx - w / 2 + 30 * s, cy + 30 * s, cx + w / 2 - 30 * s, cy + 42 * s], fill=A((150, 165, 190), alpha)); d.rectangle([cx - w / 2 + 30 * s, cy + 58 * s, cx + w / 2 - 90 * s, cy + 70 * s], fill=A((150, 165, 190), alpha))

def vault_box(C, cx, cy, label, sub, col, t):
    card_box(C, cx - 230, cy - 170, cx + 230, cy + 170, col, card, 255, 5)
    vault(C, cx, cy - 20, 80, t, 0.3)
    txt(C, label, BOLD(38), cy + 90, col, 255, x=cx); txt(C, sub, BOLD(24), cy + 132, white, 255, x=cx)

def year_medal(fr, t, x, y, age, st, col=gold, r=90, dim=False):
    if t < st: return fr
    C = new(); d = ImageDraw.Draw(C)
    d.ellipse([x - r, y - r, x + r, y + r], fill=A(card, 255), outline=A(col, 255), width=8)
    txt(C, str(age), BOLD(int(r * 0.95)), y - r * 0.55, col, 255, x=x)
    return POP(fr, C, (x - r - 10, y - r - 10, x + r + 10, y + r + 10), back((t - st) / 0.4))

# ================= BLOCK 11 =================
def b11a(t):
    fr = base(t); fr = title_layer(fr, 'SO WHY 61?', t)
    T = lambda m: tt(11, 0, m)
    for i, a in enumerate([61, 62, 63, 64, 65]):
        fr = year_medal(fr, t, 400 + i * 280, 470, a, 0.3 + i * 0.2, gold if a != 63 else red)
    b = T('Because the return')
    c = T('the first one Medicare')
    if t > b:
        C = new(); tax_form(C, 1080, 580, 160, 200, 255, 'TAX'); fr = POP(fr, C, (1070, 570, 1250, 790), back((t - b) / 0.45))
    if t > c:
        C = new(); eye(C, 960 + 0, 300, 1.3, 255, t); fr = POP(fr, C, (830, 220, 1090, 380), back((t - c) / 0.45))
        C = new(); medicare_card(C, 1520, 300, 0.5); fr = POP(fr, C, (1440, 250, 1600, 350), back((t - c) / 0.45))
        fr = pill_pop(fr, 'THE FIRST RETURN MEDICARE READS', 810, t, c + 0.3, red, size=40)
    return frame(fr)

def b11b(t):
    fr = base(t); fr = title_layer(fr, 'TWO FREE YEARS', t)
    T = lambda m: tt(11, 1, m)
    a = T('the years you turn'); b = T('the last two years'); c = T("can't touch"); d_ = T('assuming you enroll'); e = T('and then the door closes')
    for i, age in enumerate([61, 62]):
        if t > a + i * 0.4:
            C = new(); card_box(C, 300 + i * 300, 260, 300 + i * 300 + 260, 520, green, card, 255, 6); txt(C, str(age), BOLD(150), 300, green, 255, x=430 + i * 300); padlock(C, 430 + i * 300, 470, 0.38, green, 255, open_=True)
            fr = POP(fr, C, (290 + i * 300, 250, 570 + i * 300, 530), back((t - a - i * 0.4) / 0.45))
    if t > b: fr = pill_pop(fr, '2 FREE YEARS', 580, t, b, green, navy, size=48, cx=560)
    if t > c - 0.2:
        C = new(); medicare_card(C, 1300, 400, 0.9); fr = POP(fr, C, (1130, 290, 1470, 510), back((t - c + 0.2) / 0.45))
        L = new(); s0 = c
        while s0 < e:
            fly(L, t, s0, 1.0, (900, 380), (1180, 400), 30, 'coin', 255, 0, 0.9); s0 += 0.5
        fr = Image.alpha_composite(fr, L)
        C = new(); d = ImageDraw.Draw(C); d.polygon([(1300, 250), (1360, 270), (1350, 340), (1300, 380), (1250, 340), (1240, 270)], outline=green + (255,), width=8); fr = POP(fr, C, (1220, 230, 1380, 400), back((t - c) / 0.45))
    if t > d_: fr = pill_pop(fr, 'ENROLL AT 65', 760, t, d_, blue, size=36, cx=1300)
    if t > e - 0.6:
        C = new(); door(C, 1620, 700, 200, 300, red, 255, open_p=max(0, 0.9 - (t - e + 0.6) * 0.8)); padlock(C, 1620, 700, 0.6, red, 255) if t > e + 0.4 else None
        txt(C, '63', BOLD(60), 880, red, 255, x=1620)
        fr = POP(fr, C, (1450, 520, 1790, 940), back((t - e + 0.6) / 0.45))
    return frame(fr)

# ================= BLOCK 12 =================
def b12a(t):
    fr = base(t); fr = title_layer(fr, 'THE MOST COMMON TOOL', t, size=56)
    T = lambda m: tt(12, 0, m)
    a = T('those two free'); b = T('The most common tool'); c = T('Roth conversion')
    for i, age in enumerate([61, 62]):
        fr = year_medal(fr, t, 380 + i * 220, 400, age, a, green, 80) if t > a - 0.2 else fr
    if t > b:
        C = new(); toolbox(C, 1150, 480, 1.6); fr = POP(fr, C, (900, 300, 1400, 660), back((t - b) / 0.5))
    fr = pill_pop(fr, 'ROTH CONVERSION', 760, t, c, gold, navy, size=56)
    L = new(); rain(L, t, b, 900, 1400, 720, n=6, seed=101, r=22, dur=2.5) if t > b else None; fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b12b(t):
    fr = base(t); fr = title_layer(fr, 'HOW A CONVERSION WORKS', t, size=56)
    T = lambda m: tt(12, 1, m)
    a = T('You move money'); b = T('into a Roth'); c = T('you pay income tax')
    C = new(); vault_box(C, 400, 500, 'TRADITIONAL', 'IRA / 401(k)', gold, t); fr = POP(fr, C, (160, 320, 640, 690), back((t - 0.3) / 0.5))
    if t > b - 0.4:
        C = new(); vault_box(C, 1500, 500, 'ROTH', 'TAX-FREE GROWTH', green, t); fr = POP(fr, C, (1260, 320, 1740, 690), back((t - b + 0.4) / 0.5))
    if t > a:
        L = new(); d = ImageDraw.Draw(L); d.line([660, 500, 1230, 500], fill=goldL + (255,), width=8); d.polygon([(1250, 500), (1215, 478), (1215, 522)], fill=goldL + (255,))
        s0 = a
        while s0 < DUR[12][1] / 30 - 0.3:
            fly(L, t, s0, 1.2, (660, 500), (1230, 500), 70, 'bill', 255, 0, 0.7); s0 += 0.5
        fr = Image.alpha_composite(fr, L)
    if t > c:
        C = new(); tax_form(C, 850, 610, 220, 250, 255, 'TAX'); fr = POP(fr, C, (840, 600, 1080, 870), back((t - c) / 0.45))
        fr = pill_pop(fr, 'INCOME TAX NOW', 200, t, c + 0.2, red, size=40)
    return frame(fr)

def b12c(t):
    fr = base(t); fr = title_layer(fr, 'WHAT YOU GET IN EXCHANGE', t, size=56)
    T = lambda m: tt(12, 2, m)
    a = T('the money grows tax-free'); b = T('qualified withdrawals')
    L = new(); d = ImageDraw.Draw(L); xa, xb, yb, yt = 220, 900, 800, 380
    d.line([xa, yb, xb, yb], fill=gold + (255,), width=3); d.line([xa, yb, xa, yt], fill=gold + (255,), width=3)
    u = ease((t - 0.4) / 2.6); pts = [(xa + (xb - xa) * i / 30, yb - (yb - yt) * (math.exp(2.0 * i / 30) - 1) / (math.exp(2.0) - 1)) for i in range(int(30 * u) + 1)]
    if len(pts) > 1: d.line(pts, fill=green + (255,), width=10, joint='curve')
    fr = Image.alpha_composite(fr, L)
    if t > a: fr = stamp(fr, 'TAX-FREE GROWTH', 560, 300, -6, green, back((t - a) / 0.45), 46)
    if t > b - 0.2:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1240, 330, 1300, 760], radius=30, outline=goldL + (255,), width=6); d.ellipse([1225, 730, 1315, 820], fill=blue + (255,)); d.rounded_rectangle([1250, 640, 1290, 760], radius=10, fill=blue + (255,))
        txt(C, 'YOUR INCOME', BOLD(30), 850, white, 255, x=1270)
        fr = POP(fr, C, (1200, 320, 1340, 900), back((t - b + 0.2) / 0.45))
        C = new(); wallet(C, 1640, 560, 0.8); fr = POP(fr, C, (1520, 480, 1770, 650), back((t - b) / 0.45))
        L = new(); s0 = b
        while s0 < DUR[12][2] / 30 - 0.3:
            fly(L, t, s0, 1.0, (1600, 500), (1400, 420), 50, 'bill', 255, 0, 0.6); s0 += 0.45
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, "WITHDRAWALS DON'T RAISE INCOME", 860, t, b + 0.4, green, navy, size=36, cx=1350)
    return frame(fr)

# ================= BLOCK 13 =================
def b13a(t):
    fr = base(t); fr = title_layer(fr, 'THE CATCH', t, col=red)
    T = lambda m: tt(13, 0, m)
    a = T('A conversion counts')
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([1240, 300, 1330, 800], radius=40, outline=goldL + (255,), width=6); txt(C, 'INCOME THIS YEAR', BOLD(30), 830, white, 255, x=1285)
    fr = POP(fr, C, (1180, 280, 1400, 880), back((t - 0.4) / 0.4))
    L = new(); d = ImageDraw.Draw(L); h = 480 * ease((t - a) / 2.5) if t > a else 0
    d.rounded_rectangle([1250, 790 - h, 1320, 790], radius=30, fill=(red if h > 250 else gold) + (255,))
    fr = Image.alpha_composite(fr, L)
    C = new(); vault(C, 500, 520, 120, t, 0.3); txt(C, 'CONVERSION', BOLD(40), 680, gold, 255, x=500); fr = POP(fr, C, (330, 380, 670, 730), back((t - 0.3) / 0.5))
    if t > a:
        L = new(); s0 = a
        while s0 < DUR[13][0] / 30 - 0.3:
            fly(L, t, s0, 1.2, (640, 520), (1250, 700), 100, 'bill', 255, 0, 0.7); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'CONVERSION = INCOME', 880, t, a + 0.3, red, size=40, cx=760)
    return frame(fr)

def b13b(t):
    fr = base(t); fr = title_layer(fr, 'WHEN YOU CONVERT MATTERS', t, size=56)
    T = lambda m: tt(13, 1, m)
    a = T('Convert at sixty-one'); b = T('Medicare never sees'); c = T('Convert at sixty-three'); d_ = T('two years later')
    if t > a - 0.2:
        for i, age in enumerate([61, 62]): fr = year_medal(fr, t, 300 + i * 200, 380, age, a - 0.2 + i * 0.2, green, 70)
        L = new(); s0 = a
        while s0 < c:
            fly(L, t, s0, 1.0, (720, 380), (1000, 380), 40, 'bill', 255, 0, 0.6); s0 += 0.5
        fr = Image.alpha_composite(fr, L)
    if t > b:
        C = new(); eye(C, 1250, 380, 1.1, 255, t); cross(C, 1370, 340, 32, red); fr = POP(fr, C, (1120, 300, 1420, 460), back((t - b) / 0.45))
        fr = pill_pop(fr, 'NOT SEEN', 470, t, b + 0.2, green, navy, size=34, cx=1250)
    if t > c - 0.2:
        fr = year_medal(fr, t, 300, 700, 63, c - 0.2, red, 70)
        L = new(); s0 = c
        while s0 < DUR[13][1] / 30 - 0.3:
            fly(L, t, s0, 1.0, (400, 700), (1000, 700), 40, 'bill', 255, 0, 0.6); s0 += 0.5
        fr = Image.alpha_composite(fr, L)
    if t > d_:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - d_) / 0.6); d.line([720, 780, 720 + 200 * u, 780], fill=red + (255,), width=8); txt(L, '2 YEARS LATER', BOLD(30), 800, red, 255 * u, x=820); fr = Image.alpha_composite(fr, L)
        C = new(); medicare_card(C, 1250, 700, 0.7); fr = POP(fr, C, (1130, 620, 1370, 780), back((t - d_ - 0.2) / 0.45))
        fr = pill_pop(fr, '+ SURCHARGE', 800, t, d_ + 0.6, red, size=36, cx=1250)
    return frame(fr)

def b13c(t):
    fr = base(t); fr = title_layer(fr, 'SAME CONVERSION', t)
    T = lambda m: tt(13, 2, m)
    C = new(); coin_stack(C, 560, 640, 6, 70); txt(C, 'AGE 62', BOLD(44), 700, green, 255, x=560); fr = POP(fr, C, (450, 430, 680, 760), back((t - 0.3) / 0.5))
    C = new(); coin_stack(C, 1360, 640, 6, 70); txt(C, 'AGE 63', BOLD(44), 700, red, 255, x=1360); fr = POP(fr, C, (1250, 430, 1480, 760), back((t - 0.6) / 0.5))
    C = new(); txt(C, '=', BOLD(150), 420, gold, 255, x=960); fr = POP(fr, C, (880, 400, 1040, 580), back((t - T('same tax bill')) / 0.4)) if t > T('same tax bill') else fr
    if t > T('different Medicare price'):
        u = T('different Medicare price')
        fr = pill_pop(fr, '$202.90', 850, t, u, green, navy, size=48, cx=560)
        fr = pill_pop(fr, '$284.10', 850, t, u + 0.3, red, size=48, cx=1360)
    return frame(fr)

# ================= BLOCK 14 =================
def b14a(t):
    fr = base(t); fr = title_layer(fr, 'PICTURE IT', t)
    T = lambda m: tt(14, 0, m)
    fr = person_box(fr, 'MARY', 330, 520, green, t, T('Mary decides'), 2.8)
    a = T('a piece of her'); b = T('in each of the next')
    if t > a:
        C = new(); vault(C, 760, 470, 90, t, 0.3); txt(C, 'A PIECE', BOLD(30), 590, gold, 255, x=760); fr = POP(fr, C, (650, 350, 870, 630), back((t - a) / 0.45))
    for i, age in enumerate([61, 62]):
        st = b + i * 0.9
        if t > st:
            C = new(); card_box(C, 1000 + i * 380, 300, 1000 + i * 380 + 340, 680, green, card, 255, 5); txt(C, f'AGE {age}', BOLD(60), 340, green, 255, x=1170 + i * 380); vault(C, 1170 + i * 380, 520, 60, t, 0.3); check(C, 1170 + i * 380, 640, 30, green)
            fr = POP(fr, C, (990 + i * 380, 290, 1350 + i * 380, 690), back((t - st) / 0.45))
            L = new(); s0 = st
            while s0 < st + 1.8:
                fly(L, t, s0, 0.8, (860, 470), (1100 + i * 380, 520), 40, 'bill', 255, 0, 0.5); s0 += 0.4
            fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b14b(t):
    fr = base(t); fr = title_layer(fr, 'FRANK', t, col=blue)
    T = lambda m: tt(14, 1, m)
    fr = person_box(fr, 'FRANK', 330, 520, blue, t, 0.2, 2.8)
    C = new(); hourglass(C, 760, 470, 1.2, 255, p=min(1, t / 3.0)); txt(C, 'WAITS', BOLD(44), 640, gold, 255, x=760); fr = POP(fr, C, (650, 330, 870, 700), back((t - T('Frank waits') + 0.2) / 0.45)) if t > T('Frank waits') - 0.2 else fr
    a = T('At sixty-three'); b = T('converts a big amount')
    if t > a:
        C = new(); card_box(C, 1000, 300, 1360, 700, red, card, 255, 6); txt(C, 'AGE 63', BOLD(70), 330, red, 255, x=1180); txt(C, '!!', BOLD(90), 430, red, 255, x=1180)
        fr = POP(fr, C, (990, 290, 1370, 710), back((t - a) / 0.45))
    if t > b:
        L = new(); d = ImageDraw.Draw(L); h = 220 * ease((t - b) / 0.8); d.rounded_rectangle([1590, 700 - h, 1720, 700], radius=14, fill=red + (255,)); txt(L, 'BIG CONVERSION', BOLD(28), 730, red, 255 * ease((t - b) / 0.4), x=1655); fr = Image.alpha_composite(fr, L)
        L = new(); s0 = b
        while s0 < DUR[14][1] / 30 - 0.2:
            fly(L, t, s0, 0.9, (1380, 500), (1590, 600), 40, 'bill', 255, 0, 0.7); s0 += 0.3
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b14c(t):
    fr = base(t); fr = title_layer(fr, 'AT AGE 65', t)
    T = lambda m: tt(14, 2, m)
    a = T('his first Medicare letter'); b = T("that Mary's doesn't")
    C = new(); envelope(C, 560, 520, 400, 260); txt(C, 'FRANK', BOLD(44), 700, blue, 255, x=560); fr = POP(fr, C, (330, 370, 800, 760), back((t - 0.3) / 0.5))
    if t > a:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([420, 520 - 130, 700, 560], radius=10, fill=(250, 250, 250, 255)); txt(C, 'MEDICARE', BOLD(34), 400, blue, 255, x=560); txt(C, '+ SURCHARGE', BOLD(38), 470, red, 255, x=560)
        fr = POP(fr, C, (410, 380, 710, 570), back((t - a) / 0.45))
    if t > b:
        C = new(); envelope(C, 1360, 520, 400, 260); txt(C, 'MARY', BOLD(44), 700, green, 255, x=1360); fr = POP(fr, C, (1130, 370, 1600, 760), back((t - b + 0.3) / 0.5))
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1220, 390, 1500, 560], radius=10, fill=(250, 250, 250, 255)); txt(C, 'MEDICARE', BOLD(34), 400, blue, 255, x=1360); txt(C, 'STANDARD', BOLD(38), 470, green, 255, x=1360); check(C, 1360, 540, 20, green)
        fr = POP(fr, C, (1210, 380, 1510, 580), back((t - b) / 0.45))
    L = new(); rain(L, t, b, 1150, 1600, 340, n=6, seed=111, r=20, dur=2.5) if t > b else None; fr = Image.alpha_composite(fr, L)
    return frame(fr)

# ================= BLOCK 15 =================
def b15a(t):
    fr = base(t); fr = title_layer(fr, 'IS CONVERTING ALWAYS RIGHT?', t, size=56)
    T = lambda m: tt(15, 0, m)
    a = T('not always'); b = T('It costs real tax'); c = T('paying that tax now'); d_ = T('paying it later')
    tilt = 0
    if t > c: tilt = 14 * ease((t - c) / 1.0)
    L = new(); pl, pr = scale_icon(L, 960, 340, tilt) if t > a - 0.3 else ((0, 0), (0, 0))
    fr = Image.alpha_composite(fr, L)
    if t > b:
        C = new(); tax_form(C, pl[0] - 60, pl[1] + 10, 120, 150, 255, 'TAX'); coin_stack(C, pl[0] + 110, pl[1] + 150, 3, 36); txt(C, 'TAX NOW', BOLD(36), pl[1] + 200, red, 255, x=pl[0]); fr = Image.alpha_composite(fr, C)
    if t > d_ - 0.3:
        C = new(); coin_stack(C, pr[0], pr[1] + 150, 2, 36); txt(C, 'TAX LATER', BOLD(36), pr[1] + 200, gold, 255, x=pr[0]); fr = Image.alpha_composite(fr, C)
    if t > a: fr = pill_pop(fr, 'NOT ALWAYS THE RIGHT MOVE', 830, t, a, gold, navy, size=44)
    return frame(fr)

def b15b(t):
    fr = base(t); fr = title_layer(fr, 'KNOW YOUR LINES', t)
    T = lambda m: tt(15, 1, m)
    a = T("It's telling you"); b = T('every line')
    C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([250, 380, 750, 560], radius=30, fill=gold + (255,)); txt(C, 'CONVERT!', BOLD(80), 420, navy, 255, x=500); d.ellipse([230, 330, 770, 610], outline=red + (255,), width=16); d.line([260, 570, 740, 370], fill=red + (255,), width=16)
    fr = POP(fr, C, (220, 320, 780, 620), back((t - 0.3) / 0.5))
    fr = pill_pop(fr, "NOT TELLING YOU TO CONVERT", 700, t, 0.6, red, size=34, cx=500)
    if t > b - 0.3:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - b + 0.3) / 0.6)
        for k, (lab, col) in enumerate([('MEDICARE', red), ('SOCIAL SECURITY', gold), ('HEALTH INSURANCE', purple)]):
            y = 340 + k * 150
            for x in range(900, int(900 + 700 * u), 30): d.line([x, y, x + 16, y], fill=col + (255,), width=6)
            txt(L, lab, BOLD(34), y - 56, col, 255 * u, x=1250)
        h = 450 * ease((t - b) / 3.0); d.rounded_rectangle([1620, 800 - h, 1690, 800], radius=30, fill=green + (255,))
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'EVERY LINE YOUR INCOME MIGHT CROSS', 850, t, b + 0.5, gold, navy, size=36, cx=1250)
    return frame(fr)

# ================= BLOCK 16 =================
def b16a(t):
    fr = base(t); fr = title_layer(fr, 'FIND YOUR ROOM', t)
    T = lambda m: tt(16, 0, m)
    a = T('sixty-three or older'); b = T('Take the Medicare line'); c = T('subtract the income'); d_ = T("what's left")
    if t > a - 0.6: fr = pill_pop(fr, 'AGE 63+', 185, t, a - 0.6, gold, navy, size=36, cx=960)
    if t > b - 0.2:
        C = new(); card_box(C, 240, 330, 700, 680, red, card, 255, 6); txt(C, 'MEDICARE', BOLD(42), 370, red, 255, x=470); txt(C, 'LINE', BOLD(90), 440, white, 255, x=470); fr = POP(fr, C, (230, 320, 710, 690), back((t - b + 0.2) / 0.5))
    if t > c - 0.2:
        C = new(); txt(C, '\u2212', BOLD(160), 400, gold, 255, x=780); fr = POP(fr, C, (720, 380, 840, 580), back((t - c + 0.2) / 0.4))
        C = new(); card_box(C, 860, 330, 1320, 680, gold, card, 255, 6); txt(C, 'INCOME YOU', BOLD(40), 370, gold, 255, x=1090); txt(C, 'EXPECT', BOLD(76), 440, white, 255, x=1090); fr = POP(fr, C, (850, 320, 1330, 690), back((t - c + 0.2) / 0.5))
    if t > d_ - 0.2:
        C = new(); txt(C, '=', BOLD(160), 400, gold, 255, x=1400); fr = POP(fr, C, (1340, 380, 1460, 580), back((t - d_ + 0.2) / 0.4))
        C = new(); card_box(C, 1480, 330, 1760, 680, green, card, 255, 6); txt(C, 'YOUR', BOLD(40), 370, green, 255, x=1620); txt(C, 'ROOM', BOLD(76), 440, white, 255, x=1620); door(C, 1620, 590, 60, 80, green, 255, open_p=0.7)
        fr = POP(fr, C, (1470, 320, 1770, 690), back((t - d_ + 0.2) / 0.5))
    return frame(fr)

def b16b(t):
    fr = base(t); fr = title_layer(fr, 'AN EXAMPLE', t)
    T = lambda m: tt(16, 1, m)
    a = T('If the line is'); b = T('your other income is forty'); c = T('your room is sixty-nine'); d_ = T('Stay inside it')
    x0, x1, y0 = 300, 1620, 470; W_ = x1 - x0
    L = new(); d = ImageDraw.Draw(L)
    if t > a:
        u = ease((t - a) / 0.6); d.rounded_rectangle([x0, y0, x0 + W_ * u, y0 + 120], radius=16, outline=A(red, 255), width=6)
        d.line([x1, y0 - 60, x1, y0 + 180], fill=red + (255,), width=10) if u > 0.95 else None
        txt(L, 'MEDICARE LINE: $109,000', BOLD(36), y0 - 90, red, 255 * u, x=x1 - 230)
    if t > b:
        u = ease((t - b) / 0.8); d.rounded_rectangle([x0 + 4, y0 + 4, x0 + 4 + (W_ * 40 / 109) * u, y0 + 116], radius=12, fill=gold + (255,))
        txt(L, 'OTHER INCOME $40,000', BOLD(34), y0 + 150, gold, 255 * u, x=x0 + (W_ * 40 / 109) / 2)
    if t > c:
        u = ease((t - c) / 0.8); xs = x0 + W_ * 40 / 109; d.rounded_rectangle([xs + 4, y0 + 4, xs + 4 + (W_ * 69 / 109 - 8) * u, y0 + 116], radius=12, fill=green + (255,))
        txt(L, 'ROOM $69,000', BOLD(44), y0 + 150, green, 255 * u, x=xs + (W_ * 69 / 109) / 2)
    fr = Image.alpha_composite(fr, L)
    if t > d_:
        C = new(); medicare_card(C, 960, 800, 0.6); check(C, 1120, 770, 34, green); fr = POP(fr, C, (830, 720, 1180, 860), back((t - d_) / 0.45))
        L = new(); s0 = d_
        while s0 < DUR[16][1] / 30 - 0.4:
            fly(L, t, s0, 1.0, (700, 640), (1000, 590), 60, 'bill', 255, 0, 0.55); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, "INSIDE THE ROOM: NO EXTRA PREMIUM", 210, t, d_ + 0.3, green, navy, size=40)
    return frame(SRC(fr, 'Source: CMS 2026 IRMAA threshold (single filer)'))

# ================= BLOCK 17 =================
def b17a(t):
    fr = base(t); fr = title_layer(fr, 'REASON #3', t, col=red)
    T = lambda m: tt(17, 0, m)
    a = T('the one that surprises'); b = T('a Roth conversion'); c = T('can make your Social Security')
    C = new(); d = ImageDraw.Draw(C); d.ellipse([200, 340, 520, 660], fill=red + (255,)); txt(C, '3', BOLD(260), 360, (255, 255, 255), 255, x=360); fr = POP(fr, C, (190, 330, 530, 670), back((t - 0.3) / 0.5))
    if t > a: fr = pill_pop(fr, 'SURPRISES ALMOST EVERYONE', 730, t, a, red, size=38, cx=360)
    if t > b - 0.2:
        C = new(); vault(C, 780, 500, 90, t, 0.3); txt(C, 'ROTH CONVERSION', BOLD(28), 620, gold, 255, x=780); fr = POP(fr, C, (640, 380, 920, 660), back((t - b + 0.2) / 0.45))
        L = new(); d = ImageDraw.Draw(L); d.line([930, 500, 1160, 500], fill=goldL + (255,), width=8); d.polygon([(1180, 500), (1145, 478), (1145, 522)], fill=goldL + (255,)); fr = Image.alpha_composite(fr, L)
    if t > c - 0.2:
        C = new(); ss_card(C, 1480, 500, 1.1); fr = POP(fr, C, (1290, 370, 1670, 630), back((t - c + 0.2) / 0.45))
        fr = stamp(fr, 'TAXABLE', 1480, 700, -8, red, back((t - c - 0.3) / 0.45), 58)
    return frame(fr)

def b17b(t):
    fr = base(t); fr = title_layer(fr, 'HOW IT HAPPENS', t)
    T = lambda m: tt(17, 1, m)
    a = T('But the government'); b = T('adds half'); c = T('crosses a line'); d_ = T('becomes taxable income')
    C = new(); ss_card(C, 420, 480, 1.1); fr = POP(fr, C, (230, 350, 610, 610), back((t - 0.3) / 0.5))
    fr = pill_pop(fr, 'BENEFIT NOT REDUCED', 700, t, 0.6, green, navy, size=34, cx=420)
    if t > b:
        u = ease((t - b) / 1.0)
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([lerp(330, 900, u), 430, lerp(330, 900, u) + 160, 530], radius=14, fill=gold + (255,)); txt(C, '1/2', BOLD(60), 448, navy, 255, x=lerp(330, 900, u) + 80); fr = Image.alpha_composite(fr, C)
    C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1240, 260, 1330, 800], radius=40, outline=goldL + (255,), width=6); txt(C, 'TOTAL INCOME', BOLD(28), 830, white, 255, x=1285); fr = POP(fr, C, (1180, 240, 1400, 870), back((t - 1.0) / 0.4))
    L = new(); d = ImageDraw.Draw(L)
    h = 300 + 200 * ease((t - b) / 2.0) if t > b else 300 * ease((t - 1.0) / 1.0)
    d.rounded_rectangle([1250, 790 - h, 1320, 790], radius=30, fill=(red if h > 430 else gold) + (255,))
    d.line([1180, 350, 1400, 350], fill=red + (255,), width=6); txt(L, 'THE LINE', BOLD(28), 305, red, 255, x=1290)
    fr = Image.alpha_composite(fr, L)
    if t > c: fr = pill_pop(fr, 'TOTAL CROSSES A LINE', 200, t, c, red, size=40, cx=960)
    if t > d_:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([560, 420, 760, 540], radius=12, fill=red + (255,)); txt(C, 'TAXABLE PART', BOLD(28), 460, (255, 255, 255), 255, x=660); fr = POP(fr, C, (550, 410, 770, 550), back((t - d_) / 0.45))
    return frame(fr)

# ================= BLOCK 18 =================
def gauge(fr, t, cx, label, lines, st, col, zones=None, zt=0):
    if t < st: return fr
    base_y = 820; H_ = 480; top = base_y - H_
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 45, top - 20, cx + 45, base_y + 20], radius=40, outline=goldL + (255,), width=6)
    txt(C, label, BOLD(38), base_y + 40, col, 255, x=cx)
    return POP(fr, C, (cx - 60, top - 40, cx + 60, base_y + 100), back((t - st) / 0.45))

def b18a(t):
    fr = base(t); fr = title_layer(fr, 'THE LINES', t)
    T = lambda m: tt(18, 0, m)
    base_y = 820; H_ = 480; yv = lambda v: base_y - v / 50000 * H_
    fr = gauge(fr, t, 620, 'SINGLE', None, T('For a single filer'), blue)
    fr = gauge(fr, t, 1300, 'MARRIED', None, T('For a married couple'), gold)
    L = new(); d = ImageDraw.Draw(L)
    for cx, lines, st in [(620, [25000, 34000], [T('twenty-five thousand'), T('thirty-four thousand')]), (1300, [32000, 44000], [T('thirty-two thousand'), T('forty-four thousand')])]:
        for v, s0 in zip(lines, st):
            if t > s0:
                u = ease((t - s0) / 0.5); y = yv(v)
                d.line([cx - 90, y, cx + 90 * u + 0, y], fill=red + (255,), width=8)
                txt(L, f'${v:,}', BOLD(40), y - 20, red, 255 * u, x=cx + 210)
    fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: SSA (taxation of Social Security benefits)'))

def b18b(t):
    fr = base(t); fr = title_layer(fr, 'HOW MUCH GETS TAXED', t, size=56)
    T = lambda m: tt(18, 1, m)
    a = T('Between the lines'); b = T('up to fifty percent'); c = T('Above the second line'); d_ = T('up to eighty-five')
    base_y = 820; H_ = 480; yv = lambda v: base_y - v / 50000 * H_
    L = new(); d = ImageDraw.Draw(L)
    d.rounded_rectangle([480, base_y - H_ - 20, 570, base_y + 20], radius=40, outline=goldL + (255,), width=6)
    d.rectangle([497, yv(25000), 553, base_y], fill=green + (200,)); txt(L, 'NOT TAXED', BOLD(26), base_y + 30, green, 255, x=525)
    if t > a: d.rectangle([497, yv(34000), 553, yv(25000)], fill=gold + (255,)); txt(L, 'UP TO 50%', BOLD(28), yv(29500) - 14, gold, 255, x=770)
    if t > c: d.rectangle([497, yv(50000) - 10, 553, yv(34000)], fill=red + (255,)); txt(L, 'UP TO 85%', BOLD(28), yv(42000) - 14, red, 255, x=770)
    fr = Image.alpha_composite(fr, L)
    # donut
    cx, cy, R = 1330, 520, 210
    L = new(); d = ImageDraw.Draw(L)
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=(40, 62, 92, 255), width=50)
    pct = 0
    if t > b: pct = 50 * ease((t - b) / 0.7)
    if t > d_: pct = 50 + 35 * ease((t - d_) / 0.9)
    if pct > 0: d.arc([cx - R, cy - R, cx + R, cy + R], start=-90, end=-90 + 3.6 * pct, fill=(red if pct > 55 else gold) + (255,), width=50)
    txt(L, f'{int(pct)}%', BOLD(120), cy - 80, red if pct > 55 else gold, 255, x=cx); txt(L, 'OF THE BENEFIT', BOLD(30), cy + 50, white, 255, x=cx); txt(L, 'CAN BE TAXABLE', BOLD(30), cy + 90, white, 255, x=cx)
    fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: SSA (single filer example)'))

# ================= BLOCK 19 =================
def b19a(t):
    fr = base(t); fr = title_layer(fr, 'NOT AN 85% TAX RATE', t, size=56)
    T = lambda m: tt(19, 0, m)
    a = T('It means'); b = T('is added to your taxable'); c = T('taxed at your normal')
    C = new(); d = ImageDraw.Draw(C); txt(C, '85% TAX RATE', BOLD(110), 330, white, 255, x=960); d.line([420, 430, 1500, 300], fill=red + (255,), width=18); d.ellipse([360, 240, 1560, 500], outline=red + (255,), width=12)
    fr = POP(fr, C, (330, 220, 1590, 520), back((t - 0.3) / 0.5))
    if t > a:
        C = new(); ss_card(C, 420, 700, 0.9); fr = POP(fr, C, (270, 590, 570, 800), back((t - a) / 0.45))
    if t > b - 0.3:
        u = ease((t - b + 0.3) / 1.0)
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([lerp(560, 900, u), 660, lerp(560, 900, u) + 180, 740], radius=12, fill=red + (255,)); txt(C, '85%', BOLD(50), 672, (255, 255, 255), 255, x=lerp(560, 900, u) + 90); fr = Image.alpha_composite(fr, C)
        C = new(); tax_form(C, 1120, 600, 170, 210, 255, 'TAXABLE'); fr = POP(fr, C, (1110, 590, 1300, 820), back((t - b + 0.3) / 0.45))
    if t > c: fr = pill_pop(fr, 'THEN TAXED AT YOUR NORMAL RATE', 850, t, c, gold, navy, size=40, cx=1200) if False else pill_pop(fr, 'THEN TAXED AT YOUR NORMAL RATE', 860, t, c, gold, navy, size=40)
    return frame(fr)

def b19b(t):
    fr = base(t); fr = title_layer(fr, 'NEVER ADJUSTED', t)
    T = lambda m: tt(19, 1, m)
    a = T('never been adjusted'); b = T('nineteen eighties')
    x0, x1, yb, yt = 300, 1620, 800, 340
    L = new(); d = ImageDraw.Draw(L)
    d.line([x0, yb, x1, yb], fill=gold + (255,), width=3); d.line([x0, yb, x0, yt - 20], fill=gold + (255,), width=3)
    for lab, x in [('1984', 360), ('1993', 620), ('TODAY', 1560)]: txt(L, lab, BOLD(30), yb + 16, grey, 255, x=x)
    u = ease((t - 0.4) / 2.6)
    ye = 620
    d.line([x0, ye, x0 + (x1 - x0) * u, ye], fill=gold + (255,), width=12)
    pts = [(x0 + (x1 - x0) * i / 40, ye - 20 - (ye - yt) * (i / 40) ** 1.6) for i in range(int(40 * u) + 1)]
    if len(pts) > 1: d.line(pts, fill=red + (255,), width=10, joint='curve')
    txt(L, 'THE LINES: $25,000 / $34,000', BOLD(34), ye + 24, gold, 255 * ease((t - 0.8) / 0.4), x=900)
    txt(L, 'PRICES', BOLD(34), yt + 40, red, 255 * u, x=1450)
    fr = Image.alpha_composite(fr, L)
    if t > a: fr = pill_pop(fr, 'NEVER ADJUSTED FOR INFLATION', 190, t, a, red, size=40)
    return frame(fr)

# ================= BLOCK 20 =================
def b20a(t):
    fr = base(t); fr = title_layer(fr, 'TIMING MATTERS AT 61', t, size=56)
    T = lambda m: tt(20, 0, m)
    a = T('claim Social Security'); b = T('and convert in the same'); c = T('both land on the same')
    if t > a - 0.3:
        C = new(); ss_card(C, 460, 400, 1.0); txt(C, 'CLAIM AT 62', BOLD(38), 520, blue, 255, x=460); fr = POP(fr, C, (290, 280, 640, 560), back((t - a + 0.3) / 0.5))
    if t > b - 0.3:
        C = new(); vault(C, 1460, 400, 90, t, 0.3); txt(C, 'CONVERT', BOLD(38), 520, gold, 255, x=1460); fr = POP(fr, C, (1300, 280, 1620, 560), back((t - b + 0.3) / 0.5))
    if t > c - 0.4:
        C = new(); tax_form(C, 850, 620, 220, 260, 255, 'ONE RETURN'); fr = POP(fr, C, (840, 610, 1080, 890), back((t - c + 0.4) / 0.45))
        L = new(); s0 = c - 0.2
        while s0 < DUR[20][0] / 30 - 0.2:
            fly(L, t, s0, 1.2, (560, 420), (930, 640), 80, 'bill', 255, 0, 0.6); fly(L, t, s0 + 0.2, 1.2, (1360, 420), (1010, 640), 80, 'bill', 255, 0, 0.6); s0 += 0.5
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'BOTH ON THE SAME TAX RETURN', 200, t, c + 0.2, red, size=38)
    return frame(fr)

def b20b(t):
    fr = base(t); fr = title_layer(fr, 'THE SMARTER ORDER', t)
    T = lambda m: tt(20, 1, m)
    a = T('If you convert first'); b = T('before your benefits start'); c = T('cleaner'); d_ = T('It isn'); e = T('run the numbers')
    x0 = 300
    if t > a - 0.2:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - a + 0.2) / 0.8)
        d.rounded_rectangle([x0, 330, x0 + 640 * u, 450], radius=24, fill=green + (255,)); txt(L, 'CONVERT FIRST', BOLD(44), 360, navy, 255 * u, x=x0 + 320)
        fr = Image.alpha_composite(fr, L)
    if t > b:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - b) / 0.8)
        d.rounded_rectangle([x0 + 660, 330, x0 + 660 + 640 * u, 450], radius=24, fill=gold + (255,)); txt(L, 'BENEFITS START', BOLD(44), 360, navy, 255 * u, x=x0 + 980)
        fr = Image.alpha_composite(fr, L)
    if t > c: fr = pill_pop(fr, 'CLEANER CONVERSION YEARS', 490, t, c, green, navy, size=40, cx=620)
    if t > d_:
        C = new(); hourglass(C, 500, 730, 0.9, 255, p=0.5); d = ImageDraw.Draw(C); d.ellipse([400, 630, 600, 830], outline=grey + (255,), width=12); d.line([420, 810, 580, 650], fill=grey + (255,), width=12)
        fr = POP(fr, C, (380, 610, 620, 850), back((t - d_) / 0.45))
        fr = pill_pop(fr, 'NOT A REASON TO DELAY FOR EVERYONE', 860, t, d_ + 0.2, (110, 125, 150), size=32, cx=520)
    if t > e - 0.2:
        C = new(); calculator(C, 1400, 720, 1.2); fr = POP(fr, C, (1250, 560, 1550, 890), back((t - e + 0.2) / 0.5))
        fr = pill_pop(fr, 'RUN THE NUMBERS FIRST', 570, t, e, gold, navy, size=40, cx=1400)
    return frame(fr)

SLIDES = {11: [b11a, b11b], 12: [b12a, b12b, b12c], 13: [b13a, b13b, b13c], 14: [b14a, b14b, b14c], 15: [b15a, b15b], 16: [b16a, b16b], 17: [b17a, b17b], 18: [b18a, b18b], 19: [b19a, b19b], 20: [b20a, b20b]}

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'preview':
        sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(SLIDES)
        fq = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                fn(DUR[b][i] / 30 * fq).convert('RGB').save(f'/home/claude/py_{b}_{i}.png')
        print({b: DUR[b] for b in sel}, 'ok')
    else:
        sel = [int(x) for x in sys.argv[2].split(',')]
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                render_fast(fn, DUR[b][i], f'/mnt/user-data/outputs/v4-b{b}-0{i + 1}.mp4')
                print('done', b, i + 1, DUR[b][i], flush=True)
