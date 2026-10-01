from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import math, os, subprocess

W, H = 1080, 1920
FPS, DUR = 30, 6
N = FPS * DUR
CX = W // 2

GREEN_D = (7, 38, 30)
GREEN_L = (24, 86, 66)
IVORY = (246, 241, 229)
SAGE = (154, 200, 170)
SAGE_D = (96, 143, 114)
AMBER = (232, 186, 106)

FONT = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
SANS = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
SANSB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"

def serif(sz, bold=True):
    f = ImageFont.truetype(FONT, sz)
    if bold:
        try: f.set_variation_by_name("Bold")
        except Exception: pass
    return f

def ease(t):
    return 1 - (1 - t) ** 3

def clamp(t):
    return max(0.0, min(1.0, t))

# --- sfondo statico (gradiente + incisione) ---
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
for i in range(240):
    r = int(W * 1.15 * (1 - i / 240))
    md.ellipse([CX - r, H * 0.42 - r, CX + r, H * 0.42 + r], fill=int(255 * (i / 240)))
mask = mask.filter(ImageFilter.GaussianBlur(90))
BG = Image.composite(Image.new("RGB", (W, H), GREEN_D),
                     Image.new("RGB", (W, H), GREEN_L), mask)
eng = Image.new("L", (W, H), 0)
ed = ImageDraw.Draw(eng)
r = 120
while r < 1500:
    ed.ellipse([CX - r, H * 0.42 - r, CX + r, H * 0.42 + r], outline=16, width=2)
    r += 22
BG = ImageChops.add(BG, Image.merge("RGB", (eng, eng, eng)))

os.makedirs("/home/claude/frames", exist_ok=True)

def draw_text(d, t, f, y, fill, track=0, center=True, x0=None, alpha_img=None):
    bb = d.textbbox((0, 0), t, font=f)
    w = bb[2] - bb[0] + track * (len(t) - 1)
    x = (CX - w / 2 - bb[0]) if center else x0
    for ch in t:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + track
    return w

for n in range(N):
    t = n / FPS
    img = BG.copy()
    d = ImageDraw.Draw(img)

    # 1. etichetta in alto con filetto (0.0s)
    a = ease(clamp((t - 0.1) / 0.6))
    if a > 0:
        dy = int((1 - a) * 40)
        col = tuple(int(GREEN_D[i] + (SAGE[i] - GREEN_D[i]) * a) for i in range(3))
        f_lab = ImageFont.truetype(SANSB, 38)
        draw_text(d, "SENIOR DISCOUNTS", f_lab, 300 + dy, col, track=8)
        lw = int(360 * a)
        d.line([CX - lw, 372 + dy, CX + lw, 372 + dy], fill=SAGE_D, width=3)

    # 2. numero che sale (0.5s -> 2.0s)
    p = ease(clamp((t - 0.5) / 1.5))
    val = int(1284 * p)
    f_num = serif(230)
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).text((CX, 560), f"${val:,}", font=f_num, fill=150, anchor="ma")
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    img = Image.composite(Image.new("RGB", (W, H), (4, 22, 17)), img, sh)
    d = ImageDraw.Draw(img)
    d.text((CX + 4, 566), f"${val:,}", font=f_num, fill=(6, 30, 24), anchor="ma")
    d.text((CX, 560), f"${val:,}", font=f_num, fill=IVORY, anchor="ma")

    # 3. sottotitolo (1.8s)
    a2 = ease(clamp((t - 1.8) / 0.6))
    if a2 > 0:
        col = tuple(int(GREEN_D[i] + (SAGE[i] - GREEN_D[i]) * a2) for i in range(3))
        f_sub = serif(52, bold=False)
        draw_text(d, "left on the table every year", f_sub, 840 + int((1 - a2) * 25), col)

    # 4. barra che si riempie (2.4s)
    a3 = ease(clamp((t - 2.4) / 1.2))
    bx0, bx1, by = 150, W - 150, 990
    d.rounded_rectangle([bx0, by, bx1, by + 26], radius=13, fill=(16, 62, 48))
    if a3 > 0:
        d.rounded_rectangle([bx0, by, bx0 + (bx1 - bx0) * 0.78 * a3, by + 26], radius=13, fill=SAGE)
    f_small = ImageFont.truetype(SANS, 30)
    if a3 > 0.9:
        d.text((bx0, by + 46), "78% of seniors never ask", font=f_small, fill=SAGE_D)

    # 5. tre schede che entrano una dopo l'altra (3.0s)
    cards = [("GROCERY", "5%"), ("PHARMACY", "10%"), ("UTILITIES", "$30/mo")]
    cy = 1160
    ch_h = 150
    for i, (lab, v) in enumerate(cards):
        ai = ease(clamp((t - (3.0 + i * 0.35)) / 0.7))
        if ai <= 0:
            continue
        dx = int((1 - ai) * 90)
        y0 = cy + i * (ch_h + 26)
        box = [150 - dx, y0, W - 150 - dx, y0 + ch_h]
        d.rounded_rectangle([box[0] + 5, box[1] + 9, box[2] + 5, box[3] + 9], radius=22, fill=(5, 28, 22))
        d.rounded_rectangle(box, radius=22, fill=(15, 58, 45), outline=SAGE_D, width=3)
        d.rounded_rectangle([box[0], box[1] + 24, box[0] + 8, box[3] - 24], radius=4, fill=AMBER)
        d.text((box[0] + 44, y0 + 50), lab, font=ImageFont.truetype(SANSB, 40), fill=IVORY)
        d.text((box[2] - 44, y0 + 44), v, font=serif(56), fill=SAGE, anchor="ra")

    # 6. riga finale (4.8s)
    a4 = ease(clamp((t - 4.8) / 0.7))
    if a4 > 0:
        col = tuple(int(GREEN_D[i] + (IVORY[i] - GREEN_D[i]) * a4) for i in range(3))
        draw_text(d, "ASK. THEY RARELY OFFER.", ImageFont.truetype(SANSB, 44), 1700, col, track=4)

    # 7. luce che passa sul fondo
    sweep = Image.new("L", (W, H), 0)
    sx = int((t / DUR) * (W + 700)) - 350
    ImageDraw.Draw(sweep).polygon([(sx, H), (sx + 180, 0), (sx + 340, 0), (sx + 160, H)], fill=22)
    sweep = sweep.filter(ImageFilter.GaussianBlur(70))
    img = ImageChops.add(img, Image.merge("RGB", (sweep, sweep, sweep)))

    img.save(f"/home/claude/frames/f{n:04d}.png")

subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
                "-i", "/home/claude/frames/f%04d.png", "-c:v", "libx264",
                "-pix_fmt", "yuv420p", "-crf", "18",
                "/mnt/user-data/outputs/slide-campione-verticale.mp4"], check=True)
print("ok")
