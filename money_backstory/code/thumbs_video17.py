"""Miniature video 17 'Medicare Advantage Plan Not Renewed' - 2 prove con layout DIVERSI, 1280x720, a codice, niente volti.
Dopo aver guardato le miniature dei virali del tema (i.ytimg.com, Neal K. Shah 'Medicare Is Quietly Canceling Plans', 'Are You Next?'): testo enorme bianco con una parola in riquadro rosso,
timbro, freccia rossa, oggetti con ombra. A: lettera di non rinnovo + tessera Medicare + 'DEC 7 IS NOT THE LAST DAY'. B: pagina di calendario di dicembre 2026 con il 7 sbarrato e 'FEB 28' verde."""
import os, sys, math, random, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
import thumbs_video16 as T
from thumbs_video16 import gradient_bg, glow_spot, vignette, drop_shadow, text_grad, plain_text, ribbon, stamp_layer, WHITE, YEL, RED, GRN, BLK
from thumbs_video3_split import P, fit_font
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "miniature_video17"))
W, H = 1280, 720
random.seed(17); T.random.seed(17)

def notice_layer(w=560, h=640):
    L = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=10, fill=(246, 247, 250, 255), outline=(196, 202, 214, 255), width=3)
    d.rounded_rectangle([0, 0, w - 1, 112], radius=10, fill=(22, 52, 110, 255)); d.rectangle([0, 56, w - 1, 112], fill=(22, 52, 110, 255))
    d.ellipse([26, 20, 94, 88], outline=(246, 214, 140, 255), width=5); d.text((60, 54), "MA", font=P(30, True), fill=(246, 214, 140), anchor="mm")
    d.text((116, 36), "YOUR MEDICARE ADVANTAGE PLAN", font=P(22, True), fill=(190, 205, 235), anchor="lm"); d.text((116, 76), "NON-RENEWAL NOTICE", font=P(34, True), fill=(246, 214, 140), anchor="lm")
    d.text((36, 140), "OCTOBER 2026", font=P(26, True), fill=(90, 100, 124), anchor="lm")
    y = 180
    for ww in (420, 470, 360, 440):
        d.rounded_rectangle([36, y, 36 + ww, y + 18], radius=9, fill=(200, 206, 218, 255)); y += 42
    d.rounded_rectangle([26, y + 10, w - 26, y + 130], radius=14, fill=(255, 228, 228, 255), outline=RED + (255,), width=6)
    d.text((46, y + 44), "PLAN ENDS", font=P(30, True), fill=(120, 30, 36), anchor="lm"); d.text((w - 44, y + 88), "DEC 31", font=P(74, True), fill=(210, 30, 40), anchor="rm")
    y += 170
    for ww in (460, 390, 430):
        d.rounded_rectangle([36, y, 36 + ww, y + 18], radius=9, fill=(200, 206, 218, 255)); y += 42
    return L

def medicare_card(w=560, h=350):
    C = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(C)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=24, fill=(252, 252, 252, 255), outline=(170, 180, 200, 255), width=4)
    d.rounded_rectangle([4, 4, w - 5, 80], radius=20, fill=(0, 71, 155, 255)); d.rectangle([4, 40, w - 5, 80], fill=(0, 71, 155, 255)); d.rectangle([4, 80, w - 5, 94], fill=(200, 30, 45, 255))
    d.text((w / 2, 42), "MEDICARE", font=P(54, True), fill=(255, 255, 255), anchor="mm")
    d.text((28, 122), "HEALTH INSURANCE", font=P(22, True), fill=(0, 71, 155), anchor="lm")
    d.text((28, 172), "GLORIA SAMPLE", font=P(34, True), fill=(24, 48, 86), anchor="lm")
    d.text((28, 222), "MEDICARE NUMBER", font=P(18, True), fill=(110, 122, 144), anchor="lm"); d.text((28, 256), "1EG4-TE5-MK72", font=P(40, True), fill=(24, 48, 86), anchor="lm")
    d.text((28, 304), "HOSPITAL (PART A)   MEDICAL (PART B)", font=P(18, True), fill=(24, 48, 86), anchor="lm")
    d.ellipse([w - 120, h - 128, w - 28, h - 36], outline=(0, 71, 155, 255), width=5); d.rectangle([w - 84, h - 112, w - 64, h - 52], fill=(200, 30, 45, 255)); d.rectangle([w - 104, h - 92, w - 44, h - 72], fill=(200, 30, 45, 255))
    return C

def arrow_red(im, p0, p1, w=22):
    L = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0]); ex = (p1[0] - 28 * math.cos(ang), p1[1] - 28 * math.sin(ang))
    d.line([p0, ex], fill=(0, 0, 0, 255), width=w + 10); d.line([p0, ex], fill=RED + (255,), width=w)
    hd = [(p1[0], p1[1]), (p1[0] - 70 * math.cos(ang - 0.45), p1[1] - 70 * math.sin(ang - 0.45)), (p1[0] - 70 * math.cos(ang + 0.45), p1[1] - 70 * math.sin(ang + 0.45))]
    d.polygon(hd, fill=(0, 0, 0, 255)); d.polygon([(p1[0] - 8 * math.cos(ang), p1[1] - 8 * math.sin(ang)), (p1[0] - 62 * math.cos(ang - 0.45), p1[1] - 62 * math.sin(ang - 0.45)), (p1[0] - 62 * math.cos(ang + 0.45), p1[1] - 62 * math.sin(ang + 0.45))], fill=RED + (255,))
    return Image.alpha_composite(im, L)

