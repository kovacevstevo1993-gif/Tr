from v3lib import *
from v3b3_10 import POP, new, lerp, fly
from v4b11_20 import calculator, hourglass, ss_card
from v4b2_10 import cal_card, eye
import sys, math, random

S = ["Social Security only counts thirty five years of your working life.",
     "If you worked thirty, it does not skip the missing five.",
     "It fills them in with zeros.",
     "And for one average worker, those five zeros cost more than three thousand two hundred dollars every single year, for life.",
     "Stay until the end, because number four is the one that surprises almost everyone."]
GROUPS = [[0], [1, 2], [3], [4]]
TOTF = 810

def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':') + text.count('—'))
def wpos(text, marker):
    i = text.index(marker); pre = text[:i]
    return len(pre) + 3 * (pre.count(',') + pre.count(':') + pre.count('—'))
gw = [sum(len(S[i]) + 10 for i in g) for g in GROUPS]
FS = [round(w / sum(gw) * TOTF) for w in gw]; FS[-1] = TOTF - sum(FS[:-1])
TXT = [' '.join(S[i] for i in g) for g in GROUPS]
def tt(g, marker):
    return max(0.2, wpos(TXT[g], marker) / wtot(TXT[g]) * FS[g] / 30 - 0.1)

# ---------- helpers ----------
def amb(fr, t, seed=1, n=9, a=70):
    rnd = random.Random(seed); L = new()
    for k in range(n):
        x = rnd.uniform(120, 1800); sp = rnd.uniform(40, 90); ph = rnd.uniform(0, 1000); kind = rnd.random() < 0.5
        y = 1150 - ((t * sp + ph) % 1250)
        if kind: bill(L, x + math.sin(t * 1.3 + k) * 30, y, 120, 58, math.sin(t + k) * 25, a)
        else: coin(L, x + math.sin(t * 1.1 + k) * 30, y, 22, a, squash=abs(math.cos(t * 2 + k)) * 0.6 + 0.4)
    return Image.alpha_composite(fr, L)

def sparkle(L, cx, cy, r, alpha=255, col=(255, 240, 190)):
    d = ImageDraw.Draw(L)
    d.polygon([(cx, cy - r), (cx + r * 0.22, cy - r * 0.22), (cx + r, cy), (cx + r * 0.22, cy + r * 0.22), (cx, cy + r), (cx - r * 0.22, cy + r * 0.22), (cx - r, cy), (cx - r * 0.22, cy - r * 0.22)], fill=A(col, alpha))

def sparks(fr, t, box, n=8, seed=5, t0=0.0):
    rnd = random.Random(seed); L = new()
    for k in range(n):
        x = rnd.uniform(box[0], box[2]); y = rnd.uniform(box[1], box[3]); ph = rnd.uniform(0, 6.28)
        v = max(0, math.sin((t - t0) * 4 + ph))
        if t > t0 and v > 0: sparkle(L, x, y, 10 + 22 * v, 255 * v)
    return Image.alpha_composite(fr, L)

def glow(fr, cx, cy, r, col, a):
    L = new(); d = ImageDraw.Draw(L); d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=A(col, a))
    x0, y0 = int(cx - r - 120), int(cy - r - 120)
    box = (max(0, x0), max(0, y0), min(W, int(cx + r + 120)), min(H, int(cy + r + 120)))
    piece = L.crop(box).filter(ImageFilter.GaussianBlur(60)); out = new(); out.alpha_composite(piece, (box[0], box[1]))
    return Image.alpha_composite(fr, out)

def shake(t, t0, amp=14, dur=0.5):
    u = t - t0
    if u < 0 or u > dur: return 0
    return math.sin(u * 60) * amp * (1 - u / dur)

def tile(C, x, y, sz, col, label=None, fill=None, outline=None, alpha=255, hl=0.0):
    d = ImageDraw.Draw(C)
    f = fill or col
    d.rounded_rectangle([x, y + 6, x + sz, y + sz + 6], radius=14, fill=A((90, 64, 20) if fill is None else (110, 30, 30), alpha))
    d.rounded_rectangle([x, y, x + sz, y + sz], radius=14, fill=A(f, alpha), outline=A(outline or goldL, alpha), width=3)
    d.rounded_rectangle([x + 8, y + 6, x + sz - 8, y + 18], radius=6, fill=A((255, 255, 255), 55 + 120 * hl))
    if label is not None:
        txt(C, label, BOLD(int(sz * 0.5)), y + sz * 0.2, navy if fill is None else (255, 255, 255), alpha, x=x + sz / 2)

