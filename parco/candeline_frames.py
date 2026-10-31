#!/usr/bin/env python3
"""Short 'Soffia le candeline!' (primo piano del festeggiato, ispirato ai virali di compleanno): fotogrammi di partenza 720x1280 -> assets/v/candeline/startN.png"""
import os
from PIL import Image
import biscotto_frames as B
HERE = B.HERE
OUT = os.path.join(HERE, "assets", "v", "candeline"); os.makedirs(OUT, exist_ok=True)
W, H = B.W, B.H


def bg():
    return Image.open(os.path.join(HERE, "assets", "amb", "radura_festa.png")).convert("RGB").resize((W, H), Image.LANCZOS)


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    # 1: primo piano topolino dietro la torta con le candeline accese
    im = bg(); B.put(im, "topo_neutro", 360, 1280, 1100); B.obj(im, "cake", 360, 1050, 520); sv(im, 1)
    # 2: topolino soffia (bocca a O) (stessa inquadratura), candeline ancora accese
    im = bg(); B.put(im, "topo_parla_o", 360, 1280, 1100); B.obj(im, "cake", 360, 1050, 520); sv(im, 2)
    # 3: festa: topolino e Chip esultano, torta con candeline spente
    im = bg(); B.put(im, "topo_ride", 170, 1180, 640); B.put(im, "chip_ride", 560, 1180, 640); B.obj(im, "cake_off", 365, 1130, 300); sv(im, 3)
    s = Image.new("RGB", (W, H // 3))
    for k in range(1, 4): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0))
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
