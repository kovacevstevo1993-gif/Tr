"""Video lungo 9 (ALDI) - kit grafico comune. 1920x1080, 30 fps.
Stile NUOVO (ordine utente 25/10: slide piu diverse, piu professionali, elementi piu professionali):
sfondo "carta millimetrata" verde-petrolio con due griglie che scorrono e luci morbide in movimento (non anelli, non scaffali),
testata a linguetta di fascicolo con numero della voce e barra di avanzamento 1-10, schede di carta avorio con striscia colorata,
pannelli di vetro scuro, grandi numeri che contano, ombre gia cotte negli sprite (render piu veloce), movimento lento continuo
che si spegne 0,95 s prima della fine del blocco. Stessi colori del canale: verde, avorio, oro."""
import os, sys, math, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from long8_kit import *            # motore, Cv, put, sprite, tspr, txt, label_card, shelf_tag, receipt, chip, ic_*, colori
from long8_kit import background8   # noqa
from PIL import Image, ImageDraw, ImageFilter, ImageChops

COP9 = os.path.join(HERE, "..", "COPIONE-VIDEO-ALDI.md")
TEXT = {int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$", open(COP9, encoding="utf-8").read())}
ENDS9 = [1017, 1980, 2939, 3736, 4581, 5585, 6510, 7348, 8216, 9148, 10036, 10987, 11890, 12762, 13551, 14554, 15501,
         16439, 17469, 18415, 19202, 20088, 20890, 21811, 22683, 23896, 24697, 25568, 26357, 27095]
DUR = {i + 1: e - (ENDS9[i - 1] if i else 0) for i, e in enumerate(ENDS9)}
END = [0.0]

TEAL = (20, 120, 112)
SKY = (110, 176, 214)
AMBER = (240, 168, 64)
SLATE = (46, 66, 62)

def T(b, key, n=1):
    """secondo in cui la voce arriva alla parola 'key' (n-esima occorrenza) nel blocco b (voce ~94% del blocco, mai oltre il 78%)"""
    s = TEXT[b]; i = -1
    for _ in range(n):
        i = s.index(key, i + 1)
    d = DUR[b] / FPS
    return max(0.15, min(0.1 + d * 0.94 * i / len(s) - 0.12, d * 0.78))

def LAST(b):
    return DUR[b] / FPS * 0.8

def settle(t):
    e = END[0] - 0.95
    return max(0.0, min(1.0, (e - t) / 0.7))

# ------------------------------------------------------------------ sfondo
_B9 = {}
def _mk_bg():
    base = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(base)
    for y in range(H):
        k = y / H
        d.line([(0, y), (W, y)], fill=(int(6 + 8 * (1 - k)), int(36 + 24 * (1 - k)), int(36 + 18 * (1 - k))))
    glow = Image.new("L", (W, H), 0); gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.05, -H * 0.5, W * 0.95, H * 0.6], fill=80)
    glow = glow.filter(ImageFilter.GaussianBlur(170))
    base = Image.composite(Image.new("RGB", (W, H), (48, 128, 112)), base, glow)
    vig = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(vig)
    vd.rectangle([0, 0, W, H], fill=140); vd.ellipse([-W * 0.25, -H * 0.35, W * 1.25, H * 1.35], fill=0)
    vig = vig.filter(ImageFilter.GaussianBlur(150))
    base = Image.composite(Image.new("RGB", (W, H), (2, 14, 14)), base, vig)
    _B9["base"] = base
    g1 = Image.new("RGBA", (W + 60, H + 60), (0, 0, 0, 0)); d1 = ImageDraw.Draw(g1)
    for x in range(0, W + 60, 60):
        d1.line([(x, 0), (x, H + 60)], fill=(150, 215, 185, 15), width=1)
    for y in range(0, H + 60, 60):
        d1.line([(0, y), (W + 60, y)], fill=(150, 215, 185, 15), width=1)
    _B9["g1"] = g1
    g2 = Image.new("RGBA", (W + 240, H + 240), (0, 0, 0, 0)); d2 = ImageDraw.Draw(g2)
    for x in range(0, W + 240, 240):
        d2.line([(x, 0), (x, H + 240)], fill=(170, 225, 200, 30), width=2)
    for y in range(0, H + 240, 240):
        d2.line([(0, y), (W + 240, y)], fill=(170, 225, 200, 30), width=2)
    for x in range(0, W + 240, 240):
        for y in range(0, H + 240, 240):
            d2.line([(x - 9, y), (x + 9, y)], fill=(228, 179, 99, 90), width=3)
            d2.line([(x, y - 9), (x, y + 9)], fill=(228, 179, 99, 90), width=3)
    _B9["g2"] = g2
    bl = Image.new("RGBA", (900, 900), (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)
    bd.ellipse([150, 150, 750, 750], fill=(70, 170, 140, 70))
    _B9["blob"] = bl.filter(ImageFilter.GaussianBlur(120))
    sw = Image.new("RGBA", (W * 2, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sw)
    sd.polygon([(W - 120, 0), (W + 160, 0), (W - 120 + 260, H), (W - 400 + 260, H)], fill=(255, 245, 210, 20))
    _B9["sweep"] = sw.filter(ImageFilter.GaussianBlur(50))

def background9(t):
    if not _B9:
        _mk_bg()
    img = _B9["base"].copy()
    for k, (sx, sy) in enumerate(((0.25, 0.18), (0.8, 0.7))):
        x = int(W * sx + math.sin(t * 0.21 + k * 2) * 260 - 450); y = int(H * sy + math.cos(t * 0.17 + k) * 160 - 450)
        img.paste(_B9["blob"], (x, y), _B9["blob"])
    ox, oy = int((t * 14) % 60), int((t * 9) % 60)
    c = _B9["g1"].crop((ox, oy, ox + W, oy + H)); img.paste(c, (0, 0), c)
    ox, oy = int((t * 26) % 240), int((t * 15) % 240)
    c = _B9["g2"].crop((ox, oy, ox + W, oy + H)); img.paste(c, (0, 0), c)
    sx = int((t * 70) % (W * 1.6)) - W // 2
    img.paste(_B9["sweep"], (sx - W // 2, 0), _B9["sweep"])
    return img

# ------------------------------------------------------------------ sprite con ombra cotta
def bake(spr, blur=14, dy=9, alpha=0.5):
    pad = int(blur * 2.6)
    out = Image.new("RGBA", (spr.width + 2 * pad, spr.height + 2 * pad), (0, 0, 0, 0))
    sh = Image.new("L", out.size, 0)
    sh.paste(spr.getchannel("A").point(lambda v: int(v * alpha)), (pad, pad + dy))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    out.paste(Image.new("RGBA", out.size, (2, 14, 12, 255)), (0, 0), sh)
    out.alpha_composite(spr, (pad, pad))
    return out

def mk(key, w, h, fn, blur=14, dy=9, alpha=0.5, shadow=True):
    def build():
        c = Cv(w, h); fn(c); s = c.done()
        return bake(s, blur, dy, alpha) if shadow else s
    return cache(("k9", key, w, h), build)

def vgrad(c, box, r, c1, c2, outline=None, width=0):
    """rettangolo arrotondato con sfumatura verticale (dentro un Cv)"""
    ss = c.ss
    x0, y0, x1, y1 = [int(v * ss) for v in box]
    w, h = x1 - x0, y1 - y0
    g = Image.new("RGBA", (w, h))
    gd = ImageDraw.Draw(g)
    for y in range(h):
        k = y / max(1, h - 1)
        gd.line([(0, y), (w, y)], fill=tuple(int(c1[i] + (c2[i] - c1[i]) * k) for i in range(3)) + (255,))
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=int(r * ss), fill=255)
    c.im.paste(g, (x0, y0), m)
    if outline:
        c.rrect(box, r, outline=outline, width=width)

# ------------------------------------------------------------------ animazione
def show(img, t, t0, spr, cx, cy, mode="pop", amp=5.0, ph=0.0, t_out=None, scale=1.0, rot=0.0, dur=0.5, alpha=1.0, fl=True):
    """compare a t0; poi galleggia piano finche settle() > 0; sparisce a t_out"""
    if t < t0:
        return 0.0
    p = ease(seg(t, t0, dur))
    ox = oy = 0.0; s = scale; a = min(1.0, p * 2.6)
    if mode == "pop":
        s = scale * max(0.01, ease_back(seg(t, t0, dur)))
    elif mode == "up":
        oy = 60 * (1 - p)
    elif mode == "down":
        oy = -60 * (1 - p)
    elif mode == "left":
        ox = -90 * (1 - p)
    elif mode == "right":
        ox = 90 * (1 - p)
    elif mode == "zoom":
        s = scale * (0.6 + 0.4 * p)
    elif mode == "fade":
        pass
    if fl and amp:
        k = settle(t)
        oy += amp * math.sin(t * 1.7 + ph) * k
        ox += amp * 0.45 * math.cos(t * 1.3 + ph) * k
        rot = rot + 0.6 * math.sin(t * 1.1 + ph) * k
    fo = 1.0
    if t_out is not None:
        fo = 1 - ease(seg(t, t_out, 0.35))
        if fo <= 0:
            return 0.0
    put(img, spr, cx + ox, cy + oy, scale=s, alpha=a * fo * alpha, rot=rot)
    return p

def grow_x(img, t, t0, spr, x0, cy, dur=0.7):
    """sprite che si rivela da sinistra (barre)"""
    if t < t0:
        return
    p = ease(seg(t, t0, dur))
    w = max(2, int(spr.width * p))
    put(img, spr.crop((0, 0, w, spr.height)), x0 + w / 2, cy)

def count(t, t0, v, dur=1.0, dec=0):
    p = ease(seg(t, t0, dur))
    x = v * p
    return ("%d" % round(x)) if dec == 0 else ("%.*f" % (dec, x))

# ------------------------------------------------------------------ testata
def head9(img, t, num, title, mid=None):
    """num: 1..10 = voce; 0 = intro, -1 = riepilogo/chiusura (mid: testo del chip a destra)"""
    def build():
        w, h = 1780, 92
        c = Cv(w, h)
        vgrad(c, (0, 0, w, h), 22, (10, 52, 46), (6, 36, 32), outline=(70, 150, 124), width=3)
        c.rrect((12, 12, 112, h - 12), 14, fill=GOLD)
        c.text((62, h / 2 + 2), ("%02d" % num) if num > 0 else "ALDI", FONT_SANS, 44 if num > 0 else 30, GREEN_D, track=1)
        s = 42
        while tw(title, s, 3) > 1020 and s > 20:
            s -= 2
        c.text((140, h / 2 + 2), title, FONT_SANS, s, IVORY, anchor="lm", track=3)
        if num > 0:
            c.text((w - 560, h / 2 + 2), "ITEM %d OF 10" % num, FONT_SANS_M, 26, SAGE, anchor="rm", track=3)
            for i in range(10):
                x = w - 530 + i * 50
                on = i < num; cur = i == num - 1
                c.rrect((x, h / 2 - 12, x + 40, h / 2 + 12), 8, fill=GOLD if cur else (GREEN_L if on else (24, 70, 60)),
                        outline=IVORY if cur else None, width=2)
        else:
            lab = mid or ("INTRO" if num == 0 else "WRAP-UP")
            c.rrect((w - 330, 18, w - 16, h - 18), 18, fill=(24, 70, 60), outline=GOLD, width=3)
            c.text((w - 173, h / 2 + 2), lab, FONT_SANS, 30, GOLD, track=4)
        return bake(c.done(), 10, 6, 0.5)
    spr = cache(("h9", num, title, mid), build)
    show(img, t, 0.05, spr, 960, 78, mode="down", dur=0.6, fl=False)
    if t > 0.3:
        p = ease(seg(t, 0.3, 0.7))
        d = ImageDraw.Draw(img)
        d.line([(90, 134), (90 + 1740 * p, 134)], fill=GOLD, width=3)

def source9(img, t, t0, label, x=1620, y=1032):
    spr = mk(("src9", label), 560, 62, lambda c: (
        c.rrect((2, 2, 558, 60), 30, fill=(8, 44, 40), outline=SAGE_D, width=3),
        c.rrect((16, 14, 40, 48), 4, fill=PAPER), c.line([(21, 24), (35, 24)], SAGE_D, 3), c.line([(21, 31), (35, 31)], SAGE_D, 3),
        c.text((56, 31), "SOURCE", FONT_SANS_M, 20, SAGE, anchor="lm", track=3),
        c.text((150, 31), label, FONT_SANS, 24, IVORY, anchor="lm", track=2)), blur=8, dy=5)
    show(img, t, t0, spr, x, y, mode="up", dur=0.45, fl=False)

# ------------------------------------------------------------------ mattoni
def pill9(text, w, h=62, fill=GOLD, ink=GREEN_D, size=None, border=None):
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), h / 2 - 3, fill=fill, outline=border, width=3 if border else 1)
        s = size or int(h * 0.42)
        while tw(text, s, 3) > w - 40 and s > 14:
            s -= 2
        c.text((w / 2, h / 2 + 2), text, FONT_SANS, s, ink, track=3)
    return mk(("pill9", text, w, h, fill, ink), w, h, fn, blur=8, dy=5)

def paper9(key, w, h, title, lines, accent=GOLD, size=32, tsize=34, align="left", icon=None, ink=INK, sub_ink=(70, 100, 84)):
    """scheda di carta avorio con striscia colorata in alto; lines: lista di str o (str, colore)"""
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 22, fill=PAPER)
        c.rrect((3, 3, w - 3, 62), 22, fill=accent)
        c.d.rectangle(c._b((3, 40, w - 3, 62)), fill=accent)
        s = tsize
        while tw(title, s, 3) > w - (150 if icon else 60) and s > 14:
            s -= 2
        tx = 28 if not icon else 28
        c.text((w / 2 if align == "center" else tx, 34), title, FONT_SANS, s, GREEN_D if accent in (GOLD, OKG, AMBER) else IVORY,
               anchor="mm" if align == "center" else "lm", track=3)
        if icon:
            icon(c, w - 54, 36, 0.4)
        n = len(lines)
        top, bot = 80, h - 16
        gap = (bot - top) / max(1, n)
        for i, ln in enumerate(lines):
            col = ink
            if isinstance(ln, tuple):
                ln, col = ln
            s2 = size
            while tw(ln, s2, 2) > w - 56 and s2 > 14:
                s2 -= 2
            yy = top + gap * (i + 0.5)
            c.text((w / 2 if align == "center" else 28, yy), ln, FONT_SANS, s2, col, anchor="mm" if align == "center" else "lm", track=2)
    return mk(("paper9", key, w, h), w, h, fn)

