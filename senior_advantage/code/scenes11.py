import sys, math, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes10 import *
from engine import ease, ease_back, seg

# =====================================================================
# SHORT 11: Casa-Inverno (correlato al video lungo 7). Stesso motore e colori degli short 5-10, layout NUOVO:
# contatore a 9 pallini in alto (si accendono con le cose nominate, stessi numeri del lungo), neve che cade,
# schede a pannello impilate (B2), scena divisa casa/biforcazione (B3), griglia 3x3 numerata (B4),
# biglietto-video con 9 tessere + telefono (B5), scheda canale con Iscriviti e campanella (B6).
# Durate (fotogrammi, dagli screenshot CapCut del 22/10): 265 307 296 207 266 205. Ultimo elemento entro l'80%.
# Nelle slide compare SOLO cio' che la voce dice. Niente nome del programma, numero di telefono, passi: restano nel lungo.
# uso: S11_OUT=cartella SA_TMP=/tmp/x python3 scenes11.py <clip>
# =====================================================================
ICE = (150, 205, 232)
WARM = (255, 205, 110)
BROWN = (150, 96, 70)
ROOF = (62, 54, 74)
SNOW = (240, 246, 252)

# ------------------------------------------------------------------ testo con centro libero
def xtext(img, t, t0, s, cx, y, size, col, shadow=6, track=0, maxw=560):
    a = seg(t, t0, 0.4)
    if a > 0:
        sp = tspr(s, FONT_SANS, size, col, track=track)
        sc = min(1.0, maxw / sp.width)
        put(img, sp, cx, y + 18 * (1 - ease(a)), scale=sc, alpha=ease(a), shadow=shadow)

# ------------------------------------------------------------------ neve (sfondo)
def flake_spr(r):
    def mk():
        c = Cv(r * 2 + 4, r * 2 + 4)
        c.ell((2, 2, r * 2 + 2, r * 2 + 2), fill=(236, 244, 250))
        return c.done()
    return cache(("flake", r), mk)

def ambient11(img, t, n=34, seed=11, alpha=0.30):
    rnd = random.Random(seed)
    for k in range(n):
        r = rnd.choice([3, 4, 5, 6])
        x0 = rnd.uniform(20, W - 20)
        sp = rnd.uniform(60, 130)
        ph = rnd.uniform(0, 6.28)
        off = rnd.uniform(0, H + 120)
        y = (off + t * sp) % (H + 120) - 60
        x = x0 + math.sin(t * 0.9 + ph) * 26
        put(img, flake_spr(r), x, y, alpha=alpha * (0.6 + 0.4 * (r / 6)))

