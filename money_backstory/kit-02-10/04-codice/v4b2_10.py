from v3lib import *
from v3b3_10 import POP, new, lerp, fly, person_box
from v3b11_21 import crown, rot_arrow_ccw
import sys, math

SENT = {
 2: ["Here's what's coming: a two-year rule that lets Medicare read your tax return before you even enroll, income cliffs where one dollar changes your premium, a hidden tax on your Social Security, a health insurance cliff that hits before sixty-five, and a savings window that closes at sixty-three.", "By the end, you'll know exactly what to do this year and next year."],
 3: ["Meet Frank.", "He is sixty-one, single, and he plans to think about Medicare when he turns sixty-five.", "Meet Mary.", "She is also sixty-one and single, but she has just learned that Medicare will soon start reading her tax returns.", "Same age, similar savings — and two very different next years."],
 4: ["The first reason: Medicare doesn't look at your income today.", "When it sets your premium, it reads your tax return from two years earlier.", "So when you turn sixty-five and enroll, the return it checks is the one you file for the year you turned sixty-three."],
 5: ["This extra charge has a name: the Income-Related Monthly Adjustment Amount, or IRMAA.", "It is added to your Part B premium, which pays for doctor visits and outpatient care, and to your Part D prescription drug coverage.", "Many people first hear about it when the letter arrives in the mail."],
 6: ["And the income that counts is broader than your paycheck.", "Medicare uses your modified adjusted gross income, which includes your wages, pension, taxable withdrawals from retirement accounts, capital gains, and even the tax-exempt interest you earn.", "Anything that lands on that tax return can count."],
 7: ["In twenty twenty-six, the standard Part B premium is two hundred two dollars and ninety cents a month.", "But if your income on that older tax return is above one hundred nine thousand dollars for a single filer, or two hundred eighteen thousand for a married couple, the premium jumps to two hundred eighty-four dollars and ten cents."],
 8: ["The second reason is that these lines are cliffs, not slopes.", "Imagine two neighbors.", "One reports exactly one hundred nine thousand dollars and pays the standard premium.", "The other reports just one dollar more.", "Her premium is eighty-one dollars and twenty cents higher, every single month."],
 9: ["Multiply eighty-one dollars and twenty cents by twelve and you get nine hundred seventy-four dollars and forty cents a year, for one dollar.", "A married couple that crosses their first line pays almost twenty-three hundred dollars extra a year, once drug coverage is included."],
 10: ["And it doesn't stop there.", "There are five tiers, and at the top the Part B premium reaches six hundred eighty-nine dollars and ninety cents a month, more than three times the standard amount.", "Part D can add up to ninety-one dollars a month on top of that."],
}
FRAMES = {2: 787, 3: 683, 4: 490, 5: 648, 6: 591, 7: 646, 8: 658, 9: 540, 10: 538}
GROUPS = {2: [[0], [1]], 3: [[0, 1], [2, 3], [4]], 4: [[0, 1], [2]], 5: [[0], [1], [2]], 6: [[0, 1, 2]], 7: [[0], [1]], 8: [[0, 1], [2, 3], [4]], 9: [[0], [1]], 10: [[0, 1], [2]]}

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
def SRC(fr, text):
    L = new(); txt(L, text, REG(26), 985, grey, 200); return Image.alpha_composite(fr, L)

# ---------- extra icons ----------
def eye(C, cx, cy, s=1.0, alpha=255, t=0.0):
    d = ImageDraw.Draw(C)
    d.ellipse([cx - 90 * s, cy - 50 * s, cx + 90 * s, cy + 50 * s], fill=A((236, 240, 245), alpha), outline=A(goldL, alpha), width=5)
    ox = math.sin(t * 2.2) * 26 * s
    d.ellipse([cx - 34 * s + ox, cy - 34 * s, cx + 34 * s + ox, cy + 34 * s], fill=A(blue, alpha))
    d.ellipse([cx - 14 * s + ox, cy - 14 * s, cx + 14 * s + ox, cy + 14 * s], fill=A(navy, alpha))

def envelope(C, cx, cy, w=260, h=170, alpha=255):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=14, fill=A((236, 240, 245), alpha), outline=A(goldL, alpha), width=4)
    d.line([cx - w / 2 + 6, cy - h / 2 + 6, cx, cy + 10, cx + w / 2 - 6, cy - h / 2 + 6], fill=A((150, 165, 190), alpha), width=5)

def pillbottle(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 44 * s, cy - 50 * s, cx + 44 * s, cy + 70 * s], radius=int(14 * s), fill=A(gold, alpha), outline=A(goldL, alpha), width=3)
    d.rounded_rectangle([cx - 52 * s, cy - 82 * s, cx + 52 * s, cy - 48 * s], radius=int(10 * s), fill=A(blue, alpha))
    d.rectangle([cx - 30 * s, cy - 10 * s, cx + 30 * s, cy + 30 * s], fill=A((236, 240, 245), alpha))
    d.rectangle([cx - 6 * s, cy - 2 * s, cx + 6 * s, cy + 22 * s], fill=A(red, alpha)); d.rectangle([cx - 16 * s, cy + 6 * s, cx + 16 * s, cy + 14 * s], fill=A(red, alpha))

