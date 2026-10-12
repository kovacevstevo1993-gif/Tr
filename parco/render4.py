#!/usr/bin/env python3
"""Puliamo il parco! v5 - regia con camera, animazione con anticipazione/rimbalzo, lip-sync dalla voce, luce integrata."""
import math, sys, subprocess, os, json, wave
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from render import lerp, ease

W, H, FPS, DUR = 1080, 1920, 24, 52.4
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FLY = 0.55
_D = json.load(open(os.path.join(HERE, "audio3/durate.json")))

# ---------------------------------------------------------------- copione (chiave, inizio, chi, testo)
_V = [("N1", 0.4, "narr", "In un bellissimo parco, il piccolo topolino scopre una brutta sorpresa."),
      ("M1", 5.85, "mouse", "Oh no! Quanti rifiuti!"),
      ("N2", 8.7, "narr", "Ma il topolino non si arrende! Chiama i suoi amici."),
      ("M2", 13.5, "mouse", "Chip! Spike! Venite ad aiutarmi!"),
      ("C1", 18.1, "chip", "Arrivo!"),
      ("S1", 18.95, "spike", "Eccomi!"),
      ("M3", 19.9, "mouse", "Puliamo il parco insieme!"),
      ("N3", 21.8, "narr", "Prima, la bottiglia."),
      ("M4", 23.9, "mouse", "La plastica va nel giallo!"),
      ("N4", 26.0, "narr", "Poi, la carta."),
      ("C2", 27.85, "chip", "La carta va nel blu!"),
      ("N5", 29.5, "narr", "E adesso, la buccia di banana."),
      ("S2", 32.3, "spike", "L'umido va nel marrone!"),
      ("N6", 34.3, "narr", "Ancora un pochino..."),
      ("M5", 36.0, "mouse", "Forza, amici!"),
      ("N7", 40.2, "narr", "Ed ecco il parco... pulito e bellissimo!"),
      ("C3", 43.5, "chip", "Evviva!"),
      ("S3", 44.4, "spike", "Evviva!"),
      ("M6", 45.5, "mouse", "Grazie, amici! Bambini Ciao Ciao! Iscrivetevi al canale!")]
VOICES = [(k, t, w, x, _D[k]) for k, t, w, x in _V]

# ---------------------------------------------------------------- layout
BIN_X = {"giallo": 270, "blu": 540, "marrone": 810}
BIN_Y = 1340; BIN_H = 400
ITEM_H = {"bottle": 62, "paper": 100, "news": 70, "peel": 62, "can": 105, "core": 98}
CH_H = {"mouse": 540, "chip": 500, "spike": 470}
KF = {
 "mouse": [(0, -170, 1620), (2.4, 330, 1620), (21.8, 330, 1620), (22.9, 270, 1706), (23.4, 270, 1706),
           (25.3, 300, 1500), (34.6, 300, 1500), (35.15, 770, 1712), (35.4, 770, 1712),
           (36.8, 330, 1500), (37.5, 330, 1500), (39.8, 540, 1650), (60, 540, 1650)],
 "chip":  [(15.3, 1250, 1700), (17.8, 620, 1700), (26.2, 620, 1700), (26.85, 525, 1806), (27.15, 525, 1806),
           (28.95, 560, 1500), (33.2, 560, 1500), (35.55, 955, 1806), (35.85, 955, 1806),
           (38.1, 590, 1500), (38.8, 590, 1500), (40.4, 300, 1660), (60, 300, 1660)],
 "spike": [(16.0, 1250, 1740), (18.4, 880, 1740), (29.8, 880, 1740), (31.25, 405, 1664), (31.55, 405, 1664),
           (33.75, 800, 1500), (34.5, 800, 1500), (35.95, 685, 1674), (36.25, 685, 1674),
           (39.3, 830, 1500), (39.9, 830, 1500), (40.9, 780, 1660), (60, 780, 1660)],
}
# (tipo, x, y, chi, t_raccolta, t_lancio, cestino)
ITEMS = [("bottle", 270, 1712, "mouse", 23.4, 25.6, "giallo"),
         ("news",   525, 1810, "chip",  27.15, 29.2, "blu"),
         ("peel",   405, 1668, "spike", 31.55, 34.0, "marrone"),
         ("can",    775, 1718, "mouse", 35.4, 37.0, "giallo"),
         ("paper",  955, 1810, "chip",  35.85, 38.4, "blu"),
         ("core",   685, 1678, "spike", 36.25, 39.6, "marrone")]
