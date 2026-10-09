from v6b16_20 import *
import sys

def warn(C, cx, cy, s=1.0, col=red):
    d = ImageDraw.Draw(C); d.polygon([(cx, cy - 100 * s), (cx + 110 * s, cy + 80 * s), (cx - 110 * s, cy + 80 * s)], fill=A(col, 255), outline=A(goldL, 255)); txt(C, '!', BOLD(int(110 * s)), cy - 55 * s, (255, 255, 255), 255, x=cx)
def letter(C, x0, y0, x1, y1, col=goldL):
    d = ImageDraw.Draw(C); d.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=(236, 240, 245, 255), outline=A(col, 255), width=5); d.line([x0 + 8, y0 + 8, (x0 + x1) / 2, (y0 + y1) / 2 + 10, x1 - 8, y0 + 8], fill=A(col, 255), width=5)

# ============ BLOCCO 21 (996) ============
B21 = Blk2(["Number five: the other numbers that change on the same day.", "The announcement is not only the raise.",
            "The Social Security Administration also publishes the new taxable maximum, which was one hundred eighty four thousand five hundred dollars in twenty twenty six.",
            "It also publishes the earnings limit for people who claim before full retirement age, twenty four thousand four hundred eighty dollars in twenty twenty six, and sixty five thousand one hundred sixty dollars in the year you reach full retirement age.",
            "These limits usually rise a little with average wages."],
           [[0, 1], [2], [3], [4]], 996)
def s21a(t):
    fr = base_(t, 201, 'NUMBER FIVE'); T = lambda m: B21.tt(0, m)
    if t > 0.3:
        C = new(); badge(C, 250, 340, 5, gold, 70); txt(C, 'THE OTHER NUMBERS', BOLD(76), 290, white, 255, x=1080); txt(C, 'THAT CHANGE THE SAME DAY', BOLD(76), 375, goldL, 255, x=1080); fr = A_(fr, C, (120, 230, 1800, 480), t, 0.3)
    t2 = T('The announcement')
    if t > t2 - 0.2:
        C = new(); cal_card(C, 140, 540, 560, 840, 'OCTOBER', '14', bigsize=150, headcol=red); fr = A_(fr, C, (120, 520, 580, 860), t, t2 - 0.2)
    for k, (lab, col) in enumerate([('THE RAISE', green), ('TAXABLE MAXIMUM', gold), ('EARNINGS LIMITS', blue)]):
        fr = chip(fr, lab, 1130, 540 + k * 110, t, t2 + 0.2 + 0.35 * k, col, 50, fillc=card, tcol=white)
    fr = P(fr, 'NOT ONLY THE RAISE', 900, t, t2 + 0.2, goldL, navy, 46, 1130) if False else fr
    return frame(fr)
def s21b(t):
    fr = base_(t, 202, 'THE TAXABLE MAXIMUM'); T = lambda m: B21.tt(1, m)
    if t > 0.3:
        C = new(); card_(C, 140, 270, 1780, 640, gold); txt(C, 'MOST EARNINGS COUNTED FOR SOCIAL SECURITY TAX', BOLD(46), 295, white, 255, x=960)
        d = ImageDraw.Draw(C); d.rounded_rectangle([240, 420, 1200, 520], radius=22, fill=green + (255,)); d.rounded_rectangle([1200, 420, 1680, 520], radius=22, fill=grey + (255,)); d.rectangle([1180, 420, 1200, 520], fill=green + (255,))
        txt(C, 'COUNTED', BOLD(50), 442, navy, 255, x=720); txt(C, 'ABOVE: NOT COUNTED', BOLD(40), 450, navy, 255, x=1440)
        d.line([1200, 390, 1200, 560], fill=white + (255,), width=8)
        fr = A_(fr, C, (120, 250, 1800, 660), t, 0.3)
    t2 = T('which was')
    if t > t2 - 0.3:
        C = new(); txt(C, '$184,500', BOLD(150), 670, goldL, 255, x=960); txt(C, 'TAXABLE MAXIMUM IN 2026', BOLD(54), 830, white, 255, x=960); fr = A_(fr, C, (360, 650, 1560, 900), t, t2 - 0.3)
    return frame(fr)
