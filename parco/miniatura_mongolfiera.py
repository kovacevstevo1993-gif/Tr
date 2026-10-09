#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'La mongolfiera dei 4 amici' (nessuna orizzontale). Usa il motore dello Short: nessun costo."""
import os, math
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import short_mongolfiera as S
from miniatura_barattolo import outline_text, sparkle

HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    t = S.V["c1"] + 0.35                       # amici felici in cielo, pallone intero
    img = S.scene_img("cielo", t, 540, 960, 1.0)
    arr = np.asarray(img).astype(np.float32)
    bl = cv2.GaussianBlur(np.clip(arr - 200, 0, 255) * 3.0, (0, 0), 16); arr = np.clip(arr + bl * 0.35, 0, 255)
    img = Image.fromarray(arr.astype(np.uint8))
    img = ImageEnhance.Contrast(img).enhance(1.10); img = ImageEnhance.Color(img).enhance(1.20)
    # luce dal sole in alto a destra
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(9):
        a = math.radians(100 + k * 9); x1 = 880 + math.cos(a) * 2200; y1 = 140 + math.sin(a) * 2200
        d.polygon([(880, 140), (x1 - 120, y1), (x1 + 120, y1)], fill=(255, 245, 190, 38))
    lay = lay.filter(ImageFilter.GaussianBlur(10)); img.paste(lay, (0, 0), lay)
    for (x, y, r) in ((130, 520, 40), (960, 430, 46), (150, 1180, 30), (950, 1030, 34), (560, 300, 26)): sparkle(img, x, y, r)
    outline_text(img, "LA MONGOLFIERA", 540, 122, 92, (255, 244, 120), (200, 40, 70), 12, rot=0)
    outline_text(img, "dei 4 AMICI!", 540, 1815, 138, (255, 255, 255), (30, 100, 170), 12, rot=-2)
    # fumetto POP!
    d = ImageDraw.Draw(img, "RGBA"); cx, cy = 880, 1010
    pts = []
    for i in range(24):
        a = i / 24 * 2 * math.pi; r = 150 if i % 2 == 0 else 100; pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r))
    d.polygon(pts, fill=(255, 226, 60, 255), outline=(200, 40, 70, 255))
    outline_text(img, "POP?", cx, cy, 96, (200, 40, 70), (255, 255, 255), 8, rot=-8, shadow=False)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_mongolfiera_1080x1920.jpg"), quality=93)
    print("ok")
