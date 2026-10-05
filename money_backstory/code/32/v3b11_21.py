from v3lib import *
from v3b3_10 import POP, new, lerp, fly, rot_arrow, person_box
import sys, math

SENT = {
 11: ["Frank opened his Roth IRA three years ago, at age fifty-six.", "Even though he's about to turn fifty-nine and a half, if he withdraws the earnings now, before the five-year mark, he'll still owe tax on that portion.", "Age alone is not enough — the five-year clock has to be satisfied too."],
 12: ["That five-year rule is the difference between a completely tax-free withdrawal and a tax bill that can run into the thousands, depending on how much those earnings have grown."],
 13: ["Now here's the twist that surprises almost everyone — the fourth change actually works in reverse.", "If someone started what's called substantially equal periodic payments, or SEPP, from a retirement account before fifty-nine and a half, turning fifty-nine and a half does not automatically let them stop."],
 14: ["The IRS requires those payments to continue for the longer of two things: five full years, or until the person turns fifty-nine and a half.", "So if Mary had started these payments at age fifty-six, she would have to keep taking them until age sixty-one — three years past this milestone — not stop the moment she hits fifty-nine and a half."],
 15: ["Stopping early, or changing the payment amount before that window closes, triggers the ten percent penalty retroactively, on every payment already taken — sometimes going back years.", "It's one of the most expensive mistakes in early retirement planning, and it happens because people assume fifty-nine and a half is a universal reset button."],
 16: ["The fifth change isn't about withdrawing money — it's about putting more in.", "Starting the year someone turns fifty, the IRS allows catch-up contributions on top of the normal four-oh-one-k limit.", "For twenty twenty-six, the standard limit is twenty-four thousand five hundred dollars, and the catch-up adds eight thousand dollars on top."],
 17: ["That means someone fifty or older can contribute up to thirty-two thousand five hundred dollars into a four-oh-one-k in twenty twenty-six alone.", "And workers turning sixty, sixty-one, sixty-two, or sixty-three get an even bigger catch-up, allowing up to thirty-five thousand seven hundred fifty dollars in that same year."],
 18: ["The difference between the normal limit and the highest catch-up is over eleven thousand dollars a year — money that, invested for just a few years before retirement, can add tens of thousands to a nest egg."],
 19: ["So here's where Frank and Mary end up.", "Frank assumed fifty-nine and a half meant total freedom — no penalties, no rules, nothing left to check.", "Mary treated it as a checklist: she confirmed her plan's in-service withdrawal rules, tracked her Roth's five-year clock, and used the higher catch-up limit to add thousands more before retiring.", "Same age, same law — completely different outcome."],
 20: ["So here's what to actually do the week you turn fifty-nine and a half.", "One: confirm with your plan administrator whether in-service withdrawals are allowed.", "Two: check the exact opening date of any Roth IRA, to know if the five-year rule is satisfied.", "Three: if you started SEPP payments early, calculate whether your longer deadline is five years or fifty-nine and a half.", "Four: if you're still working, ask about the higher catch-up contribution limits.", "Five: before touching any account, get the numbers in writing from your plan or a fiduciary advisor — verbal answers change, paperwork doesn't."],
 21: ["Fifty-nine and a half opens some doors and keeps others locked longer than people expect.", "If you want to see the other age that changes everything for Social Security, and the exact math behind claiming at sixty-two versus seventy, that video is linked right here."],
}
FRAMES = {11: 640, 12: 332, 13: 664, 14: 727, 15: 717, 16: 615, 17: 602, 18: 410, 19: 910, 20: 1272, 21: 513}
GROUPS = {11: [[0], [1], [2]], 12: [[0]], 13: [[0], [1]], 14: [[0], [1]], 15: [[0], [1]], 16: [[0], [1], [2]], 17: [[0], [1]], 18: [[0]], 19: [[0], [1], [2], [3]], 20: [[0], [1], [2], [3], [4], [5]], 21: [[0], [1]]}

def wtot(text): return len(text) + 3 * (text.count(',') + text.count(':') + text.count('—'))
def wpos(text, marker):
    i = text.index(marker); pre = text[:i]
    return len(pre) + 3 * (pre.count(',') + pre.count(':') + pre.count('—'))
TXT, DUR = {}, {}
for b in SENT:
    gw = [sum(len(SENT[b][i]) + 10 for i in g) for g in GROUPS[b]]
    T_ = sum(gw); fs = [round(w / T_ * FRAMES[b]) for w in gw]; fs[-1] = FRAMES[b] - sum(fs[:-1])
    DUR[b] = fs; TXT[b] = [' '.join(SENT[b][i] for i in g) for g in GROUPS[b]]
def tt(b, g, marker):
    return max(0.2, wpos(TXT[b][g], marker) / wtot(TXT[b][g]) * DUR[b][g] / 30 - 0.1)
def SRC(fr, text):
    L = new(); txt(L, text, REG(26), 985, grey, 200); return Image.alpha_composite(fr, L)

def rot_arrow_ccw(C, cx, cy, R, ang, span, col, w=14, alpha=255):
    d = ImageDraw.Draw(C); d.arc([cx - R, cy - R, cx + R, cy + R], start=ang, end=ang + span, fill=A(col, alpha), width=w)
    s = math.radians(ang); tip = (cx + R * math.cos(s), cy + R * math.sin(s)); tg = (math.sin(s), -math.cos(s)); nm = (math.cos(s), math.sin(s))
    d.polygon([(tip[0] + tg[0] * 34, tip[1] + tg[1] * 34), (tip[0] + nm[0] * 24, tip[1] + nm[1] * 24), (tip[0] - nm[0] * 24, tip[1] - nm[1] * 24)], fill=A(col, alpha))

def stop_sign(C, cx, cy, r, alpha=255, label='STOP'):
    d = ImageDraw.Draw(C)
    pts = [(cx + r * math.cos(math.radians(22.5 + 45 * k)), cy + r * math.sin(math.radians(22.5 + 45 * k))) for k in range(8)]
    d.polygon(pts, fill=A(red, alpha), outline=A((255, 255, 255), alpha)); d.line(pts + [pts[0]], fill=A((255, 255, 255), alpha), width=6)
    txt(C, label, BOLD(int(r * 0.6)), cy - r * 0.32, (255, 255, 255), alpha, x=cx)

def crown(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C)
    pts = [(-40, 0), (-40, -50), (-20, -25), (0, -60), (20, -25), (40, -50), (40, 0)]
    d.polygon([(cx + x * s, cy + y * s) for x, y in pts], fill=A(gold, alpha), outline=A(goldL, alpha))

