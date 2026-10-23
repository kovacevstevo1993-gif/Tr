"""Miniature video lungo 8 (WALMART), 2 versioni diverse per il test A/B. 1280x720. Niente logo reale Walmart (solo testo).
Titolo video: Walmart Has No Senior Discount, But It Will Give You These 10 Things (If You Ask)
A = corsia di negozio sfocata, mano che regge lo scontrino: SENIOR DISCOUNT ... NOT FOUND, poi 4 voci vere con la spunta e "+6 MORE";
    testo "ASK FOR THESE 10" (curiosita: cosa c'e nello scontrino).
B = nonna sorpresa con flacone di farmaci, stella gialla "$4" (lista da 4 dollari, voce 9, vera: alcuni generici fino a 30 giorni),
    testo "WALMART'S $4 LIST" + fascia "+ 9 MORE THINGS TO ASK FOR".
uso: OUT=cartella python3 thumb_long8.py"""
import os, math, random
from PIL import Image, ImageDraw, ImageFilter
from thumb_long3 import *
from thumb_long5 import stamp_t, bg_green

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
PAPER = (252, 250, 243)
INK = (24, 30, 28)
OKG = (40, 160, 80)
BLUE_C = (40, 92, 160)


# ------------------------------------------------------------------ A: corsia + scontrino in mano
def aisle_bg():
    im = Image.new("RGB", (W, H), (226, 232, 240))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 150], fill=(70, 110, 170))
    for x in range(60, W, 230):
        d.rectangle([x, 22, x + 150, 40], fill=(250, 252, 255))
    d.rectangle([0, 590, W, H], fill=(214, 216, 220))
    rnd = random.Random(11)
    cols = [(214, 70, 60), (240, 190, 70), (60, 130, 190), (80, 170, 110), (250, 250, 246), (230, 120, 60), (150, 100, 180), (60, 180, 200)]
    for (y0, y1) in ((150, 300), (300, 450), (450, 590)):
        d.rectangle([0, y1 - 10, W, y1], fill=(170, 176, 186))
        x = 0
        while x < W:
            bw = rnd.randint(50, 110); bh = rnd.randint(int((y1 - y0) * .5), y1 - y0 - 16)
            d.rectangle([x + 3, y1 - 10 - bh, x + bw - 3, y1 - 10], fill=rnd.choice(cols), outline=(60, 60, 70), width=2)
            x += bw
    im = im.filter(ImageFilter.GaussianBlur(8))
    dark = Image.new("RGB", (W, H), (10, 20, 40))
    return Image.blend(im, dark, 0.38)


def receipt_long(w=520, h=640):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    d.rectangle([S(0), S(16), S(w), S(h - 16)], fill=PAPER)
    for k in range(0, w, 26):
        d.polygon([(S(k), S(18)), (S(k + 13), S(0)), (S(k + 26), S(18))], fill=PAPER)
        d.polygon([(S(k), S(h - 18)), (S(k + 13), S(h)), (S(k + 26), S(h - 18))], fill=PAPER)
    d.text((S(w / 2), S(64)), "RECEIPT", font=F(S(40), "Black"), fill=INK, anchor="mm")
    for k in range(30, w - 30, 18):
        d.line([(S(k), S(100)), (S(k + 9), S(100))], fill=(150, 150, 150), width=S(3))
    d.text((S(30), S(146)), "SENIOR DISCOUNT", font=F(S(34), "Black"), fill=INK, anchor="lm")
    items = [("PRICE MATCH", ""), ("$4 RX LIST", ""), ("50% OFF W+", ""), ("10¢ OFF GAS", "")]
    for i, (a, _) in enumerate(items):
        y = 290 + i * 66
        d.text((S(96), S(y)), a, font=F(S(36), "Black"), fill=INK, anchor="lm")
        d.ellipse([S(30), S(y - 24), S(78), S(y + 24)], fill=OKG)
        d.line([(S(42), S(y)), (S(52), S(y + 12)), (S(68), S(y - 12))], fill=PAPER, width=S(8), joint="curve")
    d.line([(S(30), S(546)), (S(w - 30), S(546))], fill=(150, 150, 150), width=S(3))
    d.text((S(w / 2), S(580)), "+ 6 MORE", font=F(S(42), "Black"), fill=OKG, anchor="mm")
    return done(lay, w, h)