# ------------------------------------------------------------------ icone 1-9 (stessi numeri del lungo)
def icon(c, k, cx, cy, u, col, acc):
    if k == 1:   # allarme antifumo
        c.ell((cx - u, cy - u, cx + u, cy + u), fill=col)
        c.ell((cx - 0.35 * u, cy - 0.35 * u, cx + 0.35 * u, cy + 0.35 * u), fill=acc)
        for r in (1.35, 1.7):
            c.arc((cx - r * u, cy - r * u, cx + r * u, cy + r * u), 215, 325, col, 0.14 * u)
    elif k == 2:  # maglietta (bucato)
        c.poly([(cx - 1.0 * u, cy - 0.6 * u), (cx - 0.45 * u, cy - 1.0 * u), (cx + 0.45 * u, cy - 1.0 * u), (cx + 1.0 * u, cy - 0.6 * u),
                (cx + 0.7 * u, cy - 0.1 * u), (cx + 0.5 * u, cy - 0.25 * u), (cx + 0.5 * u, cy + 1.0 * u), (cx - 0.5 * u, cy + 1.0 * u),
                (cx - 0.5 * u, cy - 0.25 * u), (cx - 0.7 * u, cy - 0.1 * u)], fill=col)
    elif k == 3:  # secchio
        c.poly([(cx - 0.9 * u, cy - 0.5 * u), (cx + 0.9 * u, cy - 0.5 * u), (cx + 0.65 * u, cy + 1.0 * u), (cx - 0.65 * u, cy + 1.0 * u)], fill=col)
        c.arc((cx - 0.8 * u, cy - 1.2 * u, cx + 0.8 * u, cy + 0.2 * u), 180, 360, col, 0.14 * u)
    elif k == 4:  # piatto con cloche
        c.d.pieslice(c._b((cx - 1.0 * u, cy - 0.9 * u, cx + 1.0 * u, cy + 1.1 * u)), 180, 360, fill=col)
        c.rrect((cx - 1.25 * u, cy + 0.12 * u, cx + 1.25 * u, cy + 0.3 * u), 2, fill=col)
        c.ell((cx - 0.14 * u, cy - 1.15 * u, cx + 0.14 * u, cy - 0.87 * u), fill=col)
    elif k == 5:  # maniglione
        c.rrect((cx - 1.1 * u, cy - 0.18 * u, cx + 1.1 * u, cy + 0.18 * u), 0.18 * u, fill=col)
        for sx in (-0.85, 0.85):
            c.rrect((cx + sx * u - 0.12 * u, cy - 0.18 * u, cx + sx * u + 0.12 * u, cy + 0.9 * u), 2, fill=col)
    elif k == 6:  # bilancia
        c.rrect((cx - 0.09 * u, cy - 1.0 * u, cx + 0.09 * u, cy + 0.9 * u), 2, fill=col)
        c.rrect((cx - 0.7 * u, cy + 0.8 * u, cx + 0.7 * u, cy + 1.0 * u), 2, fill=col)
        c.rrect((cx - 1.1 * u, cy - 0.8 * u, cx + 1.1 * u, cy - 0.66 * u), 2, fill=col)
        for sx in (-1.0, 1.0):
            c.d.pieslice(c._b((cx + sx * u - 0.45 * u, cy - 0.15 * u, cx + sx * u + 0.45 * u, cy + 0.75 * u)), 0, 180, fill=col)
    elif k == 7:  # cuore
        c.ell((cx - 1.05 * u, cy - 0.9 * u, cx + 0.05 * u, cy + 0.2 * u), fill=col)
        c.ell((cx - 0.05 * u, cy - 0.9 * u, cx + 1.05 * u, cy + 0.2 * u), fill=col)
        c.poly([(cx - 1.0 * u, cy - 0.1 * u), (cx + 1.0 * u, cy - 0.1 * u), (cx, cy + 1.1 * u)], fill=col)
    elif k == 8:  # lucchetto
        c.rrect((cx - 0.85 * u, cy - 0.15 * u, cx + 0.85 * u, cy + 1.0 * u), 0.15 * u, fill=col)
        c.arc((cx - 0.55 * u, cy - 1.0 * u, cx + 0.55 * u, cy + 0.3 * u), 180, 360, col, 0.2 * u)
        c.ell((cx - 0.14 * u, cy + 0.25 * u, cx + 0.14 * u, cy + 0.53 * u), fill=acc)
    elif k == 9:  # fiamma
        c.poly([(cx, cy - 1.2 * u), (cx + 0.75 * u, cy - 0.1 * u), (cx + 0.9 * u, cy + 0.5 * u), (cx + 0.5 * u, cy + 1.05 * u),
                (cx - 0.5 * u, cy + 1.05 * u), (cx - 0.9 * u, cy + 0.5 * u), (cx - 0.7 * u, cy - 0.1 * u), (cx - 0.25 * u, cy + 0.2 * u)], fill=col)
        c.poly([(cx, cy + 0.1 * u), (cx + 0.38 * u, cy + 0.65 * u), (cx, cy + 1.0 * u), (cx - 0.38 * u, cy + 0.65 * u)], fill=acc)

