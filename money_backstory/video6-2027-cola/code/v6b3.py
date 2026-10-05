from v3lib import *
from v3b3_10 import POP, new, lerp
from v4b11_20 import calculator
from v4b2_10 import cal_card
from v5b1 import amb, sparks, shake
from v5lib import paycheck, arrow_r
from v6b1 import A_, E_, chip_src
from v6b2 import chip
import sys, math

S = ["Here is the plan. Five things about your twenty twenty seven raise.",
     "One, what Cola really is, and how the number is picked. Two, why a raise can feel smaller than your bills.",
     "Three, what Medicare takes before the money reaches you. Four, what happens with taxes.",
     "And five, the other numbers that change on the same day.",
     "At the end, we put it all together on one real check."]
TOTF = 793   # 2415 - 1622: fine voce blocco 3 = 01:20 + 15f (screenshot utente)
def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':'))
gw = [len(s) + 10 for s in S]
FS = [round(w / sum(gw) * TOTF) for w in gw]; FS[-1] = TOTF - sum(FS[:-1])
def tt(g, marker):
    s = S[g]; i = s.index(marker)
    return max(0.2, wtot(s[:i]) / wtot(s) * FS[g] / 30 - 0.1)

def badge(C, cx, cy, n, col=gold, r=46):
    d = ImageDraw.Draw(C); d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (255,), outline=goldL + (255,), width=4)
    txt(C, str(n), BOLD(int(r * 1.3)), cy - r * 0.78, navy, 255, x=cx)

def card(C, x0, y0, x1, y1, n, l1, l2, col=gold):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([x0, y0, x1, y1], radius=34, fill=card_c + (255,), outline=col + (255,), width=6)
    badge(C, x0 + 70, y0 + 70, n, col)
    cx = (x0 + x1) / 2
    txt(C, l1, BOLD(54), y0 + 38, white, 255, x=cx + 40)
    txt(C, l2, BOLD(54), y0 + 102, white, 255, x=cx + 40)
card_c = (22, 40, 64)

def medicare_card(C, cx, cy, s=1.0):
    d = ImageDraw.Draw(C); w = 330 * s; h = 210 * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(18 * s), fill=(236, 240, 245, 255), outline=blue + (255,), width=5)
    d.rectangle([cx - w / 2 + 16 * s, cy - h / 2 + 16 * s, cx + w / 2 - 16 * s, cy - h / 2 + 70 * s], fill=blue + (255,))
    txt(C, 'MEDICARE', BOLD(int(40 * s)), cy - h / 2 + 24 * s, (255, 255, 255), 255, x=cx)
    d.rectangle([cx - w / 2 + 30 * s, cy + 20 * s, cx - w / 2 + 90 * s, cy + 36 * s], fill=red + (255,)); d.rectangle([cx - w / 2 + 52 * s, cy - 2 * s, cx - w / 2 + 68 * s, cy + 58 * s], fill=red + (255,))
    for k in range(3): d.rectangle([cx - w / 2 + 120 * s, cy + 12 * s + k * 26 * s, cx + w / 2 - 30 * s, cy + 24 * s + k * 26 * s], fill=(150, 165, 190, 255))

def drawA(t):
    fr = base(t); fr = amb(fr, t, 11, 7, 55); fr = title_layer(fr, 'THE PLAN', t, size=66)
    T = lambda m: tt(0, m)
    t1 = 0.3
    if t > t1:
        C = new(); d = ImageDraw.Draw(C)
        d.ellipse([260, 300, 640, 680], fill=gold + (255,), outline=goldL + (255,), width=10)
        txt(C, '5', BOLD(300), 330, navy, 255, x=450)
        fr = A_(fr, C, (240, 280, 660, 700), t, t1)
    t2 = T('Five things')
    if t > t2:
        C = new()
        txt(C, 'THINGS ABOUT', BOLD(70), 360, white, 255, x=1280); txt(C, 'YOUR 2027 RAISE', BOLD(84), 450, goldL, 255, x=1280)
        fr = A_(fr, C, (780, 320, 1800, 580), t, t2)
        C = new(); bill(C, 1050, 700, 250, 120, -6, 255); bill(C, 1250, 720, 250, 120, 4, 255)
        txt(C, '+$72?', BOLD(100), 650, green, 255, x=1560)
        fr = A_(fr, C, (900, 580, 1800, 820), t, t2 + 0.4)
    L = new(); d = ImageDraw.Draw(L)
    for k in range(5):
        a = E_(t, 1.6 + 0.15 * k); cx = 420 + k * 270
        d.ellipse([cx - 40, 880 - 40, cx + 40, 880 + 40], outline=goldL + (int(255 * a),), width=5)
        txt(L, str(k + 1), BOLD(48), 858, goldL, 255 * a, x=cx)
        if k < 4: d.line([cx + 46, 880, cx + 224, 880], fill=goldL + (int(150 * a),), width=4)
    fr = Image.alpha_composite(fr, L)
    return frame(fr)

