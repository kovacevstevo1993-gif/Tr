from v3lib import *
from v3b3_10 import POP, new, lerp, fly
from v3b11_21 import crown
import sys, math

S = ["Nine hundred seventy-four dollars.",
     "That is what Medicare can charge you every year for a single extra dollar of income — and the income that counts is not the one you earn at sixty-five, it's the one you report at sixty-three.",
     "Today you'll see why sixty-one is the most important age in your retirement, and reason number three surprises almost everyone."]
GROUPS = [[0, 1], [2]]
TOTF = 690

def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':') + text.count('—'))
def wpos(text, marker):
    i = text.index(marker); pre = text[:i]
    return len(pre) + 3 * (pre.count(',') + pre.count(':') + pre.count('—'))
gw = [sum(len(S[i]) + 10 for i in g) for g in GROUPS]
FS = [round(w / sum(gw) * TOTF) for w in gw]; FS[-1] = TOTF - sum(FS[:-1])
TXT = [' '.join(S[i] for i in g) for g in GROUPS]
def tt(g, marker):
    return max(0.2, wpos(TXT[g], marker) / wtot(TXT[g]) * FS[g] / 30 - 0.1)

def medicare_card(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C); w = 320 * s; h = 200 * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(18 * s), fill=A((236, 240, 245), alpha), outline=A(blue, alpha), width=5)
    d.rectangle([cx - w / 2 + 16 * s, cy - h / 2 + 16 * s, cx + w / 2 - 16 * s, cy - h / 2 + 64 * s], fill=A(blue, alpha))
    txt(C, 'MEDICARE', BOLD(int(36 * s)), cy - h / 2 + 24 * s, (255, 255, 255), alpha, x=cx)
    d.rectangle([cx - w / 2 + 28 * s, cy + 16 * s, cx - w / 2 + 84 * s, cy + 30 * s], fill=A(red, alpha))
    d.rectangle([cx - w / 2 + 49 * s, cy - 4 * s, cx - w / 2 + 63 * s, cy + 50 * s], fill=A(red, alpha))
    for k in range(3):
        d.rectangle([cx - w / 2 + 108 * s, cy + 10 * s + k * 24 * s, cx + w / 2 - 28 * s, cy + 20 * s + k * 24 * s], fill=A((150, 165, 190), alpha))

def drawA(t):
    fr = base(t)
    T = lambda m: tt(0, m)
    # hero number
    v = 974 * ease((t - 0.2) / 1.5)
    L = new()
    txt(L, '$' + str(int(round(v))), BOLD(230), 105, red, 255 * ease((t - 0.1) / 0.3), x=960)
    fr = Image.alpha_composite(fr, L)
    ty = T('every year')
    fr = pill_pop(fr, 'A YEAR', 340, t, ty, gold, navy, size=34, cx=960) if False else fr
    if t > ty:
        L = new(); txt(L, 'EVERY YEAR', BOLD(40), 350, goldL, 255 * ease((t - ty) / 0.4), x=960); fr = Image.alpha_composite(fr, L)
    # medicare card + bills
    tm = T('That is what Medicare') if False else T('what Medicare')
    if t > tm - 0.2:
        C = new(); medicare_card(C, 400, 570, 1.0); fr = POP(fr, C, (230, 460, 570, 690), back((t - tm + 0.2) / 0.5))
        L = new(); s0 = tm + 0.3
        td = T('a single extra dollar')
        while s0 < td:
            fly(L, t, s0, 1.3, (1250, 560), (560, 580), 90, 'bill', 255, 0, 0.6); s0 += 0.45
        fr = Image.alpha_composite(fr, L)
    if t > T('a single extra dollar') - 0.1:
        td = T('a single extra dollar')
        C = new(); bill(C, 1090, 600, 320, 156, 8, 255); fr = POP(fr, C, (900, 500, 1290, 700), back((t - td) / 0.5))
        L = new(); d = ImageDraw.Draw(L); u = ease((t - td - 0.4) / 0.5)
        d.line([1260, 590, 1260 - 300 * u, 590], fill=goldL + (255,), width=8)
        if u > 0.9: d.polygon([(710, 590), (760, 566), (760, 614)], fill=goldL + (255,))
        txt(L, '+ $1', BOLD(60), 660, red, 255 * ease((t - td) / 0.4), x=1090) if False else None
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'ONE EXTRA DOLLAR', 715, t, td + 0.2, red, size=36, cx=1000)
    # timeline: age 63 -> age 65
    tn = T('is not the one you earn'); t63 = T("it's the one you report")
    x0, x1, ya = 420, 1500, 890
    if t > tn - 0.2:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - tn + 0.2) / 0.6)
        d.line([x0, ya, x0 + (x1 - x0) * u, ya], fill=gold + (255,), width=4)
        d.ellipse([x1 - 18, ya - 18, x1 + 18, ya + 18], fill=A(white, 255 * u))
        txt(L, 'AGE 65', BOLD(34), ya + 26, white, 255 * u, x=x1)
        txt(L, 'INCOME YOU EARN', BOLD(26), ya - 66, grey, 255 * u, x=x1)
        fr = Image.alpha_composite(fr, L)
        C = new(); cross(C, x1, ya - 100, 30, red); fr = POP(fr, C, (x1 - 40, ya - 140, x1 + 40, ya - 60), back((t - tn - 0.6) / 0.4)) if t > tn + 0.6 else fr
    if t > t63 - 0.2:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - t63 + 0.2) / 0.5)
        d.ellipse([x0 - 22, ya - 22, x0 + 22, ya + 22], fill=A(gold, 255 * u))
        txt(L, 'AGE 63', BOLD(38), ya + 26, gold, 255 * u, x=x0)
        txt(L, 'INCOME YOU REPORT', BOLD(26), ya - 66, gold, 255 * u, x=x0)
        fr = Image.alpha_composite(fr, L)
        C = new(); tax_form(C, x0 - 50, ya - 260, 100, 120, 255, 'TAX'); fr = POP(fr, C, (x0 - 60, ya - 270, x0 + 60, ya - 130), back((t - t63 - 0.2) / 0.45))
        u2 = ease((t - t63 - 0.7) / 0.8)
        if u2 > 0:
            L = new(); d = ImageDraw.Draw(L)
            xe = lerp(x0 + 30, x1 - 30, u2)
            d.line([x0 + 30, ya - 8, xe, ya - 8], fill=red + (255,), width=10)
            txt(L, '2 YEARS LATER', BOLD(34), ya - 60, red, 255 * u2, x=(x0 + x1) / 2)
            fr = Image.alpha_composite(fr, L)
    return frame(fr)

