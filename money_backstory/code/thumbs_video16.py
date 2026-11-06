"""Miniature video 16 'Lettera di sovrapagamento Social Security' - 2 prove con layout DIVERSI, 1280x720, a codice, niente volti.
Dopo aver guardato le miniature dei virali del tema (i.ytimg.com): pochi elementi grandi, testo a 2-3 righe bianco/giallo con contorno nero e ombra, oggetto lucido con profondita'.
A: lettera ufficiale inclinata con ombra morbida e busta dietro, riga rossa 'YOU OWE $9,000', timbro, '50%' gigante giallo con riflesso.
B: assegno strappato a meta' (meta' verde che resta, meta' rossa che si stacca con bordo irregolare), 'HALF OF YOUR CHECK'."""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
from thumbs_video3_split import P, fit_font
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video16"))
W, H = 1280, 720
BLK = (0, 0, 0); WHITE = (255, 255, 255); YEL = (255, 214, 60); RED = (226, 40, 48); GRN = (34, 160, 88); GOLD = (212, 172, 82); NAVY = (10, 24, 52)
random.seed(16)

def gradient_bg(c0, c1, c2=None, angle=0.0):
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        for x in range(W):
            t = (x * math.cos(angle) + y * math.sin(angle)) / (W * abs(math.cos(angle)) + H * abs(math.sin(angle)) + 1e-9)
            t = max(0.0, min(1.0, t + 0.5 * (1 - abs(math.cos(angle)) - abs(math.sin(angle)) + 0)))
            a, b, u = (c0, c1, t * 2) if (c2 is None or t < 0.5) else (c1, c2, (t - 0.5) * 2)
            if c2 is None: a, b, u = c0, c1, t
            px[x, y] = tuple(int(a[i] + (b[i] - a[i]) * min(1, u)) for i in range(3))
    return im

def glow_spot(im, cx, cy, r, col, a=120):
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(L).ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (a,))
    return Image.alpha_composite(im.convert("RGBA"), L.filter(ImageFilter.GaussianBlur(r * 0.55)))

def vignette(im, s=0.55):
    L = Image.new("L", (W, H), 0); ImageDraw.Draw(L).ellipse([-250, -170, W + 250, H + 170], fill=255); L = L.filter(ImageFilter.GaussianBlur(160))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * s))); dark.putalpha(ImageChops.invert(L).point(lambda v: int(v * s)))
    return Image.alpha_composite(im.convert("RGBA"), dark)

def drop_shadow(base, layer, pos, off=(14, 20), blur=22, a=190):
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0)); al = layer.split()[3].point(lambda v: int(v * a / 255))
    sh.paste((0, 0, 0, 255), (pos[0] + off[0], pos[1] + off[1]), al); sh = sh.filter(ImageFilter.GaussianBlur(blur))
    base = Image.alpha_composite(base, sh); base.alpha_composite(layer, pos); return base

def text_grad(im, s, font, cx, cy, top, bot, stroke=10, sc=BLK, shadow=True):
    """testo con riempimento a gradiente verticale, contorno nero e ombra"""
    d = ImageDraw.Draw(im); bb = d.textbbox((cx, cy), s, font=font, anchor="mm", stroke_width=stroke)
    w, h = bb[2] - bb[0], bb[3] - bb[1]; pad = 30
    mask = Image.new("L", (w + 2 * pad, h + 2 * pad), 0); ImageDraw.Draw(mask).text((pad + stroke, pad + stroke + (0)), s, font=font, fill=255, anchor="la")
    mb = mask.getbbox()
    lay = Image.new("RGBA", mask.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.text((pad + stroke, pad + stroke), s, font=font, fill=sc + (255,), anchor="la", stroke_width=stroke, stroke_fill=sc + (255,))
    g = Image.new("RGBA", mask.size); gd = ImageDraw.Draw(g)
    y0, y1 = (mb[1], mb[3]) if mb else (0, mask.size[1])
    for y in range(mask.size[1]):
        t = max(0, min(1, (y - y0) / max(1, y1 - y0))); gd.line([0, y, mask.size[0], y], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)) + (255,))
    lay.paste(g, (0, 0), mask)
    px = int(cx - (mb[0] + mb[2]) / 2); py = int(cy - (mb[1] + mb[3]) / 2)
    if shadow:
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.paste((0, 0, 0, 200), (px + 8, py + 12), lay.split()[3]); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
    im.alpha_composite(lay, (px, py)); return im

def plain_text(im, s, font, cx, cy, fill=WHITE, stroke=8, sc=BLK):
    L = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(L).text((cx + 5, cy + 8), s, font=font, fill=(0, 0, 0, 190), anchor="mm", stroke_width=stroke, stroke_fill=(0, 0, 0, 190))
    im.alpha_composite(L.filter(ImageFilter.GaussianBlur(4)))
    ImageDraw.Draw(im).text((cx, cy), s, font=font, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=sc); return im