def egg(C, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(C)
    d.ellipse([cx - 70 * s, cy - 95 * s, cx + 70 * s, cy + 85 * s], fill=A((250, 232, 190), alpha), outline=A(gold, alpha), width=5)
    txt(C, '$', BOLD(int(90 * s)), cy - 48 * s, goldD, alpha, x=cx)

def rail(fr, cur, t):
    C = new(); d = ImageDraw.Draw(C)
    for k in range(5):
        cx = 660 + k * 150; done = k + 1 < cur; now = k + 1 == cur
        col = green if done else (gold if now else (60, 80, 110))
        d.ellipse([cx - 24, 905, cx + 24, 953], fill=A(col, 255), outline=A(goldL if now else col, 255), width=3)
        txt(C, str(k + 1), BOLD(28), 913, navy if (done or now) else grey, 255, x=cx)
        if k < 4: d.line([cx + 30, 929, cx + 120, 929], fill=A((60, 80, 110), 255), width=4)
    return Image.alpha_composite(fr, C)

def year_boxes(fr, t, x_c, y0, n, filled, t0, step=0.25, w=170, h=130, gap=30, labels=True):
    tot = n * w + (n - 1) * gap; xs = x_c - tot / 2
    for k in range(n):
        st = t0 + k * step
        if t < st: continue
        C = new(); d = ImageDraw.Draw(C); x = xs + k * (w + gap)
        on = k < filled
        d.rounded_rectangle([x, y0, x + w, y0 + h], radius=18, fill=A(gold if on else card, 255), outline=A(gold, 255), width=4)
        txt(C, f'YEAR {k + 1}', BOLD(30), y0 + 14, navy if on else grey, 255, x=x + w / 2)
        if on: check(C, x + w / 2, y0 + 82, 28, green)
        fr = POP(fr, C, (x - 6, y0 - 6, x + w + 6, y0 + h + 6), back((t - st) / 0.4))
    return fr

# ================= BLOCK 11 =================
def b11a(t):
    fr = base(t); fr = title_layer(fr, 'FRANK OPENS A ROTH IRA', t, size=58)
    T = lambda m: tt(11, 0, m)
    x0, x1, ya = 360, 1560, 680; ax = lambda a: x0 + (a - 55) / 5 * (x1 - x0)
    L = new(); d = ImageDraw.Draw(L)
    d.line([x0, ya, x1, ya], fill=gold + (255,), width=3)
    for a in range(55, 61):
        d.line([ax(a), ya - 8, ax(a), ya + 8], fill=gold + (255,), width=3); txt(L, str(a), REG(30), ya + 16, grey, 255, x=ax(a))
    txt(L, 'AGE', BOLD(26), ya + 58, grey, 255, x=(x0 + x1) / 2)
    fr = Image.alpha_composite(fr, L)
    C = new(); card_box(C, ax(56) - 170, 330, ax(56) + 170, 520, gold, card, 255, 5); txt(C, 'ROTH IRA', BOLD(48), 350, gold, 255, x=ax(56)); txt(C, 'OPENED', BOLD(34), 420, white, 255, x=ax(56)); coin(C, ax(56), 480, 22, 255)
    fr = POP(fr, C, (ax(56) - 180, 320, ax(56) + 180, 530), back((t - 0.3) / 0.5))
    a = T('three years ago')
    if t > a:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - a) / 2.4)
        px = lerp(ax(56), ax(59), u); d.line([ax(56), ya, px, ya], fill=green + (255,), width=10); d.ellipse([px - 16, ya - 16, px + 16, ya + 16], fill=green + (255,))
        txt(L, '3 YEARS AGO', BOLD(44), 560, green, 255 * ease((t - a) / 0.4), x=(ax(56) + ax(59)) / 2)
        fr = Image.alpha_composite(fr, L)
    b = T('at age fifty-six')
    if t > b: fr = pill_pop(fr, 'AGE 56', 770, t, b, gold, navy, size=34, cx=ax(56))
    if t > 2.6:
        C = new(); avatar(C, ax(59), 590, blue, 1.4); fr = POP(fr, C, (ax(59) - 70, 520, ax(59) + 70, 660), back((t - 2.6) / 0.4))
        fr = pill_pop(fr, 'NOW', 770, t, 2.7, blue, size=34, cx=ax(59))
    return frame(fr)

def b11b(t):
    fr = base(t); fr = title_layer(fr, 'BEFORE THE FIVE-YEAR MARK', t, size=58)
    T = lambda m: tt(11, 1, m)
    fr = year_boxes(fr, t, 960, 230, 5, 3, 0.3)
    a = T("he's about to turn")
    if t > a:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([130, 210, 330, 410], fill=gold + (255,)); age59(C, 230, 268, 74, navy); txt(C, 'ABOUT TO TURN', BOLD(22), 250, navy, 255, x=230) if False else None
        fr = POP(fr, C, (120, 200, 340, 420), back((t - a) / 0.5))
    C = new(); card_box(C, 300, 520, 760, 760, gold, card, 255, 5); txt(C, 'ROTH IRA', BOLD(50), 535, gold, 255, x=530); txt(C, 'EARNINGS', BOLD(34), 690, green, 255, x=530); coin_stack(C, 530, 665, 4, 40)
    fr = POP(fr, C, (290, 510, 770, 770), back((t - 1.2) / 0.5))
    w = T('if he withdraws')
    if t > w:
        L = new(); d = ImageDraw.Draw(L); d.line([790, 640, 1260, 640], fill=goldL + (255,), width=8); d.polygon([(1290, 640), (1256, 618), (1256, 662)], fill=goldL + (255,))
        s0 = w
        while s0 < DUR[11][1] / 30 - 0.4:
            fly(L, t, s0, 1.2, (790, 640), (1290, 640), 60, 'bill', 255, 0, 0.7); s0 += 0.5
        fr = Image.alpha_composite(fr, L)
    m = T('before the five-year')
    if t > m:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - m) / 0.4)
        d.rounded_rectangle([1135, 215, 1515, 375], radius=22, outline=A(red, 255 * u), width=8)
        txt(L, 'NOT YET', BOLD(40), 392, red, 255 * u, x=1325); fr = Image.alpha_composite(fr, L)
    o = T("he'll still owe")
    if t > o:
        C = new(); tax_form(C, 1330, 520, 210, 240, 255, 'TAX'); fr = POP(fr, C, (1320, 510, 1550, 770), back((t - o) / 0.45))
        fr = pill_pop(fr, 'TAX DUE ON EARNINGS', 810, t, o + 0.2, red, size=42, cx=1140)
    return frame(fr)

def b11c(t):
    fr = base(t); fr = title_layer(fr, 'TWO CONDITIONS', t)
    T = lambda m: tt(11, 2, m)
    C = new(); card_box(C, 330, 300, 900, 760, green, card, 255, 6); txt(C, 'AGE', BOLD(44), 340, white, 255, x=615); txt(C, '59\u00bd', SER(150), 410, gold, 255, x=615); check(C, 615, 650, 50, green)
    fr = POP(fr, C, (320, 290, 910, 770), back((t - 0.3) / 0.5))
    a = T('the five-year clock')
    if t > a:
        C = new(); card_box(C, 1020, 300, 1590, 760, red, card, 255, 6); txt(C, 'FIVE-YEAR CLOCK', BOLD(40), 340, white, 255, x=1305); clock(C, 1305, 510, 100, t, goldL, 255); cross(C, 1305, 675, 42, red)
        fr = POP(fr, C, (1010, 290, 1600, 770), back((t - a) / 0.5))
    b = T('has to be satisfied')
    if t > b:
        C = new(); txt(C, '+', BOLD(120), 480, gold, 255, x=960); fr = POP(fr, C, (900, 460, 1020, 620), back((t - b) / 0.4))
        fr = pill_pop(fr, 'BOTH ARE REQUIRED', 810, t, b + 0.3, gold, navy, size=46)
    return frame(fr)