def tile_spr(k, size, lit=True):
    def mk():
        c = Cv(size, size)
        c.rrect((3, 3, size - 3, size - 3), size * 0.16, fill=GOLD if lit else CARD, outline=CRUST_D if lit else SAGE_D, width=max(3, size // 28))
        icon(c, k, size / 2, size / 2 + size * 0.05, size * 0.24, DARK if lit else SAGE_D, GOLD if lit else CARD)
        c.ell((size * 0.04, size * 0.04, size * 0.30, size * 0.30), fill=DARK)
        c.text((size * 0.17, size * 0.18), str(k), FONT_SANS, int(size * 0.17), IVORY if lit else SAGE)
        return c.done()
    return cache(("tile11", k, size, lit), mk)

# ------------------------------------------------------------------ contatore a 9 pallini
def mdot_spr(k, lit):
    def mk():
        c = Cv(76, 76)
        c.ell((3, 3, 73, 73), fill=GOLD if lit else CARD, outline=CRUST_D if lit else SAGE_D, width=5)
        c.text((38, 40), str(k), FONT_SANS, 38, DARK if lit else SAGE)
        return c.done()
    return cache(("mdot", k, lit), mk)

def meter(img, t, lit_times, t0=0.0, y=150):
    """lit_times: dict k -> istante in cui il pallino k si accende (non presenti = spenti)"""
    a = seg(t, t0, 0.35)
    if a <= 0:
        return
    for k in range(1, 10):
        x = 540 + (k - 5) * 104
        lt = lit_times.get(k)
        on = lt is not None and t >= lt
        sc = 1.0
        if on:
            u = seg(t, lt, 0.4)
            sc = 1.0 + 0.35 * math.sin(math.pi * min(1.0, u))
        put(img, mdot_spr(k, on), x, y - 24 * (1 - ease(a)), scale=sc, alpha=ease(a), shadow=6)
        if on and lt is not None and seg(t, lt, 0.7) < 1.0:
            burst(img, t, lt, x, y, n=8, color=GOLD, dur=0.6, rad=90, seed=200 + k)

# ------------------------------------------------------------------ sprite
def house_spr():
    def mk():
        w, h = 720, 520
        c = Cv(w, h)
        c.rrect((0, h - 86, w, h - 6), 40, fill=SNOW)
        c.rrect((90, 210, w - 90, h - 60), 6, fill=BROWN, outline=DARK, width=7)
        c.poly([(46, 224), (w / 2, 56), (w - 46, 224)], fill=ROOF)
        c.line([46, 224, w / 2, 56, w - 46, 224, 46, 224], DARK, 7)
        c.poly([(96, 208), (w / 2, 82), (w - 96, 208), (w - 134, 208), (w / 2, 116), (134, 208)], fill=SNOW)
        c.rrect((w - 196, 92, w - 156, 176), 4, fill=(120, 70, 60), outline=DARK, width=5)
        c.rrect((w - 206, 82, w - 146, 102), 4, fill=SNOW, outline=DARK, width=4)
        c.rrect((150, 262, 300, 396), 10, fill=WARM, outline=DARK, width=7)
        c.line([225, 262, 225, 396], DARK, 5); c.line([150, 329, 300, 329], DARK, 5)
        c.ell((236, 282, 276, 322), fill=(120, 80, 60)); c.rrect((228, 320, 284, 396), 14, fill=(120, 80, 60))
        c.rrect((w - 290, 270, w - 176, h - 60), 10, fill=(90, 52, 40), outline=DARK, width=7)
        c.ell((w - 204, 352, w - 190, 366), fill=GOLD)
        return c.done()
    return cache("house11", mk)

def plus_spr():
    def mk():
        c = Cv(190, 190)
        c.ell((4, 4, 186, 186), fill=GOLD, outline=CRUST_D, width=6)
        c.rrect((78, 38, 112, 152), 6, fill=DARK); c.rrect((38, 78, 152, 112), 6, fill=DARK)
        return c.done()
    return cache("plus11", mk)

def age_badge11():
    def mk():
        c = Cv(260, 260)
        c.ell((4, 4, 256, 256), fill=CORAL, outline=DARK, width=7)
        c.text((130, 100), "OVER", FONT_SANS, 46, IVORY, track=5)
        c.text((130, 170), "60", FONT_SANS, 100, IVORY)
        return c.done()
    return cache("age11", mk)

def pine_spr():
    def mk():
        c = Cv(220, 380)
        c.rrect((96, 300, 124, 372), 4, fill=(96, 62, 46))
        for k, (y, w) in enumerate(((40, 150), (110, 190), (190, 210))):
            c.poly([(110, y), (110 + w / 2, y + 120), (110 - w / 2, y + 120)], fill=(20, 82, 62))
            c.poly([(110, y), (110 + w / 4, y + 52), (110 - w / 4, y + 52)], fill=SNOW)
        return c.done()
    return cache("pine11", mk)

def moon_spr():
    def mk():
        c = Cv(160, 160)
        c.ell((10, 10, 150, 150), fill=(250, 240, 200))
        c.ell((52, 4, 164, 126), fill=(0, 0, 0, 0))
        return c.done()
    return cache("moon11", mk)

def alarm_scene_spr():
    def mk():
        c = Cv(300, 300)
        c.rrect((20, 24, 290, 52), 6, fill=(200, 196, 184), outline=DARK, width=4)      # soffitto
        icon(c, 1, 180, 116, 40, IVORY, CORAL)                                           # allarme
        c.line([48, 292, 82, 118], (160, 112, 60), 10); c.line([116, 292, 128, 118], (160, 112, 60), 10)   # scala
        for yy in (150, 190, 230, 268):
            c.line([54 + (yy - 150) * -0.04, yy, 122 + (yy - 150) * -0.04, yy], (160, 112, 60), 8)
        c.ell((70, 72, 118, 120), fill=SKIN)                                              # persona sulla scala
        c.rrect((60, 118, 126, 190), 18, fill=(60, 140, 200))
        c.line([112, 128, 160, 106], SKIN, 12)
        return c.done()
    return cache("alarmscene11", mk)

def meal_scene_spr():
    def mk():
        c = Cv(300, 300)
        c.rrect((8, 20, 150, 292), 14, fill=(90, 52, 40), outline=DARK, width=6)         # porta
        c.rrect((28, 44, 130, 150), 8, fill=(120, 76, 56))
        c.ell((118, 168, 134, 184), fill=GOLD)
        c.rrect((166, 230, 292, 262), 10, fill=(214, 164, 96), outline=DARK, width=5)     # vassoio
        icon(c, 4, 230, 218, 46, IVORY, IVORY)
        for k, x in enumerate((206, 232, 258)):
            c.line([x, 150, x - 10, 124, x + 10, 100, x, 76], (230, 236, 232), 6)         # vapore
        return c.done()
    return cache("mealscene11", mk)

def legal_scene_spr():
    def mk():
        c = Cv(300, 300)
        c.rrect((190, 70, 290, 276), 10, fill=IVORY, outline=DARK, width=5)               # documento
        for k in range(5):
            c.rrect((204, 96 + k * 34, 276 - (k % 2) * 28, 108 + k * 34), 3, fill=(190, 198, 192))
        icon(c, 6, 100, 140, 76, GOLD, DARK)
        return c.done()
    return cache("legalscene11", mk)

def pcard_spr(w, h, border=GOLD, fill=None):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 40, fill=fill or CARD, outline=border, width=6)
        return c.done()
    return cache(("pcard11", w, h, border, fill), mk)

def furnace_spr():
    def mk():
        c = Cv(420, 420)
        c.rrect((40, 40, 380, 400), 26, fill=(128, 138, 136), outline=DARK, width=8)
        c.rrect((70, 70, 350, 160), 12, fill=(98, 108, 106))
        for k in range(6):
            c.rrect((92 + k * 44, 88, 112 + k * 44, 142), 4, fill=(70, 78, 76))
        c.rrect((70, 190, 350, 372), 16, fill=(60, 68, 66), outline=DARK, width=5)
        # fiamma spenta (grigia) + cristalli di ghiaccio
        icon(c, 9, 210, 286, 62, (96, 106, 104), (60, 68, 66))
        for (x, y, r) in ((110, 226, 16), (310, 330, 14), (330, 230, 12)):
            c.line([x - r, y, x + r, y], ICE, 5); c.line([x, y - r, x, y + r], ICE, 5)
            c.line([x - r * .7, y - r * .7, x + r * .7, y + r * .7], ICE, 4); c.line([x - r * .7, y + r * .7, x + r * .7, y - r * .7], ICE, 4)
        for k in range(5):  # ghiaccioli
            x = 70 + k * 70
            c.poly([(x, 40), (x + 22, 40), (x + 11, 40 + 36 + (k % 2) * 22)], fill=ICE)
        return c.done()
    return cache("furnace11", mk)

def thermo_spr(fill_frac):
    key = round(fill_frac * 40)
    def mk():
        c = Cv(130, 400)
        c.rrect((38, 6, 92, 320), 26, fill=IVORY, outline=DARK, width=6)
        c.ell((10, 280, 120, 392), fill=ICE, outline=DARK, width=6)
        top = 300 - key / 40 * 260
        c.rrect((54, top, 76, 330), 8, fill=ICE)
        c.ell((24, 294, 106, 378), fill=ICE)
        for k in range(6):
            c.line([92, 40 + k * 44, 108, 40 + k * 44], DARK, 5)
        return c.done()
    return cache(("thermo11", key), mk)

def calendar11_spr():
    def mk():
        c = Cv(290, 340)
        c.rrect((6, 6, 284, 334), 22, fill=IVORY, outline=DARK, width=6)
        c.rrect((6, 6, 284, 96), 22, fill=CORAL)
        c.rrect((6, 60, 284, 96), 2, fill=CORAL)
        c.text((145, 52), "JANUARY", FONT_SANS, 40, IVORY, track=2)
        for r in range(4):
            for q in range(5):
                c.rrect((28 + q * 46, 120 + r * 50, 56 + q * 46, 148 + r * 50), 5, fill=(206, 212, 206))
        c.ell((196, 214, 258, 276), outline=CORAL, width=7)
        return c.done()
    return cache("cal11", mk)

def van_spr():
    def mk():
        c = Cv(380, 240)
        c.rrect((10, 40, 270, 190), 18, fill=IVORY, outline=DARK, width=6)
        c.poly([(266, 76), (330, 76), (370, 130), (370, 190), (266, 190)], fill=IVORY)
        c.line([266, 76, 330, 76, 370, 130, 370, 190, 266, 190], DARK, 6)
        c.rrect((290, 92, 338, 130), 6, fill=(150, 205, 232))
        c.rrect((10, 150, 370, 168), 4, fill=CORAL)
        for x in (80, 300):
            c.ell((x - 32, 164, x + 32, 228), fill=DARK, outline=STEEL, width=6)
        c.line([70, 80, 120, 130], DARK, 12)          # chiave inglese
        c.ell((52, 62, 88, 98), fill=DARK); c.ell((60, 70, 80, 90), fill=IVORY)
        c.rrect((110, 74, 240, 96), 6, fill=(190, 198, 192))
        return c.done()
    return cache("van11", mk)

def phone11_spr():
    def mk():
        c = Cv(300, 520)
        c.rrect((6, 6, 294, 514), 44, fill=(20, 28, 26), outline=GOLD, width=7)
        c.rrect((26, 56, 274, 464), 22, fill=(22, 82, 64))
        c.ell((100, 96, 200, 196), fill=(110, 200, 130), outline=DARK, width=5)
        c.arc((122, 118, 178, 174), 200, 340, DARK, 12)
        c.text((150, 252), "ONE CALL", FONT_SANS, 40, IVORY, track=2)
        for k in range(9):
            c.ell((46 + k * 25, 312, 62 + k * 25, 328), fill=SAGE)
        for k in range(4):
            c.ell((72 + k * 40, 356, 92 + k * 40, 376), fill=SAGE_D)
        c.rrect((90, 420, 210, 448), 14, fill=(110, 200, 130))
        c.ell((130, 484, 170, 500), fill=(60, 70, 68))
        return c.done()
    return cache("phone11", mk)

def vcard11_spr():
    def mk():
        c = Cv(900, 640)
        c.rrect((4, 4, 896, 636), 44, fill=CARD, outline=GOLD, width=7)
        c.rrect((30, 30, 870, 410), 28, fill=(22, 82, 64))
        c.ell((360, 52, 540, 232), fill=GOLD, outline=CRUST_D, width=6)
        c.poly([(424, 94), (424, 190), (502, 142)], fill=DARK)
        for k in range(9):
            x = 70 + k * 86
            c.rrect((x, 270, x + 74, 344), 12, fill=GOLD)
            icon(c, k + 1, x + 37, 310, 15, DARK, GOLD)
        c.rrect((40, 380, 860, 388), 3, fill=SAGE_D)
        c.rrect((40, 380, 520, 388), 3, fill=GOLD)
        c.text((450, 482), "ALL 9 IN ONE VIDEO", FONT_SANS, 64, GOLD, track=3)
        c.text((450, 570), "NINE KINDS OF HELP", FONT_SANS, 36, SAGE, track=3)
        return c.done()
    return cache("vcard11", mk)

def channel11_spr(subscribed):
    def mk():
        c = Cv(900, 360)
        c.rrect((4, 4, 896, 356), 40, fill=CARD, outline=GOLD, width=7)
        c.ell((40, 60, 240, 260), fill=(22, 82, 64), outline=GOLD, width=7)
        c.text((140, 162), "SA", FONT_SANS, 84, GOLD)
        c.text((570, 150), "The Senior Advantage", FONT_SANS, 46, IVORY)
        if subscribed:
            c.rrect((300, 232, 760, 320), 44, fill=(60, 80, 74), outline=SAGE_D, width=5)
            c.text((530, 276), "SUBSCRIBED", FONT_SANS, 44, IVORY, track=2)
            c.line([330, 276, 346, 292, 372, 258], GOLD, 8)
        else:
            c.rrect((300, 232, 760, 320), 44, fill=(214, 62, 52), outline=DARK, width=5)
            c.text((530, 276), "SUBSCRIBE", FONT_SANS, 48, IVORY, track=3)
        return c.done()
    return cache(("chan11", subscribed), mk)

def hand_tap_spr():
    return hand_spr()

# ---------------------------------------------------------------- B1 (265 f = 8,8 s)
def c1(img, t):
    ambient11(img, t)
    meter(img, t, {k: 0.35 + 0.14 * k for k in range(1, 10)}, 0.0)
    s, al, a = pop(t, 0.5, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 560, scale=1.7, alpha=0.30 * al)
        put(img, tspr("9", FONT_SANS, 520, GOLD), 540, 560, scale=s, alpha=al, shadow=14)
        burst(img, t, 0.5, 540, 560, n=14, color=GOLD, dur=0.8, rad=420, seed=301)
    s, al, a = pop(t, 1.0, 0.5)
    if a > 0:
        put(img, moon_spr(), 900, 330, scale=0.9 * s, alpha=al * 0.95, shadow=6)
    ptext(img, t, 1.5, "KINDS OF HELP", 850, 96, IVORY, 10, track=4)
    s, al, a = pop(t, 2.4, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1280, scale=1.5, alpha=0.22 * al)
        put(img, pine_spr(), 175, 1390, scale=0.9 * s, alpha=al, shadow=10)
        put(img, pine_spr(), 905, 1410, scale=0.8 * s, alpha=al, shadow=10)
        put(img, house_spr(), 540, 1290, scale=1.1 * s, alpha=al, shadow=14, rot=-2 * (1 - ease(a)))
    s, al, a = pop(t, 3.0, 0.5)
    if a > 0:
        put(img, plus_spr(), 540, 1010, scale=0.62 * s, alpha=al, shadow=8)
        burst(img, t, 3.0, 540, 1010, n=10, color=GOLD, dur=0.6, rad=170, seed=302)
    ptext(img, t, 3.3, "TO YOUR HOME THIS WINTER", 1640, 56, GOLD, 8, track=1)
    s, al, a = pop(t, 4.5, 0.5)
    if a > 0:
        put(img, age_badge11(), 900, 1120, scale=0.7 * s, alpha=al, shadow=10, rot=6)
    s, al, a = pop(t, 6.0, 0.5)
    if a > 0:
        put(img, stamp_spr("NEVER HEARD OF A SINGLE ONE", 960, 120, CORAL), 540, 1770, scale=min(1.0, s), alpha=al, rot=-2, shadow=12)

# ---------------------------------------------------------------- B2 (307 f = 10,2 s)
def card_in(img, t, t0, y, scene, items, lit_k, lit_t):
    s_, al, a = pop(t, t0, 0.5)
    if a <= 0:
        return
    sc = min(1.0, s_)
    put(img, pcard_spr(940, 380), 540, y, scale=sc, alpha=al, shadow=12)
    put(img, scene, 540 - 305 * sc, y, scale=1.1 * sc, alpha=al)
    if a >= 1.0 and t > t0 + 0.5:
        pass

def c2(img, t):
    ambient11(img, t, seed=12)
    meter(img, t, {1: 1.2, 4: 4.9, 6: 7.6}, 0.0)
    # scheda 1: allarmi
    card_in(img, t, 0.3, 560, alarm_scene_spr(), None, 1, 1.2)
    xtext(img, t, 1.0, "SMOKE ALARMS", 700, 520, 62, GOLD, track=2, maxw=520)
    xtext(img, t, 1.5, "INSTALLED IN YOUR HOME", 700, 590, 34, IVORY, track=1, maxw=520)
    s, al, a = pop(t, 3.0, 0.45)
    if a > 0:
        put(img, tag_spr("AT NO CHARGE", 360, 74, GOLD, 40), 700, 668, scale=s, alpha=al, shadow=8)
    # scheda 2: pasto
    card_in(img, t, 4.2, 1000, meal_scene_spr(), None, 4, 4.9)
    xtext(img, t, 4.8, "A HOT MEAL", 700, 970, 66, GOLD, track=2, maxw=520)
    xtext(img, t, 5.3, "AT YOUR DOOR", 700, 1050, 46, IVORY, track=2, maxw=520)
    # scheda 3: legale
    card_in(img, t, 6.8, 1440, legal_scene_spr(), None, 6, 7.6)
    xtext(img, t, 7.3, "LEGAL HELP", 700, 1410, 66, GOLD, track=2, maxw=520)
    xtext(img, t, 7.7, "FOR LEGAL PROBLEMS", 700, 1490, 34, IVORY, track=1, maxw=520)

# ---------------------------------------------------------------- B3 (296 f = 9,9 s)
def c3(img, t):
    ambient11(img, t, seed=14)
    meter(img, t, {1: 0.0, 4: 0.0, 6: 0.0, 9: 4.4}, 0.0)
    s, al, a = pop(t, 0.3, 0.5)
    if a > 0:
        put(img, calendar11_spr(), 185, 660, scale=0.95 * s, alpha=al, shadow=12, rot=-4)
    s, al, a = pop(t, 0.9, 0.55)
    if a > 0:
        put(img, furnace_spr(), 590, 650, scale=1.2 * s, alpha=al, shadow=14)
    ptext(img, t, 1.6, "THE FURNACE STOPS", 960, 84, IVORY, 10, track=3)
    a = seg(t, 2.0, 0.4)
    if a > 0:
        fr = 1.0 - 0.9 * ease(seg(t, 2.2, 1.6))
        put(img, thermo_spr(fr), 940, 650, scale=1.0, alpha=ease(a), shadow=8)
    s, al, a = pop(t, 3.9, 0.5)
    if a > 0:
        put(img, glow_spr(), 540, 1090, scale=1.2, alpha=0.25 * al)
        put(img, tag_spr("THERE MAY BE HELP", 800, 120, GOLD, 62), 540, 1090, scale=min(1.0, s), alpha=al, rot=-2, shadow=12)
        burst(img, t, 3.9, 540, 1090, n=12, color=GOLD, dur=0.7, rad=300, seed=303)
    # biforcazione: prima la ditta di riparazioni
    s_, al_, a = pop(t, 5.9, 0.5)
    if a > 0:
        sc = min(1.0, s_)
        put(img, pcard_spr(940, 340, border=CORAL), 540, 1370, scale=sc, alpha=al_, shadow=12)
        put(img, van_spr(), 540 - 240 * sc, 1370, scale=0.95 * sc, alpha=al_)
    xtext(img, t, 6.4, "REPAIR COMPANY", 745, 1335, 58, IVORY, track=2, maxw=450)
    xtext(img, t, 6.8, "FIRST", 745, 1420, 84, CORAL, track=4, maxw=450)
    s, al, a = pop(t, 7.5, 0.5)
    if a > 0:
        put(img, stamp_spr("A BIG BILL YOU NEVER NEEDED", 960, 120, CORAL), 540, 1660, scale=min(1.0, s), alpha=al, rot=-2, shadow=12)
        burst(img, t, 7.5, 540, 1660, n=10, color=CORAL, dur=0.7, rad=170, seed=304)

# ---------------------------------------------------------------- B4 (207 f = 6,9 s)
def c4(img, t):
    ambient11(img, t, seed=16)
    ptext(img, t, 0.2, "FOUR OF NINE", 260, 110, GOLD, 10, track=3)
    lit = {1: 0.9, 4: 1.1, 6: 1.3, 9: 1.5}
    size, gap = 290, 30
    x0 = 540 - (size + gap)
    y0 = 700
    for k in range(1, 10):
        r, q = divmod(k - 1, 3)
        cx, cy = x0 + q * (size + gap), y0 + r * (size + gap) - 20
        a = seg(t, 0.35 + 0.05 * k, 0.35)
        if a <= 0:
            continue
        on = k in lit and t >= lit[k]
        sc = 1.0
        if on:
            sc = 1.0 + 0.18 * math.sin(math.pi * min(1.0, seg(t, lit[k], 0.4)))
        put(img, tile_spr(k, size, on) if on else num_tile(k, size), cx, cy, scale=sc * (0.6 + 0.4 * ease(a)), alpha=ease(a), shadow=8)
        if on and seg(t, lit[k], 0.7) < 1.0:
            burst(img, t, lit[k], cx, cy, n=8, color=GOLD, dur=0.6, rad=150, seed=400 + k)
    ptext(img, t, 2.4, "MOST SENIORS NEVER ASK", 1560, 64, IVORY, 8, track=1)
    s, al, a = pop(t, 4.5, 0.5)
    if a > 0:
        put(img, stamp_spr("NOT BECAUSE THEY DON'T QUALIFY", 1000, 112, CORAL), 540, 1710, scale=min(1.0, s), alpha=al, rot=-2, shadow=12)
        burst(img, t, 4.5, 540, 1710, n=10, color=CORAL, dur=0.7, rad=150, seed=410)

def num_tile(k, size):
    def mk():
        c = Cv(size, size)
        c.rrect((3, 3, size - 3, size - 3), size * 0.16, fill=CARD, outline=SAGE_D, width=max(3, size // 28))
        c.text((size / 2, size / 2 + 4), str(k), FONT_SANS, int(size * 0.5), SAGE_D)
        return c.done()
    return cache(("numtile11", k, size), mk)

# ---------------------------------------------------------------- B5 (266 f = 8,9 s)
def c5(img, t):
    ambient11(img, t, seed=18)
    meter(img, t, {k: 0.5 + 0.08 * k for k in range(1, 10)}, 0.0)
    s, al, a = pop(t, 0.4, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 640, scale=1.5, alpha=0.28 * al)
        put(img, vcard11_spr(), 540, 640, scale=0.98 * s, alpha=al, shadow=18, rot=-2 * (1 - ease(a)))
        burst(img, t, 0.4, 540, 640, n=12, color=GOLD, dur=0.7, rad=440, seed=311)
    s, al, a = pop(t, 3.3, 0.5)
    if a > 0:
        put(img, phone11_spr(), 270, 1250, scale=0.78 * s, alpha=al, shadow=12, rot=-4)
        burst(img, t, 3.3, 270, 1250, n=10, color=GOLD, dur=0.6, rad=200, seed=312)
    xtext(img, t, 3.7, "ONE", 720, 1150, 80, GOLD, track=4, maxw=480)
    xtext(img, t, 4.1, "PHONE CALL", 720, 1240, 64, IVORY, track=2, maxw=480)
    xtext(img, t, 4.9, "OPENS THE DOOR", 720, 1330, 42, SAGE, track=1, maxw=480)
    xtext(img, t, 5.3, "TO MOST OF THEM", 720, 1386, 42, SAGE, track=1, maxw=480)
    ptext(img, t, 5.9, "RIGHT BELOW", 1520, 104, GOLD, 12, track=4)
    ptext(img, t, 6.8, "TAP IT NOW", 1620, 84, IVORY, 10, track=4)
    for k in range(3):
        a = seg(t, 6.9 + k * 0.1, 0.35)
        if a > 0:
            put(img, chevron_spr(), 540, 1700 + k * 44 + 16 * (1 - ease(a)), alpha=ease(a) * (1 - 0.25 * k), scale=0.55)

# ---------------------------------------------------------------- B6 (205 f = 6,8 s)
def c6(img, t):
    ambient11(img, t, seed=20)
    s, al, a = pop(t, 1.3, 0.55)
    if a > 0:
        put(img, glow_spr(), 540, 470, scale=1.8, alpha=0.3 * al)
        put(img, thumb_spr(), 540, 470, scale=1.5 * s, alpha=al, shadow=14, rot=-6 * (1 - ease(a)) - 4)
        burst(img, t, 1.3, 540, 470, n=14, color=GOLD, dur=0.8, rad=360, seed=321)
    s, al, a = pop(t, 1.7, 0.45)
    if a > 0:
        put(img, tag_spr("LIKE", 340, 120, GOLD, 70), 540, 800, scale=s, alpha=al, shadow=10)
    s, al, a = pop(t, 2.4, 0.55)
    if a > 0:
        put(img, channel11_spr(t >= 3.3), 540, 1130, scale=min(1.04, s * 1.04), alpha=al, shadow=14)
    a = seg(t, 2.9, 0.8)
    if 0 < a < 1.0 or (a >= 1.0 and t < 3.4):
        u = ease(min(1.0, a))
        put(img, hand_spr(), 790 + 40 * (1 - u), 1265 + 150 * (1 - u), scale=0.6, alpha=min(1.0, a * 3))
    if t >= 3.3:
        burst(img, t, 3.3, 530, 1206, n=10, color=GOLD, dur=0.6, rad=200, seed=322)
    s, al, a = pop(t, 3.9, 0.5)
    if a > 0:
        sw = 10 * math.sin((t - 4.2) * 18) * max(0.0, 1 - (t - 4.2) / 1.0) if t > 4.2 else 0
        put(img, bell_spr(), 905, 985, scale=0.62 * s, alpha=al, rot=sw)
    ptext(img, t, 4.6, "SO YOU DON'T MISS", 1470, 80, IVORY, 8, track=2)
    ptext(img, t, 5.2, "THE NEXT ONE", 1600, 112, GOLD, 10, track=4)

SCENES11 = {1: (c1, 265), 2: (c2, 307), 3: (c3, 296), 4: (c4, 207), 5: (c5, 266), 6: (c6, 205)}
DRAW = {k: v[0] for k, v in SCENES11.items()}
DUR = {k: v[1] for k, v in SCENES11.items()}

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES11)
    out_dir = os.environ.get("S11_OUT", "short11")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        fn, nf = SCENES11[k]
        render_seq(zoomed(fn), nf, f"{out_dir}/short11-blocco{k:02d}.mp4")