def ribbon(im, s, box, fill=YEL, fg=BLK, size=64, tilt=-2):
    w, h = box[2] - box[0], box[3] - box[1]; L = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([20, 20, 20 + w, 20 + h], radius=14, fill=fill + (255,), outline=(0, 0, 0, 255), width=6)
    d.text((20 + w / 2, 20 + h / 2 + 2), s, font=fit_font(d, s, w - 40, size, True), fill=fg, anchor="mm")
    L = L.rotate(tilt, resample=Image.BICUBIC, expand=True); pos = (int(box[0] - 20 - (L.width - w - 40) / 2), int(box[1] - 20 - (L.height - h - 40) / 2))
    return drop_shadow(im, L, pos, (8, 12), 10, 170)

# ---------- oggetti ----------
def letter_layer(w=600, h=760):
    L = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=10, fill=(246, 247, 250, 255), outline=(196, 202, 214, 255), width=3)
    d.rounded_rectangle([0, 0, w - 1, 118], radius=10, fill=(22, 52, 110, 255)); d.rectangle([0, 60, w - 1, 118], fill=(22, 52, 110, 255))
    d.ellipse([28, 22, 100, 94], outline=(246, 214, 140, 255), width=5); d.text((64, 58), "★", font=P(38, True), fill=(246, 214, 140), anchor="mm")
    d.text((124, 40), "OFFICIAL NOTICE", font=P(26, True), fill=(190, 205, 235), anchor="lm"); d.text((124, 80), "OVERPAYMENT", font=P(38, True), fill=(246, 214, 140), anchor="lm")
    y = 160
    for k, ww in enumerate([440, 500, 380, 470]):
        d.rounded_rectangle([40, y, 40 + ww, y + 18], radius=9, fill=(200, 206, 218, 255)); y += 44
    d.rounded_rectangle([30, y + 10, w - 30, y + 140], radius=14, fill=(255, 228, 228, 255), outline=RED + (255,), width=6)
    d.text((50, y + 46), "YOU OWE", font=P(34, True), fill=(120, 30, 36), anchor="lm"); d.text((w - 46, y + 94), "$9,000", font=P(84, True), fill=(210, 30, 40), anchor="rm")
    y += 190
    for k, ww in enumerate([500, 420, 470, 300]):
        d.rounded_rectangle([40, y, 40 + ww, y + 18], radius=9, fill=(200, 206, 218, 255)); y += 44
    d.line([40, h - 70, 300, h - 70], fill=(22, 52, 110, 255), width=3); d.text((40, h - 50), "SIGNATURE", font=P(20, True), fill=(120, 130, 150), anchor="lm")
    return L

def envelope_layer(w=700, h=470):
    L = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=14, fill=(226, 196, 122, 255), outline=(150, 118, 50, 255), width=4)
    d.polygon([(4, 4), (w / 2, h * 0.58), (w - 4, 4)], fill=(240, 214, 146, 255), outline=(150, 118, 50, 255))
    return L

def stamp_layer(s, col=(214, 30, 40), w=420, h=120, size=70):
    L = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([4, 4, w - 5, h - 5], radius=14, outline=col + (255,), width=9); d.rounded_rectangle([16, 16, w - 17, h - 17], radius=8, outline=col + (255,), width=3)
    d.text((w / 2, h / 2 + 2), s, font=fit_font(d, s, w - 60, size, True), fill=col + (255,), anchor="mm")
    n = Image.new("L", (w, h), 0); nd = ImageDraw.Draw(n)
    for _ in range(900): x, y = random.randint(0, w - 1), random.randint(0, h - 1); nd.point((x, y), fill=255)
    a = L.split()[3]; a = ImageChops.subtract(a, n.point(lambda v: 90 if v else 0)); L.putalpha(a); return L

def A():
    im = gradient_bg((6, 14, 34), (22, 52, 104), None, 0.6).convert("RGBA")
    im = glow_spot(im, 360, 340, 380, (60, 110, 220), 110); im = glow_spot(im, 1010, 330, 300, (255, 190, 60), 70)
    # busta dietro
    env = envelope_layer().rotate(10, resample=Image.BICUBIC, expand=True); im = drop_shadow(im, env, (-30, 330), (14, 22), 24, 200)
    let = letter_layer(); let = let.resize((int(let.width * 0.86), int(let.height * 0.86)), Image.LANCZOS).rotate(-9, resample=Image.BICUBIC, expand=True); im = drop_shadow(im, let, (20, -10), (16, 24), 26, 210)
    st = stamp_layer("OVERPAID").rotate(14, resample=Image.BICUBIC, expand=True); im = drop_shadow(im, st, (200, 520), (6, 10), 8, 150)
    f1 = P(68, True); f2 = P(270, True); f3 = P(78, True)
    im = plain_text(im, "THEY CAN TAKE", f1, 905, 95, WHITE, 9)
    im = text_grad(im, "50%", f2, 930, 318, (255, 244, 150), (255, 170, 20), 14)
    im = plain_text(im, "OF YOUR CHECK", f3, 920, 500, WHITE, 10)
    im = ribbon(im, "4 MOVES THAT STOP IT", (640, 600, 1240, 690), YEL, BLK, 52, -2)
    return vignette(im, 0.45).convert("RGB")

