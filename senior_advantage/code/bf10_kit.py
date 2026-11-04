"""Video lungo 10 (BLACK FRIDAY: RESI E PRICE MATCH) - kit grafico. 1920x1080, 30 fps.
Stile NUOVO (ordine utente 04/11: slide piu diverse, elementi diversi, piu professionali, piu belle, per tutto il video):
- sfondo verde bosco Walmart con nastri diagonali che scorrono, puntini da perforazione e luci dorate che galleggiano;
- testata a BIGLIETTO (talloncino oro + etichetta avorio con tacche) e NAVIGATORE dei tre negozi (Walmart / Target / Costco);
- schede di carta avorio "da fascicolo" con bordo oro, anelli-calendario con il numero dei giorni, LINEE DEL TEMPO con date vere,
  cartellini con il buco e lo spago, timbri, cassa (POS), icone nuove (TV, frigo, apparecchio acustico, occhiali, drone...).
Colori del canale: verde bosco, avorio, oro (corallo solo per i NO). Niente blu/viola/arancio."""
import os, sys, math, re, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from long9_kit import *            # mk, bake, show, grow_x, vgrad, pill9, paper9, glass9, stamp9, bignum, okb, xb, arrow9, say9, receipt9, ic_*, END, settle, Cv, put, cache, tw, colori
import long9_kit as K
from PIL import Image, ImageDraw, ImageFilter

_poly0 = Cv.poly
def _poly(self, pts, fill=None, outline=None, width=1):
    if fill is not None:
        _poly0(self, pts, fill)
    if outline:
        self.d.line([(x * self.ss, y * self.ss) for x, y in list(pts) + [pts[0]]], fill=outline, width=max(1, int(width * self.ss)), joint="curve")
Cv.poly = _poly

