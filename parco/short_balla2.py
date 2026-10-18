#!/usr/bin/env python3
"""Short 'Balla con la volpe' v2: la volpe NUOVA con ~35 pose vere (pose_free.py) fuse col morph + corpo vivo.
Entra camminando (ciclo di 4 pose), saluta, insegna le mosse (mani in alto, batti le mani, salta in 3 fasi, giravolta con pose
di lato/schiena, coda), combo veloce, salto finale, ballo libero, saluta. Grande e al centro, niente sottotitoli.
    python3 short_balla2.py info | prep | test 1.0 | renderpart a b out.mp4 | render muto.mp4
"""
import json, math, os, subprocess, sys, wave
import numpy as np, cv2
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import morph as MO
from attori import Attore
from short_razzo import lerp, clamp, ease, back, text, star4, subscribe_button

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
    at("n1", 2.2); at("v1", 1.0); at("v2", 2.6); at("v3", 2.8); at("v4", 2.6); at("v5", 3.0); at("n2", 2.8); at("v6", 4.6); at("end", 2.2)
    return t + 3.0
DUR = _seq()
VOICES = [(k, V[k], "narr" if k.startswith("n") else "volpe", D[k]) for k in V]
E = lambda k: V[k] + D[k]

ENV = {}
for k, t0, who, d in VOICES:
    with wave.open(os.path.join(HERE, AUD, f"{k}.wav")) as wf:
        a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    win = 44100 // 60; n = len(a) // win + 1
    e = np.array([np.sqrt(np.mean(a[i * win:(i + 1) * win] ** 2) + 1e-12) for i in range(n)]); ENV[k] = e / (np.percentile(e, 95) + 1e-9)


def talk(t):
    for k, t0, who, d in VOICES:
        if who == "volpe" and t0 <= t <= t0 + d:
            e = ENV[k]; return min(1.0, e[min(len(e) - 1, int((t - t0) * 60))])
    return 0.0


# ------------------------------------------------------------------ coreografia
EV = []; JUMPS = []; XS = []          # XS: (t, x) posizione orizzontale
def P(t, pose, d=0.16): EV.append((t, pose, d))

# entrata camminando da sinistra (ciclo di 4 pose)
T_IN1 = 2.0
cyc = ["cammina1", "cammina3", "cammina2", "cammina4"]
i = 0; t = 0.0
while t < T_IN1: P(t, cyc[i % 4], 0.12); t += 0.16; i += 1
XS += [(0.0, -150.0), (T_IN1, 540.0)]
P(T_IN1, "neutro", 0.2); P(T_IN1 + 0.35, "saluta", 0.2); P(T_IN1 + 0.95, "saluta_m", 0.2); P(T_IN1 + 1.5, "saluta", 0.2)
P(V["n1"] + 2.6, "parla", 0.2); P(V["n1"] + 3.8, "abbraccia", 0.2); P(E("n1") + 0.3, "neutro", 0.2)
# mani in alto: su, con rimbalzi
t = V["v1"] - 0.15; P(t, "su", 0.16)
for k in range(4): JUMPS.append((t + 0.3 + k * BEAT, BEAT * 0.9, 45))
P(V["v2"] - 0.5, "neutro", 0.16)
# batti le mani: mani <-> abbraccia (aperte) a tempo
t = V["v2"] - 0.15; k = 0
while t < V["v3"] - 0.3: P(t, "mani" if k % 2 == 0 else "abbraccia", 0.12); t += BEAT / 2; k += 1
# salta, salta: accovacciato -> salto_su -> salto (a stella) -> atterra -> neutro
for j in range(2):
    t0 = V["v3"] - 0.1 + j * 1.25
    P(t0, "accovacciato", 0.12); P(t0 + 0.22, "salto_su", 0.1); P(t0 + 0.45, "salto", 0.12); P(t0 + 0.8, "atterra", 0.12); P(t0 + 1.05, "neutro", 0.14)
    JUMPS.append((t0 + 0.22, 0.75, 360))