def glass9(key, w, h, icon, title, sub=None, col=SAGE_D, tsize=38, ssize=28, tcol=IVORY, scol=GOLD, iconcol=GREEN_L):
    """pannello di vetro scuro orizzontale con tondo-icona"""
    def fn(c):
        vgrad(c, (3, 3, w - 3, h - 3), 26, (14, 62, 54), (7, 40, 34), outline=col, width=4)
        r = min(60, h / 2 - 14)
        x0 = 30
        if icon:
            c.ell((22, h / 2 - r, 22 + 2 * r, h / 2 + r), fill=iconcol, outline=col, width=3)
            icon(c, 22 + r, h / 2)
            x0 = 22 + 2 * r + 24
        for text_, s0, cc, dy in ((title, tsize, tcol, -0.2 if sub else 0), (sub, ssize, scol, 0.22)):
            if not text_:
                continue
            s_ = s0
            while tw(text_, s_, 2) > w - x0 - 22 and s_ > 14:
                s_ -= 2
            c.text((x0, h / 2 + dy * h * (0.95 if sub else 1)), text_, FONT_SANS, s_, cc, anchor="lm", track=2)
    return mk(("glass9", key, w, h), w, h, fn)

def bignum(key, w, h, value, label, col=GOLD, vsize=None, lsize=26, fill=(9, 46, 40)):
    def fn(c):
        vgrad(c, (3, 3, w - 3, h - 3), 28, (16, 66, 58), (7, 40, 34), outline=col, width=4)
        vs = vsize or int(h * 0.5)
        while tw(value, vs, 2) > w - 36 and vs > 18:
            vs -= 2
        c.text((w / 2, h * 0.42), value, FONT_SANS, vs, col, track=1)
        s = lsize
        while tw(label, s, 3) > w - 30 and s > 12:
            s -= 2
        c.text((w / 2, h * 0.84), label, FONT_SANS, s, IVORY, track=3)
    return mk(("bignum", key, w, h), w, h, fn)

