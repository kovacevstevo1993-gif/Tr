"""Miniature video 6 (2027 Cola) nello stesso stile dei video 1-4: sfondo rosso/verde diagonale, etichetta bianca in alto,
numeri enormi bianchi con bordo nero, banda gialla in basso. 1280x720, Montserrat ExtraBold. Due layout per il test A/B."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageOps
import thumbs_video3_split as S
from thumbs_video3_split import P, label, pill, otext, big_num, YEL, BLK, WHITE
from thumbs_video4 import bg_flip, right_arrow

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "..", "miniature_video6"))
os.makedirs(OUT, exist_ok=True)


def a():
    """A: verde a sinistra ($72 della notizia) -> rosso a destra ($65 che resta)"""
    im = bg_flip(); d = ImageDraw.Draw(im)
    label(d, "2027 COLA")
    big_num(d, "$72", "", 255, 400, 250)
    big_num(d, "$65", "", 1020, 400, 250)
    right_arrow(d, 640, 290, 110, 100)
    d.text((255, 478), "THE NEWS SAYS", font=P(44), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((1020, 478), "YOU KEEP", font=P(52), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    pill(d, "WHERE DOES THE REST GO?", maxw=1000)
    return im


def b():
    """B: rosso a sinistra (3,5%) con triangolo, testo a destra su verde ($72 = $65), stesso schema del video 4"""
    im = S.bg(); d = ImageDraw.Draw(im)
    label(d, "2027 COLA", maxw=880)
    otext(d, "3.5%", P(190, True), 290, 290, stroke=11)
    S.T.warn(d, 290, 480, 46)
    d.text((960, 190), "$72 RAISE", font=P(88, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.text((960, 310), "= $65", font=P(130, True), fill=(255, 90, 90), anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.text((960, 410), "AFTER MEDICARE", font=P(52, True), fill=WHITE, anchor="mm", stroke_width=7, stroke_fill=BLK)
    pill(d, "THE NEWS WON'T TELL YOU", maxw=1000)
    return im


if __name__ == "__main__":
    for n, f in {"video6-A-72-diventa-65": a, "video6-B-3-5-percento": b}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