COP10 = os.path.join(HERE, "..", "COPIONE-VIDEO-BLACK-FRIDAY.md")
TEXT = {int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$", open(COP10, encoding="utf-8").read())}
# fine di ogni blocco in fotogrammi (screenshot CapCut 04/11/2026, vedi screenshot_durate_blackfriday/DURATE.md)
ENDS10 = [795, 1649, 2524, 3466, 4488, 5504, 6415, 7345, 8371, 9415, 10417, 11420, 12457, 13402, 14413, 15385, 16414, 17390, 18373, 19143]
DUR = {i + 1: e - (ENDS10[i - 1] if i else 0) for i, e in enumerate(ENDS10)}
PAPER2 = (236, 231, 214)
GOLD_D = (168, 118, 40)
FOREST = (14, 62, 50)

def T(b, key, n=1):
    """secondo in cui la voce arriva alla parola 'key' (n-esima occorrenza) del blocco b; mai oltre il 78% del blocco"""
    s = TEXT[b]; i = -1
    for _ in range(n):
        i = s.index(key, i + 1)
    d = DUR[b] / FPS
    return max(0.15, min(0.1 + d * 0.94 * i / len(s) - 0.12, d * 0.78))

def LAST(b):
    return DUR[b] / FPS * 0.8

def tm(b, frac):
    """istante a una frazione della durata del blocco (per elementi non legati a una parola)"""
    return DUR[b] / FPS * frac

# ------------------------------------------------------------------ animazione (come show di long9_kit, ma gli ingressi scorrono di soli 40 px: niente taglio dai bordi)
def show(img, t, t0, spr, cx, cy, mode="pop", amp=5.0, ph=0.0, t_out=None, scale=1.0, rot=0.0, dur=0.5, alpha=1.0, fl=True):
    if t < t0:
        return 0.0
    p = ease(seg(t, t0, dur))
    ox = oy = 0.0; s = scale; a = min(1.0, p * 2.6)
    if mode == "pop":
        s = scale * max(0.01, ease_back(seg(t, t0, dur)))
    elif mode == "up":
        oy = 44 * (1 - p)
    elif mode == "down":
        oy = -44 * (1 - p)
    elif mode == "left":
        ox = -40 * (1 - p)
    elif mode == "right":
        ox = 40 * (1 - p)
    elif mode == "zoom":
        s = scale * (0.6 + 0.4 * p)
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

# ------------------------------------------------------------------ sfondo
_BG = {}
def _mk_bg():
    base = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(base)
    for y in range(H):
        k = y / H
        d.line([(0, y), (W, y)], fill=(int(9 + 7 * (1 - k)), int(38 + 20 * (1 - k)), int(31 + 13 * (1 - k))))
    glow = Image.new("L", (W, H), 0); gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.12, -H * 0.55, W * 0.88, H * 0.45], fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(170))
    base = Image.composite(Image.new("RGB", (W, H), (34, 98, 74)), base, glow)
    vig = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(vig)
    vd.rectangle([0, 0, W, H], fill=110); vd.ellipse([-W * 0.2, -H * 0.3, W * 1.2, H * 1.3], fill=0)
    vig = vig.filter(ImageFilter.GaussianBlur(150))
    _BG["base"] = Image.composite(Image.new("RGB", (W, H), (3, 20, 15)), base, vig)
    # nastri diagonali (periodo 520 px in orizzontale)
    P = 520
    rb = Image.new("RGBA", (W + P + 600, H + 40), (0, 0, 0, 0)); rd = ImageDraw.Draw(rb)
    for x0 in range(-H, W + P + 600, P):
        rd.polygon([(x0, H + 40), (x0 + 120, H + 40), (x0 + 120 + H * 0.58, 0), (x0 + H * 0.58, 0)], fill=(150, 215, 180, 13))
        rd.polygon([(x0 + 190, H + 40), (x0 + 200, H + 40), (x0 + 200 + H * 0.58, 0), (x0 + 190 + H * 0.58, 0)], fill=(228, 179, 99, 22))
    _BG["rb"] = rb; _BG["P"] = P
    # punti di perforazione
    g = Image.new("RGBA", (W + 80, H + 80), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    for x in range(0, W + 80, 40):
        for y in range(0, H + 80, 40):
            gd.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(170, 225, 195, 26))
    _BG["dots"] = g
    # luci
    bl = Image.new("RGBA", (700, 700), (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)
    bd.ellipse([120, 120, 580, 580], fill=(232, 190, 110, 40))
    _BG["blob"] = bl.filter(ImageFilter.GaussianBlur(90))
    bk = Image.new("RGBA", (90, 90), (0, 0, 0, 0)); kd = ImageDraw.Draw(bk)
    kd.ellipse([20, 20, 70, 70], fill=(240, 205, 130, 55), outline=(240, 215, 150, 95), width=2)
    _BG["bokeh"] = bk.filter(ImageFilter.GaussianBlur(1.5))

def background10(t):
    if not _BG:
        _mk_bg()
    img = _BG["base"].copy()
    for k, (sx, sy, sp) in enumerate(((0.18, 0.22, 0.19), (0.78, 0.72, 0.15))):
        x = int(W * sx + math.sin(t * sp + k * 2) * 240 - 350); y = int(H * sy + math.cos(t * sp * 0.8 + k) * 150 - 350)
        img.paste(_BG["blob"], (x, y), _BG["blob"])
    ox = int((t * 34) % _BG["P"])
    c = _BG["rb"].crop((ox, 0, ox + W, H)); img.paste(c, (0, 0), c)
    ox, oy = int((t * 12) % 40), int((t * 7) % 40)
    c = _BG["dots"].crop((ox, oy, ox + W, oy + H)); img.paste(c, (0, 0), c)
    for k in range(7):
        x = int((k * 331 + t * (11 + 3 * k)) % (W + 160)) - 80
        y = int(130 + (k * 197) % (H - 260) + math.sin(t * 0.5 + k) * 26)
        img.paste(_BG["bokeh"], (x - 45, y - 45), _BG["bokeh"])
    return img

# ------------------------------------------------------------------ testata a biglietto + navigatore dei negozi
STORES = ["WALMART", "TARGET", "COSTCO"]

def ticket_spr(label, sub=None):
    def build():
        w, h = 900, 100
        c = Cv(w, h)
        c.rrect((2, 4, w - 2, h - 4), 18, fill=PAPER, outline=(190, 184, 166), width=3)
        c.ell((-20, h / 2 - 22, 22, h / 2 + 22), fill=(10, 44, 36))
        c.ell((w - 22, h / 2 - 22, w + 20, h / 2 + 22), fill=(10, 44, 36))
        c.rrect((26, 16, 150, h - 16), 12, fill=GOLD)
        c.text((88, h / 2 + 2), "BF", FONT_SANS, 44, GREEN_D, track=2)
        for y in range(18, h - 18, 12):
            c.line([(166, y), (166, y + 6)], (170, 160, 130), 3)
        s = 42
        while tw(label, s, 3) > w - 250 and s > 20:
            s -= 2
        c.text((190, h / 2 + (-10 if sub else 2)), label, FONT_SANS, s, INK, anchor="lm", track=3)
        if sub:
            c.text((190, h / 2 + 26), sub, FONT_SANS_M, 22, (92, 118, 102), anchor="lm", track=3)
        return bake(c.done(), 10, 6, 0.5)
    return cache(("tk10", label, sub), build)

def navchip_spr(name, state):
    """state: 0 = da fare, 1 = attuale, 2 = fatto"""
    def build():
        w, h = 236, 64
        c = Cv(w, h)
        if state == 1:
            c.rrect((2, 2, w - 2, h - 2), 32, fill=GOLD, outline=IVORY, width=3)
            c.text((w / 2, h / 2 + 2), name, FONT_SANS, 28, GREEN_D, track=3)
        elif state == 2:
            c.rrect((2, 2, w - 2, h - 2), 32, fill=(20, 82, 64), outline=SAGE_D, width=3)
            c.ell((14, 14, 50, 50), fill=OKG)
            check_ic(c, 32, 33, 0.3, GREEN_D)
            c.text((w / 2 + 22, h / 2 + 2), name, FONT_SANS, 24, IVORY, track=2)
        else:
            c.rrect((2, 2, w - 2, h - 2), 32, fill=(10, 46, 38), outline=SAGE_D, width=3)
            c.text((w / 2, h / 2 + 2), name, FONT_SANS, 26, SAGE, track=3)
        return bake(c.done(), 8, 5, 0.5)
    return cache(("nv10", name, state), build)

def head10(img, t, label, store=None, sub=None):
    """store: None = nessuno in evidenza; 0/1/2 = Walmart/Target/Costco attuale (i precedenti risultano fatti)"""
    show(img, t, 0.05, ticket_spr(label, sub), 40 + 450, 82, mode="left", dur=0.6, fl=False)
    for i, n in enumerate(STORES):
        st = 0
        if store is not None:
            st = 1 if i == store else (2 if i < store else 0)
        show(img, t, 0.2 + 0.1 * i, navchip_spr(n, st), 1170 + i * 252 + 58, 82, mode="right", dur=0.5, fl=False)
    if t > 0.3:
        p = ease(seg(t, 0.3, 0.8))
        d = ImageDraw.Draw(img)
        x1 = 90 + 1740 * p
        off = int(t * 24) % 22
        for x in range(90 - off + 22, int(x1), 22):
            if x >= 90:
                d.line([(x, 146), (min(x + 11, x1), 146)], fill=GOLD, width=3)

def source10(img, t, t0, label, x=1560, y=1036):
    w = int(290 + tw(label, 22, 2))
    spr = mk(("src10", label), w, 58, lambda c: (
        c.rrect((2, 2, w - 2, 56), 28, fill=(8, 44, 38), outline=SAGE_D, width=3),
        c.rrect((16, 12, 38, 46), 4, fill=PAPER), c.line([(21, 22), (33, 22)], SAGE_D, 3), c.line([(21, 29), (33, 29)], SAGE_D, 3),
        c.text((50, 29), "OFFICIAL PAGE", FONT_SANS_M, 19, SAGE, anchor="lm", track=3),
        c.text((262, 29), label, FONT_SANS, 22, IVORY, anchor="lm", track=2)), blur=8, dy=5)
    show(img, t, t0, spr, min(x, 1900 - w / 2), y, mode="up", dur=0.45, fl=False)

# ------------------------------------------------------------------ mattoni
def dossier(key, w, h, title, lines=(), accent=GOLD, size=30, tsize=30, icon=None, align="left", ink=INK, title_ink=None):
    """scheda di carta 'da fascicolo': bordo oro a sinistra, titolo in maiuscolo con filetto, righe di testo"""
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), 20, fill=PAPER, outline=(196, 190, 170), width=3)
        c.rrect((3, 3, 30, h - 3), 14, fill=accent)
        c.d.rectangle(c._b((20, 3, 30, h - 3)), fill=accent)
        x0 = 52
        s = tsize
        while tw(title, s, 3) > w - x0 - (110 if icon else 30) and s > 14:
            s -= 2
        ty = 38
        c.text((w / 2 + 12 if align == "center" else x0, ty), title, FONT_SANS, s, title_ink or (GOLD_D if accent == GOLD else INK),
               anchor="mm" if align == "center" else "lm", track=3)
        c.line([(x0, 66), (w - 30, 66)], (210, 204, 186), 2)
        if icon:
            icon(c, w - 62, 38, 0.5)
        n = len(lines)
        top, bot = 84, h - 14
        gap = (bot - top) / max(1, n)
        for i, ln in enumerate(lines):
            col = ink
            if isinstance(ln, tuple):
                ln, col = ln
            s2 = size
            while tw(ln, s2, 2) > w - x0 - 28 and s2 > 14:
                s2 -= 2
            yy = top + gap * (i + 0.5)
            c.text((w / 2 + 12 if align == "center" else x0, yy), ln, FONT_SANS_M if size <= 30 else FONT_SANS, s2, col,
                   anchor="mm" if align == "center" else "lm", track=1)
    return mk(("dos10", key, w, h), w, h, fn)

