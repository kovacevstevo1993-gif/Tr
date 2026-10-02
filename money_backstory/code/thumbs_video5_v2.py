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
    """A: assegno inclinato su sfondo giallo a raggi, '-$274' in stella rossa. Niente banner, niente banda."""
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        for x in range(W):
            ang = math.atan2(y - 360, x - 800); ray = (math.sin(ang * 14) > 0)
            g = max(0.0, 1 - (((x - 800) / 800) ** 2 + ((y - 360) / 500) ** 2))
            base = (255, 226, 70) if ray else (255, 204, 30)
            px[x, y] = tuple(int(c * (0.78 + 0.22 * g)) for c in base)
    d = ImageDraw.Draw(im)
    # assegno su layer ruotato
    L = Image.new("RGBA", (640, 420), (0, 0, 0, 0)); ld = ImageDraw.Draw(L)
    ld.rounded_rectangle([6, 6, 634, 414], radius=26, fill=(247, 249, 252), outline=BLK, width=8)
    ld.rounded_rectangle([6, 6, 634, 100], radius=26, fill=(60, 110, 200), outline=BLK, width=8)
    ld.rectangle([10, 70, 630, 100], fill=(60, 110, 200))
    ld.text((320, 54), "SOCIAL SECURITY", font=P(46, True), fill=WHITE, anchor="mm")
    ld.text((320, 180), "$2,665", font=P(110, True), fill=(120, 120, 130), anchor="mm")
    ld.line([120, 205, 520, 150], fill=RED, width=14)
    ld.text((320, 320), "$2,391", font=P(150, True), fill=(20, 20, 20), anchor="mm")
    L = L.rotate(-6, expand=True, resample=Image.BICUBIC)
    im.paste(L, (590, 120), L)
    d = ImageDraw.Draw(im)
    starburst(d, 280, 330, 285, 210, 14, RED, rot=0.1)
    d.text((280, 300), "-$274", font=P(150, True), fill=WHITE, anchor="mm", stroke_width=11, stroke_fill=BLK)
    d.text((280, 425), "EVERY MONTH", font=P(58, True), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=BLK)
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=10, outline=BLK, width=10)
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
    for n, f in {"video5-A2-assegno-giallo": A, "video5-B2-griglia-35-anni": B}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
