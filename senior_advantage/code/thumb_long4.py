"""Miniature video lungo 4 (BOLLETTE), 3 versioni diverse per il test A/B. 1280x720. Niente loghi reali.
Modello: virali "5 Bills You Don't Have To Pay After 65" (numero gigante, pila di bollette, timbro) e nonno scioccato dei video che vanno.
A = verde bosco, "7" gigante oro, pila di bollette con timbro rosso PAYING FULL PRICE, BEFORE WINTER.
B = nonno scioccato su raggi gialli, bolletta in mano, "STILL PAYING FULL PRICE?!", fascia "7 BILLS YOU CAN LOWER".
C = griglia di 7 icone, la 7 accesa con "?" e "UP TO $10,000", "WAIT FOR #7".
uso: OUT=cartella python3 thumb_long4.py"""
import os, math
from PIL import Image, ImageDraw, ImageFilter
from thumb_long3 import *
import thumb_long3 as T

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
PAPER = (250, 248, 238)


def bill_paper(w=360, h=470, amount="$187.40", head="UTILITY BILL", due=True):
    W0, H0 = w, h; w, h = 360, 470
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, (h - 6) * s], radius=14 * s, fill=PAPER, outline=BLK, width=7 * s)
    d.rectangle([6 * s, 6 * s, (w - 6) * s, 86 * s], fill=(60, 110, 150), outline=BLK, width=7 * s)
    f = ImageFont.truetype(FP, 34 * s); f.set_variation_by_name("ExtraBold")
    d.text((w * s / 2, 48 * s), head, font=f, fill=IVORY, anchor="mm")
    for k in range(5):
        d.rounded_rectangle([40 * s, (120 + k * 38) * s, (w - 40 - (k % 2) * 70) * s, (136 + k * 38) * s], radius=6 * s, fill=(206, 206, 198))
    f2 = ImageFont.truetype(FP, 30 * s); f2.set_variation_by_name("Bold")
    d.text((40 * s, 336 * s), "AMOUNT DUE", font=f2, fill=(90, 90, 90), anchor="lm")
    f3 = ImageFont.truetype(FP, 84 * s); f3.set_variation_by_name("Black")
    d.text((w * s / 2, 400 * s), amount, font=f3, fill=RED, anchor="mm")
    return done(lay, w, h).resize((W0, H0), Image.LANCZOS)


