#!/usr/bin/env python3
"""Miniature per lo Short 'Il seme magico' (1280x720 e 1080x1920). Riusa gli helper di miniatura_barattolo.py. Nessun costo."""
import os
from PIL import Image, ImageFilter
from miniatura_barattolo import A, HERE, pose, rays, add_glow, shadow_paste, outline_text, sparkle, finish, crop


def tree(h):
    im = crop(Image.open(A("obj", "tree.png")).convert("RGBA")); return im.resize((int(im.width * h / im.height), int(h)), Image.LANCZOS)


def wide():
    W, H = 1280, 720
    bg = Image.open(A("amb", "giardino.png")).convert("RGB"); bg = bg.resize((W, int(W * bg.height / bg.width)), Image.BICUBIC)
    img = bg.crop((0, 560, W, 560 + H)).filter(ImageFilter.GaussianBlur(1.6))
    rays(img, 980, 330, n=14, a=60); img = add_glow(img, 980, 330, 420, (255, 200, 90), 0.9)
    tr = tree(650); shadow_paste(img, tr, 985 - tr.width // 2, 715 - tr.height)
    for (n, h, x, m) in (("topo_guarda_su", 430, 70, False), ("chip_guarda_su", 410, 300, True), ("spike_guarda_su", 370, 500, False)):
        im = pose(n, h, m); shadow_paste(img, im, x, 715 - im.height)
    for (x, y, r) in ((700, 330, 30), (1230, 200, 34), (800, 120, 24), (560, 300, 22), (1190, 480, 22)): sparkle(img, x, y, r)
    outline_text(img, "IL SEME", 360, 95, 134, (255, 244, 120), (200, 40, 70), 12, rot=-3)
    outline_text(img, "MAGICO!", 380, 220, 112, (255, 255, 255), (70, 40, 140), 11, rot=-3)
    return finish(img)


def tall():
    W, H = 1080, 1920
    img = Image.open(A("amb", "giardino.png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2.0))
    rays(img, 600, 700, n=16, a=60); img = add_glow(img, 600, 650, 560, (255, 200, 90), 0.9)
    tr = tree(1150); shadow_paste(img, tr, 600 - tr.width // 2, 1700 - tr.height)
    x = 10
    for (n, h, m) in (("topo_guarda_su", 560, False), ("chip_guarda_su", 520, True), ("spike_guarda_su", 460, False)):
        im = pose(n, h, m); shadow_paste(img, im, x, 1840 - im.height); x += im.width - 20
    for (px, y, r) in ((140, 640, 40), (960, 520, 46), (880, 1000, 30), (210, 1000, 28), (700, 330, 26)): sparkle(img, px, y, r)
    outline_text(img, "IL SEME", W / 2, 210, 215, (255, 244, 120), (200, 40, 70), 16, rot=-3)
    outline_text(img, "MAGICO!", W / 2, 420, 180, (255, 255, 255), (70, 40, 140), 14, rot=-3)
    return finish(img)


if __name__ == "__main__":
    wide().save(os.path.join(HERE, "miniatura_seme_1280x720.jpg"), quality=93)
    tall().save(os.path.join(HERE, "miniatura_seme_1080x1920.jpg"), quality=93)
    print("ok")
