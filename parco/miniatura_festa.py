#!/usr/bin/env python3
"""Miniatura VERTICALE 1080x1920 per lo Short 'La festa a sorpresa'."""
import os
from PIL import Image, ImageEnhance
import short_festa as S
from miniatura_barattolo import outline_text, sparkle
HERE = os.path.dirname(os.path.abspath(__file__))


def tall():
    img = Image.frombytes("RGB", (1080, 1920), S.frame(int((S.T_SPLAT + 0.6) * 30)))
    img = ImageEnhance.Color(ImageEnhance.Contrast(img).enhance(1.08)).enhance(1.12)
    for (x, y, r) in ((140, 600, 36), (950, 700, 40)): sparkle(img, x, y, r)
    outline_text(img, "SORPRESA!", 540, 170, 150, (255, 235, 90), (220, 40, 120), 14, rot=-3)
    outline_text(img, "SPLAT!", 540, 1760, 150, (255, 255, 255), (220, 40, 120), 14, rot=4)
    return img


if __name__ == "__main__":
    tall().save(os.path.join(HERE, "miniatura_festa_1080x1920.jpg"), quality=93); print("ok")
