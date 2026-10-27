import sys, math, random, os, re, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes12 as S
from scenes12 import *
from scenes11 import xtext
from PIL import Image, ImageDraw, ImageFilter

# =====================================================================
# SHORT 13: Aldi (correlato al lungo 9). Ordine utente 26/10: "slide professionali e l'elemento professionali, usa il
# colore del video" -> stessi colori del lungo Aldi (verde-petrolio, avorio, oro), sfondo "carta millimetrata" che scorre,
# testata a pannello di vetro con barra di avanzamento 1-10 (come il lungo), schede di carta avorio. Niente blu/viola.
# Durate (fotogrammi) lette dagli screenshot CapCut del 26/10 (righello + pixel concordi, fine blocco = punto di fine barra,
# valori frazionari arrotondati al fotogramma piu vicino): 349 227 323 196 195 224 204 (totale 1718).
# Nelle slide compare SOLO cio' che la voce dice. Nomi/condizioni restano nel lungo. Ultimo elemento entro l'80%.
# uso: S13_OUT=cartella python3 scenes13.py <blocco>
# =====================================================================
HERE = os.path.dirname(os.path.abspath(__file__))
S.TEXT.clear()
S.TEXT.update({int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$",
        open(os.path.join(HERE, "..", "COPIONE-SHORT-13-ALDI.md"), encoding="utf-8").read())})
S.DUR.clear()
S.DUR.update({1: 349, 2: 227, 3: 323, 4: 196, 5: 195, 6: 224, 7: 204})
DUR = S.DUR
TEXT = S.TEXT
T = S.T
bob, env, pp, bst = S.bob, S.env, S.pp, S.bst
D = S.D

TEAL = (22, 92, 80)
TEAL_L = (70, 150, 130)
GLASS = (6, 40, 37)
KRAFT = (205, 160, 100)
KRAFT_D = (140, 98, 50)
GOLD_D = (190, 140, 60)
MONEY = (96, 170, 120)
MONEY_D = (40, 100, 70)

