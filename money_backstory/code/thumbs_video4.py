"""Miniature video 4 (IRMAA, eta' 61) nello stile rosso/verde dei video 1-3. 1280x720, font Montserrat ExtraBold."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageOps
import thumbs_video3_split as S
from thumbs_video3_split import P, label, pill, otext, arrow, big_num, YEL, BLK, WHITE

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "..", "miniature_video4"))
os.makedirs(OUT, exist_ok=True)


def bg_flip(cut_top=690, cut_bot=585):
    """verde a sinistra (il dollaro innocuo), rosso a destra (il costo)"""
    return ImageOps.mirror(S.bg(W - cut_top, W - cut_bot))


def right_arrow(d, cx, cy, w=170, h=130):
    pts = [(cx - w / 2, cy - h * .22), (cx + w * .1, cy - h * .22), (cx + w * .1, cy - h / 2), (cx + w / 2, cy),
           (cx + w * .1, cy + h / 2), (cx + w * .1, cy + h * .22), (cx - w / 2, cy + h * .22)]
    d.polygon(pts, fill=YEL); d.line(pts + [pts[0]], fill=BLK, width=7, joint="curve")


def a():
    im = bg_flip(); d = ImageDraw.Draw(im)
    label(d, "MEDICARE")
    big_num(d, "$1", "", 235, 415, 320)
    big_num(d, "$974", "", 1000, 395, 200)
    right_arrow(d, 612, 285, 110, 100)
    d.text((235, 478), "ONE EXTRA DOLLAR", font=P(38), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((1000, 478), "EVERY YEAR", font=P(46), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    pill(d, "THE TRAP STARTS AT 61", maxw=960)
    return im


def b():
    im = S.bg(); d = ImageDraw.Draw(im)
    label(d, "MEDICARE SURCHARGE", maxw=880)
    otext(d, "61", P(360, True), 290, 290, stroke=11)
    S.T.warn(d, 290, 480, 46)
    d.text((1000, 190), "$1 MORE", font=P(112, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.text((1000, 310), "= $974", font=P(150, True), fill=(255, 90, 90), anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.text((1000, 410), "A YEAR", font=P(88, True), fill=WHITE, anchor="mm", stroke_width=7, stroke_fill=BLK)
    pill(d, "NOBODY WARNS YOU", maxw=900)
    return im


if __name__ == "__main__":
    for n, f in {"video4-A-1-dollaro-974": a, "video4-B-61-trappola": b}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
