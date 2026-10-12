from v3lib import *
from v3b3_10 import POP, new
from v4b2_10 import cal_card
from v5b1 import amb, sparks, shake
from v5lib import arrow_r, arrow_d, paycheck, magnifier
from v6b1 import A_, E_, chip_src
from v6b2 import chip
from v7b2_5 import tracker, numcard, ic_med, ic_ss, ic_coins, ic_time
import sys, math

# durate (fotogrammi) dalla timeline dell'utente
SPEC = {6: [130, 170, 200], 7: [140, 150, 169], 8: [125, 255, 165, 129], 9: [235, 120, 283], 10: [232, 310],
        11: [170, 190, 190, 123], 12: [150, 230, 178], 13: [125, 181], 14: [170, 150, 168], 15: [190, 200, 152]}
TOT = {6: 500, 7: 459, 8: 674, 9: 638, 10: 542, 11: 673, 12: 558, 13: 306, 14: 488, 15: 542}
for b in SPEC: assert sum(SPEC[b]) == TOT[b], b
CUR = {'D': 5.0}
D = lambda: CUR['D']
def tt_(f): return f * D()                 # istante a frazione f della slide
def LASTA(): return 0.8 * D() - 0.35       # ultimo elemento: finisce di comparire all'80%
def LASTP(): return 0.8 * D() - 0.45       # idem per le pillole
def sp(n):                                 # n istanti distribuiti da 0.07D fino all'ultimo (80%)
    if n == 1: return [LASTA()]
    a, b = 0.07 * D(), LASTA()
    return [a + (b - a) * k / (n - 1) for k in range(n)]
def P2(fr, C, box, t, t0): return A_(fr, C, box, t, t0, 0.35)

def fit(text, maxw, size, bold=True):
    d = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    while size > 20 and d.textlength(text, font=BOLD(size)) > maxw: size -= 2
    return BOLD(size)

def stage(t, title, seed, size=60):
    fr = base(t); fr = amb(fr, t, seed, 7, 55)
    return title_layer(fr, title, t, size=size)

def pill_last(fr, t, text, y, col=red, tcol=(255, 255, 255), size=50, cx=960, t0=None):
    return pill_pop(fr, text, y, t, LASTP() if t0 is None else t0, col, tcol=tcol, size=size, cx=cx)

def card_(C, x0, y0, x1, y1, col, head=None, val=None, sub=None, vsize=96, vcol=white, fill=card):
    d = ImageDraw.Draw(C); cx = (x0 + x1) / 2
    d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=fill + (255,), outline=col + (255,), width=6)
    if head: txt(C, head, fit(head, x1 - x0 - 40, 38), y0 + 18, col, 255, x=cx)
    if val: txt(C, val, fit(val, x1 - x0 - 40, vsize), y0 + (78 if head else 40), vcol, 255, x=cx)
    if sub: txt(C, sub, fit(sub, x1 - x0 - 40, 34), y1 - 56, grey, 255, x=cx)

def eq(fr, t, y, parts, times, h=230, cw=420, ow=130):
    """riga di calcolo: card ('c', head, val, sub, col) e operatori ('o', '+')"""
    nc = sum(1 for p in parts if p[0] == 'c'); total = nc * cw + (len(parts) - nc) * ow; x = 960 - total / 2; i = 0
    for p in parts:
        if p[0] == 'c':
            _, head, val, sub, col = p; t0 = times[i]; i += 1
            if t > t0:
                C = new(); card_(C, x, y, x + cw, y + h, col, head, val, sub); fr = P2(fr, C, (x - 20, y - 20, x + cw + 20, y + h + 20), t, t0)
            x += cw
        else:
            t0 = times[i] - 0.1 if i < len(times) else times[-1]
            if t > t0:
                L = new(); txt(L, p[1], BOLD(110), y + h / 2 - 70, goldL, 255 * E_(t, t0, 0.3), x=x + ow / 2); fr = Image.alpha_composite(fr, L)
            x += ow
    return fr

def ring_(C, cx, cy, r, frac, col, w=40, bg=(60, 80, 110)):
    d = ImageDraw.Draw(C); bb = [cx - r, cy - r, cx + r, cy + r]
    d.arc(bb, 0, 360, fill=bg + (255,), width=w); d.arc(bb, -90, -90 + 360 * frac, fill=col + (255,), width=w)

def bars3(fr, t, base_y, items, times, maxh=520, bw=240, gap=120):
    n = len(items); total = n * bw + (n - 1) * gap; x = 960 - total / 2
    for k, (lab, val, h, col, vcol) in enumerate(items):
        t0 = times[k]
        if t > t0:
            u = ease((t - t0) / 0.8); hh = h * maxh * u
            C = new(); d = ImageDraw.Draw(C)
            d.rounded_rectangle([x, base_y - hh, x + bw, base_y], radius=18, fill=col + (255,), outline=white + (255,), width=3)
            if u > 0.6:
                txt(C, val, fit(val, bw + gap - 10, 56), base_y - hh - 78, vcol, 255 * min(1, (u - 0.6) / 0.4), x=x + bw / 2)
                txt(C, lab, fit(lab, bw + gap - 10, 38), base_y + 16, white, 255 * min(1, (u - 0.6) / 0.4), x=x + bw / 2)
            fr = Image.alpha_composite(fr, C)
        x += bw + gap
    return fr

