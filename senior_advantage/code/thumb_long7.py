"""Miniature video lungo 7 (CASA-INVERNO), 3 versioni diverse per il test A/B. 1280x720. Niente loghi reali.
Titolo video: Over 60? 9 Kinds of Help You Can Get at Home This Winter (Most Never Ask)
A = notte d'inverno, casa con finestra accesa e neve, termometro 9, "OVER 60?" + "HELP AT HOME THIS WINTER" (scena del gancio).
B = griglia 3x3 di tessere numerate 1-9 con pittogrammi (l'elenco), "9 KINDS OF HELP" (promessa concreta).
C = frigorifero con biglietto attaccato (numero verificato Eldercare Locator), "PUT THIS ON YOUR FRIDGE" (anello aperto: la telefonata).
uso: OUT=cartella python3 thumb_long7.py"""
import os, math, random
from PIL import Image, ImageDraw, ImageFilter
from thumb_long3 import *
from thumb_long5 import stamp_t, bg_green, PAPER

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
NIGHT_T = (9, 22, 40); NIGHT_B = (24, 58, 92)
WARM = (255, 200, 90)


def bg_night():
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        t = y / H
        for x in range(W):
            px[x, y] = (int(NIGHT_T[0] + (NIGHT_B[0] - NIGHT_T[0]) * t), int(NIGHT_T[1] + (NIGHT_B[1] - NIGHT_T[1]) * t),
                        int(NIGHT_T[2] + (NIGHT_B[2] - NIGHT_T[2]) * t))
    d = ImageDraw.Draw(im); rnd = random.Random(7)
    for _ in range(90):
        x, y, r = rnd.randint(0, W), rnd.randint(0, H - 120), rnd.choice((2, 3, 3, 4, 5))
        d.ellipse([x - r, y - r, x + r, y + r], fill=(235, 242, 252))
    return im


def house(w=640, h=520):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    # neve a terra
    d.rounded_rectangle([S(0), S(h - 90), S(w), S(h)], radius=S(40), fill=(236, 244, 252))
    # muro
    d.rectangle([S(90), S(210), S(w - 90), S(h - 70)], fill=(176, 106, 78), outline=BLK, width=S(8))
    # tetto con neve
    d.polygon([(S(50), S(222)), (S(w / 2), S(60)), (S(w - 50), S(222))], fill=(78, 68, 84), outline=BLK)
    d.line([(S(50), S(222)), (S(w / 2), S(60)), (S(w - 50), S(222)), (S(50), S(222))], fill=BLK, width=S(8), joint="curve")
    d.polygon([(S(96), S(206)), (S(w / 2), S(84)), (S(w - 96), S(206)), (S(w - 130), S(206)), (S(w / 2), S(116)), (S(130), S(206))], fill=(244, 249, 255))
    # comignolo
    d.rectangle([S(w - 190), S(96), S(w - 150), S(176)], fill=(120, 70, 60), outline=BLK, width=S(6))
    d.rectangle([S(w - 198), S(86), S(w - 142), S(104)], fill=(244, 249, 255), outline=BLK, width=S(5))
    # finestra accesa
    d.rounded_rectangle([S(150), S(264), S(300), S(396)], radius=S(10), fill=WARM, outline=BLK, width=S(8))
    d.line([(S(225), S(264)), (S(225), S(396))], fill=BLK, width=S(6)); d.line([(S(150), S(330)), (S(300), S(330))], fill=BLK, width=S(6))
    # sagoma persona alla finestra
    d.ellipse([S(238), S(286), S(274), S(322)], fill=(120, 80, 60)); d.rounded_rectangle([S(230), S(322), S(282), S(396)], radius=S(14), fill=(120, 80, 60))
    # porta
    d.rounded_rectangle([S(w - 280), S(270), S(w - 170), S(h - 70)], radius=S(10), fill=(90, 52, 40), outline=BLK, width=S(8))
    d.ellipse([S(w - 196), S(352), S(w - 182), S(366)], fill=GOLD)
    return done(lay, w, h)