def tile(key, w, h, icon, title, sub=None, accent=GOLD, icon_s=1.0, tsize=26, ssize=21, dark=False):
    """tessera verticale: tondo con icona in alto, titolo e sottotitolo sotto (carta avorio o vetro scuro); il tondo si adatta all'altezza"""
    lines = title.split("\n")
    sl = sub.split("\n") if sub else []
    textH = len(lines) * (tsize + 6) + (len(sl) * (ssize + 5) + 4 if sl else 0)
    r = max(30, min(w * 0.28, (h - 28 - 26 - textH - 16) / 2))
    def fn(c):
        if dark:
            vgrad(c, (3, 3, w - 3, h - 3), 24, (16, 70, 58), (8, 42, 34), outline=accent, width=4)
            tc, sc, rc = IVORY, GOLD, (24, 84, 68)
        else:
            c.rrect((3, 3, w - 3, h - 3), 24, fill=PAPER, outline=(196, 190, 170), width=3)
            c.rrect((3, 3, w - 3, 16), 12, fill=accent)
            tc, sc, rc = INK, (120, 90, 30), (34, 96, 76)
        cy = 28 + r
        c.ell((w / 2 - r, cy - r, w / 2 + r, cy + r), fill=rc, outline=accent, width=4)
        icon(c, w / 2, cy, icon_s * r / 74)
        ty = cy + r + 26 + tsize / 2
        for i, ln in enumerate(lines):
            s_ = tsize
            while tw(ln, s_, 2) > w - 22 and s_ > 12:
                s_ -= 2
            c.text((w / 2, ty + i * (tsize + 6)), ln, FONT_SANS, s_, tc, track=2)
        if sl:
            ys = ty + len(lines) * (tsize + 6) + 2
            for i, ln in enumerate(sl):
                s_ = ssize
                while tw(ln, s_, 1) > w - 22 and s_ > 11:
                    s_ -= 2
                c.text((w / 2, ys + i * (ssize + 5)), ln, FONT_SANS_M, s_, sc, track=1)
    return mk(("tile10", key, w, h, dark), w, h, fn)

def banner10(key, w, h, text, fill=GOLD, ink=GREEN_D, size=None, border=None, sub=None, sub_ink=None):
    """nastro con coda a V (testata di sezione)"""
    def fn(c):
        n = 22
        c.poly([(3, 3), (w - 3, 3), (w - 3 - n, h / 2), (w - 3, h - 3), (3, h - 3), (3 + n, h / 2)], fill=fill)
        if border:
            c.line([(3, 3), (w - 3, 3), (w - 3 - n, h / 2), (w - 3, h - 3), (3, h - 3), (3 + n, h / 2), (3, 3)], border, 3)
        s = size or int(h * 0.46)
        while tw(text, s, 3) > w - 2 * n - 40 and s > 14:
            s -= 2
        c.text((w / 2, h / 2 + (-9 if sub else 2)), text, FONT_SANS, s, ink, track=3)
        if sub:
            c.text((w / 2, h / 2 + 24), sub, FONT_SANS_M, int(h * 0.22), sub_ink or ink, track=2)
    return mk(("ban10", key, w, h, fill), w, h, fn, blur=9, dy=6)

def hangtag(key, w, h, big, small=None, col=GOLD, ink=GREEN_D, bsize=None, ssize=None, string=True):
    """cartellino con il buco e lo spago"""
    def fn(c):
        top = 34
        c.poly([(30, top + 26), (w / 2 - 36, top), (w / 2 + 36, top), (w - 30, top + 26), (w - 6, h - 6), (6, h - 6)], fill=col)
        c.ell((w / 2 - 12, top + 8, w / 2 + 12, top + 32), fill=(10, 44, 36), outline=(150, 100, 30) if col == GOLD else IVORY, width=3)
        if string:
            c.line([(w / 2, top + 20), (w / 2 - 22, 8), (w / 2 + 10, 3)], IVORY, 4)
        bs = bsize or int(h * 0.30)
        while tw(big, bs, 2) > w - 40 and bs > 14:
            bs -= 2
        c.text((w / 2, top + (h - top) * (0.46 if small else 0.55)), big, FONT_SANS, bs, ink, track=1)
        if small:
            ss = ssize or int(h * 0.11)
            while tw(small, ss, 2) > w - 36 and ss > 11:
                ss -= 2
            c.text((w / 2, top + (h - top) * 0.80), small, FONT_SANS, ss, ink, track=2)
    return mk(("htag10", key, w, h), w, h, fn)

def dial(key, S, value, label, frac=1.0, col=GOLD, vsize=None, sub=None):
    """anello con il numero dei giorni al centro"""
    q = int(round(frac * 20)) / 20.0
    def fn(c):
        c.ell((6, 6, S - 6, S - 6), fill=(10, 50, 40), outline=(26, 88, 70), width=6)
        m = 22
        c.arc((m, m, S - m, S - m), 0, 360, (22, 74, 60), 22)
        if q > 0:
            c.arc((m, m, S - m, S - m), -90, -90 + 360 * q, col, 22)
        vs = vsize or int(S * 0.34)
        while tw(value, vs, 1) > S * 0.56 and vs > 18:
            vs -= 2
        c.text((S / 2, S * 0.43), value, FONT_SANS, vs, IVORY, track=0)
        s = int(S * 0.095)
        while tw(label, s, 3) > S * 0.60 and s > 10:
            s -= 1
        c.text((S / 2, S * 0.64), label, FONT_SANS, s, col, track=3)
        if sub:
            c.text((S / 2, S * 0.76), sub, FONT_SANS_M, int(S * 0.062), SAGE, track=2)
    return mk(("dial10", key, S, q), S, S, fn, blur=14, dy=9)

def dial_show(img, t, t0, key, S, value, label, x, y, col=GOLD, dur=1.0, **kw):
    """anello che si riempie"""
    if t < t0:
        return
    p = ease(seg(t, t0, dur))
    fr = 1.0 if p >= 1 else p
    spr = dial(key, S, value, label, fr, col, **kw)
    a = min(1.0, (t - t0) * 4)
    k = settle(t)
    oy = 4 * math.sin(t * 1.7 + x * 0.01) * k
    put(img, spr, x, y + oy, alpha=a)

def stampbox(key, w, h, text, col=CORAL, size=None, sub=None):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 14, fill=(10, 40, 34), outline=col, width=6)
        c.rrect((14, 14, w - 14, h - 14), 8, outline=col, width=2)
        s = size or int(h * 0.36)
        while tw(text, s, 3) > w - 44 and s > 14:
            s -= 2
        c.text((w / 2, h / 2 + (-10 if sub else 2)), text, FONT_SANS, s, col, track=3)
        if sub:
            c.text((w / 2, h / 2 + 26), sub, FONT_SANS_M, int(h * 0.19), IVORY, track=2)
    return mk(("sbx10", key, w, h, col), w, h, fn, blur=8, dy=5)

def strip10(key, w, h, text, fill=(10, 50, 40), ink=IVORY, border=SAGE_D, size=None, icon=None, icon_col=GOLD, bold=False):
    """striscia orizzontale (voce di elenco) con eventuale icona/numero a sinistra"""
    def fn(c):
        c.rrect((3, 3, w - 3, h - 3), h / 2 - 3, fill=fill, outline=border, width=3)
        x0 = 26
        if icon:
            r = h / 2 - 8
            c.ell((10, h / 2 - r, 10 + 2 * r, h / 2 + r), fill=(20, 84, 66), outline=icon_col, width=3)
            icon(c, 10 + r, h / 2, r / 52 * 0.62)
            x0 = 10 + 2 * r + 16
        s = size or int(h * 0.40)
        while tw(text, s, 2) > w - x0 - 22 and s > 12:
            s -= 2
        c.text((x0, h / 2 + 2), text, FONT_SANS if bold else FONT_SANS_M, s, ink, anchor="lm", track=2)
    return mk(("strip10", key, w, h, fill), w, h, fn, blur=8, dy=5)

def xcircle(S=84, col=CORAL):
    return mk(("xc10", S, col), S, S, lambda c: (c.ell((3, 3, S - 3, S - 3), fill=col), ic_x(c, S / 2, S / 2, S / 180, IVORY, 16)), blur=7, dy=5)

def okcircle(S=84, col=OKG):
    return mk(("oc10", S, col), S, S, lambda c: (c.ell((3, 3, S - 3, S - 3), fill=col), check_ic(c, S / 2, S / 2 + 2, S / 120, GREEN_D)), blur=7, dy=5)

