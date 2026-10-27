"""Miniature video lungo 8 (WALMART), 2 versioni diverse per il test A/B. 1280x720.
Logo Walmart vero (parola + spark) preso dal sito ufficiale corporate.walmart.com (riferimenti/walmart/), su richiesta dell'utente 23/10.
Titolo video: Walmart Has No Senior Discount, But It Will Give You These 10 Things (If You Ask)
A = blu Walmart, "NO SENIOR DISCOUNT?" + scontrino con 10 righe coperte da barre nere (curiosita), solo 2 visibili ($4 RX LIST,
    50% OFF W+) evidenziate, cerchio e freccia rossi; fascia rossa "ASK FOR THESE 10".
B = giallo acceso, flacone lucido con cartellino rosso "$4", secondo cartellino "90 DAYS $10", testo "WALMART'S $4 LIST",
    fascia blu "+ 9 MORE TO ASK FOR".
Tutte le scritte sono vere e dette nel video.
uso: OUT=cartella python3 thumb_long8.py"""
import os, math
from PIL import Image, ImageDraw, ImageFilter
from thumb_long3 import *
import cairosvg

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
REF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "riferimenti", "walmart")
WBLUE = (0, 83, 226); WNAVY = (0, 30, 96); WYEL = (255, 194, 32)
PAPER = (253, 252, 247); INK = (20, 24, 30); RED2 = (230, 30, 40); OKG = (30, 160, 80)


# ------------------------------------------------------------------ logo
def spark(size):
    p = f"/tmp/_spark_{size}.png"
    cairosvg.svg2png(url=os.path.join(REF, "spark.svg"), write_to=p, output_width=size)
    return Image.open(p).convert("RGBA")


def wordmark(height, col):
    w = Image.open(os.path.join(REF, "us.png")).convert("RGBA").crop((0, 0, 483, 104))
    w = w.crop(w.getbbox())
    out = Image.new("RGBA", w.size, col + (255,)); out.putalpha(w.getchannel("A"))
    return out.resize((int(w.width * height / w.height), height), Image.LANCZOS)


