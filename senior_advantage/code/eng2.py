import sys, math, os, random, subprocess
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from engine import (W, H, FPS, GREEN_D, GREEN_M, GREEN_L, CARD, IVORY, SAGE, SAGE_D, GOLD,
                    FONT_SERIF, FONT_SANS, FONT_SANS_M, font, ease, ease_back, seg, background)
from PIL import Image, ImageDraw, ImageFilter, ImageChops

CORAL = (214, 108, 96)
DARK = (7, 38, 30)
LINE = (52, 104, 84)

_sc = {}
def cache(key, fn):
    v = _sc.get(key)
    if v is None:
        v = fn()
        _sc[key] = v
    return v

# ------------------------------------------------------------------ canvas
class Cv:
    """canvas RGBA supersampled: si disegna in coordinate logiche"""
    def __init__(self, w, h, ss=2):
        self.w, self.h, self.ss = w, h, ss
        self.im = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)
    def _b(self, b):
        return [v * self.ss for v in b]
    def rrect(self, b, r, fill=None, outline=None, width=1):
        self.d.rounded_rectangle(self._b(b), radius=r * self.ss, fill=fill, outline=outline,
                                 width=max(1, int(width * self.ss)))
    def ell(self, b, fill=None, outline=None, width=1):
        self.d.ellipse(self._b(b), fill=fill, outline=outline, width=max(1, int(width * self.ss)))
    def line(self, p, fill, width):
        self.d.line(self._b(p), fill=fill, width=max(1, int(width * self.ss)), joint="curve")
    def poly(self, pts, fill):
        self.d.polygon([(x * self.ss, y * self.ss) for x, y in pts], fill=fill)
    def arc(self, b, a0, a1, fill, width):
        self.d.arc(self._b(b), a0, a1, fill=fill, width=max(1, int(width * self.ss)))
    def text(self, xy, s, path, size, fill, anchor="mm", track=0, bold=True):
        f = font(path, int(size * self.ss), bold)
        x, y = xy[0] * self.ss, xy[1] * self.ss
        if not track:
            self.d.text((x, y), s, font=f, fill=fill, anchor=anchor)
            return
        adv = [self.d.textlength(ch, font=f) + track * self.ss for ch in s]
        total = sum(adv) - track * self.ss
        if anchor[0] == "m":
            x -= total / 2
        elif anchor[0] == "r":
            x -= total
        for ch, a in zip(s, adv):
            self.d.text((x, y), ch, font=f, fill=fill, anchor="l" + anchor[1])
            x += a
    def done(self):
        return self.im.resize((self.w, self.h), Image.LANCZOS)

