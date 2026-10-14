import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes9 import *

# Copertina short 9 (Aeroporto): si capisce subito tema (volare/aeroporto) e pubblico (over 60) + curiosita' (scarpe ?, soldi indietro). 1080x1920.
def fit(spr, maxw=960):
    return spr if spr.width <= maxw else spr.resize((maxw, int(spr.height * maxw / spr.width)), Image.LANCZOS)

img = background(1.4)
ray = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(ray)
cx, cy = 540, 1250
for k in range(24):
    a0 = k * 15
    rd.pieslice([cx - 1600, cy - 1600, cx + 1600, cy + 1600], a0, a0 + 7.5, fill=(228, 179, 99, 50))
ray = ray.filter(ImageFilter.GaussianBlur(3))
base = img.convert("RGBA"); base.alpha_composite(ray); img.paste(base.convert("RGB"))

put(img, tag_spr("SENIORS 60+", 560, 112, CORAL, 62), 540, 190, rot=-3, shadow=14)
put(img, fit(tspr("FLYING?", FONT_SANS, 210, IVORY)), 540, 400, shadow=22)
put(img, fit(tspr("8 THINGS", FONT_SANS, 190, GOLD)), 540, 610, shadow=22)
put(img, fit(tspr("YOU CAN ASK FOR", FONT_SANS, 96, IVORY)), 540, 790, shadow=16)

put(img, glow_spr(), 540, 1260, scale=2.2, alpha=0.45)
put(img, plane_spr(IVORY, 300, 190), 790, 990, scale=1.3, rot=10, shadow=16)
put(img, shoes_spr(), 330, 1220, scale=0.75, rot=-4, shadow=18)
put(img, tspr("?", FONT_SANS, 200, GOLD), 330, 1020, rot=-8, shadow=16)
put(img, wallet_spr(), 780, 1300, scale=0.75, rot=3, shadow=18)
put(img, tag_spr("YOUR MONEY BACK", 760, 140, GOLD, 64), 540, 1560, rot=-2, shadow=18)
put(img, tag_spr("ALMOST NOBODY ASKS", 900, 140, CORAL, 62), 540, 1780, rot=-2, shadow=18)

out = os.environ.get("COVER_OUT", "copertina-short-09.png")
img.save(out); print("ok", out)