def avatars(fr, t, cx, cy, n, cols, t0, spread=0.5, per=6, gx=95, gy=120, s=0.9):
    C = new(); rows = (n + per - 1) // per
    for k in range(n):
        r_, c_ = divmod(k, per); u = back((t - t0 - spread * k / n) / 0.35)
        if u <= 0: continue
        avatar(C, cx + (c_ - (per - 1) / 2) * gx, cy + (r_ - (rows - 1) / 2) * gy, cols[k % len(cols)] if isinstance(cols, list) else cols, s * min(1, u))
    return Image.alpha_composite(fr, C)

# ======================= BLOCCO 6 =======================
def s6a(t):
    fr = stage(t, 'A REALITY CHECK', 41); T = sp(3)
    if t > T[0]:
        C = new(); money_bag(C, 560, 520, 1.9); coin_stack(C, 330, 700, 6, 66); coin_stack(C, 790, 700, 8, 66)
        card_(C, 1100, 330, 1700, 560, gold, None, '$500,000', 'SAVED FOR RETIREMENT', 104, goldL)
        fr = P2(fr, C, (200, 250, 1730, 760), t, T[0])
    if t > T[1]:
        C = new(); magnifier(C, 1400, 640, 70, goldL); fr = P2(fr, C, (1280, 540, 1620, 800), t, T[1])
    return frame(pill_last(fr, t, 'WHERE DOES $500,000 STAND?', 820, gold, navy, 54, 960))

