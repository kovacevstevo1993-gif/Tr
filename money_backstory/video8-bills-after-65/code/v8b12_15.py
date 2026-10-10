import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8b11 import *

def first(ph): return min(tm(ph), 0.4)

def cu(t, t0, d=0.6): return ease((t - t0) / d)
def late(ph, back=0.7): return min(tm(ph), LASTP() - back)
def count(C, x0, x1, v, col, y=328, size=130):
    f = fit('$00,000', x1 - x0 - 40, size); txt(C, counter_text(v), f, y, col, 255, x=(x0 + x1) / 2)

# ================= BLOCCO 12 =================
def s12a(t):
    fr = stage_live(t, 'IF YOU RENT, THESE RULES STILL MATTER', 131, 54)
    t1, tA, t2, tB, t3, t4 = first('rent'), tm('tune'), tm('Property'), tm('what'), tm('charges'), tm('community')
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 670, blue, None, None, None); house(C, 385, 400, 1.4, blue); txt(C, 'YOU RENT', BOLD(60), 590, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 690), t, t1)
    fr = chipE(fr, 'DO NOT TUNE OUT', 385, 705, t, tA, col=goldL, size=42)
    if t > t2:
        C = new(); card_(C, 700, 250, 1210, 670, gold, None, None, None); building(C, 955, 410, 280, 210, gold); txt(C, 'PROPERTY TAX', BOLD(52), 575, white, 255, x=955)
        fr = E(fr, C, (680, 230, 1230, 690), t, t2)
    fr = chipE(fr, 'LANDLORD CHARGES', 955, 705, t, tB, col=goldL, size=42)
    if t > t3:
        C = new(); card_(C, 1270, 250, 1790, 670, red, None, None, None); bill(C, 1530, 410, 300, 150, 0, 255); txt(C, 'IN YOUR RENT', BOLD(54), 590, white, 255, x=1530)
        fr = E(fr, C, (1250, 230, 1810, 690), t, t3)
    fr = chipE(fr, 'THE COMMUNITY', 1530, 705, t, t4, col=goldL, size=42)
    return frame(pill_last(fr, t, 'PROPERTY TAX IS PART OF YOUR RENT', PILL_Y, gold, navy, 52))

def s12b(t):
    fr = stage_live(t, 'THE NEXT FOUR BILLS', 132)
    t1, t2 = first('But'), tm('homeowner')
    items = [(2, ('TAX ON', 'SOCIAL SECURITY'), gold), (3, ('YOUR', 'INCOME TAX'), blue), (4, ('A NEW', 'DEDUCTION'), green), (5, ('MEDICARE', 'PART B'), red)]
    for k, (n, lab, col) in enumerate(items):
        tk = t1 + 0.35 * k
        if t > tk:
            C = new(); x0 = 130 + k * 425; card_(C, x0, 250, x0 + 385, 670, col, None, None, None)
            ring_(C, x0 + 192, 400, 95, 1.0 * ease((t - tk) / 0.8), col, 26); txt(C, str(n), BOLD(100), 350, goldL, 255, x=x0 + 192)
            txt(C, lab[0], fit(lab[1], 350, 42), 530, white, 255, x=x0 + 192); txt(C, lab[1], fit(lab[1], 350, 42), 580, white, 255, x=x0 + 192)
            fr = E(fr, C, (x0 - 20, 230, x0 + 405, 690), t, tk)
    fr = chipE(fr, 'HOMEOWNER OR NOT', 960, 700, t, t2, col=goldL, size=42)
    return frame(pill_last(fr, t, 'FOUR MORE BILLS FOR ALMOST EVERY RETIREE', PILL_Y, gold, navy, 48))

# ================= BLOCCO 13 =================
def s13a(t):
    fr = stage_live(t, 'BILL NUMBER TWO: TAX ON SOCIAL SECURITY', 133, 52)
    t1, t2, t3, t4 = first('Bill'), tm('tax'), tm('Social'), tm('never')
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 670, gold, None, None, None); ring_(C, 385, 410, 130, ease((t - t1) / 0.8), gold, 30)
        txt(C, 'BILL', BOLD(44), 340, white, 255, x=385); txt(C, '#2', BOLD(110), 385, goldL, 255, x=385); txt(C, 'TAX ON YOUR', BOLD(40), 560, white, 255, x=385); txt(C, 'SOCIAL SECURITY', BOLD(40), 605, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 690), t, t1)
    if t > t2:
        C = new(); card_(C, 700, 250, 1210, 670, red, None, None, None); tax_form(C, 835, 280, 240, 300, 255, 'TAX'); txt(C, 'THE TAX', BOLD(54), 600, white, 255, x=955)
        fr = E(fr, C, (680, 230, 1230, 690), t, t2)
    if t > t3:
        C = new(); paycheck(C, 1270, 250, 1790, 670, blue, 'SS', 'SOCIAL SECURITY', 'YOUR CHECK', 130)
        fr = E(fr, C, (1250, 230, 1810, 690), t, t3)
    fr = chipE(fr, 'MOST PEOPLE NEVER HEAR THIS', 960, 700, t, t4, col=goldL, size=42)
    return frame(pill_last(fr, t, 'A TAX ON YOUR SOCIAL SECURITY', PILL_Y, gold, navy, 54))

