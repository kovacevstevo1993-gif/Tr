"""Video lungo 1 - blocco 1 (gancio). Durata totale dalla timeline dell'utente: 22 s + 4 f = 664 fotogrammi a 30 fps."""
import os, sys, math
os.environ["SA_W"], os.environ["SA_H"] = "1920", "1080"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] = "/tmp/sa_bin:" + os.environ["PATH"]
from engine import *

RED = (214, 108, 96)
OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/video_lungo_1")
os.makedirs(OUT, exist_ok=True)
TOTAL = 22 * 30 + 4  # 664 (timeline utente: 22 s + 4 f)
# frasi del blocco 1 e loro peso (caratteri): la durata TOTALE e' esatta, i tagli interni sono proporzionali
SENT = ["Most senior discounts in America start at fifty-five. Not sixty-five.",
        "And almost nobody tells you: not the cashier, not the manager, not the sign on the door.",
        "In the next few minutes you'll see twelve places that take money off your bill, and one of them costs eighty dollars once and lasts for the rest of your life."]
w = [len(s) for s in SENT]
F1 = round(TOTAL * w[0] / sum(w)); F2 = round(TOTAL * w[1] / sum(w)); F3 = TOTAL - F1 - F2
DUR = [F1, F2, F3]


def spaced(img, text, cx, cy, size=44, col=SAGE, gap=12, a=1.0):
    lay = new_layer(); rgb, mask = lay; d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    f = font(FONT_SANS, size); tw = d.textlength(text, font=f) + gap * (len(text) - 1)
    x = cx - (tw + 70) / 2
    for dr, c in ((d, col), (dm, 255)):
        dr.polygon([(x, cy), (x + 16, cy - 16), (x + 32, cy), (x + 16, cy + 16)], fill=c)
    x += 70
    for ch in text:
        for dr, c in ((d, col), (dm, 255)):
            dr.text((x, cy), ch, font=f, fill=c, anchor="lm")
        x += d.textlength(ch, font=f) + gap
    alpha_layer(img, lay, a)


def pop(img, draw_fn, scale, a=1.0, dx=0, dy=0, angle=0):
    """disegna su un livello, lo scala/ruota attorno al suo centro e lo incolla con opacita' a"""
    if a <= 0 or scale <= 0: return
    rgb, mask = new_layer(); draw_fn(rgb, mask)
    bb = mask.getbbox()
    if not bb: return
    c_rgb, c_m = rgb.crop(bb), mask.crop(bb)
    if angle:
        pad = 40
        big_rgb = Image.new("RGB", (c_rgb.width + 2 * pad, c_rgb.height + 2 * pad), (0, 0, 0)); big_rgb.paste(c_rgb, (pad, pad))
        big_m = Image.new("L", big_rgb.size, 0); big_m.paste(c_m, (pad, pad))
        c_rgb, c_m = big_rgb.rotate(angle, resample=Image.BICUBIC, expand=True), big_m.rotate(angle, resample=Image.BICUBIC, expand=True)
    nw, nh = max(1, int(c_rgb.width * scale)), max(1, int(c_rgb.height * scale))
    c_rgb, c_m = c_rgb.resize((nw, nh), Image.LANCZOS), c_m.resize((nw, nh), Image.LANCZOS)
    c_m = c_m.point(lambda v: int(v * min(1.0, a)))
    cx, cy = (bb[0] + bb[2]) / 2 + dx, (bb[1] + bb[3]) / 2 + dy
    img.paste(c_rgb, (int(cx - nw / 2), int(cy - nh / 2)), c_m)


def T(rgb, mask, xy, s, f, fill, anchor="mm"):
    ImageDraw.Draw(rgb).text(xy, s, font=f, fill=fill, anchor=anchor); ImageDraw.Draw(mask).text(xy, s, font=f, fill=255, anchor=anchor)


