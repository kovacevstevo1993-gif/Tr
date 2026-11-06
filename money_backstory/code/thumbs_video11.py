"""Miniature video 11 'Never Keep More Than This in One Bank Account After 65' - 2 prove con layout DIVERSI. 1280x720, tutto a codice, niente volti.
Schema dai virali (V7lLK0JhzBQ 460K, PkQpWria5RM 176K, x5G9I1tIvPo): testo enorme bianco su fasce rosse/gialle, un oggetto-prova dettagliato (estratto conto con timbro), freccia/dito, una sola curiosita'."""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
from thumbs_video3_split import P, otext, fit_font
import thumbs_video7 as T7

W, H = 1280, 720
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video11"))
BLK, WHITE = (0, 0, 0), (255, 255, 255)
YEL, GOLD, RED, GRN, NAVY = (255, 214, 40), (212, 172, 82), (226, 30, 30), (36, 190, 96), (16, 36, 66)


def shadow(im, box, r=24, off=(10, 14), blur=14, a=170):
    s = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(s).rounded_rectangle([box[0] + off[0], box[1] + off[1], box[2] + off[0], box[3] + off[1]], radius=r, fill=(0, 0, 0, a))
    return Image.alpha_composite(im, s.filter(ImageFilter.GaussianBlur(blur)))


def vignette(im, strength=0.55):
    v = Image.new("L", (W, H), 0); d = ImageDraw.Draw(v)
    d.ellipse([-W * 0.25, -H * 0.3, W * 1.25, H * 1.3], fill=255); v = v.filter(ImageFilter.GaussianBlur(110))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * strength))); mask = Image.eval(v, lambda p: 255 - p)
    out = im.copy(); out.paste(dark, (0, 0), mask); return out


def rays(im, cx, cy, n=16, a=22, col=(255, 255, 255)):
    r = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(r)
    for k in range(n):
        t = math.radians(k * 360 / n)
        rd.polygon([(cx, cy), (cx + 1500 * math.cos(t), cy + 1500 * math.sin(t)), (cx + 1500 * math.cos(t + 0.1), cy + 1500 * math.sin(t + 0.1))], fill=col + (a,))
    return Image.alpha_composite(im, r)


def banner(im, text, box, fill=RED, fg=WHITE, size=130, tilt=0, stroke=7, outline=WHITE):
    x0, y0, x1, y1 = box; w, h = x1 - x0 + 60, y1 - y0 + 40
    L = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.polygon([(8, 10), (w - 14, 4), (w - 8, h - 8), (14, h - 4)], fill=fill, outline=outline)
    d.line([(8, 10), (w - 14, 4), (w - 8, h - 8), (14, h - 4), (8, 10)], fill=outline, width=5)
    f = fit_font(d, text, x1 - x0 - 30, size, True)
    d.text((w / 2, h / 2 + 2), text, font=f, fill=fg, anchor="mm", stroke_width=stroke if fg == WHITE else 0, stroke_fill=BLK)
    L = L.rotate(tilt, expand=True, resample=Image.BICUBIC)
    im.alpha_composite(L, (int((x0 + x1) / 2 - L.width / 2), int((y0 + y1) / 2 - L.height / 2)))


def bank(im, cx, cy, s, col=(236, 240, 245), roof=GOLD):
    d = ImageDraw.Draw(im); w = 190 * s
    d.polygon([(cx - w, cy - 60 * s), (cx, cy - 170 * s), (cx + w, cy - 60 * s)], fill=roof, outline=BLK)
    d.line([(cx - w, cy - 60 * s), (cx, cy - 170 * s), (cx + w, cy - 60 * s), (cx - w, cy - 60 * s)], fill=BLK, width=6)
    d.rectangle([cx - w + 8 * s, cy - 56 * s, cx + w - 8 * s, cy - 30 * s], fill=col, outline=BLK, width=5)
    for k in range(6):
        xx = cx - w + 40 * s + k * (2 * w - 80 * s) / 5
        d.rectangle([xx - 16 * s, cy - 24 * s, xx + 16 * s, cy + 90 * s], fill=col, outline=BLK, width=5)
    d.rectangle([cx - w - 10 * s, cy + 96 * s, cx + w + 10 * s, cy + 124 * s], fill=col, outline=BLK, width=5)
    d.rectangle([cx - w - 30 * s, cy + 124 * s, cx + w + 30 * s, cy + 150 * s], fill=(200, 205, 215), outline=BLK, width=5)
    d.ellipse([cx - 40 * s, cy - 134 * s, cx + 40 * s, cy - 78 * s], fill=NAVY, outline=BLK, width=5)
    d.text((cx, cy - 106 * s), "$", font=P(int(54 * s), True), fill=YEL, anchor="mm")


