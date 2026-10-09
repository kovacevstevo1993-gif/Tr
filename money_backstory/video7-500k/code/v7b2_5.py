from v3lib import *
from v3b3_10 import POP, new, lerp, person_box
from v4b11_20 import calculator
from v5b1 import amb, sparks, shake, tile
from v5lib import arrow_r, arrow_d, paycheck, magnifier
from v6b1 import A_, E_, chip_src
from v6b2 import chip, logo
import sys, math

# ---- durate (fotogrammi) dalla timeline dell'utente, copione a 53 blocchi ----
DUR = {2: 399, 3: 518, 4: 424, 5: 785}
SENT = {
 2: ["The average household led by someone over sixty five spends about five thousand one hundred dollars a month.",
     "In the next few minutes, we do the exact math, and number four is the one that surprises almost everyone."],
 3: ["Welcome to The Money Backstory, where we explain retirement for Americans over fifty, using official numbers.",
     "To keep this simple, we will follow two retired neighbors, Frank and Mary.",
     "Both are sixty seven, both are single, and both have exactly five hundred thousand dollars saved."],
 4: ["Both also receive the average Social Security check, two thousand seventy one dollars a month.",
     "Frank keeps all his savings in a traditional four oh one k. Mary keeps half in a Roth account. Watch what happens to each of them."],
 5: ["Here is the plan. Five numbers that decide what five hundred thousand dollars really pays.",
     "One, how much your savings can safely pay each month. Two, what Social Security adds.",
     "Three, what Medicare and taxes take before you see the money. Four, what happens to that income over the next twenty five years.",
     "And five, four things that can change the answer. At the end, we put it all on one real budget."],
}
def split(b):
    g = [len(s) + 10 for s in SENT[b]]; fs = [round(w / sum(g) * DUR[b]) for w in g]; fs[-1] = DUR[b] - sum(fs[:-1]); return fs
FS = {b: split(b) for b in SENT}
def tm(sl, f): return f * FS_cur[sl] / 30     # istante a frazione f della slide (tutto entro 0.65)
FS_cur = {}

def tracker(fr, t, active, t0, y=960):
    """barra dei 5 numeri in basso: attivi in oro"""
    if t < t0: return fr
    C = new(); d = ImageDraw.Draw(C)
    for k in range(5):
        cx = 960 + (k - 2) * 150
        on = (k + 1) in active
        d.ellipse([cx - 40, y - 40, cx + 40, y + 40], fill=(gold if on else card) + (255,), outline=(goldL if on else grey) + (255,), width=4)
        txt(C, str(k + 1), BOLD(48), y - 30, navy if on else grey, 255, x=cx)
    return A_(fr, C, (960 - 360, y - 60, 960 + 360, y + 60), t, t0, 0.5)

def numcard(fr, t, t0, x0, y0, x1, y1, num, l1, l2, sub, icon, col=gold):
    if t < t0: return fr
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([x0, y0, x1, y1], radius=34, fill=card + (255,), outline=A(col, 255), width=6)
    cx = (x0 + x1) / 2
    d.ellipse([x0 + 30, y0 + 28, x0 + 110, y0 + 108], fill=A(col, 255)); txt(C, str(num), BOLD(60), y0 + 36, navy, 255, x=x0 + 70)
    icon(C, cx, y0 + 215)
    txt(C, l1, BOLD(54), y0 + 340, white, 255, x=cx)
    if l2: txt(C, l2, BOLD(54), y0 + 400, goldL, 255, x=cx)
    txt(C, sub, BOLD(36), y1 - 70, grey, 255, x=cx)
    return A_(fr, C, (x0 - 20, y0 - 20, x1 + 20, y1 + 20), t, t0)