# ------------------------------------------------------------------ testo come sprite
def tspr(text, path, size, fill, track=0, bold=True):
    def mk():
        ss = 2
        f = font(path, size * ss, bold)
        d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
        if track:
            adv = [d0.textlength(ch, font=f) + track * ss for ch in text]
        else:
            adv = [d0.textlength(text, font=f)]
        tw = int(sum(adv))
        pad = int(size * 0.35) * ss
        hh = int(size * 1.6) * ss
        im = Image.new("RGBA", (tw + 2 * pad, hh), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        if track:
            x = pad
            for ch, a in zip(text, adv):
                d.text((x, hh // 2), ch, font=f, fill=fill, anchor="lm")
                x += a
        else:
            d.text((pad, hh // 2), text, font=f, fill=fill, anchor="lm")
        return im.resize((im.width // ss, im.height // ss), Image.LANCZOS)
    return cache(("t", text, path, size, fill, track, bold), mk)

# ------------------------------------------------------------------ incolla con scala / rotazione / alpha / ombra
def put(img, spr, cx, cy, scale=1.0, rot=0.0, alpha=1.0, shadow=0):
    s = spr
    if scale != 1.0:
        s = s.resize((max(1, int(s.width * scale)), max(1, int(s.height * scale))), Image.BILINEAR)
    if rot:
        s = s.rotate(rot, resample=Image.BICUBIC, expand=True)
    x, y = int(cx - s.width / 2), int(cy - s.height / 2)
    if shadow:
        pad = int(shadow * 3)
        sh = Image.new("L", (s.width + 2 * pad, s.height + 2 * pad), 0)
        sh.paste(s.getchannel("A").point(lambda v: int(v * 0.6 * alpha)), (pad, pad))
        sh = sh.filter(ImageFilter.GaussianBlur(shadow))
        img.paste(Image.new("RGB", sh.size, (3, 18, 14)),
                  (x - pad + int(shadow * 0.3), y - pad + int(shadow * 0.9)), sh)
    if alpha < 1.0:
        a = s.getchannel("A").point(lambda v: int(v * max(0.0, alpha)))
        s = s.copy()
        s.putalpha(a)
    img.paste(s, (x, y), s)

def pop(t, t0, dur=0.45):
    a = seg(t, t0, dur)
    return max(ease_back(a), 0.01), min(1.0, a * 3.0), a

def rot_off(dx, dy, deg):
    r = math.radians(deg)
    return dx * math.cos(r) + dy * math.sin(r), -dx * math.sin(r) + dy * math.cos(r)

# ------------------------------------------------------------------ effetti generici
def glow_spr(size=700):
    def mk():
        m = Image.new("L", (size, size), 0)
        d = ImageDraw.Draw(m)
        for i in range(60):
            r = int(size / 2 * (1 - i / 60))
            d.ellipse([size / 2 - r, size / 2 - r, size / 2 + r, size / 2 + r], fill=int(255 * (i / 60) ** 1.5))
        m = m.filter(ImageFilter.GaussianBlur(30))
        im = Image.new("RGBA", (size, size), (246, 241, 229, 0))
        im.putalpha(m)
        return im
    return cache(("glow", size), mk)

def star_spr(color):
    def mk():
        c = Cv(44, 44)
        c.poly([(22, 0), (27, 17), (44, 22), (27, 27), (22, 44), (17, 27), (0, 22), (17, 17)], fill=color)
        return c.done()
    return cache(("star", color), mk)

def burst(img, t, t0, cx, cy, n=12, color=GOLD, dur=0.7, rad=240, seed=1):
    a = (t - t0) / dur
    if a <= 0 or a >= 1:
        return
    rnd = random.Random(seed)
    for _ in range(n):
        ang = rnd.uniform(0, 6.283)
        r = rad * ease(a) * rnd.uniform(0.5, 1.0)
        sz = rnd.uniform(0.7, 1.4) * (1 - a)
        put(img, star_spr(color), cx + math.cos(ang) * r, cy + math.sin(ang) * r,
            scale=max(0.05, sz), alpha=1 - a, rot=rnd.uniform(0, 90) + a * 180)

def ambient(img, t, glyphs="%$", n=8, seed=3, alpha=0.16):
    rnd = random.Random(seed)
    for i in range(n):
        g = glyphs[i % len(glyphs)]
        x0 = rnd.uniform(90, W - 90)
        sp = rnd.uniform(26, 58)
        ph = rnd.uniform(0, 6.28)
        sz = rnd.choice([70, 90, 120])
        off = rnd.uniform(0, H + 240)
        y = (off - t * sp) % (H + 240) - 120
        x = x0 + math.sin(t * 0.8 + ph) * 24
        put(img, tspr(g, FONT_SANS, sz, SAGE_D), x, y, alpha=alpha, rot=math.sin(t + ph) * 14)

def shined(spr, a, strength=80):
    w, h = spr.size
    band = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(band)
    x = int(-0.4 * w + a * 1.8 * w)
    bw = int(w * 0.16)
    d.polygon([(x, 0), (x + bw, 0), (x + bw - int(h * 0.5), h), (x - int(h * 0.5), h)], fill=strength)
    band = band.filter(ImageFilter.GaussianBlur(12))
    band = ImageChops.multiply(band, spr.getchannel("A"))
    out = spr.copy()
    out.paste(Image.new("RGBA", (w, h), (255, 255, 255, 255)), (0, 0), band)
    return out

def label_spr(text, color):
    def mk():
        ts = tspr(text, FONT_SANS, 42, color, track=11)
        w, h = ts.width + 70, ts.height
        im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        im.paste(ts, (60, 0), ts)
        c = Cv(60, h)
        cy = h // 2
        c.poly([(8, cy), (26, cy - 17), (44, cy), (26, cy + 17)], fill=color)
        d = c.done()
        im.paste(d, (0, 0), d)
        return im
    return cache(("lab", text, color), mk)

def label(img, t, text, y, color, t0=0.0):
    a = seg(t, t0, 0.5)
    if a <= 0:
        return
    put(img, label_spr(text, color), W // 2, y - 40 * (1 - ease(a)), alpha=ease(a))

def bubble_spr(w, h, fill=IVORY, lines=None, tcolor=DARK, size=46):
    def mk():
        c = Cv(w, h + 44)
        c.rrect((0, 0, w, h), 38, fill=fill)
        c.poly([(46, h - 6), (112, h - 6), (36, h + 42)], fill=fill)
        if lines:
            n = len(lines)
            for i, ln in enumerate(lines):
                c.text((w / 2, h / 2 + (i - (n - 1) / 2) * (size * 1.18)), ln, FONT_SANS, size, tcolor)
        return c.done()
    return cache(("bub", w, h, fill, tuple(lines) if lines else None, tcolor, size), mk)

def dot_spr(color=DARK, r=15):
    def mk():
        c = Cv(r * 2 + 2, r * 2 + 2)
        c.ell((1, 1, r * 2 + 1, r * 2 + 1), fill=color)
        return c.done()
    return cache(("dot", color, r), mk)

def panel_spr(w, h, text, size, tcolor=IVORY, border=GOLD, sub=None, subcolor=SAGE):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 36, fill=CARD, outline=border, width=5)
        if sub:
            c.text((w / 2, h * 0.40), text, FONT_SANS, size, tcolor)
            c.text((w / 2, h * 0.74), sub, FONT_SANS, int(size * 0.5), subcolor, track=6)
        else:
            c.text((w / 2, h / 2), text, FONT_SANS, size, tcolor)
        return c.done()
    return cache(("pan", w, h, text, size, tcolor, border, sub))

# ------------------------------------------------------------------ render veloce (pipe diretta a ffmpeg)
def render_seq(draw_fn, nframes, out, log=None):
    background(0)   # scalda la cache
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p",
           "-crf", "18", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes):
        t = i / FPS
        img = background(t)
        draw_fn(img, t)
        p.stdin.write(img.tobytes())
        if log and i % 20 == 0:
            with open(log, "a") as f:
                f.write(f"{os.path.basename(out)} {i}/{nframes}\n")
    p.stdin.close()
    p.wait()
