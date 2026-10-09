"""Miniature video 7 'Can You Retire With $500,000?' - 3 prove con layout DIVERSI. 1280x720, Montserrat ExtraBold. Tutto a codice, niente crediti."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import thumbs_video3_split as S
from thumbs_video3_split import P, bg, otext, label, pill, arrow, fit_font

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video7"))
BLK, WHITE = (0, 0, 0), (255, 255, 255)
YEL, GOLD, RED, GRN = (254, 214, 67), (212, 172, 82), (226, 38, 38), (40, 180, 90)


def navy_bg():
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        for x in range(W):
            g = max(0.0, 1 - (((x - 900) / 760) ** 2 + ((y - 360) / 520) ** 2))
            px[x, y] = (int(8 + 18 * g), int(20 + 38 * g), int(44 + 62 * g))
    return im


def A():
    """A: rosso/verde (stile video 1-4). $500,000 -> $1,625 al mese."""
    im = bg(660, 600); d = ImageDraw.Draw(im)
    label(d, "RETIRE WITH $500,000?", maxw=900)
    f1 = fit_font(d, "$500,000", 490, 200, True); f2 = fit_font(d, "$1,625", 520, 230, True)
    otext(d, "$500,000", f1, 285, 300, stroke=10)
    d.text((285, 410), "SAVED", font=P(70, True), fill=(200, 255, 215), anchor="mm", stroke_width=7, stroke_fill=BLK)
    otext(d, "$1,625", f2, 960, 290, fill=WHITE, stroke=11)
    d.text((960, 415), "A MONTH?!", font=P(78, True), fill=YEL, anchor="mm", stroke_width=8, stroke_fill=BLK)
    pts = [(548, 285), (590, 285), (590, 262), (640, 305), (590, 348), (590, 325), (548, 325)]
    d.polygon(pts, fill=YEL); d.line(pts + [pts[0]], fill=BLK, width=6, joint="curve")
    pill(d, "THE REAL NUMBER", y0=545, h=130, maxw=860)
    return im


def B():
    """B: blu notte + oro, due barre (entrate vs spesa) e buco rosso di $1,423 al mese."""
    im = navy_bg(); d = ImageDraw.Draw(im)
    for yy in range(80, 650, 70): d.line([640, yy, 1240, yy], fill=(40, 70, 110), width=2)
    for txt, y, size, col in [("CAN YOU", 120, 118, WHITE), ("RETIRE", 245, 130, WHITE), ("WITH", 355, 90, GOLD), ("$500K?", 480, 150, (255, 80, 80))]:
        d.text((325, y), txt, font=P(size, True), fill=col, anchor="mm", stroke_width=9, stroke_fill=BLK)
    base = 655; hm = 470; hi = int(hm * 3493 / 5119)
    d.rounded_rectangle([690, base - hi, 890, base], radius=14, fill=GRN, outline=BLK, width=8)
    d.rounded_rectangle([960, base - hm, 1160, base], radius=14, fill=(224, 50, 50), outline=BLK, width=8)
    ytop = base - hm
    for x in range(690, 890, 28): d.line([x, ytop, x + 16, ytop], fill=(255, 140, 140), width=6)
    for y in range(ytop, base - hi, 12):
        d.line([690, y, 690, y + 6], fill=(255, 140, 140), width=6); d.line([890, y, 890, y + 6], fill=(255, 140, 140), width=6)
    d.rounded_rectangle([650, 80, 930, 180], radius=26, fill=(224, 50, 50), outline=WHITE, width=6)
    d.text((790, 130), "-$1,423", font=P(72, True), fill=WHITE, anchor="mm", stroke_width=3, stroke_fill=BLK)
    d.polygon([(760, 181), (820, 181), (790, ytop - 4)], fill=(224, 50, 50), outline=WHITE)
    d.text((790, base - hi + 62), "$3,493", font=P(58, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((1060, base - hm + 62), "$5,119", font=P(58, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((790, 695), "YOU GET", font=P(40, True), fill=(120, 255, 150), anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((1060, 695), "YOU SPEND", font=P(40, True), fill=(255, 130, 130), anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((1060, 40), "EVERY MONTH", font=P(34, True), fill=(200, 215, 235), anchor="mm", stroke_width=5, stroke_fill=BLK)
    return im


def C():
    """C: blu notte + oro, riga di 5 numeri con il 4 rosso '?': 'il numero 4 sorprende quasi tutti' (gancio del video)."""
    im = navy_bg(); d = ImageDraw.Draw(im)
    d.rounded_rectangle([14, 14, W - 14, H - 14], radius=30, outline=GOLD, width=8)
    fb = fit_font(d, "$500,000", 1000, 230, True)
    d.text((W / 2, 150), "$500,000", font=fb, fill=(246, 214, 140), anchor="mm", stroke_width=11, stroke_fill=BLK)
    d.text((W / 2, 285), "RETIREMENT: 5 NUMBERS", font=P(64, True), fill=WHITE, anchor="mm", stroke_width=7, stroke_fill=BLK)
    cw, gap = 190, 36; x0 = (W - (5 * cw + 4 * gap)) / 2
    for k in range(5):
        x = x0 + k * (cw + gap); hot = (k == 3); y0, y1 = 335, 545
        d.rounded_rectangle([x, y0, x + cw, y1], radius=28, fill=(224, 40, 40) if hot else (22, 40, 64), outline=(255, 255, 255) if hot else GOLD, width=8 if hot else 5)
        d.text((x + cw / 2, (y0 + y1) / 2 - (18 if hot else 0)), "?" if hot else str(k + 1), font=P(150 if hot else 130, True), fill=WHITE if hot else GOLD, anchor="mm", stroke_width=7, stroke_fill=BLK)
        if hot: d.text((x + cw / 2, y1 - 30), "4", font=P(46, True), fill=YEL, anchor="mm", stroke_width=5, stroke_fill=BLK)
    pill(d, "#4 SURPRISES ALMOST EVERYONE", y0=575, h=112, maxw=1100, fill=YEL)
    return im


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-1625-al-mese", A), ("B-buco-1423", B), ("C-il-numero-4", C)]:
        f().save(f"{OUT}/video7-{n}.png"); print("ok", n)
