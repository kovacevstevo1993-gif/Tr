#!/usr/bin/env python3
"""Copertina YouTube short 009 v2 (pensione dal 2027), 1080x1920: scena 3D code/s009v2_coverfb_3d.html (render_3d.js -> <cartella>/t2.4.png) + testi.
Curiosita: pannello con la cifra coperta da barra nera + cerchio e freccia rossi (stesso schema della copertina YouTube del mutuo, colori della spiaggia).
Zona sicura: testi x 60-1020, y 285-1635; il 67 e il pannello nella fascia 16:9 centrale (y 656-1264).
Uso: copertina_yt_short009v2.py cartella -> short009_v2/youtube/copertina-youtube-short009v2.png"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(sys.argv[1], "t2.4.png")).convert("RGB"); W, H = im.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(0, 760): d.line([(0, y), (W, y)], fill=(8, 28, 70, int(240 * max(0, 1 - y / 760) ** 0.8)))
for y in range(1230, H): d.line([(0, y), (W, y)], fill=(8, 28, 70, int(245 * min(1, (y - 1230) / 260))))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf"); NAVY = (12, 30, 72); YEL = (255, 214, 0); WHITE = (255, 255, 255); RED = (230, 36, 28)
def txt(t, size, y, fill, ow=12, outline=NAVY):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), t, font=f, stroke_width=ow); x = (W - (bb[2] - bb[0])) // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 5, y + 10), t, font=f, fill=(0, 0, 0, 170), stroke_width=ow, stroke_fill=(0, 0, 0, 170)); sh = sh.filter(ImageFilter.GaussianBlur(8)); im.paste(sh, (0, 0), sh)
    dr.text((x, y), t, font=f, fill=fill, stroke_width=ow, stroke_fill=outline); return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
B = []; N = []
def add(n, b): N.append(n); B.append(b)
add("ULTIMO ANNO", txt("L'ULTIMO ANNO", 74, 300, WHITE))
add("A 67 ANNI", txt("A 67 ANNI?", 138, 395, YEL, ow=16))
# pannello con la cifra coperta (curiosita)
d = ImageDraw.Draw(im, "RGBA"); px0, py0, px1, py1 = 70, 1190, 1010, 1272
d.rounded_rectangle((px0 + 6, py0 + 10, px1 + 6, py1 + 10), 26, fill=(0, 0, 0, 130)); d.rounded_rectangle((px0, py0, px1, py1), 26, fill=(255, 255, 255, 255), outline=NAVY, width=6)
f = ImageFont.truetype(F, 40); d.text((100, 1209), "NEL 2027 SERVONO:", font=f, fill=NAVY)
d.rounded_rectangle((640, 1204, 982, 1258), 12, fill=(8, 8, 12, 255)); fq = ImageFont.truetype(F, 38); d.text((662, 1210), "?? ANNI E ?", font=fq, fill=(70, 70, 80))
d.ellipse((616, 1180, 1004, 1284), outline=RED, width=10)
d.polygon([(900, 1430), (960, 1350), (930, 1350), (930, 1302), (870, 1302), (870, 1350), (840, 1350)], fill=RED, outline=WHITE)
add("pannello", (px0, py0, px1, py1)); add("freccia", (616, 1180, 1004, 1430))
add("E GIA LEGGE", txt("È GIÀ LEGGE", 96, 1470, WHITE, ow=12))
add("DATI INPS", txt("DATI UFFICIALI INPS", 46, 1570, YEL, ow=9))
out = os.path.join(ROOT, "short009_v2/youtube/copertina-youtube-short009v2.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out, optimize=True)
for n, b in zip(N, B): print(f"{n:14s} {b}", "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 285 and b[3] <= 1635 else "FUORI ZONA")
print(out, os.path.getsize(out) // 1024, "KB", im.size)
