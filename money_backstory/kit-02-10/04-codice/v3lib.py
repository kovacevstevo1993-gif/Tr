from common2 import *
import random, math

purple = (170, 130, 230)
pink = (230, 140, 190)
goldD = (150, 110, 40)

def A(c, a):
    return tuple(c) + (int(max(0, min(255, a))),)

def coin(L, cx, cy, r, alpha=255, squash=1.0):
    d = ImageDraw.Draw(L)
    ry = r * squash
    d.ellipse([cx - r, cy - ry, cx + r, cy + ry], fill=A(goldD, alpha))
    d.ellipse([cx - r + 3, cy - ry + 3, cx + r - 3, cy + ry - 3], fill=A(gold, alpha))
    d.ellipse([cx - r * 0.72, cy - ry * 0.72, cx + r * 0.72, cy + ry * 0.72], outline=A(goldL, alpha), width=3)
    if squash > 0.6:
        f = BOLD(int(r * 1.05))
        b = d.textbbox((0, 0), '$', font=f)
        d.text((cx - (b[2] - b[0]) / 2 - b[0], cy - (b[3] - b[1]) / 2 - b[1]), '$', font=f, fill=A(goldD, alpha))

def coin_stack(L, x, base_y, n, r=62, alpha=255):
    d = ImageDraw.Draw(L)
    th = 20
    for k in range(n):
        y = base_y - k * th
        d.ellipse([x - r, y - r * 0.36 + th * 0.6, x + r, y + r * 0.36 + th * 0.6], fill=A(goldD, alpha))
        d.rectangle([x - r, y - r * 0.02, x + r, y + th * 0.6], fill=A(goldD, alpha))
        d.ellipse([x - r, y - r * 0.36, x + r, y + r * 0.36], fill=A(gold, alpha), outline=A(goldL, alpha), width=2)

def bill(L, cx, cy, w=230, h=112, ang=0, alpha=255, col=(84, 200, 124)):
    im = Image.new('RGBA', (w + 30, h + 30), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, y0 = 15, 15
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=12, fill=A(col, alpha), outline=A((30, 110, 60), alpha), width=4)
    d.rounded_rectangle([x0 + 12, y0 + 12, x0 + w - 12, y0 + h - 12], radius=8, outline=A((190, 245, 205), alpha), width=2)
    d.ellipse([x0 + w / 2 - 34, y0 + h / 2 - 34, x0 + w / 2 + 34, y0 + h / 2 + 34], fill=A((30, 110, 60), alpha))
    f = BOLD(46)
    b = d.textbbox((0, 0), '$', font=f)
    d.text((x0 + w / 2 - (b[2] - b[0]) / 2 - b[0], y0 + h / 2 - (b[3] - b[1]) / 2 - b[1]), '$', font=f, fill=A((205, 250, 215), alpha))
    d.ellipse([x0 + 18, y0 + 18, x0 + 40, y0 + 40], outline=A((190, 245, 205), alpha), width=2)
    d.ellipse([x0 + w - 40, y0 + h - 40, x0 + w - 18, y0 + h - 18], outline=A((190, 245, 205), alpha), width=2)
    im = im.rotate(ang, expand=True, resample=Image.BICUBIC)
    L.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def money_bag(L, cx, cy, s=1.0, alpha=255, col=gold):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - 95 * s, cy - 70 * s, cx + 95 * s, cy + 100 * s], fill=A(col, alpha), outline=A(goldD, alpha), width=4)
    d.polygon([(cx - 40 * s, cy - 62 * s), (cx - 55 * s, cy - 110 * s), (cx + 55 * s, cy - 110 * s), (cx + 40 * s, cy - 62 * s)], fill=A(col, alpha), outline=A(goldD, alpha))
    d.rounded_rectangle([cx - 52 * s, cy - 72 * s, cx + 52 * s, cy - 52 * s], radius=8, fill=A(goldD, alpha))
    f = BOLD(int(96 * s))
    b = d.textbbox((0, 0), '$', font=f)
    d.text((cx - (b[2] - b[0]) / 2 - b[0], cy + 10 * s - (b[3] - b[1]) / 2 - b[1]), '$', font=f, fill=A(goldD, alpha))

