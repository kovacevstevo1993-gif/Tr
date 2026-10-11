"""Miniature video 8 '5 Bills You Don't Have To Pay After 65' - 2 prove con layout DIVERSI. 1280x720. Tutto a codice, niente crediti, niente volti."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from thumbs_video3_split import P, bg, otext, label, pill, fit_font
import thumbs_video7 as T7

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video8"))
BLK, WHITE = (0, 0, 0), (255, 255, 255)
YEL, GOLD, RED, GRN = (254, 214, 67), (212, 172, 82), (226, 38, 38), (40, 180, 90)


def bill(d, x, y, w, h, tilt, title, amount):
    """una bolletta/modulo inclinata: carta bianca, riga titolo, importo"""
    im = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0)); b = ImageDraw.Draw(im)
    b.rounded_rectangle([24, 24, w + 24, h + 24], radius=10, fill=(0, 0, 0, 110))
    b.rounded_rectangle([14, 14, w + 14, h + 14], radius=10, fill=(250, 248, 240), outline=BLK, width=5)
    b.rectangle([14, 14, w + 14, 62], fill=(30, 56, 100)); b.text((w / 2 + 14, 38), title, font=P(30, True), fill=WHITE, anchor="mm")
    for k in range(3): b.line([36, 96 + k * 26, w - 8, 96 + k * 26], fill=(200, 200, 205), width=5)
    b.text((w / 2 + 14, h - 10), amount, font=P(44, True), fill=(190, 30, 30), anchor="mm")
    return im.rotate(tilt, expand=True, resample=Image.BICUBIC)


def stamp(base, cx, cy, text, tilt, size=84):
    d0 = ImageDraw.Draw(base); f = P(size, True); tw = d0.textlength(text, font=f)
    st = Image.new("RGBA", (int(tw + 80), size + 34), (0, 0, 0, 0)); s = ImageDraw.Draw(st)
    s.rounded_rectangle([4, 4, tw + 76, size + 30], radius=14, outline=(214, 30, 30), width=8)
    s.text(((tw + 80) / 2, (size + 34) / 2), text, font=f, fill=(214, 30, 30), anchor="mm")
    st = st.rotate(tilt, expand=True, resample=Image.BICUBIC)
    base.paste(st, (int(cx - st.width / 2), int(cy - st.height / 2)), st)


def A():
    """A: blu notte + oro (schema dei 5 virali): '5 BILLS' enorme + 'YOU DON'T HAVE TO PAY' + fascia rossa 'AFTER 65' + pila di bollette col timbro EXEMPT."""
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    d.rounded_rectangle([14, 14, W - 14, H - 14], radius=30, outline=GOLD, width=8)
    f5 = P(250, True)
    d.text((300, 175), "5", font=f5, fill=(246, 214, 140), anchor="mm", stroke_width=13, stroke_fill=BLK)
    d.text((600, 190), "BILLS", font=fit_font(d, "BILLS", 440, 190, True), fill=(246, 214, 140), anchor="mm", stroke_width=12, stroke_fill=BLK)
    d.text((410, 345), "YOU DON'T", font=fit_font(d, "YOU DON'T", 700, 100, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.text((410, 440), "HAVE TO PAY", font=fit_font(d, "HAVE TO PAY", 700, 100, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    d.rounded_rectangle([40, 520, 800, 665], radius=26, fill=RED, outline=WHITE, width=7)
    d.text((420, 593), "AFTER 65", font=fit_font(d, "AFTER 65", 690, 125, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    for (x, y, t, ti, a) in [(865, 25, "INCOME TAX", 3, "$2,955"), (895, 245, "MEDICARE B", -3, "$4,870"), (865, 465, "PROPERTY TAX", 3, "BY STATE")]:
        b = bill(d, x, y, 330, 205, ti, t, a); im.paste(b, (x, y), b)
        stamp(im, x + 180, y + 128, "EXEMPT", -10, 44)
    return im.convert("RGB")


def B():
    """B (test): rosso/verde stile video 1-4 con il numero di Frank e Mary: $1,609 BACK."""
    im = bg(660, 600).convert("RGBA"); d = ImageDraw.Draw(im)
    label(d, "BILLS YOU DON'T HAVE TO PAY AFTER 65", maxw=1120)
    f1 = fit_font(d, "$1,609", 900, 300, True)
    otext(d, "$1,609", f1, 640, 270, fill=WHITE, stroke=14)
    d.text((640, 480), "BACK EVERY YEAR", font=fit_font(d, "BACK EVERY YEAR", 1000, 100, True), fill=YEL, anchor="mm", stroke_width=9, stroke_fill=BLK)
    pill(d, "SAME COUPLE. SAME INCOME.", y0=545, h=130, maxw=1000)
    return im.convert("RGB")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-5-bills-exempt", A), ("B-1609-back", B)]:
        f().save(f"{OUT}/video8-{n}.png"); print("ok", n)