# ------------------------------------------------------------------ sfondo carta millimetrata verde-petrolio (colori del lungo Aldi)
_B13 = {}
def background13(t):
    if not _B13:
        base = Image.new("RGB", (W, H)); d = ImageDraw.Draw(base)
        for y in range(H):
            k = y / H
            d.line([(0, y), (W, y)], fill=(int(6 + 7 * (1 - k)), int(34 + 22 * (1 - k)), int(30 + 19 * (1 - k))))
        glow = Image.new("L", (W, H), 0); gd = ImageDraw.Draw(glow)
        gd.ellipse([-W * 0.2, -H * 0.15, W * 1.2, H * 0.45], fill=80)
        glow = glow.filter(ImageFilter.GaussianBlur(190))
        base = Image.composite(Image.new("RGB", (W, H), (46, 126, 108)), base, glow)
        vig = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(vig)
        vd.rectangle([0, 0, W, H], fill=150); vd.ellipse([-W * 0.4, -H * 0.1, W * 1.4, H * 1.1], fill=0)
        vig = vig.filter(ImageFilter.GaussianBlur(160))
        base = Image.composite(Image.new("RGB", (W, H), (2, 14, 12)), base, vig)
        _B13["base"] = base
        g1 = Image.new("RGBA", (W + 60, H + 60), (0, 0, 0, 0)); d1 = ImageDraw.Draw(g1)
        for x in range(0, W + 60, 60):
            d1.line([(x, 0), (x, H + 60)], fill=(150, 215, 185, 15), width=1)
        for y in range(0, H + 60, 60):
            d1.line([(0, y), (W + 60, y)], fill=(150, 215, 185, 15), width=1)
        _B13["g1"] = g1
        g2 = Image.new("RGBA", (W + 240, H + 240), (0, 0, 0, 0)); d2 = ImageDraw.Draw(g2)
        for x in range(0, W + 240, 240):
            d2.line([(x, 0), (x, H + 240)], fill=(170, 225, 200, 30), width=2)
        for y in range(0, H + 240, 240):
            d2.line([(0, y), (W + 240, y)], fill=(170, 225, 200, 30), width=2)
        for x in range(0, W + 240, 240):
            for y in range(0, H + 240, 240):
                d2.line([(x - 9, y), (x + 9, y)], fill=(228, 179, 99, 90), width=3)
                d2.line([(x, y - 9), (x, y + 9)], fill=(228, 179, 99, 90), width=3)
        _B13["g2"] = g2
        bl = Image.new("RGBA", (900, 900), (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)
        bd.ellipse([150, 150, 750, 750], fill=(70, 160, 130, 64))
        _B13["blob"] = bl.filter(ImageFilter.GaussianBlur(120))
        sw = Image.new("RGBA", (W + 600, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sw)
        sd.polygon([(300, 0), (460, 0), (160, H), (0, H)], fill=(255, 245, 210, 18))
        _B13["sweep"] = sw.filter(ImageFilter.GaussianBlur(40))
    img = _B13["base"].copy()
    o1 = (t * 15) % 60; o2 = (t * 26) % 240
    img.paste(_B13["g1"].crop((int(o1), int(o1), int(o1) + W, int(o1) + H)), (0, 0), _B13["g1"].crop((int(o1), int(o1), int(o1) + W, int(o1) + H)))
    c2 = _B13["g2"].crop((int(o2), int(o2), int(o2) + W, int(o2) + H))
    img.paste(c2, (0, 0), c2)
    for k in range(2):
        bx = W * (0.25 + 0.5 * k) + 150 * math.sin(t * 0.35 + k * 2.1) - 450
        by = H * (0.30 + 0.38 * k) + 120 * math.cos(t * 0.3 + k) - 450
        img.paste(_B13["blob"], (int(bx), int(by)), _B13["blob"])
    sx = int((t * 150) % (W + 700)) - 600
    img.paste(_B13["sweep"], (sx, 0), _B13["sweep"])
    return img

def render13(draw_fn, nframes, out):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30",
           "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes):
        t = i / 30.0
        img = background13(t)
        draw_fn(img, t)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()

# ------------------------------------------------------------------ testata a pannello di vetro + barra 1-10
def hdr_spr():
    def mk():
        c = Cv(960, 210)
        c.rrect((3, 3, 957, 207), 40, fill=GLASS + (238,), outline=TEAL_L, width=5)
        c.line([50, 188, 910, 188], GOLD, 4)
        return c.done()
    return S.cache("hdr13", mk)

def pill_spr(state):
    def mk():
        c = Cv(66, 32)
        if state == "gold":
            c.rrect((2, 2, 64, 30), 14, fill=GOLD, outline=GOLD_D, width=3)
        else:
            c.rrect((2, 2, 64, 30), 14, fill=TEAL, outline=TEAL_L, width=3)
        return c.done()
    return S.cache(("pill13", state), mk)

def header13(img, t, title, pills=None, t_pills=0.0, lit=None):
    """pills: None = nessuna barra; altrimenti n. pillole (10). lit: {indice: secondo}"""
    a = seg(t, 0.05, 0.5)
    if a > 0:
        put(img, hdr_spr(), 540, 215 - 40 * (1 - ease(a)), alpha=ease(a), shadow=8)
    ty = 152 if pills else 190
    xtext(img, t, 0.2, title, 540, ty, 56, IVORY, shadow=4, track=3, maxw=880)
    if pills:
        for k in range(pills):
            ak = seg(t, t_pills + 0.05 * k, 0.3)
            if ak <= 0:
                continue
            on = lit is not None and k in lit and t >= lit[k]
            sc = 1.0
            if on:
                u = seg(t, lit[k], 0.35)
                sc = 1.0 + 0.45 * math.sin(math.pi * min(1.0, u))
            put(img, pill_spr("gold" if on else "teal"), 540 + (k - 4.5) * 80, 268, scale=sc, alpha=ease(ak))

# ------------------------------------------------------------------ sprite
def wordmark_spr():
    def mk():
        c = Cv(600, 170)
        c.rrect((3, 3, 597, 167), 40, fill=PAPER, outline=GOLD, width=7)
        c.text((300, 76), "ALDI", FONT_SANS, 104, INK, track=10)
        c.rrect((150, 132, 450, 144), 6, fill=TEAL)
        c.rrect((150, 146, 450, 152), 3, fill=GOLD)
        return c.done()
    return S.cache("wordmark13", mk)

def stamp_spr(text, w, h, size, fill=GOLD, ink=INK, edge=GOLD_D):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 30, fill=fill, outline=edge, width=7)
        c.rrect((16, 16, w - 16, h - 16), 22, outline=edge, width=3)
        c.text((w / 2, h / 2 + 3), text, FONT_SANS, size, ink, track=3)
        return c.done()
    return S.cache(("stamp13", text, w, h, size, fill, ink), mk)

def box_spr(kind):
    def mk():
        c = Cv(320, 300)
        c.poly([(40, 110), (280, 110), (306, 60), (66, 60)], fill=(226, 182, 124))
        c.rrect((40, 108, 280, 280), 10, fill=KRAFT, outline=KRAFT_D, width=6)
        c.line([40, 110, 280, 110], KRAFT_D, 5)
        c.rrect((140, 62, 180, 280), 4, fill=(238, 220, 178))
        c.rrect((190, 160, 262, 232), 8, fill=PAPER, outline=KRAFT_D, width=3)
        for y in (178, 194, 210):
            c.line([200, y, 252, y], (170, 160, 140), 4)
        if kind == "old":
            c.ell((222, 10, 306, 94), fill=CORAL, outline=RED_D, width=5)
            c.ell((248, 36, 258, 46), fill=IVORY); c.ell((272, 36, 282, 46), fill=IVORY)
            c.arc((246, 58, 284, 90), 200, 340, IVORY, 6)
        else:
            for (x, y, r) in ((24, 34, 22), (300, 70, 16), (292, 20, 12)):
                for k in range(4):
                    a = math.radians(k * 45)
                    c.line([x - r * math.cos(a), y - r * math.sin(a), x + r * math.cos(a), y + r * math.sin(a)], GOLD, 5)
        return c.done()
    return S.cache(("box13", kind), mk)

def arrow_spr(w=240, h=110, col=GOLD):
    def mk():
        c = Cv(w, h)
        c.poly([(6, h * 0.34), (w * 0.62, h * 0.34), (w * 0.62, 8), (w - 6, h / 2), (w * 0.62, h - 8), (w * 0.62, h * 0.66), (6, h * 0.66)], fill=col)
        return c.done()
    return S.cache(("arrow13", w, h, col), mk)

def bill_spr(crossed=False):
    def mk():
        c = Cv(440, 230)
        c.rrect((4, 4, 436, 226), 24, fill=MONEY, outline=MONEY_D, width=7)
        c.rrect((22, 22, 418, 208), 14, outline=(170, 224, 184), width=4)
        c.ell((150, 50, 290, 180), fill=(170, 224, 184), outline=MONEY_D, width=5)
        c.text((220, 116), "$", FONT_SANS, 100, MONEY_D)
        for (x, y) in ((54, 52), (386, 52), (54, 178), (386, 178)):
            c.ell((x - 14, y - 14, x + 14, y + 14), outline=(170, 224, 184), width=4)
        if crossed:
            c.line([30, 30, 410, 200], CORAL, 18); c.line([410, 30, 30, 200], CORAL, 18)
        return c.done()
    return S.cache(("bill13", crossed), mk)

def check_spr(r=44):
    def mk():
        c = Cv(r * 2 + 8, r * 2 + 8)
        c.ell((4, 4, r * 2 + 4, r * 2 + 4), fill=OKG, outline=(50, 120, 70), width=5)
        c.line([r * 0.55, r + 4, r * 0.9, r * 1.35, r * 1.5, r * 0.7], IVORY, int(r * 0.22))
        return c.done()
    return S.cache(("check13", r), mk)

def browser_spr():
    def mk():
        c = Cv(900, 520)
        c.rrect((4, 4, 896, 516), 40, fill=PAPER, outline=GOLD, width=7)
        c.rrect((4, 4, 896, 104), 40, fill=GLASS)
        c.rrect((4, 64, 896, 104), 2, fill=GLASS)
        for i, col in enumerate((CORAL, GOLD, SAGE)):
            c.ell((36 + i * 42, 38, 62 + i * 42, 64), fill=col)
        c.text((520, 54), "ALDI'S OFFICIAL PAGES", FONT_SANS, 40, IVORY, track=3)
        c.rrect((40, 140, 860, 220), 36, fill=(236, 240, 232), outline=(150, 170, 156), width=4)
        c.text((70, 180), "aldi.us", FONT_SANS, 40, INK, anchor="lm")
        for k in range(4):
            c.rrect((40, 262 + k * 58, 860 - (k % 2) * 160 - k * 30, 292 + k * 58), 10, fill=(206, 212, 204))
        c.rrect((40, 262, 150, 292), 10, fill=TEAL)
        return c.done()
    return S.cache("browser13", mk)

def coin_spr(r=64):
    def mk():
        c = Cv(r * 2 + 8, r * 2 + 8)
        c.ell((4, 4, r * 2 + 4, r * 2 + 4), fill=GOLD, outline=GOLD_D, width=7)
        c.ell((r * 0.32 + 4, r * 0.32 + 4, r * 1.68 + 4, r * 1.68 + 4), outline=GOLD_D, width=4)
        c.arc((r * 0.5 + 4, r * 0.5 + 4, r * 1.5 + 4, r * 1.5 + 4), 200, 290, (255, 236, 170), 7)
        return c.done()
    return S.cache(("coin13", r), mk)

def palm_spr():
    def mk():
        c = Cv(230, 260)
        for i, (x, y0) in enumerate(((36, 40), (78, 20), (120, 12), (162, 34))):
            c.rrect((x, y0, x + 36, 150), 18, fill=SKIN, outline=(190, 150, 110), width=3)
        c.rrect((26, 110, 196, 232), 52, fill=SKIN, outline=(190, 150, 110), width=3)
        c.rrect((4, 126, 70, 182), 26, fill=SKIN, outline=(190, 150, 110), width=3)
        return c.done()
    return S.cache("palm13", mk)

def quote_spr():
    def mk():
        c = Cv(920, 440)
        c.rrect((4, 4, 916, 436), 44, fill=PAPER, outline=GOLD, width=7)
        c.rrect((40, -10, 340, 70), 24, fill=GOLD, outline=GOLD_D, width=4)
        c.text((190, 34), "ALDI SAYS", FONT_SANS, 44, INK, track=3)
        c.text((90, 150), "“", FONT_SERIF, 170, GOLD_D, anchor="mm")
        return c.done()
    return S.cache("quote13", mk)

def disc_tag_spr():
    def mk():
        c = Cv(260, 260)
        c.poly([(20, 130), (110, 30), (240, 30), (240, 230), (110, 230)], fill=IVORY)
        c.line([20, 130, 110, 30, 240, 30, 240, 230, 110, 230, 20, 130], GOLD_D, 7)
        c.ell((70, 112, 104, 146), fill=(0, 0, 0, 0)); c.ell((70, 112, 104, 146), outline=GOLD_D, width=5)
        c.text((168, 132), "%", FONT_SANS, 120, INK)
        c.line([40, 230, 250, 40], CORAL, 20)
        return c.done()
    return S.cache("disctag13", mk)

def chip_spr(k, on):
    def mk():
        c = Cv(150, 72)
        c.rrect((3, 3, 147, 69), 22, fill=GLASS + (240,), outline=GOLD if on else TEAL_L, width=5)
        c.text((52 if on else 75, 38), str(k), FONT_SANS, 40, GOLD if on else SAGE)
        if on:
            c.line([92, 38, 106, 52, 130, 22], OKG, 9)
        return c.done()
    return S.cache(("chip13", k, on), mk)

def book_spr():
    def mk():
        c = Cv(300, 320)
        c.rrect((8, 14, 292, 306), 20, fill=TEAL, outline=GOLD, width=7)
        c.rrect((8, 14, 56, 306), 12, fill=(14, 66, 58))
        c.rrect((84, 56, 262, 160), 10, outline=GOLD, width=4)
        c.text((150, 108), "RULES", FONT_SANS, 46, GOLD, track=2)
        for y in (200, 226, 252):
            c.line([90, y, 250, y], (120, 190, 168), 5)
        c.poly([(246, 14), (280, 14), (280, 120), (263, 102), (246, 120)], fill=CORAL)
        return c.done()
    return S.cache("book13", mk)

def promise_spr():
    def mk():
        c = Cv(920, 540)
        c.rrect((4, 4, 916, 536), 44, fill=PAPER, outline=GOLD, width=7)
        c.rrect((4, 4, 916, 120), 44, fill=GLASS)
        c.rrect((4, 70, 916, 120), 2, fill=GLASS)
        c.text((460, 62), "THE PROMISE", FONT_SANS, 60, IVORY, track=5)
        for i, word in enumerate(("REPLACE", "REFUND")):
            y = 190 + i * 100
            c.rrect((60, y - 36, 860, y + 36), 24, fill=(232, 238, 228), outline=(150, 170, 156), width=3)
            c.text((120, y), word, FONT_SANS, 46, INK, anchor="lm", track=3)
            c.ell((750, y - 26, 802, y + 26), fill=OKG, outline=(50, 120, 70), width=4)
            c.line([762, y, 772, y + 12, 790, y - 12], IVORY, 7)
        for k in range(4):
            c.line([60, 410 + k * 26, 860 - (k % 3) * 120, 410 + k * 26], (186, 190, 182), 5)
        return c.done()
    return S.cache("promise13", mk)

def magnifier_spr():
    def mk():
        c = Cv(230, 240)
        c.ell((8, 8, 168, 168), fill=(220, 240, 236, 70), outline=GOLD, width=14)
        c.line([150, 150, 218, 226], GOLD_D, 22)
        c.arc((34, 34, 120, 120), 200, 280, (255, 255, 255, 190), 8)
        return c.done()
    return S.cache("magn13", mk)

def warn_spr():
    def mk():
        c = Cv(190, 170)
        c.poly([(95, 8), (184, 160), (6, 160)], fill=AMBER)
        c.line([95, 8, 184, 160, 6, 160, 95, 8], (180, 120, 30), 8)
        c.rrect((86, 62, 104, 116), 8, fill=INK)
        c.ell((85, 124, 105, 144), fill=INK)
        return c.done()
    return S.cache("warn13", mk)

def credit_spr():
    def mk():
        c = Cv(520, 310)
        c.rrect((4, 4, 516, 306), 34, fill=TEAL, outline=GOLD, width=7)
        c.rrect((4, 60, 516, 120), 2, fill=(14, 66, 58))
        c.text((260, 196), "STORE CREDIT", FONT_SANS, 60, IVORY, track=3)
        c.ell((40, 24, 92, 76), fill=GOLD, outline=GOLD_D, width=4)
        return c.done()
    return S.cache("credit13", mk)

def tile_spr(kind, label):
    def mk():
        c = Cv(300, 400)
        c.rrect((4, 4, 296, 396), 36, fill=PAPER, outline=GOLD, width=7)
        c.rrect((26, 26, 274, 270), 24, fill=GLASS)
        if kind == "register":
            c.rrect((60, 150, 240, 230), 14, fill=(70, 120, 110), outline=(150, 210, 190), width=4)
            c.rrect((52, 134, 248, 158), 8, fill=IVORY)
            c.rrect((98, 62, 196, 124), 10, fill=(14, 66, 58), outline=(150, 210, 190), width=4)
            for y in (80, 96, 110):
                c.line([108, y, 150 + (y % 3) * 12, y], OKG, 5)
            c.rrect((206, 42, 244, 128), 4, fill=IVORY)
            for y in (58, 74, 90, 106):
                c.line([212, y, 238, y], (160, 160, 150), 3)
            for r in range(2):
                for q in range(4):
                    c.rrect((74 + q * 38, 172 + r * 28, 100 + q * 38, 194 + r * 28), 5, fill=(170, 220, 200))
        elif kind == "website":
            c.rrect((46, 60, 254, 238), 14, fill=PAPER, outline=GOLD, width=4)
            c.rrect((46, 60, 254, 96), 14, fill=TEAL)
            for i, col in enumerate((CORAL, GOLD, SAGE)):
                c.ell((60 + i * 22, 70, 74 + i * 22, 84), fill=col)
            c.text((150, 140), "www", FONT_SANS, 54, INK, track=2)
            for k in range(2):
                c.rrect((62, 176 + k * 26, 238 - k * 50, 190 + k * 26), 6, fill=(200, 206, 198))
        else:
            c.rrect((50, 62, 250, 246), 14, fill=PAPER, outline=GOLD, width=4)
            c.rrect((50, 62, 250, 108), 14, fill=CORAL)
            c.rrect((50, 90, 250, 108), 2, fill=CORAL)
            for x in (92, 208):
                c.rrect((x - 5, 46, x + 5, 80), 5, fill=GOLD_D)
            for r in range(3):
                for q in range(4):
                    on = (r, q) == (1, 2)
                    c.rrect((64 + q * 46, 122 + r * 40, 94 + q * 46, 148 + r * 40), 5, fill=GOLD if on else (206, 212, 204))
        c.text((150, 336), label, FONT_SANS, 44, INK, track=3)
        return c.done()
    return S.cache(("tile13", kind), mk)

def shopper_spr(step):
    def mk():
        c = Cv(240, 440)
        c.ell((70, 8, 170, 108), fill=SKIN, outline=(190, 150, 110), width=4)
        c.rrect((62, 4, 178, 50), 20, fill=(214, 214, 208))
        c.rrect((40, 112, 200, 300), 40, fill=(52, 140, 122), outline=DARK, width=5)
        c.line([196, 150, 232, 224], SKIN, 22)
        c.line([46, 150, 14, 226], SKIN, 22)
        o = 16 if step else -16
        c.rrect((62 + o, 292, 114 + o, 426), 14, fill=(40, 60, 60))
        c.rrect((126 - o, 292, 178 - o, 426), 14, fill=(40, 60, 60))
        c.rrect((54 + o, 414, 122 + o, 436), 10, fill=(28, 40, 40)); c.rrect((118 - o, 414, 186 - o, 436), 10, fill=(28, 40, 40))
        return c.done()
    return S.cache(("shopper13", step), mk)

def video_spr():
    def mk():
        c = Cv(900, 560)
        c.rrect((4, 4, 896, 556), 44, fill=PAPER, outline=GOLD, width=7)
        c.rrect((30, 30, 870, 380), 28, fill=TEAL)
        for k in range(15):
            c.line([30 + k * 60, 30, 30 + k * 60 - 90, 380], (30, 104, 90), 6)
        c.ell((350, 80, 550, 280), fill=GOLD, outline=GOLD_D, width=7)
        c.poly([(418, 124), (418, 236), (510, 180)], fill=DARK)
        for k in range(10):
            c.rrect((46 + k * 82, 306, 112 + k * 82, 366), 12, fill=GLASS, outline=GOLD, width=3)
            c.text((79 + k * 82, 337), str(k + 1), FONT_SANS, 32, GOLD)
        c.text((450, 436), "ALL TEN", FONT_SANS, 86, INK, track=6)
        c.text((450, 506), "IN ONE VIDEO", FONT_SANS, 44, TEAL, track=5)
        return c.done()
    return S.cache("video13", mk)

def glass_spr(w, h):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 40, fill=GLASS + (225,), outline=TEAL_L, width=5)
        return c.done()
    return S.cache(("glass13", w, h), mk)

