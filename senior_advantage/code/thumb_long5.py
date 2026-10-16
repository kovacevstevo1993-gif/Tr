"""Miniature video lungo 5 (AEROPORTO), 3 versioni diverse per il test A/B. 1280x720. Niente loghi reali.
Titolo video: Flying Over 60? Airports and Airlines Owe You These 8 Things (If You Ask)
A = verde bosco, "8" gigante oro, carta d'imbarco con timbro rosso, "AIRLINES OWE YOU" / "IF YOU ASK".
B = nonno scioccato su raggi gialli, carta d'imbarco in mano, "THE AIRPORT RULE" / "NOBODY TELLS YOU".
C = carta d'imbarco con frase CENSURATA (barre nere) "SAY THIS BEFORE YOU FLY" (anello aperto: la frase che fa funzionare quasi tutto).
uso: OUT=cartella python3 thumb_long5.py"""
import os, math
from PIL import Image, ImageDraw, ImageFilter
from thumb_long3 import *
import thumb_long3 as T

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
PAPER = (250, 248, 238)
SKY = (66, 140, 200)


def plane(w=300, h=130, col=IVORY, ang=0):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def P(pts, **k): d.polygon([(x * w / 300 * s, y * h / 130 * s) for x, y in pts], **k)
    P([(10, 70), (60, 56), (230, 52), (285, 64), (292, 72), (230, 88), (60, 84)], fill=col, outline=BLK)
    P([(120, 58), (170, 4), (196, 4), (172, 58)], fill=col, outline=BLK)
    P([(120, 82), (170, 126), (196, 126), (172, 82)], fill=col, outline=BLK)
    P([(18, 66), (8, 22), (34, 22), (66, 58)], fill=col, outline=BLK)
    for k in range(8):
        d.ellipse([(210 - k * 20) * w / 300 * s, 62 * h / 130 * s, (220 - k * 20) * w / 300 * s, 72 * h / 130 * s], fill=SKY, outline=BLK, width=2 * s)
    return rot(done(lay, w, h), ang)


def boarding_pass(W0=620, H0=300, redact=False, stamp=None):
    w, h = 620, 300
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, (h - 6) * s], radius=22 * s, fill=PAPER, outline=BLK, width=8 * s)
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, 84 * s], radius=22 * s, fill=(36, 96, 150), outline=BLK, width=8 * s)
    d.rectangle([14 * s, 60 * s, (w - 14) * s, 80 * s], fill=(36, 96, 150))
    f = ImageFont.truetype(FP, 36 * s); f.set_variation_by_name("ExtraBold")
    d.text((34 * s, 46 * s), "BOARDING PASS", font=f, fill=IVORY, anchor="lm")
    d.line([((w - 190) * s, 100 * s), ((w - 190) * s, (h - 24) * s)], fill=(150, 150, 150), width=4 * s)
    for k in range(9):
        d.ellipse([(w - 190 - 6) * s, (104 + k * 22) * s, (w - 190 + 6) * s, (112 + k * 22) * s], fill=PAPER)
    fs = ImageFont.truetype(FP, 24 * s); fs.set_variation_by_name("Bold")
    d.text((34 * s, 124 * s), "PASSENGER", font=fs, fill=(110, 110, 110), anchor="lm")
    fb = ImageFont.truetype(FP, 32 * s); fb.set_variation_by_name("ExtraBold")
    d.text((34 * s, 162 * s), "SENIOR TRAVELER", font=fb, fill=(20, 20, 20), anchor="lm")
    if redact:
        for i, (x0, x1) in enumerate(((34, 300), (320, 420))):
            d.rounded_rectangle([x0 * s, 200 * s, x1 * s, 236 * s], radius=6 * s, fill=(10, 10, 10))
        d.rounded_rectangle([34 * s, 246 * s, 380 * s, 282 * s], radius=6 * s, fill=(10, 10, 10))
    else:
        d.text((34 * s, 222 * s), "GATE B7     SEAT 12A", font=fb, fill=(20, 20, 20), anchor="lm")
    for k in range(18):  # codice a barre
        d.rectangle([(w - 168 + k * 8) * s, 130 * s, (w - 168 + k * 8 + (3 if k % 3 else 5)) * s, 230 * s], fill=(20, 20, 20))
    img = done(lay, w, h)
    if stamp:
        img.alpha_composite(stamp, (w - stamp.width - 14, 4))
    return img.resize((W0, H0), Image.LANCZOS)