def logo_pill(h=110, bg=(255, 255, 255), txt=WBLUE):
    wm = wordmark(int(h * 0.56), txt); sp = spark(int(h * 0.62))
    W_ = wm.width + sp.width + int(h * 0.9)
    lay = Image.new("RGBA", (W_, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([0, 0, W_ - 1, h - 1], radius=h // 2, fill=bg + (255,))
    lay.alpha_composite(wm, (int(h * 0.38), (h - wm.height) // 2 + 2))
    lay.alpha_composite(sp, (int(h * 0.38) + wm.width + int(h * 0.14), (h - sp.height) // 2))
    return lay


# ------------------------------------------------------------------ sfondi
def radial(c_in, c_out, cx, cy, r):
    im = Image.new("RGB", (W, H), c_out)
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(r * 0.45))
    return Image.composite(Image.new("RGB", (W, H), c_in), im, m)


def light_rays(im, cx, cy, col, n=14, alpha=40):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i in range(n):
        a0 = 2 * math.pi * i / n; a1 = a0 + math.pi / n * 0.8
        d.polygon([(cx, cy), (cx + 2000 * math.cos(a0), cy + 2000 * math.sin(a0)), (cx + 2000 * math.cos(a1), cy + 2000 * math.sin(a1))], fill=col + (alpha,))
    lay = lay.filter(ImageFilter.GaussianBlur(6))
    base = im.convert("RGBA"); base.alpha_composite(lay); return base.convert("RGB")


def vignette(im, strength=120):
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([-200, -160, W + 200, H + 160], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(160))
    return Image.composite(im, Image.blend(im, Image.new("RGB", (W, H), (0, 0, 0)), strength / 255), m)


def pill_band(text, w, h, fill, ink, size, ang=-3, border=BLK):
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([5, 5, w - 5, h - 5], radius=h // 2 - 4, fill=fill, outline=border, width=6)
    d.text((w / 2, h / 2 + 2), text, font=F(size, "Black"), fill=ink, anchor="mm")
    return rot(lay, ang)


# ------------------------------------------------------------------ A: scontrino coperto
def receipt_redacted(w=500, h=640):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    d.rectangle([S(0), S(16), S(w), S(h - 16)], fill=PAPER)
    for k in range(0, w, 26):
        d.polygon([(S(k), S(18)), (S(k + 13), S(0)), (S(k + 26), S(18))], fill=PAPER)
        d.polygon([(S(k), S(h - 18)), (S(k + 13), S(h)), (S(k + 26), S(h - 18))], fill=PAPER)
    d.text((S(w / 2), S(60)), "RECEIPT", font=F(S(38), "Black"), fill=INK, anchor="mm")
    for k in range(30, w - 30, 18):
        d.line([(S(k), S(94)), (S(k + 9), S(94))], fill=(150, 150, 150), width=S(3))
    d.text((S(30), S(130)), "SENIOR DISCOUNT", font=F(S(26), "Black"), fill=INK, anchor="lm")
    d.text((S(w - 30), S(130)), "$0.00", font=F(S(26), "Black"), fill=RED2, anchor="rm")
    d.line([(S(24), S(132)), (S(w - 24), S(126))], fill=RED2, width=S(6))
    vis = {2: "$4 RX LIST", 5: "50% OFF W+"}
    for i in range(10):
        y = 178 + i * 44
        d.text((S(30), S(y)), f"{i + 1}.", font=F(S(28), "Black"), fill=INK, anchor="lm")
        if i in vis:
            d.rounded_rectangle([S(70), S(y - 19), S(w - 26), S(y + 19)], radius=S(6), fill=(255, 226, 80))
            d.text((S(80), S(y)), vis[i], font=F(S(30), "Black"), fill=INK, anchor="lm")
        else:
            ln = [300, 360, 0, 280, 340, 0, 310, 260, 350, 290][i]
            d.rounded_rectangle([S(72), S(y - 15), S(72 + ln), S(y + 15)], radius=S(5), fill=(18, 18, 22))
    return done(lay, w, h)


def red_circle(w=330, h=96):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    d.ellipse([8 * s, 8 * s, (w - 8) * s, (h - 8) * s], outline=RED2, width=9 * s)
    return done(lay, w, h)


def thumb_a():
    im = radial((30, 120, 255), WNAVY, 420, 330, 620)
    im = light_rays(im, 420, 330, (255, 255, 255), 16, 26)
    im = vignette(im, 110)
    rc = rot(receipt_redacted(440, 640), -5)
    im = shadow_paste(im, rc, (800, 30), off=(16, 22), blur=20, alpha=170)
    im = shadow_paste(im, rot(red_circle(360, 70), -5), (865, 480), off=(0, 0), blur=1, alpha=0)
    im = shadow_paste(im, arrow(150, 110, RED2, 160), (670, 470), off=(6, 8), blur=8)
    im = shadow_paste(im, logo_pill(96), (40, 30), off=(6, 10), blur=10)
    im = text_stroke(im, (34, 250), "NO SENIOR", 108, (255, 255, 255), stroke=12, anchor="l")
    im = text_stroke(im, (34, 390), "DISCOUNT?", 118, WYEL, stroke=13, anchor="l")
    im = shadow_paste(im, pill_band("ASK FOR THESE 10", 660, 104, RED2, (255, 255, 255), 54), (30, 520), off=(6, 10), blur=10)
    return im


# ------------------------------------------------------------------ B: flacone + cartellino $4
def bottle_glossy(w=330, h=470):
    lay = canvas(w, h); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    d.rounded_rectangle([S(26), S(6), S(w - 26), S(96)], radius=S(18), fill=(250, 250, 250), outline=BLK, width=S(8))
    for x in range(48, w - 40, 24):
        d.line([(S(x), S(20)), (S(x), S(84))], fill=(205, 205, 210), width=S(5))
    d.rounded_rectangle([S(12), S(86), S(w - 12), S(h - 6)], radius=S(36), fill=(240, 130, 30), outline=BLK, width=S(8))
    d.rounded_rectangle([S(40), S(110), S(78), S(h - 40)], radius=S(19), fill=(255, 190, 120))
    d.rounded_rectangle([S(34), S(170), S(w - 34), S(h - 70)], radius=S(12), fill=PAPER, outline=BLK, width=S(6))
    d.text((S(w / 2), S(230)), "Rx", font=F(S(70), "Black"), fill=RED2, anchor="mm")
    for y in (300, 334, 368):
        d.rounded_rectangle([S(64), S(y - 7), S(w - 64), S(y + 7)], radius=S(7), fill=(170, 170, 175))
    return done(lay, w, h)


def price_tag(w, h, big, small, fill, ink, ang):
    lay = canvas(w, h + 40); d = ImageDraw.Draw(lay); s = SS
    def S(v): return int(v * s)
    pts = [(S(60), S(40)), (S(w - 6), S(40)), (S(w - 6), S(h + 34)), (S(60), S(h + 34)), (S(6), S(h / 2 + 37))]
    d.polygon(pts, fill=fill); d.line(pts + [pts[0]], fill=BLK, width=S(8), joint="curve")
    d.ellipse([S(34), S(h / 2 + 24), S(60), S(h / 2 + 50)], fill=(255, 255, 255), outline=BLK, width=S(5))
    d.text((S(w / 2 + 28), S(40 + h * 0.42)), big, font=F(S(int(h * 0.56)), "Black"), fill=ink, anchor="mm")
    if small:
        d.text((S(w / 2 + 28), S(40 + h * 0.82)), small, font=F(S(int(h * 0.15)), "Black"), fill=ink, anchor="mm")
    return rot(done(lay, w, h + 40), ang)


def thumb_b():
    im = radial((255, 236, 140), (255, 176, 0), 940, 360, 560)
    im = light_rays(im, 940, 360, (255, 255, 255), 18, 60)
    im = vignette(im, 60)
    im = shadow_paste(im, rot(bottle_glossy(290, 420), 8), (820, 140), off=(16, 22), blur=20, alpha=150)
    im = shadow_paste(im, price_tag(370, 224, "$4", "UP TO 30 DAYS", RED2, (255, 255, 255), -14), (690, 300), off=(12, 16), blur=14)
    im = shadow_paste(im, price_tag(240, 146, "$10", "90 DAYS", WBLUE, (255, 255, 255), 12), (990, 470), off=(10, 14), blur=12)
    im = shadow_paste(im, logo_pill(92, (255, 255, 255), WBLUE), (36, 30), off=(6, 10), blur=10)
    im = text_stroke(im, (34, 236), "WALMART'S", 100, WNAVY, stroke=12, sc=(255, 255, 255), anchor="l")
    im = text_stroke(im, (30, 390), "$4 LIST", 176, RED2, stroke=14, sc=(255, 255, 255), anchor="l")
    im = shadow_paste(im, pill_band("+ 9 MORE TO ASK FOR", 640, 100, WNAVY, (255, 255, 255), 46, -2, (255, 255, 255)), (30, 540), off=(6, 10), blur=10)
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b)):
        fn().save(f"{OUT}/walmart-miniatura-{name}.png"); print("ok", name)
