"""Video lungo 6 (AMTRAK) - blocchi 2-5. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AMTRAK.md.
Durate dalla timeline dell'utente (16/10/2026): B2 551, B3 455, B4 214, B5 279.
Layout diversi dai video precedenti (regola 16/10): treno a 10 vagoni, foglietti + biglietto che perde monete,
scena di lato col binario e i gradini, lucchetti che si aprono.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long6_b02_05.py <blocco> [fotogrammi]
     python3 long6_b02_05.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long6_b01 import *

DUR = {2: 551, 3: 455, 4: 214, 5: 279}
PHRASES = {
    2: ["Today I'll show you ten things Amtrak gives", "riders over sixty five,", "and riders who need a little help,",
        "when they ask.", "One saves you money before you leave home.", "One carries your bags for you.",
        "And number ten is a piece of paper from your doctor", "that can save the whole ticket."],
    3: ["Now, some of you are thinking,", "I don't take the train.", "Others are thinking,",
        "I already know about the senior discount.", "Stay with me.", "Many people who know about the discount",
        "still lose money on the ticket,", "and I'll show you exactly where."],
    4: ["And if you've ever stood on a platform", "with a heavy bag,", "wondering how you'd get it up those steps,",
        "this video is for you."],
    5: ["Stay until the end,", "because there is one sentence", "that unlocks almost all of these.",
        "And most riders only say it", "when it's already too late."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def last_t(b, t0):
    """l'ultimo elemento compare non prima dell'80% del blocco"""
    return max(t0, DUR[b] / FPS * 0.80)

CARD_BG = (18, 66, 52)

def card(key, w, h, border):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 30, fill=CARD_BG, outline=border, width=6)
    return sprite(("card6", key, w, h, border), w, h, fn)

# ============================================================ BLOCCO 2 - treno a 10 vagoni
def loco():
    def fn(c):
        c.rrect((10, 20, 190, 110), 18, fill=GREEN_OK, outline=GREEN_D, width=4)
        c.poly([(10, 110), (10, 46), (40, 20), (60, 20), (60, 110)], fill=(90, 170, 110))
        c.rrect((84, 34, 150, 70), 8, fill=(190, 222, 232))
        c.ell((20, 64, 44, 88), fill=GOLD)
        for x in (60, 140):
            c.ell((x - 18, 98, x + 18, 134), fill=GREEN_D, outline=IVORY, width=3)
    return sprite("loco6", 200, 140, fn)

def car(n, hl=False):
    def fn(c):
        body = GOLD if hl else IVORY
        c.rrect((4, 20, 148, 110), 14, fill=body, outline=GREEN_D, width=4)
        c.rrect((4, 84, 148, 94), 2, fill=GREEN_L if not hl else (168, 118, 40))
        for x in (16, 98):
            c.rrect((x, 32, x + 38, 58), 6, fill=(190, 222, 232))
        c.ell((56, 30, 96, 70), fill=GREEN_D)
        c.text((76, 51), str(n), FONT_SANS, 26 if n < 10 else 22, GOLD if not hl else IVORY)
        for x in (36, 116):
            c.ell((x - 16, 100, x + 16, 132), fill=GREEN_D, outline=IVORY, width=3)
    return sprite(("car6", n, hl), 152, 140, fn)

def car_x(i):
    return 382 + i * 158

def ic_doc_note(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 62 * s, cx + 50 * s, cy + 62 * s), 8 * s, fill=IVORY, outline=(206, 200, 186), width=3)
    c.rrect((cx - 12 * s, cy - 50 * s, cx + 12 * s, cy - 14 * s), 3, fill=CORAL)
    c.rrect((cx - 24 * s, cy - 38 * s, cx + 24 * s, cy - 26 * s), 3, fill=CORAL)
    for k in range(3):
        c.rrect((cx - 36 * s, cy - 2 * s + k * 18 * s, cx + 36 * s - k * 10 * s, cy + 6 * s + k * 18 * s), 3, fill=(206, 202, 190))
    c.arc((cx - 30 * s, cy + 40 * s, cx + 10 * s, cy + 58 * s), 180, 360, GREEN_D, 3 * s)
    c.arc((cx + 6 * s, cy + 40 * s, cx + 38 * s, cy + 58 * s), 0, 180, GREEN_D, 3 * s)

def ic_money_home(c, cx, cy, s):
    ic_house(c, cx - 40 * s, cy, 0.9 * s)
    for k in range(3):
        ic_coin(c, cx + 52 * s, cy + 40 * s - k * 22 * s, 30 * s)

def card2(k):
    def fn(c):
        w, h = 540, 340
        border = GOLD if k == 3 else GREEN_OK
        c.rrect((4, 4, w - 4, h - 4), 30, fill=CARD_BG, outline=border, width=7 if k == 3 else 5)
        if k == 1:
            ic_money_home(c, w / 2, 110, 1.1)
            c.text((w / 2, 238), "SAVES MONEY", FONT_SANS, 48, GOLD, track=1)
            c.text((w / 2, 292), "BEFORE YOU LEAVE HOME", FONT_SANS, 30, IVORY, track=1)
        elif k == 2:
            ic_suitcase(c, w / 2 - 6, 112, 1.25)
            c.text((w / 2, 238), "CARRIES", FONT_SANS, 48, GOLD, track=1)
            c.text((w / 2, 292), "YOUR BAGS FOR YOU", FONT_SANS, 30, IVORY, track=1)
        else:
            ic_doc_note(c, w / 2 + 80, 110, 1.05)
            c.ell((86, 46, 206, 166), fill=GOLD, outline=IVORY, width=5)
            c.text((146, 108), "10", FONT_SANS, 60, GREEN_D)
            c.text((w / 2, 238), "A NOTE FROM", FONT_SANS, 44, IVORY, track=1)
            c.text((w / 2, 292), "YOUR DOCTOR", FONT_SANS, 48, GOLD, track=1)
    return sprite(("card2_6", k), 540, 340, fn)

def draw2(img, t):
    ts = starts(2)
    common(img, t, "10 THINGS AMTRAK GIVES YOU")
    seq(img, t, ts[0], loco(), 200, 260, shadow=6, dur=0.4)
    for i in range(10):
        hl = (i == 9 and t >= ts[6])
        seq(img, t, ts[0] + 0.25 + i * 0.14, car(i + 1, hl), car_x(i), 260, shadow=6, dur=0.4)
    if t >= ts[6]:
        burst(img, t, ts[6], car_x(9), 260, n=10, color=GOLD, rad=150, seed=4)
    seq(img, t, ts[1], chip6w("RIDERS 65+", 400), 420, 450, shadow=6)
    seq(img, t, ts[2], chip6w("RIDERS WHO NEED A LITTLE HELP", 700), 1010, 450, shadow=6)
    seq(img, t, ts[3], pill_spr("WHEN THEY ASK", 40, 420, 76, GOLD, GREEN_D, border=(168, 118, 40), track=2), 1620, 450, shadow=8)
    for k, i, x in ((1, 4, 330), (2, 5, 960), (3, 6, 1590)):
        slide_in(img, t, ts[i], card2(k), x, 760, dy=60, dur=0.5, shadow=10)
    tl = last_t(2, ts[7])
    p = ease(seg(t, tl, 0.5))
    if p > 0:
        put(img, sprite("glow_c3", 556, 356, lambda c: c.rrect((4, 4, 552, 352), 34, outline=GOLD, width=8)), 1590, 760, alpha=p)
    ban(img, t, tl, "CAN SAVE THE WHOLE TICKET", cy=1010, cx=1290, w=1100, h=84, size=46)

def chip6w(text, w):
    return pill_spr(text, 38, w, 76, IVORY, GREEN_D, border=GOLD, track=2)

# ============================================================ BLOCCO 3 - foglietti + biglietto che perde monete
def note(lines, rot_col):
    def fn(c):
        w, h = 660, 230
        c.rrect((6, 6, w - 6, h - 6), 14, fill=(246, 232, 170), outline=(214, 190, 110), width=3)
        c.rrect((w / 2 - 70, 0, w / 2 + 70, 30), 4, fill=(190, 222, 232))
        for k, ln in enumerate(lines):
            c.text((w / 2, 96 + k * 64), ln, FONT_SANS, 46, GREEN_D, track=1)
    return sprite(("note6", tuple(lines)), 660, 230, fn)

def ticket():
    def fn(c):
        w, h = 640, 300
        c.rrect((4, 4, w - 4, h - 4), 26, fill=IVORY, outline=GOLD, width=6)
        c.ell((-30, h / 2 - 34, 34, h / 2 + 34), fill=(0, 0, 0, 0))
        c.d.ellipse(c._b((-34, h / 2 - 34, 34, h / 2 + 34)), fill=(0, 0, 0, 0))
        c.rrect((4, 4, w - 4, 84), 26, fill=GREEN_L)
        c.d.rectangle(c._b((4, 50, w - 4, 84)), fill=GREEN_L)
        c.text((w / 2, 46), "TRAIN TICKET", FONT_SANS, 44, IVORY, track=6)
        for k in range(3):
            c.rrect((48, 118 + k * 46, 48 + (380 if k % 2 == 0 else 280), 136 + k * 46), 9, fill=(206, 212, 206))
        c.line([(470, 96), (470, 286)], (206, 200, 186), 4)
        c.ell((500, 150, 600, 250), fill=GOLD, outline=(168, 118, 40), width=4)
        c.text((550, 202), "$", FONT_SANS, 60, GREEN_D)
    im = sprite("ticket6", 640, 300, fn)
    return im

def coin_spr(r=26):
    return sprite(("coin6", r), 2 * r + 4, 2 * r + 4, lambda c: ic_coin(c, r + 2, r + 2, r))

COINS = [(-120, 0.00, 780), (-40, 0.12, 790), (40, 0.24, 782), (120, 0.36, 792), (-80, 0.48, 742), (0, 0.60, 748), (80, 0.72, 740)]

def draw3(img, t):
    ts = starts(3)
    common(img, t, "TWO THOUGHTS")
    seq(img, t, ts[0], sprite("think6", 160, 160, lambda c: person_ic(c, 80, 96, 1.3, SAGE)), 150, 300, shadow=6)
    seq(img, t, ts[1], note(["“I DON'T TAKE", "THE TRAIN”"], 0), 560, 300, shadow=10, rot=2)
    seq(img, t, ts[2], sprite("think6b", 160, 160, lambda c: person_ic(c, 80, 96, 1.3, GOLD)), 150, 580, shadow=6)
    seq(img, t, ts[3], note(["“I ALREADY KNOW THE", "SENIOR DISCOUNT”"], 0), 560, 580, shadow=10, rot=-2)
    seq(img, t, ts[4], pill_spr("STAY WITH ME", 42, 460, 80, GOLD, GREEN_D, border=(168, 118, 40), track=3), 560, 820, shadow=8)
    # destra: il biglietto di chi conosce lo sconto
    slide_in(img, t, ts[5], ticket(), 1400, 420, dx=60, dur=0.5, shadow=14)
    seq(img, t, ts[5] + 0.4, pill_spr("THEY KNOW THE DISCOUNT", 34, 560, 70, IVORY, GREEN_D, border=GREEN_OK, track=2), 1400, 225, shadow=6)
    # monete che cadono e si fermano
    for dx, d0, yend in COINS:
        p = seg(t, ts[6] + d0, 0.55)
        if p > 0:
            y = 560 + (yend - 560) * (p * p)
            put(img, coin_spr(), 1400 + dx, y, alpha=min(1, p * 4))
    seq(img, t, ts[6] + 0.3, pill_spr("STILL LOSE MONEY", 40, 520, 76, CORAL, IVORY, border=(176, 70, 62), track=2), 1400, 880, shadow=8)
    tl = last_t(3, ts[7])
    s_, a, p = pop(t, tl, 0.5)
    if p > 0:
        put(img, sprite("mag6", 240, 240, lambda c: magnifier(c, 100, 100, 70, GOLD, 14)), 1600, 470, scale=s_, alpha=a, shadow=10)
    ban(img, t, tl, "I'LL SHOW YOU EXACTLY WHERE", cy=1010, w=1100, h=84, size=46)

# ============================================================ BLOCCO 4 - binario, borsa pesante, gradini
def train_side():
    def fn(c):
        w, h = 860, 560
        c.rrect((4, 4, w - 4, h - 60), 40, fill=IVORY, outline=(170, 190, 180), width=6)
        c.rrect((4, 300, w - 4, 330), 2, fill=GREEN_L)
        for x in (60, 560, 700):
            c.rrect((x, 70, x + 110, 170), 14, fill=(190, 222, 232), outline=(170, 190, 180), width=4)
        c.rrect((230, 60, 450, h - 60), 12, fill=(30, 60, 50), outline=(170, 190, 180), width=6)
        for k in range(3):
            y = h - 60 + k * 0 - (k + 1) * 0
        c.rrect((220, h - 64, 460, h - 40), 4, fill=(150, 160, 156))
        c.rrect((240, h - 40, 440, h - 18), 4, fill=(130, 140, 136))
        c.rrect((260, h - 18, 420, h - 2), 4, fill=(110, 120, 116))
    return sprite("tside6", 860, 560, fn)

def platform():
    def fn(c):
        c.rrect((0, 0, 1640, 80), 10, fill=(120, 132, 126))
        c.rrect((0, 0, 1640, 16), 4, fill=GOLD)
    return sprite("plat6", 1640, 80, fn)

def rider():
    def fn(c):
        c.ell((80, 20, 160, 100), fill=SKIN)
        c.d.pieslice(c._b((76, 10, 164, 80)), 180, 360, fill=HAIR)
        c.rrect((60, 110, 180, 300), 40, fill=(118, 150, 206))
        c.rrect((70, 290, 110, 420), 14, fill=GREEN_D)
        c.rrect((130, 290, 170, 420), 14, fill=GREEN_D)
        c.line([(170, 150), (220, 250)], (118, 150, 206), 26)
    return sprite("rider6", 240, 430, fn)

def heavy_bag():
    def fn(c):
        x, y, k = 110, 120, 1.8
        c.rrect((x - 30 * k, y - 56 * k, x + 30 * k, y - 36 * k), 8 * k, outline=(214, 164, 96), width=8 * k)
        c.rrect((x - 44 * k, y - 40 * k, x + 44 * k, y + 40 * k), 12 * k, fill=(214, 164, 96), outline=(160, 112, 60), width=4)
        c.rrect((x - 24 * k, y - 40 * k, x - 14 * k, y + 40 * k), 2, fill=(160, 112, 60))
        c.rrect((x + 14 * k, y - 40 * k, x + 24 * k, y + 40 * k), 2, fill=(160, 112, 60))
        for k in range(3):
            c.line([(20 + k * 14, 210), (34 + k * 14, 226)], SAGE, 6)
    return sprite("hbag6", 240, 240, fn)

def dash_arc(img, t, t0):
    p = ease(seg(t, t0, 0.8))
    if p <= 0:
        return
    n = int(14 * p)
    for k in range(n):
        u = k / 13
        x = 780 + 490 * u
        y = 690 + 110 * u - 300 * math.sin(u * math.pi)
        put(img, sprite("dot6", 22, 22, lambda c: c.ell((2, 2, 20, 20), fill=GOLD)), x, y)

def draw4(img, t):
    ts = starts(4)
    common(img, t, "ON THE PLATFORM")
    slide_in(img, t, ts[0], platform(), 960, 880, dy=30, dur=0.4)
    slide_in(img, t, ts[0] + 0.1, train_side(), 1360, 560, dx=60, dur=0.5, shadow=12)
    seq(img, t, ts[0] + 0.3, rider(), 470, 620, shadow=10, scale=0.95, dur=0.45)
    seq(img, t, ts[1], heavy_bag(), 690, 735, shadow=8, dur=0.45)
    seq(img, t, ts[1] + 0.3, pill_spr("HEAVY", 36, 200, 64, CORAL, IVORY, border=(176, 70, 62), track=3), 690, 590, shadow=6)
    dash_arc(img, t, ts[2])
    s_, a, p = pop(t, ts[2] + 0.6, 0.45)
    if p > 0:
        put(img, eq_circle("?", CORAL), 1025, 330, scale=s_ * 1.1, alpha=a, shadow=10)
    ban(img, t, last_t(4, ts[3]), "THIS VIDEO IS FOR YOU", cy=1010, w=980, h=84, size=46)

# ============================================================ BLOCCO 5 - una frase, lucchetti, troppo tardi
def lock(open_):
    def fn(c):
        col = GREEN_OK if open_ else (150, 160, 156)
        if open_:
            c.arc((30, 0, 90, 70), 180, 330, IVORY, 12)
        else:
            c.arc((30, 10, 90, 70), 180, 360, IVORY, 12)
            c.line([(30, 40), (30, 56)], IVORY, 12); c.line([(90, 40), (90, 56)], IVORY, 12)
        c.rrect((14, 50, 106, 130), 14, fill=col, outline=GREEN_D, width=4)
        c.ell((50, 74, 70, 94), fill=GREEN_D)
        c.rrect((56, 88, 64, 112), 3, fill=GREEN_D)
    return sprite(("lock6", open_), 120, 136, fn)

def sentence_bubble():
    def fn(c):
        w, h = 620, 300
        c.rrect((4, 4, w - 4, h - 60), 40, fill=IVORY, outline=GOLD, width=7)
        c.poly([(120, h - 64), (110, h - 4), (190, h - 64)], fill=IVORY)
        c.text((w / 2, 66), "ONE SENTENCE", FONT_SANS, 46, GREEN_D, track=4)
        for k, ww in enumerate((440, 340)):
            c.rrect((w / 2 - ww / 2, 120 + k * 46, w / 2 + ww / 2, 144 + k * 46), 12, fill=(206, 212, 206))
    return sprite("sbub6", 620, 300, fn)

def key_spr():
    def fn(c):
        c.ell((6, 6, 86, 86), outline=GOLD, width=16)
        c.rrect((80, 38, 230, 56), 6, fill=GOLD)
        c.rrect((180, 54, 196, 82), 4, fill=GOLD); c.rrect((206, 54, 222, 74), 4, fill=GOLD)
    return sprite("key6", 240, 92, fn)

def flag_pill():
    def fn(c):
        w, h = 760, 96
        c.rrect((3, 3, w - 3, h - 3), h / 2, fill=GOLD, outline=(168, 118, 40), width=5)
        c.line([(70, 18), (70, 80)], GREEN_D, 6)
        for r in range(3):
            for q in range(3):
                if (r + q) % 2 == 0:
                    c.rrect((72 + q * 16, 18 + r * 12, 88 + q * 16, 30 + r * 12), 1, fill=GREEN_D)
        c.text((w / 2 + 40, h / 2 + 2), "STAY UNTIL THE END", FONT_SANS, 44, GREEN_D, track=3)
    return sprite("flag6", 760, 96, fn)

LOCKS = [(1010 + (i % 5) * 170, 420 + (i // 5) * 190) for i in range(10)]

def draw5(img, t):
    ts = starts(5)
    common(img, t, "ONE SENTENCE")
    seq(img, t, ts[0], flag_pill(), 960, 190, shadow=8)
    seq(img, t, ts[1], sentence_bubble(), 470, 500, shadow=12)
    seq(img, t, ts[1] + 0.4, key_spr(), 560, 700, shadow=6, rot=12)
    for i, (x, y) in enumerate(LOCKS):
        op = i != 9 and t >= ts[2] + 0.2 + i * 0.12
        seq(img, t, ts[1] + 0.3 + i * 0.05, lock(op), x, y, shadow=6, dur=0.35)
    seq(img, t, ts[2] + 1.3, pill_spr("UNLOCKS ALMOST ALL", 38, 560, 72, IVORY, GREEN_D, border=GREEN_OK, track=2), 1350, 745, shadow=6)
    seq(img, t, ts[3], pill_spr("MOST RIDERS SAY IT...", 40, 640, 80, IVORY, GREEN_D, border=GOLD, track=2), 470, 880, shadow=8)
    tl = last_t(5, ts[4])
    s_, a, p = pop(t, tl, 0.5)
    if p > 0:
        put(img, sprite("clk6", 170, 170, lambda c: ic_clock(c, 85, 85, 78, 2.2)), 950, 880, scale=s_, alpha=a, shadow=8)
        put(img, stamp("ALREADY TOO LATE", 560, 120, CORAL), 1430, 880, scale=s_, alpha=a, rot=-6, shadow=10)

DRAW = {2: draw2, 3: draw3, 4: draw4, 5: draw5}

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