# ================= BLOCK 12 =================
def b12(t):
    fr = base(t); fr = title_layer(fr, 'THE 5-YEAR RULE', t)
    T = lambda m: tt(12, 0, m)
    a = T('completely tax-free'); b = T('a tax bill'); c = T('depending on how much')
    if t > a - 0.4:
        C = new(); card_box(C, 240, 260, 770, 780, green, card, 255, 6); txt(C, 'TAX-FREE WITHDRAWAL', BOLD(38), 285, white, 255, x=505); txt(C, '$0', BOLD(170), 380, green, 255, x=505); txt(C, 'TAX', BOLD(60), 570, green, 255, x=505); coin_stack(C, 505, 730, 5, 50)
        fr = POP(fr, C, (230, 250, 780, 790), back((t - a + 0.4) / 0.5))
    if t > b - 0.3:
        C = new(); card_box(C, 1150, 260, 1680, 780, red, card, 255, 6); txt(C, 'TAX BILL', BOLD(44), 285, white, 255, x=1415); tax_form(C, 1330, 360, 170, 200, 255, 'TAX')
        txt(C, 'CAN RUN INTO', BOLD(34), 600, white, 255, x=1415); txt(C, 'THE THOUSANDS', BOLD(44), 645, red, 255, x=1415)
        fr = POP(fr, C, (1140, 250, 1690, 790), back((t - b + 0.3) / 0.5))
    if t > c - 0.5:
        L = new(); d = ImageDraw.Draw(L)
        for i, v in enumerate([50, 80, 120, 170, 230, 300]):
            h = v * ease((t - c + 0.4 - i * 0.25) / 0.7)
            if h > 2: d.rounded_rectangle([810 + i * 52, 780 - h, 850 + i * 52, 780], radius=8, fill=green + (255,))
        d.line([800, 780, 1130, 780], fill=gold + (255,), width=3)
        txt(L, 'EARNINGS GROWN', BOLD(28), 800, white, 255 * ease((t - c) / 0.4), x=965)
        u = ease((t - c) / 2.4); d.rounded_rectangle([1200, 700, 1200 + 430 * u, 740], radius=14, fill=red + (255,))
        fr = Image.alpha_composite(fr, L)
    return frame(fr)

# ================= BLOCK 13 =================
def b13a(t):
    fr = base(t); fr = title_layer(fr, 'THE TWIST', t, col=red)
    C = new(); card_box(C, 700, 300, 1220, 640, red, card, 255, 8); txt(C, '#4', BOLD(190), 320, red, 255, x=960); padlock(C, 960, 590, 0.5, red, 255)
    fr = POP(fr, C, (690, 290, 1230, 650), back((t - 0.3) / 0.5))
    a = tt(13, 0, 'works in reverse')
    L = new()
    if t > a - 0.5: rot_arrow_ccw(L, 960, 470, 350, -t * 220, 230, goldL, 14, 255 * ease((t - a + 0.5) / 0.4))
    for k in range(6):
        xx = 1800 - ((t * 260 + k * 320) % 1800); coin(L, xx, 232, 24, 255 if xx > 120 else 0, squash=abs(math.cos(t * 4 + k)) * 0.6 + 0.4)
    fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'IT WORKS IN REVERSE', 690, t, a, gold, navy, size=44)
    b = tt(13, 0, 'surprises almost everyone')
    fr = pill_pop(fr, 'SURPRISES ALMOST EVERYONE', 810, t, b, red, size=44)
    return frame(fr)

def b13b(t):
    fr = base(t); fr = title_layer(fr, 'SEPP PAYMENTS', t)
    T = lambda m: tt(13, 1, m)
    x0, x1, ya = 300, 1620, 720; ax = lambda a: x0 + (a - 54) / 9 * (x1 - x0)
    L = new(); d = ImageDraw.Draw(L)
    d.line([x0, ya, x1, ya], fill=gold + (255,), width=3)
    for a in range(54, 64):
        d.line([ax(a), ya - 8, ax(a), ya + 8], fill=gold + (255,), width=3); txt(L, str(a), REG(30), ya + 16, grey, 255, x=ax(a))
    fr = Image.alpha_composite(fr, L)
    s = T('If someone started'); sp = T('substantially equal'); bf = T('before fifty-nine'); tu = T('turning fifty-nine'); ns = T('does not automatically')
    if t > s:
        C = new(); avatar(C, ax(56), 470, gold, 1.3); txt(C, 'STARTS SEPP', BOLD(30), 540, gold, 255, x=ax(56)); fr = POP(fr, C, (ax(56) - 110, 400, ax(56) + 110, 580), back((t - s) / 0.45))
    if t > sp: fr = pill_pop(fr, 'SUBSTANTIALLY EQUAL PERIODIC PAYMENTS', 190, t, sp, purple, size=34)
    xj = ax(59.5)
    if t > bf:
        L = new(); d = ImageDraw.Draw(L)
        for k in range(0, 30):
            y = 300 + k * 14
            if k % 2 == 0 and y < ya: d.line([xj, y, xj, y + 8], fill=goldL + (230,), width=3)
        txt(L, '59\u00bd', SER(56), 240, goldL, 255 * ease((t - bf) / 0.4), x=xj); fr = Image.alpha_composite(fr, L)
    ts = s + 0.5; te = DUR[13][1] / 30 - 0.9; n = 14
    for k in range(n):
        st = ts + k * (te - ts) / (n - 1)
        if t < st: continue
        age = 56 + k * 0.5; C = new(); d = ImageDraw.Draw(C); x = ax(age)
        past = age > 59.5
        d.rounded_rectangle([x - 34, 600, x + 34, 670], radius=10, fill=A(red if past else gold, 255)); txt(C, 'PMT', BOLD(22), 615, navy if not past else (255, 255, 255), 255, x=x)
        fr = POP(fr, C, (x - 40, 590, x + 40, 680), back((t - st) / 0.3))
    if t > ns:
        C = new(); padlock(C, xj, 470, 0.8, red, 255); fr = POP(fr, C, (xj - 90, 370, xj + 90, 580), back((t - ns) / 0.45))
        fr = pill_pop(fr, "CAN'T STOP AUTOMATICALLY", 810, t, ns + 0.2, red, size=44)
    return frame(fr)

# ================= BLOCK 14 =================
def b14a(t):
    fr = base(t); fr = title_layer(fr, 'THE LONGER OF TWO', t)
    T = lambda m: tt(14, 0, m)
    a = T('five full years'); b = T('or until the person')
    L = new(); d = ImageDraw.Draw(L)
    for i, (lab, col, st, ln) in enumerate([('FIVE FULL YEARS', gold, a, 1000), ('UNTIL AGE 59 1/2', blue, b, 640)]):
        y = 350 + i * 190
        if t > st - 0.2:
            u = ease((t - st) / 1.4)
            txt(L, lab, BOLD(38), y - 56, white, 255 * ease((t - st + 0.2) / 0.3), x=400, anchor='l')
            d.rounded_rectangle([400, y, 400 + ln * u, y + 80], radius=30, fill=col + (255,))
    fr = Image.alpha_composite(fr, L)
    c = T('the longer of two')
    if t > b + 1.8:
        C = new(); crown(C, 1430, 330, 1.4); fr = POP(fr, C, (1370, 240, 1490, 340), back((t - b - 1.8) / 0.45))
        fr = pill_pop(fr, 'THE LONGER ONE WINS', 760, t, b + 2.0, gold, navy, size=48)
    return frame(fr)

