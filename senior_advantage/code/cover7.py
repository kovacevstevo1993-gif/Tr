import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes7 import *

# Copertina short 7 (Costco): curiosita' + click. 1080x1920.
img = background(1.4)

# raggi dorati dietro il banco
ray = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(ray)
cx, cy = 540, 1060
for k in range(24):
    a0 = k * 15
    rd.pieslice([cx - 1600, cy - 1600, cx + 1600, cy + 1600], a0, a0 + 7.5, fill=(228, 179, 99, 50))
ray = ray.filter(ImageFilter.GaussianBlur(3))
base = img.convert("RGBA"); base.alpha_composite(ray); img.paste(base.convert("RGB"))

put(img, tag_spr("SENIORS 60+", 560, 112, CORAL, 62), 540, 190, rot=-3, shadow=14)

# titolo gigante
put(img, tspr("COSTCO", FONT_SANS, 215, IVORY), 540, 395, shadow=22)
put(img, tspr("NO CARD", FONT_SANS, 205, GOLD), 540, 600, shadow=22)
put(img, tspr("NEEDED?", FONT_SANS, 205, GOLD), 540, 790, shadow=22)

# banco della farmacia
put(img, glow_spr(), 540, 1260, scale=2.2, alpha=0.55)
put(img, glow_spr(), 540, 1260, scale=1.4, alpha=0.4)
put(img, counter_spr(), 540, 1235, scale=1.3, shadow=24, rot=-1)

# tessera barrata che vola
put(img, mcard_spr(), 800, 1470, scale=0.62, rot=12, shadow=16)
put(img, bigx_spr(), 800, 1470, scale=0.7, rot=12)

# anziano + punto interrogativo
put(img, glow_spr(), 190, 1590, scale=1.0, alpha=0.3)
put(img, elder_spr(), 190, 1590, scale=1.0, shadow=18)

put(img, tag_spr("MOST SENIORS MISS IT", 900, 150, CORAL, 62), 560, 1800, rot=-2, shadow=18)

out = os.environ.get("COVER_OUT", "copertina-short-07.png")
img.save(out); print("ok", out)
