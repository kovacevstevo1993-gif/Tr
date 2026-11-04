#!/usr/bin/env python3
"""Soldi che Contano versione 2 (realistica): compone profilo 1080x1080 e copertina Facebook 1640x624 da code/brand_fb2_3d.html resa in <cartella>/b21 (profilo) e b22 (copertina). Uso: brand_fb2_compose.py cartella"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
D = sys.argv[1]; OUT = os.path.join(ROOT, "brand/soldi_che_contano"); os.makedirs(OUT, exist_ok=True)
p = Image.open(os.path.join(D, "b21/t1.0.png")).convert("RGB"); p.save(os.path.join(OUT, "profilo-v2-soldi-che-contano.png"))
m = Image.new("L", p.size, 0); ImageDraw.Draw(m).ellipse((0, 0) + p.size, fill=255); c = Image.new("RGB", p.size, (30, 30, 30)); c.paste(p, (0, 0), m); c.resize((540, 540)).save(os.path.join(D, "profilo2-circolare.png"))
im = Image.open(os.path.join(D, "b22/t1.0.png")).convert("RGB"); W, H = im.size
# velo scuro al centro per leggere il testo sopra lo skyline
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for i in range(60):
    a = int(150 * (1 - i / 60) ** 1.4); d.ellipse((W // 2 - 520 - i * 4, 40 - i, W // 2 + 520 + i * 4, 600 + i), outline=(3, 5, 12, 0))
glow = Image.new("L", (W, H), 0); ImageDraw.Draw(glow).ellipse((W // 2 - 480, 60, W // 2 + 480, 560), fill=165); glow = glow.filter(ImageFilter.GaussianBlur(90))
im = Image.composite(Image.new("RGB", (W, H), (3, 5, 12)), im, glow)
def sz(text, size): f = ImageFont.truetype(F, size); bb = ImageDraw.Draw(im).textbbox((0, 0), text, font=f); return f, bb
def gold_text(text, size, cx, y):
    f, bb = sz(text, size); w = bb[2] - bb[0]; x = cx - w // 2 - bb[0]
    mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).text((x, y), text, font=f, fill=255)
    grad = Image.new("RGB", (W, H)); gd = ImageDraw.Draw(grad)
    top = y + bb[1]; bot = y + bb[3]
    for yy in range(top - 4, bot + 6):
        t = min(1, max(0, (yy - top) / max(1, bot - top))); col = (int(255 - 40 * t), int(226 - 70 * t), int(140 - 90 * t)) if t < .5 else (int(235 - 30 * (t - .5) * 2), int(190 - 50 * (t - .5) * 2), int(70 - 30 * (t - .5) * 2)); gd.line([(0, yy), (W, yy)], fill=col)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 3, y + 8), text, font=f, fill=(0, 0, 0, 200)); sh = sh.filter(ImageFilter.GaussianBlur(7)); im.paste(sh, (0, 0), sh)
    im.paste(grad, (0, 0), mask); return (x + bb[0], y + bb[1], x + bb[2], y + bb[3])
def white_text(text, size, cx, y, fill=(255, 255, 255), track=0):
    f, bb = sz(text, size); w = bb[2] - bb[0] + track * (len(text) - 1); x = cx - w // 2 - bb[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh); dr = ImageDraw.Draw(im); xx = x
    for ch in text:
        sd.text((xx + 3, y + 6), ch, font=f, fill=(0, 0, 0, 190)); xx += dr.textlength(ch, font=f) + track
    sh = sh.filter(ImageFilter.GaussianBlur(5)); im.paste(sh, (0, 0), sh); xx = x
    for ch in text: dr.text((xx, y), ch, font=f, fill=fill); xx += dr.textlength(ch, font=f) + track
    return (x + bb[0], y + bb[1], x + w, y + bb[3])
CX = W // 2
b1 = white_text("SOLDI CHE", 64, CX, 150, track=14)
b2 = gold_text("CONTANO", 132, CX, 238)
dd = ImageDraw.Draw(im); dd.line([(CX - 300, 418), (CX + 300, 418)], fill=(236, 190, 80), width=3); dd.polygon([(CX - 8, 418), (CX, 410), (CX + 8, 418), (CX, 426)], fill=(236, 190, 80))
b3 = white_text("SOLDI E FINANZA SPIEGATI CON I NUMERI UFFICIALI", 24, CX, 446, fill=(226, 232, 245), track=3)
im.save(os.path.join(OUT, "copertina-v2-soldi-che-contano.png"))
for n, b in (("SOLDI CHE", b1), ("CONTANO", b2), ("tagline", b3)): print(n, b, "ok" if b[0] >= 380 and b[2] <= 1260 else "FUORI ZONA CENTRALE")