CHEER_T = 39.8
SPK_COL = {"narr": (255, 233, 190), "mouse": (255, 255, 255), "chip": (255, 214, 180), "spike": (200, 225, 255)}

# camera: (t, cx, cy, zoom)
CAM = [(0, 540, 1150, 1.0), (3.5, 450, 1380, 1.12), (5.0, 450, 1380, 1.12), (6.0, 330, 1390, 1.65), (8.6, 330, 1390, 1.7),
       (9.8, 400, 1450, 1.2), (13.5, 400, 1450, 1.2), (15.0, 540, 1330, 1.0), (19.0, 540, 1330, 1.0),
       (20.0, 330, 1520, 1.3), (22.0, 330, 1560, 1.3), (23.4, 290, 1560, 1.4), (25.0, 300, 1450, 1.35), (26.2, 300, 1450, 1.35),
       (27.1, 560, 1620, 1.3), (29.3, 560, 1450, 1.3), (30.5, 540, 1450, 1.15), (31.4, 440, 1600, 1.3), (34.0, 800, 1450, 1.3),
       (35.0, 540, 1450, 1.1), (40.0, 540, 1450, 1.1), (41.0, 540, 1400, 1.0), (44.0, 540, 1400, 1.0),
       (46.0, 540, 1500, 1.2), (60, 540, 1500, 1.28)]

def camera(t):
    for (t0, a, b, z), (t1, a1, b1, z1) in zip(CAM, CAM[1:]):
        if t0 <= t <= t1:
            u = ease((t-t0)/(t1-t0)) if (t1 > t0) else 1
            cx, cy, z_ = lerp(a, a1, u), lerp(b, b1, u), lerp(z, z1, u)
            break
    else: cx, cy, z_ = CAM[-1][1:]
    hx, hy = 540/z_, 960/z_
    return min(max(cx, hx), W-hx), min(max(cy, hy), H-hy), z_

# ---------------------------------------------------------------- lip-sync dalle voci
ENV = {}
def env_of(key):
    if key not in ENV:
        with wave.open(os.path.join(HERE, f"audio3/{key}.wav")) as w:
            a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)/32768
        n = int(len(a)/44100*FPS*2)+1; win = 44100//(FPS*2)
        e = np.array([np.sqrt(np.mean(a[i*win:(i+1)*win]**2)+1e-12) for i in range(n)])
        e = np.convolve(e, np.ones(3)/3, mode="same"); ENV[key] = e/(np.percentile(e, 95)+1e-9)
    return ENV[key]

def mouth_level(who, t):
    for k, t0, w, tx, d in VOICES:
        if w == who and t0 <= t <= t0+d:
            e = env_of(k); i = min(len(e)-1, int((t-t0)*FPS*2)); v = e[i]
            return 0 if v < 0.16 else (1 if v < 0.55 else 2)
    return -1       # non parla

# ---------------------------------------------------------------- sprite & luce
_cache = {}
def load(path, tint=True):
    if path not in _cache:
        im = Image.open(os.path.join(HERE, path)).convert("RGBA")
        if tint and "assets/s/sfondo" not in path and ("assets/v/" in path or "item_" in path or "bin_" in path):
            a = np.asarray(im).astype(np.float32); h = a.shape[0]
            a[..., 0] *= 1.035; a[..., 2] *= 0.93                           # luce calda del sole
            g = np.linspace(0, 1, h)[:, None]**2.2 * 0.10                  # rimbalzo verde dal prato (in basso)
            a[..., 1] += g*14; a[..., 0] -= g*6
            im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
        _cache[path] = im
    return _cache[path]

