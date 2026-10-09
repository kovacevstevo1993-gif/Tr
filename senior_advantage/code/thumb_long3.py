"""Miniature video lungo 3 (Costco), 3 versioni diverse per il test A/B. 1280x720. Niente logo reale Costco: carta generica.
A = nonno scioccato su raggi gialli, tag "SENIOR DISCOUNT" barrato (curiosita: NO SENIOR DISCOUNT?!).
B = numero 14 gigante su verde bosco, "paghi 65 dollari e ne usi 1" (curiosita dal blocco 1).
C = magazzino sfocato, mano con carta, lista FREE (asciutta e chiara, promessa concreta).
uso: OUT=cartella python3 thumb_long3.py"""
import os, math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

W, H = 1280, 720
SS = 2
OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
FP = "/home/user/Tr/money_backstory/code/fonts/Montserrat.ttf"
GREEN_D = (7, 38, 30); GREEN_M = (14, 58, 45); GREEN_L = (26, 92, 71); IVORY = (246, 241, 229); GOLD = (244, 190, 70)
YEL = (255, 214, 40); RED = (226, 52, 44); BLK = (0, 0, 0); SAGE = (154, 200, 170); SKIN = (240, 196, 160); HAIR = (240, 240, 238)


def F(size, w="ExtraBold"):
    f = ImageFont.truetype(FP, int(size)); f.set_variation_by_name(w); return f


def shadow_paste(im, lay, xy, off=(8, 12), blur=10, alpha=150):
    base = im.convert("RGBA")
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0)); sh.paste(Image.new("RGBA", lay.size, (0, 0, 0, alpha)), (0, 0), lay.split()[3])
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(sh, (xy[0] + off[0], xy[1] + off[1])); base.alpha_composite(lay, xy)
    return base.convert("RGB")


def rot(lay, ang):
    return lay.rotate(ang, expand=True, resample=Image.BICUBIC)


def text_stroke(im, xy, s, size, fill, stroke=8, sc=BLK, anchor="mm", w="ExtraBold", rot_deg=0):
    f = F(size, w)
    bb = ImageDraw.Draw(Image.new("L", (4, 4))).textbbox((0, 0), s, font=f, stroke_width=stroke)
    tw, th = bb[2] - bb[0] + 40, bb[3] - bb[1] + 40
    lay = Image.new("RGBA", (tw, th), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.text((tw / 2, th / 2), s, font=f, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=sc)
    if rot_deg: lay = rot(lay, rot_deg)
    ax = {"l": 0, "m": .5, "r": 1}[anchor[0]]
    x = int(xy[0] - lay.width * ax); y = int(xy[1] - lay.height / 2)
    return shadow_paste(im, lay, (x, y), off=(5, 8), blur=7, alpha=130)


# ------------------------------------------------------------------ disegni (supersampled)
def canvas(w, h):
    return Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))


def done(lay, w, h):
    return lay.resize((w, h), Image.LANCZOS)


