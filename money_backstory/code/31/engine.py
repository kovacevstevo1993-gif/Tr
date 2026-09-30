"""Motore slide animate 1080x1920 - The Senior Advantage."""
import math, os, random, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H, FPS = 1080, 1920, 30

GREEN_D = (7, 38, 30)
GREEN_M = (14, 58, 45)
GREEN_L = (26, 92, 71)
CARD = (12, 58, 45)
IVORY = (246, 241, 229)
SAGE = (154, 200, 170)
SAGE_D = (96, 143, 114)
GOLD = (228, 179, 99)

FONT_SERIF = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
FONT_SANS = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FONT_SANS_M = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"

_fc = {}
def font(path, size, bold=True):
    k = (path, size, bold)
    if k not in _fc:
        f = ImageFont.truetype(path, size)
        if path == FONT_SERIF and bold:
            try: f.set_variation_by_name("Bold")
            except Exception: pass
        _fc[k] = f
    return _fc[k]

def ease(t):           # easeOutCubic
    t = max(0.0, min(1.0, t)); return 1 - (1 - t) ** 3
def ease_back(t):
    t = max(0.0, min(1.0, t)); c = 1.70158 + 1
    return 1 + c * (t - 1) ** 3 + 1.70158 * (t - 1) ** 2

def seg(t, start, dur):
    return max(0.0, min(1.0, (t - start) / dur)) if dur else 1.0

# ---------- sfondo ----------
_bg_cache = {}
def background(t):
    """gradiente + anelli incisi che ruotano lentamente + polvere d'oro"""
    key = int(t * FPS)
    img = Image.new("RGB", (W, H), GREEN_D)
    # gradiente radiale
    if "grad" not in _bg_cache:
        m = Image.new("L", (W, H), 0)
        d = ImageDraw.Draw(m)
        for i in range(160):
            r = int(W * 1.15 * (1 - i / 160))
            d.ellipse([W//2 - r, H//2 - r, W//2 + r, H//2 + r], fill=int(255 * (i / 160)))
        _bg_cache["grad"] = m.filter(ImageFilter.GaussianBlur(90))
    img = Image.composite(Image.new("RGB", (W, H), GREEN_D),
                          Image.new("RGB", (W, H), GREEN_L), _bg_cache["grad"])
    # anelli incisi (ruotano: si espandono lentamente)
    eng = Image.new("L", (W, H), 0)
    ed = ImageDraw.Draw(eng)
    off = (t * 9) % 34
    r = 60 + off
    while r < 1500:
        ed.ellipse([W//2 - r, H//2 - r, W//2 + r, H//2 + r], outline=17, width=2)
        r += 34
    eng = eng.filter(ImageFilter.GaussianBlur(1.1))
    img = ImageChops.add(img, Image.merge("RGB", (eng, eng, eng)))
    # polvere d'oro
    rnd = random.Random(7)
    dust = Image.new("RGB", (W, H), (0, 0, 0))
    dd = ImageDraw.Draw(dust)
    for i in range(38):
        bx = rnd.uniform(0, W); by = rnd.uniform(0, H)
        sp = rnd.uniform(6, 22); rad = rnd.uniform(2, 6)
        y = (by - t * sp) % H
        x = bx + math.sin(t * 0.6 + i) * 14
        a = 0.25 + 0.25 * math.sin(t * 1.4 + i * 1.7)
        c = tuple(int(v * a) for v in GOLD)
        dd.ellipse([x - rad, y - rad, x + rad, y + rad], fill=c)
    dust = dust.filter(ImageFilter.GaussianBlur(2))
    img = ImageChops.add(img, dust)
    return img

# ---------- helper disegno ----------
def shadow_text(img, xy, text, f, fill, anchor="mm", off=(4, 7), blur=9, alpha=150):
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).text((xy[0] + off[0], xy[1] + off[1]), text, font=f, fill=alpha, anchor=anchor)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    img.paste(Image.new("RGB", (W, H), (4, 22, 17)), (0, 0), sh)
    ImageDraw.Draw(img).text(xy, text, font=f, fill=fill, anchor=anchor)

def panel(img, box, radius=34, fill=CARD, border=SAGE_D, bw=4, shadow=True):
    if shadow:
        sh = Image.new("L", (W, H), 0)
        ImageDraw.Draw(sh).rounded_rectangle([box[0]+6, box[1]+14, box[2]+6, box[3]+14], radius=radius, fill=150)
        sh = sh.filter(ImageFilter.GaussianBlur(18))
        img.paste(Image.new("RGB", (W, H), (3, 18, 14)), (0, 0), sh)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=border, width=bw)

def alpha_layer(img, layer, a):
    """incolla layer RGB su img con opacità a, usando la sua maschera"""
    if a <= 0: return
    rgb, mask = layer
    m = mask.point(lambda v: int(v * max(0.0, min(1.0, a))))
    img.paste(rgb, (0, 0), m)

def new_layer():
    return Image.new("RGB", (W, H), (0, 0, 0)), Image.new("L", (W, H), 0)

# ---------- oggetti disegnati ----------
def banknote(rgb, mask, cx, cy, w=430, h=210, label="SENIOR RATE", sub="ask before paying"):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    box = [cx - w//2, cy - h//2, cx + w//2, cy + h//2]
    for dr, col in ((d, CARD), (dm, 255)):
        dr.rounded_rectangle(box, radius=26, fill=col)
    d.rounded_rectangle(box, radius=26, outline=SAGE_D, width=5)
    d.rounded_rectangle([box[0]+14, box[1]+14, box[2]-14, box[3]-14], radius=18, outline=(52, 104, 84), width=2)
    # tondo col dollaro
    r = 52
    d.ellipse([box[0]+40, cy-r, box[0]+40+2*r, cy+r], fill=SAGE)
    d.text((box[0]+40+r, cy), "$", font=font(FONT_SERIF, 72), fill=GREEN_D, anchor="mm")
    d.text((box[0]+40+2*r+28, cy-22), label, font=font(FONT_SANS, 40), fill=IVORY, anchor="lm")
    d.text((box[0]+40+2*r+28, cy+28), sub, font=font(FONT_SANS_M, 28), fill=SAGE, anchor="lm")

def price_tag(rgb, mask, cx, cy, text="55+", w=300, h=170):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    box = [cx - w//2, cy - h//2, cx + w//2, cy + h//2]
    for dr, col in ((d, GOLD), (dm, 255)):
        dr.rounded_rectangle(box, radius=22, fill=col)
    for dr, col in ((d, GREEN_D), (dm, 255)):
        dr.ellipse([box[0]+22, cy-16, box[0]+54, cy+16], fill=col)
    d.text((cx + 30, cy), text, font=font(FONT_SANS, 74), fill=GREEN_D, anchor="mm")

def encode(frames_dir, out, fps=FPS):
    subprocess.run(["ffmpeg", "-y", "-framerate", str(fps), "-i", f"{frames_dir}/%05d.png",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", out],
                   check=True, capture_output=True)

def render(draw_fn, duration, out):
    tmp = "/tmp/frames"
    os.system(f"rm -rf {tmp} && mkdir -p {tmp}")
    n = int(round(duration * FPS))
    for i in range(n):
        t = i / FPS
        img = background(t)
        draw_fn(img, t)
        img.save(f"{tmp}/{i:05d}.png")
    encode(tmp, out)
    return out
