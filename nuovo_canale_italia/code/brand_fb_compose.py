#!/usr/bin/env python3
"""Soldi che Contano: compone profilo (1080x1080) e copertina Facebook (1640x624) da code/brand_fb_3d.html resa in <cartella>/br1 (profilo) e br2 (copertina). Uso: brand_fb_compose.py cartella"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
D = sys.argv[1]; OUT = os.path.join(ROOT, "brand/soldi_che_contano"); os.makedirs(OUT, exist_ok=True)
GOLD = (243, 190, 58); WHITE = (255, 255, 255); GREEN = (25, 211, 122)
# profilo
p = Image.open(os.path.join(D, "br1/t1.0.png")).convert("RGB"); p.save(os.path.join(OUT, "profilo-soldi-che-contano.png"))
# anteprima circolare (come la mostra Facebook)
m = Image.new("L", p.size, 0); ImageDraw.Draw(m).ellipse((0, 0) + p.size, fill=255); c = Image.new("RGB", p.size, (30, 30, 30)); c.paste(p, (0, 0), m); c.resize((540, 540)).save(os.path.join(D, "profilo-circolare.png"))
# copertina
im = Image.open(os.path.join(D, "br2/t1.0.png")).convert("RGB"); W, H = im.size
def txt(text, size, cx, y, fill, stroke=0, scol=(0, 0, 0), shadow=True):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), text, font=f, stroke_width=stroke); w = bb[2] - bb[0]; x = cx - w // 2 - bb[0]
    if shadow:
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 4, y + 8), text, font=f, fill=(0, 0, 0, 170), stroke_width=stroke, stroke_fill=(0, 0, 0, 170)); sh = sh.filter(ImageFilter.GaussianBlur(6)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=scol); return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
CX = W // 2
b1 = txt("SOLDI CHE", 112, CX, 150, WHITE)
b2 = txt("CONTANO", 112, CX, 262, GOLD)
d = ImageDraw.Draw(im); d.rounded_rectangle((CX - 250, 418, CX + 250, 424), 3, fill=GREEN)
b3 = txt("Soldi e finanza spiegati con i numeri ufficiali", 29, CX, 450, (214, 240, 226), shadow=True)
im.save(os.path.join(OUT, "copertina-soldi-che-contano.png"))
for n, b in (("SOLDI CHE", b1), ("CONTANO", b2), ("tagline", b3)): print(n, b, "ok" if b[0] >= 400 and b[2] <= 1240 else "FUORI ZONA CENTRALE")
