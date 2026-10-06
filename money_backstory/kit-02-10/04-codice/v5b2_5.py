from v5lib import *

LOGO_SRC = Image.open('/home/claude/kit1/KIT-MONEY-BACKSTORY-COMPLETO-28-09/04-immagini/logo/logo-the-money-backstory-pro2.png').convert('RGBA')
_m = Image.new('L', (1024, 1024), 0); ImageDraw.Draw(_m).ellipse([50, 50, 974, 974], fill=255); LOGO_SRC.putalpha(_m)
LOGO = LOGO_SRC.resize((370, 370), Image.LANCZOS)

# ======================= BLOCK 2 =======================
S2 = ["Welcome to The Money Backstory, where we explain retirement for Americans over fifty, using official numbers.",
      "To keep this simple, we will follow two coworkers, Frank and Mary.",
      "They earned exactly the same wages.",
      "The only difference is that Frank stopped working after thirty years, and Mary kept going for thirty five.",
      "Watch what happens to their checks."]
B2 = Blk(2, S2, [[0], [1, 2], [3, 4]])

def b2a(t):
    T = lambda m: B2.tt(0, m)
    fr = base(t)
    C = new(); C.alpha_composite(LOGO, (960 - 185, 130)); fr = appear(fr, C, (760, 110, 1160, 520), t, 0.3, 1.0)
    L = new(); txt(L, 'THE MONEY BACKSTORY', SER(84), 535, goldL, 255 * E(t, 1.0), x=960); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'RETIREMENT EXPLAINED FOR AMERICANS OVER 50', 650, 52, white, t, T('where we explain'))
    fr = label(fr, 'USING OFFICIAL NUMBERS FROM', 750, 42, grey, t, T('using official') - 0.3)
    for k, (nm, col) in enumerate([('SSA.GOV', goldL), ('MEDICARE.GOV', blue), ('IRS.GOV', green)]):
        fr = chip(fr, nm, 480 + k * 480, 815, t, T('using official') + 0.1 + k * 0.4, col, 46)
    return frame(fr)

def b2b(t):
    T = lambda m: B2.tt(1, m)
    fr = base(t); fr = title(fr, 'MEET FRANK AND MARY', t)
    tf = T('Frank and Mary'); tsw = T('same wages')
    for nm, cx, col, t0 in [('FRANK', 520, blue, 0.4), ('MARY', 1400, green, tf + 0.6)]:
        C = new(); person(C, cx, 500, col, 3.4); txt(C, nm, BOLD(62), 690, col, 255, x=cx)
        fr = appear(fr, C, (cx - 200, 290, cx + 200, 770), t, t0, 1.0)
    if t > tsw:
        fr = label(fr, '=', 400, 200, goldL, t, tsw, 960)
        fr = label(fr, 'SAME WAGES', 830, 60, goldL, t, tsw + 0.3, 960)
        for cx in (520, 1400):
            C = new(); bill(C, cx - 60, 880, 240, 116, 4); bill(C, cx + 60, 870, 240, 116, -4)
            fr = appear(fr, C, (cx - 220, 780, cx + 220, 960), t, tsw + 0.2, 1.0)
    return frame(fr)

def b2c(t):
    T = lambda m: B2.tt(2, m)
    fr = base(t); fr = title(fr, 'WHAT IS DIFFERENT?', t)
    tf = T('Frank stopped'); tm = T('Mary kept going'); tw = T('Watch what')
    x0 = 520; ppy = 28
    for nm, y, yrs, col, t0, dur in [('FRANK', 250, 30, blue, tf, 2.6), ('MARY', 390, 35, green, tm, 2.8)]:
        L = new(); txt(L, nm, BOLD(58), y + 20, col, 255 * E(t, t0 - 0.2), x=140, anchor='l'); fr = Image.alpha_composite(fr, L)
        u = ease((t - t0) / dur)
        if u > 0:
            L = new(); d = ImageDraw.Draw(L); xe = x0 + yrs * ppy * u
            d.rounded_rectangle([x0, y, xe, y + 100], radius=26, fill=A(col, 255))
            if u > 0.95: txt(L, f'{yrs} YEARS', BOLD(56), y + 20, navy, 255, x=(x0 + xe) / 2)
            fr = Image.alpha_composite(fr, L)
    if t > tm + 3.0:
        L = new(); d = ImageDraw.Draw(L); a = E(t, tm + 3.0, 0.8)
        xa = x0 + 30 * ppy; xb = x0 + 35 * ppy
        d.line([xa, 515, xb, 515], fill=A(red, 255 * a), width=8); d.line([xa, 500, xa, 530], fill=A(red, 255 * a), width=8); d.line([xb, 500, xb, 530], fill=A(red, 255 * a), width=8)
        txt(L, '5 YEARS', BOLD(50), 535, red, 255 * a, x=(xa + xb) / 2)
        fr = Image.alpha_composite(fr, L)
    for nm, cx, col, dt in [("FRANK'S CHECK", 520, blue, 0.0), ("MARY'S CHECK", 1400, green, 0.6)]:
        if t > tw + dt:
            C = new(); paycheck(C, cx - 300, 640, cx + 300, 930, col, '$ ?', sub='', head=nm, size=120)
            fr = appear(fr, C, (cx - 310, 630, cx + 310, 940), t, tw + dt, 0.9)
    return frame(fr)