def badge_ic(key, S, icon, ring=GOLD, fill=(14, 62, 54), scale=1.0):
    def fn(c):
        c.ell((4, 4, S - 4, S - 4), fill=fill, outline=ring, width=5)
        icon(c, S / 2, S / 2, scale)
    return mk(("bic9", key, S), S, S, fn, blur=10, dy=7)

def xb(S=96, col=CORAL):
    return mk(("xb9", S, col), S, S, lambda c: (c.ell((3, 3, S - 3, S - 3), fill=col), ic_x(c, S / 2, S / 2, S / 180, IVORY, 16)), blur=7, dy=5)

def okb(S=96, col=OKG):
    return mk(("okb9", S, col), S, S, lambda c: (c.ell((3, 3, S - 3, S - 3), fill=col), check_ic(c, S / 2, S / 2 + 2, S / 120, GREEN_D)), blur=7, dy=5)

def stamp9(text, w, h, col=CORAL, size=None):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 16, fill=(10, 40, 36), outline=col, width=6)
        c.rrect((14, 14, w - 14, h - 14), 10, outline=col, width=2)
        s = size or int(h * 0.38)
        while tw(text, s, 3) > w - 44 and s > 14:
            s -= 2
        c.text((w / 2, h / 2 + 2), text, FONT_SANS, s, col, track=3)
    return mk(("st9", text, w, h, col), w, h, fn, blur=8, dy=5)

