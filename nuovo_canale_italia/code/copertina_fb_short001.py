#!/usr/bin/env python3
"""Copertina Facebook short 001: sovrappone i testi alla scena 3D (code/s001_cover_3d.html resa con render_3d.js in <scratch>/cov/t1.0.png).
Uso: copertina_fb_short001.py cartella_con_t1.0.png  -> short001_inflazione/facebook/copertina-fb-short001.png (1080x1920, zona sicura: testi tra y 250 e 1670, fascia 16:9 centrale y 656-1264 con pannelli e torri)"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(sys.argv[1], "t1.0.png")).convert("RGB"); W, H = im.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(0, 700): d.line([(0, y), (W, y)], fill=(5, 5, 8, int(215 * max(0, 1 - y / 700) ** 1.3)))
for y in range(1230, H): d.line([(0, y), (W, y)], fill=(5, 5, 8, int(235 * min(1, (y - 1230) / 330) ** 1.2)))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
def txt(text, size, y, fill, stroke=12):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), text, font=f, stroke_width=stroke); x = (W - (bb[2] - bb[0])) // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 6, y + 10), text, font=f, fill=(0, 0, 0, 200), stroke_width=stroke, stroke_fill=(0, 0, 0, 200))
    sh = sh.filter(ImageFilter.GaussianBlur(7)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=(8, 8, 10))
    return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
bs = [txt("INFLAZIONE", 130, 268, (255, 255, 255)), txt("5,4%", 232, 372, (255, 225, 74)), txt("UN TERZO", 150, 1322, (255, 225, 74)), txt("IN PIÙ?", 150, 1478, (255, 255, 255))]
out = os.path.join(ROOT, "short001_inflazione/facebook/copertina-fb-short001.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out)
for n, b in zip(["INFLAZIONE", "5,4%", "UN TERZO", "IN PIÙ?"], bs): print(n, b, "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 250 and b[3] <= 1670 else "FUORI ZONA SICURA")
