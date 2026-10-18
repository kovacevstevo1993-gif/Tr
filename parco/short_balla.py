#!/usr/bin/env python3
"""Short 'Balla con la volpe' (9:16, 1080x1920, 30 fps): la volpe insegna un ballo ai bambini (interattivo: i bambini imitano).
Animazione a MARIONETTA (rig.py): la volpe si muove in modo continuo (braccia, gambe, testa, coda con articolazioni),
le mosse si fondono una nell'altra, salti con anticipo e atterraggio, giravolte, coda che scodinzola con ritardo.
Personaggio GRANDE e al CENTRO, niente sottotitoli.
    python3 short_balla.py info | test 1.0 5.5 | renderpart a b out.mp4 | render muto.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import rig
from short_razzo import lerp, clamp, ease, back, osc, text, star4, subscribe_button

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
AUD = "audioM"
D = json.load(open(os.path.join(HERE, AUD, "durate.json")))
BEAT = 0.5

V = {}
def _seq():
    t = 0.0
    def at(k, gap):
        nonlocal t
        V[k] = t + gap; t = V[k] + D[k]
    at("n1", 0.5); at("v1", 1.0); at("v2", 2.6); at("v3", 2.8); at("v4", 2.6); at("v5", 2.8); at("n2", 2.8); at("v6", 4.6); at("end", 2.2)
    return t + 3.0
DUR = _seq()
VOICES = [(k, V[k], "narr" if k.startswith("n") else "volpe", D[k]) for k in V]
E = lambda k: V[k] + D[k]

# mosse: (inizio, nome) ; ogni mossa è una funzione del tempo locale
MOVES = [(0.0, "ciao"), (V["v1"] - 0.15, "alto"), (V["v2"] - 0.15, "mani"), (V["v3"] - 0.15, "salta"), (V["v4"] - 0.15, "gira"),
         (V["v5"] - 0.15, "coda"), (V["n2"] - 0.1, "ciao"), (E("n2") + 0.1, "combo"), (V["v6"] - 0.35, "evviva"), (V["v6"] + 1.6, "festa"),
         (V["end"] - 0.1, "saluta")]
BLEND = 0.3
STAND = {"braccio_s": -100.0, "braccio_d": 100.0, "gamba_s": -24.0, "gamba_d": 28.0, "coda": 0.0, "testa": 0.0, "busto": 0.0}


def _talk_env():
    env = {}
    for k, t0, who, d in VOICES:
        with wave.open(os.path.join(HERE, AUD, f"{k}.wav")) as wf:
            a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
        win = 44100 // 60; n = len(a) // win + 1
        e = np.array([np.sqrt(np.mean(a[i * win:(i + 1) * win] ** 2) + 1e-12) for i in range(n)]); env[k] = e / (np.percentile(e, 95) + 1e-9)
    return env
ENV = _talk_env()


def talk(t):
    for k, t0, who, d in VOICES:
        if who == "volpe" and t0 <= t <= t0 + d:
            e = ENV[k]; return min(1.0, e[min(len(e) - 1, int((t - t0) * 60))])
    return 0.0


def move_pose(name, u, t):
    """posa (angoli) + extra: hop (px), flip (scala x), rot (gradi), sq"""
    p = dict(STAND); hop = 0.0; flip = 1.0; rot = 0.0; sq = 1.0
    b = (t / BEAT) % 1.0; bb = math.sin(2 * math.pi * t / BEAT)
    if name == "ciao":
        p["braccio_d"] = 8 + 26 * math.sin(t * 9.5); p["braccio_s"] = -95 + 6 * math.sin(t * 2)
        p["busto"] = 4 * math.sin(t * 2.2); p["testa"] = -6 + 4 * math.sin(t * 2.6)
        sq = 1 + 0.015 * math.sin(t * 4.4)
    elif name == "alto":
        p["braccio_s"] = -8 + 14 * math.sin(t * 11); p["braccio_d"] = 8 + 14 * math.sin(t * 11 + 1)
        sq = 1 - 0.035 * abs(bb); hop = 18 * abs(math.sin(math.pi * t / BEAT)); p["testa"] = 6 * math.sin(t * 5)
    elif name == "mani":                                                      # batte le mani sopra la testa a tempo
        c = 0.5 - 0.5 * math.cos(2 * math.pi * t / BEAT); c = c ** 0.6
        p["braccio_s"] = lerp(-30, 72, c); p["braccio_d"] = lerp(30, -66, c)
        sq = 1 - 0.03 * c; p["testa"] = 5 * math.sin(t * 6.3)
    elif name == "salta":                                                     # due salti: anticipo, volo con gambe aperte, atterraggio
        per = 1.0; ph = (u % per) / per
        if ph < 0.22:
            k = ease(ph / 0.22); sq = 1 - 0.10 * k; p["braccio_s"] = lerp(-100, -125, k); p["braccio_d"] = lerp(100, 125, k)
        elif ph < 0.80:
            k = (ph - 0.22) / 0.58; hop = 4 * k * (1 - k) * 330; sq = 1 + 0.06 * math.sin(math.pi * k)
            p["braccio_s"] = lerp(-125, -5, ease(min(1, k * 2.5))); p["braccio_d"] = lerp(125, 5, ease(min(1, k * 2.5)))
            p["gamba_s"] = lerp(-24, 2, math.sin(math.pi * k)); p["gamba_d"] = lerp(28, -2, math.sin(math.pi * k)); p["coda"] = -25 * math.sin(math.pi * k)
        else:
            k = (ph - 0.80) / 0.20; sq = 1 - 0.10 * math.sin(math.pi * k); p["braccio_s"] = lerp(-5, -100, ease(k)); p["braccio_d"] = lerp(5, 100, ease(k))
    elif name == "gira":                                                      # giravolta: larghezza = cos(angolo), si specchia a metà
        per = 1.15; ph = (u % per) / per
        flip = math.cos(2 * math.pi * ease(ph)); hop = 40 * math.sin(math.pi * ph)
        p["braccio_s"] = -40; p["braccio_d"] = 40; p["coda"] = 30 * math.sin(2 * math.pi * ph)
    elif name == "coda":                                                      # scodinzola + anche che ondeggiano
        p["coda"] = 38 * math.sin(t * 14); p["busto"] = 7 * math.sin(t * 7); rot = 3 * math.sin(t * 7)
        p["braccio_s"] = -70 + 10 * math.sin(t * 7); p["braccio_d"] = 70 + 10 * math.sin(t * 7); p["testa"] = -8 * math.sin(t * 7)
    elif name == "combo":                                                     # tutto insieme, più veloce
        seq = ["alto", "mani", "salta", "gira"]; seg = 1.0; i = int(u / seg) % 4
        return move_pose(seq[i], (u % seg) / seg * (1.0 if seq[i] != "gira" else 1.15) + (0 if seq[i] != "salta" else 0), t)
    elif name == "evviva":
        k = clamp(u / 1.3)
        if k < 0.2: sq = 1 - 0.12 * ease(k / 0.2)
        else:
            q = (k - 0.2) / 0.8; hop = 4 * q * (1 - q) * 520; p["braccio_s"] = -5; p["braccio_d"] = 5
            p["gamba_s"] = lerp(-24, 4, math.sin(math.pi * q)); p["gamba_d"] = lerp(28, -4, math.sin(math.pi * q)); rot = 8 * math.sin(math.pi * q)
    elif name == "festa":                                                     # ballo libero
        p["braccio_s"] = -40 + 40 * math.sin(t * 6.3); p["braccio_d"] = 40 + 40 * math.sin(t * 6.3 + math.pi)
        p["busto"] = 8 * math.sin(t * 6.3); p["coda"] = 30 * math.sin(t * 12); hop = 22 * abs(math.sin(t * 6.3)); p["testa"] = -6 * math.sin(t * 6.3)
        p["gamba_s"] = -24 + 8 * math.sin(t * 6.3); p["gamba_d"] = 28 + 8 * math.sin(t * 6.3)
    elif name == "saluta":
        p["braccio_d"] = 8 + 26 * math.sin(t * 9.5); p["braccio_s"] = -8 - 26 * math.sin(t * 9.5 + 1)
        p["busto"] = 5 * math.sin(t * 3); p["coda"] = 25 * math.sin(t * 10); hop = 10 * abs(math.sin(t * 4))
    # vita: respiro, coda che segue, testa che annuisce parlando
    tk = talk(t)
    p["testa"] += 2.5 * math.sin(t * 1.7) + 7 * tk * math.sin(t * 13)
    p["coda"] += 10 * math.sin(t * 3.1 - 0.6)
    p["_breath"] = 1 + 0.012 * math.sin(t * 2.4)
    return p, hop, flip, rot, sq


def pose_at(t):
    idx = 0
    for i, (t0, _) in enumerate(MOVES):
        if t >= t0: idx = i
    t0, nm = MOVES[idx]
    cur = move_pose(nm, t - t0, t)
    if idx > 0 and t - t0 < BLEND:                                               # fusione morbida con la mossa precedente
        pt0, pnm = MOVES[idx - 1]; prev = move_pose(pnm, t - pt0, t); k = ease((t - t0) / BLEND)
        p = {key: lerp(prev[0].get(key, 0.0), cur[0].get(key, 0.0), k) for key in set(prev[0]) | set(cur[0])}
        return p, lerp(prev[1], cur[1], k), lerp(prev[2], cur[2], k) if (prev[2] > 0) == (cur[2] > 0) else cur[2], lerp(prev[3], cur[3], k), lerp(prev[4], cur[4], k)
    return cur


# ------------------------------------------------------------------ disegno
RIG = None
_bg = None
def bg():
    global _bg
    if _bg is None:
        _bg = Image.open(os.path.join(HERE, "assets", "amb", "radura_festa.png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.6))
    return _bg


GROUND = 1760.0
SCALE = 1.15


def fox_layer(t):
    """volpe in posa su un livello RGBA a piena scena, appoggiata a terra"""
    global RIG
    if RIG is None: RIG = rig.Rig(rig.CONF["volpe"])
    p, hop, flip, rot, sq = pose_at(t)
    p["_rot"] = rot; p["_sq"] = sq
    arr = RIG.render(p, SCALE)
    a = arr[..., 3] > 30; ys, xs = np.nonzero(a)
    bot = ys.max(); cxm = 0.5 * (xs.min() + xs.max())
    im = Image.fromarray(arr, "RGBA")
    if abs(flip) < 0.999:
        w = max(4, int(im.width * abs(flip))); im = im.resize((w, im.height), Image.LANCZOS)
        if flip < 0: im = im.transpose(Image.FLIP_LEFT_RIGHT)
        cxm = cxm * abs(flip) if flip > 0 else (im.width - cxm * abs(flip))
    return im, int(W / 2 - cxm), int(GROUND - hop - bot), hop, abs(flip)


def confetti(d, t, t0, n=120, dur=3.2, seed=4):
    if not (t0 <= t < t0 + dur): return
    rng = np.random.default_rng(seed); u = t - t0
    cols = [(255, 80, 120), (80, 180, 255), (255, 220, 60), (120, 230, 120), (200, 120, 255), (255, 150, 60)]
    for k in range(n):
        x0 = rng.uniform(0, W); vx = rng.uniform(-200, 200); vy = rng.uniform(-1700, -900)
        x = x0 + vx * u + 40 * math.sin(u * 5 + k); y = H + 50 + vy * u + 900 * u * u
        if y > H + 60: continue
        s = rng.uniform(9, 17); ang = u * rng.uniform(4, 10) + k; fl = abs(math.cos(u * 7 + k)); ca, sa = math.cos(ang), math.sin(ang)
        pts = [(x + dx * s * ca - dy * s * 0.5 * fl * sa, y + dx * s * sa + dy * s * 0.5 * fl * ca) for dx, dy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        d.polygon(pts, fill=cols[k % 6] + (255,))


def frame(i):
    t = i / FPS
    img = bg().copy()
    # camera lievemente viva: piccolo zoom a tempo
    z = 1.0 + 0.02 * (0.5 - 0.5 * math.cos(2 * math.pi * t / (4 * BEAT)))
    if z > 1.0:
        w2, h2 = int(W / z), int(H / z); img = img.crop(((W - w2) // 2, (H - h2) // 2 + 60, (W - w2) // 2 + w2, (H - h2) // 2 + 60 + h2)).resize((W, H), Image.BICUBIC)
    d = ImageDraw.Draw(img, "RGBA")
    glow = Image.new("RGB", (W, H), (0, 0, 0)); gd = ImageDraw.Draw(glow)
    # lucine che pulsano a tempo + lucciole
    rng = np.random.default_rng(7)
    for k in range(40):
        x = rng.uniform(0, W); y = rng.uniform(150, 1000); ph = rng.uniform(0, 6.28)
        a = 0.5 + 0.5 * math.sin(2 * math.pi * t / BEAT + ph)
        if a > 0.5: star4(gd, x, y, 6 + 10 * a, (int(180 * a), int(140 * a), int(60 * a)))
    for k in range(18):
        r2 = np.random.default_rng(300 + k); x0 = r2.uniform(0, W); y0 = r2.uniform(900, 1500)
        x = x0 + 50 * math.sin(t * 0.7 + k); y = y0 + 40 * math.sin(t * 0.9 + 2 * k); a = max(0.0, math.sin(t * 2 + k)) ** 2
        if a > 0.05:
            for rr, lv in ((18, 0.25), (9, 0.6), (4, 1.0)): gd.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(int(170 * a * lv), int(210 * a * lv), int(70 * a * lv)))
    # luce del 'palco' sotto la volpe, che pulsa a tempo
    pulse = 0.5 + 0.5 * math.cos(2 * math.pi * t / BEAT)
    for rr, lv in ((420, 0.18), (300, 0.3), (180, 0.4)):
        gd.ellipse([W / 2 - rr, GROUND - rr * 0.22, W / 2 + rr, GROUND + rr * 0.22], fill=(int(120 * lv * (0.6 + 0.4 * pulse)), int(90 * lv * (0.6 + 0.4 * pulse)), int(40 * lv)))
    fox, fx, fy, hop, fw = fox_layer(t)
    # ombra a terra (si stringe nei salti)
    sw = 330 * fw * clamp(1 - hop / 700, 0.35, 1) + 60
    sh = Image.new("RGBA", (int(sw * 2.2), 120), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([10, 20, sw * 2.2 - 10, 100], fill=(30, 10, 30, int(130 * clamp(1 - hop / 800, 0.3, 1))))
    sh = sh.filter(ImageFilter.GaussianBlur(14)); img.paste(sh, (int(W / 2 - sh.width / 2), int(GROUND - 60)), sh)
    # luce calda del tramonto sul bordo della volpe
    fa = np.asarray(fox).astype(np.float32); al = fa[..., 3] / 255.0
    Lb = cv2.GaussianBlur(al, (0, 0), 7); Ls = cv2.warpAffine(Lb, np.float32([[1, 0, 9], [0, 1, 8]]), (fox.width, fox.height))
    rim = np.clip(al * (1 - Ls * 1.25), 0, 1) ** 1.3
    fa[..., :3] = np.clip(fa[..., :3] * np.array([1.03, 0.98, 0.95]) + rim[..., None] * np.array([255, 170, 120]) * 0.55, 0, 255)
    fox = Image.fromarray(fa.astype(np.uint8), "RGBA")
    img.paste(fox, (fx, fy), fox)
    # scintille a ogni battito di mani e ad ogni atterraggio
    if V["v2"] - 0.15 <= t < V["v3"] - 0.15 or (E("n2") + 1.1 <= t < E("n2") + 2.1):
        c = (t / BEAT) % 1.0
        if c > 0.85 or c < 0.15:
            k = 1 - abs(((c + 0.5) % 1.0) - 0.5) / 0.15
            for j in range(8):
                a = j * 0.785 + t; r = 60 + 90 * (1 - k); star4(gd, W / 2 + math.cos(a) * r, fy + 110 * SCALE + math.sin(a) * r, 18 * k, (int(255 * k), int(230 * k), int(120 * k)))
    confetti(d, t, V["v6"] + 0.4, n=140)
    confetti(d, t, V["end"] + 0.6, n=90, seed=9)
    img = ImageChops.add(ImageChops.add(img, glow), glow.filter(ImageFilter.GaussianBlur(10)))
    a = np.asarray(img).astype(np.float32)
    a = a + np.random.default_rng(i).normal(0, 2.0, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(img, "RGBA")
    if t < 2.4:
        u = back(t / 0.35); al_ = int(255 * clamp((2.4 - t) / 0.4))
        text(d, "BALLA CON ME!", W / 2, 200 - 10 * math.sin(t * 6), int(108 * clamp(max(0.6, u), 0, 1.0)), (255, 235, 90, al_), (200, 40, 110, al_), 13)
    subscribe_button(img, t, V["end"] + 0.9, cy=1830)
    return img.tobytes()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2)); print({k: round(v, 2) for k, v in V.items()}); print([(round(a, 2), b) for a, b in MOVES])
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(round(float(ts) * FPS)))).save(f"/tmp/claude-0/prova/test_b_{ts}.png")
    else:
        if cmd == "renderpart": a, b, out = int(sys.argv[2]), min(int(sys.argv[3]), int(DUR * FPS)), sys.argv[4]
        else: a, b, out = 0, int(DUR * FPS), sys.argv[2]
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
        with Pool(4) as pool:
            for n, fr in enumerate(pool.imap(frame, range(a, b), chunksize=4)):
                ff.stdin.write(fr)
                if n % 90 == 0: print(f"{a + n}/{b}", flush=True)
        ff.stdin.close(); ff.wait()
