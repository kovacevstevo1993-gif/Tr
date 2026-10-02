"""Miniature video 5 (Social Security Benefits Explained) per test A/B. 1280x720, Montserrat ExtraBold, stile rosso/verde dei video 1-3."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw
import thumbs_video3_split as S
from thumbs_video3_split import P, label, pill, otext, YEL, BLK, WHITE

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "..", "miniature_video5"))
os.makedirs(OUT, exist_ok=True)
RED = (224, 40, 40)


def bg_red():
    """tutto rosso scuro con alone chiaro al centro (allarme)"""
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        for x in range(W):
            g = max(0.0, 1 - (((x - 640) / 640) ** 2 + ((y - 330) / 420) ** 2))
            px[x, y] = (int(96 + 100 * g), int(10 + 30 * g), int(20 + 28 * g))
    return im


def a():
    """A: i 5 zeri che mangiano l'assegno"""
    im = bg_red(); d = ImageDraw.Draw(im)
    label(d, "SOCIAL SECURITY")
    otext(d, "5 ZEROS", P(250, True), 640, 270, stroke=12)
    for k in range(5):
        cx = 640 + (k - 2) * 150
        d.ellipse([cx - 58, 400, cx + 58, 516], fill=RED, outline=WHITE, width=7)
        d.ellipse([cx - 58, 400, cx + 58, 516], outline=BLK, width=3)
        d.text((cx, 459), "0", font=P(84, True), fill=WHITE, anchor="mm", stroke_width=2, stroke_fill=BLK)
    pill(d, "-$3,292 A YEAR", maxw=860)
    return im


def b():
    """B: stesso stipendio, due assegni diversi (Frank rosso / Mary verde)"""
    im = S.bg(); d = ImageDraw.Draw(im)
    label(d, "SAME WAGES", maxw=640)
    otext(d, "FRANK", P(118, True), 285, 205)
    otext(d, "MARY", P(118, True), 985, 205)
    otext(d, "VS", P(80, True), 640, 215, fill=YEL, stroke=7)
    otext(d, "$2,391", P(150, True), 285, 380, fill=(255, 120, 120), stroke=9)
    otext(d, "$2,665", P(150, True), 985, 380, fill=(120, 255, 150), stroke=9)
    S.T.cross(d, 285, 505, 44); S.T.check(d, 985, 505, 44)
    pill(d, "WHY $274 LESS?", maxw=900)
    return im


if __name__ == "__main__":
    for n, f in {"video5-A-5-zeri": a, "video5-B-frank-vs-mary": b}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