def s21c(t):
    fr = base_(t, 203, 'THE EARNINGS LIMIT'); T = lambda m: B21.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 270, 900, 700, gold); txt(C, 'BEFORE FULL', BOLD(54), 300, white, 255, x=520); txt(C, 'RETIREMENT AGE', BOLD(54), 365, white, 255, x=520); txt(C, '$24,480', BOLD(130), 470, goldL, 255, x=520); txt(C, 'IN 2026', BOLD(50), 620, grey, 255, x=520); fr = A_(fr, C, (120, 250, 920, 720), t, 0.3)
    t2 = T('and sixty five') - 0.1
    if t > t2:
        C = new(); card_(C, 1020, 270, 1780, 700, blue); txt(C, 'THE YEAR YOU REACH', BOLD(50), 300, white, 255, x=1400); txt(C, 'FULL RETIREMENT AGE', BOLD(50), 365, white, 255, x=1400); txt(C, '$65,160', BOLD(130), 470, blue, 255, x=1400); txt(C, 'IN 2026', BOLD(50), 620, grey, 255, x=1400); fr = A_(fr, C, (1000, 250, 1800, 720), t, t2)
    fr = P(fr, 'LIMITS ON EARNINGS WHILE YOU COLLECT', 810, t, 1.0, goldL, navy, 50)
    return frame(fr)
def s21d(t):
    fr = base_(t, 204, 'THEY USUALLY RISE'); T = lambda m: B21.tt(3, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 880, 700, gold); [avatar(C, 330 + k * 130, 520, [blue, pink, gold][k], 1.6) for k in range(3)]; txt(C, 'AVERAGE WAGES', BOLD(62), 330, white, 255, x=510); up_arrow(C, 760, 540, 0.6, green); fr = A_(fr, C, (120, 270, 900, 720), t, 0.3)
    t2 = T('usually rise')
    if t > t2 - 0.3:
        L = new(); arrow_r(L, 910, 1030, 500, goldL, 255 * E_(t, t2 - 0.3)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 1060, 290, 1780, 700, green); txt(C, 'THE LIMITS', BOLD(70), 340, white, 255, x=1420); txt(C, 'RISE A LITTLE', BOLD(70), 420, green, 255, x=1420); up_arrow(C, 1420, 600, 0.55, green); fr = A_(fr, C, (1040, 270, 1800, 720), t, t2 - 0.3)
    fr = P(fr, 'USUALLY A LITTLE EVERY YEAR', 810, t, 1.2, goldL, navy, 52)
    return frame(fr)

# ============ BLOCCO 22 (698) ============
B22 = Blk2(["One more thing that most people do not know.", "The raise is not only for people who already collect.",
            "If you are at least sixty two, even if you have not claimed yet, your future benefit grows with each Cola as well.",
            "That is one more reason why waiting does not mean standing still, and it is a topic we explained in our video about claiming at sixty two versus seventy."],
           [[0, 1], [2], [3]], 698)
def s22a(t):
    fr = base_(t, 211, 'ONE MORE THING'); T = lambda m: B22.tt(0, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 880, 700, green); avatar(C, 330, 540, green, 2.0); check(C, 700, 470, 55, green); txt(C, 'ALREADY COLLECTING', BOLD(56), 320, white, 255, x=510); txt(C, 'GETS THE RAISE', BOLD(54), 600, green, 255, x=620); fr = A_(fr, C, (120, 270, 900, 720), t, 0.3)
    t2 = T('not only')
    if t > t2:
        C = new(); card_(C, 1040, 290, 1780, 700, gold); avatar(C, 1230, 540, gold, 2.0); txt(C, '?', BOLD(130), 400, goldL, 255, x=1620); txt(C, 'NOT CLAIMED YET', BOLD(52), 320, white, 255, x=1410); txt(C, 'ALSO GETS IT', BOLD(54), 600, goldL, 255, x=1520); fr = A_(fr, C, (1020, 270, 1800, 720), t, t2)
    fr = P(fr, 'THE RAISE IS NOT ONLY FOR PEOPLE WHO COLLECT', 810, t, 1.0, goldL, navy, 44)
    return frame(fr)
