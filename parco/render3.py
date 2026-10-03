#!/usr/bin/env python3
"""Puliamo il parco! v4 - TUTTO con le immagini AI Studio: sfondo, topolino, Chip, Spike, cestini, rifiuti."""
import math, sys, subprocess, os
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import render as R0                    # tempi, voci, keyframe dei personaggi
from render import lerp, ease, interp, VOICES

W, H, FPS, DUR = 1080, 1920, 24, 36.0
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FLY = 0.55

# ---------------------------------------------------------------- layout
BIN_X = {"giallo": 270, "blu": 540, "marrone": 810}
BIN_Y = 1340                       # piedi dei cestini
BIN_H = 400
BIN_STAND = {"giallo": (300, 1500), "blu": (560, 1500), "marrone": (800, 1500)}
ITEM_H = {"bottle": 62, "paper": 100, "news": 70, "peel": 62, "can": 105, "core": 98}   # altezza a terra (px)

KF = {
 "mouse": [(0, -170, 1620), (2.0, 300, 1620), (12.0, 300, 1620), (13.6, 260, 1700), (13.9, 260, 1700),
           (16.3, 300, 1500), (17.4, 300, 1500), (22.6, 770, 1710), (23.0, 770, 1710),
           (24.4, 330, 1500), (25.0, 330, 1500), (27.2, 540, 1650), (40, 540, 1650)],
 "chip":  [(6.8, 1250, 1700), (8.8, 600, 1700), (13.0, 600, 1700), (15.6, 520, 1800), (15.9, 520, 1800),
           (18.3, 560, 1500), (19.2, 560, 1500), (21.6, 950, 1800), (21.9, 950, 1800),
           (24.9, 590, 1500), (25.6, 590, 1500), (27.2, 300, 1660), (40, 300, 1660)],
 "spike": [(7.8, 1250, 1740), (9.6, 880, 1740), (14.0, 880, 1740), (18.0, 400, 1660), (18.3, 400, 1660),
           (20.9, 790, 1500), (21.8, 790, 1500), (23.4, 680, 1670), (23.7, 680, 1670),
           (25.8, 830, 1500), (26.6, 830, 1500), (28.0, 780, 1660), (40, 780, 1660)],
}
# (tipo, x, y, chi, t_raccolta, t_lancio, cestino)
ITEMS = [
 ("bottle", 270, 1712, "mouse", 13.9, 16.5, "giallo"),
 ("news",   525, 1806, "chip",  15.9, 18.6, "blu"),
 ("peel",   405, 1664, "spike", 18.3, 21.1, "marrone"),
 ("can",    775, 1714, "mouse", 23.0, 24.5, "giallo"),
 ("paper",  955, 1806, "chip",  21.9, 25.3, "blu"),
 ("core",   685, 1674, "spike", 23.7, 26.1, "marrone"),
]
CH_H = {"mouse": 540, "chip": 500, "spike": 470}     # altezza a y=1650

# ---------------------------------------------------------------- sprite
_cache = {}
def load(path):
    if path not in _cache: _cache[path] = Image.open(os.path.join(HERE, path)).convert("RGBA")
    return _cache[path]

def persp(y): return 0.86 + (y-1450)/1000*0.45

