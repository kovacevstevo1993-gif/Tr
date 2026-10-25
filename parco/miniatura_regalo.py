#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'Il regalo per la volpe' (fotogramma della volpe col regalo)."""
import os
from PIL import Image, ImageDraw, ImageEnhance
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    import biscotto_frames as B
    img = Image.open(os.path.join(HERE, "assets", "amb", "tramonto.png")).convert("RGB").resize((B.W, B.H))
    B.put(img, "volpe_mani", 360, 1240, 1000); B.obj(img, "gift", 360, 1080, 240); img = img.resize((1080, 1920), Image.LANCZOS)
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.15)
    for (x, y, r) in ((130, 700, 38), (960, 560, 42), (900, 1060, 30), (170, 1180, 28)): sparkle(img, x, y, r)
    outline_text(img, "IL REGALO", 540, 150, 140, (255, 235, 90), (190, 60, 20), 14, rot=-2)
    outline_text(img, "PER LA VOLPE!", 540, 310, 112, (255, 235, 90), (190, 60, 20), 13, rot=-2)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_regalo_1080x1920.jpg"), quality=93); print("ok")
