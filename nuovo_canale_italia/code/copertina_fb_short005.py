#!/usr/bin/env python3
"""Copertina Facebook short 005 (manovra 2027, bollo auto): scena 3D code/s003_cover_3d.html resa con render_3d.js in <cartella>/t1.0.png + testi.
Uso: copertina_fb_short003.py cartella_con_t1.0.png -> short005_pacchi/facebook/copertina-fb-short005.png (1080x1920; testi tra y 250 e 1670; fascia 16:9 centrale y 656-1264 = auto + bolletta barrata)"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(sys.argv[1], "t1.0.png")).convert("RGB"); W, H = im.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(0, 660): d.line([(0, y), (W, y)], fill=(255, 255, 255, int(205 * max(0, 1 - y / 660) ** 1.2)))
for y in range(1330, H): d.line([(0, y), (W, y)], fill=(255, 255, 255, int(225 * min(1, (y - 1330) / 260) ** 1.1)))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
def txt(text, size, y, fill, stroke=14, scol=(255, 255, 255)):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), text, font=f, stroke_width=stroke); x = (W - (bb[2] - bb[0])) // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 5, y + 9), text, font=f, fill=(23, 50, 77, 110), stroke_width=stroke, stroke_fill=(23, 50, 77, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(7)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=scol)
    return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
NAVY = (20, 33, 61); RED = (214, 40, 30)
L = [("ORDINI ONLINE?", 96, 270, NAVY), ("DA NOVEMBRE COSTA DI PIÙ", 56, 420, RED), ("FINO A +6,10 €", 112, 1425, RED), ("PER OGNI TIPO DI PRODOTTO", 52, 1585, NAVY)]
bs = [txt(*a) for a in L]
out = os.path.join(ROOT, "short005_pacchi/facebook/copertina-fb-short005.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out)
for a, b in zip(L, bs): print(a[0], b, "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 250 and b[3] <= 1670 else "FUORI ZONA SICURA")
