import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes6 import *

img = background(1.4)
d = ImageDraw.Draw(img)

# raggi dorati dietro la scatola
ray = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(ray)
cx, cy = 540, 1000
for k in range(24):
    a0 = k * 15
    rd.pieslice([cx - 1500, cy - 1500, cx + 1500, cy + 1500], a0, a0 + 7.5, fill=(228, 179, 99, 46))
ray = ray.filter(ImageFilter.GaussianBlur(3))
base = img.convert("RGBA"); base.alpha_composite(ray); img.paste(base.convert("RGB"))

put(img, tag_spr("SENIORS 60+", 560, 112, CORAL, 62), 540, 200, rot=-3, shadow=14)

# titolo grande a due righe, con contorno
for txt, y, sz, col in (("MONTHLY", 425, 195, IVORY), ("FOOD BOX", 625, 185, GOLD)):
    sp = tspr(txt, FONT_SANS, sz, col)
    put(img, sp, 540, y, shadow=20)

# esplosione dietro la scatola
put(img, glow_spr(), 540, 1130, scale=2.2, alpha=0.55)
put(img, glow_spr(), 540, 1130, scale=1.4, alpha=0.4)

# cibo che esce dalla scatola
items = [(apple_spr, 215, 905, 1.5, -18), (milk_spr, 395, 780, 1.45, -8), (cheese_spr, 700, 800, 1.7, 10),
         (can_spr, 870, 900, 1.9, 16), (bread_spr, 540, 840, 1.2, 4),
         (carrot_spr, 930, 760, 1.3, 20)]
for fn, x, y, sc, r in items:
    put(img, fn(), x, y, scale=sc, rot=r, shadow=12)

put(img, box_spr(), 540, 1250, scale=1.75, shadow=22, rot=-1)

# elder + punto interrogativo curiosita'
put(img, glow_spr(), 190, 1620, scale=1.0, alpha=0.3)
put(img, elder_spr(), 190, 1640, scale=1.05, shadow=18)
put(img, tspr("?", FONT_SERIF, 330, GOLD), 960, 1480, shadow=18, rot=10)
put(img, stamp_spr("WHO GETS IT?", 520, 130, GOLD), 700, 1540, rot=-5, shadow=14)

put(img, tag_spr("NOBODY TELLS YOU", 880, 150, CORAL, 74), 560, 1770, rot=-2, shadow=18)

out = os.environ.get("COVER_OUT", "copertina-short-06.png")
img.save(out); print("ok", out)
