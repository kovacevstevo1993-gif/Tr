import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from scenes2 import *

img = background(1.2)

label(img, 1.0, "SENIOR DISCOUNTS", 330, SAGE)

# grande 4 + PLACES
put(img, glow_spr(), 400, 700, alpha=0.32)
put(img, tspr("4", FONT_SERIF, 620, IVORY), 400, 710, shadow=24)
put(img, tspr("PLACES", FONT_SANS, 96, SAGE), 745, 850, shadow=6)

# icone + età
xs = [186, 422, 658, 894]
for x, k, age in zip(xs, ["food", "phone", "ticket", "peak"], ["55+", "55+", "60+", "62+"]):
    put(img, badge_spr(k), x, 1060, shadow=12)
    put(img, tag_spr(age, 170, 78, GOLD, 46), x, 1210, shadow=8)

# riquadro finale
c = Cv(860, 250)
c.rrect((4, 4, 856, 246), 44, fill=CARD, outline=GOLD, width=7)
c.text((430, 88), "NOBODY", FONT_SANS, 92, IVORY)
c.text((430, 178), "TELLS YOU", FONT_SANS, 92, GOLD)
put(img, c.done(), 540, 1470, shadow=14)

img.save("/mnt/user-data/outputs/copertina-short-02.png")
img.resize((420, 747)).save("/tmp/cov2.png")
print("ok")