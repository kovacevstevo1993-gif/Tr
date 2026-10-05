from v3lib import *
from v3b3_10 import POP, new, lerp, person_box
from v4b2_10 import eye
from v5b1 import amb, sparks, shake
from v5lib import paycheck
from v6b1 import A_, E_, chip_src
import sys, math

S = ["Welcome to The Money Backstory, where we explain retirement for Americans over fifty, using official numbers.",
     "To keep this simple, we will follow two retired coworkers, Frank and Mary.",
     "Both are single, and both receive exactly the average Social Security check, two thousand seventy one dollars a month.",
     "The only difference is that Frank also has a small pension, and Mary does not. Watch what the raise does to each of them."]
TOTF = 765   # 1622 - 857: fine voce blocco 2 = 00:54 + 2f (screenshot utente)
def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':'))
gw = [len(s) + 10 for s in S]
FS = [round(w / sum(gw) * TOTF) for w in gw]; FS[-1] = TOTF - sum(FS[:-1])
def tt(g, marker):
    s = S[g]; i = s.index(marker)
    return max(0.2, wtot(s[:i]) / wtot(s) * FS[g] / 30 - 0.1)

def chip(fr, text, cx, y, t, t0, col=goldL, size=44, fillc=None, tcol=None):
    if t < t0: return fr
    C = new(); d = ImageDraw.Draw(C); f = BOLD(size); b = d.textbbox((0, 0), text, font=f)
    w = b[2] - b[0] + 70; h = size * 1.9
    d.rounded_rectangle([cx - w / 2, y, cx + w / 2, y + h], radius=int(h / 2), fill=(fillc or card) + (255,), outline=col + (255,), width=4)
    d.text((cx - (b[2] - b[0]) / 2 - b[0], y + h / 2 - (b[3] - b[1]) / 2 - b[1]), text, font=f, fill=(tcol or col) + (255,))
    return A_(fr, C, (cx - w / 2 - 10, y - 10, cx + w / 2 + 10, y + h + 10), t, t0, 0.5)