def two_cards(t, g, seed, items):
    fr = base(t); fr = amb(fr, t, seed, 6, 50); fr = title_layer(fr, 'THE PLAN', t, size=66)
    T = lambda m: tt(g, m)
    for (x0, x1, marker, n, l1, l2, icon, col) in items:
        t0 = max(0.3, T(marker) - 0.1)
        if t < t0: continue
        C = new(); card(C, x0, 250, x1, 800, n, l1, l2, col); icon(C, (x0 + x1) / 2, 560, t)
        fr = A_(fr, C, (x0 - 20, 230, x1 + 20, 820), t, t0, 0.6)
    return fr

def ic1(C, cx, cy, t):
    calculator(C, cx - 150, cy, 1.25)
    d = ImageDraw.Draw(C); d.ellipse([cx + 20, cy - 110, cx + 260, cy + 110], fill=gold + (255,), outline=goldL + (255,), width=6)
    txt(C, '%', BOLD(170), cy - 100, navy, 255, x=cx + 140)
    chip_ = None
def ic2(C, cx, cy, t):
    cart(C, cx - 120, cy, 1.5, 255, gold)
    wallet(C, cx + 190, cy + 10, 1.05)
    txt(C, 'BILLS', BOLD(46), cy + 130, red, 255, x=cx + 190)
def ic3(C, cx, cy, t):
    bill(C, cx - 250, cy, 220, 108, 0, 255); arrow_r(C, cx - 110, cx - 10, cy, red, 255); medicare_card(C, cx + 190, cy, 0.9)
    txt(C, 'FIRST BITE', BOLD(46), cy + 150, red, 255, x=cx + 50)
def ic4(C, cx, cy, t):
    tax_form(C, cx - 100, cy - 140, 200, 260, 255, 'IRS')
    d = ImageDraw.Draw(C)
    txt(C, '50% - 85%', BOLD(60), cy + 150, red, 255, x=cx + 0)

def drawB(t):
    return frame(two_cards(t, 1, 12, [(130, 930, 'One,', 1, 'WHAT COLA IS,', 'HOW IT IS PICKED', ic1, gold), (990, 1790, 'Two,', 2, 'WHY IT FEELS', 'SMALLER THAN BILLS', ic2, goldL)]))
def drawC(t):
    return frame(two_cards(t, 2, 13, [(130, 930, 'Three,', 3, 'WHAT MEDICARE', 'TAKES FIRST', ic3, red), (990, 1790, 'Four,', 4, 'WHAT HAPPENS', 'WITH TAXES', ic4, red)]))

def drawD(t):
    fr = base(t); fr = amb(fr, t, 14, 6, 50); fr = title_layer(fr, 'THE PLAN', t, size=66)
    t1 = 0.3
    if t > t1:
        C = new(); card(C, 360, 250, 1560, 800, 5, 'THE OTHER NUMBERS', 'THAT CHANGE THE SAME DAY', gold)
        cal_card(C, 440, 450, 800, 780, 'OCTOBER', '14', bigsize=150, headcol=red)
        fr = A_(fr, C, (340, 230, 1580, 820), t, t1)
    for k, lab in enumerate(['TAXABLE MAXIMUM', 'EARNINGS LIMITS', 'AND MORE']):
        fr = chip(fr, lab, 1180, 470 + k * 100, t, 0.9 + 0.35 * k, goldL, 46)
    return frame(fr)

def drawE(t):
    fr = base(t); fr = amb(fr, t, 15, 6, 50); fr = title_layer(fr, 'ONE REAL CHECK', t, size=66)
    T = lambda m: tt(4, m)
    t1 = 0.3
    if t > t1:
        C = new(); paycheck(C, 640, 330, 1280, 700, gold, '$2,071', 'PER MONTH', 'MONTHLY CHECK', 140)
        fr = A_(fr, C, (620, 310, 1300, 720), t, t1)
    for k, (lab, col, x, y, tcol) in enumerate([('RAISE', green, 360, 380, navy), ('MEDICARE', blue, 1650, 380, (255, 255, 255)), ('TAXES', red, 960, 850, (255, 255, 255))]):
        t0 = 0.9 + 0.5 * k
        fr = chip(fr, lab, x, y, t, t0, col, 52, fillc=col, tcol=tcol)
    L = new(); a1 = E_(t, 1.1); a2 = E_(t, 1.6)
    arrow_r(L, 470, 630, 470, green, 255 * a1)
    d = ImageDraw.Draw(L)
    if a2 > 0:
        d.polygon([(1470, 470), (1430, 444), (1430, 496)], fill=blue + (int(255 * a2),)); d.line([1296, 470, 1440, 470], fill=blue + (int(255 * a2),), width=10)
    a3 = E_(t, 1.9)
    if a3 > 0:
        d.line([960, 716, 960, 800], fill=red + (int(255 * a3),), width=10); d.polygon([(960, 840), (930, 800), (990, 800)], fill=red + (int(255 * a3),))
    fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'ALL TOGETHER ON ONE REAL CHECK', 880 if False else 900, t, 2.0, goldL, tcol=navy, size=46, cx=960) if False else fr
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1]; fns = [drawA, drawB, drawC, drawD, drawE]
    sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2, 3, 4, 5]
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.2, 0.5, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}pv3_{i}_{int(fq*100)}.png')
        print(FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b3-0{i}.mp4'); print('done', i, f, flush=True)
