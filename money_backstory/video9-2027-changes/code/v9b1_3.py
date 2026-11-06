"""Video 9 - blocchi 1-3 (primi 44 s). Modello unico (stile video 8), layout diversi slide per slide.
Uso: python3 v9b1_3.py render|preview|check <blocco>  (OUT=cartella)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); VID = os.path.dirname(HERE); MB = os.path.dirname(VID)
sys.path.insert(0, os.path.join(MB, 'video8-bills-after-65/code'))
import v8b1
from v8b1 import *
from v8b2_5 import initials
from sync_voce import Voice
VID = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = Voice(os.path.join(VID, 'sync.json')); v8b1.V = V
SRC = 'SOURCE: SSA 2027 COLA FACT SHEET (ssa.gov)'

# ======================= BLOCCO 1 =======================
def s1a(t):
    fr = stage_live(t, 'YOUR CHECK IS ABOUT TO CHANGE', 101, 58)
    tc, to = 0.35, tm('official', LASTP() - 1.0)
    if t > tc:
        C = new(); paycheck(C, 150, 260, 900, 660, gold, '$ ? ? ?', 'STARTING JANUARY 2027', 'SOCIAL SECURITY', 130)
        fr = P2(fr, C, (130, 240, 920, 680), t, tc)
    if t > tc + 0.6:
        L = new(); arrow_r(L, 930, 1060, 460, goldL, 255 * E_(t, tc + 0.6, 0.4)); fr = Image.alpha_composite(fr, L)
    if t > to - 0.9:
        C = new(); cal_card(C, 1110, 250, 1770, 700, 'ANNOUNCED', 'OCT 14', 130, red)
        txt(C, '2026', BOLD(60), 505, navy, 255, x=1440)
        fr = P2(fr, C, (1090, 230, 1790, 720), t, to - 0.9)
    if t > to:
        fr = stamp(fr, 'OFFICIAL', 1440, 628, 6, green, min(1.0, ease((t - to) / 0.35)), 64)
    return frame(pill_last(fr, t, 'MADE OFFICIAL ON OCTOBER 14', PILL_Y, gold, navy, 54))

def s1b(t):
    fr = stage_live(t, 'THE 2027 RAISE', 102, 60)
    tr, tf = min(0.35, tm('three', 1.5)), tm('five', LASTP() - 1.6)
    if t > tr:
        C = new(); ring_(C, 480, 440, 185, 0.036 * 10 * ease((t - tr) / 0.9), green, 38)
        txt(C, '+3.6%', BOLD(92), 380, goldL, 255, x=480); txt(C, 'COLA', BOLD(52), 500, white, 255, x=480)
        fr = P2(fr, C, (270, 230, 690, 650), t, tr)
    ty = tm('twenty', tf - 0.8)
    if t > ty:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([330, 650, 630, 720], radius=34, fill=green + (255,)); txt(C, 'FOR 2027', BOLD(44), 660, white, 255, x=480)
        fr = P2(fr, C, (310, 630, 650, 740), t, ty)
    labels = ['3.6%', '?', '?', '?', '?']
    for k in range(5):
        tk = tf + 0.22 * k
        if t > tk:
            C = new(); x = 860 + k * 190; d = ImageDraw.Draw(C); on = k == 0
            d.rounded_rectangle([x, 300, x + 160, 560], radius=26, fill=(gold if on else card) + (255,), outline=(white if on else (120, 140, 170)) + (255,), width=5)
            txt(C, f'#{k + 1}', BOLD(40), 320, navy if on else (150, 165, 190), 255, x=x + 80)
            txt(C, labels[k], fit(labels[k], 140, 64 if on else 110), 400, navy if on else goldL, 255, x=x + 80)
            fr = P2(fr, C, (x - 20, 280, x + 180, 580), t, tk)
    if t > tf + 1.1:
        C = new(); txt(C, 'HIT YOUR MONEY IN JANUARY', BOLD(46), 600, white, 255, x=1335); fr = P2(fr, C, (840, 580, 1830, 670), t, tf + 1.1)
    return frame(pill_last(fr, t, 'THE RAISE IS ONLY 1 OF 5 NEW NUMBERS', PILL_Y, gold, navy, 52))

# ======================= BLOCCO 2 =======================
def person(C, x0, x1, letter, name, age, line1, line2, col):
    d = ImageDraw.Draw(C); cx = (x0 + x1) / 2
    d.rounded_rectangle([x0, 250, x1, 700], radius=34, fill=card + (255,), outline=col + (255,), width=6)
    initials(C, cx, 350, letter, 70, col); txt(C, name, BOLD(64), 440, white, 255, x=cx)
    txt(C, f'AGE {age}', BOLD(84), 515, goldL, 255, x=cx)
    d.rounded_rectangle([x0 + 40, 615, x1 - 40, 680], radius=30, fill=col + (255,))
    txt(C, line1, fit(line1, x1 - x0 - 110, 38), 627, navy if col == gold else white, 255, x=cx)

def s2a(t):
    fr = stage_live(t, 'MEET FRANK AND MARY', 103, 60)
    tm_, tf = tm('meet', 0.4) + 0.5, tm('sixty-three', LASTP() - 0.6)
    if t > tm_ - 0.5:
        C = new(); person(C, 220, 860, 'M', 'MARY', 67, 'FULLY RETIRED', '', gold); fr = P2(fr, C, (200, 230, 880, 720), t, tm_ - 0.5)
    if t > tf - 0.5:
        C = new(); person(C, 1060, 1700, 'F', 'FRANK', 63, 'STILL WORKS PART TIME', '', blue); fr = P2(fr, C, (1040, 230, 1720, 720), t, tf - 0.5)
    return frame(pill_last(fr, t, 'ONE RETIRED, ONE STILL WORKING', PILL_Y, gold, navy, 54))

def s2b(t):
    fr = stage_live(t, 'ONE NUMBER, OR FIVE?', 104, 60)
    t1, t2 = 0.35, tm('found', LASTP() - 0.8)
    tq = tm('only', t2 - 0.6)
    if t > t1:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([140, 260, 900, 700], radius=34, fill=card + (255,), outline=blue + (255,), width=6)
        initials(C, 260, 360, 'F', 62, blue); txt(C, 'FRANK SEES', BOLD(54), 335, white, 255, x=600, anchor='l') if False else txt(C, 'FRANK SEES', BOLD(54), 332, white, 255, x=600)
        d.rounded_rectangle([300, 430, 740, 590], radius=28, fill=gold + (255,)); txt(C, '+3.6%', BOLD(104), 445, navy, 255, x=520)
        fr = P2(fr, C, (120, 240, 920, 720), t, t1)
    if t > tq:
        C = new(); txt(C, 'THE ONLY NUMBER?', BOLD(44), 618, goldL, 255, x=520); fr = P2(fr, C, (140, 600, 900, 690), t, tq)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1020, 260, 1780, 700], radius=34, fill=card + (255,), outline=gold + (255,), width=6)
        initials(C, 1140, 360, 'M', 62, gold); txt(C, 'MARY FINDS', BOLD(54), 332, white, 255, x=1480)
        for k in range(4):
            x = 1080 + k * 170; d.rounded_rectangle([x, 450, x + 140, 640], radius=24, fill=green + (255,)); txt(C, '+1', BOLD(70), 500, white, 255, x=x + 70)
        fr = P2(fr, C, (1000, 240, 1800, 720), t, t2)
    return frame(pill_last(fr, t, 'MARY FOUND THE OTHER FOUR', PILL_Y, gold, navy, 54))

def s2c(t):
    fr = stage_live(t, 'THE ONE THAT CAN COST YOU', 105, 58)
    t3 = 0.35
    t1, t2 = tm('claims', LASTP() - 1.3), tm('working', LASTP() - 0.7)
    t1 = min(t1, t2 - 0.6)
    for x0, lab, tk, ic in [(140, 'CLAIMS EARLY', t1, 'c'), (640, 'KEEPS WORKING', t2, 'b')]:
        if t > tk:
            C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([x0, 270, x0 + 440, 650], radius=30, fill=card + (255,), outline=blue + (255,), width=6)
            if ic == 'c': cal_card(C, x0 + 110, 310, x0 + 330, 500, 'AGE', '62+', 80, blue)
            else: briefcase(C, x0 + 220, 410, 1.3)
            txt(C, lab, fit(lab, 400, 46), 560, white, 255, x=x0 + 220)
            fr = P2(fr, C, (x0 - 20, 250, x0 + 460, 670), t, tk)
    if t > t2 + 0.25:
        L = new(); txt(L, '+', BOLD(90), 395, goldL, 255, x=610); fr = Image.alpha_composite(fr, L)
    if t > t3:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1180, 270, 1790, 650], radius=30, fill=(70, 22, 30, 255), outline=red + (255,), width=7)
        padlock(C, 1485, 380, 0.9, red); txt(C, '$ THOUSANDS', BOLD(70), 470, white, 255, x=1485); txt(C, 'HELD BACK', BOLD(56), 560, red, 255, x=1485)
        fr = P2(fr, C, (1160, 250, 1810, 670), t, t3)
    if t > t2 + 0.25:
        L = new(); arrow_r(L, 1100, 1170, 460, red, 255 * E_(t, t2 + 0.25, 0.3)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'IT CAN QUIETLY HOLD BACK THOUSANDS', PILL_Y, red, (255, 255, 255), 52))

# ======================= BLOCCO 3 =======================
def s3a(t):
    fr = stage_live(t, 'STRAIGHT FROM THE SOURCE', 106, 60)
    t1, t2 = tm('official', 2.5), tm('raise', LASTP() - 0.7)
    ta = tm('start', t2 - 0.5)
    if t > 0.35:
        C = new(); d = ImageDraw.Draw(C)
        d.rounded_rectangle([230, 230, 830, 700], radius=18, fill=(236, 240, 245, 255), outline=gold + (255,), width=5)
        d.rounded_rectangle([230, 230, 830, 330], radius=18, fill=navy + (255,)); d.rectangle([230, 300, 830, 330], fill=navy + (255,))
        txt(C, 'SOCIAL SECURITY', BOLD(40), 252, goldL, 255, x=530)
        txt(C, '2027 COLA', BOLD(64), 360, navy, 255, x=530); txt(C, 'FACT SHEET', BOLD(52), 440, navy, 255, x=530)
        for k in range(4): d.rectangle([300, 530 + k * 38, 760 - (k % 2) * 120, 546 + k * 38], fill=(170, 180, 200, 255))
        fr = P2(fr, C, (210, 210, 850, 720), t, 0.35)
    if t > t1:
        C = new(); check(C, 790, 260, 52, green); fr = P2(fr, C, (720, 190, 860, 330), t, t1)
    if t > t2:
        C = new(); d = ImageDraw.Draw(C); d.rounded_rectangle([1060, 300, 1720, 620], radius=34, fill=gold + (255,))
        txt(C, 'STEP 1', BOLD(60), 340, navy, 255, x=1390); txt(C, 'THE RAISE', BOLD(96), 430, navy, 255, x=1390)
        fr = P2(fr, C, (1040, 280, 1740, 640), t, t2)
    if t > ta:
        L = new(); arrow_r(L, 880, 1040, 460, goldL, 255 * E_(t, ta, 0.4)); fr = Image.alpha_composite(fr, L)
    return frame(pill_last(fr, t, 'WHAT IT REALLY ADDS TO A TYPICAL CHECK', PILL_Y, gold, navy, 50))

from v4b2_10 import cal_card
from v5lib import paycheck
SLIDES = {1: [frozen(s1a), frozen(s1b)], 2: [frozen(s2a), frozen(s2b), frozen(s2c)], 3: [frozen(s3a)]}
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
if __name__ == '__main__':
    if sys.argv[1] == 'spec': print(SPEC, {b: sum(v) for b, v in SPEC.items()})
    else: run(SPEC, SLIDES, 'v9', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
