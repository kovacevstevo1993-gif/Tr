from v3lib import *
import sys

SENT = {
 3: ["Meet Frank.", "He just turned fifty-nine and a half, and he thinks that's the finish line — the day every rule about his retirement savings resets.", "Meet Mary.", "She turned fifty-nine and a half two years ago, and she already learned the hard way that some of these rules don't work the way you'd guess."],
 4: ["The first thing that changes: the ten percent early withdrawal penalty from the IRS disappears.", "Before fifty-nine and a half, if Frank pulled one hundred thousand dollars from his four-oh-one-k or his IRA, ten thousand dollars of that would go straight to a penalty, on top of regular income tax.", "The day he turns fifty-nine and a half, that penalty is gone for good."],
 5: ["But here's the catch nobody tells you: the penalty disappearing does not mean the money is tax-free.", "Frank still owes ordinary income tax on every dollar he takes from a traditional account.", "The rule only removes the extra ten percent — not the tax bill itself."],
 6: ["Ten thousand dollars is roughly what a lot of families spend on groceries for an entire year.", "That's the exact size of the penalty that vanishes the moment Frank crosses this age — money that used to be lost automatically, now staying in his pocket."],
 7: ["The second change is one almost nobody talks about: in-service withdrawals.", "Many four-oh-one-k plans allow you to withdraw money while you are still working, but only starting at fifty-nine and a half.", "Before that age, most plans simply will not let you touch the funds unless you leave the company."],
 8: ["Mary didn't know her plan allowed this until her financial advisor mentioned it.", "At fifty-nine and a half, she was able to move part of her four-oh-one-k into an IRA, still fully employed, without paying a cent in penalties, just by asking her plan administrator one question."],
 9: ["Not every plan offers this option, and the rules are set by the employer, not the IRS.", "So the real move at fifty-nine and a half isn't withdrawing anything blindly — it's calling your plan and asking one simple question: does this plan allow in-service withdrawals."],
 10: ["The third change involves the Roth IRA, and this is where a lot of people get burned.", "At fifty-nine and a half, the earnings inside a Roth IRA can come out completely tax-free and penalty-free.", "But there's a second requirement that trips people up: the account must have been open for at least five years."],
}
FRAMES = {3: 610, 4: 758, 5: 540, 6: 461, 7: 584, 8: 550, 9: 538, 10: 615}
GROUPS = {3: [[0, 1], [2, 3]], 4: [[0], [1], [2]], 5: [[0], [1], [2]], 6: [[0], [1]], 7: [[0], [1], [2]], 8: [[0], [1]], 9: [[0], [1]], 10: [[0], [1], [2]]}

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

def lerp(a, b, u): return a + (b - a) * u
def clampi(v): return int(max(0, v))
def POP(fr, C, box, s):
    x0, y0, x1, y1 = box
    return pop(fr, C, (max(0, int(x0)), max(0, int(y0)), min(W, int(x1)), min(H, int(y1))), s)
def new(): return Image.new('RGBA', (W, H), (0, 0, 0, 0))

def rot_arrow(C, cx, cy, R, ang, span, col, w=14, alpha=255):
    d = ImageDraw.Draw(C)
    d.arc([cx - R, cy - R, cx + R, cy + R], start=ang, end=ang + span, fill=A(col, alpha), width=w)
    e = math.radians(ang + span)
    tip = (cx + R * math.cos(e), cy + R * math.sin(e)); tg = (-math.sin(e), math.cos(e)); nm = (math.cos(e), math.sin(e))
    d.polygon([(tip[0] + tg[0] * 34, tip[1] + tg[1] * 34), (tip[0] + nm[0] * 24, tip[1] + nm[1] * 24), (tip[0] - nm[0] * 24, tip[1] - nm[1] * 24)], fill=A(col, alpha))

def fly(L, t, st, dur, p0, p1, arc=110, kind='bill', alpha=255, ang=10, size=1.0):
    u = (t - st) / dur
    if u < 0 or u > 1: return
    e = ease(u)
    x = lerp(p0[0], p1[0], e); y = lerp(p0[1], p1[1], e) - arc * math.sin(math.pi * u)
    a = alpha * min(1, u / 0.15) * min(1, (1 - u) / 0.15)
    if kind == 'bill': bill(L, x, y, int(150 * size), int(72 * size), ang + 200 * u, a)
    else: coin(L, x, y, 24 * size, a, squash=abs(math.cos(u * 9)) * 0.6 + 0.4)

def person_box(fr, name, cx, cy, col, t, t0, s=3.4):
    C = new(); avatar(C, cx, cy + math.sin(t * 2) * 6, col, s)
    txt(C, name, BOLD(56), cy + 210, col, 255, x=cx)
    return POP(fr, C, (cx - 250, cy - 200, cx + 250, cy + 290), back((t - t0) / 0.5))