def quote9(key, w, h, lines, size=40, ink=INK, bar=GOLD):
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 24, fill=PAPER)
        c.rrect((3, 3, 24, h - 3), 12, fill=bar)
        c.text((52, 66), "“", FONT_SERIF, 120, bar, anchor="lm")
        n = len(lines)
        for i, ln in enumerate(lines):
            s = size
            while tw(ln, s, 2) > w - 150 and s > 14:
                s -= 2
            c.text((100, h / 2 + (i - (n - 1) / 2) * size * 1.3 + 14), ln, FONT_SANS, s, ink, anchor="lm", track=2)
    return mk(("quote9", key, w, h), w, h, fn)

def arrow9(w=140, h=56, col=GOLD, down=False):
    def fn(c):
        if down:
            c.rrect((w / 2 - 10, 0, w / 2 + 10, h - 30), 8, fill=col)
            c.poly([(w / 2 - 28, h - 34), (w / 2, h - 2), (w / 2 + 28, h - 34)], fill=col)
        else:
            c.rrect((0, h / 2 - 10, w - 34, h / 2 + 10), 8, fill=col)
            c.poly([(w - 40, 4), (w - 2, h / 2), (w - 40, h - 4)], fill=col)
    return mk(("arr9", w, h, col, down), w, h, fn, blur=6, dy=4, alpha=0.4)

