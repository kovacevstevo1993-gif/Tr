"""Video lungo 3 (Costco) - blocchi 31-35 (fine punto 6 garanzia, punto 7 gomme).
Durate dalla timeline dell'utente (07/10/2026): B31 628, B32 222, B33 398, B34 358, B35 422 fotogrammi.
Uso: OUT=cartella python3 long3_b31_35.py <blocco 31..35> [fotogrammi]
     python3 long3_b31_35.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b26_30 import *

DUR.update({31: 628, 32: 222, 33: 398, 34: 358, 35: 393})
PHRASES.update({
    31: ["Now the fine print, because it matters.", "The second year mirrors the manufacturer's warranty.",
         "If something is not covered in the first year, it is not covered in the second.",
         "Data backup, software replacement, physical damage and liquid damage are common exclusions.",
         "And touchscreen tablets are not included."],
    32: ["So before a salesperson at any store", "sells you an extended warranty,", "stop and check what you already have."],
    33: ["For example, if you bought a television at Costco,", "mark two dates in your calendar:", "one year from the day you bought it,",
         "and two years.", "Those are the dates when your coverage changes, and when it ends."],
    34: ["Seven.", "Tires.", "If you buy tires at Costco,", "installation is included at no charge.",
         "And the installation package also includes lifetime maintenance for those tires."],
    35: ["That means rotations,", "balancing,", "inflation pressure checks", "and flat repairs,", "for as long as you own the tires.",
         "Flat repairs follow industry standards, so not every puncture can be repaired."],
})

# ------------------------------------------------------------------ icone nuove
def i_tire(c, cx, cy, s=1.0): ic_tire(c, cx, cy)
def i_cloud(c, cx, cy, s=1.0):
    c.ell((cx - 60 * s, cy - 6 * s, cx - 8 * s, cy + 40 * s), fill=IVORY); c.ell((cx - 30 * s, cy - 40 * s, cx + 34 * s, cy + 24 * s), fill=IVORY)
    c.ell((cx + 6 * s, cy - 14 * s, cx + 62 * s, cy + 40 * s), fill=IVORY); c.rrect((cx - 40 * s, cy + 6 * s, cx + 44 * s, cy + 40 * s), 10 * s, fill=IVORY)
    c.poly([(cx, cy - 8 * s), (cx + 22 * s, cy + 14 * s), (cx + 8 * s, cy + 14 * s), (cx + 8 * s, cy + 32 * s), (cx - 8 * s, cy + 32 * s), (cx - 8 * s, cy + 14 * s), (cx - 22 * s, cy + 14 * s)], fill=BLUE)
def i_disc(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 46 * s, cx + 56 * s, cy + 46 * s), 8 * s, fill=IVORY)
    c.rrect((cx - 56 * s, cy - 46 * s, cx + 56 * s, cy - 24 * s), 8 * s, fill=BLUE)
    for k in range(3): c.rrect((cx - 42 * s, cy - 8 * s + k * 18 * s, cx + (30 - k * 12) * s, cy + 2 * s + k * 18 * s), 3 * s, fill=(176, 188, 180))
def i_crack(c, cx, cy, s=1.0):
    ic_tv(c, cx, cy, s)
    c.line([(cx - 10 * s, cy - 34 * s), (cx + 4 * s, cy - 12 * s), (cx - 8 * s, cy + 2 * s), (cx + 10 * s, cy + 20 * s)], IVORY, 5 * s)
    c.line([(cx + 4 * s, cy - 12 * s), (cx + 28 * s, cy - 18 * s)], IVORY, 4 * s)
def i_drop(c, cx, cy, s=1.0):
    c.poly([(cx, cy - 58 * s), (cx + 40 * s, cy + 6 * s), (cx - 40 * s, cy + 6 * s)], fill=BLUE)
    c.ell((cx - 40 * s, cy - 16 * s, cx + 40 * s, cy + 56 * s), fill=BLUE)
    c.ell((cx - 22 * s, cy + 2 * s, cx - 8 * s, cy + 20 * s), fill=IVORY)
def i_salesman(c, cx, cy, s=1.0):
    person_ic(c, cx, cy + 6 * s, 1.3 * s, (80, 96, 120))
    c.poly([(cx - 6 * s, cy + 18 * s), (cx + 6 * s, cy + 18 * s), (cx + 10 * s, cy + 56 * s), (cx, cy + 62 * s), (cx - 10 * s, cy + 56 * s)], fill=CORAL)
def i_stop(c, cx, cy, s=1.0):
    pts = [(cx + math.cos(math.pi / 8 + k * math.pi / 4) * 56 * s, cy + math.sin(math.pi / 8 + k * math.pi / 4) * 56 * s) for k in range(8)]
    c.poly(pts, fill=CORAL)
    c.text((cx, cy + 2 * s), "STOP", FONT_SANS, 24 * s, IVORY)
def i_search(c, cx, cy, s=1.0): magnifier(c, cx - 14 * s, cy - 14 * s, 34 * s, IVORY, 10 * s)
def i_cal1(c, cx, cy, s=1.0):
    calendar(c, cx, cy, s); c.text((cx, cy + 22 * s), "1", FONT_SERIF, 46 * s, GREEN_D)
def i_cal2(c, cx, cy, s=1.0):
    calendar(c, cx, cy, s); c.text((cx, cy + 22 * s), "2", FONT_SERIF, 46 * s, GREEN_D)
def i_wrench(c, cx, cy, s=1.0):
    c.line([(cx - 40 * s, cy + 46 * s), (cx + 30 * s, cy - 24 * s)], IVORY, 18 * s)
    c.ell((cx + 6 * s, cy - 62 * s, cx + 62 * s, cy - 6 * s), fill=IVORY); c.ell((cx + 26 * s, cy - 54 * s, cx + 52 * s, cy - 28 * s), fill=GREEN_D)
def i_rot(c, cx, cy, s=1.0):
    ic_tire(c, cx, cy)
    c.arc((cx - 66 * s, cy - 66 * s, cx + 66 * s, cy + 66 * s), 300, 40, GOLD, 8 * s)
    c.poly([(cx + 56 * s, cy - 40 * s), (cx + 78 * s, cy - 44 * s), (cx + 68 * s, cy - 22 * s)], fill=GOLD)
def i_bal(c, cx, cy, s=1.0):
    ic_tire(c, cx, cy)
    for a in (0.3, 3.2): c.ell((cx + math.cos(a) * 52 * s - 9 * s, cy + math.sin(a) * 52 * s - 9 * s, cx + math.cos(a) * 52 * s + 9 * s, cy + math.sin(a) * 52 * s + 9 * s), fill=GOLD)
def i_gauge(c, cx, cy, s=1.0):
    c.ell((cx - 56 * s, cy - 56 * s, cx + 56 * s, cy + 56 * s), fill=IVORY, outline=GOLD, width=7 * s)
    c.arc((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), 150, 390, (176, 188, 180), 6 * s)
    c.line([(cx, cy + 4 * s), (cx + 32 * s, cy - 22 * s)], CORAL, 6 * s); c.ell((cx - 8 * s, cy - 4 * s, cx + 8 * s, cy + 12 * s), fill=GREEN_D)
    c.text((cx, cy + 36 * s), "PSI", FONT_SANS, 16 * s, GREEN_D)
def i_patch(c, cx, cy, s=1.0):
    ic_tire(c, cx, cy)
    c.rrect((cx - 20 * s, cy - 14 * s, cx + 20 * s, cy + 14 * s), 6 * s, fill=GOLD)
    c.line([(cx - 8 * s, cy), (cx + 8 * s, cy)], GREEN_D, 5 * s)
def i_inf(c, cx, cy, s=1.0):
    c.ell((cx - 66 * s, cy - 30 * s, cx + 8 * s, cy + 30 * s), outline=GOLD, width=11 * s)
    c.ell((cx - 8 * s, cy - 30 * s, cx + 66 * s, cy + 30 * s), outline=GOLD, width=11 * s)

def sh_gold(c, cx, cy, s=1.0): shield(c, cx, cy, 0.8 * s)
def w_gold(c, cx, cy, s=1.0): warn_tri(c, cx, cy, 0.55 * s, GOLD, PANEL_FILL)
def w_coral(c, cx, cy, s=1.0): warn_tri(c, cx, cy, 0.8 * s, CORAL, PANEL_FILL)
def mk_chip(key, w, h, fill, border, fn, sc, lines, sizes, colors, **kw):
    return chipx(key, w, h, fill, border, fn, sc, lines, sizes, colors, **kw)

def draw31(img, t):
    ts = starts(31)
    common4(img, t, "THE FINE PRINT", 6)
    intro(img, t, "THE FINE PRINT", "MATTERS", ts[1], size=140)
    show(img, t, ts[1], mk_chip("c31a", 1500, 150, GREEN_L, GOLD, i_cal2, 0.5, ("YEAR 2 MIRRORS THE MANUFACTURER'S WARRANTY",), (46,), (IVORY,)), 960, 215)
    show(img, t, ts[2], mk_chip("c31b", 740, 170, GREEN_L, SAGE, i_cal1, 0.6, ("NOT COVERED", "IN YEAR 1"), (38, 52), (IVORY, GOLD)), 480, 420)
    ar = seg(t, ts[2] + 0.8, 0.4)
    if ar > 0: put(img, arrow_spr(), 960, 420, scale=0.9 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[2] + 1.3, mk_chip("c31c", 740, 170, PANEL_FILL, CORAL, i_cal2, 0.6, ("NOT COVERED", "IN YEAR 2"), (38, 52), (IVORY, CORAL)), 1440, 420)
    ex = [(i_cloud, "DATA", "BACKUP"), (i_disc, "SOFTWARE", "REPLACEMENT"), (i_crack, "PHYSICAL", "DAMAGE"), (i_drop, "LIQUID", "DAMAGE")]
    for i, (fn, a, b) in enumerate(ex):
        def mkc(i=i, fn=fn, a=a, b=b):
            def mk():
                w, h = 410, 330
                c = Cv(w, h)
                c.rrect((3, 3, w - 3, h - 3), 36, fill=PANEL_FILL, outline=CORAL, width=6)
                c.ell((w / 2 - 78, 22, w / 2 + 78, 178), fill=GREEN_L)
                c.text((w / 2, 226), a, FONT_SANS, 40, IVORY); c.text((w / 2, 276), b, FONT_SANS, 40, CORAL)
                im = c.done(); paste_c(im, mini(fn, 0.75), w / 2, 100)
                c2 = Cv(w, h)
                c2.ell((w / 2 - 78, 22, w / 2 + 78, 178), outline=CORAL, width=9)
                c2.line([(w / 2 - 54, 46), (w / 2 + 54, 154)], CORAL, 9)
                o = c2.done(); im.paste(o, (0, 0), o)
                return im
            return cache(("x31", i), mk)
        show(img, t, ts[3] + 0.2 + i * 0.9, mkc(), 255 + i * 470, 700, sh=12)
    show(img, t, ts[4], mk_chip("c31t", 1300, 130, PANEL_FILL, CORAL, i_tablet_w, 0.45, ("TOUCHSCREEN TABLETS ARE NOT INCLUDED",), (46,), (CORAL,)), 960, 955, sh=10)

def i_tablet_w(c, cx, cy, s=1.0):
    ic_tablet(c, cx, cy, s)
    c.ell((cx - 60 * s, cy - 60 * s, cx + 60 * s, cy + 60 * s), outline=CORAL, width=8 * s); c.line([(cx - 40 * s, cy - 40 * s), (cx + 40 * s, cy + 40 * s)], CORAL, 8 * s)

def draw32(img, t):
    ts = starts(32)
    common4(img, t, "BEFORE YOU BUY ANOTHER", 6)
    show(img, t, ts[0], card_big("c32a", 500, 400, SAGE_D, i_salesman, 0.9, "A SALESPERSON", "AT ANY STORE", 36, 40, c2=SAGE, cy=125, r=92), 400, 330, sh=12)
    show(img, t, ts[1], card_big("c32b", 560, 400, GOLD, ic_dollar, 0.9, "SELLS YOU AN", "EXTENDED WARRANTY", 38, 38, cy=125, r=92), 1100, 330, sh=12)
    s2, a2, p2 = pop(t, ts[2], 0.45)
    if p2 > 0: put(img, mini(i_stop, 1.9), 1590, 400, scale=s2, alpha=a2, shadow=10)
    show(img, t, ts[2] + 0.7, mk_chip("c32c", 1560, 190, GREEN_L, GOLD, sh_gold, 1.0, ("CHECK WHAT YOU", "ALREADY HAVE"), (50, 66), (IVORY, GOLD)), 960, 790, sh=14)
    if t > ts[2] + 1.0: burst(img, t, ts[2] + 1.0, 400, 790, n=8, seed=3, rad=100)

def draw33(img, t):
    ts = starts(33)
    common4(img, t, "MARK TWO DATES", 6)
    show(img, t, ts[0], mk_chip("c33a", 1300, 150, GREEN_L, SAGE, ic_tv, 0.5, ("YOUR TV, BOUGHT AT COSTCO",), (50,), (IVORY,)), 960, 200)
    show(img, t, ts[1], pill_spr("MARK TWO DATES IN YOUR CALENDAR", 44, 1040, 90, GOLD, GREEN_D), 960, 360, sh=8)
    show(img, t, ts[2], card_big("c33b", 520, 380, GOLD, i_cal1, 1.0, "ONE YEAR", "AFTER YOU BOUGHT IT", 44, 34, cy=120, r=90), 520, 640, sh=12)
    show(img, t, ts[3], card_big("c33c", 520, 380, GOLD, i_cal2, 1.0, "TWO YEARS", "AFTER YOU BOUGHT IT", 44, 34, cy=120, r=90), 1400, 640, sh=12)
    show(img, t, ts[4], mk_chip("c33d", 1560, 130, PANEL_FILL, GOLD, w_gold, 1.0, ("YEAR 1: COVERAGE CHANGES.   YEAR 2: COVERAGE ENDS",), (40,), (GOLD,)), 960, 930, sh=10)

def draw34(img, t):
    ts = starts(34)
    common4(img, t, "SAVING NUMBER 7", 7 if False else None)
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(7), 330, 300, scale=0.8 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 300, n=14, seed=3, rad=240)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("TIRES", FONT_SANS, 150, GOLD), 590, 300, 150, alpha=h1)
    show(img, t, ts[2], mk_chip("c34a", 1100, 170, GREEN_L, SAGE, i_tire, 0.7, ("BUY TIRES", "AT COSTCO"), (38, 60), (SAGE, IVORY)), 760, 560)
    def inst(c, x, y, s=1.0):
        i_wrench(c, x, y); c.ell((x - 62, y - 62, x + 62, y + 62), outline=GOLD, width=0)
    show(img, t, ts[3], mk_chip("c34b", 1500, 170, GREEN_L, GOLD, i_wrench, 0.7, ("INSTALLATION INCLUDED", "AT NO CHARGE"), (60, 50), (IVORY, GOLD)), 960, 760, sh=12)
    show(img, t, ts[4], mk_chip("c34c", 1500, 170, GOLD, (168, 118, 40), i_inf, 0.8, ("LIFETIME MAINTENANCE", "FOR THOSE TIRES"), (60, 46), (GREEN_D, GREEN_D)), 960, 960, sh=12)
    if t > ts[4]: burst(img, t, ts[4] + 0.3, 960, 960, n=10, seed=6, rad=110)

def draw35(img, t):
    ts = starts(35)
    common4(img, t, "WHAT MAINTENANCE MEANS", None)
    cards = [(i_rot, "ROTATIONS", ""), (i_bal, "BALANCING", ""), (i_gauge, "PRESSURE", "CHECKS"), (i_patch, "FLAT", "REPAIRS")]
    for i, (fn, a, b) in enumerate(cards):
        def mk(i=i, fn=fn, a=a, b=b):
            return card_big(("c35", i), 410, 380, GOLD, fn, 0.95, a, b if b else "", 40, 40, cy=125, r=92)
        show(img, t, ts[i] + 0.1, mk(), 255 + i * 470, 330, sh=12)
    show(img, t, ts[4], mk_chip("c35e", 1500, 150, GOLD, (168, 118, 40), i_inf, 0.7, ("FOR AS LONG AS YOU OWN THE TIRES",), (50,), (GREEN_D,)), 960, 640, sh=12)
    show(img, t, ts[5], mk_chip("c35f", 1620, 190, PANEL_FILL, CORAL, w_coral, 1.0, ("FLAT REPAIRS FOLLOW INDUSTRY STANDARDS:", "NOT EVERY PUNCTURE CAN BE REPAIRED"), (40, 44), (IVORY, CORAL)), 960, 880, sh=12)

DRAW.update({31: draw31, 32: draw32, 33: draw33, 34: draw34, 35: draw35})

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/costco-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
