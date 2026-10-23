"""Video lungo 8 (WALMART OVER 60) - kit grafico comune. 1920x1080, 30 fps.
Stile NUOVO rispetto ai video precedenti (ordine utente 23/10: slide piu diverse, piu professionali, piu elementi):
sfondo a righe di scaffale con luce dall'alto (non gli anelli dei video 1-7), testata a scontrino con numero della voce,
contatore 1-10 a cartellini da scaffale in alto a destra, schede a forma di scontrino e di cartellino prezzo.
Stessi colori del canale: verde bosco, avorio, oro."""
import os, sys, math, re, random, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long7_b01_10 import *          # motore, Cv, put, pop, ease, seg, txt, tag, panel, card, row_card, stamp, sprite, ic_*
from long7_b11_29 import ic_car
from long5_b01_05 import ic_pills, ic_idcard
from long3_b02_05 import magnifier, check_ic
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
COP = os.path.join(HERE, "..", "COPIONE-VIDEO-WALMART.md")
TEXT = {int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$", open(COP, encoding="utf-8").read())}

PAPER = (250, 247, 238)
INK = (24, 40, 34)
SHELF = (12, 50, 39)
BLUE = (70, 120, 180)
OKG = (110, 200, 130)

DUR = {}

def T(b, key, n=1):
    """secondo in cui la voce arriva alla parola 'key' (n-esima occorrenza) nel blocco b. Voce ~96% del blocco.
    Mai oltre l'80% della durata (regola: ultimo elemento all'80%)."""
    s = TEXT[b]; i = -1
    for _ in range(n):
        i = s.index(key, i + 1)
    d = DUR[b] / FPS
    return min(0.15 + d * 0.96 * i / len(s), d * 0.8)

def LAST(b):
    return DUR[b] / FPS * 0.8

# ------------------------------------------------------------------ sfondo nuovo (scaffali)
_bg = {}
def background8(t):
    if "base" not in _bg:
        im = Image.new("RGB", (W, H), GREEN_D)
        d = ImageDraw.Draw(im)
        for y in range(H):
            k = y / H
            d.line([(0, y), (W, y)], fill=(int(9 + 10 * (1 - k)), int(40 + 22 * (1 - k)), int(32 + 16 * (1 - k))))
        lay = Image.new("L", (W, H), 0); ld = ImageDraw.Draw(lay)
        for y in range(150, H, 210):                      # ripiani
            ld.rectangle([0, y, W, y + 6], fill=60)
            for x in range(-40, W, 160):                  # montanti
                ld.rectangle([x, y + 6, x + 4, y + 40], fill=28)
        for x in range(0, W, 48):                          # trama verticale leggera
            ld.line([(x, 0), (x, H)], fill=10)
        lay = lay.filter(ImageFilter.GaussianBlur(1.2))
        im = Image.composite(Image.new("RGB", (W, H), (40, 96, 74)), im, lay)
        glow = Image.new("L", (W, H), 0); gd = ImageDraw.Draw(glow)
        gd.ellipse([W * 0.15, -H * 0.55, W * 0.85, H * 0.55], fill=70)
        glow = glow.filter(ImageFilter.GaussianBlur(160))
        im = Image.composite(Image.new("RGB", (W, H), (60, 130, 100)), im, glow)
        vig = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(vig)
        vd.rectangle([0, 0, W, H], fill=120); vd.ellipse([-W * 0.2, -H * 0.3, W * 1.2, H * 1.3], fill=0)
        vig = vig.filter(ImageFilter.GaussianBlur(140))
        _bg["base"] = Image.composite(Image.new("RGB", (W, H), (3, 18, 14)), im, vig)
    img = _bg["base"].copy()
    # luce che scorre lenta sui ripiani
    x0 = int((t * 60) % (W + 600)) - 300
    sh = Image.new("L", (W, H), 0); sd = ImageDraw.Draw(sh)
    sd.polygon([(x0, 0), (x0 + 120, 0), (x0 - 80, H), (x0 - 200, H)], fill=18)
    sh = sh.filter(ImageFilter.GaussianBlur(40))
    img = Image.composite(Image.new("RGB", (W, H), (90, 160, 128)), img, sh)
    return img

def render8(draw_fn, nframes, out):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes):
        t = i / FPS
        img = background8(t); draw_fn(img, t)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()