def medicare_card(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C); w = 320 * s; h = 200 * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(18 * s), fill=A((236, 240, 245), alpha), outline=A(blue, alpha), width=5)
    d.rectangle([cx - w / 2 + 16 * s, cy - h / 2 + 16 * s, cx + w / 2 - 16 * s, cy - h / 2 + 64 * s], fill=A(blue, alpha))
    txt(C, 'MEDICARE', BOLD(int(36 * s)), cy - h / 2 + 24 * s, (255, 255, 255), alpha, x=cx)
    d.rectangle([cx - w / 2 + 28 * s, cy + 16 * s, cx - w / 2 + 84 * s, cy + 30 * s], fill=A(red, alpha)); d.rectangle([cx - w / 2 + 49 * s, cy - 4 * s, cx - w / 2 + 63 * s, cy + 50 * s], fill=A(red, alpha))
    for k in range(3): d.rectangle([cx - w / 2 + 108 * s, cy + 10 * s + k * 24 * s, cx + w / 2 - 28 * s, cy + 20 * s + k * 24 * s], fill=A((150, 165, 190), alpha))

def cal_card(C, x0, y0, x1, y1, head, big, bigsize=110, headcol=red, bigcol=navy):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([x0, y0, x1, y1], radius=28, fill=(236, 240, 245, 255)); d.rounded_rectangle([x0, y0, x1, y0 + 80], radius=28, fill=headcol + (255,)); d.rectangle([x0, y0 + 50, x1, y0 + 80], fill=headcol + (255,))
    txt(C, head, BOLD(34), y0 + 20, (255, 255, 255), 255, x=(x0 + x1) / 2)
    txt(C, big, BOLD(bigsize), y0 + 100, bigcol, 255, x=(x0 + x1) / 2)

def cliff_icon(C, cx, cy, s=1.0, alpha=255, col=red):
    d = ImageDraw.Draw(C)
    d.polygon([(cx - 60 * s, cy - 30 * s), (cx + 10 * s, cy - 30 * s), (cx + 10 * s, cy + 30 * s), (cx + 60 * s, cy + 30 * s), (cx + 60 * s, cy + 60 * s), (cx - 60 * s, cy + 60 * s)], fill=A(col, alpha))

# ================= BLOCK 2 =================
def pin_icon(C, k, cx, cy, alpha=255):
    if k == 0:
        d = ImageDraw.Draw(C); d.rounded_rectangle([cx - 46, cy - 46, cx + 46, cy + 46], radius=12, fill=A((236, 240, 245), alpha)); d.rectangle([cx - 46, cy - 46, cx + 46, cy - 20], fill=A(red, alpha)); txt(C, '2Y', BOLD(40), cy - 12, navy, alpha, x=cx)
    elif k == 1: cliff_icon(C, cx, cy, 0.8, alpha)
    elif k == 2: tax_form(C, cx - 34, cy - 46, 68, 92, alpha, 'TAX')
    elif k == 3:
        d = ImageDraw.Draw(C); d.rectangle([cx - 44, cy - 14, cx + 44, cy + 14], fill=A(red, alpha)); d.rectangle([cx - 14, cy - 44, cx + 14, cy + 44], fill=A(red, alpha))
    else: coin_stack(C, cx, cy + 20, 4, 40, alpha)

PINS = [('TWO-YEAR', 'RULE'), ('INCOME', 'CLIFFS'), ('SOCIAL SECURITY', 'TAX'), ('HEALTH INSURANCE', 'CLIFF'), ('SAVINGS', 'WINDOW')]
def b2a(t):
    fr = base(t); fr = title_layer(fr, "HERE'S WHAT'S COMING", t)
    T = lambda m: tt(2, 0, m)
    st = [T('a two-year rule'), T('income cliffs'), T('a hidden tax'), T('a health insurance cliff'), T('a savings window')]
    px = [300, 630, 960, 1290, 1620]; py = lambda x: 600 + 100 * math.sin((x - 200) / 230)
    L = new(); d = ImageDraw.Draw(L)
    xs = [200 + i * 8 for i in range(int(1600 / 8) + 1)]
    lead = 200
    for k in range(5):
        if t > st[k] - 0.4: lead = max(lead, lerp(px[k - 1] if k else 200, px[k], ease((t - st[k] + 0.4) / 0.9)))
    pts = [(x, py(x)) for x in xs if x <= lead]
    if len(pts) > 1: d.line(pts, fill=A(gold, 255), width=10, joint='curve')
    coin(L, lead, py(lead), 26, 255, squash=abs(math.cos(t * 5)) * 0.6 + 0.4)
    fr = Image.alpha_composite(fr, L)
    for k in range(5):
        if t < st[k]: continue
        x = px[k]; y = py(x); above = (k % 2 == 0)
        C = new(); d = ImageDraw.Draw(C)
        cy = y - 190 if above else y + 190
        col = red if k in (1, 3) else gold
        d.rounded_rectangle([x - 165, cy - 80, x + 165, cy + 80], radius=22, fill=A(card, 255), outline=A(col, 255), width=4)
        pin_icon(C, k, x - 100, cy)
        txt(C, PINS[k][0], BOLD(26), cy - 40, white, 255, x=x + 50)
        txt(C, PINS[k][1], BOLD(38), cy + 4, col, 255, x=x + 50)
        d.ellipse([x - 28, y - 28, x + 28, y + 28], fill=A(col, 255)); txt(C, str(k + 1), BOLD(34), y - 24, navy, 255, x=x)
        d.line([x, y - (28 if above else -28), x, cy + (80 if above else -80)], fill=A(col, 255), width=4)
        fr = POP(fr, C, (x - 175, min(y, cy) - 100, x + 175, max(y, cy) + 100), back((t - st[k]) / 0.4))
    return frame(fr)