def s6b(t):
    fr = stage(t, 'THE FEDERAL RESERVE SURVEY', 42); T = sp(4)
    if t > T[0]:
        C = new(); building(C, 380, 450, 400, 330, blue); txt(C, 'FEDERAL RESERVE', BOLD(52), 640, white, 255, x=380); fr = P2(fr, C, (130, 230, 640, 720), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([760, 270, 1300, 700], radius=30, fill=(236, 240, 245, 255), outline=goldL + (255,), width=6)
        txt(C, 'SURVEY OF', BOLD(44), 305, navy, 255, x=1030); txt(C, 'CONSUMER FINANCES', BOLD(46), 360, navy, 255, x=1030)
        for k in range(5): d.rectangle([810, 450 + k * 48, 1250, 470 + k * 48], fill=(170, 180, 200, 255))
        fr = P2(fr, C, (740, 250, 1320, 720), t, T[1])
    if t > T[2]:
        C = new(); cal_card(C, 1420, 290, 1760, 620, 'SURVEY YEAR', '2022', 120, blue); fr = P2(fr, C, (1400, 270, 1780, 640), t, T[2])
    return frame(fr if t < T[3] else chip_src(fr, 'SOURCE: FEDERAL RESERVE, SURVEY OF CONSUMER FINANCES 2022', 840, t, T[3]))

def s6c(t):
    fr = stage(t, 'THE TYPICAL HOUSEHOLD, AGE 65 TO 74', 43, 56); T = sp(4)
    fr = avatars(fr, t, 400, 430, 10, [blue, pink, gold, green, purple], T[0], 0.6, 5, 120, 150, 1.2)
    if t > T[0]: 
        L = new(); txt(L, 'AGE 65 TO 74', BOLD(58), 640, white, 255 * E_(t, T[0] + 0.3), x=400); fr = Image.alpha_composite(fr, L)
    if t > T[1]:
        C = new(); wallet(C, 1000, 400, 1.9); txt(C, 'RETIREMENT', BOLD(46), 600, white, 255, x=1000); txt(C, 'ACCOUNT', BOLD(46), 655, white, 255, x=1000); fr = P2(fr, C, (800, 290, 1200, 740), t, T[1])
    if t > T[2]:
        v = 200000 * ease((t - T[2]) / 0.9)
        C = new(); card_(C, 1300, 330, 1800, 560, gold, 'THE TYPICAL BALANCE', '$' + f'{int(v):,}', None, 100, goldL); fr = P2(fr, C, (1280, 310, 1820, 580), t, T[2])
    return frame(pill_last(fr, t, 'HOUSEHOLDS WITH AN ACCOUNT HELD $200,000', 800, gold, navy, 46))

# ======================= BLOCCO 7 =======================
def s7a(t):
    fr = stage(t, 'THE TYPICAL BALANCE BY AGE', 44); T = sp(3)
    fr = bars3(fr, t, 760, [('AGE 55 TO 64', '$185,000', 185 / 200, (90, 130, 190), white), ('AGE 65 TO 74', '$200,000', 1.0, gold, goldL)][:2], [T[0], T[1]], 480, 300, 200)
    return frame(pill_last(fr, t, 'TYPICAL BALANCES: UNDER $200,000', 850, gold, navy, 50))

def s7b(t):
    fr = stage(t, 'ONLY ABOUT 54% HAVE AN ACCOUNT', 45, 58); T = sp(3)
    C = new()
    for k in range(20):
        r_, c_ = divmod(k, 5); u = back((t - T[0] - 0.7 * k / 20) / 0.3)
        if u <= 0: continue
        avatar(C, 330 + c_ * 125, 300 + r_ * 125, gold if k < 11 else (95, 110, 135), 1.0 * min(1, u))
    fr = Image.alpha_composite(fr, C)
    if t > T[1]:
        C = new(); ring_(C, 1380, 430, 175, 0.54 * ease((t - T[1]) / 0.8), gold, 46)
        txt(C, '54%', BOLD(120), 372, goldL, 255, x=1380); txt(C, 'HAVE AN', BOLD(32), 470, white, 255, x=1380); txt(C, 'ACCOUNT', BOLD(32), 508, white, 255, x=1380)
        fr = P2(fr, C, (1160, 230, 1600, 660), t, T[1])
    return frame(pill_last(fr, t, 'OF HOUSEHOLDS HAD A RETIREMENT ACCOUNT AT ALL', 870, gold, navy, 46))

def s7c(t):
    fr = stage(t, 'WHERE $500,000 STANDS', 46); T = sp(5)
    fr = bars3(fr, t, 700, [('AGE 55 TO 64', '$185,000', 0.37, (90, 130, 190), white), ('AGE 65 TO 74', '$200,000', 0.40, (90, 130, 190), white), ('YOUR $500,000', '$500,000', 1.0, gold, goldL)], [T[0], T[1], T[2]], 440, 280, 140)
    if t > T[3]: fr = pill_pop(fr, 'WELL ABOVE THE TYPICAL BALANCE', 800, t, T[3], green, tcol=navy, size=36, cx=960)
    return frame(pill_last(fr, t, 'THE QUESTION: WHAT CAN IT DO?', 902, gold, navy, 36))

# ======================= BLOCCO 8 =======================
def s8a(t):
    fr = stage(t, 'NUMBER ONE', 47); T = sp(3)
    fr = numcard(fr, t, T[0], 140, 200, 900, 800, 1, 'HOW MUCH CAN', 'YOUR SAVINGS', 'SAFELY PAY EVERY MONTH', ic_coins, gold) if t > T[0] else fr
    if t > T[1]:
        C = new(); paycheck(C, 1060, 280, 1770, 700, green, '$ ?', 'EVERY MONTH', 'SAFE PAYMENT', 160); fr = P2(fr, C, (1040, 260, 1790, 720), t, T[1])
        L = new(); arrow_r(L, 920, 1040, 490, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(tracker(fr, t, {1}, 0.3, 965), t, 'SAFELY PAY EACH MONTH', 815, gold, navy, 46))

def s8b(t):
    fr = stage(t, 'THE FOUR PERCENT RULE', 48); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 150, 260, 650, 640, gold, 'THE CLASSIC ANSWER', '4%', 'THE FOUR PERCENT RULE', 230, goldL); fr = P2(fr, C, (130, 240, 670, 660), t, T[0])
    if t > T[1]:
        C = new(); avatar(C, 1000, 430, blue, 3.0); txt(C, 'WILLIAM BENGEN', BOLD(52), 580, white, 255, x=1000); txt(C, 'FINANCIAL PLANNER', BOLD(38), 640, grey, 255, x=1000); fr = P2(fr, C, (780, 250, 1220, 700), t, T[1])
        L = new(); arrow_r(L, 680, 770, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); cal_card(C, 1380, 290, 1760, 640, 'PUBLISHED', '1994', 130, goldL, ); fr = P2(fr, C, (1360, 270, 1780, 660), t, T[2])
        L = new(); arrow_r(L, 1240, 1360, 450, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'RESEARCH PUBLISHED IN 1994', 830, gold, navy, 50))

def s8c(t):
    fr = stage(t, 'YOUR FIRST YEAR OF RETIREMENT', 49, 56); T = sp(4)
    if t > T[0]:
        C = new(); money_bag(C, 420, 480, 1.9); card_(C, 190, 680, 650, 800, gold, None, '$500,000', None, 70, goldL); fr = P2(fr, C, (170, 270, 670, 820), t, T[0])
    if t > T[1]:
        C = new(); ring_(C, 960, 470, 130, 0.04 * 6 * ease((t - T[1]) / 0.7), gold, 56); txt(C, '4%', BOLD(110), 410, goldL, 255, x=960); fr = P2(fr, C, (800, 310, 1120, 630), t, T[1])
        L = new(); arrow_r(L, 640, 800, 470, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); paycheck(C, 1300, 300, 1780, 640, green, '4%', 'WITHDRAW', 'YEAR ONE', 130); fr = P2(fr, C, (1280, 280, 1800, 660), t, T[2])
        L = new(); arrow_r(L, 1130, 1280, 470, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'YOU WITHDRAW 4% OF YOUR SAVINGS', 820, gold, navy, 50))