# ------------------------------------------------------------------ icone nuove
def ic_coin25(c, cx, cy, s, spin=1.0):
    r = 58 * s
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=(176, 184, 190), outline=(120, 128, 134), width=5 * s)
    c.ell((cx - r * 0.84, cy - r * 0.84, cx + r * 0.84, cy + r * 0.84), fill=(206, 212, 216), outline=(150, 158, 164), width=3 * s)
    c.text((cx, cy - 4 * s), "25", FONT_SANS, 46 * s, (70, 78, 84))
    c.text((cx, cy + 32 * s), "CENTS", FONT_SANS, 13 * s, (90, 98, 104), track=2)
    c.arc((cx - r * 0.7, cy - r * 0.7, cx + r * 0.7, cy + r * 0.7), 200, 250, (255, 255, 255), 5 * s)

def ic_cart_big(c, cx, cy, s, col=IVORY, basket=(190, 200, 204)):
    c.line([(cx - 74 * s, cy - 56 * s), (cx - 50 * s, cy - 56 * s), (cx - 28 * s, cy + 22 * s)], col, 9 * s)
    c.poly([(cx - 46 * s, cy - 36 * s), (cx + 70 * s, cy - 36 * s), (cx + 54 * s, cy + 14 * s), (cx - 28 * s, cy + 14 * s)], fill=basket)
    for k in range(4):
        c.line([(cx - 40 * s + k * 28 * s, cy - 32 * s), (cx - 28 * s + k * 24 * s, cy + 10 * s)], (130, 140, 146), 3 * s)
    c.line([(cx - 28 * s, cy + 22 * s), (cx + 50 * s, cy + 22 * s)], col, 8 * s)
    c.ell((cx - 28 * s, cy + 34 * s, cx - 8 * s, cy + 54 * s), fill=col)
    c.ell((cx + 28 * s, cy + 34 * s, cx + 48 * s, cy + 54 * s), fill=col)

def ic_tote(c, cx, cy, s, col=OKG):
    c.arc((cx - 28 * s, cy - 70 * s, cx + 28 * s, cy - 10 * s), 180, 360, col, 7 * s)
    c.rrect((cx - 52 * s, cy - 24 * s, cx + 52 * s, cy + 56 * s), 8 * s, fill=col)
    c.rrect((cx - 52 * s, cy - 24 * s, cx + 52 * s, cy - 6 * s), 8 * s, fill=tuple(min(255, v + 25) for v in col))
    c.ell((cx - 18 * s, cy + 8 * s, cx + 18 * s, cy + 40 * s), outline=IVORY, width=4 * s)

def ic_paperbag(c, cx, cy, s):
    c.poly([(cx - 44 * s, cy - 36 * s), (cx + 44 * s, cy - 36 * s), (cx + 50 * s, cy + 56 * s), (cx - 50 * s, cy + 56 * s)], fill=(204, 160, 104))
    c.poly([(cx - 44 * s, cy - 36 * s), (cx - 10 * s, cy - 36 * s), (cx - 20 * s, cy + 56 * s), (cx - 50 * s, cy + 56 * s)], fill=(184, 140, 88))
    c.rrect((cx - 24 * s, cy - 6 * s, cx + 24 * s, cy + 26 * s), 4 * s, fill=PAPER)
    c.text((cx, cy + 10 * s), "ALDI", FONT_SANS, 14 * s, (60, 90, 120))

def ic_donut(c, cx, cy, s, frac, col=GOLD, track=(24, 70, 60), width=26):
    r = 70 * s
    c.arc((cx - r, cy - r, cx + r, cy + r), 0, 360, track, width * s)
    c.arc((cx - r, cy - r, cx + r, cy + r), -90, -90 + 360 * frac, col, width * s)

def ic_shield(c, cx, cy, s, col=GOLD, mark=None):
    pts = [(cx - 56 * s, cy - 56 * s), (cx + 56 * s, cy - 56 * s), (cx + 56 * s, cy + 6 * s), (cx, cy + 66 * s), (cx - 56 * s, cy + 6 * s)]
    c.poly(pts, fill=col)
    pts2 = [(cx - 44 * s, cy - 44 * s), (cx + 44 * s, cy - 44 * s), (cx + 44 * s, cy + 2 * s), (cx, cy + 52 * s), (cx - 44 * s, cy + 2 * s)]
    c.poly(pts2, fill=(14, 62, 54))
    if mark:
        mark(c, cx, cy - 4 * s, 0.8 * s)

def ic_weekstrip(c, cx, cy, s, hl=2, hlcol=GOLD):
    days = ["M", "T", "W", "T", "F", "S", "S"]
    for i, dname in enumerate(days):
        x = cx + (i - 3) * 38 * s
        on = i == hl
        c.rrect((x - 16 * s, cy - 26 * s, x + 16 * s, cy + 26 * s), 7 * s, fill=hlcol if on else (230, 226, 214))
        c.text((x, cy), dname, FONT_SANS, 22 * s, GREEN_D if on else (110, 120, 112))