def b14b(t):
    fr = base(t); fr = title_layer(fr, "MARY'S SEPP CLOCK", t)
    T = lambda m: tt(14, 1, m)
    x0, x1, ya = 300, 1620, 700; ax = lambda a: x0 + (a - 55) / 8 * (x1 - x0)
    L = new(); d = ImageDraw.Draw(L)
    d.line([x0, ya, x1, ya], fill=gold + (255,), width=3)
    for a in range(55, 64):
        d.line([ax(a), ya - 8, ax(a), ya + 8], fill=gold + (255,), width=3); txt(L, str(a), REG(30), ya + 16, grey, 255, x=ax(a))
    fr = Image.alpha_composite(fr, L)
    s = T('started these payments')
    if t > s:
        C = new(); avatar(C, ax(56), 500, green, 1.5); txt(C, 'STARTED AT 56', BOLD(30), 575, green, 255, x=ax(56)); fr = POP(fr, C, (ax(56) - 130, 420, ax(56) + 130, 610), back((t - s) / 0.45))
    k = T('keep taking them')
    xj = ax(59.5)
    if t > k:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - k) / 2.0); xe = lerp(ax(56), ax(61), u)
        d.rounded_rectangle([ax(56), 770, min(xe, xj), 830], radius=26, fill=gold + (255,))
        if xe > xj: d.rounded_rectangle([xj - 4, 770, xe, 830], radius=26, fill=red + (255,))
        if u > 0.98:
            d.line([ax(61), 640, ax(61), 770], fill=goldL + (255,), width=6); txt(L, 'AGE 61', BOLD(36), 590, goldL, 255, x=ax(61))
        fr = Image.alpha_composite(fr, L)
    m = T('past this milestone')
    L = new(); d = ImageDraw.Draw(L)
    if t > m - 1.5:
        for i in range(0, 30):
            y = 330 + i * 14
            if i % 2 == 0 and y < ya: d.line([xj, y, xj, y + 8], fill=goldL + (230,), width=3)
        txt(L, '59\u00bd', SER(52), 250, goldL, 255 * ease((t - m + 1.5) / 0.4), x=xj)
    if t > m:
        u = ease((t - m) / 0.5)
        d.line([xj, 860, ax(61), 860], fill=red + (255,), width=6); txt(L, 'PAST THE MILESTONE', BOLD(30), 875, red, 255 * u, x=(xj + ax(61)) / 2)
    fr = Image.alpha_composite(fr, L)
    n = T('not stop the moment')
    if t > n:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([xj - 60, 480, xj + 60, 600], outline=red + (255,), width=12); d.line([xj - 42, 582, xj + 42, 498], fill=red + (255,), width=12); txt(C, 'STOP', BOLD(32), 520, red, 255, x=xj)
        fr = POP(fr, C, (xj - 70, 470, xj + 70, 610), back((t - n) / 0.45))
    return frame(fr)

# ================= BLOCK 15 =================
def b15a(t):
    fr = base(t); fr = title_layer(fr, 'STOP EARLY = PENALTY ON EVERY PAYMENT', t, size=48)
    T = lambda m: tt(15, 0, m)
    C = new(); stop_sign(C, 260, 340, 90); fr = POP(fr, C, (160, 240, 360, 440), back((t - 0.3) / 0.5))
    tg = T('triggers the ten percent'); ch = T('changing the payment'); rt = T('retroactively'); yr = T('sometimes going back')
    for k in range(8):
        st = 0.6 + k * 0.2
        if t < st: continue
        x = 470 + k * 140; C = new(); d = ImageDraw.Draw(C)
        h = 90
        if k == 3 and t > ch: h = 90 + 60 * ease((t - ch) / 0.6)
        col = purple if (k == 3 and t > ch) else gold
        d.rounded_rectangle([x - 55, 560 - (h - 90), x + 55, 650], radius=12, fill=A(col, 255)); txt(C, 'PMT', BOLD(30), 585, navy, 255, x=x)
        fr = POP(fr, C, (x - 60, 480, x + 60, 660), back((t - st) / 0.35))
    if t > ch:
        fr = pill_pop(fr, 'CHANGE THE AMOUNT', 190, t, ch, purple, size=34, cx=1100)
    if t > tg:
        C = new(); building(C, 1720, 590, 200, 160, red); fr = POP(fr, C, (1600, 490, 1840, 700), back((t - tg) / 0.45))
    for i in range(8):
        idx = 7 - i; st = rt + i * 0.3
        if t < st: continue
        u = min(1, (t - st) / 0.7); e = ease(u)
        x = lerp(1690, 470 + idx * 140, e); y = lerp(560, 440, e) - 90 * math.sin(math.pi * u)
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([x - 46, y - 24, x + 46, y + 24], radius=12, fill=red + (255,)); txt(C, '10%', BOLD(30), y - 18, (255, 255, 255), 255, x=x)
        fr = Image.alpha_composite(fr, C)
    if t > yr:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - yr) / 1.2)
        d.line([1560, 780, 1560 - 1100 * u, 780], fill=goldL + (255,), width=8); d.polygon([(1560 - 1100 * u - 30, 780), (1560 - 1100 * u + 8, 758), (1560 - 1100 * u + 8, 802)], fill=goldL + (255,))
        for j in range(4):
            if u > j / 4: txt(L, f'YEAR {j + 1}', BOLD(28), 800, grey, 255, x=1400 - j * 320)
        txt(L, 'GOING BACK YEARS', BOLD(40), 850, goldL, 255 * u, x=960); fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b15b(t):
    fr = base(t); fr = title_layer(fr, 'THE MOST EXPENSIVE MISTAKE', t, size=58)
    T = lambda m: tt(15, 1, m)
    C = new(); money_bag(C, 420, 540, 1.4); fr = POP(fr, C, (250, 340, 600, 740), back((t - 0.3) / 0.5))
    L = new(); rain(L, t, 0.8, 340, 520, 800, n=10, seed=17, r=24, dur=6.0); fr = Image.alpha_composite(fr, L)
    fr = pill_pop(fr, 'ONE OF THE MOST EXPENSIVE', 190, t, T('one of the most'), gold, navy, size=34, cx=960)
    a = T('universal reset button')
    L = new(); d = ImageDraw.Draw(L)
    press = 0.5 + 0.5 * math.sin(t * 3)
    d.ellipse([790, 400, 1130, 740], fill=(60, 30, 30, 255), outline=goldL + (255,), width=6)
    r = 150 - 12 * press; d.ellipse([960 - r, 570 - r, 960 + r, 570 + r], fill=red + (255,))
    txt(L, '59\u00bd', SER(96), 512, (255, 255, 255), 255, x=960); txt(L, 'RESET?', BOLD(40), 640, (255, 255, 255), 255, x=960)
    fr = Image.alpha_composite(fr, L)
    b = T('because people assume')
    if t > b:
        C = new(); d = ImageDraw.Draw(C)
        for (x, y, rr) in [(1330, 430, 55), (1420, 400, 66), (1520, 435, 55)]: d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(236, 240, 245, 255))
        txt(C, '?', BOLD(90), 350, navy, 255, x=1420); fr = POP(fr, C, (1250, 320, 1600, 520), back((t - b) / 0.45))
        avatar_l = new(); avatar(avatar_l, 1420, 640, blue, 1.8); fr = POP(fr, avatar_l, (1330, 540, 1510, 740), back((t - b) / 0.45))
    if t > a: fr = pill_pop(fr, 'NOT A RESET BUTTON', 800, t, a, red, size=48)
    return frame(fr)

# ================= BLOCK 16 =================
def b16a(t):
    fr = base(t); fr = title_layer(fr, 'THE FIFTH CHANGE', t)
    T = lambda m: tt(16, 0, m)
    C = new(); card_box(C, 250, 280, 820, 720, grey, card, 255, 5); txt(C, 'WITHDRAWING', BOLD(44), 310, grey, 255, x=535)
    d = ImageDraw.Draw(C); d.polygon([(535, 640), (620, 540), (575, 540), (575, 420), (495, 420), (495, 540), (450, 540)], fill=A(grey, 255)); cross(C, 700, 400, 50, red)
    fr = POP(fr, C, (240, 270, 830, 730), back((t - 0.3) / 0.5))
    a = T("it's about putting")
    if t > a:
        C = new(); card_box(C, 1100, 280, 1670, 720, green, card, 255, 6); txt(C, 'PUTTING MORE IN', BOLD(44), 310, green, 255, x=1385); vault(C, 1385, 540, 110, t, 0.0)
        fr = POP(fr, C, (1090, 270, 1680, 730), back((t - a) / 0.5))
        L = new(); s0 = a + 0.3
        while s0 < DUR[16][0] / 30 - 0.4:
            fly(L, t, s0, 1.0, (1385, 260), (1385, 470), 30, 'bill', 255, 0, 0.7); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'MORE MONEY INTO YOUR 401(k)', 790, t, a + 0.5, green, navy, size=40, cx=1385)
    return frame(fr)