# ------------------------------------------------------------------ linee del tempo con date vere
class TL:
    """asse del tempo: x(data) lineare tra d0 e d1 su [x0, x1]"""
    def __init__(self, d0, d1, x0, x1):
        self.d0, self.d1, self.x0, self.x1 = d0, d1, x0, x1
        self.ppd = (x1 - x0) / ((d1 - d0).days + 1)
    def x(self, d):
        return self.x0 + ((d - self.d0).days) * self.ppd
    def xe(self, d):          # fine del giorno
        return self.x0 + ((d - self.d0).days + 1) * self.ppd

def D(m, d, y=2026):
    return datetime.date(y, m, d)

def axis_spr(tl, h=96):
    """asse con i mesi e i giorni: sprite largo quanto la linea del tempo"""
    def build():
        w = int(tl.x1 - tl.x0) + 8
        c = Cv(w, h)
        c.rrect((0, 30, w, 66), 8, fill=(10, 50, 40), outline=SAGE_D, width=3)
        d = tl.d0
        while d <= tl.d1:
            x = (d - tl.d0).days * tl.ppd + 4
            if d.day == 1:
                c.line([(x, 22), (x, 74)], GOLD, 4)
                nm = d.strftime("%b").upper()
                yy = d.year
                c.text((x + 12, 48), nm + (" %d" % yy if d.month == 1 else ""), FONT_SANS, 24, IVORY, anchor="lm", track=3)
            elif d.weekday() == 0:
                c.line([(x, 38), (x, 58)], (60, 120, 98), 2)
            if d == tl.d0 and d.day != 1:
                c.text((x + 12, 48), d.strftime("%b").upper(), FONT_SANS, 24, IVORY, anchor="lm", track=3)
            d += datetime.timedelta(days=1)
        return c.done()
    return cache(("ax10", tl.d0, tl.d1, tl.x0, tl.x1), build)

def bar_spr(w, h, text, fill=GOLD, ink=GREEN_D, size=None, right_cap=True, hatch=False, shadow=True, left=0):
    def fn(c):
        c.rrect((2, 2, w - 2, h - 2), h / 2 - 2, fill=fill)
        if hatch:
            for x in range(-h, w, 26):
                c.line([(max(2, x), h - 4 if x >= 2 else h - 4 - (2 - x)), (min(w - 2, x + h - 8), 4)], tuple(min(255, v + 18) for v in fill), 6)
        s = size or int(h * 0.42)
        while tw(text, s, 2) > w - 36 and s > 12:
            s -= 2
        if left:
            c.text((left, h / 2 + 2), text, FONT_SANS, s, ink, anchor="lm", track=2)
        else:
            c.text((w / 2, h / 2 + 2), text, FONT_SANS, s, ink, track=2)
    return mk(("bar10", text, w, h, fill, hatch, shadow, left), w, h, fn, blur=8, dy=5, shadow=shadow)

def flag10(text, sub=None, col=GOLD, ink=GREEN_D, w=None, down=False):
    """bandierina con asta: sull'asse del tempo (si ancora in basso al centro dell'asta)"""
    s = 24
    ww = w or max(150, int(tw(text, s, 2) + 44))
    hh = 62 if not sub else 92
    def fn(c):
        c.rrect((3, 3, ww - 3, hh - 3), 12, fill=col)
        c.text((ww / 2, 3 + (hh - 6) / (2 if not sub else 3.2)), text, FONT_SANS, s, ink, track=2)
        if sub:
            c.text((ww / 2, hh - 24), sub, FONT_SANS_M, 19, ink, track=1)
    return mk(("flag10", text, sub, col, ww), ww, hh, fn, blur=8, dy=5)

def post10(x, y0, y1, col=GOLD, w=5):
    """asta verticale (disegno diretto, y0<y1)"""
    return (x, y0, y1, col, w)

def draw_posts(img, posts, alpha=1.0):
    d = ImageDraw.Draw(img)
    for (x, y0, y1, col, w) in posts:
        d.line([(x, y0), (x, y1)], fill=col, width=w)
        d.ellipse([x - 9, y1 - 9, x + 9, y1 + 9], fill=col)

# ------------------------------------------------------------------ icone nuove
def ic_tv(c, cx, cy, s):
    c.rrect((cx - 66 * s, cy - 46 * s, cx + 66 * s, cy + 34 * s), 8 * s, fill=(34, 42, 44), outline=(120, 132, 130), width=3)
    c.rrect((cx - 58 * s, cy - 38 * s, cx + 58 * s, cy + 26 * s), 4 * s, fill=(176, 206, 192))
    c.poly([(cx - 40 * s, cy - 38 * s), (cx - 14 * s, cy - 38 * s), (cx - 44 * s, cy + 26 * s), (cx - 58 * s, cy + 26 * s), (cx - 58 * s, cy - 10 * s)], fill=(206, 228, 216))
    c.poly([(cx - 26 * s, cy + 34 * s), (cx + 26 * s, cy + 34 * s), (cx + 40 * s, cy + 54 * s), (cx - 40 * s, cy + 54 * s)], fill=(120, 132, 130))

def ic_fridge(c, cx, cy, s):
    c.rrect((cx - 40 * s, cy - 62 * s, cx + 40 * s, cy + 60 * s), 10 * s, fill=(226, 232, 228), outline=(150, 162, 156), width=3)
    c.line([(cx - 40 * s, cy - 14 * s), (cx + 40 * s, cy - 14 * s)], (150, 162, 156), 4 * s)
    c.rrect((cx + 20 * s, cy - 48 * s, cx + 28 * s, cy - 24 * s), 3, fill=(120, 132, 128))
    c.rrect((cx + 20 * s, cy + 0 * s, cx + 28 * s, cy + 30 * s), 3, fill=(120, 132, 128))
    c.rrect((cx - 30 * s, cy + 60 * s, cx - 20 * s, cy + 68 * s), 2, fill=(90, 100, 96)); c.rrect((cx + 20 * s, cy + 60 * s, cx + 30 * s, cy + 68 * s), 2, fill=(90, 100, 96))

def ic_hearing(c, cx, cy, s):
    skin = (226, 184, 150)
    c.ell((cx - 44 * s, cy - 52 * s, cx + 6 * s, cy + 44 * s), fill=skin)
    c.ell((cx - 30 * s, cy - 36 * s, cx - 6 * s, cy + 20 * s), fill=(196, 150, 120))
    c.arc((cx - 16 * s, cy - 60 * s, cx + 56 * s, cy + 30 * s), 215, 330, GOLD, 13 * s)
    c.ell((cx + 22 * s, cy - 20 * s, cx + 52 * s, cy + 36 * s), fill=GOLD, outline=GOLD_D, width=3 * s)
    c.line([(cx + 26 * s, cy - 8 * s), (cx - 14 * s, cy - 6 * s)], GOLD_D, 5 * s)


def ic_glasses(c, cx, cy, s):
    for dx in (-30, 30):
        c.ell((cx + (dx - 28) * s, cy - 26 * s, cx + (dx + 28) * s, cy + 30 * s), fill=(214, 232, 224, 140), outline=IVORY, width=6 * s)
    c.arc((cx - 12 * s, cy - 20 * s, cx + 12 * s, cy + 8 * s), 200, 340, IVORY, 6 * s)
    c.line([(cx - 58 * s, cy - 10 * s), (cx - 74 * s, cy - 18 * s)], IVORY, 6 * s)
    c.line([(cx + 58 * s, cy - 10 * s), (cx + 74 * s, cy - 18 * s)], IVORY, 6 * s)

