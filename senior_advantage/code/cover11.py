import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes11 import *

# Copertina short 11 (Casa-Inverno): layout nuovo rispetto alle copertine 7-10 (niente raggi gialli, niente binari):
# notte d'inverno con neve e luna, casa con finestra accesa e 4 tessere in fila (allarme, pasto, bilancia, fiamma) che "arrivano",
# titolo grande OVER 60? / HELP COMES TO YOUR HOME, badge 9 KINDS, timbro ALMOST NOBODY ASKS. 1080x1920.
# Tema (aiuto a casa in inverno) e pubblico (over 60) a prima vista; curiosita: nessuno chiede.
# uso: SA_TMP=/tmp/x python3 cover11.py [cartella_out]
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/user/Tr/senior_advantage/miniature"

img = background(1.4)
ambient11(img, 1.4, n=46, alpha=0.55)

# alone caldo dietro la casa
put(img, glow_spr(), 540, 1330, scale=2.3, alpha=0.30)
put(img, moon_spr(), 960, 715, scale=0.62, alpha=0.95, shadow=6)

# titolo
def line(s, y, size, col, maxw=980, track=0, shadow=10):
    sp = tspr(s, FONT_SANS, size, col, track=track)
    sc = min(1.0, maxw / sp.width)
    put(img, sp, 540, y, scale=sc, shadow=shadow)

line("OVER 60?", 215, 230, GOLD, maxw=1000, track=2, shadow=14)
line("HELP COMES", 440, 120, IVORY, maxw=980, track=2)
line("TO YOUR HOME", 575, 120, IVORY, maxw=980, track=2)
line("THIS WINTER", 700, 100, GOLD, maxw=980, track=4)

# casa + alberi
put(img, pine_spr(), 140, 1590, scale=1.0, shadow=10)
put(img, pine_spr(), 940, 1610, scale=0.9, shadow=10)
put(img, house_spr(), 540, 1380, scale=1.3, shadow=16)

# 4 tessere che arrivano alla casa (stessi numeri del video: 1 allarme, 4 pasto, 6 legale, 9 caldaia)
for i, (k, rot) in enumerate(((1, -6), (4, 3), (6, -3), (9, 6))):
    x = 190 + i * 233
    y = 930 + (12 if i % 2 else -12)
    put(img, tile_spr(k, 200, True), x, y, shadow=10, rot=rot)

# badge 9 KINDS
c = Cv(300, 300)
c.ell((6, 6, 294, 294), fill=CORAL, outline=DARK, width=8)
c.text((150, 140), "9", FONT_SANS, 170, IVORY)
c.text((150, 236), "KINDS", FONT_SANS, 52, IVORY, track=4)
put(img, c.done(), 905, 1175, scale=0.85, shadow=12, rot=7)

# timbro finale
put(img, stamp_spr("ALMOST NOBODY ASKS", 960, 130, CORAL), 540, 1790, rot=-2, shadow=14)

os.makedirs(OUT, exist_ok=True)
img.save(f"{OUT}/copertina-short-11.png")
print("ok", img.size)
