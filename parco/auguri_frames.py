#!/usr/bin/env python3
"""Short 'Tanti auguri!' (ispirato a 'Tanti Auguri #shorts' di HeyKids: corsa alla festa -> gioia -> chi presenta la torta -> soffio -> applausi).
Fotogrammi di partenza 720x1280 delle 3 inquadrature nuove -> assets/v/auguri/startN.png (soffio e applausi riusano le clip di assets/v/candeline)."""
import os
from PIL import Image
import biscotto_frames as B
HERE = B.HERE
OUT = os.path.join(HERE, "assets", "v", "auguri"); os.makedirs(OUT, exist_ok=True)
W, H = B.W, B.H


def bg(n):
    return Image.open(os.path.join(HERE, "assets", "amb", n + ".png")).convert("RGB").resize((W, H), Image.LANCZOS)


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    # 1: topolino corre verso destra sulla collina, il regalo lo segue
    im = bg("collina"); B.obj(im, "gift", 110, 1120, 220); B.put(im, "topo_corre", 330, 1250, 760); sv(im, 1)
    # 2: primo piano di gioia davanti alla festa (stessa radura delle candeline)
    im = bg("radura_festa"); B.put(im, "topo_ride", 360, 1280, 1100); sv(im, 2)
    # 3: la volpe presenta la torta (a sinistra topolino e volpe ai lati della torta con le candeline)
    im = bg("radura_festa"); B.put(im, "volpe_saluta", 540, 1230, 820); B.put(im, "topo_ride", 140, 1230, 560); B.obj(im, "cake", 330, 1105, 300); sv(im, 3)
    s = Image.new("RGB", (W, H // 3))
    for k in range(1, 4): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0))
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
