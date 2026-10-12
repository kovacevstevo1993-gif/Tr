"""Video lungo 4 (BOLLETTE) - blocchi 51-55 (fine bus, inizio riparazioni USDA 504). 1920x1080, 30 fps.
Durate (timeline utente 08/10/2026): B51 343, B52 282, B53 230, B54 368, B55 352.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long4_b51_55.py <blocco>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b36_50 import *

DUR = {51: 343, 52: 282, 53: 230, 54: 368, 55: 352}
PHRASES = {
    51: ["So call your local transit agency, or check their website,", "and ask for the senior reduced fare card.", "Ten minutes, and every ride after that costs less."],
    52: ["Who does this help most?", "Anyone who gave up driving, or wants to.", "If you ride the bus a few times a week, half fare adds up fast."],
    53: ["And now, bill number seven.", "The one I told you to wait for.", "Because it's the biggest dollar amount on this whole list."],
    54: ["It's a repair bill.", "The furnace that quits in January.", "The roof that leaks.", "The wiring that isn't safe anymore.", "For a lot of seniors, one of those bills can wipe out their savings."],
    55: ["The U S Department of Agriculture has a program called Section five oh four Home Repair.", "And for homeowners sixty two or older, it offers grants.", "Not loans.", "Grants."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def ic_wire(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 60 * s, cx + 50 * s, cy + 60 * s), 12 * s, fill=IVORY, outline=(206, 200, 186), width=4)
    c.ell((cx - 22 * s, cy - 36 * s, cx - 2 * s, cy - 16 * s), fill=(60, 60, 60)); c.ell((cx + 6 * s, cy - 36 * s, cx + 26 * s, cy - 16 * s), fill=(60, 60, 60))
    c.line([(cx - 40 * s, cy + 50 * s), (cx - 14 * s, cy + 10 * s), (cx + 6 * s, cy + 36 * s), (cx + 40 * s, cy - 2 * s)], RED, 7 * s)
    c.poly([(cx + 24 * s, cy + 6 * s), (cx + 44 * s, cy + 6 * s), (cx + 34 * s, cy + 26 * s)], fill=GOLD)

def ic_leak_roof(c, cx, cy, s):
    c.poly([(cx - 70 * s, cy + 10 * s), (cx, cy - 56 * s), (cx + 70 * s, cy + 10 * s)], fill=CORAL)
    c.rrect((cx - 50 * s, cy + 6 * s, cx + 50 * s, cy + 56 * s), 3, fill=IVORY)
    for k, dx in enumerate((-20, 6, 28)):
        c.poly([(cx + dx * s, cy + 14 * s), (cx + (dx + 7) * s, cy + 30 * s), (cx + (dx - 7) * s, cy + 30 * s)], fill=(110, 170, 230))
        c.ell((cx + (dx - 7) * s, cy + 26 * s, cx + (dx + 7) * s, cy + 38 * s), fill=(110, 170, 230))

def ic_furnace(c, cx, cy, s, cold=True):
    c.rrect((cx - 50 * s, cy - 62 * s, cx + 50 * s, cy + 62 * s), 12 * s, fill=(170, 176, 178), outline=(110, 118, 120), width=4)
    c.rrect((cx - 36 * s, cy - 46 * s, cx + 36 * s, cy - 6 * s), 6 * s, fill=(70, 78, 80))
    for k in range(3):
        c.line([(cx - 30 * s, cy + 12 * s + k * 14 * s), (cx + 30 * s, cy + 12 * s + k * 14 * s)], (110, 118, 120), 5 * s)
    c.ell((cx + 22 * s, cy - 56 * s, cx + 40 * s, cy - 38 * s), fill=ICE if cold else FLAME)

# ============================================================ BLOCCO 51
def draw51(img, t):
    ts = starts(51)
    common(img, t, "THE FIX")
    slide_in(img, t, ts[0], panel(660, 520, border=SAGE), 400, 540, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.3, sprite("bus51", 300, 220, lambda c: ic_bus(c, 150, 110, 1.9)), 400, 440, shadow=8)
    seq(img, t, ts[0] + 0.6, txt("YOUR LOCAL", 40, IVORY, 3), 400, 600)
    seq(img, t, ts[0] + 0.8, txt("TRANSIT AGENCY", 52, GOLD, 3), 400, 660)
    seq(img, t, ts[0] + 1.3, sprite("ph51", 160, 200, lambda c: ic_phone(c, 80, 100, 1.4)), 210, 770, scale=0.75)
    seq(img, t, ts[0] + 1.5, sprite("web51", 160, 160, lambda c: (c.ell((10, 10, 150, 150), outline=SAGE, width=8), c.line([(10, 80), (150, 80)], SAGE, 6), c.arc((40, 10, 120, 150), 0, 360, SAGE, 6))), 590, 780, scale=0.7)
    p = ease(seg(t, ts[1] - 0.2, 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 860, 540, alpha=p)
    slide_in(img, t, ts[1], sprite("card51", 500, 320, lambda c: ic_card_id(c, 250, 160, 2.3, "SENIOR FARE")), 1320, 540, dy=50, dur=0.55, shadow=16)
    seq(img, t, ts[1] + 0.6, txt("ASK FOR THE", 40, SAGE, 3), 1320, 770)
    seq(img, t, ts[1] + 0.8, txt("REDUCED FARE CARD", 48, GOLD, 3), 1320, 830)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("cl51", 200, 200, lambda c: ic_clock(c, 100, 100, 88, 1.0)), 1760, 330, scale=s, alpha=a, shadow=8)
    seq(img, t, ts[2] + 0.2, txt("TEN MINUTES", 40, GOLD, 3), 1760, 450)
    ban(img, t, ts[2] + 0.5, "EVERY RIDE AFTER THAT COSTS LESS", cy=985, w=1180, size=50)

# ============================================================ BLOCCO 52
def draw52(img, t):
    ts = starts(52)
    common(img, t, "WHO IT HELPS MOST")
    seq(img, t, ts[0], stamp("WHO IT HELPS MOST", 760, 120, GOLD, size=52), 960, 200, shadow=12)
    seq(img, t, ts[1], sprite("car52", 360, 280, lambda c: (c.rrect((20, 100, 340, 210), 40, fill=(190, 80, 70)), c.rrect((90, 50, 270, 120), 30, fill=(190, 222, 232)), c.ell((60, 180, 130, 250), fill=GREEN_D, outline=IVORY, width=5), c.ell((230, 180, 300, 250), fill=GREEN_D, outline=IVORY, width=5))), 420, 520, shadow=12)
    seq(img, t, ts[1] + 0.6, sprite("x52", 300, 300, lambda c: ic_x(c, 150, 150, 3.0, RED, 14)), 420, 520, scale=0.9)
    seq(img, t, ts[1] + 1.0, txt("GAVE UP DRIVING", 40, IVORY, 3), 420, 700)
    seq(img, t, ts[1] + 1.2, txt("OR WANTS TO", 34, SAGE, 3), 420, 750)
    slide_in(img, t, ts[2], panel(900, 520, border=GOLD), 1330, 520, dx=60, dur=0.55, shadow=14)
    for k in range(5):
        s, a, p = pop(t, ts[2] + 0.4 + k * 0.3, 0.35)
        if p > 0:
            put(img, sprite(("dd52", k), 110, 110, lambda c, k=k: (c.ell((4, 4, 106, 106), fill=GOLD, outline=(168, 118, 40), width=5), c.text((55, 58), "MTWTF"[k], FONT_SANS, 52, GREEN_D))), 1020 + k * 130, 400, scale=s, alpha=a, shadow=6)
    seq(img, t, ts[2] + 1.2, txt("A FEW TIMES A WEEK", 42, IVORY, 3), 1330, 520)
    seq(img, t, ts[2] + 1.8, sprite("bus52", 280, 200, lambda c: ic_bus(c, 140, 100, 1.7)), 1330, 620, shadow=6)
    seq(img, t, ts[2] + 2.3, stamp("HALF FARE ADDS UP", 640, 100, GOLD, size=44), 1330, 830, rot=-2, shadow=10)
    if t >= ts[2] + 2.3:
        for k in range(4):
            u = seg(t, ts[2] + 2.5 + k * 0.2, 0.5)
            if 0 < u:
                put(img, ic_coin_sp(34), 1060 + k * 150, 960 - 30 * ease(u), alpha=min(1, u * 3))

def ic_coin_sp(r):
    def fn(c):
        ic_coin(c, r + 2, r + 2, r)
    return sprite(("coin52", r), r * 2 + 4, r * 2 + 4, fn)

# ============================================================ BLOCCO 53
def draw53(img, t):
    ts = starts(53)
    common(img, t, "BILL NUMBER SEVEN")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(7, 400), 360, 330, scale=s, alpha=a, shadow=18)
        burst(img, t, ts[0], 360, 330, n=14, color=GOLD, rad=300, seed=53)
    seq(img, t, ts[0] + 0.4, panel(1080, 400, border=CORAL), 1230, 330, shadow=14)
    seq(img, t, ts[0] + 0.6, sprite("rep53", 340, 340, lambda c: ic_repair(c, 170, 170, 2.2)), 880, 330)
    seq(img, t, ts[0] + 0.8, txt("YOUR", 64, SAGE, 5), 1360, 250)
    seq(img, t, ts[0] + 0.95, txt("REPAIR BILL", 88, IVORY, 3), 1360, 360)
    seq(img, t, ts[1], sprite("hg53", 200, 200, lambda c: (c.rrect((60, 10, 140, 190), 10, fill=SAGE_D), c.ell((50, 120, 150, 200), fill=SAGE_D), c.text((100, 150), "WAIT", FONT_SANS, 30, IVORY, track=1))), 500, 760, shadow=8, scale=0.9)
    seq(img, t, ts[1] + 0.2, txt("THE ONE I TOLD YOU TO WAIT FOR", 36, SAGE, 3), 1000, 760)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, stamp("BIGGEST DOLLAR AMOUNT", 780, 120, GOLD, size=44), 960, 910, scale=s, alpha=a, rot=-2, shadow=14)
        burst(img, t, ts[2], 960, 910, n=12, color=GOLD, rad=130, seed=54)

# ============================================================ BLOCCO 54
def draw54(img, t):
    ts = starts(54)
    common(img, t, "A REPAIR BILL")
    seq(img, t, ts[0], stamp("A REPAIR BILL", 560, 120, CORAL, size=54), 960, 200, shadow=12, rot=-2)
    cards = [(ic_furnace, "THE FURNACE", "QUITS IN JANUARY", ICE), (ic_leak_roof, "THE ROOF", "THAT LEAKS", CORAL), (ic_wire, "THE WIRING", "NOT SAFE ANYMORE", RED)]
    for k, (fn, a1, a2, col) in enumerate(cards):
        st = ts[1 + k]
        slide_in(img, t, st, sprite(("rc54", k), 540, 520, lambda c, fn=fn, a1=a1, a2=a2, col=col: (c.rrect((5, 5, 535, 515), 40, fill=PANEL_FILL, outline=col, width=8), fn(c, 270, 190, 2.0), c.text((270, 400), a1, FONT_SANS, 46, IVORY, track=2), c.text((270, 455), a2, FONT_SANS, 34, col, track=2))), 340 + k * 620, 520, dy=50, dur=0.55, shadow=14, scale=0.92)
    seq(img, t, ts[4], sprite("wipe54", 360, 220, lambda c: (ic_jar(c, 100, 110, 1.2), ic_x(c, 250, 120, 1.5, RED, 12))), 600, 880, shadow=8, scale=0.8)
    ban(img, t, ts[4] + 0.3, "ONE BILL CAN WIPE OUT YOUR SAVINGS", cy=900, cx=1250, w=1120, size=44)

# ============================================================ BLOCCO 55
def draw55(img, t):
    ts = starts(55)
    common(img, t, "SECTION 504 HOME REPAIR")
    seq(img, t, ts[0] - 0.05, sprite("usda55", 280, 220, lambda c: ic_gov(c, 140, 110, 1.9)), 300, 260, shadow=8)
    seq(img, t, ts[0] + 0.3, txt("U S DEPARTMENT OF AGRICULTURE", 38, SAGE, 3), 960, 160)
    for k, ch in enumerate(("504",)):
        pass
    s, a, p = pop(t, ts[0] + 1.0, 0.5)
    if p > 0:
        put(img, sprite("n504", 420, 220, lambda c: c.text((210, 110), "504", FONT_SERIF, 200, GOLD)), 960, 300, scale=s, alpha=a, shadow=12)
        burst(img, t, ts[0] + 1.0, 960, 300, n=12, color=GOLD, rad=260, seed=55)
    seq(img, t, ts[0] + 1.6, txt("HOME REPAIR", 58, IVORY, 6), 960, 440)
    slide_in(img, t, ts[1], panel(780, 380, border=GOLD), 520, 780, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, sprite("el55", 260, 300, lambda c: (ic_person(c, 130, 160, 2.2, col=GOLD), c.rrect((70, 6, 190, 56), 14, fill=IVORY), c.text((130, 32), "62+", FONT_SANS, 34, GREEN_D))), 400, 760, shadow=8)
    seq(img, t, ts[1] + 0.6, sprite("hm55", 220, 200, lambda c: ic_house(c, 110, 100, 1.8)), 680, 740, shadow=8)
    seq(img, t, ts[1] + 1.0, txt("HOMEOWNERS 62 OR OLDER", 34, IVORY, 3), 520, 930)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("nl55", 380, 220, lambda c: (c.rrect((5, 5, 375, 215), 40, fill=PANEL_FILL, outline=RED, width=8), c.text((190, 90), "LOANS", FONT_SANS, 64, RED, track=3), ic_x(c, 190, 100, 1.5, RED, 10))), 1450, 550, scale=s, alpha=a, rot=-3, shadow=12)
    seq(img, t, ts[2] + 0.1, txt("NOT LOANS", 36, RED, 4), 1450, 690)
    s, a, p = pop(t, ts[3] - 0.6, 0.5)
    if p > 0:
        put(img, sprite("gr55", 600, 240, lambda c: (c.rrect((5, 5, 595, 235), 44, fill=GOLD, outline=(168, 118, 40), width=8), c.text((300, 124), "GRANTS", FONT_SANS, 110, GREEN_D, track=4))), 1500, 880, scale=s, alpha=a, rot=2, shadow=16)
        burst(img, t, ts[3] - 0.6, 1500, 880, n=14, color=GOLD, rad=150, seed=56)

DRAW = {51: draw51, 52: draw52, 53: draw53, 54: draw54, 55: draw55}

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