GX, GY, SZ, GAP = 250, 245, 92, 16
def pos(i): return GX + (i % 7) * (SZ + GAP), GY + (i // 7) * (SZ + GAP)

def drawA(t):
    fr = base(t); fr = amb(fr, t, 1); fr = title_layer(fr, 'THE THIRTY FIVE YEAR RULE', t, size=60)
    T = lambda m: tt(0, m)
    tss = T('Social Security'); t35 = T('thirty five'); twl = T('working life')
    band = (t - 2.6) * 900 if t > 2.6 else -999
    for i in range(35):
        st = 0.35 + i * 0.09
        if t < st: continue
        x, y = pos(i)
        hl = max(0, 1 - abs((x + y * 0.6) - band) / 160)
        C = new(); tile(C, x, y, SZ, gold, str(i + 1), hl=hl)
        fr = POP(fr, C, (x - 12, y - 12, x + SZ + 12, y + SZ + 18), back((t - st) / 0.3))
    L = new()
    for k in range(6):
        fly(L, t, 0.5 + k * 0.42, 1.2, (pos(min(34, int(k * 6)))[0] + 46, pos(0)[1] + 100), (1400, 330), 120, 'bill', 255, 0, 0.7)
    fr = Image.alpha_composite(fr, L)
    C = new(); ss_card(C, 1400, 330 + math.sin(t * 2.4) * 8, 1.15); fr = POP(fr, C, (1180, 170, 1620, 500), back((t - 0.15) / 0.5))
    n = min(35, int(max(0, (t - 0.35) / 0.09)))
    L = new()
    txt(L, str(n), BOLD(260), 470, goldL, 255 * ease((t - 0.3) / 0.3), x=1400)
    txt(L, 'YEARS COUNTED', BOLD(48), 745, white, 255 * ease((t - 0.6) / 0.4), x=1400)
    txt(L, 'Source: Social Security Administration', REG(26), 985, grey, 200)
    fr = Image.alpha_composite(fr, L)
    if t > twl:
        C = new(); briefcase(C, 1700, 640, 1.5); fr = POP(fr, C, (1580, 540, 1820, 740), back((t - twl) / 0.45))
        C = new(); coin_stack(C, 1130, 700, min(6, int((t - twl) / 0.18) + 1), 56); fr = POP(fr, C, (1060, 540, 1200, 730), back((t - twl) / 0.4))
        fr = sparks(fr, t, (1100, 560, 1800, 740), 7, 3, twl)
    fr = pill_pop(fr, 'ONLY YOUR BEST 35 YEARS COUNT', 850, t, t35 + 0.8, gold, navy, size=38, cx=1400)
    return frame(fr)

def drawB(t):
    fr = base(t); fr = amb(fr, t, 2, 6, 45); fr = title_layer(fr, 'FRANK WORKED ONLY THIRTY YEARS', t, size=58)
    T = lambda m: tt(1, m)
    tw = T('worked thirty'); tm = T('missing five'); tz = T('zeros')
    if t > tz:
        L = new(); rnd = random.Random(9)
        for k in range(16):
            st = tz + rnd.uniform(0, 3.0); x = rnd.uniform(140, 1780)
            if t < st: continue
            y = -80 + (t - st) * rnd.uniform(240, 380)
            if y < 1000: txt(L, '0', BOLD(rnd.randint(70, 150)), y, red, 70, x=x)
        fr = Image.alpha_composite(fr, L)
    dx = shake(t, tz, 12)
    for i in range(30):
        st = 0.3 + i * 0.05
        if t < st: continue
        x, y = pos(i)
        C = new(); tile(C, x, y, SZ, gold, str(i + 1))
        fr = POP(fr, C, (x - 12, y - 12, x + SZ + 12, y + SZ + 18), back((t - st) / 0.3))
    for k in range(5):
        x, y = pos(30 + k); x += dx
        if t > tz + k * 0.22:
            C = new(); tile(C, x, y, SZ, red, '0', fill=red, outline=(255, 150, 150))
            fr = POP(fr, C, (x - 12, y - 12, x + SZ + 12, y + SZ + 18), back((t - tz - k * 0.22) / 0.3))
        elif t > tm + k * 0.15:
            L = new(); d = ImageDraw.Draw(L); a = ease((t - tm - k * 0.15) / 0.3)
            d.rounded_rectangle([x, y, x + SZ, y + SZ], radius=14, outline=A(red, 255 * a), width=4, fill=A((60, 20, 30), 120 * a))
            txt(L, '?', BOLD(56), y + 16 + math.sin(t * 6 + k) * 4, red, 255 * a, x=x + SZ / 2)
            fr = Image.alpha_composite(fr, L)
    if t > tm:
        L = new(); d = ImageDraw.Draw(L); a = ease((t - tm) / 0.4)
        x0 = pos(30)[0]; x1 = pos(34)[0] + SZ; yy = pos(30)[1] + SZ + 44
        d.line([x0, yy, x1, yy], fill=A(red, 255 * a), width=5)
        d.line([x0, yy - 12, x0, yy + 12], fill=A(red, 255 * a), width=5); d.line([x1, yy - 12, x1, yy + 12], fill=A(red, 255 * a), width=5)
        txt(L, '5 MISSING YEARS', BOLD(34), yy + 18, red, 255 * a, x=(x0 + x1) / 2)
        fr = Image.alpha_composite(fr, L)
    C = new(); avatar(C, 1400, 330 + math.sin(t * 2) * 6, blue, 2.6); txt(C, 'FRANK', BOLD(48), 470, blue, 255, x=1400)
    fr = POP(fr, C, (1180, 90, 1620, 540), back((t - 0.1) / 0.5))
    C = new(); briefcase(C, 1700, 400, 1.3); fr = POP(fr, C, (1600, 320, 1800, 480), back((t - tw) / 0.45)) if t > tw else fr
    L = new()
    txt(L, '30 YEARS WORKED', BOLD(58), 560, goldL, 255 * ease((t - 0.4) / 0.4), x=1400)
    fr = Image.alpha_composite(fr, L)
    if t > tz:
        L = new(); txt(L, '= ZEROS', BOLD(120), 690 + shake(t, tz, 10), red, 255 * ease((t - tz) / 0.3), x=1400); fr = Image.alpha_composite(fr, L)
        fr = stamp(fr, 'ZERO YEARS', 1400, 900, -10, red, min(1, ease((t - tz - 0.3) / 0.35)) * (1 + 0.04 * math.sin(t * 8)), size=48)
    return frame(fr)

def drawC(t):
    fr = base(t); fr = amb(fr, t, 3, 6, 45); fr = title_layer(fr, 'THE PRICE OF FIVE ZEROS', t, size=60)
    T = lambda m: tt(2, m)
    tm = T('more than three'); te = T('every single year'); tl = T('for life')
    fr = glow(fr, 1250, 320, 260, red, 60 + 30 * math.sin(t * 3)) if t > tm else fr
    C = new(); wallet(C, 400, 600 + math.sin(t * 2) * 6, 2.3); fr = POP(fr, C, (130, 400, 700, 800), back(t / 0.5))
    L = new(); s0 = 0.5; k = 0
    while s0 < FS[2] / 30:
        fly(L, t, s0, 1.7, (430, 560), (930, 300), 40, 'coin' if k % 2 == 0 else 'bill', 255, 0, 1.2 if k % 2 == 0 else 0.7); s0 += 0.4; k += 1
    fr = Image.alpha_composite(fr, L)
    for k in range(5):
        st = 0.3 + k * 0.25
        if t < st: continue
        C = new(); tile(C, 1290 - 250 + k * 100, 195, 84, red, '0', fill=red, outline=(255, 150, 150)); fr = POP(fr, C, (1290 - 262 + k * 100, 183, 1290 - 154 + k * 100 + 60, 290), back((t - st) / 0.3))
    u = ease((t - tm + 0.2) / 2.2) if t > tm - 0.2 else 0
    L = new()
    txt(L, '-$' + f'{int(3200 * u):,}' + ('+' if u > 0.98 else ''), BOLD(150), 272, red, 255 * ease((t - tm + 0.2) / 0.3), x=1290)
    fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'EVERY YEAR', 462, t, te, gold, navy, size=44, cx=1290)
    for k in range(5):
        st = te + 0.25 + k * 0.35
        if t < st: continue
        x0 = 735 + k * 192
        C = new(); cal_card(C, x0, 580, x0 + 170, 790, f'YEAR {k + 1}', '-3.2K', 56, red, red)
        fr = POP(fr, C, (x0 - 12, 568, x0 + 182, 802), back((t - st) / 0.35))
    if t > te + 0.25 + 4 * 0.35 + 0.3:
        L = new(); d = ImageDraw.Draw(L); a = ease((t - te - 1.95) / 0.4)
        txt(L, '...', BOLD(90), 610, red, 255 * a, x=1700)
        fr = Image.alpha_composite(fr, L)
    if t > tl - 0.2:
        C = new(); clock(C, 760, 860, 70, t * 3); fr = POP(fr, C, (670, 770, 850, 950), back((t - tl + 0.2) / 0.4))
        C = new(); hourglass(C, 1660, 860, 0.62, 255, min(1, max(0, (t - tl) / 2.0))); fr = POP(fr, C, (1590, 780, 1730, 940), back((t - tl + 0.2) / 0.4))
        fr = pill_pop(fr, 'FOR LIFE', 835, t, tl, red, size=50, cx=1210)
    L = new(); txt(L, 'Example: same pay, 30 years vs 35 years · SSA 2026 formula', REG(26), 985, grey, 200)
    return frame(Image.alpha_composite(fr, L))

