import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes9 import *

# =====================================================================
# SHORT 10: Amtrak (correlato al video lungo 6). Stesso motore e colori degli short 5-9, layout NUOVO:
# intestazione a tabellone partenze (lettere che girano) + binario con 6 fermate e trenino che avanza,
# binari leggeri sullo sfondo, disegni grandi (modulo di prenotazione, facchino in rosso, nota del medico, treno a 10 vagoni,
# biglietto-video, biglietto finale con like/iscriviti).
# Durate (fotogrammi): 273 311 309 210 228 203. Ultimo elemento di ogni blocco entro l'80%.
# Nelle slide compare SOLO cio' che la voce dice. Niente "Senior", "Red Cap", nomi o passi: restano nel video lungo.
# uso: S10_OUT=cartella SA_TMP=/tmp/x python3 scenes10.py <clip>
# =====================================================================
RED = (200, 62, 56)
RED_D = (150, 40, 36)
SKIN = (236, 194, 154)
STEEL = (200, 210, 206)
BOARD = (10, 22, 20)
AMBER = (246, 196, 92)
GREEN_OK = (110, 200, 130)

def ptext(img, t, t0, s, y, size, col, shadow=8, track=0, maxw=960):
    """pop_text che non esce mai dai bordi (riduce la dimensione se serve)"""
    a = seg(t, t0, 0.4)
    if a > 0:
        sp = tspr(s, FONT_SANS, size, col, track=track)
        sc = min(1.0, maxw / sp.width)
        put(img, sp, 540, y + 22 * (1 - ease(a)), scale=sc, alpha=ease(a), shadow=shadow)

# ------------------------------------------------------------------ intestazione: tabellone partenze
def flap_spr(ch, col):
    def mk():
        c = Cv(56, 80)
        c.rrect((2, 2, 54, 78), 8, fill=(24, 36, 34), outline=(44, 60, 56), width=2)
        c.line([4, 40, 52, 40], BOARD, 3)
        if ch != " ":
            c.text((28, 42), ch, FONT_SANS, 50, col)
        return c.done()
    return cache(("flap", ch, col), mk)

def board_frame_spr(n):
    def mk():
        w = n * 58 + 70
        c = Cv(w, 128)
        c.rrect((3, 3, w - 3, 125), 22, fill=BOARD, outline=GOLD, width=5)
        for x in (24, w - 24):
            c.ell((x - 7, 57, x + 7, 71), fill=(60, 74, 70))
        return c.done()
    return cache(("bframe", n), mk)

FLAP_CH = "ABCDEFGHIJKLMNOPRSTUVWXYZ?0123456789"