def cta_spr():
    def mk():
        c = Cv(620, 150)
        c.rrect((4, 4, 616, 146), 75, fill=GOLD, outline=GOLD_D, width=7)
        c.text((310, 78), "TAP IT NOW", FONT_SANS, 72, INK, track=4)
        return c.done()
    return S.cache("cta13", mk)

def reveal(img, spr, left, cy, frac, alpha=1.0, shadow=0):
    w = int(spr.width * max(0.0, min(1.0, frac)))
    if w < 2:
        return
    part = spr.crop((0, 0, w, spr.height))
    put(img, part, left + w / 2, cy, alpha=alpha, shadow=shadow)

# ------------------------------------------------------------------ B1 (349 f = 11,6 s)
def c1(img, t):
    S._cur["b"] = 1
    header13(img, t, "THE PROMISE")
    ta = T("Aldi makes"); tg = T("too good"); tn = T("not satisfied"); tr = T("replace"); tf = T("refund"); tb = T("Both")
    pp(img, t, ta, wordmark_spr(), 540, 450, shadow=12, amp=5, ph=0.2)
    s, al, a = pop(t, tg, 0.5)
    if a > 0:
        put(img, stamp_spr("TOO GOOD TO BE TRUE?", 880, 130, 50), 540 + bob(t, 3, 0.4, 1), 612 + bob(t, 4, 0.55, 2), scale=min(1.0, s), rot=-4, alpha=al, shadow=10)
        bst(img, t, tg, 540, 612, n=10, rad=240, seed=13, dur=0.5)
    # riga A: non soddisfatto -> sostituzione
    pp(img, t, tn, box_spr("old"), 250, 880, sc=0.9, shadow=10, amp=4, ph=0.5)
    xtext(img, t, tn + 0.15, "NOT SATISFIED", 250, 1052, 36, IVORY, shadow=4, track=2, maxw=330)
    sa, ala, aa = pop(t, tr - 0.1, 0.4)
    if aa > 0:
        put(img, arrow_spr(), 540 + 8 * (1 - ease(aa)), 880, scale=min(1.0, sa), alpha=ala)
    pp(img, t, tr + 0.2, box_spr("new"), 830, 880, sc=0.9, shadow=10, amp=4, ph=1.4)
    bst(img, t, tr + 0.2, 830, 880, n=9, rad=170, seed=14, dur=0.5)
    xtext(img, t, tr + 0.35, "REPLACE IT", 830, 1052, 40, GOLD, shadow=4, track=2, maxw=330)
    # riga B: rimborso
    pp(img, t, tf, bill_spr(), 540, 1290, sc=1.0, rot=-3, shadow=12, amp=5, ph=0.9)
    bst(img, t, tf, 540, 1290, n=10, rad=210, seed=15, dur=0.5)
    xtext(img, t, tf + 0.15, "REFUND YOUR MONEY", 540, 1470, 48, GOLD, shadow=4, track=2, maxw=900)
    # entrambe
    sb, alb, ab = pop(t, tb, 0.5)
    if ab > 0:
        put(img, stamp_spr("BOTH", 520, 190, 120, fill=GOLD, ink=INK), 540, 1690, scale=min(1.0, sb), alpha=alb, shadow=12)
        put(img, check_spr(44), 190, 1690, scale=min(1.0, sb), alpha=alb, shadow=6)
        put(img, check_spr(44), 890, 1690, scale=min(1.0, sb), alpha=alb, shadow=6)
        bst(img, t, tb, 540, 1690, n=12, rad=140, seed=16, dur=0.55)

