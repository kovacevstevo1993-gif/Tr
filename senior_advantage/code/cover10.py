import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes10 import *

# Copertina short 10 (Amtrak): layout nuovo rispetto alle copertine 7-9 (niente raggi gialli):
# binari in prospettiva verso l'orizzonte, treno visto di fronte coi fari accesi, tabellone partenze "OVER 65?".
# Tema (Amtrak/treno) e pubblico (over 65) a prima vista; curiosita: casella vuota ?, divisa rossa, nota del medico. 1080x1920.
def fit(spr, maxw=960):
    return spr if spr.width <= maxw else spr.resize((maxw, int(spr.height * maxw / spr.width)), Image.LANCZOS)

def train_front_spr():
    c = Cv(620, 720)
    c.poly([(120, 40), (500, 40), (590, 300), (600, 640), (20, 640), (30, 300)], fill=(22, 82, 64))
    c.poly([(150, 70), (470, 70), (540, 280), (80, 280)], fill=(190, 222, 232))
    c.poly([(150, 70), (300, 70), (200, 280), (80, 280)], fill=(225, 240, 246))
    c.rrect((40, 330, 580, 372), 10, fill=GOLD)
    c.rrect((40, 392, 580, 410), 6, fill=RED)
    for x in (130, 490):
        c.ell((x - 62, 440, x + 62, 564), fill=(255, 244, 200), outline=GOLD, width=10)
        c.ell((x - 34, 468, x + 34, 536), fill=(255, 255, 240))
    c.rrect((236, 450, 384, 540), 16, fill=DARK, outline=GOLD, width=5)
    c.text((310, 496), "65+", FONT_SANS, 54, GOLD)
    c.rrect((10, 600, 610, 690), 14, fill=(40, 48, 48), outline=STEEL, width=5)
    for k in range(5):
        c.rrect((60 + k * 110, 620, 120 + k * 110, 670), 6, fill=(70, 78, 78))
    return c.done()

def beam_layer():
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for x in (430, 650):
        d.polygon([(x, 1240), (x - 380, 1920), (x + 380, 1920)], fill=(255, 236, 170, 46))
    return lay.filter(ImageFilter.GaussianBlur(26))

img = background(1.4)
# binari in prospettiva verso il punto di fuga
VX, VY = 540, 880
lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
d.polygon([(VX - 6, VY), (VX + 6, VY), (1080 + 420, 1920), (-420, 1920)], fill=(10, 30, 26, 200))
for k in range(26):
    f = (k / 25.0) ** 2.2
    y = VY + (1920 - VY) * f
    hw = 10 + (1080 * 0.78) * f
    d.line([(VX - hw, y), (VX + hw, y)], fill=(120, 96, 64, 200), width=max(2, int(4 + 34 * f)))
for sgn in (-1, 1):
    d.line([(VX + sgn * 6, VY), (VX + sgn * 560, 1920)], fill=(200, 210, 206, 255), width=16)
    d.line([(VX + sgn * 6, VY), (VX + sgn * 560, 1920)], fill=(240, 244, 242, 255), width=6)
base = img.convert("RGBA"); base.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1)))
base.alpha_composite(beam_layer())
img = base.convert("RGB")

# tabellone partenze OVER 65?
txt = "OVER 65?"
n = len(txt)
fr = Cv(n * 108 + 90, 190)
fr.rrect((4, 4, n * 108 + 86, 186), 30, fill=BOARD, outline=GOLD, width=7)
put(img, fr.done(), 540, 190, shadow=16)
for i, ch in enumerate(txt):
    c = Cv(100, 150)
    c.rrect((3, 3, 97, 147), 12, fill=(24, 36, 34), outline=(44, 60, 56), width=3)
    c.line([5, 75, 95, 75], BOARD, 5)
    if ch != " ":
        c.text((50, 78), ch, FONT_SANS, 100, AMBER)
    put(img, c.done(), 540 - (n - 1) * 108 / 2 + i * 108, 190)

put(img, fit(tspr("RIDING AMTRAK?", FONT_SANS, 130, IVORY)), 540, 395, shadow=22)
put(img, fit(tspr("3 THINGS", FONT_SANS, 200, GOLD)), 540, 575, shadow=22)
put(img, fit(tspr("YOU CAN ASK FOR", FONT_SANS, 96, IVORY)), 540, 740, shadow=16)

# treno di fronte
put(img, glow_spr(), 540, 1190, scale=2.0, alpha=0.5)
put(img, train_front_spr(), 540, 1150, scale=0.78, shadow=20)

# curiosita ai lati: divisa rossa (sx), nota del medico (dx), casella vuota ? (dx alto)
put(img, porter_spr(), 175, 1370, scale=0.62, shadow=16)
put(img, note_spr(), 915, 1360, scale=0.48, rot=8, shadow=16)
put(img, checkbox_spr(CORAL), 905, 1010, scale=0.9, rot=-6, shadow=14)
put(img, tspr("?", FONT_SANS, 120, CORAL), 905, 1012, rot=-6)

put(img, tag_spr("ALMOST NOBODY ASKS", 900, 150, CORAL, 66), 540, 1700, rot=-2, shadow=20)

out = os.environ.get("COVER_OUT", "copertina-short-10.png")
img.save(out); print("ok", out)