def ic_lens(c, cx, cy, s):
    c.rrect((cx - 66 * s, cy + 6 * s, cx + 66 * s, cy + 52 * s), 12 * s, fill=(226, 232, 228), outline=(150, 162, 156), width=3)
    c.ell((cx - 54 * s, cy + 14 * s, cx - 6 * s, cy + 44 * s), fill=(176, 206, 192))
    c.ell((cx + 6 * s, cy + 14 * s, cx + 54 * s, cy + 44 * s), fill=(176, 206, 192))
    c.ell((cx - 30 * s, cy - 52 * s, cx + 30 * s, cy + 2 * s), fill=(214, 236, 230), outline=IVORY, width=4 * s)
    c.arc((cx - 22 * s, cy - 44 * s, cx + 22 * s, cy - 6 * s), 200, 300, (150, 190, 176), 5 * s)

def ic_vacuum(c, cx, cy, s):
    c.rrect((cx - 56 * s, cy + 36 * s, cx + 24 * s, cy + 56 * s), 8 * s, fill=(70, 80, 80))
    c.line([(cx - 8 * s, cy + 40 * s), (cx + 16 * s, cy - 40 * s)], (190, 198, 200), 12 * s)
    c.rrect((cx + 2 * s, cy - 62 * s, cx + 40 * s, cy - 8 * s), 12 * s, fill=GOLD, outline=GOLD_D, width=3 * s)
    c.ell((cx + 12 * s, cy - 44 * s, cx + 30 * s, cy - 26 * s), fill=(250, 226, 160))


def ic_tree(c, cx, cy, s):
    for k, (y0, wd) in enumerate(((-58, 36), (-30, 50), (0, 64))):
        c.poly([(cx, cy + y0 * s), (cx - wd * s, cy + (y0 + 40) * s), (cx + wd * s, cy + (y0 + 40) * s)], fill=(60, 150, 100))
    c.rrect((cx - 8 * s, cy + 40 * s, cx + 8 * s, cy + 58 * s), 2, fill=(130, 90, 56))
    for (x, y) in ((-14, -10), (18, 6), (-30, 24), (10, 28)):
        c.ell((cx + (x - 6) * s, cy + (y - 6) * s, cx + (x + 6) * s, cy + (y + 6) * s), fill=GOLD)

def ic_gem(c, cx, cy, s):
    c.poly([(cx - 52 * s, cy - 14 * s), (cx - 30 * s, cy - 44 * s), (cx + 30 * s, cy - 44 * s), (cx + 52 * s, cy - 14 * s), (cx, cy + 52 * s)], fill=(214, 238, 232))
    c.poly([(cx - 52 * s, cy - 14 * s), (cx + 52 * s, cy - 14 * s), (cx, cy + 52 * s)], fill=(172, 214, 204))
    c.poly([(cx - 30 * s, cy - 44 * s), (cx - 14 * s, cy - 14 * s), (cx, cy - 44 * s)], fill=(240, 252, 248))
    c.poly([(cx, cy - 44 * s), (cx + 14 * s, cy - 14 * s), (cx + 30 * s, cy - 44 * s)], fill=(190, 226, 216))

def ic_laptop(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 44 * s, cx + 50 * s, cy + 18 * s), 8 * s, fill=(34, 42, 44), outline=(120, 132, 130), width=3)
    c.rrect((cx - 42 * s, cy - 36 * s, cx + 42 * s, cy + 10 * s), 3 * s, fill=(176, 206, 192))
    c.poly([(cx - 68 * s, cy + 24 * s), (cx + 68 * s, cy + 24 * s), (cx + 54 * s, cy + 44 * s), (cx - 54 * s, cy + 44 * s)], fill=(150, 160, 160))

def ic_tablet(c, cx, cy, s):
    c.rrect((cx - 44 * s, cy - 56 * s, cx + 44 * s, cy + 56 * s), 12 * s, fill=(34, 42, 44), outline=(120, 132, 130), width=3)
    c.rrect((cx - 36 * s, cy - 46 * s, cx + 36 * s, cy + 44 * s), 4 * s, fill=(176, 206, 192))
    c.ell((cx - 4 * s, cy + 47 * s, cx + 4 * s, cy + 55 * s), fill=(120, 132, 130))

def ic_watch(c, cx, cy, s):
    c.rrect((cx - 20 * s, cy - 64 * s, cx + 20 * s, cy + 64 * s), 10 * s, fill=(120, 96, 70))
    c.rrect((cx - 38 * s, cy - 38 * s, cx + 38 * s, cy + 38 * s), 18 * s, fill=(34, 42, 44), outline=GOLD, width=4 * s)
    c.ell((cx - 26 * s, cy - 26 * s, cx + 26 * s, cy + 26 * s), fill=(176, 206, 192))
    c.line([(cx, cy), (cx, cy - 18 * s)], INK, 4 * s); c.line([(cx, cy), (cx + 12 * s, cy + 6 * s)], INK, 4 * s)

def ic_camera(c, cx, cy, s):
    c.rrect((cx - 62 * s, cy - 30 * s, cx + 62 * s, cy + 40 * s), 12 * s, fill=(60, 70, 72), outline=(120, 132, 130), width=3)
    c.rrect((cx - 30 * s, cy - 44 * s, cx + 10 * s, cy - 28 * s), 4 * s, fill=(60, 70, 72))
    c.ell((cx - 30 * s, cy - 24 * s, cx + 30 * s, cy + 36 * s), fill=(24, 30, 32), outline=(150, 160, 160), width=5 * s)
    c.ell((cx - 16 * s, cy - 10 * s, cx + 16 * s, cy + 22 * s), fill=(90, 130, 120))
    c.ell((cx - 8 * s, cy - 6 * s, cx + 0 * s, cy + 2 * s), fill=(210, 236, 226))
    c.rrect((cx + 40 * s, cy - 22 * s, cx + 54 * s, cy - 12 * s), 3, fill=GOLD)

def ic_drone(c, cx, cy, s):
    for (dx, dy) in ((-52, -34), (52, -34), (-52, 34), (52, 34)):
        c.line([(cx, cy), (cx + dx * s, cy + dy * s)], (110, 122, 122), 8 * s)
        c.ell((cx + (dx - 22) * s, cy + (dy - 6) * s, cx + (dx + 22) * s, cy + (dy + 6) * s), fill=(206, 214, 210))
    c.rrect((cx - 24 * s, cy - 16 * s, cx + 24 * s, cy + 16 * s), 8 * s, fill=(60, 70, 72), outline=GOLD, width=3 * s)
    c.ell((cx - 8 * s, cy - 6 * s, cx + 8 * s, cy + 10 * s), fill=(176, 206, 192))

def ic_camcorder(c, cx, cy, s):
    c.rrect((cx - 56 * s, cy - 30 * s, cx + 26 * s, cy + 32 * s), 10 * s, fill=(60, 70, 72), outline=(120, 132, 130), width=3)
    c.rrect((cx + 26 * s, cy - 22 * s, cx + 60 * s, cy + 14 * s), 6 * s, fill=(34, 42, 44), outline=(120, 132, 130), width=3)
    c.ell((cx - 44 * s, cy - 20 * s, cx - 10 * s, cy + 14 * s), fill=(24, 30, 32), outline=GOLD, width=4 * s)
    c.ell((cx - 36 * s, cy - 12 * s, cx - 18 * s, cy + 6 * s), fill=(90, 130, 120))
    c.rrect((cx - 56 * s, cy + 32 * s, cx + 20 * s, cy + 42 * s), 3, fill=(120, 132, 130))