def s8d(t):
    fr = stage(t, 'THEN RAISE IT WITH INFLATION', 50); T = sp(4)
    labs = [('YEAR 1', '4%', 'FIRST WITHDRAWAL', blue), ('YEAR 2', '+ INFLATION', 'A LITTLE MORE', gold), ('YEAR 3', '+ INFLATION', 'A LITTLE MORE', gold)]
    for k, (h, v, s_, col) in enumerate(labs):
        if t > T[k]:
            C = new(); card_(C, 130 + k * 600, 400 - k * 70, 560 + k * 600, 700 - k * 70 + 0, col, h, v, s_, 66, white); fr = P2(fr, C, (110 + k * 600, 380 - k * 70, 580 + k * 600, 720 - k * 70), t, T[k])
            if k: 
                L = new(); arrow_r(L, 570 + (k - 1) * 600, 130 + k * 600, 590 - k * 70 + 0, goldL, 255 * E_(t, T[k] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'RAISE THE AMOUNT EACH YEAR WITH INFLATION', 830, green, navy, 48))

# ======================= BLOCCO 9 =======================
def s9a(t):
    fr = stage(t, 'FOUR PERCENT OF $500,000', 51); T = sp(5)
    fr = eq(fr, t, 230, [('c', 'YOUR SAVINGS', '$500,000', None, gold), ('o', '×'), ('c', 'THE RULE', '4%', None, blue), ('o', '='), ('c', 'EVERY YEAR', '$20,000', 'ABOUT', green)], [T[0], T[1], T[2]], 250, 400, 150)
    fr = eq(fr, t, 580, [('c', 'EVERY YEAR', '$20,000', None, green), ('o', '÷'), ('c', 'MONTHS', '12', None, blue), ('o', '='), ('c', 'EVERY MONTH', '$1,667', 'ABOUT', goldL)], [T[2] + 0.4, T[3], T[4]], 250, 400, 150)
    return frame(fr)

def s9b(t):
    fr = stage(t, 'BUT THE RULE IS NOT CARVED IN STONE', 52, 56); T = sp(3)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C)
        d.polygon([(660, 760), (640, 360), (720, 270), (1200, 270), (1280, 360), (1260, 760)], fill=(120, 128, 142, 255), outline=(60, 66, 80, 255))
        d.line([(960, 270), (930, 400), (990, 480), (940, 600), (975, 760)], fill=(40, 46, 60, 255), width=10)
        txt(C, '4%', BOLD(200), 380, (230, 232, 238), 255, x=960); fr = P2(fr, C, (620, 250, 1300, 780), t, T[0])
    if t > T[1]:
        L = new(); txt(L, '?', BOLD(150), 330, red, 255 * E_(t, T[1]), x=1450); txt(L, '?', BOLD(110), 520, red, 255 * E_(t, T[1] + 0.2), x=1520); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'IT IS NOT CARVED IN STONE', 830, red, (255, 255, 255), 54))

def s9c(t):
    fr = stage(t, 'MORNINGSTAR, THE RESEARCH FIRM', 53); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 130, 280, 650, 620, blue, 'INVESTMENT RESEARCH', 'MORNINGSTAR', None, 66, white); fr = P2(fr, C, (110, 260, 670, 640), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([760, 250, 1190, 700], radius=26, fill=(236, 240, 245, 255), outline=goldL + (255,), width=6)
        txt(C, 'STATE OF', BOLD(38), 285, navy, 255, x=975); txt(C, 'RETIREMENT', BOLD(38), 330, navy, 255, x=975); txt(C, 'INCOME', BOLD(38), 372, navy, 255, x=975)
        d.rounded_rectangle([830, 440, 1120, 515], radius=14, fill=gold + (255,)); txt(C, 'DECEMBER 2025', BOLD(36), 458, navy, 255, x=975)
        for k in range(4): d.rectangle([830, 550 + k * 36, 1120, 562 + k * 36], fill=(170, 180, 200, 255))
        fr = P2(fr, C, (740, 230, 1210, 720), t, T[1])
        L = new(); arrow_r(L, 660, 750, 450, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); card_(C, 1300, 300, 1800, 650, green, 'SAFE STARTING RATE', '3.9%', 'NOT 4%', 170, white); fr = P2(fr, C, (1280, 280, 1820, 670), t, T[2])
        L = new(); arrow_r(L, 1200, 1290, 450, goldL, 255 * E_(t, T[2] - 0.2)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'ITS 2026 ESTIMATE: THREE POINT NINE PERCENT', 830, gold, navy, 46))