def statement(im, x, y, w, h, tilt, rows, head="CHECKING ACCOUNT", stamp_txt=None, stamp_col=RED):
    L = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rectangle([20, 20, w + 20, h + 20], fill=(247, 247, 243), outline=BLK, width=6)
    d.rectangle([20, 20, w + 20, 96], fill=(34, 70, 150)); d.text((20 + w / 2, 58), head, font=fit_font(d, head, w - 50, 40, True), fill=WHITE, anchor="mm")
    d.rectangle([20, 96, w + 20, 108], fill=RED)
    for i, (a, b, bad) in enumerate(rows):
        yy = 150 + i * 62
        d.text((44, yy), a, font=P(30, True), fill=(40, 46, 60), anchor="lm")
        d.text((w - 4, yy), b, font=P(34, True), fill=RED if bad else (22, 120, 60), anchor="rm")
        d.line([36, yy + 28, w + 4, yy + 28], fill=(200, 204, 214), width=3)
    if stamp_txt:
        f = P(70, True); tw = d.textlength(stamp_txt, font=f)
        S = Image.new("RGBA", (int(tw + 70), 150), (0, 0, 0, 0)); sd = ImageDraw.Draw(S)
        sd.rounded_rectangle([4, 4, tw + 62, 142], radius=16, outline=stamp_col + (235,), width=11); sd.text(((tw + 70) / 2, 74), stamp_txt, font=f, fill=stamp_col + (235,), anchor="mm")
        S = S.rotate(14, expand=True, resample=Image.BICUBIC); L.alpha_composite(S, (int(w / 2 - S.width / 2 + 20), int(h * 0.91 - S.height / 2)))
    L = L.rotate(tilt, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", L.size, (0, 0, 0, 0)); sh.paste((0, 0, 0, 160), mask=L.split()[3]); sh = sh.filter(ImageFilter.GaussianBlur(10))
    im.alpha_composite(sh, (x + 14, y + 16)); im.alpha_composite(L, (x, y))


def padlock(im, cx, cy, s, col=RED):
    d = ImageDraw.Draw(im)
    d.arc([cx - 46 * s, cy - 92 * s, cx + 46 * s, cy + 6 * s], 180, 360, fill=(200, 205, 215), width=int(20 * s)); d.arc([cx - 46 * s, cy - 92 * s, cx + 46 * s, cy + 6 * s], 180, 360, fill=BLK, width=int(5 * s))
    d.rounded_rectangle([cx - 70 * s, cy - 14 * s, cx + 70 * s, cy + 100 * s], radius=int(18 * s), fill=col, outline=BLK, width=6)
    d.ellipse([cx - 14 * s, cy + 18 * s, cx + 14 * s, cy + 46 * s], fill=BLK); d.rectangle([cx - 6 * s, cy + 36 * s, cx + 6 * s, cy + 74 * s], fill=BLK)


def bills(im, x, y, n=4, tilt0=-8):
    for k in range(n):
        L = Image.new("RGBA", (230, 120), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        d.rounded_rectangle([3, 3, 226, 116], radius=10, fill=(96, 190, 120), outline=BLK, width=4); d.ellipse([84, 20, 148, 98], fill=(70, 160, 96), outline=BLK, width=3)
        d.text((115, 59), "$", font=P(52, True), fill=(20, 80, 40), anchor="mm"); d.text((26, 22), "100", font=P(26, True), fill=(20, 80, 40), anchor="mm"); d.text((204, 98), "100", font=P(26, True), fill=(20, 80, 40), anchor="mm")
        L = L.rotate(tilt0 + k * 6, expand=True, resample=Image.BICUBIC); im.alpha_composite(L, (x + k * 22, y - k * 26))


def A():
    """A (come i virali): rosso/nero. 'NEVER KEEP / MORE THAN / THIS' enorme a sinistra su fasce; a destra estratto conto con timbro FROZEN, lucchetto, banca; fascia gialla 'IN ONE BANK ACCOUNT'."""
    im = Image.new("RGBA", (W, H), (14, 14, 18, 255)); d = ImageDraw.Draw(im)
    for y in range(H):
        g = int(26 * (1 - y / H)); d.line([(0, y), (W, y)], fill=(18 + g, 14 + g // 2, 16 + g // 2))
    im = rays(im, 920, 360, 18, 26, (255, 90, 60)); d = ImageDraw.Draw(im)
    bank(im, 985, 150, 0.62, col=(222, 226, 236))
    statement(im, 725, 205, 460, 450, -5, [("DEPOSIT", "+$2,140", False), ("PAYMENT", "-$310", True), ("BALANCE", "$380,000", False)], stamp_txt="FROZEN")
    padlock(im, 1190, 95, 0.55)
    d = ImageDraw.Draw(im)
    banner(im, "NEVER KEEP", (30, 28, 680, 190), fill=RED, size=150)
    banner(im, "MORE THAN", (30, 210, 680, 372), fill=RED, size=150, tilt=-1)
    banner(im, "THIS", (30, 392, 440, 560), fill=YEL, fg=BLK, size=170, tilt=1)
    banner(im, "IN ONE BANK ACCOUNT", (30, 590, 700, 690), fill=WHITE, fg=BLK, size=80, outline=BLK)
    # freccia rossa verso il saldo
    return vignette(im, 0.35).convert("RGB")


def B():
    """B (stile canale, navy + oro): scudo FDIC con '$250,000' enorme e '?' rosso; sotto barra copertura verde/rossa 'FRANK $380,000' con timbro '$130,000 NOT COVERED'; fascia 'THE 5 RULES'."""
    im = T7.navy_bg().convert("RGBA"); d = ImageDraw.Draw(im)
    im = rays(im, 640, 300, 20, 20, (255, 255, 255)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([12, 12, W - 12, H - 12], radius=30, outline=GOLD, width=9)
    d.text((640, 62), "NEVER KEEP MORE THAN THIS", font=fit_font(d, "NEVER KEEP MORE THAN THIS", 1120, 88, True), fill=WHITE, anchor="mm", stroke_width=9, stroke_fill=BLK)
    # scudo
    cx, cy = 640, 290; K = 0.85
    pts = [(cx + K * a, cy + K * b) for a, b in [(-310, -150), (0, -195), (310, -150), (310, 20), (190, 120), (0, 190), (-190, 120), (-310, 20)]]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).polygon([(x + 12, y + 18) for x, y in pts], fill=(0, 0, 0, 170)); im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(12))); d = ImageDraw.Draw(im)
    d.polygon(pts, fill=(22, 48, 90), outline=GOLD); d.line(pts + [pts[0]], fill=GOLD, width=14)
    inner = [(cx + K * a, cy + K * b) for a, b in [(-288, -136), (0, -178), (288, -136), (288, 14), (178, 108), (0, 170), (-178, 108), (-288, 14)]]
    d.line(inner + [inner[0]], fill=(255, 255, 255), width=4)
    d.text((cx - 24, cy - 25), "$250,000", font=fit_font(d, "$250,000", 470, 150, True), fill=YEL, anchor="mm", stroke_width=12, stroke_fill=BLK)
    d.text((cx + 232, cy - 100), "?", font=P(170, True), fill=RED, anchor="mm", stroke_width=12, stroke_fill=WHITE)
    d.text((cx, cy + 80), "FDIC INSURED", font=P(38, True), fill=WHITE, anchor="mm", stroke_width=5, stroke_fill=BLK)
    # barra copertura
    x0, x1, y0, y1 = 110, 1170, 512, 588; lim = x0 + (x1 - x0) * 250 / 380
    d.rounded_rectangle([x0 - 8, y0 - 8, x1 + 8, y1 + 8], radius=26, fill=BLK)
    d.rounded_rectangle([x0, y0, lim, y1], radius=20, fill=GRN); d.rectangle([lim - 20, y0, lim, y1], fill=GRN)
    d.rounded_rectangle([lim, y0, x1, y1], radius=20, fill=RED); d.rectangle([lim, y0, lim + 20, y1], fill=RED)
    d.line([lim, y0 - 26, lim, y1 + 18], fill=WHITE, width=8)
    d.text(((x0 + lim) / 2, (y0 + y1) / 2), "$250,000 COVERED", font=fit_font(d, "$250,000 COVERED", lim - x0 - 40, 58, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text(((lim + x1) / 2, (y0 + y1) / 2), "$130,000 AT RISK", font=fit_font(d, "$130,000 AT RISK", x1 - lim - 30, 56, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=BLK)
    d.text((x0 + 10, y0 - 40), "FRANK: $380,000 IN ONE BANK", font=P(46, True), fill=YEL, anchor="lm", stroke_width=6, stroke_fill=BLK)
    banner(im, "5 RULES MOST SENIORS MISS", (330, 640, 950, 696), fill=RED, size=52, tilt=0)
    return im.convert("RGB")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n, f in [("A-never-keep-this", A), ("B-250000-shield", B)]:
        f().save(f"{OUT}/video11-{n}.png"); print("ok", n)
