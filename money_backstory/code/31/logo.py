from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 1600  # supersample, downscale a 800
C = S // 2

GREEN_D = (9, 46, 36)
GREEN_L = (21, 79, 61)
IVORY = (244, 239, 227)
SAGE = (150, 196, 166)

img = Image.new("RGB", (S, S), GREEN_D)
d = ImageDraw.Draw(img)

# gradiente radiale morbido
grad = Image.new("L", (S, S), 0)
gd = ImageDraw.Draw(grad)
steps = 220
for i in range(steps):
    r = int(S * 0.75 * (1 - i / steps))
    gd.ellipse([C - r, C - r, C + r, C + r], fill=int(255 * (i / steps)))
grad = grad.filter(ImageFilter.GaussianBlur(S // 40))
img = Image.composite(Image.new("RGB", (S, S), GREEN_D), Image.new("RGB", (S, S), GREEN_L), grad)
d = ImageDraw.Draw(img)

# anelli
d.ellipse([C - 700, C - 700, C + 700, C + 700], outline=IVORY, width=10)
d.ellipse([C - 655, C - 655, C + 655, C + 655], outline=SAGE, width=4)

# font
try:
    f = ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf", 640)
    try:
        f.set_variation_by_name("Bold")
    except Exception:
        pass
except Exception:
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 600)

text = "SA"
bbox = d.textbbox((0, 0), text, font=f)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
tx = C - tw / 2 - bbox[0]
ty = C - th / 2 - bbox[1] - 90
d.text((tx, ty), text, font=f, fill=IVORY)

# gradini in salita sotto il monogramma
base_y = C + 400
heights = [90, 160, 240]
bw = 120
gap = 34
total = len(heights) * bw + (len(heights) - 1) * gap
x = C - total / 2
for h in heights:
    d.rounded_rectangle([x, base_y - h, x + bw, base_y], radius=18, fill=SAGE)
    x += bw + gap

img = img.resize((800, 800), Image.LANCZOS)
img.save("/mnt/user-data/outputs/logo-senior-advantage.png")
print("ok")
