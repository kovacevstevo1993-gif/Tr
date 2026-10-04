"""Miniature video lungo 2 (SNAP over 60), 3 versioni per il test A/B. 1280x720.
A = stesso stile del video 1 (verde, numero gigante). B = nonno su giallo a raggi. C = chiara, X rossa sul test del reddito.
uso: OUT=cartella python3 thumb_long2.py"""
import os, math
from PIL import Image, ImageDraw, ImageFilter
import thumb_long1 as T
import thumb_long1_c as C
from thumb_long1 import F, GREEN_D, GREEN_L, IVORY, GOLD, RED, BLK, SAGE

W, H = 1280, 720
OUT = os.environ.get("OUT", "/tmp/thumb2")
os.makedirs(OUT, exist_ok=True)


def person(d, x, y, s, fill, line=None, w=0):
    d.ellipse([x - s * .24, y - s * .46, x + s * .24, y - s * .02], fill=fill, outline=line, width=w)
    d.rounded_rectangle([x - s * .4, y + s * .02, x + s * .4, y + s * .46], radius=s * .2, fill=fill, outline=line, width=w)


def grid_card(size):
    w, h = size
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([8, 8, w - 8, h - 8], radius=30, fill=(12, 58, 45), outline=BLK, width=7)
    d.rounded_rectangle([8, 8, w - 8, 66], radius=30, fill=GREEN_L, outline=BLK, width=7)
    d.rectangle([14, 40, w - 14, 66], fill=GREEN_L)
    d.text((w / 2, 38), "100 ELIGIBLE SENIORS", font=F(30), fill=IVORY, anchor="mm")
    cw, ch = (w - 60) / 10, (h - 110) / 10
    for i in range(100):
        x = 30 + (i % 10 + .5) * cw; y = 84 + (i // 10 + .5) * ch + 8
        if i < 55:
            person(d, x, y, min(cw, ch) * 0.82, GOLD, BLK, 2)
        else:
            person(d, x, y, min(cw, ch) * 0.82, (74, 120, 104), None, 0)
    return lay


def paste_rot(im, lay, center, ang):
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0)); sh.paste(Image.new("RGBA", lay.size, (0, 0, 0, 150)), (0, 0), lay.split()[3]); sh = sh.filter(ImageFilter.GaussianBlur(9))
    lay = lay.rotate(ang, expand=True, resample=Image.BICUBIC); sh = sh.rotate(ang, expand=True, resample=Image.BICUBIC)
    x, y = int(center[0] - lay.width / 2), int(center[1] - lay.height / 2)
    base = im.convert("RGBA"); base.alpha_composite(sh, (x + 8, y + 12)); base.alpha_composite(lay, (x, y))
    return base.convert("RGB")


def food_bits(im, items):
    for (kind, cx, cy, ang, sc) in items:
        w, h = 200, 200
        lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        if kind == "apple":
            d.ellipse([20, 40, 180, 190], fill=RED, outline=BLK, width=6); d.line([100, 46, 108, 10], fill=(110, 70, 40), width=9)
            d.polygon([(108, 30), (160, 8), (150, 44)], fill=(60, 160, 90), outline=BLK, width=4)
        elif kind == "milk":
            d.polygon([(40, 60), (100, 10), (160, 60)], fill=(226, 220, 204), outline=BLK, width=5)
            d.rounded_rectangle([40, 56, 160, 192], radius=10, fill=IVORY, outline=BLK, width=6); d.rounded_rectangle([66, 100, 134, 160], radius=10, fill=(100, 170, 130))
        elif kind == "bread":
            d.rounded_rectangle([10, 60, 190, 170], radius=50, fill=(222, 164, 80), outline=BLK, width=6)
            for x in (60, 100, 140): d.line([x, 80, x + 14, 120], fill=(180, 120, 50), width=8)
        elif kind == "can":
            d.rounded_rectangle([40, 24, 160, 186], radius=16, fill=(190, 198, 196), outline=BLK, width=6); d.rectangle([44, 70, 156, 140], fill=RED); d.ellipse([76, 80, 124, 130], fill=IVORY)
        if sc != 1: lay = lay.resize((int(w * sc), int(h * sc)), Image.LANCZOS)
        im = paste_rot(im, lay, (cx, cy), ang)
    return im


# ---------------------------------------------------------------- A: stile video 1
def build_a():
    im = T.bg(); d = ImageDraw.Draw(im)
    d.rounded_rectangle([46, 40, 46 + 640, 104], radius=32, fill=GOLD, outline=BLK, width=5)
    T.text_c(d, (46 + 320, 73), "SNAP FOR SENIORS 60+", F(38), GREEN_D)
    f55 = F(390, "Black")
    im = T.shadow(im, lambda dr, c: dr.text((300, 330), "55", font=f55, fill=c, anchor="mm"), off=(10, 14), blur=12)
    d = ImageDraw.Draw(im)
    T.text_c(d, (300, 330), "55", f55, IVORY, stroke=14)
    T.text_c(d, (60, 160), "ONLY", F(56), GOLD, stroke=5, anchor="lm")
    T.text_c(d, (300, 545), "OUT OF 100", F(92, "Black"), GOLD, stroke=7)
    im = paste_rot(im, grid_card((500, 470)), (1000, 345), 4)
    im = T.rot_paste(im, lambda dd, s: T.coupon(dd, s, "SNAP"), (250, 130), (640, 300), -9)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([40, 622, W - 40, 696], radius=24, fill=RED, outline=BLK, width=6)
    T.text_c(d, (W / 2, 660), "THE RULES NOBODY EXPLAINS", F(52), IVORY, stroke=3)
    return im


