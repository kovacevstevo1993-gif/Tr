#!/usr/bin/env python3
"""Copertina Facebook short 008 (cedolare secca affitti): scena 3D code/s008_cover_3d.html resa con render_3d.js in <cartella>/t1.0.png + testi.
Uso: copertina_fb_short008.py cartella_con_t1.0.png -> short008_cedolare/facebook/copertina-fb-short008.png (1080x1920; testi tra y 250 e 1670; fascia 16:9 centrale y 656-1264 = medaglioni 10% barrato / 5% + chiavi)"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(sys.argv[1], "t1.0.png")).convert("RGB"); W, H = im.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(0, 640): d.line([(0, y), (W, y)], fill=(6, 26, 36, int(215 * max(0, 1 - y / 640) ** 0.8)))
for y in range(1400, H): d.line([(0, y), (W, y)], fill=(255, 250, 235, int(235 * min(1, (y - 1400) / 200) ** 1.1)))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
def txt(text, size, y, fill, stroke=12, scol=(8, 36, 44)):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), text, font=f, stroke_width=stroke); x = (W - (bb[2] - bb[0])) // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 5, y + 9), text, font=f, fill=(0, 0, 0, 130), stroke_width=stroke, stroke_fill=(0, 0, 0, 130))
    sh = sh.filter(ImageFilter.GaussianBlur(7)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=scol)
    return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
WHITE = (255, 255, 255); YEL = (255, 214, 0); NAVY = (8, 36, 44); RED = (214, 40, 30)
L = [("CEDOLARE SECCA", 72, 255, WHITE, 12, NAVY), ("TASSA DIMEZZATA?", 70, 340, YEL, 12, NAVY),
     ("SOLO CANONE CONCORDATO", 54, 1450, RED, 0, NAVY), ("BOZZA MANOVRA 2027: NON ANCORA LEGGE", 32, 1560, NAVY, 0, NAVY)]
bs = [txt(*a) for a in L]
out = os.path.join(ROOT, "short008_cedolare/facebook/copertina-fb-short008.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out)
for a, b in zip(L, bs): print(a[0], b, "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 250 and b[3] <= 1670 else "FUORI ZONA SICURA")