# ------------------------------------------------------------------ testata a scontrino + contatore 1-10
def header_spr(num, title):
    def mk():
        w, h = 1180, 104
        c = Cv(w, h + 14)
        c.rrect((0, 0, w, h), 14, fill=PAPER)
        # bordo inferiore a dente di sega (scontrino)
        for k in range(0, w, 24):
            c.poly([(k, h - 2), (k + 12, h + 12), (k + 24, h - 2)], fill=PAPER)
        if num:
            c.rrect((14, 14, 186, h - 14), 12, fill=GREEN_D)
            c.text((100, h / 2 + 2), "#" + str(num), FONT_SANS, 50, GOLD, track=2)
            x0 = 214
        else:
            c.ell((22, h / 2 - 22, 66, h / 2 + 22), fill=GOLD); x0 = 92
        s = 44
        while tw(title, s, 3) > w - x0 - 170 and s > 18:
            s -= 2
        c.text((x0, h / 2 + 2), title, FONT_SANS, s, INK, anchor="lm", track=3)
        for k in range(6):
            c.line([(w - 120 + k * 16, 26), (w - 120 + k * 16, h - 26)], (180, 176, 164), 3 if k % 2 else 6)
        return c.done()
    return cache(("hdr8", num, title), mk)

def tracker_spr(active):
    def mk():
        w, h = 620, 96
        c = Cv(w, h)
        for i in range(10):
            x = 8 + i * 61
            on = (i + 1) == active; done = active and (i + 1) < active
            fill = GOLD if on else (PANEL_FILL if not done else GREEN_L)
            c.poly([(x, 24), (x + 52, 24), (x + 52, 86), (x + 26, 94), (x, 86)], fill=fill)
            c.ell((x + 20, 8, x + 32, 20), outline=SAGE_D if not on else GOLD, width=3)
            c.line([(x + 26, 20), (x + 26, 26)], SAGE_D if not on else GOLD, 3)
            c.text((x + 26, 58), str(i + 1), FONT_SANS, 30, GREEN_D if on else (IVORY if done else SAGE), track=0)
        return c.done()
    return cache(("trk8", active), mk)

def head(img, t, num, title):
    ap(img, t, 0.05, header_spr(num, title), 30 + 590, 78, pop_=False, dx=-20, dur=0.55, shadow=10)
    if num:
        ap(img, t, 0.25, tracker_spr(num), 1880 - 310, 78, pop_=False, dx=20, dur=0.55, shadow=8)

# ------------------------------------------------------------------ mattoni grafici
def receipt(key, w, h, title, lines, accent=GOLD, size=40, title_size=46):
    """scheda a forma di scontrino: titolo + righe con puntini"""
    def mk():
        c = Cv(w, h + 20)
        c.rrect((0, 10, w, h), 10, fill=PAPER)
        for k in range(0, w, 26):
            c.poly([(k, 12), (k + 13, 0), (k + 26, 12)], fill=PAPER)
            c.poly([(k, h - 2), (k + 13, h + 12), (k + 26, h - 2)], fill=PAPER)
        y = 70
        if title:
            s = title_size
            while tw(title, s, 3) > w - 60 and s > 18:
                s -= 2
            c.text((w / 2, y), title, FONT_SANS, s, INK, track=3)
            y += s * 0.9
            for k in range(30, w - 30, 16):
                c.line([(k, y), (k + 8, y)], (170, 166, 154), 3)
            y += 40
        gap = (h - y - 30) / max(1, len(lines))
        for i, ln in enumerate(lines):
            if isinstance(ln, tuple):
                left, right = ln
            else:
                left, right = ln, None
            s = size
            mx = w - 70 - (tw(right, size, 2) + 30 if right else 0)
            while tw(left, s, 2) > mx and s > 16:
                s -= 2
            yy = y + gap * (i + 0.5)
            c.text((34, yy), left, FONT_SANS, s, INK, anchor="lm", track=2)
            if right:
                c.text((w - 34, yy), right, FONT_SANS, size, accent if accent != GOLD else (170, 120, 30), anchor="rm", track=2)
        return c.done()
    return cache(("rcpt8", key, w, h), mk)

