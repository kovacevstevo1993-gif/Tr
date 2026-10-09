import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); VID = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(os.path.dirname(VID), 'modello-unico'))
from modello_unico import *
from v3lib import phone, bill, cross, stamp, coin_stack
SYNC = os.path.join(VID, 'sync.json')
V = Voice(SYNC)
def tm(phrase, mx=None, mn=0.15):
    """istante della parola dal calcolo; mai oltre l'ultimo elemento (mx)"""
    return max(mn, min(V.at(CUE['blk'], phrase) - CUE['t0'], LASTP() - 0.3 if mx is None else mx))

# ---- SLIDE 1: "Born before 1962 ... stop, lower, or freeze a stack of bills" ----
def s1(t):
    fr = stage(t, 'BORN BEFORE 1962?', 81)
    tc, tr = tm('born before', 3.0), tm('turned', 4.6)
    tb = tm('right', LASTP() - 1.6)
    tags = [tm('stop', LASTP() - 0.95), tm('lower', LASTP() - 0.65), tm('freeze', LASTP() - 0.35)]
    if t > tc:
        C = new(); cal_card(C, 130, 260, 640, 560, 'BORN BEFORE', 'JAN 2, 1962', 60, red)
        txt(C, 'ALL BORN BEFORE THIS DATE', BOLD(34), 590, grey, 255, x=385)
        fr = P2(fr, C, (110, 240, 660, 650), t, tc)
    if t > tc + 0.5:
        L = new(); arrow_r(L, 680, 820, 410, goldL, 255 * E_(t, tc + 0.5, 0.4)); fr = Image.alpha_composite(fr, L)
    if t > tr:
        C = new(); ring_(C, 960, 410, 135, 1.0 * ease((t - tr) / 0.8), gold, 36)
        txt(C, 'AGE', BOLD(46), 340, white, 255, x=960); txt(C, '65', BOLD(112), 380, goldL, 255, x=960)
        fr = P2(fr, C, (790, 250, 1130, 590), t, tr)
    if t > tb:
        C = new()
        for ang, dx, dy in [(-9, -26, 8), (6, 24, -2), (-2, 0, -18)]: bill(C, 960 + dx, 625 + dy, 250, 122, ang, 255)
        txt(C, 'YOUR BILLS', BOLD(44), 722, white, 255, x=960)
        fr = P2(fr, C, (790, 520, 1130, 780), t, tb)
    names = [('STOP', red), ('LOWER', gold), ('FREEZE', blue)]
    for k, ((nm, col), tk) in enumerate(zip(names, tags)):
        if t > tk:
            C = new(); y = 250 + k * 170; card_(C, 1250, y, 1790, y + 140, col, None, nm, None, 76, white)
            fr = P2(fr, C, (1230, y - 20, 1810, y + 160), t, tk)
    return frame(pill_last(fr, t, 'THE LAW GAVE YOU THE RIGHT', PILL_Y, gold, navy, 54))

# ---- SLIDE 2: "still paying every single one ... nobody will call you to say stop" ----
BILLS = ['PROPERTY TAX', 'TAX ON SOCIAL SECURITY', 'INCOME TAX', 'MEDICARE PART B']
def s2(t):
    fr = stage(t, 'YOU MAY STILL BE PAYING THEM', 82, 58)
    t0 = tm('paying', 3.0); rows = [t0 + 0.55 * k for k in range(4)]
    for k, (nm, tk) in enumerate(zip(BILLS, rows)):
        if t > tk:
            C = new(); y = 240 + k * 135; d = ImageDraw.Draw(C)
            d.rounded_rectangle([110, y, 1080, y + 112], radius=26, fill=card + (255,), outline=gold + (255,), width=5)
            bill(C, 205, y + 56, 150, 74, 0, 255); txt(C, nm, fit(nm, 590, 46), y + 28, white, 255, x=300, anchor='l')
            d.rounded_rectangle([905, y + 28, 1060, y + 84], radius=28, fill=red + (255,)); txt(C, 'PAYING', BOLD(34), y + 41, white, 255, x=982)
            fr = P2(fr, C, (90, y - 20, 1100, y + 132), t, tk)
    tn = tm('nobody', LASTP() - 1.2)
    if t > tn:
        C = new(); phone(C, 1500, 430, 1.55, 255, t - tn, True); cross(C, 1620, 300, 62, red)
        txt(C, 'NO ONE CALLS', BOLD(56), 650, white, 255, x=1500)
        fr = P2(fr, C, (1270, 200, 1740, 730), t, tn)
    return frame(pill_last(fr, t, 'NOBODY WILL TELL YOU TO STOP', PILL_Y, red, (255, 255, 255), 54))

from v4b2_10 import cal_card
def frozen(fn):
    """tutto fermo dall'80% (regola dell'utente 10/10): dopo l'80% il tempo si ferma, nessun elemento si muove"""
    return lambda t: fn(min(t, 0.8 * D()))
SLIDES = {1: [frozen(s1), frozen(s2)]}
if __name__ == '__main__':
    SPEC = {1: V.plan(1, 2)}
    if sys.argv[1] == 'spec': print(SPEC, sum(SPEC[1]))
    else: run(SPEC, SLIDES, 'v8', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