def hand_holding(w=420, h=380):
    """mano anziana che regge dal basso (pollice davanti)"""
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    sk = (238, 190, 156); ol = (120, 70, 50)
    d.rounded_rectangle([S(70), S(150), S(330), S(h + 60)], radius=S(70), fill=sk, outline=ol, width=S(6))   # palmo e polso
    d.rounded_rectangle([S(110), S(h - 70), S(310), S(h + 60)], radius=S(30), fill=(70, 110, 160))            # manica
    for i, x in enumerate((92, 152, 212, 272)):
        d.rounded_rectangle([S(x), S(40 + abs(i - 1.5) * 18), S(x + 62), S(230)], radius=S(31), fill=sk, outline=ol, width=S(6))
    return done(lay, w, h)


def thumb_hand():
    lay = canvas(170, 230); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    d.rounded_rectangle([S(20), S(10), S(110), S(220)], radius=S(45), fill=(238, 190, 156), outline=(120, 70, 50), width=S(6))
    d.rounded_rectangle([S(36), S(20), S(94), S(70)], radius=S(22), fill=(250, 226, 210))
    return done(lay, 170, 230)


def thumb_a():
    im = aisle_bg()
    im = shadow_paste(im, hand_holding(400, 330), (850, 420), off=(10, 14), blur=14)
    rc = rot(receipt_long(440, 630), -5)
    im = shadow_paste(im, rc, (810, 18), off=(14, 18), blur=16)
    im = shadow_paste(im, rot(thumb_hand(), -14), (775, 540), off=(6, 8), blur=8)
    im = shadow_paste(im, stamp_t("NOT FOUND", 40, RED, -8), (900, 200), off=(6, 8), blur=8)
    im = text_stroke(im, (36, 140), "ASK FOR", 128, IVORY, stroke=13, anchor="l", rot_deg=2)
    im = text_stroke(im, (36, 320), "THESE 10", 140, YEL, stroke=14, anchor="l", rot_deg=2)
    band = Image.new("RGBA", (520, 106), (0, 0, 0, 0)); dd = ImageDraw.Draw(band)
    dd.rounded_rectangle([6, 6, 514, 100], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    dd.text((260, 55), "AT WALMART", font=F(58, "Black"), fill=IVORY, anchor="mm")
    im = shadow_paste(im, rot(band, -3), (50, 490))
    return im


# ------------------------------------------------------------------ B: nonna + flacone + stella $4
def starburst(r=230, n=20, fill=YEL):
    lay = canvas(2 * r + 20, 2 * r + 20); d = ImageDraw.Draw(lay); s = SS
    c = (r + 10) * s
    pts = []
    for i in range(2 * n):
        rr = (r if i % 2 == 0 else r * 0.78) * s
        a = math.pi * i / n
        pts.append((c + rr * math.cos(a), c + rr * math.sin(a)))
    d.polygon(pts, fill=fill, outline=BLK); d.line(pts + [pts[0]], fill=BLK, width=10 * s, joint="curve")
    d.text((c, c + 6 * s), "$4", font=F(int(r * 0.95) * s, "Black"), fill=RED, anchor="mm", stroke_width=6 * s, stroke_fill=BLK)
    return done(lay, 2 * r + 20, 2 * r + 20)


def pill_bottle(w=230, h=330):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    d.rounded_rectangle([S(20), S(4), S(w - 20), S(70)], radius=S(14), fill=(250, 250, 250), outline=BLK, width=S(7))
    for x in range(40, w - 30, 22):
        d.line([(S(x), S(14)), (S(x), S(60))], fill=(200, 200, 200), width=S(4))
    d.rounded_rectangle([S(10), S(62), S(w - 10), S(h - 6)], radius=S(26), fill=(236, 140, 50), outline=BLK, width=S(7))
    d.rounded_rectangle([S(26), S(120), S(w - 26), S(h - 50)], radius=S(10), fill=PAPER, outline=BLK, width=S(5))
    d.text((S(w / 2), S(170)), "Rx", font=F(S(56), "Black"), fill=RED, anchor="mm")
    for y in (220, 246):
        d.line([(S(46), S(y)), (S(w - 46), S(y))], fill=(150, 150, 150), width=S(6))
    return done(lay, w, h)


def grandma(w=560, h=640):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    sk = (240, 198, 166); ol = BLK
    # busto (cardigan)
    d.rounded_rectangle([S(60), S(450), S(w - 60), S(h + 80)], radius=S(120), fill=(150, 70, 90), outline=ol, width=S(8))
    d.polygon([(S(w / 2 - 70), S(452)), (S(w / 2), S(560)), (S(w / 2 + 70), S(452))], fill=(250, 246, 236), outline=ol)
    # collo
    d.rectangle([S(w / 2 - 50), S(380), S(w / 2 + 50), S(470)], fill=sk, outline=ol, width=S(6))
    # capelli dietro
    d.ellipse([S(90), S(40), S(w - 90), S(430)], fill=(232, 232, 236), outline=ol, width=S(8))
    d.ellipse([S(w / 2 - 70), S(0), S(w / 2 + 70), S(110)], fill=(232, 232, 236), outline=ol, width=S(8))
    # viso
    d.ellipse([S(130), S(100), S(w - 130), S(440)], fill=sk, outline=ol, width=S(8))
    # frangia
    d.chord([S(130), S(80), S(w - 130), S(300)], 190, 350, fill=(232, 232, 236), outline=ol, width=S(8))
    # occhi e occhiali
    for cx in (w / 2 - 70, w / 2 + 70):
        d.ellipse([S(cx - 52), S(220), S(cx + 52), S(318)], fill=(255, 255, 255), outline=ol, width=S(9))
        d.ellipse([S(cx - 18), S(250), S(cx + 18), S(288)], fill=BLK)
        d.arc([S(cx - 46), S(168), S(cx + 46), S(214)], 200, 340, fill=(140, 140, 150), width=S(9))
    d.line([(S(w / 2 - 18), S(266)), (S(w / 2 + 18), S(266))], fill=ol, width=S(8))
    # guance e bocca aperta (sorpresa)
    for cx in (w / 2 - 110, w / 2 + 110):
        d.ellipse([S(cx - 30), S(320), S(cx + 30), S(356)], fill=(240, 150, 140))
    d.ellipse([S(w / 2 - 40), S(340), S(w / 2 + 40), S(420)], fill=(150, 40, 50), outline=ol, width=S(7))
    d.ellipse([S(w / 2 - 22), S(384), S(w / 2 + 22), S(414)], fill=(230, 110, 110))
    return done(lay, w, h)


def thumb_b():
    im = bg_green(980, 380)
    d = ImageDraw.Draw(im)
    for i in range(16):
        a0 = 2 * math.pi * i / 16; a1 = a0 + math.pi / 16
        d.polygon([(980, 380), (980 + 1500 * math.cos(a0), 380 + 1500 * math.sin(a0)), (980 + 1500 * math.cos(a1), 380 + 1500 * math.sin(a1))], fill=(18, 70, 54))
    im = shadow_paste(im, grandma(520, 600), (690, 140), off=(10, 14), blur=14)
    im = shadow_paste(im, rot(pill_bottle(210, 296), 8), (1010, 410), off=(10, 14), blur=12)
    im = shadow_paste(im, rot(starburst(84), 10), (1040, 500), off=(6, 8), blur=8)
    im = text_stroke(im, (36, 120), "WALMART'S", 104, IVORY, stroke=12, anchor="l", rot_deg=2)
    im = text_stroke(im, (32, 300), "$4 LIST", 176, YEL, stroke=15, anchor="l", rot_deg=2)
    band = Image.new("RGBA", (640, 106), (0, 0, 0, 0)); dd = ImageDraw.Draw(band)
    dd.rounded_rectangle([6, 6, 634, 100], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    dd.text((320, 55), "+ 9 MORE TO ASK FOR", font=F(48, "Black"), fill=IVORY, anchor="mm")
    im = shadow_paste(im, rot(band, -3), (40, 500))
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b)):
        fn().save(f"{OUT}/walmart-miniatura-{name}.png"); print("ok", name)
