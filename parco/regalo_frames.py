#!/usr/bin/env python3
"""Short 'Il regalo per la volpe' (storiella in 8 scene, tramonto) -> assets/v/regalo/startN.png"""
import os
from PIL import Image
import biscotto_frames as B
HERE = B.HERE
OUT = os.path.join(HERE, "assets", "v", "regalo"); os.makedirs(OUT, exist_ok=True)
W, H = B.W, B.H


def bg():
    return Image.open(os.path.join(HERE, "assets", "amb", "tramonto.png")).convert("RGB").resize((W, H), Image.LANCZOS)


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    # 1 topolino e Chip portano il regalo (scena larga)
    im = bg(); B.put(im, "topo_tiene", 190, 1180, 640); B.put(im, "chip_tiene", 520, 1190, 640); B.obj(im, "gift", 360, 1010, 260); sv(im, 1)
    # 2 Chip primo piano, dito sulle labbra
    im = bg(); B.put(im, "chip_parla_a", 360, 1240, 1000); sv(im, 2)
    # 3 scena larga: dietro un cespuglio Spike sbircia, i due col regalo piu' lontani
    im = bg(); B.put(im, "topo_tiene", 150, 1130, 520); B.put(im, "chip_tiene", 330, 1135, 520); B.obj(im, "gift", 240, 1000, 190)
    B.put(im, "spike_sbircia", 600, 1150, 520); B.obj(im, "bush", 590, 1150, 380); sv(im, 3)
    # 4 topolino primo piano, sussurra
    im = bg(); B.put(im, "topo_parla_a", 360, 1240, 960); sv(im, 4)
    # 5 la volpe arriva camminando da destra, i tre col regalo a sinistra
    im = bg(); B.put(im, "topo_tiene", 110, 1170, 470); B.put(im, "chip_tiene", 270, 1175, 470); B.put(im, "spike_neutro", 430, 1185, 440); B.obj(im, "gift", 210, 1030, 170)
    B.put(im, "volpe_cammina1", 620, 1160, 560); sv(im, 5)
    # 6 tutti insieme gridano auguri, la volpe al centro (scena larga)
    im = bg(); B.put(im, "topo_saluta", 100, 1180, 520); B.put(im, "chip_saluta", 250, 1190, 520); B.put(im, "volpe_sorpreso", 430, 1190, 600); B.put(im, "spike_saluta", 600, 1200, 520); sv(im, 6)
    # 7 volpe primo piano apre il regalo, felice
    im = bg(); B.put(im, "volpe_ride", 360, 1240, 1000); B.obj(im, "gift", 360, 1080, 240); sv(im, 7)
    # 8 abbraccio finale, scena larga
    im = bg(); B.put(im, "topo_ride", 90, 1190, 520); B.put(im, "chip_ride", 240, 1200, 520); B.put(im, "volpe_abbraccia", 430, 1210, 620); B.put(im, "spike_ride", 610, 1210, 520); sv(im, 8)
    s = Image.new("RGB", (W * 8 // 4, H * 2 // 4))
    for k in range(1, 9): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 4, H // 4)), (((k - 1) % 4) * W // 4 * 2 // 2, 0 if k <= 4 else H // 4))
    s = s.crop((0, 0, W, H // 2)); s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