def b2b(t):
    fr = base(t); fr = title_layer(fr, 'YOUR PLAN', t)
    T = lambda m: tt(2, 1, m)
    a = T('this year'); b = T('next year')
    if t > 0.4:
        C = new(); cal_card(C, 400, 300, 860, 700, 'PLAN', 'THIS YEAR', 60, gold); check(C, 630, 620, 40, green)
        fr = POP(fr, C, (390, 290, 870, 710), back((t - a + 0.6) / 0.5))
    if t > b - 0.6:
        C = new(); cal_card(C, 1060, 300, 1520, 700, 'PLAN', 'NEXT YEAR', 60, blue); check(C, 1290, 620, 40, green)
        fr = POP(fr, C, (1050, 290, 1530, 710), back((t - b + 0.6) / 0.5))
    L = new(); rain(L, t, 1.5, 300, 1600, 800, n=8, seed=51, r=22, dur=3.0)
    fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'EXACTLY WHAT TO DO', 780, t, T('know exactly'), gold, navy, size=44)
    return frame(fr)

# ================= BLOCK 3 =================
def badge61(C, cx, cy, r=80):
    d = ImageDraw.Draw(C); d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=gold + (255,)); txt(C, '61', BOLD(int(r * 1.0)), cy - r * 0.55, navy, 255, x=cx)

def b3a(t):
    fr = base(t); fr = title_layer(fr, 'MEET FRANK', t)
    T = lambda m: tt(3, 0, m)
    fr = person_box(fr, 'FRANK', 470, 520, blue, t, 0.2)
    a = T('He is sixty-one')
    if t > a:
        C = new(); badge61(C, 700, 330); fr = POP(fr, C, (600, 230, 800, 430), back((t - a) / 0.5))
    s = T('single')
    fr = pill_pop(fr, 'SINGLE', 800, t, s, purple, size=40, cx=470)
    m = T('think about Medicare')
    if t > m:
        C = new(); d = ImageDraw.Draw(C)
        for (x, y, r) in [(1080, 380, 60), (1170, 350, 74), (1270, 384, 60)]: d.ellipse([x - r, y - r, x + r, y + r], fill=(236, 240, 245, 255))
        medicare_card(C, 1170, 355, 0.32)
        d.ellipse([1000, 500, 1030, 530], fill=(236, 240, 245, 255)); d.ellipse([960, 560, 980, 580], fill=(236, 240, 245, 255))
        fr = POP(fr, C, (980, 270, 1360, 600), back((t - m) / 0.5))
    u = T('turns sixty-five')
    if t > u:
        C = new(); cal_card(C, 1300, 500, 1660, 800, 'HE TURNS', '65', 150, red); fr = POP(fr, C, (1290, 490, 1670, 810), back((t - u) / 0.5))
    return frame(fr)

def b3b(t):
    fr = base(t); fr = title_layer(fr, 'MEET MARY', t)
    T = lambda m: tt(3, 1, m)
    fr = person_box(fr, 'MARY', 470, 520, green, t, 0.2)
    a = T('She is also sixty-one')
    if t > a:
        C = new(); badge61(C, 700, 330); fr = POP(fr, C, (600, 230, 800, 430), back((t - a) / 0.5))
        fr = pill_pop(fr, 'SINGLE', 800, t, a + 0.5, purple, size=40, cx=470)
    b = T('has just learned')
    if t > b:
        C = new(); bulb(C, 470, 200, 1.0); fr = POP(fr, C, (380, 100, 560, 290), back((t - b) / 0.45))
    c = T('Medicare will soon')
    if t > c:
        C = new(); tax_form(C, 1050, 470, 300, 380, 255, 'TAX'); fr = POP(fr, C, (1040, 460, 1360, 860), back((t - c) / 0.5))
        C = new(); eye(C, 1200, 340, 1.4, 255, t); fr = POP(fr, C, (1060, 260, 1340, 420), back((t - c - 0.3) / 0.5))
        C = new(); medicare_card(C, 1600, 400, 0.6); fr = POP(fr, C, (1490, 330, 1710, 470), back((t - c - 0.15) / 0.5))
    return frame(fr)

def b3c(t):
    fr = base(t); fr = title_layer(fr, 'THE NEXT TWO YEARS', t)
    T = lambda m: tt(3, 2, m)
    fr = pill_pop(fr, 'SAME AGE', 190, t, 0.3, gold, navy, size=36, cx=700)
    fr = pill_pop(fr, 'SIMILAR SAVINGS', 190, t, T('similar savings') - 0.3, gold, navy, size=36, cx=1220)
    C = new(); avatar(C, 380, 560, blue, 1.4); avatar(C, 380, 660, green, 1.4)
    fr = POP(fr, C, (300, 460, 460, 760), back((t - 0.4) / 0.5))
    a = T('two very different')
    if t > a - 0.6:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - a + 0.6) / 1.4)
        d.line([460, 610, 460 + 500 * u, 610], fill=grey + (255,), width=10)
        d.line([460, 610, 460 + 500 * u, 610 - 170 * u], fill=red + (255,), width=10)
        d.line([460, 610, 460 + 500 * u, 610 + 170 * u], fill=green + (255,), width=10)
        if u > 0.95:
            txt(L, 'FRANK', BOLD(36), 400, red, 255, x=1100); txt(L, 'MARY', BOLD(36), 815, green, 255, x=1100)
        fr = Image.alpha_composite(fr, L)
    if t > a + 0.8:
        C = new(); avatar(C, 1100, 470, blue, 1.3); avatar(C, 1100, 700, green, 1.3); coin_stack(C, 1300, 780, 5, 50); fr = POP(fr, C, (1000, 380, 1420, 830), back((t - a - 0.8) / 0.5))
    return frame(fr)