# ======================= BLOCK 3 =======================
S3 = ["Here is the plan.", "You will learn the five things that decide your Social Security check.",
      "One, the thirty five year rule.", "Two, the formula that turns your salary into a monthly amount.",
      "Three, what your claiming age really does to that amount.", "Four, what happens if you keep working while you collect.",
      "And five, what your spouse can get.", "At the end, we will answer the question everybody asks: will the money still be there?"]
B3 = Blk(3, S3, [[0, 1], [2, 3], [4, 5], [6, 7]])

def plan_card(fr, t, t0, x0, num, col, lines, icon, y0=240, y1=860):
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([x0, y0, x0 + 800, y1], radius=36, fill=A(card, 255), outline=A(col, 255), width=6)
    d.ellipse([x0 + 40, y0 + 34, x0 + 150, y0 + 144], fill=A(col, 255)); txt(C, str(num), BOLD(80), y0 + 44, navy, 255, x=x0 + 95)
    icon(C, x0 + 400, y0 + 300)
    for i, ln in enumerate(lines):
        txt(C, ln, BOLD(60), y1 - 200 + i * 74 + (0 if len(lines) > 1 else 40), white, 255, x=x0 + 400)
    return appear(fr, C, (x0 - 10, y0 - 10, x0 + 810, y1 + 10), t, t0, 0.9)

def b3a(t):
    T = lambda m: B3.tt(0, m)
    fr = base(t); fr = title(fr, 'HERE IS THE PLAN', t, 64)
    C = new(); ss_card(C, 640, 560, 1.9); fr = appear(fr, C, (300, 350, 980, 780), t, 0.5, 1.0)
    L = new(); txt(L, '5', BOLD(430), 250, goldL, 255 * E(t, T('the five things'), 0.9), x=1390); fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'THINGS THAT DECIDE', 700, 60, white, t, T('decide'), 1390)
    fr = label(fr, 'YOUR CHECK', 775, 60, goldL, t, T('decide') + 0.3, 1390)
    return frame(fr)

def b3b(t):
    T = lambda m: B3.tt(1, m)
    fr = base(t); fr = title(fr, 'THE FIVE THINGS', t)
    fr = plan_card(fr, t, T('One'), 110, 1, gold, ['THE 35 YEAR RULE'], lambda C, cx, cy: tile(C, cx - 100, cy - 100, 200, gold, '35'))
    fr = plan_card(fr, t, T('Two'), 1010, 2, blue, ['THE FORMULA'], lambda C, cx, cy: calculator(C, cx, cy, 1.3))
    return frame(fr)

def b3c(t):
    T = lambda m: B3.tt(2, m)
    fr = base(t); fr = title(fr, 'THE FIVE THINGS', t)
    fr = plan_card(fr, t, T('Three'), 110, 3, purple, ['CLAIMING AGE'], lambda C, cx, cy: clock(C, cx, cy, 120, 3.0, goldL))
    def wk(C, cx, cy):
        briefcase(C, cx, cy, 2.6)
    fr = plan_card(fr, t, T('Four'), 1010, 4, red, ['WORKING WHILE', 'YOU COLLECT'], wk)
    return frame(fr)

