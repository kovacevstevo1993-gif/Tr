"""Miniatura B video lungo 1 (The Senior Advantage): giallo acceso, personaggio sorpreso, scontrino barrato."""
import os, math
from PIL import Image, ImageDraw, ImageFilter
from thumb_long1 import F, W, H, GREEN_D, GREEN_L, IVORY, GOLD, RED, BLK, SAGE, shadow, text_c, rot_paste, OUT

SKIN = (243, 200, 160); HAIR = (250, 250, 250); YEL = (255, 214, 54)


def bg():
    im = Image.new("RGB", (W, H), YEL); d = ImageDraw.Draw(im)
    cx, cy = 930, 380
    for k in range(24):
        a0 = k * 15; 
        d.pieslice([cx - 1400, cy - 1400, cx + 1400, cy + 1400], a0, a0 + 7.5, fill=(255, 226, 96))
    vg = Image.new("L", (W, H), 0); ImageDraw.Draw(vg).ellipse([-250, -200, W + 250, H + 200], fill=255)
    vg = vg.filter(ImageFilter.GaussianBlur(120))
    dark = Image.new("RGB", (W, H), (214, 150, 20))
    return Image.composite(im, dark, vg)


def person(im, cx, cy):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    # busto verde
    d.pieslice([cx - 260, cy + 140, cx + 260, cy + 640], 180, 360, fill=GREEN_L, outline=BLK, width=8)
    d.polygon([(cx - 40, cy + 150), (cx, cy + 215), (cx + 40, cy + 150)], fill=IVORY, outline=BLK)
    # capelli bianchi
    for dx in (-165, 165):
        d.ellipse([cx + dx - 85, cy - 120, cx + dx + 85, cy + 60], fill=HAIR, outline=BLK, width=8)
        # testa
    d.ellipse([cx - 188, cy - 262, cx + 188, cy + 20], fill=HAIR, outline=BLK, width=8)
    d.ellipse([cx - 165, cy - 170, cx + 165, cy + 170], fill=SKIN, outline=BLK, width=8)
    
    # occhiali + occhi enormi
    for dx in (-72, 72):
        d.ellipse([cx + dx - 62, cy - 60, cx + dx + 62, cy + 64], fill=IVORY, outline=BLK, width=9)
        d.ellipse([cx + dx - 22, cy - 22, cx + dx + 22, cy + 22], fill=BLK)
        d.ellipse([cx + dx - 10, cy - 14, cx + dx + 2, cy - 2], fill=IVORY)
    d.line([cx - 10, cy + 0, cx + 10, cy + 0], fill=BLK, width=9)
    # sopracciglia alzate
    for dx, s in ((-72, 1), (72, -1)):
        d.line([cx + dx - 55, cy - 95 + 10 * s, cx + dx + 55, cy - 108 - 10 * s], fill=(90, 90, 90), width=14)
    # bocca aperta
    d.ellipse([cx - 62, cy + 85, cx + 62, cy + 160], fill=(80, 20, 20), outline=BLK, width=8)
    d.ellipse([cx - 36, cy + 128, cx + 36, cy + 158], fill=(224, 100, 110))
    return Image.alpha_composite(im.convert("RGBA"), lay).convert("RGB")


def receipt(d, size):
    w, h = size
    d.rounded_rectangle([8, 8, w - 8, h - 8], radius=18, fill=IVORY, outline=BLK, width=7)
    d.text((w / 2, 42), "RECEIPT", font=F(34), fill=GREEN_D, anchor="mm")
    d.line([30, 72, w - 30, 72], fill=(150, 150, 140), width=4)
    d.text((40, 118), "BEFORE", font=F(36), fill=(90, 90, 90), anchor="lm")
    d.text((w - 40, 118), "$50", font=F(58, "Black"), fill=RED, anchor="rm")
    d.line([w - 190, 118, w - 30, 118], fill=RED, width=9)
    d.line([30, 162, w - 30, 162], fill=(150, 150, 140), width=4)
    d.text((40, 218), "NOW", font=F(40), fill=GREEN_D, anchor="lm")
    d.text((w - 40, 214), "$40", font=F(80, "Black"), fill=(20, 150, 70), anchor="rm")


def build():
    im = bg()
    im = person(im, 960, 300)
    im = rot_paste(im, receipt, (400, 270), (1070, 575), -6)
    # titolo a sinistra
    d = ImageDraw.Draw(im)
    L = [("STOP", 100, 150, GREEN_D), ("PAYING", 270, 150, GREEN_D), ("FULL", 440, 150, RED), ("PRICE", 590, 150, RED)]
    def t(dr, c):
        for s_, y, sz, _ in L: dr.text((50, y), s_, font=F(sz, "Black"), fill=c, anchor="lm")
    im = shadow(im, t, off=(8, 12), blur=8, alpha=190)
    d = ImageDraw.Draw(im)
    for s_, y, sz, col in L: d.text((50, y), s_, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=10, stroke_fill=IVORY)
    d.ellipse([1110, 40, 1270, 200], fill=GOLD, outline=BLK, width=7)
    d.text((1190, 105), "55+", font=F(60, "Black"), fill=GREEN_D, anchor="mm")
    d.text((1190, 158), "OFF", font=F(30), fill=GREEN_D, anchor="mm")
    return im


if __name__ == "__main__":
    p = f"{OUT}/video-lungo-1-stop-paying-full-price.png"; build().save(p); print(p)