# ---------------------------------------------------------------- B: nonno su giallo
def build_b():
    im = C.bg()
    im = C.grandpa(im, 930, 300)
    im = C.sticker(im, 1165, 130, "MEDICAL", "COSTS COUNT", 250, 120, 8, (30, 150, 80), IVORY, 44, 24)
    im = C.sticker(im, 1175, 370, "60+", "ONLY", 190, 110, 6, GOLD, GREEN_D, 64, 24)
    im = C.sticker(im, 1130, 600, "SNAP", "FOR SENIORS", 280, 120, -7, RED, IVORY, 64, 24)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    L = [("THE", 90, 80, GREEN_D), ("$35", 270, 300, RED), ("RULE", 520, 170, GREEN_D)]
    for s_, y, sz, _ in L: sd.text((C.P(50), C.P(y)), s_, font=F(C.P(sz), "Black"), fill=(0, 0, 0, 190), anchor="lm")
    sh = sh.filter(ImageFilter.GaussianBlur(C.P(8))); base = im.convert("RGBA"); base.alpha_composite(sh, (C.P(8), C.P(12))); im = base.convert("RGB")
    d = ImageDraw.Draw(im)
    for s_, y, sz, col in L: d.text((C.P(50), C.P(y)), s_, font=F(C.P(sz), "Black"), fill=col, anchor="lm", stroke_width=C.P(10), stroke_fill=IVORY)
    d.text((C.P(50), C.P(650)), "NOBODY TELLS YOU", font=F(C.P(52), "Black"), fill=GREEN_D, anchor="lm", stroke_width=C.P(6), stroke_fill=IVORY)
    return im.resize((W, H), Image.LANCZOS)


# ---------------------------------------------------------------- C: chiara, X rossa sul test
def build_c():
    im = Image.new("RGB", (W, H), (250, 244, 228)); d = ImageDraw.Draw(im)
    for k in range(-2, 12):
        d.polygon([(k * 150, 0), (k * 150 + 70, 0), (k * 150 + 70 - 300, H), (k * 150 - 300, H)], fill=(244, 234, 208))
    d.rectangle([0, 0, W, 18], fill=GREEN_D); d.rectangle([0, H - 18, W, H], fill=GREEN_D)
    # carta del test
    lay = Image.new("RGBA", (520, 400), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.rounded_rectangle([8, 8, 512, 392], radius=26, fill=IVORY, outline=BLK, width=7)
    ld.rounded_rectangle([8, 8, 512, 96], radius=26, fill=GREEN_L, outline=BLK, width=7); ld.rectangle([14, 60, 506, 96], fill=GREEN_L)
    ld.text((260, 56), "GROSS INCOME TEST", font=F(40), fill=IVORY, anchor="mm")
    for i in range(4): ld.rounded_rectangle([44, 130 + i * 62, 476 - (i % 2) * 90, 168 + i * 62], radius=10, fill=(206, 200, 176))
    ld.text((260, 352), "$1,729", font=F(70, "Black"), fill=(120, 120, 110), anchor="mm")
    im = paste_rot(im, lay, (960, 300), 5)
    d = ImageDraw.Draw(im)
    # X rossa grande
    cx, cy = 965, 300
    d.line([cx - 230, cy - 190, cx + 230, cy + 190], fill=BLK, width=62); d.line([cx + 230, cy - 190, cx - 230, cy + 190], fill=BLK, width=62)
    d.line([cx - 230, cy - 190, cx + 230, cy + 190], fill=RED, width=44); d.line([cx + 230, cy - 190, cx - 230, cy + 190], fill=RED, width=44)
    # testo
    for s_, y, sz, col in (("SKIP THE", 130, 100, GREEN_D), ("INCOME", 250, 130, RED), ("TEST", 385, 130, RED)):
        T.text_c(d, (50, y), s_, F(sz, "Black"), col, stroke=9, sc=IVORY, anchor="lm")
    d.rounded_rectangle([40, 480, 640, 576], radius=30, fill=GREEN_D, outline=BLK, width=6)
    T.text_c(d, (340, 528), "AFTER AGE 60", F(66, "Black"), GOLD)
    im = food_bits(im, [("apple", 760, 610, -10, .7), ("bread", 910, 630, 6, .7), ("milk", 1040, 610, 8, .7), ("can", 1160, 630, -6, .7)])
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([40, 604, 660, 690], radius=26, fill=RED, outline=BLK, width=6)
    T.text_c(d, (350, 647), "SNAP RULE NOBODY EXPLAINS", F(32), IVORY)
    return im


if __name__ == "__main__":
    for n, f in (("A-verde-55-su-100", build_a), ("B-nonno-35-dollari", build_b), ("C-chiara-salta-il-test", build_c)):
        p = f"{OUT}/miniatura-video-lungo-2-{n}.png"; f().save(p); print(p)
