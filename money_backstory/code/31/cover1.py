import sys
sys.path.insert(0, "/home/claude/slides")
from engine import *

img = background(1.2)
d = ImageDraw.Draw(img)

# etichetta
f = font(FONT_SANS, 58)
txt = "SENIOR DISCOUNTS"
tw = d.textlength(txt, font=f) + 14 * (len(txt) - 1)
x = W//2 - tw/2
for ch in txt:
    d.text((x, 430), ch, font=f, fill=SAGE, anchor="lm")
    x += d.textlength(ch, font=f) + 14

# START AT
shadow_text(img, (W//2, 620), "START AT", font(FONT_SANS, 104), IVORY, off=(5, 10), blur=14)

# 55 enorme
shadow_text(img, (W//2, 900), "55", font(FONT_SERIF, 540), IVORY, off=(10, 22), blur=26)

# NOT 65 barrato
f2 = font(FONT_SANS, 130)
shadow_text(img, (W//2, 1230), "NOT 65", f2, (214, 108, 96), off=(6, 12), blur=16)
tw2 = d.textlength("NOT 65", font=f2)
d.line([W//2 - tw2/2 - 20, 1235, W//2 + tw2/2 + 20, 1235], fill=(214, 108, 96), width=14)

# riquadro finale
box = [110, 1400, W-110, 1640]
panel(img, box, radius=38, border=GOLD, bw=6)
d.text((W//2, 1470), "AND NOBODY", font=font(FONT_SANS, 70), fill=IVORY, anchor="mm")
d.text((W//2, 1570), "TELLS YOU", font=font(FONT_SANS, 70), fill=GOLD, anchor="mm")

img.save("/mnt/user-data/outputs/copertina-short-01.png")
print("ok")