# ============ BLOCK 3 ============
def b3a(t):
    fr = base(t); fr = title_layer(fr, 'MEET FRANK', t)
    fr = person_box(fr, 'FRANK', 430, 520, blue, t, 0.2)
    a = tt(3, 0, 'He just turned')
    if t > a:
        C = new(); d = ImageDraw.Draw(C)
        d.ellipse([610, 250, 810, 450], fill=gold + (255,)); age59(C, 710, 318, 74, navy)
        txt(C, 'JUST TURNED', BOLD(26), 478, white, 255, x=710)
        fr = POP(fr, C, (590, 240, 830, 520), back((t - a) / 0.5))
    a = tt(3, 0, 'and he thinks')
    if t > a:
        C = new(); flag(C, 1010, 760, t)
        txt(C, 'FINISH LINE?', BOLD(50), 800, white, 255, x=1105)
        fr = POP(fr, C, (900, 440, 1340, 880), back((t - a) / 0.5))
    a = tt(3, 0, 'the day every rule')
    if t > a:
        C = new(); money_bag(C, 1560, 560, 1.2); ang = t * 180
        rot_arrow(C, 1560, 560, 200, ang, 230, goldL); rot_arrow(C, 1560, 560, 200, ang + 180, 100, goldL, alpha=0)
        txt(C, 'RETIREMENT SAVINGS', BOLD(30), 250, grey, 255, x=1560)
        txt(C, 'RULES RESET?', BOLD(50), 830, goldL, 255, x=1560)
        fr = POP(fr, C, (1300, 230, 1820, 890), back((t - a) / 0.5))
    return frame(fr)

def b3b(t):
    fr = base(t); fr = title_layer(fr, 'MEET MARY', t)
    fr = person_box(fr, 'MARY', 430, 520, green, t, 0.2)
    a = tt(3, 1, 'two years ago')
    if t > a:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - a) / 0.5)
        d.line([880, 430, 880 + 820 * u, 430], fill=goldL + (255,), width=6)
        d.ellipse([958, 408, 1002, 452], fill=gold + (255,)); txt(L, '59 1/2', BOLD(34), 340, gold, 255 * u, x=980); txt(L, '2 YEARS AGO', BOLD(28), 478, white, 255 * u, x=980)
        d.ellipse([1578, 408, 1622, 452], fill=white + (255,)); txt(L, 'NOW', BOLD(34), 340, white, 255 * u, x=1600)
        px = 980 + 620 * ease((t - a - 0.4) / 1.8); d.ellipse([px - 15, 415, px + 15, 445], fill=green + (255,))
        fr = Image.alpha_composite(fr, L)
    a = tt(3, 1, 'learned the hard way')
    if t > a:
        C = new(); d = ImageDraw.Draw(C)
        d.polygon([(1000, 560), (1080, 700), (920, 700)], fill=card + (255,), outline=red + (255,))
        d.line([1000, 560, 1080, 700, 920, 700, 1000, 560], fill=red + (255,), width=10, joint='curve')
        txt(C, '!', BOLD(70), 596, red, 255, x=1000)
        fr = POP(fr, C, (900, 540, 1100, 720), back((t - a) / 0.45))
        fr = pill_pop(fr, 'LEARNED THE HARD WAY', 590, t, a + 0.15, red, size=40, cx=1440)
    a = tt(3, 1, "some of these rules")
    if t > a:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - a) / 1.6)
        txt(L, "WHAT YOU'D GUESS", BOLD(28), 748, grey, 255, x=880, anchor='l')
        for k in range(int(41 * u)):
            x = 880 + k * 20
            if k % 2 == 0: d.line([x, 810, x + 14, 810], fill=grey + (255,), width=6)
        txt(L, 'HOW IT ACTUALLY WORKS', BOLD(28), 852, red, 255, x=880, anchor='l')
        pts = []
        for k in range(int(42 * u) + 1):
            pts.append((880 + k * 20, 918 + (26 if k % 2 else -26) * (1 + 0.4 * math.sin(k))))
        if len(pts) > 1: d.line(pts, fill=red + (255,), width=7, joint='curve')
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

