#!/usr/bin/env python3
"""Puliamo il parco! v3 - topolino reale (immagini AI Studio) sopra lo sfondo, storia solo del topolino."""
import math, sys, subprocess, json, os
from multiprocessing import Pool
from PIL import Image, ImageFilter, ImageFont
import render as R
from render import Cv, lerp, ease, W, H, FPS, K

DUR = 36.0
HERE = os.path.dirname(os.path.abspath(__file__))
_D = json.load(open(os.path.join(HERE, "audio/durate.json")))

# ---------------------------------------------------------------- storia
R.BINS["giallo"] = (300, R.BINS["giallo"][1], "PLASTICA")
R.BINS["blu"] = (560, R.BINS["blu"][1], "CARTA")
R.BINS["marrone"] = (820, R.BINS["marrone"][1], "UMIDO")
R.BIN_Y = 1470
BIN_S = 1.5

# (tipo, x, y, chi, t_raccolta, t_lancio, cestino)
ITEMS = [
 ("bottle", 200, 1720, "mouse", 8.6, 10.8, "giallo"),
 ("news",   520, 1790, "mouse", 12.2, 14.0, "blu"),
 ("peel",   800, 1700, "mouse", 15.4, 17.4, "marrone"),
 ("can",    400, 1665, "mouse", 18.8, 20.6, "giallo"),
 ("paper",  900, 1800, "mouse", 22.0, 24.0, "blu"),
 ("core",   700, 1650, "mouse", 25.2, 27.0, "marrone"),
]
FLY = 0.55
_V = [("n1", 0.6, "mouse", "Oh no! Quanti rifiuti nel parco!"),
      ("n2", 4.6, "mouse", "Ma io so cosa fare! Raccolgo tutto!"),
      ("n3", 9.0, "mouse", "La bottiglia va nel giallo!"),
      ("n4", 12.4, "mouse", "La carta va nel blu!"),
      ("n5", 15.6, "mouse", "La buccia va nel marrone!"),
      ("n6", 19.0, "mouse", "Ancora un po'!"),
      ("n7", 28.0, "mouse", "Il parco è pulito!"),
      ("n8", 30.6, "mouse", "Ciao ciao bambini!")]
VOICES = [(k, t, w, x, _D[k]) for k, t, w, x in _V]

STAND = lambda ix, iy: (ix + 75, iy - 35)
BINSTAND = {"giallo": (330, 1600), "blu": (590, 1605), "marrone": (850, 1605)}
KF = [(0, -220, 1640), (2.0, 300, 1640), (8.0, 300, 1640)]
for kind, ix, iy, who, tp, tl, b in ITEMS:
    sx, sy = STAND(ix, iy); bx, by = BINSTAND[b]
    KF += [(tp - 0.7, sx, sy), (tp + 0.1, sx, sy)]
    KF += [(tl - 0.3, bx, by), (tl + 0.5, bx, by)]
KF += [(28.0, 540, 1655), (40, 540, 1655)]
# elimina eventuali istanti non crescenti
_clean = [KF[0]]
for k in KF[1:]:
    if k[0] > _clean[-1][0]: _clean.append(k)
KF = _clean

def pos(t):
    return R.interp(KF, t)

# ---------------------------------------------------------------- immagini
POSE = {}
def pose(name):
    if name not in POSE: POSE[name] = Image.open(os.path.join(HERE, f"assets/topo/{name}.png")).convert("RGBA")
    return POSE[name]

BINSPR = {}
def bin_sprite(key):
    if key not in BINSPR:
        layer = Image.new("RGBA", (W*K, H*K), (0, 0, 0, 0)); c = Cv(layer)
        R.draw_bin(c, key, 0)
        bx = R.BINS[key][0]
        BINSPR[key] = layer.crop(((bx-125)*K, (R.BIN_Y-260)*K, (bx+125)*K, (R.BIN_Y+35)*K))
    return BINSPR[key]

def paste_center_bottom(img, sp, x, y, sx, sy, ang=0):
    """Incolla lo sprite con il centro-basso in (x,y), scala (sx,sy) in unità schermo."""
    w, h = sp.size
    nw, nh = int(w*sx*K/ K * 1), int(h*sy*K/ K * 1)
    return None

