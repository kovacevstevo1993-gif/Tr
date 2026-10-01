"""Miniatura C video lungo 1 (The Senior Advantage): nonno dettagliato, giallo a raggi. Disegnata a 2x e ridotta."""
import os, math
from PIL import Image, ImageDraw, ImageFilter, ImageChops
from thumb_long1 import F, GREEN_D, GREEN_L, IVORY, GOLD, RED, BLK, OUT

S = 2
W, H = 1280 * S, 720 * S
SKIN = (240, 190, 150); SKIN_D = (212, 150, 112); SKIN_L = (255, 222, 190)
HAIR = (246, 246, 244); HAIR_D = (200, 204, 206)


def P(v): return v * S


def rg(size, c0, c1, center=None, r=None):
    w, h = size
    cx, cy = center or (w / 2, h / 2); r = r or max(w, h) / 2
    im = Image.new("RGB", size); px = im.load()
    for y in range(h):
        for x in range(w):
            t = min(1, math.hypot(x - cx, y - cy) / r)
            px[x, y] = tuple(int(c0[i] + (c1[i] - c0[i]) * t) for i in range(3))
    return im


def shape(img, mask_fn, fill, outline=BLK, ow=8, grad=None):
    """disegna una forma con maschera; fill = colore o (c0,c1) gradiente radiale"""
    m = Image.new("L", img.size, 0); mask_fn(ImageDraw.Draw(m), 255)
    if isinstance(fill[0], tuple):
        bb = m.getbbox(); sz = (bb[2] - bb[0], bb[3] - bb[1])
        g = rg(sz, fill[0], fill[1], center=(sz[0] * .38, sz[1] * .32), r=max(sz) * .75)
        full = Image.new("RGB", img.size); full.paste(g, (bb[0], bb[1])); img.paste(full, (0, 0), m)
    else:
        img.paste(Image.new("RGB", img.size, fill), (0, 0), m)
    if outline:
        bb = m.getbbox()
        if bb:
            k = ow * S // 2; pad = k + 2
            box = (max(0, bb[0] - pad), max(0, bb[1] - pad), min(img.width, bb[2] + pad), min(img.height, bb[3] + pad))
            mc = m.crop(box); big = mc.filter(ImageFilter.MaxFilter(2 * k + 1))
            ring = ImageChops.subtract(big, mc)
            img.paste(Image.new("RGB", mc.size, outline), (box[0], box[1]), ring)


def bg():
    im = Image.new("RGB", (W, H), (255, 212, 48)); d = ImageDraw.Draw(im)
    cx, cy = P(930), P(360)
    for k in range(18):
        a0 = k * 20
        d.pieslice([cx - P(1500), cy - P(1500), cx + P(1500), cy + P(1500)], a0, a0 + 10, fill=(255, 228, 100))
    vg = Image.new("L", (W, H), 0); ImageDraw.Draw(vg).ellipse([P(-300), P(-250), W + P(300), H + P(250)], fill=255)
    vg = vg.filter(ImageFilter.GaussianBlur(P(110)))
    return Image.composite(im, Image.new("RGB", (W, H), (208, 140, 14)), vg)