def b3d(t):
    T = lambda m: B3.tt(3, m)
    fr = base(t); fr = title(fr, 'THE FIVE THINGS', t)
    def sp(C, cx, cy):
        person(C, cx - 80, cy + 20, blue, 2.4); person(C, cx + 80, cy + 20, pink, 2.4)
    fr = plan_card(fr, t, 0.3, 110, 5, green, ['YOUR SPOUSE'], sp)
    ta = T('At the end')
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([1010, 240, 1810, 860], radius=36, fill=A(card, 255), outline=A(red, 255), width=6)
    building(C, 1410, 470, 380, 300, gold)
    txt(C, '?', BOLD(200), 380, red, 255, x=1410)
    txt(C, 'WILL THE MONEY', BOLD(58), 660, white, 255, x=1410); txt(C, 'STILL BE THERE?', BOLD(58), 735, goldL, 255, x=1410)
    fr = appear(fr, C, (1000, 230, 1820, 870), t, ta, 1.0)
    return frame(fr)

# ======================= BLOCK 4 =======================
S4 = ["Number one: the thirty five year rule.",
      "To qualify for retirement benefits, you need forty credits, which usually means about ten years of work.",
      "But the size of your check depends on something else.",
      "The Social Security Administration adjusts your old salaries to today's wage levels, and then picks your highest thirty five years.",
      "Your last salary does not matter.", "Your best thirty five years do."]
B4 = Blk(4, S4, [[0, 1], [2], [3], [4, 5]])