def shelf_tag(key, w, h, big, small, col=GOLD, ink=GREEN_D, big_size=None, small_size=None):
    """cartellino da scaffale: numero grande + scritta sotto"""
    def mk():
        c = Cv(w, h + 30)
        c.rrect((4, 30, w - 4, h + 26), 18, fill=col, outline=(168, 118, 40) if col == GOLD else IVORY, width=5)
        c.ell((w / 2 - 14, 4, w / 2 + 14, 32), outline=col, width=6)
        bs = big_size or int(h * 0.42)
        while tw(big, bs, 2) > w - 40 and bs > 16:
            bs -= 2
        c.text((w / 2, 30 + h * 0.40), big, FONT_SANS, bs, ink, track=2)
        if small:
            ss = small_size or int(h * 0.16)
            while tw(small, ss, 3) > w - 40 and ss > 14:
                ss -= 2
            c.text((w / 2, 30 + h * 0.78), small, FONT_SANS, ss, ink, track=3)
        return c.done()
    return cache(("stag8", key, w, h), mk)

def label_card(key, w, h, icon, title, sub=None, col=SAGE_D, fill=PANEL_FILL, tsize=40, ssize=30, ink=IVORY, sink=GOLD):
    """scheda orizzontale: icona in un tondo a sinistra, titolo e sottotitolo"""
    def mk():
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 26, fill=fill, outline=col, width=5)
        r = min(64, h / 2 - 16)
        if icon:
            c.ell((22, h / 2 - r, 22 + 2 * r, h / 2 + r), fill=GREEN_L, outline=col, width=4)
            icon(c, 22 + r, h / 2)
            x0 = 22 + 2 * r + 24
        else:
            x0 = 44
        for txt_, s0, colr, dy in ((title, tsize, ink, -0.20 if sub else 0), (sub, ssize, sink, 0.24)):
            if not txt_:
                continue
            s_ = s0
            while tw(txt_, s_, 2) > w - x0 - 24 and s_ > 14:
                s_ -= 2
            c.text((x0, h / 2 + dy * h * (0.9 if sub else 1)), txt_, FONT_SANS, s_, colr, anchor="lm", track=2)
        return c.done()
    return cache(("lcard8", key, w, h), mk)

def bubble(key, w, h, lines, size=40, fill=IVORY, ink=INK, tail="bl", border=GOLD):
    def mk():
        c = Cv(w, h + 50)
        c.rrect((4, 4, w - 4, h - 4), 34, fill=fill, outline=border, width=6)
        if tail == "bl":
            c.poly([(70, h - 10), (140, h - 10), (50, h + 44)], fill=fill)
        elif tail == "br":
            c.poly([(w - 140, h - 10), (w - 70, h - 10), (w - 50, h + 44)], fill=fill)
        n = len(lines)
        for i, ln in enumerate(lines):
            s_ = size
            while tw(ln, s_, 2) > w - 60 and s_ > 16:
                s_ -= 2
            c.text((w / 2, h / 2 + (i - (n - 1) / 2) * size * 1.2), ln, FONT_SANS, s_, ink, track=2)
        return c.done()
    return cache(("bub8", key, w, h), mk)

def chip(text, w, h=64, fill=GOLD, ink=GREEN_D, size=None, border=None):
    return tag(text, w, h, fill, ink, size or int(h * 0.44), border=border, track=3)

def xmark_spr(S=110, col=CORAL):
    return sprite(("xm8", S, col), S, S, lambda c: (c.ell((4, 4, S - 4, S - 4), fill=col), ic_x(c, S / 2, S / 2, S / 180, IVORY, 18)))

def ok_spr(S=110, col=OKG):
    return sprite(("ok8", S, col), S, S, lambda c: (c.ell((4, 4, S - 4, S - 4), fill=col), check_ic(c, S / 2, S / 2 + 2, S / 120, GREEN_D)))