# ---------------- BLOCCO 2 ----------------
def b2a(t):
    D = FS_cur[0] / 30
    fr = base(t); fr = amb(fr, t, 21, 7, 55); fr = title_layer(fr, 'THE AVERAGE HOUSEHOLD OVER 65 SPENDS', t, size=56)
    cats = [('HOUSING', lambda C, cx, cy: building(C, cx, cy - 30, 190, 170, gold)), ('FOOD', lambda C, cx, cy: cart(C, cx + 20, cy, 0.8, 255, green)),
            ('TRANSPORT', None), ('HEALTH CARE', None)]
    for k, (lab, ic) in enumerate(cats):
        t1 = 0.25 + 0.3 * k
        if t < t1: continue
        C = new(); d = ImageDraw.Draw(C); cx = 330 + k * 420 if False else 270 + k * 460
        d.rounded_rectangle([cx - 190, 200, cx + 190, 500], radius=30, fill=card + (255,), outline=goldL + (255,), width=4)
        cy = 330
        if lab == 'TRANSPORT':
            d.rounded_rectangle([cx - 85, cy - 25, cx + 85, cy + 30], radius=18, fill=A(blue, 255)); d.polygon([(cx - 50, cy - 25), (cx - 30, cy - 62), (cx + 30, cy - 62), (cx + 55, cy - 25)], fill=A(blue, 255))
            d.ellipse([cx - 70, cy + 12, cx - 30, cy + 52], fill=A(navy, 255), outline=A(white, 255), width=5); d.ellipse([cx + 30, cy + 12, cx + 70, cy + 52], fill=A(navy, 255), outline=A(white, 255), width=5)
        elif lab == 'HEALTH CARE':
            d.rounded_rectangle([cx - 55, cy - 55, cx + 55, cy + 55], radius=14, fill=A((236, 240, 245), 255), outline=A(red, 255), width=5)
            d.rectangle([cx - 10, cy - 36, cx + 10, cy + 36], fill=A(red, 255)); d.rectangle([cx - 36, cy - 10, cx + 36, cy + 10], fill=A(red, 255))
        else: ic(C, cx, cy)
        txt(C, lab, BOLD(44), 440, white, 255, x=cx)
        fr = A_(fr, C, (cx - 210, 180, cx + 210, 520), t, t1)
    t2 = tm(0, 0.38)
    if t > t2:
        v = 5119 * ease((t - t2) / 1.0)
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([430, 560, 1490, 830], radius=40, fill=card + (255,), outline=gold + (255,), width=6)
        txt(C, 'ABOUT', BOLD(44), 575, grey, 255, x=960); txt(C, '$' + f'{int(round(v, -2)):,}', BOLD(130), 625, goldL, 255, x=960)
        txt(C, 'A MONTH', BOLD(54), 765, white, 255, x=960)
        fr = A_(fr, C, (410, 540, 1510, 840), t, t2, 0.5)
    fr = chip_src(fr, '$61,432 A YEAR IN 2024  |  SOURCE: BUREAU OF LABOR STATISTICS', 900, t, tm(0, 0.55))
    return frame(fr)

def b2b(t):
    fr = base(t); fr = amb(fr, t, 22, 7, 55); fr = title_layer(fr, 'NOW THE EXACT MATH', t, size=64)
    t1 = 0.3
    if t > t1:
        C = new(); calculator(C, 400, 500, 2.0); txt(C, '$500,000', BOLD(40), 370, (20, 50, 30), 255, x=400)
        fr = A_(fr, C, (190, 250, 610, 780), t, t1)
    t2 = tm(1, 0.12)
    if t > t2:
        C = new(); magnifier(C, 780, 400, 60, goldL); txt(C, 'EXACT', BOLD(50), 520, goldL, 255, x=780); txt(C, 'NUMBERS', BOLD(50), 575, goldL, 255, x=780)
        fr = A_(fr, C, (660, 300, 920, 640), t, t2)
    t3 = tm(1, 0.30)
    tn = tm(1, 0.55)
    for k in range(5):
        st = t3 + 0.18 * k
        if t < st: continue
        hl = (k == 3 and t > tn)
        cx = 1090 + k * 150; cy = 470
        C = new(); d = ImageDraw.Draw(C); cx2 = cx + (shake(t, tn, 8, 0.6) if hl else 0)
        d.rounded_rectangle([cx2 - 62, cy - 90, cx2 + 62, cy + 90], radius=24, fill=A(red if hl else card, 255), outline=A(goldL if hl else (80, 100, 130), 255), width=6 if hl else 3)
        txt(C, ('?' if hl else str(k + 1)), BOLD(110 if hl else 90), cy - 62, white if hl else grey, 255, x=cx2)
        if hl: txt(C, '4', BOLD(44), cy + 38, goldL, 255, x=cx2)
        fr = POP(fr, C, (cx - 80, cy - 110, cx + 80, cy + 110), back((t - st) / 0.35))
    if t > tn: fr = sparks(fr, t, (1400, 380, 1560, 560), 8, 11, tn)
    fr = pill_pop(fr, 'NUMBER FOUR SURPRISES ALMOST EVERYONE', 830, t, tm(1, 0.5), red, size=50, cx=960)
    return frame(fr)