# ======================= BLOCCO 10 =======================
def s10a(t):
    fr = stage(t, 'WHAT THE 3.9% ASSUMES', 54); T = sp(4)
    if t > T[0]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([130, 260, 640, 720], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        d.ellipse([260, 330, 510, 580], fill=(95, 135, 195, 255)); d.pieslice([260, 330, 510, 580], -90, 54, fill=gold + (255,))
        txt(C, '30 TO 50%', BOLD(60), 600, goldL, 255, x=385); txt(C, 'IN STOCKS', BOLD(44), 665, white, 255, x=385); fr = P2(fr, C, (110, 240, 660, 740), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([700, 260, 1210, 720], radius=34, fill=card + (255,), outline=gold + (255,), width=6)
        cal_card(C, 790, 300, 1120, 560, 'RETIREMENT', '30', 120, gold); txt(C, '30 YEARS', BOLD(60), 600, goldL, 255, x=955); txt(C, 'LONG RETIREMENT', BOLD(36), 665, white, 255, x=955); fr = P2(fr, C, (680, 240, 1230, 740), t, T[1])
    if t > T[2]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1270, 260, 1780, 720], radius=34, fill=card + (255,), outline=green + (255,), width=6)
        ring_(C, 1525, 440, 120, 0.9 * ease((t - T[2]) / 0.8), green, 40); txt(C, '90%', BOLD(80), 405, white, 255, x=1525); txt(C, 'IT LASTS', BOLD(54), 600, goldL, 255, x=1525); txt(C, 'CHANCE THE MONEY', BOLD(34), 665, white, 255, x=1525); fr = P2(fr, C, (1250, 240, 1800, 740), t, T[2])
    return frame(pill_last(fr, t, 'THE ASSUMPTIONS BEHIND 3.9%', 830, gold, navy, 50))

def s10b(t):
    fr = stage(t, 'THREE POINT NINE PERCENT OF $500,000', 55, 54); T = sp(5)
    fr = eq(fr, t, 230, [('c', 'YOUR SAVINGS', '$500,000', None, gold), ('o', '×'), ('c', 'THE RATE', '3.9%', None, blue), ('o', '='), ('c', 'EVERY YEAR', '$19,500', None, green)], [T[0], T[1], T[2]], 250, 400, 150)
    fr = eq(fr, t, 580, [('c', 'EVERY YEAR', '$19,500', None, green), ('o', '÷'), ('c', 'MONTHS', '12', None, blue), ('o', '='), ('c', 'EVERY MONTH', '$1,625', None, goldL)], [T[2] + 0.4, T[3], T[4]], 250, 400, 150)
    if t > T[4] + 0.3: fr = sparks(fr, t, (1360, 560, 1760, 820), 9, 13, T[4] + 0.3)
    return frame(fr if t < LASTP() - 0.05 else pill_pop(fr, 'WE WILL USE THIS NUMBER', 880, t, LASTP(), gold, tcol=navy, size=52, cx=960))

# ======================= BLOCCO 11 =======================
def s11a(t):
    fr = stage(t, 'FRANK AND MARY START HERE', 56); T = sp(3)
    for k, (nm, col, x0) in enumerate([('FRANK', blue, 110), ('MARY', pink, 1020)]):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([x0, 230, x0 + 790, 700], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            avatar(C, x0 + 150, 410, col, 2.6); txt(C, nm, BOLD(56), 540, col, 255, x=x0 + 150)
            paycheck(C, x0 + 300, 280, x0 + 760, 650, col, '$1,625', 'PER MONTH', 'FROM SAVINGS', 100); fr = P2(fr, C, (x0 - 20, 210, x0 + 810, 720), t, T[k])
    return frame(pill_last(fr, t, 'ABOUT $1,625 A MONTH EACH, FROM SAVINGS', 800, gold, navy, 50))

def s11b(t):
    fr = stage(t, 'WHAT THAT NUMBER IS NOT', 57); T = sp(3)
    for k, (h, sub, ic, x0) in enumerate([('THE BALANCE', 'NOT THE SAVINGS TOTAL', 'bag', 140), ('A PAYCHECK', 'NOT GUARANTEED', 'chk', 1000)]):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([x0, 250, x0 + 780, 700], radius=34, fill=card + (255,), outline=red + (255,), width=6)
            if ic == 'bag': money_bag(C, x0 + 390, 430, 1.35)
            else: paycheck(C, x0 + 170, 270, x0 + 610, 550, blue, '$1,625', 'PER MONTH', 'PAYCHECK', 66)
            txt(C, h, BOLD(54), 585, white, 255, x=x0 + 390); txt(C, sub, BOLD(38), 648, grey, 255, x=x0 + 390)
            cross(C, x0 + 690, 330, 52, red); fr = P2(fr, C, (x0 - 20, 230, x0 + 800, 720), t, T[k])
    return frame(pill_last(fr, t, 'NOT THE BALANCE. NOT A GUARANTEED PAYCHECK.', 810, red, (255, 255, 255), 46))

def s11c(t):
    fr = stage(t, 'A STARTING WITHDRAWAL', 58); T = sp(4)
    if t > T[0]:
        C = new(); card_(C, 130, 280, 700, 640, gold, 'STARTING WITHDRAWAL', '$1,625', 'THE FIRST MONTH', 110, goldL); fr = P2(fr, C, (110, 260, 720, 660), t, T[0])
    if t > T[1]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([820, 250, 1800, 680], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        pts = [(900, 580), (1020, 470), (1110, 530), (1230, 400), (1330, 470), (1420, 340), (1520, 450), (1610, 380), (1720, 330)]
        prog = ease((t - T[1]) / 1.2); n = max(2, int(len(pts) * prog))
        d.line(pts[:n], fill=green + (255,), width=12, joint='curve'); txt(C, 'THE MARKET', BOLD(48), 275, white, 255, x=1310)
        fr = P2(fr, C, (800, 230, 1820, 700), t, T[1])
    if t > T[2]:
        L = new(); arrow_r(L, 720, 820, 460, goldL, 255 * E_(t, T[2])); txt(L, 'DECIDES', BOLD(40), 720, goldL, 255 * E_(t, T[2]), x=1310); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'CAN THE BALANCE KEEP SUPPORTING IT?', 830, gold, navy, 50))

