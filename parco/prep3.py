from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
from collections import deque
SRC = "/tmp/claude-0/-home-user-Tr/849f8aec-d85c-569a-8f81-2125e45b7ce6/images/%d.webp"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def key(im, lo=20, hi=70, erode=5):
    a = np.asarray(im.convert("RGB")).astype(np.float32); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    gd = g - np.maximum(r, b)
    alpha = np.clip(1 - (gd-lo)/(hi-lo), 0, 1)
    from PIL import ImageFilter as IF
    A = Image.fromarray((alpha*255).astype(np.uint8))
    A = A.filter(IF.MinFilter(erode))                      # mangia l'alone
    A = A.filter(IF.GaussianBlur(0.8))
    edge = np.asarray(A.filter(IF.MinFilter(13))) < 250      # fascia di bordo (~6px)
    g2 = np.where(edge, np.minimum(g, np.maximum(r, b)), g)
    return np.dstack([r, g2, b, np.asarray(A)]).astype(np.uint8)

def components(arr, thr=128, min_area=2000):
    m = arr[..., 3] > thr; h, w = m.shape; lab = np.zeros((h, w), np.int32); comps = []; k = 0
    for y in range(h):
        for x in range(w):
            if m[y, x] and lab[y, x] == 0:
                k += 1; q = deque([(y, x)]); lab[y, x] = k; pts = 0; x0 = x1 = x; y0 = y1 = y
                while q:
                    cy, cx = q.popleft(); pts += 1
                    x0 = min(x0, cx); x1 = max(x1, cx); y0 = min(y0, cy); y1 = max(y1, cy)
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and lab[ny, nx] == 0: lab[ny, nx] = k; q.append((ny, nx))
                if pts >= min_area: comps.append((pts, k, (x0, y0, x1+1, y1+1)))
    return lab, comps

def cut(arr, lab, k, box, pad=6):
    a = arr.copy(); a[..., 3] = np.where(lab == k, a[..., 3], 0)
    x0, y0, x1, y1 = box
    return Image.fromarray(a, "RGBA").crop((max(0, x0-pad), max(0, y0-pad), x1+pad, y1+pad))

# personaggi
for idx, name in ((6, "chip"), (7, "spike")):
    arr = key(Image.open(SRC % idx)); lab, comps = components(arr, min_area=20000)
    pts, k, box = max(comps); cut(arr, lab, k, box).save(f"assets/s/{name}.png"); print(name, box)

# sfondo: via la filigrana (clona un pezzo di prato) e porta a 1080x1920
bg = Image.open(SRC % 8).convert("RGB")
patch = bg.crop((560, 1290, 680, 1376)); bg.paste(patch, (648, 1290))
bg = bg.resize((1080, 1546), Image.LANCZOS)
bg = bg.crop((0, 0, 1080, 1546)).resize((1080, 1920), Image.LANCZOS) if False else bg.resize((1080, 1920), Image.LANCZOS)
bg.save("assets/s/sfondo.png")

# cestini: scritte in italiano
im = Image.open(SRC % 9).convert("RGB"); d = ImageDraw.Draw(im)
for (x0, x1), lab in (((236, 397), "PLASTICA"), ((603, 764), "CARTA"), ((970, 1131), "UMIDO")):
    d.rectangle([x0+6, 392, x1-6, 450], fill=(236, 238, 240))
    f = ImageFont.truetype(FONT, 25)
    d.text(((x0+x1)/2, 421), lab, font=f, fill=(25, 25, 30), anchor="mm")
arr = key(im, 25, 80, 3); lab, comps = components(arr, min_area=20000)
comps = sorted(sorted(comps, reverse=True)[:3], key=lambda c: c[2][0])
for (pts, k, box), n in zip(comps, ("giallo", "blu", "marrone")):
    cut(arr, lab, k, box).save(f"assets/s/bin_{n}.png"); print("bin", n, box)

# rifiuti: copri il logo Pepsi
Image.open(SRC % 10).convert("RGB").save("/tmp/x10.png")
import cv2
cv = cv2.imread("/tmp/x10.png"); mask = np.zeros(cv.shape[:2], np.uint8)
cv2.ellipse(mask, (714, 560), (52, 38), 0, 0, 360, 255, -1)
cv2.rectangle(mask, (668, 586), (762, 616), 255, -1)
cv = cv2.inpaint(cv, mask, 9, cv2.INPAINT_TELEA)
im = Image.fromarray(cv2.cvtColor(cv, cv2.COLOR_BGR2RGB))
arr = key(im, 25, 80, 3); lab, comps = components(arr, min_area=1500)
comps = sorted(comps, reverse=True)[:6]
comps = sorted(comps, key=lambda c: (c[2][1] > 380, c[2][0]))
names = ["bottle", "paper", "news", "peel", "can", "core"]
for (pts, k, box), n in zip(comps, names):
    cut(arr, lab, k, box).save(f"assets/s/item_{n}.png"); print("item", n, box, pts)