# ------------------------------------------------------------------ B2 (227 f = 7,6 s)
def c2(img, t):
    S._cur["b"] = 2
    t10 = T("ten things")
    header13(img, t, "ONE OF TEN", pills=10, t_pills=t10 + 0.1, lit={0: t10 + 0.9})
    tf = T("found"); ta = T("Another"); tc = T("small coin"); tg = T("gives back")
    pp(img, t, tf - 0.2, browser_spr(), 540, 720, sc=1.0, shadow=12, amp=5, ph=0.3)
    # Aldi + moneta che torna alla mano
    pp(img, t, ta, wordmark_spr(), 300, 1330, sc=0.72, shadow=10, amp=4, ph=0.8)
    s, al, a = pop(t, tc, 0.45)
    xtext(img, t, tc + 0.1, "A SMALL COIN", 540, 1590, 56, GOLD, shadow=4, track=3, maxw=900)
    ah = seg(t, ta + 0.2, 0.5)
    if ah > 0:
        put(img, palm_spr(), 800, 1370 + 60 * (1 - ease(ah)), scale=1.0, alpha=ease(ah), shadow=8)
    u = seg(t, tg - 0.2, 0.9)
    if a > 0:
        if u <= 0:
            cx, cy = 300 + bob(t, 0, 0.5, 0), 1330 + bob(t, 4, 0.6, 1)
        else:
            e = ease(u)
            cx = 300 + (780 - 300) * e
            cy = 1330 - 260 * math.sin(math.pi * e) - 40 * e
        put(img, coin_spr(60), cx, cy, scale=min(1.0, s), alpha=al, shadow=8, rot=(u * 360 if 0 < u < 1 else 0))
    if u >= 1.0 or (u > 0.98):
        bst(img, t, tg + 0.7, 770, 1290, n=10, rad=150, seed=21, dur=0.5)
    xtext(img, t, tg + 0.3, "GIVEN BACK TO YOU", 540, 1700, 56, IVORY, shadow=4, track=3, maxw=900)