# ================= BLOCK 4 =================
def b4a(t):
    fr = base(t); fr = title_layer(fr, 'REASON #1: THE LOOKBACK', t, size=56)
    T = lambda m: tt(4, 0, m)
    C = new(); cal_card(C, 220, 300, 600, 640, 'TODAY', 'NOW', 120, blue); fr = POP(fr, C, (210, 290, 610, 650), back((t - 0.3) / 0.5))
    a = T("doesn't look at")
    if t > a:
        C = new(); eye(C, 410, 720, 1.0, 255, t); cross(C, 520, 690, 34, red); fr = POP(fr, C, (300, 640, 560, 780), back((t - a) / 0.45))
    b = T('it reads your tax return')
    if t > b - 0.3:
        C = new(); medicare_card(C, 960, 470, 0.9); fr = POP(fr, C, (790, 360, 1130, 590), back((t - b + 0.3) / 0.5))
    c = T('from two years earlier')
    if t > c:
        C = new(); tax_form(C, 1420, 300, 260, 340, 255, 'TAX'); fr = POP(fr, C, (1410, 290, 1690, 650), back((t - c) / 0.5))
        L = new(); d = ImageDraw.Draw(L); u = ease((t - c - 0.4) / 0.9)
        d.arc([980, 250, 1500, 560], start=200, end=200 + 140 * u, fill=goldL + (255,), width=10)
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, '2 YEARS EARLIER', 720, t, c + 0.5, gold, navy, size=42, cx=1200)
    return frame(fr)

def b4b(t):
    fr = base(t); fr = title_layer(fr, 'THE YEAR THAT COUNTS', t, size=56)
    T = lambda m: tt(4, 1, m)
    a = T('turn sixty-five'); b = T('the return it checks'); c = T('the year you turned sixty-three')
    C = new(); cal_card(C, 1140, 300, 1600, 700, 'ENROLL AT', '65', 180, blue); fr = POP(fr, C, (1130, 290, 1610, 710), back((t - a + 0.3) / 0.5)) if t > a - 0.3 else fr
    if t > b:
        C = new(); tax_form(C, 810, 400, 200, 260, 255, 'TAX'); fr = POP(fr, C, (800, 390, 1020, 670), back((t - b) / 0.45))
    if t > c - 0.3:
        C = new(); cal_card(C, 300, 300, 700, 700, 'YEAR YOU TURN', '63', 180, gold); fr = POP(fr, C, (290, 290, 710, 710), back((t - c + 0.3) / 0.5))
        L = new(); d = ImageDraw.Draw(L); u = ease((t - c) / 0.8)
        d.line([720, 500, 720 + 80 * u, 500], fill=goldL + (255,), width=8) if u > 0 else None
        fr = Image.alpha_composite(fr, L)
        L = new(); s0 = c
        while s0 < DUR[4][1] / 30 - 0.5:
            fly(L, t, s0, 1.4, (700, 480), (1150, 480), 100, 'bill', 255, 0, 0.6); s0 += 0.5
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'THE RETURN FROM AGE 63 SETS THE PREMIUM AT 65', 800, t, c + 0.6, gold, navy, size=34)
    return frame(fr)

