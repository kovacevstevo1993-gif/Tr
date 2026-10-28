#!/usr/bin/env python3
"""Short 'Chi ha rubato la torta?' (schema dei virali: scena larga -> primo piano -> scena larga col colpo di scena) -> assets/v/torta/startN.png"""
import os
from PIL import Image, ImageDraw
import biscotto_frames as B
HERE = B.HERE
OUT = os.path.join(HERE, "assets", "v", "torta"); os.makedirs(OUT, exist_ok=True)
W, H = B.W, B.H


def bg():
    return Image.open(os.path.join(HERE, "assets", "amb", "collina.png")).convert("RGB").resize((W, H), Image.LANCZOS)


def blanket(im, cx, cy, w, h):
    d = ImageDraw.Draw(im, "RGBA"); x0, y0, x1, y1 = cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2
    d.ellipse([x0, y0, x1, y1], fill=(210, 40, 45, 255))
    for k in range(-5, 6):
        d.line([cx + k * w // 11, y0 + 6, cx + k * w // 11, y1 - 6], fill=(255, 255, 255, 140), width=18)
    d.ellipse([x0, y0, x1, y1], outline=(150, 20, 25, 255), width=6)


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    # 1: scena larga, picnic su collina, torta al centro, un uccellino lontano nel cielo
    im = bg(); blanket(im, 360, 1010, 600, 190); B.put(im, "topo_ride", 150, 1020, 430); B.put(im, "chip_ride", 575, 1020, 430)
    B.obj(im, "cake", 360, 960, 190); B.obj(im, "bird", 560, 330, 90); sv(im, 1)
    # 2: primo piano del topolino sorpreso, plaid vuoto dietro
    im = bg(); blanket(im, 360, 1130, 700, 220); B.put(im, "topo_sorpreso", 360, 1230, 960); sv(im, 2)
    # 3: scena larga, l'uccello vola via con la torta, i due guardano su
    im = bg(); blanket(im, 360, 1100, 600, 190); B.put(im, "topo_guarda_su", 150, 1110, 430); B.put(im, "chip_guarda_su", 575, 1110, 430)
    B.obj(im, "bird", 370, 420, 240); B.obj(im, "cake", 370, 560, 120); sv(im, 3)
    s = Image.new("RGB", (W, H // 3))
    for k in range(1, 4): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0))
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
