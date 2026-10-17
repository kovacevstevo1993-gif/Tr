"""Video lungo 6 (AMTRAK) - blocco 1 (gancio). 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AMTRAK.md.
Durata dalla timeline dell'utente (16/10/2026): B1 574 fotogrammi (19 s + 4 f).
Layout NUOVO rispetto ai primi blocchi dei video precedenti: schermo diviso in due (due viaggiatori a confronto), stessa grafica.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long6_b01.py <blocco> [fotogrammi]
     python3 long6_b01.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b01_10 import *      # 1920x1080, motore, sprite comuni, banner, txt, seq, slide_in, panel, sprite, pill_spr, common

DUR = {1: 574}
PHRASES = {
    1: ["Two people over sixty five ride", "the same Amtrak train,", "on the same day,", "in the same kind of seat.",
        "One of them paid less,", "never lifted a suitcase,", "and knew how to cancel without losing money.",
        "The other one paid full price", "and carried every bag alone.", "The only difference?", "One of them asked."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

GREEN_OK = (110, 200, 130)
SEAT = (84, 112, 150)
SEAT_L = (112, 142, 180)
PW, PH = 800, 700           # pannelli
LCX, RCX, PCY = 500, 1420, 490

# ------------------------------------------------------------------ ritratti (stesso stile del nonno del video Costco)
def portrait(kind, mood):
    def mk():
        S = 320
        c = Cv(S, S)
        shirt = (190, 140, 66) if kind == "man" else (118, 150, 206)
        c.ell((4, 4, S - 4, S - 4), fill=GREEN_L)
        c.ell((40, 215, 280, 420), fill=shirt)
        c.poly([(125, 222), (160, 268), (195, 222)], fill=IVORY)
        c.rrect((146, 190, 174, 236), 10, fill=SKIN)
        c.ell((106, 78, 214, 206), fill=SKIN)
        c.ell((98, 128, 114, 164), fill=SKIN); c.ell((206, 128, 222, 164), fill=SKIN)
        if kind == "woman":
            c.d.pieslice(c._b((98, 62, 222, 190)), 180, 360, fill=HAIR)
            c.ell((98, 98, 122, 150), fill=HAIR); c.ell((198, 98, 222, 150), fill=HAIR)
            c.ell((118, 70, 202, 112), fill=HAIR)
            c.ell((128, 40, 192, 98), fill=HAIR)
            c.ell((124, 100, 196, 124), fill=SKIN)
        else:
            c.ell((96, 104, 120, 154), fill=HAIR); c.ell((200, 104, 224, 154), fill=HAIR)
            c.arc((108, 74, 212, 150), 200, 340, HAIR, 7)
        c.line([(130, 118), (150, 114)], HAIR, 5); c.line([(170, 114), (190, 118)], HAIR, 5)
        c.ell((131, 132, 149, 150), fill=(255, 255, 255)); c.ell((171, 132, 189, 150), fill=(255, 255, 255))
        c.ell((137, 137, 145, 147), fill=GREEN_D); c.ell((177, 137, 185, 147), fill=GREEN_D)
        c.ell((124, 124, 156, 158), outline=GREEN_D, width=5); c.ell((164, 124, 196, 158), outline=GREEN_D, width=5)
        c.line([(156, 138), (164, 138)], GREEN_D, 5)
        mc = (160, 80, 70)
        if kind == "man":
            c.poly([(160, 160), (132, 158), (124, 170), (146, 172), (160, 166), (174, 172), (196, 170), (188, 158)], fill=HAIR)
        if mood == "happy":
            c.arc((136, 150, 184, 190), 20, 160, mc, 5)
        elif mood == "sad":
            c.arc((136, 170, 184, 210), 200, 340, mc, 5)
            c.ell((204, 100, 218, 124), fill=ICE)       # goccia di sudore
        else:
            c.line([(144, 174), (176, 174)], mc, 5)
        im = c.done()
        mask = Image.new("L", (S * 2, S * 2), 0)
        ImageDraw.Draw(mask).ellipse((8, 8, S * 2 - 8, S * 2 - 8), fill=255)
        mask = mask.resize((S, S), Image.LANCZOS)
        im.putalpha(ImageChops.multiply(im.getchannel("A"), mask))
        ring = Cv(S, S)
        ring.ell((5, 5, S - 5, S - 5), outline=GOLD, width=12)
        ring.ell((16, 16, S - 16, S - 16), outline=GREEN_D, width=3)
        r = ring.done()
        im.paste(r, (0, 0), r)
        return im
    return cache(("portrait6", kind, mood), mk)

def chip65():
    def fn(c):
        c.ell((4, 4, 116, 116), fill=IVORY, outline=GOLD, width=7)
        c.text((60, 62), "65+", FONT_SANS, 46, GREEN_D)
    return sprite("chip65_6", 120, 120, fn)

def seat():
    def fn(c):
        c.rrect((20, 20, 280, 420), 60, fill=SEAT, outline=(60, 84, 120), width=5)
        c.rrect((54, 36, 246, 150), 40, fill=SEAT_L)
        c.rrect((2, 250, 40, 380), 16, fill=(60, 84, 120))
        c.rrect((260, 250, 298, 380), 16, fill=(60, 84, 120))
    return sprite("seat6", 300, 440, fn)

def window():
    def fn(c):
        w, h = 720, 150
        c.rrect((4, 4, w - 4, h - 4), 30, fill=(150, 205, 232), outline=(170, 190, 180), width=10)
        c.ell((560, 24, 626, 90), fill=GOLD)
        c.poly([(14, 138), (14, 96), (120, 56), (230, 100), (330, 70), (430, 104), (520, 80), (706, 118), (706, 138)], fill=(90, 160, 110))
        c.poly([(14, 138), (14, 118), (160, 96), (300, 122), (460, 100), (706, 130), (706, 138)], fill=(60, 130, 90))
        c.line([(360, 8), (360, 142)], (170, 190, 180), 8)
    return sprite("window6", 720, 150, fn)

def frame_only(col):
    def fn(c):
        c.rrect((4, 4, PW - 4, PH - 4), 36, outline=col, width=10)
    return sprite(("frame6", col), PW, PH, fn)

# ------------------------------------------------------------------ icone delle righe
def ic_tag(c, cx, cy, s, col, up):
    c.poly([(cx - 44 * s, cy - 36 * s), (cx + 14 * s, cy - 36 * s), (cx + 50 * s, cy), (cx + 14 * s, cy + 36 * s), (cx - 44 * s, cy + 36 * s)], fill=col)
    c.ell((cx - 36 * s, cy - 7 * s, cx - 22 * s, cy + 7 * s), fill=(18, 66, 52))
    c.text((cx + 2 * s, cy + 2 * s), "$", FONT_SANS, 40 * s, GREEN_D)
    ay = cy - 48 * s if up else cy + 48 * s
    d = -1 if up else 1
    c.poly([(cx + 30 * s, ay - d * 16 * s), (cx + 52 * s, ay + d * 12 * s), (cx + 8 * s, ay + d * 12 * s)], fill=col)

def ic_suitcase(c, cx, cy, s):
    c.rrect((cx - 30 * s, cy - 56 * s, cx + 30 * s, cy - 36 * s), 8 * s, outline=(214, 164, 96), width=8 * s)
    c.rrect((cx - 44 * s, cy - 40 * s, cx + 44 * s, cy + 40 * s), 12 * s, fill=(214, 164, 96), outline=(160, 112, 60), width=4)
    c.rrect((cx - 24 * s, cy - 40 * s, cx - 14 * s, cy + 40 * s), 2, fill=(160, 112, 60))
    c.rrect((cx + 14 * s, cy - 40 * s, cx + 24 * s, cy + 40 * s), 2, fill=(160, 112, 60))
    c.ell((cx + 22 * s, cy + 14 * s, cx + 74 * s, cy + 66 * s), fill=GREEN_OK, outline=GREEN_D, width=3)
    check_ic(c, cx + 48 * s, cy + 40 * s, 0.55 * s, GREEN_D)

def ic_refund6(c, cx, cy, s):
    ic_coin(c, cx, cy, 30 * s)
    c.arc((cx - 52 * s, cy - 52 * s, cx + 52 * s, cy + 52 * s), 40, 320, GREEN_OK, 9 * s)
    ex, ey = cx + 52 * s * math.cos(math.radians(320)), cy + 52 * s * math.sin(math.radians(320))
    c.poly([(ex - 14 * s, ey - 4 * s), (ex + 20 * s, ey - 8 * s), (ex + 6 * s, ey + 22 * s)], fill=GREEN_OK)

def ic_bags(c, cx, cy, s):
    for dx, dy, k in ((-40, 12, 0.62), (4, 0, 0.7), (46, 14, 0.6)):
        ic_bag(c, cx + dx * s, cy + dy * s, k * s)

def row(key, icon, l1, l2, col):
    def fn(c):
        w, h = 470, 128
        c.rrect((4, 4, w - 4, h - 4), 30, fill=(18, 66, 52), outline=col, width=6)
        icon(c, 66, h / 2)
        if l2:
            c.text((132, 42), l1, FONT_SANS, 38, IVORY, anchor="lm", track=1)
            c.text((132, 88), l2, FONT_SANS, 38, col, anchor="lm", track=1)
        else:
            c.text((132, h / 2 + 2), l1, FONT_SANS, 52, col, anchor="lm", track=1)
    return sprite(("row6", key), 470, 128, fn)

R_L1 = lambda: row("l1", lambda c, x, y: ic_tag(c, x, y - 4, 0.78, GREEN_OK, False), "PAID LESS", "", GREEN_OK)
R_L2 = lambda: row("l2", lambda c, x, y: ic_suitcase(c, x - 8, y + 2, 0.85), "NEVER LIFTED", "A SUITCASE", GREEN_OK)
R_L3 = lambda: row("l3", lambda c, x, y: ic_refund6(c, x, y, 0.95), "CANCELS AND", "KEEPS MONEY", GREEN_OK)
R_R1 = lambda: row("r1", lambda c, x, y: ic_tag(c, x, y + 4, 0.78, CORAL, True), "PAID", "FULL PRICE", CORAL)
R_R2 = lambda: row("r2", lambda c, x, y: ic_bags(c, x + 6, y + 4, 0.5), "EVERY BAG", "CARRIED ALONE", CORAL)

CHIP_W = 330
def chip6(text):
    return pill_spr(text, 38, CHIP_W, 72, IVORY, GREEN_D, border=GOLD, track=2)

def eq_circle(sym, col=GOLD):
    def fn(c):
        c.ell((4, 4, 116, 116), fill=col, outline=IVORY, width=6)
        c.text((60, 62), sym, FONT_SANS, 76, GREEN_D)
    return sprite(("eq6", sym, col), 120, 120, fn)

# ============================================================ BLOCCO 1
def draw1(img, t):
    ts = starts(1)
    common(img, t, "TWO RIDERS, ONE TRAIN")
    # pannelli a sinistra e a destra
    slide_in(img, t, ts[0], panel(PW, PH, border=GREEN_OK), LCX, PCY, dx=-70, dur=0.6, shadow=16)
    slide_in(img, t, ts[0] + 0.15, panel(PW, PH, border=CORAL), RCX, PCY, dx=70, dur=0.6, shadow=16)
    for cx_ in (LCX, RCX):
        seq(img, t, ts[0] + 0.5, window(), cx_, 245, shadow=6, dur=0.5)
    # i due viaggiatori: sedile + ritratto + 65+
    pxL, pxR = LCX - 265, RCX - 265
    for px, kind, key in ((pxL, "man", "L"), (pxR, "woman", "R")):
        seq(img, t, ts[0] + 0.7, seat(), px, 610, shadow=8, scale=0.95, dur=0.5)
        mood = "neutral"
        if key == "L" and t >= ts[4]:
            mood = "happy"
        if key == "R" and t >= ts[7]:
            mood = "sad"
        seq(img, t, ts[0] + 0.85, portrait(kind, mood), px, 590, scale=0.78, shadow=8, dur=0.5)
        seq(img, t, ts[0] + 1.1, chip65(), px + 105, 490, shadow=6, scale=0.85, dur=0.45)
    # etichette in basso: stesso treno, stesso giorno, stesso sedile
    for i, (txt_, k) in enumerate((("SAME TRAIN", 1), ("SAME DAY", 2), ("SAME SEAT", 3))):
        seq(img, t, ts[k], chip6(txt_), 960 + (i - 1) * 370, 905, shadow=6, dur=0.45)
    # cerchio centrale: = poi ?
    if t < ts[9]:
        seq(img, t, ts[3] + 0.4, eq_circle("="), 960, PCY, shadow=10, dur=0.45)
    else:
        s_, a, p = pop(t, ts[9], 0.5)
        put(img, eq_circle("?", CORAL), 960, PCY, scale=s_ * 1.25, alpha=a, shadow=12)
        burst(img, t, ts[9], 960, PCY, n=12, color=GOLD, rad=200, seed=7)
    # righe di sinistra (chi ha chiesto) e di destra
    for k, r_, y in ((4, R_L1, 440), (5, R_L2, 580), (6, R_L3, 720)):
        slide_in(img, t, ts[k], r_(), 650 if False else LCX + 150, y, dx=60, dur=0.5, shadow=8)
    for k, r_, y in ((7, R_R1, 510), (8, R_R2, 650)):
        slide_in(img, t, ts[k], r_(), RCX + 150, y, dx=60, dur=0.5, shadow=8)
    # finale: chi ha chiesto
    p = ease(seg(t, ts[10], 0.5))
    if p > 0:
        put(img, frame_only(GOLD), LCX, PCY, alpha=p)
    ban(img, t, ts[10], "ONE OF THEM ASKED", cy=1010, w=980, h=84, size=46)

DRAW = {1: draw1}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/V6-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
