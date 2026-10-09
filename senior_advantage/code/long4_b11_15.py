"""Video lungo 4 (BOLLETTE) - blocchi 11-15. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-BOLLETTE.md.
Durate (timeline utente 08/10/2026): B11 256, B12 434, B13 284, B14 239, B15 240.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long4_b11_15.py <blocco>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b01_10 import *

DUR = {11: 256, 12: 434, 13: 284, 14: 239, 15: 240}
PHRASES = {
    11: ["The mistake people make?", "They wait for the bill to get scary.", "Don't.", "Apply in the fall,", "before the cold,", "while the funds are still there."],
    12: ["Income limits depend on your state, so you need your local office.", "To find it, call the national energy line:",
         "one, eight six six, six seven four, six three two seven.", "Or go to energy help dot u s."],
    13: ["Who does this help most?", "Anyone heating a house on a fixed income.", "And if you got help last year, don't assume it continues.", "Ask again this year."],
    14: ["Number two is connected to this one.", "And it's the reason some people pay less for heat every winter,", "not just this one."],
    15: ["Bill number two.", "And this one doesn't just help with one bill.", "It can lower your energy bill every month, for years."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def cal(top, big, col, mark=None):
    def fn(c):
        w, h = 330, 380
        c.rrect((4, 4, w - 4, h - 4), 28, fill=IVORY, outline=(206, 200, 186), width=5)
        c.rrect((4, 4, w - 4, 96), 28, fill=col)
        c.d.rectangle(c._b((4, 60, w - 4, 96)), fill=col)
        c.text((w / 2, 52), top, FONT_SANS, 40, IVORY, track=3)
        c.text((w / 2, 220), big, FONT_SANS, 76, GREEN_D, track=2)
        if mark == "check":
            c.ell((w / 2 - 38, 270, w / 2 + 38, 346), fill=GOLD, outline=(168, 118, 40), width=4)
            c.line([(w / 2 - 18, 308), (w / 2 - 4, 324), (w / 2 + 22, 290)], GREEN_D, 11)
        elif mark == "q":
            c.text((w / 2, 312), "?", FONT_SERIF, 100, RED)
    return sprite(("cal4", top, big, col, mark), 330, 380, fn)

def rarrow(col=GOLD, w=170, h=120):
    return sprite(("rarrow4", col, w, h), w, h, lambda c: c.poly([(6, h * .32), (w * .55, h * .32), (w * .55, 8), (w - 6, h / 2), (w * .55, h - 8), (w * .55, h * .68), (6, h * .68)], fill=col))

def leaf():
    def fn(c):
        c.poly([(70, 8), (116, 56), (130, 120), (70, 160), (10, 120), (24, 56)], fill=(214, 120, 52))
        c.line([(70, 20), (70, 170)], (150, 80, 30), 6)
    return sprite("leaf4", 140, 180, fn)

# ============================================================ BLOCCO 11
def draw11(img, t):
    ts = starts(11)
    common(img, t, "THE MISTAKE")
    seq(img, t, ts[0], stamp("THE MISTAKE", 560, 120, RED, size=56), 960, 205, shadow=12, rot=-2)
    # la bolletta spaventosa
    p = slide_in(img, t, ts[1], bill_paper(), 420, 520, dy=-90, dur=0.55, shadow=18, scale=0.85, rot=2 * math.sin(t * 9) * (1 if t < ts[2] else 0))
    seq(img, t, ts[1] + 0.5, sprite("warn11", 190, 180, lambda c: warn_tri(c, 95, 98, 1.45)), 620, 330, shadow=10)
    seq(img, t, ts[1] + 0.9, txt("WAIT UNTIL IT GETS SCARY", 38, RED, 2), 420, 790)
    # NO
    s, a, pp = pop(t, ts[2], 0.45)
    if pp > 0:
        put(img, sprite("x11", 300, 300, lambda c: ic_x(c, 150, 150, 3.3, RED, 16)), 420, 520, scale=0.95 * s, alpha=a)
        put(img, stamp("DON'T", 360, 110, RED, size=56), 420, 205 + 0, scale=0.0001) if False else None
    # autunno
    s, a, pp = pop(t, ts[3], 0.5)
    if pp > 0:
        put(img, cal("FALL", "OCT", (214, 120, 52), "check"), 1010, 500, scale=0.95 * s, alpha=a, shadow=14)
    # freddo
    p = ease(seg(t, ts[4], 0.5))
    if p > 0:
        put(img, rarrow(), 1250, 500, alpha=p, scale=0.8)
        put(img, sprite("snowball11", 300, 300, lambda c: (c.ell((6, 6, 294, 294), fill=PANEL_FILL, outline=ICE, width=7), ic_snow(c, 150, 150, 1.5))), 1560, 500, alpha=p, shadow=12)
        seq(img, t, ts[4] + 0.3, txt("BEFORE THE COLD", 36, ICE, 3), 1560, 690)
    # fondi
    p = ease(seg(t, ts[5], 0.5))
    if p > 0:
        put(img, fund_bar(1.0), 1260, 850, alpha=p, shadow=6)
        seq(img, t, ts[5] + 0.3, txt("FUNDS STILL THERE", 40, GOLD, 3), 1260, 775)
    ban(img, t, ts[5] + 0.5, "APPLY IN THE FALL", cy=985, cx=960, w=760, size=52)

# ============================================================ BLOCCO 12
def draw12(img, t):
    ts = starts(12)
    common(img, t, "YOUR LOCAL OFFICE")
    # pannello sinistro: stato
    slide_in(img, t, ts[0], panel(800, 560, border=GOLD), 500, 520, dx=-90, dur=0.55, shadow=16)
    seq(img, t, ts[0] + 0.35, sprite("gov12", 230, 200, lambda c: ic_gov(c, 115, 100, 1.5)), 500, 380, shadow=8)
    for k, col in enumerate((GOLD, SAGE, CORAL)):
        seq(img, t, ts[0] + 0.8 + k * 0.25, sprite(("pin12", k), 100, 130, lambda c, col=col: ic_pin(c, 50, 60, 1.1, col=col)), 350 + k * 150, 560)
    seq(img, t, ts[0] + 1.6, txt("LIMITS DEPEND ON YOUR STATE", 36, IVORY, 2), 500, 680)
    seq(img, t, ts[0] + 2.0, txt("FIND YOUR LOCAL OFFICE", 40, GOLD, 3), 500, 740)
    # pannello destro: linea nazionale
    slide_in(img, t, ts[1], panel(860, 560, border=SAGE), 1420, 520, dx=40, dur=0.55, shadow=16)
    seq(img, t, ts[1] + 0.3, sprite("ph12", 200, 200, lambda c: ic_phone(c, 100, 100, 1.4)), 1420, 360, shadow=8)
    seq(img, t, ts[1] + 0.6, txt("NATIONAL ENERGY LINE", 38, SAGE, 3), 1420, 460)
    num = "1-866-674-6327"
    t_start = ts[2] + 0.1; t_end = ts[3] - 0.5
    k = int(len(num) * min(1.0, max(0.0, (t - t_start) / max(0.1, t_end - t_start)))) if t >= t_start else 0
    if k > 0:
        put(img, txt(num[:k], 88, GOLD, 3), 1420 - (txt(num, 88, GOLD, 3).width - txt(num[:k], 88, GOLD, 3).width) / 2, 590, shadow=8) if False else None
        sp = txt(num[:k], 88, GOLD, 3); full = txt(num, 88, GOLD, 3)
        img.paste(sp, (int(1420 - full.width / 2), int(555 - sp.height / 2)), sp)
    # sito
    s, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, sprite("web12", 760, 110, lambda c: (c.rrect((4, 4, 756, 106), 55, fill=IVORY, outline=GOLD, width=7), c.ell((28, 22, 88, 82), outline=GREEN_D, width=6), c.line([(28, 52), (88, 52)], GREEN_D, 5), c.text((420, 56), "energyhelp.us", FONT_SANS_M, 50, GREEN_D))), 1420, 735, scale=s, alpha=a, shadow=10)
    seq(img, t, ts[3] + 0.4, txt("OR GO ONLINE", 36, SAGE, 3), 1420, 650)

# ============================================================ BLOCCO 13
def draw13(img, t):
    ts = starts(13)
    common(img, t, "WHO IT HELPS MOST")
    seq(img, t, ts[0], stamp("WHO IT HELPS MOST", 760, 120, GOLD, size=52), 960, 200, shadow=12)
    # casa con fuoco e fisso
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, sprite("hh13", 360, 360, lambda c: (ic_house(c, 180, 190, 3.0, col=IVORY), ic_flame(c, 180, 230, 1.3))), 400, 520, scale=s, alpha=a, shadow=14)
    seq(img, t, ts[1] + 0.6, sprite("fix13", 460, 120, lambda c: (c.rrect((4, 4, 456, 116), 30, fill=PANEL_FILL, outline=SAGE, width=6), c.text((230, 62), "FIXED INCOME", FONT_SANS, 42, SAGE, track=3))), 400, 790, shadow=8)
    # anno scorso -> quest'anno
    seq(img, t, ts[2], cal("LAST YEAR", "2025", SAGE_D, "check"), 1060, 520, shadow=14, scale=0.9)
    p = ease(seg(t, ts[2] + 0.8, 0.4))
    if p > 0:
        put(img, rarrow(w=140, h=100), 1280, 520, alpha=p, scale=0.8)
    seq(img, t, ts[2] + 1.0, cal("THIS YEAR", "2026", GOLD, "q"), 1500, 520, shadow=14, scale=0.9)
    seq(img, t, ts[2] + 1.8, txt("DON'T ASSUME IT CONTINUES", 38, RED, 2), 1280, 760)
    ban(img, t, ts[3] + 0.1, "ASK AGAIN THIS YEAR", cy=960, w=900, size=56)

# ============================================================ BLOCCO 14
def draw14(img, t):
    ts = starts(14)
    common(img, t, "TWO BILLS, CONNECTED")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(1, 280), 330, 340, scale=s, alpha=a, shadow=14)
        put(img, sprite("f14", 200, 220, lambda c: ic_flame(c, 100, 110, 1.6)), 330, 340, scale=0.0001 + 0.0 * s) if False else None
    seq(img, t, ts[0] + 0.1, sprite("ic1_14", 220, 240, lambda c: ic_flame(c, 110, 125, 1.8)), 700, 340, shadow=8)
    seq(img, t, ts[0] + 0.3, txt("HEATING HELP", 40, ORANGE if False else FLAME, 3), 700, 480)
    p = ease(seg(t, ts[0] + 0.6, 0.6))
    if p > 0:
        put(img, sprite("chain14", 360, 60, lambda c: link_chain(c, 20, 30, 9)), 1000, 340, alpha=p)
    seq(img, t, ts[0] + 0.9, numbadge(2, 280), 1590, 340, shadow=14)
    seq(img, t, ts[0] + 1.1, sprite("ic2_14", 230, 240, lambda c: ic_house(c, 115, 130, 1.8)), 1290, 340, shadow=8)
    seq(img, t, ts[0] + 1.3, txt("HOME UPGRADE", 40, GOLD, 3), 1290, 480)
    # inverni
    labels = ["THIS WINTER", "NEXT WINTER", "EVERY WINTER"]
    for k in range(3):
        s, a, p = pop(t, ts[1] + 0.2 + k * 0.7, 0.45)
        if p > 0:
            x = 420 + k * 540
            put(img, sprite(("w14", k), 440, 300, lambda c, k=k: (c.rrect((5, 5, 435, 295), 34, fill=PANEL_FILL, outline=ICE, width=6), ic_snow(c, 110, 130, 1.0), ic_flame(c, 250, 120, 0.8, col=FLAME), c.poly([(330, 70), (410, 70), (370, 150)], fill=GOLD), c.text((220, 235), labels[k], FONT_SANS, 40, IVORY, track=2))), x, 700, scale=0.9 * s, alpha=a, shadow=10)
    ban(img, t, ts[2] + 0.1, "NOT JUST THIS ONE", cy=985, w=860, size=52)

ORANGE = FLAME

# ============================================================ BLOCCO 15
def draw15(img, t):
    ts = starts(15)
    common(img, t, "BILL NUMBER TWO")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(2, 400), 360, 330, scale=s, alpha=a, shadow=18)
        burst(img, t, ts[0], 360, 330, n=14, color=GOLD, rad=300, seed=15)
    seq(img, t, ts[0] + 0.3, panel(1080, 400, border=GOLD), 1230, 330, shadow=14)
    seq(img, t, ts[0] + 0.5, sprite("bolt15", 300, 340, lambda c: ic_bolt(c, 150, 170, 2.4)), 880, 330)
    seq(img, t, ts[0] + 0.7, txt("YOUR", 64, SAGE, 5), 1360, 250)
    seq(img, t, ts[0] + 0.85, txt("ENERGY BILL", 88, IVORY, 3), 1360, 360)
    # grafico: barre che scendono mese per mese
    t0 = ts[2] + 0.1
    for k in range(12):
        g = ease(seg(t, t0 + k * 0.1, 0.4))
        if g > 0:
            h = 230 * (1 - 0.055 * k)
            hh = int(h * g)
            put(img, sprite(("bar15", k, hh), 70, max(4, hh), lambda c, hh=hh: c.rrect((2, 2, 68, max(6, hh) - 2), 10, fill=GOLD if hh > 60 else CORAL)), 520 + k * 80, 880 - hh / 2)
    seq(img, t, ts[1], sprite("down15", 200, 240, lambda c: (c.rrect((70, 6, 130, 130), 8, fill=GOLD), c.poly([(16, 120), (184, 120), (100, 232)], fill=GOLD))), 330, 760, scale=0.9, shadow=8)
    ban(img, t, ts[2] + 0.9, "EVERY MONTH, FOR YEARS", cy=985, w=960, size=54)

DRAW = {11: draw11, 12: draw12, 13: draw13, 14: draw14, 15: draw15}

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
