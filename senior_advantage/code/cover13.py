"""Copertina SHORT 13 (ALDI), 1080x1920. Ordine utente 26/10: "la miniatura attira click e curiosita". Regola 32: professionale, curiosita
(righe coperte da barre nere, cerchio e freccia rossi), colori accesi (blu Aldi, giallo, rosso, bianco), logo Aldi VERO (riferimenti/aldi/, SVG ufficiale di corporate.aldi.us).
Layout verticale: logo lucido in alto, "TOO GOOD / TO BE TRUE?" gigante (detto nello short), scheda "ALDI'S PROMISE" con 2 righe leggibili
(REPLACE IT, REFUND YOUR MONEY, dette nello short) e la riga delle condizioni coperta da barre nere con cerchio rosso + freccia rossa e targhetta "FINE PRINT?",
striscia bianca "10 THINGS FROM ALDI'S OWN PAGES" con targhetta rossa "FULL VIDEO BELOW". Niente nome della garanzia, niente scontrino, niente moneta (restano nel lungo).
uso: OUT=cartella python3 cover13.py"""
import os, math, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import thumb_long9 as T
W, H = 1080, 1920
T.W, T.H = W, H
SS = 2
OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
F, rot, sp, text3d, sheen, aldi_logo, glow, vignette = T.F, T.rot, T.sp, T.text3d, T.sheen, T.aldi_logo, T.glow, T.vignette
AYEL, ARED, ANAVY, INK = T.AYEL, T.ARED, T.ANAVY, T.INK


def vgrad_np(c0, c1, ang=-35):
    ys, xs = np.mgrid[0:H, 0:W]
    ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    span = abs(W * ca) + abs(H * sa)
    t = np.clip(((xs - W / 2) * ca + (ys - H / 2) * sa) / span + .5, 0, 1)[..., None]
    a = np.array(c0, float)[None, None, :]; b = np.array(c1, float)[None, None, :]
    return Image.fromarray((a + (b - a) * t).astype("uint8"), "RGB")


def stripes(im, col=(120, 200, 255), alpha=46):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for x0, wd, a in ((560, 80, alpha), (700, 140, int(alpha * .8)), (930, 250, int(alpha * .55))):
        d.polygon([(x0 + 520, -10), (x0 + 520 + wd, -10), (x0 + wd - 700, H + 10), (x0 - 700, H + 10)], fill=col + (a,))
    lay = lay.filter(ImageFilter.GaussianBlur(5))
    base = im.convert("RGBA"); base.alpha_composite(lay); return base.convert("RGB")


def promise_card(w=900, h=640):
    s = SS
    lay = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    S = lambda v: int(v * s)
    d.rounded_rectangle([S(4), S(4), S(w - 4), S(h - 4)], radius=S(40), fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=S(8))
    d.rounded_rectangle([S(4), S(4), S(w - 4), S(130)], radius=S(40), fill=ANAVY + (255,), outline=(0, 0, 0, 255), width=S(8))
    d.rectangle([S(10), S(90), S(w - 10), S(130)], fill=ANAVY + (255,))
    d.text((S(w / 2), S(70)), "ALDI'S PROMISE", font=F(S(66), "Black"), fill=AYEL, anchor="mm")
    for i, word in enumerate(("REPLACE IT", "REFUND YOUR MONEY")):
        y = 215 + i * 112
        d.rounded_rectangle([S(40), S(y - 44), S(w - 40), S(y + 44)], radius=S(26), fill=(234, 240, 250, 255), outline=(20, 40, 90, 255), width=S(4))
        d.text((S(80), S(y + 2)), word, font=F(S(52), "Black"), fill=INK, anchor="lm")
        cx = w - 110
        d.ellipse([S(cx - 34), S(y - 34), S(cx + 34), S(y + 34)], fill=(40, 190, 90, 255), outline=(0, 0, 0, 255), width=S(5))
        d.line([(S(cx - 16), S(y + 2)), (S(cx - 4), S(y + 16)), (S(cx + 18), S(y - 14))], fill=(255, 255, 255, 255), width=S(9))
    # righe delle condizioni coperte da barre nere
    for k, ln in enumerate((690, 780, 620, 740)):
        y = 400 + k * 52
        d.rounded_rectangle([S(46), S(y - 20), S(46 + ln), S(y + 20)], radius=S(8), fill=(14, 14, 18, 255))
    return lay.resize((w, h), Image.LANCZOS)


def ring(w, h, wd=14):
    s = SS
    lay = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse([wd * s, wd * s, (w - wd) * s, (h - wd) * s], outline=(0, 0, 0, 255), width=(wd + 10) * s)
    d.ellipse([wd * s, wd * s, (w - wd) * s, (h - wd) * s], outline=ARED + (255,), width=wd * s)
    return lay.resize((w, h), Image.LANCZOS)


def tag(text, w, h, size, fill, ink, ang=0):
    s = SS
    lay = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, (h - 6) * s], radius=18 * s, fill=fill + (255,), outline=(0, 0, 0, 255), width=7 * s)
    d.text((w * s / 2, h * s / 2 + 3 * s), text, font=F(size * s, "Black"), fill=ink, anchor="mm")
    lay = lay.resize((w, h), Image.LANCZOS)
    return rot(lay, ang) if ang else lay


def cover():
    im = vgrad_np((2, 22, 78), (14, 96, 205))
    im = glow(im, 540, 1000, 760, (34, 120, 230), 150)
    im = stripes(im)
    im = vignette(im, 105)
    # logo Aldi vero, lucido, inclinato
    lg = rot(sheen(aldi_logo(330), 85), 4)
    im = sp(im, lg, (int(W / 2 - lg.width / 2), 50), off=(14, 22), blur=22, alpha=190)
    # titolo gigante (detto nello short)
    im = text3d(im, (540, 545), "TOO GOOD", 150, AYEL, (176, 112, 0), stroke=16, dep=13)
    im = text3d(im, (540, 725), "TO BE TRUE?", 116, (255, 255, 255), (150, 160, 190), stroke=15, dep=12)
    # scheda con le due promesse e le condizioni coperte
    pc = rot(promise_card(900, 640), -3)
    px, py = int(W / 2 - pc.width / 2), 850
    im = sp(im, pc, (px, py), off=(16, 24), blur=24, alpha=180)
    # cerchio rosso sulle barre nere + freccia rossa + targhetta
    cx, cy = 590, 1330
    rg = ring(700, 150, 13)
    im = sp(im, rg, (cx - 350, cy - 75 - 4), off=(0, 0), blur=1, alpha=0)
    ar = T.fat_arrow(190, 130, ARED, 0)
    im = sp(im, ar, (14, cy - 66), off=(8, 10), blur=10, alpha=160)
    tg = tag("FINE PRINT?", 420, 96, 54, AYEL, INK, 4)
    im = sp(im, tg, (590, 1425), off=(6, 10), blur=10, alpha=170)
    # striscia bianca + targhetta rossa
    wb = T.white_band("10 THINGS FROM ALDI'S OFFICIAL PAGES", 1010, 120, 40, tag="FULL VIDEO BELOW", tag_size=36)
    im = sp(im, wb, (35, 1640), off=(0, 10), blur=12, alpha=170)
    return im


if __name__ == "__main__":
    im = cover()
    im.save(f"{OUT}/copertina-short-13.png"); print("ok", im.size)