def arrow_spr(w=160, h=60, col=GOLD):
    def fn(c):
        c.rrect((0, h / 2 - 10, w - 40, h / 2 + 10), 8, fill=col)
        c.poly([(w - 52, 4), (w, h / 2), (w - 52, h - 4)], fill=col)
    return sprite(("arr8", w, h, col), w, h, fn)

def numdisc(n, S=110, fill=GOLD, ink=GREEN_D):
    return sprite(("nd8", n, S, fill), S, S, lambda c: (c.ell((4, 4, S - 4, S - 4), fill=fill, outline=IVORY, width=4), c.text((S / 2, S / 2 + 2), str(n), FONT_SANS, S * 0.5, ink)))

def grow(img, t, t0, spr, cx, cy, dur=0.6, shadow=0):
    """barra che cresce da sinistra"""
    if t < t0:
        return
    p = ease(seg(t, t0, dur))
    w = max(1, int(spr.width * p))
    put(img, spr.crop((0, 0, w, spr.height)), cx - spr.width / 2 + w / 2, cy, shadow=shadow)

def strike(img, t, t0, x0, x1, y, col=CORAL, w=12, dur=0.4):
    if t < t0:
        return
    p = ease(seg(t, t0, dur))
    d = ImageDraw.Draw(img)
    d.line([(x0, y), (x0 + (x1 - x0) * p, y - 10 * p)], fill=col, width=w)

# ------------------------------------------------------------------ icone nuove (Walmart video)
def ic_register(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy - 10 * s, cx + 70 * s, cy + 50 * s), 10 * s, fill=(70, 78, 90))
    c.rrect((cx - 50 * s, cy - 56 * s, cx + 30 * s, cy - 14 * s), 8 * s, fill=(30, 34, 40), outline=(150, 156, 166), width=3)
    c.text((cx - 10 * s, cy - 35 * s), "$", FONT_SANS, 26 * s, OKG)
    for r_ in range(2):
        for k in range(4):
            c.rrect((cx - 54 * s + k * 28 * s, cy + 2 * s + r_ * 20 * s, cx - 36 * s + k * 28 * s, cy + 16 * s + r_ * 20 * s), 3, fill=IVORY)

def ic_web(c, cx, cy, s, col=IVORY):
    c.rrect((cx - 64 * s, cy - 46 * s, cx + 64 * s, cy + 46 * s), 10 * s, fill=col, outline=(190, 184, 170), width=3)
    c.rrect((cx - 64 * s, cy - 46 * s, cx + 64 * s, cy - 26 * s), 10 * s, fill=(200, 214, 204))
    for k in range(3):
        c.ell((cx - 54 * s + k * 14 * s, cy - 40 * s, cx - 46 * s + k * 14 * s, cy - 32 * s), fill=(150, 150, 146))
    for k in range(3):
        c.rrect((cx - 46 * s, cy - 12 * s + k * 18 * s, cx + (40 - k * 18) * s, cy - 2 * s + k * 18 * s), 3, fill=(196, 204, 198))

def ic_card(c, cx, cy, s, col=(70, 120, 180)):
    c.rrect((cx - 66 * s, cy - 42 * s, cx + 66 * s, cy + 42 * s), 10 * s, fill=col, outline=IVORY, width=3)
    c.rrect((cx - 66 * s, cy - 24 * s, cx + 66 * s, cy - 8 * s), 1, fill=(30, 34, 40))
    c.rrect((cx - 50 * s, cy + 6 * s, cx - 14 * s, cy + 28 * s), 4 * s, fill=GOLD)
    c.rrect((cx + 4 * s, cy + 14 * s, cx + 50 * s, cy + 22 * s), 3, fill=IVORY)

