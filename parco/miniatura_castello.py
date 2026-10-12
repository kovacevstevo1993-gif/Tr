#!/usr/bin/env python3
"""Miniature per lo Short 'Il castello di sabbia' (1280x720 e 1080x1920). Riusa gli helper di miniatura_barattolo.py. Nessun costo."""
import os, math
from PIL import Image, ImageDraw, ImageFilter
from miniatura_barattolo import A, HERE, pose, rays, add_glow, shadow_paste, outline_text, sparkle, finish, crop

RB = [(255, 70, 70), (255, 150, 50), (255, 225, 70), (100, 210, 100), (80, 160, 255), (110, 100, 230), (190, 110, 230)]


def rainbow(img, cx, cy, R, band, alpha=190):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i, col in enumerate(RB):
        r = R - i * band
        d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=col + (alpha,), width=band + 2)
    lay = lay.filter(ImageFilter.GaussianBlur(1.5)); img.paste(lay, (0, 0), lay)


def castle(h):
    im = crop(Image.open(A("obj", "castle_big.png")).convert("RGBA")); return im.resize((int(im.width * h / im.height), int(h)), Image.LANCZOS)


def drops(img, x, y, n=40, spread=150, seed=2):
    import random; rnd = random.Random(seed); d = ImageDraw.Draw(img, "RGBA")
    for k in range(n):
        a = rnd.uniform(-2.5, -0.6); r = rnd.uniform(40, spread); px, py = x + math.cos(a) * r * 0.9, y + math.sin(a) * r * 1.3 + rnd.uniform(0, 30)
        s = rnd.uniform(5, 11); d.ellipse([px - s, py - s * 1.2, px + s, py + s * 1.2], fill=(190, 232, 255, 215)); d.ellipse([px - s * .4, py - s * .8, px, py - s * .2], fill=(255, 255, 255, 240))


def wide():
    W, H = 1280, 720
    bg = Image.open(A("amb", "spiaggia_baia.png")).convert("RGB"); bg = bg.resize((W, int(W * bg.height / bg.width)), Image.BICUBIC)
    img = bg.crop((0, 1000, W, 1000 + H)).filter(ImageFilter.GaussianBlur(1.4))
    rays(img, 900, 120, n=14, a=40); img = add_glow(img, 150, 90, 420, (255, 215, 130), 0.45)
    rainbow(img, 650, 640, 560, 30, alpha=175)
    c = castle(590); shadow_paste(img, c, 650 - c.width // 2, 712 - c.height)
    ele = pose("ele_spruzza", 540); shadow_paste(img, ele, 905, 722 - ele.height)
    drops(img, 1040, 60, 46, 200)
    m = pose("topo_ride", 380); shadow_paste(img, m, 30, 722 - m.height)
    ch = pose("chip_salto", 300); shadow_paste(img, ch, 330, 700 - ch.height)
    for (x, y, r) in ((560, 250, 30), (1230, 330, 30), (300, 330, 24), (880, 300, 22), (40, 330, 22)): sparkle(img, x, y, r)
    outline_text(img, "CASTELLO", 320, 90, 108, (255, 244, 120), (200, 40, 70), 11, rot=-3)
    outline_text(img, "DI SABBIA!", 330, 195, 92, (255, 255, 255), (30, 100, 170), 10, rot=-3)
    return finish(img)


def tall():
    W, H = 1080, 1920
    img = Image.open(A("amb", "spiaggia_baia.png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2.0))
    rays(img, 700, 300, n=16, a=40); img = add_glow(img, 140, 160, 500, (255, 215, 130), 0.45)
    rainbow(img, 560, 1350, 700, 40, alpha=175)
    c = castle(980); shadow_paste(img, c, 470 - c.width // 2, 1700 - c.height)
    ele = pose("ele_spruzza", 820); shadow_paste(img, ele, 620, 1860 - ele.height)
    drops(img, 770, 1020, 60, 240)
    m = pose("topo_ride", 560); shadow_paste(img, m, 10, 1860 - m.height)
    ch = pose("chip_salto", 470); shadow_paste(img, ch, 320, 1700 - ch.height + 100)
    for (px, y, r) in ((120, 640, 40), (980, 520, 46), (900, 1100, 30), (200, 1000, 28), (700, 420, 26)): sparkle(img, px, y, r)
    outline_text(img, "CASTELLO", W / 2, 190, 168, (255, 244, 120), (200, 40, 70), 14, rot=-3)
    outline_text(img, "DI SABBIA!", W / 2, 370, 142, (255, 255, 255), (30, 100, 170), 12, rot=-3)
    return finish(img)


if __name__ == "__main__":
    wide().save(os.path.join(HERE, "miniatura_castello_1280x720.jpg"), quality=93)
    tall().save(os.path.join(HERE, "miniatura_castello_1080x1920.jpg"), quality=93)
    print("ok")
