"""Miniature video 6 (2027 Cola): due layout diversi per il test A/B. 1280x720. Blu notte + oro, rosso/verde."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from PIL import Image, ImageDraw
from thumbs_video3_split import P

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "..", "miniature_video6"))
BLK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, GOLD, GOLDL = (226, 44, 44), (40, 190, 95), (212, 172, 82), (246, 214, 140)


def bg(cx, cy, k=1.0):
    yy, xx = np.mgrid[0:H, 0:W]
    g = np.clip(1 - (((xx - cx) / 800) ** 2 + ((yy - cy) / 520) ** 2), 0, 1) * k
    arr = np.stack([8 + 18 * g, 20 + 38 * g, 44 + 62 * g], axis=-1).astype("uint8")
    return Image.fromarray(arr)


def T(d, xy, s, size, fill, sw=8, anchor="mm"):
    d.text(xy, s, font=P(size, True), fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=BLK)


def arrow(d, x1, y, x2, col, th=34, head=70):
    d.polygon([(x1, y - th / 2), (x2 - head, y - th / 2), (x2 - head, y - head), (x2, y), (x2 - head, y + head), (x2 - head, y + th / 2), (x1, y + th / 2)], fill=col, outline=BLK)
    d.line([(x1, y - th / 2), (x2 - head, y - th / 2), (x2 - head, y - head), (x2, y), (x2 - head, y + head), (x2 - head, y + th / 2), (x1, y + th / 2), (x1, y - th / 2)], fill=BLK, width=7)


def A():
    """A: $72 (titolo del giornale) barrato -> $65 (vero), morso rosso di Medicare."""
    im = bg(640, 330); d = ImageDraw.Draw(im)
    d.rounded_rectangle([40, 30, 430, 120], radius=24, fill=GOLD, outline=BLK, width=7)
    T(d, (235, 76), "2027 COLA", 58, (14, 26, 52), sw=0)
    T(d, (330, 205), "THE NEWS SAYS", 40, (200, 215, 235), 6)
    T(d, (950, 205), "YOU KEEP", 40, (200, 215, 235), 6)
    T(d, (310, 370), "$72", 235, GOLDL, 14)
    d.line([130, 470, 500, 270], fill=RED, width=26)
    d.line([130, 470, 500, 270], fill=WHITE, width=6)
    arrow(d, 570, 380, 690, WHITE, th=30, head=56)
    T(d, (960, 370), "$65", 235, (110, 255, 150), 14)
    # chip rosso "Medicare" con freccia verso il pezzo mancante
    d.rounded_rectangle([720, 505, 1200, 600], radius=26, fill=RED, outline=WHITE, width=6)
    T(d, (960, 553), "-$6.60 MEDICARE", 42, WHITE, 0)
    d.rounded_rectangle([0, 630, W, 720], fill=(255, 214, 50))
    T(d, (640, 677), "WHERE DOES THE REST GO?", 62, (14, 14, 14), 0)
    return im


def B():
    """B: notifica del deposito in banca con la riga rossa + titolo a destra."""
    im = bg(420, 360, 0.9); d = ImageDraw.Draw(im)
    d.rounded_rectangle([14, 14, W - 15, H - 15], radius=30, outline=GOLD, width=10)
    # carta 'deposito'
    d.rounded_rectangle([50, 90, 640, 640], radius=44, fill=(245, 247, 250), outline=BLK, width=8)
    d.rounded_rectangle([86, 124, 190, 196], radius=18, fill=(14, 26, 52))
    T(d, (138, 160), "SS", 44, GOLD, 0)
    d.text((210, 138), "SOCIAL SECURITY", font=P(34, True), fill=(30, 40, 70), anchor="lm")
    d.text((210, 178), "Deposit - January 2027", font=P(28, False), fill=(110, 120, 140), anchor="lm")
    T(d, (345, 320), "+$72", 150, GREEN, 10)
    d.text((345, 410), "YOUR RAISE", font=P(40, True), fill=(30, 40, 70), anchor="mm")
    d.rounded_rectangle([86, 430, 604, 510], radius=22, fill=RED)
    T(d, (345, 470), "-$6.60 MEDICARE", 42, WHITE, 0)
    d.rounded_rectangle([86, 530, 604, 610], radius=22, fill=(255, 214, 50))
    T(d, (345, 570), "TAXES: ???", 42, (14, 14, 14), 0)
    # testo a destra
    T(d, (945, 150), "2027 COLA", 92, GOLD, 9)
    T(d, (945, 290), "YOUR RAISE", 84, WHITE, 8)
    T(d, (945, 410), "HAS A", 90, WHITE, 8)
    T(d, (945, 540), "CATCH", 140, (255, 80, 80), 12)
    return im


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in {"video6-A-72-diventa-65": A, "video6-B-deposito-ha-un-trucco": B}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