def ic_bank(c, cx, cy, s, col=IVORY):
    c.poly([(cx - 66 * s, cy - 14 * s), (cx, cy - 58 * s), (cx + 66 * s, cy - 14 * s)], fill=col)
    for k in range(4):
        c.rrect((cx - 52 * s + k * 34 * s, cy - 8 * s, cx - 40 * s + k * 34 * s, cy + 36 * s), 3, fill=col)
    c.rrect((cx - 66 * s, cy + 40 * s, cx + 66 * s, cy + 56 * s), 4, fill=col)

def ic_pharmacy(c, cx, cy, s, col=OKG):
    c.rrect((cx - 54 * s, cy - 54 * s, cx + 54 * s, cy + 54 * s), 12 * s, fill=PAPER)
    c.rrect((cx - 14 * s, cy - 40 * s, cx + 14 * s, cy + 40 * s), 4, fill=col)
    c.rrect((cx - 40 * s, cy - 14 * s, cx + 40 * s, cy + 14 * s), 4, fill=col)

def ic_cheese(c, cx, cy, s):
    c.poly([(cx - 62 * s, cy + 36 * s), (cx + 62 * s, cy + 36 * s), (cx + 62 * s, cy - 6 * s), (cx - 10 * s, cy - 44 * s)], fill=(244, 204, 96))
    c.poly([(cx - 62 * s, cy + 36 * s), (cx + 62 * s, cy + 36 * s), (cx + 62 * s, cy + 56 * s), (cx - 62 * s, cy + 56 * s)], fill=(222, 178, 70))
    for (x, y, r) in ((-20, 10, 9), (20, 18, 7), (40, -4, 8), (0, 28, 6)):
        c.ell((cx + (x - r) * s, cy + (y - r) * s, cx + (x + r) * s, cy + (y + r) * s), fill=(222, 178, 70))

def ic_clock2(c, cx, cy, s, ang=0.0, col=IVORY):
    c.ell((cx - 52 * s, cy - 52 * s, cx + 52 * s, cy + 52 * s), fill=col, outline=(150, 158, 150), width=5 * s)
    for k in range(12):
        a = math.radians(k * 30)
        c.line([(cx + 42 * s * math.sin(a), cy - 42 * s * math.cos(a)), (cx + 48 * s * math.sin(a), cy - 48 * s * math.cos(a))], (90, 100, 94), 3 * s)
    a = math.radians(ang)
    c.line([(cx, cy), (cx + 36 * s * math.sin(a), cy - 36 * s * math.cos(a))], INK, 5 * s)
    c.line([(cx, cy), (cx + 24 * s * math.sin(a / 12), cy - 24 * s * math.cos(a / 12))], INK, 6 * s)

def ic_paycard(c, cx, cy, s, col, label=None, lcol=IVORY):
    c.rrect((cx - 66 * s, cy - 42 * s, cx + 66 * s, cy + 42 * s), 10 * s, fill=col)
    c.rrect((cx - 66 * s, cy - 24 * s, cx + 66 * s, cy - 6 * s), 1, fill=(24, 30, 34))
    if label:
        c.text((cx, cy + 20 * s), label, FONT_SANS, 17 * s, lcol, track=1)

def ic_tap(c, cx, cy, s, col=IVORY):
    for k in range(3):
        c.arc((cx - (20 + k * 18) * s, cy - (20 + k * 18) * s, cx + (20 + k * 18) * s, cy + (20 + k * 18) * s), -45, 45, col, 6 * s)
    c.ell((cx - 30 * s, cy - 10 * s, cx - 10 * s, cy + 10 * s), fill=col)

def ic_truck2(c, cx, cy, s, col=SKY):
    c.rrect((cx - 70 * s, cy - 36 * s, cx + 20 * s, cy + 24 * s), 6 * s, fill=col)
    c.poly([(cx + 20 * s, cy - 20 * s), (cx + 50 * s, cy - 20 * s), (cx + 68 * s, cy + 2 * s), (cx + 68 * s, cy + 24 * s), (cx + 20 * s, cy + 24 * s)], fill=tuple(min(255, v + 30) for v in col))
    c.ell((cx - 54 * s, cy + 12 * s, cx - 26 * s, cy + 40 * s), fill=(36, 40, 46)); c.ell((cx + 22 * s, cy + 12 * s, cx + 50 * s, cy + 40 * s), fill=(36, 40, 46))

def ic_apple(c, cx, cy, s):
    c.ell((cx - 36 * s, cy - 30 * s, cx + 36 * s, cy + 44 * s), fill=CORAL)
    c.line([(cx, cy - 28 * s), (cx + 8 * s, cy - 50 * s)], (110, 80, 50), 6 * s)
    c.ell((cx + 6 * s, cy - 56 * s, cx + 34 * s, cy - 36 * s), fill=OKG)

def ic_lock(c, cx, cy, s, col=GOLD):
    c.arc((cx - 24 * s, cy - 56 * s, cx + 24 * s, cy - 4 * s), 180, 360, col, 8 * s)
    c.rrect((cx - 36 * s, cy - 18 * s, cx + 36 * s, cy + 40 * s), 8 * s, fill=col)
    c.ell((cx - 7 * s, cy + 2 * s, cx + 7 * s, cy + 16 * s), fill=GREEN_D)