def cart(rgb, mask, cx, cy, s=1.0):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, IVORY), (dm, 255)):
        dr.line([(cx - 190 * s, cy - 150 * s), (cx - 130 * s, cy - 150 * s), (cx - 70 * s, cy + 60 * s), (cx + 150 * s, cy + 60 * s)], fill=c, width=int(14 * s))
        dr.polygon([(cx - 115 * s, cy - 110 * s), (cx + 190 * s, cy - 110 * s), (cx + 150 * s, cy + 30 * s), (cx - 75 * s, cy + 30 * s)], outline=c, width=int(12 * s))
        for x in (-30, 40, 110):
            dr.line([(cx + x * s, cy - 100 * s), (cx + (x - 8) * s, cy + 20 * s)], fill=c, width=int(7 * s))
        for x in (-30, 120):
            dr.ellipse([cx + x * s - 24 * s, cy + 100 * s - 24 * s, cx + x * s + 24 * s, cy + 100 * s + 24 * s], fill=c)
    for x in (-30, 120):
        d.ellipse([cx + x * s - 10 * s, cy + 100 * s - 10 * s, cx + x * s + 10 * s, cy + 100 * s + 10 * s], fill=GREEN_D)


# ------------------------------------------------------------------ SLIDE 1: START AT 55 / NOT 65
def s1(img, t):
    d = ImageDraw.Draw(img)
    spaced(img, "SENIOR DISCOUNTS", W // 2, 110, 46, a=ease(seg(t, 0, .5)))
    a = ease(seg(t, .2, .5)); shadow_text_a = a
    if a > 0:
        lay = new_layer(); T(lay[0], lay[1], (560 - 60 * (1 - a), 300), "START AT", font(FONT_SANS, 110), IVORY); alpha_layer(img, lay, a)
    p = ease_back(seg(t, .5, .7))
    pop(img, lambda r, m: T(r, m, (560, 610), "55", font(FONT_SERIF, 560), IVORY), p, a=ease(seg(t, .5, .25)))
    a = ease(seg(t, 1.5, .4))
    if a > 0:
        f2 = font(FONT_SANS, 150); lay = new_layer(); T(lay[0], lay[1], (560, 945 + 30 * (1 - a)), "NOT 65", f2, RED); alpha_layer(img, lay, a)
        tw = d.textlength("NOT 65", font=f2); g = ease(seg(t, 2.0, .5))
        d.line([560 - tw / 2 - 20, 950, 560 - tw / 2 - 20 + (tw + 40) * g, 950], fill=RED, width=14)
    bob = math.sin(t * 2.2) * 6
    pop(img, lambda r, m: banknote(r, m, 1450, 330, 560, 270, "SENIOR RATE", "ask before paying"), 1.0, a=ease(seg(t, 2.3, .5)), dx=300 * (1 - ease(seg(t, 2.3, .6))), dy=bob, angle=4)
    pop(img, lambda r, m: price_tag(r, m, 1690, 610, "55+", 340, 190), 1.0, a=ease(seg(t, 2.9, .4)), dy=-120 * (1 - ease_back(seg(t, 2.9, .6))) + bob * .8, angle=-9)
    pop(img, lambda r, m: cart(r, m, 1290, 700, 1.1), 1.0, a=ease(seg(t, 3.3, .5)), dx=-260 * (1 - ease(seg(t, 3.3, .7))))


# ------------------------------------------------------------------ SLIDE 2: nessuno te lo dice
def person(rgb, mask, cx, cy, s=1.0, tie=False, badge=None):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, SAGE), (dm, 255)):
        dr.ellipse([cx - 62 * s, cy - 150 * s, cx + 62 * s, cy - 26 * s], fill=c)
        dr.pieslice([cx - 125 * s, cy - 10 * s, cx + 125 * s, cy + 250 * s], 180, 360, fill=c)
    d.ellipse([cx - 62 * s, cy - 150 * s, cx + 62 * s, cy - 26 * s], outline=GREEN_D, width=4)
    if tie:
        d.polygon([(cx, cy + 6 * s), (cx - 20 * s, cy + 40 * s), (cx, cy + 120 * s), (cx + 20 * s, cy + 40 * s)], fill=RED)
    if badge:
        d.rounded_rectangle([cx + 38 * s, cy + 50 * s, cx + 118 * s, cy + 88 * s], radius=6, fill=IVORY)
        d.text((cx + 78 * s, cy + 69 * s), badge, font=font(FONT_SANS, int(15 * s)), fill=GREEN_D, anchor="mm")


def register(rgb, mask, cx, cy):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, GOLD), (dm, 255)):
        dr.rounded_rectangle([cx - 130, cy + 30, cx + 130, cy + 130], radius=14, fill=c)
    d.rounded_rectangle([cx - 100, cy - 30, cx + 40, cy + 40], radius=8, fill=GREEN_D, outline=IVORY, width=4)
    d.text((cx - 30, cy + 5), "$", font=font(FONT_SERIF, 46), fill=GOLD, anchor="mm")
    for i in range(3):
        for j in range(2):
            d.rounded_rectangle([cx + 60 + i * 24, cy + 50 + j * 24, cx + 78 + i * 24, cy + 68 + j * 24], radius=3, fill=GREEN_D)


