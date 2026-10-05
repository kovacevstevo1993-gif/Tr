from v6b21_25 import *
from v6b2 import logo
import sys

def dashed(C, x0, y0, x1, y1, col=goldL, w=6, dash=28, gap=18):
    d = ImageDraw.Draw(C)
    for (xa, ya, xb, yb) in [(x0, y0, x1, y0), (x0, y1, x1, y1), (x0, y0, x0, y1), (x1, y0, x1, y1)]:
        L = math.hypot(xb - xa, yb - ya); n = int(L // (dash + gap)) + 1
        for k in range(n):
            s0 = k * (dash + gap); s1 = min(L, s0 + dash)
            d.line([xa + (xb - xa) * s0 / L, ya + (yb - ya) * s0 / L, xa + (xb - xa) * s1 / L, ya + (yb - ya) * s1 / L], fill=col + (255,), width=w)
def dashed_circle(C, cx, cy, r, col=goldL, w=6):
    d = ImageDraw.Draw(C)
    for k in range(18): d.arc([cx - r, cy - r, cx + r, cy + r], start=k * 20, end=k * 20 + 12, fill=col + (255,), width=w)

# ============ BLOCCO 27 (738) ============
B27 = Blk2(["Before we finish, a word about sources.", "The raise formula comes from the Social Security Administration.", "The inflation numbers come from the Bureau of Labor Statistics.",
            "The Medicare premium projection comes from the Medicare Trustees Report, and the tax lines come from the Internal Revenue Service.",
            "Every source is listed in the description, and the official twenty twenty seven numbers may be different from the estimates we used today."],
           [[0, 1], [2], [3], [4]], 738)
def srccard(C, x0, y0, x1, y1, col, l1, l2, site, icon=None):
    card_(C, x0, y0, x1, y1, col); cx = (x0 + x1) / 2
    txt(C, l1, BOLD(52), y0 + 40, white, 255, x=cx); txt(C, l2, BOLD(52), y0 + 105, col, 255, x=cx); txt(C, site, BOLD(70), y1 - 130, goldL, 255, x=cx)
def s27a(t):
    fr = base_(t, 301, 'OUR SOURCES'); T = lambda m: B27.tt(0, m)
    if t > 0.3:
        C = new(); txt(C, 'A WORD ABOUT SOURCES', BOLD(86), 280, goldL, 255, x=960); fr = A_(fr, C, (160, 260, 1760, 420), t, 0.3)
    t2 = T('The raise formula')
    if t > t2:
        C = new(); building(C, 420, 640, 240, 200, blue); srccard(C, 700, 480, 1780, 820, blue, 'THE RAISE FORMULA COMES FROM', 'SOCIAL SECURITY ADMINISTRATION', 'ssa.gov'); fr = A_(fr, C, (260, 450, 1800, 840), t, t2)
    return frame(fr)
def s27b(t):
    fr = base_(t, 302, 'OUR SOURCES'); T = lambda m: B27.tt(1, m)
    if t > 0.3:
        C = new(); building(C, 420, 520, 260, 220, gold); srccard(C, 700, 320, 1780, 720, gold, 'THE INFLATION NUMBERS COME FROM', 'BUREAU OF LABOR STATISTICS', 'bls.gov'); fr = A_(fr, C, (240, 290, 1800, 740), t, 0.3)
    return frame(fr)
def s27c(t):
    fr = base_(t, 303, 'OUR SOURCES'); T = lambda m: B27.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 900, 740, blue); medicare_card(C, 520, 480, 0.7); txt(C, 'MEDICARE PREMIUM PROJECTION', BOLD(44), 320, white, 255, x=520); txt(C, 'MEDICARE TRUSTEES REPORT', BOLD(46), 600, blue, 255, x=520); txt(C, 'cms.gov', BOLD(56), 670, goldL, 255, x=520); fr = A_(fr, C, (120, 270, 920, 760), t, 0.3)
    t2 = T('tax lines')
    if t > t2 - 0.2:
        C = new(); card_(C, 1020, 290, 1780, 740, red); tax_form(C, 1330, 390, 140, 180, 255, 'IRS'); txt(C, 'THE TAX LINES', BOLD(52), 320, white, 255, x=1400); txt(C, 'INTERNAL REVENUE SERVICE', BOLD(40), 600, red, 255, x=1400); txt(C, 'irs.gov', BOLD(56), 670, goldL, 255, x=1400); fr = A_(fr, C, (1000, 270, 1800, 760), t, t2 - 0.2)
    return frame(fr)
