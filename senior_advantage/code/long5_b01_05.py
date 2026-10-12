"""Video lungo 5 (AEROPORTO) - blocchi 1-5. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AEROPORTO.md.
Durate dalla timeline dell'utente (12/10/2026): B1 381, B2 466, B3 382, B4 310, B5 306.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long5_b01_05.py <blocco> [fotogrammi]
     python3 long5_b01_05.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b01_10 import *      # 1920x1080, motore, icone, banner, txt, seq, slide_in, panel, stamp, bubble3

DUR = {1: 381, 2: 466, 3: 382, 4: 310, 5: 306}
PHRASES = {
    1: ["At an airport security line,", "there is a rule written only for people seventy five and older.",
        "And the people it was written for often walk right past it,", "because nobody at the checkpoint says a word."],
    2: ["I'm talking about eight things.", "Your photo I D.", "Help from the curb to your gate.", "Your cane.",
        "Your oxygen machine.", "Your pills.", "And one rule about a cancelled flight",
        "that can put real money back in your pocket.", "The biggest one is number eight."],
    3: ["Now, some of you are thinking,", "I don't need any help at the airport.", "Others are thinking,",
        "I only fly once a year, so this isn't for me.", "Both are missing something,", "and I'll show you what in a minute."],
    4: ["And if you've ever stood in a security line", "wondering if you were doing something wrong,", "stay with me.",
        "Most of these take thirty seconds to use,", "and they cost nothing."],
    5: ["Stay until the end,", "because there is one sentence", "that makes almost all of these work.",
        "And most people only say it", "after the problem has already happened."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

STEEL = (200, 215, 205)
BELT = (70, 96, 86)

# ------------------------------------------------------------------ icone nuove
def star5(c, cx, cy, r, col):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * 0.42
        pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    c.poly(pts, fill=col)

def ic_idcard(c, cx, cy, s):
    c.rrect((cx - 80 * s, cy - 52 * s, cx + 80 * s, cy + 52 * s), 10 * s, fill=IVORY, outline=(206, 200, 186), width=3)
    c.ell((cx - 62 * s, cy - 28 * s, cx - 14 * s, cy + 20 * s), fill=SKIN)
    c.d.pieslice(c._b((cx - 66 * s, cy + 6 * s, cx - 10 * s, cy + 60 * s)), 180, 360, fill=SAGE_D)
    for k in range(3):
        c.rrect((cx + 4 * s, cy - 24 * s + k * 22 * s, cx + 62 * s - k * 8 * s, cy - 12 * s + k * 22 * s), 3, fill=(206, 212, 206))
    star5(c, cx + 58 * s, cy - 36 * s, 17 * s, GOLD)

def ic_gate(c, cx, cy, s):
    ic_person(c, cx - 78 * s, cy + 6 * s, s * 0.9, col=SAGE)
    c.poly([(cx - 36 * s, cy + 2 * s), (cx + 6 * s, cy + 2 * s), (cx + 6 * s, cy - 14 * s), (cx + 36 * s, cy + 16 * s),
            (cx + 6 * s, cy + 46 * s), (cx + 6 * s, cy + 30 * s), (cx - 36 * s, cy + 30 * s)], fill=GOLD)
    c.rrect((cx + 50 * s, cy - 40 * s, cx + 112 * s, cy + 56 * s), 8 * s, fill=GREEN_L, outline=GOLD, width=3)
    c.text((cx + 81 * s, cy - 8 * s), "GATE", FONT_SANS, 17 * s, IVORY, track=1)
    c.text((cx + 81 * s, cy + 26 * s), "A12", FONT_SANS, 26 * s, GOLD)

def ic_cane(c, cx, cy, s):
    c.line([(cx + 8 * s, cy - 50 * s), (cx + 8 * s, cy + 66 * s)], (214, 164, 96), 14 * s)
    c.arc((cx - 40 * s, cy - 82 * s, cx + 20 * s, cy - 24 * s), 180, 360, (214, 164, 96), 14 * s)
    c.rrect((cx - 2 * s, cy + 60 * s, cx + 18 * s, cy + 72 * s), 3, fill=SAGE_D)

def ic_oxygen(c, cx, cy, s):
    c.rrect((cx - 30 * s, cy - 44 * s, cx + 30 * s, cy + 66 * s), 24 * s, fill=(110, 176, 124), outline=SAGE, width=3)
    c.rrect((cx - 12 * s, cy - 62 * s, cx + 12 * s, cy - 42 * s), 4, fill=STEEL)
    c.text((cx, cy + 12 * s), "O2", FONT_SANS, 30 * s, GREEN_D)
    c.arc((cx + 10 * s, cy - 92 * s, cx + 90 * s, cy - 20 * s), 270, 450, ICE, 7 * s)
    c.ell((cx + 70 * s, cy - 36 * s, cx + 96 * s, cy - 12 * s), fill=ICE)

def ic_pills(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy - 6 * s, cx + 10 * s, cy + 38 * s), 22 * s, fill=CORAL)
    c.rrect((cx - 70 * s, cy - 6 * s, cx - 30 * s, cy + 38 * s), 22 * s, fill=IVORY)
    c.d.rectangle(c._b((cx - 50 * s, cy - 6 * s, cx - 30 * s, cy + 38 * s)), fill=IVORY)
    c.ell((cx + 14 * s, cy - 44 * s, cx + 74 * s, cy + 16 * s), fill=GOLD, outline=(168, 118, 40), width=3)
    c.line([(cx + 26 * s, cy - 14 * s), (cx + 62 * s, cy - 14 * s)], (168, 118, 40), 4 * s)
    c.ell((cx + 30 * s, cy + 20 * s, cx + 84 * s, cy + 74 * s), fill=ICE, outline=(96, 150, 176), width=3)

def ic_plane(c, cx, cy, s, col=IVORY):
    c.ell((cx - 70 * s, cy - 14 * s, cx + 70 * s, cy + 14 * s), fill=col)
    c.poly([(cx - 8 * s, cy - 6 * s), (cx + 22 * s, cy - 62 * s), (cx + 40 * s, cy - 62 * s), (cx + 24 * s, cy - 4 * s)], fill=col)
    c.poly([(cx - 8 * s, cy + 6 * s), (cx + 22 * s, cy + 62 * s), (cx + 40 * s, cy + 62 * s), (cx + 24 * s, cy + 4 * s)], fill=col)
    c.poly([(cx - 62 * s, cy - 4 * s), (cx - 74 * s, cy - 36 * s), (cx - 56 * s, cy - 36 * s), (cx - 38 * s, cy - 4 * s)], fill=col)

def ic_refund(c, cx, cy, s):
    ic_plane(c, cx - 22 * s, cy - 4 * s, s * 0.95, col=SAGE)
    ic_x(c, cx - 22 * s, cy - 4 * s, s * 1.2, RED, 12)
    ic_coin(c, cx + 62 * s, cy + 40 * s, 38 * s)

def ic_clockface(c, cx, cy, r, sweep):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=IVORY, outline=GOLD, width=r * 0.09)
    for k in range(12):
        a = math.pi * k / 6
        c.line([(cx + math.sin(a) * r * 0.80, cy - math.cos(a) * r * 0.80), (cx + math.sin(a) * r * 0.92, cy - math.cos(a) * r * 0.92)], GREEN_D, r * 0.05)
    if sweep > 0.01:
        c.d.pieslice(c._b((cx - r * 0.78, cy - r * 0.78, cx + r * 0.78, cy + r * 0.78)), -90, -90 + 360 * sweep, fill=(246, 210, 140))
    a = 2 * math.pi * sweep
    c.line([(cx, cy), (cx + math.sin(a) * r * 0.78, cy - math.cos(a) * r * 0.78)], CORAL_D, r * 0.07)
    c.ell((cx - r * 0.08, cy - r * 0.08, cx + r * 0.08, cy + r * 0.08), fill=GREEN_D)

def ic_officer(c, cx, cy, s):
    c.ell((cx - 22 * s, cy - 58 * s, cx + 22 * s, cy - 14 * s), fill=SKIN)
    c.rrect((cx - 28 * s, cy - 68 * s, cx + 28 * s, cy - 44 * s), 6 * s, fill=(36, 76, 128))
    c.d.pieslice(c._b((cx - 44 * s, cy - 6 * s, cx + 44 * s, cy + 80 * s)), 180, 360, fill=(54, 100, 160))
    star5(c, cx + 16 * s, cy + 16 * s, 9 * s, GOLD)

# ============================================================ BLOCCO 1
def checkpoint():
    def fn(c):
        c.rrect((30, 400, 730, 480), 22, fill=BELT, outline=SAGE_D, width=5)
        for k in range(10):
            c.line([(80 + k * 66, 414), (80 + k * 66, 466)], (50, 74, 66), 4)
        c.rrect((120, 330, 330, 404), 12, fill=(150, 170, 160), outline=IVORY, width=4)
        c.rrect((146, 342, 200, 380), 6, fill=CORAL)
        c.rrect((214, 346, 300, 380), 6, fill=GOLD)
        for x in (440, 640):
            c.rrect((x, 150, x + 44, 410), 8, fill=STEEL, outline=SAGE_D, width=3)
        c.rrect((424, 70, 704, 160), 18, fill=IVORY, outline=SAGE_D, width=4)
        c.text((564, 115), "SECURITY", FONT_SANS, 44, GREEN_D, track=3)
        c.ell((545, 168, 565, 188), fill=(110, 200, 130))
        c.rrect((470, 224, 614, 300), 8, fill=(30, 68, 58))
        c.rrect((476, 258, 608, 266), 3, fill=(110, 200, 130))
    return sprite("check5", 760, 520, fn)

def shield75():
    def fn(c):
        pts = [(190, 12), (350, 68), (342, 250), (190, 428), (38, 250), (30, 68)]
        c.poly(pts, fill=GOLD)
        c.poly([(190, 38), (326, 84), (320, 244), (190, 396), (60, 244), (54, 84)], fill=(246, 214, 140))
        c.text((190, 200), "75+", FONT_SANS, 128, GREEN_D)
        c.text((190, 300), "AND OLDER", FONT_SANS, 34, GREEN_D, track=2)
        star5(c, 190, 360, 20, GREEN_D)
    return sprite("shield75", 380, 440, fn)

def walker():
    def fn(c):
        ic_person(c, 90, 100, 1.5, col=SAGE)
        c.line([(150, 120), (160, 190)], (214, 164, 96), 9)
        c.arc((140, 100, 170, 130), 180, 360, (214, 164, 96), 9)
    return sprite("walker5", 220, 250, fn)

def bubble_dots():
    def fn(c):
        w, h = 300, 190
        c.rrect((6, 6, w - 6, 140), 40, fill=IVORY, outline=SAGE_D, width=4)
        c.poly([(46, 134), (100, 134), (36, 184)], fill=IVORY)
        for k in range(3):
            c.ell((82 + k * 68, 56, 118 + k * 68, 92), fill=GREEN_D)
    return sprite("bubdots5", 300, 190, fn)

def draw1(img, t):
    ts = starts(1)
    common(img, t, "AIRPORT SECURITY")
    slide_in(img, t, ts[0], checkpoint(), 540, 430, dx=-60, dur=0.6, shadow=16, scale=1.05)
    s_, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, shield75(), 1190, 400, scale=s_ * 1.15, alpha=a, shadow=14)
        burst(img, t, ts[1], 1190, 400, n=12, color=GOLD, rad=260, seed=5)
    seq(img, t, ts[1] + 0.5, txt("A RULE FOR", 44, SAGE, 2), 1650, 330)
    seq(img, t, ts[1] + 0.7, txt("AGES 75", 70, GOLD, 2), 1650, 410)
    seq(img, t, ts[1] + 0.9, txt("AND OLDER", 70, GOLD, 2), 1650, 495)
    # persona col bastone che cammina oltre la regola
    p = ease(seg(t, ts[2], 1.8))
    if p > 0:
        x = 360 + 1280 * p
        put(img, sprite("walk_arrow5", 1500, 60, lambda c: (c.line([(10, 30), (1420, 30)], SAGE_D, 8), c.poly([(1420, 6), (1490, 30), (1420, 54)], fill=SAGE_D))), 1060, 820, alpha=0.9)
        put(img, walker(), x, 760, shadow=8, scale=1.35)
    if ts[2] + 0.4 <= t < ts[3]:
        seq(img, t, ts[2] + 0.4, txt("WALKS RIGHT PAST IT", 52, IVORY, 2), 960, 940)
    # nessuno dice una parola
    seq(img, t, ts[3], sprite("officer5", 220, 220, lambda c: ic_officer(c, 110, 110, 1.4)), 190, 870, shadow=8, scale=1.3)
    seq(img, t, ts[3] + 0.35, bubble_dots(), 440, 830, shadow=8, scale=0.85)
    ban(img, t, ts[3] + 0.8, "NOBODY SAYS A WORD", cy=1005, w=1000, h=84, size=46)

# ============================================================ BLOCCO 2
def tile2e(n, fn, name, hl=False, hidden=False, filled=True):
    def mk():
        w, h = 400, 320
        c = Cv(w, h)
        if hidden or not filled:
            c.rrect((4, 4, w - 4, h - 4), 30, fill=(10, 40, 32), outline=SAGE_D, width=4)
            c.text((w / 2, 130), "?" if hidden else str(n), FONT_SANS, 130, (40, 84, 70))
            c.ell((w / 2 - 30, 232, w / 2 + 30, 292), fill=(20, 56, 46), outline=SAGE_D, width=3)
            c.text((w / 2, 263), str(n), FONT_SERIF, 36, SAGE_D)
            return c.done()
        c.rrect((4, 4, w - 4, h - 4), 30, fill=(40, 70, 52) if hl else PANEL_FILL, outline=GOLD if hl else SAGE_D, width=9 if hl else 5)
        if n is not None:
            c.ell((22, 20, 82, 80), fill=GOLD, outline=(168, 118, 40), width=4)
            c.text((52, 51), str(n), FONT_SERIF, 42, GREEN_D)
        fn(c, w / 2, 148, 1.15)
        c.text((w / 2, 276), name, FONT_SANS, 31, GOLD if hl else IVORY, track=0)
        return c.done()
    return cache(("tile5", n, name, hl, hidden, filled), mk)

SIX = [(ic_idcard, "PHOTO I D"), (ic_gate, "HELP TO THE GATE"), (ic_cane, "YOUR CANE"),
       (ic_oxygen, "OXYGEN MACHINE"), (ic_pills, "YOUR PILLS"), (ic_refund, "CANCELLED FLIGHT")]
def tile_pos(i):
    return 480 + (i % 3) * 480, 410 + (i // 3) * 370

def draw2(img, t):
    ts = starts(2)
    common(img, t, "THE LIST")
    s_, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, stamp("8 THINGS", 520, 120, GOLD, size=72), 960, 160, scale=s_, alpha=a, shadow=10)
        burst(img, t, ts[0], 960, 160, n=12, color=GOLD, rad=240, seed=3)
    st = [ts[1], ts[2], ts[3], ts[4], ts[5], ts[6]]
    for i, (fn, name) in enumerate(SIX):
        x, y = tile_pos(i)
        hl = (i == 5 and t > ts[8])
        s2, a2, p2 = pop(t, st[i], 0.45)
        if p2 > 0:
            put(img, tile2e(8 if hl else None, fn, name, hl=hl), x, y, scale=s2 * (1.05 if hl else 1.0), alpha=a2, shadow=10)
            if p2 < 1 and i != 5:
                burst(img, t, st[i], x, y, n=8, color=GOLD, rad=170, seed=i + 1)
    x6, y6 = tile_pos(5)
    if t >= ts[7]:
        burst(img, t, ts[7], x6 + 60, y6 + 20, n=14, color=GOLD, rad=260, seed=11)
    if ts[7] <= t < ts[8]:
        ban(img, t, ts[7], "REAL MONEY BACK IN YOUR POCKET", cy=1010, w=1260, h=96, size=48)
    if t >= ts[8]:
        seq(img, t, ts[8], sprite("crown5", 120, 90, lambda c: (c.poly([(8, 76), (8, 22), (38, 52), (60, 8), (82, 52), (112, 22), (112, 76)], fill=GOLD), c.rrect((8, 70, 112, 86), 6, fill=(168, 118, 40)))), x6 + 142, y6 - 96, scale=0.62)
        ban(img, t, ts[8] + 0.1, "THE BIGGEST ONE IS NUMBER EIGHT", cy=1010, w=1260, h=96, size=48)

# ============================================================ BLOCCO 3
def chip(text, col):
    return pill_spr(text, 34, 320, 58, col, GREEN_D, track=2)

def draw3(img, t):
    ts = starts(3)
    common(img, t, "TWO WRONG IDEAS")
    seq(img, t, ts[0], chip("SOME OF YOU", SAGE), 520, 150, shadow=6)
    slide_in(img, t, ts[0] + 0.3, bubble3(["I DON'T NEED ANY", "HELP AT THE", "AIRPORT"], SAGE, lambda c, x, y, s: ic_person(c, x, y + 30, s * 1.1, col=SAGE_D)), 520, 480, dx=-100, dur=0.6, shadow=14)
    seq(img, t, ts[2], chip("OTHERS", GOLD), 1400, 150, shadow=6)
    slide_in(img, t, ts[2] + 0.3, bubble3(["I ONLY FLY", "ONCE A YEAR,", "SO THIS ISN'T FOR ME"], GOLD, lambda c, x, y, s: (ic_plane(c, x - 30, y + 10, s * 0.6, col=IVORY), c.text((x + 90, y + 14), "1x", FONT_SANS, 64, GOLD))), 1400, 480, dx=100, dur=0.6, shadow=14)
    s, a, p = pop(t, ts[4], 0.5)
    if p > 0:
        put(img, stamp("BOTH ARE MISSING SOMETHING", 1100, 130, GOLD, size=52), 960, 855, scale=s, alpha=a, shadow=14)
        burst(img, t, ts[4], 960, 855, n=14, color=GOLD, rad=230, seed=9)
    ban(img, t, ts[5] + 0.1, "I'LL SHOW YOU WHAT IN A MINUTE", cy=1005, w=1200, h=84, size=44)

# ============================================================ BLOCCO 4
def draw4(img, t):
    ts = starts(4)
    common(img, t, "THE SECURITY LINE")
    # fila di persone
    cols = [SAGE, GOLD, (120, 170, 210), CORAL, SAGE_D]
    for i in range(5):
        st = ts[0] + 0.18 * i
        s, a, p = pop(t, st, 0.4)
        if p > 0:
            put(img, sprite(("q5", i), 260, 300, lambda c, i=i: ic_person(c, 130, 150, 2.0, col=cols[i])), 220 + i * 190, 690, scale=s, alpha=a, shadow=6)
    seq(img, t, ts[0] + 1.0, txt("SECURITY LINE", 44, SAGE, 4), 590, 870)
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, bubble_spr(720, 240, IVORY, ["AM I DOING", "SOMETHING WRONG?"], DARK, 58), 560, 380, scale=s, alpha=a, shadow=10)
    ban(img, t, ts[2], "STAY WITH ME", cy=1005, w=700, h=84, size=46)
    # 30 secondi
    slide_in(img, t, ts[3], panel(700, 300, border=GOLD), 1440, 290, dx=80, dur=0.5, shadow=14)
    sw = ease(seg(t, ts[3] + 0.3, 1.4)) * 0.5
    if t >= ts[3] + 0.2:
        put(img, sprite(("clk5", round(sw, 3)), 200, 200, lambda c: ic_clockface(c, 100, 100, 86, sw)), 1190, 290)
        seq(img, t, ts[3] + 0.3, txt("30 SECONDS", 62, GOLD, 2), 1550, 262)
        seq(img, t, ts[3] + 0.6, txt("TO USE MOST OF THESE", 34, SAGE, 2), 1550, 330)
    # costano zero
    slide_in(img, t, ts[4], panel(700, 300, border=SAGE), 1440, 640, dx=80, dur=0.5, shadow=14)
    s, a, p = pop(t, ts[4] + 0.3, 0.45)
    if p > 0:
        put(img, sprite("coin0_5", 200, 200, lambda c: (c.ell((10, 10, 190, 190), fill=GOLD, outline=(168, 118, 40), width=8), c.text((100, 104), "$0", FONT_SANS, 76, GREEN_D))), 1190, 640, scale=s, alpha=a, shadow=8)
    seq(img, t, ts[4] + 0.5, txt("THEY COST", 48, IVORY, 2), 1550, 610)
    seq(img, t, ts[4] + 0.7, txt("NOTHING", 62, GOLD, 2), 1550, 680)

# ============================================================ BLOCCO 5
def lockbar(w, h):
    def mk():
        c = Cv(w, h)
        c.rrect((0, 0, w, h), h / 2, fill=(70, 92, 84))
        return c.done()
    return cache(("lb5", w, h), mk)

def secret_bubble():
    def fn(c):
        w, h = 1100, 380
        c.rrect((6, 6, w - 6, h - 46), 54, fill=PANEL_FILL, outline=GOLD, width=8)
        c.poly([(160, h - 50), (260, h - 50), (140, h - 4)], fill=PANEL_FILL)
        c.line([(160, h - 48), (140, h - 4), (260, h - 48)], GOLD, 8)
        c.text((120, 100), "“", FONT_SERIF, 150, GOLD)
        for k, wd in enumerate((820, 720, 520)):
            c.rrect((170, 96 + k * 66, 170 + wd, 134 + k * 66), 19, fill=(70, 92, 84))
        # cadenaccio
        c.rrect((w - 190, 160, w - 90, 240), 12, fill=GOLD, outline=(168, 118, 40), width=4)
        c.arc((w - 175, 100, w - 105, 190), 180, 360, GOLD, 12)
        c.ell((w - 150, 190, w - 130, 210), fill=GREEN_D)
    return sprite("secret5", 1100, 380, fn)

def num_dot(n, on=True):
    def mk():
        c = Cv(110, 110)
        c.ell((4, 4, 106, 106), fill=GOLD if on else (30, 62, 52), outline=(168, 118, 40), width=5)
        c.text((55, 57), str(n), FONT_SERIF, 56, GREEN_D)
        return c.done()
    return cache(("nd5", n, on), mk)

def marker(text, col, sub, w=420):
    def mk():
        c = Cv(w, 170)
        c.rrect((4, 4, w - 4, 86), 22, fill=PANEL_FILL, outline=col, width=6)
        c.text((w / 2, 46), text, FONT_SANS, 30, col, track=1)
        c.poly([(w / 2 - 18, 84), (w / 2 + 18, 84), (w / 2, 118)], fill=col)
        c.ell((w / 2 - 14, 118, w / 2 + 14, 146), fill=col)
        return c.done()
    return cache(("mk5", text, col, sub, w), mk)

def draw5(img, t):
    ts = starts(5)
    common(img, t, "THE ONE SENTENCE")
    seq(img, t, ts[1], secret_bubble(), 960, 330, shadow=16)
    # otto cose
    on_a = fade(t, ts[3], 0.4)
    if t >= ts[2]:
        for i in range(8):
            s, a, p = pop(t, ts[2] + 0.12 * i, 0.4)
            if p > 0 and on_a < 1:
                put(img, num_dot(i + 1), 450 + i * 150, 720, scale=s, alpha=a * (1 - on_a))
        seq(img, t, ts[2] + 1.2, txt("IT WORKS FOR ALMOST ALL OF THEM", 52, IVORY, 2), 960, 840) if on_a < 1 else None
    # linea del tempo
    if t >= ts[3]:
        p = ease(seg(t, ts[3], 0.6))
        put(img, sprite("tl5", 1500, 40, lambda c: c.rrect((0, 12, 1500, 28), 8, fill=SAGE_D)), 960, 807, alpha=p)
        s, a, pp = pop(t, ts[3] + 0.3, 0.5)
        if pp > 0:
            put(img, marker("MOST PEOPLE SAY IT HERE", RED, "", w=600), 1500, 760, scale=s, alpha=a, shadow=8)
    if t >= ts[4]:
        s, a, pp = pop(t, ts[4], 0.5)
        put(img, marker("THE PROBLEM HAPPENS", GOLD, "", w=480), 960, 760, scale=s, alpha=a, shadow=8)
        s, a, pp = pop(t, ts[4] + 0.6, 0.5)
        if pp > 0:
            put(img, marker("SAY IT BEFORE", (110, 200, 130), "", w=380), 440, 760, scale=s, alpha=a, shadow=8)
        seq(img, t, ts[4] + 0.9, txt("TIME", 36, SAGE, 6), 1690, 865)
    # etichette sotto la linea
    # (nessun testo extra: tutto e nei marcatori)

DRAW = {1: draw1, 2: draw2, 3: draw3, 4: draw4, 5: draw5}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/V5-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
