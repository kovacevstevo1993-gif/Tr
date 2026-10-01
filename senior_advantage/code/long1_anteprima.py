"""Anteprima video lungo 1 (1920x1080) con il motore degli short: stessi colori, font e sfondo."""
import os, sys, math
os.environ["SA_W"], os.environ["SA_H"] = "1920", "1080"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import *

RED = (214, 108, 96)
OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/anteprima")
os.makedirs(OUT, exist_ok=True)


def spaced(img, text, cx, cy, size=44, col=SAGE, gap=12, diamond=True):
    d = ImageDraw.Draw(img); f = font(FONT_SANS, size)
    tw = d.textlength(text, font=f) + gap * (len(text) - 1)
    x = cx - (tw + (70 if diamond else 0)) / 2
    if diamond:
        d.polygon([(x, cy), (x + 16, cy - 16), (x + 32, cy), (x + 16, cy + 16)], fill=col); x += 70
    for ch in text:
        d.text((x, cy), ch, font=f, fill=col, anchor="lm"); x += d.textlength(ch, font=f) + gap


def paste_rot(img, layer, angle, center):
    rgb, mask = layer
    r = rgb.rotate(angle, resample=Image.BICUBIC, center=center); m = mask.rotate(angle, resample=Image.BICUBIC, center=center)
    img.paste(r, (0, 0), m)


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


def hook(t=3.0):
    img = background(t); d = ImageDraw.Draw(img)
    spaced(img, "SENIOR DISCOUNTS", W // 2, 110, 46)
    shadow_text(img, (560, 300), "START AT", font(FONT_SANS, 110), IVORY, off=(5, 10), blur=14)
    shadow_text(img, (560, 610), "55", font(FONT_SERIF, 560), IVORY, off=(10, 22), blur=26)
    f2 = font(FONT_SANS, 150)
    shadow_text(img, (560, 945), "NOT 65", f2, RED, off=(6, 12), blur=16)
    tw = d.textlength("NOT 65", font=f2)
    d.line([560 - tw / 2 - 20, 950, 560 + tw / 2 + 20, 950], fill=RED, width=14)
    lay = new_layer(); banknote(lay[0], lay[1], 1450, 330, 560, 270, "SENIOR RATE", "ask before paying"); paste_rot(img, lay, 4, (1450, 330))
    lay = new_layer(); price_tag(lay[0], lay[1], 1690, 610, "55+", 340, 190); paste_rot(img, lay, -9, (1690, 610))
    lay = new_layer(); cart(lay[0], lay[1], 1290, 700, 1.1); alpha_layer(img, lay, 1)
    panel(img, [1130, 880, 1810, 1010], radius=34, border=GOLD, bw=5)
    d = ImageDraw.Draw(img)
    d.text((1470, 945), "AND NOBODY TELLS YOU", font=font(FONT_SANS, 50), fill=IVORY, anchor="mm")
    return img


def item(t=3.0):
    img = background(t); d = ImageDraw.Draw(img)
    spaced(img, "PLACE #1  ·  RESTAURANTS", W // 2, 110, 44)
    # anello che si riempie al 10%
    cx, cy, r = 600, 560, 290
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CARD, outline=SAGE_D, width=6)
    d.arc([cx - r + 30, cy - r + 30, cx + r - 30, cy + r - 30], -90, 270, fill=(30, 80, 64), width=34)
    d.arc([cx - r + 30, cy - r + 30, cx + r - 30, cy + r - 30], -90, -90 + 360 * .10, fill=GOLD, width=34)
    shadow_text(img, (cx, cy - 20), "10%", font(FONT_SERIF, 230), IVORY, off=(6, 12), blur=14)
    d.text((cx, cy + 135), "OFF", font=font(FONT_SANS, 64), fill=SAGE, anchor="mm")
    # piatto con cloche + scontrino
    lay = new_layer(); rgb, mask = lay; r_, m_ = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    px, py = 1330, 560
    for dr, c1, c2 in ((r_, (232, 228, 214), (200, 196, 182)), (m_, 255, 255)):
        dr.ellipse([px - 300, py + 60, px + 300, py + 200], fill=c1)
    r_.ellipse([px - 250, py + 80, px + 250, py + 170], fill=(246, 241, 229))
    r_.ellipse([px - 110, py + 90, px + 90, py + 150], fill=(112, 70, 40)); r_.ellipse([px + 110, py + 95, px + 190, py + 150], fill=(140, 190, 150))
    alpha_layer(img, lay, 1)
    lay = new_layer(); price_tag(lay[0], lay[1], 1330, 380, "AGE 55+", 480, 190); paste_rot(img, lay, -6, (1330, 380))
    panel(img, [1030, 830, 1790, 960], radius=34, border=GOLD, bw=5)
    d = ImageDraw.Draw(img)
    d.text((1410, 895), "ASK BEFORE THE TOTAL", font=font(FONT_SANS, 50), fill=IVORY, anchor="mm")
    d.text((W // 2, 1030), "Varies by location · confirm with the business", font=font(FONT_SANS_M, 28), fill=SAGE, anchor="mm")
    return img


if __name__ == "__main__":
    hook().save(f"{OUT}/1-gancio.png"); item().save(f"{OUT}/2-luogo-1-ristoranti.png"); print("ok")