def ic_note(c, cx, cy, s, col=GOLD):
    c.poly([(cx - 40 * s, cy - 46 * s), (cx + 40 * s, cy - 46 * s), (cx + 40 * s, cy + 24 * s), (cx + 14 * s, cy + 24 * s), (cx, cy + 46 * s), (cx - 14 * s, cy + 24 * s), (cx - 40 * s, cy + 24 * s)], fill=col)

def ic_flask(c, cx, cy, s):
    c.poly([(cx - 16 * s, cy - 54 * s), (cx + 16 * s, cy - 54 * s), (cx + 16 * s, cy - 14 * s), (cx + 52 * s, cy + 44 * s), (cx - 52 * s, cy + 44 * s), (cx - 16 * s, cy - 14 * s)], fill=(210, 230, 236))
    c.poly([(cx - 36 * s, cy + 14 * s), (cx + 36 * s, cy + 14 * s), (cx + 52 * s, cy + 44 * s), (cx - 52 * s, cy + 44 * s)], fill=OKG)
    c.rrect((cx - 22 * s, cy - 60 * s, cx + 22 * s, cy - 50 * s), 3, fill=IVORY)

def ic_repeat(c, cx, cy, s, col=GOLD):
    c.arc((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), 200, 340, col, 9 * s)
    c.poly([(cx + 40 * s, cy - 24 * s), (cx + 58 * s, cy - 2 * s), (cx + 26 * s, cy - 4 * s)], fill=col)
    c.arc((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), 20, 160, col, 9 * s)
    c.poly([(cx - 40 * s, cy + 24 * s), (cx - 58 * s, cy + 2 * s), (cx - 26 * s, cy + 4 * s)], fill=col)

def ic_list(c, cx, cy, s, done=3, n=5):
    c.rrect((cx - 50 * s, cy - 60 * s, cx + 50 * s, cy + 60 * s), 8 * s, fill=PAPER)
    for k in range(n):
        y = cy - 40 * s + k * 20 * s
        c.rrect((cx - 38 * s, y - 6 * s, cx - 26 * s, y + 6 * s), 2, fill=OKG if k < done else (200, 196, 184))
        c.rrect((cx - 18 * s, y - 3 * s, cx + 34 * s - (k % 3) * 10 * s, y + 3 * s), 2, fill=(170, 166, 154))

def ic_gift2(c, cx, cy, s, col=SKY):
    c.rrect((cx - 66 * s, cy - 42 * s, cx + 66 * s, cy + 42 * s), 10 * s, fill=col)
    c.rrect((cx - 66 * s, cy - 6 * s, cx + 66 * s, cy + 6 * s), 1, fill=GOLD)
    c.text((cx - 24 * s, cy - 24 * s), "ALDI", FONT_SANS, 17 * s, IVORY)
    c.text((cx + 28 * s, cy + 24 * s), "GIFT", FONT_SANS, 17 * s, IVORY)

def ic_megaphone(c, cx, cy, s, col=GOLD):
    c.poly([(cx - 50 * s, cy - 14 * s), (cx + 30 * s, cy - 44 * s), (cx + 30 * s, cy + 44 * s), (cx - 50 * s, cy + 14 * s)], fill=col)
    c.rrect((cx - 60 * s, cy - 16 * s, cx - 44 * s, cy + 16 * s), 4, fill=col)
    c.rrect((cx - 40 * s, cy + 14 * s, cx - 20 * s, cy + 46 * s), 4, fill=col)

def ic_heart2(c, cx, cy, s, col=CORAL):
    c.ell((cx - 44 * s, cy - 40 * s, cx + 2 * s, cy + 6 * s), fill=col); c.ell((cx - 2 * s, cy - 40 * s, cx + 44 * s, cy + 6 * s), fill=col)
    c.poly([(cx - 42 * s, cy - 8 * s), (cx + 42 * s, cy - 8 * s), (cx, cy + 46 * s)], fill=col)

def ic_bell(c, cx, cy, s, col=GOLD):
    c.poly([(cx - 40 * s, cy + 24 * s), (cx - 30 * s, cy - 24 * s), (cx, cy - 46 * s), (cx + 30 * s, cy - 24 * s), (cx + 40 * s, cy + 24 * s)], fill=col)
    c.rrect((cx - 46 * s, cy + 20 * s, cx + 46 * s, cy + 34 * s), 5 * s, fill=col)
    c.ell((cx - 9 * s, cy + 34 * s, cx + 9 * s, cy + 50 * s), fill=col)