def b16b(t):
    fr = base(t); fr = title_layer(fr, 'CATCH-UP CONTRIBUTIONS', t, size=58)
    T = lambda m: tt(16, 1, m)
    C = new(); d = ImageDraw.Draw(C); x0, y0, x1, y1 = 300, 300, 720, 760
    d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=(236, 240, 245, 255)); d.rounded_rectangle([x0, y0, x1, y0 + 90], radius=30, fill=red + (255,)); d.rectangle([x0, y0 + 60, x1, y0 + 90], fill=red + (255,))
    txt(C, 'YOU TURN', BOLD(44), y0 + 20, (255, 255, 255), 255, x=(x0 + x1) / 2); txt(C, '50', BOLD(230), y0 + 130, navy, 255, x=(x0 + x1) / 2)
    fr = POP(fr, C, (x0 - 6, y0 - 6, x1 + 6, y1 + 6), back((t - 0.3) / 0.5))
    a = T('the IRS allows') ; b = T('on top of the normal')
    C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([960, 470, 1560, 760], radius=20, fill=gold + (255,)); txt(C, 'NORMAL 401(k) LIMIT', BOLD(40), 585, navy, 255, x=1260)
    fr = POP(fr, C, (950, 460, 1570, 770), back((t - 1.2) / 0.5))
    if t > a:
        u = ease((t - a) / 0.6); yy = lerp(150, 330, u)
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([960, yy, 1560, yy + 130], radius=20, fill=green + (255,)); txt(C, 'CATCH-UP', BOLD(46), yy + 38, navy, 255, x=1260)
        fr = Image.alpha_composite(fr, C)
    if t > b:
        L = new(); txt(L, 'ON TOP', BOLD(40), 790, white, 255 * ease((t - b) / 0.4), x=1260); fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b16c(t):
    fr = base(t); fr = title_layer(fr, 'THE 2026 NUMBERS', t)
    T = lambda m: tt(16, 2, m)
    a = T('twenty-four thousand'); b = T('eight thousand')
    L = new(); d = ImageDraw.Draw(L)
    base_y = 830; sc = 400 / 24500
    h1 = 24500 * sc * ease((t - 0.4) / 1.4)
    d.rounded_rectangle([860, base_y - h1, 1060, base_y], radius=14, fill=gold + (255,))
    d.line([760, base_y, 1160, base_y], fill=gold + (255,), width=3)
    txt(L, 'STANDARD LIMIT', BOLD(34), 400, white, 255 * ease((t - 0.4) / 0.4), x=560, anchor='c')
    txt(L, counter_text(24500 * ease((t - 0.4) / 1.4) // 100 * 100), BOLD(90), 470, gold, 255 * ease((t - 0.4) / 0.4), x=560)
    if t > b - 0.3:
        u = ease((t - b + 0.3) / 1.0); h2 = 8000 * sc * u
        d.rounded_rectangle([860, base_y - h1 - h2, 1060, base_y - h1], radius=14, fill=green + (255,))
        txt(L, 'CATCH-UP', BOLD(34), 400, white, 255 * ease((t - b + 0.3) / 0.4), x=1450)
        txt(L, '+ ' + counter_text(8000 * u // 100 * 100), BOLD(90), 470, green, 255 * ease((t - b + 0.3) / 0.4), x=1450)
    fr = Image.alpha_composite(fr, L)
    return SRC(frame(fr) if False else fr, 'Source: IRS Notice 2025-67') if False else frame(SRC(fr, 'Source: IRS Notice 2025-67'))

# ================= BLOCK 17 =================
def b17a(t):
    fr = base(t); fr = title_layer(fr, 'THE 2026 MAXIMUM', t)
    T = lambda m: tt(17, 0, m)
    fr = pill_pop(fr, 'AGE 50 OR OLDER', 190, t, T('someone fifty'), gold, navy, size=40)
    a = T('up to thirty-two')
    L = new()
    txt(L, counter_text(32500 * ease((t - a) / 1.6) // 100 * 100) if t > a else '$0', BOLD(190), 360, green, 255 * ease((t - 0.3) / 0.4))
    fr = Image.alpha_composite(fr, L)
    if t > a:
        L = new(); txt(L, '$24,500', BOLD(60), 610, gold, 255 * ease((t - a - 1.0) / 0.4), x=760); txt(L, '+', BOLD(60), 610, white, 255 * ease((t - a - 1.0) / 0.4), x=960); txt(L, '$8,000', BOLD(60), 610, green, 255 * ease((t - a - 1.0) / 0.4), x=1160)
        fr = Image.alpha_composite(fr, L)
    v = T('into a four-oh-one-k')
    if t > v:
        C = new(); vault(C, 400, 700, 90, t, 0.0); fr = POP(fr, C, (290, 590, 510, 810), back((t - v) / 0.45))
        L = new(); s0 = v
        while s0 < DUR[17][0] / 30 - 0.3:
            fly(L, t, s0, 1.0, (700, 660), (480, 700), 60, 'bill', 255, 0, 0.6); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
    y = T('in twenty twenty-six')
    fr = pill_pop(fr, 'IN 2026 ALONE', 800, t, y, blue, size=42, cx=1300)
    return frame(SRC(fr, 'Source: IRS Notice 2025-67'))

def b17b(t):
    fr = base(t); fr = title_layer(fr, 'AGES 60 TO 63: EVEN BIGGER', t, size=58)
    T = lambda m: tt(17, 1, m)
    a = T('And workers turning')
    for k, age in enumerate([60, 61, 62, 63]):
        st = a + k * 0.5
        if t < st: continue
        C = new(); card_box(C, 590 + k * 210, 230, 590 + k * 210 + 180, 350, gold, card, 255, 4, 16); txt(C, str(age), BOLD(72), 250, gold, 255, x=590 + k * 210 + 90)
        fr = POP(fr, C, (580 + k * 210, 220, 590 + k * 210 + 190, 360), back((t - st) / 0.4))
    b = T('an even bigger'); c = T('thirty-five thousand')
    base_y = 860
    if t > b:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - b) / 1.2)
        d.rounded_rectangle([640, base_y - 300 * u, 840, base_y], radius=14, fill=gold + (255,)); txt(L, 'AGE 50+', BOLD(34), base_y + 10, white, 255 * u, x=740) if False else None
        txt(L, '$32,500', BOLD(56), base_y - 300 * u - 70, gold, 255 * u, x=740)
        fr = Image.alpha_composite(fr, L)
    if t > c - 0.5:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - c + 0.5) / 1.4)
        d.rounded_rectangle([1000, base_y - 360 * u, 1200, base_y], radius=14, fill=green + (255,))
        txt(L, counter_text(35750 * u // 50 * 50), BOLD(56), base_y - 360 * u - 70, green, 255 * ease((t - c + 0.5) / 0.3), x=1100)
        fr = Image.alpha_composite(fr, L)
    L = new(); d = ImageDraw.Draw(L); d.line([560, base_y, 1280, base_y], fill=gold + (255,), width=3)
    txt(L, 'AGE 50+', BOLD(30), base_y + 14, grey, 255, x=740); txt(L, 'AGE 60-63', BOLD(30), base_y + 14, green, 255, x=1100)
    fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: IRS Notice 2025-67'))

# ================= BLOCK 18 =================
def b18(t):
    fr = base(t); fr = title_layer(fr, 'A GAP WORTH THOUSANDS', t)
    T = lambda m: tt(18, 0, m)
    base_y = 800; sc = 350 / 35750
    a = T('the normal limit'); b = T('over eleven thousand'); c = T('invested for just'); d_ = T('can add tens')
    L = new(); d = ImageDraw.Draw(L)
    u1 = ease((t - 0.4) / 1.0); u2 = ease((t - a - 0.4) / 1.0) if t > a else 0
    d.rounded_rectangle([320, base_y - 24500 * sc * u1, 470, base_y], radius=12, fill=gold + (255,)); d.rounded_rectangle([560, base_y - 35750 * sc * u2, 710, base_y], radius=12, fill=green + (255,)) if t > a else None
    d.line([280, base_y, 760, base_y], fill=gold + (255,), width=3)
    txt(L, 'NORMAL', BOLD(28), base_y + 12, gold, 255, x=395); txt(L, 'HIGHEST', BOLD(28), base_y + 12, green, 255 * u2, x=635)
    txt(L, '$24,500', BOLD(40), base_y - 24500 * sc * u1 - 56, gold, 255 * u1, x=395)
    if t > a: txt(L, '$35,750', BOLD(40), base_y - 35750 * sc * u2 - 56, green, 255 * u2, x=635)
    fr = Image.alpha_composite(fr, L)
    if t > b:
        L = new(); d = ImageDraw.Draw(L); u = ease((t - b) / 0.6)
        y0 = base_y - 35750 * sc; y1 = base_y - 24500 * sc
        d.line([780, y0, 780, y1], fill=red + (255,), width=8); d.line([760, y0, 800, y0], fill=red + (255,), width=8); d.line([760, y1, 800, y1], fill=red + (255,), width=8)
        txt(L, '$11,250', BOLD(46), (y0 + y1) / 2 - 24, red, 255 * u, x=900); txt(L, 'MORE A YEAR', BOLD(28), (y0 + y1) / 2 + 26, white, 255 * u, x=900)
        fr = Image.alpha_composite(fr, L)
    if t > c:
        L = new(); d = ImageDraw.Draw(L); xa, xb, yb, yt = 1080, 1700, 780, 420
        d.line([xa, yb, xb, yb], fill=gold + (255,), width=3); d.line([xa, yb, xa, yt], fill=gold + (255,), width=3)
        u = ease((t - c) / 2.4); pts = [(xa + (xb - xa) * i / 30, yb - (yb - yt) * (math.exp(2.2 * i / 30) - 1) / (math.exp(2.2) - 1)) for i in range(int(30 * u) + 1)]
        if len(pts) > 1: d.line(pts, fill=green + (255,), width=10, joint='curve')
        txt(L, 'A FEW YEARS BEFORE RETIREMENT', BOLD(28), yb + 14, grey, 255, x=(xa + xb) / 2)
        fr = Image.alpha_composite(fr, L)
    if t > d_:
        C = new(); egg(C, 1620, 370, 1.0); fr = POP(fr, C, (1530, 260, 1710, 470), back((t - d_) / 0.5))
        fr = pill_pop(fr, 'TENS OF THOUSANDS MORE', 850, t, d_ + 0.2, green, navy, size=44, cx=1290)
    return frame(SRC(fr, 'Source: IRS Notice 2025-67'))

# ================= BLOCK 19 =================
def b19a(t):
    fr = base(t); fr = title_layer(fr, 'WHERE THEY END UP', t)
    fr = person_box(fr, 'FRANK', 560, 520, blue, t, 0.3, 3.0)
    fr = person_box(fr, 'MARY', 1360, 520, green, t, 0.7, 3.0)
    fr = pill_pop(fr, 'VS', 480, t, 1.2, gold, navy, size=60)
    return frame(fr)

def b19b(t):
    fr = base(t); fr = title_layer(fr, "FRANK'S ASSUMPTION", t)
    T = lambda m: tt(19, 1, m)
    fr = person_box(fr, 'FRANK', 330, 520, blue, t, 0.2, 3.0)
    a = T('total freedom'); items = [('NO PENALTIES', T('no penalties')), ('NO RULES', T('no rules')), ('NOTHING LEFT TO CHECK', T('nothing left'))]
    if t > a: fr = pill_pop(fr, 'TOTAL FREEDOM?', 190, t, a, gold, navy, size=44)
    end = items[2][1] + 0.9
    for k, (lab, st) in enumerate(items):
        if t < st: continue
        C = new(); d = ImageDraw.Draw(C); y = 320 + k * 150
        d.rounded_rectangle([700, y, 1560, y + 110], radius=24, fill=card + (255,), outline=(green if t < end else red) + (255,), width=4)
        txt(C, lab, BOLD(46), y + 28, white, 255, x=1020, anchor='c')
        (check if t < end else cross)(C, 780, y + 55, 34, green if t < end else red)
        fr = POP(fr, C, (690, y - 10, 1570, y + 120), back((t - st) / 0.4))
    if t > end: fr = pill_pop(fr, 'IS IT REALLY?', 810, t, end, red, size=44, cx=1130)
    return frame(fr)

def b19c(t):
    fr = base(t); fr = title_layer(fr, "MARY'S CHECKLIST", t)
    T = lambda m: tt(19, 2, m)
    fr = person_box(fr, 'MARY', 300, 520, green, t, 0.2, 2.8)
    rows = [('IN-SERVICE RULES CONFIRMED', T("she confirmed"), 'door'), ("ROTH 5-YEAR CLOCK TRACKED", T('tracked her'), 'clock'), ('HIGHER CATCH-UP USED', T('used the higher'), 'arrow')]
    for k, (lab, st, ic) in enumerate(rows):
        if t < st: continue
        C = new(); d = ImageDraw.Draw(C); y = 270 + k * 170
        d.rounded_rectangle([560, y, 1400, y + 130], radius=26, fill=card + (255,), outline=green + (255,), width=4)
        if ic == 'door': door(C, 640, y + 65, 60, 90, blue, 255, open_p=0.6)
        elif ic == 'clock': clock(C, 640, y + 65, 42, t, purple, 255)
        else: up_arrow(C, 640, y + 70, 0.5, green, 255)
        txt(C, lab, BOLD(40), y + 44, white, 255, x=740, anchor='l')
        if t > st + 0.7: check(C, 1330, y + 65, 32, green)
        fr = POP(fr, C, (550, y - 10, 1410, y + 140), back((t - st) / 0.4))
    m = T('add thousands more')
    if t > m:
        L = new(); coin_stack(L, 1600, 760, min(9, int((t - m) / 0.3) + 1), 60); fr = Image.alpha_composite(fr, L)
        L = new(); rain(L, t, m, 1520, 1690, 500, n=8, seed=31, r=24, dur=2.0); txt(L, '+ THOUSANDS', BOLD(44), 810, green, 255 * ease((t - m) / 0.4), x=1600); fr = Image.alpha_composite(fr, L)
    r = T('before retiring')
    fr = pill_pop(fr, 'BEFORE RETIRING', 820, t, r, gold, navy, size=40, cx=900)
    return frame(fr)

def b19d(t):
    fr = base(t); fr = title_layer(fr, 'SAME AGE. SAME LAW.', t)
    T = lambda m: tt(19, 3, m)
    C = new(); avatar(C, 560, 480, blue, 2.4); coin_stack(C, 560, 820, 2, 60); txt(C, 'FRANK', BOLD(48), 610, blue, 255, x=560)
    fr = POP(fr, C, (330, 300, 790, 880), back((t - 0.3) / 0.5))
    C = new(); avatar(C, 1360, 480, green, 2.4); coin_stack(C, 1360, 820, 8, 60); txt(C, 'MARY', BOLD(48), 610, green, 255, x=1360)
    fr = POP(fr, C, (1130, 300, 1590, 880), back((t - 0.6) / 0.5))
    a = T('completely different')
    if t > a:
        fr = pill_pop(fr, 'DIFFERENT OUTCOME', 190, t, a, red, size=44)
        C = new(); cross(C, 700, 400, 44, red); fr = POP(fr, C, (640, 350, 760, 450), back((t - a - 0.2) / 0.4))
        C = new(); check(C, 1500, 400, 44, green); fr = POP(fr, C, (1440, 350, 1560, 450), back((t - a - 0.4) / 0.4))
    return frame(fr)

# ================= BLOCK 20 =================
def b20a(t):
    fr = base(t); fr = title_layer(fr, 'THE WEEK YOU TURN 59\u00bd', t)
    C = new(); d = ImageDraw.Draw(C)
    d.rounded_rectangle([640, 240, 1280, 830], radius=26, fill=(236, 240, 245, 255)); d.rounded_rectangle([860, 210, 1060, 270], radius=14, fill=gold + (255,))
    txt(C, 'CHECKLIST', BOLD(40), 290, navy, 255, x=960)
    fr = POP(fr, C, (630, 200, 1290, 840), back((t - 0.3) / 0.5))
    L = new(); d = ImageDraw.Draw(L)
    for k in range(5):
        st = 0.9 + k * 0.6; u = ease((t - st) / 0.5)
        if u <= 0: continue
        y = 380 + k * 82
        d.ellipse([690, y, 740, y + 50], fill=gold + (int(255 * u),)); txt(L, str(k + 1), BOLD(32), y + 6, navy, 255 * u, x=715)
        d.rounded_rectangle([770, y + 14, 770 + 440 * u, y + 34], radius=10, fill=(170, 180, 200, 255))
    fr = Image.alpha_composite(fr, L)
    return frame(fr)

def b20b(t):
    fr = base(t); fr = title_layer(fr, 'STEP 1: IN-SERVICE?', t)
    T = lambda m: tt(20, 1, m)
    a = T('confirm with your plan'); b = T('whether in-service')
    C = new(); phone(C, 420, 520, 1.5, 255, t, True); fr = POP(fr, C, (250, 300, 600, 760), back((t - 0.3) / 0.5)) if False else Image.alpha_composite(fr, C)
    if t > a:
        C = new(); avatar(C, 420, 720, gold, 1.2); txt(C, 'PLAN ADMINISTRATOR', BOLD(26), 780, gold, 255, x=420); fr = POP(fr, C, (250, 640, 600, 820), back((t - a) / 0.45))
    if t > b:
        C = new(); bubble(C, 720, 300, 1260, 440, 'ARE IN-SERVICE\nWITHDRAWALS ALLOWED?', size=34, tail='left'); fr = POP(fr, C, (710, 290, 1270, 500), back((t - b) / 0.45))
        C = new(); vault(C, 1530, 560, 130, t, 0.5 * (0.5 - 0.5 * math.cos(t * 1.6))); fr = POP(fr, C, (1360, 390, 1700, 730), back((t - b - 0.2) / 0.45))
        fr = pill_pop(fr, 'ASK IT', 780, t, b + 0.6, gold, navy, size=44, cx=1000)
    return frame(rail(fr, 1, t))

def b20c(t):
    fr = base(t); fr = title_layer(fr, 'STEP 2: ROTH OPENING DATE', t, size=58)
    T = lambda m: tt(20, 2, m)
    a = T('the exact opening'); b = T('five-year rule')
    C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([300, 260, 700, 640], radius=30, fill=(236, 240, 245, 255)); d.rounded_rectangle([300, 260, 700, 340], radius=30, fill=red + (255,)); d.rectangle([300, 300, 700, 340], fill=red + (255,))
    txt(C, 'ROTH IRA OPENED', BOLD(34), 282, (255, 255, 255), 255, x=500); txt(C, '?', BOLD(230), 360, navy, 255, x=500)
    fr = POP(fr, C, (290, 250, 710, 650), back((t - 0.3) / 0.5))
    if t > a:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([560, 480, 700, 620], outline=gold + (255,), width=14); d.line([690, 610, 770, 690], fill=gold + (255,), width=18); fr = POP(fr, C, (540, 460, 790, 710), back((t - a) / 0.45))
    if t > b - 1.0:
        fr = year_boxes(fr, t, 1240, 320, 3, 3, b - 1.0, 0.0, 140, 120, 20) if False else fr
        for k in range(5):
            st = b - 1.2 + k * 0.3
            if t < st: continue
            C = new(); d = ImageDraw.Draw(C); x = 860 + k * 150
            d.rounded_rectangle([x, 350, x + 130, 470], radius=16, fill=gold + (255,), outline=goldL + (255,), width=3); txt(C, f'Y{k + 1}', BOLD(44), 375, navy, 255, x=x + 65); check(C, x + 65, 440, 22, green)
            fr = POP(fr, C, (x - 5, 340, x + 135, 480), back((t - st) / 0.35))
        fr = pill_pop(fr, 'FIVE-YEAR RULE SATISFIED?', 560, t, b, green, navy, size=42, cx=1230)
    return frame(rail(fr, 2, t))

def b20d(t):
    fr = base(t); fr = title_layer(fr, 'STEP 3: SEPP DEADLINE', t)
    T = lambda m: tt(20, 3, m)
    a = T('if you started SEPP'); b = T('five years or'); c = T('calculate whether')
    if t > a - 0.2:
        C = new(); card_box(C, 320, 270, 860, 600, gold, card, 255, 5); txt(C, '5 YEARS', BOLD(90), 310, gold, 255, x=590); txt(C, 'FROM YOUR START DATE', BOLD(30), 420, white, 255, x=590); coin_stack(C, 590, 570, 4, 45)
        fr = POP(fr, C, (310, 260, 870, 610), back((t - a + 0.2) / 0.5))
    if t > b - 0.3:
        C = new(); card_box(C, 1060, 270, 1600, 600, blue, card, 255, 5); txt(C, 'AGE', BOLD(40), 300, white, 255, x=1330); txt(C, '59\u00bd', SER(120), 350, blue, 255, x=1330)
        fr = POP(fr, C, (1050, 260, 1610, 610), back((t - b + 0.3) / 0.5))
        C = new(); txt(C, 'OR', BOLD(70), 380, white, 255, x=960); fr = POP(fr, C, (900, 360, 1020, 470), back((t - b + 0.3) / 0.4))
    m = T('longer deadline')
    if t > m:
        C = new(); crown(C, 590, 250, 1.3); fr = POP(fr, C, (520, 160, 660, 260), back((t - m) / 0.45))
        fr = pill_pop(fr, 'MARK THE LATER DATE', 700, t, m + 0.3, gold, navy, size=46)
        C = new(); d = ImageDraw.Draw(C); d.polygon([(960, 830), (930, 790), (990, 790)], fill=red + (255,)); d.ellipse([930, 740, 990, 800], fill=red + (255,)); fr = POP(fr, C, (920, 730, 1000, 840), back((t - m - 0.6) / 0.4))
    return frame(rail(fr, 3, t))

def b20e(t):
    fr = base(t); fr = title_layer(fr, 'STEP 4: CATCH-UP LIMITS', t, size=58)
    T = lambda m: tt(20, 4, m)
    a = T("if you're still working"); b = T('ask about'); c = T('higher catch-up')
    C = new(); avatar(C, 380, 520, gold, 2.2); briefcase(C, 300, 660, 0.7); txt(C, 'STILL WORKING', BOLD(34), 730, gold, 255, x=380)
    fr = POP(fr, C, (200, 380, 560, 780), back((t - 0.3) / 0.5))
    if t > b:
        C = new(); bubble(C, 620, 280, 1120, 420, 'HIGHER CATCH-UP\nLIMITS?', size=36, tail='left'); fr = POP(fr, C, (610, 270, 1130, 480), back((t - b) / 0.45))
    if t > c:
        C = new(); up_arrow(C, 1480, 470, 1.2, green, 255); fr = POP(fr, C, (1360, 340, 1600, 590), back((t - c) / 0.45))
        L = new(); s0 = c
        while s0 < DUR[20][4] / 30 - 0.3:
            fly(L, t, s0, 1.0, (1100, 640), (1420, 600), 70, 'coin', 255, 0, 1.0); s0 += 0.4
        fr = Image.alpha_composite(fr, L)
        fr = pill_pop(fr, 'AGES 60-63: EVEN HIGHER', 740, t, c + 0.5, green, navy, size=38, cx=1250)
    return frame(rail(fr, 4, t))

def b20f(t):
    fr = base(t); fr = title_layer(fr, 'STEP 5: GET IT IN WRITING', t, size=58)
    T = lambda m: tt(20, 5, m)
    a = T('before touching'); b = T('get the numbers'); c = T('from your plan'); d_ = T('verbal answers'); e = T("paperwork doesn't")
    if t > a - 0.2:
        C = new(); stop_sign(C, 300, 330, 80); fr = POP(fr, C, (210, 240, 390, 420), back((t - a + 0.2) / 0.45))
    if t > b:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([760, 240, 1100, 660], radius=16, fill=(236, 240, 245, 255), outline=gold + (255,), width=5)
        u = ease((t - b) / 1.4)
        for k in range(6):
            if u > k / 6: d.rectangle([800, 290 + k * 46, 800 + 260 * min(1, (u - k / 6) * 6), 306 + k * 46], fill=(120, 135, 160, 255))
        txt(C, 'IN WRITING', BOLD(36), 620, navy, 255, x=930) if u > 0.9 else None
        fr = POP(fr, C, (750, 230, 1110, 670), back((t - b) / 0.45))
    if t > c:
        C = new(); avatar(C, 1400, 400, gold, 1.5); txt(C, 'YOUR PLAN', BOLD(30), 470, gold, 255, x=1400); avatar(C, 1650, 400, blue, 1.5); txt(C, 'FIDUCIARY ADVISOR', BOLD(24), 470, blue, 255, x=1650)
        fr = POP(fr, C, (1250, 300, 1780, 510), back((t - c) / 0.45))
    if t > d_:
        fade = 0.5 + 0.5 * math.sin((t - d_) * 5)
        C = new(); bubble(C, 300, 730, 780, 850, 'VERBAL ANSWERS CHANGE', fillc=(150, 165, 185), size=34, tail='left', alpha=int(255 * (0.35 + 0.65 * fade))); fr = POP(fr, C, (290, 720, 790, 900), back((t - d_) / 0.45))
    if t > e:
        C = new(); check(C, 1000, 790, 44, green); txt(C, "PAPERWORK DOESN'T", BOLD(40), 760, green, 255, x=1420); fr = POP(fr, C, (940, 720, 1760, 850), back((t - e) / 0.45))
    return frame(rail(fr, 5, t))

# ================= BLOCK 21 =================
def b21a(t):
    fr = base(t); fr = title_layer(fr, '59\u00bd: DOORS OPEN AND LOCKED', t, size=56)
    T = lambda m: tt(21, 0, m)
    a = T('opens some doors'); b = T('keeps others locked')
    C = new(); d = ImageDraw.Draw(C); d.ellipse([860, 380, 1060, 580], fill=gold + (255,)); age59(C, 960, 430, 74, navy); fr = POP(fr, C, (850, 370, 1070, 590), back((t - 0.3) / 0.5))
    if t > a - 0.3:
        C = new(); door(C, 440, 520, 200, 320, green, 255, open_p=min(1, (t - a + 0.3) / 1.2) * 0.85); txt(C, 'OPENS SOME DOORS', BOLD(36), 730, green, 255, x=440); fr = POP(fr, C, (250, 340, 640, 780), back((t - a + 0.3) / 0.5))
        L = new(); s0 = a; 
        while s0 < a + 3.5: fly(L, t, s0, 1.0, (500, 520), (700, 560), 60, 'coin', 255, 0, 0.9); s0 += 0.45
        fr = Image.alpha_composite(fr, L)
    if t > b:
        C = new(); door(C, 1480, 520, 200, 320, red, 255, open_p=0.0); padlock(C, 1480, 520, 0.9, red, 255); txt(C, 'KEEPS OTHERS LOCKED', BOLD(36), 730, red, 255, x=1480); fr = POP(fr, C, (1250, 340, 1720, 780), back((t - b) / 0.5))
    fr = pill_pop(fr, 'LONGER THAN PEOPLE EXPECT', 830, t, T('longer than people'), gold, navy, size=40)
    return frame(fr)

def b21b(t):
    fr = base(t); fr = title_layer(fr, 'THE OTHER AGE THAT CHANGES EVERYTHING', t, size=50)
    T = lambda m: tt(21, 1, m)
    a = T('Social Security'); b = T('exact math')
    if t > a - 0.3:
        L = new(); d = ImageDraw.Draw(L); base_y = 800; sc = 330 / 124
        u1 = ease((t - a + 0.3) / 1.2); u2 = ease((t - b) / 1.2) if t > b else 0
        d.rounded_rectangle([220, base_y - 70 * sc * u1, 400, base_y], radius=14, fill=red + (255,)); txt(L, '70%', BOLD(56), base_y - 70 * sc * u1 - 70, red, 255 * u1, x=310); txt(L, 'AT 62', BOLD(36), base_y + 14, white, 255, x=310)
        if t > b:
            d.rounded_rectangle([480, base_y - 124 * sc * u2, 660, base_y], radius=14, fill=green + (255,)); txt(L, '124%', BOLD(56), base_y - 124 * sc * u2 - 70, green, 255 * u2, x=570); txt(L, 'AT 70', BOLD(36), base_y + 14, white, 255, x=570)
        d.line([180, base_y, 720, base_y], fill=gold + (255,), width=3)
        fr = Image.alpha_composite(fr, L)
    if t > 1.0:
        L = new(); d = ImageDraw.Draw(L); xa, ya_, xb, yb = 1080, 290, 1740, 661
        for i in range(0, 66):
            x = xa + i * 10
            if i % 2 == 0: d.line([x, ya_, min(x + 6, xb), ya_], fill=goldL + (255,), width=5); d.line([x, yb, min(x + 6, xb), yb], fill=goldL + (255,), width=5)
        for j in range(0, 38):
            y = ya_ + j * 10
            if j % 2 == 0: d.line([xa, y, xa, min(y + 6, yb)], fill=goldL + (255,), width=5); d.line([xb, y, xb, min(y + 6, yb)], fill=goldL + (255,), width=5)
        txt(L, 'SOCIAL SECURITY AT 62 VS 70', BOLD(30), 450, (110, 130, 160), 255, x=(xa + xb) / 2)
        fr = Image.alpha_composite(fr, L)
        L = new(); pulse = 6 * math.sin(t * 4)
        txt(L, 'WATCH NEXT', BOLD(50), 720, gold, 255, x=(1080 + 1740) / 2); d = ImageDraw.Draw(L); d.polygon([(1410, 800 + pulse), (1370, 760 + pulse), (1450, 760 + pulse)], fill=gold + (255,)) if False else None
        fr = Image.alpha_composite(fr, L)
    return frame(SRC(fr, 'Source: Social Security Administration (full retirement age 67)'))

SLIDES = {11: [b11a, b11b, b11c], 12: [b12], 13: [b13a, b13b], 14: [b14a, b14b], 15: [b15a, b15b], 16: [b16a, b16b, b16c], 17: [b17a, b17b], 18: [b18], 19: [b19a, b19b, b19c, b19d], 20: [b20a, b20b, b20c, b20d, b20e, b20f], 21: [b21a, b21b]}

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'preview':
        sel = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(SLIDES)
        fq = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                fn(DUR[b][i] / 30 * fq).convert('RGB').save(f'/home/claude/pw_{b}_{i}.png')
        print({b: DUR[b] for b in sel}, 'ok')
    else:
        sel = [int(x) for x in sys.argv[2].split(',')]
        for b in sel:
            for i, fn in enumerate(SLIDES[b]):
                render_fast(fn, DUR[b][i], f'/mnt/user-data/outputs/v3-b{b}-0{i + 1}.mp4')
                print('done', b, i + 1, DUR[b][i], flush=True)
