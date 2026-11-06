#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Contiamo i pesci' (fotogramma pulito fk4: pinguino + 4 pesci composti)."""
import os
from PIL import Image, ImageEnhance
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    img = Image.open(os.path.join(HERE, "assets", "v", "pesci", "fk4.png")).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.1)).enhance(1.15)
    for (x, y, r) in ((90, 700, 34), (1000, 560, 40), (980, 1380, 30)): sparkle(img, x, y, r)
    outline_text(img, "QUANTI", 540, 150, 200, (255, 235, 90), (200, 40, 40), 16, rot=0)
    outline_text(img, "PESCI?", 540, 360, 200, (255, 255, 255), (30, 90, 200), 16, rot=0)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_pesci_1080x1920.jpg"), quality=93); print("ok")
