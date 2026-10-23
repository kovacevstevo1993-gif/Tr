"""Miniature video 13 'RMD at 73 + QCD' - 2 prove con layout DIVERSI. 1280x720, a codice, niente volti.
A (stile virali, rosso/giallo): 'RMD AT 73' + estratto 'Walter' con il -$2,089 e timbro. B (navy+oro): due barre della tassa $2,675 -> $586 con freccia."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
from thumbs_video3_split import P, fit_font
import thumbs_video7 as T7
from thumbs_video11 import *
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video13"))

def A13():
    im = Image.new("RGBA", (W, H), (14, 14, 18, 255)); d = ImageDraw.Draw(im)
    for y in range(H):
        g = int(26 * (1 - y / H)); d.line([(0, y), (W, y)], fill=(18 + g, 14 + g // 2, 16 + g // 2))
    im = rays(im, 930, 360, 18, 26, (255, 200, 60)); d = ImageDraw.Draw(im)
    statement(im, 700, 170, 500, 450, -4, [("RMD", "$32,520", False), ("TAX BEFORE", "$2,675", True), ("WITH QCD", "$586", False)], head="WALTER, 75", stamp_txt="-$2,089", stamp_col=RED)
    d = ImageDraw.Draw(im)
    banner(im, "RMD AT 73", (30, 28, 660, 230), fill=YEL, fg=BLK, size=190, tilt=-1)
    banner(im, "ONE MOVE", (30, 250, 640, 400), fill=RED, size=140, tilt=1)
    banner(im, "CUTS YOUR TAX", (30, 415, 640, 565), fill=RED, size=110, tilt=-1)
    banner(im, "THE IRS ALLOWS IT", (30, 590, 700, 690), fill=WHITE, fg=BLK, size=70, outline=BLK)
    return vignette(im, 0.35).convert("RGB")

def B13():
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    im = rays(im, 640, 330, 20, 18, (255, 255, 255)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([12, 12, W - 12, H - 12], radius=30, outline=GOLD, width=9)
    d.text((640, 66), "THE RMD TAX TRAP", font=fit_font(d, "THE RMD TAX TRAP", 1120, 92, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    base = 575; mh = 290
    for x0, val, txt, col in [(170, 2675, "$2,675", RED), (700, 586, "$586", GRN if 'GRN' in globals() else (36, 190, 96))]:
        hh = mh * val / 2675; d.rounded_rectangle([x0, base - hh, x0 + 330, base], radius=22, fill=col, outline=WHITE, width=6)
        d.text((x0 + 165, base - hh - 56), txt, font=P(104, True), fill=YEL, anchor="mm", stroke_width=10, stroke_fill=BLK)
    d.text((335, base + 40), "RMD ONLY", font=P(48, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((865, base + 40), "WITH A Q C D", font=P(48, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.polygon([(515, 400), (615, 400), (615, 365), (690, 430), (615, 495), (615, 460), (515, 460)], fill=YEL, outline=BLK)
    banner(im, "SAVE $2,089", (850, 170, 1240, 290), fill=RED, size=70)
    banner(im, "AGE 73+", (930, 320, 1230, 405), fill=YEL, fg=BLK, size=70)
    return im.convert("RGB")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-rmd-73-one-move", A13), ("B-tax-bars", B13)]:
        f().save(f"{OUT}/video13-{n}.png"); print("ok", n)
