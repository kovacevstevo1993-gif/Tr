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


def receipt(img, x0, y0, x1, y1):
    """scontrino dettagliato: righe, sconto senior evidenziato, totale"""
    panel(img, [x0, y0, x1, y1], radius=26, fill=(246, 241, 229), border=(200, 190, 165), bw=4)
    d = ImageDraw.Draw(img); dark = GREEN_D
    d.text(((x0 + x1) / 2, y0 + 55), "RECEIPT", font=font(FONT_SANS, 40), fill=dark, anchor="mm")
    d.line([x0 + 40, y0 + 95, x1 - 40, y0 + 95], fill=(170, 160, 135), width=3)
    rows = [("Burger", "$12.50"), ("Fries", "$4.00"), ("Drink", "$3.50")]
    y = y0 + 140
    for a, b in rows:
        d.text((x0 + 50, y), a, font=font(FONT_SANS_M, 36), fill=dark, anchor="lm")
        d.text((x1 - 50, y), b, font=font(FONT_SANS_M, 36), fill=dark, anchor="rm"); y += 62
    d.line([x0 + 40, y - 10, x1 - 40, y - 10], fill=(170, 160, 135), width=3)
    d.text((x0 + 50, y + 35), "Subtotal", font=font(FONT_SANS_M, 36), fill=dark, anchor="lm")
    d.text((x1 - 50, y + 35), "$20.00", font=font(FONT_SANS_M, 36), fill=dark, anchor="rm")
    d.rounded_rectangle([x0 + 30, y + 80, x1 - 30, y + 160], radius=16, fill=GOLD)
    d.text((x0 + 46, y + 120), "SENIOR 10%", font=font(FONT_SANS, 34), fill=GREEN_D, anchor="lm")
    d.text((x1 - 46, y + 120), "\u2212$2.00", font=font(FONT_SANS, 34), fill=GREEN_D, anchor="rm")
    d.text((x0 + 50, y + 215), "TOTAL", font=font(FONT_SANS, 44), fill=dark, anchor="lm")
    d.text((x1 - 50, y + 215), "$18.00", font=font(FONT_SANS, 44), fill=dark, anchor="rm")


def item2(t=3.0):
    """luogo 1 piu' dettagliato: anello %, scontrino, piatto, didascalia grande"""
    img = background(t); d = ImageDraw.Draw(img)
    spaced(img, "PLACE #1  \u00b7  RESTAURANTS", W // 2, 90, 42)
    cx, cy, r = 430, 450, 240
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CARD, outline=SAGE_D, width=6)
    d.arc([cx - r + 28, cy - r + 28, cx + r - 28, cy + r - 28], -90, 270, fill=(30, 80, 64), width=30)
    d.arc([cx - r + 28, cy - r + 28, cx + r - 28, cy + r - 28], -90, -90 + 360 * .10, fill=GOLD, width=30)
    shadow_text(img, (cx, cy - 15), "10%", font(FONT_SERIF, 190), IVORY, off=(6, 10), blur=12)
    d.text((cx, cy + 110), "OFF", font=font(FONT_SANS, 56), fill=SAGE, anchor="mm")
    lay = new_layer(); price_tag(lay[0], lay[1], cx, 780, "AGE 55+", 420, 160); paste_rot(img, lay, -5, (cx, 780))
    receipt(img, 850, 190, 1330, 850)
    # piatto con cloche accanto allo scontrino
    lay = new_layer(); rgb, mask = lay; r_, m_ = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    px, py = 1590, 640
    for dr, c in ((r_, (232, 228, 214)), (m_, 255)):
        dr.ellipse([px - 250, py + 40, px + 250, py + 160], fill=c)
    r_.ellipse([px - 205, py + 58, px + 205, py + 138], fill=(246, 241, 229))
    for dr, c in ((r_, (190, 196, 190)), (m_, 255)):
        dr.pieslice([px - 170, py - 85, px + 170, py + 155], 180, 360, fill=c)
        dr.rounded_rectangle([px - 190, py + 135, px + 190, py + 160], radius=12, fill=c)
        dr.ellipse([px - 22, py - 110, px + 22, py - 66], fill=c)
    r_.pieslice([px - 125, py - 55, px - 20, py + 25], 200, 300, fill=(225, 230, 225))
    for k in range(3):
        sx = px - 70 + k * 70
        for dr, c in ((r_, (170, 200, 180)), (m_, 200)):
            dr.arc([sx - 25, py - 195, sx + 25, py - 125], 90, 270, fill=c, width=7)
    alpha_layer(img, lay, 1)
    # didascalia grande e chiara (per chi legge da lontano)
    panel(img, [180, 920, 1740, 1030], radius=34, border=GOLD, bw=5)
    d = ImageDraw.Draw(img)
    d.text((960, 975), "CHILI'S: 10% OFF FROM AGE 55", font=font(FONT_SANS, 62), fill=IVORY, anchor="mm")
    d.text((960, 1058), "Varies by location \u00b7 confirm with the business", font=font(FONT_SANS_M, 26), fill=SAGE, anchor="mm")
    return img


def closing(t=3.0):
    """ultima slide: disclaimer in chiaro + spazio per la schermata finale"""
    img = background(t); d = ImageDraw.Draw(img)
    spaced(img, "BEFORE YOU GO", W // 2, 120, 44)
    shadow_text(img, (560, 330), "ALWAYS ASK", font(FONT_SANS, 110), IVORY)
    shadow_text(img, (560, 470), "BEFORE YOU PAY", font(FONT_SANS, 90), GOLD)
    panel(img, [100, 620, 1020, 960], radius=34, border=SAGE_D, bw=4)
    d = ImageDraw.Draw(img)
    lines = ["Discounts, ages and prices change", "and differ by location and plan.", "Always confirm with the business", "or the official source before you rely on them.", "General information, not financial advice."]
    for i, l in enumerate(lines):
        d.text((560, 670 + i * 56), l, font=font(FONT_SANS_M, 36), fill=IVORY if i < 4 else SAGE, anchor="mm")
    # riquadro tratteggiato per la schermata finale di YouTube
    bx0, by0, bx1, by1 = 1150, 250, 1830, 710
    for x in range(bx0 + 20, bx1 - 20, 40):
        d.line([x, by0, x + 20, by0], fill=GOLD, width=4); d.line([x, by1, x + 20, by1], fill=GOLD, width=4)
    for y in range(by0 + 20, by1 - 20, 40):
        d.line([bx0, y, bx0, y + 20], fill=GOLD, width=4); d.line([bx1, y, bx1, y + 20], fill=GOLD, width=4)
    d.text(((bx0 + bx1) / 2, by1 + 50), "WATCH NEXT", font=font(FONT_SANS, 40), fill=GOLD, anchor="mm")
    return img


if __name__ == "__main__":
    hook().save(f"{OUT}/1-gancio.png"); item2().save(f"{OUT}/2-luogo-1-ristoranti.png"); closing().save(f"{OUT}/3-finale-disclaimer.png"); print("ok")
