#!/usr/bin/env python3
"""Short 'La mela di Spike' (storia logica: condividere) nel bosco -> assets/v/mela2/startN.png"""
import os
from PIL import Image
import biscotto_frames as B
HERE = B.HERE
OUT = os.path.join(HERE, "assets", "v", "mela2"); os.makedirs(OUT, exist_ok=True)
W, H = B.W, B.H


def bg():
    return Image.open(os.path.join(HERE, "assets", "amb", "bosco.png")).convert("RGB").resize((W, H), Image.LANCZOS)


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    im = bg(); B.put(im, "chip_indica", 360, 1240, 1000); sv(im, 1)
    im = bg(); B.put(im, "spike_tiene_mela", 360, 1240, 980); sv(im, 2)
    im = bg(); B.put(im, "spike_riceve", 360, 1240, 980); B.obj(im, "apple", 575, 600, 130); sv(im, 3)
    im = bg(); B.put(im, "topo_mangia_mela", 120, 1230, 600); B.put(im, "spike_mangia_mela", 360, 1250, 620); B.put(im, "chip_mangia_mela", 600, 1240, 620); sv(im, 4)
    s = Image.new("RGB", (W * 4 // 3, H // 3))
    for k in range(1, 5): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0))
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
