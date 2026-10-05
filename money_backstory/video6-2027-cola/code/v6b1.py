from v3lib import *
from v3b3_10 import POP, new, lerp, fly
from v4b11_20 import calculator
from v4b2_10 import cal_card, eye
from v5b1 import amb, sparks, shake, tile
from v5lib import arrow_r, paycheck
import sys, math

S = ["On October fourteenth, the Social Security Administration will announce the yearly raise for more than seventy million Americans.",
     "The early estimate is about three point five percent, which would be roughly seventy two dollars more on the average check.",
     "But here is the part almost nobody talks about: by the time that raise reaches your bank account, a piece of it may already be spoken for.",
     "Stay until the end, because number three is the one that surprises almost everyone."]
TOTF = 861   # fine voce blocco 1 = 00:28 + 21f dallo screenshot dell'utente
def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':'))
gw = [len(s) + 10 for s in S]
FS = [round(w / sum(gw) * TOTF) for w in gw]; FS[-1] = TOTF - sum(FS[:-1])
def tt(g, marker):
    s = S[g]; i = s.index(marker)
    return max(0.2, wtot(s[:i]) / wtot(s) * FS[g] / 30 - 0.1)

def A_(fr, C, box, t, t0, d=0.6):
    return POP(fr, C, box, back((t - t0) / d))

def drawA(t):
    fr = base(t); fr = amb(fr, t, 2, 7, 55); fr = title_layer(fr, 'THE 2027 RAISE: ANNOUNCEMENT DAY', t, size=58)
    T = lambda m: tt(0, m)
    # calendar
    t1 = 0.35
    if t > t1:
        C = new(); cal_card(C, 140, 320, 610, 700, 'OCTOBER', '14', bigsize=230, headcol=red)
        txt(C, '2026', BOLD(70), 600, (70, 84, 108), 255, x=375)
        fr = A_(fr, C, (120, 300, 630, 720), t, t1)
    # arrow cal -> building
    L = new(); arrow_r(L, 640, 770, 510, goldL, 255 * E_(t, T('the Social Security') - 0.2)); fr = Image.alpha_composite(fr, L)
    t2 = T('the Social Security')
    if t > t2:
        C = new(); building(C, 940, 470, 330, 280, gold)
        txt(C, 'SOCIAL SECURITY', BOLD(58), 660, white, 255, x=940); txt(C, 'ADMINISTRATION', BOLD(58), 730, white, 255, x=940)
        txt(C, 'ANNOUNCES THE RAISE', BOLD(46), 815, goldL, 255, x=940)
        fr = A_(fr, C, (650, 280, 1230, 880), t, t2)
    t3 = T('for more than')
    L = new(); arrow_r(L, 1200, 1320, 510, goldL, 255 * E_(t, t3 - 0.1)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); cols = [blue, pink, gold, green, purple]
        for k in range(15):
            r_, c_ = divmod(k, 5)
            u = back((t - t3 - 0.04 * k) / 0.4)
            if u <= 0: continue
            avatar(C, 1410 + c_ * 80, 390 + r_ * 120, cols[(r_ + c_) % 5], 0.9 * min(1, u))
        txt(C, '70+ MILLION', BOLD(72), 770, goldL, 255, x=1560); txt(C, 'AMERICANS', BOLD(58), 860, white, 255, x=1560)
        fr = Image.alpha_composite(fr, C)
    fr = chip_src(fr, 'SOURCE: SSA.GOV', 930, t, 1.4)
    return frame(fr)

def E_(t, t0, d=0.6): return ease((t - t0) / d)

def chip_src(fr, text, y, t, t0):
    if t < t0: return fr
    C = new(); d = ImageDraw.Draw(C); f = BOLD(34); b = d.textbbox((0, 0), text, font=f); w = b[2] - b[0] + 60
    d.rounded_rectangle([960 - w / 2, y, 960 + w / 2, y + 62], radius=31, fill=card + (255,), outline=grey + (255,), width=3)
    d.text((960 - (b[2] - b[0]) / 2 - b[0], y + 31 - (b[3] - b[1]) / 2 - b[1]), text, font=f, fill=grey + (255,))
    return A_(fr, C, (960 - w / 2 - 10, y - 10, 960 + w / 2 + 10, y + 72), t, t0, 0.5)

