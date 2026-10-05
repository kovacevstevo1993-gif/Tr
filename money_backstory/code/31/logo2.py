from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import math

S = 1600
C = S // 2

GREEN_D = (7, 38, 30)
GREEN_M = (14, 58, 45)
GREEN_L = (26, 92, 71)
IVORY = (246, 241, 229)
IVORY_SH = (198, 190, 172)
SAGE = (154, 200, 170)
SAGE_D = (96, 143, 114)

# ---------- sfondo: gradiente radiale ----------
base = Image.new("RGB", (S, S), GREEN_D)
mask = Image.new("L", (S, S), 0)
md = ImageDraw.Draw(mask)
steps = 260
for i in range(steps):
    r = int(S * 0.78 * (1 - i / steps))
    md.ellipse([C - r, C - r, C + r, C + r], fill=int(255 * (i / steps)))
mask = mask.filter(ImageFilter.GaussianBlur(S // 30))
img = Image.composite(Image.new("RGB", (S, S), GREEN_D),
                      Image.new("RGB", (S, S), GREEN_L), mask)

# ---------- incisione: cerchi concentrici sottilissimi ----------
eng = Image.new("L", (S, S), 0)
ed = ImageDraw.Draw(eng)
r = 120
while r < 640:
    ed.ellipse([C - r, C - r, C + r, C + r], outline=26, width=2)
    r += 16
eng = eng.filter(ImageFilter.GaussianBlur(1.2))
img = ImageChops.add(img, Image.merge("RGB", (eng, eng, eng)))
d = ImageDraw.Draw(img)

# ---------- tacche perimetrali ----------
for i in range(72):
    a = math.radians(i * 5)
    r1, r2 = 612, (634 if i % 6 else 646)
    w = 3 if i % 6 else 6
    col = (70, 120, 98) if i % 6 else SAGE_D
    d.line([C + r1 * math.cos(a), C + r1 * math.sin(a),
            C + r2 * math.cos(a), C + r2 * math.sin(a)], fill=col, width=w)

# ---------- anelli con rilievo ----------
def ring(radius, color, width, emboss=True):
    if emboss:
        d.ellipse([C - radius, C - radius + 7, C + radius, C + radius + 7],
                  outline=(5, 28, 22), width=width)
    d.ellipse([C - radius, C - radius, C + radius, C + radius], outline=color, width=width)

ring(700, IVORY, 11)
ring(672, SAGE_D, 4)
ring(590, (52, 104, 84), 3)

# ---------- monogramma ----------
try:
    f = ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf", 620)
    try:
        f.set_variation_by_name("Bold")
    except Exception:
        pass
except Exception:
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 580)

text = "SA"
bbox = d.textbbox((0, 0), text, font=f)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
tx = C - tw / 2 - bbox[0]
ty = C - th / 2 - bbox[1] - 165

# ombra portata morbida
sh = Image.new("L", (S, S), 0)
ImageDraw.Draw(sh).text((tx + 10, ty + 22), text, font=f, fill=170)
sh = sh.filter(ImageFilter.GaussianBlur(20))
img = Image.composite(Image.new("RGB", (S, S), (4, 22, 17)), img, sh)
d = ImageDraw.Draw(img)

# bordo scuro inciso + lettera
d.text((tx + 4, ty + 6), text, font=f, fill=(6, 30, 24))
d.text((tx, ty), text, font=f, fill=IVORY)
# riflesso in basso sulle lettere
gloss = Image.new("L", (S, S), 0)
ImageDraw.Draw(gloss).text((tx, ty + 9), text, font=f, fill=255)
g2 = Image.new("L", (S, S), 0)
ImageDraw.Draw(g2).text((tx, ty), text, font=f, fill=255)
gloss = ImageChops.subtract(gloss, g2).filter(ImageFilter.GaussianBlur(4))
img = Image.composite(Image.new("RGB", (S, S), IVORY_SH), img, gloss)
d = ImageDraw.Draw(img)

# ---------- gradini in salita ----------
base_y = C + 430
heights = [72, 124, 180]
bw, gap = 95, 30
total = len(heights) * bw + (len(heights) - 1) * gap
x0 = C - total / 2

bsh = Image.new("L", (S, S), 0)
bd = ImageDraw.Draw(bsh)
x = x0
for h in heights:
    bd.rounded_rectangle([x + 8, base_y - h + 16, x + bw + 8, base_y + 16], radius=16, fill=160)
    x += bw + gap
bsh = bsh.filter(ImageFilter.GaussianBlur(16))
img = Image.composite(Image.new("RGB", (S, S), (4, 22, 17)), img, bsh)
d = ImageDraw.Draw(img)

x = x0
for h in heights:
    d.rounded_rectangle([x, base_y - h, x + bw, base_y], radius=16, fill=SAGE_D)
    d.rounded_rectangle([x, base_y - h, x + bw, base_y - h * 0.55], radius=16, fill=SAGE)
    x += bw + gap

# linea di base sotto i gradini
d.line([x0 - 26, base_y + 14, x0 + total + 26, base_y + 14], fill=(70, 120, 98), width=6)

# ---------- vignettatura ----------
vig = Image.new("L", (S, S), 0)
vd = ImageDraw.Draw(vig)
for i in range(120):
    rr = int(S * 0.72 * (1 - i / 120))
    vd.ellipse([C - rr, C - rr, C + rr, C + rr], fill=int(255 * (i / 120) ** 1.6))
vig = vig.filter(ImageFilter.GaussianBlur(60))
img = Image.composite(Image.new("RGB", (S, S), (3, 18, 14)), img, vig.point(lambda v: 255 - v))

img.resize((800, 800), Image.LANCZOS).save("/mnt/user-data/outputs/logo-senior-advantage.png")
print("ok")