def s13b(t):
    fr = stage_live(t, 'WRITTEN INTO LAW LONG AGO', 134)
    t1, tA, t2, tB, t3 = first('The'), tm('decide'), tm('Social'), tm('taxed'), tm('written')
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 670, gold, None, None, None); coin_stack(C, 385, 520, 6, 62); txt(C, 'THE INCOME LIMITS', BOLD(46), 575, white, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 690), t, t1)
    fr = chipE(fr, 'THE LIMITS DECIDE', 385, 705, t, tA, col=goldL, size=42)
    if t > t2:
        C = new(); paycheck(C, 700, 250, 1210, 670, blue, 'SS', 'SOCIAL SECURITY', 'YOUR CHECK', 130); fr = E(fr, C, (680, 230, 1230, 690), t, t2)
    fr = chipE(fr, 'TAXED OR NOT', 955, 705, t, tB, col=goldL, size=42)
    if t > t3:
        C = new(); cal_card(C, 1270, 270, 1790, 650, 'WRITTEN INTO LAW', '1983', 130, blue); fr = E(fr, C, (1250, 250, 1810, 670), t, t3)
    return frame(pill_last(fr, t, 'WRITTEN INTO LAW IN 1983', PILL_Y, gold, navy, 54))

def s13c(t):
    fr = stage_live(t, 'AND NEVER ADJUSTED FOR INFLATION', 135, 54)
    t1, t2, t3, t4 = first('and'), tm('have never'), tm('adjusted'), tm('inflation')
    if t > t1:
        C = new(); cal_card(C, 130, 270, 640, 650, 'AND THE LAW OF', '1993', 120, green); fr = E(fr, C, (110, 250, 660, 670), t, t1)
    fr = flat_card(fr, t, t2, 700, 1210, gold, 'THE INCOME LIMITS')
    fr = chipE(fr, 'NEVER ADJUSTED', 955, 705, t, t3, col=goldL, size=42)
    fr = chart_card(fr, t, t4, 1270, 1790, red, 'PRICES AND INFLATION', [90, 150, 230])
    return frame(pill_last(fr, t, 'THE LIMITS NEVER MOVED', PILL_Y, gold, navy, 54))

# ================= BLOCCO 14 =================
def s14a(t):
    fr = stage_live(t, 'THE FIRST LINE', 136)
    t1, tA, tB, t2, tC = first('For'), tm('person'), tm('line'), tm('married'), late('thirty')
    tN = late('twenty')
    if t > t1:
        C = new(); card_(C, 130, 250, 900, 670, blue, 'SINGLE PERSON', None, 'THE LINE', 130, goldL); count(C, 130, 900, 25000 * cu(t, tN), goldL); fr = E(fr, C, (110, 230, 920, 690), t, t1)
    fr = chipE(fr, 'FOR ONE PERSON', 515, 705, t, tA, col=goldL, size=42)
    fr = chipE(fr, 'THE FIRST LINE', 1000, 705, t, tB, col=goldL, size=42) if False else fr
    if t > t2:
        C = new(); card_(C, 1020, 250, 1790, 670, green, 'MARRIED COUPLE', None, 'THE LINE', 130, goldL); count(C, 1020, 1790, 32000 * cu(t, tC), goldL); fr = E(fr, C, (1000, 230, 1810, 690), t, t2)
    fr = chipE(fr, 'THE FIRST LINE', 1405, 705, t, tm('couple'), col=goldL, size=42)
    return frame(pill_last(fr, t, '$25,000 SINGLE, $32,000 MARRIED', PILL_Y, gold, navy, 54))

