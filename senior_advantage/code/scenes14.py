import sys, math, random, os, re, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes13 as P
from scenes13 import *
import scenes12 as S
from scenes11 import xtext
from scenes5 import zoomed
from PIL import Image, ImageDraw, ImageFilter

# =====================================================================
# SHORT 14: Black Friday (correlato al lungo 10). Ordine utente 06/11: screenshot delle durate = fare subito le slide.
# Colori del lungo Black Friday (verde bosco Walmart, avorio, oro, corallo solo per i NO), nastri diagonali, testata a
# BIGLIETTO con navigatore WALMART / TARGET / COSTCO (come il lungo). Layout nuovi (niente barra 1-10, niente pannelli di vetro).
# Durate (fotogrammi) dagli screenshot CapCut del 06/11 (screenshot_durate_short14/DURATE.md): 474 500 489 300 256 250 202.
# Nelle slide compare SOLO cio che la voce dice. Ultimo elemento entro l'80%.  uso: S14_OUT=cartella python3 scenes14.py <blocco>
# =====================================================================
_poly0 = Cv.poly
def _poly(self, pts, fill=None, outline=None, width=1):
    if fill is not None:
        _poly0(self, pts, fill)
    if outline:
        self.d.line([(x * self.ss, y * self.ss) for x, y in list(pts) + [pts[0]]], fill=outline, width=max(1, int(width * self.ss)), joint="curve")
Cv.poly = _poly

HERE = os.path.dirname(os.path.abspath(__file__))
S.TEXT.clear()
S.TEXT.update({int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$",
        open(os.path.join(HERE, "..", "COPIONE-SHORT-14-BLACKFRIDAY.md"), encoding="utf-8").read())})
S.DUR.clear()
S.DUR.update({1: 474, 2: 500, 3: 489, 4: 300, 5: 256, 6: 250, 7: 202})
DUR = S.DUR
TEXT = S.TEXT
T = S.T
bob, env, pp, bst, pop = S.bob, S.env, S.pp, S.bst, S.pop
D = S.D

PAPER2 = (236, 231, 214)
FOREST = (14, 62, 50)
FOREST_D = (8, 40, 32)
GOLD_D = (168, 118, 40)
CORAL_D = (150, 60, 52)
STORES = ["WALMART", "TARGET", "COSTCO"]

def Q(key, n=1, off=0.0):
    """secondo della parola 'key' (+off), mai oltre l'80% del blocco: l'ultimo elemento compare entro l'80%"""
    return min(T(key, n) + off, D() * 0.8)