def s27d(t):
    fr = base_(t, 304, 'IN THE DESCRIPTION'); T = lambda m: B27.tt(3, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 900, 700, green); [ImageDraw.Draw(C).rectangle([300, 490 + k * 60, 740, 515 + k * 60], fill=A(grey, 255)) for k in range(3)]; txt(C, 'EVERY SOURCE IS', BOLD(60), 320, white, 255, x=520); txt(C, 'IN THE DESCRIPTION', BOLD(60), 390, green, 255, x=520); fr = A_(fr, C, (120, 270, 920, 720), t, 0.3)
    t2 = T('official twenty twenty seven') - 0.2
    if t > t2:
        C = new(); card_(C, 1020, 290, 1780, 700, gold); txt(C, 'OFFICIAL 2027 NUMBERS', BOLD(54), 330, white, 255, x=1400); txt(C, 'MAY BE DIFFERENT', BOLD(60), 420, goldL, 255, x=1400); txt(C, 'FROM TODAY\'S ESTIMATES', BOLD(46), 520, white, 255, x=1400); fr = A_(fr, C, (1000, 270, 1800, 720), t, t2)
    return frame(fr)

# ============ BLOCCO 28 (865) ============
B28 = Blk2(["Let's recap the five things.", "One: Cola is a formula, based on prices from July, August and September.", "Two: that formula can feel smaller than the real cost of retirement.",
            "Three: Medicare Part B comes out of the check first, and the hold harmless rule protects most people but not everyone.",
            "Four: the tax lines never move, so more of each check can become taxable.", "Five: other limits change on the same day."],
           [[0, 1], [2], [3], [4], [5]], 865)
def recap(t, g, n, seed, l1, l2, l3, col, iconf):
    fr = base_(t, seed, 'RECAP: THE FIVE THINGS')
    if t > 0.3:
        C = new(); badge(C, 300, 420, n, col, 100); txt(C, l1, BOLD(76), 340, white, 255, x=1130); txt(C, l2, BOLD(56), 450, col, 255, x=1130)
        if l3: txt(C, l3, BOLD(50), 560, grey, 255, x=1170)
        fr = A_(fr, C, (140, 280, 1800, 640), t, 0.3)
    if t > 0.9:
        C = new(); iconf(C); fr = A_(fr, C, (140, 620, 1800, 900), t, 0.9)
    L = new(); d = ImageDraw.Draw(L)
    for k in range(5):
        cx = 760 + k * 100; d.ellipse([cx - 22, 952 - 22, cx + 22, 952 + 22], fill=(gold if k < n else card) + (255,), outline=goldL + (255,), width=3)
    fr = Image.alpha_composite(fr, L)
    return frame(fr)
def ic_r1(C):
    for k, m in enumerate(['JULY', 'AUGUST', 'SEPTEMBER']): ImageDraw.Draw(C).rounded_rectangle([420 + k * 410, 700, 760 + k * 410, 830], radius=24, fill=gold + (255,)); txt(C, m, BOLD(50), 740, navy, 255, x=590 + k * 410)
def ic_r2(C):
    wallet(C, 560, 760, 1.3); bill(C, 960, 740, 220, 106, -6, 255); txt(C, 'BILLS > RAISE?', BOLD(60), 720, red, 255, x=1420)
def ic_r3(C):
    medicare_card(C, 600, 760, 0.8); shield(C, 1120, 740, 0.8, green); txt(C, 'PROTECTS MOST, NOT ALL', BOLD(42), 720, goldL, 255, x=1470)
def ic_r4(C):
    taxbar(C, 700, 25000, 34000, 50000)
def ic_r5(C):
    cal_card(C, 420, 640, 780, 900, 'OCTOBER', '14', bigsize=120, headcol=red); txt(C, 'TAXABLE MAXIMUM', BOLD(52), 700, white, 255, x=1230); txt(C, 'EARNINGS LIMITS', BOLD(52), 780, goldL, 255, x=1230)