def torn_check(w=820, h=330):
    C = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(C)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=16, fill=(240, 244, 232, 255), outline=(60, 110, 76, 255), width=5)
    for k in range(0, h, 9): d.line([8, k, w - 8, k + int(10 * math.sin(k / 20))], fill=(190, 214, 190, 255), width=2)     # fondino
    d.rectangle([0, 0, w - 1, 72], fill=(32, 110, 70, 255)); d.text((28, 36), "MONTHLY BENEFIT", font=P(36, True), fill=(236, 248, 238), anchor="lm"); d.text((w - 28, 36), "No. 0916", font=P(28, True), fill=(190, 226, 200), anchor="rm")
    d.text((34, 140), "PAY TO THE ORDER OF  CAROL", font=P(26, True), fill=(60, 80, 66), anchor="lm")
    d.rounded_rectangle([w - 330, 100, w - 24, 200], radius=10, fill=(255, 255, 255, 255), outline=(60, 110, 76, 255), width=4); d.text((w - 177, 150), "$2,100", font=P(76, True), fill=(20, 60, 36), anchor="mm")
    d.line([34, h - 60, 360, h - 60], fill=(60, 110, 76, 255), width=3); d.text((34, h - 36), "AUTHORIZED SIGNATURE", font=P(20, True), fill=(90, 110, 96), anchor="lm")
    return C

def B():
    im = gradient_bg((120, 14, 22), (14, 20, 44), None, 0.0).convert("RGBA")
    im = glow_spot(im, 980, 380, 380, (255, 80, 60), 90); im = glow_spot(im, 300, 380, 340, (40, 160, 100), 80)
    chk = torn_check(); k = 1.15; chk = chk.resize((int(chk.width * k), int(chk.height * k)), Image.LANCZOS); w, h = chk.size
    cut = int(w * 0.52); rnd = random.Random(7)
    zig = [(cut + rnd.randint(-18, 18), y) for y in range(0, h + 1, 24)]
    mL = Image.new("L", (w, h), 0); ImageDraw.Draw(mL).polygon([(0, 0)] + zig + [(0, h)], fill=255)
    mR = Image.new("L", (w, h), 0); ImageDraw.Draw(mR).polygon(zig + [(w, h), (w, 0)], fill=255)
    left = Image.new("RGBA", (w, h), (0, 0, 0, 0)); left.paste(chk, (0, 0), mL); left = left.crop((0, 0, cut + 30, h))
    right = Image.new("RGBA", (w, h), (0, 0, 0, 0)); right.paste(chk, (0, 0), mR)
    rt = Image.new("RGBA", (w, h), (0, 0, 0, 0)); rt.paste(Image.new("RGBA", (w, h), (226, 40, 48, 150)), (0, 0), mR); right = Image.alpha_composite(right, rt)
    ImageDraw.Draw(right).text((cut + (w - cut) / 2 + 10, h - 92), "-$1,050", font=P(78, True), fill=(255, 255, 255), anchor="mm", stroke_width=7, stroke_fill=(110, 10, 18))
    right = right.crop((cut - 30, 0, w, h))
    lft = left.rotate(3, resample=Image.BICUBIC, expand=True); rgt = right.rotate(-8, resample=Image.BICUBIC, expand=True)
    im = drop_shadow(im, lft, (50, 340), (12, 20), 22, 200); im = drop_shadow(im, rgt, (700, 335), (12, 20), 22, 210)
    im = plain_text(im, "SOCIAL SECURITY", P(54, True), 640, 52, YEL, 8)
    im = text_grad(im, "HALF OF", P(120, True), 640, 150, (255, 255, 255), (214, 220, 236), 12)
    im = text_grad(im, "YOUR CHECK GONE?", fit_font(ImageDraw.Draw(im), "YOUR CHECK GONE?", 1180, 120, True), 640, 262, (255, 244, 150), (255, 176, 24), 12)
    im = ribbon(im, "GOT THE LETTER? DO THIS FIRST", (60, 622, 660, 700), WHITE, BLK, 40, 1)
    return vignette(im, 0.4).convert("RGB")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("video16-A-they-can-take-50-percent", A), ("video16-B-half-your-check-gone", B)):
        fn().save(os.path.join(OUT, name + ".png")); print("ok", name)
