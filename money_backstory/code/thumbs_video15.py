"""Miniature video 15 'Vendere casa dopo i 65 anni' - 2 prove con layout DIVERSI. 1280x720, a codice, niente volti.
A (stile virali, giallo/rosso): 'SELLING YOUR HOME?' + casa con cartello SOLD + '$500,000 FREE' verde / '$146,000 TAXED' rosso + 'MEDICARE TRAP'.
B (navy+oro): barra divisa del guadagno ($646,000: escluso / tassato) + tessera Medicare '+$1,949' e calendario '2 YEARS LATER'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from thumbs_video3_split import P, fit_font
import thumbs_video7 as T7
from thumbs_video11 import *
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video15"))

def house(im, cx, cy, s, body=(236, 240, 245), roof=(212, 150, 40)):
    d = ImageDraw.Draw(im)
    d.polygon([(cx - 130 * s, cy), (cx, cy - 110 * s), (cx + 130 * s, cy)], fill=roof, outline=BLK)
    d.rectangle([cx - 105 * s, cy, cx + 105 * s, cy + 120 * s], fill=body, outline=BLK, width=5)
    d.rectangle([cx - 26 * s, cy + 36 * s, cx + 26 * s, cy + 120 * s], fill=roof, outline=BLK, width=4)
    d.rectangle([cx + 52 * s, cy + 26 * s, cx + 92 * s, cy + 66 * s], fill=(70, 130, 220), outline=BLK, width=4)
    d.rectangle([cx - 92 * s, cy + 26 * s, cx - 52 * s, cy + 66 * s], fill=(70, 130, 220), outline=BLK, width=4)

def card(im, box, text, fill, sub=None, size=70):
    shadow(im, box, 28); d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, radius=28, fill=fill, outline=WHITE, width=7)
    f = fit_font(d, text, box[2] - box[0] - 30, size, True)
    d.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2 - (16 if sub else 0)), text, font=f, fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    if sub: d.text(((box[0] + box[2]) / 2, box[3] - 40), sub, font=P(34, True), fill=YEL, anchor="mm", stroke_width=4, stroke_fill=BLK)

def A15():
    im = Image.new("RGBA", (W, H), (14, 14, 18, 255)); d = ImageDraw.Draw(im)
    for y in range(H):
        g = int(26 * (1 - y / H)); d.line([(0, y), (W, y)], fill=(18 + g, 14 + g // 2, 16 + g // 2))
    im = rays(im, 420, 430, 18, 26, (255, 200, 60)); d = ImageDraw.Draw(im)
    banner(im, "SELLING YOUR HOME?", (30, 24, 1020, 180), fill=YEL, fg=BLK, size=120, tilt=-1)
    shadow(im, (40, 240, 560, 650), 30); house(im, 270, 400, 1.55)
    d = ImageDraw.Draw(im)
    d.rectangle([472, 430, 486, 640], fill=(160, 170, 185), outline=BLK, width=3)
    banner(im, "SOLD", (385, 320, 590, 430), fill=RED, size=88, tilt=-4)
    card(im, (640, 235, 1240, 405), "$500,000 FREE", (28, 150, 80), "THE I R S EXCLUSION", 76)
    card(im, (640, 430, 1240, 600), "$146,000 TAXED", RED, "AND MORE...", 72)
    banner(im, "MEDICARE TRAP", (690, 618, 1240, 705), fill=WHITE, fg=BLK, size=62, tilt=1, outline=BLK)
    return vignette(im, 0.35).convert("RGB")

def B15():
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    im = rays(im, 640, 380, 20, 16, (255, 255, 255)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([12, 12, W - 12, H - 12], radius=30, outline=GOLD, width=9)
    d.text((640, 70), "YOUR HOME PROFIT AFTER 65", font=fit_font(d, "YOUR HOME PROFIT AFTER 65", 1100, 66, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.rounded_rectangle([60, 150, 1220, 300], radius=26, fill=(22, 36, 70), outline=GOLD, width=7)
    d.text((640, 205), "$646,000 GAIN", font=P(100, True), fill=YEL, anchor="mm", stroke_width=10, stroke_fill=BLK)
    d.text((640, 275), "SELLING PRICE - COSTS - BASIS", font=P(34, True), fill=WHITE, anchor="mm", stroke_width=4, stroke_fill=BLK)
    d.rounded_rectangle([60, 330, 930, 470], radius=22, fill=(28, 150, 80), outline=WHITE, width=7)
    d.text((495, 385), "$500,000", font=P(84, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.text((495, 442), "EXCLUDED", font=P(38, True), fill=WHITE, anchor="mm", stroke_width=5, stroke_fill=BLK)
    d.rounded_rectangle([940, 330, 1220, 470], radius=22, fill=RED, outline=WHITE, width=7)
    d.text((1080, 385), "$146,000", font=fit_font(d, "$146,000", 250, 60, True), fill=WHITE, anchor="mm", stroke_width=7, stroke_fill=BLK)
    d.text((1080, 442), "TAXED", font=P(38, True), fill=WHITE, anchor="mm", stroke_width=5, stroke_fill=BLK)
    d.rounded_rectangle([60, 510, 760, 690], radius=26, fill=(236, 240, 245), outline=GOLD, width=7)
    d.rectangle([60, 510, 760, 575], fill=RED); d.text((410, 543), "EXAMPLE: MEDICARE 2 YEARS LATER", font=fit_font(d, "EXAMPLE: MEDICARE 2 YEARS LATER", 640, 40, True), fill=WHITE, anchor="mm")
    d.text((410, 635), "+$1,949 A YEAR", font=fit_font(d, "+$1,949 A YEAR", 640, 88, True), fill=(14, 24, 50), anchor="mm")
    banner(im, "THE TRAP", (800, 540, 1220, 670), fill=RED, size=96, tilt=3)
    return im.convert("RGB")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-selling-your-home-146000-taxed", A15), ("B-646000-gain-medicare-trap", B15)]:
        f().save(f"{OUT}/video15-{n}.png"); print("ok", n)