def put(img, sp, x, y, h, ang=0, sq=1.0, flip=False):
    """Incolla lo sprite con centro-basso in (x,y), alto h px, squash sq (>1 = più alto e stretto)."""
    if flip: sp = sp.transpose(Image.FLIP_LEFT_RIGHT)
    nh = max(1, int(h*sq)); nw = max(1, int(sp.width * h / sp.height / sq))
    s2 = sp.resize((nw, nh), Image.LANCZOS if nh < sp.height else Image.BICUBIC)
    if ang:
        pad = int(nw*0.3); cv = Image.new("RGBA", (nw+2*pad, nh+pad), (0, 0, 0, 0)); cv.paste(s2, (pad, 0), s2)
        cv = cv.rotate(ang, resample=Image.BICUBIC, center=(pad+nw//2, nh))
        img.paste(cv, (int(x - pad - nw/2), int(y - nh)), cv)
    else:
        img.paste(s2, (int(x - nw/2), int(y - nh)), s2)
    return nw, nh

SH = None
def shadow(img, x, y, w):
    global SH
    if SH is None:
        sh = Image.new("RGBA", (300, 80), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([20, 20, 280, 60], fill=(15, 50, 15, 110))
        SH = sh.filter(ImageFilter.GaussianBlur(8))
    s2 = SH.resize((int(w*1.3), int(w*1.3*80/300)), Image.BICUBIC); img.paste(s2, (int(x - s2.width/2), int(y - s2.height/2)), s2)

# ---------------------------------------------------------------- animazione
def speaking(name, t):
    return any(w == name and t0 <= t <= t0+d for k, t0, w, tx, d in VOICES)

def cstate(name, t):
    x, y, walking, dirn = interp(KF[name], t)
    h = CH_H[name]*persp(y)
    sq = 1.0; hop = 0; rot = 0
    ph = t*11 + (0 if name == "mouse" else 2 if name == "chip" else 4)
    if walking: hop = abs(math.sin(ph))*0.05*h; rot = math.sin(ph)*3.2; sq = 1 + 0.025*math.sin(ph*2)
    elif t >= 27.4: hop = abs(math.sin(t*5 + (0 if name == "mouse" else 1.5)))*0.09*h; rot = math.sin(t*5)*3; sq = 1 + 0.03*math.sin(t*10)
    else: sq = 1 + 0.012*math.sin(t*3 + ph)
    if speaking(name, t): sq *= 1 + 0.025*math.sin(t*18); hop += abs(math.sin(t*9))*0.012*h
    return x, y, h, hop, rot, sq, dirn

def sprite_for(name, t):
    if name == "mouse":
        cheer = t >= 27.4; sad = 1.7 < t < 4.5
        n = "triste" if sad else ("braccia_su" if cheer else "neutro")
        if speaking("mouse", t) and not sad and not cheer and math.sin(t*15) > -0.1: n = "parla"
        if speaking("mouse", t) and cheer and math.sin(t*15) > 0.3: n = "braccia_su"
        return load(f"assets/topo/{n}.png")
    return load(f"assets/s/{name}.png")

def hold_pos(name, x, y, h, hop, dirn):
    sp = sprite_for(name, 0); w = sp.width * h / sp.height
    return x + (0.26*w if dirn >= 0 else -0.26*w), y - hop - 0.28*h

def draw_flower(d, x, y, s, col):
    d.line([(x, y), (x, y+40*s)], fill=(60, 150, 60), width=max(1, int(6*s)))
    for i in range(5):
        a = i*2*math.pi/5; d.ellipse([x+math.cos(a)*14*s-11*s, y+math.sin(a)*14*s-11*s, x+math.cos(a)*14*s+11*s, y+math.sin(a)*14*s+11*s], fill=col)
    d.ellipse([x-8*s, y-8*s, x+8*s, y+8*s], fill=(255, 200, 40))

def text(d, s, x, y, size, fill, out, ow):
    f = ImageFont.truetype(FONT, size); d.text((x, y), s, font=f, fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)

def frame(i):
    t = i / FPS
    img = load("assets/s/sfondo.png").convert("RGB").copy()
    d = ImageDraw.Draw(img, "RGBA")
    # cestini (con piccolo rimbalzo all'arrivo dell'oggetto)
    for b, bx in BIN_X.items():
        v = 0
        for it in ITEMS:
            tl = it[5]+FLY
            if it[6] == b and tl <= t < tl+0.45: v = max(v, math.sin((t-tl)/0.45*math.pi)*(1-(t-tl)/0.45))
        shadow(img, bx, BIN_Y, 250)
        put(img, load(f"assets/s/bin_{b}.png"), bx, BIN_Y+4, BIN_H, sq=1 - 0.07*v)
    # rifiuti a terra
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if t < tp: put(img, load(f"assets/s/item_{kind}.png"), ix, iy, ITEM_H[kind]*persp(iy)/0.86*0.9, ang=((ix*7) % 50)-25)
    # personaggi ordinati per y
    chars = []
    for n in ("mouse", "chip", "spike"):
        if n == "chip" and t < 6.5: continue
        if n == "spike" and t < 7.5: continue
        chars.append((cstate(n, t), n))
    for (x, y, h, hop, rot, sq, dirn), n in sorted(chars, key=lambda c: c[0][1]):
        shadow(img, x, y, h*0.55)
        put(img, sprite_for(n, t), x, y - hop, h, ang=rot, sq=sq, flip=(dirn < 0))
        for kind, ix, iy, who, tp, tl, b in ITEMS:
            if who == n and tp <= t < tl:
                hx, hy = hold_pos(n, x, y, h, hop, dirn)
                put(img, load(f"assets/s/item_{kind}.png"), hx, hy+ITEM_H[kind]*0.5, ITEM_H[kind]*1.15, ang=math.sin(t*9)*8)
    # oggetti in volo + stelline
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if tl <= t < tl+FLY:
            x, y, h, hop, rot, sq, dirn = cstate(who, tl)
            hx, hy = hold_pos(who, x, y, h, 0, dirn)
            u = (t-tl)/FLY; bx, by = BIN_X[b], BIN_Y - BIN_H
            px, py = lerp(hx, bx, u), lerp(hy, by, u) - 260*math.sin(u*math.pi)
            put(img, load(f"assets/s/item_{kind}.png"), px, py+ITEM_H[kind]*0.5, ITEM_H[kind]*1.15*(1-0.3*u), ang=u*540)
        if tl+FLY <= t < tl+FLY+0.5:
            u = (t-tl-FLY)/0.5; bx = BIN_X[b]
            for k in range(6):
                a = k*math.pi/3+0.4; r_ = 10*(1-u)+2; cx = bx+math.cos(a)*(30+100*u); cy = BIN_Y-BIN_H-20+math.sin(a)*(30+100*u)-40*u
                d.ellipse([cx-r_, cy-r_, cx+r_, cy+r_], fill=(255, 235, 90, int(255*(1-u))))
    # finale: fiori, farfalle, coriandoli
    if t > 26.4:
        g = ease((t-26.4)/2.0)
        for fx, fy, col in ((120, 1660, (255, 110, 150)), (330, 1820, (255, 220, 70)), (610, 1760, (255, 255, 255)),
                            (830, 1660, (190, 140, 255)), (1000, 1800, (255, 110, 150)), (60, 1860, (255, 220, 70))):
            draw_flower(d, fx, fy-20, 1.3*g, col)
        for k in range(4):
            bx = 200+k*220+math.sin(t*1.7+k)*70; by = 900+k*60+math.cos(t*2.3+k)*50; wv = abs(math.sin(t*14+k))
            col = ((255, 140, 200), (255, 190, 70), (140, 200, 255), (200, 160, 255))[k]
            d.ellipse([bx-18*wv-8, by-26, bx+2, by+26], fill=col); d.ellipse([bx-2, by-26, bx+18*wv+8, by+26], fill=col)
        if t > 27.2:
            for k in range(10):
                cx = (k*113+40) % W + math.sin(t*3+k)*30; cy = ((t-27.2)*260+k*170) % 1500+200
                d.ellipse([cx-9, cy-9, cx+9, cy+9], fill=((255, 120, 150), (255, 220, 70), (120, 200, 255), (160, 230, 120))[k % 4])
    # sottotitoli
    for k, t0, who, txt, dur in VOICES:
        if t0-0.05 <= t <= t0+dur+0.35:
            f = ImageFont.truetype(FONT, 72); bb = d.textbbox((0, 0), txt, font=f, anchor="mm", stroke_width=6)
            lines = [txt]
            if bb[2]-bb[0] > 960:
                ws = txt.split(); hf = len(ws)//2; lines = [" ".join(ws[:hf]), " ".join(ws[hf:])]
            yy = 360 if len(lines) == 1 else 320
            for ln in lines: text(d, ln, W/2, yy, 72, (255, 255, 255), (60, 40, 20), 7); yy += 90
            break
    if t < 3: text(d, "PULIAMO IL PARCO!", W/2, 140, 70, (255, 255, 255, int(255*min(1, (3-t)/0.6))), (230, 90, 60), 10)
    if t > 33.2:
        u = ease((t-33.2)/0.6)
        img = Image.blend(img, Image.new("RGB", (W, H), (255, 245, 210)), 0.92*u); d = ImageDraw.Draw(img, "RGBA")
        by = 520+(1-u)*60
        text(d, "Ricicla anche tu!", W/2, by, 86, (60, 160, 70), (255, 255, 255), 8)
        for j, col in enumerate(((245, 200, 40), (60, 120, 220), (140, 90, 55))):
            d.ellipse([240+j*300-70, by+150-70, 240+j*300+70, by+150+70], fill=col, outline=(255, 255, 255), width=6)
        text(d, "Plastica  ·  Carta  ·  Umido", W/2, by+300, 52, (90, 70, 50), None, 0)
        text(d, "Bambini Ciao Ciao", W/2, by+450, 92, (230, 90, 60), (255, 255, 255), 8)
        text(d, "Un nuovo video ogni settimana!", W/2, by+550, 46, (110, 90, 70), None, 0)
        put(img, load("assets/topo/braccia_su.png"), W/2, 1820-abs(math.sin(t*5))*30, 520)
    return img.tobytes()

if __name__ == "__main__":
    if sys.argv[1] == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts)*FPS))).save(f"test3_{ts}.png")
    else:
        N = int(DUR*FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "medium", "video_muto3.mp4"], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
