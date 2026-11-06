#!/usr/bin/env python3
"""Copertina Facebook short 009 v2 (pensione dal 2027): scena 3D code/s009v2_coverfb_3d.html resa con render_3d.js in <cartella>/t2.4.png + testi.
Uso: copertina_fb_short009v2.py cartella -> short009_v2/facebook/copertina-fb-short009v2.png (1080x1920; testi tra y 250 e 1670; fascia 16:9 y 656-1264 = numero 67 in oro)"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(sys.argv[1], "t2.4.png")).convert("RGB"); W, H = im.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(0, 700): d.line([(0, y), (W, y)], fill=(12, 36, 70, int(225 * max(0, 1 - y / 700) ** 0.9)))
for y in range(1250, H): d.line([(0, y), (W, y)], fill=(12, 36, 70, int(235 * min(1, (y - 1250) / 300) ** 1.0)))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
def txt(text, size, y, fill, stroke=12, scol=(12, 36, 70)):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), text, font=f, stroke_width=stroke); x = (W - (bb[2] - bb[0])) // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 5, y + 9), text, font=f, fill=(0, 0, 0, 140), stroke_width=stroke, stroke_fill=(0, 0, 0, 140))
    sh = sh.filter(ImageFilter.GaussianBlur(7)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=scol)
    return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
WHITE = (255, 255, 255); YEL = (255, 214, 0); RED = (255, 80, 60)
L = [("PENSIONE DAL 2027", 76, 260, WHITE), ("CAMBIA L'ETÀ?", 100, 370, YEL),
     ("NON È UNA PROPOSTA", 58, 1370, WHITE), ("È GIÀ LEGGE", 104, 1450, RED), ("DATI UFFICIALI INPS", 44, 1600, WHITE)]
bs = [txt(*a) for a in L]
out = os.path.join(ROOT, "short009_v2/facebook/copertina-fb-short009v2.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out)
for a, b in zip(L, bs): print(a[0], b, "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 250 and b[3] <= 1670 else "FUORI ZONA SICURA")