def ic_receipt(c, cx, cy, s):
    c.rrect((cx - 36 * s, cy - 54 * s, cx + 36 * s, cy + 50 * s), 4 * s, fill=PAPER, outline=(190, 184, 170), width=2)
    for k in range(5):
        c.rrect((cx - 24 * s, cy - 38 * s + k * 16 * s, cx + (24 - (k % 2) * 16) * s, cy - 32 * s + k * 16 * s), 2, fill=(170, 166, 154))
    for k in range(4):
        c.poly([(cx - 36 * s + k * 18 * s, cy + 50 * s), (cx - 27 * s + k * 18 * s, cy + 60 * s), (cx - 18 * s + k * 18 * s, cy + 50 * s)], fill=PAPER)

def ic_gift(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 20 * s, cx + 50 * s, cy + 50 * s), 6 * s, fill=CORAL)
    c.rrect((cx - 56 * s, cy - 36 * s, cx + 56 * s, cy - 14 * s), 6 * s, fill=(232, 130, 116))
    c.rrect((cx - 9 * s, cy - 36 * s, cx + 9 * s, cy + 50 * s), 2, fill=GOLD)
    c.ell((cx - 34 * s, cy - 62 * s, cx - 2 * s, cy - 34 * s), outline=GOLD, width=7 * s)
    c.ell((cx + 2 * s, cy - 62 * s, cx + 34 * s, cy - 34 * s), outline=GOLD, width=7 * s)

def ic_syringe(c, cx, cy, s):
    c.line([(cx - 50 * s, cy + 50 * s), (cx + 30 * s, cy - 30 * s)], IVORY, 26 * s)
    c.line([(cx - 40 * s, cy + 40 * s), (cx + 14 * s, cy - 14 * s)], ICE, 14 * s)
    c.line([(cx + 30 * s, cy - 30 * s), (cx + 58 * s, cy - 58 * s)], (190, 192, 198), 5 * s)
    c.line([(cx - 64 * s, cy + 36 * s), (cx - 36 * s, cy + 64 * s)], IVORY, 10 * s)

def ic_van(c, cx, cy, s, col=(70, 120, 180)):
    c.rrect((cx - 70 * s, cy - 34 * s, cx + 30 * s, cy + 26 * s), 8 * s, fill=col)
    c.poly([(cx + 30 * s, cy - 18 * s), (cx + 56 * s, cy - 18 * s), (cx + 72 * s, cy + 2 * s), (cx + 72 * s, cy + 26 * s), (cx + 30 * s, cy + 26 * s)], fill=col)
    c.poly([(cx + 36 * s, cy - 12 * s), (cx + 54 * s, cy - 12 * s), (cx + 64 * s, cy + 2 * s), (cx + 36 * s, cy + 2 * s)], fill=(190, 226, 242))
    c.ell((cx - 54 * s, cy + 14 * s, cx - 28 * s, cy + 40 * s), fill=(40, 44, 52)); c.ell((cx + 26 * s, cy + 14 * s, cx + 52 * s, cy + 40 * s), fill=(40, 44, 52))
    c.text((cx - 20 * s, cy - 4 * s), "Rx", FONT_SANS, 30 * s, IVORY)

def ic_bottle(c, cx, cy, s, col=(232, 150, 60)):
    c.rrect((cx - 30 * s, cy - 34 * s, cx + 30 * s, cy + 50 * s), 10 * s, fill=col)
    c.rrect((cx - 36 * s, cy - 56 * s, cx + 36 * s, cy - 32 * s), 6 * s, fill=IVORY)
    c.rrect((cx - 22 * s, cy - 14 * s, cx + 22 * s, cy + 26 * s), 4 * s, fill=PAPER)
    c.text((cx, cy + 6 * s), "Rx", FONT_SANS, 22 * s, INK)

def ic_pump(c, cx, cy, s):
    c.rrect((cx - 40 * s, cy - 56 * s, cx + 24 * s, cy + 56 * s), 8 * s, fill=CORAL)
    c.rrect((cx - 30 * s, cy - 44 * s, cx + 14 * s, cy - 12 * s), 4 * s, fill=PAPER)
    c.line([(cx + 24 * s, cy - 30 * s), (cx + 48 * s, cy - 30 * s), (cx + 48 * s, cy + 20 * s)], (40, 44, 52), 8 * s)
    c.rrect((cx - 50 * s, cy + 50 * s, cx + 34 * s, cy + 62 * s), 4, fill=(80, 84, 92))

