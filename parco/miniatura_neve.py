#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Il pupazzo di neve' (nessuna orizzontale). Usa il motore dello Short: nessun costo."""
import os, math
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import short_neve as S
from miniatura_barattolo import outline_text, sparkle

HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    t = S.T_WINK + 0.2                                  # il pupazzo gigante fa l'occhiolino, amici felici
    img = S.scene_img("neve_sera", t, 585, 1060, 1.12)
    arr = np.asarray(img).astype(np.float32)
    bl = cv2.GaussianBlur(np.clip(arr - 200, 0, 255) * 3.0, (0, 0), 16); arr = np.clip(arr + bl * 0.35, 0, 255)
    img = Image.fromarray(arr.astype(np.uint8))
    img = ImageEnhance.Contrast(img).enhance(1.10); img = ImageEnhance.Color(img).enhance(1.20)
    for (x, y, r) in ((120, 640, 40), (960, 560, 46), (150, 1080, 30), (980, 980, 34), (300, 420, 26), (800, 380, 30)): sparkle(img, x, y, r)
    outline_text(img, "IL PUPAZZO", 540, 120, 128, (255, 255, 255), (40, 90, 190), 13, rot=0)
    outline_text(img, "DI NEVE", 540, 262, 128, (255, 255, 255), (40, 90, 190), 13, rot=0)
    d = ImageDraw.Draw(img, "RGBA"); cx, cy = 540, 1790                         # fumetto in basso
    pts = []
    for i in range(28):
        a = i / 28 * 2 * math.pi; r = 1.0 if i % 2 == 0 else 0.78; pts.append((cx + math.cos(a) * 330 * r, cy + math.sin(a) * 120 * r))
    d.polygon(pts, fill=(255, 226, 60, 255), outline=(200, 40, 70, 255))
    outline_text(img, "È VIVO?!", cx, cy, 104, (200, 40, 70), (255, 255, 255), 8, rot=-3, shadow=False)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_neve_1080x1920.jpg"), quality=93)
    print("ok")