# ---------------- BLOCCO 3 ----------------
def b3a(t):
    fr = base(t); fr = amb(fr, t, 23, 7, 55)
    t1 = 0.3
    if t > t1:
        C = new(); logo(C, 480, 500, 190); fr = A_(fr, C, (250, 270, 710, 730), t, t1)
    t2 = tm(0, 0.18)
    if t > t2:
        C = new()
        txt(C, 'THE MONEY BACKSTORY', SER(68), 290, goldL, 255, x=1230)
        txt(C, 'RETIREMENT EXPLAINED', BOLD(60), 420, white, 255, x=1230); txt(C, 'FOR AMERICANS OVER 50', BOLD(60), 500, white, 255, x=1230)
        fr = A_(fr, C, (760, 250, 1700, 600), t, t2)
    t3 = tm(0, 0.40)
    if t > t3:
        for k, (lab, x) in enumerate([('SSA.GOV', 800), ('CMS.GOV', 1030), ('IRS.GOV', 1260), ('BLS.GOV', 1490)]):
            fr = chip(fr, lab, x, 660, t, t3 + 0.2 * k, goldL, 40)
        fr = pill_pop(fr, 'OFFICIAL NUMBERS ONLY', 800, t, t3 + 0.7, green, tcol=navy, size=54, cx=1230)
    return frame(fr)

def b3b(t):
    fr = base(t); fr = amb(fr, t, 24, 7, 55); fr = title_layer(fr, 'MEET OUR TWO RETIRED NEIGHBORS', t, size=60)
    fr = person_box(fr, 'FRANK', 560, 470, blue, t, 0.3, s=4.0)
    tf = tm(1, 0.35)
    if t > tf: fr = person_box(fr, 'MARY', 1360, 470, pink, t, tf, s=4.0)
    L = new(); txt(L, '&', BOLD(120), 440, goldL, 255 * E_(t, tf + 0.1), x=960); fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'WE FOLLOW THEM IN THIS VIDEO', 830, t, tm(1, 0.5), goldL, tcol=navy, size=54, cx=960)
    return frame(fr)

def b3c(t):
    fr = base(t); fr = amb(fr, t, 25, 7, 55); fr = title_layer(fr, 'SAME AGE, SAME SAVINGS', t, size=64)
    for k, (nm, col, cx) in enumerate([('FRANK', blue, 500), ('MARY', pink, 1420)]):
        t1 = 0.3 + 0.2 * k
        if t < t1: continue
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([cx - 400, 230, cx + 400, 690], radius=34, fill=card + (255,), outline=col + (255,), width=6)
        avatar(C, cx - 250, 400, col, 2.4); txt(C, nm, BOLD(54), 520, col, 255, x=cx - 250)
        d.ellipse([cx - 120, 280, cx + 20, 420], fill=gold + (255,)); txt(C, '67', BOLD(76), 308, navy, 255, x=cx - 50); txt(C, 'YEARS OLD', BOLD(26), 430, white, 255, x=cx - 50)
        money_bag(C, cx + 210, 400, 1.0)
        txt(C, '$500,000', BOLD(66), 540, goldL, 255, x=cx + 150); txt(C, 'SAVED', BOLD(44), 618, white, 255, x=cx + 150)
        fr = A_(fr, C, (cx - 420, 210, cx + 420, 710), t, t1)
    fr = pill_pop(fr, 'BOTH SINGLE', 760, t, tm(2, 0.30), goldL, tcol=navy, size=50, cx=960)
    fr = pill_pop(fr, 'BOTH HAVE EXACTLY $500,000', 880, t, tm(2, 0.50), green, tcol=navy, size=52, cx=960)
    return frame(fr)

# ---------------- BLOCCO 4 ----------------
def b4a(t):
    fr = base(t); fr = amb(fr, t, 26, 7, 55); fr = title_layer(fr, 'THE SAME SOCIAL SECURITY CHECK', t, size=60)
    t1 = 0.35
    if t > t1:
        C = new(); paycheck(C, 150, 280, 810, 640, blue, '$2,071', 'PER MONTH', 'FRANK: SOCIAL SECURITY', 140); fr = A_(fr, C, (130, 260, 830, 660), t, t1)
    t2 = tm(0, 0.35)
    if t > t2:
        C = new(); paycheck(C, 1110, 280, 1770, 640, pink, '$2,071', 'PER MONTH', 'MARY: SOCIAL SECURITY', 140); fr = A_(fr, C, (1090, 260, 1790, 660), t, t2)
        L = new(); txt(L, '=', BOLD(190), 380, goldL, 255 * E_(t, t2 + 0.3), x=960); fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'THE AVERAGE CHECK: $2,071 A MONTH', 770, t, tm(0, 0.55), green, tcol=navy, size=54, cx=960)
    fr = chip_src(fr, 'AVERAGE RETIRED WORKER CHECK, 2026: SSA.GOV', 920, t, tm(0, 0.6))
    return frame(fr)