# ------------------------------------------------------------------ sfondo verde bosco con nastri diagonali (verticale)
_BG = {}
def _mk_bg():
    base = Image.new("RGB", (W, H)); d = ImageDraw.Draw(base)
    for y in range(H):
        k = y / H
        d.line([(0, y), (W, y)], fill=(int(9 + 7 * (1 - k)), int(38 + 20 * (1 - k)), int(31 + 13 * (1 - k))))
    glow = Image.new("L", (W, H), 0); gd = ImageDraw.Draw(glow)
    gd.ellipse([-W * 0.2, -H * 0.12, W * 1.2, H * 0.42], fill=75)
    glow = glow.filter(ImageFilter.GaussianBlur(180))
    base = Image.composite(Image.new("RGB", (W, H), (34, 98, 74)), base, glow)
    vig = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(vig)
    vd.rectangle([0, 0, W, H], fill=130); vd.ellipse([-W * 0.4, -H * 0.1, W * 1.4, H * 1.1], fill=0)
    vig = vig.filter(ImageFilter.GaussianBlur(160))
    _BG["base"] = Image.composite(Image.new("RGB", (W, H), (3, 20, 15)), base, vig)
    Pp = 420
    rb = Image.new("RGBA", (W + Pp + 2200, H + 40), (0, 0, 0, 0)); rd = ImageDraw.Draw(rb)
    for x0 in range(-H * 2, W + Pp + 2200, Pp):
        rd.polygon([(x0, H + 40), (x0 + 110, H + 40), (x0 + 110 + H * 0.5, 0), (x0 + H * 0.5, 0)], fill=(150, 215, 180, 13))
        rd.polygon([(x0 + 170, H + 40), (x0 + 180, H + 40), (x0 + 180 + H * 0.5, 0), (x0 + 170 + H * 0.5, 0)], fill=(228, 179, 99, 24))
    _BG["rb"] = rb; _BG["P"] = Pp
    g = Image.new("RGBA", (W + 80, H + 80), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    for x in range(0, W + 80, 40):
        for y in range(0, H + 80, 40):
            gd.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(170, 225, 195, 26))
    _BG["dots"] = g
    bl = Image.new("RGBA", (700, 700), (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)
    bd.ellipse([120, 120, 580, 580], fill=(232, 190, 110, 40))
    _BG["blob"] = bl.filter(ImageFilter.GaussianBlur(90))
    bk = Image.new("RGBA", (90, 90), (0, 0, 0, 0)); kd = ImageDraw.Draw(bk)
    kd.ellipse([20, 20, 70, 70], fill=(240, 205, 130, 55), outline=(240, 215, 150, 95), width=2)
    _BG["bokeh"] = bk.filter(ImageFilter.GaussianBlur(1.5))

def background14(t):
    if not _BG:
        _mk_bg()
    img = _BG["base"].copy()
    for k, (sx, sy, sp) in enumerate(((0.25, 0.25, 0.19), (0.75, 0.72, 0.15))):
        x = int(W * sx + math.sin(t * sp + k * 2) * 200 - 350); y = int(H * sy + math.cos(t * sp * 0.8 + k) * 220 - 350)
        img.paste(_BG["blob"], (x, y), _BG["blob"])
    ox = int((t * 34) % _BG["P"])
    c = _BG["rb"].crop((ox, 0, ox + W, H)); img.paste(c, (0, 0), c)
    ox, oy = int((t * 12) % 40), int((t * 7) % 40)
    c = _BG["dots"].crop((ox, oy, ox + W, oy + H)); img.paste(c, (0, 0), c)
    for k in range(8):
        x = int((k * 251 + t * (9 + 3 * k)) % (W + 160)) - 80
        y = int(330 + (k * 197) % (H - 560) + math.sin(t * 0.5 + k) * 26)
        img.paste(_BG["bokeh"], (x - 45, y - 45), _BG["bokeh"])
    return img

def render14(draw_fn, nframes, out):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30",
           "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes):
        t = i / 30.0
        img = background14(t)
        draw_fn(img, t)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()

# ------------------------------------------------------------------ testata a biglietto + navigatore dei negozi
def ticket_spr():
    def mk():
        c = Cv(940, 132)
        c.rrect((3, 3, 937, 129), 30, fill=FOREST_D + (240,), outline=GOLD, width=5)
        c.rrect((20, 18, 190, 114), 20, fill=GOLD, outline=GOLD_D, width=4)
        for k in range(5):
            c.ell((196, 22 + k * 20, 206, 32 + k * 20), fill=(0, 0, 0, 0)); c.ell((196, 22 + k * 20, 206, 32 + k * 20), fill=FOREST)
        for (x, y, r) in ((105, 66, 34),):
            for k in range(8):
                a = math.radians(k * 22.5)
                c.line([x - r * math.cos(a), y - r * math.sin(a), x + r * math.cos(a), y + r * math.sin(a)], FOREST_D, 6)
            c.ell((x - 14, y - 14, x + 14, y + 14), fill=FOREST_D)
        return c.done()
    return S.cache("ticket14", mk)

def chip_store(name, on):
    def mk():
        c = Cv(290, 70)
        c.rrect((3, 3, 287, 67), 24, fill=GOLD if on else FOREST_D + (235,), outline=GOLD_D if on else (70, 150, 120), width=5)
        c.text((145, 37), name, FONT_SANS, 34, FOREST_D if on else SAGE, track=2)
        return c.done()
    return S.cache(("chst14", name, on), mk)

def header14(img, t, title, nav=True, lit=None):
    a = seg(t, 0.05, 0.5)
    if a > 0:
        put(img, ticket_spr(), 540, 215 - 40 * (1 - ease(a)), alpha=ease(a), shadow=8)
    xtext(img, t, 0.2, title, 600, 215, 54, IVORY, shadow=4, track=3, maxw=680)
    if nav:
        for k, nm in enumerate(STORES):
            ak = seg(t, 0.3 + 0.08 * k, 0.35)
            if ak <= 0:
                continue
            on = lit is not None and nm in lit and t >= lit[nm]
            sc = 1.0
            if on:
                sc = 1.0 + 0.12 * math.sin(math.pi * min(1.0, seg(t, lit[nm], 0.4)))
            put(img, chip_store(nm, on), 540 + (k - 1) * 300, 335, scale=sc, alpha=ease(ak))

# ------------------------------------------------------------------ sprite
def sale_tag_spr():
    def mk():
        c = Cv(560, 330)
        c.line([40, 60, 120, 140], GOLD_D, 8)
        c.poly([(110, 40), (520, 40), (540, 100), (540, 260), (520, 320), (110, 320), (20, 180)], fill=FOREST_D, outline=GOLD, width=7)
        c.ell((60, 160, 104, 204), fill=(0, 0, 0, 0)); c.ell((62, 162, 102, 202), fill=FOREST, outline=GOLD, width=5)
        c.text((330, 130), "BLACK", FONT_SANS, 100, GOLD, track=6)
        c.text((330, 240), "FRIDAY", FONT_SANS, 100, IVORY, track=6)
        return c.done()
    return S.cache("saletag14", mk)

def plate_spr(name):
    def mk():
        c = Cv(300, 190)
        c.rrect((6, 40, 294, 184), 20, fill=PAPER2, outline=GOLD, width=6)
        for k in range(6):
            c.poly([(6 + k * 48, 8), (54 + k * 48, 8), (54 + k * 48, 56), (6 + k * 48, 56)], fill=GOLD if k % 2 == 0 else IVORY)
        c.rrect((6, 8, 294, 58), 14, outline=GOLD_D, width=4)
        c.text((150, 118), name, FONT_SANS, 46, FOREST_D, track=2)
        c.rrect((100, 146, 200, 172), 8, fill=FOREST, outline=GOLD_D, width=3)
        return c.done()
    return S.cache(("plate14", name), mk)

def rulecard_spr(kind):
    def mk():
        c = Cv(440, 300)
        c.rrect((4, 4, 436, 296), 36, fill=PAPER2, outline=GOLD, width=7)
        c.rrect((4, 4, 436, 76), 36, fill=FOREST_D)
        c.rrect((4, 40, 436, 76), 2, fill=FOREST_D)
        if kind == "ret":
            c.text((220, 42), "RETURNS", FONT_SANS, 44, GOLD, track=4)
            c.rrect((130, 150, 300, 260), 12, fill=KRAFT, outline=KRAFT_D, width=5)
            c.line([130, 172, 300, 172], KRAFT_D, 4)
            c.arc((90, 100, 350, 280), 200, 330, GOLD_D, 12)
            c.poly([(326, 160), (352, 112), (372, 168)], fill=GOLD_D)
        else:
            c.text((220, 42), "PRICE MATCH", FONT_SANS, 40, GOLD, track=3)
            c.poly([(70, 160), (130, 110), (250, 110), (250, 240), (130, 240)], fill=PAPER, outline=GOLD_D, width=5)
            c.ell((100, 164, 126, 190), outline=GOLD_D, width=4)
            c.text((196, 178), "$", FONT_SANS, 70, FOREST_D)
            c.rrect((280, 150, 392, 170), 8, fill=GOLD_D); c.rrect((280, 196, 392, 216), 8, fill=GOLD_D)
        return c.done()
    return S.cache(("rulecard14", kind), mk)

def policy_spr(hit=True):
    def mk():
        c = Cv(900, 520)
        c.rrect((4, 4, 896, 516), 36, fill=PAPER2, outline=GOLD, width=7)
        c.rrect((4, 4, 896, 90), 36, fill=FOREST_D); c.rrect((4, 50, 896, 90), 2, fill=FOREST_D)
        c.text((450, 48), "POLICY PAGE", FONT_SANS, 50, GOLD, track=5)
        ys = (150, 206, 262, 318, 374, 430)
        for k, y in enumerate(ys):
            if hit and k == 3:
                c.rrect((40, y - 24, 860, y + 24), 12, fill=(250, 224, 214), outline=CORAL, width=5)
                c.text((450, y + 1), "BLACK FRIDAY", FONT_SANS, 40, CORAL_D, track=5)
            else:
                c.rrect((40, y - 8, 860 - (k % 3) * 150, y + 8), 8, fill=(196, 198, 188))
        if hit:
            c.ell((20, 276, 880, 362), outline=CORAL, width=9)
        return c.done()
    return S.cache(("policy14", hit), mk)

def tab_spr(name):
    def mk():
        c = Cv(300, 190)
        c.rrect((4, 4, 296, 186), 24, fill=PAPER2, outline=GOLD, width=6)
        c.rrect((4, 4, 296, 56), 24, fill=FOREST_D); c.rrect((4, 30, 296, 56), 2, fill=FOREST_D)
        for i, col in enumerate((CORAL, GOLD, SAGE)):
            c.ell((20 + i * 24, 20, 36 + i * 24, 36), fill=col)
        c.text((122, 104), name, FONT_SANS, 36, FOREST_D, track=1)
        c.rrect((40, 140, 260, 156), 8, fill=(196, 198, 188))
        c.ell((236, 60, 284, 108), fill=OKG, outline=(50, 120, 70), width=4)
        c.line([246, 84, 256, 94, 276, 70], IVORY, 6)
        return c.done()
    return S.cache(("tab14", name), mk)

def crossed_spr(label):
    def mk():
        c = Cv(430, 170)
        c.rrect((4, 4, 426, 166), 26, fill=PAPER2, outline=(170, 160, 140), width=6)
        c.text((196, 85), label, FONT_SANS, 40, (90, 90, 80), track=2)
        c.line([30, 88, 360, 88], CORAL, 7)
        c.ell((352, 40, 410, 98), fill=CORAL, outline=CORAL_D, width=4)
        c.line([368, 56, 394, 82], IVORY, 7); c.line([394, 56, 368, 82], IVORY, 7)
        return c.done()
    return S.cache(("crossed14", label), mk)

def tv_spr():
    def mk():
        c = Cv(400, 320)
        c.rrect((6, 6, 394, 236), 20, fill=(20, 28, 26), outline=GOLD, width=8)
        c.rrect((26, 26, 374, 216), 10, fill=(40, 100, 86))
        c.poly([(70, 190), (140, 110), (190, 160), (240, 80), (330, 190)], fill=(60, 140, 118))
        c.ell((300, 50, 344, 94), fill=GOLD)
        c.rrect((160, 236, 240, 290), 6, fill=(40, 48, 46))
        c.rrect((100, 286, 300, 312), 10, fill=(40, 48, 46), outline=GOLD, width=3)
        return c.done()
    return S.cache("tv14", mk)

def clock_big_spr():
    def mk():
        c = Cv(300, 300)
        c.ell((6, 6, 294, 294), fill=PAPER2, outline=GOLD, width=12)
        c.ell((24, 24, 276, 276), outline=GOLD_D, width=4)
        for k in range(12):
            a = math.radians(k * 30)
            c.line([150 + 108 * math.sin(a), 150 - 108 * math.cos(a), 150 + 124 * math.sin(a), 150 - 124 * math.cos(a)], FOREST_D, 6)
        c.line([150, 150, 150, 70], FOREST_D, 12); c.line([150, 150, 206, 180], CORAL, 10)
        c.ell((138, 138, 162, 162), fill=GOLD_D)
        return c.done()
    return S.cache("clockbig14", mk)

def hand_clock_spr(ang):
    def mk():
        c = Cv(300, 300)
        c.line([150, 150, 150 + 82 * math.sin(math.radians(ang)), 150 - 82 * math.cos(math.radians(ang))], CORAL, 10)
        c.ell((138, 138, 162, 162), fill=GOLD_D)
        return c.done()
    return S.cache(("hclock14", int(ang)), mk)

def dec_cal_spr():
    def mk():
        c = Cv(460, 480)
        c.rrect((4, 4, 456, 476), 34, fill=PAPER2, outline=GOLD, width=8)
        c.rrect((4, 4, 456, 130), 34, fill=CORAL, outline=CORAL_D, width=6); c.rrect((4, 90, 456, 130), 2, fill=CORAL)
        c.text((230, 70), "DECEMBER", FONT_SANS, 62, IVORY, track=5)
        for x in (110, 350):
            c.rrect((x - 10, -4, x + 10, 40), 8, fill=GOLD_D)
        c.text((230, 300), "26", FONT_SANS, 230, FOREST_D)
        c.rrect((60, 420, 400, 446), 10, fill=(206, 208, 198))
        return c.done()
    return S.cache("deccal14", mk)

def start_flag_spr():
    def mk():
        c = Cv(420, 110)
        c.rrect((4, 4, 416, 106), 26, fill=GOLD, outline=GOLD_D, width=6)
        c.text((210, 56), "CLOCK STARTS", FONT_SANS, 44, FOREST_D, track=2)
        return c.done()
    return S.cache("startflag14b", mk)

def senior_tag_spr():
    def mk():
        c = Cv(520, 230)
        c.poly([(120, 20), (490, 20), (505, 70), (505, 160), (490, 210), (120, 210), (24, 115)], fill=PAPER2, outline=GOLD, width=7)
        c.ell((64, 95, 96, 127), fill=(0, 0, 0, 0)); c.ell((64, 95, 96, 127), outline=GOLD_D, width=5)
        c.text((310, 82), "SENIOR", FONT_SANS, 78, FOREST_D, track=4)
        c.text((310, 160), "DISCOUNT", FONT_SANS, 70, FOREST_D, track=3)
        c.line([40, 200, 490, 30], CORAL, 12)
        return c.done()
    return S.cache("seniortag14", mk)

def notfound_spr():
    def mk():
        c = Cv(520, 330)
        c.rrect((4, 4, 516, 326), 30, fill=PAPER2, outline=GOLD, width=7)
        for k in range(5):
            c.rrect((40, 34 + k * 40, 480 - (k % 3) * 100, 50 + k * 40), 8, fill=(196, 198, 188))
        c.rrect((60, 236, 460, 304), 22, fill=FOREST_D)
        c.text((260, 271), "NOT MENTIONED", FONT_SANS, 42, GOLD, track=3)
        return c.done()
    return S.cache("notfound14", mk)

def shield_spr():
    def mk():
        c = Cv(300, 360)
        c.poly([(150, 8), (284, 52), (270, 210), (150, 350), (30, 210), (16, 52)], fill=FOREST_D, outline=GOLD, width=9)
        c.poly([(150, 40), (250, 74), (240, 200), (150, 312), (60, 200), (50, 74)], outline=GOLD_D, width=4)
        c.text((150, 170), "$", FONT_SANS, 170, GOLD)
        return c.done()
    return S.cache("shield14", mk)

def card2_spr(kind):
    def mk():
        c = Cv(460, 460)
        c.rrect((4, 4, 456, 456), 36, fill=PAPER2, outline=GOLD, width=7)
        c.rrect((4, 4, 456, 90), 36, fill=FOREST_D); c.rrect((4, 50, 456, 90), 2, fill=FOREST_D)
        if kind == "long":
            c.text((230, 48), "HOW LONG", FONT_SANS, 46, GOLD, track=4)
            c.rrect((120, 170, 340, 410), 18, fill=KRAFT, outline=KRAFT_D, width=6)
            c.line([120, 204, 340, 204], KRAFT_D, 5)
            c.ell((300, 120, 400, 220), fill=PAPER, outline=GOLD_D, width=7)
            c.line([350, 170, 350, 142], FOREST_D, 6); c.line([350, 170, 372, 182], CORAL, 6)
            c.text((230, 320), "RETURN", FONT_SANS, 44, KRAFT_D, track=3)
        else:
            c.text((230, 48), "PRICE DROPS", FONT_SANS, 44, GOLD, track=3)
            c.poly([(70, 190), (140, 130), (320, 130), (320, 330), (140, 330)], fill=PAPER, outline=GOLD_D, width=5)
            c.ell((104, 214, 134, 244), outline=GOLD_D, width=5)
            c.text((236, 240), "$", FONT_SANS, 110, FOREST_D)
            c.poly([(350, 170), (420, 170), (420, 270), (440, 270), (385, 350), (330, 270), (350, 270)], fill=CORAL, outline=CORAL_D, width=4)
            c.text((230, 400), "AFTER YOU BUY", FONT_SANS, 34, KRAFT_D, track=2)
        return c.done()
    return S.cache(("card2_14", kind), mk)

def age_strip_spr():
    def mk():
        c = Cv(760, 130)
        c.rrect((4, 4, 756, 126), 60, fill=GLASS + (235,), outline=GOLD, width=6)
        c.text((380, 66), "ANY AGE", FONT_SANS, 70, IVORY, track=8)
        return c.done()
    return S.cache("agestrip14", mk)

def shopfront_spr(label, lim):
    def mk():
        c = Cv(300, 330)
        c.rrect((6, 70, 294, 320), 20, fill=PAPER2, outline=GOLD, width=6)
        for k in range(6):
            c.poly([(6 + k * 48, 20), (54 + k * 48, 20), (54 + k * 48, 80), (6 + k * 48, 80)], fill=GOLD if k % 2 == 0 else IVORY)
        c.rrect((6, 20, 294, 80), 14, outline=GOLD_D, width=4)
        c.rrect((100, 190, 200, 320), 10, fill=FOREST, outline=GOLD_D, width=4)
        c.rrect((30, 110, 90, 170), 8, fill=(180, 214, 204), outline=GOLD_D, width=3); c.rrect((210, 110, 270, 170), 8, fill=(180, 214, 204), outline=GOLD_D, width=3)
        return c.done()
    return S.cache(("shop14", label, lim), mk)

def hourglass_spr():
    def mk():
        c = Cv(180, 260)
        c.rrect((10, 8, 170, 36), 10, fill=GOLD, outline=GOLD_D, width=5); c.rrect((10, 224, 170, 252), 10, fill=GOLD, outline=GOLD_D, width=5)
        c.poly([(28, 36), (152, 36), (98, 130), (152, 224), (28, 224), (82, 130)], fill=(220, 240, 232, 150), outline=GOLD, width=7)
        c.poly([(52, 52), (128, 52), (92, 112)], fill=GOLD)
        c.poly([(62, 220), (118, 220), (90, 180)], fill=GOLD)
        c.line([90, 112, 90, 190], GOLD, 5)
        return c.done()
    return S.cache("hourglass14", mk)

def window_spr():
    def mk():
        c = Cv(900, 230)
        c.rrect((4, 4, 896, 226), 30, fill=PAPER2, outline=GOLD, width=7)
        c.text((450, 70), "THE WINDOW TO ASK", FONT_SANS, 52, FOREST_D, track=4)
        for k in range(10):
            c.rrect((30 + k * 84, 150, 100 + k * 84, 206), 10, fill=(206, 208, 198))
        return c.done()
    return S.cache("window14b", mk)

def shutter_spr(frac):
    def mk():
        c = Cv(900, 230)
        c.rrect((4, 4, 896, 226), 30, outline=GOLD, width=7)
        return c.done()
    return None

def no_stamp_spr():
    def mk():
        c = Cv(360, 190)
        c.rrect((4, 4, 356, 186), 34, fill=CORAL, outline=CORAL_D, width=8)
        c.rrect((18, 18, 342, 172), 24, outline=IVORY, width=4)
        c.text((180, 98), "NO", FONT_SANS, 130, IVORY, track=8)
        return c.done()
    return S.cache("nostamp14", mk)

def sheet_spr(label, rot=0):
    def mk():
        c = Cv(300, 400)
        c.rrect((4, 4, 296, 396), 22, fill=PAPER2, outline=GOLD, width=6)
        c.rrect((4, 4, 296, 84), 22, fill=FOREST_D); c.rrect((4, 50, 296, 84), 2, fill=FOREST_D)
        c.text((150, 46), label, FONT_SANS, 40, GOLD, track=3)
        for k in range(7):
            c.rrect((30, 124 + k * 38, 270 - (k % 3) * 50, 138 + k * 38), 7, fill=(196, 198, 188))
        return c.done()
    return S.cache(("sheet14", label), mk)

def video_card14():
    def mk():
        c = Cv(900, 600)
        c.rrect((4, 4, 896, 596), 44, fill=PAPER2, outline=GOLD, width=8)
        c.rrect((30, 30, 870, 350), 28, fill=FOREST)
        for k in range(15):
            c.line([30 + k * 60, 30, 30 + k * 60 - 90, 350], (24, 84, 68), 6)
        c.ell((360, 70, 540, 250), fill=GOLD, outline=GOLD_D, width=7)
        c.poly([(422, 108), (422, 212), (506, 160)], fill=FOREST_D)
        for k, nm in enumerate(STORES):
            c.rrect((50 + k * 270, 280, 280 + k * 270 - 20, 334), 18, fill=FOREST_D, outline=GOLD, width=4)
            c.text((165 + k * 270 - 10, 308), nm, FONT_SANS, 30, GOLD, track=2)
        c.text((450, 430), "STORE BY STORE", FONT_SANS, 80, FOREST_D, track=4)
        c.text((450, 512), "ONE VIDEO", FONT_SANS, 56, GOLD_D, track=6)
        return c.done()
    return S.cache("video14", mk)

def cta14_spr():
    def mk():
        c = Cv(620, 150)
        c.rrect((4, 4, 616, 146), 75, fill=GOLD, outline=GOLD_D, width=7)
        c.text((310, 78), "TAP IT NOW", FONT_SANS, 72, FOREST_D, track=4)
        return c.done()
    return S.cache("cta14", mk)

def medal_spr(n, col=GOLD):
    def mk():
        c = Cv(150, 150)
        c.ell((6, 6, 144, 144), fill=col, outline=GOLD_D, width=8)
        c.ell((22, 22, 128, 128), outline=GOLD_D, width=4)
        c.text((75, 76), str(n), FONT_SANS, 80, FOREST_D)
        return c.done()
    return S.cache(("medal14", n, col), mk)

def line_v_spr(h):
    def mk():
        c = Cv(14, h)
        c.rrect((2, 0, 12, h), 5, fill=GOLD_D)
        return c.done()
    return S.cache(("linev14", h), mk)

def reveal(img, spr, left, cy, frac, alpha=1.0, shadow=0):
    P.reveal(img, spr, left, cy, frac, alpha, shadow)

# ------------------------------------------------------------------ B1 (474 f = 15,8 s): le tre grandi catene, due temi, un'eccezione scritta sulla pagina
def c1(img, t):
    S._cur["b"] = 1
    t3 = Q("three big stores"); tw = Q("Each one"); tr = Q("returns"); tpm = Q("price matching"); te = Q("exception", off=-0.9); tpg = Q("policy page")
    header14(img, t, "BLACK FRIDAY", lit={n: t3 + 0.2 * k for k, n in enumerate(STORES)})
    pp(img, t, Q("Black Friday"), sale_tag_spr(), 540, 560, sc=0.84, rot=-3, shadow=12, amp=5, ph=0.2)
    for k, nm in enumerate(STORES):
        pp(img, t, t3 + 0.2 * k, plate_spr(nm), 235 + k * 305, 830, sc=0.94, shadow=10, amp=4, ph=0.4 + k)
    bst(img, t, t3, 540, 830, n=10, rad=330, seed=141, dur=0.5)
    pp(img, t, tr, rulecard_spr("ret"), 300, 1090, sc=0.82, rot=-2, shadow=10, amp=4, ph=0.3)
    pp(img, t, tpm, rulecard_spr("pm"), 780, 1090, sc=0.82, rot=2, shadow=10, amp=4, ph=1.3)
    xtext(img, t, tw, "OWN RULES AT EACH STORE", 540, 1270, 44, IVORY, shadow=4, track=3, maxw=880)
    pp(img, t, te, policy_spr(True), 540, 1570, sc=0.82, shadow=12, amp=3, ph=0.7)
    bst(img, t, te + 0.4, 540, 1600, n=10, rad=260, seed=142, color=CORAL, dur=0.5)

# ------------------------------------------------------------------ B2 (500 f = 16,7 s): pagine ufficiali (non blog), l'orologio parte il 26 dicembre
def c2(img, t):
    S._cur["b"] = 2
    tw = Q("Walmart"); tt = Q("Target"); tc = Q("Costco"); tb = Q("blogs"); tcs = Q("coupon sites"); tf = Q("One thing"); te = Q("electronics"); tck = Q("clock"); td = Q("December twenty sixth")
    header14(img, t, "OFFICIAL PAGES", lit={"WALMART": tw, "TARGET": tt, "COSTCO": tc})
    pp(img, t, tw, tab_spr("WALMART"), 230, 560, sc=0.94, shadow=10, amp=4, ph=0.2)
    pp(img, t, tt, tab_spr("TARGET"), 540, 560, sc=0.94, shadow=10, amp=4, ph=1.2)
    pp(img, t, tc, tab_spr("COSTCO"), 850, 560, sc=0.94, shadow=10, amp=4, ph=2.2)
    pp(img, t, tb, crossed_spr("BLOGS"), 300, 790, sc=0.88, rot=-3, shadow=8, amp=3, ph=0.5)
    pp(img, t, tcs, crossed_spr("COUPON SITES"), 790, 790, sc=0.88, rot=3, shadow=8, amp=3, ph=1.5)
    s, al, a = pop(t, tf, 0.45)
    if a > 0:
        put(img, P.magnifier_spr(), 130 + bob(t, 6, 0.6, 0), 1010 + bob(t, 6, 0.7, 1), scale=0.7 * min(1.0, s), alpha=al, shadow=8)
    pp(img, t, te, tv_spr(), 330, 1200, sc=0.8, rot=-2, shadow=10, amp=4, ph=0.9)
    xtext(img, t, te + 0.1, "SOME ELECTRONICS", 320, 1380, 40, IVORY, shadow=4, track=2, maxw=500)
    pp(img, t, tck, clock_big_spr(), 300, 1590, sc=0.72, shadow=10, amp=3, ph=0.4)
    u = seg(t, tck + 0.2, 1.4)
    if u > 0:
        put(img, hand_clock_spr(int(150 + 150 * ease(u))), 300, 1590, scale=0.72, alpha=ease(min(1.0, u * 3)))
    sd, ald, ad = pop(t, td, 0.5)
    if ad > 0:
        put(img, dec_cal_spr(), 770 + bob(t, 3, 0.5, 2), 1330 + bob(t, 4, 0.6, 1), scale=0.88 * min(1.0, sd), alpha=ald, shadow=12, rot=3)
        bst(img, t, td, 770, 1330, n=12, rad=250, seed=151, dur=0.55)
    pp(img, t, td + 0.3, start_flag_spr(), 770, 1650, sc=0.8, rot=-2, shadow=10, amp=3, ph=0.8)

# ------------------------------------------------------------------ B3 (489 f = 16,3 s): non e uno sconto senior, sono due cose che proteggono i soldi a ogni eta
def c3(img, t):
    S._cur["b"] = 3
    tn = Q("not about a senior"); tp = Q("pages I read"); tt = Q("two things"); tl = Q("how long"); tpd = Q("what happens when"); ta = Q("at any age", off=-0.8)
    header14(img, t, "THE STRANGE PART", nav=False)
    pp(img, t, tn, senior_tag_spr(), 540, 470, sc=0.9, rot=-3, shadow=12, amp=4, ph=0.2)
    pp(img, t, tp, notfound_spr(), 520, 790, sc=0.8, rot=2, shadow=10, amp=3, ph=1.0)
    s, al, a = pop(t, tp + 0.2, 0.45)
    if a > 0:
        put(img, P.magnifier_spr(), 860 + bob(t, 5, 0.6, 0), 830 + bob(t, 5, 0.7, 1), scale=0.75 * min(1.0, s), alpha=al, shadow=8)
    pp(img, t, tt, shield_spr(), 540, 1110, sc=0.74, shadow=12, amp=4, ph=0.5)
    bst(img, t, tt, 540, 1110, n=10, rad=200, seed=161, dur=0.5)
    xtext(img, t, tt + 0.15, "PROTECTS YOUR MONEY", 540, 1290, 46, GOLD, shadow=4, track=3, maxw=880)
    pp(img, t, tl, card2_spr("long"), 290, 1590, sc=0.72, rot=-2, shadow=10, amp=4, ph=0.3)
    pp(img, t, tpd, card2_spr("drop"), 790, 1590, sc=0.72, rot=2, shadow=10, amp=4, ph=1.3)
    pp(img, t, ta, age_strip_spr(), 540, 1385, sc=0.62, shadow=8, amp=2, ph=0.5)

# ------------------------------------------------------------------ B4 (300 f = 10 s): due negozi su tre danno giorni limitati, poi la risposta puo essere no
def c4(img, t):
    S._cur["b"] = 4
    tc = Q("catch"); t3 = Q("three stores"); tl = Q("limited number"); tm = Q("miss that window"); tn = Q("answer can be no")
    header14(img, t, "THE CATCH", nav=False)
    for k in range(3):
        pp(img, t, t3 - 0.6 + 0.18 * k, shopfront_spr("S", k), 215 + k * 325, 620, sc=0.9, shadow=10, amp=4, ph=0.3 + k)
    for k in (0, 2):
        pp(img, t, tl + 0.25 * (k // 2), hourglass_spr(), 215 + k * 325, 905, sc=0.8, shadow=8, amp=4, ph=0.5 + k)
        xtext(img, t, tl + 0.2 + 0.25 * (k // 2), "LIMITED DAYS", 215 + k * 325, 1075, 34, GOLD, shadow=4, track=2, maxw=290)
    pp(img, t, tl + 0.5, window_spr(), 540, 1300, sc=0.96, shadow=10, amp=3, ph=0.4)
    u = seg(t, tm, 1.1)
    if u > 0:
        w = int(900 * 0.96 * ease(u))
        sh = Image.new("RGBA", (max(2, w), 230), (0, 0, 0, 0))
        d = ImageDraw.Draw(sh)
        d.rounded_rectangle([0, 4, max(2, w) - 1, 226], radius=26, fill=(70, 28, 24, 235), outline=CORAL, width=6)
        for k in range(0, max(2, w), 40):
            d.line([k, 14, k, 216], fill=(150, 60, 52, 200), width=5)
        put(img, sh, 540 - 432 + w / 2, 1300, alpha=min(1.0, u * 4))
    xtext(img, t, tm + 0.1, "MISS THE WINDOW", 540, 1470, 56, IVORY, shadow=4, track=3, maxw=900)
    s, al, a = pop(t, tn, 0.45)
    if a > 0:
        put(img, no_stamp_spr(), 540 + bob(t, 3, 0.5, 0), 1680 + bob(t, 4, 0.55, 1), scale=min(1.0, s), rot=-6, alpha=al, shadow=12)
        bst(img, t, tn, 540, 1680, n=10, rad=230, seed=171, color=CORAL, dur=0.5)

# ------------------------------------------------------------------ B5 (256 f = 8,5 s): giorni, date, eccezioni cambiano e sono sparsi su piu pagine
def c5(img, t):
    S._cur["b"] = 5
    td = Q("days"); tda = Q("dates"); te = Q("exceptions"); tdf = Q("different at each"); ts = Q("spread across"); tw = Q("walk right past", off=-0.8)
    header14(img, t, "EVERY STORE DIFFERENT", nav=False)
    pp(img, t, td, sheet_spr("DAYS"), 230, 620, sc=0.78, rot=-4, shadow=10, amp=4, ph=0.2)
    pp(img, t, tda, sheet_spr("DATES"), 540, 590, sc=0.78, rot=0, shadow=10, amp=4, ph=1.2)
    pp(img, t, te, sheet_spr("EXCEPTIONS"), 850, 620, sc=0.78, rot=4, shadow=10, amp=4, ph=2.2)
    s, al, a = pop(t, tdf, 0.45)
    if a > 0:
        put(img, P.neq_spr(), 540, 900, scale=0.9 * min(1.0, s), alpha=al, shadow=8)
    xtext(img, t, tdf + 0.1, "NOT THE SAME", 540, 1040, 56, GOLD, shadow=4, track=3, maxw=860)
    for k in range(5):
        ak = seg(t, ts + 0.12 * k, 0.4)
        if ak > 0:
            put(img, sheet_spr("PAGE"), 150 + k * 195, 1240 + 14 * math.sin(k * 1.7) + bob(t, 4, 0.6, k), scale=0.42, rot=-12 + 6 * k, alpha=ease(ak), shadow=6)
    u = seg(t, tw, 1.8)
    if u > 0:
        x = 130 + (900 - 130) * ease(u)
        step = int((t * 3.4) % 2) if u < 1 else 0
        put(img, shopper_spr(step), x, 1520, scale=0.88, alpha=min(1.0, u * 5), shadow=10)
    xtext(img, t, tw + 0.1, "EASY TO WALK RIGHT PAST", 540, 1750, 46, IVORY, shadow=4, track=2, maxw=940)

# ------------------------------------------------------------------ B6 (250 f = 8,3 s): tutto in un video, negozio per negozio, qui sotto
def c6(img, t):
    S._cur["b"] = 6
    tv = Q("one video"); tsb = Q("store by store"); tp = Q("what each page"); tr = Q("right below"); tn = Q("Tap it now")
    header14(img, t, "ALL IN ONE VIDEO", lit={"WALMART": tsb, "TARGET": tsb + 0.2, "COSTCO": tsb + 0.4})
    pp(img, t, tv, video_card14(), 540, 760, sc=0.98, shadow=14, amp=5, ph=0.4)
    xtext(img, t, tp, "WHAT EACH PAGE ITSELF SAYS", 540, 1150, 46, IVORY, shadow=4, track=2, maxw=940)
    xtext(img, t, tr, "RIGHT BELOW THIS SHORT", 540, 1290, 58, GOLD, shadow=4, track=3, maxw=940)
    for k in range(3):
        a = seg(t, tr + 0.12 * k, 0.35)
        if a > 0:
            put(img, S.chevron_spr(), 540, 1410 + k * 66 + 12 * (1 - ease(a)) + bob(t, 6, 0.9, k * 0.8), alpha=ease(a) * (1 - 0.2 * k), scale=0.55)
    s, al, a = pop(t, tn, 0.45)
    if a > 0:
        pulse = 1.0 + 0.03 * math.sin(t * 6.0) * env(t)
        put(img, cta14_spr(), 540, 1700, scale=min(1.0, s) * pulse, alpha=al, shadow=12)
        bst(img, t, tn, 540, 1700, n=10, rad=120, seed=181, dur=0.5)
    ah = seg(t, tn + 0.1, 0.5)
    if ah > 0 and t < D() - 0.5:
        put(img, hand_spr(), 790 + 50 * (1 - ease(ah)), 1760 + 50 * (1 - ease(ah)) - (10 * math.sin(t * 6) * env(t) if ah >= 1 else 0), scale=0.6, alpha=min(1.0, ah * 3))

# ------------------------------------------------------------------ B7 (202 f = 6,7 s): mi piace, iscriviti, non perdere il prossimo (linea verticale con 3 medaglie)
def c7(img, t):
    S._cur["b"] = 7
    tl = Q("like this short"); ts_ = Q("subscribe"); tm = Q("so you don't miss")
    header14(img, t, "LIKE  AND  SUBSCRIBE", nav=False)
    ln = seg(t, tl - 0.2, 1.8)
    if ln > 0:
        hh = int(1050 * ease(min(1.0, ln)))
        put(img, line_v_spr(max(2, hh)), 150, 480 + max(2, hh) / 2, alpha=0.9)
    s, al, a = pop(t, tl, 0.45)
    if a > 0:
        put(img, medal_spr(1), 150, 520, scale=min(1.0, s), alpha=al, shadow=8)
        put(img, thumb_spr(), 530 + bob(t, 3, 0.5, 0), 520, scale=0.9 * min(1.0, s), alpha=al, shadow=8, rot=-4)
        xtext(img, t, tl + 0.1, "LIKE THIS SHORT", 770, 700, 44, IVORY, shadow=4, track=2, maxw=420)
        bst(img, t, tl, 530, 520, n=9, rad=150, seed=191, dur=0.45)
    s, al, a = pop(t, ts_, 0.5)
    if a > 0:
        put(img, medal_spr(2), 150, 1010, scale=min(1.0, s), alpha=al, shadow=8)
        put(img, S.channel11_spr(t >= ts_ + 0.9), 600 + bob(t, 2, 0.5), 1030 + bob(t, 4, 0.7, 1), scale=0.8 * min(1.0, s), alpha=al, shadow=10)
    if t >= ts_ + 0.9:
        bst(img, t, ts_ + 0.9, 600, 1030, n=10, rad=200, seed=192, dur=0.45)
    ah = seg(t, ts_ + 0.3, 0.6)
    if 0 < ah and t < ts_ + 1.3:
        u = ease(min(1.0, ah))
        put(img, hand_spr(), 800 + 60 * (1 - u), 1150 + 120 * (1 - u), scale=0.5, alpha=min(1.0, ah * 3))
    s, al, a = pop(t, tm, 0.45)
    if a > 0:
        put(img, medal_spr(3), 150, 1500, scale=min(1.0, s), alpha=al, shadow=8)
        put(img, bell_spr(), 440, 1500, scale=0.95 * min(1.0, s), alpha=al, shadow=8, rot=(10 * math.sin((t - tm) * 14) * max(0.0, 1 - (t - tm) / 0.8)))
        xtext(img, t, tm + 0.1, "DON'T MISS", 790, 1450, 48, GOLD, shadow=4, maxw=380, track=2)
        xtext(img, t, tm + 0.25, "THE NEXT ONE", 790, 1530, 48, IVORY, shadow=4, maxw=380, track=2)

SCENES14 = {1: c1, 2: c2, 3: c3, 4: c4, 5: c5, 6: c6, 7: c7}
DRAW = SCENES14

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or sorted(SCENES14)
    out_dir = os.environ.get("S14_OUT", "short14")
    os.makedirs(out_dir, exist_ok=True)
    for k in ks:
        S._cur["b"] = k
        render14(zoomed(SCENES14[k]), DUR[k], f"{out_dir}/SA-blackfriday-short-blocco{k:02d}.mp4")
