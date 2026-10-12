"""Varianti con lip-sync (bocca chiusa/aperta) e occhi che sbattono, dipinte sulle immagini AI Studio."""
import numpy as np, math
from PIL import Image, ImageDraw, ImageFilter
exec(open("prep3.py").read().split("# personaggi")[0])      # key(), components(), cut()
SRC = "/tmp/claude-0/-home-user-Tr/849f8aec-d85c-569a-8f81-2125e45b7ce6/images/%d.webp"

def fur_color(im, cx, cy, rx, ry):
    a = np.asarray(im.convert("RGB")).astype(np.float32); H, W_ = a.shape[:2]
    ys, xs = np.mgrid[max(0, int(cy-ry*2.2)):min(H, int(cy+ry*2.2)), max(0, int(cx-rx*2.2)):min(W_, int(cx+rx*2.2))]
    d = ((xs-cx)/(rx+4))**2 + ((ys-cy)/(ry+4))**2
    m = (d > 1.1) & (d < 2.2) & (ys < cy+ry*0.6)
    px = a[ys[m], xs[m]]; return tuple(int(v) for v in np.median(px, axis=0))

def blink(im, eyes, line_col_k=0.42):
    """Chiude gli occhi: copre con il colore del pelo e disegna la palpebra."""
    S = 4; out = im.convert("RGBA")
    for cx, cy, rx, ry in eyes:
        fc = fur_color(out, cx, cy, rx, ry)
        x0, y0, x1, y1 = int(cx-rx*1.6), int(cy-ry*1.6), int(cx+rx*1.6), int(cy+ry*1.6)
        patch = out.crop((x0, y0, x1, y1)); big = patch.resize((patch.width*S, patch.height*S), Image.BICUBIC)
        d = ImageDraw.Draw(big); ox, oy = (cx-x0)*S, (cy-y0)*S
        d.ellipse([ox-(rx+5)*S, oy-(ry+6)*S, ox+(rx+5)*S, oy+(ry+5)*S], fill=fc+(255,))
        big = big.filter(ImageFilter.GaussianBlur(2*S)) if False else big
        d = ImageDraw.Draw(big); lc = tuple(int(c*line_col_k) for c in fc) + (255,)
        pts = [(ox+(t*rx*1.05)*S, oy+(0.22*ry*(1-t*t)+0.1*ry)*S) for t in np.linspace(-1, 1, 24)]
        d.line(pts, fill=lc, width=int(3.2*S), joint="curve")
        for sx in (-1, 1):   # ciglia
            d.line([(ox+sx*rx*1.02*S, oy+0.1*ry*S), (ox+sx*rx*1.3*S, oy-0.05*ry*S)], fill=lc, width=int(2.4*S))
        small = big.resize(patch.size, Image.LANCZOS)
        mask = Image.new("L", patch.size, 0); ImageDraw.Draw(mask).ellipse([4, 4, patch.width-4, patch.height-4], fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(5)); out.paste(small, (x0, y0), mask)
    return out

def mouth(im, cx, cy, level, teeth=False, scale=1.0):
    if level == 0: return im
    S = 4; out = im.convert("RGBA")
    rx, ry = (24*scale, 13*scale) if level == 1 else (31*scale, 27*scale)
    x0, y0, x1, y1 = int(cx-60*scale), int(cy-40*scale), int(cx+60*scale), int(cy+55*scale)
    patch = out.crop((x0, y0, x1, y1)); big = patch.resize((patch.width*S, patch.height*S), Image.BICUBIC)
    d = ImageDraw.Draw(big); ox, oy = (cx-x0)*S, (cy-y0+ry*0.25)*S
    d.ellipse([ox-(rx+3)*S, oy-(ry+3)*S, ox+(rx+3)*S, oy+(ry+3)*S], fill=(150, 80, 70, 255))   # labbro
    d.ellipse([ox-rx*S, oy-ry*S, ox+rx*S, oy+ry*S], fill=(62, 18, 24, 255))                    # interno
    tg = Image.new("RGBA", big.size, (0, 0, 0, 0)); td = ImageDraw.Draw(tg)
    td.ellipse([ox-rx*0.7*S, oy+ry*0.1*S, ox+rx*0.7*S, oy+ry*1.15*S], fill=(214, 100, 110, 255))   # lingua
    cm = Image.new("L", big.size, 0); ImageDraw.Draw(cm).ellipse([ox-rx*S, oy-ry*S, ox+rx*S, oy+ry*S], fill=255)
    big.paste(tg, (0, 0), Image.composite(tg.getchannel("A"), Image.new("L", big.size, 0), cm))
    if teeth:
        d = ImageDraw.Draw(big)
        tw = rx*0.62
        tm = Image.new("L", big.size, 0); ImageDraw.Draw(tm).rounded_rectangle([ox-tw*S, oy-ry*S, ox+tw*S, oy-ry*S+ry*0.9*S], radius=int(5*S), fill=255)
        tm = Image.composite(tm, Image.new("L", big.size, 0), cm)
        big.paste(Image.new("RGBA", big.size, (250, 246, 236, 255)), (0, 0), tm)
        d.line([(ox, oy-ry*S), (ox, oy-ry*S+ry*0.85*S)], fill=(190, 180, 170, 255), width=int(1.6*S))
    small = big.resize(patch.size, Image.LANCZOS)
    mask = Image.new("L", patch.size, 0); ImageDraw.Draw(mask).ellipse([3, 3, patch.width-3, patch.height-3], fill=255)
    out.paste(small, (x0, y0), mask.filter(ImageFilter.GaussianBlur(3))); return out

CH = {"chip": dict(src=6, eyes=[(302, 472, 30, 26), (470, 475, 30, 26)], mouth=(387, 566), teeth=True, ms=1.0),
      "spike": dict(src=7, eyes=[(305, 535, 30, 26), (465, 532, 30, 26)], mouth=(387, 632), teeth=False, ms=1.0)}
for name, c in CH.items():
    arr = key(Image.open(SRC % c["src"])); lab, comps = components(arr, min_area=20000)
    pts, k, box = max(comps); x0, y0 = max(0, box[0]-6), max(0, box[1]-6)
    base = cut(arr, lab, k, box)
    eyes = [(cx-x0, cy-y0, rx, ry) for cx, cy, rx, ry in c["eyes"]]; mx, my = c["mouth"][0]-x0, c["mouth"][1]-y0
    for m in (0, 1, 2):
        im = mouth(base, mx, my, m, c["teeth"], c["ms"])
        im.save(f"assets/v/{name}_m{m}b0.png"); blink(im, eyes).save(f"assets/v/{name}_m{m}b1.png")
# topolino: occhi che sbattono sulle pose con occhi aperti
for n, eyes in (("neutro", [(302, 405, 36, 34), (470, 402, 36, 34)]), ("parla", [(302, 405, 36, 34), (470, 402, 36, 34)])):
    full = Image.open(f"assets/topo/{n}_full.png").convert("RGBA"); bb = full.getbbox()
    full.crop(bb).save(f"assets/v/mouse_{n}_b0.png"); blink(full, eyes).crop(bb).save(f"assets/v/mouse_{n}_b1.png")
for n in ("braccia_su", "triste"):
    Image.open(f"assets/topo/{n}.png").save(f"assets/v/mouse_{n}.png")
print("ok")