def s11d(t):
    fr = stage(t, 'WE COME BACK TO THIS', 59); T = sp(3)
    fr = numcard(fr, t, T[0], 560, 210, 1360, 760, 4, 'WHAT HAPPENS TO', 'THAT INCOME', 'OVER THE NEXT 25 YEARS', ic_time, green) if t > T[0] else fr
    return frame(pill_last(tracker(fr, t, {4}, T[1]), t, 'WE WILL COME BACK TO THAT IN NUMBER FOUR', 800, green, navy, 44))

# ======================= BLOCCO 12 =======================
def s12a(t):
    fr = stage(t, 'NUMBER TWO: SOCIAL SECURITY', 60); T = sp(3)
    fr = numcard(fr, t, T[0], 140, 190, 900, 800, 2, 'SOCIAL', 'SECURITY', 'THE SECOND NUMBER', ic_ss, blue) if t > T[0] else fr
    if t > T[1]:
        C = new(); paycheck(C, 1060, 260, 1770, 690, blue, '$2,071', 'PER MONTH', 'AVERAGE RETIRED WORKER', 150); fr = P2(fr, C, (1040, 240, 1790, 710), t, T[1])
        L = new(); arrow_r(L, 920, 1040, 480, goldL, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L)
    fr = tracker(fr, t, {2}, 0.3, 965)
    return frame(pill_last(fr, t, 'THE AVERAGE CHECK: $2,071 A MONTH', 818, blue, navy, 42))

def s12b(t):
    fr = stage(t, 'SOCIAL SECURITY FOR A WHOLE YEAR', 61, 58); T = sp(3)
    fr = eq(fr, t, 300, [('c', 'EVERY MONTH', '$2,071', None, blue), ('o', '×'), ('c', 'MONTHS', '12', 'IN A YEAR', gold), ('o', '='), ('c', 'EVERY YEAR', '$24,852', None, green)], [T[0], T[1], T[2]], 260, 420, 150)
    fr = chip_src(fr, 'SOURCE: SSA.GOV', 640, t, T[1] + 0.3)
    return frame(pill_last(tracker(fr, t, {2}, 0.3), t, 'ABOUT $24,852 A YEAR FROM SOCIAL SECURITY', 760, blue, navy, 46))

def s12c(t):
    fr = stage(t, 'ADD THE SAVINGS WITHDRAWALS', 62); T = sp(3)
    fr = eq(fr, t, 290, [('c', 'FROM SAVINGS', '$19,500', 'A YEAR', gold), ('o', '+'), ('c', 'SOCIAL SECURITY', '$24,852', 'A YEAR', blue), ('o', '='), ('c', 'EACH, PER YEAR', '$44,352', 'BEFORE TAXES', green)], [T[0], T[1], T[2]], 270, 420, 150)
    fr = tracker(fr, t, {1, 2}, 0.3)
    return frame(pill_last(fr, t, 'ABOUT $44,352 A YEAR BEFORE TAXES', 740, green, navy, 50))

# ======================= BLOCCO 13 =======================
def s13a(t):
    fr = stage(t, 'THE SAME INCOME, MONTH BY MONTH', 63, 58); T = sp(3)
    fr = eq(fr, t, 300, [('c', 'EVERY YEAR', '$44,352', 'BEFORE TAXES', green), ('o', '÷'), ('c', 'MONTHS', '12', None, gold), ('o', '='), ('c', 'EVERY MONTH', '$3,696', 'ABOUT', goldL)], [T[0], T[1], T[2]], 260, 420, 150)
    return frame(pill_last(fr, t, 'ABOUT $3,696 A MONTH BEFORE TAXES', 640, green, navy, 52))

