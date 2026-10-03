import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes5 import *

img = background(1.4)
put(img, tag_spr("SENIORS 60+", 520, 104, CORAL, 56), 540, 300, rot=-3, shadow=12)

put(img, glow_spr(), 540, 640, scale=1.6, alpha=0.3)
put(img, tspr("SKIP THIS", FONT_SANS, 190, IVORY), 540, 560, shadow=18)
put(img, tspr("INCOME TEST", FONT_SANS, 150, GOLD), 540, 740, shadow=16)

put(img, test_card("GROSS INCOME", "THE FIRST TEST", CORAL, "bills"), 540, 1010, scale=1.1, alpha=0.85, shadow=14, rot=-2)
put(img, bigx_spr(), 580, 1010, scale=0.95, rot=-4, shadow=10)

put(img, glow_spr(), 330, 1340, scale=1.0, alpha=0.3)
put(img, elder_spr(), 330, 1340, scale=1.0, shadow=16)
put(img, age_badge(), 560, 1420, scale=1.0, rot=-8, shadow=12)
put(img, apple_spr(), 850, 1290, scale=0.95, rot=12, shadow=10)
put(img, basket_spr(), 880, 1470, scale=0.6, rot=-6, shadow=10)
put(img, milk_spr(), 740, 1330, scale=0.8, rot=6, shadow=10)

put(img, tag_spr("SNAP FOOD HELP", 820, 170, GOLD, 88), 540, 1700, rot=-2, shadow=16)

out = os.environ.get("COVER_OUT", "copertina-short-05.png")
img.save(out); print("ok", out)
