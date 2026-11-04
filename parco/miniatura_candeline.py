#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Soffia le candeline!' (fotogramma pulito di partenza start1: topolino con la torta)."""
import os
from PIL import Image, ImageEnhance
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    img = Image.open(os.path.join(HERE, "assets", "v", "candeline", "start1.png")).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.12)
    for (x, y, r) in ((110, 700, 38), (980, 600, 42), (950, 1250, 30), (120, 1400, 28)): sparkle(img, x, y, r)
    outline_text(img, "SOFFIA LE", 540, 130, 140, (255, 235, 90), (200, 40, 40), 14, rot=-2)
    outline_text(img, "CANDELINE!", 540, 300, 140, (255, 235, 90), (200, 40, 40), 14, rot=-2)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_candeline_1080x1920.jpg"), quality=93); print("ok")