def s13b(t):
    fr = stage(t, 'ON PAPER... BUT THERE IS A CATCH', 64, 58); T = sp(4)
    if t > T[0]:
        C = new(); paycheck(C, 130, 260, 760, 640, green, '$3,696', 'PER MONTH', 'ON PAPER', 130); check(C, 700, 280, 46, green); fr = P2(fr, C, (110, 240, 780, 660), t, T[0])
    if t > T[1]:
        L = new(); arrow_r(L, 790, 930, 450, goldL, 255 * E_(t, T[1] - 0.2)); txt(L, 'BUT...', BOLD(60), 330, red, 255 * E_(t, T[1]), x=860); fr = Image.alpha_composite(fr, L)
    if t > T[2]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([960, 260, 1780, 680], radius=34, fill=card + (255,), outline=red + (255,), width=6)
        ic_med(C, 1270, 400); txt(C, 'THE MEDICARE BILL', BOLD(58), 505, white, 255, x=1370); txt(C, 'COMES FIRST', BOLD(52), 580, red, 255, x=1370); fr = P2(fr, C, (940, 240, 1800, 700), t, T[2])
    return frame(pill_last(fr, t, 'THERE IS A CATCH, AND IT STARTS WITH MEDICARE', 800, red, (255, 255, 255), 46))

# ======================= BLOCCO 14 =======================
def s14a(t):
    fr = stage(t, 'NUMBER THREE: AFTER MEDICARE AND TAXES', 65, 54); T = sp(3)
    fr = numcard(fr, t, T[0], 140, 190, 900, 800, 3, 'MEDICARE', 'AND TAXES', 'WHAT ARRIVES AFTER THEM', ic_med, red) if t > T[0] else fr
    if t > T[1]:
        C = new(); card_(C, 1020, 280, 1780, 700, red, 'START WITH', 'PART B', 'DOCTOR VISITS, OUTPATIENT CARE', 120, white); fr = P2(fr, C, (1000, 260, 1800, 720), t, T[1])
    fr = tracker(fr, t, {3}, 0.3, 965)
    return frame(pill_last(fr, t, 'START WITH MEDICARE PART B', 818, red, (255, 255, 255), 42))

def s14b(t):
    fr = stage(t, 'THE 2026 STANDARD PREMIUM', 66); T = sp(3)
    if t > T[0]:
        C = new(); card_(C, 460, 250, 1460, 640, red, 'MEDICARE PART B', '$202.90', 'EVERY MONTH, STANDARD PREMIUM 2026', 190, white)
        ic_med(C, 1670, 445); fr = P2(fr, C, (440, 230, 1800, 660), t, T[0])
    fr = tracker(fr, t, {3}, 0.3)
    fr = chip_src(fr, 'SOURCE: CMS.GOV, MEDICARE PART B 2026', 700, t, 0.45 * D())
    return frame(pill_last(fr, t, 'TAKEN STRAIGHT FROM THE SOCIAL SECURITY CHECK', 780, red, (255, 255, 255), 44))

def s14c(t):
    fr = stage(t, 'TAKEN FROM THE CHECK FIRST', 67); T = sp(4)
    if t > T[0]:
        C = new(); paycheck(C, 130, 260, 760, 650, blue, '$2,071', 'PER MONTH', 'SOCIAL SECURITY CHECK', 140); fr = P2(fr, C, (110, 240, 780, 670), t, T[0])
    if t > T[1]:
        C = new(); card_(C, 830, 530, 1090, 680, red, None, '-$202.90', None, 54, white); L = new(); arrow_r(L, 770, 1110, 455, red, 255 * E_(t, T[1] - 0.2)); fr = Image.alpha_composite(fr, L); fr = P2(fr, C, (810, 510, 1110, 700), t, T[1])
        fr = chip(fr, 'PART B', 960, 330, t, T[1] + 0.1, red, 40)
    if t > T[2]:
        C = new(); building(C, 1520, 450, 420, 330, blue); txt(C, 'YOUR BANK DEPOSIT', BOLD(50), 660, white, 255, x=1520); fr = P2(fr, C, (1250, 250, 1800, 720), t, T[2])
    fr = tracker(fr, t, {3}, 0.3, 965)
    return frame(pill_last(fr, t, 'TAKEN OUT BEFORE THE DEPOSIT', 800, red, (255, 255, 255), 44))