def stamp_t(s_, size=70, col=RED, w=None, h=None, ang=-8):
    f = F(size, "Black")
    bb = ImageDraw.Draw(Image.new("L", (4, 4))).textbbox((0, 0), s_, font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    W_, H_ = tw + 70, th + 60
    lay = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([5, 5, W_ - 5, H_ - 5], radius=16, fill=(255, 255, 255, 235), outline=col, width=9)
    d.rounded_rectangle([17, 17, W_ - 17, H_ - 17], radius=10, outline=col, width=3)
    d.text((W_ / 2, H_ / 2 - 2), s_, font=f, fill=col, anchor="mm")
    return rot(lay, ang)


def icon_tile(kind, size=190, on=False, qmark=False):
    lay = canvas(size, size); d = ImageDraw.Draw(lay); s = SS
    fillc = GOLD if on else (24, 78, 62)
    d.rounded_rectangle([5 * s, 5 * s, (size - 5) * s, (size - 5) * s], radius=26 * s, fill=fillc, outline=BLK, width=7 * s)
    c = size / 2
    ink = GREEN_D if on else IVORY
    def P(pts, **k): d.polygon([(x * s, y * s) for x, y in pts], **k)
    if kind == "flame":
        P([(c, 28), (c + 40, 90), (c + 34, 140), (c, 160), (c - 34, 140), (c - 42, 92), (c - 14, 74)], fill=(238, 110, 40), outline=BLK)
        P([(c, 92), (c + 18, 130), (c, 152), (c - 18, 130)], fill=YEL)
    elif kind == "bolt":
        P([(c + 16, 24), (c - 38, 98), (c - 4, 98), (c - 18, 164), (c + 40, 80), (c + 4, 80)], fill=YEL, outline=BLK)
    elif kind == "phone":
        d.rounded_rectangle([(c - 30) * s, 26 * s, (c + 30) * s, 164 * s], radius=10 * s, fill=ink, outline=BLK, width=4 * s)
        d.rectangle([(c - 22) * s, 44 * s, (c + 22) * s, 140 * s], fill=GREEN_L if not on else (240, 230, 190))
    elif kind == "bag":
        d.rectangle([(c - 40) * s, 70 * s, (c + 40) * s, 160 * s], fill=(214, 170, 110), outline=BLK, width=4 * s)
        d.ellipse([(c - 22) * s, 36 * s, (c + 22) * s, 96 * s], outline=BLK, width=5 * s)
        d.ellipse([(c - 30) * s, 48 * s, (c) * s, 84 * s], fill=(220, 60, 50)); d.ellipse([(c) * s, 44 * s, (c + 30) * s, 82 * s], fill=(80, 170, 90))
    elif kind == "box":
        d.rectangle([(c - 46) * s, 70 * s, (c + 46) * s, 154 * s], fill=(214, 170, 110), outline=BLK, width=4 * s)
        d.rectangle([(c - 46) * s, 50 * s, (c + 46) * s, 76 * s], fill=(190, 140, 84), outline=BLK, width=4 * s)
        d.rectangle([(c - 12) * s, 76 * s, (c + 12) * s, 96 * s], fill=BLK)
    elif kind == "bus":
        d.rounded_rectangle([(c - 52) * s, 56 * s, (c + 52) * s, 140 * s], radius=14 * s, fill=(240, 180, 60), outline=BLK, width=4 * s)
        for k in range(3): d.rectangle([(c - 42 + k * 30) * s, 68 * s, (c - 22 + k * 30) * s, 94 * s], fill=(190, 225, 245), outline=BLK, width=2 * s)
        for x in (-30, 30): d.ellipse([(c + x - 12) * s, 130 * s, (c + x + 12) * s, 154 * s], fill=BLK)
    elif kind == "house":
        P([(c - 60, 98), (c, 40), (c + 60, 98)], fill=(214, 90, 80), outline=BLK)
        d.rectangle([(c - 44) * s, 98 * s, (c + 44) * s, 160 * s], fill=PAPER, outline=BLK, width=4 * s)
        d.rectangle([(c - 12) * s, 122 * s, (c + 12) * s, 160 * s], fill=(150, 98, 56), outline=BLK, width=3 * s)
    return done(lay, size, size)


def thumb_a():
    im = Image.new("RGB", (W, H), GREEN_D); px = im.load()
    for y in range(H):
        for x in range(W):
            t = max(0, 1 - math.hypot(x - 460, y - 330) / 900)
            px[x, y] = (int(7 + 24 * t), int(38 + 62 * t), int(30 + 48 * t))
    im = text_stroke(im, (40, 250), "7", 520, GOLD, stroke=16, anchor="l", w="Black")
    im = text_stroke(im, (330, 150), "BILLS", 150, IVORY, stroke=12, anchor="l")
    im = text_stroke(im, (330, 275), "YOU CAN", 78, IVORY, stroke=10, anchor="l")
    im = text_stroke(im, (330, 365), "LOWER", 100, (255, 214, 40), stroke=10, anchor="l")
    im = text_stroke(im, (40, 650), "BEFORE WINTER", 84, (255, 80, 60), stroke=11, anchor="l", rot_deg=-2)
    for i, (dx, dy, a, amt) in enumerate(((0, 50, 10, "$212"), (80, 10, 2, "$96"), (160, 40, -8, "$187"))):
        im = shadow_paste(im, rot(bill_paper(250, 330, amt, ("ELECTRIC", "PHONE", "HEATING")[i]), a), (870 + dx - 20, 40 + dy), off=(8, 12), blur=10)
    im = shadow_paste(im, stamp_t("PAYING FULL PRICE", 38, RED, ang=-8), (800, 520))
    return im


def thumb_b():
    im = Image.new("RGB", (W, H), YEL)
    rays(im, 940, 330, YEL, (255, 188, 20), 22)
    glow = Image.new("RGB", (W, H), (255, 240, 120)); m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([600, -40, 1280, 700], fill=170); m = m.filter(ImageFilter.GaussianBlur(90))
    im = Image.composite(glow, im, m)
    face = senior_shocked(620, 760)
    im = shadow_paste(im, face, (700, 40), off=(10, 14), blur=12)
    im = shadow_paste(im, rot(bill_paper(260, 340, "$212", "ELECTRIC"), 10), (630, 285), off=(8, 12), blur=10)
    im = text_stroke(im, (36, 120), "STILL PAYING", 112, IVORY, stroke=12, anchor="l", rot_deg=3)
    im = text_stroke(im, (36, 250), "FULL PRICE?!", 122, (255, 60, 44), stroke=12, anchor="l", rot_deg=3)
    band = Image.new("RGBA", (700, 120), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.rounded_rectangle([6, 6, 694, 114], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    d.text((350, 62), "7 BILLS YOU CAN LOWER", font=F(46), fill=YEL, anchor="mm")
    im = shadow_paste(im, rot(band, -2), (30, 590))
    return im


def thumb_c():
    im = Image.new("RGB", (W, H), (10, 20, 16)); px = im.load()
    for y in range(H):
        for x in range(W):
            t = max(0, 1 - math.hypot(x - 640, y - 300) / 800)
            px[x, y] = (int(10 + 20 * t), int(20 + 60 * t), int(16 + 44 * t))
    kinds = ["flame", "bolt", "phone", "bag", "box", "bus"]
    pos = [(60, 40), (270, 40), (480, 40), (60, 250), (270, 250), (480, 250)]
    for k, p in zip(kinds, pos):
        im = shadow_paste(im, icon_tile(k, 190), p, off=(5, 8), blur=7, alpha=120)
    big = icon_tile("house", 190, on=True).resize((330, 330), Image.LANCZOS)
    im = shadow_paste(im, big, (800, 30), off=(10, 14), blur=12)
    im = text_stroke(im, (965, 440), "#7", 150, (255, 60, 44), stroke=12, anchor="m", w="Black")
    im = text_stroke(im, (965, 560), "UP TO $10,000", 70, YEL, stroke=10, anchor="m")
    im = text_stroke(im, (40, 540), "WAIT FOR", 104, IVORY, stroke=12, anchor="l", rot_deg=-2)
    im = text_stroke(im, (40, 650), "NUMBER 7", 116, YEL, stroke=12, anchor="l", rot_deg=-2)
    a = arrow(150, 110, RED, 0)
    im = shadow_paste(im, a, (700, 160))
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b), ("c", thumb_c)):
        fn().save(f"{OUT}/bollette-miniatura-{name}.png"); print("ok", name)