def building(L, cx, cy, w=320, h=260, col=gold, alpha=255):
    d = ImageDraw.Draw(L)
    x0, x1 = cx - w / 2, cx + w / 2
    top = cy - h / 2
    d.polygon([(x0 - 10, top + 70), (cx, top), (x1 + 10, top + 70)], fill=A(col, alpha))
    d.rectangle([x0, top + 78, x1, top + 96], fill=A(col, alpha))
    n = 4
    cw = 36
    gap = (w - n * cw) / (n - 1)
    for k in range(n):
        xx = x0 + k * (cw + gap)
        d.rectangle([xx, top + 104, xx + cw, top + h - 40], fill=A(col, alpha))
    d.rectangle([x0 - 16, top + h - 34, x1 + 16, top + h - 14], fill=A(col, alpha))
    d.rectangle([x0 - 30, top + h - 12, x1 + 30, top + h + 8], fill=A(col, alpha))

def padlock(L, cx, cy, s=1.0, col=red, alpha=255, open_=False):
    d = ImageDraw.Draw(L)
    lw = 10 * s
    if open_:
        d.arc([cx - 46 * s, cy - 100 * s, cx + 46 * s, cy - 10 * s], start=180, end=340, fill=A(col, alpha), width=int(lw))
    else:
        d.arc([cx - 46 * s, cy - 92 * s, cx + 46 * s, cy - 6 * s], start=180, end=360, fill=A(col, alpha), width=int(lw))
        d.line([cx - 46 * s, cy - 50 * s, cx - 46 * s, cy], fill=A(col, alpha), width=int(lw))
        d.line([cx + 46 * s, cy - 50 * s, cx + 46 * s, cy], fill=A(col, alpha), width=int(lw))
    d.rounded_rectangle([cx - 70 * s, cy - 6 * s, cx + 70 * s, cy + 92 * s], radius=int(16 * s), fill=A(col, alpha))
    d.ellipse([cx - 12 * s, cy + 22 * s, cx + 12 * s, cy + 46 * s], fill=A(navy, alpha))
    d.rectangle([cx - 5 * s, cy + 40 * s, cx + 5 * s, cy + 68 * s], fill=A(navy, alpha))

def clock(L, cx, cy, r, t, col=goldL, alpha=255):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=A(col, alpha), width=8)
    for k in range(12):
        a = k * math.pi / 6
        d.line([cx + math.cos(a) * r * 0.82, cy + math.sin(a) * r * 0.82, cx + math.cos(a) * r * 0.94, cy + math.sin(a) * r * 0.94], fill=A(col, alpha), width=4)
    a = -math.pi / 2 + t * 2.4
    d.line([cx, cy, cx + math.cos(a) * r * 0.7, cy + math.sin(a) * r * 0.7], fill=A(col, alpha), width=8)
    a2 = -math.pi / 2 + t * 0.2
    d.line([cx, cy, cx + math.cos(a2) * r * 0.45, cy + math.sin(a2) * r * 0.45], fill=A(col, alpha), width=10)
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=A(col, alpha))

def door(L, cx, cy, w=110, h=170, col=blue, alpha=255, open_p=0.0):
    d = ImageDraw.Draw(L)
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=14, outline=A(col, alpha), width=8)
    ww = w * (1 - 0.72 * open_p)
    d.polygon([(cx - w / 2 + 6, cy - h / 2 + 6), (cx - w / 2 + 6 + ww, cy - h / 2 + 6 + 10 * open_p), (cx - w / 2 + 6 + ww, cy + h / 2 - 6 - 10 * open_p), (cx - w / 2 + 6, cy + h / 2 - 6)], fill=A(col, alpha * 0.85))
    d.ellipse([cx - w / 2 + ww - 14, cy - 8, cx - w / 2 + ww - 2, cy + 4], fill=A(goldL, alpha))

def up_arrow(L, cx, cy, s=1.0, col=green, alpha=255):
    d = ImageDraw.Draw(L)
    d.polygon([(cx, cy - 90 * s), (cx + 70 * s, cy - 10 * s), (cx + 28 * s, cy - 10 * s), (cx + 28 * s, cy + 80 * s), (cx - 28 * s, cy + 80 * s), (cx - 28 * s, cy - 10 * s), (cx - 70 * s, cy - 10 * s)], fill=A(col, alpha))

def check(L, cx, cy, r=34, col=green, alpha=255):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=A(col, alpha))
    d.line([cx - r * 0.45, cy + 2, cx - r * 0.1, cy + r * 0.38, cx + r * 0.5, cy - r * 0.35], fill=A((255, 255, 255), alpha), width=max(4, int(r * 0.2)), joint='curve')