def b4a(t):
    T = lambda m: B4.tt(0, m)
    fr = base(t); fr = title(fr, 'NUMBER ONE: THE 35 YEAR RULE', t, 54)
    tc = T('you need forty credits')
    L = new(); tile(L, 830, 330, 260, gold, '35'); txt(L, 'YEARS', BOLD(60), 620, goldL, 255, x=960); fr = appear(fr, L, (810, 310, 1110, 700), t, 0.3, 0.9) if t < tc else fr
    fr = label(fr, '40 CREDITS', 240, 64, goldL, t, tc, 510)
    for i in range(40):
        st = tc + 0.2 + i * 0.07
        if t < st: continue
        x = 170 + (i % 8) * 84; y = 340 + (i // 8) * 84
        C = new(); tile(C, x, y, 70, gold); fr = appear(fr, C, (x - 6, y - 6, x + 76, y + 82), t, st, 0.4)
    ty = T('about ten years')
    fr = label(fr, '=', 470, 170, goldL, t, ty, 1000)
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([1120, 290, 1700, 780], radius=32, fill=(236, 240, 245, 255)); d.rounded_rectangle([1120, 290, 1700, 380], radius=32, fill=A(blue, 255)); d.rectangle([1120, 350, 1700, 380], fill=A(blue, 255))
    txt(C, 'ABOUT', BOLD(50), 306, (255, 255, 255), 255, x=1410); txt(C, '10', BOLD(270), 395, navy, 255, x=1410); txt(C, 'YEARS OF WORK', BOLD(48), 700, (70, 84, 108), 255, x=1410)
    fr = appear(fr, C, (1110, 280, 1710, 790), t, ty, 1.0)
    return frame(fr)

def b4b(t):
    T = lambda m: B4.tt(1, m)
    fr = base(t); fr = title(fr, 'HOW BIG IS YOUR CHECK?', t)
    C = new(); paycheck(C, 560, 260, 1360, 640, blue, '$ ?', sub='PER MONTH', head='SOCIAL SECURITY CHECK', size=170)
    fr = appear(fr, C, (550, 250, 1370, 650), t, 0.4, 0.9)
    fr = chip(fr, 'IT DEPENDS ON SOMETHING ELSE', 960, 740, t, T('depends'), gold, 50)
    return frame(fr)

import random as _r
_rnd = _r.Random(11)
DIP = {4, 11, 17, 26, 33}
H0 = [ 1.5 * (70 + i * 3.4) * _rnd.uniform(0.85, 1.1) for i in range(40)]
H1 = [ 1.5 * (250 + i * 1.4 + _rnd.uniform(-18, 18)) * (0.5 if i in DIP else 1.0) for i in range(40)]

def b4c(t):
    T = lambda m: B4.tt(2, m)
    fr = base(t)
    t2 = T("to today's wage levels"); t3 = T('picks your highest')
    cap = 'YOUR OLD SALARIES' if t < t2 else ("ADJUSTED TO TODAY'S WAGES" if t < t3 else 'ONLY THE HIGHEST 35 YEARS COUNT')
    colc = white if t < t2 else (goldL if t < t3 else green)
    fr = title(fr, 'YOUR EARNINGS, YEAR BY YEAR', t, 54)
    L = new(); txt(L, cap, BOLD(58), 200, colc, 255, x=960); fr = Image.alpha_composite(fr, L)
    L = new(); d = ImageDraw.Draw(L); base_y = 850; x0 = 130
    d.line([100, base_y, 1820, base_y], fill=A(gold, 255), width=4)
    u2 = ease((t - t2) / 2.2); u3 = ease((t - t3) / 1.0)
    for i in range(40):
        st = 0.3 + i * 0.03
        g = ease((t - st) / 0.6)
        if g <= 0: continue
        h = (H0[i] + (H1[i] - H0[i]) * u2) * g * 1.0
        col0 = (96, 128, 176); col1 = gold
        col = tuple(int(col0[k] + (col1[k] - col0[k]) * u2) for k in range(3))
        if i in DIP:
            col = tuple(int(col[k] + ((90, 96, 110)[k] - col[k]) * u3) for k in range(3))
        x = x0 + i * 42
        d.rounded_rectangle([x, base_y - h, x + 30, base_y], radius=8, fill=A(col, 255))
        if i in DIP and u3 > 0.5:
            d.line([x - 2, base_y - h - 52, x + 32, base_y - h - 18], fill=A(red, 255), width=8); d.line([x + 32, base_y - h - 52, x - 2, base_y - h - 18], fill=A(red, 255), width=8)
    if t > t3:
        a = E(t, t3 + 0.6, 0.8)
        d.rounded_rectangle([120, 300, 1810, 306], radius=3, fill=A(green, 255 * a))
        txt(L, '35 BEST YEARS', BOLD(46), 314, green, 255 * a, x=960)
    fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b4d(t):
    T = lambda m: B4.tt(3, m)
    fr = base(t); fr = title(fr, 'WHAT REALLY COUNTS?', t)
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([130, 250, 920, 850], radius=36, fill=A(card, 255), outline=A(red, 255), width=6)
    cross(C, 525, 470, 100, red)
    txt(C, 'YOUR LAST SALARY', BOLD(60), 640, white, 255, x=525); txt(C, 'DOES NOT MATTER', BOLD(52), 730, red, 255, x=525)
    fr = appear(fr, C, (120, 240, 930, 860), t, 0.4, 0.9)
    tb = T('Your best')
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([1000, 250, 1790, 850], radius=36, fill=A(card, 255), outline=A(green, 255), width=6)
    check(C, 1395, 470, 100, green)
    txt(C, 'YOUR BEST 35 YEARS', BOLD(60), 640, white, 255, x=1395); txt(C, 'DO MATTER', BOLD(52), 730, green, 255, x=1395)
    fr = appear(fr, C, (990, 240, 1800, 860), t, tb, 0.9)
    return frame(fr)

# ======================= BLOCK 5 =======================
S5 = ["Now here is the catch.", "If you have fewer than thirty five years of earnings, the missing years are counted as zero.",
      "Not skipped.", "Zero.", "Those zeros get averaged in with everything else, and they drag your monthly average down.",
      "Many people who stayed home to raise kids, care for a parent, or lost a job never realize this is happening."]
B5 = Blk(5, S5, [[0, 1], [2, 3, 4], [5]])
G5X, G5Y, G5S, G5P = 190, 250, 100, 114
def g5(i): return G5X + (i % 7) * G5P, G5Y + (i // 7) * G5P

def b5a(t):
    T = lambda m: B5.tt(0, m)
    fr = base(t); fr = title(fr, 'THE CATCH', t)
    tf = T('fewer than thirty five'); tz = T('counted as zero')
    for i in range(30):
        st = 0.3 + i * 0.07
        if t < st: continue
        x, y = g5(i); C = new(); tile(C, x, y, G5S, gold, str(i + 1)); fr = appear(fr, C, (x - 8, y - 8, x + G5S + 8, y + G5S + 16), t, st, 0.4)
    for k in range(5):
        x, y = g5(30 + k)
        if t > tz + k * 0.4:
            C = new(); tile(C, x, y, G5S, red, '0', fill=red, outline=(255, 150, 150)); fr = appear(fr, C, (x - 8, y - 8, x + G5S + 8, y + G5S + 16), t, tz + k * 0.4, 0.5)
        elif t > tf + k * 0.25:
            L = new(); d = ImageDraw.Draw(L); a = E(t, tf + k * 0.25, 0.5)
            d.rounded_rectangle([x, y, x + G5S, y + G5S], radius=14, outline=A(red, 255 * a), width=4, fill=A((60, 20, 30), 120 * a)); txt(L, '?', BOLD(60), y + 20, red, 255 * a, x=x + G5S / 2)
            fr = Image.alpha_composite(fr, L)
    fr = label(fr, 'FEWER THAN', 300, 62, white, t, tf, 1440); fr = label(fr, '35 YEARS?', 380, 96, goldL, t, tf + 0.3, 1440)
    fr = chip(fr, 'MISSING YEAR = ZERO', 1440, 600, t, tz + 0.3, red, 46, filled=red, tcol=(255, 255, 255))
    return frame(fr)

def b5b(t):
    T = lambda m: B5.tt(1, m)
    fr = base(t); fr = title(fr, 'NOT SKIPPED. ZERO.', t, 60)
    tz = T('Zero.'); ta = T('averaged in'); td = T('drag your')
    L = new(); txt(L, 'SKIPPED', BOLD(100), 240, grey, 150 * E(t, 0.3), x=530); fr = Image.alpha_composite(fr, L)
    L = new(); strike(L, 300, 760, 290, red, 255 * E(t, 0.9, 0.8), 12); fr = Image.alpha_composite(fr, L)
    L = new(); txt(L, '0', BOLD(470), 340, red, 255 * E(t, tz, 0.9), x=530); fr = Image.alpha_composite(fr, L)
    if t > ta:
        C = new(); d = ImageDraw.Draw(C)
        txt(C, 'YOUR MONTHLY AVERAGE', BOLD(52), 270, white, 255, x=1395)
        d.rounded_rectangle([1075, 360, 1715, 470], radius=30, fill=A(card, 255), outline=A(goldL, 255), width=5)
        fr = appear(fr, C, (1000, 250, 1790, 490), t, ta, 0.9)
        u = ease((t - td) / 2.4)
        L = new(); d = ImageDraw.Draw(L); wdt = 620 * (1 - 0.143 * u)
        d.rounded_rectangle([1085, 370, 1085 + wdt, 460], radius=24, fill=A(gold, 255))
        fr = Image.alpha_composite(fr, L)
        if t > td:
            L = new(); arrow_d(L, 1395, 520, 640, red, 255 * E(t, td + 0.6, 0.6)); txt(L, 'ZEROS DRAG IT DOWN', BOLD(54), 670, red, 255 * E(t, td + 0.8, 0.6), x=1395)
            fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b5c(t):
    T = lambda m: B5.tt(2, m)
    fr = base(t); fr = title(fr, 'WHO IS AFFECTED?', t)
    specs = [('RAISING KIDS', 'raise kids'), ('CARING FOR A PARENT', 'care for a parent'), ('LOSING A JOB', 'lost a job')]
    for k, (nm, mk) in enumerate(specs):
        x0 = 130 + k * 570; cx = x0 + 260
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([x0, 240, x0 + 520, 770], radius=34, fill=A(card, 255), outline=A(gold, 255), width=5)
        if k == 0:
            person(C, cx - 70, 460, gold, 2.3); person(C, cx + 70, 500, pink, 1.3); person(C, cx + 150, 510, blue, 1.1)
        elif k == 1:
            person(C, cx - 90, 460, green, 2.3); person(C, cx + 90, 500, (170, 175, 190), 1.9)
            d.line([cx + 165, 470, cx + 165, 590], fill=A(goldL, 255), width=8)
        else:
            briefcase(C, cx, 470, 2.5); cross(C, cx + 110, 395, 46, red)
        txt(C, nm, BOLD(46 if k != 1 else 40), 660, white, 255, x=cx)
        fr = appear(fr, C, (x0 - 10, 230, x0 + 530, 780), t, T(mk) - 0.3, 0.9)
    fr = chip(fr, 'NEVER REALIZE IT IS HAPPENING', 960, 830, t, T('never realize'), red, 46, filled=red, tcol=(255, 255, 255))
    return frame(fr)

SL = {2: [b2a, b2b, b2c], 3: [b3a, b3b, b3c, b3d], 4: [b4a, b4b, b4c, b4d], 5: [b5a, b5b, b5c]}
FSD = {2: B2.FS, 3: B3.FS, 4: B4.FS, 5: B5.FS}

if __name__ == '__main__':
    run_cli('b2_5', SL, FSD, None)