def s22b(t):
    fr = base_(t, 212, 'AT LEAST SIXTY TWO'); T = lambda m: B22.tt(1, m)
    if t > 0.3:
        C = new(); d = ImageDraw.Draw(C); d.ellipse([160, 300, 480, 620], fill=gold + (255,), outline=goldL + (255,), width=8); txt(C, '62+', BOLD(130), 390, navy, 255, x=320); txt(C, 'NOT CLAIMED YET', BOLD(44), 660, white, 255, x=320); fr = A_(fr, C, (100, 280, 560, 740), t, 0.3)
    t2 = T('your future benefit')
    if t > t2 - 0.4:
        C = new()
        for k in range(4):
            h_ = 150 + k * 55; C.alpha_composite(bar(h_, gold, 150), (700 + k * 240, 700 - h_)); txt(C, 'COLA', BOLD(44), 700 - h_ - 60, goldL, 255, x=775 + k * 240)
        txt(C, 'FUTURE BENEFIT GROWS', BOLD(60), 740, white, 255, x=1150); fr = A_(fr, C, (520, 290, 1800, 830), t, t2 - 0.4)
        L = new(); arrow_r(L, 520, 680, 520, goldL, 255 * E_(t, t2 - 0.4)); fr = Image.alpha_composite(fr, L)
    return frame(fr)
def s22c(t):
    fr = base_(t, 213, 'WAITING IS NOT STANDING STILL'); T = lambda m: B22.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 1780, 520, gold); txt(C, 'WAITING DOES NOT MEAN STANDING STILL', BOLD(70), 350, white, 255, x=960); txt(C, 'EACH COLA STILL COUNTS', BOLD(56), 440, goldL, 255, x=960); fr = A_(fr, C, (120, 270, 1800, 540), t, 0.3)
    t2 = T('our video')
    if t > t2 - 0.4:
        C = new(); d = ImageDraw.Draw(C)
        for k, (age, col) in enumerate([('62', red), ('70', green)]):
            d.ellipse([400 + k * 700, 590, 640 + k * 700, 830], fill=col + (255,), outline=goldL + (255,), width=6); txt(C, age, BOLD(120), 645, (255, 255, 255), 255, x=520 + k * 700)
        txt(C, 'VS', BOLD(80), 680, goldL, 255, x=960); fr = A_(fr, C, (360, 570, 1520, 850), t, t2 - 0.4)
    fr = P(fr, 'EXPLAINED IN OUR VIDEO: 62 VS 70', 880, t, T('claiming') if False else 1.2, goldL, navy, 44)
    return frame(fr)

# ============ BLOCCO 23 (536) ============
B23 = Blk2(["When does the raise start?", "It applies to the benefits for December, which are paid in January.", "So the new amount shows up in your January deposit.",
            "The Social Security Administration sends a notice before then, and you can check your amount for free in your my Social Security account at ssa dot gov."],
           [[0, 1], [2], [3]], 536)
def s23a(t):
    fr = base_(t, 221, 'WHEN DOES IT START?'); T = lambda m: B23.tt(0, m)
    if t > 0.3:
        C = new(); cal_card(C, 200, 300, 700, 700, 'BENEFITS FOR', 'DEC', bigsize=170, headcol=blue); fr = A_(fr, C, (180, 280, 720, 720), t, 0.3)
    t2 = T('paid in January') - 0.3
    L = new(); arrow_r(L, 760, 1000, 500, goldL, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); cal_card(C, 1060, 300, 1560, 700, 'PAID IN', 'JAN', bigsize=170, headcol=green); fr = A_(fr, C, (1040, 280, 1580, 720), t, t2)
    fr = P(fr, 'DECEMBER BENEFITS, PAID IN JANUARY', 800, t, 1.0, goldL, navy, 52)
    return frame(fr)