def cross(L, cx, cy, r=34, col=red, alpha=255):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=A(col, alpha))
    k = r * 0.42
    d.line([cx - k, cy - k, cx + k, cy + k], fill=A((255, 255, 255), alpha), width=max(4, int(r * 0.22)))
    d.line([cx - k, cy + k, cx + k, cy - k], fill=A((255, 255, 255), alpha), width=max(4, int(r * 0.22)))

def stamp(fr, text, cx, cy, ang, col, s, size=54):
    if s <= 0.02:
        return fr
    f = BOLD(size)
    tmp = Image.new('RGBA', (10, 10))
    b = ImageDraw.Draw(tmp).textbbox((0, 0), text, font=f)
    tw, th = b[2] - b[0], b[3] - b[1]
    im = Image.new('RGBA', (tw + 90, th + 70), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([4, 4, im.width - 5, im.height - 5], radius=16, outline=A(col, 255), width=8)
    d.text((45 - b[0], 35 - b[1]), text, font=f, fill=A(col, 255))
    im = im.rotate(ang, expand=True, resample=Image.BICUBIC)
    im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))))
    fr.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))
    return fr

def rain(L, t, t0, x0, x1, floor, n=16, seed=3, r=30, dur=3.0):
    rnd = random.Random(seed)
    for k in range(n):
        st = t0 + rnd.uniform(0, dur)
        x = rnd.uniform(x0, x1)
        if t < st:
            continue
        u = t - st
        y = 90 + 260 * u + 220 * u * u
        if y > floor:
            continue
        a = 255 if y < floor - 80 else max(0, int(255 * (floor - y) / 80))
        coin(L, x, y, r, a, squash=abs(math.cos(u * 6 + k)) * 0.6 + 0.4)

def card_box(L, x0, y0, x1, y1, outline=gold, fill=card, alpha=255, width=4, radius=22):
    d = ImageDraw.Draw(L)
    d.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=A(fill, alpha), outline=A(outline, alpha), width=width)

def frames_split(sentences, total_frames):
    w = [len(x) + 10 for x in sentences]
    T = sum(w)
    fs = [round(x / T * total_frames) for x in w]
    fs[-1] = total_frames - sum(fs[:-1])
    return fs

def counter_text(v):
    return f'${int(v):,}'

def age59(C, cx, y, size, col):
    d = ImageDraw.Draw(C)
    f1 = BOLD(size); f2 = SER(int(size * 0.8))
    b1 = d.textbbox((0, 0), '59', font=f1); b2 = d.textbbox((0, 0), '\u00bd', font=f2)
    w1 = b1[2] - b1[0]; w2 = b2[2] - b2[0]; tot = w1 + w2 + 8
    x = cx - tot / 2
    d.text((x - b1[0], y - b1[1]), '59', font=f1, fill=A(col, 255))
    d.text((x + w1 + 8 - b2[0], y - b2[1] + size * 0.05), '\u00bd', font=f2, fill=A(col, 255))

# ---------------- extra helpers (blocks 3-10) ----------------
def avatar(L, cx, cy, col, s=1.0, alpha=255):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - 18 * s, cy - 52 * s, cx + 18 * s, cy - 16 * s], fill=A(col, alpha))
    d.rounded_rectangle([cx - 30 * s, cy - 10 * s, cx + 30 * s, cy + 46 * s], radius=int(22 * s), fill=A(col, alpha))

def bubble(L, x0, y0, x1, y1, text, fillc=(236, 240, 245), tcol=navy, size=36, tail=None, alpha=255):
    d = ImageDraw.Draw(L)
    d.rounded_rectangle([x0, y0, x1, y1], radius=28, fill=A(fillc, alpha))
    if tail == 'left':
        d.polygon([(x0 + 40, y1 - 4), (x0 + 6, y1 + 44), (x0 + 96, y1 - 4)], fill=A(fillc, alpha))
    if tail == 'right':
        d.polygon([(x1 - 40, y1 - 4), (x1 - 6, y1 + 44), (x1 - 96, y1 - 4)], fill=A(fillc, alpha))
    lines = text.split('\n'); f = BOLD(size); h = size * 1.3
    y = (y0 + y1) / 2 - h * len(lines) / 2 + 4
    for ln in lines:
        txt(L, ln, f, y, tcol, alpha, x=(x0 + x1) / 2); y += h