# gira, gira: tre_quarti -> lato -> gira (schiena) -> lato_sx -> tre_quarti_sx -> neutro (giravolta vera)
for j in range(2):
    t0 = V["v4"] - 0.1 + j * 1.3
    for q, pz in enumerate(["tre_quarti", "lato", "gira", "lato_sx", "tre_quarti_sx", "neutro"]): P(t0 + q * 0.2, pz, 0.1)
    JUMPS.append((t0 + 0.1, 1.1, 60))
# muovi la coda: di schiena, ondeggia (la coda si vede)
P(V["v5"] - 0.15, "gira", 0.14); P(E("v5") + 1.6, "tre_quarti", 0.14); P(E("v5") + 1.9, "neutro", 0.14)
T_CODA0, T_CODA1 = V["v5"] - 0.05, E("v5") + 1.6
# n2: ride, poi combo veloce
P(V["n2"] + 0.2, "ride", 0.16); P(V["n2"] + 1.8, "occhi_chiusi", 0.16); P(E("n2") - 0.1, "neutro", 0.14)
t = E("n2") + 0.15
for pz in ["su", "neutro", "mani", "abbraccia", "mani", "accovacciato", "salto", "atterra", "lato", "gira", "lato_sx", "neutro"]:
    P(t, pz, 0.1); t += 0.33
JUMPS.append((E("n2") + 0.15 + 6 * 0.33 - 0.05, 0.62, 260))
# evviva: grande salto
P(V["v6"] - 0.45, "accovacciato", 0.12); P(V["v6"] - 0.2, "salto_su", 0.1); P(V["v6"] + 0.15, "salto", 0.12); P(V["v6"] + 1.0, "atterra", 0.12)
JUMPS.append((V["v6"] - 0.2, 1.15, 520))
# ballo libero
t = V["v6"] + 1.25; k = 0
while t < V["end"] - 0.2: P(t, ["balla", "balla2", "balla_m", "su"][k % 4], 0.14); t += BEAT; k += 1
# saluto finale
t = V["end"] - 0.1; k = 0
while t < DUR + 1: P(t, "saluta" if k % 2 == 0 else "saluta_m", 0.18); t += 0.6; k += 1
P(DUR - 1.4, "inchino", 0.2)

FOX = Attore("volpe", EV, JUMPS, talk, height=1020)


def fox_x(t):
    if t <= XS[0][0]: return XS[0][1]
    if t >= XS[-1][0]: return XS[-1][1]
    (t0, x0), (t1, x1) = XS[0], XS[1]; return lerp(x0, x1, (t - t0) / (t1 - t0))


# ------------------------------------------------------------------ scena
GROUND = 1800.0
_bg = None
def bg():
    global _bg
    if _bg is None: _bg = Image.open(os.path.join(HERE, "assets", "amb", "radura_festa.png")).convert("RGB").resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.6))
    return _bg


def confetti(d, t, t0, n=120, dur=3.2, seed=4):
    if not (t0 <= t < t0 + dur): return
    rng = np.random.default_rng(seed); u = t - t0
    cols = [(255, 80, 120), (80, 180, 255), (255, 220, 60), (120, 230, 120), (200, 120, 255), (255, 150, 60)]
    for k in range(n):
        x0 = rng.uniform(0, W); vx = rng.uniform(-200, 200); vy = rng.uniform(-1700, -900)
        x = x0 + vx * u + 40 * math.sin(u * 5 + k); y = H + 50 + vy * u + 900 * u * u
        if y > H + 60: continue
        s = rng.uniform(9, 17); ang = u * rng.uniform(4, 10) + k; fl = abs(math.cos(u * 7 + k)); ca, sa = math.cos(ang), math.sin(ang)
        d.polygon([(x + dx * s * ca - dy * s * 0.5 * fl * sa, y + dx * s * sa + dy * s * 0.5 * fl * ca) for dx, dy in ((-1, -1), (1, -1), (1, 1), (-1, 1))], fill=cols[k % 6] + (255,))


