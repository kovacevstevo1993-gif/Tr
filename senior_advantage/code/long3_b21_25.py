"""Video lungo 3 (Costco) - blocchi 21-25 (fine punto 4, riepilogo, punto 5 Concierge). 1920x1080, 30 fps.
Durate dalla timeline dell'utente (07/10/2026): B21 324, B22 359, B23 496, B24 555, B25 400 fotogrammi.
Uso: OUT=cartella python3 long3_b21_25.py <blocco 21..25> [fotogrammi]
     python3 long3_b21_25.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b16_20 import *

DUR.update({21: 324, 22: 359, 23: 496, 24: 555, 25: 400})
PHRASES.update({
    21: ["Think about how many seniors skip the eye doctor", "because of the cost of glasses.",
         "At Costco, the exam and the glasses are two separate decisions,", "and that gives you room to compare."],
    22: ["But if you want to buy glasses or contact lenses from Costco,", "then you do need a membership.",
         "So you can take the exam first,", "get your prescription,", "and decide later where to buy."],
    23: ["Let's pause and count what we have so far.", "One, a drug discount program.", "Two, a pharmacy anyone can use.",
         "Three, a free hearing test.", "Four, an eye exam with no membership.", "And we are not even a third of the way through."],
    24: ["Five.", "Free tech support for the electronics you buy at Costco.", "It is called Concierge.",
         "If you bought a television, a projector, a computer, a laptop, a tablet,",
         "a camera, a home theater system, a printer or a major appliance,", "you can call for free technical help."],
    25: ["Think about what this means.", "The television that is stuck on the wrong input,", "the computer that will not connect,",
         "the printer that will not print.", "Instead of waiting for a grandchild or paying a stranger,", "you pick up the phone."],
})

BLUE = (110, 170, 200)

# ------------------------------------------------------------------ icone (centro cx, cy, scala s)
def ic_tv(c, cx, cy, s=1.0):
    c.rrect((cx - 70 * s, cy - 46 * s, cx + 70 * s, cy + 34 * s), 10 * s, fill=GREEN_D, outline=IVORY, width=7 * s)
    c.rrect((cx - 56 * s, cy - 34 * s, cx + 56 * s, cy + 22 * s), 4 * s, fill=BLUE)
    c.line([(cx, cy + 34 * s), (cx, cy + 52 * s)], IVORY, 8 * s)
    c.line([(cx - 30 * s, cy + 54 * s), (cx + 30 * s, cy + 54 * s)], IVORY, 9 * s)

def ic_projector(c, cx, cy, s=1.0):
    c.poly([(cx + 44 * s, cy + 6 * s), (cx + 96 * s, cy - 30 * s), (cx + 96 * s, cy + 46 * s)], fill=(240, 214, 140))
    c.rrect((cx - 70 * s, cy - 24 * s, cx + 52 * s, cy + 36 * s), 12 * s, fill=IVORY)
    c.ell((cx + 6 * s, cy - 12 * s, cx + 46 * s, cy + 28 * s), fill=GREEN_D, outline=GOLD, width=5 * s)
    c.ell((cx + 18 * s, cy, cx + 34 * s, cy + 16 * s), fill=BLUE)
    for k in range(3):
        c.rrect((cx - 54 * s, cy - 6 * s + k * 14 * s, cx - 14 * s, cy - 2 * s + k * 14 * s), 2 * s, fill=(176, 188, 180))

def ic_computer(c, cx, cy, s=1.0):
    c.rrect((cx - 60 * s, cy - 56 * s, cx + 60 * s, cy + 22 * s), 8 * s, fill=GREEN_D, outline=IVORY, width=7 * s)
    c.rrect((cx - 46 * s, cy - 42 * s, cx + 46 * s, cy + 8 * s), 4 * s, fill=BLUE)
    c.rrect((cx - 8 * s, cy + 22 * s, cx + 8 * s, cy + 44 * s), 2 * s, fill=IVORY)
    c.rrect((cx - 34 * s, cy + 44 * s, cx + 34 * s, cy + 56 * s), 5 * s, fill=IVORY)

def ic_laptop(c, cx, cy, s=1.0):
    c.rrect((cx - 62 * s, cy - 50 * s, cx + 62 * s, cy + 28 * s), 8 * s, fill=GREEN_D, outline=IVORY, width=7 * s)
    c.rrect((cx - 48 * s, cy - 36 * s, cx + 48 * s, cy + 14 * s), 4 * s, fill=BLUE)
    c.poly([(cx - 82 * s, cy + 40 * s), (cx + 82 * s, cy + 40 * s), (cx + 66 * s, cy + 58 * s), (cx - 66 * s, cy + 58 * s)], fill=IVORY)

def ic_tablet(c, cx, cy, s=1.0):
    c.rrect((cx - 44 * s, cy - 62 * s, cx + 44 * s, cy + 62 * s), 12 * s, fill=GREEN_D, outline=IVORY, width=7 * s)
    c.rrect((cx - 32 * s, cy - 50 * s, cx + 32 * s, cy + 38 * s), 4 * s, fill=BLUE)
    c.ell((cx - 7 * s, cy + 44 * s, cx + 7 * s, cy + 58 * s), fill=IVORY)

def ic_camera(c, cx, cy, s=1.0):
    c.rrect((cx - 30 * s, cy - 50 * s, cx + 14 * s, cy - 26 * s), 6 * s, fill=IVORY)
    c.rrect((cx - 66 * s, cy - 32 * s, cx + 66 * s, cy + 46 * s), 14 * s, fill=IVORY)
    c.ell((cx - 34 * s, cy - 20 * s, cx + 34 * s, cy + 48 * s), fill=GREEN_D, outline=GOLD, width=6 * s)
    c.ell((cx - 15 * s, cy - 1 * s, cx + 15 * s, cy + 29 * s), fill=BLUE)
    c.ell((cx + 42 * s, cy - 22 * s, cx + 56 * s, cy - 8 * s), fill=GOLD)

def ic_theater(c, cx, cy, s=1.0):
    c.rrect((cx - 60 * s, cy - 56 * s, cx + 60 * s, cy + 4 * s), 6 * s, fill=GREEN_D, outline=IVORY, width=6 * s)
    c.rrect((cx - 48 * s, cy - 44 * s, cx + 48 * s, cy - 8 * s), 3 * s, fill=BLUE)
    for sx in (-1, 1):
        c.rrect((cx + sx * 62 * s - 14 * s, cy + 14 * s, cx + sx * 62 * s + 14 * s, cy + 62 * s), 6 * s, fill=IVORY)
        c.ell((cx + sx * 62 * s - 7 * s, cy + 22 * s, cx + sx * 62 * s + 7 * s, cy + 36 * s), fill=GREEN_D)
        c.ell((cx + sx * 62 * s - 9 * s, cy + 40 * s, cx + sx * 62 * s + 9 * s, cy + 58 * s), fill=GREEN_D)
    c.rrect((cx - 36 * s, cy + 28 * s, cx + 36 * s, cy + 46 * s), 8 * s, fill=GOLD)

def ic_printer(c, cx, cy, s=1.0):
    c.rrect((cx - 38 * s, cy - 58 * s, cx + 38 * s, cy - 6 * s), 4 * s, fill=(236, 238, 230), outline=(180, 190, 180), width=3 * s)
    c.rrect((cx - 66 * s, cy - 12 * s, cx + 66 * s, cy + 44 * s), 10 * s, fill=IVORY)
    c.rrect((cx - 40 * s, cy + 26 * s, cx + 40 * s, cy + 64 * s), 4 * s, fill=(250, 250, 244), outline=(180, 190, 180), width=3 * s)
    c.ell((cx + 38 * s, cy + 2 * s, cx + 52 * s, cy + 16 * s), fill=GOLD)
    for k in range(2):
        c.line([(cx - 24 * s, cy + (38 + k * 12) * s), (cx + 24 * s, cy + (38 + k * 12) * s)], (190, 200, 190), 3 * s)

def ic_fridge(c, cx, cy, s=1.0):
    c.rrect((cx - 40 * s, cy - 64 * s, cx + 40 * s, cy + 64 * s), 10 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    c.line([(cx - 40 * s, cy - 8 * s), (cx + 40 * s, cy - 8 * s)], SAGE_D, 4 * s)
    c.rrect((cx + 22 * s, cy - 42 * s, cx + 29 * s, cy - 18 * s), 2 * s, fill=GREEN_D)
    c.rrect((cx + 22 * s, cy + 6 * s, cx + 29 * s, cy + 36 * s), 2 * s, fill=GREEN_D)

def ic_headset(c, cx, cy, s=1.0):
    c.arc((cx - 56 * s, cy - 64 * s, cx + 56 * s, cy + 48 * s), 180, 360, IVORY, 10 * s)
    c.rrect((cx - 68 * s, cy - 12 * s, cx - 38 * s, cy + 38 * s), 10 * s, fill=GOLD)
    c.rrect((cx + 38 * s, cy - 12 * s, cx + 68 * s, cy + 38 * s), 10 * s, fill=GOLD)
    c.line([(cx + 58 * s, cy + 36 * s), (cx + 42 * s, cy + 62 * s), (cx + 8 * s, cy + 62 * s)], IVORY, 7 * s)
    c.ell((cx - 2 * s, cy + 54 * s, cx + 16 * s, cy + 70 * s), fill=GOLD)

def ic_phone(c, cx, cy, s=1.0):
    c.arc((cx - 58 * s, cy - 44 * s, cx + 58 * s, cy + 72 * s), 200, 340, IVORY, 22 * s)
    c.rrect((cx - 70 * s, cy - 6 * s, cx - 36 * s, cy + 38 * s), 10 * s, fill=IVORY)
    c.rrect((cx + 36 * s, cy - 6 * s, cx + 70 * s, cy + 38 * s), 10 * s, fill=IVORY)

def ic_scale(c, cx, cy, s=1.0):
    c.line([(cx, cy - 58 * s), (cx, cy + 50 * s)], IVORY, 8 * s)
    c.line([(cx - 62 * s, cy - 38 * s), (cx + 62 * s, cy - 38 * s)], IVORY, 8 * s)
    for sx in (-1, 1):
        x0 = cx + sx * 62 * s
        c.line([(x0, cy - 38 * s), (x0 - 26 * s, cy + 8 * s)], IVORY, 5 * s)
        c.line([(x0, cy - 38 * s), (x0 + 26 * s, cy + 8 * s)], IVORY, 5 * s)
        c.arc((x0 - 28 * s, cy - 14 * s, x0 + 28 * s, cy + 32 * s), 0, 180, GOLD, 8 * s)
    c.rrect((cx - 34 * s, cy + 46 * s, cx + 34 * s, cy + 60 * s), 5 * s, fill=IVORY)

def ic_rx(c, cx, cy, s=1.0):
    c.rrect((cx - 48 * s, cy - 62 * s, cx + 48 * s, cy + 62 * s), 8 * s, fill=IVORY)
    c.text((cx - 12 * s, cy - 30 * s), "Rx", FONT_SERIF, 36 * s, CORAL_D)
    for k in range(3):
        c.line([(cx - 32 * s, cy + (6 + k * 18) * s), (cx + 32 * s - k * 10 * s, cy + (6 + k * 18) * s)], (176, 188, 180), 4 * s)

def ic_lens(c, cx, cy, s=1.0):
    c.ell((cx - 44 * s, cy - 44 * s, cx + 44 * s, cy + 44 * s), fill=(154, 200, 170), outline=IVORY, width=7 * s)
    c.arc((cx - 28 * s, cy - 28 * s, cx + 28 * s, cy + 28 * s), 200, 290, IVORY, 6 * s)

def ic_glasses_s(c, cx, cy, s=1.0):
    ic_glasses(c, cx, cy)

def ic_eyechart(c, cx, cy, s=1.0):
    eye_chart(c, cx, cy, 1.0 * s)

def ic_store(c, cx, cy, s=1.0):
    for k in range(5):
        c.poly([(cx - 62 * s + k * 25 * s, cy - 50 * s), (cx - 62 * s + (k + 1) * 25 * s, cy - 50 * s),
                (cx - 58 * s + (k + 1) * 25 * s, cy - 8 * s), (cx - 66 * s + k * 25 * s, cy - 8 * s)], fill=CORAL if k % 2 == 0 else IVORY)
    c.rrect((cx - 56 * s, cy - 8 * s, cx + 56 * s, cy + 56 * s), 6 * s, fill=CARD, outline=GOLD, width=4 * s)
    cross_ic(c, cx, cy + 18 * s, 20 * s, IVORY, GREEN_L)

def ic_hear_s(c, cx, cy, s=1.0):
    ic_hear(c, cx, cy)

def ic_pill(c, cx, cy, s=1.0):
    bottle(c, cx, cy, 1.0 * s)

def ic_dollar(c, cx, cy, s=1.0):
    c.ell((cx - 44 * s, cy - 44 * s, cx + 44 * s, cy + 44 * s), fill=GOLD, outline=(168, 118, 40), width=4 * s)
    c.text((cx, cy + 3 * s), "$", FONT_SANS, 58 * s, GREEN_D)

def ic_clock_(c, cx, cy, s=1.0):
    clock(c, cx, cy, 52 * s)

def ic_wifi_x(c, cx, cy, s=1.0):
    for r_ in (62, 42, 22):
        c.arc((cx - r_ * s, cy - r_ * s + 20 * s, cx + r_ * s, cy + r_ * s + 20 * s), 225, 315, IVORY, 9 * s)
    c.ell((cx - 7 * s, cy + 24 * s, cx + 7 * s, cy + 38 * s), fill=IVORY)
    c.line([(cx - 52 * s, cy - 40 * s), (cx + 52 * s, cy + 50 * s)], CORAL, 10 * s)

def ic_tv_warn(c, cx, cy, s=1.0):
    ic_tv(c, cx - 8 * s, cy - 6 * s, s * 0.92)
    warn_tri(c, cx + 52 * s, cy + 36 * s, 0.5 * s, CORAL, PANEL_FILL)

def ic_computer_x(c, cx, cy, s=1.0):
    ic_computer(c, cx, cy, s * 0.95)
    c.ell((cx - 34 * s, cy - 36 * s, cx + 34 * s, cy + 16 * s), outline=CORAL, width=8 * s)
    c.line([(cx - 24 * s, cy - 28 * s), (cx + 24 * s, cy + 8 * s)], CORAL, 8 * s)

def ic_printer_x(c, cx, cy, s=1.0):
    ic_printer(c, cx, cy, s * 0.95)
    c.ell((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), outline=CORAL, width=8 * s)
    c.line([(cx - 28 * s, cy - 28 * s), (cx + 28 * s, cy + 28 * s)], CORAL, 8 * s)

# ------------------------------------------------------------------ generatori
def mini(fn, sc):
    def mk():
        c = Cv(260, 260)
        fn(c, 130, 130, 1.0)
        return c.done().resize((int(260 * sc), int(260 * sc)), Image.LANCZOS)
    return cache(("mini", fn.__name__, sc), mk)

def paste_c(im, spr, cx, cy):
    im.paste(spr, (int(cx - spr.width / 2), int(cy - spr.height / 2)), spr)

def chipx(key, w, h, fill, border, fn, sc, lines, sizes, colors, bw=7, crossed_text=False):
    """chip con tondo scuro a sinistra + icona + 1 o 2 righe"""
    def mk():
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), min(44, h / 2), fill=fill, outline=border, width=bw)
        if h >= 200:
            d, left = 154, 34
        else:
            d, left = h - 30, 22
        c.ell((left, h / 2 - d / 2, left + d, h / 2 + d / 2), fill=GREEN_D)
        tx = left + d + 26
        if len(lines) == 1:
            c.text((tx, h / 2 + 2), lines[0], FONT_SANS, sizes[0], colors[0], anchor="lm")
        else:
            c.text((tx, h / 2 - 0.15 * h), lines[0], FONT_SANS, sizes[0], colors[0], anchor="lm")
            c.text((tx, h / 2 + 0.13 * h), lines[1], FONT_SANS, sizes[1], colors[1], anchor="lm")
        if crossed_text:
            c.line([(tx - 10, h / 2 + 2), (w - 40, h / 2 + 2)], CORAL, 6)
        im = c.done()
        paste_c(im, mini(fn, sc), left + d / 2, h / 2)
        return im
    return cache(key, mk)

def common4(img, t, text, n=None):
    ambient(img, t, "$", n=6, alpha=0.08)
    label(img, t, text, 70, GOLD, t0=0.1)
    if n:
        s, a, p = pop(t, 0.2, 0.4)
        put(img, num_badge(n, 120, 70), 96, 78, scale=s, alpha=a, shadow=5)

def show(img, t, t0, spr, x, y, sc=1.0, rot=0, sh=10, dur=0.45):
    s, a, p = pop(t, t0, dur)
    if p > 0:
        put(img, spr, x, y, scale=sc * s, alpha=a, rot=rot, shadow=sh)
    return p

def card_big(key, w, h, border, fn, sc, l1, l2, s1, s2, c1=IVORY, c2=GOLD, circle=(GREEN_L,), cy=130, r=92):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=border, width=6)
        c.ell((w / 2 - r, cy - r, w / 2 + r, cy + r), fill=circle[0])
        c.text((w / 2, cy + r + 44), l1, FONT_SANS, s1, c1)
        c.text((w / 2, cy + r + 44 + int(s2 * 1.15)), l2, FONT_SANS, s2, c2)
        im = c.done()
        paste_c(im, mini(fn, sc), w / 2, cy)
        return im
    return cache(key, mk)

# ============================================================ BLOCCO 21
def divider():
    def mk():
        c = Cv(30, 340)
        for k in range(8):
            c.rrect((11, 6 + k * 42, 19, 34 + k * 42), 4, fill=GOLD)
        return c.done()
    return cache("div21", mk)

def draw21(img, t):
    ts = starts(21)
    common4(img, t, "THE EYE EXAM", 4)
    show(img, t, ts[0], chipx("c21a", 880, 230, PANEL_FILL, CORAL, ic_eyechart, 0.78, ("SENIORS SKIP", "THE EYE DOCTOR"), (40, 56), (SAGE, CORAL), bw=8), 490, 270)
    show(img, t, ts[1], chipx("c21b", 880, 230, GREEN_L, SAGE, ic_dollar, 0.9, ("BECAUSE OF THE COST", "OF GLASSES"), (40, 60), (IVORY, GOLD)), 1430, 270)
    show(img, t, ts[2], pill_spr("TWO SEPARATE DECISIONS", 44, 860, 88, GOLD, GREEN_D), 960, 440, sh=8)
    show(img, t, ts[2] + 0.5, card_big("c21e", 560, 340, GOLD, ic_eyechart, 0.9, "THE", "EXAM", 40, 64, cy=100, r=74), 470, 685)
    show(img, t, ts[2] + 1.0, card_big("c21g", 560, 340, GOLD, ic_glasses_s, 0.9, "THE", "GLASSES", 40, 64, cy=100, r=74), 1450, 685)
    dv = fade(t, ts[2] + 0.9)
    if dv > 0:
        put(img, divider(), 960, 685, alpha=dv)
    show(img, t, ts[3], chipx("c21s", 1200, 150, GREEN_L, GOLD, ic_scale, 0.5, ("ROOM TO COMPARE",), (56,), (IVORY,)), 960, 950)

# ============================================================ BLOCCO 22
def step22(i):
    def mk():
        w, h = 540, 400
        fns = (ic_eyechart, ic_rx, ic_store)
        l = (("TAKE THE", "EXAM FIRST"), ("GET YOUR", "PRESCRIPTION"), ("DECIDE LATER", "WHERE TO BUY"))[i]
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=GOLD, width=6)
        c.ell((24, 22, 104, 102), fill=GOLD)
        c.text((64, 62), str(i + 1), FONT_SERIF, 52, GREEN_D)
        c.ell((w / 2 - 82, 70, w / 2 + 82, 234), fill=GREEN_L)
        c.text((w / 2, 288), l[0], FONT_SANS, 40, IVORY)
        c.text((w / 2, 348), l[1], FONT_SANS, 48 if i != 1 else 44, GOLD)
        im = c.done()
        paste_c(im, mini(fns[i], 0.78), w / 2, 152)
        return im
    return cache(("s22", i), mk)

def draw22(img, t):
    ts = starts(22)
    common4(img, t, "BUYING IS A DIFFERENT STEP", 4)
    def gl(c, cx, cy, s=1.0):
        ic_glasses(c, cx - 36, cy + 6)
    show(img, t, ts[0], chipx("c22a", 1600, 150, GREEN_L, SAGE, ic_lens, 0.5, ("GLASSES OR CONTACT LENSES FROM COSTCO",), (50,), (IVORY,)), 960, 215)
    def memb(c, cx, cy, s=1.0):
        c.rrect((cx - 66, cy - 44, cx + 66, cy + 44), 10, fill=(236, 188, 108))
        c.rrect((cx - 66, cy - 26, cx + 66, cy - 8), 0, fill=(150, 105, 40))
        c.rrect((cx - 46, cy + 8, cx - 12, cy + 30), 4, fill=(210, 160, 80))
    show(img, t, ts[1], chipx("c22b", 1600, 150, PANEL_FILL, GOLD, memb, 0.5, ("THEN YOU DO NEED A MEMBERSHIP",), (50,), (GOLD,)), 960, 395)
    pos = (330, 960, 1590)
    for i, k in enumerate((2, 3, 4)):
        show(img, t, ts[k], step22(i), pos[i], 770, sh=12)
        if i > 0:
            ar = seg(t, ts[k] - 0.05, 0.35)
            if ar > 0:
                put(img, arrow_spr(), pos[i] - 315, 770, scale=0.55 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))

# ============================================================ BLOCCO 23
def row23(i):
    def mk():
        w, h = 1500, 120
        fns = (ic_pill, ic_store, ic_hear_s, ic_eyechart)
        txt = ("A DRUG DISCOUNT PROGRAM", "A PHARMACY ANYONE CAN USE", "A FREE HEARING TEST", "AN EYE EXAM, NO MEMBERSHIP")
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=GOLD, width=5)
        c.ell((22, 15, 112, 105), fill=GOLD)
        c.text((67, 62), str(i + 1), FONT_SERIF, 58, GREEN_D)
        c.ell((136, 12, 228, 108), fill=GREEN_D)
        c.text((262, h / 2 + 2), txt[i], FONT_SANS, 48, IVORY, anchor="lm")
        im = c.done()
        paste_c(im, mini(fns[i], 0.38), 182, 60)
        return im
    return cache(("r23", i), mk)

def prog23(k):
    def mk():
        w, h = 1520, 90
        c = Cv(w, h)
        for j in range(14):
            x0 = 8 + j * 108
            on = j < k
            c.rrect((x0, 14, x0 + 100, 76), 14, fill=GOLD if on else CARD, outline=(168, 118, 40) if on else SAGE_D, width=4)
            c.text((x0 + 50, 46), str(j + 1), FONT_SANS, 34, GREEN_D if on else SAGE)
        return c.done()
    return cache(("p23", k), mk)

def draw23(img, t):
    ts = starts(23)
    common4(img, t, "LET'S COUNT")
    for i in range(4):
        show(img, t, ts[i + 1], row23(i), 960, 215 + i * 140, sh=8)
    k = int(max(0, min(4, (t - (ts[5] + 0.2)) / 0.4 + 1))) if t > ts[5] + 0.2 else 0
    pb = pop(t, ts[5], 0.45)
    if pb[2] > 0:
        put(img, prog23(k), 960, 840, alpha=pb[1], scale=pb[0])
    mk_ = fade(t, ts[5] + 1.8)
    if mk_ > 0:
        put(img, pill_spr("NOT EVEN A THIRD OF THE WAY", 46, 980, 96, PANEL_FILL, GOLD, GOLD), 960, 965, alpha=mk_, shadow=8)

# ============================================================ BLOCCO 24
DEVICES = [(ic_tv, "TV", ""), (ic_projector, "PROJECTOR", ""), (ic_computer, "COMPUTER", ""), (ic_laptop, "LAPTOP", ""),
           (ic_tablet, "TABLET", ""), (ic_camera, "CAMERA", ""), (ic_theater, "HOME", "THEATER"),
           (ic_printer, "PRINTER", ""), (ic_fridge, "MAJOR", "APPLIANCE")]

def tile24(i):
    def mk():
        w, h = 190, 215
        fn, l1, l2 = DEVICES[i]
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 26, fill=CARD, outline=GOLD, width=5)
        if l2:
            c.text((w / 2, 158), l1, FONT_SANS, 24, IVORY)
            c.text((w / 2, 188), l2, FONT_SANS, 24, GOLD)
        else:
            c.text((w / 2, 172), l1, FONT_SANS, 26, GOLD)
        im = c.done()
        paste_c(im, mini(fn, 0.56), w / 2, 84)
        return im
    return cache(("t24", i), mk)

def draw24(img, t):
    ts = starts(24)
    common4(img, t, "SAVING NUMBER 5")
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(5), 330, 330, scale=0.85 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 330, n=14, seed=3, rad=250)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("FREE TECH SUPPORT", FONT_SANS, 100, GOLD), 590, 290, 100, alpha=h1)
        put_left(img, tspr("FOR THE ELECTRONICS YOU BUY AT COSTCO", FONT_SANS, 48, IVORY), 590, 392, 48, alpha=h1)
    show(img, t, ts[2], pill_spr("IT IS CALLED CONCIERGE", 44, 820, 92, GOLD, GREEN_D), 1000, 500, sh=8)
    for i in range(9):
        if i < 5:
            st = ts[3] + 0.3 + i * 0.4
        else:
            st = ts[4] + 0.1 + (i - 5) * 0.5
        show(img, t, st, tile24(i), 140 + i * 205, 725, sh=6, dur=0.4)
    show(img, t, ts[5], chipx("c24p", 1300, 150, GOLD, (168, 118, 40), ic_headset, 0.5, ("CALL FOR FREE TECHNICAL HELP",), (50,), (GREEN_D,)), 960, 945, sh=12)
    if t > ts[5]:
        burst(img, t, ts[5] + 0.2, 960, 945, n=10, seed=7, rad=110)

# ============================================================ BLOCCO 25
def prob25(i):
    fns = (ic_tv_warn, ic_wifi_x, ic_printer_x)
    ls = (("TV STUCK ON", "THE WRONG INPUT"), ("COMPUTER WILL", "NOT CONNECT"), ("PRINTER WILL", "NOT PRINT"))
    return card_big(("p25", i), 500, 400, CORAL, fns[i], 0.9, ls[i][0], ls[i][1], 40, 44, c2=CORAL, circle=(PANEL_FILL,), cy=125, r=92)

def draw25(img, t):
    ts = starts(25)
    common4(img, t, "WHAT THIS MEANS", 5)
    intro(img, t, "THINK ABOUT", "WHAT THIS MEANS", ts[1], size=130)
    xs = (320, 960, 1600)
    for i in range(3):
        show(img, t, ts[i + 1], prob25(i), xs[i], 360, sh=12)
    show(img, t, ts[4], chipx("c25a", 860, 130, PANEL_FILL, CORAL, ic_tv_blank, 0.4, ("WAITING FOR A GRANDCHILD",), (40,), (IVORY,), crossed_text=True), 480, 715, sh=8)
    show(img, t, ts[4] + 2.1, chipx("c25b", 860, 130, PANEL_FILL, CORAL, ic_dollar, 0.5, ("PAYING A STRANGER",), (44,), (IVORY,), crossed_text=True), 1440, 715, sh=8)
    show(img, t, ts[5], chipx("c25c", 1300, 150, GOLD, (168, 118, 40), ic_phone, 0.5, ("YOU PICK UP THE PHONE",), (58,), (GREEN_D,)), 960, 915, sh=12)
    if t > ts[5]:
        burst(img, t, ts[5] + 0.2, 960, 915, n=10, seed=4, rad=110)

def ic_tv_blank(c, cx, cy, s=1.0):
    person_ic(c, cx, cy + 6, 1.1, (190, 140, 66))

DRAW.update({21: draw21, 22: draw22, 23: draw23, 24: draw24, 25: draw25})

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