def drawB(t):
    fr = base(t); fr = amb(fr, t, 3, 7, 55); fr = title_layer(fr, 'THE EARLY ESTIMATE', t, size=62)
    T = lambda m: tt(1, m)
    t1 = 0.35
    if t > t1:
        C = new(); paycheck(C, 130, 290, 640, 640, blue, '$2,071', 'PER MONTH', 'AVERAGE CHECK', 124)
        fr = A_(fr, C, (110, 270, 660, 670), t, t1)
    t2 = T('about three point five')
    L = new(); arrow_r(L, 665, 790, 470, goldL, 255 * E_(t, t2 - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([800, 330, 1120, 590], radius=40, fill=card + (255,), outline=goldL + (255,), width=6)
        txt(C, '3.5%', BOLD(140), 370, goldL, 255, x=960)
        txt(C, 'RAISE', BOLD(52), 520, white, 255, x=960)
        fr = A_(fr, C, (780, 310, 1140, 610), t, t2)
        fr = pill_pop(fr, 'ESTIMATE, NOT OFFICIAL', 640, t, t2 + 0.5, red, size=40, cx=960)
    t3 = T('roughly seventy two')
    L = new(); arrow_r(L, 1145, 1275, 470, goldL, 255 * E_(t, t3 - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); paycheck(C, 1290, 290, 1800, 640, green, '+$72', 'MORE PER MONTH', 'THE RAISE', 124)
        up_arrow(C, 1710, 215, 0.55, green)
        fr = A_(fr, C, (1270, 150, 1820, 670), t, t3)
    t4 = T('on the average check')
    if t > t4:
        fr = pill_pop(fr, '$2,071 x 3.5% = ABOUT $72 MORE', 790, t, t4, green, tcol=navy, size=56, cx=960)
    fr = chip_src(fr, 'ESTIMATES: SENIOR CITIZENS LEAGUE, AARP', 935, t, 2.0)
    return frame(fr)

def drawC(t):
    fr = base(t); fr = amb(fr, t, 4, 6, 50); fr = title_layer(fr, 'WHERE DOES THE RAISE GO?', t, size=62)
    T = lambda m: tt(2, m)
    t1 = 0.35
    if t > t1:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([150, 300, 560, 690], radius=34, fill=card + (255,), outline=green + (255,), width=6)
        bill(C, 355, 400, 230, 110, 0, 255)
        txt(C, '+$72', BOLD(116), 470, green, 255, x=355)
        txt(C, 'THE RAISE', BOLD(50), 610, white, 255, x=355)
        fr = A_(fr, C, (130, 280, 580, 710), t, t1)
    t2 = T('by the time')
    L = new()
    for k in range(5):
        fly(L, t, t2 + k * 0.35, 1.6, (560, 460), (1290, 460), arc=70, kind='bill', size=0.8)
    fr = Image.alpha_composite(fr, L)
    t3 = T('your bank account')
    if t > t3 - 0.6:
        C = new(); building(C, 1560, 440, 330, 270, blue)
        txt(C, 'YOUR BANK', BOLD(62), 620, white, 255, x=1560); txt(C, 'ACCOUNT', BOLD(62), 692, white, 255, x=1560)
        fr = A_(fr, C, (1280, 250, 1850, 760), t, t3 - 0.6)
    t4 = T('a piece of it')
    if t > t4:
        C = new(); padlock(C, 960, 740, 1.15, red)
        txt(C, '?', BOLD(110), 640, white, 255, x=960)
        fr = A_(fr, C, (840, 520, 1080, 880), t, t4)
        L = new()
        for k in range(4):
            fly(L, t, t4 + 0.2 + k * 0.3, 1.1, (1000, 470), (960, 700), arc=60, kind='coin', size=0.9)
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'A PIECE MAY ALREADY BE SPOKEN FOR', 900, t, t4 + 0.5, red, size=46, cx=960)
    return frame(fr)

LABELS = [('WHAT', 'COLA IS'), ('FEELS', 'SMALLER'), ('MEDICARE', 'PART B'), ('TAXES', ''), ('OTHER', 'NUMBERS')]
def drawD(t):
    fr = base(t); fr = amb(fr, t, 5, 6, 50); fr = title_layer(fr, 'FIVE THINGS ABOUT YOUR 2027 RAISE', t, size=58)
    tn = tt(3, 'number three'); ts = tt(3, 'Stay until')
    for k in range(5):
        st = 0.3 + k * 0.2
        if t < st: continue
        hl = (k == 2 and t > tn)
        cx = 330 + k * 315; cy = 470
        s = 1.12 if hl else 1.0
        w2, h2 = 140 * s, 200 * s
        C = new(); d = ImageDraw.Draw(C)
        cx2 = cx + (shake(t, tn, 10, 0.6) if hl else 0)
        d.rounded_rectangle([cx2 - w2, cy - h2, cx2 + w2, cy + h2], radius=26, fill=A(red if hl else card, 255), outline=A(goldL if hl else (80, 100, 130), 255), width=6 if hl else 3)
        col = (255, 255, 255) if hl else (150, 165, 185)
        txt(C, str(k + 1), BOLD(int(84 * s)), cy - h2 + 14, col, 255, x=cx2)
        iy = cy - 5
        if k == 0: tile(C, cx2 - 46, iy - 46, 92, gold, '%')
        elif k == 1: wallet(C, cx2, iy, 0.75)
        elif k == 2:
            if hl: txt(C, '?', BOLD(150), iy - 95 + math.sin(t * 6) * 6, (255, 255, 255), 255, x=cx2)
            else:
                d.rounded_rectangle([cx2 - 46, iy - 46, cx2 + 46, iy + 46], radius=12, fill=A((236, 240, 245), 255)); d.rectangle([cx2 - 8, iy - 30, cx2 + 8, iy + 30], fill=A(red, 255)); d.rectangle([cx2 - 30, iy - 8, cx2 + 30, iy + 8], fill=A(red, 255))
        elif k == 3: tax_form(C, cx2 - 38, iy - 50, 76, 100, 255, 'TAX')
        else: calculator(C, cx2, iy, 0.6)
        l1, l2 = LABELS[k]
        if l2: txt(C, l1, BOLD(int(40 * s)), cy + h2 - 112, col, 255, x=cx2); txt(C, l2, BOLD(int(40 * s)), cy + h2 - 62, col, 255, x=cx2)
        else: txt(C, l1, BOLD(int(40 * s)), cy + h2 - 80, col, 255, x=cx2)
        fr = POP(fr, C, (cx - w2 - 20, cy - h2 - 20, cx + w2 + 20, cy + h2 + 20), back((t - st) / 0.35))
    if t > tn: fr = sparks(fr, t, (930, 250, 1250, 700), 9, 7, tn)
    fr = pill_pop(fr, 'NUMBER THREE SURPRISES ALMOST EVERYONE', 770, t, tn + 0.3, red, size=44)
    if t > ts + 0.3:
        C = new(); eye(C, 620, 925, 0.7, 255, t); fr = POP(fr, C, (540, 870, 700, 980), back((t - ts - 0.3) / 0.4))
        C = new(); eye(C, 1300, 925, 0.7, 255, t + 1); fr = POP(fr, C, (1220, 870, 1380, 980), back((t - ts - 0.4) / 0.4))
        L = new(); txt(L, 'STAY UNTIL THE END', BOLD(48), 900, goldL, 255 * ease((t - ts - 0.3) / 0.4), x=960); fr = Image.alpha_composite(fr, L)
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1]; fns = [drawA, drawB, drawC, drawD]
    sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2, 3, 4]
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.2, 0.5, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((960, 540)).save(f'{OUT}pv_{i}_{int(fq*100)}.png')
        print(FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b1-0{i}.mp4'); print('done', i, f, flush=True)