def b4b(t):
    fr = base(t); fr = amb(fr, t, 27, 7, 55); fr = title_layer(fr, 'WHERE THEIR SAVINGS SIT', t, size=64)
    t1 = 0.3
    if t > t1:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([140, 240, 900, 700], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        avatar(C, 290, 400, blue, 2.4); txt(C, 'FRANK', BOLD(56), 520, blue, 255, x=290)
        d.rounded_rectangle([430, 300, 870, 520], radius=22, fill=A((60, 90, 140), 255), outline=goldL + (255,), width=4)
        txt(C, 'TRADITIONAL', BOLD(42), 322, white, 255, x=650); txt(C, '401(k)', BOLD(70), 378, goldL, 255, x=650); txt(C, '$500,000', BOLD(56), 458, white, 255, x=650)
        txt(C, 'ALL OF HIS SAVINGS', BOLD(38), 620, grey, 255, x=520)
        fr = A_(fr, C, (120, 220, 920, 720), t, t1)
    t2 = tm(1, 0.34)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([1020, 240, 1780, 700], radius=34, fill=card + (255,), outline=pink + (255,), width=6)
        avatar(C, 1170, 400, pink, 2.4); txt(C, 'MARY', BOLD(56), 520, pink, 255, x=1170)
        d.rounded_rectangle([1310, 290, 1750, 400], radius=18, fill=A((50, 130, 90), 255), outline=goldL + (255,), width=4)
        txt(C, 'ROTH', BOLD(36), 298, white, 255, x=1530); txt(C, '$250,000', BOLD(56), 335, goldL, 255, x=1530)
        d.rounded_rectangle([1310, 415, 1750, 525], radius=18, fill=A((60, 90, 140), 255), outline=grey + (255,), width=4)
        txt(C, 'TRADITIONAL', BOLD(36), 423, white, 255, x=1530); txt(C, '$250,000', BOLD(56), 460, white, 255, x=1530)
        txt(C, 'HALF IN A ROTH ACCOUNT', BOLD(38), 620, grey, 255, x=1400)
        fr = A_(fr, C, (1000, 220, 1800, 720), t, t2)
    fr = pill_pop(fr, 'WATCH WHAT HAPPENS TO EACH OF THEM', 800, t, tm(1, 0.62), red, size=48, cx=960)
    return frame(fr)

# ---------------- BLOCCO 5 ----------------
def ic_coins(C, cx, cy): coin_stack(C, cx, cy + 50, 5, 56)
def ic_ss(C, cx, cy): building(C, cx, cy, 190, 150, gold)
def ic_med(C, cx, cy):
    d = ImageDraw.Draw(C); d.rounded_rectangle([cx - 140, cy - 55, cx - 30, cy + 55], radius=14, fill=A((236, 240, 245), 255), outline=A(red, 255), width=5)
    d.rectangle([cx - 94, cy - 36, cx - 76, cy + 36], fill=A(red, 255)); d.rectangle([cx - 122, cy - 9, cx - 48, cy + 9], fill=A(red, 255))
    tax_form(C, cx + 10, cy - 62, 100, 124, 255, 'TAX')
def ic_time(C, cx, cy): clock(C, cx, cy, 62, 1.5, goldL)
def ic_levers(C, cx, cy):
    d = ImageDraw.Draw(C)
    for k, p in enumerate([0.3, 0.7, 0.45, 0.8]):
        x = cx - 90 + k * 60; d.rounded_rectangle([x - 8, cy - 60, x + 8, cy + 60], radius=8, fill=A((80, 100, 130), 255))
        y = cy - 52 + p * 104; d.ellipse([x - 22, y - 16, x + 22, y + 16], fill=A(goldL, 255), outline=A(gold, 255), width=3)

def b5a(t):
    fr = base(t); fr = amb(fr, t, 28, 7, 55); fr = title_layer(fr, 'THE PLAN: FIVE NUMBERS', t, size=64)
    t1 = 0.3
    if t > t1:
        C = new(); money_bag(C, 460, 480, 1.7); coin_stack(C, 230, 640, 6, 66); coin_stack(C, 690, 640, 8, 66)
        fr = A_(fr, C, (110, 260, 820, 760), t, t1)
    t2 = tm(0, 0.40)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([900, 330, 1800, 640], radius=40, fill=card + (255,), outline=goldL + (255,), width=6)
        txt(C, '$500,000', BOLD(120), 360, goldL, 255, x=1350); txt(C, 'WHAT DOES IT REALLY PAY?', BOLD(56), 520, white, 255, x=1350)
        fr = A_(fr, C, (880, 310, 1820, 660), t, t2)
    fr = tracker(fr, t, set(), tm(0, 0.5))
    fr = pill_pop(fr, 'FIVE NUMBERS DECIDE THE ANSWER', 780, t, tm(0, 0.55), gold, tcol=navy, size=50, cx=960)
    return frame(fr)

def b5b(t):
    fr = base(t); fr = amb(fr, t, 29, 7, 55); fr = title_layer(fr, 'NUMBERS ONE AND TWO', t, size=64)
    fr = numcard(fr, t, 0.3, 140, 190, 900, 800, 1, 'SAFE MONTHLY', 'WITHDRAWAL', 'WHAT YOUR SAVINGS CAN PAY', ic_coins, gold)
    fr = numcard(fr, t, tm(1, 0.35), 1020, 190, 1780, 800, 2, 'SOCIAL', 'SECURITY', 'WHAT IT ADDS EVERY MONTH', ic_ss, blue)
    if t > tm(1, 0.35) + 0.2:
        L = new(); txt(L, '+', BOLD(160), 420, goldL, 255 * E_(t, tm(1, 0.35) + 0.2), x=960); fr = Image.alpha_composite(fr, L)
    fr = tracker(fr, t, {1, 2}, 0.5)
    return frame(fr)

def b5c(t):
    fr = base(t); fr = amb(fr, t, 30, 7, 55); fr = title_layer(fr, 'NUMBERS THREE AND FOUR', t, size=64)
    fr = numcard(fr, t, 0.3, 140, 190, 900, 800, 3, 'MEDICARE', 'AND TAXES', 'TAKEN BEFORE YOU SEE THE MONEY', ic_med, red)
    fr = numcard(fr, t, tm(2, 0.40), 1020, 190, 1780, 800, 4, 'THE NEXT', '25 YEARS', 'WHAT HAPPENS TO THAT INCOME', ic_time, green)
    fr = tracker(fr, t, {3, 4}, 0.5)
    return frame(fr)

def b5d(t):
    fr = base(t); fr = amb(fr, t, 31, 7, 55); fr = title_layer(fr, 'NUMBER FIVE, AND THE FINAL BUDGET', t, size=60)
    fr = numcard(fr, t, 0.3, 140, 190, 900, 800, 5, 'FOUR THINGS THAT', 'CHANGE THE ANSWER', 'WE TEST EACH ONE', ic_levers, purple)
    t2 = tm(3, 0.38)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([1020, 190, 1780, 800], radius=34, fill=(236, 240, 245, 255), outline=goldL + (255,), width=6)
        d.rounded_rectangle([1020, 190, 1780, 290], radius=34, fill=gold + (255,)); d.rectangle([1020, 250, 1780, 290], fill=gold + (255,))
        txt(C, 'ONE REAL BUDGET', BOLD(54), 212, navy, 255, x=1400)
        for k, lab in enumerate(['SAVINGS', 'SOCIAL SECURITY', 'MEDICARE + TAXES', 'WHAT IS LEFT']):
            y = 330 + k * 105; d.line([1080, y + 62, 1720, y + 62], fill=(170, 180, 200, 255), width=3)
            txt(C, lab, BOLD(40), y, (50, 64, 90), 255, x=1090, anchor='l'); txt(C, '$ ?', BOLD(40), y, red if k == 3 else (50, 64, 90), 255, x=1710, anchor='r')
        fr = A_(fr, C, (1000, 170, 1800, 820), t, t2)
    fr = tracker(fr, t, {5}, 0.5)
    return frame(fr)

SLIDES = {2: [b2a, b2b], 3: [b3a, b3b, b3c], 4: [b4a, b4b], 5: [b5a, b5b, b5c, b5d]}

if __name__ == '__main__':
    mode = sys.argv[1]; blk = int(sys.argv[2]); sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
    OUT = '/tmp/claude-0/-home-user-Tr/ca75d3ba-ecb8-59f6-9dcd-864234e0ec2e/scratchpad/w7/out/'
    FS_cur.update({i: f for i, f in enumerate(FS[blk])})
    for i, (fn, f) in enumerate(zip(SLIDES[blk], FS[blk]), 1):
        if sel and i not in sel: continue
        if mode == 'preview':
            for fq in [0.3, 0.55, 0.8, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((960, 540)).save(f'{OUT}pv{blk}_{i}_{int(fq*100)}.png')
        else:
            render_fast(fn, f, f'{OUT}v7-b{blk}-0{i}.mp4'); print('done', blk, i, f, flush=True)
    if mode == 'preview': print(blk, FS[blk], sum(FS[blk]))
