#!/usr/bin/env python3
"""Motore di regia 2.5D: camera a inquadrature con tagli netti, lip-sync dalla voce, anticipazione/rimbalzo,
luce integrata, effetti magici (scintille, arcobaleno, farfalle, fiori). La scena è un modulo (SCENE=sceneA)."""
import math, sys, subprocess, os, json, wave, importlib
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

S = importlib.import_module(os.environ.get("SCENE", "sceneA"))
W, H, FPS = 1080, 1920, 24
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FLY = 0.55
def lerp(a, b, u): return a + (b-a)*u
def ease(u): u = max(0, min(1, u)); return u*u*(3-2*u)
def back(u, k=1.7): u = max(0, min(1, u)); return 1 + (k+1)*(u-1)**3 + k*(u-1)**2

# ---------------------------------------------------------------- layout comune
BIN_X = {"giallo": 270, "blu": 540, "marrone": 810}
BIN_Y = 1340; BIN_H = 400
ITEM_H = {"bottle": 62, "paper": 100, "news": 70, "peel": 62, "can": 105, "core": 98}
CH_H = {"mouse": 540, "chip": 500, "spike": 470}

def persp(y):
    return S.persp(y) if hasattr(S, "persp") else 0.86 + (y-1450)/1000*0.45

# ---------------------------------------------------------------- camera
def camera(t):
    for (t0, t1, a, b) in S.SHOTS:
        if t0 <= t < t1:
            u = (t-t0)/(t1-t0); cx, cy, z = [lerp(a[i], b[i], u) for i in range(3)]; break
    else: cx, cy, z = S.SHOTS[-1][3]
    for (ts, amp, dur) in getattr(S, "SHAKE", []):
        if ts <= t < ts+dur:
            k = (1-(t-ts)/dur)*amp; cx += math.sin(t*90)*k; cy += math.cos(t*77)*k
    hx, hy = 540/z, 960/z
    return min(max(cx, hx), W-hx), min(max(cy, hy), H-hy), z

def shot_index(t):
    for i, (t0, t1, a, b) in enumerate(S.SHOTS):
        if t0 <= t < t1: return i
    return len(S.SHOTS)-1

# ---------------------------------------------------------------- lip-sync
ENV = {}
def env_of(key):
    if key not in ENV:
        with wave.open(os.path.join(HERE, S.AUDIO, f"{key}.wav")) as w:
            a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)/32768
        n = int(len(a)/44100*FPS*2)+1; win = 44100//(FPS*2)
        e = np.array([np.sqrt(np.mean(a[i*win:(i+1)*win]**2)+1e-12) for i in range(n)])
        e = np.convolve(e, np.ones(3)/3, mode="same"); ENV[key] = e/(np.percentile(e, 95)+1e-9)
    return ENV[key]

def mouth_level(who, t):
    for k, t0, w, tx, d in S.VOICES:
        if w == who and t0 <= t <= t0+d:
            e = env_of(k); i = min(len(e)-1, int((t-t0)*FPS*2)); v = e[i]
            return 0 if v < 0.16 else (1 if v < 0.55 else 2)
    for (n, a, b, lv) in getattr(S, "FORCE_MOUTH", []):
        if n == who and a <= t <= b: return lv
    return -1

# ---------------------------------------------------------------- sprite & luce
_cache = {}
def load(path):
    if path not in _cache:
        im = Image.open(os.path.join(HERE, path)).convert("RGBA")
        if "assets/v/" in path or "item_" in path or "bin_" in path:
            a = np.asarray(im).astype(np.float32); h = a.shape[0]
            a[..., 0] *= 1.035; a[..., 2] *= 0.93
            g = np.linspace(0, 1, h)[:, None]**2.2*0.10; a[..., 1] += g*14; a[..., 0] -= g*6
            im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
        _cache[path] = im
    return _cache[path]

