"""Miniature video 5, 2a versione: due layout/stili davvero diversi per il test A/B. 1280x720."""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw
import thumbs_video3_split as S
from thumbs_video3_split import P

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "..", "miniature_video5"))
BLK, WHITE = (0, 0, 0), (255, 255, 255)
RED, YEL, GOLD = (226, 38, 38), (255, 214, 50), (212, 172, 82)


def starburst(d, cx, cy, r1, r2, n, fill, outline=BLK, ow=9, rot=0):
    pts = []
    for i in range(n * 2):
        a = rot + math.pi * i / n
        r = r1 if i % 2 == 0 else r2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=fill); d.line(pts + [pts[0]], fill=outline, width=ow, joint="curve")


def A():
    """A: confronto a barre su blu notte (identita' Money Backstory: navy, oro, rosso/verde). Nessun giallo a raggi."""
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        for x in range(W):
            g = max(0.0, 1 - (((x - 900) / 700) ** 2 + ((y - 380) / 480) ** 2))
            px[x, y] = (int(8 + 18 * g), int(20 + 38 * g), int(44 + 62 * g))
    d = ImageDraw.Draw(im)
    for yy in range(80, 640, 70):  # griglia sottile del grafico
        d.line([640, yy, 1240, yy], fill=(40, 70, 110), width=2)
    # testo a sinistra
    for txt, y, size, col in [("SAME", 140, 150, WHITE), ("WAGES", 280, 150, WHITE), ("DIFFERENT", 410, 82, GOLD), ("CHECK?", 520, 130, (255, 80, 80))]:
        d.text((330, y), txt, font=P(size, True), fill=col, anchor="mm", stroke_width=9, stroke_fill=BLK)
    # barre (scala reale: 2.391 / 2.665)
    base = 650; hm = 440; hf = int(hm * 2391 / 2665)
    d.rounded_rectangle([690, base - hm, 890, base], radius=14, fill=(40, 180, 90), outline=BLK, width=8)
    d.rounded_rectangle([960, base - hf, 1160, base], radius=14, fill=(224, 50, 50), outline=BLK, width=8)
    # pezzo mancante tratteggiato sopra Frank (scala reale) + callout rosso
    ytop = base - hm
    for x in range(960, 1160, 28):
        d.line([x, ytop, x + 16, ytop], fill=(255, 140, 140), width=6)
    for y in range(ytop, base - hf, 12):
        d.line([960, y, 960, y + 6], fill=(255, 140, 140), width=6); d.line([1160, y, 1160, y + 6], fill=(255, 140, 140), width=6)
    d.rounded_rectangle([930, 80, 1190, 175], radius=26, fill=(224, 50, 50), outline=WHITE, width=6)
    d.text((1060, 128), "-$274", font=P(76, True), fill=WHITE, anchor="mm", stroke_width=3, stroke_fill=BLK)
    d.polygon([(1030, 176), (1090, 176), (1060, ytop - 4)], fill=(224, 50, 50), outline=WHITE)
    d.text((790, base - hm + 62), "$2,665", font=P(56, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((1060, base - hf + 62), "$2,391", font=P(56, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((790, 688), "MARY", font=P(54, True), fill=(120, 255, 150), anchor="mm", stroke_width=7, stroke_fill=BLK)
    d.text((1060, 688), "FRANK", font=P(54, True), fill=(255, 130, 130), anchor="mm", stroke_width=7, stroke_fill=BLK)
    d.text((1060, 40), "EVERY MONTH", font=P(36, True), fill=(200, 215, 235), anchor="mm", stroke_width=5, stroke_fill=BLK)
    return im


def B():
    """B: griglia dei 35 anni stile canale (blu notte + oro), 5 caselle rosse con 0, cerchio rosso e freccia."""
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        for x in range(W):
            g = max(0.0, 1 - (((x - 640) / 760) ** 2 + ((y - 380) / 520) ** 2))
            px[x, y] = (int(8 + 16 * g), int(22 + 34 * g), int(46 + 52 * g))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([14, 14, W - 15, H - 15], radius=30, outline=GOLD, width=10)
    d.text((640, 92), "WORKED 30 YEARS?", font=P(100, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    cols, rows, tw, th, gap = 7, 5, 100, 82, 12
    x0 = 44; y0 = 168
    centers = []
    for i in range(35):
        r, c = divmod(i, cols); x = x0 + c * (tw + gap); y = y0 + r * (th + gap)
        zero = i >= 30
        d.rounded_rectangle([x, y, x + tw, y + th], radius=14, fill=RED if zero else GOLD, outline=WHITE if zero else BLK, width=5)
        d.text((x + tw / 2, y + th / 2 + 2), "0" if zero else str(i + 1), font=P(44, True), fill=WHITE if zero else (20, 28, 50), anchor="mm")
        if zero: centers.append((x + tw / 2, y + th / 2))
    xs = [c[0] for c in centers]; ys = [c[1] for c in centers]
    d.rounded_rectangle([min(xs) - tw / 2 - 14, ys[0] - th / 2 - 14, max(xs) + tw / 2 + 14, ys[0] + th / 2 + 14], radius=40, outline=(255, 70, 70), width=11)
    d.text((1040, 245), "5 YEARS", font=P(78, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.text((1040, 330), "COUNT AS", font=P(68, True), fill=GOLD, anchor="mm", stroke_width=7, stroke_fill=BLK)
    d.text((1040, 450), "ZERO", font=P(138, True), fill=(255, 80, 80), anchor="mm", stroke_width=10, stroke_fill=BLK)
    d.text((1040, 575), "-$3,292", font=P(84, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.text((1040, 640), "EVERY YEAR", font=P(44, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    return im


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in {"video5-A3-barre-stesso-stipendio": A, "video5-B2-griglia-35-anni": B}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
