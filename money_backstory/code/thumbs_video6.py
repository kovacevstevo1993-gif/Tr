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


def bill(w=330, h=150, rot=0, tint=(92, 170, 105)):
    """banconota da 100 dollari disegnata"""
    b = Image.new("RGBA", (sc(w), sc(h)), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.rounded_rectangle([0, 0, sc(w) - 1, sc(h) - 1], radius=sc(10), fill=tint, outline=(20, 60, 30), width=sc(5))
    d.rounded_rectangle([sc(12), sc(12), sc(w - 12), sc(h - 12)], radius=sc(6), outline=(190, 235, 190), width=sc(3))
    d.ellipse([sc(w / 2 - 38), sc(h / 2 - 38), sc(w / 2 + 38), sc(h / 2 + 38)], fill=(150, 205, 150), outline=(20, 60, 30), width=sc(4))
    d.text((sc(w / 2), sc(h / 2)), "$", font=P(sc(54), True), fill=(25, 85, 40), anchor="mm")
    for cx in (sc(40), sc(w - 40)):
        d.text((cx, sc(34)), "100", font=P(sc(30), True), fill=(25, 85, 40), anchor="mm")
        d.text((cx, sc(h - 34)), "100", font=P(sc(30), True), fill=(25, 85, 40), anchor="mm")
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


def a():
    """A: $72 barrato -> $65, pila di banconote con forbici, pill rossa 'WHERE'S THE REST?'"""
    im = canvas(420, 330, glow=(60, 50, 110))
    d = ImageDraw.Draw(im)
    txt(d, (350, 78), "2027 COLA", 104, YEL, 9)
    # $72 barrato
    txt(d, (260, 235), "$72", 190, WHITE, 11)
    d.line([sc(95), sc(300), sc(430), sc(170)], fill=RED, width=sc(24)); d.line([sc(95), sc(300), sc(430), sc(170)], fill=(255, 150, 150), width=sc(5))
    arrow_down(d, 520, 150, 330, w=48)
    txt(d, (330, 440), "$65", 230, GREEN, 12)
    # pila + forbici a destra
    cash_stack(im, 700, 330, n=5, w=420, h=190)
    sc_a = scissors(300, open_deg=20, rot=205); cxy = tip_center(770, 430, 300, 205); place(im, sc_a, *cxy)
    d = ImageDraw.Draw(im)
    rrect(d, (130, 570, 1150, 690), 36, RED, WHITE, 7)
    txt(d, (640, 632), "WHERE'S THE REST?", 90, WHITE, 6)
    rrect(d, (840, 36, 1250, 126), 22, YEL, BLK, 6)
    txt(d, (1045, 82), "-$6.60 MEDICARE", 38, (15, 15, 15), 0)
    return done(im)


def b():
    """B: assegno Social Security a cui le forbici tagliano via un pezzo da -$6.60"""
    im = canvas(640, 400, glow=(120, 40, 50))
    d = ImageDraw.Draw(im)
    txt(d, (640, 78), "YOUR 2027 RAISE", 104, WHITE, 10)
    cw, ch, cut = 700, 290, 520
    chk = check_card(cw, ch, "$2,143.00")
    left = chk.crop((0, 0, sc(cut), sc(ch)))
    dl = ImageDraw.Draw(left); dl.line([sc(cut) - 3, 0, sc(cut) - 3, sc(ch)], fill=(40, 50, 80), width=sc(6))
    shadow_paste(im, left.rotate(2, expand=True, resample=Image.BICUBIC), 60, 165)
    piece = Image.new("RGBA", (sc(cw - cut), sc(ch)), (0, 0, 0, 0)); dp = ImageDraw.Draw(piece)
    dp.rounded_rectangle([sc(-20), 0, sc(cw - cut) - 1, sc(ch) - 1], radius=sc(16), fill=(247, 244, 232), outline=(40, 50, 80), width=sc(6))
    dp.rectangle([sc(-20), sc(6), sc(cw - cut) - sc(6), sc(54)], fill=(24, 52, 120))
    dp.text((sc((cw - cut) / 2), sc(170)), "-$6.60", font=P(sc(50), True), fill=RED, anchor="mm", stroke_width=sc(2), stroke_fill=BLK)
    dp.text((sc((cw - cut) / 2), sc(220)), "MEDICARE", font=P(sc(24), True), fill=(20, 20, 30), anchor="mm")
    shadow_paste(im, piece.rotate(-14, expand=True, resample=Image.BICUBIC), 770, 160)
    # linea di taglio tratteggiata e forbici sul taglio
    d = ImageDraw.Draw(im)
    for yy in range(176, 470, 34):
        d.line([sc(594), sc(yy), sc(594), sc(yy + 18)], fill=WHITE, width=sc(6))
    sc_b = scissors(200, open_deg=16, rot=-90); place(im, sc_b, *tip_center(594, 440, 200, -90))
    d = ImageDraw.Draw(im)
    txt(d, (640, 575), "GETS CUT", 140, (255, 70, 70), 12)
    rrect(d, (150, 630, 1130, 714), 28, YEL, BLK, 6)
    txt(d, (640, 672), "BEFORE IT REACHES YOUR BANK", 52, (15, 15, 15), 0)
    return done(im)


if __name__ == "__main__":
    for n, f in {"video6-A-72-diventa-65": a, "video6-B-assegno-tagliato": b}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