def put(img, sp, x, y, h, ang=0, sq=1.0, flip=False):
    if flip: sp = sp.transpose(Image.FLIP_LEFT_RIGHT)
    nh = max(1, int(h*sq)); nw = max(1, int(sp.width*h/sp.height/sq))
    if nh > 4000 or nw > 4000: return
    s2 = sp.resize((nw, nh), Image.LANCZOS if nh < sp.height else Image.BICUBIC)
    if ang:
        pad = int(nw*0.3); cv = Image.new("RGBA", (nw+2*pad, nh+pad), (0, 0, 0, 0)); cv.paste(s2, (pad, 0), s2)
        cv = cv.rotate(ang, resample=Image.BICUBIC, center=(pad+nw//2, nh)); img.paste(cv, (int(x-pad-nw/2), int(y-nh)), cv)
    else: img.paste(s2, (int(x-nw/2), int(y-nh)), s2)

SHD = None
def shadow(img, x, y, w, k=1.0):
    global SHD
    if SHD is None:
        sh = Image.new("RGBA", (300, 90), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([25, 25, 275, 65], fill=(10, 40, 10, 120)); SHD = sh.filter(ImageFilter.GaussianBlur(9))
    s2 = SHD.resize((max(2, int(w*1.35)), max(2, int(w*1.35*90/300))), Image.BICUBIC)
    if k < 1: s2.putalpha(s2.getchannel("A").point(lambda v: int(v*k)))
    img.paste(s2, (int(x-s2.width/2), int(y-s2.height/2)), s2)

VIG = None
def vignette():
    global VIG
    if VIG is None:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt(((xx-W*0.5)/(W*0.62))**2 + ((yy-H*0.5)/(H*0.60))**2); v = 1 - 0.30*np.clip(d-0.55, 0, 1)**1.5
        VIG = Image.fromarray(np.clip(v*255, 0, 255).astype(np.uint8), "L").convert("RGB")
    return VIG

# ---------------------------------------------------------------- animazione personaggi
def seg_info(kf, t):
    cum = 0.0
    if t <= kf[0][0]: return kf[0][1], kf[0][2], False, 1, 0.0, 0.0
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        L = math.hypot(x1-x0, y1-y0)
        if t0 <= t <= t1:
            mv = L > 0; u = ease((t-t0)/(t1-t0)) if mv else 0
            vx = (lerp(x0, x1, ease(min(1, (t+0.02-t0)/(t1-t0)))) - lerp(x0, x1, ease(max(0, (t-0.02-t0)/(t1-t0)))))/0.04 if mv else 0
            return lerp(x0, x1, u), lerp(y0, y1, u), mv, (1 if x1 >= x0 else -1), cum+L*u, vx
        cum += L
    return kf[-1][1], kf[-1][2], False, 1, cum, 0.0

def walk_events(name):
    ev = []; prev = None
    for i in range(int(S.DUR*240)):
        t = i/240; x, y, mv, d_, cum, vx = seg_info(S.KF[name], t)
        ph = math.floor(cum/130.0) if mv else prev
        if prev is not None and mv and ph != prev: ev.append(t)
        prev = ph if mv else prev
    return ev

def kick(t, lo, hi): return math.sin(math.pi*(t-lo)/(hi-lo)) if lo <= t <= hi else 0.0

def cstate(name, t):
    kf = S.KF[name]; x, y, mv, dirn, cum, vx = seg_info(kf, t)
    h = CH_H[name]*persp(y)*getattr(S, "SCALE", {}).get(name, 1.0); hop = 0.0; rot = 0.0; sq = 1.0
    off = {"mouse": 0.0, "chip": 0.3, "spike": 0.55}[name]
    if mv:
        s = abs(math.sin(cum/130.0*math.pi)); hop = (s**0.8)*0.045*h; sq = 1 - 0.055*(1-min(1, s*3)) + 0.02*s
        rot = -max(-5.5, min(5.5, vx*0.005)) + math.sin(cum/130.0*math.pi)*2.4
    for (t0, x0, y0), (t1, x1, y1) in zip(kf, kf[1:]):
        if (x0, y0) != (x1, y1):
            if t0-0.18 <= t < t0: u = (t-(t0-0.18))/0.18; sq *= 1 - 0.07*math.sin(u*math.pi/2); rot += (1 if x1 > x0 else -1)*3*u
            if t1 <= t < t1+0.6: tau = t-t1; sq *= 1 + 0.05*math.exp(-7*tau)*math.sin(24*tau)
    for kind, ix, iy, who, tp, tl, b in S.ITEMS:
        if who != name: continue
        c = kick(t, tp-0.25, tp+0.25); sq *= 1 - 0.13*c; rot += -6*c*(1 if dirn >= 0 else -1)
        if tl-0.4 <= t < tl: u = (t-(tl-0.4))/0.4; sq *= 1 + 0.06*ease(u); rot += 5*ease(u)
        elif tl <= t < tl+0.3: u = (t-tl)/0.3; sq *= 1 + 0.06*(1-u) - 0.07*math.sin(u*math.pi); rot += -7*math.sin(u*math.pi)
    for (n, a, b_) in getattr(S, "JUMP", []):                 # esultanza / salti
        if n in (name, "all") and a <= t < b_:
            p = ((t-a)/0.9 + off) % 1; air = 4*p*(1-p)
            hop += air*0.20*h; sq *= 1 + 0.06*air - 0.08*(max(0, 1-p*6)+max(0, 1-(1-p)*6)); rot += math.sin(2*math.pi*p)*4
    for (n, a, b_, amp) in getattr(S, "BOUNCE", []):          # ballo a tempo
        if n in (name, "all") and a <= t < b_:
            p = ((t-a)*2.25 + off) % 1; air = 4*p*(1-p); hop += air*amp*h; sq *= 1 + 0.035*air - 0.04*(1-air)**6; rot += math.sin(2*math.pi*p)*3
    ml = mouth_level(name, t)
    if ml >= 0: sq *= 1 + 0.012*(ml == 2); rot += 1.3*math.sin(t*8+off)
    else: sq *= 1 + 0.010*math.sin(t*3+off*5)
    return x, y, h, hop, rot, sq, dirn, mv

def blinking(name, t):
    off = {"mouse": 0.1, "chip": 0.55, "spike": 0.8}[name]; return ((t*0.37+off) % 1.0) < 0.05

def sprite_name(name, t):
    b = 1 if blinking(name, t) else 0; ml = mouth_level(name, t)
    if name == "mouse":
        o = S.mouse_sprite(t, ml, b) if hasattr(S, "mouse_sprite") else None
        return o or f"assets/v/mouse_{'parla' if ml >= 1 else 'neutro'}_b{b}.png"
    return f"assets/v/{name}_m{max(0, ml)}b{b}.png"

def hold_off(name, t, h, dirn):
    sp = load(sprite_name(name, t)); w = sp.width*h/sp.height
    return (0.26*w if dirn >= 0 else -0.26*w), -0.28*h

# ---------------------------------------------------------------- effetti
class Ctx: pass

def star4(d, x, y, r, col):
    k = 0.2; d.polygon([(x, y-r), (x+r*k, y-r*k), (x+r, y), (x+r*k, y+r*k), (x, y+r), (x-r*k, y+r*k), (x-r, y), (x-r*k, y-r*k)], fill=col)

def sparkles(c, x, y, t0, dur, n=14, spread=120, rise=60, size=16, colors=((255, 245, 170), (255, 255, 255), (255, 210, 120)), seed=1):
    """Scintille additive (coordinate mondo)."""
    t = c.t
    if not (t0 <= t < t0+dur): return
    for k in range(n):
        ph = (k*0.6180339+seed*0.37) % 1.0; life = 0.5+0.5*((k*0.41+seed) % 1.0); u = ((t-t0)/dur*1.4 + ph) % 1.0
        if u > life: continue
        a = k*2.399+seed; r = spread*(0.25+0.75*((k*0.37+seed*0.11) % 1.0))*(0.4+u)
        px, py = c.X(x+math.cos(a)*r), c.Y(y+math.sin(a)*r*0.8-rise*u)
        fade = math.sin(math.pi*u/life); col = tuple(int(v*fade) for v in colors[k % len(colors)])
        rr = size*c.Z*(0.5+fade*0.7)*(0.6+0.4*math.sin(t*12+k))
        star4(c.gd, px, py, rr, col); c.gd.ellipse([px-rr*0.25, py-rr*0.25, px+rr*0.25, py+rr*0.25], fill=col)
        c.glow_used = True

RB = [(255, 70, 70), (255, 150, 50), (255, 225, 70), (100, 210, 100), (80, 160, 255), (110, 100, 230), (190, 110, 230)]
def rainbow(c, t0, cx=540, cy=1190, R=520, band=34, fadeout=None):
    if c.t < t0: return
    p = ease((c.t-t0)/1.4); a = min(1, (c.t-t0)/0.5)*0.88
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i, col in enumerate(RB):
        r = (R-i*band)*c.Z; bb = [c.X(cx)-r, c.Y(cy)-r, c.X(cx)+r, c.Y(cy)+r]
        d.arc(bb, 180, 180+180*p, fill=col+(int(255*a),), width=int(band*c.Z)+1)
    lay = lay.filter(ImageFilter.GaussianBlur(1.6)); c.img.paste(lay, (0, 0), lay)
    if p < 1:                                     # scintille sulla punta
        ang = math.radians(180+180*p); ex, ey = c.X(cx+math.cos(ang)*(R-3*band)), c.Y(cy+math.sin(ang)*(R-3*band))
        star4(c.gd, ex, ey, 40*c.Z, (255, 255, 220)); c.glow_used = True

def butterfly(c, x, y, size, ang, phase, cols):
    Ssz = 3; w = int(size*c.Z*2.6); w = max(20, min(w, 600)); cv = Image.new("RGBA", (w*Ssz, w*Ssz), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
    ox, oy = w*Ssz/2, w*Ssz/2; u = w*Ssz*0.30; fl = abs(math.cos(phase))*0.82+0.18
    fore = [(0, 0), (0.95, -0.95), (1.45, -0.55), (1.2, 0.1), (0.15, 0.1)]; hind = [(0, 0.05), (1.0, 0.18), (1.05, 0.85), (0.5, 1.0), (0.1, 0.5)]
    for sg in (-1, 1):
        for poly, col, col2 in ((fore, cols[0], cols[1]), (hind, cols[1], cols[0])):
            pts = [(ox+sg*px*fl*u, oy+py*u) for px, py in poly]; d.polygon(pts, fill=col+(255,), outline=(60, 40, 70, 255))
            cxp = sum(p[0] for p in pts)/len(pts); cyp = sum(p[1] for p in pts)/len(pts); r_ = u*0.28
            d.ellipse([cxp-r_, cyp-r_, cxp+r_, cyp+r_], fill=col2+(255,))
    d.ellipse([ox-u*0.07, oy-u*0.55, ox+u*0.07, oy+u*0.55], fill=(60, 40, 60, 255))
    d.line([(ox, oy-u*0.5), (ox-u*0.25, oy-u*0.9)], fill=(60, 40, 60, 255), width=int(u*0.04)+1); d.line([(ox, oy-u*0.5), (ox+u*0.25, oy-u*0.9)], fill=(60, 40, 60, 255), width=int(u*0.04)+1)
    cv = cv.resize((w, w), Image.LANCZOS).rotate(ang, resample=Image.BICUBIC); c.img.paste(cv, (int(x-w/2), int(y-w/2)), cv)

def flower(c, x, y, size, grow, col, sway=0.0):
    """Fiore che sboccia: x,y mondo (base), size mondo, grow 0..1."""
    if grow <= 0: return
    g = back(grow); sz = size*c.Z; Sx = 2; w = int(sz*3.2); w = max(16, min(w, 500)); hgt = int(sz*3.6)
    cv = Image.new("RGBA", (w*Sx, hgt*Sx), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
    bx, by = w*Sx/2, hgt*Sx-4*Sx; sh = sz*1.7*min(1, g)*Sx
    d.line([(bx, by), (bx+sway*sz*0.25*Sx, by-sh)], fill=(60, 150, 70, 255), width=int(sz*0.12*Sx)+1)
    lx, ly = bx+sway*sz*0.06*Sx, by-sh*0.45
    d.ellipse([lx, ly-sz*0.12*Sx, lx+sz*0.5*Sx, ly+sz*0.12*Sx], fill=(90, 190, 90, 255))
    fx, fy = bx+sway*sz*0.25*Sx, by-sh; pr = sz*0.36*g*Sx; dark = tuple(int(v*0.82) for v in col)
    for k in range(6):
        a = k*math.pi/3+0.3; px, py = fx+math.cos(a)*pr*0.95, fy+math.sin(a)*pr*0.95
        d.ellipse([px-pr*0.62, py-pr*0.62, px+pr*0.62, py+pr*0.62], fill=dark+(255,)); d.ellipse([px-pr*0.5, py-pr*0.52, px+pr*0.42, py+pr*0.42], fill=col+(255,))
    d.ellipse([fx-pr*0.5, fy-pr*0.5, fx+pr*0.5, fy+pr*0.5], fill=(255, 205, 60, 255)); d.ellipse([fx-pr*0.28, fy-pr*0.32, fx+pr*0.1, fy+pr*0.05], fill=(255, 235, 140, 255))
    cv = cv.resize((w, hgt), Image.LANCZOS); c.img.paste(cv, (int(c.X(x)-w/2), int(c.Y(y)-hgt+4)), cv)

def notes(c, x, y, t0, dur, n=6, seed=2):
    if not (t0 <= c.t < t0+dur): return
    f = ImageFont.truetype(FONT, int(54*c.Z))
    for k in range(n):
        u = ((c.t-t0)/dur*1.6 + k/n) % 1.0; px = c.X(x+math.sin(u*6+k)*90+(k-n/2)*40); py = c.Y(y-u*300)
        a = int(255*math.sin(math.pi*u)); col = ((255, 120, 150), (255, 220, 70), (120, 200, 255), (160, 230, 120))[k % 4]
        c.d.text((px, py), "♪♫"[k % 2], font=f, fill=col+(a,), anchor="mm", stroke_width=3, stroke_fill=(60, 40, 20, a))

def confetti(c, t0, n=14):
    if c.t < t0: return
    for k in range(n):
        px = ((k*113+40) % W) + math.sin(c.t*3+k)*30; py = ((c.t-t0)*240+k*160) % 1700+120
        col = ((255, 120, 150), (255, 220, 70), (120, 200, 255), (160, 230, 120))[k % 4]; c.d.ellipse([px-9, py-9, px+9, py+9], fill=col)

def subscribe_button(img, t, t0, cy=1480):
    """Pulsante 'Iscriviti' dentro la scena (non una slide): compare con rimbalzo, la campanella dondola."""
    if t < t0: return
    u = back((t-t0)/0.45); s = max(0.05, u)*(1+0.03*math.sin((t-t0)*6))
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

# ---------------------------------------------------------------- frame
_bgsrc = None
def frame(i):
    global _bgsrc
    t = i/FPS; cx, cy, Z = camera(t)
    if _bgsrc is None: _bgsrc = Image.open(os.path.join(HERE, "assets/s/sfondo_src.png")).convert("RGB")
    sx_, sy_ = _bgsrc.width/W, _bgsrc.height/H
    img = _bgsrc.resize((W, H), Image.BICUBIC, box=((cx-540/Z)*sx_, (cy-960/Z)*sy_, (cx+540/Z)*sx_, (cy+960/Z)*sy_))
    img = img.filter(ImageFilter.GaussianBlur(1.0+1.6*max(0, Z-1)))
    c = Ctx(); c.img = img; c.d = ImageDraw.Draw(img, "RGBA"); c.t = t; c.Z = Z; c.cx = cx; c.cy = cy
    c.X = lambda x: (x-cx)*Z+W/2; c.Y = lambda y: (y-cy)*Z+H/2
    c.glow = Image.new("RGB", (W, H), (0, 0, 0)); c.gd = ImageDraw.Draw(c.glow); c.glow_used = False
    X, Y, d = c.X, c.Y, c.d
    if hasattr(S, "back_fx0"): S.back_fx0(c)
    for b, bx in ([] if getattr(S, "NO_BINS", False) else BIN_X.items()):
        v = 0
        for it in S.ITEMS:
            tl = it[5]+FLY
            if it[6] == b and tl <= t < tl+0.45: v = max(v, math.sin((t-tl)/0.45*math.pi)*(1-(t-tl)/0.45))
        shadow(img, X(bx+25), Y(BIN_Y), 250*Z); put(img, load(f"assets/s/bin_{b}.png"), X(bx), Y(BIN_Y+4), BIN_H*Z, sq=1-0.07*v)
    if hasattr(S, "back_fx1"): S.back_fx1(c)
    for kind, ix, iy, who, tp, tl, b in S.ITEMS:
        if t < tp:
            hh = ITEM_H[kind]*persp(iy)/0.86*0.9
            shadow(img, X(ix+8), Y(iy), hh*Z*1.2, 0.8); put(img, load(f"assets/s/item_{kind}.png"), X(ix), Y(iy), hh*Z, ang=((ix*7) % 50)-25)
    chars = []
    for n, tin in S.CHARS.items():
        if tin is not None and t >= tin and not (n in getattr(S, "HIDE", {}) and S.HIDE[n][0] <= t < S.HIDE[n][1]): chars.append((cstate(n, t), n))
    for (x, y, h, hop, rot, sq, dirn, mv), n in sorted(chars, key=lambda cc: cc[0][1]):
        shadow(img, X(x+0.12*h), Y(y), h*0.62*Z, max(0.45, 1-1.6*hop/h))
        put(img, load(sprite_name(n, t)), X(x), Y(y-hop), h*Z, ang=rot, sq=sq, flip=(dirn < 0 and mv))
        for kind, ix, iy, who, tp, tl, b in S.ITEMS:
            if who == n and tp <= t < tl:
                ox, oy = hold_off(n, t, h, dirn)
                put(img, load(f"assets/s/item_{kind}.png"), X(x+ox), Y(y-hop+oy)+ITEM_H[kind]*0.5*Z, ITEM_H[kind]*1.15*Z, ang=math.sin(t*9)*8)
        if hasattr(S, "char_fx"): S.char_fx(c, n, x, y, h, hop, t)
    for kind, ix, iy, who, tp, tl, b in S.ITEMS:
        if tl <= t < tl+FLY:
            x, y, h, hop, rot, sq, dirn, mv = cstate(who, tl); ox, oy = hold_off(who, tl, h, dirn)
            hx, hy = x+ox, y+oy; u = (t-tl)/FLY; bx, by = BIN_X[b], BIN_Y-BIN_H
            px, py = lerp(hx, bx, u), lerp(hy, by, u)-260*math.sin(u*math.pi)
            put(img, load(f"assets/s/item_{kind}.png"), X(px), Y(py)+ITEM_H[kind]*0.5*Z, ITEM_H[kind]*1.15*Z*(1-0.3*u), ang=u*540)
    if hasattr(S, "front_fx"): S.front_fx(c)
    if c.glow_used:
        g2 = c.glow.filter(ImageFilter.GaussianBlur(9)); c.img = img = ImageChops.add(ImageChops.add(img, c.glow), g2); c.d = d = ImageDraw.Draw(img, "RGBA")
    img = ImageChops.multiply(img, vignette())
    img = Image.blend(img, ImageChops.multiply(img, Image.new("RGB", (W, H), (255, 250, 238))), 0.6)
    d = ImageDraw.Draw(img, "RGBA")
    for k, t0, who, txt, dur in S.VOICES:
        if getattr(S, "SUBS", True) and t0-0.05 <= t <= t0+dur+0.3:
            u = ease((t-t0+0.05)/0.18); f = ImageFont.truetype(FONT, 66); lines = []; cur = ""
            for wd in txt.split():
                tl_ = (cur+" "+wd).strip(); bb = d.textbbox((0, 0), tl_, font=f, anchor="mm", stroke_width=6)
                if bb[2]-bb[0] > 930 and cur: lines.append(cur); cur = wd
                else: cur = tl_
            lines.append(cur); yy = S.SUB_Y(t) - 41*(len(lines)-1) + (1-u)*14
            for ln in lines: text(d, ln, W/2, yy, 66, S.SPK_COL[who]+(int(255*u),), (60, 40, 20, int(255*u)), 7); yy += 82
            break
    if hasattr(S, "overlay"):
        r = S.overlay(img, t); img = r if r is not None else img
    return img.tobytes()

if __name__ == "__main__":
    if sys.argv[1] == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(float(ts)*FPS))).save(f"test_{S.__name__}_{ts}.png")
    else:
        out = sys.argv[2]; N = int(S.DUR*FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