def flame(L, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(L)
    pts = [(0, -110), (22, -60), (58, -20), (62, 30), (38, 80), (0, 100), (-38, 80), (-62, 30), (-50, -15), (-20, -40)]
    d.polygon([(cx + x * s, cy + y * s) for x, y in pts], fill=A((240, 100, 50), alpha))
    pts2 = [(0, -40), (20, 0), (34, 40), (18, 78), (0, 88), (-18, 78), (-32, 40), (-16, 0)]
    d.polygon([(cx + x * s, cy + y * s) for x, y in pts2], fill=A((255, 205, 90), alpha))

def flag(L, x, y, t, alpha=255):
    d = ImageDraw.Draw(L)
    d.rectangle([x - 6, y - 300, x + 6, y], fill=A(goldL, alpha))
    for r in range(4):
        for c in range(6):
            wave = math.sin(t * 4 + c * 0.7) * 6
            col = (20, 20, 30) if (r + c) % 2 == 0 else (240, 240, 240)
            x0 = x + 8 + c * 30; y0 = y - 296 + r * 30 + wave * (c / 5)
            d.rectangle([x0, y0, x0 + 30, y0 + 30], fill=A(col, alpha))

def cart(L, cx, cy, s=1.0, alpha=255, col=gold):
    d = ImageDraw.Draw(L)
    w = max(2, int(8 * s))
    d.polygon([(cx - 90 * s, cy - 50 * s), (cx + 90 * s, cy - 50 * s), (cx + 65 * s, cy + 40 * s), (cx - 65 * s, cy + 40 * s)], outline=A(col, alpha), width=w)
    d.line([cx - 90 * s, cy - 50 * s, cx - 120 * s, cy - 90 * s, cx - 150 * s, cy - 90 * s], fill=A(col, alpha), width=w)
    d.ellipse([cx - 55 * s, cy + 52 * s, cx - 31 * s, cy + 76 * s], fill=A(col, alpha))
    d.ellipse([cx + 31 * s, cy + 52 * s, cx + 55 * s, cy + 76 * s], fill=A(col, alpha))

def wallet(L, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(L)
    d.rounded_rectangle([cx - 110 * s, cy - 70 * s, cx + 110 * s, cy + 70 * s], radius=int(20 * s), fill=A((150, 100, 50), alpha), outline=A(goldL, alpha), width=4)
    d.rounded_rectangle([cx + 30 * s, cy - 24 * s, cx + 120 * s, cy + 24 * s], radius=int(14 * s), fill=A((190, 135, 70), alpha), outline=A(goldL, alpha), width=3)
    d.ellipse([cx + 62 * s, cy - 9 * s, cx + 80 * s, cy + 9 * s], fill=A(goldL, alpha))

def phone(L, cx, cy, s=1.0, alpha=255, t=0.0, ring=True):
    d = ImageDraw.Draw(L)
    sh = math.sin(t * 40) * 4 if (ring and int(t * 3) % 2 == 0) else 0
    x = cx + sh
    d.rounded_rectangle([x - 60 * s, cy - 110 * s, x + 60 * s, cy + 110 * s], radius=int(24 * s), fill=A((30, 40, 60), alpha), outline=A(goldL, alpha), width=5)
    d.rounded_rectangle([x - 48 * s, cy - 90 * s, x + 48 * s, cy + 80 * s], radius=int(12 * s), fill=A((60, 110, 170), alpha))
    d.ellipse([x - 8 * s, cy + 88 * s, x + 8 * s, cy + 104 * s], outline=A(goldL, alpha), width=3)
    if ring:
        for k in (1, 2):
            r = 80 * s + k * 34 * s
            a2 = alpha * (0.5 + 0.5 * math.sin(t * 6 - k))
            d.arc([x - r, cy - r, x + r, cy + r], start=-35, end=35, fill=A(goldL, a2), width=6)
            d.arc([x - r, cy - r, x + r, cy + r], start=145, end=215, fill=A(goldL, a2), width=6)

def tax_form(L, x0, y0, w, h, alpha=255, label='TAX'):
    d = ImageDraw.Draw(L)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=12, fill=A((236, 240, 245), alpha), outline=A(red, alpha), width=4)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h * 0.22], radius=12, fill=A(red, alpha))
    txt(L, label, BOLD(int(h * 0.15)), y0 + h * 0.045, (255, 255, 255), alpha, x=x0 + w / 2)
    for k in range(4):
        d.rectangle([x0 + w * 0.12, y0 + h * 0.34 + k * h * 0.15, x0 + w * 0.88, y0 + h * 0.34 + k * h * 0.15 + h * 0.05], fill=A((170, 180, 200), alpha))