def drawB(t):
    fr = base(t); fr = title_layer(fr, 'THE AGE THAT CHANGES EVERYTHING', t, size=58)
    T = lambda m: tt(1, m)
    t61 = T('sixty-one is'); tmi = T('the most important age'); trn = T('reason number three'); tsu = T('surprises almost everyone')
    ages = [60, 61, 62, 63, 64, 65]
    for i, a in enumerate(ages):
        st = 0.3 + i * 0.18
        if t < st: continue
        hl = (a == 61 and t > t61)
        cx = 330 + i * 252; cy = 500 - (25 if hl else 0)
        h = 100 * (1.28 if hl else 1.0)
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([cx - h, cy - h, cx + h, cy + h], radius=24, fill=A(gold if hl else card, 255), outline=A(goldL if hl else (80, 100, 130), 255), width=6 if hl else 3)
        txt(C, str(a), BOLD(int(96 * (1.28 if hl else 1.0))), cy - 62 * (1.28 if hl else 1.0), navy if hl else (150, 165, 185), 255, x=cx)
        fr = POP(fr, C, (cx - h - 10, cy - h - 10, cx + h + 10, cy + h + 10), back((t - st) / 0.35))
    if t > t61:
        C = new(); crown(C, 330 + 252, 335, 1.6); fr = POP(fr, C, (540, 240, 700, 350), back((t - t61 - 0.2) / 0.45))
        L = new(); rain(L, t, t61 + 0.2, 480, 760, 620, n=8, seed=41, r=22, dur=3.0); fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'THE MOST IMPORTANT AGE', 690, t, tmi, gold, navy, size=42)
    if t > trn - 0.2:
        for k in range(5):
            st = trn - 0.2 + k * 0.2
            if t < st: continue
            cx = 660 + k * 150; pulse = 1 + 0.08 * math.sin(t * 6) if k == 2 and t > tsu else 1
            C = new(); d = ImageDraw.Draw(C); r = 34 * pulse
            col = red if k == 2 else gold
            d.ellipse([cx - r, 850 - r, cx + r, 850 + r], fill=A(col, 255)); txt(C, str(k + 1), BOLD(40), 850 - 26, navy if k != 2 else (255, 255, 255), 255, x=cx)
            fr = POP(fr, C, (cx - 45, 800, cx + 45, 900), back((t - st) / 0.35))
        if t > tsu:
            L = new(); txt(L, '?', BOLD(80), 730, red, 255 * ease((t - tsu) / 0.3), x=960 + math.sin(t * 5) * 6); txt(L, 'THE SURPRISE', BOLD(30), 900, red, 255 * ease((t - tsu) / 0.4), x=960)
            fr = Image.alpha_composite(fr, L)
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1]
    fns = [drawA, drawB]
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            for fq in [0.15, 0.4, 0.7, 0.97]:
                fn(f / 30 * fq).convert('RGB').save(f'/home/claude/pv4_{i}_{int(fq * 100)}.png')
        print(FS)
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            render_fast(fn, f, f'/mnt/user-data/outputs/v4-b1-0{i}.mp4'); print('done', i, f, flush=True)