def put_sprite(img, sp, x, y, scale_x, scale_y, ang=0):
    w, h = sp.size
    nw, nh = max(1, int(w*scale_x)), max(1, int(h*scale_y))
    s2 = sp.resize((nw, nh), Image.BICUBIC)
    if ang:
        pad = int(nw*0.25)
        cv = Image.new("RGBA", (nw+2*pad, nh+pad), (0, 0, 0, 0)); cv.paste(s2, (pad, 0), s2)
        cv = cv.rotate(ang, resample=Image.BICUBIC, center=(pad+nw//2, nh))
        img.paste(cv, (int(x*K - pad - nw/2), int(y*K - nh)), cv)
    else:
        img.paste(s2, (int(x*K - nw/2), int(y*K - nh)), s2)

def scale_at(y): return 0.74 * (0.9 + (y-1500)/1500*0.5)

def speaking(t):
    for k, t0, who, txt, dur in VOICES:
        if t0 <= t <= t0+dur: return True
    return False

def mouse_state(t):
    x, y, walking, dirn = pos(t)
    sc = scale_at(y)
    cheer = t >= 27.4
    sad = 1.7 < t < 4.5
    if sad: name = "triste"
    elif cheer: name = "braccia_su"
    else: name = "neutro"
    if speaking(t) and not sad and math.sin(t*15) > -0.1: name = "parla" if not cheer else "braccia_su"
    hop = rot = 0; sq = 1.0
    if walking:
        ph = t*11; hop = abs(math.sin(ph))*26*sc/0.56; rot = math.sin(ph)*3.2
        sq = 1 + 0.03*math.sin(ph*2)
    elif cheer:
        hop = abs(math.sin(t*5))*40; sq = 1 + 0.04*math.sin(t*10)
    else:
        sq = 1 + 0.012*math.sin(t*3)
    return x, y, sc, name, dirn, hop, rot, sq, walking

def hand_of(x, y, sc, dirn, hop):
    # mano destra del personaggio (nell'immagine ritagliata 598x956: ~ (483,694)); mirror se va a sinistra
    iw, ih = 598, 956
    hx = (483 - iw/2) * sc * (1 if dirn >= 0 else -1)
    hy = -(ih - 694) * sc
    return x + hx, y + hy - hop

def bin_squash(t):
    out = {}
    for it in ITEMS:
        tl = it[5] + FLY; v = out.get(it[6], 0)
        if tl <= t < tl+0.45: v = max(v, math.sin((t-tl)/0.45*math.pi) * (1-(t-tl)/0.45))
        out[it[6]] = v
    return out

def frame(i):
    t = i / FPS
    img = R.get_bg().copy().convert("RGB")
    c = Cv(img)
    for cx, cy, sp_, sc_ in ((100, 230, 14, 1.0), (520, 420, 9, 0.8), (800, 130, 11, 0.7)):
        R.cloud(c, (cx + t*sp_) % (W+400) - 200, cy, sc_)
    sq = bin_squash(t)
    for key in R.BINS:
        sp = bin_sprite(key); bx = R.BINS[key][0]
        put_sprite(img, sp, bx, R.BIN_Y + 6, BIN_S*(1+0.06*sq.get(key, 0)), BIN_S*(1-0.08*sq.get(key, 0)))
    c = Cv(img)
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if t < tp: R.draw_item(c, kind, ix, iy, ang=(ix*7) % 50 - 25, s=1.25)
    # topolino
    x, y, sc, name, dirn, hop, rot, sq_, walking = mouse_state(t)
    c.e(x, y+4, 150*sc/0.56*0.55, 22*sc/0.56*0.55, (20, 60, 20, 70))
    sp = pose(name)
    if dirn < 0: sp = sp.transpose(Image.FLIP_LEFT_RIGHT)
    put_sprite(img, sp, x, y - hop, sc*K*sq_**-1, sc*K*sq_, rot)
    c = Cv(img)
    # oggetto in mano / in volo
    for kind, ix, iy, who, tp, tl, b in ITEMS:
        if tp <= t < tl:
            hx, hy = hand_of(x, y, sc, dirn, hop)
            R.draw_item(c, kind, hx, hy - 20, ang=math.sin(t*9)*8, s=1.0)
        elif tl <= t < tl + FLY:
            xs, ys, scs, _, ds, hp, _, _, _ = mouse_state(tl)
            hx, hy = hand_of(xs, ys, scs, ds, 0)
            bx, by = R.BINS[b][0], R.BIN_Y - 285
            u = (t - tl) / FLY
            R.draw_item(c, kind, lerp(hx, bx, u), lerp(hy-20, by, u) - 260*math.sin(u*math.pi), ang=u*540, s=1.0*(1-0.3*u))
        if tl + FLY <= t < tl + FLY + 0.5:
            u = (t-tl-FLY)/0.5; bx = R.BINS[b][0]
            for k in range(6):
                a = k*math.pi/3 + 0.4
                c.e(bx+math.cos(a)*(30+100*u), R.BIN_Y-300+math.sin(a)*(30+100*u)-40*u, 10*(1-u)+2, 10*(1-u)+2, (255, 235, 90, int(255*(1-u))))
    # fiori e farfalle alla fine
    if t > 27.0:
        g = ease((t-27.0)/2.0)
        for fx, fy, col in ((140, 1640, (255, 110, 150)), (300, 1810, (255, 220, 70)), (470, 1720, (255, 255, 255)),
                            (650, 1800, (190, 140, 255)), (820, 1690, (255, 110, 150)), (990, 1770, (255, 220, 70)),
                            (70, 1860, (190, 140, 255)), (700, 1880, (255, 110, 150))):
            R.flower(c, fx, fy-20, 1.4*g, col)
        for k in range(4):
            bx = 200 + k*220 + math.sin(t*1.7 + k)*70; by = 1000 + k*60 + math.cos(t*2.3 + k)*50
            wv = abs(math.sin(t*14 + k)); col = ((255, 140, 200), (255, 190, 70), (140, 200, 255), (200, 160, 255))[k]
            c.e(bx-18*wv-4, by, 20*wv+4, 26, col); c.e(bx+18*wv+4, by, 20*wv+4, 26, col)
            c.l([(bx, by-12), (bx, by+14)], (80, 60, 70), 5)
    # sottotitoli
    for k, t0, who, txt, dur in VOICES:
        if t0 - 0.05 <= t <= t0 + dur + 0.35:
            a = int(255 * min(1, (t-t0+0.05)/0.15))
            f = ImageFont.truetype(R.FONT, 72*K)
            bb = c.d.textbbox((0, 0), txt, font=f, anchor="mm", stroke_width=6*K)
            lines = [txt]
            if (bb[2]-bb[0])/K > 960:
                words = txt.split(); half = len(words)//2; lines = [" ".join(words[:half]), " ".join(words[half:])]
            yy = 360 if len(lines) == 1 else 320
            for ln in lines:
                c.t(ln, W/2, yy, 72, (255, 255, 255, a), (60, 40, 20, a), 7); yy += 90
            break
    if t < 3:
        a = int(255 * min(1, (3-t)/0.6))
        c.t("PULIAMO IL PARCO!", W/2, 140, 70, (255, 255, 255, a), (230, 90, 60, a), 10)
    if t > 33.2:
        u = ease((t-33.2)/0.6)
        img = Image.blend(img, Image.new("RGB", (W*K, H*K), (255, 245, 210)), 0.92*u); c = Cv(img)
        by = 520 + (1-u)*60
        c.t("Ricicla anche tu!", W/2, by, 86, (60, 160, 70), (255, 255, 255), 8)
        for j, key in enumerate(("giallo", "blu", "marrone")):
            c.e(240+j*300, by+150, 70, 70, R.BINS[key][1], (255, 255, 255), 6)
        c.t("Plastica  ·  Carta  ·  Umido", W/2, by+300, 52, (90, 70, 50))
        c.t("Bambini Ciao Ciao", W/2, by+450, 92, (230, 90, 60), (255, 255, 255), 8)
        c.t("Un nuovo video ogni settimana!", W/2, by+550, 46, (110, 90, 70))
        put_sprite(img, pose("braccia_su"), W/2, 1800 - abs(math.sin(t*5))*30, 0.72*K, 0.72*K)
    return img.convert("RGB").resize((W, H), Image.LANCZOS).tobytes()

if __name__ == "__main__":
    if sys.argv[1] == "test":
        for ts in sys.argv[2:]:
            Image.frombytes("RGB", (W, H), frame(int(float(ts)*FPS))).save(f"test2_{ts}.png")
    else:
        N = int(DUR*FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                               "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17",
                               "-preset", "medium", "video_muto2.mp4"], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(N), chunksize=4)):
                ff.stdin.write(fr)
                if n % 48 == 0: print(f"{n}/{N}", flush=True)
        ff.stdin.close(); ff.wait()