# ============ BLOCK 4 ============
def b4a(t):
    fr = base(t); fr = title_layer(fr, 'THE FIRST CHANGE', t)
    cx, cy, R = 560, 570, 210
    dis = tt(4, 0, 'disappears'); irs = tt(4, 0, 'from the IRS')
    fade = 1 - ease((t - dis) / 0.9) if t > dis else 1
    L = new(); d = ImageDraw.Draw(L); p = ease((t - 0.3) / 1.1)
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=(40, 62, 92, int(255 * fade)), width=46)
    d.arc([cx - R, cy - R, cx + R, cy + R], start=-54, end=-54 + 324 * p, fill=gold + (int(200 * fade),), width=46)
    d.arc([cx - R, cy - R, cx + R, cy + R], start=-90, end=-90 + 36 * p, fill=red + (int(255 * fade),), width=46)
    txt(L, f'{int(10 * p)}%', BOLD(130), cy - 95, red, 255 * fade, x=cx)
    txt(L, 'EARLY WITHDRAWAL', BOLD(30), cy + 48, white, 255 * fade, x=cx); txt(L, 'PENALTY', BOLD(30), cy + 88, white, 255 * fade, x=cx)
    fr = Image.alpha_composite(fr, L)
    if t > irs:
        C = new(); building(C, 1380, 500, 320, 250, gold if t < dis else (90, 100, 120)); txt(C, 'IRS', BOLD(60), 640, white, 255, x=1380)
        fr = POP(fr, C, (1160, 340, 1600, 720), back((t - irs) / 0.5))
        L = new()
        for k in range(12):
            fly(L, t, irs + 0.3 + k * 0.28, 1.3, (700, 470), (1290, 480), 140, 'coin', 255 if t < dis + 0.3 else 0)
        fr = Image.alpha_composite(fr, L)
    if t > dis:
        fr = pill_pop(fr, 'GONE', 800, t, dis + 0.3, green, size=64, cx=960)
        L = new(); d = ImageDraw.Draw(L)
        for k in range(16):
            a2 = k * 0.39; r = (t - dis) * 300
            al = max(0, 255 * (1 - (t - dis) / 1.3))
            d.ellipse([cx + math.cos(a2) * (R + r) - 9, cy + math.sin(a2) * (R + r) - 9, cx + math.cos(a2) * (R + r) + 9, cy + math.sin(a2) * (R + r) + 9], fill=red + (int(al),))
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b4b(t):
    fr = base(t); fr = title_layer(fr, 'FRANK PULLS $100,000', t, size=58)
    T = lambda m: tt(4, 1, m)
    a = T('four-oh-one-k')
    fr = pill_pop(fr, '401(k)', 185, t, a, blue, size=28, cx=830)
    fr = pill_pop(fr, 'IRA', 185, t, a + 0.5, purple, size=28, cx=990)
    a100 = T('one hundred thousand')
    L = new(); d = ImageDraw.Draw(L)
    txt(L, counter_text(100000 * ease((t - 0.4) / 1.4) // 1000 * 1000), BOLD(100), 470, green, 255 * ease((t - 0.3) / 0.3), x=400)
    gx0, gy0, cell, gap = 700, 300, 34, 8
    a10 = T('ten thousand dollars'); tax = T('on top of regular')
    bx, by = 1480, 520
    for i in range(100):
        r, c = i // 10, i % 10
        st = 0.5 + i * 0.012
        if t < st: continue
        al = 255 * ease((t - st) / 0.25)
        x = gx0 + c * (cell + gap); y = gy0 + r * (cell + gap)
        if i < 10 and t > a10:
            u = ease((t - a10 - c * 0.08) / 1.2)
            x = lerp(x, bx - 150 + c * 8, u); y = lerp(y, by - 20, u)
            col = red
            if u >= 1: al = 0
        else: col = gold
        d.rounded_rectangle([x, y, x + cell, y + cell], radius=6, fill=A(col, al))
    if t > a10:
        txt(L, '$10,000', BOLD(80), 300, red, 255 * ease((t - a10) / 0.4), x=bx)
        txt(L, 'PENALTY', BOLD(34), 400, white, 255 * ease((t - a10) / 0.4), x=bx)
    fr = Image.alpha_composite(fr, L)
    if t > a10:
        C = new(); building(C, bx, by + 80, 280, 220, red); fr = POP(fr, C, (bx - 200, by - 60, bx + 200, by + 300), back((t - a10) / 0.5))
    if t > tax:
        C = new(); tax_form(C, 1330, 700, 190, 200, 255, 'TAX'); fr = POP(fr, C, (1310, 690, 1540, 920), back((t - tax) / 0.45))
        fr = pill_pop(fr, '+ INCOME TAX', 840, t, tax + 0.2, purple, size=34, cx=1300)
    return frame(fr)

def b4c(t):
    fr = base(t); fr = title_layer(fr, 'THE 10% PENALTY BY AGE', t, size=58)
    x0, x1, yt, yb = 300, 1600, 300, 760
    ax = lambda a: x0 + (a - 55) / 10 * (x1 - x0)
    L = new(); d = ImageDraw.Draw(L)
    d.line([x0, yb, x1, yb], fill=gold + (255,), width=3); d.line([x0, yt - 20, x0, yb], fill=gold + (255,), width=3)
    for a in range(55, 66):
        d.line([ax(a), yb - 8, ax(a), yb + 8], fill=gold + (255,), width=3); txt(L, str(a), REG(30), yb + 18, grey, 255, x=ax(a))
    txt(L, '10%', BOLD(34), yt - 18, red, 255, x=x0 - 60); txt(L, '0%', BOLD(34), yb - 18, green, 255, x=x0 - 60)
    xj = ax(59.5)
    for k in range(0, 40):
        y = yt - 20 + k * 14
        if k % 2 == 0 and y < yb: d.line([xj, y, xj, y + 8], fill=goldL + (200,), width=3)
    txt(L, '59\u00bd', SER(60), 200, goldL, 255 * ease((t - 0.6) / 0.4), x=xj)
    pts = [(x0, yt), (xj, yt), (xj, yb), (x1, yb)]; cols = [red, red, green]
    lens = [math.dist(pts[i], pts[i + 1]) for i in range(3)]; tot = sum(lens)
    prog = ease((t - 0.3) / 2.8) * tot; acc = 0
    for i in range(3):
        seg = min(max(prog - acc, 0), lens[i])
        if seg > 0:
            u = seg / lens[i]; p1 = (lerp(pts[i][0], pts[i + 1][0], u), lerp(pts[i][1], pts[i + 1][1], u))
            d.line([pts[i], p1], fill=cols[i] + (255,), width=12)
        acc += lens[i]
    fr = Image.alpha_composite(fr, L)
    g = tt(4, 2, 'that penalty is gone')
    if t > g:
        fr = pill_pop(fr, 'GONE FOR GOOD', 845, t, g, green, size=52, cx=1200)
        L = new(); rain(L, t, g, xj - 100, xj + 400, 740, n=10, seed=4, r=24, dur=1.2); fr = Image.alpha_composite(fr, L)
    return frame(fr)

# ============ BLOCK 5 ============
def b5a(t):
    fr = base(t); fr = title_layer(fr, 'THE CATCH', t, col=red)
    C = new(); money_bag(C, 960, 560 + math.sin(t * 2) * 8, 1.7)
    fr = POP(fr, C, (700, 340, 1220, 800), back((t - 0.3) / 0.5))
    L = new()
    for k in range(4):
        bill(L, 960 + 380 * math.cos(t * 0.9 + k * 1.57), 560 + 200 * math.sin(t * 0.9 + k * 1.57), 170, 82, 20 * math.sin(t + k), 230)
    fr = Image.alpha_composite(fr, L)
    a = tt(5, 0, 'nobody tells you'); fr = pill_pop(fr, 'NOBODY TELLS YOU', 190, t, a, purple, size=38)
    a = tt(5, 0, 'does not mean')
    if t > a:
        fr = stamp(fr, 'NOT TAX-FREE', 960, 700, -8, red, back((t - a) / 0.45), 78)
    return frame(fr)

def b5b(t):
    fr = base(t); fr = title_layer(fr, 'EVERY DOLLAR COUNTS', t)
    fr = person_box(fr, 'FRANK', 300, 520, blue, t, 0.2, 3.0)
    C = new(); vault(C, 760, 540, 110, t, 0.0); txt(C, 'TRADITIONAL', BOLD(30), 700, white, 255, x=760); txt(C, '401(k) / IRA', BOLD(30), 738, gold, 255, x=760)
    fr = POP(fr, C, (600, 400, 920, 790), back((t - 0.4) / 0.5))
    C = new(); tax_form(C, 1330, 330, 270, 340, 255, 'INCOME TAX'); fr = POP(fr, C, (1310, 310, 1620, 700), back((t - 0.5) / 0.5))
    ev = tt(5, 1, 'every dollar')
    L = new(); k = 0; st = 0.9
    while st < DUR[5][1] / 30 - 0.6:
        fly(L, t, st, 1.4, (830, 540), (1330, 500), 130, 'bill', 255, 10, 0.8)
        st += 0.42 if st < ev else 0.16
    fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'EVERY DOLLAR', 800, t, ev, gold, navy, size=42, cx=1120)
    return frame(fr)

def b5c(t):
    fr = base(t); fr = title_layer(fr, 'WHAT CHANGES  ·  WHAT STAYS', t, size=58)
    a = tt(5, 2, 'The rule only')
    C = new(); d = ImageDraw.Draw(C)
    card_box(C, 330, 300, 900, 790, gold, card, 255, 5)
    txt(C, 'EXTRA PENALTY', BOLD(44), 340, white, 255, x=615)
    txt(C, '10%', BOLD(190), 430, red, 255, x=615)
    su = ease((t - a - 0.6) / 0.5)
    d.line([430, 560, 430 + 370 * su, 560 - 0 * su], fill=red + (255,), width=16)
    fr = POP(fr, C, (320, 290, 910, 800), back((t - 0.3) / 0.5))
    fr = pill_pop(fr, 'REMOVED', 700, t, a + 1.0, green, size=44, cx=615)
    b = tt(5, 2, 'not the tax bill')
    if t > b:
        C = new(); card_box(C, 1020, 300, 1590, 790, red, card, 255, 6)
        txt(C, 'INCOME TAX', BOLD(44), 340, white, 255, x=1305); tax_form(C, 1215, 420, 180, 210, 255, 'TAX')
        sc = back((t - b) / 0.5) * (1 + 0.015 * math.sin(t * 6))
        fr = POP(fr, C, (1010, 290, 1600, 800), sc)
        fr = pill_pop(fr, 'STILL THERE', 700, t, b + 0.3, red, size=44, cx=1305)
    return frame(fr)

# ============ BLOCK 6 ============
def b6a(t):
    fr = base(t); fr = title_layer(fr, 'A YEAR OF GROCERIES', t)
    L = new()
    txt(L, counter_text(10000 * ease((t - 0.3) / 1.5) // 100 * 100), BOLD(110), 190, green, 255 * ease((t - 0.2) / 0.3))
    fr = Image.alpha_composite(fr, L)
    a = tt(6, 0, 'a lot of families')
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    for m in range(12):
        st = a + m * 0.16
        if t < st: continue
        C = new(); d = ImageDraw.Draw(C); x = 340 + (m % 6) * 210; y = 340 + (m // 6) * 200
        d.rounded_rectangle([x, y, x + 190, y + 170], radius=18, fill=card + (255,), outline=green + (255,), width=3)
        txt(C, months[m], BOLD(26), y + 12, white, 255, x=x + 95)
        cart(C, x + 95, y + 82, 0.38, 255, gold)
        txt(C, '$830', BOLD(34), y + 122, green, 255, x=x + 95)
        fr = POP(fr, C, (x - 5, y - 5, x + 195, y + 175), back((t - st) / 0.35))
    b = tt(6, 0, 'for an entire year')
    fr = pill_pop(fr, 'ABOUT $830 A MONTH', 780, t, b, gold, navy, size=44)
    return frame(fr)

def b6b(t):
    fr = base(t); fr = title_layer(fr, 'THE $10,000 PENALTY', t)
    T = lambda m: tt(6, 1, m)
    vn = T('vanishes'); lo = T('used to be lost'); st_ = T('now staying')
    if t < vn + 0.6:
        fr = pill_pop(fr, '$10,000 PENALTY', 190, t, 0.3, red, size=46)
    if t > vn:
        fr = pill_pop(fr, 'GONE', 190, t, vn, green, size=46)
    fr = person_box(fr, 'FRANK', 300, 510, blue, t, 0.2, 2.6)
    if t > lo:
        C = new(); d = ImageDraw.Draw(C); dim = 0.45 if t > st_ else 1.0
        d.rounded_rectangle([500, 470, 1330, 530], radius=20, fill=A((90, 104, 126), 230 * dim))
        building(C, 1520, 480, 300, 230, red if t <= st_ else (90, 100, 120), alpha=int(255 * dim)); txt(C, 'IRS', BOLD(56), 630, white, 255 * dim, x=1520)
        fr = POP(fr, C, (450, 330, 1780, 700), back((t - lo) / 0.5))
        L = new(); k = 0; s0 = lo + 0.3
        while s0 < st_ + 0.2:
            fly(L, t, s0, 1.5, (520, 500), (1330, 500), 60, 'bill', 150, 5, 0.7); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
        txt_l = new(); txt(txt_l, 'LOST AUTOMATICALLY', BOLD(34), 570, red, 255 * (0.4 if t > st_ else 1), x=900); fr = Image.alpha_composite(fr, txt_l)
    if t > st_:
        C = new(); wallet(C, 300, 850, 0.85); fr = POP(fr, C, (140, 760, 470, 950), back((t - st_) / 0.45))
        L = new(); s0 = st_ + 0.3
        while s0 < DUR[6][1] / 30 - 0.5:
            fly(L, t, s0, 0.9, (330, 640), (300, 830), 30, 'bill', 255, 0, 0.6); s0 += 0.32
        fr = Image.alpha_composite(fr, L)
        L = new(); txt(L, counter_text(10000 * ease((t - st_) / 1.2) // 100 * 100), BOLD(96), 780, green, 255 * ease((t - st_) / 0.3), x=1000)
        txt(L, 'STAYS IN HIS POCKET', BOLD(38), 890, white, 255 * ease((t - st_ - 0.4) / 0.4), x=1000)
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

# ============ BLOCK 7 ============
def b7a(t):
    fr = base(t); fr = title_layer(fr, '#2  IN-SERVICE WITHDRAWALS', t, size=58)
    C = new(); op = 0.62 * (0.5 - 0.5 * math.cos(t * 1.3)); vault(C, 960, 560, 190, t, op)
    fr = POP(fr, C, (740, 340, 1180, 780), back((t - 0.3) / 0.5))
    a = tt(7, 0, 'almost nobody')
    fr = pill_pop(fr, 'ALMOST NOBODY TALKS ABOUT IT', 830, t, a, gold, navy, size=44)
    L = new(); rain(L, t, 1.0, 400, 700, 780, n=5, seed=8, r=22, dur=3.0); rain(L, t, 1.2, 1230, 1530, 780, n=5, seed=9, r=22, dur=3.0)
    return frame(Image.alpha_composite(fr, L))

def b7b(t):
    fr = base(t); fr = title_layer(fr, 'WHILE STILL WORKING', t)
    T = lambda m: tt(7, 1, m)
    x0, x1, ya = 300, 1600, 700
    ax = lambda a: x0 + (a - 50) / 15 * (x1 - x0)
    L = new(); d = ImageDraw.Draw(L)
    d.line([x0, ya, x1, ya], fill=gold + (255,), width=3)
    for a in range(50, 66, 5):
        d.line([ax(a), ya - 8, ax(a), ya + 8], fill=gold + (255,), width=3); txt(L, str(a), REG(30), ya + 16, grey, 255, x=ax(a))
    st = T('but only starting'); wd = T('withdraw money')
    u = ease((t - 0.4) / 1.6)
    d.rounded_rectangle([x0, 790, x0 + (x1 - x0) * u, 850], radius=30, fill=green + (255,))
    if u > 0.9: txt(L, 'STILL WORKING', BOLD(36), 800, navy, 255, x=(x0 + x1) / 2)
    xj = ax(59.5)
    for k in range(0, 24):
        y = 470 + k * 10
        if k % 2 == 0 and y < ya: d.line([xj, y, xj, y + 6], fill=goldL + (220,), width=3)
    txt(L, '59\u00bd', SER(56), 330, goldL, 255 * ease((t - st) / 0.4), x=xj) if t > st else None
    fr = Image.alpha_composite(fr, L)
    C = new(); op = ease((t - st) / 0.8) * 0.8 if t > st else 0.0
    vault(C, xj, 470, 100, t, op)
    if t <= st: padlock(C, xj, 470, 0.55, red, 255)
    fr = POP(fr, C, (xj - 140, 340, xj + 140, 600), back((t - 0.5) / 0.5))
    px = lerp(ax(51), ax(58.4), ease(t / max(st, 1.0)))
    C = new(); avatar(C, px, 610, gold, 1.5); briefcase(C, px - 60, 650, 0.5)
    fr = Image.alpha_composite(fr, C)
    if t > wd:
        L = new(); s0 = wd
        while s0 < DUR[7][1] / 30 - 0.4:
            fly(L, t, s0, 1.3, (xj, 450), (px + 30, 580), 100, 'bill', 255, 0, 0.6); s0 += 0.45
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b7c(t):
    fr = base(t); fr = title_layer(fr, 'BEFORE 59\u00bd', t)
    T = lambda m: tt(7, 2, m)
    C = new(); vault(C, 520, 560, 150, t, 0.0); padlock(C, 520, 560, 1.2, red, 255)
    fr = POP(fr, C, (330, 370, 710, 760), back((t - 0.3) / 0.5))
    a = T('most plans'); fr = pill_pop(fr, 'MOST PLANS: LOCKED', 190, t, a, red, size=44)
    b = T('unless you leave')
    if t > b:
        C = new(); door(C, 1560, 560, 150, 240, blue, 255, open_p=min(1, (t - b) / 1.5) * 0.9)
        txt(C, 'LEAVE THE COMPANY', BOLD(36), 730, white, 255, x=1500)
        fr = POP(fr, C, (1300, 400, 1760, 780), back((t - b) / 0.45))
        u = ease((t - b - 0.3) / 1.6); px = lerp(1000, 1500, u)
        C = new(); avatar(C, px, 570, gold, 1.8, 255 * (1 - max(0, (u - 0.8) * 5))); briefcase(C, px - 70, 620, 0.5, 255 * (1 - max(0, (u - 0.8) * 5)))
        fr = Image.alpha_composite(fr, C)
    return frame(fr)

# ============ BLOCK 8 ============
def b8a(t):
    fr = base(t); fr = title_layer(fr, 'MARY FINDS OUT', t)
    fr = person_box(fr, 'MARY', 500, 540, green, t, 0.2, 3.0)
    T = lambda m: tt(8, 0, m)
    fa = T('her financial advisor'); me = T('mentioned it')
    if t < me + 0.3:
        C = new(); d = ImageDraw.Draw(C)
        for (x, y, r) in [(560, 250, 50), (640, 230, 60), (720, 260, 46)]: d.ellipse([x - r, y - r, x + r, y + r], fill=(236, 240, 245, 255))
        txt(C, '?', BOLD(80), 200, navy, 255, x=640)
        fr = POP(fr, C, (480, 150, 800, 340), back((t - 0.7) / 0.4))
    if t > fa:
        fr = person_box(fr, 'ADVISOR', 1400, 540, gold, t, fa, 3.0)
        C = new(); bubble(C, 1000, 230, 1520, 380, "YOUR PLAN MAY\nALLOW THIS", tail='right', size=38)
        fr = POP(fr, C, (990, 220, 1530, 440), back((t - fa - 0.3) / 0.45))
    if t > me:
        C = new(); bulb(C, 500, 300, 1.4); fr = POP(fr, C, (380, 160, 620, 420), back((t - me) / 0.45))
    return frame(fr)

def b8b(t):
    fr = base(t); fr = title_layer(fr, '401(k)  \u2192  IRA', t)
    T = lambda m: tt(8, 1, m)
    mv = T('move part'); em = T('still fully employed'); nc = T('without paying'); ask = T('just by asking')
    C = new(); card_box(C, 250, 250, 650, 480, gold, card, 255, 5); txt(C, '401(k)', BOLD(80), 300, gold, 255, x=450); txt(C, 'YOUR PLAN', BOLD(30), 410, grey, 255, x=450)
    fr = POP(fr, C, (240, 240, 660, 490), back((t - 0.3) / 0.5))
    if t > mv - 0.2:
        C = new(); card_box(C, 1270, 250, 1670, 480, blue, card, 255, 5); txt(C, 'IRA', BOLD(80), 300, blue, 255, x=1470); txt(C, 'YOUR ACCOUNT', BOLD(30), 410, grey, 255, x=1470)
        fr = POP(fr, C, (1260, 240, 1680, 490), back((t - mv + 0.2) / 0.5))
        L = new(); d = ImageDraw.Draw(L)
        d.line([700, 365, 1210, 365], fill=goldL + (255,), width=8); d.polygon([(1235, 365), (1200, 342), (1200, 388)], fill=goldL + (255,))
        s0 = mv
        while s0 < DUR[8][1] / 30 - 0.4:
            fly(L, t, s0, 1.2, (700, 365), (1220, 365), 70, 'bill', 255, 0, 0.65); s0 += 0.55
        fr = Image.alpha_composite(fr, L)
    if t > em:
        C = new(); briefcase(C, 960, 610, 0.9); fr = POP(fr, C, (860, 520, 1060, 690), back((t - em) / 0.45))
        fr = pill_pop(fr, 'STILL FULLY EMPLOYED', 530, t, em + 0.1, green, navy, size=40, cx=1330)
    if t > nc:
        L = new(); txt(L, '$0', BOLD(150), 700, green, 255 * ease((t - nc) / 0.3), x=430)
        txt(L, 'PENALTY', BOLD(44), 860, white, 255 * ease((t - nc) / 0.3), x=430); fr = Image.alpha_composite(fr, L)
        C = new(); check(C, 640, 780, 44, green); fr = POP(fr, C, (580, 720, 700, 840), back((t - nc - 0.2) / 0.4))
    if t > ask:
        fr = person_box(fr, 'ADMIN', 1500, 700, gold, t, ask, 1.5) if False else fr
        C = new(); avatar(C, 1500, 800, gold, 1.5); txt(C, 'PLAN ADMINISTRATOR', BOLD(28), 890, white, 255, x=1500)
        fr = POP(fr, C, (1340, 700, 1660, 930), back((t - ask) / 0.45))
        C = new(); bubble(C, 1000, 660, 1340, 780, 'ONE QUESTION', size=36, tail='right')
        fr = POP(fr, C, (990, 650, 1350, 830), back((t - ask - 0.3) / 0.45))
    return frame(fr)

# ============ BLOCK 9 ============
def b9a(t):
    fr = base(t); fr = title_layer(fr, 'NOT EVERY PLAN OFFERS IT', t)
    T = lambda m: tt(9, 0, m)
    a = T('Not every plan')
    ok = [True, False, False, True, False, True]
    for k in range(6):
        st = 0.5 + k * 0.4
        if t < st: continue
        cx = 1000 + (k % 3) * 310; cy = 380 + (k // 3) * 270
        C = new(); card_box(C, cx - 130, cy - 100, cx + 130, cy + 100, green if ok[k] else red, card, 255, 5)
        txt(C, f'PLAN {chr(65 + k)}', BOLD(34), cy - 88, white, 255, x=cx)
        (check if ok[k] else cross)(C, cx, cy - 5, 36, green if ok[k] else red)
        txt(C, 'ALLOWED' if ok[k] else 'NOT OFFERED', BOLD(28), cy + 52, green if ok[k] else red, 255, x=cx)
        fr = POP(fr, C, (cx - 140, cy - 110, cx + 140, cy + 110), back((t - st) / 0.4))
    em = T('set by the employer')
    if t > em:
        C = new(); building(C, 430, 400, 260, 200, gold); txt(C, 'EMPLOYER', BOLD(40), 520, gold, 255, x=430); txt(C, 'SETS THE RULES', BOLD(28), 566, white, 255, x=430)
        fr = POP(fr, C, (250, 280, 620, 620), back((t - em) / 0.45))
    ir = T('not the IRS')
    if t > ir:
        C = new(); building(C, 430, 760, 200, 150, (90, 100, 120)); cross(C, 540, 700, 40, red); txt(C, 'NOT THE IRS', BOLD(34), 850, red, 255, x=430)
        fr = POP(fr, C, (290, 650, 620, 900), back((t - ir) / 0.45))
    return frame(fr)

def b9b(t):
    fr = base(t); fr = title_layer(fr, 'THE REAL MOVE', t)
    T = lambda m: tt(9, 1, m)
    a = T("isn't withdrawing")
    if t > a:
        C = new(); bill(C, 330, 560, 260, 126, 8, 255); d = ImageDraw.Draw(C)
        d.ellipse([190, 420, 470, 700], outline=red + (255,), width=16); d.line([230, 640, 430, 480], fill=red + (255,), width=16)
        txt(C, 'BLINDLY', BOLD(40), 730, red, 255, x=330)
        fr = POP(fr, C, (170, 400, 500, 800), back((t - a) / 0.5))
    b = T("it's calling")
    if t > b:
        C = new(); phone(C, 800, 560, 1.4, 255, t - b); fr = Image.alpha_composite(fr, C)
    c = T('does this plan allow')
    if t > c:
        s = "Does this plan allow\nin-service withdrawals?"
        n = int(len(s) * min(1, (t - c) / 2.4)); part = s[:n]
        C = new(); bubble(C, 1080, 400, 1780, 640, part, size=42, tail='left')
        fr = POP(fr, C, (1070, 390, 1790, 700), back((t - c) / 0.4))
    e = T('asking one simple')
    fr = pill_pop(fr, 'ASK ONE SIMPLE QUESTION', 800, t, e, gold, navy, size=44)
    return frame(fr)

# ============ BLOCK 10 ============
def b10a(t):
    fr = base(t); fr = title_layer(fr, '#3  THE ROTH IRA', t)
    C = new(); card_box(C, 600, 400, 1320, 700, gold, card, 255, 6); txt(C, 'ROTH IRA', BOLD(130), 470, gold, 255, x=960)
    fr = POP(fr, C, (590, 390, 1330, 710), back((t - 0.3) / 0.5))
    L = new()
    for k in range(6):
        a = t * 1.1 + k * 1.047
        coin(L, 960 + 470 * math.cos(a), 550 + 260 * math.sin(a), 30, 255, squash=abs(math.cos(a * 3)) * 0.6 + 0.4)
    fr = Image.alpha_composite(fr, L)
    g = tt(10, 0, 'get burned')
    if t > g:
        C = new(); flame(C, 1560, 610 + math.sin(t * 9) * 6, 1.6); flame(C, 1400, 690, 0.9); flame(C, 1700, 700, 0.8)
        fr = POP(fr, C, (1280, 420, 1800, 820), back((t - g) / 0.45))
        fr = pill_pop(fr, 'A LOT OF PEOPLE GET BURNED', 820, t, g + 0.2, red, size=44)
    return frame(fr)

def b10b(t):
    fr = base(t); fr = title_layer(fr, 'ROTH EARNINGS AT 59\u00bd', t, size=58)
    T = lambda m: tt(10, 1, m)
    vals = [60, 90, 130, 170, 220, 270, 330, 400]
    L = new(); d = ImageDraw.Draw(L)
    d.line([320, 780, 1080, 780], fill=gold + (255,), width=3)
    for i, v in enumerate(vals):
        h = v * ease((t - 0.3 - i * 0.22) / 0.7)
        if h > 2: d.rounded_rectangle([340 + i * 90, 780 - h, 410 + i * 90, 780], radius=10, fill=green + (255,))
    txt(L, 'EARNINGS INSIDE THE ROTH IRA', BOLD(30), 810, white, 255 * ease((t - 0.5) / 0.4), x=700)
    fr = Image.alpha_composite(fr, L)
    co = T('come out')
    if t > co:
        C = new(); wallet(C, 1500, 620, 1.0); fr = POP(fr, C, (1340, 520, 1680, 730), back((t - co) / 0.45))
        L = new(); s0 = co
        while s0 < DUR[10][1] / 30 - 0.5:
            fly(L, t, s0, 1.2, (1000, 420), (1450, 600), 120, 'coin', 255, 0, 1.0); s0 += 0.3
        fr = Image.alpha_composite(fr, L)
    a = T('tax-free')
    if t > a: fr = stamp(fr, 'TAX-FREE', 1400, 340, -6, green, back((t - a) / 0.45), 60)
    b = T('penalty-free')
    if t > b: fr = stamp(fr, 'PENALTY-FREE', 1400, 850, -6, green, back((t - b) / 0.45), 60)
    return frame(fr)

def b10c(t):
    fr = base(t); fr = title_layer(fr, 'THE 5-YEAR RULE', t)
    T = lambda m: tt(10, 2, m)
    sr = T('second requirement'); tr = T('trips people up'); ac = T('the account must')
    fr = pill_pop(fr, 'A SECOND REQUIREMENT', 185, t, sr, purple, size=40)
    for k in range(5):
        cx = 500 + k * 230; cy = 500
        C = new(); d = ImageDraw.Draw(C)
        st = ac + k * 0.55
        fill = gold if t > st else card
        d.rounded_rectangle([cx - 95, cy - 100, cx + 95, cy + 100], radius=22, fill=A(fill, 255), outline=A(gold, 255), width=5)
        txt(C, f'YEAR {k + 1}', BOLD(38), cy - 80, navy if t > st else white, 255, x=cx)
        if t > st: check(C, cx, cy + 25, 42, green)
        fr = POP(fr, C, (cx - 105, cy - 110, cx + 105, cy + 110), back((t - 0.5 - k * 0.15) / 0.4))
    if t > tr:
        C = new(); d = ImageDraw.Draw(C)
        d.polygon([(1700, 300), (1770, 420), (1630, 420)], fill=card + (255,)); d.line([1700, 300, 1770, 420, 1630, 420, 1700, 300], fill=red + (255,), width=9, joint='curve')
        txt(C, '!', BOLD(60), 330, red, 255, x=1700)
        fr = POP(fr, C, (1600, 280, 1800, 440), back((t - tr) / 0.4))
    last = ac + 4 * 0.55 + 0.4
    C = new(); padlock(C, 960, 800, 0.8, green if t > last else red, 255, open_=t > last); fr = POP(fr, C, (860, 690, 1060, 900), back((t - 0.8) / 0.4))
    if t > last: fr = pill_pop(fr, 'AT LEAST 5 YEARS', 820, t, last, green, navy, size=44, cx=1400)
    return frame(fr)

SLIDES = {3: [b3a, b3b], 4: [b4a, b4b, b4c], 5: [b5a, b5b, b5c], 6: [b6a, b6b], 7: [b7a, b7b, b7c], 8: [b8a, b8b], 9: [b9a, b9b], 10: [b10a, b10b, b10c]}

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'preview':
        sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(SLIDES)
        fracs = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [0.9]
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                T = DUR[b][i] / 30
                for fq in fracs:
                    fn(T * fq).convert('RGB').save(f'/home/claude/pv_{b}_{i}_{int(fq*100)}.png')
        print({b: DUR[b] for b in sel}, 'ok')
    else:
        sel = [int(x) for x in sys.argv[2].split(',')]
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                render_fast(fn, DUR[b][i], f'/mnt/user-data/outputs/v3-b{b}-0{i + 1}.mp4')
                print('done', b, i + 1, DUR[b][i], flush=True)