# ================= BLOCK 5 =================
def b5a(t):
    fr = base(t); fr = title_layer(fr, 'THE EXTRA CHARGE', t)
    T = lambda m: tt(5, 0, m)
    tiles = [('I', 'INCOME-', 'Income-Related'), ('R', 'RELATED', 'Income-Related'), ('M', 'MONTHLY', 'Monthly'), ('A', 'ADJUSTMENT', 'Adjustment'), ('A', 'AMOUNT', 'Amount')]
    xs = [420, 690, 960, 1230, 1500]
    for k, (ch, word, mk) in enumerate(tiles):
        st = T(mk) + (0.35 if k == 1 else 0)
        if t < st: continue
        C = new(); d = ImageDraw.Draw(C); x = xs[k]
        d.rounded_rectangle([x - 100, 340, x + 100, 560], radius=24, fill=gold + (255,)); txt(C, ch, BOLD(170), 360, navy, 255, x=x)
        txt(C, word, BOLD(30), 600, white, 255, x=x)
        fr = POP(fr, C, (x - 110, 330, x + 110, 650), back((t - st) / 0.4))
    if t > T('or IRMAA') - 0.3: fr = pill_pop(fr, 'IRMAA', 760, t, T('or IRMAA') - 0.3, red, size=70)
    L = new(); rain(L, t, 1.0, 300, 1620, 700, n=8, seed=61, r=22, dur=4.0); fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b5b(t):
    fr = base(t); fr = title_layer(fr, 'WHERE IT IS ADDED', t)
    T = lambda m: tt(5, 1, m)
    a = T('Part B premium'); b = T('doctor visits'); c = T('Part D prescription')
    if t > a - 0.4:
        C = new(); card_box(C, 240, 260, 900, 760, blue, card, 255, 6); txt(C, 'PART B', BOLD(80), 290, blue, 255, x=570)
        d = ImageDraw.Draw(C); d.rectangle([520, 440, 620, 470], fill=A(red, 255)); d.rectangle([555, 405, 585, 505], fill=A(red, 255))
        fr = POP(fr, C, (230, 250, 910, 770), back((t - a + 0.4) / 0.5))
    if t > b:
        L = new(); txt(L, 'DOCTOR VISITS', BOLD(38), 570, white, 255 * ease((t - b) / 0.4), x=570); txt(L, 'OUTPATIENT CARE', BOLD(38), 620, white, 255 * ease((t - b - 0.3) / 0.4), x=570); fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, '+ IRMAA', 690, t, b + 0.6, red, size=40, cx=570)
    if t > c - 0.3:
        C = new(); card_box(C, 1020, 260, 1680, 760, gold, card, 255, 6); txt(C, 'PART D', BOLD(80), 290, gold, 255, x=1350); pillbottle(C, 1350, 480, 1.2)
        fr = POP(fr, C, (1010, 250, 1690, 770), back((t - c + 0.3) / 0.5))
        L = new(); txt(L, 'PRESCRIPTION DRUGS', BOLD(38), 600, white, 255 * ease((t - c) / 0.4), x=1350); fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, '+ IRMAA', 690, t, c + 0.8, red, size=40, cx=1350)
    L = new(); rain(L, t, a, 250, 890, 780, n=6, seed=62, r=20, dur=5.0); rain(L, t, c, 1030, 1670, 780, n=6, seed=63, r=20, dur=3.0); fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b5c(t):
    fr = base(t); fr = title_layer(fr, 'THE LETTER', t)
    T = lambda m: tt(5, 2, m)
    a = T('the letter arrives')
    u = ease((t - 0.3) / 1.2)
    C = new(); envelope(C, lerp(1700, 960, u), 540, 420, 270); fr = Image.alpha_composite(fr, C)
    if t > a:
        C = new(); d = ImageDraw.Draw(C); v = ease((t - a) / 0.6)
        d.rounded_rectangle([780, 540 - 200 * v, 1140, 640], radius=12, fill=(250, 250, 250, 255)) if v > 0.05 else None
        txt(C, 'IRMAA', BOLD(70), 540 - 200 * v + 30, red, 255 * v, x=960); txt(C, '$$$', BOLD(60), 540 - 200 * v + 120, red, 255 * v, x=960)
        fr = Image.alpha_composite(fr, C)
    fr = pill_pop(fr, 'MANY HEAR ABOUT IT ONLY NOW', 770, t, T('Many people first') + 0.3, red, size=42)
    C = new(); txt(C, '!', BOLD(140), 250, red, 255, x=1300); fr = POP(fr, C, (1240, 240, 1360, 420), back((t - 1.5) / 0.4)) if t > 1.5 else fr
    return frame(fr)

# ================= BLOCK 6 =================
def b6(t):
    fr = base(t); fr = title_layer(fr, 'WHAT COUNTS AS INCOME', t)
    T = lambda m: tt(6, 0, m)
    srcs = [('WAGES', 'your wages', 'brief'), ('PENSION', 'pension', 'bag'), ('IRA / 401(k)', 'taxable withdrawals', 'vault'), ('CAPITAL GAINS', 'capital gains', 'up'), ('TAX-EXEMPT INTEREST', 'tax-exempt interest', 'coin')]
    xs = [360, 660, 960, 1260, 1560]
    C = new(); card_box(C, 620, 600, 1300, 900, gold, card, 255, 6); txt(C, 'YOUR TAX RETURN', BOLD(38), 620, gold, 255, x=960); txt(C, 'MODIFIED ADJUSTED', BOLD(28), 690, white, 255, x=960); txt(C, 'GROSS INCOME', BOLD(28), 726, white, 255, x=960)
    fr = POP(fr, C, (610, 590, 1310, 910), back((t - 0.5) / 0.5)) if t > 0.5 else fr
    for k, (lab, mk, ic) in enumerate(srcs):
        st = T(mk)
        if t < st - 0.2: continue
        x = xs[k]; C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([x - 130, 220, x + 130, 440], radius=20, fill=card + (255,), outline=green + (255,), width=4)
        if ic == 'brief': briefcase(C, x, 300, 0.8)
        elif ic == 'bag': money_bag(C, x, 310, 0.6)
        elif ic == 'vault': vault(C, x, 310, 50, t, 0.4)
        elif ic == 'up': up_arrow(C, x, 315, 0.6, green, 255)
        else: coin(C, x, 315, 42, 255)
        txt(C, lab, BOLD(24), 380, white, 255, x=x)
        fr = POP(fr, C, (x - 140, 210, x + 140, 450), back((t - st + 0.2) / 0.4))
        L = new(); s0 = st
        while s0 < st + 2.2:
            fly(L, t, s0, 1.0, (x, 450), (960, 620), 20, 'bill' if ic != 'coin' else 'coin', 255, 0, 0.6); s0 += 0.55
        fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'ANYTHING ON THE RETURN CAN COUNT', 815, t, T('Anything that lands'), red, size=42, cx=1550) if False else pill_pop(fr, 'ANYTHING ON THE RETURN CAN COUNT', 930, t, T('Anything that lands'), red, size=32)
    return frame(fr)