# ------------------------------------------------------------------ B3 (323 f = 10,8 s)
def c3(img, t):
    S._cur["b"] = 3
    header13(img, t, "THE STRANGE PART")
    tsays = T("Aldi says"); tdo = T("does not offer"); tst = T("stores"); tdi = T("discounts"); tn = T("none of these ten"); tt = T("tricks"); tow = T("own rules")
    s, al, a = pop(t, tsays, 0.5)
    qy = 600
    if a > 0:
        put(img, quote_spr(), 540 + bob(t, 2, 0.4, 0), qy + bob(t, 4, 0.55, 1), scale=min(1.0, s), alpha=al, shadow=12)
    f = seg(t, tdo, max(0.5, tst - tdo + 0.3))
    l1 = S.cache(("q13a",), lambda: tspr("NO DISCOUNTS", FONT_SANS, 76, INK, track=2))
    l2 = S.cache(("q13b",), lambda: tspr("AT ITS STORES", FONT_SANS, 76, INK, track=2))
    if a > 0 and f > 0:
        reveal(img, l1, 200, qy - 10 + bob(t, 4, 0.55, 1), min(1.0, f * 2.0))
        reveal(img, l2, 200, qy + 98 + bob(t, 4, 0.55, 1), max(0.0, min(1.0, f * 2.0 - 1.0)))
    pp(img, t, tdi + 0.1, disc_tag_spr(), 905, 430, sc=0.56, rot=8, shadow=8, amp=3, ph=1.1)
    # dieci voci: nessun trucco
    tcn = tn
    for k in range(10):
        row, col = divmod(k, 5)
        x = 540 + (col - 2) * 172; y = 960 + row * 92
        ak = seg(t, tcn + 0.06 * k, 0.3)
        if ak > 0:
            on = t >= tcn + 0.06 * k + 0.35
            put(img, chip_spr(k + 1, on), x, y, alpha=ease(ak), scale=1.0 + (0.18 * math.sin(math.pi * min(1.0, seg(t, tcn + 0.06 * k + 0.35, 0.3))) if on else 0))
    s2, al2, a2 = pop(t, tt, 0.5)
    if a2 > 0:
        put(img, stamp_spr("NOT TRICKS", 640, 140, 70, fill=IVORY, ink=INK), 540, 1260 + bob(t, 3, 0.5, 2), scale=min(1.0, s2), rot=-4, alpha=al2, shadow=10)
        bst(img, t, tt, 540, 1260, n=10, rad=230, seed=31, dur=0.5)
    pp(img, t, tow, book_spr(), 330, 1560, sc=0.85, rot=-5, shadow=10, amp=4, ph=0.6)
    xtext(img, t, tow + 0.15, "ALDI'S", 760, 1500, 64, GOLD, shadow=4, track=3, maxw=420)
    xtext(img, t, tow + 0.3, "OWN RULES", 760, 1590, 72, IVORY, shadow=4, track=3, maxw=520)