def logo(C, cx, cy, r):
    d = ImageDraw.Draw(C)
    d.ellipse([cx - r - 14, cy - r - 14, cx + r + 14, cy + r + 14], fill=goldD + (255,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(14, 30, 52, 255), outline=gold + (255,), width=10)
    d.ellipse([cx - r + 24, cy - r + 24, cx + r - 24, cy + r - 24], outline=goldL + (255,), width=3)
    txt(C, 'MB', SER(int(r * 0.95)), cy - r * 0.62, goldL, 255, x=cx)
    for k, h_ in enumerate([0.22, 0.34, 0.5]):
        x0 = cx - r * 0.45 + k * r * 0.34
        d.rectangle([x0, cy + r * 0.62 - r * h_, x0 + r * 0.22, cy + r * 0.62], fill=gold + (255,))

def drawA(t):
    fr = base(t); fr = amb(fr, t, 6, 7, 55)
    T = lambda m: tt(0, m)
    t1 = 0.3
    if t > t1:
        C = new(); logo(C, 480, 500, 190)
        fr = A_(fr, C, (250, 270, 710, 730), t, t1)
    t2 = T('where we explain')
    if t > t2:
        C = new()
        txt(C, 'THE MONEY BACKSTORY', SER(68), 290, goldL, 255, x=1230)
        txt(C, 'RETIREMENT EXPLAINED', BOLD(60), 420, white, 255, x=1230)
        txt(C, 'FOR AMERICANS OVER 50', BOLD(60), 500, white, 255, x=1230)
        fr = A_(fr, C, (760, 250, 1700, 600), t, t2)
    t3 = T('using official numbers')
    if t > t3:
        for k, (lab, x) in enumerate([('SSA.GOV', 880), ('MEDICARE.GOV', 1230), ('IRS.GOV', 1560)]):
            fr = chip(fr, lab, x, 660, t, t3 + 0.2 * k, goldL, 44)
        fr = pill_pop(fr, 'OFFICIAL NUMBERS ONLY', 800, t, t3 + 0.7, green, tcol=navy, size=54, cx=1230)
    return frame(fr)

def drawB(t):
    fr = base(t); fr = amb(fr, t, 7, 7, 55); fr = title_layer(fr, 'MEET OUR TWO RETIREES', t, size=64)
    T = lambda m: tt(1, m)
    tf = T('Frank and Mary') - 0.4
    fr = person_box(fr, 'FRANK', 560, 470, blue, t, 0.3, s=4.0)
    if t > T('Frank and Mary') - 0.2:
        fr = person_box(fr, 'MARY', 1360, 470, pink, t, T('Frank and Mary') - 0.2, s=4.0)
    t2 = T('two retired')
    fr = pill_pop(fr, 'TWO RETIRED COWORKERS', 830, t, 0.9, goldL, tcol=navy, size=54, cx=960)
    L = new(); txt(L, '&', BOLD(120), 440, goldL, 255 * E_(t, T('Frank and Mary') - 0.1), x=960); fr = Image.alpha_composite(fr, L)
    return frame(fr)

def drawC(t):
    fr = base(t); fr = amb(fr, t, 8, 6, 55); fr = title_layer(fr, 'SAME CHECK, SAME AMOUNT', t, size=64)
    T = lambda m: tt(2, m)
    t1 = 0.35
    if t > t1:
        C = new(); paycheck(C, 150, 280, 810, 640, blue, '$2,071', 'PER MONTH', 'FRANK: SOCIAL SECURITY', 140)
        fr = A_(fr, C, (130, 260, 830, 660), t, t1)
    t2 = T('both receive') + 0.1
    if t > t2:
        C = new(); paycheck(C, 1110, 280, 1770, 640, pink, '$2,071', 'PER MONTH', 'MARY: SOCIAL SECURITY', 140)
        fr = A_(fr, C, (1090, 260, 1790, 660), t, t2)
        L = new(); txt(L, '=', BOLD(190), 380, goldL, 255 * E_(t, t2 + 0.3), x=960); fr = Image.alpha_composite(fr, L)
    t3 = T('exactly the average')
    fr = pill_pop(fr, 'BOTH SINGLE', 700, t, T('Both are single') if False else 0.9, goldL, tcol=navy, size=50, cx=960)
    if t > t3:
        fr = pill_pop(fr, 'EXACTLY THE AVERAGE CHECK: $2,071 A MONTH', 830, t, t3, green, tcol=navy, size=52, cx=960)
    fr = chip_src(fr, 'AVERAGE RETIRED WORKER CHECK, 2026: SSA.GOV', 945, t, t3 + 0.6)
    return frame(fr)

def drawD(t):
    fr = base(t); fr = amb(fr, t, 9, 6, 55); fr = title_layer(fr, 'THE ONLY DIFFERENCE', t, size=64)
    T = lambda m: tt(3, m)
    t1 = 0.35
    if t > t1:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([140, 240, 900, 700], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        avatar(C, 290, 420, blue, 2.6); txt(C, 'FRANK', BOLD(60), 560, blue, 255, x=290)
        bill(C, 600, 370, 230, 112, 0, 255); txt(C, 'SOCIAL SECURITY', BOLD(38), 450, white, 255, x=600)
        fr = A_(fr, C, (120, 220, 920, 720), t, t1)
    t2 = T('Frank also has')
    if t > t2:
        C = new(); coin_stack(C, 820, 620, 6, 66)
        txt(C, 'SMALL PENSION', BOLD(46), 640, goldL, 255, x=555)
        fr = A_(fr, C, (330, 440, 920, 710), t, t2)
        fr = chip(fr, 'CHECK + PENSION', 520, 730, t, t2 + 0.3, goldL, 44)
    t3 = T('and Mary does not')
    if t > t3:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([1020, 240, 1780, 700], radius=34, fill=card + (255,), outline=pink + (255,), width=6)
        avatar(C, 1170, 420, pink, 2.6); txt(C, 'MARY', BOLD(60), 560, pink, 255, x=1170)
        bill(C, 1480, 370, 230, 112, 0, 255); txt(C, 'SOCIAL SECURITY', BOLD(38), 450, white, 255, x=1480)
        cross(C, 1380, 610, 40, red); txt(C, 'NO PENSION', BOLD(46), 585, grey, 255, x=1580)
        fr = A_(fr, C, (1000, 220, 1800, 720), t, t3)
        fr = chip(fr, 'CHECK ONLY', 1400, 730, t, t3 + 0.3, pink, 44)
    t4 = T('Watch what')
    if t > t4:
        fr = pill_pop(fr, 'WATCH WHAT THE RAISE DOES TO EACH', 860, t, t4, red, size=48, cx=960)
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1]; fns = [drawA, drawB, drawC, drawD]
    sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2, 3, 4]
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.2, 0.5, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}pv2_{i}_{int(fq*100)}.png')
        print(FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b2-0{i}.mp4'); print('done', i, f, flush=True)
