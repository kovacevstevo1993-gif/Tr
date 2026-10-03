#!/usr/bin/env python3
"""Miniature per lo Short 'Il barattolo misterioso': 1280x720 (YouTube) e 1080x1920 (verticale). Usa gli asset già generati (nessun costo)."""
import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops, ImageEnhance
HERE = os.path.dirname(os.path.abspath(__file__)); A = lambda *p: os.path.join(HERE, "assets", *p)
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def crop(im):
    return im.crop(im.getchannel("A").point(lambda v: 255 if v > 30 else 0).getbbox())


def pose(n, h, mirror=False):
    im = crop(Image.open(A("pose", n + ".png")).convert("RGBA"))
    if mirror: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    return im.resize((int(im.width * h / im.height), int(h)), Image.LANCZOS)


def glow(size, cx, cy, r, col, a=1.0):
    y, x = np.mgrid[0:size[1], 0:size[0]]; d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2) / r
    g = np.clip(1 - d, 0, 1) ** 1.6 * a
    return np.dstack([np.full(g.shape, c) * g for c in col]).astype("float32")


def add_glow(img, cx, cy, r, col, a=1.0):
    arr = np.asarray(img).astype("float32") + glow(img.size, cx, cy, r, col, a)
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))


def shadow_paste(img, im, x, y, blur=14, off=(10, 14), alpha=120):
    sh = Image.new("RGBA", im.size, (20, 8, 0, 0)); sh.putalpha(im.getchannel("A").point(lambda v: min(v, alpha)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); lay.paste(sh, (x + off[0], y + off[1]), sh)
    lay = lay.filter(ImageFilter.GaussianBlur(blur)); img.paste(lay, (0, 0), lay); img.paste(im, (x, y), im)


def outline_text(img, s, cx, cy, size, fill, out, ow, rot=0, shadow=True):
    f = ImageFont.truetype(F, size); lay = Image.new("RGBA", (img.width * 2, size * 3), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    c = (lay.width // 2, lay.height // 2)
    if shadow: d.text((c[0] + 8, c[1] + 12), s, font=f, fill=(0, 0, 0, 150), anchor="mm", stroke_width=ow, stroke_fill=(0, 0, 0, 150))
    d.text(c, s, font=f, fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)
    lay = lay.rotate(rot, resample=Image.BICUBIC, expand=True)
    img.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)


def rays(img, cx, cy, col=(255, 240, 160), n=14, a=70):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); R = max(img.size) * 1.2
    for k in range(n):
        a0 = 2 * math.pi * k / n; a1 = a0 + math.pi / n
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=col + (a,))
    lay = lay.filter(ImageFilter.GaussianBlur(6)); img.paste(lay, (0, 0), lay)


def jar_scene(img, cx, base, h, tilt=-6):
    body = crop(Image.open(A("obj", "jar_open.png")).convert("RGBA")); cap = crop(Image.open(A("obj", "lid.png")).convert("RGBA"))
    k = h / (body.height + cap.height); w = int(body.width * k)
    cv = Image.new("RGBA", (w + 40, int(h) + 60), (0, 0, 0, 0))
    cv.paste(body.resize((w, int(body.height * k)), Image.LANCZOS), (20, 60 + int(cap.height * k)))
    cp = cap.resize((w, int(cap.height * k)), Image.LANCZOS); cv.paste(cp, (20, 22), cp)   # coperchio sollevato
    cv = cv.rotate(tilt, resample=Image.BICUBIC, expand=True)
    shadow_paste(img, cv, int(cx - cv.width / 2), int(base - cv.height))


def sparkle(img, x, y, r, col=(255, 250, 200)):
    d = ImageDraw.Draw(img, "RGBA"); k = 0.18
    d.polygon([(x, y - r), (x + r * k, y - r * k), (x + r, y), (x + r * k, y + r * k), (x, y + r), (x - r * k, y + r * k), (x - r, y), (x - r * k, y - r * k)], fill=col + (255,))


def finish(img):
    img = ImageEnhance.Contrast(img).enhance(1.12); img = ImageEnhance.Color(img).enhance(1.18)
    vig = Image.new("L", img.size, 0); d = ImageDraw.Draw(vig); d.ellipse([-img.width * .25, -img.height * .25, img.width * 1.25, img.height * 1.25], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(img.width / 6)); dark = Image.new("RGB", img.size, (60, 25, 10))
    return Image.composite(img, Image.blend(img, dark, 0.45), vig)


def wide():
    W, H = 1280, 720
    bg = Image.open(A("amb", "cucina.png")).convert("RGB"); bg = bg.resize((W, int(W * bg.height / bg.width)), Image.BICUBIC)
    img = bg.crop((0, 560, W, 560 + H)).filter(ImageFilter.GaussianBlur(2.2))
    rays(img, 960, 470); img = add_glow(img, 960, 450, 360, (255, 190, 70), 0.95); rays(img, 960, 470, a=40, n=9)
    jar_scene(img, 985, 700, 470)
    for (n, h, x, m) in (("topo_sorpreso", 440, 110, False), ("chip_sorpreso", 410, 345, False), ("spike_sorpreso", 370, 540, True)):
        im = pose(n, h, m); shadow_paste(img, im, x, 712 - im.height)
    for (x, y, r) in ((760, 300, 30), (1200, 280, 36), (1230, 480, 24), (800, 470, 22), (1100, 230, 20)): sparkle(img, x, y, r)
    outline_text(img, "COSA C'È", 450, 95, 128, (255, 244, 120), (200, 40, 70), 12, rot=-2)
    outline_text(img, "NEL BARATTOLO?!", 610, 205, 84, (255, 255, 255), (70, 40, 140), 10, rot=-2)
    return finish(img)


def tall():
    W, H = 1080, 1920
    img = Image.open(A("amb", "cucina.png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2.5))
    rays(img, 540, 900, n=16); img = add_glow(img, 540, 880, 560, (255, 190, 70), 0.95)
    jar_scene(img, 540, 1290, 720)
    x = 20
    for (n, h, m) in (("topo_sorpreso", 540, False), ("chip_sorpreso", 500, False), ("spike_sorpreso", 440, True)):
        im = pose(n, h, m); shadow_paste(img, im, x, 1830 - im.height); x += im.width - 10
    for (px, y, r) in ((200, 700, 44), (900, 640, 52), (960, 1000, 34), (130, 1000, 30), (780, 480, 28)): sparkle(img, px, y, r)
    outline_text(img, "COSA C'È", W / 2, 200, 175, (255, 244, 120), (200, 40, 70), 16, rot=-3)
    outline_text(img, "NEL BARATTOLO?!", W / 2, 385, 90, (255, 255, 255), (70, 40, 140), 11, rot=-3)
    return finish(img)


if __name__ == "__main__":
    wide().save(os.path.join(HERE, "miniatura_barattolo_1280x720.jpg"), quality=93)
    tall().save(os.path.join(HERE, "miniatura_barattolo_1080x1920.jpg"), quality=93)
    print("ok")
