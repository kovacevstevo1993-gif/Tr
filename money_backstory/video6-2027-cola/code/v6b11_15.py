from v6b6_10 import *
from v6b3 import medicare_card
import sys

def mini_check(C, x0, y0, x1, y1, col, amount, sub, head, size=110): paycheck(C, x0, y0, x1, y1, col, amount, sub, head, size)

# ============ BLOCCO 11 (690) ============
B11 = Blk2(["Let's put real numbers on it.", "Frank and Mary each get two thousand seventy one dollars a month.",
            "If the raise is three point five percent, it adds about seventy two dollars, bringing each check to about two thousand one hundred forty three dollars.",
            "Over a year, that is about eight hundred sixty four dollars more.", "Hold on to that seventy two. Now watch what happens to it."],
           [[0, 1], [2], [3], [4]], 690)
def s11a(t):
    fr = base_(t, 91, 'REAL NUMBERS'); T = lambda m: B11.tt(0, m)
    t1 = T('Frank and Mary') - 0.1
    if t > max(0.3, t1):
        C = new(); mini_check(C, 130, 290, 900, 650, blue, '$2,071', 'PER MONTH', 'FRANK: SOCIAL SECURITY', 140); fr = A_(fr, C, (110, 270, 920, 670), t, max(0.3, t1))
    t2 = T('each get')
    if t > t2:
        C = new(); mini_check(C, 1020, 290, 1790, 650, pink, '$2,071', 'PER MONTH', 'MARY: SOCIAL SECURITY', 140); fr = A_(fr, C, (1000, 270, 1810, 670), t, t2)
    fr = P(fr, 'THE SAME AVERAGE CHECK', 800, t, 0.9, goldL, navy, 56)
    return frame(fr)
