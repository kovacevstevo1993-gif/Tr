#!/usr/bin/env python3
"""Banner YouTube 2560x1440 di Soldi che Contano: scena 3D (brand_yt_3d.html) + testo nell'AREA SICURA centrale (1546x423, x 507-2053, y 508-932). Uso: brand_yt_compose.py cartella_con_t1.0.png"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); F = os.path.join(ROOT, "brand/fonts/ArchivoBlack-Regular.ttf")
OUT = os.path.join(ROOT, "brand/soldi_che_contano"); os.makedirs(OUT, exist_ok=True)
im = Image.open(os.path.join(sys.argv[1], "t1.0.png")).convert("RGB"); W, H = im.size; CX, CY = W // 2, H // 2
glow = Image.new("L", (W, H), 0); ImageDraw.Draw(glow).ellipse((CX - 800, CY - 250, CX + 800, CY + 250), fill=175); glow = glow.filter(ImageFilter.GaussianBlur(110))
im = Image.composite(Image.new("RGB", (W, H), (3, 5, 12)), im, glow)
def bb(text, size): f = ImageFont.truetype(F, size); return f, ImageDraw.Draw(im).textbbox((0, 0), text, font=f)
def gold(text, size, y):
    f, b = bb(text, size); w = b[2] - b[0]; x = CX - w // 2 - b[0]
    mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).text((x, y), text, font=f, fill=255)
    grad = Image.new("RGB", (W, H)); gd = ImageDraw.Draw(grad); top = y + b[1]; bot = y + b[3]
    for yy in range(top - 4, bot + 6):
        t = min(1, max(0, (yy - top) / max(1, bot - top))); col = (int(255 - 40 * t), int(226 - 70 * t), int(140 - 90 * t)) if t < .5 else (int(235 - 30 * (t - .5) * 2), int(190 - 50 * (t - .5) * 2), int(70 - 30 * (t - .5) * 2)); gd.line([(0, yy), (W, yy)], fill=col)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 4, y + 10), text, font=f, fill=(0, 0, 0, 210)); sh = sh.filter(ImageFilter.GaussianBlur(9)); im.paste(sh, (0, 0), sh)
    im.paste(grad, (0, 0), mask); return (x + b[0], y + b[1], x + b[2], y + b[3])
def white(text, size, y, fill=(255, 255, 255), track=0):
    f, b = bb(text, size); dr = ImageDraw.Draw(im); w = b[2] - b[0] + track * (len(text) - 1); x = CX - w // 2 - b[0]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh); xx = x
    for ch in text: sd.text((xx + 4, y + 8), ch, font=f, fill=(0, 0, 0, 200)); xx += dr.textlength(ch, font=f) + track
    sh = sh.filter(ImageFilter.GaussianBlur(6)); im.paste(sh, (0, 0), sh); xx = x
    for ch in text: dr.text((xx, y), ch, font=f, fill=fill); xx += dr.textlength(ch, font=f) + track
    return (x + b[0], y + b[1], x + w, y + b[3])
b1 = white("SOLDI CHE", 92, 520, track=20)
b2 = gold("CONTANO", 190, 622)
dd = ImageDraw.Draw(im); dd.line([(CX - 420, 862), (CX + 420, 862)], fill=(236, 190, 80), width=4); dd.polygon([(CX - 11, 862), (CX, 851), (CX + 11, 862), (CX, 873)], fill=(236, 190, 80))
b3 = white("SOLDI E FINANZA SPIEGATI CON I NUMERI UFFICIALI", 33, 884, fill=(226, 232, 245), track=4)
out = os.path.join(OUT, "banner-youtube-soldi-che-contano.png"); im.save(out, optimize=True)
for n, b in (("SOLDI CHE", b1), ("CONTANO", b2), ("tagline", b3)): print(n, b, "ok" if b[0] >= 507 and b[2] <= 2053 and b[1] >= 508 and b[3] <= 932 else "FUORI AREA SICURA")
print(out, os.path.getsize(out) // 1024, "KB", im.size)