def door(rgb, mask, cx, cy):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, (120, 80, 45)), (dm, 255)):
        dr.rounded_rectangle([cx - 90, cy - 170, cx + 90, cy + 190], radius=8, fill=c)
    d.rounded_rectangle([cx - 70, cy - 150, cx + 70, cy - 20], radius=6, outline=(90, 58, 30), width=5)
    d.rounded_rectangle([cx - 70, cy + 10, cx + 70, cy + 160], radius=6, outline=(90, 58, 30), width=5)
    d.ellipse([cx + 55, cy + 10, cx + 75, cy + 30], fill=GOLD)
    d.line([cx - 40, cy - 110, cx - 40, cy - 60], fill=IVORY, width=3)
    for dr, c in ((d, IVORY), (dm, 255)):
        dr.rounded_rectangle([cx - 62, cy - 85, cx + 62, cy - 30], radius=6, fill=c)
    d.text((cx, cy - 58), "OPEN", font=font(FONT_SANS, 30), fill=GREEN_D, anchor="mm")


def stamp_x(img, cx, cy, p):
    if p <= 0: return
    r = int(70 * ease_back(p)); a = ease(seg(p, 0, .3))
    lay = new_layer(); rgb, mask = lay; d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((d, RED), (dm, 255)):
        dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
        k = r * .45
        dr.line([(cx - k, cy - k), (cx + k, cy + k)], fill=(255, 255, 255) if dr is d else 0, width=max(2, int(r * .24)))
        dr.line([(cx - k, cy + k), (cx + k, cy - k)], fill=(255, 255, 255) if dr is d else 0, width=max(2, int(r * .24)))
    alpha_layer(img, lay, a)


