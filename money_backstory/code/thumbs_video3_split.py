"""Miniature video 3 nello stile rosso/verde dei video 1 e 2 (misurate dallo screenshot di 'Social Security 62 vs 70')."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import thumbs_video3 as T

W, H = 1280, 720
OUT = T.OUT
FD = os.path.join(os.path.dirname(__file__), "fonts")
XB, BLACKF = f"{FD}/Poppins-ExtraBold.ttf", f"{FD}/Poppins-Black.ttf"
NAVY = (20, 38, 105)
YEL = (254, 214, 67)
BLK = (0, 0, 0)
WHITE = (255, 255, 255)


def P(size, black=False):
    return ImageFont.truetype(BLACKF if black else XB, size)


def bg(cut_top=690, cut_bot=585):
    """rosso scuro a sinistra, verde a destra, luce interna e cucitura scura al centro"""
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        xc = cut_top + (cut_bot - cut_top) * y / H
        for x in range(W):
            if x < xc:
                dx = (x - 290) / 560; dy = (y - 330) / 520
                v = max(0.0, 1 - (dx * dx + dy * dy))
                seam = min(1.0, (xc - x) / 220)
                k = v * (0.55 + 0.45 * seam)
                px[x, y] = (int(105 + 95 * k), int(14 + 34 * k), int(22 + 30 * k))
            else:
                dx = (x - 1010) / 560; dy = (y - 300) / 520
                v = max(0.0, 1 - (dx * dx + dy * dy))
                seam = min(1.0, (x - xc) / 220)
                k = v * (0.5 + 0.5 * seam)
                px[x, y] = (int(4 + 34 * k), int(60 + 135 * k), int(22 + 62 * k))
    return im


def otext(d, s, font, cx, cy, fill=WHITE, stroke=8, sc=BLK):
    d.text((cx, cy), s, font=font, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=sc)


def fit_font(d, s, maxw, start, black=False):
    size = start
    while size > 20 and d.textlength(s, font=P(size, black)) > maxw:
        size -= 2
    return P(size, black)


def label(d, s, y0=20, h=100, maxw=760):
    f = fit_font(d, s, maxw, 76)
    tw = d.textlength(s, font=f)
    x0 = W / 2 - tw / 2 - 46
    d.rounded_rectangle([x0, y0, x0 + tw + 92, y0 + h], radius=22, fill=WHITE, outline=BLK, width=5)
    d.text((W / 2, y0 + h / 2 + 2), s, font=f, fill=NAVY, anchor="mm")


def pill(d, s, y0=562, h=136, maxw=880, fill=YEL, fg=(20, 20, 20)):
    f = fit_font(d, s, maxw, 92)
    tw = d.textlength(s, font=f)
    x0 = W / 2 - tw / 2 - 52
    d.rounded_rectangle([x0, y0, x0 + tw + 104, y0 + h], radius=34, fill=fill, outline=BLK, width=6)
    d.text((W / 2, y0 + h / 2 + 3), s, font=f, fill=fg, anchor="mm")


def arrow(d, cx, top, up):
    """frecce come nel video 1: piccole, con contorno nero e tinta chiara"""
    col = (98, 232, 140) if up else (236, 80, 80)
    w, h, sh = 78, 118, 34
    if up:
        pts = [(cx, top), (cx + w, top + h * .5), (cx + sh, top + h * .5), (cx + sh, top + h), (cx - sh, top + h), (cx - sh, top + h * .5), (cx - w, top + h * .5)]
    else:
        pts = [(cx - sh, top), (cx + sh, top), (cx + sh, top + h * .5), (cx + w, top + h * .5), (cx, top + h), (cx - w, top + h * .5), (cx - sh, top + h * .5)]
    d.polygon(pts, fill=col)
    d.line(pts + [pts[0]], fill=BLK, width=6, joint="curve")


def s1():
    """Titolo 1: 59 (giu') vs 59 1/2 (su')"""
    im = bg(); d = ImageDraw.Draw(im)
    label(d, "THE 59½ RULE")
    otext(d, "59", P(250, True), 250, 275)
    otext(d, "59½", P(250, True), 965, 275)
    otext(d, "VS", P(80, True), 600, 300, fill=YEL, stroke=7)
    arrow(d, 250, 420, False); arrow(d, 965, 420, True)
    pill(d, "$10,000 SAVED OR TRAPPED?", maxw=1000)
    return im


def s2():
    """Titolo 2: sul modello del secondo test del video 2 - grande 5, triangolo, testo a destra, banda rossa"""
    im = bg(660, 600); d = ImageDraw.Draw(im)
    label(d, "401k 59½ RULE", maxw=640)
    otext(d, "5", P(350, True), 275, 270, stroke=10)
    T.warn(d, 275, 490, 58)
    for k, (line, col) in enumerate([("CHANGES", WHITE), ("YOU MUST", WHITE), ("CHECK", YEL)]):
        d.text((730, 210 + k * 112), line, font=P(92), fill=col, anchor="lm", stroke_width=7, stroke_fill=BLK)
    d.rounded_rectangle([170, 600, 1110, 704], radius=18, fill=(224, 40, 40), outline=WHITE, width=5)
    d.text((640, 654), "#4 IS A TRAP", font=P(78), fill=WHITE, anchor="mm")
    return im


def s3():
    """Titolo 3: Frank (rosso) vs Mary (verde)"""
    im = bg(); d = ImageDraw.Draw(im)
    label(d, "RETIRE AT 59½")
    otext(d, "FRANK", P(128, True), 285, 250)
    otext(d, "MARY", P(128, True), 985, 250)
    otext(d, "VS", P(80, True), 640, 330, fill=YEL, stroke=7)
    T.cross(d, 285, 440, 62); T.check(d, 985, 440, 62)
    pill(d, "NOBODY WARNS YOU", maxw=900)
    return im


if __name__ == "__main__":
    for n, f in {"titolo1-stile-rosso-verde": s1, "titolo2-stile-rosso-verde": s2, "titolo3-stile-rosso-verde": s3}.items():
        f().save(f"{OUT}/{n}.png"); print("ok", n)