def ic_mp3(c, cx, cy, s):
    c.rrect((cx - 34 * s, cy - 58 * s, cx + 34 * s, cy + 58 * s), 14 * s, fill=(226, 232, 228), outline=(150, 162, 156), width=3)
    c.rrect((cx - 24 * s, cy - 46 * s, cx + 24 * s, cy - 6 * s), 4 * s, fill=(60, 120, 100))
    c.ell((cx - 22 * s, cy + 4 * s, cx + 22 * s, cy + 48 * s), fill=(206, 212, 208), outline=(150, 162, 156), width=3)
    c.ell((cx - 8 * s, cy + 18 * s, cx + 8 * s, cy + 34 * s), fill=GOLD)

def ic_projector(c, cx, cy, s):
    c.poly([(cx + 30 * s, cy - 6 * s), (cx + 70 * s, cy - 34 * s), (cx + 70 * s, cy + 34 * s)], fill=(240, 228, 170, 150))
    c.rrect((cx - 66 * s, cy - 26 * s, cx + 36 * s, cy + 30 * s), 12 * s, fill=(200, 208, 204), outline=(150, 162, 156), width=3)
    c.ell((cx + 4 * s, cy - 16 * s, cx + 36 * s, cy + 16 * s), fill=(34, 42, 44), outline=GOLD, width=4 * s)
    c.ell((cx + 12 * s, cy - 8 * s, cx + 28 * s, cy + 8 * s), fill=(240, 228, 170))
    for k in range(4):
        c.line([(cx - 52 * s + k * 12 * s, cy - 14 * s), (cx - 52 * s + k * 12 * s, cy + 14 * s)], (150, 162, 156), 3 * s)

def ic_ticket(c, cx, cy, s):
    c.poly([(cx - 64 * s, cy - 30 * s), (cx + 64 * s, cy - 30 * s), (cx + 64 * s, cy - 8 * s), (cx + 52 * s, cy), (cx + 64 * s, cy + 8 * s), (cx + 64 * s, cy + 30 * s),
            (cx - 64 * s, cy + 30 * s), (cx - 64 * s, cy + 8 * s), (cx - 52 * s, cy), (cx - 64 * s, cy - 8 * s)], fill=PAPER)
    c.line([(cx + 26 * s, cy - 24 * s), (cx + 26 * s, cy + 24 * s)], (170, 164, 146), 3 * s)
    for k in range(3):
        c.rrect((cx - 48 * s, cy - 14 * s + k * 12 * s, cx + 8 * s - k * 8 * s, cy - 8 * s + k * 12 * s), 2, fill=(170, 164, 146))
    c.poly([(cx + 34 * s, cy + 12 * s), (cx + 56 * s, cy - 2 * s), (cx + 50 * s, cy + 2 * s), (cx + 56 * s, cy + 10 * s)], fill=GOLD_D)

def ic_goldbar(c, cx, cy, s):
    for (x, y, w_) in ((-34, 18, 62), (34, 18, 62), (0, -16, 62)):
        c.poly([(cx + (x - w_ / 2 + 8) * s, cy + (y - 18) * s), (cx + (x + w_ / 2 - 8) * s, cy + (y - 18) * s), (cx + (x + w_ / 2) * s, cy + (y + 18) * s), (cx + (x - w_ / 2) * s, cy + (y + 18) * s)], fill=GOLD, outline=GOLD_D, width=3 * s)
        c.line([(cx + (x - w_ / 2 + 10) * s, cy + (y - 10) * s), (cx + (x + w_ / 2 - 10) * s, cy + (y - 10) * s)], (250, 226, 160), 4 * s)

def ic_giftcard(c, cx, cy, s):
    c.rrect((cx - 62 * s, cy - 40 * s, cx + 62 * s, cy + 40 * s), 10 * s, fill=(60, 150, 100), outline=IVORY, width=3)
    c.rrect((cx - 8 * s, cy - 40 * s, cx + 8 * s, cy + 40 * s), 1, fill=GOLD)
    c.rrect((cx - 62 * s, cy - 6 * s, cx + 62 * s, cy + 6 * s), 1, fill=GOLD)
    c.ell((cx - 30 * s, cy - 36 * s, cx - 2 * s, cy - 6 * s), outline=GOLD, width=6 * s)
    c.ell((cx + 2 * s, cy - 36 * s, cx + 30 * s, cy - 6 * s), outline=GOLD, width=6 * s)

def ic_wrench(c, cx, cy, s):
    c.line([(cx - 44 * s, cy + 46 * s), (cx + 20 * s, cy - 18 * s)], (190, 198, 200), 22 * s)
    c.ell((cx + 6 * s, cy - 62 * s, cx + 62 * s, cy - 6 * s), fill=(190, 198, 200))
    c.ell((cx + 22 * s, cy - 48 * s, cx + 46 * s, cy - 24 * s), fill=(10, 46, 38))
    c.poly([(cx + 34 * s, cy - 36 * s), (cx + 64 * s, cy - 70 * s), (cx + 72 * s, cy - 40 * s)], fill=(10, 46, 38))
    c.ell((cx - 54 * s, cy + 36 * s, cx - 34 * s, cy + 56 * s), fill=(190, 198, 200))

def ic_tire(c, cx, cy, s):
    c.ell((cx - 56 * s, cy - 56 * s, cx + 56 * s, cy + 56 * s), fill=(40, 46, 46), outline=(90, 100, 100), width=4 * s)
    c.ell((cx - 30 * s, cy - 30 * s, cx + 30 * s, cy + 30 * s), fill=(176, 184, 186))
    c.ell((cx - 8 * s, cy - 8 * s, cx + 8 * s, cy + 8 * s), fill=(60, 70, 70))
    for k in range(5):
        a = math.radians(k * 72 - 90)
        c.ell((cx + 18 * s * math.cos(a) - 4 * s, cy + 18 * s * math.sin(a) - 4 * s, cx + 18 * s * math.cos(a) + 4 * s, cy + 18 * s * math.sin(a) + 4 * s), fill=(60, 70, 70))

def ic_battery(c, cx, cy, s):
    c.rrect((cx - 52 * s, cy - 28 * s, cx + 44 * s, cy + 28 * s), 8 * s, fill=(226, 232, 228), outline=(150, 162, 156), width=3)
    c.rrect((cx + 44 * s, cy - 12 * s, cx + 56 * s, cy + 12 * s), 3, fill=(150, 162, 156))
    c.poly([(cx + 4 * s, cy - 22 * s), (cx - 18 * s, cy + 4 * s), (cx - 2 * s, cy + 4 * s), (cx - 8 * s, cy + 22 * s), (cx + 18 * s, cy - 6 * s), (cx + 2 * s, cy - 6 * s)], fill=(60, 150, 100))

def ic_chat(c, cx, cy, s):
    c.rrect((cx - 56 * s, cy - 40 * s, cx + 56 * s, cy + 30 * s), 18 * s, fill=PAPER)
    c.poly([(cx - 30 * s, cy + 26 * s), (cx - 14 * s, cy + 26 * s), (cx - 38 * s, cy + 54 * s)], fill=PAPER)
    for k in range(3):
        c.ell((cx - 28 * s + k * 28 * s, cy - 14 * s, cx - 12 * s + k * 28 * s, cy + 2 * s), fill=GOLD_D)

