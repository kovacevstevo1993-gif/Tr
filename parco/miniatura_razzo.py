#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Il razzo per la luna'. Usa il motore dello Short: nessun costo."""
import os, math
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageEnhance
import short_razzo as S
from miniatura_barattolo import outline_text, sparkle

HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    t = S.T_THINK + 0.5                                   # sulla luna, nuvoletta col formaggio, razzo e Terra
    img = S.scene_img("luna", t, 560, 1060, 1.12)
    arr = np.asarray(img).astype(np.float32)
    arr = np.clip(arr + cv2.GaussianBlur(np.clip(arr - 200, 0, 255) * 3.0, (0, 0), 16) * 0.35, 0, 255)
    img = ImageEnhance.Color(ImageEnhance.Contrast(Image.fromarray(arr.astype(np.uint8))).enhance(1.1)).enhance(1.2)
    for (x, y, r) in ((120, 520, 40), (960, 760, 40), (300, 900, 26), (860, 300, 30)): sparkle(img, x, y, r)
    outline_text(img, "SULLA LUNA!", 540, 150, 130, (255, 235, 90), (110, 40, 160), 13, rot=-3)
    d = ImageDraw.Draw(img, "RGBA"); cx, cy = 540, 1780
    pts = [(cx + math.cos(i / 28 * 6.283) * 470 * (1 if i % 2 == 0 else 0.8), cy + math.sin(i / 28 * 6.283) * 120 * (1 if i % 2 == 0 else 0.8)) for i in range(28)]
    d.polygon(pts, fill=(255, 205, 60, 255), outline=(200, 40, 70, 255))
    outline_text(img, "È FORMAGGIO?!", cx, cy, 80, (200, 40, 70), (255, 255, 255), 7, rot=-2, shadow=False)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_razzo_1080x1920.jpg"), quality=93); print("ok")