# ------------------------------------------------------------------ B4 (196 f = 6,5 s)
def c4(img, t):
    S._cur["b"] = 4
    header13(img, t, "THE FINE PRINT")
    tfp = T("fine print"); tm = T("one small mistake"); tsc = T("store credit")
    pp(img, t, 0.3, promise_spr(), 540, 640, sc=1.0, shadow=12, amp=4, ph=0.4)
    u = seg(t, tfp, 1.6)
    if u > 0:
        mx = 330 + 430 * (0.5 + 0.5 * math.sin(u * math.pi * 2.0 - math.pi / 2)) * (1.0 if u < 1 else 1.0)
        put(img, magnifier_spr(), mx + bob(t, 0, 0.5, 0), 860 + 6 * math.sin(t * 3), alpha=ease(min(1.0, u * 4)), shadow=8)
    xtext(img, t, tfp + 0.1, "FINE PRINT", 540, 1030, 52, GOLD, shadow=4, track=3, maxw=800)
    pp(img, t, tm, warn_spr(), 200, 1230, sc=0.95, shadow=8, amp=5, ph=0.7)
    xtext(img, t, tm + 0.1, "ONE SMALL MISTAKE", 640, 1230, 54, IVORY, shadow=4, track=2, maxw=720)
    pp(img, t, tsc - 0.5, bill_spr(True), 250, 1560, sc=0.62, rot=-4, shadow=8, amp=3, ph=0.2)
    sa, ala, aa = pop(t, tsc - 0.3, 0.4)
    if aa > 0:
        put(img, arrow_spr(190, 90), 520, 1560, scale=min(1.0, sa), alpha=ala)
    pp(img, t, tsc, credit_spr(), 800, 1560, sc=0.68, rot=3, shadow=10, amp=4, ph=1.0)
    bst(img, t, tsc, 800, 1560, n=10, rad=180, seed=41, dur=0.5)

