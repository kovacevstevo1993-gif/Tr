"""Video lungo 4 (BOLLETTE) - blocchi 31-35 (spesa/SNAP 60+). 1920x1080, 30 fps.
Durate (timeline utente 08/10/2026): B31 308, B32 295, B33 336, B34 315, B35 345.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long4_b31_35.py <blocco>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b16_30 import *

DUR = {31: 308, 32: 295, 33: 336, 34: 315, 35: 345}
PHRASES = {
    31: ["Bill number four.", "Your grocery bill.", "You know the program, snap.", "But almost nobody knows that the rules change the day you turn sixty."],
    32: ["Only about fifty five out of every one hundred eligible people over sixty actually get snap.", "The rest decide they make too much, and never apply."],
    33: ["After sixty, the rules work in your favor.", "You skip the gross income test,", "and only your net income counts.", "That's your income after certain costs come off."],
    34: ["And one of those costs is medical.", "If you pay more than thirty five dollars a month for medical expenses yourself,", "the amount above thirty five can come off your income."],
    35: ["Your housing costs can come off too,", "and for people over sixty, there's no cap on that deduction.", "Rent, mortgage, property bills, utilities.", "It can all count."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def ebt():
    def fn(c):
        w, h = 520, 330
        c.rrect((4, 4, w - 4, h - 4), 30, fill=(70, 120, 176), outline=(36, 76, 128), width=6)
        c.rrect((4, 70, w - 4, 120), 2, fill=(36, 76, 128))
        c.text((46, 40), "FOOD BENEFITS", FONT_SANS, 30, IVORY, anchor="lm", track=3)
        c.rrect((46, 160, 150, 228), 12, fill=(232, 200, 130), outline=(190, 140, 60), width=3)
        c.text((330, 190), "snap", FONT_SANS, 92, IVORY, track=2)
        c.text((46, 290), "EBT CARD", FONT_SANS, 34, IVORY, anchor="lm", track=5)
    return sprite("ebt31", 520, 330, fn)

def star60(label="60"):
    def fn(c):
        S = 300; pts = []
        for i in range(24):
            a = math.pi * 2 * i / 24 - math.pi / 2
            r = 144 if i % 2 == 0 else 124
            pts.append((150 + r * math.cos(a), 150 + r * math.sin(a)))
        c.poly(pts, fill=GOLD)
        c.ell((32, 32, 268, 268), outline=(168, 118, 40), width=6)
        c.text((150, 140), label, FONT_SERIF, 130, GREEN_D)
        c.text((150, 222), "YEARS", FONT_SANS, 32, GREEN_D, track=4)
    return sprite(("star60", label), 300, 300, fn)

# ============================================================ BLOCCO 31
def draw31(img, t):
    ts = starts(31)
    common(img, t, "BILL NUMBER FOUR")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(4, 400), 360, 330, scale=s, alpha=a, shadow=18)
        burst(img, t, ts[0], 360, 330, n=14, color=GOLD, rad=300, seed=31)
    seq(img, t, ts[1], panel(1080, 400, border=GOLD), 1230, 330, shadow=14)
    seq(img, t, ts[1] + 0.2, sprite("bag31", 300, 340, lambda c: ic_bag(c, 150, 170, 2.6)), 880, 330)
    seq(img, t, ts[1] + 0.4, txt("YOUR", 64, SAGE, 5), 1360, 250)
    seq(img, t, ts[1] + 0.55, txt("GROCERY BILL", 84, IVORY, 3), 1360, 360)
    slide_in(img, t, ts[2], ebt(), 520, 760, dy=60, dur=0.55, shadow=16, scale=0.95)
    p = ease(seg(t, ts[3], 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 900, 760, alpha=p)
    s, a, p = pop(t, ts[3] + 0.3, 0.5)
    if p > 0:
        put(img, star60(), 1180, 760, scale=0.95 * s, alpha=a, shadow=14)
        burst(img, t, ts[3] + 0.3, 1180, 760, n=12, color=GOLD, rad=220, seed=32)
    seq(img, t, ts[3] + 1.0, stamp("RULES CHANGE", 460, 100, GOLD, size=44), 1560, 700, rot=-4, shadow=10)
    seq(img, t, ts[3] + 1.3, txt("THE DAY YOU TURN 60", 34, IVORY, 3), 1560, 800)

# ============================================================ BLOCCO 32
def tiny(kind):
    def fn(c):
        col = {"on": GOLD, "off": SAGE_D}[kind]
        c.ell((15, 4, 49, 38), fill=(236, 194, 154) if kind == "on" else (90, 120, 106))
        c.d.pieslice(c._b((6, 38, 58, 86)), 180, 360, fill=col)
        c.rrect((6, 62, 58, 70), 3, fill=col)
    return sprite(("tiny32", kind), 64, 80, fn)

def draw32(img, t):
    ts = starts(32)
    common(img, t, "ELIGIBLE SENIORS OVER 60")
    seq(img, t, ts[0] - 0.05, txt("100 ELIGIBLE PEOPLE", 46, IVORY, 3), 480, 190)
    for i in range(100):
        r, q = i // 10, i % 10
        x, y = 190 + q * 66, 280 + r * 66
        if i < 55:
            st = ts[0] + 0.3 + i * 0.04
            s, a, p = pop(t, st, 0.3)
            if p > 0:
                put(img, tiny("on"), x, y, scale=0.9 * s, alpha=a)
        else:
            st = ts[1] + (i - 55) * 0.03
            s, a, p = pop(t, st, 0.3)
            if p > 0:
                put(img, tiny("off"), x, y, scale=0.9 * s, alpha=a * 0.9)
            elif t > ts[0] + 0.3:
                pass
    # numero 55
    slide_in(img, t, ts[0] + 0.4, panel(760, 420, border=GOLD), 1400, 440, dx=60, dur=0.55, shadow=14)
    counter(img, t, ts[0] + 0.6, 1.6, "", 55, "", 210, GOLD, 1400, 400, fmt="{}")
    seq(img, t, ts[0] + 1.6, txt("GET SNAP", 64, IVORY, 6), 1400, 540)
    seq(img, t, ts[0] + 1.9, txt("OUT OF EVERY 100", 34, SAGE, 4), 1400, 600)
    slide_in(img, t, ts[1], panel(760, 330, border=RED), 1400, 800, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, txt("45", 100, RED, 4), 1160, 790)
    seq(img, t, ts[1] + 0.5, txt("THINK THEY MAKE", 34, IVORY, 3), 1500, 760)
    seq(img, t, ts[1] + 0.65, txt("TOO MUCH, AND", 34, IVORY, 3), 1500, 810)
    seq(img, t, ts[1] + 0.8, txt("NEVER APPLY", 40, RED, 3), 1500, 865)

# ============================================================ BLOCCO 33
def draw33(img, t):
    ts = starts(33)
    common(img, t, "AFTER SIXTY")
    seq(img, t, ts[0], stamp("THE RULES WORK FOR YOU", 900, 120, GOLD, size=50), 960, 200, shadow=12, rot=-1)
    slide_in(img, t, ts[1], panel(760, 340, border=RED), 520, 470, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.25, sprite("coins33", 300, 200, lambda c: [ic_coin(c, 70 + k * 80, 100 + (k % 2) * 8, 48) for k in range(3)]), 520, 430, shadow=6)
    seq(img, t, ts[1] + 0.5, txt("GROSS INCOME TEST", 44, IVORY, 3), 520, 560)
    s, a, p = pop(t, ts[1] + 0.9, 0.45)
    if p > 0:
        put(img, sprite("x33", 300, 300, lambda c: ic_x(c, 150, 150, 3.0, RED, 16)), 520, 450, scale=s, alpha=a)
        put(img, stamp("SKIPPED", 280, 90, RED, size=42), 520, 650, scale=s, alpha=a, rot=-4, shadow=8)
    slide_in(img, t, ts[2], panel(760, 340, border=GOLD), 1400, 470, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[2] + 0.25, sprite("net33", 300, 200, lambda c: (c.rrect((40, 30, 260, 170), 16, fill=GOLD), c.text((150, 100), "NET", FONT_SANS, 90, GREEN_D, track=4))), 1400, 420, shadow=6)
    seq(img, t, ts[2] + 0.5, txt("NET INCOME", 44, IVORY, 3), 1400, 560)
    check_at(img, t, ts[2] + 0.9, 1640, 340, 1.2)
    seq(img, t, ts[2] + 1.0, stamp("ONLY THIS COUNTS", 440, 90, GOLD, size=36), 1400, 650, rot=-2, shadow=8)
    # formula
    items = [("GROSS", 430, SAGE_D), ("-", 650, None), ("COSTS", 870, CORAL), ("=", 1090, None), ("NET", 1310, GOLD)]
    for k, (name, x, col) in enumerate(items):
        s, a, p = pop(t, ts[3] + 0.1 + k * 0.45, 0.4)
        if p > 0:
            if col:
                put(img, pill_spr(name, 46, 320, 110, PANEL_FILL, col, border=col, track=3), x, 860, scale=s, alpha=a, shadow=8)
            else:
                put(img, txt(name, 90, IVORY, 0), x, 860, scale=s, alpha=a)
    ban(img, t, ts[3] + 2.4, "INCOME AFTER CERTAIN COSTS COME OFF", cy=985, w=1280)

# ============================================================ BLOCCO 34
def draw34(img, t):
    ts = starts(34)
    common(img, t, "MEDICAL COSTS")
    slide_in(img, t, ts[0], panel(620, 540, border=CORAL), 440, 540, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.3, sprite("mc34", 260, 260, lambda c: (c.ell((6, 6, 254, 254), fill=PANEL_FILL, outline=CORAL, width=8), c.rrect((106, 50, 154, 210), 10, fill=CORAL), c.rrect((50, 106, 210, 154), 10, fill=CORAL))), 440, 440, shadow=8)
    seq(img, t, ts[0] + 0.7, txt("MEDICAL COSTS", 48, IVORY, 3), 440, 620)
    seq(img, t, ts[0] + 0.9, txt("YOU PAY YOURSELF", 34, SAGE, 3), 440, 680)
    seq(img, t, ts[1] - 0.2, txt("EACH MONTH", 40, GOLD, 4), 1230, 250)
    pa = ease(seg(t, ts[1], 0.7))
    if pa > 0:
        w1 = int(280 * pa)
        put(img, sprite(("g34", w1), max(8, w1), 130, lambda c: c.rrect((2, 2, max(8, w1) - 2, 128), 14, fill=SAGE_D)), 830 + w1 / 2, 400)
    pb = ease(seg(t, ts[1] + 0.9, 0.8))
    if pb > 0:
        w2 = int(520 * pb)
        put(img, sprite(("y34", w2), max(8, w2), 130, lambda c: c.rrect((2, 2, max(8, w2) - 2, 128), 14, fill=GOLD)), 1110 + w2 / 2, 400)
    seq(img, t, ts[1] + 0.7, txt("FIRST $35", 40, IVORY, 3), 920, 500)
    seq(img, t, ts[1] + 1.8, txt("EVERYTHING ABOVE $35", 40, GOLD, 3), 1440, 500)
    p = ease(seg(t, ts[2], 0.5))
    if p > 0:
        put(img, sprite("dn34", 140, 180, lambda c: (c.rrect((50, 6, 90, 100), 8, fill=GOLD), c.poly([(10, 94), (130, 94), (70, 168)], fill=GOLD))), 1370, 620, alpha=p)
    ban(img, t, ts[2] + 0.3, "COMES OFF YOUR INCOME", cy=830, cx=1230, w=900, size=54)

# ============================================================ BLOCCO 35
def draw35(img, t):
    ts = starts(35)
    common(img, t, "HOUSING COSTS")
    slide_in(img, t, ts[0], panel(760, 400, border=SAGE), 500, 380, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.3, sprite("hs35", 260, 240, lambda c: ic_house(c, 130, 130, 2.6)), 500, 330, shadow=8)
    seq(img, t, ts[0] + 0.7, txt("HOUSING COSTS", 48, IVORY, 3), 500, 480)
    seq(img, t, ts[0] + 0.9, txt("COME OFF TOO", 42, GOLD, 3), 500, 540)
    slide_in(img, t, ts[1], panel(760, 400, border=GOLD), 1400, 380, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, sprite("cap35", 360, 240, lambda c: (c.rrect((20, 40, 340, 80), 8, fill=RED), c.line([(100, 80), (100, 190)], SAGE_D, 8), c.line([(180, 80), (180, 190)], SAGE_D, 8), c.line([(260, 80), (260, 190)], SAGE_D, 8), ic_x(c, 180, 130, 2.0, RED, 12))), 1400, 330, shadow=8)
    seq(img, t, ts[1] + 0.8, stamp("NO CAP", 280, 90, GOLD, size=46), 1400, 470, rot=-3, shadow=8)
    seq(img, t, ts[1] + 1.1, txt("FOR PEOPLE OVER 60", 36, SAGE, 3), 1400, 545)
    names = ["RENT", "MORTGAGE", "PROPERTY BILLS", "UTILITIES"]
    xs = [240, 640, 1150, 1640]
    ws = [300, 420, 520, 380]
    for k, name in enumerate(names):
        s, a, p = pop(t, ts[2] + 0.1 + k * 0.5, 0.4)
        if p > 0:
            put(img, pill_spr(name, 40, ws[k], 120, PANEL_FILL, IVORY, border=SAGE, track=2), xs[k], 780, scale=s, alpha=a, shadow=8)
        check_at(img, t, ts[3] - 0.3 + k * 0.2, xs[k] + ws[k] / 2 - 10, 700, 0.8)
    ban(img, t, ts[3] - 0.1, "IT CAN ALL COUNT", cy=975, w=700, size=54)

DRAW = {31: draw31, 32: draw32, 33: draw33, 34: draw34, 35: draw35}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/bollette-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