def ic_handset(c, cx, cy, s):
    """cornetta classica: curva spessa con due capsule e onde"""
    pts = []
    for k in range(0, 25):
        u = k / 24.0
        x = (1 - u) ** 2 * -46 + 2 * u * (1 - u) * -10 + u ** 2 * 40
        y = (1 - u) ** 2 * 40 + 2 * u * (1 - u) * -50 + u ** 2 * -34
        pts.append((cx + x * s, cy + y * s))
    c.line(pts, IVORY, 17 * s)
    for (ex, ey, ang) in ((-46, 40, -50), (40, -34, -50)):
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a)
        c.line([(cx + (ex - 14 * ux) * s, cy + (ey - 14 * uy) * s), (cx + (ex + 14 * ux) * s, cy + (ey + 14 * uy) * s)], IVORY, 30 * s)
    for k in range(2):
        c.arc((cx + (30 + k * 14) * s, cy + (-70 - k * 14) * s, cx + (70 + k * 14) * s, cy + (-28 - k * 14) * s), 270, 350, GOLD, 5 * s)


def ic_desk(c, cx, cy, s):
    c.rrect((cx - 64 * s, cy - 6 * s, cx + 64 * s, cy + 52 * s), 6 * s, fill=(176, 132, 84), outline=(130, 92, 56), width=3)
    c.rrect((cx - 64 * s, cy - 14 * s, cx + 64 * s, cy + 2 * s), 4 * s, fill=(206, 164, 112))
    c.rrect((cx - 36 * s, cy - 58 * s, cx + 36 * s, cy - 18 * s), 6 * s, fill=PAPER, outline=(190, 184, 166), width=3)
    c.text((cx, cy - 38 * s), "i", FONT_SERIF, 34 * s, GOLD_D)
    c.ell((cx - 6 * s, cy - 24 * s, cx + 6 * s, cy - 14 * s), fill=GOLD_D)

def ic_scissors(c, cx, cy, s):
    c.line([(cx - 40 * s, cy + 36 * s), (cx + 30 * s, cy - 44 * s)], (206, 214, 214), 10 * s)
    c.line([(cx + 40 * s, cy + 36 * s), (cx - 30 * s, cy - 44 * s)], (206, 214, 214), 10 * s)
    c.ell((cx - 56 * s, cy + 22 * s, cx - 24 * s, cy + 54 * s), outline=CORAL, width=7 * s)
    c.ell((cx + 24 * s, cy + 22 * s, cx + 56 * s, cy + 54 * s), outline=CORAL, width=7 * s)

def ic_coupon(c, cx, cy, s):
    c.poly([(cx - 64 * s, cy - 30 * s), (cx + 64 * s, cy - 30 * s), (cx + 64 * s, cy - 8 * s), (cx + 52 * s, cy), (cx + 64 * s, cy + 8 * s), (cx + 64 * s, cy + 30 * s),
            (cx - 64 * s, cy + 30 * s), (cx - 64 * s, cy + 8 * s), (cx - 52 * s, cy), (cx - 64 * s, cy - 8 * s)], fill=GOLD)
    for x in range(-48, 56, 14):
        c.line([(cx + x * s, cy - 24 * s), (cx + (x + 6) * s, cy - 24 * s)], GOLD_D, 3 * s)
    c.text((cx, cy + 4 * s), "COUPON", FONT_SANS, 22 * s, GREEN_D, track=2)

def ic_pricetag(c, cx, cy, s, down=True):
    c.poly([(cx - 52 * s, cy - 8 * s), (cx - 8 * s, cy - 52 * s), (cx + 52 * s, cy - 52 * s), (cx + 52 * s, cy + 8 * s), (cx + 8 * s, cy + 52 * s)], fill=GOLD)
    c.ell((cx + 22 * s, cy - 40 * s, cx + 42 * s, cy - 20 * s), fill=(10, 46, 38))
    if down:
        c.line([(cx - 6 * s, cy - 18 * s), (cx - 6 * s, cy + 12 * s)], GREEN_D, 8 * s)
        c.poly([(cx - 22 * s, cy + 8 * s), (cx + 10 * s, cy + 8 * s), (cx - 6 * s, cy + 30 * s)], fill=GREEN_D)

def ic_openbox(c, cx, cy, s):
    c.poly([(cx - 50 * s, cy - 10 * s), (cx + 50 * s, cy - 10 * s), (cx + 50 * s, cy + 50 * s), (cx - 50 * s, cy + 50 * s)], fill=(206, 164, 108))
    c.poly([(cx - 50 * s, cy - 10 * s), (cx - 30 * s, cy - 44 * s), (cx - 4 * s, cy - 10 * s)], fill=(226, 186, 130))
    c.poly([(cx + 50 * s, cy - 10 * s), (cx + 30 * s, cy - 44 * s), (cx + 4 * s, cy - 10 * s)], fill=(226, 186, 130))
    c.rrect((cx - 12 * s, cy + 10 * s, cx + 12 * s, cy + 24 * s), 3, fill=(176, 132, 84))

def ic_crack(c, cx, cy, s):
    c.rrect((cx - 48 * s, cy - 40 * s, cx + 48 * s, cy + 46 * s), 8 * s, fill=(206, 164, 108))
    c.line([(cx + 8 * s, cy - 40 * s), (cx - 6 * s, cy - 14 * s), (cx + 12 * s, cy + 2 * s), (cx - 8 * s, cy + 24 * s), (cx + 6 * s, cy + 46 * s)], (60, 40, 24), 6 * s)
    c.line([(cx - 6 * s, cy - 14 * s), (cx - 30 * s, cy - 8 * s)], (60, 40, 24), 4 * s)

def ic_norcpt(c, cx, cy, s):
    c.rrect((cx - 34 * s, cy - 54 * s, cx + 34 * s, cy + 50 * s), 4 * s, fill=PAPER, outline=(190, 184, 170), width=2)
    for k in range(4):
        c.rrect((cx - 22 * s, cy - 38 * s + k * 16 * s, cx + (22 - (k % 2) * 14) * s, cy - 32 * s + k * 16 * s), 2, fill=(170, 166, 154))
    c.ell((cx + 4 * s, cy + 8 * s, cx + 64 * s, cy + 68 * s), fill=CORAL)
    ic_x(c, cx + 34 * s, cy + 38 * s, 0.34 * s, IVORY, 14)

def ic_barcode(c, cx, cy, s):
    c.rrect((cx - 56 * s, cy - 40 * s, cx + 56 * s, cy + 40 * s), 6 * s, fill=PAPER)
    x = -46
    for k, wd in enumerate((4, 2, 6, 2, 3, 6, 2, 4, 3, 2, 6, 3, 2, 4)):
        c.rrect((cx + x * s, cy - 26 * s, cx + (x + wd) * s, cy + 18 * s), 0, fill=INK)
        x += wd + 3
    c.text((cx, cy + 30 * s), "0 12345 67890", FONT_SANS_M, 10 * s, INK)

def ic_share(c, cx, cy, s):
    c.rrect((cx - 40 * s, cy - 8 * s, cx + 40 * s, cy + 52 * s), 10 * s, outline=IVORY, width=7 * s)
    c.line([(cx, cy + 22 * s), (cx, cy - 54 * s)], IVORY, 9 * s)
    c.poly([(cx - 26 * s, cy - 36 * s), (cx, cy - 66 * s), (cx + 26 * s, cy - 36 * s)], fill=IVORY)

