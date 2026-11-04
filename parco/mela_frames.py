#!/usr/bin/env python3
"""Short 'L'elefantino ha fame' (formato virale 8-10 s, una gag): fotogrammi di partenza 720x1280 per Wan 2.2 -> assets/v/mela/startN.png"""
import os
from PIL import Image
import biscotto_frames as B
HERE = B.HERE
OUT = os.path.join(HERE, "assets", "v", "mela"); os.makedirs(OUT, exist_ok=True)
W, H = B.W, B.H


def bg():
    return Image.open(os.path.join(HERE, "assets", "amb", "giardino.png")).convert("RGB").resize((W, H), Image.LANCZOS)


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    # 1: topolino (a sinistra) offre una mela grande all'elefantino affamato (a destra)
    im = bg(); B.put(im, "topo_tiene", 190, 1180, 700); B.put(im, "ele_guarda_su", 520, 1200, 860); B.obj(im, "apple", 330, 800, 150); sv(im, 1)
    # 2: elefantino con la mela, sta per mangiarla
    im = bg(); B.put(im, "ele_tiene", 400, 1220, 1000); B.obj(im, "apple", 400, 880, 140); sv(im, 2)
    # 3: elefantino fa spruzzo, topolino davanti sorpreso
    im = bg(); B.put(im, "topo_sorpreso", 170, 1180, 640); B.put(im, "ele_spruzza", 520, 1200, 900); sv(im, 3)
    # 4: ridono insieme
    im = bg(); B.put(im, "topo_ride", 190, 1180, 700); B.put(im, "ele_ride", 520, 1200, 900); sv(im, 4)
    s = Image.new("RGB", (W * 4 // 3, H // 3))
    for k in range(1, 5): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0))
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
