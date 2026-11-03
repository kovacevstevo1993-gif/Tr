#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Chi ha rubato la torta?' (fotogramma pulito di partenza start3: l'uccello vola via con la torta)."""
import os
from PIL import Image, ImageEnhance
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    img = Image.open(os.path.join(HERE, "assets", "v", "torta", "start3.png")).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.12)
    for (x, y, r) in ((130, 700, 38), (960, 620, 42), (900, 1250, 30), (150, 1350, 28)): sparkle(img, x, y, r)
    outline_text(img, "CHI HA RUBATO", 540, 120, 112, (255, 235, 90), (200, 40, 40), 14, rot=-2)
    outline_text(img, "LA TORTA?!", 540, 290, 130, (255, 235, 90), (200, 40, 40), 14, rot=-2)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_torta_1080x1920.jpg"), quality=93); print("ok")