def thermometer(w=170, h=420, label="9"):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    d.rounded_rectangle([S(50), S(6), S(w - 50), S(h - 80)], radius=S(34), fill=IVORY, outline=BLK, width=S(8))
    d.ellipse([S(14), S(h - 130), S(w - 14), S(h - 6)], fill=(60, 140, 230), outline=BLK, width=S(8))
    d.rounded_rectangle([S(68), S(h - 170), S(w - 68), S(h - 90)], radius=S(8), fill=(60, 140, 230))
    d.rounded_rectangle([S(68), S(h - 190), S(w - 68), S(h - 140)], radius=S(8), fill=(60, 140, 230))
    for k in range(5):
        y = 50 + k * 42
        d.line([(S(w - 50), S(y)), (S(w - 30), S(y))], fill=BLK, width=S(6))
    return done(lay, w, h)


def thumb_a():
    im = bg_night()
    im = shadow_paste(im, house(660, 540), (610, 150), off=(12, 16), blur=16)
    im = shadow_paste(im, thermometer(150, 380), (1090, 200), off=(10, 14), blur=12)
    im = text_stroke(im, (1160, 160), "9°", 120, (110, 190, 255), stroke=12, anchor="m", w="Black")
    im = text_stroke(im, (40, 120), "OVER 60?", 190, (255, 60, 44), stroke=14, anchor="l", rot_deg=2)
    im = text_stroke(im, (44, 290), "HELP AT HOME", 100, IVORY, stroke=11, anchor="l", rot_deg=2)
    im = text_stroke(im, (44, 400), "THIS WINTER", 100, YEL, stroke=11, anchor="l", rot_deg=2)
    band = Image.new("RGBA", (560, 112), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.rounded_rectangle([6, 6, 554, 106], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    d.text((280, 58), "MOST NEVER ASK", font=F(52), fill=YEL, anchor="mm")
    im = shadow_paste(im, rot(band, -3), (40, 520))
    return im


# ---------- B: griglia 1-9 con pittogrammi
TILE_C = [(214, 70, 60), (60, 140, 200), (218, 150, 40), (210, 98, 60), (60, 160, 110),
          (120, 90, 190), (210, 80, 130), (50, 150, 170), (230, 110, 40)]


def pict(d, k, cx, cy, u):
    """pittogramma bianco k (1-9) centrato in (cx,cy), u = unita"""
    W_ = (255, 255, 255)
    if k == 1:  # allarme antifumo
        d.ellipse([cx - 1.0 * u, cy - 1.0 * u, cx + 1.0 * u, cy + 1.0 * u], fill=W_)
        d.ellipse([cx - 0.35 * u, cy - 0.35 * u, cx + 0.35 * u, cy + 0.35 * u], fill=TILE_C[0])
        for r in (1.35, 1.7):
            d.arc([cx - r * u, cy - r * u, cx + r * u, cy + r * u], 215, 325, fill=W_, width=int(0.14 * u))
    elif k == 2:  # maglietta (bucato)
        d.polygon([(cx - 1.0 * u, cy - 0.6 * u), (cx - 0.45 * u, cy - 1.0 * u), (cx + 0.45 * u, cy - 1.0 * u), (cx + 1.0 * u, cy - 0.6 * u),
                   (cx + 0.7 * u, cy - 0.1 * u), (cx + 0.5 * u, cy - 0.25 * u), (cx + 0.5 * u, cy + 1.0 * u), (cx - 0.5 * u, cy + 1.0 * u),
                   (cx - 0.5 * u, cy - 0.25 * u), (cx - 0.7 * u, cy - 0.1 * u)], fill=W_)
    elif k == 3:  # secchio
        d.polygon([(cx - 0.9 * u, cy - 0.5 * u), (cx + 0.9 * u, cy - 0.5 * u), (cx + 0.65 * u, cy + 1.0 * u), (cx - 0.65 * u, cy + 1.0 * u)], fill=W_)
        d.arc([cx - 0.8 * u, cy - 1.2 * u, cx + 0.8 * u, cy + 0.2 * u], 180, 360, fill=W_, width=int(0.14 * u))
    elif k == 4:  # piatto con cloche
        d.pieslice([cx - 1.0 * u, cy - 0.9 * u, cx + 1.0 * u, cy + 1.1 * u], 180, 360, fill=W_)
        d.rectangle([cx - 1.25 * u, cy + 0.12 * u, cx + 1.25 * u, cy + 0.3 * u], fill=W_)
        d.ellipse([cx - 0.14 * u, cy - 1.15 * u, cx + 0.14 * u, cy - 0.87 * u], fill=W_)
    elif k == 5:  # maniglione
        d.rounded_rectangle([cx - 1.1 * u, cy - 0.18 * u, cx + 1.1 * u, cy + 0.18 * u], radius=int(0.18 * u), fill=W_)
        for sx in (-0.85, 0.85):
            d.rectangle([cx + sx * u - 0.12 * u, cy - 0.18 * u, cx + sx * u + 0.12 * u, cy + 0.9 * u], fill=W_)
    elif k == 6:  # bilancia
        d.rectangle([cx - 0.09 * u, cy - 1.0 * u, cx + 0.09 * u, cy + 0.9 * u], fill=W_)
        d.rectangle([cx - 0.7 * u, cy + 0.8 * u, cx + 0.7 * u, cy + 1.0 * u], fill=W_)
        d.rectangle([cx - 1.1 * u, cy - 0.8 * u, cx + 1.1 * u, cy - 0.66 * u], fill=W_)
        for sx in (-1.0, 1.0):
            d.pieslice([cx + sx * u - 0.45 * u, cy - 0.15 * u, cx + sx * u + 0.45 * u, cy + 0.75 * u], 0, 180, fill=W_)
    elif k == 7:  # cuore
        d.ellipse([cx - 1.05 * u, cy - 0.9 * u, cx + 0.05 * u, cy + 0.2 * u], fill=W_)
        d.ellipse([cx - 0.05 * u, cy - 0.9 * u, cx + 1.05 * u, cy + 0.2 * u], fill=W_)
        d.polygon([(cx - 1.0 * u, cy - 0.1 * u), (cx + 1.0 * u, cy - 0.1 * u), (cx, cy + 1.1 * u)], fill=W_)
    elif k == 8:  # lucchetto/contatore: spina staccata -> fiamma barrata; qui lucchetto
        d.rounded_rectangle([cx - 0.85 * u, cy - 0.15 * u, cx + 0.85 * u, cy + 1.0 * u], radius=int(0.15 * u), fill=W_)
        d.arc([cx - 0.55 * u, cy - 1.0 * u, cx + 0.55 * u, cy + 0.3 * u], 180, 360, fill=W_, width=int(0.2 * u))
        d.ellipse([cx - 0.14 * u, cy + 0.25 * u, cx + 0.14 * u, cy + 0.53 * u], fill=TILE_C[7])
    elif k == 9:  # fiamma
        d.polygon([(cx, cy - 1.2 * u), (cx + 0.75 * u, cy - 0.1 * u), (cx + 0.9 * u, cy + 0.5 * u), (cx + 0.5 * u, cy + 1.05 * u),
                   (cx - 0.5 * u, cy + 1.05 * u), (cx - 0.9 * u, cy + 0.5 * u), (cx - 0.7 * u, cy - 0.1 * u), (cx - 0.25 * u, cy + 0.2 * u)], fill=W_)
        d.polygon([(cx, cy + 0.1 * u), (cx + 0.38 * u, cy + 0.65 * u), (cx, cy + 1.0 * u), (cx - 0.38 * u, cy + 0.65 * u)], fill=TILE_C[8])


def tile(k, size=190):
    lay = canvas(size, size); d = ImageDraw.Draw(lay); s = SS
    d.rounded_rectangle([6 * s, 6 * s, (size - 6) * s, (size - 6) * s], radius=26 * s, fill=TILE_C[k - 1], outline=BLK, width=8 * s)
    pict(d, k, size * s / 2 + 8 * s, size * s / 2 + 14 * s, size * s / 4.4)
    d.ellipse([6 * s, 6 * s, 62 * s, 62 * s], fill=BLK)
    d.text((34 * s, 36 * s), str(k), font=F(40 * s, "Black"), fill=IVORY, anchor="mm")
    return done(lay, size, size)


def thumb_b():
    im = bg_green(900, 330)
    size, gap, x0, y0 = 160, 12, 756, 108
    for k in range(1, 10):
        r, c = divmod(k - 1, 3)
        im = shadow_paste(im, tile(k, size), (x0 + c * (size + gap), y0 + r * (size + gap)), off=(6, 9), blur=8)
    im = text_stroke(im, (40, 100), "OVER 60?", 128, (255, 60, 44), stroke=12, anchor="l", rot_deg=2)
    im = text_stroke(im, (40, 238), "9 KINDS", 128, GOLD, stroke=12, anchor="l", rot_deg=2)
    im = text_stroke(im, (44, 352), "OF HELP AT HOME", 58, IVORY, stroke=10, anchor="l", rot_deg=2)
    im = shadow_paste(im, stamp_t("THIS WINTER", 56, RED, -4), (50, 420), off=(6, 8), blur=8)
    im = text_stroke(im, (44, 636), "MOST NEVER ASK", 78, YEL, stroke=11, anchor="l")
    return im


# ---------- C: frigorifero con biglietto
def fridge(w=520, h=700):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    d.rounded_rectangle([S(10), S(6), S(w - 10), S(h - 14)], radius=S(34), fill=(226, 232, 238), outline=BLK, width=S(9))
    d.line([(S(14), S(250)), (S(w - 14), S(250))], fill=BLK, width=S(8))
    d.rounded_rectangle([S(w - 78), S(70), S(w - 50), S(190)], radius=S(12), fill=(150, 156, 164), outline=BLK, width=S(6))
    d.rounded_rectangle([S(w - 78), S(300), S(w - 50), S(480)], radius=S(12), fill=(150, 156, 164), outline=BLK, width=S(6))
    return done(lay, w, h)


def note(w=470, h=400):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    d.rectangle([6 * s, 6 * s, (w - 6) * s, (h - 6) * s], fill=(255, 245, 160), outline=BLK, width=7 * s)
    d.text((w * s / 2, 64 * s), "ONE CALL", font=F(56 * s, "Black"), fill=(20, 20, 20), anchor="mm")
    d.line([(40 * s, 108 * s), ((w - 40) * s, 108 * s)], fill=(120, 110, 40), width=4 * s)
    d.text((w * s / 2, 180 * s), "1-800-", font=F(86 * s, "Black"), fill=(200, 30, 24), anchor="mm")
    d.text((w * s / 2, 276 * s), "677-1116", font=F(86 * s, "Black"), fill=(200, 30, 24), anchor="mm")
    d.text((w * s / 2, 352 * s), "ELDERCARE LOCATOR", font=F(30 * s, "Bold"), fill=(20, 20, 20), anchor="mm")
    return done(lay, w, h)


def magnet(r=34, col=RED):
    lay = canvas(r * 2 + 8, r * 2 + 8); d = ImageDraw.Draw(lay); s = SS
    d.ellipse([4 * s, 4 * s, (r * 2 + 4) * s, (r * 2 + 4) * s], fill=col, outline=BLK, width=6 * s)
    d.ellipse([(r - 12) * s, (r - 16) * s, (r + 2) * s, (r - 4) * s], fill=(255, 150, 140))
    return done(lay, r * 2 + 8, r * 2 + 8)


def thumb_c():
    im = Image.new("RGB", (W, H), (30, 96, 78))
    d = ImageDraw.Draw(im)
    for y in range(0, H, 90):  # pareti a righe
        d.rectangle([0, y, W, y + 44], fill=(36, 108, 88))
    im = shadow_paste(im, fridge(470, 700), (790, 30), off=(12, 16), blur=16)
    im = shadow_paste(im, rot(note(430, 400), 4), (810, 130), off=(8, 12), blur=10)
    im = shadow_paste(im, magnet(32), (985, 118), off=(4, 6), blur=5)
    im = text_stroke(im, (40, 100), "OVER 60?", 138, (255, 60, 44), stroke=13, anchor="l", rot_deg=2)
    im = text_stroke(im, (44, 258), "PUT THIS ON", 96, IVORY, stroke=11, anchor="l", rot_deg=2)
    im = text_stroke(im, (44, 380), "YOUR FRIDGE", 96, YEL, stroke=11, anchor="l", rot_deg=2)
    band = Image.new("RGBA", (680, 112), (0, 0, 0, 0)); dd = ImageDraw.Draw(band)
    dd.rounded_rectangle([6, 6, 674, 106], radius=24, fill=(12, 12, 12), outline=BLK, width=6)
    dd.text((340, 58), "HELP AT HOME THIS WINTER", font=F(40), fill=IVORY, anchor="mm")
    im = shadow_paste(im, rot(band, -3), (40, 520))
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b), ("c", thumb_c)):
        fn().save(f"{OUT}/casa-inverno-miniatura-{name}.png"); print("ok", name)
