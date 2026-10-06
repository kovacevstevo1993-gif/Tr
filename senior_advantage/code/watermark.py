from PIL import Image, ImageDraw, ImageFont
import os
S = 1200
GREEN_D = (7, 38, 30); GREEN_L = (26, 92, 71)
IVORY = (246, 241, 229); SAGE = (154, 200, 170); SAGE_D = (96, 143, 114)
sc = 4
W = S
img = Image.new("RGBA", (W, W), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
C = W // 2
# disco con gradiente semplice
for i in range(60):
    r = int(C * 0.94 * (1 - i / 60))
    t = i / 60
    col = tuple(int(GREEN_L[k] * t + GREEN_D[k] * (1 - t)) for k in range(3))
    d.ellipse([C - r, C - r, C + r, C + r], fill=col + (255,))
d.ellipse([C - int(C*0.94), C - int(C*0.94), C + int(C*0.94), C + int(C*0.94)], outline=IVORY, width=40)
d.ellipse([C - int(C*0.80), C - int(C*0.80), C + int(C*0.80), C + int(C*0.80)], outline=SAGE_D, width=12)
f = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "fonts/Lora-Variable.ttf"), 470)
try: f.set_variation_by_name("Bold")
except Exception: pass
b = d.textbbox((0, 0), "SA", font=f)
tw, th = b[2]-b[0], b[3]-b[1]
tx, ty = C - tw/2 - b[0], C - th/2 - b[1] - 110
d.text((tx+8, ty+12), "SA", font=f, fill=(4, 22, 17, 255))
d.text((tx, ty), "SA", font=f, fill=IVORY + (255,))
# gradini
base = C + 330; bw, gap = 80, 26; hs = [60, 105, 150]
x0 = C - (3*bw + 2*gap)/2
for h in hs:
    d.rounded_rectangle([x0, base-h, x0+bw, base], radius=14, fill=SAGE_D + (255,))
    d.rounded_rectangle([x0, base-h, x0+bw, base-h*0.55], radius=14, fill=SAGE + (255,))
    x0 += bw + gap
img.resize((400, 400), Image.LANCZOS).save(os.environ.get("WM_OUT", "filigrana-senior-advantage.png"))