def grandpa(im, cx, cy):
    cx, cy = P(cx), P(cy)
    d = ImageDraw.Draw(im)
    def E(box): return [cx + P(box[0]), cy + P(box[1]), cx + P(box[2]), cy + P(box[3])]
    # corpo: cardigan
    shape(im, lambda dr, c: dr.pieslice(E([-300, 190, 300, 800]), 180, 360, fill=c) or dr.rectangle(E([-300, 500, 300, 520]), fill=0), (GREEN_L, GREEN_D))
    d = ImageDraw.Draw(im)
    # camicia + colletto
    d.polygon([(cx - P(70), cy + P(190)), (cx + P(70), cy + P(190)), (cx, cy + P(400))], fill=IVORY, outline=BLK, width=P(5))
    d.polygon([(cx - P(75), cy + P(185)), (cx - P(10), cy + P(215)), (cx - P(50), cy + P(280))], fill=(226, 222, 208), outline=BLK, width=P(4))
    d.polygon([(cx + P(75), cy + P(185)), (cx + P(10), cy + P(215)), (cx + P(50), cy + P(280))], fill=(226, 222, 208), outline=BLK, width=P(4))
    # papillon rosso
    d.polygon([(cx, cy + P(228)), (cx - P(62), cy + P(200)), (cx - P(62), cy + P(262))], fill=RED, outline=BLK, width=P(5))
    d.polygon([(cx, cy + P(228)), (cx + P(62), cy + P(200)), (cx + P(62), cy + P(262))], fill=RED, outline=BLK, width=P(5))
    d.ellipse(E([-18, 212, 18, 248]), fill=(180, 30, 30), outline=BLK, width=P(4))
    # bottoni cardigan
    for y in (330, 410):
        d.ellipse(E([-10 + 0, y, 14, y + 24]), fill=GOLD, outline=BLK, width=P(3))
    # collo
    shape(im, lambda dr, c: dr.rounded_rectangle(E([-60, 120, 60, 215]), radius=P(30), fill=c), (SKIN, SKIN_D), ow=5)
    # capelli laterali (nuvole) dietro la testa
    for sx in (-1, 1):
        for (bx, by, r) in ((172, -10, 70), (190, -75, 62), (150, -125, 58), (205, 40, 52)):
            shape(im, lambda dr, c, sx=sx, bx=bx, by=by, r=r: dr.ellipse(E([sx * bx - r, by - r, sx * bx + r, by + r]), fill=c), (HAIR, HAIR_D), ow=6)
    # orecchie
    for sx in (-1, 1):
        shape(im, lambda dr, c, sx=sx: dr.ellipse(E([sx * 150 - 34, -40, sx * 150 + 34, 70]), fill=c), (SKIN, SKIN_D), ow=6)
        ImageDraw.Draw(im).arc(E([sx * 150 - 16, -16, sx * 150 + 16, 42]), 0, 360, fill=SKIN_D, width=P(5))
    # testa
    shape(im, lambda dr, c: dr.ellipse(E([-160, -190, 160, 190]), fill=c), (SKIN_L, SKIN), ow=9)
    d = ImageDraw.Draw(im)
    # ciuffo sulla fronte (pochi capelli)
    shape(im, lambda dr, c: dr.pieslice(E([-95, -220, 95, -60]), 195, 345, fill=c), (HAIR, HAIR_D), ow=6)
    # rughe fronte
    for k, y in enumerate((-118, -100)):
        d.arc(E([-70 + k * 8, y - 14, 70 - k * 8, y + 22]), 200, 340, fill=SKIN_D, width=P(5))
    # guance rosa
    ch = Image.new("RGBA", im.size, (0, 0, 0, 0)); cd = ImageDraw.Draw(ch)
    for sx in (-1, 1): cd.ellipse(E([sx * 98 - 46, 55, sx * 98 + 46, 120]), fill=(238, 110, 100, 120))
    ch = ch.filter(ImageFilter.GaussianBlur(P(14))); im.paste(Image.alpha_composite(im.convert("RGBA"), ch).convert("RGB"), (0, 0)); d = ImageDraw.Draw(im)
    # sopracciglia cespugliose (alzate, sorpresa)
    for sx in (-1, 1):
        pts = [(sx * 22, -88), (sx * 40, -116), (sx * 80, -134), (sx * 120, -116), (sx * 140, -92), (sx * 120, -100), (sx * 80, -112), (sx * 42, -94)]
        d.polygon([(cx + P(x), cy + P(y)) for x, y in pts], fill=HAIR, outline=BLK, width=P(5))
    # occhi dentro occhiali
    for sx in (-1, 1):
        ex = sx * 68
        d.ellipse(E([ex - 50, -75, ex + 50, 25]), fill=(255, 255, 255), outline=BLK, width=P(4))
        d.ellipse(E([ex - 24, -50, ex + 24, 2]), fill=(122, 78, 40)); d.ellipse(E([ex - 12, -38, ex + 12, -14]), fill=BLK)
        d.ellipse(E([ex - 16 + 6, -46, ex - 2 + 6, -34]), fill=(255, 255, 255))
        # borse sotto gli occhi
        d.arc(E([ex - 48, 14, ex + 48, 54]), 20, 160, fill=SKIN_D, width=P(4))
    # lenti (riflesso) e montatura dorata
    lens = Image.new("RGBA", im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lens)
    for sx in (-1, 1):
        ex = sx * 68
        ld.ellipse(E([ex - 54, -80, ex + 54, 30]), fill=(180, 225, 255, 55))
        ld.polygon([(cx + P(ex - 36), cy + P(-62)), (cx + P(ex - 12), cy + P(-72)), (cx + P(ex - 40), cy + P(-30))], fill=(255, 255, 255, 140))
    im.paste(Image.alpha_composite(im.convert("RGBA"), lens).convert("RGB"), (0, 0)); d = ImageDraw.Draw(im)
    for sx in (-1, 1):
        ex = sx * 68
        d.ellipse(E([ex - 54, -80, ex + 54, 30]), outline=(214, 160, 40), width=P(9))
        d.ellipse(E([ex - 54, -80, ex + 54, 30]), outline=BLK, width=P(2))
    d.arc(E([-24, -62, 24, -34]), 200, 340, fill=(214, 160, 40), width=P(8))
    for sx in (-1, 1): d.line([cx + P(sx * 120), cy + P(-40), cx + P(sx * 158), cy + P(-20)], fill=(214, 160, 40), width=P(7))
    # naso
    shape(im, lambda dr, c: dr.ellipse(E([-34, -8, 34, 70]), fill=c), (SKIN_L, SKIN_D), ow=6)
    d = ImageDraw.Draw(im)
    d.ellipse(E([-18, 48, -4, 62]), fill=SKIN_D); d.ellipse(E([4, 48, 18, 62]), fill=SKIN_D)
    # bocca aperta con denti e lingua
    shape(im, lambda dr, c: dr.pieslice(E([-80, 80, 80, 175]), 0, 180, fill=c) or dr.ellipse(E([-80, 100, 80, 175]), fill=c), (70, 15, 20), ow=7) if False else None
    mouth = lambda dr, c: dr.ellipse(E([-72, 92, 72, 172]), fill=c)
    shape(im, mouth, (74, 14, 22), ow=7)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(E([-56, 98, 56, 124]), radius=P(10), fill=(255, 255, 255), outline=BLK, width=P(3))
    for x in (-28, 0, 28): d.line([cx + P(x), cy + P(100), cx + P(x), cy + P(122)], fill=(190, 190, 190), width=P(3))
    d.ellipse(E([-40, 138, 40, 176]), fill=(226, 96, 110))
    # baffi bianchi a manubrio
    for sx in (-1, 1):
        pts = [(sx * 4, 76), (sx * 40, 70), (sx * 86, 82), (sx * 112, 66), (sx * 104, 100), (sx * 60, 108), (sx * 8, 92)]
        shape(im, lambda dr, c, pts=pts: dr.polygon([(cx + P(x), cy + P(y)) for x, y in pts], fill=c), (HAIR, HAIR_D), ow=5)
    return im


