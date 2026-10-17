"""Miniature video 10 'Medicare 2027 Changes: 5 New Rules Before Open Enrollment Ends (Dec 7)' - 2 prove con layout DIVERSI. 1280x720. Tutto a codice, niente volti.
Schema dai virali Medicare 2027 (vidIQ outliers 17/10): 'MEDICARE CHANGES 2027' enorme, 2027 rosso/giallo, calendario con data cerchiata, lista/busta, freccia rossa, una sola curiosita'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from thumbs_video3_split import P, bg, otext, label, pill, arrow, fit_font
import thumbs_video7 as T7
from thumbs_video8 import stamp

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video10"))
BLK, WHITE = (0, 0, 0), (255, 255, 255)
YEL, GOLD, RED, GRN = (254, 214, 67), (212, 172, 82), (226, 38, 38), (40, 180, 90)


def calendar(d, x0, y0, x1, y1, head, big):
    d.rounded_rectangle([x0 + 10, y0 + 12, x1 + 10, y1 + 12], radius=34, fill=(0, 0, 0))
    d.rounded_rectangle([x0, y0, x1, y1], radius=34, fill=(245, 245, 242), outline=BLK, width=6)
    hh = int((y1 - y0) * 0.27)
    d.rounded_rectangle([x0, y0, x1, y0 + hh], radius=34, fill=RED, outline=BLK, width=6)
    d.rectangle([x0 + 3, y0 + hh - 34, x1 - 3, y0 + hh - 3], fill=RED)
    d.line([x0, y0 + hh, x1, y0 + hh], fill=BLK, width=6)
    for rx in (x0 + (x1 - x0) // 4, x1 - (x1 - x0) // 4):
        d.rounded_rectangle([rx - 14, y0 - 30, rx + 14, y0 + 30], radius=12, fill=(60, 60, 60), outline=BLK, width=4)
    d.text(((x0 + x1) // 2, y0 + hh // 2 + 4), head, font=fit_font(d, head, x1 - x0 - 60, 70, True), fill=WHITE, anchor="mm", stroke_width=5, stroke_fill=BLK)
    cy = (y0 + hh + y1) // 2
    f = fit_font(d, big, x1 - x0 - 150, 190, True)
    d.text(((x0 + x1) // 2, cy), big, font=f, fill=(20, 20, 30), anchor="mm")
    bb = d.textbbox(((x0 + x1) // 2, cy), big, font=f, anchor="mm")
    d.ellipse([bb[0] - 45, bb[1] - 40, bb[2] + 45, bb[3] + 40], outline=RED, width=12)


def A():
    """A: blu notte + oro. 'MEDICARE' + '2027' giallo enorme + '5 NEW RULES' + fascia rossa '#5 IS A TRAP'; a destra calendario 'DEC 7' cerchiato + timbro DEADLINE."""
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    d.rounded_rectangle([14, 14, W - 14, H - 14], radius=30, outline=GOLD, width=8)
    d.text((350, 100), "MEDICARE", font=fit_font(d, "MEDICARE", 640, 130, True), fill=WHITE, anchor="mm", stroke_width=10, stroke_fill=BLK)
    d.text((350, 265), "2027", font=fit_font(d, "2027", 600, 250, True), fill=YEL, anchor="mm", stroke_width=14, stroke_fill=BLK)
    d.text((350, 440), "5 NEW RULES", font=fit_font(d, "5 NEW RULES", 640, 120, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.rounded_rectangle([45, 535, 655, 670], radius=26, fill=RED, outline=WHITE, width=7)
    d.text((350, 603), "#5 IS A TRAP", font=fit_font(d, "#5 IS A TRAP", 570, 100, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    calendar(d, 735, 150, 1215, 560, "LAST DAY", "DEC 7")
    stamp(im, 975, 625, "DEADLINE", -5, 62)
    return im.convert("RGB")


def B():
    """B: rosso/verde stile video 1-4. Stesso farmaco: '$959' (rosso, barrato, freccia giu') contro '$274' (verde, freccia su, 2027 PRICE) + 'BUT THERE'S A CATCH'."""
    im = bg(660, 600).convert("RGBA"); d = ImageDraw.Draw(im)
    label(d, "MEDICARE 2027", maxw=760)
    f = fit_font(d, "$959", 520, 240, True)
    otext(d, "$959", f, 330, 275, fill=WHITE, stroke=13)
    bb = d.textbbox((330, 275), "$959", font=f, anchor="mm")
    d.line([bb[0] - 20, bb[3] - 10, bb[2] + 20, bb[1] + 10], fill=BLK, width=34)
    d.line([bb[0] - 20, bb[3] - 10, bb[2] + 20, bb[1] + 10], fill=(255, 80, 80), width=20)
    otext(d, "$274", fit_font(d, "$274", 520, 240, True), 975, 275, fill=WHITE, stroke=13)
    arrow(d, 330, 380, False)
    d.rounded_rectangle([845, 375, 1105, 455], radius=22, fill=(20, 120, 55), outline=BLK, width=6)
    d.text((975, 416), "-71%", font=fit_font(d, "-71%", 220, 70, True), fill=WHITE, anchor="mm", stroke_width=5, stroke_fill=BLK)
    d.text((330, 515), "LIST PRICE", font=fit_font(d, "LIST PRICE", 520, 80, True), fill=YEL, anchor="mm", stroke_width=7, stroke_fill=BLK)
    d.text((975, 515), "2027 PRICE", font=fit_font(d, "2027 PRICE", 520, 80, True), fill=YEL, anchor="mm", stroke_width=7, stroke_fill=BLK)
    pill(d, "BUT THERE'S A CATCH", y0=575, h=120, maxw=1000)
    return im.convert("RGB")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-dec7-trap", A), ("B-959-vs-274", B)]:
        f().save(f"{OUT}/video10-{n}.png"); print("ok", n)