def s23b(t):
    fr = base_(t, 222, 'YOUR JANUARY DEPOSIT'); T = lambda m: B23.tt(1, m)
    if t > 0.3:
        C = new(); mini_check(C, 440, 290, 1120, 650, green, 'NEW', 'AMOUNT', 'JANUARY DEPOSIT', 150); up_arrow(C, 1340, 470, 1.1, green); fr = A_(fr, C, (420, 260, 1500, 700), t, 0.3)
    fr = P(fr, 'THE NEW AMOUNT SHOWS UP IN JANUARY', 790, t, 1.0, green, navy, 52)
    return frame(fr)
def s23c(t):
    fr = base_(t, 223, 'HOW TO CHECK'); T = lambda m: B23.tt(2, m)
    if t > 0.3:
        C = new(); letter(C, 160, 320, 620, 620); txt(C, 'NOTICE FROM SSA', BOLD(50), 650, white, 255, x=390); fr = A_(fr, C, (140, 300, 640, 720), t, 0.3)
    t2 = T('check your amount') - 0.2
    if t > t2:
        L = new(); arrow_r(L, 660, 780, 470, goldL, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
        C = new(); card_(C, 800, 300, 1780, 700, gold); txt(C, 'MY SOCIAL SECURITY', BOLD(66), 350, white, 255, x=1290); txt(C, 'ACCOUNT', BOLD(66), 425, goldL, 255, x=1290); txt(C, 'ssa.gov', BOLD(100), 540, white, 255, x=1290); fr = A_(fr, C, (780, 280, 1800, 720), t, t2)
    fr = P(fr, 'CHECK YOUR AMOUNT FOR FREE', 800, t, 1.0, green, navy, 52)
    return frame(fr)

# ============ BLOCCO 24 (732) ============
B24 = Blk2(["One warning.", "Every year, right after the announcement, scammers send fake texts and calls saying you must confirm or pay to receive your raise.",
            "The Social Security Administration has warned about scams like this for years.",
            "Its guidance is simple: if a message pressures you or asks for payment, hang up, and contact the agency directly through ssa dot gov."],
           [[0, 1], [2], [3]], 732)
def s24a(t):
    fr = base_(t, 231, 'ONE WARNING'); T = lambda m: B24.tt(0, m)
    if t > 0.3:
        C = new(); warn(C, 330, 520, 1.8); fr = A_(fr, C, (100, 340, 560, 720), t, 0.3)
    t2 = T('scammers') - 0.2
    if t > t2:
        C = new(); phone(C, 900, 520, 1.5, 255, t, True); bubble(C, 1050, 330, 1760, 470, 'CONFIRM YOUR RAISE\nNOW!', fillc=(255, 225, 225), tcol=red, size=48, tail='left'); fr = A_(fr, C, (780, 300, 1800, 800), t, t2)
    t3 = T('or pay')
    if t > t3:
        C = new(); bubble(C, 1050, 560, 1760, 700, 'PAY TO RECEIVE\nYOUR RAISE!', fillc=(255, 225, 225), tcol=red, size=48, tail='left'); fr = A_(fr, C, (1030, 540, 1780, 760), t, t3)
    fr = P(fr, 'FAKE TEXTS AND CALLS: A SCAM', 860, t, 1.2, red, (255, 255, 255), 52)
    return frame(fr)
def s24b(t):
    fr = base_(t, 232, 'THE AGENCY HAS WARNED'); T = lambda m: B24.tt(1, m)
    if t > 0.3:
        C = new(); building(C, 480, 480, 300, 250, blue); txt(C, 'SOCIAL SECURITY', BOLD(56), 680, white, 255, x=480); txt(C, 'ADMINISTRATION', BOLD(56), 745, white, 255, x=480); fr = A_(fr, C, (140, 290, 820, 820), t, 0.3)
    t2 = T('warned')
    if t > t2:
        C = new(); shield(C, 1250, 470, 1.6, blue); txt(C, 'HAS WARNED ABOUT', BOLD(60), 660, white, 255, x=1450); txt(C, 'SCAMS FOR YEARS', BOLD(60), 730, red, 255, x=1450); fr = A_(fr, C, (1000, 290, 1800, 800), t, t2)
    return frame(fr)
def s24c(t):
    fr = base_(t, 233, 'THE SIMPLE RULE'); T = lambda m: B24.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 290, 640, 700, red); txt(C, 'PRESSURE OR', BOLD(46), 340, white, 255, x=390); txt(C, 'ASKS FOR PAYMENT', BOLD(46), 405, white, 255, x=390); warn(C, 390, 560, 1.0); fr = A_(fr, C, (120, 270, 660, 720), t, 0.3)
    t2 = T('hang up') - 0.2
    L = new(); arrow_r(L, 660, 740, 500, red, 255 * E_(t, t2)); fr = Image.alpha_composite(fr, L)
    if t > t2:
        C = new(); card_(C, 760, 290, 1160, 700, gold); phone(C, 960, 500, 1.0, 255, t, False); txt(C, 'HANG UP', BOLD(70), 620, goldL, 255, x=960); fr = A_(fr, C, (740, 270, 1180, 720), t, t2)
    t3 = T('contact the agency') - 0.2
    L = new(); arrow_r(L, 1190, 1260, 500, green, 255 * E_(t, t3)); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); card_(C, 1280, 290, 1780, 700, green); check(C, 1530, 400, 55, green); txt(C, 'CONTACT THE', BOLD(46), 500, white, 255, x=1530); txt(C, 'AGENCY DIRECTLY', BOLD(46), 565, white, 255, x=1530); txt(C, 'ssa.gov', BOLD(70), 630, green, 255, x=1530); fr = A_(fr, C, (1260, 270, 1800, 720), t, t3)
    return frame(fr)