def briefcase(L, cx, cy, s=1.0, alpha=255, col=(150, 100, 50)):
    d = ImageDraw.Draw(L)
    d.arc([cx - 30 * s, cy - 70 * s, cx + 30 * s, cy - 10 * s], start=180, end=360, fill=A(goldL, alpha), width=max(2, int(8 * s)))
    d.rounded_rectangle([cx - 70 * s, cy - 40 * s, cx + 70 * s, cy + 40 * s], radius=int(12 * s), fill=A(col, alpha), outline=A(goldL, alpha), width=3)
    d.rectangle([cx - 70 * s, cy - 6 * s, cx + 70 * s, cy + 4 * s], fill=A(goldL, alpha))

def vault(L, cx, cy, r, t, open_p=0.0, alpha=255):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - r - 16, cy - r - 16, cx + r + 16, cy + r + 16], fill=A((60, 72, 92), alpha), outline=A(goldL, alpha), width=6)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=A((24, 32, 46), alpha))
    if open_p > 0.05:
        for k in range(3):
            coin(L, cx - r * 0.3 + k * r * 0.3, cy + r * 0.25, r * 0.2, alpha)
    w = r * (1 - 0.85 * open_p)
    d.ellipse([cx - r, cy - r, cx - r + 2 * w, cy + r], fill=A((110, 124, 148), alpha), outline=A(goldL, alpha), width=5)
    xc = cx - r + w
    if w > r * 0.3:
        for k in range(4):
            a = t * 0.8 + k * math.pi / 2
            d.line([xc - math.cos(a) * w * 0.4, cy - math.sin(a) * r * 0.4, xc + math.cos(a) * w * 0.4, cy + math.sin(a) * r * 0.4], fill=A(goldL, alpha), width=8)
        d.ellipse([xc - 16, cy - 16, xc + 16, cy + 16], fill=A(gold, alpha))

def bulb(L, cx, cy, s=1.0, alpha=255):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - 44 * s, cy - 60 * s, cx + 44 * s, cy + 28 * s], fill=A((255, 225, 120), alpha))
    d.rectangle([cx - 22 * s, cy + 24 * s, cx + 22 * s, cy + 60 * s], fill=A((170, 180, 200), alpha))
    for k in range(7):
        a = math.radians(-160 + k * 22)
        d.line([cx + math.cos(a) * 64 * s, cy - 16 * s + math.sin(a) * 64 * s, cx + math.cos(a) * 92 * s, cy - 16 * s + math.sin(a) * 92 * s], fill=A((255, 225, 120), alpha), width=6)

def title_layer(fr, text, t, size=62, y=90, col=None):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    txt(L, text, SER(size), y, col or goldL, 255 * ease(t / 0.4))
    return Image.alpha_composite(fr, L)

def pill_pop(fr, text, y, t, t0, col=red, tcol=(255, 255, 255), size=44, cx=None):
    if t < t0:
        return fr
    C = Image.new('RGBA', (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(C)
    f = BOLD(size); b = cd.textbbox((0, 0), text, font=f); bw = b[2] - b[0] + 80
    bx = (W - bw) / 2 if cx is None else cx - bw / 2
    hh = size * 2.1
    cd.rounded_rectangle([bx, y, bx + bw, y + hh], radius=int(hh / 2), fill=col + (255,))
    cd.text((bx + 40 - b[0], y + hh / 2 - (b[3] - b[1]) / 2 - b[1]), text, font=f, fill=tcol + (255,))
    return pop(fr, C, (int(bx) - 5, int(y) - 5, int(bx + bw) + 5, int(y + hh) + 5), back((t - t0) / 0.45))

def render_fast(draw, n_frames, out):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pixel_format", "rgb24", "-video_size", f"{W}x{H}", "-framerate", "30", "-i", "-",
           "-frames:v", str(n_frames), "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-crf", "19", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n_frames):
        p.stdin.write(draw(i / 30.0).convert('RGB').tobytes())
    p.stdin.close(); p.wait()