# ======================= BLOCCO 15 =======================
def s15a(t):
    fr = stage(t, 'WHAT YOU REALLY RECEIVE', 68); T = sp(4)
    fr = eq(fr, t, 230, [('c', 'SOCIAL SECURITY', '$2,071', 'THE CHECK', blue), ('o', '−'), ('c', 'MEDICARE PART B', '$202.90', 'A MONTH', red), ('o', '='), ('c', 'YOU RECEIVE', '$1,868.10', 'EVERY MONTH', green)], [T[0], T[1], T[2]], 270, 420, 150)
    if t > T[3]:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([330, 560, 1590, 850], radius=36, fill=card + (255,), outline=green + (255,), width=6)
        avatar(C, 420, 715, blue, 1.4); avatar(C, 520, 715, pink, 1.4); building(C, 1480, 700, 200, 150, blue)
        txt(C, 'IN THE BANK EVERY MONTH', BOLD(44), 595, white, 255, x=960); txt(C, '$1,868.10', BOLD(110), 670, green, 255, x=960)
        L = new(); arrow_r(L, 1250, 1320, 745, goldL, 255); C.alpha_composite(L)
        fr = P2(fr, C, (310, 540, 1610, 850), t, T[3])
    return frame(fr)

def s15b(t):
    fr = stage(t, 'PART B FOR A WHOLE YEAR', 69); T = sp(3)
    fr = eq(fr, t, 230, [('c', 'PART B', '$202.90', 'A MONTH', red), ('o', '×'), ('c', 'MONTHS', '12', 'IN A YEAR', gold), ('o', '='), ('c', 'PART B ALONE', '$2,434.80', 'A YEAR', red)], [T[0], T[1], T[2]], 270, 420, 150)
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    for k, m in enumerate(months):
        t0 = T[0] + (T[2] - T[0]) * k / 12
        if t > t0:
            C = new(); d = ImageDraw.Draw(C); x0 = 130 + k * 140
            d.rounded_rectangle([x0, 580, x0 + 120, 720], radius=18, fill=card + (255,), outline=red + (255,), width=4); txt(C, m, BOLD(32), 592, white, 255, x=x0 + 60); txt(C, '-$203', BOLD(30), 650, red, 255, x=x0 + 60)
            fr = A_(fr, C, (x0 - 10, 570, x0 + 130, 730), t, t0, 0.3)
    return frame(pill_last(fr, t, 'PART B ALONE COSTS $2,434.80 A YEAR', 780, red, (255, 255, 255), 50))

def s15c(t):
    fr = stage(t, 'AND PART B IS ONLY THE BEGINNING', 70, 56); T = sp(4)
    labs = [('PART B', 'PREMIUM', red), ('DRUG', 'COVERAGE', blue), ('OUT-OF-POCKET', 'COSTS', gold)]
    for k, (a, b2, col) in enumerate(labs):
        if t > T[k]:
            C = new(); d = ImageDraw.Draw(C); x0 = 170 + k * 560; d.rounded_rectangle([x0, 280, x0 + 500, 620], radius=34, fill=card + (255,), outline=col + (255,), width=6)
            if k == 0: ic_med(C, x0 + 260, 400)
            elif k == 1: d.rounded_rectangle([x0 + 200, 350, x0 + 320, 450], radius=40, fill=col + (255,)); d.line([x0 + 260, 350, x0 + 260, 450], fill=white + (255,), width=6)
            else: wallet(C, x0 + 260, 405, 1.1)
            txt(C, a, fit(a, 480, 52), 490, white, 255, x=x0 + 250); txt(C, b2, BOLD(52), 550, col, 255, x=x0 + 250); fr = P2(fr, C, (x0 - 20, 260, x0 + 520, 640), t, T[k])
    return frame(pill_last(fr, t, 'MEDICARE IS MORE THAN ONE BILL', 800, red, (255, 255, 255), 52))

SLIDES = {6: [s6a, s6b, s6c], 7: [s7a, s7b, s7c], 8: [s8a, s8b, s8c, s8d], 9: [s9a, s9b, s9c], 10: [s10a, s10b],
          11: [s11a, s11b, s11c, s11d], 12: [s12a, s12b, s12c], 13: [s13a, s13b], 14: [s14a, s14b, s14c], 15: [s15a, s15b, s15c]}

if __name__ == '__main__':
    mode = sys.argv[1]; blk = int(sys.argv[2]); sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
    OUT = '/tmp/claude-0/-home-user-Tr/ca75d3ba-ecb8-59f6-9dcd-864234e0ec2e/scratchpad/w7/out/'
    for i, (fn, f) in enumerate(zip(SLIDES[blk], SPEC[blk]), 1):
        if sel and i not in sel: continue
        CUR['D'] = f / 30
        if mode == 'preview':
            for fq in [0.25, 0.5, 0.78, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((960, 540)).save(f'{OUT}pv{blk}_{i}_{int(fq*100)}.png')
        else:
            render_fast(fn, f, f'{OUT}v7-b{blk}-0{i}.mp4'); print('done', blk, i, f, flush=True)
    if mode == 'preview': print(blk, SPEC[blk], sum(SPEC[blk]))
