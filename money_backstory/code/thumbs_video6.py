"""Miniature video 6 (2027 Cola). Stile 'YouTube che funziona' (numero barrato -> numero vero, oggetti reali disegnati, testo enorme
giallo/bianco/verde/rosso con bordo nero, pill rossa con domanda) ma con l'identita' del canale: blu notte + oro, Montserrat ExtraBold.
Tutto disegnato a codice (gratis). 1280x720, disegno a 2x e ridotto."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageFilter
from thumbs_video3_split import P

W, H = 1280, 720
S = 2
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(__file__), "..", "miniature_video6"))
os.makedirs(OUT, exist_ok=True)
BLK, WHITE = (0, 0, 0), (255, 255, 255)
YEL, GOLD, RED, GREEN, NAVY = (255, 218, 40), (212, 172, 82), (230, 40, 40), (60, 220, 110), (12, 24, 52)


def sc(v): return int(v * S)


def canvas(cx, cy, glow=(40, 70, 130), rays=True):
    im = Image.new("RGB", (W * S, H * S), (6, 12, 28)); px = im.load()
    for y in range(0, H * S):
        for x in range(0, W * S):
            g = max(0.0, 1 - (((x / S - cx) / 760) ** 2 + ((y / S - cy) / 520) ** 2))
            px[x, y] = (int(6 + glow[0] * g * .6), int(12 + glow[1] * g * .6), int(28 + glow[2] * g * .7))
    if rays:
        ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
        for i in range(18):
            a0 = math.radians(i * 20); a1 = a0 + math.radians(7)
            R = 2400
            od.polygon([(sc(cx), sc(cy)), (sc(cx) + R * math.cos(a0), sc(cy) + R * math.sin(a0)), (sc(cx) + R * math.cos(a1), sc(cy) + R * math.sin(a1))], fill=(255, 255, 255, 14))
        im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    return im


def txt(d, xy, s, size, fill, sw=9, anchor="mm", black=True):
    d.text((sc(xy[0]), sc(xy[1])), s, font=P(int(size * S), black), fill=fill, anchor=anchor, stroke_width=sc(sw), stroke_fill=BLK)


def rrect(d, box, r, fill, outline=BLK, w=6):
    d.rounded_rectangle([sc(v) for v in box], radius=sc(r), fill=fill, outline=outline, width=sc(w))


def bill(w=330, h=150, rot=0, tint=(92, 170, 105), val="100", dark=(25, 85, 40)):
    """banconota da 100 dollari disegnata"""
    b = Image.new("RGBA", (sc(w), sc(h)), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.rounded_rectangle([0, 0, sc(w) - 1, sc(h) - 1], radius=sc(10), fill=tint, outline=(20, 60, 30), width=sc(5))
    d.rounded_rectangle([sc(12), sc(12), sc(w - 12), sc(h - 12)], radius=sc(6), outline=(190, 235, 190), width=sc(3))
    d.ellipse([sc(w / 2 - 38), sc(h / 2 - 38), sc(w / 2 + 38), sc(h / 2 + 38)], fill=(150, 205, 150), outline=(20, 60, 30), width=sc(4))
    d.text((sc(w / 2), sc(h / 2)), "$", font=P(sc(54), True), fill=dark, anchor="mm")
    for cx in (sc(40), sc(w - 40)):
        d.text((cx, sc(34)), val, font=P(sc(30), True), fill=dark, anchor="mm")
        d.text((cx, sc(h - 34)), val, font=P(sc(30), True), fill=dark, anchor="mm")
    return b.rotate(rot, expand=True, resample=Image.BICUBIC)


def shadow_paste(im, obj, x, y):
    sh = Image.new("RGBA", obj.size, (0, 0, 0, 0))
    sh.putalpha(obj.getchannel("A").point(lambda v: int(v * .55)))
    sh = sh.filter(ImageFilter.GaussianBlur(sc(10)))
    im.paste(sh, (sc(x) + sc(8), sc(y) + sc(14)), sh)
    im.paste(obj, (sc(x), sc(y)), obj)


def place(im, obj, cx, cy):
    """incolla obj centrato su (cx, cy) (coordinate 1x)"""
    shadow_paste(im, obj, cx - obj.width / (2 * S), cy - obj.height / (2 * S))


def tip_center(tipx, tipy, L, rot):
    """centro dell'immagine delle forbici tale che la punta cada su (tipx, tipy)"""
    a = math.radians(rot); r = .9 * L
    return tipx - r * math.cos(a), tipy + r * math.sin(a)


