from v3lib import *
import sys

S = ["Here's what's coming: the ten percent penalty that disappears, a hidden door inside your four-oh-one-k that most people never open, a five-year clock on your Roth IRA that can quietly cost you thousands, a trap that locks some people into payments even after fifty-nine and a half, and a bigger contribution limit that starts the same year.",
     "Stick around, because by the end you'll know exactly what to check the week you turn fifty-nine and a half."]
TOTF = 848
fs = frames_split(S, TOTF)
durs = fs
D1 = fs[0] / 30.0

def wpos(text, marker):
    # weighted char position (commas/colons add a small pause)
    i = text.index(marker)
    pre = text[:i]
    return len(pre) + 3 * (pre.count(',') + pre.count(':'))
def wtot(text):
    return len(text) + 3 * (text.count(',') + text.count(':'))
marks = ["the ten percent", "a hidden door", "a five-year clock", "a trap that", "and a bigger"]
ST = [max(0.5, wpos(S[0], m) / wtot(S[0]) * D1 - 0.1) for m in marks]

ROWS = [
    ('THE 10% PENALTY DISAPPEARS', 'gone at 59 1/2', green, gold),
    ('A HIDDEN DOOR INSIDE YOUR 401(k)', 'most people never open it', grey, blue),
    ('A 5-YEAR CLOCK ON YOUR ROTH IRA', 'can quietly cost you thousands', red, purple),
    ('A TRAP THAT LOCKS YOU INTO PAYMENTS', 'even after 59 1/2', red, red),
    ('A BIGGER CONTRIBUTION LIMIT', 'starts the same year', green, green),
]
RW, RH = 1300, 118

def row_icon(C, k, cx, cy, t, col):
    if k == 0:
        coin(C, cx, cy, 40, 255)
        ImageDraw.Draw(C).line([cx - 46, cy + 42, cx + 46, cy - 42], fill=A(red, 255), width=8)
    elif k == 1:
        door(C, cx, cy, 66, 92, blue, 255, open_p=(math.sin(t * 1.8) * 0.5 + 0.5))
    elif k == 2:
        clock(C, cx, cy, 42, t, purple, 255)
    elif k == 3:
        padlock(C, cx, cy - 6, 0.46, red, 255)
    else:
        up_arrow(C, cx, cy, 0.5, green, 255)

def floaters(fr, t):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for j in range(3):
        y = 1000 - ((t * 60 + j * 330) % 1000) + 40
        a = 255 * min(1, (y - 120) / 100) * min(1, (940 - y) / 100)
        if a > 0:
            bill(L, 190 + 22 * math.sin(t * 1.3 + j), y, 170, 82, 20 * math.sin(t * 1.1 + j), a)
            coin(L, 1735 + 20 * math.sin(t * 1.5 + j), 1000 - ((t * 70 + j * 300 + 150) % 1000) + 40, 30, a, squash=abs(math.cos(t * 3 + j)) * 0.6 + 0.4)
    return Image.alpha_composite(fr, L)

def drawA(t):
    fr = base(t)
    fr = floaters(fr, t)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    txt(L, "HERE'S WHAT'S COMING", SER(64), 90, goldL, 255 * ease(t / 0.4))
    fr = Image.alpha_composite(fr, L)
    for k, (lab, sub, subcol, col) in enumerate(ROWS):
        u = t - ST[k]
        if u < 0:
            continue
        C = Image.new('RGBA', (RW, RH), (0, 0, 0, 0)); d = ImageDraw.Draw(C)
        a = 255 * ease(u / 0.3)
        hot = u < 1.8
        d.rounded_rectangle([4, 4, RW - 5, RH - 5], radius=26, fill=A(card, a), outline=A(goldL if hot else col, a), width=8 if hot else 4)
        d.ellipse([28, 24, 98, 94], fill=A(col, a))
        f = BOLD(46); b = d.textbbox((0, 0), str(k + 1), font=f)
        d.text((63 - (b[2] - b[0]) / 2 - b[0], 59 - (b[3] - b[1]) / 2 - b[1]), str(k + 1), font=f, fill=A(navy, a))
        d.text((130, 14), lab, font=BOLD(40), fill=A(white, a))
        d.text((130, 68), sub, font=REG(30), fill=A(subcol, a))
        row_icon(C, k, RW - 90, RH / 2, t, col)
        dx = int((1 - ease(u / 0.45)) * 420)
        y0 = 190 + k * 132
        fr.alpha_composite(C, (310 + dx, y0))
    # burst of coins when the penalty row / limit row lands
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    if 0 <= t - ST[0] < 2.2:
        rain(L, t, ST[0], 1660, 1780, 330, n=6, seed=11, r=20, dur=1.2)
    if 0 <= t - ST[4] < 2.6:
        rain(L, t, ST[4], 1660, 1780, 840, n=8, seed=13, r=20, dur=1.4)
    fr = Image.alpha_composite(fr, L)
    return frame(fr)

CHK = ['In-service withdrawals allowed?', 'Roth IRA 5-year clock', 'SEPP payment deadline', 'Higher catch-up limit', 'Get every number in writing']
D2 = fs[1] / 30.0