# ============ BLOCCO 25 (716) ============
B25 = Blk2(["Now let's put it all together on one check.", "In our example, the raise looks like seventy two dollars.",
            "Medicare Part B takes about six dollars and sixty cents of it, leaving about sixty five dollars.", "For Mary, that is the end of the story.",
            "For Frank, a little more of his benefit is also counted as taxable.", "Same raise, same size check, two different real raises."],
           [[0, 1], [2], [3, 4], [5]], 716)
def s25a(t):
    fr = base_(t, 241, 'ONE CHECK, ALL TOGETHER'); T = lambda m: B25.tt(0, m)
    if t > 0.3:
        C = new(); mini_check(C, 640, 280, 1280, 640, gold, '$2,071', 'PER MONTH', 'ONE REAL CHECK', 140); fr = A_(fr, C, (620, 260, 1300, 660), t, 0.3)
    t2 = T('raise looks')
    if t > t2:
        C = new(); card_(C, 560, 690, 1360, 860, green); bill(C, 720, 775, 200, 98, 0, 255); txt(C, '+$72', BOLD(110), 725, green, 255, x=1090); fr = A_(fr, C, (540, 670, 1380, 880), t, t2)
    return frame(fr)
def s25b(t):
    fr = base_(t, 242, 'WHAT STAYS IN THE BANK'); T = lambda m: B25.tt(1, m)
    if t > 0.3:
        C = new(); txt(C, '$72  -  $6.60  =  ABOUT $65', BOLD(100), 290, white, 255, x=960); fr = A_(fr, C, (140, 270, 1780, 430), t, 0.3)
    if t > 0.9:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([260, 540, 260 + 1271, 650], radius=24, fill=green + (255,)); d.rounded_rectangle([260 + 1271, 540, 1660, 650], radius=24, fill=blue + (255,))
        txt(C, '$65.40 IN THE BANK', BOLD(56), 565, navy, 255, x=900); fr = A_(fr, C, (240, 520, 1680, 670), t, 0.9)
    t2 = T('Medicare Part B')
    if t > t2 - 0.2:
        C = new(); arrow_d(C, 1596, 660, 740, blue); txt(C, '$6.60 TO MEDICARE', BOLD(54), 760, blue, 255, x=1400); fr = A_(fr, C, (1100, 650, 1750, 850), t, t2 - 0.2)
    fr = P(fr, 'ABOUT $65 LEFT OF THE $72', 880, t, 1.4, goldL, navy, 48, 700)
    return frame(fr)
