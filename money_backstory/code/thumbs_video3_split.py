"""Miniature video 3 nello stile rosso/verde del video 1 e 2 (diagonale, numeri bianchi con contorno, riquadro bianco in alto)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import thumbs_video3 as T

W, H = 1280, 720
OUT = T.OUT
LN = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
LNN = "/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf"
if not os.path.exists(LNN):
    LNN = LN


def FN(size):
    return ImageFont.truetype(LNN, size)


def split_bg(cut_top=640, cut_bot=520):
    """rosso a sinistra, verde a destra, con luce radiale e taglio diagonale"""
    im = Image.new("RGB", (W, H))
    px = im.load()
    for y in range(H):
        xc = cut_top + (cut_bot - cut_top) * y / H
        for x in range(W):
            if x < xc:
                dx = (x - 300) / 700; dy = (y - 300) / 500
                v = max(0.0, 1 - (dx * dx + dy * dy) * .8)
                px[x, y] = (int(120 + 90 * v), int(15 + 25 * v), int(25 + 30 * v))
            else:
                dx = (x - 980) / 700; dy = (y - 380) / 500
                v = max(0.0, 1 - (dx * dx + dy * dy) * .8)
                px[x, y] = (int(8 + 15 * v), int(90 + 110 * v), int(45 + 45 * v))
    return im


def outlined(d, s, font, cx, y, fill=(255, 255, 255), stroke=10):
    b = d.textbbox((0, 0), s, font=font, stroke_width=stroke)
    d.text((cx - (b[2] - b[0]) / 2 - b[0], y - b[1]), s, font=font, fill=fill,
           stroke_width=stroke, stroke_fill=(0, 0, 0))


def top_box(d, s, size=52):
    f = FN(size)
    tw = d.textlength(s, font=f)
    x0 = W / 2 - tw / 2 - 40
    d.rounded_rectangle([x0, 22, x0 + tw + 80, 22 + size + 40], radius=14, fill=(255, 255, 255), outline=(0, 0, 0), width=4)
    d.text((W / 2, 22 + (size + 40) / 2), s, font=f, fill=(20, 32, 90), anchor="mm")


def bottom_pill(d, s, fill, fg, size=64, y=590):
    f = FN(size)
    tw = d.textlength(s, font=f)
    x0 = W / 2 - tw / 2 - 45
    d.rounded_rectangle([x0, y, x0 + tw + 90, y + size + 44], radius=26, fill=fill, outline=(0, 0, 0), width=6)
    d.text((W / 2, y + (size + 44) / 2 + 2), s, font=f, fill=fg, anchor="mm")


def small_arrow(d, cx, top, up, col):
    h = 95; w = 40
    if up:
        pts = [(cx - w, top + h * .5), (cx, top), (cx + w, top + h * .5), (cx + w * .5, top + h * .5), (cx + w * .5, top + h), (cx - w * .5, top + h), (cx - w * .5, top + h * .5)]
    else:
        pts = [(cx - w, top + h * .5), (cx, top + h), (cx + w, top + h * .5), (cx + w * .5, top + h * .5), (cx + w * .5, top), (cx - w * .5, top), (cx - w * .5, top + h * .5)]
    d.polygon(pts, fill=col, outline=(0, 0, 0))
    d.line(pts + [pts[0]], fill=(0, 0, 0), width=5)


YEL = (255, 214, 60)
RED = (224, 40, 40)


def s1():
    """Titolo 1: 59 (rosso, giu') vs 59 1/2 (verde, su') - 10.000 $"""
    im = split_bg(); d = ImageDraw.Draw(im)
    top_box(d, "THE 59½ RULE")
    outlined(d, "59", FN(330), 300, 90)
    outlined(d, "59½", FN(330), 950, 90)
    f = FN(64); d.text((595, 270), "VS", font=f, fill=YEL, anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
    small_arrow(d, 240, 400, False, RED); small_arrow(d, 985, 400, True, (40, 200, 90))
    d.text((240, 540), "10% PENALTY", font=FN(44), fill=(255, 255, 255), anchor="mm", stroke_width=5, stroke_fill=(0, 0, 0))
    d.text((985, 540), "PENALTY GONE", font=FN(44), fill=(255, 255, 255), anchor="mm", stroke_width=5, stroke_fill=(0, 0, 0))
    bottom_pill(d, "#4 IS A TRAP", YEL, (15, 15, 15), 44, 606)
    return im


def s2():
    """Titolo 2: 5 con triangolo + testo a destra + banda rossa"""
    im = split_bg(560, 470); d = ImageDraw.Draw(im)
    top_box(d, "401k 59½ RULE")
    outlined(d, "5", FN(400), 250, 115, stroke=12)
    T.warn(d, 250, 520, 70)
    for k, (line, col) in enumerate([("CHANGES", (255, 255, 255)), ("YOU MUST", YEL), ("CHECK", YEL)]):
        d.text((900, 220 + k * 105), line, font=FN(96), fill=col, anchor="mm", stroke_width=7, stroke_fill=(0, 0, 0))
    d.rounded_rectangle([260, 600, 1240, 700], radius=16, fill=RED, outline=(255, 255, 255), width=4)
    d.text((750, 650), "#4 IS A TRAP", font=FN(76), fill=(255, 255, 255), anchor="mm")
    return im


def s3():
    """Titolo 3: Frank (rosso, X) vs Mary (verde, V)"""
    im = split_bg(); d = ImageDraw.Draw(im)
    top_box(d, "HOW TO RETIRE AT 59½", 50)
    outlined(d, "FRANK", FN(120), 290, 135, stroke=8)
    outlined(d, "MARY", FN(120), 970, 135, stroke=8)
    T.cross(d, 290, 390, 80); T.check(d, 970, 390, 80)
    d.text((290, 520), "THINKS IT'S OVER", font=FN(40), fill=(255, 255, 255), anchor="mm", stroke_width=5, stroke_fill=(0, 0, 0))
    d.text((970, 520), "CHECKS THE 5 RULES", font=FN(40), fill=(255, 255, 255), anchor="mm", stroke_width=5, stroke_fill=(0, 0, 0))
    bottom_pill(d, "NOBODY WARNS YOU", YEL, (15, 15, 15), 46, 596)
    return im


if __name__ == "__main__":
    for n, f in {"titolo1-stile-rosso-verde": s1, "titolo2-stile-rosso-verde": s2, "titolo3-stile-rosso-verde": s3}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
