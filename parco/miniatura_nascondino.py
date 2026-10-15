#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Nascondino nel bosco d'autunno'."""
import os, math
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageEnhance
import short_nascondino as S
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    i = int((S.T_LOOK2 + 1.6) * 30)
    img = Image.frombytes("RGB", (1080, 1920), S.frame(i))
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.15)
    for (x, y, r) in ((140, 640, 36), (950, 520, 40), (880, 980, 28)): sparkle(img, x, y, r)
    outline_text(img, "DOVE SI È", 540, 150, 130, (255, 235, 90), (190, 60, 20), 13, rot=-2)
    outline_text(img, "NASCOSTO?", 540, 300, 130, (255, 235, 90), (190, 60, 20), 13, rot=-2)
    d = ImageDraw.Draw(img, "RGBA")
    d.line([(760, 560), (820, 820)], fill=(255, 255, 255, 255), width=18); d.polygon([(785, 850), (850, 790), (870, 880)], fill=(255, 255, 255, 255))
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_nascondino_1080x1920.jpg"), quality=93); print("ok")