# ------------------------------------------------------------------ B5 (195 f = 6,5 s)
def c5(img, t):
    S._cur["b"] = 5
    to = T("other eight")
    header13(img, t, "THE OTHER EIGHT", pills=10, t_pills=to, lit={0: to, 1: to})
    tc = T("checkout"); tw = T("website"); tca = T("calendar"); te = T("easy"); twk = T("walk")
    pp(img, t, tc, tile_spr("register", "CHECKOUT"), 210, 590, sc=0.92, shadow=10, amp=4, ph=0.2)
    pp(img, t, tw, tile_spr("website", "WEBSITE"), 540, 590, sc=0.92, shadow=10, amp=4, ph=1.2)
    pp(img, t, tca, tile_spr("calendar", "CALENDAR"), 870, 590, sc=0.92, shadow=10, amp=4, ph=2.2)
    for k in range(8):
        row, col = divmod(k, 4)
        ak = seg(t, to + 0.1 + 0.07 * k, 0.3)
        if ak > 0:
            put(img, chip_spr("?", False), 540 + (col - 1.5) * 190, 960 + row * 92, alpha=ease(ak), scale=0.5 + 0.5 * ease_back(min(1.0, ak)))
    # corsia: il cliente passa oltre
    floor = Image.new("RGBA", (960, 10), (0, 0, 0, 0))
    ad = seg(t, te - 0.2, 0.5)
    if ad > 0:
        fl = S.cache("floor13", lambda: _floor())
        put(img, fl, 540, 1680, alpha=ease(ad))
    u = seg(t, twk - 0.6, 2.3)
    if u > 0:
        x = 150 + (800 - 150) * ease(u)
        step = int((t * 3.4) % 2) if u < 1 else 0
        put(img, shopper_spr(step), x, 1470, alpha=min(1.0, u * 5), shadow=10)
    xtext(img, t, te, "EASY TO WALK RIGHT PAST", 540, 1790, 50, GOLD, shadow=4, track=2, maxw=940)