def put(img, sp, x, y, h, ang=0, sq=1.0, flip=False):
    if flip: sp = sp.transpose(Image.FLIP_LEFT_RIGHT)
    nh = max(1, int(h*sq)); nw = max(1, int(sp.width*h/sp.height/sq))
    s2 = sp.resize((nw, nh), Image.LANCZOS if nh < sp.height else Image.BICUBIC)
    if ang:
        pad = int(nw*0.3); cv = Image.new("RGBA", (nw+2*pad, nh+pad), (0, 0, 0, 0)); cv.paste(s2, (pad, 0), s2)
        cv = cv.rotate(ang, resample=Image.BICUBIC, center=(pad+nw//2, nh))
        img.paste(cv, (int(x-pad-nw/2), int(y-nh)), cv)
    else: img.paste(s2, (int(x-nw/2), int(y-nh)), s2)

SHD = None
def shadow(img, x, y, w, k=1.0):
    global SHD
    if SHD is None:
        sh = Image.new("RGBA", (300, 90), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([25, 25, 275, 65], fill=(10, 40, 10, 120))
        SHD = sh.filter(ImageFilter.GaussianBlur(9))
    s2 = SHD.resize((max(2, int(w*1.35)), max(2, int(w*1.35*90/300))), Image.BICUBIC)
    if k < 1: s2.putalpha(s2.getchannel("A").point(lambda v: int(v*k)))
    img.paste(s2, (int(x-s2.width/2), int(y-s2.height/2)), s2)

VIG = None
def vignette():
    global VIG
    if VIG is None:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt(((xx-W*0.5)/(W*0.62))**2 + ((yy-H*0.5)/(H*0.60))**2)
        v = 1 - 0.30*np.clip(d-0.55, 0, 1)**1.5
        glow = 1 + 0.07*np.clip(1-np.sqrt(((xx-W*0.15)/(W*0.9))**2 + ((yy-H*0.05)/(H*0.55))**2), 0, 1)   # luce dall'alto a sinistra
        m = np.clip(np.minimum(v*glow, 1.0)*255, 0, 255).astype(np.uint8)
        VIG = Image.fromarray(m, "L").convert("RGB")
    return VIG

# ---------------------------------------------------------------- animazione
def seg_info(kf, t):
    """posizione, movimento, direzione, distanza cumulata, velocità, (t_inizio, t_fine) del segmento corrente."""
    cum = 0.0
    if t <= kf[0][0]: return kf[0][1], kf[0][2], False, 1, 0.0, 0.0, None
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        L = math.hypot(x1-x0, y1-y0)
        if t0 <= t <= t1:
            mv = L > 0; u = ease((t-t0)/(t1-t0)) if mv else 0
            x, y = lerp(x0, x1, u), lerp(y0, y1, u)
            vx = (lerp(x0, x1, ease(min(1, (t+0.02-t0)/(t1-t0)))) - lerp(x0, x1, ease(max(0, (t-0.02-t0)/(t1-t0)))))/0.04 if mv else 0
            return x, y, mv, (1 if x1 >= x0 else -1), cum + L*u, vx, (t0, t1)
        cum += L
    return kf[-1][1], kf[-1][2], False, 1, cum, 0.0, None

def walk_events(name):
    """istanti in cui i piedi toccano terra (per i passi)."""
    ev = []; prev = None; stride = 130.0
    for i in range(int(DUR*240)):
        t = i/240; x, y, mv, d_, cum, vx, seg = seg_info(KF[name], t)
        ph = math.floor(cum/stride) if mv else prev
        if prev is not None and mv and ph != prev: ev.append(t)
        prev = ph if mv else prev
    return ev

def persp(y): return 0.86 + (y-1450)/1000*0.45

def kick(t, lo, hi):  # 0..1..0 nella finestra
    return math.sin(math.pi*min(1, max(0, (t-lo)/(hi-lo)))) if lo <= t <= hi else 0.0

def cstate(name, t):
    kf = KF[name]; x, y, mv, dirn, cum, vx, seg = seg_info(kf, t)
    h = CH_H[name]*persp(y); hop = 0.0; rot = 0.0; sq = 1.0
    off = {"mouse": 0.0, "chip": 0.3, "spike": 0.55}[name]
    if mv:
        s = abs(math.sin(cum/130.0*math.pi))
        hop = (s**0.8)*0.045*h; sq = 1 - 0.055*(1 - min(1, s*3)) + 0.02*s
        rot = -max(-5.5, min(5.5, vx*0.005)) + math.sin(cum/130.0*math.pi)*2.4
    # anticipazione prima di partire / assestamento dopo l'arresto
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        if (x0, y0) != (x1, y1):
            if t0-0.18 <= t < t0: u = (t-(t0-0.18))/0.18; sq *= 1 - 0.07*math.sin(u*math.pi/2); rot += (1 if x1 > x0 else -1)*3*u
            if t1 <= t < t1+0.6: tau = t-t1; sq *= 1 + 0.05*math.exp(-7*tau)*math.sin(24*tau)
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if who != name: continue
        c = kick(t, tp-0.25, tp+0.25)                    # si china a raccogliere
        sq *= 1 - 0.13*c; rot += -6*c*(1 if dirn >= 0 else -1)
        if tl-0.4 <= t < tl:                             # carica il lancio
            u = (t-(tl-0.4))/0.4; sq *= 1 + 0.06*ease(u); rot += 5*ease(u)
        elif tl <= t < tl+0.3:                           # rilascio
            u = (t-tl)/0.3; sq *= 1 + 0.06*(1-u) - 0.07*math.sin(u*math.pi); rot += -7*math.sin(u*math.pi)
    if t >= CHEER_T:                                     # esultanza: salti con squash & stretch
        p = ((t-CHEER_T)/0.9 + off) % 1; air = 4*p*(1-p)
        hop += air*0.20*h; sq *= 1 + 0.06*air - 0.08*(max(0, 1-p*6)+max(0, 1-(1-p)*6)); rot += math.sin(2*math.pi*p)*4
    ml = mouth_level(name, t)
    if ml >= 0: sq *= 1 + 0.012*(ml == 2); rot += 1.3*math.sin(t*8+off)
    else: sq *= 1 + 0.010*math.sin(t*3+off*5)
    return x, y, h, hop, rot, sq, dirn, mv

def blinking(name, t):
    off = {"mouse": 0.1, "chip": 0.55, "spike": 0.8}[name]
    return ((t*0.37+off) % 1.0) < 0.05

def sprite_name(name, t):
    b = 1 if blinking(name, t) else 0
    ml = mouth_level(name, t)
    if name == "mouse":
        if t >= CHEER_T and (t < 45.4 or t >= 49.0): return "assets/v/mouse_braccia_su.png"
        if t >= CHEER_T: pass
        if 5.0 < t < 9.4: return "assets/v/mouse_triste.png"
        if 14.0 < t < 17.0: return "assets/v/mouse_braccia_su.png"
        return f"assets/v/mouse_{'parla' if ml >= 1 else 'neutro'}_b{b}.png"
    return f"assets/v/{name}_m{max(0, ml)}b{b}.png"

def hold_off(name, t, h, dirn):
    sp = load(sprite_name(name, t)); w = sp.width*h/sp.height
    return (0.26*w if dirn >= 0 else -0.26*w), -0.28*h

def draw_flower(d, x, y, s, col):
    d.line([(x, y), (x, y+40*s)], fill=(60, 150, 60), width=max(1, int(6*s)))
    for i in range(5):
        a = i*2*math.pi/5; cx, cy = x+math.cos(a)*14*s, y+math.sin(a)*14*s
        d.ellipse([cx-11*s, cy-11*s, cx+11*s, cy+11*s], fill=col)
    d.ellipse([x-8*s, y-8*s, x+8*s, y+8*s], fill=(255, 200, 40))

def subscribe_button(img, t, t0, cy=1480):
    """Pulsante 'Iscriviti' dentro la scena (non una slide): compare con rimbalzo, la campanella dondola."""
    if t < t0: return
    u = (1 + 2.7*((min(1, max(0, (t-t0)/0.45))-1)**3 + 0*1) + 1.7*(min(1, max(0, (t-t0)/0.45))-1)**2); s = max(0.05, u)*(1+0.03*math.sin((t-t0)*6))
    w, h = 520, 130; Sx = 2; cv = Image.new("RGBA", (w*Sx, h*Sx+20), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
    d.rounded_rectangle([6*Sx, 10*Sx, (w-6)*Sx, (h-6)*Sx], radius=34*Sx, fill=(0, 0, 0, 70))
    d.rounded_rectangle([0, 0, (w-12)*Sx, (h-16)*Sx], radius=34*Sx, fill=(232, 36, 36, 255), outline=(255, 255, 255, 255), width=4*Sx)
    f = ImageFont.truetype(FONT, 54*Sx); d.text((((w-12)/2+34)*Sx, (h-16)/2*Sx), "ISCRIVITI", font=f, fill=(255, 255, 255, 255), anchor="mm")
    bell = Image.new("RGBA", (90*Sx, 90*Sx), (0, 0, 0, 0)); bd = ImageDraw.Draw(bell)
    bd.pieslice([20*Sx, 12*Sx, 70*Sx, 62*Sx], 180, 360, fill=(255, 255, 255, 255)); bd.polygon([(20*Sx, 38*Sx), (70*Sx, 38*Sx), (78*Sx, 62*Sx), (12*Sx, 62*Sx)], fill=(255, 255, 255, 255))
    bd.ellipse([36*Sx, 62*Sx, 54*Sx, 78*Sx], fill=(255, 255, 255, 255)); bd.ellipse([40*Sx, 4*Sx, 50*Sx, 14*Sx], fill=(255, 255, 255, 255))
    bell = bell.rotate(math.sin((t-t0)*14)*16*max(0, 1-(t-t0)/1.8), resample=Image.BICUBIC, center=(45*Sx, 14*Sx))
    cv.paste(bell, (24*Sx, int(((h-16)/2-45)*Sx)), bell)
    cv = cv.resize((int(w*s), int((h+10)*s)), Image.LANCZOS); img.paste(cv, (int(W/2-cv.width/2), int(cy-cv.height/2)), cv)


def text(d, s, x, y, size, fill, out, ow):
    f = ImageFont.truetype(FONT, size); d.text((x, y), s, font=f, fill=fill, anchor="mm", stroke_width=ow, stroke_fill=out)

_bgsrc = None
def frame(i):
    global _bgsrc
    t = i/FPS; cx, cy, Z = camera(t)
    if _bgsrc is None: _bgsrc = Image.open(os.path.join(HERE, "assets/s/sfondo_src.png")).convert("RGB")
    sx_, sy_ = _bgsrc.width/W, _bgsrc.height/H
    box = ((cx-540/Z)*sx_, (cy-960/Z)*sy_, (cx+540/Z)*sx_, (cy+960/Z)*sy_)
    img = _bgsrc.resize((W, H), Image.BICUBIC, box=box)
    img = img.filter(ImageFilter.GaussianBlur(1.0 + 1.6*max(0, Z-1)))                 # profondità di campo
    d = ImageDraw.Draw(img, "RGBA")
    X = lambda x: (x-cx)*Z + W/2
    Y = lambda y: (y-cy)*Z + H/2
    # cestini
    for b, bx in BIN_X.items():
        v = 0
        for it in ITEMS:
            tl = it[5]+FLY
            if it[6] == b and tl <= t < tl+0.45: v = max(v, math.sin((t-tl)/0.45*math.pi)*(1-(t-tl)/0.45))
        shadow(img, X(bx+25), Y(BIN_Y), 250*Z)
        put(img, load(f"assets/s/bin_{b}.png"), X(bx), Y(BIN_Y+4), BIN_H*Z, sq=1-0.07*v)
    # rifiuti a terra
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if t < tp:
            hh = ITEM_H[kind]*persp(iy)/0.86*0.9
            shadow(img, X(ix+8), Y(iy), hh*Z*1.2, 0.8)
            put(img, load(f"assets/s/item_{kind}.png"), X(ix), Y(iy), hh*Z, ang=((ix*7) % 50)-25)
    # personaggi
    chars = []
    for n, tin in (("mouse", 0), ("chip", 15.2), ("spike", 15.9)):
        if t >= tin: chars.append((cstate(n, t), n))
    for (x, y, h, hop, rot, sq, dirn, mv), n in sorted(chars, key=lambda c: c[0][1]):
        shadow(img, X(x+0.12*h), Y(y), h*0.62*Z, max(0.45, 1-1.6*hop/h))
        put(img, load(sprite_name(n, t)), X(x), Y(y-hop), h*Z, ang=rot, sq=sq, flip=(dirn < 0 and mv))
        for kind, ix, iy, who, tp, tl, b in ITEMS:
            if who == n and tp <= t < tl:
                ox, oy = hold_off(n, t, h, dirn)
                put(img, load(f"assets/s/item_{kind}.png"), X(x+ox), Y(y-hop+oy)+ITEM_H[kind]*0.5*Z, ITEM_H[kind]*1.15*Z, ang=math.sin(t*9)*8)
    # oggetti in volo + stelline all'impatto
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if tl <= t < tl+FLY:
            x, y, h, hop, rot, sq, dirn, mv = cstate(who, tl); ox, oy = hold_off(who, tl, h, dirn)
            hx, hy = x+ox, y+oy; u = (t-tl)/FLY; bx, by = BIN_X[b], BIN_Y-BIN_H
            px, py = lerp(hx, bx, u), lerp(hy, by, u)-260*math.sin(u*math.pi)
            put(img, load(f"assets/s/item_{kind}.png"), X(px), Y(py)+ITEM_H[kind]*0.5*Z, ITEM_H[kind]*1.15*Z*(1-0.3*u), ang=u*540)
        if tl+FLY <= t < tl+FLY+0.5:
            u = (t-tl-FLY)/0.5; bx = BIN_X[b]
            for k in range(7):
                a = k*2*math.pi/7+0.4; r_ = (10*(1-u)+2)*Z; px, py = X(bx+math.cos(a)*(30+110*u)), Y(BIN_Y-BIN_H-20+math.sin(a)*(30+110*u)-40*u)
                d.ellipse([px-r_, py-r_, px+r_, py+r_], fill=(255, 235, 90, int(255*(1-u))))
    # finale: fiori, farfalle, coriandoli
    if t > 38.8:
        g = ease((t-38.8)/2.2)
        for fx, fy, col in ((120, 1660, (255, 110, 150)), (330, 1830, (255, 220, 70)), (610, 1770, (255, 255, 255)),
                            (830, 1670, (190, 140, 255)), (1000, 1810, (255, 110, 150)), (60, 1870, (255, 220, 70)), (470, 1745, (190, 140, 255))):
            draw_flower(d, X(fx), Y(fy-20), 1.3*g*Z, col)
        for k in range(5):
            bx = 150+k*200+math.sin(t*1.7+k)*70; by = 1000+k*55+math.cos(t*2.3+k)*50; wv = abs(math.sin(t*14+k))
            col = ((255, 140, 200), (255, 190, 70), (140, 200, 255), (200, 160, 255), (255, 150, 120))[k]
            wx, wy = X(bx), Y(by)
            d.ellipse([wx-(18*wv+8)*Z, wy-26*Z, wx+2, wy+26*Z], fill=col); d.ellipse([wx-2, wy-26*Z, wx+(18*wv+8)*Z, wy+26*Z], fill=col)
        if t > CHEER_T:
            for k in range(12):
                px = ((k*113+40) % W) + math.sin(t*3+k)*30; py = ((t-CHEER_T)*240+k*160) % 1700+120
                d.ellipse([px-9, py-9, px+9, py+9], fill=((255, 120, 150), (255, 220, 70), (120, 200, 255), (160, 230, 120))[k % 4])
    # grading: vignetta e luce, leggera saturazione
    img = ImageChops.multiply(img, vignette())
    img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 250, 238))), 0.6)
    d = ImageDraw.Draw(img, "RGBA")
    # sottotitoli (con piccola entrata)
    for k, t0, who, txt, dur in VOICES:
        if t0-0.05 <= t <= t0+dur+0.3:
            u = ease((t-t0+0.05)/0.18); f = ImageFont.truetype(FONT, 66)
            lines = []; cur = ""
            for wd in txt.split():
                tryl = (cur+" "+wd).strip()
                if d.textbbox((0, 0), tryl, font=f, anchor="mm", stroke_width=6)[2] - d.textbbox((0, 0), tryl, font=f, anchor="mm", stroke_width=6)[0] > 930 and cur:
                    lines.append(cur); cur = wd
                else: cur = tryl
            lines.append(cur)
            yy = 330 + (1-u)*14 - 41*(len(lines)-1) + (70 if t < 3.4 else 0)
            for ln in lines: text(d, ln, W/2, yy, 66, SPK_COL[who]+(int(255*u),), (60, 40, 20, int(255*u)), 7); yy += 82
            break
    if t < 3.2: text(d, "PULIAMO IL PARCO!", W/2, 95, 70, (255, 255, 255, int(255*min(1, (3.2-t)/0.6))), (230, 90, 60), 10)
    subscribe_button(img, t, 48.9, cy=1450)
    return img.tobytes()

if __name__ == "__main__":
    if sys.argv[1] == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts)*FPS))).save(f"test4_{ts}.png")
    else:
        a, b = int(sys.argv[2]), int(sys.argv[3]); out = sys.argv[4]
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(a, b), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{a+n}/{b}", flush=True)
        ff.stdin.close(); ff.wait()
