from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import math

W, H = 2560, 1440
CX, CY = W // 2, H // 2

GREEN_D = (7, 38, 30)
GREEN_L = (26, 92, 71)
IVORY = (246, 241, 229)
SAGE = (154, 200, 170)
SAGE_D = (96, 143, 114)

img = Image.composite(
    Image.new("RGB", (W, H), GREEN_D),
    Image.new("RGB", (W, H), GREEN_L),
    (lambda m: m)(None) if False else None
) if False else None

# gradiente radiale
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
steps = 260
for i in range(steps):
    r = int(W * 0.62 * (1 - i / steps))
    md.ellipse([CX - r, CY - r, CX + r, CY + r], fill=int(255 * (i / steps)))
mask = mask.filter(ImageFilter.GaussianBlur(120))
img = Image.composite(Image.new("RGB", (W, H), GREEN_D),
                      Image.new("RGB", (W, H), GREEN_L), mask)

# incisione concentrica
eng = Image.new("L", (W, H), 0)
ed = ImageDraw.Draw(eng)
r = 200
while r < 1500:
    ed.ellipse([CX - r, CY - r, CX + r, CY + r], outline=20, width=2)
    r += 26
eng = eng.filter(ImageFilter.GaussianBlur(1.2))
img = ImageChops.add(img, Image.merge("RGB", (eng, eng, eng)))
d = ImageDraw.Draw(img)

def font(size, bold=True):
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf", size)
        if bold:
            try:
                f.set_variation_by_name("Bold")
            except Exception:
                pass
        return f
    except Exception:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", size)

def centered(text, f, y, fill, shadow=True, track=0):
    bb = d.textbbox((0, 0), text, font=f)
    w = bb[2] - bb[0] + track * (len(text) - 1)
    x = CX - w / 2 - bb[0]
    if shadow:
        sh = Image.new("L", (W, H), 0)
        sd = ImageDraw.Draw(sh)
        cx = x + 5
        for ch in text:
            sd.text((cx, y + 9), ch, font=f, fill=150)
            cx += d.textlength(ch, font=f) + track
        sh2 = sh.filter(ImageFilter.GaussianBlur(14))
        base = Image.new("RGB", (W, H), (4, 22, 17))
        img2 = Image.composite(base, img, sh2)
        img.paste(img2)
    cx = x
    for ch in text:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += d.textlength(ch, font=f) + track

# titolo
f1 = font(150)
centered("THE SENIOR ADVANTAGE", f1, CY - 190, IVORY, track=6)

# filetto con losanga
y = CY + 20
d.line([CX - 640, y, CX - 40, y], fill=SAGE_D, width=5)
d.line([CX + 40, y, CX + 640, y], fill=SAGE_D, width=5)
d.polygon([(CX, y - 20), (CX + 20, y), (CX, y + 20), (CX - 20, y)], fill=SAGE)

# sottotitolo
f2 = font(64, bold=False)
centered("Benefits, discounts and savings most Americans over 60 never claim", f2, CY + 80, SAGE, shadow=False, track=2)

# gradini decorativi
base_y = CY + 300
hs = [34, 60, 88]
bw, gap = 46, 16
tot = len(hs) * bw + (len(hs) - 1) * gap
x = CX - tot / 2
for h in hs:
    d.rounded_rectangle([x, base_y - h, x + bw, base_y], radius=9, fill=SAGE_D)
    d.rounded_rectangle([x, base_y - h, x + bw, base_y - h * 0.55], radius=9, fill=SAGE)
    x += bw + gap

# vignettatura
vig = Image.new("L", (W, H), 0)
vd = ImageDraw.Draw(vig)
for i in range(120):
    rr = int(W * 0.60 * (1 - i / 120))
    vd.ellipse([CX - rr, CY - rr * H / W, CX + rr, CY + rr * H / W], fill=int(255 * (i / 120) ** 1.5))
vig = vig.filter(ImageFilter.GaussianBlur(140)).point(lambda v: int((255 - v) * 0.5))
img = Image.composite(Image.new("RGB", (W, H), (3, 18, 14)), img, vig)

img.save("/mnt/user-data/outputs/banner-senior-advantage.png")
print("ok")