def ic_calendar(c, cx, cy, s, top=CORAL, txt_=None):
    c.rrect((cx - 54 * s, cy - 50 * s, cx + 54 * s, cy + 54 * s), 12 * s, fill=PAPER, outline=(190, 184, 170), width=3)
    c.rrect((cx - 54 * s, cy - 50 * s, cx + 54 * s, cy - 18 * s), 12 * s, fill=top)
    c.d.rectangle(c._b((cx - 54 * s, cy - 30 * s, cx + 54 * s, cy - 18 * s)), fill=top)
    if txt_:
        c.text((cx, cy + 18 * s), txt_, FONT_SANS, 36 * s, INK)

def ic_phone_app(c, cx, cy, s):
    c.rrect((cx - 40 * s, cy - 70 * s, cx + 40 * s, cy + 70 * s), 14 * s, fill=(30, 34, 40))
    c.rrect((cx - 32 * s, cy - 58 * s, cx + 32 * s, cy + 56 * s), 6 * s, fill=PAPER)
    for k in range(3):
        c.rrect((cx - 24 * s, cy - 46 * s + k * 26 * s, cx + 24 * s, cy - 28 * s + k * 26 * s), 4 * s, fill=(200, 214, 204))
    c.rrect((cx - 24 * s, cy + 30 * s, cx + 24 * s, cy + 48 * s), 6 * s, fill=GOLD)

def ic_storefront(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy - 30 * s, cx + 70 * s, cy + 50 * s), 6 * s, fill=PAPER)
    for k in range(5):
        c.d.pieslice(c._b((cx - 70 * s + k * 28 * s, cy - 50 * s, cx - 42 * s + k * 28 * s, cy - 14 * s)), 0, 180, fill=GOLD if k % 2 else OKG)
    c.rrect((cx - 70 * s, cy - 34 * s, cx + 70 * s, cy - 28 * s), 1, fill=(168, 118, 40))
    c.rrect((cx - 16 * s, cy + 6 * s, cx + 16 * s, cy + 50 * s), 3, fill=(90, 140, 190))
    c.rrect((cx - 58 * s, cy + 2 * s, cx - 28 * s, cy + 28 * s), 3, fill=(190, 226, 242))
    c.rrect((cx + 28 * s, cy + 2 * s, cx + 58 * s, cy + 28 * s), 3, fill=(190, 226, 242))

def ic_cart2(c, cx, cy, s, col=IVORY):
    c.line([(cx - 70 * s, cy - 50 * s), (cx - 50 * s, cy - 50 * s), (cx - 30 * s, cy + 20 * s), (cx + 50 * s, cy + 20 * s), (cx + 64 * s, cy - 30 * s), (cx - 42 * s, cy - 30 * s)], col, 8 * s)
    c.ell((cx - 30 * s, cy + 30 * s, cx - 10 * s, cy + 50 * s), fill=col); c.ell((cx + 30 * s, cy + 30 * s, cx + 50 * s, cy + 50 * s), fill=col)

def ic_water(c, cx, cy, s):
    for k in range(3):
        x = cx - 44 * s + k * 44 * s
        c.rrect((x - 18 * s, cy - 30 * s, x + 18 * s, cy + 50 * s), 8 * s, fill=ICE, outline=IVORY, width=3)
        c.rrect((x - 8 * s, cy - 44 * s, x + 8 * s, cy - 28 * s), 3, fill=(70, 120, 180))

def ic_rain(c, cx, cy, s):
    c.ell((cx - 60 * s, cy - 50 * s, cx + 10 * s, cy + 6 * s), fill=(176, 184, 196))
    c.ell((cx - 20 * s, cy - 64 * s, cx + 60 * s, cy + 6 * s), fill=(176, 184, 196))
    for k in range(4):
        x = cx - 40 * s + k * 26 * s
        c.line([(x, cy + 16 * s), (x - 8 * s, cy + 46 * s)], ICE, 6 * s)