def board(img, t, text, y, col, t0=0.0):
    """tabellone con lettere che girano e si fermano una dopo l'altra (fermo entro t0+1,4 s)"""
    a = seg(t, t0, 0.35)
    if a <= 0:
        return
    n = len(text)
    put(img, board_frame_spr(n), W // 2, y - 30 * (1 - ease(a)), alpha=ease(a), shadow=10)
    x0 = W // 2 - (n - 1) * 58 / 2
    for i, ch in enumerate(text):
        stop = t0 + 0.3 + i * (1.0 / max(1, n))
        if ch == " ":
            shown = " "
        elif t < stop:
            shown = FLAP_CH[(int(t * 30) * 7 + i * 5) % len(FLAP_CH)]
        else:
            shown = ch
        put(img, flap_spr(shown, col if t >= stop else (150, 140, 110)), x0 + i * 58, y - 30 * (1 - ease(a)), alpha=ease(a))

def mini_train_spr():
    def mk():
        c = Cv(120, 64)
        c.rrect((4, 6, 104, 50), 16, fill=GOLD, outline=CRUST_D, width=3)
        c.poly([(96, 6), (118, 28), (118, 50), (96, 50)], fill=GOLD)
        for k in range(3):
            c.rrect((16 + k * 26, 14, 34 + k * 26, 30), 4, fill=(190, 222, 232))
        c.ell((18, 44, 38, 64), fill=DARK); c.ell((70, 44, 90, 64), fill=DARK)
        return c.done()
    return cache("mtrain", mk)

def track_line(img, t, y, k, n=6):
    """binario con n fermate; il trenino arriva alla fermata k"""
    a = seg(t, 0.15, 0.4)
    if a <= 0:
        return
    al = ease(a)
    x0, x1 = 170, 910
    put(img, rail_spr(), 540, y, alpha=al)
    for i in range(n):
        x = x0 + i * (x1 - x0) / (n - 1)
        col = GOLD if i < k else (60, 112, 92)
        put(img, dot_spr(col, 13 if i == k - 1 else 9), x, y, alpha=al)
    u = ease(seg(t, 0.3, 1.0))
    xa = x0 + max(0, k - 2) * (x1 - x0) / (n - 1)
    xb = x0 + (k - 1) * (x1 - x0) / (n - 1)
    put(img, mini_train_spr(), xa + (xb - xa) * u, y - 34, alpha=al, scale=0.9)

def rail_spr():
    def mk():
        c = Cv(820, 30)
        c.rrect((10, 12, 810, 18), 3, fill=SAGE_D)
        for k in range(27):
            c.rrect((14 + k * 30, 6, 22 + k * 30, 24), 2, fill=(40, 86, 70))
        return c.done()
    return cache("rail10", mk)

def ambient10(img, t, seed=10, alpha=0.08):
    """binari diagonali molto leggeri che scorrono (sfondo)"""
    sp = cache("amb_rail", lambda: _amb_rail())
    off = (t * 40) % 120
    put(img, sp, 540 - off, 1890, alpha=alpha * 1.6, rot=0)

def _amb_rail():
    c = Cv(1400, 80)
    c.rrect((0, 20, 1400, 28), 3, fill=(190, 224, 210))
    c.rrect((0, 54, 1400, 62), 3, fill=(190, 224, 210))
    for k in range(48):
        c.rrect((k * 30, 12, k * 30 + 12, 70), 3, fill=(190, 224, 210))
    return c.done()

# ------------------------------------------------------------------ sprite
def booking_spr():
    """modulo di prenotazione treno (senza marchi): FROM, TO, DATE, TRAVELER con casella"""
    def mk():
        c = Cv(820, 720)
        c.rrect((4, 4, 816, 716), 40, fill=CARD, outline=GOLD, width=6)
        c.rrect((4, 4, 816, 120), 40, fill=(22, 82, 64))
        c.rrect((4, 80, 816, 120), 2, fill=(22, 82, 64))
        c.rrect((44, 34, 140, 88), 14, fill=GOLD)
        for k in range(3):
            c.rrect((56 + k * 28, 44, 76 + k * 28, 60), 3, fill=(190, 222, 232))
        c.text((470, 62), "BOOK A TRAIN", FONT_SANS, 48, IVORY, track=4)
        rows = [("FROM", 0.62), ("TO", 0.48), ("DATE", 0.34)]
        for i, (lab, wl) in enumerate(rows):
            y = 160 + i * 112
            c.text((60, y + 42), lab, FONT_SANS, 30, SAGE, anchor="lm", track=3)
            c.rrect((230, y + 6, 770, y + 78), 16, fill=(18, 70, 56), outline=SAGE_D, width=3)
            c.rrect((256, y + 34, 256 + 480 * wl, y + 50), 6, fill=(120, 160, 140))
        y = 160 + 3 * 112
        c.text((60, y + 42), "TRAVELER", FONT_SANS, 30, SAGE, anchor="lm", track=3)
        c.rrect((300, y + 6, 770, y + 78), 16, fill=(18, 70, 56), outline=SAGE_D, width=3)
        c.rrect((326, y + 34, 560, y + 50), 6, fill=(120, 160, 140))
        c.rrect((230, 620, 640, 690), 34, fill=GOLD)
        c.text((435, 656), "BUY TICKET", FONT_SANS, 34, DARK, track=4)
        return c.done()
    return cache("booking10", mk)

def checkbox_spr(col):
    def mk():
        c = Cv(140, 140)
        c.rrect((8, 8, 132, 132), 22, fill=IVORY, outline=col, width=10)
        return c.done()
    return cache(("cbox", col), mk)

def hand_spr():
    def mk():
        c = Cv(160, 200)
        c.rrect((52, 6, 92, 110), 20, fill=SKIN, outline=(190, 150, 110), width=3)
        c.rrect((26, 80, 146, 190), 40, fill=SKIN, outline=(190, 150, 110), width=3)
        for k in range(3):
            pass
        c.line([90, 100, 90, 128], (190, 150, 110), 3)
        c.line([118, 104, 118, 130], (190, 150, 110), 3)
        return c.done()
    return cache("hand10", mk)

def coin_spr():
    def mk():
        c = Cv(110, 110)
        c.ell((4, 4, 106, 106), fill=GOLD, outline=CRUST_D, width=5)
        c.ell((18, 18, 92, 92), outline=CRUST_D, width=3)
        c.text((55, 57), "$", FONT_SANS, 54, CRUST_D)
        return c.done()
    return cache("coin10", mk)

def station_spr():
    def mk():
        c = Cv(900, 560)
        c.rrect((40, 170, 860, 540), 26, fill=(22, 82, 64), outline=SAGE_D, width=6)
        c.poly([(20, 190), (450, 30), (880, 190)], fill=(30, 100, 80))
        c.ell((380, 70, 520, 210), fill=IVORY, outline=GOLD, width=8)
        c.line([450, 140, 450, 98], DARK, 8); c.line([450, 140, 482, 156], DARK, 8)
        for k in range(3):
            x = 120 + k * 250
            c.rrect((x, 290, x + 170, 540), 80, fill=(14, 58, 45), outline=SAGE_D, width=5)
            c.rrect((x + 20, 320, x + 150, 520), 64, fill=(40, 70, 64))
        c.rrect((300, 224, 600, 280), 14, fill=DARK, outline=GOLD, width=4)
        c.text((450, 252), "STATION", FONT_SANS, 34, GOLD, track=8)
        return c.done()
    return cache("station10", mk)

def porter_spr():
    """persona in divisa rossa con carrello di valigie"""
    def mk():
        c = Cv(520, 560)
        # carrello
        c.line([300, 120, 330, 470, 500, 470], STEEL, 12)
        c.ell((316, 450, 366, 500), fill=DARK, outline=STEEL, width=5)
        c.ell((460, 450, 510, 500), fill=DARK, outline=STEEL, width=5)
        c.rrect((340, 300, 490, 460), 16, fill=(214, 164, 96), outline=(160, 112, 60), width=5)
        c.rrect((392, 280, 438, 300), 6, outline=(160, 112, 60), width=5)
        c.rrect((350, 180, 480, 300), 16, fill=(110, 176, 124), outline=DARK, width=5)
        c.rrect((380, 120, 460, 180), 12, fill=(120, 170, 190), outline=DARK, width=5)
        # persona
        c.ell((120, 60, 220, 160), fill=SKIN)
        c.d.chord(c._b((112, 36, 228, 130)), 180, 360, fill=RED)
        c.rrect((160, 76, 262, 96), 8, fill=RED_D)
        c.rrect((90, 170, 250, 400), 50, fill=RED)
        c.rrect((160, 176, 180, 330), 4, fill=RED_D)
        c.line([230, 220, 310, 150], RED, 34)
        c.ell((292, 128, 334, 170), fill=SKIN)
        c.rrect((104, 390, 160, 540), 18, fill=DARK)
        c.rrect((180, 390, 236, 540), 18, fill=DARK)
        return c.done()
    return cache("porter10", mk)

def senior_spr(col=SAGE_D, cane=True):
    def mk():
        c = Cv(260, 520)
        c.ell((80, 20, 180, 120), fill=SKIN)
        c.ell((74, 10, 186, 64), fill=(240, 240, 236))
        c.rrect((50, 130, 210, 360), 60, fill=col)
        c.rrect((70, 350, 120, 510), 18, fill=(40, 60, 60))
        c.rrect((140, 350, 190, 510), 18, fill=(40, 60, 60))
        if cane:
            c.line([214, 250, 236, 510], (160, 112, 60), 12)
            c.arc((190, 226, 240, 276), 180, 360, (160, 112, 60), 12)
        c.rrect((4, 300, 64, 420), 12, fill=(120, 170, 190), outline=DARK, width=4)
        return c.done()
    return cache(("senior10", col, cane), mk)

def walker_spr():
    def mk():
        c = Cv(120, 240)
        c.ell((32, 4, 88, 60), fill=(16, 64, 50), outline=SAGE_D, width=5)
        c.rrect((20, 66, 100, 170), 30, fill=(16, 64, 50), outline=SAGE_D, width=5)
        c.line([46, 166, 30, 236], SAGE_D, 12); c.line([74, 166, 92, 236], SAGE_D, 12)
        return c.done()
    return cache("walker10", mk)

def ticket_spr(price=True):
    def mk():
        c = Cv(760, 330)
        c.rrect((4, 4, 756, 326), 30, fill=IVORY, outline=GOLD, width=6)
        c.ell((-30, 135, 30, 195), fill=(0, 0, 0, 0))
        c.ell((730, 135, 790, 195), fill=(0, 0, 0, 0))
        for k in range(11):
            c.rrect((540, 26 + k * 26, 546, 40 + k * 26), 2, fill=(206, 200, 186))
        c.rrect((40, 34, 320, 92), 14, fill=(22, 82, 64))
        c.text((180, 64), "TRAIN TICKET", FONT_SANS, 30, IVORY, track=3)
        for k in range(3):
            c.rrect((44, 128 + k * 44, 470 - k * 80, 146 + k * 44), 6, fill=(214, 210, 198))
        if price:
            c.ell((570, 90, 730, 250), fill=GOLD, outline=CRUST_D, width=6)
            c.text((650, 172), "$", FONT_SANS, 100, DARK)
        return c.done()
    return cache(("ticket10", price), mk)

def note_spr():
    """nota del medico: foglio con croce rossa, righe, firma"""
    def mk():
        c = Cv(420, 540)
        c.rrect((6, 6, 414, 534), 18, fill=IVORY, outline=(206, 200, 186), width=5)
        c.rrect((6, 6, 414, 120), 18, fill=(230, 236, 232))
        c.rrect((6, 90, 414, 120), 2, fill=(230, 236, 232))
        c.rrect((40, 26, 112, 98), 12, fill=IVORY, outline=RED, width=4)
        c.rrect((66, 36, 86, 88), 3, fill=RED); c.rrect((50, 52, 102, 72), 3, fill=RED)
        c.text((262, 64), "DOCTOR", FONT_SANS, 40, DARK, track=4)
        for k in range(6):
            c.rrect((44, 160 + k * 46, 380 - (k % 3) * 60, 174 + k * 46), 5, fill=(206, 212, 206))
        c.line([60, 470, 100, 440, 130, 480, 170, 436, 210, 478, 250, 446, 300, 466], (40, 70, 140), 6)
        c.rrect((44, 494, 330, 498), 2, fill=(180, 176, 166))
        return c.done()
    return cache("note10", mk)

def sick_spr():
    """persona a letto con termometro"""
    def mk():
        c = Cv(520, 340)
        c.rrect((20, 150, 500, 280), 20, fill=(120, 170, 190), outline=DARK, width=5)
        c.rrect((20, 60, 70, 320), 14, fill=(160, 112, 60))
        c.rrect((460, 140, 500, 320), 14, fill=(160, 112, 60))
        c.rrect((70, 110, 220, 170), 30, fill=IVORY)
        c.ell((90, 60, 190, 160), fill=SKIN)
        c.ell((84, 52, 196, 100), fill=(240, 240, 236))
        c.rrect((180, 150, 470, 230), 30, fill=(214, 108, 96), outline=DARK, width=4)
        c.line([170, 122, 250, 70], (236, 236, 236), 12)
        c.ell((242, 58, 266, 82), fill=RED)
        return c.done()
    return cache("sick10", mk)

def clock_spr():
    def mk():
        c = Cv(240, 240)
        c.ell((6, 6, 234, 234), fill=IVORY, outline=CORAL, width=10)
        for k in range(12):
            a = k * math.pi / 6
            c.line([120 + 92 * math.sin(a), 120 - 92 * math.cos(a), 120 + 104 * math.sin(a), 120 - 104 * math.cos(a)], DARK, 5)
        c.line([120, 120, 120, 54], DARK, 10)
        c.line([120, 120, 166, 140], DARK, 10)
        c.ell((108, 108, 132, 132), fill=CORAL)
        return c.done()
    return cache("clock10", mk)

def train_side_spr():
    def mk():
        c = Cv(640, 260)
        c.rrect((10, 30, 560, 210), 40, fill=(22, 82, 64), outline=GOLD, width=6)
        c.poly([(540, 30), (630, 120), (630, 210), (540, 210)], fill=(22, 82, 64))
        c.line([540, 30, 630, 120, 630, 210], GOLD, 6)
        for k in range(5):
            c.rrect((40 + k * 100, 60, 116 + k * 100, 120), 10, fill=(190, 222, 232))
        c.rrect((10, 150, 630, 166), 4, fill=GOLD)
        for x in (90, 220, 400, 530):
            c.ell((x - 28, 190, x + 28, 246), fill=DARK, outline=STEEL, width=5)
        return c.done()
    return cache("tside10", mk)

def lock_spr(col=GOLD):
    def mk():
        c = Cv(120, 150)
        c.arc((22, 6, 98, 90), 180, 360, col, 14)
        c.rrect((22, 44, 98, 50), 2, fill=col)
        c.line([28, 48, 28, 64], col, 14); c.line([92, 48, 92, 64], col, 14)
        c.rrect((6, 60, 114, 146), 18, fill=col)
        c.ell((48, 86, 72, 110), fill=DARK)
        c.rrect((55, 100, 65, 128), 3, fill=DARK)
        return c.done()
    return cache(("lock10", col), mk)

# vagoni 1-10: 1-3 accesi con l'assaggio, 4-10 chiusi
def car_spr(n, on):
    def mk():
        c = Cv(190, 170)
        c.rrect((6, 10, 184, 136), 24, fill=GOLD if on else (16, 64, 50), outline=CRUST_D if on else SAGE_D, width=5)
        c.rrect((22, 26, 168, 66), 10, fill=(190, 222, 232) if on else (30, 80, 66))
        c.ell((26, 126, 66, 166), fill=DARK, outline=STEEL, width=4)
        c.ell((124, 126, 164, 166), fill=DARK, outline=STEEL, width=4)
        c.text((95, 100), str(n), FONT_SANS, 44, DARK if on else SAGE_D)
        return c.done()
    return cache(("car10", n, on), mk)

def icon_box(c, cx, cy):
    c.rrect((cx - 34, cy - 34, cx + 34, cy + 34), 10, fill=IVORY, outline=DARK, width=5)
def icon_bag(c, cx, cy):
    c.rrect((cx - 36, cy - 24, cx + 36, cy + 38), 10, fill=(214, 164, 96), outline=DARK, width=4)
    c.rrect((cx - 14, cy - 40, cx + 14, cy - 22), 5, outline=DARK, width=4)
def icon_note(c, cx, cy):
    c.rrect((cx - 30, cy - 40, cx + 30, cy + 40), 6, fill=IVORY, outline=DARK, width=3)
    c.rrect((cx - 6, cy - 30, cx + 6, cy - 6), 2, fill=RED); c.rrect((cx - 18, cy - 24, cx + 18, cy - 12), 2, fill=RED)

def chip_spr(kind):
    def mk():
        c = Cv(120, 120)
        c.ell((4, 4, 116, 116), fill=IVORY, outline=GOLD, width=5)
        {"box": icon_box, "bag": icon_bag, "note": icon_note}[kind](c, 60, 60)
        if kind == "box":
            c.line([42, 60, 56, 74, 82, 44], DARK, 8)
        return c.done()
    return cache(("chip10", kind), mk)

def vticket_spr():
    """biglietto-video del lungo (anteprima con play)"""
    def mk():
        c = Cv(900, 560)
        c.rrect((4, 4, 896, 556), 44, fill=CARD, outline=GOLD, width=7)
        c.rrect((30, 30, 870, 340), 28, fill=(22, 82, 64))
        for k in range(10):
            x = 70 + k * 78
            c.rrect((x, 250, x + 64, 300), 10, fill=GOLD if k < 3 else (30, 96, 76))
        c.rrect((40, 306, 860, 314), 3, fill=SAGE_D)
        c.ell((360, 70, 540, 250), fill=GOLD, outline=CRUST_D, width=6)
        c.poly([(424, 112), (424, 208), (502, 160)], fill=DARK)
        c.text((450, 418), "ALL 10 THINGS", FONT_SANS, 76, GOLD, track=5)
        c.text((450, 494), "OVER 65  ·  IF YOU ASK", FONT_SANS, 38, SAGE, track=4)
        return c.done()
    return cache("vticket10", mk)

def hidden_bubble_spr():
    def mk():
        c = Cv(760, 250)
        c.rrect((4, 4, 756, 200), 40, fill=IVORY)
        c.poly([(120, 196), (90, 246), (190, 196)], fill=IVORY)
        for k, w in enumerate((520, 420)):
            c.rrect((190, 52 + k * 62, 190 + w, 86 + k * 62), 16, fill=(206, 212, 206))
        c.ell((40, 42, 150, 152), fill=GOLD)
        c.text((95, 99), "“", FONT_SERIF, 110, DARK)
        return c.done()
    return cache("hbub10", mk)

def endticket_spr():
    """biglietto finale: LIKE | SUBSCRIBE"""
    def mk():
        c = Cv(960, 460)
        c.rrect((4, 4, 956, 456), 36, fill=IVORY, outline=GOLD, width=7)
        c.ell((-34, 196, 34, 264), fill=(0, 0, 0, 0)); c.ell((926, 196, 994, 264), fill=(0, 0, 0, 0))
        for k in range(15):
            c.rrect((477, 24 + k * 28, 483, 38 + k * 28), 2, fill=(206, 200, 186))
        c.rrect((4, 4, 956, 70), 36, fill=(22, 82, 64)); c.rrect((4, 40, 956, 70), 2, fill=(22, 82, 64))
        c.text((480, 38), "TICKET TO THE NEXT ONE", FONT_SANS, 34, GOLD, track=6)
        return c.done()
    return cache("endt10", mk)

def punch(img, t, t0, x, y):
    a = seg(t, t0, 0.3)
    if a > 0:
        put(img, cache("hole10", lambda: _hole()), x, y, scale=0.6 + 0.4 * ease(a), alpha=ease(a))

def _hole():
    c = Cv(70, 70)
    c.ell((4, 4, 66, 66), fill=GREEN_D)
    return c.done()

# ---------------------------------------------------------------- B1 (273 f = 9,1 s): gancio
def c1(img, t):
    ambient10(img, t)
    board(img, t, "OVER 65?", 230, AMBER)
    track_line(img, t, 360, 1)
    s, al, a = pop(t, 1.2, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 820, scale=1.4, alpha=0.25 * al)
        put(img, booking_spr(), 540, 820, scale=1.0 * s, alpha=al, shadow=16, rot=-2 * (1 - ease(a)))
    # la casella (riga TRAVELER) evidenziata
    s, al, a = pop(t, 3.3, 0.45)
    if a > 0:
        bx, by = 830, 998
        put(img, glow_spr(), bx, by, scale=0.45, alpha=0.5 * al)
        put(img, checkbox_spr(CORAL), bx, by, scale=0.7 * s, alpha=al, shadow=8)
        burst(img, t, 3.3, bx, by, n=10, color=GOLD, dur=0.6, rad=160, seed=101)
        u = ease(seg(t, 3.6, 0.8))
        put(img, hand_spr(), bx + 38 + 140 * (1 - u), by + 100 + 120 * (1 - u), scale=0.6, alpha=al)
    ptext(img, t, 3.6, "ONE BOX", 1340, 110, GOLD, 10, track=6)
    ptext(img, t, 4.5, "MOST PEOPLE NEVER CLICK", 1460, 60, IVORY, 8, track=1)
    s, al, a = pop(t, 6.4, 0.5)
    if a > 0:
        put(img, stamp_spr("COSTS YOU MONEY", 860, 150, CORAL), 540, 1690, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 6.4, 540, 1690, n=12, color=CORAL, dur=0.7, rad=190, seed=102)

# ---------------------------------------------------------------- B2 (311 f = 10,4 s): divisa rossa
def c2(img, t):
    ambient10(img, t, seed=12)
    board(img, t, "BIG STATIONS", 230, AMBER)
    track_line(img, t, 360, 2)
    s, al, a = pop(t, 0.4, 0.5)
    if a > 0:
        put(img, station_spr(), 540, 610, scale=0.8 * s, alpha=al, shadow=12)
    s, al, a = pop(t, 1.6, 0.5)
    if a > 0:
        put(img, glow_spr(), 380, 1000, scale=1.0, alpha=0.3 * al)
        put(img, porter_spr(), 400, 1000, scale=0.8 * s, alpha=al, shadow=14)
        burst(img, t, 1.6, 380, 1000, n=10, color=RED, dur=0.6, rad=260, seed=103)
    s, al, a = pop(t, 2.2, 0.45)
    if a > 0:
        put(img, senior_spr(), 850, 1010, scale=0.78 * s, alpha=al, shadow=10)
    s, al, a = pop(t, 2.4, 0.45)
    if a > 0:
        put(img, tag_spr("RED UNIFORM", 520, 110, RED, 54), 400, 1270, scale=s, alpha=al, rot=-2, shadow=10)
    ptext(img, t, 3.3, "CARRIES YOUR BAGS", 1390, 76, IVORY, 8, track=2)
    s, al, a = pop(t, 5.0, 0.5)
    if a > 0:
        put(img, stamp_spr("AMTRAK CALLS IT FREE", 900, 130, GOLD), 540, 1510, scale=s, alpha=al, rot=-2, shadow=12)
        burst(img, t, 5.0, 540, 1510, n=12, color=GOLD, dur=0.7, rad=300, seed=104)
    # persone che passano oltre
    for k in range(3):
        u = seg(t, 6.8 + k * 0.15, 1.2)
        if u > 0:
            put(img, walker_spr(), 180 + k * 150 + 300 * ease(u), 1640, scale=0.45, alpha=min(1.0, 3 * u))
    ptext(img, t, 7.4, "MOST WALK RIGHT PAST", 1745, 62, CORAL, 8, track=2)

# ---------------------------------------------------------------- B3 (309 f = 10,3 s): nota del medico
def c3(img, t):
    ambient10(img, t, seed=14)
    board(img, t, "IF YOU GET SICK", 230, AMBER)
    track_line(img, t, 360, 3)
    s, al, a = pop(t, 0.4, 0.5)
    if a > 0:
        put(img, sick_spr(), 290, 600, scale=0.95 * s, alpha=al, shadow=12)
    s, al, a = pop(t, 1.3, 0.5)
    if a > 0:
        put(img, ticket_spr(), 760, 600, scale=0.55 * s, alpha=al, shadow=12, rot=4)
    s, al, a = pop(t, 2.2, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 960, scale=1.1, alpha=0.3 * al)
        put(img, note_spr(), 540, 960, scale=0.62 * s, alpha=al, shadow=14, rot=-5 * (1 - ease(a)) - 3)
        burst(img, t, 2.2, 540, 960, n=12, color=GOLD, dur=0.7, rad=300, seed=105)
    ptext(img, t, 2.8, "ONE PIECE OF PAPER", 1200, 72, IVORY, 8, track=2)
    ptext(img, t, 3.9, "CAN SAVE YOUR TICKET MONEY", 1295, 54, GOLD, 8, track=1)
    ptext(img, t, 5.7, "BUT ONLY IF", 1415, 84, CORAL, 10, track=6)
    s, al, a = pop(t, 6.4, 0.5)
    if a > 0:
        put(img, train_side_spr(), 330, 1570, scale=0.55 * s, alpha=al, shadow=10)
        put(img, clock_spr(), 760, 1570, scale=0.6 * s, alpha=al, shadow=10)
    s, al, a = pop(t, 7.2, 0.45)
    if a > 0:
        put(img, tag_spr("1 THING BEFORE IT LEAVES", 900, 96, GOLD, 44), 540, 1720, scale=s, alpha=al, shadow=10)

# ---------------------------------------------------------------- B4 (210 f = 7 s): 3 di 10
def c4(img, t):
    ambient10(img, t, seed=16)
    board(img, t, "3 OF 10", 230, AMBER)
    track_line(img, t, 360, 4)
    for n in range(10):
        r, q = divmod(n, 5)
        s, al, a = pop(t, 0.3 + n * 0.08, 0.35)
        if a > 0:
            on = n < 3 and t > 1.6 + n * 0.25
            put(img, car_spr(n + 1, on), 160 + q * 190, 640 + r * 220, scale=s, alpha=al, shadow=8)
            if n >= 3:
                put(img, lock_spr(SAGE_D), 160 + q * 190, 600 + r * 220, scale=0.32 * s, alpha=al)
    for n, kind in enumerate(("box", "bag", "note")):
        s, al, a = pop(t, 1.6 + n * 0.25, 0.4)
        if a > 0:
            put(img, chip_spr(kind), 160 + n * 190, 520, scale=0.8 * s, alpha=al, shadow=8)
            burst(img, t, 1.6 + n * 0.25, 160 + n * 190, 640, n=8, color=GOLD, dur=0.5, rad=140, seed=106 + n)
    ptext(img, t, 1.8, "3 OF 10 THINGS", 1170, 92, IVORY, 10, track=4)
    ptext(img, t, 2.8, "RIDERS OVER 65 GET", 1290, 62, SAGE, 8, track=2)
    s, al, a = pop(t, 3.6, 0.45)
    if a > 0:
        put(img, tag_spr("IF THEY ASK", 560, 120, GOLD, 64), 540, 1430, scale=s, alpha=al, rot=-2, shadow=12)
    s, al, a = pop(t, 4.9, 0.5)
    if a > 0:
        put(img, stamp_spr("MOST PEOPLE NEVER DO", 900, 140, CORAL), 540, 1630, scale=s, alpha=al, rot=-3, shadow=12)
        burst(img, t, 4.9, 540, 1630, n=12, color=CORAL, dur=0.7, rad=300, seed=110)

# ---------------------------------------------------------------- B5 (228 f = 7,6 s): video lungo
def c5(img, t):
    ambient10(img, t, seed=18)
    board(img, t, "THE FULL VIDEO", 230, AMBER)
    track_line(img, t, 360, 5)
    s, al, a = pop(t, 0.3, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 650, scale=1.5, alpha=0.3 * al)
        put(img, vticket_spr(), 540, 650, scale=1.0 * s, alpha=al, shadow=18, rot=-2 * (1 - ease(a)))
        burst(img, t, 0.3, 540, 650, n=12, color=GOLD, dur=0.7, rad=460, seed=111)
    s, al, a = pop(t, 1.7, 0.5)
    if a > 0:
        put(img, hidden_bubble_spr(), 520, 1040, scale=0.9 * s, alpha=al, shadow=12)
        put(img, lock_spr(), 880, 1010, scale=0.6 * s, alpha=al, shadow=8)
    ptext(img, t, 2.2, "THE EXACT SENTENCE TO SAY", 1210, 54, IVORY, 8, track=1)
    ptext(img, t, 4.0, "RIGHT BELOW", 1340, 104, GOLD, 12, track=4)
    ptext(img, t, 5.2, "TAP IT NOW", 1460, 86, IVORY, 10, track=4)
    for k in range(3):
        a = seg(t, 5.4 + k * 0.12, 0.35)
        if a > 0:
            put(img, chevron_spr(), 540, 1570 + k * 50 + 16 * (1 - ease(a)), alpha=ease(a) * (1 - 0.25 * k), scale=0.7)

# ---------------------------------------------------------------- B6 (203 f = 6,8 s): like e iscrizione
def c6(img, t):
    ambient10(img, t, seed=20)
    board(img, t, "BEFORE YOU GO", 230, AMBER)
    track_line(img, t, 360, 6)
    s, al, a = pop(t, 0.4, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 860, scale=1.5, alpha=0.25 * al)
        put(img, endticket_spr(), 540, 860, scale=1.0 * s, alpha=al, shadow=16, rot=-2 * (1 - ease(a)))
    s, al, a = pop(t, 0.9, 0.5)
    if a > 0:
        put(img, thumb_spr(), 300, 820, scale=0.6 * s, alpha=al, rot=-6)
        burst(img, t, 0.9, 300, 820, n=10, color=GOLD, dur=0.6, rad=200, seed=114)
    s, al, a = pop(t, 1.2, 0.4)
    if a > 0:
        put(img, tag_spr("LIKE", 300, 100, GOLD, 64), 300, 1010, scale=s, alpha=al, shadow=8)
    punch(img, t, 1.4, 140, 710)
    s, al, a = pop(t, 2.2, 0.5)
    if a > 0:
        sw = 10 * math.sin((t - 2.5) * 18) * max(0.0, 1 - (t - 2.5) / 1.0) if t > 2.5 else 0
        put(img, bell_spr(), 780, 815, scale=0.9 * s, alpha=al, rot=sw)
        burst(img, t, 2.2, 780, 815, n=10, color=GOLD, dur=0.6, rad=180, seed=115)
    s, al, a = pop(t, 2.5, 0.4)
    if a > 0:
        put(img, tag_spr("SUBSCRIBE", 400, 100, GOLD, 56), 780, 1010, scale=s, alpha=al, shadow=8)
    punch(img, t, 2.7, 940, 710)
    ptext(img, t, 3.4, "SO YOU DON'T MISS", 1260, 84, IVORY, 8, track=2)
    ptext(img, t, 4.0, "THE NEXT ONE", 1390, 112, GOLD, 10, track=4)
    a = seg(t, 4.6, 0.4)
    if a > 0:
        put(img, pill9_spr(), 540, 1540 + 20 * (1 - ease(a)), alpha=ease(a), shadow=10)

SCENES10 = {1: (c1, 273), 2: (c2, 311), 3: (c3, 309), 4: (c4, 210), 5: (c5, 228), 6: (c6, 203)}
DRAW = {k: v[0] for k, v in SCENES10.items()}
DUR = {k: v[1] for k, v in SCENES10.items()}

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES10)
    out_dir = os.environ.get("S10_OUT", "short10")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        fn, nf = SCENES10[k]
        render_seq(zoomed(fn), nf, f"{out_dir}/short10-blocco{k:02d}.mp4")
