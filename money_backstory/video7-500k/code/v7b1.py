from v3lib import *
from v3b3_10 import POP, new, lerp, fly
from v5b1 import amb, sparks, shake, tile
from v5lib import arrow_r, arrow_d, paycheck
import sys, math

S = ["If you have five hundred thousand dollars saved for retirement, you are ahead of most Americans.",
     "But the question that matters is different: how much does it pay you every month, after Medicare, and is that enough?"]
TOTF = 388   # fine voce blocco 1 = 00:12 + 28f dalla timeline dell'utente (05/10/2026)
gw = [len(s) + 10 for s in S]
FS = [round(w / sum(gw) * TOTF) for w in gw]; FS[-1] = TOTF - sum(FS[:-1])

def E_(t, t0, d=0.6): return ease((t - t0) / d)
def A_(fr, C, box, t, t0, d=0.6): return POP(fr, C, box, back((t - t0) / d))

def med_tile(C, cx, cy, s=1.0):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - 62 * s, cy - 62 * s, cx + 62 * s, cy + 62 * s], radius=int(16 * s), fill=A((236, 240, 245), 255), outline=A(red, 255), width=5)
    d.rectangle([cx - 11 * s, cy - 40 * s, cx + 11 * s, cy + 40 * s], fill=A(red, 255)); d.rectangle([cx - 40 * s, cy - 11 * s, cx + 40 * s, cy + 11 * s], fill=A(red, 255))

def podium(C, cx, y, w, h, col, label, n):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([cx - w / 2, y, cx + w / 2, y + h], radius=14, fill=A(col, 255), outline=A(goldL, 255), width=4)
    txt(C, label, BOLD(52), y + h / 2 - 28, navy, 255, x=cx)

def drawA(t):
    fr = base(t); fr = amb(fr, t, 2, 7, 55); fr = title_layer(fr, 'FIVE HUNDRED THOUSAND DOLLARS SAVED', t, size=56)
    # sinistra: sacco di soldi + pile di monete + importo che sale
    t1 = 0.3
    if t > t1:
        C = new()
        coin_stack(C, 150, 660, 6, 66); coin_stack(C, 500, 660, 8, 66)
        money_bag(C, 325, 520, 1.3)
        fr = A_(fr, C, (60, 340, 590, 720), t, t1)
    t2 = 0.7
    if t > t2:
        v = 500000 * ease((t - t2) / 1.2)
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([70, 735, 580, 865], radius=34, fill=card + (255,), outline=goldL + (255,), width=5)
        txt(C, counter_text(v), BOLD(88), 757, goldL, 255, x=325)
        fr = A_(fr, C, (50, 715, 600, 885), t, t2, 0.4)
        if t > t2 + 1.2: fr = sparks(fr, t, (120, 400, 540, 760), 8, 4, t2 + 1.2)
    # destra: fila di persone, la tua davanti sul podio dorato
    t3 = 1.3
    cols = [(120, 135, 160)] * 5
    if t > t3:
        C = new()
        for k in range(18):
            r_, c_ = divmod(k, 6)
            u = back((t - t3 - 0.05 * k) / 0.4)
            if u <= 0: continue
            avatar(C, 780 + c_ * 120, 360 + r_ * 130, (110, 128, 156), 0.95 * min(1, u))
        txt(C, 'MOST AMERICANS', BOLD(50), 760, (170, 185, 205), 255, x=1020)
        fr = Image.alpha_composite(fr, C)
    t4 = 2.2
    if t > t4:
        C = new(); d = ImageDraw.Draw(C)
        podium(C, 1560, 590, 220, 150, gold, '1', 1)
        avatar(C, 1560, 520, goldL, 1.9)
        txt(C, 'YOU', BOLD(60), 330, goldL, 255, x=1560)
        d.polygon([(1560, 410), (1530, 372), (1590, 372)], fill=A(goldL, 255))
        fr = A_(fr, C, (1400, 300, 1720, 740), t, t4)
    t5 = 2.9
    if t > t5:
        fr = pill_pop(fr, 'YOU ARE AHEAD OF MOST AMERICANS', 915, t, t5, green, tcol=navy, size=50, cx=960)
    return frame(fr)

def drawB(t):
    fr = base(t); fr = amb(fr, t, 3, 7, 55); fr = title_layer(fr, 'THE REAL QUESTION', t, size=64)
    t1 = 0.35
    if t > t1:
        C = new(); paycheck(C, 120, 280, 660, 640, blue, '$ ?', 'EVERY MONTH', 'HOW MUCH DOES IT PAY?', 150)
        fr = A_(fr, C, (100, 260, 680, 660), t, t1)
    t2 = 1.1
    L = new(); arrow_r(L, 690, 840, 470, goldL, 255 * E_(t, t2 - 0.3)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); med_tile(C, 960, 440, 1.35)
        txt(C, 'AFTER', BOLD(50), 565, white, 255, x=960); txt(C, 'MEDICARE', BOLD(58), 625, red, 255, x=960)
        fr = A_(fr, C, (780, 330, 1140, 700), t, t2)
    t3 = 1.9
    L = new(); arrow_r(L, 1090, 1240, 470, goldL, 255 * E_(t, t3 - 0.3)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([1250, 280, 1800, 640], radius=30, fill=card + (255,), outline=goldL + (255,), width=6)
        txt(C, 'ENOUGH?', BOLD(92), 340, goldL, 255, x=1525)
        pulse = 1 + 0.06 * math.sin((t - t3) * 4)
        check(C, 1400, 540, 52 * pulse, green); cross(C, 1650, 540, 52 * pulse, red)
        fr = A_(fr, C, (1230, 260, 1820, 660), t, t3)
    t4 = 2.6
    if t > t4:
        fr = pill_pop(fr, 'HOW MUCH PER MONTH, AFTER MEDICARE?', 790, t, t4, red, size=52, cx=960)
    t5 = 3.3
    if t > t5:
        L = new(); txt(L, 'AND IS IT ENOUGH?', BOLD(56), 930, goldL, 255 * ease((t - t5) / 0.5), x=960); fr = Image.alpha_composite(fr, L)
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1]; fns = [drawA, drawB]
    sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2]
    OUT = '/tmp/claude-0/-home-user-Tr/ca75d3ba-ecb8-59f6-9dcd-864234e0ec2e/scratchpad/w7/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.15, 0.35, 0.6, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((960, 540)).save(f'{OUT}pv_{i}_{int(fq*100)}.png')
        print(FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v7-b1-0{i}.mp4'); print('done', i, f, flush=True)