def s11b(t):
    fr = base_(t, 92, 'THE RAISE IN DOLLARS'); T = lambda m: B11.tt(1, m)
    if t > 0.3:
        C = new(); mini_check(C, 110, 290, 590, 600, blue, '$2,071', 'PER MONTH', 'CHECK TODAY', 110); fr = A_(fr, C, (90, 270, 610, 620), t, 0.3)
    t2 = T('three point five')
    L = new(); arrow_r(L, 620, 720, 450, goldL, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([740, 330, 1000, 590], fill=gold + (255,), outline=goldL + (255,), width=8); txt(C, '3.5%', BOLD(100), 400, navy, 255, x=870); txt(C, 'RAISE', BOLD(46), 510, navy, 255, x=870); fr = A_(fr, C, (720, 310, 1020, 610), t, t2)
    t3 = T('it adds')
    L = new(); arrow_r(L, 1030, 1130, 450, goldL, 255 * E_(t, t3)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); mini_check(C, 1150, 290, 1630, 600, green, '+$72', 'PER MONTH', 'THE RAISE', 110); fr = A_(fr, C, (1130, 270, 1650, 620), t, t3)
    t4 = T('bringing each check')
    if t > t4: fr = P(fr, 'NEW CHECK: ABOUT $2,143', 760, t, t4, gold, navy, 70)
    return frame(fr)
def s11c(t):
    fr = base_(t, 93, 'OVER ONE YEAR'); T = lambda m: B11.tt(2, m)
    if t > 0.3:
        C = new(); txt(C, '$72  x  12 MONTHS', BOLD(110), 270, white, 255, x=960); fr = A_(fr, C, (140, 250, 1780, 420), t, 0.3)
    fr = months(fr, t, 460, 0.6, hl=tuple(range(12)), step=0.05)
    t2 = T('about eight hundred')
    if t > t2: fr = P(fr, '= ABOUT $864 MORE A YEAR', 700, t, t2, green, navy, 80)
    return frame(fr)
def s11d(t):
    fr = base_(t, 94, 'HOLD ON TO THIS NUMBER'); T = lambda m: B11.tt(3, m)
    if t > 0.3:
        C = new(); card_(C, 460, 280, 1460, 700, green); bill(C, 960, 430, 300, 146, 0, 255); txt(C, '+$72', BOLD(160), 520, green, 255, x=960); fr = A_(fr, C, (440, 260, 1480, 720), t, 0.3)
    t2 = T('watch what')
    if t > t2:
        C = new(); magnifier(C, 1650, 480, 90); txt(C, '?', BOLD(120), 430, goldL, 255, x=1635); fr = A_(fr, C, (1500, 330, 1800, 640), t, t2)
    fr = P(fr, 'NOW WATCH WHAT HAPPENS TO IT', 800, t, T('watch what'), red, (255, 255, 255), 56)
    return frame(fr)

# ============ BLOCCO 12 (829) ============
B12 = Blk2(["Number three: Medicare Part B.",
            "Part B pays for doctor visits and outpatient care, and for most retirees the premium is taken straight out of the Social Security check, before any money is deposited.",
            "In twenty twenty five, it was one hundred eighty five dollars a month.", "In twenty twenty six, it rose to two hundred two dollars and ninety cents.",
            "That is seventeen dollars and ninety cents more, an increase of nearly ten percent."],
           [[0], [1], [2, 3], [4]], 829)
def s12a(t):
    fr = base_(t, 101, 'NUMBER THREE'); T = lambda m: B12.tt(0, m)
    if t > 0.3:
        C = new(); badge(C, 330, 330, 3, red, 70); txt(C, 'MEDICARE PART B', BOLD(100), 290, white, 255, x=1090); fr = A_(fr, C, (200, 240, 1820, 440), t, 0.3)
    if t > 0.8:
        C = new(); medicare_card(C, 960, 640, 1.5); fr = A_(fr, C, (640, 430, 1280, 860), t, 0.8)
    return frame(fr)
def s12b(t):
    fr = base_(t, 102, 'WHERE PART B COMES OUT'); T = lambda m: B12.tt(1, m)
    fr = chip(fr, 'DOCTOR VISITS', 560, 260, t, 0.3, goldL, 48); fr = chip(fr, 'OUTPATIENT CARE', 1360, 260, t, 0.7, goldL, 48)
    t1 = T('for most retirees')
    if t > t1:
        C = new(); mini_check(C, 110, 400, 590, 720, blue, '$2,071', 'PER MONTH', 'MONTHLY CHECK', 110); fr = A_(fr, C, (90, 380, 610, 740), t, t1)
    t2 = T('taken straight')
    L = new(); arrow_r(L, 620, 720, 560, red, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); medicare_card(C, 960, 560, 0.9); txt(C, 'PART B TAKEN FIRST', BOLD(44), 700, red, 255, x=960); fr = A_(fr, C, (690, 400, 1230, 760), t, t2)
    t3 = T('before any money')
    L = new(); arrow_r(L, 1200, 1300, 560, goldL, 255 * E_(t, t3)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); card_(C, 1320, 400, 1800, 720, green); building(C, 1560, 520, 180, 160, green); txt(C, 'DEPOSIT', BOLD(60), 640, green, 255, x=1560); fr = A_(fr, C, (1300, 380, 1820, 740), t, t3)
    fr = P(fr, 'BEFORE ANY MONEY IS DEPOSITED', 810, t, T('before any money'), goldL, navy, 50)
    return frame(fr)
def s12c(t):
    fr = base_(t, 103, 'PART B PER MONTH'); T = lambda m: B12.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 860, 700, gold); txt(C, '2025', BOLD(90), 320, goldL, 255, x=500); txt(C, '$185.00', BOLD(130), 450, white, 255, x=500); fr = A_(fr, C, (120, 270, 880, 720), t, 0.3)
    t2 = T('In twenty twenty six') - 0.1
    L = new(); arrow_r(L, 890, 1030, 500, red, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); card_(C, 1060, 290, 1780, 700, red); txt(C, '2026', BOLD(90), 320, red, 255, x=1420); txt(C, '$202.90', BOLD(130), 450, white, 255, x=1420); fr = A_(fr, C, (1040, 270, 1800, 720), t, t2)
    fr = P(fr, 'IT ROSE FROM ONE YEAR TO THE NEXT', 800, t, 1.0, red, (255, 255, 255), 50)
    return frame(fr)
def s12d(t):
    fr = base_(t, 104, 'THE INCREASE'); T = lambda m: B12.tt(3, m)
    if t > 0.3:
        C = new(); up_arrow(C, 480, 500, 1.6, red); txt(C, '+$17.90', BOLD(190), 330, red, 255, x=1130); txt(C, 'A MONTH MORE', BOLD(70), 560, white, 255, x=1130); fr = A_(fr, C, (260, 250, 1800, 660), t, 0.3)
    t2 = T('nearly ten percent')
    if t > t2: fr = P(fr, 'NEARLY 10% MORE', 770, t, t2, red, (255, 255, 255), 80)
    return frame(fr)