def s2(img, t):
    d = ImageDraw.Draw(img)
    spaced(img, "AND ALMOST NOBODY TELLS YOU", W // 2, 105, 44, a=ease(seg(t, 0, .5)))
    cards = [(380, "THE CASHIER", lambda r, m, cx, cy: (person(r, m, cx, cy - 70, 0.95), register(r, m, cx + 20, cy + 95))),
             (960, "THE MANAGER", lambda r, m, cx, cy: person(r, m, cx, cy + 20, 1.1, tie=True, badge="MANAGER")),
             (1540, "THE SIGN ON THE DOOR", lambda r, m, cx, cy: door(r, m, cx, cy + 10))]
    starts = [.4, 2.0, 3.6]
    for (cx, label, icon), st in zip(cards, starts):
        a = ease(seg(t, st, .5)); off = 60 * (1 - ease_back(seg(t, st, .6)))
        if a <= 0: continue
        lay = new_layer(); rgb, mask = lay
        box = [cx - 270, 220 + off, cx + 270, 900 + off]
        dm = ImageDraw.Draw(mask); dm.rounded_rectangle(box, radius=34, fill=255)
        ImageDraw.Draw(rgb).rounded_rectangle(box, radius=34, fill=CARD, outline=SAGE_D, width=4)
        icon(rgb, mask, cx, 520 + off)
        T(rgb, mask, (cx, 840 + off), label, font(FONT_SANS, 42), IVORY)
        alpha_layer(img, lay, a)
        stamp_x(img, cx + 190, 300 + off, seg(t, st + 1.2, .5))
    if t > 5.0:
        a = ease(seg(t, 5.0, .5)); lay = new_layer(); T(lay[0], lay[1], (W // 2, 975), "NOT ONE OF THEM WILL TELL YOU", font(FONT_SANS, 50), GOLD); alpha_layer(img, lay, a)


# ------------------------------------------------------------------ SLIDE 3: 12 posti, $80 una volta
def tile_icon(kind, rgb, mask, cx, cy):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    box = [cx - 85, cy - 85, cx + 85, cy + 85]
    dm.rounded_rectangle(box, radius=26, fill=255)
    d.rounded_rectangle(box, radius=26, fill=CARD, outline=SAGE_D, width=4)
    P = lambda *a, **k: d.polygon(*a, **k); E_ = lambda *a, **k: d.ellipse(*a, **k); R = lambda *a, **k: d.rounded_rectangle(*a, **k)
    if kind == "plate":
        E_([cx - 62, cy + 8, cx + 62, cy + 44], fill=IVORY); d.pieslice([cx - 46, cy - 46, cx + 46, cy + 40], 180, 360, fill=(190, 196, 190)); E_([cx - 8, cy - 58, cx + 8, cy - 42], fill=(190, 196, 190))
    elif kind == "pharmacy":
        R([cx - 48, cy - 48, cx + 48, cy + 48], radius=14, fill=IVORY); d.rectangle([cx - 10, cy - 34, cx + 10, cy + 34], fill=RED); d.rectangle([cx - 34, cy - 10, cx + 34, cy + 10], fill=RED)
    elif kind == "shirt":
        P([(cx - 30, cy - 50), (cx - 70, cy - 20), (cx - 48, cy + 6), (cx - 36, cy - 6), (cx - 36, cy + 52), (cx + 36, cy + 52), (cx + 36, cy - 6), (cx + 48, cy + 6), (cx + 70, cy - 20), (cx + 30, cy - 50), (cx, cy - 30)], fill=SAGE)
    elif kind == "tag":
        P([(cx - 60, cy), (cx - 20, cy - 46), (cx + 60, cy - 46), (cx + 60, cy + 46), (cx - 20, cy + 46)], fill=GOLD); E_([cx - 40, cy - 8, cx - 24, cy + 8], fill=GREEN_D); d.text((cx + 18, cy), "%", font=font(FONT_SANS, 44), fill=GREEN_D, anchor="mm")
    elif kind == "hanger":
        d.arc([cx - 14, cy - 58, cx + 14, cy - 28], 180, 450, fill=IVORY, width=7); d.line([(cx, cy - 30), (cx, cy - 14)], fill=IVORY, width=7); P([(cx, cy - 14), (cx + 64, cy + 36), (cx - 64, cy + 36)], outline=IVORY, width=7)
    elif kind == "craft":
        E_([cx - 54, cy - 46, cx + 54, cy + 46], fill=(170, 130, 90))
        for dx, dy, col in ((-24, -18, RED), (6, -26, GOLD), (28, -2, SAGE), (-18, 14, IVORY)): E_([cx + dx - 11, cy + dy - 11, cx + dx + 11, cy + dy + 11], fill=col)
    elif kind == "phone":
        R([cx - 34, cy - 58, cx + 34, cy + 58], radius=14, fill=IVORY); R([cx - 26, cy - 44, cx + 26, cy + 36], radius=6, fill=GREEN_D); E_([cx - 7, cy + 42, cx + 7, cy + 54], fill=SAGE_D); d.text((cx, cy - 4), "55+", font=font(FONT_SANS, 20), fill=GOLD, anchor="mm")
    elif kind == "ticket":
        R([cx - 66, cy - 40, cx + 66, cy + 40], radius=10, fill=GOLD); E_([cx - 78, cy - 12, cx - 54, cy + 12], fill=CARD); E_([cx + 54, cy - 12, cx + 78, cy + 12], fill=CARD); d.text((cx, cy), "SENIOR", font=font(FONT_SANS, 24), fill=GREEN_D, anchor="mm")
    elif kind == "train":
        R([cx - 54, cy - 52, cx + 54, cy + 36], radius=18, fill=IVORY); R([cx - 40, cy - 38, cx + 40, cy - 2], radius=8, fill=GREEN_D); E_([cx - 40, cy + 8, cx - 22, cy + 26], fill=GOLD); E_([cx + 22, cy + 8, cx + 40, cy + 26], fill=GOLD); d.line([(cx - 40, cy + 56), (cx + 40, cy + 56)], fill=SAGE, width=6)
    elif kind == "bus":
        R([cx - 62, cy - 42, cx + 62, cy + 34], radius=12, fill=GOLD)
        for i in range(3): R([cx - 50 + i * 36, cy - 30, cx - 22 + i * 36, cy - 4], radius=4, fill=GREEN_D)
        E_([cx - 46, cy + 22, cx - 20, cy + 48], fill=IVORY); E_([cx + 20, cy + 22, cx + 46, cy + 48], fill=IVORY)
    elif kind == "park":
        E_([cx + 26, cy - 52, cx + 52, cy - 26], fill=GOLD); P([(cx - 66, cy + 46), (cx - 14, cy - 34), (cx + 30, cy + 46)], fill=SAGE); P([(cx - 10, cy + 46), (cx + 36, cy - 14), (cx + 68, cy + 46)], fill=SAGE_D)
    elif kind == "aarp":
        R([cx - 62, cy - 40, cx + 62, cy + 40], radius=12, fill=RED); d.text((cx, cy - 4), "50+", font=font(FONT_SANS, 40), fill=IVORY, anchor="mm")


KINDS = ["plate", "pharmacy", "shirt", "tag", "hanger", "craft", "phone", "ticket", "train", "bus", "park", "aarp"]


def s3(img, t):
    d = ImageDraw.Draw(img)
    spaced(img, "IN THE NEXT FEW MINUTES", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    cx, cy, r = 560, 500, 330
    a = ease(seg(t, .2, .6))
    lay = new_layer(); rgb, mask = lay; dd, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    for dr, c in ((dd, CARD), (dm, 255)):
        dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    dd.ellipse([cx - r, cy - r, cx + r, cy + r], outline=SAGE_D, width=6)
    alpha_layer(img, lay, a)
    for i in range(12):
        ang = -math.pi / 2 + i * 2 * math.pi / 12
        x, y = cx + (r - 40) * math.cos(ang), cy + (r - 40) * math.sin(ang)
        on = ease(seg(t, .8 + i * .33, .3))
        col = tuple(int(SAGE_D[k] + (GOLD[k] - SAGE_D[k]) * on) for k in range(3))
        rr = 15 + 9 * on
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=col)
    p = ease_back(seg(t, .5, .7))
    pop(img, lambda r_, m_: T(r_, m_, (cx, cy - 30), "12", font(FONT_SERIF, 330), IVORY), p, a=ease(seg(t, .5, .3)))
    a = ease(seg(t, 1.4, .5))
    if a > 0:
        lay = new_layer(); T(lay[0], lay[1], (cx, cy + 135), "PLACES", font(FONT_SANS, 66), SAGE); alpha_layer(img, lay, a)
    a = ease(seg(t, 4.5, .5))
    if a > 0:
        lay = new_layer(); T(lay[0], lay[1], (cx, 960), "THAT TAKE MONEY OFF YOUR BILL", font(FONT_SANS, 58), IVORY); alpha_layer(img, lay, a)
    # le 12 icone dei posti, una per ogni puntino che si accende
    gfade = 1 - ease(seg(t, 5.7, .4))
    for i, kind in enumerate(KINDS):
        st = .95 + i * .33
        col_, row_ = i % 4, i // 4
        gx, gy = 1060 + col_ * 200, 300 + row_ * 215
        pop(img, lambda r_, m_, k=kind, x=gx, y=gy: tile_icon(k, r_, m_, x, y), ease_back(seg(t, st, .45)), a=ease(seg(t, st, .25)) * gfade)
    # tessera "una volta, per sempre"
    st = 6.0
    def card(r_, m_):
        bx = [1060, 330, 1760, 760]
        ImageDraw.Draw(m_).rounded_rectangle(bx, radius=36, fill=255)
        dr = ImageDraw.Draw(r_); dr.rounded_rectangle(bx, radius=36, fill=GOLD)
        dr.rounded_rectangle([bx[0] + 18, bx[1] + 18, bx[2] - 18, bx[3] - 18], radius=26, outline=GREEN_D, width=4)
        T(r_, m_, (1410, 420), "LIFETIME PASS", font(FONT_SANS, 44), GREEN_D)
        T(r_, m_, (1410, 560), "$80", font(FONT_SERIF, 190), GREEN_D)
        T(r_, m_, (1410, 700), "PAID ONCE", font(FONT_SANS, 46), GREEN_D)
    pop(img, card, 0.7 + 0.3 * ease_back(seg(t, st, .7)), a=ease(seg(t, st, .4)), dy=math.sin(t * 2) * 5 if t > st + .8 else 0, angle=-4)
    a = ease(seg(t, st + 1.6, .5))
    if a > 0:
        lay = new_layer(); T(lay[0], lay[1], (1410, 880), "AND IT LASTS FOR LIFE", font(FONT_SANS, 56), GOLD); alpha_layer(img, lay, a)


if __name__ == "__main__":
    which = sys.argv[1:] or ["1", "2", "3"]
    for k, fn in (("1", s1), ("2", s2), ("3", s3)):
        if k in which:
            render(fn, DUR[int(k) - 1] / FPS, f"{OUT}/bloco01-slide0{k}.mp4")
            print("ok", k, DUR[int(k) - 1], "fotogrammi")