# ================= BLOCK 7 =================
def b7a(t):
    fr = base(t); fr = title_layer(fr, 'STANDARD PART B PREMIUM 2026', t, size=56)
    T = lambda m: tt(7, 0, m)
    C = new(); medicare_card(C, 560, 540, 1.4); fr = POP(fr, C, (300, 350, 820, 740), back((t - 0.3) / 0.5))
    a = T('two hundred two')
    L = new(); v = 202.90 * ease((t - a) / 1.3) if t > a else 0
    txt(L, f'${v:,.2f}', BOLD(150), 420, green, 255 * ease((t - a + 0.2) / 0.3), x=1250); txt(L, 'A MONTH', BOLD(50), 620, white, 255 * ease((t - a) / 0.5), x=1250)
    fr = Image.alpha_composite(fr, L)
    L = new(); rain(L, t, a, 1000, 1500, 400, n=8, seed=71, r=20, dur=3.0); fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: CMS, 2026 Medicare Part B premium'))

def b7b(t):
    fr = base(t); fr = title_layer(fr, 'THE FIRST LINE', t)
    T = lambda m: tt(7, 1, m)
    a = T('above one hundred nine'); b = T('or two hundred eighteen'); c = T('the premium jumps')
    if t > a - 0.3:
        C = new(); avatar(C, 260, 320, blue, 1.5); txt(C, 'SINGLE', BOLD(30), 390, blue, 255, x=260); fr = POP(fr, C, (170, 220, 350, 420), back((t - a + 0.3) / 0.4))
        fr = pill_pop(fr, '> $109,000', 440, t, a, blue, size=40, cx=430)
    if t > b - 0.3:
        C = new(); avatar(C, 260, 640, gold, 1.5); avatar(C, 340, 640, green, 1.5); txt(C, 'MARRIED', BOLD(30), 710, gold, 255, x=300); fr = POP(fr, C, (170, 540, 400, 740), back((t - b + 0.3) / 0.4))
        fr = pill_pop(fr, '> $218,000', 770, t, b, gold, navy, size=40, cx=430)
    base_y = 860; sc = 480 / 284.1
    L = new(); d = ImageDraw.Draw(L)
    u1 = ease((t - 0.5) / 1.0)
    d.rounded_rectangle([1000, base_y - 202.9 * sc * u1, 1200, base_y], radius=14, fill=green + (255,)); txt(L, '$202.90', BOLD(54), base_y - 202.9 * sc * u1 - 70, green, 255 * u1, x=1100); txt(L, 'STANDARD', BOLD(28), base_y + 12, white, 255, x=1100)
    if t > c:
        u2 = ease((t - c) / 1.0)
        d.rounded_rectangle([1360, base_y - 284.1 * sc * u2, 1560, base_y], radius=14, fill=red + (255,)); txt(L, '$284.10', BOLD(54), base_y - 284.1 * sc * u2 - 70, red, 255 * u2, x=1460); txt(L, 'ABOVE THE LINE', BOLD(28), base_y + 12, white, 255, x=1460)
    d.line([940, base_y, 1620, base_y], fill=gold + (255,), width=3)
    fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: CMS, 2026 Medicare Part B premium and IRMAA'))

# ================= BLOCK 8 =================
def b8a(t):
    fr = base(t); fr = title_layer(fr, 'CLIFFS, NOT SLOPES', t)
    T = lambda m: tt(8, 0, m)
    L = new(); d = ImageDraw.Draw(L); x0, x1, yb, yt = 300, 1300, 800, 380
    d.line([x0, yb, x1, yb], fill=gold + (255,), width=3); d.line([x0, yb, x0, yt - 40], fill=gold + (255,), width=3)
    u = ease((t - 0.4) / 1.6)
    for k in range(int(40 * u)):
        x = x0 + k * 25
        d.line([x, yb - 0.25 * k * 25 * 0.5 - 20, x + 14, yb - 0.25 * (k * 25 + 14) * 0.5 - 20], fill=grey + (255,), width=6)
    txt(L, 'SLOPE', BOLD(34), 520, grey, 255 * u, x=560)
    c = T('cliffs, not slopes')
    if t > c:
        u2 = ease((t - c) / 0.8); xj = 1000
        d.line([x0, yb - 80, xj, yb - 80], fill=red + (255,), width=12); d.line([xj, yb - 80, xj, yb - 80 - 300 * u2], fill=red + (255,), width=12); d.line([xj, yb - 80 - 300 * u2, x1, yb - 80 - 300 * u2], fill=red + (255,), width=12) if u2 > 0.95 else None
        txt(L, 'CLIFF', BOLD(44), 380, red, 255 * u2, x=1150)
    fr = Image.alpha_composite(fr, L)
    n = T('Imagine two neighbors')
    if t > n:
        C = new(); avatar(C, 1500, 620, blue, 1.4); avatar(C, 1620, 620, green, 1.4); fr = POP(fr, C, (1400, 520, 1710, 720), back((t - n) / 0.45))
        fr = pill_pop(fr, 'TWO NEIGHBORS', 760, t, n + 0.2, gold, navy, size=36, cx=1560)
    return frame(fr)