# ============ BLOCCO 13 (642) ============
B13 = Blk2(["Here is a number worth pausing on.", "Two hundred two dollars and ninety cents is almost ten percent of the average Social Security check.",
            "Nearly one dollar out of every ten goes to Part B before Frank or Mary ever see it.", "And Part B is only one piece of Medicare.",
            "So any increase in this premium goes straight to the heart of the budget."],
           [[0, 1], [2], [3, 4]], 642)
def s13a(t):
    fr = base_(t, 111, 'A NUMBER WORTH PAUSING ON'); T = lambda m: B13.tt(0, m)
    if t > 0.3:
        C = new(); d = ImageDraw.Draw(C); cx, cy, r = 600, 540, 230
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=blue + (255,)); d.pieslice([cx - r, cy - r, cx + r, cy + r], -90, -90 + 360 * 0.098, fill=red + (255,)); d.ellipse([cx - 130, cy - 130, cx + 130, cy + 130], fill=navy + (255,))
        txt(C, '~10%', BOLD(90), cy - 60, white, 255, x=cx); fr = A_(fr, C, (330, 290, 870, 800), t, 0.3)
    t2 = T('Two hundred two')
    if t > t2:
        C = new(); txt(C, '$202.90', BOLD(150), 340, red, 255, x=1360); txt(C, 'PART B', BOLD(60), 500, white, 255, x=1360); txt(C, 'OF A $2,071 CHECK', BOLD(56), 580, goldL, 255, x=1360); fr = A_(fr, C, (960, 300, 1800, 680), t, t2)
    fr = P(fr, 'ALMOST TEN PERCENT OF THE CHECK', 830, t, T('almost ten percent'), red, (255, 255, 255), 50)
    return frame(fr)