def ic_thumb(c, cx, cy, s, col=IVORY):
    c.rrect((cx - 54 * s, cy - 6 * s, cx - 26 * s, cy + 48 * s), 6 * s, fill=col)
    c.poly([(cx - 20 * s, cy - 6 * s), (cx - 2 * s, cy - 50 * s), (cx + 16 * s, cy - 46 * s), (cx + 10 * s, cy - 16 * s), (cx + 52 * s, cy - 16 * s), (cx + 56 * s, cy + 40 * s), (cx - 20 * s, cy + 48 * s)], fill=col)

def ic_note2(c, cx, cy, s, col=GOLD):
    c.rrect((cx - 48 * s, cy - 40 * s, cx + 48 * s, cy + 40 * s), 8 * s, fill=col)
    c.text((cx, cy), "!", FONT_SANS, 64 * s, GREEN_D)

def ic_hand(c, cx, cy, s):
    c.rrect((cx - 36 * s, cy - 6 * s, cx + 36 * s, cy + 50 * s), 14 * s, fill=(226, 184, 150))
    for k in range(4):
        c.rrect((cx - 34 * s + k * 18 * s, cy - 46 * s + (0 if k % 3 else 6 * s), cx - 20 * s + k * 18 * s, cy + 6 * s), 7 * s, fill=(226, 184, 150))
    c.rrect((cx - 52 * s, cy - 2 * s, cx - 30 * s, cy + 30 * s), 8 * s, fill=(226, 184, 150))

def ic_house_pin(c, cx, cy, s):
    ic_pin8(c, cx, cy + 20 * s, 1.6 * s)

def ic_tagtag(c, cx, cy, s):
    ic_pricetag(c, cx, cy, s, down=False)

def ic_stack(c, cx, cy, s):
    for k in range(3):
        c.rrect((cx - 50 * s, cy - 40 * s + k * 26 * s, cx + 50 * s, cy - 18 * s + k * 26 * s), 6 * s, fill=PAPER if k % 2 == 0 else PAPER2, outline=(190, 184, 166), width=2)

def ic_car2(c, cx, cy, s):
    c.rrect((cx - 66 * s, cy - 6 * s, cx + 66 * s, cy + 30 * s), 12 * s, fill=(226, 232, 228), outline=(150, 162, 156), width=3)
    c.poly([(cx - 38 * s, cy - 6 * s), (cx - 22 * s, cy - 34 * s), (cx + 26 * s, cy - 34 * s), (cx + 44 * s, cy - 6 * s)], fill=(206, 214, 210))
    c.poly([(cx - 30 * s, cy - 8 * s), (cx - 18 * s, cy - 28 * s), (cx + 20 * s, cy - 28 * s), (cx + 34 * s, cy - 8 * s)], fill=(176, 206, 192))
    c.ell((cx - 52 * s, cy + 14 * s, cx - 24 * s, cy + 42 * s), fill=(40, 46, 46)); c.ell((cx + 24 * s, cy + 14 * s, cx + 52 * s, cy + 42 * s), fill=(40, 46, 46))

def ic_lightbulb(c, cx, cy, s):
    c.ell((cx - 34 * s, cy - 60 * s, cx + 34 * s, cy + 8 * s), fill=(250, 226, 160))
    c.rrect((cx - 18 * s, cy + 4 * s, cx + 18 * s, cy + 30 * s), 4 * s, fill=(170, 176, 176))
    c.line([(cx - 12 * s, cy + 40 * s), (cx + 12 * s, cy + 40 * s)], (130, 138, 138), 6 * s)

def ic_cardring(c, cx, cy, s):
    c.rrect((cx - 64 * s, cy - 40 * s, cx + 64 * s, cy + 40 * s), 10 * s, fill=(34, 42, 44), outline=GOLD, width=4)
    c.ell((cx - 52 * s, cy - 24 * s, cx - 16 * s, cy + 12 * s), outline=CORAL, width=6 * s)
    c.ell((cx - 42 * s, cy - 14 * s, cx - 26 * s, cy + 2 * s), fill=CORAL)
    c.rrect((cx + 0 * s, cy + 10 * s, cx + 50 * s, cy + 20 * s), 3, fill=IVORY)
    c.rrect((cx + 0 * s, cy - 14 * s, cx + 34 * s, cy - 6 * s), 3, fill=SAGE)

def ic_island(c, cx, cy, s):
    c.poly([(cx - 52 * s, cy + 14 * s), (cx - 40 * s, cy - 6 * s), (cx - 14 * s, cy - 14 * s), (cx + 20 * s, cy - 8 * s), (cx + 50 * s, cy + 8 * s), (cx + 40 * s, cy + 26 * s), (cx - 10 * s, cy + 32 * s)], fill=(206, 190, 130))
    c.line([(cx - 10 * s, cy - 10 * s), (cx - 10 * s, cy - 50 * s)], (130, 92, 56), 6 * s)
    for a in (-50, -20, 20, 50):
        c.line([(cx - 10 * s, cy - 50 * s), (cx - 10 * s + 34 * math.sin(math.radians(a)) * s, cy - 50 * s - 4 * s + 22 * math.cos(math.radians(a)) * s - 20 * s)], (60, 150, 100), 7 * s)

def ic_hourglass(c, cx, cy, s):
    c.poly([(cx - 32 * s, cy - 54 * s), (cx + 32 * s, cy - 54 * s), (cx + 4 * s, cy), (cx + 32 * s, cy + 54 * s), (cx - 32 * s, cy + 54 * s), (cx - 4 * s, cy)], fill=(226, 232, 228), outline=IVORY, width=3)
    c.poly([(cx - 22 * s, cy - 46 * s), (cx + 22 * s, cy - 46 * s), (cx + 2 * s, cy - 6 * s), (cx - 2 * s, cy - 6 * s)], fill=GOLD)
    c.poly([(cx - 24 * s, cy + 50 * s), (cx + 24 * s, cy + 50 * s), (cx + 10 * s, cy + 22 * s), (cx - 10 * s, cy + 22 * s)], fill=GOLD)
    c.rrect((cx - 40 * s, cy - 62 * s, cx + 40 * s, cy - 52 * s), 3, fill=GOLD_D); c.rrect((cx - 40 * s, cy + 52 * s, cx + 40 * s, cy + 62 * s), 3, fill=GOLD_D)


def grow_bar(img, t, t0, x0, x1, y, text, fill=GOLD, ink=GREEN_D, h=66, size=None, dur=0.7, hatch=False, left=0):
    """barra sul tempo che cresce da x0 a x1 (senza ombra, allineata esattamente alle date)"""
    if t < t0:
        return
    p = ease(seg(t, t0, dur))
    spr = bar_spr(int(x1 - x0), h, text, fill, ink, size, hatch=hatch, shadow=False, left=left)
    w = max(2, int(spr.width * p))
    put(img, spr.crop((0, 0, w, spr.height)), x0 + w / 2, y)


def ic_magnify(c, cx, cy, s):
    c.line([(cx + 20 * s, cy + 20 * s), (cx + 54 * s, cy + 54 * s)], GOLD_D, 14 * s)
    c.ell((cx - 50 * s, cy - 50 * s, cx + 32 * s, cy + 32 * s), fill=(214, 236, 230), outline=GOLD_D, width=9 * s)
    c.arc((cx - 36 * s, cy - 36 * s, cx + 18 * s, cy + 18 * s), 200, 280, (255, 255, 255), 6 * s)
