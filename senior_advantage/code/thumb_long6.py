"""Miniature video lungo 6 (AMTRAK), 2 versioni diverse per il test A/B. 1280x720. Niente loghi reali.
Titolo video: If You're Over 65, Amtrak Gives You These 10 Things (If You Ask)
A = raggi gialli + nonno scioccato (stile del canale), "OVER 65?" rosso, "AMTRAK GIVES YOU 10 THINGS", treno disegnato.
B = verde, biglietto del treno con riga CENSURATA + "?" (curiosita), "BEFORE YOU BOOK AMTRAK", "10" gigante, "OVER 65? ASK FOR THESE".
uso: OUT=cartella python3 thumb_long6.py"""
import os, math
from PIL import Image, ImageDraw, ImageFilter
from thumb_long3 import *
from thumb_long5 import stamp_t, bg_green, PAPER

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
TRAIN_C = (36, 96, 150)


def train(w=560, h=230):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return v * s
    # locomotiva con muso arrotondato
    d.rounded_rectangle([S(10), S(30), S(w - 10), S(h - 50)], radius=S(46), fill=IVORY, outline=BLK, width=S(8))
    d.rectangle([S(14), S(h - 112), S(w - 14), S(h - 88)], fill=TRAIN_C)
    d.rectangle([S(14), S(h - 86), S(w - 14), S(h - 76)], fill=(214, 52, 44))
    for k in range(5):
        x = 70 + k * 92
        d.rounded_rectangle([S(x), S(56), S(x + 64), S(108)], radius=S(10), fill=(150, 205, 232), outline=BLK, width=S(5))
    d.rounded_rectangle([S(w - 70), S(52), S(w - 26), S(124)], radius=S(12), fill=(150, 205, 232), outline=BLK, width=S(5))
    for x in (90, 190, w - 190, w - 90):
        d.ellipse([S(x - 28), S(h - 66), S(x + 28), S(h - 10)], fill=(40, 40, 40), outline=BLK, width=S(5))
        d.ellipse([S(x - 10), S(h - 48), S(x + 10), S(h - 28)], fill=(170, 170, 170))
    return done(lay, w, h)


def ticket(w0=760, h0=360, redact=True):
    w, h = 760, 360
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, (h - 6) * s], radius=26 * s, fill=PAPER, outline=BLK, width=8 * s)
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, 96 * s], radius=26 * s, fill=TRAIN_C, outline=BLK, width=8 * s)
    d.rectangle([14 * s, 70 * s, (w - 14) * s, 92 * s], fill=TRAIN_C)
    d.text((40 * s, 52 * s), "TRAIN TICKET", font=F(44 * s), fill=IVORY, anchor="lm")
    d.text((40 * s, 140 * s), "PASSENGER", font=F(26 * s, "Bold"), fill=(110, 110, 110), anchor="lm")
    d.text((40 * s, 184 * s), "SENIOR 65+", font=F(46 * s), fill=(20, 20, 20), anchor="lm")
    if redact:
        d.rounded_rectangle([40 * s, 226 * s, 470 * s, 266 * s], radius=6 * s, fill=(10, 10, 10))
        d.rounded_rectangle([40 * s, 280 * s, 360 * s, 320 * s], radius=6 * s, fill=(10, 10, 10))
    d.line([((w - 220) * s, 112 * s), ((w - 220) * s, (h - 24) * s)], fill=(150, 150, 150), width=4 * s)
    for k in range(20):
        d.rectangle([(w - 196 + k * 8) * s, 140 * s, (w - 196 + k * 8 + (3 if k % 3 else 5)) * s, 300 * s], fill=(20, 20, 20))
    return done(lay, w, h).resize((w0, h0), Image.LANCZOS)


def thumb_a():
    im = Image.new("RGB", (W, H), YEL)
    rays(im, 960, 320, YEL, (255, 188, 20), 22)
    glow = Image.new("RGB", (W, H), (255, 240, 120)); m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([620, -40, 1300, 700], fill=170); m = m.filter(ImageFilter.GaussianBlur(90))
    im = Image.composite(glow, im, m)
    face = senior_shocked(560, 690)
    im = shadow_paste(im, face, (760, 30), off=(10, 14), blur=12)
    im = shadow_paste(im, rot(train(460, 190), -3), (440, 515), off=(10, 14), blur=12)
    im = text_stroke(im, (36, 130), "OVER 65?", 170, (255, 60, 44), stroke=14, anchor="l", rot_deg=2)
    im = text_stroke(im, (40, 285), "AMTRAK GIVES YOU", 70, IVORY, stroke=10, anchor="l", rot_deg=2)
    im = text_stroke(im, (40, 420), "10 THINGS", 150, IVORY, stroke=14, anchor="l", rot_deg=2)
    band = Image.new("RGBA", (400, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.rounded_rectangle([6, 6, 394, 104], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    d.text((200, 57), "IF YOU ASK", font=F(56), fill=YEL, anchor="mm")
    im = shadow_paste(im, rot(band, -3), (40, 560))
    return im


def thumb_b():
    im = bg_green(640, 380)
    im = text_stroke(im, (640, 74), "BEFORE YOU BOOK AMTRAK", 82, IVORY, stroke=11, anchor="m")
    im = shadow_paste(im, rot(ticket(760, 360, True), -4), (60, 150), off=(10, 14), blur=12)
    im = text_stroke(im, (520, 440), "?", 190, (255, 60, 44), stroke=14, anchor="m", w="Black")
    im = text_stroke(im, (1060, 330), "10", 330, GOLD, stroke=16, anchor="m", w="Black")
    im = shadow_paste(im, stamp_t("THINGS", 52, RED, -8), (900, 470), off=(6, 8), blur=8)
    im = text_stroke(im, (640, 640), "OVER 65? ASK FOR THESE", 86, YEL, stroke=12, anchor="m")
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b)):
        fn().save(f"{OUT}/amtrak-miniatura-{name}.png"); print("ok", name)