def s14b(t):
    fr = stage_live(t, 'THE SECOND LINE: UP TO 85% TAXED', 137, 54)
    t1, tR, tA, tB, t3, t4 = first('second'), tm('eighty five'), tm('benefit'), tm('taxed'), tm('is'), late('forty', 0.9)
    tS = late('thirty four', 0.9)
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 670, red, None, None, None); ring_(C, 385, 410, 130, 0.85 * cu(t, tR, 0.9), red, 30)
        if t > tR: txt(C, '85%', BOLD(84), 370, goldL, 255, x=385)
        fr = E(fr, C, (110, 230, 660, 690), t, t1)
    if t > tR: EVT.append(tR)
    fr = chipE(fr, 'OF YOUR BENEFIT', 385, 705, t, tA, col=goldL, size=42)
    fr = chipE(fr, 'CAN BE TAXED', 385, 785, t, tB, col=red, size=40) if False else fr
    if t > tm('is') and False: pass
    if t > t3:
        C = new(); card_(C, 720, 250, 1240, 670, blue, 'SINGLE PERSON', None, None, 100, goldL); count(C, 720, 1240, 34000 * cu(t, tS), goldL, 328, 100); fr = E(fr, C, (700, 230, 1260, 690), t, t3)
    if t > t4:
        C = new(); card_(C, 1270, 250, 1790, 670, green, 'MARRIED COUPLE', None, None, 100, goldL); count(C, 1270, 1790, 44000 * cu(t, t4), goldL, 328, 100); fr = E(fr, C, (1250, 230, 1810, 690), t, t4)
    fr = chipE(fr, 'CAN BE TAXED', 960, 705, t, tB, col=red, size=42)
    return frame(pill_last(fr, t, '$34,000 SINGLE, $44,000 MARRIED', PILL_Y, gold, navy, 54))

# ================= BLOCCO 15 =================
def s15a(t):
    fr = stage_live(t, 'THE I R S COUNTS ONLY HALF', 138)
    t1, tX, tA, t2, tH, t3 = first('But'), tm('use'), tm('full'), tm('The I R S'), tm('half'), tm('other')
    if t > t1:
        C = new(); card_(C, 130, 250, 640, 670, grey, None, None, None); paycheck(C, 160, 270, 610, 560, blue, '$$$', 'FULL BENEFIT', 'YOUR CHECK', 90)
        fr = E(fr, C, (110, 230, 660, 690), t, t1)
    if t > tX:
        C = new(); cross(C, 560, 300, 44, red); fr = E(fr, C, (500, 250, 620, 360), t, tX)
    fr = chipE(fr, 'NOT USED IN FULL', 385, 705, t, tA, col=red, size=42)
    if t > t2:
        C = new(); card_(C, 700, 250, 1210, 670, gold, None, None, None); ring_(C, 955, 410, 130, 0.5 * cu(t, tH, 0.8), gold, 30)
        if t > tH: txt(C, '50%', BOLD(80), 370, goldL, 255, x=955)
        txt(C, 'THE I R S COUNTS', BOLD(40), 585, white, 255, x=955)
        fr = E(fr, C, (680, 230, 1230, 690), t, t2)
    if t > tH: EVT.append(tH)
    if t > t3:
        C = new(); card_(C, 1270, 250, 1790, 670, green, None, None, None); wallet(C, 1530, 410, 1.5); txt(C, 'PLUS YOUR', BOLD(46), 545, white, 255, x=1530); txt(C, 'OTHER INCOME', BOLD(46), 600, white, 255, x=1530)
        fr = E(fr, C, (1250, 230, 1810, 690), t, t3)
    fr = chipE(fr, 'ONLY HALF OF YOUR BENEFIT', 955, 705, t, tm('benefit'), col=goldL, size=40)
    return frame(pill_last(fr, t, 'ONLY HALF OF YOUR BENEFIT COUNTS', PILL_Y, gold, navy, 52))

def s15b(t):
    fr = stage_live(t, 'PROVISIONAL INCOME', 139)
    t1, t2, t3 = first('That'), tm('provisional'), tm('decides')
    T = [t1, min(t1 + 0.9, t2 - 0.1), t2]
    fr = eq(fr, t, 260, [('c', 'COUNTED', 'HALF', 'OF YOUR BENEFIT', gold), ('o', '+'), ('c', 'YOUR', 'OTHER', 'INCOME', blue), ('o', '='), ('c', 'THE KEY NUMBER', 'PROVISIONAL', 'INCOME', green)], T, 230, 420, 130)
    EVT.extend(T)
    fr = chipE(fr, 'THE NUMBER THAT DECIDES EVERYTHING', 960, 580, t, t3, col=goldL, size=44)
    return frame(pill_last(fr, t, 'PROVISIONAL INCOME DECIDES IT', PILL_Y, green, navy, 54))

SLIDES = {12: [frozen(s12a), frozen(s12b)], 13: [frozen(s13a), frozen(s13b), frozen(s13c)], 14: [frozen(s14a), frozen(s14b)], 15: [frozen(s15a), frozen(s15b)]}
RAW = {12: [s12a, s12b], 13: [s13a, s13b, s13c], 14: [s14a, s14b], 15: [s15a, s15b]}
SPEC = {12: spec(12, ['But the']), 13: spec(13, ['The income', 'and nineteen']), 14: spec(14, ['The second']), 15: spec(15, ['That total'])}
DUR = {12: 400, 13: 495, 14: 464, 15: 400}
for b in SPEC: assert sum(SPEC[b]) == DUR[b], (b, SPEC[b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec': print(SPEC)
    else: run(SPEC, SLIDES, 'v8', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
