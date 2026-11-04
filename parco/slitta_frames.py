#!/usr/bin/env python3
"""Short 'Lo slittino pazzo' (schema virali: scena larga -> primo piano -> scena larga col colpo di scena) -> assets/v/slitta/startN.png"""
import os
from PIL import Image
import biscotto_frames as B
HERE = B.HERE
OUT = os.path.join(HERE, "assets", "v", "slitta"); os.makedirs(OUT, exist_ok=True)
W, H = B.W, B.H


def bg(n="neve_discesa"):
    return Image.open(os.path.join(HERE, "assets", "amb", n + ".png")).convert("RGB").resize((W, H), Image.LANCZOS)


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    # 1: in cima alla discesa, volpe e Chip sullo slittino pronti a partire
    im = bg(); B.obj(im, "sled", 360, 1060, 700); B.put(im, "volpe_seduto", 290, 1060, 480); B.put(im, "chip_tiene", 450, 1060, 430); sv(im, 1)
    # 2: primo piano volpe con il vento in faccia
    im = bg(); B.put(im, "volpe_sorpreso", 360, 1240, 1000); sv(im, 2)
    # 3: in fondo, il mucchio di neve enorme; lo slittino arriva con i due
    im = bg(); B.obj(im, "snowball", 560, 1000, 520); B.obj(im, "sled", 230, 1110, 480); B.put(im, "volpe_seduto", 170, 1110, 330); B.put(im, "chip_tiene", 290, 1110, 300); sv(im, 3)
    s = Image.new("RGB", (W, H // 3))
    for k in range(1, 4): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0))
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
