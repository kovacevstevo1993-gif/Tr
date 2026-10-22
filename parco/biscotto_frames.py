#!/usr/bin/env python3
"""Short 'Chi ha mangiato il biscotto?': fotogrammi di partenza 720x1280 (cucina) per le clip Wan 2.2. -> assets/v/biscotto/startN.png"""
import os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "v", "biscotto"); os.makedirs(OUT, exist_ok=True)
W, H = 720, 1280


def bg():
    return Image.open(os.path.join(HERE, "assets", "amb", "cucina.png")).convert("RGB").resize((W, H), Image.LANCZOS)


def img(path):
    im = Image.open(path).convert("RGBA"); return im.crop(im.getbbox())


def put(im, n, cx, foot, h):
    p = img(os.path.join(HERE, "assets", "pose", n + ".png")); p = p.resize((int(p.width * h / p.height), h), Image.LANCZOS)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([cx - p.width * 0.42, foot - 16, cx + p.width * 0.42, foot + 14], fill=(60, 35, 10, 120)); sh = sh.filter(ImageFilter.GaussianBlur(8))
    im.paste(sh, (0, 0), sh); im.paste(p, (int(cx - p.width / 2), int(foot - p.height)), p)


def obj(im, n, cx, cy, w):
    o = img(os.path.join(HERE, "assets", "obj", n + ".png")); o = o.resize((w, int(o.height * w / o.width)), Image.LANCZOS); im.paste(o, (int(cx - o.width / 2), int(cy - o.height / 2)), o)


def crumbs(im, pts):
    d = ImageDraw.Draw(im, "RGBA")
    for x, y, r in pts: d.ellipse([x - r, y - r * 0.7, x + r, y + r * 0.7], fill=(150, 95, 40, 255)); d.ellipse([x - r * 0.5, y - r * 0.5, x, y - r * 0.1], fill=(190, 130, 70, 255))


def main():
    sv = lambda im, k: im.save(os.path.join(OUT, f"start{k}.png"))
    # 1: piatto vuoto bene in vista, i tre sospettati sotto, sorpresi
    im = bg(); d = ImageDraw.Draw(im, "RGBA")
    d.ellipse([245, 580, 465, 645], fill=(245, 245, 240, 255), outline=(190, 190, 185, 255), width=4); d.ellipse([268, 592, 442, 632], fill=(230, 230, 225, 255))
    put(im, "topo_sorpreso", 130, 1250, 520); put(im, "volpe_sorpreso", 360, 1255, 560); put(im, "rana_sorpreso", 590, 1260, 530); sv(im, 1)
    # 2: topolino da solo, alza le mani "non sono io"
    im = bg(); put(im, "topo_sorpreso", 360, 1230, 960); sv(im, 2)
    # 3: volpe da sola, finge niente (guarda di lato)
    im = bg(); put(im, "volpe_pensa", 360, 1235, 1000); sv(im, 3)
    # 4: rana da sola
    im = bg(); put(im, "rana_neutro", 360, 1240, 980); sv(im, 4)
    # 5: i tre guardano per terra, scia di briciole grandi in primo piano
    im = bg(); put(im, "topo_sbircia", 130, 1010, 540); put(im, "volpe_indica", 360, 1000, 600); put(im, "rana_indica", 595, 1015, 560)
    crumbs(im, [(130, 1110, 20), (230, 1150, 24), (340, 1190, 22), (450, 1215, 26), (560, 1235, 24), (660, 1255, 22)]); sv(im, 5)
    # 6: Spike col biscotto, scoperto
    im = bg(); put(im, "spike_tiene_biscotto", 360, 1235, 960); sv(im, 6)
    # 7: tutti insieme ridono (Spike davanti)
    im = bg(); put(im, "topo_ride", 110, 1220, 560); put(im, "volpe_ride", 280, 1230, 640); put(im, "rana_ride", 630, 1240, 580); put(im, "spike_ride", 470, 1250, 600); sv(im, 7)
    s = Image.new("RGB", (W * 7 // 3, H // 3))
    for k in range(1, 8): s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0))
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
