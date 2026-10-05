import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes4 import *

img = background(1.4)
label(img, 1.0, "ENERGY BILL HELP", 320, SAGE)

# 8 case, una sola accesa
for i in range(8):
    x = 540 + (i % 4 - 1.5) * 232
    y = 560 + (i // 4) * 250
    if i == 6:
        put(img, glow_spr(), x, y, scale=1.1, alpha=0.55)
        put(img, small_house(True), x, y, scale=1.85, shadow=12)
    else:
        put(img, small_house(False), x, y, scale=1.6, alpha=0.85, shadow=6)

put(img, glow_spr(), 540, 1215, scale=1.4, alpha=0.3)
put(img, tspr("1 IN 8", FONT_SERIF, 340, GOLD), 540, 1225, shadow=22)
put(img, tspr("GETS THIS HELP", FONT_SANS, 88, IVORY), 540, 1420, shadow=10)

put(img, flame_spr(), 140, 1420, scale=0.7, rot=-8, shadow=8)
put(img, snow_spr(), 940, 1420, scale=0.62, rot=10, shadow=8)

put(img, tag_spr("DO YOU QUALIFY?", 620, 100, GOLD, 44), 540, 985, rot=-4, shadow=12)

c = Cv(880, 250)
c.rrect((4, 4, 876, 246), 44, fill=CARD, outline=GOLD, width=7)
c.text((440, 88), "HELP WITH", FONT_SANS, 92, IVORY)
c.text((440, 178), "ENERGY BILLS", FONT_SANS, 92, GOLD)
put(img, c.done(), 540, 1660, shadow=14)

out = os.environ.get("COVER_OUT", "copertina-short-04.png")
img.save(out)
print("ok", out)