def senior_shocked(w=620, h=760):
    """nonno scioccato, busto, bocca aperta, sopracciglia alte, occhiali"""
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def E(b, **k): d.ellipse([v * s for v in b], **k)
    def R(b, r, **k): d.rounded_rectangle([v * s for v in b], radius=r * s, **k)
    # spalle / cardigan
    E((-60, 560, w + 60, h + 420), fill=(176, 120, 70), outline=BLK, width=6 * s)
    d.polygon([(210 * s, 580 * s), (310 * s, 700 * s), (410 * s, 580 * s)], fill=IVORY, outline=BLK)
    d.polygon([(230 * s, 600 * s), (310 * s, 690 * s), (390 * s, 600 * s), (310 * s, h * s)], fill=(150, 98, 56))
    for k in range(4):
        E((300, 640 + k * 34, 320, 660 + k * 34), fill=(236, 188, 108), outline=BLK, width=2 * s)
    # collo
    R((250, 480, 370, 620), 30, fill=(224, 176, 142), outline=BLK, width=6 * s)
    # orecchie
    E((92, 290, 150, 400), fill=SKIN, outline=BLK, width=6 * s); E((470, 290, 528, 400), fill=SKIN, outline=BLK, width=6 * s)
    # testa
    E((120, 130, 500, 560), fill=SKIN, outline=BLK, width=7 * s)
    # capelli bianchi ai lati e sopra
    E((112, 110, 330, 250), fill=HAIR, outline=BLK, width=6 * s); E((290, 110, 508, 250), fill=HAIR, outline=BLK, width=6 * s)
    E((96, 180, 168, 340), fill=HAIR, outline=BLK, width=6 * s); E((452, 180, 524, 340), fill=HAIR, outline=BLK, width=6 * s)
    E((190, 96, 430, 220), fill=HAIR, outline=BLK, width=6 * s)
    E((150, 150, 470, 270), fill=SKIN)                      # fronte
    # sopracciglia molto alte (shock)
    d.line([(172 * s, 222 * s), (230 * s, 190 * s), (286 * s, 214 * s)], fill=HAIR, width=18 * s, joint="curve")
    d.line([(334 * s, 214 * s), (390 * s, 190 * s), (448 * s, 222 * s)], fill=HAIR, width=18 * s, joint="curve")
    d.line([(172 * s, 222 * s), (230 * s, 190 * s), (286 * s, 214 * s)], fill=(190, 190, 188), width=6 * s, joint="curve")
    # occhi grandi
    for cx in (232, 388):
        E((cx - 52, 252, cx + 52, 360), fill=(255, 255, 255), outline=BLK, width=6 * s)
        E((cx - 22, 282, cx + 22, 330), fill=(60, 40, 30)); E((cx - 8, 292, cx + 6, 306), fill=(255, 255, 255))
    # occhiali
    for cx in (232, 388):
        E((cx - 70, 236, cx + 70, 376), outline=BLK, width=11 * s)
    d.line([(302 * s, 306 * s), (318 * s, 306 * s)], fill=BLK, width=11 * s)
    d.line([(162 * s, 300 * s), (116 * s, 290 * s)], fill=BLK, width=10 * s); d.line([(458 * s, 300 * s), (504 * s, 290 * s)], fill=BLK, width=10 * s)
    # naso
    d.polygon([(310 * s, 330 * s), (280 * s, 420 * s), (340 * s, 420 * s)], fill=(228, 168, 134), outline=BLK)
    E((278, 402, 342, 440), fill=(228, 168, 134), outline=BLK, width=4 * s)
    # guance
    E((170, 410, 250, 470), fill=(238, 140, 120)); E((370, 410, 450, 470), fill=(238, 140, 120))
    # bocca aperta
    E((236, 450, 384, 556), fill=(90, 20, 20), outline=BLK, width=7 * s)
    E((262, 506, 358, 560), fill=(214, 90, 90))
    R((254, 452, 366, 480), 8, fill=(250, 250, 248))
    return done(lay, w, h)


def hand_card(w=420, h=470, ang=0):
    """mano che regge la carta (disegnata, generica)"""
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def E(b, **k): d.ellipse([v * s for v in b], **k)
    def R(b, r, **k): d.rounded_rectangle([v * s for v in b], radius=r * s, **k)
    R((70, 130, 350, 400), 30, fill=SKIN, outline=BLK, width=6 * s)
    for i, x in enumerate((70, 150, 230, 310)):
        pass
    return done(lay, w, h)


def membership_card(w=470, h=300, text1="WAREHOUSE", text2="MEMBERSHIP", gold=True):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    base = (236, 188, 108) if gold else (230, 58, 52)
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, (h - 6) * s], radius=26 * s, fill=base, outline=BLK, width=7 * s)
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, 96 * s], radius=26 * s, fill=(190, 140, 66) if gold else (170, 30, 26), outline=BLK, width=7 * s)
    d.rectangle([14 * s, 60 * s, (w - 14) * s, 94 * s], fill=(190, 140, 66) if gold else (170, 30, 26))
    f = ImageFont.truetype(FP, 38 * s); f.set_variation_by_name("ExtraBold")
    d.text((36 * s, 52 * s), text1, font=f, fill=GREEN_D if gold else IVORY, anchor="lm")
    f2 = ImageFont.truetype(FP, 24 * s); f2.set_variation_by_name("Bold")
    d.text((36 * s, 128 * s), text2, font=f2, fill=GREEN_D if gold else IVORY, anchor="lm")
    d.rounded_rectangle([36 * s, 160 * s, 120 * s, 226 * s], radius=10 * s, fill=(210, 160, 80), outline=(150, 105, 40), width=3 * s)
    x = 36
    for bw in (5, 3, 7, 3, 4, 8, 3, 5, 3, 6, 4, 3, 7, 3, 5, 4, 8, 3, 4, 6, 3):
        d.rectangle([x * s, 246 * s, (x + bw) * s, 282 * s], fill=GREEN_D); x += bw + 4
    return done(lay, w, h)


def x_mark(size=300, wd=40):
    lay = canvas(size, size); d = ImageDraw.Draw(lay); s = SS
    d.line([(30 * s, 30 * s), ((size - 30) * s, (size - 30) * s)], fill=BLK, width=(wd + 16) * s)
    d.line([(30 * s, (size - 30) * s), ((size - 30) * s, 30 * s)], fill=BLK, width=(wd + 16) * s)
    d.line([(30 * s, 30 * s), ((size - 30) * s, (size - 30) * s)], fill=RED, width=wd * s)
    d.line([(30 * s, (size - 30) * s), ((size - 30) * s, 30 * s)], fill=RED, width=wd * s)
    return done(lay, size, size)