def _floor():
    c = Cv(960, 14)
    c.rrect((2, 2, 958, 12), 5, fill=TEAL_L)
    return c.done()

# ------------------------------------------------------------------ B6 (224 f = 7,5 s)
def c6(img, t):
    S._cur["b"] = 6
    tall = T("all ten"); tov = T("one video"); tw = T("what Aldi itself"); trb = T("right below"); ttn = T("Tap it now")
    header13(img, t, "ALL TEN IN ONE VIDEO", pills=10, t_pills=tall, lit={k: tall + 0.45 + 0.05 * k for k in range(10)})
    pp(img, t, tov, video_spr(), 540, 640, sc=0.98, shadow=14, amp=5, ph=0.4)
    xtext(img, t, tw, "WHAT ALDI ITSELF SAYS ABOUT EACH", 540, 1012, 40, IVORY, shadow=4, track=2, maxw=940)
    xtext(img, t, trb, "RIGHT BELOW THIS SHORT", 540, 1230, 58, GOLD, shadow=4, track=3, maxw=940)
    for k in range(3):
        a = seg(t, trb + 0.12 * k, 0.35)
        if a > 0:
            put(img, S.chevron_spr(), 540, 1350 + k * 66 + 12 * (1 - ease(a)) + bob(t, 6, 0.9, k * 0.8), alpha=ease(a) * (1 - 0.2 * k), scale=0.55)
    s, al, a = pop(t, ttn, 0.45)
    if a > 0:
        pulse = 1.0 + 0.03 * math.sin(t * 6.0) * env(t)
        put(img, cta_spr(), 540, 1670, scale=min(1.0, s) * pulse, alpha=al, shadow=12)
        bst(img, t, ttn, 540, 1670, n=10, rad=120, seed=61, dur=0.5)
    ah = seg(t, ttn + 0.1, 0.5)
    if ah > 0 and t < D() - 0.5:
        put(img, hand_spr(), 780 + 50 * (1 - ease(ah)), 1730 + 50 * (1 - ease(ah)) - (10 * math.sin(t * 6) * env(t) if ah >= 1 else 0), scale=0.6, alpha=min(1.0, ah * 3))

# ------------------------------------------------------------------ B7 (204 f = 6,8 s)
def c7(img, t):
    S._cur["b"] = 7
    tl = T("like this short"); ts_ = T("subscribe"); tm = T("so you don't miss")
    header13(img, t, "LIKE  AND  SUBSCRIBE")
    # riga 1: mi piace
    s, al, a = pop(t, tl, 0.45)
    if a > 0:
        put(img, glass_spr(940, 300), 540, 560, alpha=al, shadow=10)
        put(img, thumb_spr(), 250, 560, scale=0.62 * min(1.0, s), alpha=al, shadow=8, rot=-4)
        xtext(img, t, tl + 0.1, "LIKE THIS SHORT", 665, 560, 56, IVORY, shadow=0, maxw=520)
        bst(img, t, tl, 250, 560, n=9, rad=130, seed=71, dur=0.45)
    # riga 2: iscriviti
    s, al, a = pop(t, ts_, 0.5)
    if a > 0:
        put(img, S.channel11_spr(t >= ts_ + 0.9), 540 + bob(t, 2, 0.5), 960 + bob(t, 4, 0.7, 1), scale=0.98 * min(1.0, s), alpha=al, shadow=10)
    if t >= ts_ + 0.9:
        bst(img, t, ts_ + 0.9, 540, 1000, n=10, rad=200, seed=72, dur=0.45)
    ah = seg(t, ts_ + 0.3, 0.6)
    if 0 < ah and t < ts_ + 1.3:
        u = ease(min(1.0, ah))
        put(img, hand_spr(), 700 + 60 * (1 - u), 1090 + 120 * (1 - u), scale=0.55, alpha=min(1.0, ah * 3))
    # riga 3: non perdere il prossimo
    s, al, a = pop(t, tm, 0.45)
    if a > 0:
        put(img, glass_spr(940, 300), 540, 1440, alpha=al, shadow=10)
        put(img, bell_spr(), 250, 1440, scale=0.78 * min(1.0, s), alpha=al, shadow=8, rot=(10 * math.sin((t - tm) * 14) * max(0.0, 1 - (t - tm) / 0.8)))
        xtext(img, t, tm + 0.1, "DON'T MISS", 700, 1395, 56, GOLD, shadow=0, maxw=480, track=2)
        xtext(img, t, tm + 0.25, "THE NEXT ONE", 700, 1480, 56, IVORY, shadow=0, maxw=480, track=2)

SCENES13 = {1: c1, 2: c2, 3: c3, 4: c4, 5: c5, 6: c6, 7: c7}
DRAW = SCENES13
DUR13 = DUR

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES13)
    out_dir = os.environ.get("S13_OUT", "short13")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        S._cur["b"] = k
        render13(zoomed(SCENES13[k]), DUR[k], f"{out_dir}/SA-aldi-short-blocco{k:02d}.mp4")