def s28a(t): return recap(t, 0, 1, 311, 'COLA IS A FORMULA', 'BASED ON JULY-SEPTEMBER PRICES', '', gold, ic_r1)
def s28b(t): return recap(t, 1, 2, 312, 'IT CAN FEEL SMALLER', 'THAN THE REAL COST OF RETIREMENT', '', goldL, ic_r2)
def s28c(t): return recap(t, 2, 3, 313, 'PART B COMES OUT FIRST', 'HOLD HARMLESS: MOST, NOT EVERYONE', '', red, ic_r3)
def s28d(t): return recap(t, 3, 4, 314, 'THE TAX LINES NEVER MOVE', 'MORE OF EACH CHECK CAN BECOME TAXABLE', '', red, ic_r4)
def s28e(t): return recap(t, 4, 5, 315, 'OTHER LIMITS CHANGE', 'ON THE SAME DAY', '', gold, ic_r5)

# ============ BLOCCO 29 (472) ============
B29 = Blk2(["If this helped, tap like and subscribe to The Money Backstory, so you do not miss the next one.",
            "And if you want to see how the age you claim can change your lifetime income by more than one hundred twenty four thousand dollars, that video is right on your screen now.", "See you there."],
           [[0], [1, 2]], 472)
def s29a(t):
    fr = base_(t, 321, 'THANK YOU FOR WATCHING'); T = lambda m: B29.tt(0, m)
    if t > 0.3:
        C = new(); logo(C, 360, 520, 150); fr = A_(fr, C, (160, 330, 580, 720), t, 0.3)
    t2 = T('tap like') - 0.1
    if t > max(0.5, t2):
        C = new(); card_(C, 760, 330, 1160, 600, blue); d = ImageDraw.Draw(C); d.polygon([(960, 380), (1010, 460), (1060, 460), (1060, 560), (900, 560), (900, 460), (930, 460)], fill=white + (255,)); txt(C, 'LIKE', BOLD(70), 580 - 0, white, 255, x=960) if False else None; txt(C, 'LIKE', BOLD(60), 600, white, 255, x=960); fr = A_(fr, C, (740, 310, 1180, 680), t, max(0.5, t2))
    t3 = T('subscribe') - 0.1
    if t > max(0.9, t3):
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1260, 400, 1780, 540], radius=70, fill=red + (255,)); txt(C, 'SUBSCRIBE', BOLD(70), 430, white, 255, x=1520); fr = A_(fr, C, (1240, 380, 1800, 560), t, max(0.9, t3))
    fr = P(fr, 'THE MONEY BACKSTORY', 800, t, 1.3, goldL, navy, 64)
    return frame(fr)
def s29b(t):
    fr = base_(t, 322, 'WATCH NEXT'); T = lambda m: B29.tt(1, m)
    if t > 0.3:
        C = new(); txt(C, 'THE AGE YOU CLAIM CAN CHANGE', BOLD(48), 300, white, 255, x=620); txt(C, 'YOUR LIFETIME INCOME BY', BOLD(48), 365, white, 255, x=620); txt(C, '$124,000+', BOLD(130), 460, green, 255, x=620); fr = A_(fr, C, (140, 260, 1140, 640), t, 0.3)
    if t > 0.6:
        C = new(); dashed(C, 1120, 280, 1780, 700); txt(C, 'WATCH NEXT', BOLD(60), 460, goldL, 255, x=1450); fr = A_(fr, C, (1100, 260, 1800, 720), t, 0.6)
    t2 = T('on your screen') - 0.2
    if t > t2:
        L = new(); arrow_r(L, 900, 1090, 790, goldL, 255 * E_(t, t2)); txt(L, 'ON YOUR SCREEN NOW', BOLD(54), 760, goldL, 255 * E_(t, t2), x=470); fr = Image.alpha_composite(fr, L)
    return frame(fr)

# ============ BLOCCO 30 (358) ============
B30 = Blk2(["Rules, amounts and ages change and differ by location and plan.", "Always confirm with the official source before you rely on them.", "This is general information, not financial advice."],
           [[0, 1, 2]], 358)
def s30a(t):
    fr = base_(t, 331, 'IMPORTANT', 64); T = lambda m: B30.tt(0, m)
    if t > 0.3:
        C = new(); lines = [('Rules, amounts and ages change', white, 250), ('and differ by location and plan.', white, 315), ('Always confirm with the official', goldL, 410), ('source before you rely on them.', goldL, 475), ('General information,', white, 570), ('not financial advice.', white, 635)]
        for tx, cl, yy in lines: txt(C, tx, BOLD(52), yy, cl, 255, x=650)
        fr = A_(fr, C, (140, 240, 1160, 770), t, 0.3)
    if t > 0.6:
        C = new(); dashed(C, 1220, 280, 1780, 640); txt(C, 'WATCH NEXT', BOLD(56), 430, goldL, 255, x=1500); dashed_circle(C, 260, 860, 85); txt(C, 'SUBSCRIBE', BOLD(44), 835, goldL, 255, x=560); fr = A_(fr, C, (160, 240, 1800, 1010), t, 0.6)
    return frame(fr)


