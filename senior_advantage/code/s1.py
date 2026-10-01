import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from engine import *

DUR = 5.4

def draw(img, t):
    d = ImageDraw.Draw(img)

    # --- etichetta in alto ---
    a = seg(t, 0.0, 0.5)
    if a > 0:
        y = 300 - 40 * (1 - ease(a))
        lay = new_layer(); rgb, mask = lay
        dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
        txt = "SENIOR DISCOUNTS"
        f = font(FONT_SANS, 42)
        tw = dr.textlength(txt, font=f) + 12 * (len(txt) - 1)
        x = W//2 - (tw + 70) / 2
        dr.polygon([(x, y), (x+16, y-16), (x+32, y), (x+16, y+16)], fill=SAGE)
        dm.polygon([(x, y), (x+16, y-16), (x+32, y), (x+16, y+16)], fill=255)
        cx = x + 70
        for ch in txt:
            dr.text((cx, y), ch, font=f, fill=SAGE, anchor="lm")
            dm.text((cx, y), ch, font=f, fill=255, anchor="lm")
            cx += dr.textlength(ch, font=f) + 12
        alpha_layer(img, lay, ease(a))

    # --- "MOST START AT" ---
    a = seg(t, 0.25, 0.5)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        for dr, col in ((ImageDraw.Draw(rgb), IVORY), (ImageDraw.Draw(mask), 255)):
            dr.text((W//2, 470), "MOST START AT", font=font(FONT_SANS, 76), fill=col, anchor="mm")
        alpha_layer(img, lay, ease(a))

    # --- numero grande che sale ---
    a = seg(t, 0.35, 0.55)
    if a > 0:
        p = ease_back(a)
        val = int(30 + (55 - 30) * ease(seg(t, 0.4, 1.3)))
        size = int(430 * min(1.0, p))
        if size > 20:
            f = font(FONT_SERIF, size)
            shadow_text(img, (W//2 - 60, 790), str(val), f, IVORY, off=(8, 18), blur=22)
            fy = font(FONT_SANS, int(70 * min(1.0, p)))
            d.text((W//2 + 210, 900), "YEARS", font=fy, fill=SAGE, anchor="lm")

    # --- tessera sconto che entra dal basso ---
    a = seg(t, 1.5, 0.6)
    if a > 0:
        lay = new_layer()
        banknote(lay[0], lay[1], W//2, 1180 + int(90 * (1 - ease(a))))
        alpha_layer(img, lay, ease(a))

    # --- NOT SIXTY-FIVE ---
    a = seg(t, 2.6, 0.55)
    if a > 0:
        p = min(1.0, ease_back(a))
        f = font(FONT_SANS, int(92 * p))
        if f.size > 10:
            shadow_text(img, (W//2, 1450), "NOT SIXTY-FIVE", f, GOLD, off=(5, 10), blur=14)

    # --- barra che si riempie ---
    a = seg(t, 3.1, 1.4)
    if a > 0:
        bw, bh, by = 660, 22, 1640
        x0 = W//2 - bw//2
        d.rounded_rectangle([x0, by, x0+bw, by+bh], radius=11, fill=CARD)
        fw = int(bw * ease(a))
        if fw > bh:
            d.rounded_rectangle([x0, by, x0+fw, by+bh], radius=11, fill=SAGE)

render(draw, DUR, "/mnt/user-data/outputs/slide-01.mp4")
print("ok")
