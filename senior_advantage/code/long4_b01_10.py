"""Video lungo 4 (BOLLETTE) - blocchi 1-10. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-BOLLETTE.md.
Durate dalla timeline dell'utente (08/10/2026): B1 391, B2 374, B3 430, B4 260, B5 393, B6 392, B7 205, B8 423, B9 320, B10 392.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long4_b01_10.py <blocco> [fotogrammi]
     python3 long4_b01_10.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b02_05 import *      # 1920x1080, motore, sprite comuni (common, pill_spr, magnifier, check_ic...)

DUR = {1: 391, 2: 374, 3: 430, 4: 260, 5: 393, 6: 392, 7: 205, 8: 423, 9: 320, 10: 392}
PHRASES = {
    1: ["Right now, somewhere in your mail,", "there is a bill you are paying in full,",
        "that a program in your state was set up to help you pay.",
        "And nobody whose job is collecting that money", "is ever going to call you and tell you."],
    2: ["I'm talking about seven bills.", "Heating,", "electricity,", "your phone,", "groceries,", "the bus,",
        "and one repair bill that can cost thousands.", "And the biggest one on this list is number seven."],
    3: ["Now, some of you are thinking, this is only for people who are really struggling.",
        "Others are thinking, I own my home, so this isn't for me.",
        "Both groups are wrong,", "and I'll show you exactly who each one helps most."],
    4: ["And if you rent, don't click away.", "Six of these seven work for renters too,",
        "and one of them can make your apartment cheaper to heat for years."],
    5: ["Stay until the end,", "because there is one thing that connects several of these bills.",
        "Most people apply in the wrong order,", "and miss help they already qualified for.",
        "I'll show you the right order at the end."],
    6: ["One more thing before we start.", "Everything in this video comes from official government pages.",
        "No guesses, no rumors.", "Rules and limits change by state,", "so I'll always tell you where to check."],
    7: ["Bill number one.", "Your heating bill.",
        "And this one comes first for a reason, because the clock is already running."],
    8: ["It's a federal program called L I H E A P,", "the Low Income Home Energy Assistance Program.",
        "It helps pay heating bills in winter,", "cooling bills in summer,",
        "and it can help in an emergency, like a shutoff notice."],
    9: ["Here's the part almost nobody knows.", "When there is an older adult in the home, that household is a priority.",
        "You are not at the back of the line.", "You are near the front."],
    10: ["But here's the catch.", "The money is limited.", "Every year, each state gets a set amount.",
         "And when it runs out, it runs out.", "Some offices stop taking applications when the money is gone."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

RED = (214, 108, 96)
FLAME = (236, 128, 52)
ICE = (150, 205, 232)

# ------------------------------------------------------------------ icone (centro cx, cy, scala s)
def ic_flame(c, cx, cy, s, col=FLAME, inner=(250, 200, 90)):
    pts = [(0, -70), (22, -38), (44, -2), (46, 28), (30, 56), (0, 68), (-30, 56), (-46, 28), (-40, -4), (-20, 14), (-14, -30)]
    c.poly([(cx + x * s, cy + y * s) for x, y in pts], fill=col)
    pts2 = [(0, -8), (18, 18), (20, 40), (0, 56), (-20, 40), (-18, 18)]
    c.poly([(cx + x * s, cy + y * s) for x, y in pts2], fill=inner)

def ic_bolt(c, cx, cy, s, col=GOLD):
    pts = [(14, -72), (-30, 6), (-4, 6), (-18, 72), (32, -12), (4, -12)]
    c.poly([(cx + x * s, cy + y * s) for x, y in pts], fill=col)

def ic_phone(c, cx, cy, s, col=IVORY, scr=GREEN_D):
    c.rrect((cx - 34 * s, cy - 62 * s, cx + 34 * s, cy + 62 * s), 12 * s, fill=col, outline=SAGE_D, width=3)
    c.rrect((cx - 27 * s, cy - 48 * s, cx + 27 * s, cy + 40 * s), 5 * s, fill=scr)
    c.ell((cx - 7 * s, cy + 46 * s, cx + 7 * s, cy + 58 * s), fill=SAGE_D)

def ic_bag(c, cx, cy, s):
    c.line([(cx - 22 * s, cy - 34 * s), (cx - 22 * s, cy - 58 * s), (cx + 22 * s, cy - 58 * s), (cx + 22 * s, cy - 34 * s)], (160, 112, 60), 8 * s)
    c.poly([(cx - 52 * s, cy - 34 * s), (cx + 52 * s, cy - 34 * s), (cx + 44 * s, cy + 62 * s), (cx - 44 * s, cy + 62 * s)], fill=(214, 164, 96))
    c.ell((cx - 30 * s, cy - 58 * s, cx + 4 * s, cy - 24 * s), fill=CORAL)
    c.poly([(cx + 4 * s, cy - 46 * s), (cx + 40 * s, cy - 44 * s), (cx + 34 * s, cy - 24 * s), (cx + 8 * s, cy - 28 * s)], fill=(110, 176, 124))

def ic_bus(c, cx, cy, s):
    c.rrect((cx - 66 * s, cy - 44 * s, cx + 66 * s, cy + 40 * s), 14 * s, fill=GOLD, outline=(168, 118, 40), width=3)
    for k in range(3):
        c.rrect((cx - 56 * s + k * 38 * s, cy - 32 * s, cx - 26 * s + k * 38 * s, cy - 2 * s), 4 * s, fill=(190, 222, 232))
    c.rrect((cx - 66 * s, cy + 6 * s, cx + 66 * s, cy + 14 * s), 2, fill=(168, 118, 40))
    for x in (-38, 38):
        c.ell((cx + (x - 14) * s, cy + 28 * s, cx + (x + 14) * s, cy + 56 * s), fill=GREEN_D, outline=IVORY, width=3)

def ic_repair(c, cx, cy, s):
    c.poly([(cx - 60 * s, cy - 2 * s), (cx, cy - 56 * s), (cx + 60 * s, cy - 2 * s)], fill=CORAL)
    c.rrect((cx - 46 * s, cy - 6 * s, cx + 46 * s, cy + 56 * s), 3, fill=IVORY)
    c.rrect((cx - 12 * s, cy + 18 * s, cx + 12 * s, cy + 56 * s), 3, fill=(160, 112, 60))
    # chiave inglese
    c.line([(cx + 12 * s, cy + 52 * s), (cx + 62 * s, cy + 2 * s)], GOLD, 14 * s)
    c.ell((cx + 50 * s, cy - 18 * s, cx + 80 * s, cy + 12 * s), fill=GOLD)
    c.ell((cx + 58 * s, cy - 10 * s, cx + 72 * s, cy + 4 * s), fill=GREEN_D)

def ic_snow(c, cx, cy, s, col=ICE):
    for k in range(3):
        a = math.pi * k / 3
        dx, dy = math.cos(a) * 52 * s, math.sin(a) * 52 * s
        c.line([(cx - dx, cy - dy), (cx + dx, cy + dy)], col, 8 * s)
        for sgn in (-1, 1):
            ex, ey = cx + sgn * dx, cy + sgn * dy
            for da in (-0.6, 0.6):
                c.line([(ex, ey), (ex - sgn * math.cos(a + da) * 16 * s, ey - sgn * math.sin(a + da) * 16 * s)], col, 6 * s)

def ic_sun(c, cx, cy, s, col=GOLD):
    c.ell((cx - 28 * s, cy - 28 * s, cx + 28 * s, cy + 28 * s), fill=col)
    for k in range(8):
        a = math.pi * k / 4
        c.line([(cx + math.cos(a) * 40 * s, cy + math.sin(a) * 40 * s), (cx + math.cos(a) * 58 * s, cy + math.sin(a) * 58 * s)], col, 8 * s)

def ic_notice(c, cx, cy, s):
    c.rrect((cx - 46 * s, cy - 58 * s, cx + 46 * s, cy + 58 * s), 8 * s, fill=IVORY)
    c.rrect((cx - 46 * s, cy - 58 * s, cx + 46 * s, cy - 24 * s), 8 * s, fill=RED)
    c.text((cx, cy - 40 * s), "NOTICE", FONT_SANS, 17 * s, IVORY, track=2)
    for k in range(3):
        c.rrect((cx - 32 * s, cy - 8 * s + k * 20 * s, cx + 32 * s, cy + 2 * s + k * 20 * s), 3, fill=(206, 202, 190))

def ic_clock(c, cx, cy, r, ang=0.0):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=IVORY, outline=GOLD, width=r * 0.09)
    for k in range(12):
        a = math.pi * k / 6
        c.line([(cx + math.sin(a) * r * 0.80, cy - math.cos(a) * r * 0.80), (cx + math.sin(a) * r * 0.92, cy - math.cos(a) * r * 0.92)], GREEN_D, r * 0.04)
    c.line([(cx, cy), (cx + math.sin(ang * 0.0833) * r * 0.5, cy - math.cos(ang * 0.0833) * r * 0.5)], GREEN_D, r * 0.08)
    c.line([(cx, cy), (cx + math.sin(ang) * r * 0.74, cy - math.cos(ang) * r * 0.74)], CORAL_D, r * 0.05)
    c.ell((cx - r * 0.07, cy - r * 0.07, cx + r * 0.07, cy + r * 0.07), fill=GREEN_D)

def ic_gov(c, cx, cy, s, col=IVORY):
    c.poly([(cx - 70 * s, cy - 22 * s), (cx, cy - 66 * s), (cx + 70 * s, cy - 22 * s)], fill=col)
    for k in range(4):
        x = cx - 52 * s + k * 35 * s
        c.rrect((x - 8 * s, cy - 14 * s, x + 8 * s, cy + 40 * s), 2, fill=col)
    c.rrect((cx - 70 * s, cy + 44 * s, cx + 70 * s, cy + 60 * s), 3, fill=col)

def ic_house(c, cx, cy, s, col=IVORY, roof=CORAL):
    c.poly([(cx - 62 * s, cy - 4 * s), (cx, cy - 58 * s), (cx + 62 * s, cy - 4 * s)], fill=roof)
    c.rrect((cx - 46 * s, cy - 6 * s, cx + 46 * s, cy + 56 * s), 3, fill=col)
    c.rrect((cx - 10 * s, cy + 18 * s, cx + 10 * s, cy + 56 * s), 3, fill=(160, 112, 60))

def ic_building(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 62 * s, cx + 50 * s, cy + 58 * s), 5, fill=(190, 150, 120))
    for r in range(4):
        for q in range(3):
            c.rrect((cx - 36 * s + q * 28 * s, cy - 48 * s + r * 26 * s, cx - 18 * s + q * 28 * s, cy - 32 * s + r * 26 * s), 2, fill=(246, 222, 150) if (r + q) % 2 == 0 else (190, 222, 232))
    c.rrect((cx - 10 * s, cy + 28 * s, cx + 10 * s, cy + 58 * s), 2, fill=(110, 76, 50))

def ic_envelope(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 34 * s, cx + 50 * s, cy + 34 * s), 5 * s, fill=IVORY, outline=(206, 200, 186), width=3)
    c.line([(cx - 48 * s, cy - 32 * s), (cx, cy + 6 * s), (cx + 48 * s, cy - 32 * s)], (190, 184, 170), 4 * s)

def ic_person(c, cx, cy, s, col=GOLD, head=SKIN):
    c.ell((cx - 20 * s, cy - 50 * s, cx + 20 * s, cy - 10 * s), fill=head)
    c.d.pieslice(c._b((cx - 38 * s, cy - 4 * s, cx + 38 * s, cy + 70 * s)), 180, 360, fill=col)

def ic_x(c, cx, cy, s, col=RED, w=16):
    c.line([(cx - 34 * s, cy - 34 * s), (cx + 34 * s, cy + 34 * s)], col, w * s)
    c.line([(cx + 34 * s, cy - 34 * s), (cx - 34 * s, cy + 34 * s)], col, w * s)

def ic_pin(c, cx, cy, s, col=GOLD):
    c.poly([(cx, cy + 58 * s), (cx - 34 * s, cy - 8 * s), (cx + 34 * s, cy - 8 * s)], fill=col)
    c.ell((cx - 36 * s, cy - 50 * s, cx + 36 * s, cy + 18 * s), fill=col)
    c.ell((cx - 14 * s, cy - 28 * s, cx + 14 * s, cy), fill=GREEN_D)

def ic_coin(c, cx, cy, r):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=GOLD, outline=(168, 118, 40), width=max(2, r * 0.08))
    c.text((cx, cy + 2), "$", FONT_SANS, r * 1.1, GREEN_D)

def ic_warn(c, cx, cy, s):
    warn_tri(c, cx, cy, s * 1.2)

def sprite(key, w, h, fn):
    def mk():
        c = Cv(w, h); fn(c); return c.done()
    return cache(key, mk)

def stamp(text, w, h, col, size=None, fill=PANEL_FILL):
    def mk():
        c = Cv(w, h)
        c.rrect((5, 5, w - 5, h - 5), 20, fill=fill, outline=col, width=8)
        c.rrect((17, 17, w - 17, h - 17), 12, outline=col, width=3)
        c.text((w / 2, h / 2 + 2), text, FONT_SANS, size or h * 0.40, col, track=3)
        return c.done()
    return cache(("stamp4", text, w, h, col, size, fill), mk)

def banner(text, w=1300, h=104, size=50, fill=GOLD, ink=GREEN_D):
    return pill_spr(text, size, w, h, fill, ink, border=(168, 118, 40), track=2)

def panel(w, h, border=SAGE_D, fill=PANEL_FILL):
    def mk():
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 36, fill=fill, outline=border, width=5)
        return c.done()
    return cache(("panel4", w, h, border, fill), mk)

def txt(text, size, col=IVORY, track=0):
    return tspr(text, FONT_SANS, size, col, track=track)

def seq(img, t, t0, spr, cx, cy, scale=1.0, shadow=0, rot=0.0, dur=0.45):
    s, a, p = pop(t, t0, dur)
    if p > 0:
        put(img, spr, cx, cy, scale=scale * s, alpha=a, shadow=shadow, rot=rot)
    return p

def slide_in(img, t, t0, spr, cx, cy, dx=0, dy=0, dur=0.5, shadow=0, scale=1.0, rot=0.0):
    p = ease(seg(t, t0, dur))
    if p > 0:
        put(img, spr, cx + dx * (1 - p), cy + dy * (1 - p), alpha=min(1, p * 2.5), shadow=shadow, scale=scale, rot=rot)
    return p

def ban(img, t, t0, text, cy=975, cx=960, **kw):
    p = ease(seg(t, t0, 0.4))
    if p > 0:
        put(img, banner(text, **kw), cx, cy + 18 * (1 - p), alpha=p, shadow=10)

# ============================================================ BLOCCO 1
def bill_paper():
    def fn(c):
        w, h = 400, 500
        c.rrect((6, 6, w - 6, h - 6), 24, fill=IVORY, outline=(206, 200, 186), width=5)
        c.rrect((6, 6, w - 6, 96), 24, fill=GREEN_L)
        c.d.rectangle(c._b((6, 60, w - 6, 96)), fill=GREEN_L)
        c.text((w / 2, 52), "UTILITY BILL", FONT_SANS, 40, IVORY, track=4)
        for k in range(4):
            c.rrect((40, 130 + k * 44, 40 + (300 if k % 2 == 0 else 220), 146 + k * 44), 8, fill=(206, 212, 206))
        c.text((w / 2, 360), "AMOUNT DUE", FONT_SANS_M, 26, GREEN_D, track=4)
        c.text((w / 2, 430), "$ $ $", FONT_SANS, 70, CORAL_D, track=14)
    return sprite("bill4", 400, 500, fn)

def mailbox():
    def fn(c):
        c.rrect((150, 250, 230, 450), 8, fill=(122, 88, 54))
        for k, dx in enumerate((-60, 0, 62)):
            c.rrect((84 + dx + 40, 40 + k * 10, 196 + dx + 40, 130 + k * 10), 8, fill=IVORY, outline=(206, 200, 186), width=3)
            c.line([(90 + dx + 40, 46 + k * 10), (140 + dx + 40, 90 + k * 10), (190 + dx + 40, 46 + k * 10)], (190, 184, 170), 4)
        c.rrect((20, 120, 360, 300), 80, fill=(70, 120, 176), outline=(36, 76, 128), width=6)
        c.rrect((20, 200, 360, 300), 20, fill=(70, 120, 176))
        c.rrect((300, 150, 332, 240), 6, fill=RED)
        c.rrect((120, 190, 260, 232), 10, fill=(36, 76, 128))
    return sprite("mailbox4", 380, 460, fn)

def draw1(img, t):
    ts = starts(1)
    common(img, t, "A BILL YOU PAY IN FULL")
    # 1 cassetta delle lettere (a sinistra)
    p = slide_in(img, t, ts[0], mailbox(), 330, 470, dx=-110, dur=0.6, shadow=16, scale=1.05)
    seq(img, t, ts[0] + 0.5, txt("YOUR MAIL", 40, SAGE, 4), 330, 770)
    # 2 la bolletta pagata per intero
    p = slide_in(img, t, ts[1], bill_paper(), 960, 460, dy=-110, dur=0.6, shadow=18, scale=1.0)
    s, a, pp = pop(t, ts[1] + 0.9, 0.45)
    if pp > 0:
        put(img, stamp("PAID IN FULL", 460, 120, RED), 990, 560, scale=s, alpha=a, rot=-9, shadow=12)
        burst(img, t, ts[1] + 0.9, 990, 560, n=12, color=RED, rad=240, seed=3)
    # 3 il programma statale che aiuta a pagarla
    slide_in(img, t, ts[2], panel(500, 560, border=GOLD), 1590, 470, dx=60, dur=0.6, shadow=16)
    seq(img, t, ts[2] + 0.35, sprite("gov4", 220, 190, lambda c: ic_gov(c, 110, 95, 1.4)), 1590, 380, shadow=8)
    seq(img, t, ts[2] + 0.7, txt("A PROGRAM IN", 40, IVORY, 2), 1590, 520)
    seq(img, t, ts[2] + 0.85, txt("YOUR STATE", 56, GOLD, 3), 1590, 590)
    p3 = ease(seg(t, ts[2] + 1.6, 0.5))
    if p3 > 0:
        put(img, sprite("arrow4", 160, 120, lambda c: c.poly([(6, 38), (92, 38), (92, 8), (154, 60), (92, 112), (92, 82), (6, 82)], fill=GOLD)), 1250 - 20 * (1 - p3), 470, alpha=p3, rot=180)
    seq(img, t, ts[2] + 1.9, txt("HELPS YOU PAY IT", 36, SAGE, 3), 1590, 670)
    # 4-5 nessuno ti chiama
    s, a, pp = pop(t, ts[3], 0.45)
    if pp > 0:
        put(img, sprite("phone4", 220, 220, lambda c: (ic_phone(c, 110, 110, 1.4), ic_x(c, 150, 150, 1.5))), 330, 925, scale=0.85 * s, alpha=a)
    ban(img, t, ts[4], "NOBODY IS GOING TO CALL AND TELL YOU", cy=925, cx=1090, w=1180)

# ============================================================ BLOCCO 2
def tile2(i, fn, name, hl=False):
    def mk():
        w, h = 228, 390
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 30, fill=PANEL_FILL if not hl else (40, 70, 52), outline=GOLD if hl else SAGE_D, width=9 if hl else 5)
        c.ell((w / 2 - 34, 22, w / 2 + 34, 90), fill=GOLD, outline=(168, 118, 40), width=4)
        c.text((w / 2, 58), str(i), FONT_SERIF, 54, GREEN_D)
        fn(c, w / 2, 205, 1.05)
        c.text((w / 2, 335), name, FONT_SANS, 31, GOLD if hl else IVORY, track=1)
        return c.done()
    return cache(("tile2", i, name, hl), mk)

BILLS = [(1, ic_flame, "HEATING"), (2, ic_bolt, "ENERGY"), (3, ic_phone, "PHONE"), (4, ic_bag, "GROCERIES"),
         (5, lambda c, x, y, s: ic_bag(c, x, y, s), "FOOD BOX"), (6, ic_bus, "THE BUS"), (7, ic_repair, "REPAIRS")]

def tile_xy(i):
    return 192 + 256 * i, 560      # i = 0..6

def draw2(img, t):
    ts = starts(2)
    common(img, t, "SEVEN BILLS")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, stamp("7 BILLS", 520, 130, GOLD, size=70), 960, 215, scale=s, alpha=a, shadow=12)
        burst(img, t, ts[0], 960, 215, n=12, color=GOLD, rad=260, seed=4)
    # tessere una per parola: 1 heating (ts1), 2 energy (ts2), 3 phone (ts3), 4 groceries (ts4), 5 food box (ts4+), 6 bus (ts5), 7 repairs (ts6)
    st = [ts[1], ts[2], ts[3], ts[4], ts[4] + 0.55, ts[5], ts[6]]
    for i, (n, fn, name) in enumerate(BILLS):
        hl = (i == 6 and t > ts[7] + 0.1)
        x, y = tile_xy(i)
        s, a, p = pop(t, st[i], 0.45)
        if p > 0:
            put(img, tile2(n, fn, name, hl), x, y, scale=s * (1.06 if hl else 1.0), alpha=a, shadow=10)
            if i == 6 and p < 1:
                burst(img, t, st[i], x, y, n=10, color=GOLD, rad=200, seed=7)
    ban(img, t, ts[7] + 0.1, "THE BIGGEST ONE IS NUMBER SEVEN", cy=930, w=1200)
    seq(img, t, ts[7] + 0.2, sprite("crown4", 120, 90, lambda c: (c.poly([(8, 76), (8, 22), (38, 52), (60, 8), (82, 52), (112, 22), (112, 76)], fill=GOLD), c.rrect((8, 70, 112, 86), 6, fill=(168, 118, 40)))), tile_xy(6)[0], 330, scale=0.9)

# ============================================================ BLOCCO 3
def bubble3(lines, col, icon, w=760, h=560):
    def mk():
        c = Cv(w, h)
        c.rrect((6, 6, w - 6, h - 46), 44, fill=PANEL_FILL, outline=col, width=7)
        c.poly([(110, h - 50), (190, h - 50), (96, h - 4)], fill=PANEL_FILL)
        c.line([(110, h - 48), (96, h - 4), (190, h - 48)], col, 7)
        icon(c, w / 2, 150, 1.6)
        for k, ln in enumerate(lines):
            c.text((w / 2, 300 + k * 58), ln, FONT_SANS, 44, IVORY if k < len(lines) - 1 else col, track=1)
        return c.done()
    return cache(("bub3", tuple(lines), col), mk)

def draw3(img, t):
    ts = starts(3)
    common(img, t, "TWO WRONG IDEAS")
    slide_in(img, t, ts[0], bubble3(["THIS IS ONLY FOR", "PEOPLE WHO", "REALLY STRUGGLE"], SAGE, lambda c, x, y, s: ic_person(c, x, y + 30, s * 1.1, col=SAGE_D)), 520, 470, dx=-100, dur=0.6, shadow=14)
    slide_in(img, t, ts[1], bubble3(["I OWN MY HOME,", "SO THIS ISN'T", "FOR ME"], GOLD, lambda c, x, y, s: ic_house(c, x, y + 20, s * 1.2)), 1400, 470, dx=100, dur=0.6, shadow=14)
    # entrambi sbagliati
    s, a, p = pop(t, ts[2], 0.45)
    if p > 0:
        put(img, sprite("bigx3", 300, 300, lambda c: ic_x(c, 150, 150, 3.4, RED, 16)), 520, 340, scale=0.5 * s, alpha=a)
    s, a, p = pop(t, ts[2] + 0.35, 0.45)
    if p > 0:
        put(img, sprite("bigx3", 300, 300, lambda c: ic_x(c, 150, 150, 3.4, RED, 16)), 1400, 340, scale=0.5 * s, alpha=a)
    s, a, p = pop(t, ts[2] + 0.7, 0.5)
    if p > 0:
        put(img, stamp("BOTH GROUPS ARE WRONG", 880, 130, RED, size=52), 960, 835, scale=s, alpha=a, rot=-2, shadow=14)
        burst(img, t, ts[2] + 0.7, 960, 835, n=14, color=RED, rad=200, seed=8)
    ban(img, t, ts[3] + 0.1, "I'LL SHOW WHO EACH ONE HELPS MOST", cy=985, w=1240)

# ============================================================ BLOCCO 4
def apt():
    def fn(c):
        ic_building(c, 160, 190, 2.5)
        c.rrect((60, 330, 260, 380), 14, fill=GOLD)
        c.text((160, 356), "FOR RENT", FONT_SANS, 28, GREEN_D, track=2)
    return sprite("apt4", 320, 400, fn)

def dot7(on, label=None):
    def mk():
        w, h = 200, 230
        c = Cv(w, h)
        c.ell((20, 10, 180, 170), fill=GOLD if on else (24, 60, 48), outline=(168, 118, 40) if on else SAGE_D, width=6)
        if on:
            check_ic(c, 100, 92, 2.2, GREEN_D)
        else:
            ic_house(c, 100, 88, 1.0, col=SAGE_D, roof=SAGE_D)
        if label:
            c.text((w / 2, 205), label, FONT_SANS, 26, SAGE, track=1)
        return c.done()
    return cache(("dot7", on, label), mk)

def draw4(img, t):
    ts = starts(4)
    common(img, t, "IF YOU RENT")
    slide_in(img, t, ts[0], apt(), 330, 470, dx=-110, dur=0.6, shadow=16, scale=1.0)
    seq(img, t, ts[0] + 0.5, txt("DON'T CLICK AWAY", 44, GOLD, 3), 330, 740)
    # sei su sette
    seq(img, t, ts[1], txt("6 OF 7", 150, GOLD, 4), 1190, 250, shadow=10)
    for i in range(7):
        s, a, p = pop(t, ts[1] + 0.4 + i * 0.16, 0.35)
        if p > 0:
            on = i < 6
            put(img, dot7(on, "OWNERS ONLY" if i == 6 else None), 760 + i * 150, 470, scale=0.7 * s, alpha=a)
    seq(img, t, ts[1] + 1.9, txt("WORK FOR RENTERS TOO", 44, IVORY, 3), 1190, 640)
    # riscaldare costa meno
    p = ease(seg(t, ts[2], 0.5))
    if p > 0:
        put(img, sprite("heatdown4", 300, 220, lambda c: (ic_flame(c, 90, 112, 1.3), c.rrect((196, 30, 236, 110), 6, fill=GOLD), c.poly([(176, 104), (256, 104), (216, 170)], fill=GOLD))), 480, 900, alpha=p)
    ban(img, t, ts[2] + 0.2, "CHEAPER TO HEAT FOR YEARS", cy=900, cx=1240, w=1000)
    # (il banner e' a destra del fuoco)

# ============================================================ BLOCCO 5
def link_chain(c, x0, y, n, col=GOLD):
    for k in range(n):
        c.rrect((x0 + k * 38, y - 14, x0 + k * 38 + 52, y + 14), 14, outline=col, width=7)

def draw5(img, t):
    ts = starts(5)
    common(img, t, "STAY TO THE END")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, stamp("STAY TO THE END", 800, 130, GOLD, size=62), 960, 215, scale=s, alpha=a, shadow=14)
    # quattro bollette collegate da una catena
    icons = [(ic_flame, 420), (ic_bolt, 760), (ic_phone, 1100), (ic_bag, 1440)]
    p = ease(seg(t, ts[1], 0.5))
    if p > 0:
        put(img, sprite("chain5", 1200, 60, lambda c: link_chain(c, 40, 30, 29)), 960, 480, alpha=p)
    for k, (fn, x) in enumerate(icons):
        s, a, pp = pop(t, ts[1] + 0.2 + k * 0.25, 0.45)
        if pp > 0:
            put(img, sprite(("ic5", k), 220, 220, lambda c, fn=fn: (c.ell((6, 6, 214, 214), fill=PANEL_FILL, outline=SAGE_D, width=6), fn(c, 110, 108, 1.1))), x, 480, scale=s, alpha=a, shadow=10)
    # ordine sbagliato: tre numeri mescolati
    seq(img, t, ts[2], txt("WRONG ORDER", 54, RED, 4), 560, 700, shadow=8)
    for k, (n, x) in enumerate(((3, 400), (1, 560), (2, 720))):
        s, a, pp = pop(t, ts[2] + 0.25 + k * 0.2, 0.4)
        if pp > 0:
            put(img, sprite(("n5", n, "r"), 120, 120, lambda c, n=n: (c.ell((6, 6, 114, 114), fill=(70, 38, 36), outline=RED, width=6), c.text((60, 64), str(n), FONT_SERIF, 64, IVORY))), x, 790, scale=s, alpha=a)
    # aiuto perso
    seq(img, t, ts[3], stamp("HELP MISSED", 440, 110, RED, size=44), 1280, 700, rot=-3, shadow=10)
    # ordine giusto con lucchetto
    s, a, p = pop(t, ts[4], 0.5)
    if p > 0:
        put(img, sprite("lock5", 150, 170, lambda c: (c.d.arc(c._b((38, 8, 112, 90)), 180, 360, fill=GOLD, width=22), c.rrect((20, 70, 130, 160), 16, fill=GOLD), c.ell((62, 96, 88, 122), fill=GREEN_D), c.rrect((70, 112, 80, 140), 3, fill=GREEN_D))), 1330, 960, scale=0.85 * s, alpha=a, shadow=10)
        put(img, banner("THE RIGHT ORDER: AT THE END", w=900, size=42, h=96), 790, 960, scale=s, alpha=a, shadow=10)

# ============================================================ BLOCCO 6
def draw6(img, t):
    ts = starts(6)
    common(img, t, "OFFICIAL SOURCES ONLY")
    seq(img, t, ts[0], txt("BEFORE WE START", 70, IVORY, 4), 960, 190, shadow=8)
    # pagina .gov con spunta
    slide_in(img, t, ts[1], browser_gov(), 560, 520, dx=-110, dur=0.6, shadow=18)
    s, a, p = pop(t, ts[1] + 1.2, 0.4)
    if p > 0:
        put(img, check_spr(), 960, 360, scale=1.4 * s, alpha=a)
        burst(img, t, ts[1] + 1.2, 960, 360, n=10, rad=150, seed=11)
    # niente supposizioni, niente voci
    seq(img, t, ts[2], stamp("NO GUESSES", 400, 100, SAGE, size=42), 1450, 340, rot=-2, shadow=8)
    seq(img, t, ts[2] + 0.4, stamp("NO RUMORS", 400, 100, SAGE, size=42), 1450, 470, rot=2, shadow=8)
    for k, y in enumerate((340, 470)):
        s, a, p = pop(t, ts[2] + 0.9 + k * 0.2, 0.35)
        if p > 0:
            put(img, sprite("xs6", 120, 120, lambda c: ic_x(c, 60, 60, 1.2, RED, 14)), 1710, y, scale=s, alpha=a)
    # le regole cambiano per stato
    seq(img, t, ts[3], sprite("pins6", 420, 200, lambda c: [ic_pin(c, 70 + k * 140, 100, 1.0, col=[GOLD, SAGE, CORAL][k]) for k in range(3)]), 1450, 650, shadow=8)
    seq(img, t, ts[3] + 0.5, txt("RULES CHANGE BY STATE", 36, IVORY, 2), 1450, 760)
    # dove controllare
    ban(img, t, ts[4] + 0.1, "I'LL ALWAYS TELL YOU WHERE TO CHECK", cy=960, w=1260)

def browser_gov():
    def fn(c):
        w, h = 860, 560
        c.rrect((3, 3, w - 3, h - 3), 30, fill=IVORY, outline=SAGE_D, width=5)
        c.rrect((3, 3, w - 3, 78), 30, fill=(214, 224, 214))
        c.d.rectangle(c._b((3, 40, w - 3, 78)), fill=(214, 224, 214))
        for i, col in enumerate((RED, GOLD, (110, 190, 130))):
            c.ell((30 + i * 36, 28, 52 + i * 36, 50), fill=col)
        c.rrect((170, 18, w - 40, 62), 22, fill=IVORY)
        c.text((200, 41), "OFFICIAL .GOV PAGE", FONT_SANS_M, 28, GREEN_D, anchor="lm", track=2)
        c.d.rectangle(c._b((3, 78, w - 3, 170)), fill=GREEN_D)
        ic_gov(c, 90, 126, 0.6, GOLD)
        c.text((150, 126), "U.S. GOVERNMENT", FONT_SANS, 40, IVORY, anchor="lm", track=3)
        for i, ww in enumerate((620, 520, 580, 440, 560)):
            c.rrect((46, 210 + i * 44, 46 + ww, 228 + i * 44), 9, fill=(206, 214, 206))
        c.rrect((w - 250, 440, w - 40, 520), 14, fill=GOLD)
        c.text((w - 145, 481), "OFFICIAL", FONT_SANS, 32, GREEN_D, track=2)
    return sprite("browsergov", 860, 560, fn)

# ============================================================ BLOCCO 7
def numbadge(n, S=260):
    def fn(c):
        c.ell((6, 6, S - 6, S - 6), fill=GOLD, outline=(168, 118, 40), width=10)
        c.ell((26, 26, S - 26, S - 26), outline=(168, 118, 40), width=4)
        c.text((S / 2, S / 2 + 6), str(n), FONT_SERIF, S * 0.62, GREEN_D)
    return sprite(("numbadge4", n, S), S, S, fn)

def draw7(img, t):
    ts = starts(7)
    common(img, t, "BILL NUMBER ONE")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, numbadge(1, 400), 360, 330, scale=s, alpha=a, shadow=18)
        burst(img, t, ts[0], 360, 330, n=14, color=GOLD, rad=300, seed=12)
    # titolo e fuoco
    seq(img, t, ts[1], panel(1080, 400, border=FLAME), 1230, 330, shadow=14)
    seq(img, t, ts[1] + 0.2, sprite("flame7", 340, 360, lambda c: ic_flame(c, 170, 180, 2.6)), 860, 330)
    seq(img, t, ts[1] + 0.4, txt("YOUR", 64, SAGE, 5), 1350, 250)
    seq(img, t, ts[1] + 0.55, txt("HEATING BILL", 92, IVORY, 3), 1350, 360)
    # orologio che gira
    p = ease(seg(t, ts[2], 0.5))
    ang = min(t - ts[2], 2.0) * 1.6
    if p > 0:
        cv = Cv(340, 340); ic_clock(cv, 170, 170, 150, ang)
        put(img, cv.done(), 360, 800, alpha=p, shadow=12)
    ban(img, t, ts[2] + 0.4, "THE CLOCK IS ALREADY RUNNING", cy=800, cx=1230, w=1180, size=54)

# ============================================================ BLOCCO 8
def card8(icon, top, bottom, col, w=520, h=420):
    def mk():
        c = Cv(w, h)
        c.rrect((5, 5, w - 5, h - 5), 36, fill=PANEL_FILL, outline=col, width=7)
        icon(c, w / 2, 150, 1.5)
        c.text((w / 2, 292), top, FONT_SANS, 44, col, track=3)
        c.text((w / 2, 350), bottom, FONT_SANS, 34, IVORY, track=1)
        return c.done()
    return cache(("card8", top, bottom), mk)

def draw8(img, t):
    ts = starts(8)
    common(img, t, "THE PROGRAM")
    # LIHEAP lettera per lettera
    for k, ch in enumerate("LIHEAP"):
        s, a, p = pop(t, ts[0] + 0.1 + k * 0.28, 0.4)
        if p > 0:
            put(img, tspr(ch, FONT_SERIF, 210, GOLD), 600 + k * 135, 250, scale=s, alpha=a, shadow=12)
    seq(img, t, ts[1], txt("LOW INCOME HOME ENERGY ASSISTANCE PROGRAM", 44, IVORY, 2), 960, 420, shadow=6)
    p = seq(img, t, ts[1] + 0.5, stamp("FEDERAL PROGRAM", 460, 90, SAGE, size=38), 960, 505, shadow=6)
    slide_in(img, t, ts[2], card8(lambda c, x, y, s: (ic_snow(c, x - 70, y, 0.9), ic_flame(c, x + 60, y, 0.8)), "WINTER", "PAYS HEATING", FLAME), 360, 790, dy=50, dur=0.55, shadow=14, scale=0.9)
    slide_in(img, t, ts[3], card8(lambda c, x, y, s: ic_sun(c, x, y, 1.1), "SUMMER", "PAYS COOLING", GOLD), 960, 790, dy=50, dur=0.55, shadow=14, scale=0.9)
    slide_in(img, t, ts[4], card8(lambda c, x, y, s: ic_notice(c, x, y, 1.2), "EMERGENCY", "SHUTOFF NOTICE", RED), 1560, 790, dy=50, dur=0.55, shadow=14, scale=0.9)

# ============================================================ BLOCCO 9
def person_q(col, ring=None):
    def fn(c):
        if ring:
            c.ell((4, 4, 156, 156), outline=ring, width=9)
        ic_person(c, 80, 84, 1.3, col=col)
    return sprite(("pq9", col, ring), 160, 170, fn)

def star_spr():
    def fn(c):
        pts = []
        for i in range(10):
            a = -math.pi / 2 + math.pi * i / 5
            r = 60 if i % 2 == 0 else 26
            pts.append((70 + r * math.cos(a), 70 + r * math.sin(a)))
        c.poly(pts, fill=GOLD)
    return sprite("star9", 140, 140, fn)

def draw9(img, t):
    ts = starts(9)
    common(img, t, "ALMOST NOBODY KNOWS")
    seq(img, t, ts[0], txt("ALMOST NOBODY KNOWS THIS", 66, IVORY, 3), 960, 190, shadow=8)
    # una casa con un anziano dentro = priorita
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, sprite("homesr9", 400, 340, lambda c: (ic_house(c, 200, 160, 2.6, col=IVORY), c.ell((150, 140, 250, 240), fill=GREEN_L), ic_person(c, 200, 230, 1.0, col=GOLD))), 440, 490, scale=1.3 * s, alpha=a, shadow=14)
    seq(img, t, ts[1] + 0.8, stamp("PRIORITY", 520, 130, GOLD, size=66), 1100, 380, rot=-3, shadow=12)
    seq(img, t, ts[1] + 1.2, txt("OLDER ADULT AT HOME", 50, SAGE, 3), 1100, 500)
    # la coda: 8 persone, il senior parte dietro e va avanti
    p_q = ease(seg(t, ts[2], 0.6))
    xs = [260 + k * 200 for k in range(8)]
    if p_q > 0:
        put(img, sprite("lane9", 1700, 8, lambda c: c.rrect((0, 0, 1700, 8), 4, fill=SAGE_D)), 960, 895, alpha=p_q)
    for k, x in enumerate(xs[:7]):
        s, a, p = pop(t, ts[2] + 0.15 + k * 0.07, 0.35)
        if p > 0:
            put(img, person_q(SAGE_D), x, 800, scale=1.0 * s, alpha=a * 0.9)
    # il senior: dietro, poi davanti
    mv = ease(seg(t, ts[3], 0.7))
    sx = xs[7] + (xs[0] - 90 - xs[7]) * mv if t >= ts[3] else xs[7]
    s, a, p = pop(t, ts[2] + 0.7, 0.4)
    if p > 0:
        put(img, person_q(GOLD, ring=GOLD), sx, 795, scale=1.2 * s, alpha=a, shadow=8)
    if t < ts[3]:
        seq(img, t, ts[2] + 1.0, txt("NOT HERE", 38, SAGE, 3), xs[7], 945)
    s, a, p = pop(t, ts[3] + 0.6, 0.4)
    if p > 0:
        put(img, star_spr(), xs[0] - 90, 660, scale=0.9 * s, alpha=a)
    ban(img, t, ts[3] + 0.1, "YOU ARE NEAR THE FRONT", cy=985, w=900, h=90, size=46)

# ============================================================ BLOCCO 10
def fund_bar(frac, w=620, h=120):
    def mk():
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 30, fill=(20, 52, 42), outline=GOLD, width=6)
        iw = int((w - 28) * max(0.0, min(1.0, frac)))
        if iw > 4:
            c.rrect((14, 14, 14 + iw, h - 14), 18, fill=GOLD if frac > 0.25 else RED)
        return c.done()
    return cache(("fund10", round(frac, 2), w, h), mk)

def draw10(img, t):
    ts = starts(10)
    common(img, t, "THE CATCH")
    s, a, p = pop(t, ts[0], 0.45)
    if p > 0:
        put(img, sprite("warn10", 200, 190, lambda c: warn_tri(c, 100, 100, 1.5)), 400, 250, scale=s, alpha=a)
    seq(img, t, ts[0] + 0.3, txt("THE CATCH", 90, GOLD, 4), 840, 250, shadow=10)
    # soldi limitati: barra piena
    seq(img, t, ts[1], panel(1100, 380, border=GOLD), 960, 580, shadow=14)
    seq(img, t, ts[1] + 0.2, txt("THE MONEY IS LIMITED", 54, IVORY, 3), 960, 460)
    fill_p = ease(seg(t, ts[2] + 0.3, 0.7))
    drain = ease(seg(t, ts[3], 1.5))
    frac = fill_p * (1 - drain)
    if fill_p > 0:
        put(img, fund_bar(frac), 960, 600, alpha=1.0)
    if t >= ts[2]:
        seq(img, t, ts[2], txt("EACH STATE: A SET AMOUNT", 40, SAGE, 3), 960, 700)
    if t >= ts[3] + 1.2:
        s, a, p = pop(t, ts[3] + 1.2, 0.4)
        put(img, stamp("RUNS OUT", 300, 90, RED, size=40), 1690, 590, scale=s, alpha=a, rot=-5, shadow=8)
    # ufficio chiuso
    slide_in(img, t, ts[4], sprite("office10", 300, 280, lambda c: (ic_gov(c, 150, 120, 1.8), c.rrect((90, 218, 210, 262), 10, fill=RED), c.text((150, 241), "CLOSED", FONT_SANS, 26, IVORY, track=2))), 260, 835, dx=-100, dur=0.5, shadow=10, scale=0.85)
    ban(img, t, ts[4] + 0.4, "SOME OFFICES STOP TAKING APPLICATIONS", cy=950, cx=1170, w=1200)

DRAW = {1: draw1, 2: draw2, 3: draw3, 4: draw4, 5: draw5, 6: draw6, 7: draw7, 8: draw8, 9: draw9, 10: draw10}

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
