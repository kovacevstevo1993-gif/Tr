#!/usr/bin/env python3
"""Copertina YouTube short 007 (mutuo), 1080x1920, da brand/sfondo Blender short007_mutuo/facebook/sfondo-blender-short007.png.
Zona sicura: tutto il testo dentro il ritaglio 4:5 (y 285-1635) e x 60-1020; il 759 e la barra del totale dentro la fascia 16:9 centrale (y 656-1264)."""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(ROOT, "short007_mutuo/facebook/sfondo-blender-short007.png")).convert("RGB"); W, H = im.size
im = ImageEnhance.Contrast(im).enhance(1.22); im = ImageEnhance.Color(im).enhance(1.5); im = ImageEnhance.Brightness(im).enhance(.96)
def grad(c0, c1, y0, y1, a0, a1):
    o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    for y in range(max(0, y0), min(H, y1)):
        t = (y - y0) / max(1, y1 - y0); a = int(a0 + (a1 - a0) * t); c = tuple(int(c0[i] + (c1[i] - c0[i]) * t) for i in range(3)); d.line([(0, y), (W, y)], fill=c + (a,))
    return o
im = Image.alpha_composite(im.convert("RGBA"), grad((8, 36, 110), (30, 90, 190), 0, 760, 235, 0))
im = Image.alpha_composite(im, grad((20, 70, 170), (6, 20, 60), 1100, H, 0, 255))
glow = Image.new("L", (W, H), 0); ImageDraw.Draw(glow).ellipse((60, 620, 1020, 1160), fill=120); glow = glow.filter(ImageFilter.GaussianBlur(120))
warm = Image.new("RGB", (W, H), (255, 214, 120)); base = im.convert("RGB"); im = ImageChops.screen(base, Image.composite(warm, Image.new("RGB", (W, H), (0, 0, 0)), glow).point(lambda v: int(v * .55)))
vig = Image.new("L", (W, H), 0); ImageDraw.Draw(vig).ellipse((-380, -260, W + 380, H + 260), fill=255); vig = vig.filter(ImageFilter.GaussianBlur(220))
im = Image.composite(im, Image.new("RGB", (W, H), (3, 8, 24)), vig.point(lambda v: int(120 + v * .53)))
F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf"); NAVY = (14, 30, 72); YEL = (255, 214, 0); WHITE = (255, 255, 255); RED = (230, 36, 28)
def txt(t, size, y, fill, outline=NAVY, ow=12, x=None):
    f = ImageFont.truetype(F, size); dr = ImageDraw.Draw(im); bb = dr.textbbox((0, 0), t, font=f, stroke_width=ow); xx = (W - (bb[2] - bb[0])) // 2 - bb[0] if x is None else x
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((xx + 5, y + 10), t, font=f, fill=(0, 0, 0, 170), stroke_width=ow, stroke_fill=(0, 0, 0, 170)); sh = sh.filter(ImageFilter.GaussianBlur(8)); im.paste(sh, (0, 0), sh)
    dr.text((xx, y), t, font=f, fill=fill, stroke_width=ow, stroke_fill=outline); return (xx + bb[0], y + bb[1], xx + bb[2], y + bb[3])
B = []
B.append(txt("QUANTO RESTITUISCI", 68, 300, WHITE))
B.append(txt("DAVVERO?", 150, 400, YEL, ow=16))
B.append(txt("MUTUO DA 150.000 € IN 25 ANNI", 46, 590, WHITE, ow=9))
# pannello totale coperto da barra nera + cerchio e freccia rossi (curiosita)
d = ImageDraw.Draw(im, "RGBA"); px0, py0, px1, py1 = 70, 1178, 1010, 1260
d.rounded_rectangle((px0 + 6, py0 + 10, px1 + 6, py1 + 10), 26, fill=(0, 0, 0, 120)); d.rounded_rectangle((px0, py0, px1, py1), 26, fill=(255, 255, 255, 255), outline=NAVY, width=6)
f = ImageFont.truetype(F, 38); d.text((100, 1198), "TOTALE RESTITUITO:", font=f, fill=NAVY)
d.rounded_rectangle((640, 1192, 980, 1246), 12, fill=(8, 8, 12, 255)); fq = ImageFont.truetype(F, 40); d.text((660, 1196), "?????? €", font=fq, fill=(70, 70, 80))
d.ellipse((616, 1168, 1004, 1272), outline=RED, width=10)
d.polygon([(900, 1420), (960, 1340), (930, 1340), (930, 1290), (870, 1290), (870, 1340), (840, 1340)], fill=RED, outline=WHITE)
B.append((px0, py0, px1, py1)); B.append((616, 1168, 1004, 1420))
B.append(txt("DATI BCE · SETTEMBRE 2026", 50, 1500, WHITE, ow=9))
B.append(txt("SOLDI CHE CONTANO", 44, 1575, YEL, ow=8))
out = os.path.join(ROOT, "short007_mutuo/youtube/copertina-youtube-short007.png"); im.convert("RGB").save(out, optimize=True)
names = ["QUANTO RESTITUISCI", "DAVVERO?", "MUTUO DA...", "pannello", "freccia", "DATI BCE", "SOLDI CHE CONTANO"]
for n, b in zip(names, B): print(f"{n:20s} {b}", "ok" if b[0] >= 60 and b[2] <= 1020 and b[1] >= 285 and b[3] <= 1635 else "FUORI ZONA 4:5")
print(out, os.path.getsize(out) // 1024, "KB", im.size)