def stamp_t(s_, size=60, col=RED, ang=-10):
    f = F(size, "Black")
    bb = ImageDraw.Draw(Image.new("L", (4, 4))).textbbox((0, 0), s_, font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    W_, H_ = tw + 60, th + 50
    lay = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([5, 5, W_ - 5, H_ - 5], radius=14, fill=(255, 255, 255, 235), outline=col, width=8)
    d.text((W_ / 2, H_ / 2 - 2), s_, font=f, fill=col, anchor="mm")
    return rot(lay, ang)


def suitcase(w=240, h=250, col=(214, 90, 70)):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    d.rounded_rectangle([80 * s, 8 * s, (w - 80) * s, 60 * s], radius=14 * s, outline=BLK, width=10 * s)
    d.rounded_rectangle([6 * s, 40 * s, (w - 6) * s, (h - 20) * s], radius=24 * s, fill=col, outline=BLK, width=8 * s)
    for x in (70, 120, 170):
        d.rectangle([(x - 8) * s, 52 * s, (x + 8) * s, (h - 32) * s], fill=(0, 0, 0, 50))
    for x in (60, w - 60):
        d.ellipse([(x - 14) * s, (h - 24) * s, (x + 14) * s, (h + 2) * s], fill=BLK)
    return done(lay, w, h + 4)


def bg_green(cx=460, cy=330):
    im = Image.new("RGB", (W, H), GREEN_D); px = im.load()
    for y in range(H):
        for x in range(W):
            t = max(0, 1 - math.hypot(x - cx, y - cy) / 900)
            px[x, y] = (int(7 + 24 * t), int(38 + 62 * t), int(30 + 48 * t))
    return im


def thumb_a():
    im = bg_green()
    im = text_stroke(im, (30, 270), "8", 600, GOLD, stroke=16, anchor="l", w="Black")
    im = text_stroke(im, (330, 120), "AIRLINES", 128, IVORY, stroke=12, anchor="l")
    im = text_stroke(im, (330, 245), "OWE YOU", 128, YEL, stroke=12, anchor="l")
    im = text_stroke(im, (330, 345), "THESE THINGS", 62, IVORY, stroke=9, anchor="l")
    im = shadow_paste(im, plane(300, 130, IVORY, 8), (930, 320), off=(8, 12), blur=10)
    im = shadow_paste(im, rot(boarding_pass(440, 213, False, stamp=stamp_t("OVER 60", 40, RED, -8)), 5), (760, 470), off=(8, 12), blur=10)
    im = text_stroke(im, (40, 650), "IF YOU ASK", 96, (255, 80, 60), stroke=11, anchor="l", rot_deg=-2)
    return im


def thumb_b():
    im = Image.new("RGB", (W, H), YEL)
    rays(im, 940, 330, YEL, (255, 188, 20), 22)
    glow = Image.new("RGB", (W, H), (255, 240, 120)); m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([600, -40, 1280, 700], fill=170); m = m.filter(ImageFilter.GaussianBlur(90))
    im = Image.composite(glow, im, m)
    face = senior_shocked(620, 760)
    im = shadow_paste(im, face, (700, 40), off=(10, 14), blur=12)
    im = shadow_paste(im, rot(boarding_pass(380, 184, False), 8), (480, 440), off=(8, 12), blur=10)
    im = text_stroke(im, (36, 120), "THE AIRPORT RULE", 96, IVORY, stroke=12, anchor="l", rot_deg=3)
    im = text_stroke(im, (36, 250), "NOBODY", 150, (255, 60, 44), stroke=13, anchor="l", rot_deg=3)
    im = text_stroke(im, (36, 395), "TELLS YOU", 150, (255, 60, 44), stroke=13, anchor="l", rot_deg=3)
    band = Image.new("RGBA", (470, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.rounded_rectangle([6, 6, 464, 104], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    d.text((235, 57), "OVER 75? READ THIS", font=F(40), fill=YEL, anchor="mm")
    im = shadow_paste(im, rot(band, -2), (30, 590))
    return im


def thumb_c():
    im = Image.new("RGB", (W, H), (10, 20, 16)); px = im.load()
    for y in range(H):
        for x in range(W):
            t = max(0, 1 - math.hypot(x - 640, y - 340) / 800)
            px[x, y] = (int(10 + 20 * t), int(20 + 60 * t), int(16 + 44 * t))
    im = text_stroke(im, (640, 80), "SAY THIS BEFORE YOU FLY", 84, IVORY, stroke=11, anchor="m")
    im = shadow_paste(im, rot(boarding_pass(860, 416, True), -3), (210, 140), off=(10, 14), blur=12)
    im = text_stroke(im, (905, 460), "?", 170, YEL, stroke=14, anchor="m", w="Black")
    im = text_stroke(im, (640, 612), "THE 1 SENTENCE", 90, YEL, stroke=11, anchor="m")
    im = text_stroke(im, (640, 678), "MOST PEOPLE SAY IT TOO LATE", 36, IVORY, stroke=7, anchor="m")
    a = arrow(130, 90, RED, 90)
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b), ("c", thumb_c)):
        fn().save(f"{OUT}/aeroporto-miniatura-{name}.png"); print("ok", name)