def arrow(w=260, h=200, color=RED, ang=0):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    pts = [(10, 70), (150, 70), (150, 20), (250, 100), (150, 180), (150, 130), (10, 130)]
    sx, sy = (w - 10) / 260.0, (h - 6) / 200.0
    pp = [(x * sx * s, y * sy * s) for x, y in pts]
    d.polygon(pp, fill=color, outline=BLK); d.line(pp + [pp[0]], fill=BLK, width=8 * s, joint="curve")
    return rot(done(lay, w, h), ang)


def check(size=90):
    lay = canvas(size, size); d = ImageDraw.Draw(lay); s = SS
    d.ellipse([4 * s, 4 * s, (size - 4) * s, (size - 4) * s], fill=(60, 190, 90), outline=BLK, width=6 * s)
    pts = [(size * .24 * s, size * .52 * s), (size * .43 * s, size * .70 * s), (size * .78 * s, size * .30 * s)]
    d.line(pts, fill=IVORY, width=int(size * .13) * s, joint="curve")
    return done(lay, size, size)


def rays(im, cx, cy, c1, c2, n=18):
    d = ImageDraw.Draw(im)
    for i in range(n):
        a0 = 2 * math.pi * i / n; a1 = a0 + math.pi / n
        R = 1800
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=c2)
    return im