def drawD(t):
    fr = base(t); fr = amb(fr, t, 4, 7, 55); fr = title_layer(fr, 'FIVE THINGS THAT DECIDE YOUR CHECK', t, size=56)
    T = lambda m: tt(3, m)
    tn = T('number four'); ts = T('surprises')
    labels = ['35 YEARS', 'THE FORMULA', 'CLAIMING AGE', '???', 'YOUR SPOUSE']
    if t > tn: fr = glow(fr, 330 + 3 * 315, 470, 220, red, 90 + 40 * math.sin(t * 5))
    for k in range(5):
        st = 0.3 + k * 0.22
        if t < st: continue
        hl = (k == 3 and t > tn)
        cx = 330 + k * 315; cy = 470
        s = 1.12 if hl else 1.0
        w2, h2 = 140 * s, 200 * s
        C = new(); d = ImageDraw.Draw(C)
        dx = shake(t, tn, 10, 0.6) if hl else 0
        cx2 = cx + dx
        d.rounded_rectangle([cx2 - w2, cy - h2, cx2 + w2, cy + h2], radius=26, fill=A(red if hl else card, 255), outline=A(goldL if hl else (80, 100, 130), 255), width=6 if hl else 3)
        col = (255, 255, 255) if hl else (150, 165, 185)
        txt(C, str(k + 1), BOLD(int(84 * s)), cy - h2 + 14, col, 255, x=cx2)
        iy = cy + 10
        if k == 0: tile(C, cx2 - 46, iy - 46, 92, gold, '35')
        elif k == 1: calculator(C, cx2, iy, 0.62)
        elif k == 2: clock(C, cx2, iy, 56, t * 2)
        elif k == 3:
            if hl: txt(C, '?', BOLD(150), iy - 95 + math.sin(t * 6) * 6, (255, 255, 255), 255, x=cx2)
            else: briefcase(C, cx2, iy, 1.0, 255, (110, 60, 60))
        else:
            avatar(C, cx2 - 34, iy, blue, 0.9); avatar(C, cx2 + 34, iy, pink, 0.9)
        txt(C, labels[k], BOLD(int(28 * s)), cy + h2 - 52, col if not hl else (255, 255, 255), 255, x=cx2)
        fr = POP(fr, C, (cx - w2 - 20, cy - h2 - 20, cx + w2 + 20, cy + h2 + 20), back((t - st) / 0.35))
    if t > tn: fr = sparks(fr, t, (930, 250, 1250, 700), 9, 7, tn)
    if t > tn:
        L = new(); d = ImageDraw.Draw(L); a = ease((t - tn) / 0.4); yb = 700 + math.sin(t * 7) * 8
        d.polygon([(330 + 3 * 315 - 34, 730 + math.sin(t * 7) * 8), (330 + 3 * 315 + 34, 730 + math.sin(t * 7) * 8), (330 + 3 * 315, 780 + math.sin(t * 7) * 8)], fill=A(red, 0)) if False else None
        fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'NUMBER FOUR SURPRISES ALMOST EVERYONE', 770, t, tn + 0.3, red, size=44)
    if t > ts + 0.3:
        C = new(); eye(C, 620, 925, 0.7, 255, t); fr = POP(fr, C, (540, 870, 700, 980), back((t - ts - 0.3) / 0.4))
        C = new(); eye(C, 1300, 925, 0.7, 255, t + 1); fr = POP(fr, C, (1220, 870, 1380, 980), back((t - ts - 0.4) / 0.4))
        L = new(); txt(L, 'STAY UNTIL THE END', BOLD(48), 900, goldL, 255 * ease((t - ts - 0.3) / 0.4), x=960); fr = Image.alpha_composite(fr, L)
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1]
    fns = [drawA, drawB, drawC, drawD]
    sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2, 3, 4]
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.25, 0.55, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'/home/claude/pv5_{i}_{int(fq * 100)}.png')
        print(FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'/mnt/user-data/outputs/v5-b1-0{i}.mp4'); print('done', i, f, flush=True)