def cash_stack(im, x, y, n=5, w=330, h=150, spread=7):
    for i in range(n):
        shadow_paste(im, bill(w, h, rot=(i - n / 2) * spread * .4, tint=(80 + i * 4, 165 + i * 2, 100)), x + i * 6, y - i * 14)


def check_card(w=520, h=250, amount="$2,143.00"):
    c = Image.new("RGBA", (sc(w), sc(h)), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, sc(w) - 1, sc(h) - 1], radius=sc(16), fill=(247, 244, 232), outline=(40, 50, 80), width=sc(6))
    d.rectangle([sc(6), sc(6), sc(w - 6), sc(54)], fill=(24, 52, 120))
    d.text((sc(24), sc(30)), "SOCIAL SECURITY", font=P(sc(30), True), fill=WHITE, anchor="lm")
    d.text((sc(24), sc(84)), "PAY TO THE ORDER OF", font=P(sc(15), False), fill=(90, 90, 100), anchor="lm")
    d.line([sc(24), sc(140), sc(w * .62), sc(140)], fill=(90, 90, 100), width=sc(3))
    d.text((sc(w * .69), sc(108)), amount, font=P(sc(44), True), fill=(20, 20, 30), anchor="rm")
    return c


def scissors(L=300, open_deg=22, rot=0):
    """forbici: due meta' (lama + manico con anello) incrociate sul perno. Punta verso destra, poi ruotata di rot gradi."""
    sz = int(L * 1.7)
    s = Image.new("RGBA", (sc(sz), sc(sz)), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    cx, cy = sc(sz / 2 - L * .1), sc(sz / 2)

    def R(x, y, a):
        a = math.radians(a)
        return (cx + sc(x) * math.cos(a) - sc(y) * math.sin(a), cy + sc(x) * math.sin(a) + sc(y) * math.cos(a))

    for sign in (1, -1):
        a = -sign * open_deg
        blade = [R(-14, -sign * 17, a), R(L, -sign * 1, a), R(L, sign * 3, a), R(-14, sign * 3, a)]
        d.polygon(blade, fill=(232, 238, 246)); d.line(blade + [blade[0]], fill=BLK, width=sc(6), joint="curve")
        d.line([R(-6, 0, a), R(L * .06, sign * 0, a)], fill=(255, 255, 255), width=sc(3))
        hx, hy = R(-L * .5, sign * 6, a)
        d.line([R(-10, 0, a), (hx, hy)], fill=BLK, width=sc(34)); d.line([R(-10, 0, a), (hx, hy)], fill=(150, 160, 178), width=sc(22))
        r = sc(L * .15)
        d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=None, outline=BLK, width=sc(34))
        d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=None, outline=RED, width=sc(22))
    d.ellipse([cx - sc(13), cy - sc(13), cx + sc(13), cy + sc(13)], fill=(110, 120, 140), outline=BLK, width=sc(5))
    return s.rotate(rot, expand=True, resample=Image.BICUBIC)


def arrow_down(d, cx, y0, y1, col=RED, w=60):
    pts = [(cx - w / 2, y0), (cx + w / 2, y0), (cx + w / 2, y1 - 56), (cx + w, y1 - 56), (cx, y1), (cx - w, y1 - 56), (cx - w / 2, y1 - 56)]
    pts = [(sc(a), sc(b)) for a, b in pts]
    d.polygon(pts, fill=col); d.line(pts + [pts[0]], fill=BLK, width=sc(7), joint="curve")


def done(im):
    return im.resize((W, H), Image.LANCZOS)


