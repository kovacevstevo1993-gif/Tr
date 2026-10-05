import sys
sys.path.insert(0, "/home/claude/slides")
from scenes3 import *

img = background(1.4)

label(img, 1.0, "SENIOR MEALS", 320, SAGE)

# OVER 60+
put(img, tspr("OVER", FONT_SANS, 70, SAGE, track=14), 540, 460)
put(img, glow_spr(), 540, 650, scale=1.2, alpha=0.32)
put(img, tspr("60+", FONT_SERIF, 420, IVORY), 540, 660, shadow=22)

# porta con piatto scoperto e vapore
put(img, door_spr(), 540, 1060, scale=0.85, shadow=16)
yy = 1290
put(img, plate_spr(), 540, yy + 34, scale=1.35, shadow=10)
put(img, dome_spr(), 540, yy - 46 - 130, scale=1.35, rot=10, shadow=10)
steam(img, 1.4, 540, yy - 150, alpha=1.0)

# adesivo oro
put(img, tag_spr("CHECK IF YOU QUALIFY", 660, 100, GOLD, 42), 720, 800, rot=-6, shadow=12)

# riquadro finale
c = Cv(880, 250)
c.rrect((4, 4, 876, 246), 44, fill=CARD, outline=GOLD, width=7)
c.text((440, 88), "HOT MEALS", FONT_SANS, 92, IVORY)
c.text((440, 178), "AT YOUR DOOR", FONT_SANS, 92, GOLD)
put(img, c.done(), 540, 1530, shadow=14)

img.save("/mnt/user-data/outputs/copertina-short-03.png")
img.resize((420, 747)).save("/tmp/cov3.png")
print("ok")