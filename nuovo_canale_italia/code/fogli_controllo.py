#!/usr/bin/env python3
"""Controllo fotogrammi: mette TUTTI i fotogrammi (miniature in demo/frames/NNNN.jpg) in fogli da 48, numerati.
Uso: fogli_controllo.py cartella_frames cartella_uscita"""
import os, sys, glob
from PIL import Image, ImageDraw, ImageFont
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
fs = sorted(f for f in glob.glob(os.path.join(src, "[0-9][0-9][0-9][0-9].jpg")))
W, H, C, R = 192, 108, 10, 10; font = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 14)
for k in range(0, len(fs), C * R):
    sheet = Image.new("RGB", (W * C, H * R), (255, 255, 255)); d = ImageDraw.Draw(sheet)
    for j, f in enumerate(fs[k:k + C * R]):
        x, y = (j % C) * W, (j // C) * H
        sheet.paste(Image.open(f).resize((W - 4, H - 4)), (x + 2, y + 2))
        n = os.path.basename(f)[:4]; d.rectangle([x + 2, y + 2, x + 44, y + 20], fill=(0, 0, 0)); d.text((x + 6, y + 3), n, font=font, fill=(255, 255, 0))
    sheet.save(os.path.join(out, f"foglio_{k // (C * R) + 1:02d}.jpg"), quality=88)
print(len(fs), "fotogrammi in", (len(fs) + C * R - 1) // (C * R), "fogli")