# ------------------------------------------------------------------ VERSIONE A
def thumb_a():
    im = Image.new("RGB", (W, H), YEL)
    rays(im, 900, 330, YEL, (255, 188, 20), 22)
    glow = Image.new("RGB", (W, H), (255, 240, 120)); m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([560, -40, 1260, 700], fill=170); m = m.filter(ImageFilter.GaussianBlur(90))
    im = Image.composite(glow, im, m)
    face = senior_shocked(640, 780)
    im = shadow_paste(im, face, (640, 30), off=(10, 14), blur=12)
    # testo grande a sinistra
    im = text_stroke(im, (36, 128), "NO SENIOR", 124, IVORY, stroke=12, anchor="l", rot_deg=3)
    im = text_stroke(im, (36, 262), "DISCOUNT?!", 126, (255, 70, 50), stroke=12, anchor="l", rot_deg=3)
    # carta "SENIOR DISCOUNT" barrata, in basso a sinistra
    card = rot(membership_card(470, 300, "SENIOR", "DISCOUNT CARD"), -7)
    im = shadow_paste(im, card, (36, 390))
    im = shadow_paste(im, x_mark(300, 46), (122, 395), off=(4, 6), blur=6)
    # fascia in basso a destra
    band = Image.new("RGBA", (720, 120), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.rounded_rectangle([6, 6, 714, 114], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    d.text((360, 62), "BUT 14 THINGS SAVE YOU MONEY", font=F(38), fill=YEL, anchor="mm")
    im = shadow_paste(im, rot(band, -2), (520, 590))
    a = arrow(220, 160, RED, 15)
    im = shadow_paste(im, a, (520, 420))
    return im


# ------------------------------------------------------------------ VERSIONE B
def thumb_b():
    im = Image.new("RGB", (W, H), GREEN_D)
    px = im.load()
    for y in range(H):
        for x in range(W):
            t = max(0, 1 - math.hypot(x - 420, y - 360) / 900)
            px[x, y] = (int(7 + 24 * t), int(38 + 62 * t), int(30 + 48 * t))
    gx0, gy0, step, tw = 690, 50, 114, 102
    tile = Image.new("RGBA", (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(tile)
    for i in range(14):
        c, r = i % 5, i // 5
        x = gx0 + c * step; y = gy0 + r * step
        on = i == 0
        td.rounded_rectangle([x, y, x + tw, y + tw], radius=18, fill=GOLD if on else (24, 78, 62), outline=BLK, width=6)
        td.text((x + tw / 2, y + tw / 2 + 4), str(i + 1), font=F(56, "Black"), fill=GREEN_D if on else (80, 130, 110), anchor="mm")
    im = shadow_paste(im, tile, (0, 0), off=(6, 8), blur=8, alpha=120)
    im = shadow_paste(im, check(76), (gx0 + 66, gy0 - 22), off=(3, 5), blur=4)
    im = text_stroke(im, (50, 240), "14", 330, GOLD, stroke=14, anchor="l", w="Black")
    im = text_stroke(im, (50, 470), "COSTCO PERKS", 84, IVORY, stroke=10, anchor="l")
    im = text_stroke(im, (50, 565), "YOU PAY FOR", 78, IVORY, stroke=10, anchor="l")
    im = text_stroke(im, (50, 655), "BUT USE 1?", 78, (255, 70, 50), stroke=10, anchor="l")
    tag = Image.new("RGBA", (440, 210), (0, 0, 0, 0)); tdd = ImageDraw.Draw(tag)
    tdd.rounded_rectangle([8, 8, 432, 202], radius=30, fill=IVORY, outline=BLK, width=7)
    tdd.ellipse([30, 89, 62, 121], fill=GREEN_D, outline=BLK, width=4)
    tdd.text((246, 90), "$65", font=F(126, "Black"), fill=RED, anchor="mm")
    tdd.text((246, 168), "A YEAR", font=F(42), fill=GREEN_D, anchor="mm")
    im = shadow_paste(im, rot(tag, -5), (810, 460))
    a = arrow(140, 110, RED, 0)
    im = shadow_paste(im, a, (660, 590))
    return im


# ------------------------------------------------------------------ VERSIONE C
def warehouse_bg():
    im = Image.new("RGB", (W, H), (190, 186, 176))
    d = ImageDraw.Draw(im)
    # soffitto e pavimento
    d.rectangle([0, 0, W, 170], fill=(120, 124, 128)); d.rectangle([0, 560, W, H], fill=(206, 202, 192))
    rnd = random.Random(5)
    cols = [(214, 70, 60), (240, 190, 70), (60, 130, 190), (80, 160, 100), (236, 236, 230), (220, 120, 60), (140, 90, 170)]
    for row, (y0, y1) in enumerate(((170, 330), (330, 470), (470, 570))):
        d.rectangle([0, y1 - 8, W, y1], fill=(210, 120, 40))
        x = 0
        while x < W:
            bw = rnd.randint(70, 150); bh = rnd.randint(int((y1 - y0) * .55), y1 - y0 - 14)
            c = rnd.choice(cols)
            d.rectangle([x + 3, y1 - 8 - bh, x + bw - 3, y1 - 8], fill=c, outline=(40, 40, 40), width=2)
            d.rectangle([x + 10, y1 - 8 - bh + 12, x + bw - 10, y1 - 8 - bh + 30], fill=(250, 250, 250))
            x += bw
    # lampade
    for x in range(120, W, 260):
        d.rectangle([x, 20, x + 150, 38], fill=(255, 255, 240))
    # cartello generico
    d.rectangle([0, 0, W, 6], fill=(60, 60, 60))
    return im.filter(ImageFilter.GaussianBlur(7))


def thumb_c():
    im = warehouse_bg().convert("RGB")
    ov = Image.new("RGB", (W, H), (255, 252, 240)); m = Image.new("L", (W, H), 90)
    im = Image.composite(ov, im, m)
    pw = 560
    pan = Image.new("RGBA", (pw, 620), (0, 0, 0, 0)); d = ImageDraw.Draw(pan)
    d.rounded_rectangle([8, 8, pw - 8, 612], radius=40, fill=(255, 255, 255), outline=BLK, width=8)
    d.rounded_rectangle([8, 8, pw - 8, 130], radius=40, fill=RED, outline=BLK, width=8)
    d.rectangle([16, 80, pw - 16, 130], fill=RED)
    d.text((pw / 2, 70), "OVER 60? ASK FOR", font=F(46, "Black"), fill=IVORY, anchor="mm", stroke_width=4, stroke_fill=BLK)
    items = ["FREE HEARING TEST", "FREE TECH SUPPORT", "FREE 2ND CARD", "PHARMACY: NO CARD"]
    for i, t in enumerate(items):
        y = 190 + i * 104
        d.rounded_rectangle([36, y - 40, pw - 36, y + 40], radius=22, fill=(240, 250, 240), outline=BLK, width=4)
        d.text((120, y + 2), t, font=F(30, "ExtraBold"), fill=GREEN_D, anchor="lm")
    im = shadow_paste(im, pan, (690, 50), off=(10, 14), blur=12)
    for i in range(4):
        im = shadow_paste(im, check(64), (716, 50 + 190 + i * 104 - 34), off=(2, 3), blur=3)
    card = membership_card(500, 320, "MEMBER", "YOU ALREADY PAY FOR IT", gold=False)
    im = shadow_paste(im, rot(card, -8), (40, 340), off=(10, 14), blur=12)
    im = text_stroke(im, (40, 110), "NO DISCOUNT.", 72, IVORY, stroke=11, anchor="l", rot_deg=-2)
    im = text_stroke(im, (40, 235), "BUT THIS?", 104, YEL, stroke=12, anchor="l", rot_deg=-2)
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b), ("c", thumb_c)):
        im = fn()
        im.save(f"{OUT}/costco-miniatura-{name}.png")
        print("ok", name)
