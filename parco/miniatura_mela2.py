#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'La mela di Spike' (fotogramma pulito di partenza start2: Spike con la mela)."""
import os
from PIL import Image, ImageEnhance
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    img = Image.open(os.path.join(HERE, "assets", "v", "mela2", "start2.png")).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.12)
    for (x, y, r) in ((130, 640, 38), (960, 560, 42), (930, 1150, 30), (140, 1300, 28)): sparkle(img, x, y, r)
    outline_text(img, "È MIA,", 540, 150, 130, (255, 235, 90), (200, 40, 40), 14, rot=-2)
    outline_text(img, "SOLO MIA!", 540, 320, 130, (255, 235, 90), (200, 40, 40), 14, rot=-2)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_mela2_1080x1920.jpg"), quality=93); print("ok")
