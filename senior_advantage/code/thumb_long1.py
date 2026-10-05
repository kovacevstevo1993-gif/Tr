"""Miniatura video lungo 1 (The Senior Advantage) 1280x720: verde bosco/avorio/oro + rosso, Montserrat ExtraBold."""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1280, 720
OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
FP = "/home/user/Tr/money_backstory/code/fonts/Montserrat.ttf"
GREEN_D = (7, 38, 30); GREEN_L = (26, 92, 71); IVORY = (246, 241, 229); GOLD = (244, 190, 70)
RED = (226, 52, 44); BLK = (0, 0, 0); SAGE = (154, 200, 170)


def F(size, w="ExtraBold"):
    f = ImageFont.truetype(FP, size); f.set_variation_by_name(w); return f


def bg():
    im = Image.new("RGB", (W, H), GREEN_D)
    px = im.load()
    cx, cy = 430, 360
    for y in range(H):
        for x in range(W):
            d = math.hypot(x - cx, y - cy) / 900
            t = max(0, 1 - d)
            px[x, y] = (int(7 + 24 * t), int(38 + 62 * t), int(30 + 48 * t))
    return im


def shadow(im, layer_fn, off=(8, 10), blur=10, alpha=170):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); layer_fn(ImageDraw.Draw(lay), (0, 0, 0, alpha))
    lay = lay.filter(ImageFilter.GaussianBlur(blur))
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sh.paste(lay, off)
    return Image.alpha_composite(im.convert("RGBA"), sh).convert("RGB")


def text_c(d, xy, s, f, fill, stroke=0, sc=BLK, anchor="mm"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=sc)


def rot_paste(im, draw_fn, size, center, angle):
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); draw_fn(ImageDraw.Draw(lay), size)
    sh = Image.new("RGBA", size, (0, 0, 0, 0))
    sm = Image.new("RGBA", size, (0, 0, 0, 0)); sm.paste(Image.new("RGBA", size, (0, 0, 0, 150)), (0, 0), lay.split()[3])
    sm = sm.filter(ImageFilter.GaussianBlur(8))
    lay = lay.rotate(angle, expand=True, resample=Image.BICUBIC); sm = sm.rotate(angle, expand=True, resample=Image.BICUBIC)
    x, y = int(center[0] - lay.width / 2), int(center[1] - lay.height / 2)
    base = im.convert("RGBA"); base.alpha_composite(sm, (x + 8, y + 12)); base.alpha_composite(lay, (x, y))
    return base.convert("RGB")


def tag(d, size):
    w, h = size
    d.rounded_rectangle([10, 10, w - 10, h - 10], radius=34, fill=GOLD, outline=BLK, width=7)
    d.ellipse([34, h / 2 - 20, 74, h / 2 + 20], fill=GREEN_D, outline=BLK, width=5)
    d.text((w / 2 + 24, h / 2), "55+", font=F(150, "Black"), fill=GREEN_D, anchor="mm")


def idcard(d, size):
    w, h = size
    d.rounded_rectangle([8, 8, w - 8, h - 8], radius=26, fill=IVORY, outline=BLK, width=6)
    d.rounded_rectangle([8, 8, w - 8, 66], radius=26, fill=GREEN_L)
    d.rectangle([8, 40, w - 8, 66], fill=GREEN_L)
    d.text((w / 2, 38), "PHOTO ID", font=F(30), fill=IVORY, anchor="mm")
    d.rounded_rectangle([34, 96, 170, h - 34], radius=14, fill=SAGE)
    for i in range(3):
        d.rounded_rectangle([200, 104 + i * 50, w - 36 - (i % 2) * 50, 132 + i * 50], radius=8, fill=(190, 184, 160))


def coupon(d, size, s):
    w, h = size
    d.rounded_rectangle([8, 8, w - 8, h - 8], radius=24, fill=RED, outline=BLK, width=6)
    for k in range(9):
        d.line([(30 + k * ((w - 60) / 8), 24), (30 + k * ((w - 60) / 8) + 12, 24)], fill=IVORY, width=5)
    d.text((w / 2, h / 2 + 6), s, font=F(78, "Black"), fill=IVORY, anchor="mm", stroke_width=2, stroke_fill=BLK)


def build():
    im = bg()
    d = ImageDraw.Draw(im)
    # titolo piccolo in alto
    pw = 560
    d.rounded_rectangle([46, 40, 46 + pw, 104], radius=32, fill=GOLD, outline=BLK, width=5)
    text_c(d, (46 + pw / 2, 73), "SENIOR DISCOUNTS", F(38), GREEN_D)
    # 55 gigante con ombra
    f55 = F(390, "Black")
    im = shadow(im, lambda dr, c: dr.text((300, 335), "55", font=f55, fill=c, anchor="mm"), off=(10, 14), blur=12)
    d = ImageDraw.Draw(im)
    text_c(d, (300, 335), "55", f55, IVORY, stroke=14)
    text_c(d, (60, 160), "STARTS AT", F(50), GOLD, stroke=5, anchor="lm")
    # NOT 65 barrato
    f65 = F(120, "Black")
    f65 = F(100, "Black")
    text_c(d, (305, 548), "NOT 65", f65, GOLD, stroke=7)
    bb = d.textbbox((305, 548), "NOT 65", font=f65, anchor="mm")
    d.line([(bb[0] - 14, (bb[1] + bb[3]) / 2 + 4), (bb[2] + 14, (bb[1] + bb[3]) / 2 - 4)], fill=RED, width=16)
    # oggetti a destra
    im = rot_paste(im, tag, (460, 270), (1010, 220), -9)
    im = rot_paste(im, idcard, (460, 280), (1050, 470), 6)
    im = rot_paste(im, lambda dd, s: coupon(dd, s, "-10%"), (250, 130), (790, 540), -10)
    d = ImageDraw.Draw(im)
    # fascia rossa in basso
    d.rounded_rectangle([40, 622, W - 40, 696], radius=24, fill=RED, outline=BLK, width=6)
    text_c(d, (W / 2, 660), "NOBODY TELLS YOU", F(54), IVORY, stroke=3)
    return im


if __name__ == "__main__":
    im = build(); p = f"{OUT}/video-lungo-1-55-not-65.png"; im.save(p); print(p)
