"""Miniature video 14 'Medigap / Plan G' - 2 prove con layout DIVERSI. 1280x720, a codice, niente volti.
A (stile virali, rosso/giallo): 'DROP MEDIGAP?' + porta a senso unico (freccia avanti verde, indietro rossa barrata) + 'MAY NOT COME BACK'.
B (navy+oro): lettera G in cerchio oro + 'PLAN G' + il numero che non copre ($283) + calendario DEC 7."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
from thumbs_video3_split import P, fit_font
import thumbs_video7 as T7
from thumbs_video11 import *
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video14"))
BLUE = (40, 110, 230)

def arrow(d, x0, x1, y, col, w=26, head=70, back=False):
    if not back:
        d.polygon([(x0, y - w // 2), (x1 - head, y - w // 2), (x1 - head, y - head // 2 - 8), (x1, y), (x1 - head, y + head // 2 + 8), (x1 - head, y + w // 2), (x0, y + w // 2)], fill=col, outline=BLK)
    else:
        d.polygon([(x1, y - w // 2), (x0 + head, y - w // 2), (x0 + head, y - head // 2 - 8), (x0, y), (x0 + head, y + head // 2 + 8), (x0 + head, y + w // 2), (x1, y + w // 2)], fill=col, outline=BLK)

def card(im, box, text, fill, sub=None):
    shadow(im, box, 28); d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, radius=28, fill=fill, outline=WHITE, width=7)
    f = fit_font(d, text, box[2] - box[0] - 30, 70, True)
    d.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2 - (14 if sub else 0)), text, font=f, fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    if sub: d.text(((box[0] + box[2]) / 2, box[3] - 42), sub, font=P(34, True), fill=YEL, anchor="mm", stroke_width=4, stroke_fill=BLK)

def A14():
    im = Image.new("RGBA", (W, H), (14, 14, 18, 255)); d = ImageDraw.Draw(im)
    for y in range(H):
        g = int(26 * (1 - y / H)); d.line([(0, y), (W, y)], fill=(18 + g, 14 + g // 2, 16 + g // 2))
    im = rays(im, 640, 420, 18, 26, (255, 200, 60)); d = ImageDraw.Draw(im)
    banner(im, "DROP MEDIGAP?", (30, 26, 880, 190), fill=YEL, fg=BLK, size=150, tilt=-1)
    card(im, (50, 250, 440, 470), "MEDIGAP", (200, 150, 30), "YOUR PLAN")
    card(im, (840, 250, 1230, 470), "ADVANTAGE", BLUE, "NEW PLAN")
    d = ImageDraw.Draw(im)
    arrow(d, 470, 810, 320, (36, 190, 96))
    arrow(d, 470, 810, 410, RED, back=True)
    d.line([(600, 365), (680, 455)], fill=BLK, width=34); d.line([(680, 365), (600, 455)], fill=BLK, width=34)
    d.line([(602, 365), (678, 455)], fill=RED, width=20); d.line([(678, 365), (602, 455)], fill=RED, width=20)
    banner(im, "MAY NOT COME BACK", (50, 520, 800, 670), fill=RED, size=104, tilt=-2)
    banner(im, "BEFORE DEC 7", (880, 545, 1240, 655), fill=WHITE, fg=BLK, size=58, tilt=2, outline=BLK)
    return vignette(im, 0.35).convert("RGB")

def B14():
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    im = rays(im, 420, 380, 20, 18, (255, 255, 255)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([12, 12, W - 12, H - 12], radius=30, outline=GOLD, width=9)
    d.ellipse([60, 120, 500, 560], fill=GOLD, outline=WHITE, width=10)
    d.text((280, 335), "G", font=P(380, True), fill=(14, 24, 50), anchor="mm")
    d.text((280, 612), "PLAN G", font=P(88, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.text((880, 92), "WHAT IT DOES NOT COVER", font=fit_font(d, "WHAT IT DOES NOT COVER", 640, 52, True), fill=WHITE, anchor="mm", stroke_width=7, stroke_fill=BLK)
    d.rounded_rectangle([560, 150, 1230, 430], radius=30, fill=(22, 36, 70), outline=RED, width=9)
    d.text((895, 275), "$283", font=P(180, True), fill=YEL, anchor="mm", stroke_width=12, stroke_fill=BLK)
    d.text((895, 398), "PART B DEDUCTIBLE", font=P(42, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.rounded_rectangle([560, 465, 960, 650], radius=22, fill=(236, 240, 245), outline=GOLD, width=7)
    d.rectangle([560, 465, 960, 525], fill=RED); d.text((760, 495), "OPEN ENROLLMENT", font=fit_font(d, "OPEN ENROLLMENT", 360, 36, True), fill=WHITE, anchor="mm")
    d.text((760, 590), "ENDS DEC 7", font=fit_font(d, "ENDS DEC 7", 360, 70, True), fill=(14, 24, 50), anchor="mm")
    banner(im, "IN 2026", (990, 500, 1230, 620), fill=RED, size=80, tilt=3)
    return im.convert("RGB")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-drop-medigap-may-not-come-back", A14), ("B-plan-g-283", B14)]:
        f().save(f"{OUT}/video14-{n}.png"); print("ok", n)
