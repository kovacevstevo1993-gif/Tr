"""Copertina SHORT 12 (WALMART), 1080x1920. Ordine utente 24/10: "mignatura attira click". Regola 32: professionale, curiosita (righe coperte da barre nere,
cerchio e freccia rossi), colori accesi (blu Walmart, giallo, rosso, bianco), logo Walmart vero (riferimenti/walmart/, da corporate.walmart.com).
Layout verticale NUOVO rispetto alle miniature lunghe: logo in alto, titolo grande NO SENIOR / DISCOUNT?, scontrino alto e inclinato con 10 righe:
SENIOR DISCOUNT $0.00 barrato; evidenziate solo 4 righe con le parole che dice la voce (AT THE REGISTER, THIS SEASON, YOUR MEDICINE, THE HEADLINE PRICE),
le altre 6 coperte da barre nere; cerchio rosso su una barra + freccia rossa; fascia rossa "10 THINGS IF YOU ASK". Nessun nome di programma, nessuna cifra di prezzo.
uso: OUT=cartella python3 cover12.py"""
import os, math, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
import thumb_long8 as T8
from thumb_long8 import F, text_stroke, shadow_paste, rot, arrow, logo_pill, pill_band, WBLUE, WNAVY, WYEL, PAPER, INK, RED2, BLK

W, H = 1080, 1920
SS = 2
OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)


def radial(c_in, c_out, cx, cy, r):
    im = Image.new("RGB", (W, H), c_out)
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(r * 0.45))
    return Image.composite(Image.new("RGB", (W, H), c_in), im, m)


def light_rays(im, cx, cy, col, n=18, alpha=34):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i in range(n):
        a0 = 2 * math.pi * i / n; a1 = a0 + math.pi / n * 0.8
        d.polygon([(cx, cy), (cx + 3000 * math.cos(a0), cy + 3000 * math.sin(a0)), (cx + 3000 * math.cos(a1), cy + 3000 * math.sin(a1))], fill=col + (alpha,))
    lay = lay.filter(ImageFilter.GaussianBlur(6))
    base = im.convert("RGBA"); base.alpha_composite(lay); return base.convert("RGB")


def vignette(im, strength=120):
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([-300, -240, W + 300, H + 240], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(200))
    return Image.composite(im, Image.blend(im, Image.new("RGB", (W, H), (0, 0, 0)), strength / 255), m)


def receipt(w=820, h=1010):
    s = SS
    lay = Image.new("RGBA", (w * s, (h + 40) * s), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    def S(v): return int(v * s)
    d.rectangle([S(0), S(30), S(w), S(h + 10)], fill=PAPER)
    for k in range(0, w, 30):
        d.polygon([(S(k), S(32)), (S(k + 15), S(8)), (S(k + 30), S(32))], fill=PAPER)
        d.polygon([(S(k), S(h + 8)), (S(k + 15), S(h + 34)), (S(k + 30), S(h + 8))], fill=PAPER)
    d.text((S(w / 2), S(96)), "RECEIPT", font=F(S(62), "Black"), fill=INK, anchor="mm")
    for k in range(40, w - 40, 22):
        d.line([(S(k), S(150)), (S(k + 11), S(150))], fill=(150, 150, 150), width=S(4))
    d.text((S(40), S(206)), "SENIOR DISCOUNT", font=F(S(40), "Black"), fill=INK, anchor="lm")
    d.text((S(w - 40), S(206)), "$0.00", font=F(S(40), "Black"), fill=RED2, anchor="rm")
    d.line([(S(30), S(210)), (S(w - 30), S(200))], fill=RED2, width=S(9))
    vis = {1: "AT THE REGISTER", 2: "THIS SEASON", 9: "YOUR MEDICINE", 10: "THE HEADLINE PRICE"}
    lens = {3: 520, 4: 610, 5: 470, 6: 560, 7: 600, 8: 500}
    for i in range(1, 11):
        y = 288 + (i - 1) * 72
        d.text((S(40), S(y)), f"{i}.", font=F(S(42), "Black"), fill=INK, anchor="lm")
        if i in vis:
            d.rounded_rectangle([S(112), S(y - 30), S(w - 34), S(y + 30)], radius=S(10), fill=(255, 226, 80))
            d.text((S(128), S(y + 1)), vis[i], font=F(S(40), "Black"), fill=INK, anchor="lm")
        else:
            d.rounded_rectangle([S(114), S(y - 25), S(114 + lens[i]), S(y + 25)], radius=S(8), fill=(18, 18, 22))
    out = lay.resize((w, h + 40), Image.LANCZOS)
    return out


def red_circle(w, h, wd=12):
    s = SS
    lay = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse([wd * s, wd * s, (w - wd) * s, (h - wd) * s], outline=RED2, width=wd * s)
    return lay.resize((w, h), Image.LANCZOS)


def cover():
    im = radial((30, 120, 255), WNAVY, 540, 760, 900)
    im = light_rays(im, 540, 760, (255, 255, 255), 20, 30)
    im = vignette(im, 120)
    # logo Walmart vero
    im = shadow_paste(im, logo_pill(150), (int(W / 2 - logo_pill(150).width / 2), 130), off=(6, 12), blur=12)
    # titolo
    im = text_stroke(im, (540, 400), "NO SENIOR", 158, (255, 255, 255), stroke=16, anchor="mm")
    im = text_stroke(im, (540, 575), "DISCOUNT?", 166, WYEL, stroke=17, anchor="mm")
    # scontrino con righe coperte
    rc = rot(receipt(820, 1010), -4)
    im = shadow_paste(im, rc, (int(W / 2 - rc.width / 2 + 30), 700), off=(18, 26), blur=24, alpha=180)
    # cerchio rosso su una barra nera + freccia
    cx, cy = 560, 1240
    im = shadow_paste(im, red_circle(660, 124), (cx - 330 + 30, cy - 62 - 4), off=(0, 0), blur=1, alpha=0)
    im = shadow_paste(im, arrow(200, 150, RED2, 0), (24, cy - 55), off=(8, 10), blur=10)
    # fascia rossa
    im = shadow_paste(im, pill_band("10 THINGS IF YOU ASK", 940, 150, RED2, (255, 255, 255), 74, -2), (70, 1730), off=(8, 12), blur=12)
    return im


if __name__ == "__main__":
    im = cover()
    im.save(f"{OUT}/copertina-short-12.png"); print("ok", im.size)