def med_cross(d, cx, cy, r):
    d.ellipse([sc(cx - r), sc(cy - r), sc(cx + r), sc(cy + r)], fill=WHITE, outline=BLK, width=sc(7))
    t, l = r * .24, r * .62
    d.rectangle([sc(cx - t), sc(cy - l), sc(cx + t), sc(cy + l)], fill=RED); d.rectangle([sc(cx - l), sc(cy - t), sc(cx + l), sc(cy + t)], fill=RED)


def a():
    """A: schermo diviso verde/rosso: +$864 di aumento contro -$2.435 di Medicare ogni anno"""
    im = canvas(640, 360, rays=False)
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    od.polygon([(0, 0), (sc(690), 0), (sc(590), sc(H)), (0, sc(H))], fill=(20, 140, 60, 255))
    od.polygon([(sc(690), 0), (sc(W), 0), (sc(W), sc(H)), (sc(590), sc(H))], fill=(170, 24, 30, 255))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    for k in range(6):  # luce: sfumatura piu' chiara al centro di ogni meta'
        pass
    rrect(d, (440, 20, 840, 100), 22, YEL, BLK, 6)
    txt(d, (640, 62), "2027 COLA", 54, (15, 15, 15), 0)
    txt(d, (310, 195), "YOUR RAISE", 62, WHITE, 8)
    txt(d, (310, 325), "+$864", 150, WHITE, 10)
    txt(d, (975, 195), "MEDICARE", 62, WHITE, 8)
    txt(d, (975, 325), "-$2,435", 128, WHITE, 10)
    txt(d, (310, 435), "A YEAR", 54, WHITE, 7)
    txt(d, (975, 435), "A YEAR", 54, WHITE, 7)
    cash_stack(im, 120, 560, n=3, w=250, h=112)
    d = ImageDraw.Draw(im)
    med_cross(d, 975, 535, 60)
    d.ellipse([sc(580), sc(470), sc(676), sc(566)], fill=YEL, outline=BLK, width=sc(7))
    txt(d, (628, 519), "VS", 48, (15, 15, 15), 0)
    rrect(d, (700, 600, 1250, 700), 30, YEL, BLK, 6)
    txt(d, (975, 650), "WHO WINS?", 66, (15, 15, 15), 0)
    return done(im)


def b():
    """B: 1 dollaro su 10 se ne va a Medicare prima che arrivi: 9 banconote verdi + 1 rossa che esce"""
    im = canvas(640, 380, glow=(120, 40, 50))
    d = ImageDraw.Draw(im)
    txt(d, (640, 108), "EVERY $10 OF YOUR CHECK", 74, WHITE, 8)
    for k in range(9):
        r, c = divmod(k, 3)
        shadow_paste(im, bill(215, 98, rot=(-2, 1, -1)[c], tint=(80 + 4 * r, 170, 100), val="10"), 40 + c * 225, 190 + r * 122)
    red = bill(330, 148, rot=8, tint=(215, 50, 55), val="10", dark=(110, 15, 20))
    shadow_paste(im, red, 820, 215)
    d = ImageDraw.Draw(im)
    pts = [(715, 310), (775, 310), (775, 282), (825, 332), (775, 382), (775, 354), (715, 354)]
    d.polygon([(sc(a), sc(b2)) for a, b2 in pts], fill=YEL, outline=BLK); d.line([(sc(a), sc(b2)) for a, b2 in pts + [pts[0]]], fill=BLK, width=sc(6), joint="curve")
    txt(d, (990, 440), "-$1", 120, (255, 90, 90), 10)
    med_cross(d, 1165, 215, 44)
    rrect(d, (90, 575, 1190, 700), 34, RED, WHITE, 7)
    txt(d, (640, 637), "GOES TO MEDICARE FIRST", 82, WHITE, 6)
    rrect(d, (480, 12, 800, 62), 16, YEL, BLK, 5)
    txt(d, (640, 37), "2027 COLA", 34, (15, 15, 15), 0)
    return done(im)


if __name__ == "__main__":
    for n, f in {"video6-A-aumento-vs-medicare": a, "video6-B-1-dollaro-su-10": b}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