def frame(i):
    t = i / FPS
    img = bg().copy()
    z = 1.0 + 0.025 * (0.5 - 0.5 * math.cos(2 * math.pi * t / (4 * BEAT)))
    w2, h2 = int(W / z), int(H / z); img = img.crop(((W - w2) // 2, (H - h2) // 2 + 40, (W - w2) // 2 + w2, (H - h2) // 2 + 40 + h2)).resize((W, H), Image.BICUBIC)
    d = ImageDraw.Draw(img, "RGBA")
    glow = Image.new("RGB", (W, H), (0, 0, 0)); gd = ImageDraw.Draw(glow)
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
    pulse = 0.5 + 0.5 * math.cos(2 * math.pi * t / BEAT)
    for rr, lv in ((420, 0.18), (300, 0.3), (180, 0.4)):
        gd.ellipse([W / 2 - rr, GROUND - rr * 0.22, W / 2 + rr, GROUND + rr * 0.22], fill=(int(120 * lv * (0.6 + 0.4 * pulse)), int(90 * lv * (0.6 + 0.4 * pulse)), int(40 * lv)))
    x = fox_x(t)
    rot = 7 * math.sin(t * 7) if T_CODA0 <= t < T_CODA1 else 0.0
    extra = 14 * abs(math.sin(math.pi * t / BEAT)) if (V["v6"] + 1.25 <= t < V["end"]) else (6 * abs(math.sin(math.pi * t / BEAT)) if t > 2.0 else 0.0)
    FOX.draw(img, t, x, GROUND, 1.0, rot=rot, extra_hop=extra)
    if T_CODA0 <= t < T_CODA1:                                                   # 'swish' della coda
        for j in range(3):
            a = math.sin(t * 7) * 0.8 + j * 0.25; r = 230 + 30 * j
            gd.arc([x - r, GROUND - 520 - r * 0.5, x + r, GROUND - 520 + r * 0.5], 140 + 30 * math.sin(t * 7), 200 + 30 * math.sin(t * 7), fill=(70, 60, 30), width=6)
    confetti(d, t, V["v6"] + 0.3, n=140)
    confetti(d, t, V["end"] + 0.6, n=90, seed=9)
    img = ImageChops.add(ImageChops.add(img, glow), glow.filter(ImageFilter.GaussianBlur(10)))
    a = np.asarray(img).astype(np.float32)
    a = a + np.random.default_rng(i).normal(0, 2.0, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(img, "RGBA")
    if t < 2.4:
        u = back(t / 0.35); al_ = int(255 * clamp((2.4 - t) / 0.4))
        text(d, "BALLA CON ME!", W / 2, 200 - 10 * math.sin(t * 6), int(108 * clamp(max(0.6, u), 0, 1.0)), (255, 235, 90, al_), (200, 40, 110, al_), 13)
    subscribe_button(img, t, V["end"] + 0.9, cy=1840)
    return img.tobytes()


def _prep(p):
    try: MO.transition(*p); return None
    except Exception as e: return (p, str(e)[:80])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "info":
        print("DUR", round(DUR, 2)); print({k: round(v, 2) for k, v in V.items()}); print(sorted({e[1] for e in EV}))
    elif cmd == "prep":
        ps = sorted(FOX.pairs()); print(len(ps), "transizioni")
        with Pool(4) as pool:
            for r in pool.imap_unordered(_prep, ps):
                if r: print("manca", r)
    elif cmd == "test":
        for ts in sys.argv[2:]: Image.frombytes("RGB", (W, H), frame(int(round(float(ts) * FPS)))).save(f"/tmp/claude-0/prova/test_b2_{ts}.png")
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
