#!/usr/bin/env python3
"""Copertina Facebook short 002 (BCE/Lagarde): scena 3D code/s002_cover_3d.html resa con render_3d.js in <cartella>/t1.0.png + testi.
Uso: copertina_fb_short002.py cartella_con_t1.0.png -> short002_bce/facebook/copertina-fb-short002.png (1080x1920; testi tra y 250 e 1670; fascia 16:9 centrale y 656-1264 = poltrona)"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(sys.argv[1], "t1.0.png")).convert("RGB"); W, H = im.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(0, 640): d.line([(0, y), (W, y)], fill=(5, 5, 8, int(225 * max(0, 1 - y / 640) ** 1.2)))
for y in range(1260, H): d.line([(0, y), (W, y)], fill=(5, 5, 8, int(240 * min(1, (y - 1260) / 300) ** 1.1)))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
def txt(text, size, y, fill, stroke=12):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), text, font=f, stroke_width=stroke); x = (W - (bb[2] - bb[0])) // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 6, y + 10), text, font=f, fill=(0, 0, 0, 200), stroke_width=stroke, stroke_fill=(0, 0, 0, 200))
    sh = sh.filter(ImageFilter.GaussianBlur(7)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=(8, 8, 10))
    return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
L = [("LAGARDE", 150, 262, (255, 255, 255)), ("LASCIA LA BCE", 104, 428, (255, 225, 74)), ("7 FEBBRAIO", 124, 1340, (255, 225, 74)), ("CHI AL SUO POSTO?", 72, 1520, (255, 255, 255))]
bs = [txt(*a) for a in L]
out = os.path.join(ROOT, "short002_bce/facebook/copertina-fb-short002.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out)
for a, b in zip(L, bs): print(a[0], b, "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 250 and b[3] <= 1670 else "FUORI ZONA SICURA")