def b8b(t):
    fr = base(t); fr = title_layer(fr, 'ONE DOLLAR APART', t)
    T = lambda m: tt(8, 1, m)
    a = T('One reports exactly'); b = T('pays the standard'); c = T('The other reports')
    L = new(); d = ImageDraw.Draw(L)
    d.rectangle([200, 560, 960, 700], fill=(60, 80, 110, 255)); d.rectangle([960, 700, 1720, 840], fill=(60, 80, 110, 255))
    fr = Image.alpha_composite(fr, L)
    if t > a:
        C = new(); avatar(C, 800, 500, blue, 1.6); fr = POP(fr, C, (700, 380, 900, 590), back((t - a) / 0.45))
        fr = pill_pop(fr, '$109,000', 250, t, a + 0.2, blue, size=44, cx=700)
    if t > b:
        fr = pill_pop(fr, '$202.90  STANDARD', 780, t, b, green, navy, size=40, cx=560)
        C = new(); check(C, 560, 720, 34, green); fr = POP(fr, C, (500, 670, 620, 770), back((t - b) / 0.4)) if False else fr
    if t > c:
        u = ease((t - c - 0.4) / 0.8); y = lerp(500, 640, u)
        C = new(); avatar(C, 1140, y, green, 1.6); fr = POP(fr, C, (1040, 380, 1240, 780), back((t - c) / 0.45))
        fr = pill_pop(fr, '$109,001', 250, t, c + 0.2, red, size=44, cx=1240)
        if t > c + 1.4: fr = pill_pop(fr, '$284.10', 870, t, c + 1.4, red, size=40, cx=1300)
    return frame(fr)

def b8c(t):
    fr = base(t); fr = title_layer(fr, 'EVERY SINGLE MONTH', t)
    T = lambda m: tt(8, 2, m)
    a = T('eighty-one')
    L = new(); v = 81.20 * ease((t - a) / 1.0) if t > a else 0
    txt(L, f'+ ${v:,.2f}', BOLD(170), 200, red, 255 * ease((t - 0.2) / 0.4), x=960); fr = Image.alpha_composite(fr, L)
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    st0 = T('every single month') - 0.4
    for m in range(12):
        st = st0 + m * 0.11
        if t < st: continue
        C = new(); d = ImageDraw.Draw(C); x = 380 + (m % 6) * 200; y = 500 + (m // 6) * 190
        d.rounded_rectangle([x, y, x + 180, y + 160], radius=18, fill=card + (255,), outline=red + (255,), width=3)
        txt(C, months[m], BOLD(28), y + 14, white, 255, x=x + 90); txt(C, '+$81.20', BOLD(34), y + 84, red, 255, x=x + 90)
        fr = POP(fr, C, (x - 5, y - 5, x + 185, y + 165), back((t - st) / 0.3))
    return frame(fr)

# ================= BLOCK 9 =================
def b9a(t):
    fr = base(t); fr = title_layer(fr, 'DO THE MATH', t)
    T = lambda m: tt(9, 0, m)
    a = T('by twelve'); b = T('nine hundred seventy-four'); c = T('for one dollar')
    L = new()
    txt(L, '$81.20', BOLD(120), 330, red, 255 * ease((t - 0.3) / 0.4), x=520)
    if t > a - 0.2: txt(L, '\u00d7 12', BOLD(120), 330, white, 255 * ease((t - a + 0.2) / 0.4), x=1000)
    if t > a + 0.3: txt(L, '=', BOLD(120), 330, gold, 255 * ease((t - a - 0.3) / 0.3), x=1300)
    fr = Image.alpha_composite(fr, L)
    if t > b:
        L = new(); v = 974.40 * ease((t - b) / 1.2); txt(L, f'${v:,.2f}', BOLD(190), 500, green, 255, x=960); txt(L, 'A YEAR', BOLD(56), 720, white, 255 * ease((t - b) / 0.5), x=960); fr = Image.alpha_composite(fr, L)
        L = new(); rain(L, t, b, 300, 1620, 700, n=10, seed=81, r=22, dur=3.0); fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'FOR ONE DOLLAR', 800, t, c, red, size=48)
    return frame(fr)