def s13b(t):
    fr = base_(t, 112, 'ONE DOLLAR OUT OF TEN'); T = lambda m: B13.tt(1, m)
    if t > 0.3:
        C = new()
        for k in range(10): coin(C, 260 + k * 160, 430, 62, 255)
        d = ImageDraw.Draw(C); d.ellipse([260 - 80, 430 - 80, 260 + 80, 430 + 80], outline=red + (255,), width=10)
        fr = A_(fr, C, (140, 330, 1800, 540), t, 0.3)
    t2 = T('goes to Part B')
    if t > t2:
        L = new(); arrow_d(L, 260, 530, 640, red, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
        C = new(); medicare_card(C, 420, 760, 0.7); txt(C, 'PART B', BOLD(60), 700, red, 255, x=900); fr = A_(fr, C, (240, 640, 1100, 880), t, t2)
    t3 = T('Frank or Mary')
    if t > t3:
        C = new(); avatar(C, 1500, 760, blue, 1.6); avatar(C, 1650, 760, pink, 1.6); fr = A_(fr, C, (1400, 660, 1760, 860), t, t3)
        fr = P(fr, 'BEFORE THEY EVER SEE IT', 900, t, t3, goldL, navy, 46, 1500) if False else fr
    fr = P(fr, 'ONE DOLLAR OUT OF EVERY TEN', 900, t, 0.9, red, (255, 255, 255), 54)
    return frame(fr)
def s13c(t):
    fr = base_(t, 113, 'ONE PIECE OF MEDICARE'); T = lambda m: B13.tt(2, m)
    for k, (lab, hot) in enumerate([('PART A', 0), ('PART B', 1), ('PART C', 0), ('PART D', 0)]):
        t0 = 0.3 + 0.2 * k
        if t < t0: continue
        cx = 330 + k * 420; C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([cx - 180, 290, cx + 180, 450], radius=26, fill=(red if hot else card) + (255,), outline=(goldL if hot else (80, 100, 130)) + (255,), width=6)
        txt(C, lab, BOLD(64), 340, (255, 255, 255) if hot else (170, 185, 205), 255, x=cx)
        fr = A_(fr, C, (cx - 200, 270, cx + 200, 470), t, t0, 0.5)
    t2 = T('any increase')
    if t > t2:
        C = new(); card_(C, 380, 540, 960, 800, red); txt(C, 'PREMIUM UP', BOLD(70), 590, red, 255, x=670); up_arrow(C, 480, 700, 0.6, red); txt(C, 'EVERY YEAR?', BOLD(50), 700, white, 255, x=720); fr = A_(fr, C, (360, 520, 980, 820), t, t2)
        L = new(); arrow_r(L, 1000, 1110, 670, red, 255 * E_(t, t2 + 0.3)); fr = Image.alpha_composite(fr, L)
        C = new(); wallet(C, 1400, 650, 1.3); txt(C, 'YOUR BUDGET', BOLD(56), 760, white, 255, x=1400); fr = A_(fr, C, (1180, 520, 1640, 840), t, t2 + 0.3)
    fr = P(fr, 'PART B IS ONLY ONE PIECE', 880, t, T('only one piece'), goldL, navy, 50)
    return frame(fr)

# ============ BLOCCO 14 (678) ============
B14 = Blk2(["What about twenty twenty seven?", "The official Medicare Trustees Report projects a Part B premium of about two hundred nine dollars and fifty cents.",
            "That is six dollars and sixty cents more.", "It is only a projection.",
            "The Centers for Medicare and Medicaid Services usually announces the official number in November, and the final figure can move in either direction."],
           [[0, 1], [2, 3], [4]], 678)
def s14a(t):
    fr = base_(t, 121, 'PART B IN 2027'); T = lambda m: B14.tt(0, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 860, 700, grey); txt(C, '2026', BOLD(90), 320, grey, 255, x=500); txt(C, '$202.90', BOLD(130), 450, white, 255, x=500); fr = A_(fr, C, (120, 270, 880, 720), t, 0.3)
    t2 = T('The official')
    L = new(); arrow_r(L, 890, 1030, 500, goldL, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); card_(C, 1060, 290, 1780, 700, gold); txt(C, '2027 PROJECTION', BOLD(60), 320, goldL, 255, x=1420); txt(C, '$209.50', BOLD(130), 450, white, 255, x=1420); txt(C, 'MEDICARE TRUSTEES REPORT', BOLD(38), 620, grey, 255, x=1420); fr = A_(fr, C, (1040, 270, 1800, 720), t, t2)
    fr = P(fr, 'THE 2027 PART B PROJECTION', 800, t, 1.0, goldL, navy, 52)
    return frame(fr)
def s14b(t):
    fr = base_(t, 122, 'ONLY A PROJECTION'); T = lambda m: B14.tt(1, m)
    if t > 0.3:
        C = new(); up_arrow(C, 520, 500, 1.5, red); txt(C, '+$6.60', BOLD(200), 340, red, 255, x=1130); txt(C, 'A MONTH MORE', BOLD(70), 570, white, 255, x=1130); fr = A_(fr, C, (300, 260, 1800, 680), t, 0.3)
    t2 = T('only a projection')
    if t > t2 - 0.3: fr = stamp(fr, 'ONLY A PROJECTION', 960, 800, -6, gold, back((t - t2 + 0.3) / 0.4), 70)
    return frame(fr)
def s14c(t):
    fr = base_(t, 123, 'THE OFFICIAL NUMBER'); T = lambda m: B14.tt(2, m)
    if t > 0.3:
        C = new(); building(C, 370, 440, 260, 220, blue); txt(C, 'CMS ANNOUNCES', BOLD(54), 610, white, 255, x=370); txt(C, 'THE OFFICIAL NUMBER', BOLD(46), 675, blue, 255, x=370); fr = A_(fr, C, (110, 270, 650, 730), t, 0.3)
    t2 = T('in November')
    if t > t2 - 0.2:
        C = new(); cal_card(C, 700, 300, 1220, 700, 'USUALLY IN', 'NOV', bigsize=190, headcol=gold); fr = A_(fr, C, (680, 280, 1240, 720), t, t2 - 0.2)
    t3 = T('either direction')
    if t > t3 - 0.5:
        C = new(); up_arrow(C, 1450, 470, 0.9, green); arrow_d(C, 1640, 400, 560, red); txt(C, 'EITHER WAY', BOLD(56), 600, goldL, 255, x=1540); fr = A_(fr, C, (1280, 330, 1800, 700), t, t3 - 0.5)
    fr = P(fr, 'THE FINAL FIGURE CAN CHANGE', 810, t, T('the final figure'), goldL, navy, 52)
    return frame(fr)

# ============ BLOCCO 15 (750) ============
B15 = Blk2(["Let's follow the money for Frank and Mary.", "Today, after Part B, their deposit is one thousand eight hundred sixty eight dollars and ten cents.",
            "After the raise and the projected new premium, the deposit would be one thousand nine hundred thirty three dollars and fifty cents.",
            "So in this example, the seventy two dollar raise becomes about sixty five dollars in the bank.", "Six dollars and sixty cents of it goes to Medicare."],
           [[0, 1], [2], [3, 4]], 750)
def deposit_row(t, T, title, a, b, c, col):
    fr = base_(t, 131, title)
    t1 = 0.3
    if t > t1:
        C = new(); mini_check(C, 110, 300, 560, 640, blue, a, 'PER MONTH', 'SOCIAL SECURITY', 110); fr = A_(fr, C, (90, 280, 580, 660), t, t1)
        L = new(); txt(L, '-', BOLD(150), 400, red, 255 * E_(t, t1 + 0.5), x=650); fr = Image.alpha_composite(fr, L)
    t2 = T('after Part B') if False else t1 + 1.0
    if t > t2:
        C = new(); card_(C, 740, 330, 1170, 610, red); txt(C, 'PART B', BOLD(64), 360, red, 255, x=955); txt(C, b, BOLD(78), 460, white, 255, x=955); fr = A_(fr, C, (720, 310, 1190, 630), t, t2)
        L = new(); txt(L, '=', BOLD(150), 400, goldL, 255 * E_(t, t2 + 0.5), x=1250); fr = Image.alpha_composite(fr, L)
    t3 = t1 + 2.0
    if t > t3:
        C = new(); mini_check(C, 1330, 300, 1800, 640, green, c, 'IN THE BANK', 'DEPOSIT', 80); fr = A_(fr, C, (1310, 280, 1820, 660), t, t3)
    return fr
def s15a(t):
    fr = deposit_row(t, lambda m: 1.0, "TODAY'S DEPOSIT", '$2,071', '-$202.90', '$1,868.10', green)
    fr = P(fr, 'TODAY: ABOUT $1,868 IN THE BANK', 800, t, 3.0, goldL, navy, 52)
    return frame(fr)
def s15b(t):
    fr = deposit_row(t, lambda m: 1.0, 'AFTER THE RAISE', '$2,143', '-$209.50', '$1,933.50', green)
    fr = P(fr, 'AFTER: ABOUT $1,933 IN THE BANK', 800, t, 3.0, goldL, navy, 52)
    return frame(fr)
def s15c(t):
    fr = base_(t, 133, 'WHAT REALLY REACHES THE BANK'); T = lambda m: B15.tt(2, m)
    if t > 0.3:
        C = new(); txt(C, '$1,868.10   >   $1,933.50', BOLD(96), 280, white, 255, x=960); fr = A_(fr, C, (140, 260, 1780, 410), t, 0.3)
    t2 = T('about sixty five')
    if t > t2 - 0.3: fr = P(fr, '+ABOUT $65 IN THE BANK', 450, t, t2 - 0.3, green, navy, 80)
    t3 = T('Six dollars')
    if t > 0.9:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([260, 700, 260 + 1271, 800], radius=24, fill=green + (255,)); d.rounded_rectangle([260 + 1271, 700, 1660, 800], radius=24, fill=blue + (255,))
        txt(C, '$72 RAISE', BOLD(46), 630, white, 255, x=960); txt(C, '$65.40 IN THE BANK', BOLD(50), 725, navy, 255, x=900)
        fr = A_(fr, C, (240, 600, 1680, 820), t, 0.9)
    if t > t3 - 0.2:
        C = new(); arrow_d(C, 1596, 820, 880, blue); txt(C, '$6.60 TO MEDICARE', BOLD(54), 900, blue, 255, x=1400); fr = A_(fr, C, (1100, 800, 1700, 980), t, t3 - 0.2)
    return frame(fr)

FNS2 = {11: [s11a, s11b, s11c, s11d], 12: [s12a, s12b, s12c, s12d], 13: [s13a, s13b, s13c], 14: [s14a, s14b, s14c], 15: [s15a, s15b, s15c]}
BLK2 = {11: B11, 12: B12, 13: B13, 14: B14, 15: B15}
if __name__ == '__main__':
    mode = sys.argv[1]; b = int(sys.argv[2]); fns = FNS2[b]; FS = BLK2[b].FS
    sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, len(fns) + 1))
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.35, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}px{b}_{i}_{int(fq*100)}.png')
        print(b, FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b{b}-0{i}.mp4'); print('done', b, i, f, flush=True)
