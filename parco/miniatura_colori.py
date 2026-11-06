#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Le porte dei colori' (fotogramma pulito di partenza R_0.45: porte + pinguino)."""
import os
from PIL import Image, ImageEnhance
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    img = Image.open(os.path.join(HERE, "assets", "v", "colori", "R_0.45.png")).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.12)
    for (x, y, r) in ((90, 1330, 36), (990, 1250, 42), (960, 1650, 30), (130, 1700, 28)): sparkle(img, x, y, r)
    outline_text(img, "COLORI!", 540, 140, 200, (255, 235, 90), (200, 40, 40), 16, rot=0)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_colori_1080x1920.jpg"), quality=93); print("ok")