def s25c(t):
    fr = base_(t, 243, 'MARY AND FRANK'); T = lambda m: B25.tt(2, m)
    if t > 0.3:
        C = new(); card_(C, 140, 270, 900, 720, pink); avatar(C, 260, 520, pink, 1.7); txt(C, 'MARY', BOLD(70), 300, pink, 255, x=620); txt(C, 'ABOUT $65', BOLD(86), 440, white, 255, x=640); txt(C, 'END OF THE STORY', BOLD(46), 570, green, 255, x=640); check(C, 260, 650, 38, green); fr = A_(fr, C, (120, 250, 920, 740), t, 0.3)
    t2 = T('For Frank') - 0.1
    if t > t2:
        C = new(); card_(C, 1020, 270, 1780, 720, blue); avatar(C, 1110, 520, blue, 1.7); txt(C, 'FRANK', BOLD(70), 300, blue, 255, x=1480); txt(C, 'ABOUT $65', BOLD(86), 440, white, 255, x=1500); txt(C, '+ MORE OF HIS BENEFIT', BOLD(40), 560, goldL, 255, x=1480); txt(C, 'COUNTED AS TAXABLE', BOLD(40), 610, goldL, 255, x=1480); fr = A_(fr, C, (1000, 250, 1800, 740), t, t2)
    return frame(fr)
def s25d(t):
    fr = base_(t, 244, 'SAME RAISE, DIFFERENT RESULT'); T = lambda m: B25.tt(3, m)
    if t > 0.3:
        C = new(); avatar(C, 480, 480, pink, 2.4); avatar(C, 1440, 480, blue, 2.4); txt(C, '=', BOLD(190), 380, goldL, 255, x=960); fr = A_(fr, C, (300, 280, 1640, 640), t, 0.3)
        C = new(); txt(C, 'SAME RAISE', BOLD(56), 700, white, 255, x=480); txt(C, 'SAME SIZE CHECK', BOLD(56), 700, white, 255, x=1440); fr = A_(fr, C, (180, 680, 1760, 780), t, 0.7)
    fr = P(fr, 'TWO DIFFERENT REAL RAISES', 830, t, 1.1, red, (255, 255, 255), 66)
    return frame(fr)

FNS4 = {21: [s21a, s21b, s21c, s21d], 22: [s22a, s22b, s22c], 23: [s23a, s23b, s23c], 24: [s24a, s24b, s24c], 25: [s25a, s25b, s25c, s25d]}
BLK4 = {21: B21, 22: B22, 23: B23, 24: B24, 25: B25}
if __name__ == '__main__':
    mode = sys.argv[1]; b = int(sys.argv[2]); fns = FNS4[b]; FS = BLK4[b].FS
    sel = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, len(fns) + 1))
    OUT = '/tmp/claude-0/-home-user-Tr/f7e0e4f8-271a-59ba-8107-39d9b491975d/scratchpad/out/'
    if mode == 'preview':
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            for fq in [0.35, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((640, 360)).save(f'{OUT}pz{b}_{i}_{int(fq*100)}.png')
        print(b, FS, sum(FS))
    else:
        for i, (fn, f) in enumerate(zip(fns, FS), 1):
            if i not in sel: continue
            render_fast(fn, f, f'{OUT}v6-b{b}-0{i}.mp4'); print('done', b, i, f, flush=True)
