#!/usr/bin/env python3
"""Compone la scena 'tre porte colorate + pinguino' (porte disegnate da codice, pinguino SD-Turbo ritagliato con GrabCut), poi rifinitura img2img SD-Turbo."""
import cv2, numpy as np, torch
from PIL import Image, ImageDraw, ImageFilter
D = "assets/v/colori"
W, H = 720, 1280
def penguin():
    im = cv2.imread(f"{D}/pen_2.png"); h, w = im.shape[:2]
    mask = np.zeros((h, w), np.uint8); bg = np.zeros((1, 65)); fg = np.zeros((1, 65))
    cv2.grabCut(im, mask, (25, 15, w - 50, h - 25), bg, fg, 8, cv2.GC_INIT_WITH_RECT)
    m = np.where((mask == 1) | (mask == 3), 255, 0).astype(np.uint8)
    m = cv2.GaussianBlur(cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)), (5, 5), 0)
    rgba = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA); rgba[..., 3] = m
    out = Image.fromarray(rgba); return out.crop(out.getbbox())
def scene():
    img = Image.new("RGB", (W, H), (252, 240, 222)); d = ImageDraw.Draw(img)
    for y in range(H):                                                    # parete con sfumatura
        t = y / H; d.line([(0, y), (W, y)], fill=(int(255 - 18 * t), int(243 - 25 * t), int(226 - 40 * t)))
    d.rectangle([0, 760, W, H], fill=(214, 168, 118))                     # pavimento in legno
    for x in range(-40, W + 40, 90): d.line([(x, 760), (x - 60, H)], fill=(190, 145, 100), width=3)
    d.rectangle([0, 745, W, 775], fill=(255, 255, 255))                   # battiscopa
    cols = [(226, 36, 40), (255, 205, 20), (30, 100, 230)]; xs = [40, 265, 490]
    for c, x in zip(cols, xs):
        x0, y0, x1, y1 = x, 190, x + 190, 760
        d.rounded_rectangle([x0 - 14, y0 - 14, x1 + 14, y1], 12, fill=(250, 250, 250), outline=(205, 195, 180), width=3)   # cornice
        d.rounded_rectangle([x0, y0, x1, y1], 8, fill=c)
        dark = tuple(int(v * .78) for v in c)
        d.rounded_rectangle([x0 + 22, y0 + 28, x1 - 22, y0 + 250], 10, outline=dark, width=6)
        d.rounded_rectangle([x0 + 22, y0 + 290, x1 - 22, y1 - 28], 10, outline=dark, width=6)
        d.ellipse([x1 - 52, y0 + 270 - 40, x1 - 22, y0 + 270 - 10], fill=(245, 200, 60), outline=(150, 110, 20), width=3)  # maniglia
    return img.filter(ImageFilter.GaussianBlur(0.8))
if __name__ == "__main__":
    s = scene(); p = penguin(); ph = 400; p = p.resize((int(p.width * ph / p.height), ph), Image.LANCZOS)
    sh = Image.new("RGBA", s.size, (0, 0, 0, 0)); x = (W - p.width) // 2; y = 1180 - ph
    shadow = Image.new("RGBA", (p.width + 80, 60), (0, 0, 0, 0)); ImageDraw.Draw(shadow).ellipse([0, 0, p.width + 80, 60], fill=(0, 0, 0, 90))
    s.paste(shadow.filter(ImageFilter.GaussianBlur(10)), (x - 40, 1150), shadow.filter(ImageFilter.GaussianBlur(10)))
    s.paste(p, (x, y), p); s.save(f"{D}/compose.png"); print("ok")
