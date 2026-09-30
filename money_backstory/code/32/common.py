import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, math, random

W, H = 1920, 1080
FPS = 30

GOLD = (255, 205, 90)
GOLD_LIGHT = (255, 230, 160)
NAVY_DARK = (7, 11, 28)
NAVY_MID = (13, 20, 46)
RED = (235, 70, 70)
GREEN = (95, 210, 130)
WHITE = (240, 244, 250)

def font(size, bold=True):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

def _vgrad(w, h, top, bottom):
    arr = np.zeros((h, w, 3), dtype=np.float32)
    for y in range(h):
        f = y / (h - 1)
        arr[y, :, 0] = top[0] * (1 - f) + bottom[0] * f
        arr[y, :, 1] = top[1] * (1 - f) + bottom[1] * f
        arr[y, :, 2] = top[2] * (1 - f) + bottom[2] * f
    return arr

BASE_BG = _vgrad(W, H, NAVY_DARK, NAVY_MID)

def make_particles(n=90, seed=7):
    rnd = random.Random(seed)
    parts = []
    for _ in range(n):
        parts.append({
            "x": rnd.uniform(0, W),
            "y": rnd.uniform(0, H),
            "speed": rnd.uniform(18, 55),
            "size": rnd.uniform(1.4, 3.6),
            "amp": rnd.uniform(6, 22),
            "phase": rnd.uniform(0, math.tau),
        })
    return parts

def draw_particles(draw, particles, t):
    for p in particles:
        y = (p["y"] - p["speed"] * t) % H
        x = p["x"] + math.sin(t * 0.6 + p["phase"]) * p["amp"]
        s = p["size"]
        glow = min(1.0, 0.35 + 0.5 * (1 - y / H))
        c = tuple(int(GOLD[i] * glow + NAVY_MID[i] * (1 - glow)) for i in range(3))
        draw.ellipse([x - s * 2.2, y - s * 2.2, x + s * 2.2, y + s * 2.2], fill=c + (40,))
        draw.ellipse([x - s, y - s, x + s, y + s], fill=GOLD_LIGHT + (220,))

def light_sweep(img, t, period=6.0):
    w, h = img.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    pos = (t % period) / period
    cx = -w * 0.3 + pos * w * 1.6
    band = w * 0.22
    for i in range(int(band)):
        a = int(26 * (1 - abs(i - band / 2) / (band / 2)))
        if a <= 0:
            continue
        x = int(cx - band / 2 + i)
        d.line([(x, 0), (x - h * 0.35, h)], fill=(255, 235, 190, a))
    return Image.alpha_composite(img.convert("RGBA"), overlay)

def base_frame(t, particles):
    img = Image.fromarray(BASE_BG.astype(np.uint8), "RGB").convert("RGBA")
    d = ImageDraw.Draw(img, "RGBA")
    draw_particles(d, particles, t)
    img = light_sweep(img, t)
    return img

def gold_frame_overlay():
    """3D gold frame with outer glow and inner shadow, precomputed once."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    margin = 34
    thick = 16
    d = ImageDraw.Draw(img)
    box = [margin, margin, W - margin, H - margin]
    # outer glow
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle(box, radius=28, outline=GOLD + (255,), width=thick)
    glow = glow.filter(ImageFilter.GaussianBlur(18))
    img = Image.alpha_composite(img, glow)
    d = ImageDraw.Draw(img)
    # crisp gold border with subtle vertical gradient
    for i in range(thick):
        f = i / max(1, thick - 1)
        col = tuple(int(GOLD[j] * (1 - f) + GOLD_LIGHT[j] * f) for j in range(3))
        d.rounded_rectangle([box[0]+i, box[1]+i, box[2]-i, box[3]-i], radius=28-i//2, outline=col + (255,), width=1)
    # inner shadow
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([box[0]+thick, box[1]+thick, box[2]-thick, box[3]-thick], radius=20, outline=(0, 0, 0, 200), width=22)
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    img = Image.alpha_composite(img, shadow)
    return img

FRAME_OVERLAY = gold_frame_overlay()

def source_note(img, text):
    d = ImageDraw.Draw(img, "RGBA")
    f = font(20, bold=False)
    d.text((W/2, H-70), text, font=f, fill=(190, 195, 210, 210), anchor="mm")

def ease(x):
    return 1 - (1 - x) ** 3

def open_writer(path, n_frames):
    cmd = [
        "ffmpeg", "-y", "-f", "rawvideo", "-pixel_format", "rgb24",
        "-video_size", f"{W}x{H}", "-framerate", str(FPS), "-i", "-",
        "-frames:v", str(n_frames),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p",
        path,
    ]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE)

def render(path, duration_frames, content_fn, particles=None, source=None):
    particles = particles or make_particles()
    proc = open_writer(path, duration_frames)
    for i in range(duration_frames):
        t = i / FPS
        img = base_frame(t, particles)
        content_fn(img, t, i, duration_frames)
        img = Image.alpha_composite(img, FRAME_OVERLAY)
        if source:
            source_note(img, source)
        rgb = img.convert("RGB")
        proc.stdin.write(np.asarray(rgb, dtype=np.uint8).tobytes())
    proc.stdin.close()
    proc.wait()
