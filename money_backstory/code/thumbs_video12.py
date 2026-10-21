"""Miniature video 12 'New $6,000 Senior Tax Deduction' - 2 prove con layout DIVERSI. 1280x720, a codice, niente volti.
A (stile virali, rosso/giallo): '$6,000' enorme + modulo con timbro. B (stile canale navy+oro): grafico del fase-out $6,000 -> $0."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
from thumbs_video3_split import P, fit_font
import thumbs_video7 as T7
from thumbs_video11 import *
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video12"))

def A12():
    im = Image.new("RGBA", (W, H), (14, 14, 18, 255)); d = ImageDraw.Draw(im)
    for y in range(H):
        g = int(26 * (1 - y / H)); d.line([(0, y), (W, y)], fill=(18 + g, 14 + g // 2, 16 + g // 2))
    im = rays(im, 930, 360, 18, 26, (255, 200, 60)); d = ImageDraw.Draw(im)
    statement(im, 700, 170, 500, 450, -4, [("INCOME", "$140,000", False), ("DEDUCTION", "$2,100", True), ("LOST", "-$3,900", True)], head="SCHEDULE 1-A", stamp_txt="SHRINKS", stamp_col=RED)
    d = ImageDraw.Draw(im)
    banner(im, "$6,000", (30, 28, 660, 230), fill=YEL, fg=BLK, size=220, tilt=-1)
    banner(im, "SENIOR TAX", (30, 250, 640, 400), fill=RED, size=140, tilt=1)
    banner(im, "DEDUCTION", (30, 415, 640, 565), fill=RED, size=140, tilt=-1)
    banner(im, "WHO LOSES IT?", (30, 590, 700, 690), fill=WHITE, fg=BLK, size=90, outline=BLK)
    return vignette(im, 0.35).convert("RGB")

def B12():
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    im = rays(im, 640, 330, 20, 18, (255, 255, 255)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([12, 12, W - 12, H - 12], radius=30, outline=GOLD, width=9)
    d.text((640, 66), "THE NEW SENIOR DEDUCTION", font=fit_font(d, "THE NEW SENIOR DEDUCTION", 1120, 88, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    x0, x1, y0, y1 = 120, 1160, 150, 560; xa = x0 + (x1 - x0) * 0.22; xb = x0 + (x1 - x0) * 0.78
    d.rounded_rectangle([x0 - 20, y0 - 20, x1 + 20, y1 + 50], radius=24, fill=(8, 22, 46), outline=GOLD, width=5)
    d.polygon([(x0, y0 + 20), (xa, y0 + 20), (xb, y1), (x0, y1)], fill=(36, 190, 96))
    d.line([(x0, y0 + 20), (xa, y0 + 20), (xb, y1), (x1, y1)], fill=YEL, width=16, joint="curve")
    d.text((x0 + 30, y0 + 90), "$6,000", font=P(190, True), fill=YEL, anchor="lm", stroke_width=12, stroke_fill=BLK)
    d.text((x1 - 20, y1 - 62), "$0", font=P(150, True), fill=RED, anchor="rm", stroke_width=12, stroke_fill=WHITE)
    d.line([xb, y1 - 160, xb, y1 + 20], fill=WHITE, width=6)
    d.text((xb - 40, y1 - 215), "AT $175,000", font=P(52, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((xa, y1 + 30), "$75,000", font=P(40, True), fill=YEL, anchor="mm", stroke_width=5, stroke_fill=BLK)
    banner(im, "WHO GETS IT? WHO LOSES IT?", (260, 628, 1020, 698), fill=RED, size=62)
    return im.convert("RGB")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-6000-who-loses", A12), ("B-phaseout-chart", B12)]:
        f().save(f"{OUT}/video12-{n}.png"); print("ok", n)