def A():
    im = gradient_bg((6, 14, 34), (22, 52, 104), None, 0.6).convert("RGBA")
    im = glow_spot(im, 300, 460, 380, (60, 110, 220), 110); im = glow_spot(im, 1000, 330, 300, (255, 190, 60), 70)
    let = notice_layer(); let = let.resize((int(let.width * 0.70), int(let.height * 0.70)), Image.LANCZOS).rotate(-6, resample=Image.BICUBIC, expand=True); im = drop_shadow(im, let, (60, 322), (14, 22), 24, 210)
    card = medicare_card().resize((470, 294), Image.LANCZOS).rotate(7, resample=Image.BICUBIC, expand=True); im = drop_shadow(im, card, (730, 345), (14, 22), 24, 210)
    im = text_grad(im, "YOUR PLAN", P(125, True), 640, 85, (255, 255, 255), (214, 220, 236), 11)
    rb = Image.new("RGBA", (1100, 150), (0, 0, 0, 0)); d = ImageDraw.Draw(rb); d.rounded_rectangle([0, 0, 1099, 149], radius=10, fill=RED + (255,), outline=BLK + (255,), width=8)
    d.text((550, 78), "NOT RENEWED?", font=fit_font(d, "NOT RENEWED?", 1040, 120, True), fill=WHITE, anchor="mm", stroke_width=6, stroke_fill=(120, 10, 18))
    im = drop_shadow(im, rb.rotate(-1.5, resample=Image.BICUBIC, expand=True), (90, 150), (10, 16), 14, 190)
    im = ribbon(im, "DEC 7 IS NOT THE LAST DAY", (700, 650, 1260, 712), YEL, BLK, 38, -2)
    return vignette(im, 0.45).convert("RGB")

def calendar_layer(w=600, h=560):
    C = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(C)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=18, fill=(246, 247, 250, 255), outline=(196, 202, 214, 255), width=4)
    d.rounded_rectangle([0, 0, w - 1, 92], radius=18, fill=(200, 30, 45, 255)); d.rectangle([0, 50, w - 1, 92], fill=(200, 30, 45, 255))
    d.text((w / 2, 48), "DECEMBER 2026", font=P(48, True), fill=(255, 255, 255), anchor="mm")
    first = datetime.date(2026, 12, 1); wd0 = (first.weekday() + 1) % 7; cw = (w - 40) / 7; ch = (h - 150) / 6
    for j, nm in enumerate("SMTWTFS"): d.text((20 + cw * (j + 0.5), 112), nm, font=P(24, True), fill=(110, 122, 144), anchor="mm")
    for dn in range(1, 32):
        idx = wd0 + dn - 1; r_, c_ = divmod(idx, 7); bx = 20 + c_ * cw; by = 132 + r_ * ch
        col = (30, 130, 80) if dn >= 8 else ((200, 30, 45) if dn == 7 else None)
        if col: d.rounded_rectangle([bx + 3, by + 3, bx + cw - 3, by + ch - 5], radius=10, fill=col + (255,))
        d.text((bx + cw / 2, by + ch / 2), str(dn), font=P(34, True), fill=(255, 255, 255) if col else (24, 48, 86), anchor="mm")
        if dn == 7:
            d.ellipse([bx - 6, by - 6, bx + cw + 6, by + ch + 4], outline=(255, 255, 255, 255), width=6)
            d.line([bx + 12, by + 10, bx + cw - 12, by + ch - 12], fill=(255, 255, 255, 255), width=7); d.line([bx + cw - 12, by + 10, bx + 12, by + ch - 12], fill=(255, 255, 255, 255), width=7)
    return C

def B():
    im = gradient_bg((120, 14, 22), (14, 20, 44), None, 0.0).convert("RGBA")
    im = glow_spot(im, 300, 380, 360, (255, 90, 70), 90); im = glow_spot(im, 1000, 420, 340, (40, 160, 100), 80)
    cal = calendar_layer(); cal = cal.resize((int(cal.width * 0.9), int(cal.height * 0.9)), Image.LANCZOS).rotate(4, resample=Image.BICUBIC, expand=True); im = drop_shadow(im, cal, (20, 110), (14, 22), 24, 210)
    im = plain_text(im, "MEDICARE ADVANTAGE", P(46, True), 905, 60, YEL, 7)
    im = text_grad(im, "NOT YOUR", P(120, True), 905, 160, (255, 255, 255), (214, 220, 236), 12)
    im = text_grad(im, "LAST", P(190, True), 905, 320, (255, 244, 150), (255, 170, 20), 14)
    im = text_grad(im, "CHANCE", P(150, True), 905, 475, (255, 244, 150), (255, 170, 20), 14)
    st = stamp_layer("FEB 28", (30, 160, 88), 330, 120, 74).rotate(-8, resample=Image.BICUBIC, expand=True); im = drop_shadow(im, st, (620, 575), (6, 10), 8, 150)
    im = ribbon(im, "PLAN NOT RENEWED? READ THIS", (40, 640, 600, 705), WHITE, BLK, 38, 1)
    return vignette(im, 0.4).convert("RGB")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("video17-A-plan-not-renewed", A), ("video17-B-not-your-last-chance", B)):
        fn().save(os.path.join(OUT, name + ".png")); print("ok", name)
