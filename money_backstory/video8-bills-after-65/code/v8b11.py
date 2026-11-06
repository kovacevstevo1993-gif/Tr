import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8b6_10 import *

def flat_card(fr, t, t0, x0, x1, col, title):
    if t > t0:
        C = new(); card_(C, x0, 250, x1, 670, col, title, None, None); bw, gap = 100, 40; sx = (x0 + x1) / 2 - (3 * bw + 2 * gap) / 2
        u = ease((t - t0 - 0.2) / 0.9)
        for i in range(3): vbar(C, sx + i * (bw + gap), 585, bw, 110, col, 'YEAR %d' % (i + 1), u, 28)
        fr = E(fr, C, (x0 - 20, 230, x1 + 20, 690), t, t0)
    return fr

# ================= BLOCCO 11 =================
def s11a(t):
    fr = stage_live(t, 'TEXAS: A CEILING ON SCHOOL TAXES', 121, 56)
    t1, t2, t3, t4 = tm('Texas', 0.3, 0.0), tm('ceiling', 1.4, 0.9), tm('school', 2.2, 1.6), tm('homeowners', 3.0, 2.3)
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 670, gold, None, None, None); building(C, 385, 410, 280, 210, gold); txt(C, 'TEXAS', BOLD(64), 580, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 690), t, t1)
    if t > t2:
        C = new(); card_(C, 700, 250, 1210, 670, blue, None, None, None); padlock(C, 955, 420, 1.7, blue); txt(C, 'TAX CEILING', BOLD(56), 590, white, 255, x=955)
        fr = E(fr, C, (680, 230, 1230, 690), t, t2)
    if t > t3:
        C = new(); card_(C, 1270, 250, 1790, 670, green, None, None, None); building(C, 1530, 410, 280, 210, green); txt(C, 'SCHOOL TAXES', BOLD(54), 590, white, 255, x=1530)
        fr = E(fr, C, (1250, 230, 1810, 690), t, t3)
    fr = chipE(fr, 'HOMEOWNERS 65 AND OLDER', 960, 700, t, t4, col=goldL, size=42)
    return frame(pill_last(fr, t, 'A CEILING ON SCHOOL TAXES', PILL_Y, blue, (255, 255, 255), 54))

def s11b(t):
    fr = stage_live(t, 'YOUR HOUSE CAN DOUBLE IN VALUE', 122, 56)
    t1, t2, t3, t4 = tm('house', 0.3, 0.0), tm('double', 1.3, 0.9), tm('bill', 2.4, 1.8), tm('follow', 3.0, 2.5)
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 670, gold, None, None, None); house(C, 385, 400, 1.5, gold); txt(C, 'YOUR HOUSE', BOLD(60), 590, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 690), t, t1)
    fr = chart_card(fr, t, t2, 700, 1210, gold, 'HOME VALUE', [90, 150, 230])
    fr = chipE(fr, 'IT DOUBLES', 955, 700, t, t2 + 0.4, col=goldL, size=42)
    fr = flat_card(fr, t, t3, 1270, 1790, green, 'SCHOOL TAX PART')
    fr = chipE(fr, 'DOES NOT FOLLOW', 1530, 700, t, t4, col=green, size=42)
    return frame(pill_last(fr, t, 'THE HOUSE DOUBLES, THAT TAX PART DOES NOT', PILL_Y, green, navy, 48))

def s11c(t):
    fr = stage_live(t, 'DIFFERENT IN EVERY STATE', 123, 56)
    t1, t2, t3, t4, t5, t6, t7 = tm('rules', 0.3, 0.0), tm('every', 1.3, 0.8), tm('simple', 2.3, 1.7), tm('Call', 3.4, 2.6), tm('assessor', 4.3, 3.5), tm('three', 5.0, 4.2), tm('by name', 5.6, 4.8)
    if t > t1:
        C = new(); card_(C, 130, 250, 900, 560, blue, None, None, None)
        for k in range(3): building(C, 280 + k * 235, 340, 170, 200, blue)
        txt(C, 'THE RULES DIFFER', BOLD(52), 485, white, 255, x=515)
        fr = E(fr, C, (110, 230, 920, 580), t, t1)
    fr = chipE(fr, 'IN EVERY STATE', 515, 585, t, t2, col=goldL, size=42)
    fr = chipE(fr, 'THE ACTION IS SIMPLE', 515, 690, t, t3, col=green, size=42)
    if t > t4:
        C = new(); card_(C, 960, 250, 1790, 520, gold, None, None, None); phone(C, 1130, 385, 0.9, 255, t - t4, True); txt(C, 'CALL YOUR', BOLD(44), 335, white, 255, x=1535); txt(C, 'COUNTY ASSESSOR', BOLD(44), 390, goldL, 255, x=1535)
        fr = E(fr, C, (940, 230, 1810, 540), t, t4)
    fr = chipE(fr, 'HOMESTEAD', 1080, 575, t, t5, col=gold, size=40)
    fr = chipE(fr, 'SENIOR EXEMPTION', 1540, 575, t, t6, col=blue, size=40)
    fr = chipE(fr, 'FREEZE', 1730, 640, t, t7, col=green, size=40) if False else fr
    fr = chipE(fr, 'THE FREEZE', 1310, 685, t, t7, col=green, size=40)
    return frame(pill_last(fr, t, 'CALL AND ASK ABOUT ALL THREE, BY NAME', PILL_Y, gold, navy, 50))

SLIDES = {11: [frozen(s11a), frozen(s11b), frozen(s11c)]}
RAW = {11: [s11a, s11b, s11c]}
SPEC = {11: spec(11, ['Your house', 'The rules'])}
assert sum(SPEC[11]) == 543, SPEC
if __name__ == '__main__':
    if sys.argv[1] == 'spec': print(SPEC)
    else: run(SPEC, SLIDES, 'v8', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
