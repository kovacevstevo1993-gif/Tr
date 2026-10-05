from v3lib import *
import sys, shutil

S = ["On the exact day you turn fifty-nine and a half, the IRS makes a change that could save you ten thousand dollars — or trap you into years of payments you can't stop.",
     "Today we're breaking down five things that happen the moment you hit this age, and number four surprises almost everyone, because it works backwards from what you'd expect."]
TOTF = 694
fs = frames_split(S, TOTF)
durs = fs

def drawA(t):
    fr = base(t)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    txt(L, 'THE DAY YOU TURN 59\u00bd', SER(64), 100, goldL, 255 * ease(t / 0.4))
    fr = Image.alpha_composite(fr, L)

    # calendar card (left)
    C = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
    x0, y0, x1, y1 = 150, 250, 570, 640
    cd.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=(236, 240, 245, 255))
    cd.rounded_rectangle([x0, y0, x1, y0 + 96], radius=30, fill=red + (255,)); cd.rectangle([x0, y0 + 60, x1, y0 + 96], fill=red + (255,))
    txt(C, 'BIRTHDAY', BOLD(48), y0 + 20, (255, 255, 255), 255, x=(x0 + x1) / 2)
    txt(C, 'AGE', BOLD(44), y0 + 130, (90, 100, 120), 255, x=(x0 + x1) / 2)
    p = ease((t - 0.5) / 1.4)
    age = 59.0 + 0.5 * p
    txt(C, '59\u00bd' if p > 0.98 else f'{int(age)}', BOLD(170), y0 + 190, navy, 255, x=(x0 + x1) / 2)
    bob = math.sin(t * 2.0) * 6
    C = C.transform(C.size, Image.AFFINE, (1, 0, 0, 0, 1, -bob), resample=Image.BICUBIC)
    fr = pop(fr, C, (x0 - 6, y0 - 16, x1 + 6, y1 + 16), back((t - 0.25) / 0.5))

    # IRS building + stamp (center)
    if t > 3.3:
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        s = back((t - 3.3) / 0.5)
        Cb = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        building(Cb, 960, 470, 320, 250, gold)
        txt(Cb, 'IRS', BOLD(60), 630, white, 255, x=960)
        fr = pop(fr, Cb, (760, 320, 1160, 700), s)
        fr = stamp(fr, 'NEW RULE', 1010, 330, -12, red, back((t - 3.9) / 0.45), 50)

    # money (right)
    if t > 4.9:
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        u = t - 4.9
        n = min(6, int(u / 0.35) + 1)
        coin_stack(L, 1320, 590, n, 60)
        coin_stack(L, 1450, 590, min(10, int(u / 0.22) + 1), 60)
        coin_stack(L, 1580, 590, min(4, int(u / 0.45) + 1), 60)
        bl = ease((t - 5.4) / 0.6)
        if bl > 0:
            bill(L, 1690, 520 - 20 * math.sin(t * 2.4), 200, 98, 14, 255 * bl)
            bill(L, 1250, 470 + 14 * math.sin(t * 2.0), 190, 92, -12, 255 * bl)
        rain(L, t, 4.9, 1200, 1760, 500, n=14, seed=5, r=26, dur=2.4)
        v = 10000 * ease((t - 5.2) / 1.6)
        txt(L, counter_text(v // 100 * 100), BOLD(130), 640, green, 255 * ease((t - 5.0) / 0.3), x=1490)
        txt(L, 'saved on a $100,000 withdrawal', REG(34), 790, white, 255 * ease((t - 6.4) / 0.4), x=1490)
        txt(L, 'Source: IRC \u00a772(t)', REG(26), 985, grey, 200)
        fr = Image.alpha_composite(fr, L)

    # trap: payments + padlock (bottom band)
    if t > 7.8:
        u = t - 7.8
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        dim = 0.0
        for k in range(12):
            st = k * 0.16
            if u < st:
                continue
            x = 230 + k * 118
            a = ease((u - st) / 0.25)
            d.rounded_rectangle([x, 850, x + 100, 930], radius=14, fill=A(card, 255 * a), outline=A(red, 255 * a), width=3)
            txt(L, 'PMT', BOLD(30), 868, red, 255 * a, x=x + 50)
            txt(L, '$', BOLD(26), 898, white, 255 * a, x=x + 50)
        fr = Image.alpha_composite(fr, L)
        C = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
        padlock(C, 1730, 870, 0.62, red, 255)
        fr = pop(fr, C, (1650, 760, 1810, 960), back((u - 0.4) / 0.45))
        C2 = Image.new('RGBA', (W, H), (0, 0, 0, 0)); c2 = ImageDraw.Draw(C2)
        f = BOLD(40); lab = '...OR TRAPPED IN PAYMENTS YOU CAN\'T STOP'; b = c2.textbbox((0, 0), lab, font=f); bw = b[2] - b[0] + 70; bx = (W - bw) / 2 - 40; y = 760
        c2.rounded_rectangle([bx, y, bx + bw, y + 74], radius=37, fill=red + (255,)); c2.text((bx + 35 - b[0], y + 37 - (b[3] - b[1]) / 2 - b[1]), lab, font=f, fill=(255, 255, 255, 255))
        fr = pop(fr, C2, (int(bx) - 5, y - 5, int(bx + bw) + 5, y + 79), back((u - 0.2) / 0.45))
    return frame(fr)

LAB = ['PENALTY\nGONE', 'HIDDEN\nDOOR', 'ROTH\n5-YEAR CLOCK', 'THE\nTRAP', 'BIGGER\nLIMIT']
def icon(C, k, cx, cy, t, col, a=255):
    if k == 0:
        coin(C, cx, cy, 52, a)
        d = ImageDraw.Draw(C); d.line([cx - 60, cy + 56, cx + 60, cy - 56], fill=A(red, a), width=10)
    elif k == 1:
        door(C, cx, cy, 90, 130, blue, a, open_p=(math.sin(t * 1.6) * 0.5 + 0.5))
    elif k == 2:
        clock(C, cx, cy, 58, t, purple, a)
    elif k == 3:
        padlock(C, cx, cy - 8, 0.62, red, a)
    else:
        up_arrow(C, cx, cy, 0.7, green, a)

def drawB(t):
    fr = base(t)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    txt(L, '5 THINGS THAT CHANGE AT 59\u00bd', SER(64), 100, goldL, 255 * ease(t / 0.4))
    fr = Image.alpha_composite(fr, L)
    focus = t > 5.3
    cols = [gold, blue, purple, red, green]
    for k in range(5):
        st = 0.6 + k * 0.85
        if t < st:
            continue
        cx = 300 + k * 330; cy = 440
        C = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
        dimmed = focus and k != 3
        a = 110 if dimmed else 255
        oc = red if (focus and k == 3) else cols[k]
        card_box(C, cx - 135, cy - 175, cx + 135, cy + 175, oc, card, a, 5 if not (focus and k == 3) else 8)
        icon(C, k, cx, cy - 60 + math.sin(t * 2 + k) * 5, t, cols[k], a)
        txt(C, f'#{k+1}', BOLD(68), cy + 22, oc, a, x=cx)
        for j, line in enumerate(LAB[k].split('\n')):
            txt(C, line, BOLD(28), cy + 100 + j * 34, white, a, x=cx)
        sc = back((t - st) / 0.45)
        if focus and k == 3:
            sc *= 1.0 + 0.10 * ease((t - 5.3) / 0.4) + 0.02 * math.sin(t * 5)
        fr = pop(fr, C, (cx - 150, cy - 190, cx + 150, cy + 190), sc)
    if t > 5.3:
        C = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
        f = BOLD(44); lab = 'NUMBER 4 SURPRISES ALMOST EVERYONE'; b = cd.textbbox((0, 0), lab, font=f); bw = b[2] - b[0] + 80; bx = (W - bw) / 2; y = 720
        cd.rounded_rectangle([bx, y, bx + bw, y + 92], radius=46, fill=red + (255,)); cd.text((bx + 40 - b[0], y + 46 - (b[3] - b[1]) / 2 - b[1]), lab, font=f, fill=(255, 255, 255, 255))
        fr = pop(fr, C, (int(bx) - 5, y - 5, int(bx + bw) + 5, y + 97), back((t - 5.3) / 0.45))
    if t > 8.3:
        u = t - 8.3
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        cx, cy, R = 700, 900, 44
        ang = -u * 300
        d.arc([cx - R, cy - R, cx + R, cy + R], start=ang, end=ang + 270, fill=A(goldL, 255 * ease(u / 0.3)), width=10)
        ex = cx + R * math.cos(math.radians(ang)); ey = cy + R * math.sin(math.radians(ang))
        d.ellipse([ex - 9, ey - 9, ex + 9, ey + 9], fill=A(goldL, 255 * ease(u / 0.3)))
        txt(L, 'IT WORKS BACKWARDS', BOLD(56), 862, goldL, 255 * ease(u / 0.4), x=1180)
        for k in range(3):
            q = ease((u - 0.5 - k * 0.3) / 0.3)
            txt(L, '?', BOLD(60 + k * 8), 800 - k * 12 + math.sin(t * 3 + k) * 6, red, 255 * q, x=1560 + k * 70)
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'render'
    fns = [drawA, drawB]
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, durs), 1):
            T = f / 30
            for tt in [T * 0.15, T * 0.45, T * 0.75, T * 0.97]:
                fn(tt).convert('RGB').save(f'/home/claude/pv_b1_{i}_{int(tt*10):03d}.png')
        print('preview ok', durs)
    else:
        sel = [int(x) for x in sys.argv[2:]] or [1, 2]
        for i, (fn, f) in enumerate(zip(fns, durs), 1):
            if i not in sel:
                continue
            render(fn, f / 30, f'/mnt/user-data/outputs/v3-b1-0{i}.mp4')
            print('done', i, f)
