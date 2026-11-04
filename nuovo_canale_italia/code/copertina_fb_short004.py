#!/usr/bin/env python3
"""Copertina Facebook short 004 (manovra 2027, bollo auto): scena 3D code/s003_cover_3d.html resa con render_3d.js in <cartella>/t1.0.png + testi.
Uso: copertina_fb_short003.py cartella_con_t1.0.png -> short004_benzina/facebook/copertina-fb-short004.png (1080x1920; testi tra y 250 e 1670; fascia 16:9 centrale y 656-1264 = auto + bolletta barrata)"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(sys.argv[1], "t1.0.png")).convert("RGB"); W, H = im.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(0, 700): d.line([(0, y), (W, y)], fill=(12, 12, 40, int(215 * max(0, 1 - y / 700) ** 1.1)))
for y in range(1300, H): d.line([(0, y), (W, y)], fill=(12, 12, 40, int(225 * min(1, (y - 1300) / 300) ** 1.1)))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
def txt(text, size, y, fill, stroke=12, scol=(20, 20, 60)):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), text, font=f, stroke_width=stroke); x = (W - (bb[2] - bb[0])) // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 5, y + 9), text, font=f, fill=(0, 0, 0, 150), stroke_width=stroke, stroke_fill=(0, 0, 0, 150))
    sh = sh.filter(ImageFilter.GaussianBlur(7)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=scol)
    return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
WHITE = (255, 255, 255); AMBER = (255, 190, 30)
L = [("BENZINA", 130, 262, WHITE), ("IN AUTOSTRADA", 74, 420, AMBER), ("+1,30 € A PIENO", 96, 1420, AMBER), ("CIRCA 68 € L'ANNO", 66, 1580, WHITE)]
bs = [txt(*a) for a in L]
out = os.path.join(ROOT, "short004_benzina/facebook/copertina-fb-short004.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out)
for a, b in zip(L, bs): print(a[0], b, "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 250 and b[3] <= 1670 else "FUORI ZONA SICURA")