def drawB(t):
    fr = base(t)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    txt(L, 'STICK AROUND', SER(66), 88, goldL, 255 * ease(t / 0.35))
    # video progress bar
    d.rounded_rectangle([300, 212, 1620, 230], radius=9, fill=(40, 62, 92, 255))
    p = min(1.0, t / (D2 - 0.3))
    xe = 300 + 1320 * p
    d.rounded_rectangle([300, 212, max(312, xe), 230], radius=9, fill=gold + (255,))
    d.ellipse([xe - 16, 204, xe + 16, 238], fill=goldL + (255,))
    txt(L, 'START', REG(28), 244, grey, 220, x=300, anchor='l')
    txt(L, 'END OF THE VIDEO', REG(28), 244, grey, 220, x=1620, anchor='r')
    fr = Image.alpha_composite(fr, L)
    unlock = 5.0
    # checklist card
    if t > 0.9:
        C = Image.new('RGBA', (860, 500), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
        cd.rounded_rectangle([4, 4, 855, 495], radius=30, fill=A(card, 255), outline=A(gold, 255), width=5)
        for k, lab in enumerate(CHK):
            st = 1.1 + k * 0.28
            if t < st:
                continue
            a = 255 * ease((t - st) / 0.3)
            y = 26 + k * 92
            un = t > unlock + k * 0.18
            cd.rounded_rectangle([26, y, 834, y + 76], radius=18, outline=A(green if un else (80, 100, 130), a), width=3, fill=A((30, 52, 80), a * 0.6))
            cd.text((110, y + 20), lab, font=BOLD(34), fill=A(white if un else (150, 165, 185), a))
            if un:
                check(C, 62, y + 38, 24, green, a)
            else:
                padlock(C, 62, y + 40, 0.3, gold, a)
        fr = pop(fr, C, (0, 0, 860, 500), 1.0) if False else fr
        fr.alpha_composite(C, (290, 290))
    # pill
    if t > 2.4:
        C = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
        f = BOLD(44); lab = "YOU'LL KNOW EXACTLY WHAT TO CHECK"; b = cd.textbbox((0, 0), lab, font=f); bw = b[2] - b[0] + 80; bx = (W - bw) / 2; y = 838
        cd.rounded_rectangle([bx, y, bx + bw, y + 92], radius=46, fill=gold + (255,)); cd.text((bx + 40 - b[0], y + 46 - (b[3] - b[1]) / 2 - b[1]), lab, font=f, fill=navy + (255,))
        fr = pop(fr, C, (int(bx) - 5, y - 5, int(bx + bw) + 5, y + 97), back((t - 2.4) / 0.45))
    # week calendar (right)
    if t > 3.9:
        C = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
        x0, y0, x1, y1 = 1190, 290, 1640, 790
        cd.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=(236, 240, 245, 255))
        cd.rounded_rectangle([x0, y0, x1, y0 + 80], radius=30, fill=red + (255,)); cd.rectangle([x0, y0 + 50, x1, y0 + 80], fill=red + (255,))
        txt(C, 'THE WEEK YOU TURN', BOLD(36), y0 + 18, (255, 255, 255), 255, x=(x0 + x1) / 2)
        age59(C, (x0 + x1) / 2, y0 + 120, 150, navy)
        days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
        for k, dd in enumerate(days):
            xx = x0 + 30 + k * 57
            hl = (k == 3)
            cd.rounded_rectangle([xx, y0 + 340, xx + 47, y0 + 420], radius=10, fill=(gold if hl else (205, 212, 224)) + (255,))
            txt(C, dd, BOLD(30), y0 + 366, navy, 255, x=xx + 23)
        txt(C, 'CHECK THIS WEEK', BOLD(30), y0 + 440, (90, 100, 120), 255, x=(x0 + x1) / 2)
        sc = back((t - 3.9) / 0.5) * (1 + 0.012 * math.sin(t * 4))
        fr = pop(fr, C, (x0 - 6, y0 - 6, x1 + 6, y1 + 6), sc)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    if t > unlock:
        rain(L, t, unlock, 130, 260, 800, n=6, seed=21, r=22, dur=1.4)
        rain(L, t, unlock, 1670, 1790, 800, n=6, seed=22, r=22, dur=1.4)
    fr = Image.alpha_composite(fr, L)
    return frame(fr)

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'render'
    fns = [drawA, drawB]
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, durs), 1):
            T = f / 30
            for tt in [T * 0.12, T * 0.4, T * 0.7, T * 0.97]:
                fn(tt).convert('RGB').save(f'/home/claude/pv_b2_{i}_{int(tt*10):03d}.png')
        print('preview ok', durs, [round(x, 1) for x in ST], round(D1, 1), round(D2, 1))
    else:
        sel = [int(x) for x in sys.argv[2:]] or [1, 2]
        for i, (fn, f) in enumerate(zip(fns, durs), 1):
            if i not in sel:
                continue
            render(fn, f / 30, f'/mnt/user-data/outputs/v3-b2-0{i}.mp4')
            print('done', i, f)
