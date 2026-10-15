"""Miniature video 9 '2027 Social Security Changes: 5 New Numbers Just Made Official (3.6% COLA)' - 2 prove con layout DIVERSI. 1280x720. Tutto a codice, niente crediti, niente volti.
Schema dai virali sul COLA 2027 (curl 15/10): 2-4 parole enormi, anno 2027 giallo, timbro rosso, freccia/grafico, contorno nero."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from thumbs_video3_split import P, bg, otext, label, pill, arrow, fit_font
import thumbs_video7 as T7
from thumbs_video8 import stamp

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video9"))
BLK, WHITE = (0, 0, 0), (255, 255, 255)
YEL, GOLD, RED, GRN = (254, 214, 67), (212, 172, 82), (226, 38, 38), (40, 180, 90)


def chip(d, cx, cy, r, num, txt, known):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(18, 34, 66), outline=GRN if known else GOLD, width=8)
    f = fit_font(d, txt, int(r * 1.7), 100 if known else 110, True)
    d.text((cx, cy + 2), txt, font=f, fill=(120, 245, 160) if known else YEL, anchor="mm", stroke_width=5, stroke_fill=BLK)
    d.ellipse([cx - r - 6, cy - r - 6, cx - r + 40, cy - r + 40], fill=GOLD, outline=BLK, width=4)
    d.text((cx - r + 17, cy - r + 17), str(num), font=P(32, True), fill=BLK, anchor="mm")


def A():
    """A: blu notte + oro. '2027' giallo enorme + '5 NEW NUMBERS' + fascia rossa 'YOU KNOW 1 OF 5' + 5 cerchi (1 = +3.6% svelato, 4 con '?') + timbro OFFICIAL."""
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    d.rounded_rectangle([14, 14, W - 14, H - 14], radius=30, outline=GOLD, width=8)
    d.text((345, 165), "2027", font=fit_font(d, "2027", 620, 270, True), fill=YEL, anchor="mm", stroke_width=14, stroke_fill=BLK)
    d.text((345, 345), "5 NEW", font=fit_font(d, "5 NEW", 620, 120, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.text((345, 455), "NUMBERS", font=fit_font(d, "NUMBERS", 620, 120, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.rounded_rectangle([40, 535, 650, 670], radius=26, fill=RED, outline=WHITE, width=7)
    d.text((345, 603), "YOU KNOW 1", font=fit_font(d, "YOU KNOW 1", 570, 100, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.rounded_rectangle([700, 40, 1235, 682], radius=30, fill=(14, 28, 56), outline=GOLD, width=6)
    chip(d, 830, 250, 82, 1, "+3.6%", True)
    for i, (cx, cy) in enumerate([(1100, 250), (830, 425), (1100, 425), (965, 590)]):
        chip(d, cx, cy, 82, i + 2, "?", False)
    stamp(im, 965, 95, "OFFICIAL", -4, 50)
    return im.convert("RGB")


def B():
    """B: rosso/verde stile video 1-4. '+$75' (verde, freccia su, THE RAISE) contro '-$5,000' (rosso, freccia giu', HELD BACK)."""
    im = bg(660, 600).convert("RGBA"); d = ImageDraw.Draw(im)
    label(d, "SOCIAL SECURITY 2027", maxw=900)
    f1 = fit_font(d, "+$75", 520, 230, True)
    otext(d, "+$75", f1, 975, 270, fill=WHITE, stroke=13)
    f2 = fit_font(d, "-$5,000", 600, 230, True)
    otext(d, "-$5,000", f2, 330, 270, fill=WHITE, stroke=13)
    arrow(d, 975, 370, True); arrow(d, 330, 370, False)
    d.text((975, 510), "THE RAISE", font=fit_font(d, "THE RAISE", 520, 80, True), fill=YEL, anchor="mm", stroke_width=7, stroke_fill=BLK)
    d.text((330, 510), "HELD BACK", font=fit_font(d, "HELD BACK", 520, 80, True), fill=YEL, anchor="mm", stroke_width=7, stroke_fill=BLK)
    pill(d, "THE NUMBER FRANK MISSED", y0=570, h=120, maxw=1000)
    return im.convert("RGB")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-5-new-numbers", A), ("B-75-vs-5000", B)]:
        f().save(f"{OUT}/video9-{n}.png"); print("ok", n)