def pricetag(im, cx, cy, ang):
    w, h = P(420), P(230)
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([P(8), P(8), w - P(8), h - P(8)], radius=P(34), fill=GOLD, outline=BLK, width=P(7))
    d.ellipse([P(30), h / 2 - P(22), P(74), h / 2 + P(22)], fill=(255, 212, 48), outline=BLK, width=P(5))
    d.text((w / 2 + P(24), h / 2 - P(14)), "55+", font=F(P(120), "Black"), fill=GREEN_D, anchor="mm")
    d.text((w / 2 + P(24), h / 2 + P(70)), "SENIOR PRICE", font=F(P(28)), fill=GREEN_D, anchor="mm")
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0)); sh.paste(Image.new("RGBA", lay.size, (0, 0, 0, 160)), (0, 0), lay.split()[3]); sh = sh.filter(ImageFilter.GaussianBlur(P(8)))
    lay = lay.rotate(ang, expand=True, resample=Image.BICUBIC); sh = sh.rotate(ang, expand=True, resample=Image.BICUBIC)
    x, y = int(P(cx) - lay.width / 2), int(P(cy) - lay.height / 2)
    base = im.convert("RGBA"); base.alpha_composite(sh, (x + P(8), y + P(12))); base.alpha_composite(lay, (x, y))
    return base.convert("RGB")


def hand(im, x, y, flip=False):
    d = ImageDraw.Draw(im)
    def E(b): return [P(x + b[0] * (-1 if flip else 1) - (0 if not flip else 0)), P(y + b[1]), P(x + b[2] * (-1 if flip else 1)), P(y + b[3])]
    for k in range(4):
        d.rounded_rectangle([P(x + k * 34 - 60), P(y - 12), P(x + k * 34 - 28), P(y + 62)], radius=P(16), fill=SKIN, outline=BLK, width=P(4))
    d.rounded_rectangle([P(x - 70), P(y + 40), P(x + 80), P(y + 140)], radius=P(36), fill=SKIN, outline=BLK, width=P(5))
    d.ellipse([P(x + 62), P(y - 12), P(x + 112), P(y + 60)], fill=SKIN, outline=BLK, width=P(4))
    d.rectangle([P(x - 60), P(y + 130), P(x + 80), P(y + 180)], fill=GREEN_L, outline=BLK, width=P(4))


def build():
    im = bg()
    im = grandpa(im, 930, 300)
    im = pricetag(im, 1120, 590, -8)

    # titolo
    L = [("STOP", 95, GREEN_D), ("PAYING", 255, GREEN_D), ("FULL", 415, RED), ("PRICE", 560, RED)]
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    for s_, y, _ in L: sd.text((P(50), P(y)), s_, font=F(P(150), "Black"), fill=(0, 0, 0, 190), anchor="lm")
    sh = sh.filter(ImageFilter.GaussianBlur(P(8))); base = im.convert("RGBA"); base.alpha_composite(sh, (P(8), P(12))); im = base.convert("RGB")
    d = ImageDraw.Draw(im)
    for s_, y, col in L: d.text((P(50), P(y)), s_, font=F(P(150), "Black"), fill=col, anchor="lm", stroke_width=P(10), stroke_fill=IVORY)
    return im.resize((1280, 720), Image.LANCZOS)


if __name__ == "__main__":
    p = f"{OUT}/video-lungo-1-nonno-stop-paying-full-price.png"; build().save(p); print(p)