# ============ BLOCCO 26 (414) — voce letta dallo screenshot: contiene solo le ultime 2 frasi ============
B26 = Blk2(["The headline percentage is only the starting point.",
            "And when the official number comes out, you can redo this math yourself in a minute: multiply your check by the raise, then subtract any increase in the Part B premium."],
           [[0], [1]], 414)
def s26a(t):
    fr = base_(t, 291, 'ONLY THE STARTING POINT'); T = lambda m: B26.tt(0, m)
    if t > 0.3:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([200, 300, 620, 720], fill=gold + (255,), outline=goldL + (255,), width=10); txt(C, '3.5%', BOLD(150), 410, navy, 255, x=410); txt(C, 'THE HEADLINE', BOLD(52), 590, navy, 255, x=410); fr = A_(fr, C, (180, 280, 640, 740), t, 0.3)
    t2 = T('only the starting')
    L = new(); arrow_r(L, 660, 880, 510, goldL, 255 * E_(t, t2 - 0.2)); fr = Image.alpha_composite(fr, L)
    if t > t2 - 0.2:
        C = new(); card_(C, 920, 300, 1780, 720, green); txt(C, 'OUR EXAMPLE: WHAT', BOLD(50), 340, white, 255, x=1350); txt(C, 'REACHES THE BANK', BOLD(50), 405, white, 255, x=1350); txt(C, 'ABOUT $65', BOLD(130), 500, green, 255, x=1350); fr = A_(fr, C, (900, 280, 1800, 740), t, t2 - 0.2)
    fr = P(fr, 'THE HEADLINE IS ONLY THE STARTING POINT', 810, t, 1.0, goldL, navy, 54)
    return frame(fr)
def s26b(t):
    fr = base_(t, 292, 'REDO THE MATH YOURSELF'); T = lambda m: B26.tt(1, m)
    if t > 0.3:
        C = new(); cal_card(C, 140, 280, 520, 580, 'OFFICIAL NUMBER', '14', bigsize=120, headcol=red); txt(C, 'OCTOBER', BOLD(46), 500, (70, 84, 108), 255, x=330); fr = A_(fr, C, (120, 260, 540, 580), t, 0.3)
    items = [('multiply your check', 'YOUR CHECK', blue, 620), ('by the raise', 'x THE RAISE', green, 1000), ('then subtract', '- PART B INCREASE', red, 1380)]
    for k, (m, lab, col, x0) in enumerate(items):
        t0 = max(0.5, T(m) - 0.1)
        if t < t0: continue
        C = new(); card_(C, x0, 300, x0 + 340, 520, col); l = lab.split(' ', 1) if k != 2 else ['- PART B', 'INCREASE']
        if k == 0: l = ['YOUR', 'CHECK']
        if k == 1: l = ['x THE', 'RAISE']
        txt(C, l[0], BOLD(60), 350, white, 255, x=x0 + 170); txt(C, l[1], BOLD(60), 425, col, 255, x=x0 + 170); fr = A_(fr, C, (x0 - 20, 280, x0 + 360, 540), t, t0)
    t4 = T('in a minute')
    if t > t4 - 0.5: fr = P(fr, '= YOUR REAL RAISE, IN A MINUTE', 700, t, t4 - 0.5, gold, navy, 66)
    return frame(fr)

FNS5 = {26: [s26a, s26b], 27: [s27a, s27b, s27c, s27d], 28: [s28a, s28b, s28c, s28d, s28e], 29: [s29a, s29b], 30: [s30a]}
BLK5 = {26: B26, 27: B27, 28: B28, 29: B29, 30: B30}
if __name__ == '__main__':
    mode = sys.argv[1]; b = int(sys.argv[2]); fns = FNS5[b]; FS = BLK5[b].FS
    sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, len(fns) + 1))
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.35, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}pq{b}_{i}_{int(fq*100)}.png')
        print(b, FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b{b}-0{i}.mp4'); print('done', b, i, f, flush=True)
