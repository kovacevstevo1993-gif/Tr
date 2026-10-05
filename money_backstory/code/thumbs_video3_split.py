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


MONT = f"{FD}/Montserrat.ttf"


def P(size, black=False):
    f = ImageFont.truetype(MONT, size)
    f.set_variation_by_axes([900 if black else 800])
    return f


def bg(cut_top=690, cut_bot=585):
    """rosso scuro a sinistra, verde a destra, macchie di luce e cucitura scura: colori misurati sul video 1"""
    im = Image.new("RGB", (W, H)); px = im.load()
    for y in range(H):
        xc = cut_top + (cut_bot - cut_top) * y / H
        for x in range(W):
            if x < xc:
                g = max(0.0, 1 - (((x - 330) / 430) ** 2 + ((y - 380) / 430) ** 2))
                seam = min(1.0, (xc - x) / 260)
                m = 0.62 + 0.38 * seam
                px[x, y] = (int((108 + 84 * g) * m), int((14 + 32 * g) * m), int((22 + 30 * g) * m))
            else:
                g = max(0.0, 1 - (((x - 1040) / 430) ** 2 + ((y - 330) / 430) ** 2))
                seam = min(1.0, (x - xc) / 260)
                m = 0.6 + 0.4 * seam
                px[x, y] = (int((8 + 22 * g) * m), int((104 + 80 * g) * m), int((37 + 40 * g) * m))
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
    col = (94, 250, 144) if up else (255, 90, 90)
    w, h, sh = 62, 96, 26
    if up:
        pts = [(cx, top), (cx + w, top + h * .5), (cx + sh, top + h * .5), (cx + sh, top + h), (cx - sh, top + h), (cx - sh, top + h * .5), (cx - w, top + h * .5)]
    else:
        pts = [(cx - sh, top), (cx + sh, top), (cx + sh, top + h * .5), (cx + w, top + h * .5), (cx, top + h), (cx - w, top + h * .5), (cx - sh, top + h * .5)]
    d.polygon(pts, fill=col)
    d.line(pts + [pts[0]], fill=BLK, width=6, joint="curve")


def big_num(d, base, sub, cx, baseline, size=300):
    """numero grande (e frazione piu' piccola) centrato su cx, con contorno nero come nel video 1"""
    f = P(size, True); f2 = P(int(size * .58), True)
    w1 = d.textlength(base, font=f); w2 = d.textlength(sub, font=f2) if sub else 0
    x0 = cx - (w1 + w2) / 2
    d.text((x0, baseline), base, font=f, fill=WHITE, anchor="ls", stroke_width=9, stroke_fill=BLK)
    if sub:
        d.text((x0 + w1 + 4, baseline), sub, font=f2, fill=WHITE, anchor="ls", stroke_width=7, stroke_fill=BLK)


def s1():
    """Titolo 1: 59 (giu') vs 59 1/2 (su')"""
    im = bg(); d = ImageDraw.Draw(im)
    label(d, "THE 59\u00bd RULE")
    big_num(d, "59", "", 245, 385, 275)
    big_num(d, "59", "½", 975, 385, 275)
    otext(d, "VS", P(84, True), 598, 318, fill=YEL, stroke=7)
    arrow(d, 245, 432, False); arrow(d, 975, 432, True)
    pill(d, "$10,000 SAVED OR TRAPPED?", maxw=1000)
    return im


def s2():
    """Titolo 2: sul modello del secondo test del video 2 - grande 5, triangolo, testo a destra, banda rossa"""
    im = bg(660, 600); d = ImageDraw.Draw(im)
    label(d, "401k 59½ RULE", maxw=640)
    otext(d, "5", P(350, True), 275, 270, stroke=10)
    T.warn(d, 275, 490, 58)
    for k, (line, col) in enumerate([("CHANGES", WHITE), ("YOU MUST", WHITE), ("CHECK", YEL)]):
        d.text((730, 210 + k * 112), line, font=P(84), fill=col, anchor="lm", stroke_width=7, stroke_fill=BLK)
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