def phone9(key, w=300, h=560, screen=None):
    """telefono con schermo; screen(c,x0,y0,x1,y1)"""
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 40, fill=(26, 32, 34), outline=(120, 132, 130), width=4)
        c.rrect((16, 16, w - 16, h - 16), 30, fill=PAPER)
        c.rrect((w / 2 - 40, 22, w / 2 + 40, 34), 6, fill=(26, 32, 34))
        if screen:
            screen(c, 16, 44, w - 16, h - 40)
    return mk(("ph9", key, w, h), w, h, fn, blur=16, dy=12)

def laptop9(key, w=720, h=470, screen=None, bar="aldi.us"):
    def fn(c):
        c.rrect((60, 4, w - 60, h - 56), 22, fill=(30, 36, 38), outline=(120, 132, 130), width=4)
        c.rrect((78, 20, w - 78, h - 74), 10, fill=PAPER)
        c.rrect((78, 20, w - 78, 66), 10, fill=(214, 224, 218))
        c.d.rectangle(c._b((78, 48, w - 78, 66)), fill=(214, 224, 218))
        for k in range(3):
            c.ell((96 + k * 24, 36, 110 + k * 24, 50), fill=(CORAL, AMBER, OKG)[k])
        c.rrect((190, 32, w - 100, 56), 12, fill=PAPER)
        c.text((206, 44), bar, FONT_SANS_M, 18, (90, 100, 94), anchor="lm")
        c.poly([(0, h - 52), (w, h - 52), (w - 40, h - 20), (40, h - 20)], fill=(150, 160, 160))
        if screen:
            screen(c, 78, 70, w - 78, h - 74)
    return mk(("lt9", key, w, h), w, h, fn, blur=16, dy=12)

def receipt9(key, w, h, rows, title="ALDI", hl=None, foot=None, hlcol=GOLD):
    """scontrino lungo: rows = lista di (testo, importo?) senza cifre; hl = indice riga evidenziata"""
    def fn(c):
        c.rrect((0, 10, w, h - 10), 8, fill=PAPER)
        for k in range(0, w, 24):
            c.poly([(k, 12), (k + 12, 0), (k + 24, 12)], fill=PAPER)
            c.poly([(k, h - 12), (k + 12, h), (k + 24, h - 12)], fill=PAPER)
        c.text((w / 2, 52), title, FONT_SANS, 34, INK, track=8)
        for k in range(24, w - 24, 14):
            c.line([(k, 86), (k + 7, 86)], (170, 166, 154), 2)
        n = len(rows)
        gap = (h - 190) / max(1, n)
        for i, (a, b_) in enumerate(rows):
            y = 120 + gap * (i + 0.5)
            if hl is not None and i == hl:
                c.rrect((10, y - gap * 0.46, w - 10, y + gap * 0.46), 8, fill=hlcol)
            c.text((28, y), a, FONT_SANS, 24, INK, anchor="lm", track=2)
            if b_:
                c.text((w - 28, y), b_, FONT_SANS, 24, INK, anchor="rm", track=1)
        if foot:
            c.text((w / 2, h - 44), foot, FONT_SANS, 20, (110, 110, 100), track=3)
    return mk(("rc9", key, w, h), w, h, fn, blur=14, dy=10)

def checklist9(key, w, rows, size=34, gap=74, col=OKG):
    """righe con spunta; rows: lista di str"""
    h = gap * len(rows) + 20
    def fn(c):
        for i, r_ in enumerate(rows):
            y = 20 + i * gap + gap / 2
            c.ell((6, y - 24, 54, y + 24), fill=col)
            check_ic(c, 30, y + 1, 0.42, GREEN_D)
            s = size
            while tw(r_, s, 2) > w - 90 and s > 14:
                s -= 2
            c.text((74, y), r_, FONT_SANS, s, IVORY, anchor="lm", track=2)
    return mk(("chk9", key, w), w, h, fn, shadow=False)

def map_pin9(S=64, col=GOLD):
    return mk(("pin9", S, col), S, int(S * 1.3), lambda c: (c.ell((S * 0.12, S * 0.06, S * 0.88, S * 0.82), fill=col), c.poly([(S * 0.2, S * 0.62), (S * 0.8, S * 0.62), (S * 0.5, S * 1.24)], fill=col), c.ell((S * 0.34, S * 0.28, S * 0.66, S * 0.6), fill=GREEN_D)), blur=7, dy=5)

def say9(key, w, h, lines, size=40, fill=IVORY, ink=INK, tail="bl", border=GOLD):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 34, fill=fill, outline=border, width=5)
        if tail == "bl":
            c.poly([(70, h - 10), (140, h - 10), (50, h + 44)], fill=fill)
        elif tail == "br":
            c.poly([(w - 140, h - 10), (w - 70, h - 10), (w - 50, h + 44)], fill=fill)
        n = len(lines)
        for i, ln in enumerate(lines):
            s_ = size
            while tw(ln, s_, 2) > w - 60 and s_ > 16:
                s_ -= 2
            c.text((w / 2, h / 2 + (i - (n - 1) / 2) * size * 1.22), ln, FONT_SANS, s_, ink, track=2)
    return mk(("say9", key, w, h), w, h + 50, fn)
