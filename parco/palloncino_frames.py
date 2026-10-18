#!/usr/bin/env python3
"""Short 'Il palloncino rosso': fotogrammi di partenza (720x1280) per le clip Wan 2.2 (immagine -> video, gratis su HuggingFace).
Topolino e Chip GRANDI e al CENTRO, giardino, palloncino disegnato. -> assets/v/palloncino/startN.png"""
import math, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "v", "palloncino"); os.makedirs(OUT, exist_ok=True)
W, H = 720, 1280


def bg():
    return Image.open(os.path.join(HERE, "assets", "amb", "giardino.png")).convert("RGB").resize((W, H), Image.LANCZOS)


def pose(n, h):
    im = Image.open(os.path.join(HERE, "assets", "pose", n + ".png")).convert("RGBA"); im = im.crop(im.getbbox())
    return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)


def put(img, n, cx, foot, h, flip=False):
    p = pose(n, h)
    if flip: p = p.transpose(Image.FLIP_LEFT_RIGHT)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([cx - p.width * 0.38, foot - 18, cx + p.width * 0.38, foot + 14], fill=(30, 50, 20, 110))
    img.paste(sh.filter(ImageFilter.GaussianBlur(8)), (0, 0), sh.filter(ImageFilter.GaussianBlur(8)))
    img.paste(p, (int(cx - p.width / 2), int(foot - p.height)), p)
    return lambda fx, fy: (cx - p.width / 2 + fx * p.width, foot - p.height + fy * p.height)


def balloon(img, x, y, r=78, string_to=None):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    if string_to:
        pts = []
        for k in range(21):
            u = k / 20; px = x + (string_to[0] - x) * u + 14 * math.sin(u * math.pi * 2); py = y + r * 1.15 + (string_to[1] - y - r * 1.15) * u
            pts.append((px, py))
        d.line(pts, fill=(250, 250, 250, 255), width=3)
    for i in range(r, 0, -1):                                    # sfera lucida: rosso scuro al bordo, chiaro al centro-alto
        u = i / r; c = (int(150 + 95 * (1 - u)), int(10 + 30 * (1 - u)), int(25 + 30 * (1 - u)), 255)
        d.ellipse([x - i, y - i * 1.15 - (r - i) * 0.25, x + i, y + i * 1.15 - (r - i) * 0.25], fill=c)
    d.polygon([(x - 11, y + r * 1.15 + 12), (x + 11, y + r * 1.15 + 12), (x, y + r * 1.15 - 4)], fill=(170, 15, 30, 255))
    hl = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(hl).ellipse([x - r * 0.55, y - r * 0.85, x - r * 0.15, y - r * 0.3], fill=(255, 255, 255, 170))
    lay.alpha_composite(hl.filter(ImageFilter.GaussianBlur(6)))
    img.paste(lay, (0, 0), lay)


def main():
    def up(hand, r=78, lift=330, x=None): balloon(im, x or hand[0], hand[1] - lift, r, hand)
    # 1-2: il topolino tiene il palloncino con la mano alzata (il filo non passa davanti alla faccia)
    for k in (1, 2):
        im = bg(); h = put(im, "topo_saluta", 340, 1210, 860); up(h(0.88, 0.26)); im.save(os.path.join(OUT, f"start{k}.png"))
    # 3: palloncino incastrato tra i rami dell'albero a destra, il topolino guarda su e indica
    im = bg(); balloon(im, 600, 380, 62, (640, 520)); put(im, "topo_guarda_su", 330, 1210, 860); im.save(os.path.join(OUT, "start3.png"))
    # 4: arriva Chip di corsa verso l'albero
    im = bg(); balloon(im, 600, 380, 62, (640, 520)); put(im, "topo_indica", 190, 1220, 720); put(im, "chip_corre", 530, 1200, 660); im.save(os.path.join(OUT, "start4.png"))
    # 5: Chip riporta il palloncino (mano alzata), il topolino lo aspetta
    im = bg(); put(im, "topo_neutro", 190, 1220, 740); h = put(im, "chip_saluta", 520, 1215, 740); up(h(0.1, 0.08), 72, 260); im.save(os.path.join(OUT, "start5.png"))
    # 6: festa insieme, Chip tiene alto il palloncino
    im = bg(); put(im, "topo_balla", 210, 1215, 720); h = put(im, "chip_balla", 530, 1215, 720); up(h(0.12, 0.08), 70, 260); im.save(os.path.join(OUT, "start6.png"))
    # 7: salutano i bambini
    im = bg(); h = put(im, "topo_saluta", 200, 1215, 760); put(im, "chip_saluta", 530, 1215, 750, flip=True); up(h(0.88, 0.26), 66, 280); im.save(os.path.join(OUT, "start7.png"))
    s = Image.new("RGB", (W * 7 // 3, H // 3 * 1)); [s.paste(Image.open(os.path.join(OUT, f"start{k}.png")).resize((W // 3, H // 3)), ((k - 1) * W // 3, 0)) for k in range(1, 8)]
    s.save(os.path.join(OUT, "sheet.png"))


if __name__ == "__main__":
    main()