def b9b(t):
    fr = base(t); fr = title_layer(fr, 'A MARRIED COUPLE', t)
    T = lambda m: tt(9, 1, m)
    a = T('A married couple'); b = T('crosses their first line'); c = T('almost twenty-three'); d_ = T('once drug coverage')
    C = new(); avatar(C, 360, 500, blue, 2.2); avatar(C, 520, 500, green, 2.2); fr = POP(fr, C, (250, 350, 640, 650), back((t - 0.3) / 0.5))
    if t > b:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - b) / 0.5); d.line([200, 700, 200 + 500 * u, 700], fill=red + (255,), width=10); txt(L, 'FIRST LINE: $218,000', BOLD(30), 725, red, 255 * u, x=450); fr = Image.alpha_composite(fr, L)
    if t > c - 0.4:
        L = new(); d = ImageDraw.Draw(L); base_y = 860; sc = 480 / 2297; u = ease((t - c + 0.4) / 1.0)
        hb = 1949 * sc * u
        d.rounded_rectangle([820, base_y - hb, 1120, base_y], radius=12, fill=red + (255,)); txt(L, 'PART B', BOLD(30), base_y - hb / 2 - 16, white, 255 * u, x=970) if hb > 40 else None
        if t > d_ - 0.2:
            u2 = ease((t - d_ + 0.2) / 0.8); hd = 348 * sc * u2 * 1.0
            d.rounded_rectangle([820, base_y - hb - hd, 1120, base_y - hb], radius=12, fill=purple + (255,)); txt(L, 'PART D', BOLD(26), base_y - hb - hd / 2 - 14, white, 255 * u2, x=970) if hd > 30 else None
        txt(L, '$' + f'{int(2297 * u):,}', BOLD(96), 220, green, 255 * u, x=1150) if False else None
        d.line([760, base_y, 1180, base_y], fill=gold + (255,), width=3)
        txt(L, '$' + f'{int(2297 * u):,}', BOLD(110), 330, green, 255 * u, x=1500); txt(L, 'EXTRA A YEAR', BOLD(38), 470, white, 255 * u, x=1500)
        fr = Image.alpha_composite(fr, L)
    if t > d_: fr = pill_pop(fr, 'DRUG COVERAGE INCLUDED', 880, t, d_ + 0.3, purple, size=32, cx=1150) if False else pill_pop(fr, 'DRUG COVERAGE INCLUDED', 580, t, d_ + 0.3, purple, size=34, cx=1500)
    return frame(SRC(fr, 'Source: CMS 2026 IRMAA tiers (Part B and Part D surcharges)'))

# ================= BLOCK 10 =================
TIERS = [284.10, 405.80, 527.50, 649.20, 689.90]
def b10a(t):
    fr = base(t); fr = title_layer(fr, 'FIVE TIERS', t)
    T = lambda m: tt(10, 0, m)
    a = T('five tiers'); b = T('at the top'); c = T('six hundred eighty-nine'); d_ = T('more than three times')
    base_y = 860; sc = 560 / 689.9
    L = new(); d = ImageDraw.Draw(L)
    d.line([300, base_y, 1560, base_y], fill=gold + (255,), width=3)
    hs = 202.9 * sc
    d.line([300, base_y - hs, 1560, base_y - hs], fill=green + (255,), width=4); txt(L, 'STANDARD $202.90', BOLD(26), base_y - hs - 34, green, 255, x=520)
    for k, v in enumerate(TIERS):
        st = a + k * 0.35
        if t < st: continue
        u = ease((t - st) / 0.6); h = v * sc * u; x = 420 + k * 240
        col = red if k == 4 and t > b else (gold if k < 4 else gold)
        d.rounded_rectangle([x, base_y - h, x + 170, base_y], radius=12, fill=col + (255,))
        txt(L, f'TIER {k + 1}', BOLD(24), base_y + 10, white, 255, x=x + 85)
        if k < 4: txt(L, f'${v:,.2f}', BOLD(34), base_y - h - 46, white, 255 * u, x=x + 85)
    if t > c:
        u = ease((t - c) / 1.0); txt(L, '$' + f'{689.90 * u:,.2f}', BOLD(60), base_y - 689.9 * sc - 90, red, 255, x=1380)
    fr = Image.alpha_composite(fr, L)
    if t > d_: fr = pill_pop(fr, 'MORE THAN 3\u00d7 THE STANDARD', 230, t, d_, red, size=36, cx=640)
    return frame(SRC(fr, 'Source: CMS, 2026 Part B IRMAA tiers'))

def b10b(t):
    fr = base(t); fr = title_layer(fr, 'PART D ON TOP', t)
    T = lambda m: tt(10, 1, m)
    a = T('ninety-one')
    C = new(); pillbottle(C, 560, 560, 2.2); fr = POP(fr, C, (400, 320, 720, 780), back((t - 0.3) / 0.5))
    L = new(); v = 91.0 * ease((t - a) / 1.0) if t > a else 0
    txt(L, f'+ ${v:,.2f}', BOLD(150), 420, red, 255 * ease((t - a + 0.2) / 0.3), x=1250); txt(L, 'A MONTH, UP TO', BOLD(46), 620, white, 255 * ease((t - a) / 0.5), x=1250); fr = Image.alpha_composite(fr, L)
    L = new(); rain(L, t, a, 950, 1550, 400, n=8, seed=91, r=20, dur=2.5); fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: CMS, 2026 Part D IRMAA'))

SLIDES = {2: [b2a, b2b], 3: [b3a, b3b, b3c], 4: [b4a, b4b], 5: [b5a, b5b, b5c], 6: [b6], 7: [b7a, b7b], 8: [b8a, b8b, b8c], 9: [b9a, b9b], 10: [b10a, b10b]}

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'preview':
        sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(SLIDES)
        fq = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                fn(DUR[b][i] / 30 * fq).convert('RGB').save(f'/home/claude/px_{b}_{i}.png')
        print({b: DUR[b] for b in sel}, 'ok')
    else:
        sel = [int(x) for x in sys.argv[2].split(',')]
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                render_fast(fn, DUR[b][i], f'/mnt/user-data/outputs/v4-b{b}-0{i + 1}.mp4')
                print('done', b, i + 1, DUR[b][i], flush=True)
