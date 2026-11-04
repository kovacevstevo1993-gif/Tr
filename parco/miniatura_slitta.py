#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Lo slittino pazzo' (fotogramma pulito di partenza: volpe sorpresa)."""
import os
from PIL import Image, ImageEnhance
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    img = Image.open(os.path.join(HERE, "assets", "v", "slitta", "start2.png")).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.12)
    for (x, y, r) in ((130, 640, 38), (960, 520, 42), (900, 1100, 30), (150, 1200, 28)): sparkle(img, x, y, r)
    outline_text(img, "SLITTINO", 540, 150, 150, (255, 235, 90), (30, 90, 190), 14, rot=-2)
    outline_text(img, "PAZZO!", 540, 330, 150, (255, 235, 90), (30, 90, 190), 14, rot=-2)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_slitta_1080x1920.jpg"), quality=93); print("ok")