def ic_ice(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy + 14 * s, cx + 70 * s, cy + 40 * s), 12 * s, fill=ICE)
    ic_snowflake(c, cx, cy - 20 * s, 1.1 * s, IVORY)

def ic_keypad(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 64 * s, cx + 50 * s, cy + 64 * s), 12 * s, fill=(60, 66, 76))
    c.rrect((cx - 38 * s, cy - 54 * s, cx + 38 * s, cy - 28 * s), 4 * s, fill=(190, 226, 242))
    c.text((cx, cy - 41 * s), "* * * *", FONT_SANS, 18 * s, INK)
    for r_ in range(3):
        for k in range(3):
            c.rrect((cx - 36 * s + k * 26 * s, cy - 16 * s + r_ * 24 * s, cx - 16 * s + k * 26 * s, cy + 2 * s + r_ * 24 * s), 4, fill=IVORY)

def ic_seal(c, cx, cy, s, txt_="USDA", col=GOLD):
    for k in range(16):
        a = math.radians(k * 22.5)
        c.ell((cx + 50 * s * math.cos(a) - 14 * s, cy + 50 * s * math.sin(a) - 14 * s, cx + 50 * s * math.cos(a) + 14 * s, cy + 50 * s * math.sin(a) + 14 * s), fill=col)
    c.ell((cx - 52 * s, cy - 52 * s, cx + 52 * s, cy + 52 * s), fill=col)
    c.ell((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), outline=GREEN_D, width=4 * s)
    c.text((cx, cy + 2 * s), txt_, FONT_SANS, (26 if len(txt_) > 3 else 30) * s, GREEN_D)

def ic_doc(c, cx, cy, s, col=PAPER, mark=None):
    c.poly([(cx - 44 * s, cy - 58 * s), (cx + 22 * s, cy - 58 * s), (cx + 44 * s, cy - 36 * s), (cx + 44 * s, cy + 58 * s), (cx - 44 * s, cy + 58 * s)], fill=col)
    c.poly([(cx + 22 * s, cy - 58 * s), (cx + 44 * s, cy - 36 * s), (cx + 22 * s, cy - 36 * s)], fill=(206, 200, 186))
    for k in range(5):
        c.rrect((cx - 30 * s, cy - 30 * s + k * 16 * s, cx + (30 - (k % 3) * 12) * s, cy - 24 * s + k * 16 * s), 2, fill=(180, 176, 164))
    if mark:
        mark(c, cx + 20 * s, cy + 36 * s, 0.5 * s)

def ic_box8(c, cx, cy, s):
    c.poly([(cx - 70 * s, cy - 20 * s), (cx, cy - 50 * s), (cx + 70 * s, cy - 20 * s), (cx, cy + 10 * s)], fill=(226, 196, 140))
    c.poly([(cx - 70 * s, cy - 20 * s), (cx, cy + 10 * s), (cx, cy + 70 * s), (cx - 70 * s, cy + 40 * s)], fill=(190, 140, 86))
    c.poly([(cx + 70 * s, cy - 20 * s), (cx, cy + 10 * s), (cx, cy + 70 * s), (cx + 70 * s, cy + 40 * s)], fill=(160, 112, 66))

def ic_pin8(c, cx, cy, s, col=GOLD):
    c.ell((cx - 22 * s, cy - 44 * s, cx + 22 * s, cy), fill=col)
    c.poly([(cx - 18 * s, cy - 14 * s), (cx + 18 * s, cy - 14 * s), (cx, cy + 22 * s)], fill=col)
    c.ell((cx - 9 * s, cy - 31 * s, cx + 9 * s, cy - 13 * s), fill=GREEN_D)

def ic_question(c, cx, cy, s, col=GOLD):
    c.ell((cx - 50 * s, cy - 50 * s, cx + 50 * s, cy + 50 * s), fill=col)
    c.text((cx, cy + 4 * s), "?", FONT_SANS, 70 * s, GREEN_D)

def ic_couple(c, cx, cy, s):
    ic_person(c, cx - 32 * s, cy, 0.85 * s, GOLD)
    ic_person(c, cx + 32 * s, cy, 0.85 * s, SAGE)
