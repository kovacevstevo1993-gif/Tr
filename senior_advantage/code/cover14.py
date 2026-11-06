"""Copertina SHORT 14 (BLACK FRIDAY), 1080x1920. Ordine utente 06/11: "La Copertina". Regola 32: professionale, curiosita (riga coperta da barre
nere, cerchio e freccia rossi), colori accesi (rosso, giallo, bianco, nero), loghi VERI Walmart / Target / Costco (riferimenti/walmart, riferimenti/logos_bf).
Diversa dalle due miniature del lungo (blu e nero-giallo). Tutto cio che c'e scritto e detto nello short: tre negozi, l'eccezione Black Friday
scritta sulla pagina di uno di loro (non dice quale), pagine ufficiali. Niente date, niente giorni, niente nome del negozio dell'eccezione.
uso: OUT=cartella python3 cover14.py"""
import os, math, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import cover13 as C      # imposta T.W, T.H = 1080, 1920 e porta ring/tag/vgrad_np
import thumb_long9 as T
import thumb_bf10 as B
W, H = 1080, 1920
OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
F, rot, sp, text3d, glow, vignette = T.F, T.rot, T.sp, T.text3d, T.glow, T.vignette
BLK = (10, 10, 14); YEL = (255, 214, 28); RED = (236, 28, 36)

def bokeh(im, seed=5, n=40):
    rnd = random.Random(seed)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for _ in range(n):
        r = rnd.choice((20, 30, 44, 62, 86)); x = rnd.randint(-20, W + 20); y = rnd.randint(-20, H + 20)
        col = rnd.choice(((255, 214, 80), (255, 255, 255), (255, 120, 90), (255, 170, 40))); a = rnd.randint(30, 80)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col + (a,))
        d.ellipse([x - r, y - r, x + r, y + r], outline=tuple(min(255, c + 30) for c in col) + (min(255, a + 40),), width=2)
    lay = lay.filter(ImageFilter.GaussianBlur(14))
    base = im.convert("RGBA"); base.alpha_composite(lay); return base.convert("RGB")

def policy_card(w=900, h=720):
    s = 2
    lay = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    S = lambda v: int(v * s)
    d.rounded_rectangle([S(4), S(4), S(w - 4), S(h - 4)], radius=S(36), fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=S(8))
    d.rounded_rectangle([S(4), S(4), S(w - 4), S(130)], radius=S(36), fill=BLK + (255,), outline=(0, 0, 0, 255), width=S(8))
    d.rectangle([S(10), S(90), S(w - 10), S(130)], fill=BLK + (255,))
    for i, col in enumerate(((236, 28, 36), (255, 190, 30), (80, 200, 110))):
        d.ellipse([S(34 + i * 44), S(46), S(62 + i * 44), S(74)], fill=col + (255,))
    d.text((S(w / 2 + 70), S(70)), "ITS OWN POLICY PAGE", font=F(S(48), "Black"), fill=YEL, anchor="mm")
    for k, ln in enumerate((760, 700, 780)):
        y = 190 + k * 56
        d.rounded_rectangle([S(46), S(y - 12), S(46 + ln), S(y + 12)], radius=S(8), fill=(208, 212, 220, 255))
    # righe dell'eccezione coperte da barre nere
    for k, ln in enumerate((800, 720, 790)):
        y = 400 + k * 64
        d.rounded_rectangle([S(46), S(y - 24), S(46 + ln), S(y + 24)], radius=S(10), fill=(12, 12, 16, 255))
    for k, ln in enumerate((740, 560)):
        y = 620 + k * 56
        d.rounded_rectangle([S(46), S(y - 12), S(46 + ln), S(y + 12)], radius=S(8), fill=(208, 212, 220, 255))
    return lay.resize((w, h), Image.LANCZOS)

def cover():
    im = C.vgrad_np((52, 0, 8), (214, 26, 34))
    im = bokeh(im)
    im = glow(im, 540, 900, 760, (255, 80, 60), 120)
    im = vignette(im, 110)
    # tre loghi veri su striscia bianca (in alto)
    im = B.logos_strip(im, 50, 60, 980, 170)
    # titolo gigante
    im = text3d(im, (540, 390), "BLACK FRIDAY", 118, YEL, (170, 90, 0), stroke=16, dep=13)
    im = text3d(im, (540, 570), "EXCEPTION?", 132, (255, 255, 255), (90, 90, 110), stroke=15, dep=12)
    # pagina con le righe coperte
    pc = rot(policy_card(900, 720), -3)
    px, py = int(W / 2 - pc.width / 2), 740
    im = sp(im, pc, (px, py), off=(16, 24), blur=24, alpha=190)
    # cerchio rosso sulle barre nere + freccia + targhetta
    rg = C.ring(900, 300, 13)
    im = sp(im, rg, (90, 1050), off=(0, 0), blur=1, alpha=0)
    ar = T.fat_arrow(190, 130, RED, 0)
    im = sp(im, ar, (10, 1290), off=(8, 10), blur=10, alpha=160)
    tg = C.tag("WHICH STORE?", 520, 100, 50, YEL, BLK, 4)
    im = sp(im, tg, (520, 1425), off=(6, 10), blur=10, alpha=170)
    # striscia bianca + targhetta rossa
    wb = T.white_band("WHAT EACH PAGE ITSELF SAYS", 1010, 120, 46, tag="FULL VIDEO BELOW", tag_size=36)
    im = sp(im, wb, (35, 1640), off=(0, 10), blur=12, alpha=170)
    return B.grain(im, 6)

if __name__ == "__main__":
    im = cover()
    im.save(f"{OUT}/copertina-short-14.png"); print("ok", im.size)
