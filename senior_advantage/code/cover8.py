import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes8 import *

# Copertina short 8 (Bollette): curiosita' + click. 1080x1920.
img = background(1.4)
ray = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(ray)
cx, cy = 540, 1150
for k in range(24):
    a0 = k * 15
    rd.pieslice([cx - 1600, cy - 1600, cx + 1600, cy + 1600], a0, a0 + 7.5, fill=(228, 179, 99, 50))
ray = ray.filter(ImageFilter.GaussianBlur(3))
base = img.convert("RGBA"); base.alpha_composite(ray); img.paste(base.convert("RGB"))

put(img, tag_spr("SENIORS 60+", 560, 112, CORAL, 62), 540, 190, rot=-3, shadow=14)
put(img, tspr("7 BILLS", FONT_SANS, 250, IVORY), 540, 395, shadow=22)
put(img, tspr("YOU PAY", FONT_SANS, 205, GOLD), 540, 600, shadow=22)
put(img, tspr("IN FULL?", FONT_SANS, 205, GOLD), 540, 790, shadow=22)

# sei bollette piccole in fila + la casa (la settima) con il premio
kinds = (("HEAT", CORAL), ("POWER", GOLD), ("PHONE", SAGE), ("FOOD", CORAL), ("BOX", GOLD), ("BUS", SAGE))
for i, (w, col) in enumerate(kinds):
    put(img, bill_spr(w, col), 130 + i * 164, 1030, scale=0.42, rot=-6 + 3 * i, shadow=10)
put(img, glow_spr(), 560, 1400, scale=2.2, alpha=0.55)
put(img, glow_spr(), 560, 1400, scale=1.4, alpha=0.4)
put(img, house_spr(), 640, 1375, scale=0.85, shadow=24, rot=-1)
put(img, tag_spr("#7 = UP TO $10,000", 860, 150, GOLD, 70), 600, 1620, rot=-2, shadow=18)
put(img, glow_spr(), 170, 1360, scale=1.0, alpha=0.3)
put(img, elder_spr(), 170, 1360, scale=0.9, shadow=18)
put(img, tag_spr("NOBODY CALLS TO TELL YOU", 940, 140, CORAL, 56), 540, 1810, rot=-2, shadow=18)

out = os.environ.get("COVER_OUT", "copertina-short-08.png")
img.save(out); print("ok", out)
