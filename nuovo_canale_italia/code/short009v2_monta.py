#!/usr/bin/env python3
"""Short 009 - monta un blocco: render fotogrammi (4 processi), audio (voce + effetti + musica), mp4.
Uso: short009v2_monta.py N   (N = numero blocco; pagina code/short009_bloccoN.html, voce short009_v2/voce/bNN.mp3)"""
import sys, os, json, subprocess, shutil, numpy as np
N = int(sys.argv[1]); HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SC = "/tmp/claude-0/-home-user-Tr/b8b99809-dfef-5405-923e-22f69e8e39e7/scratchpad"
FR = f"{SC}/frames{N}"; OUT = f"{ROOT}/short009_v2/clip"; os.makedirs(OUT, exist_ok=True)
voce = f"{ROOT}/short009_v2/voce/b{N:02d}.mp3"
dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",voce],capture_output=True,text=True).stdout)
nf = int(np.ceil(dur * 30 - 1e-6)); SR = 48000
# ---- 1) fotogrammi ----
SKIP = os.environ.get("SKIP_RENDER") and os.path.isdir(FR) and len([f for f in os.listdir(FR) if f.endswith(".png")]) == nf
if not SKIP:
    if os.path.isdir(FR) and not os.environ.get('RESUME'): shutil.rmtree(FR)
    os.makedirs(FR, exist_ok=True)
ps = []; step = (nf + 3) // 4
for k in range(4):
    a, b = k * step, min(nf - 1, (k + 1) * step - 1)
    h3 = f"{HERE}/s009v2_b{N}_3d.html"
    if a <= b and not SKIP: ps.append(subprocess.Popen(["node", f"{HERE}/render_3d.js", h3, FR, str(a), str(b)], stdout=subprocess.PIPE, text=True) if os.path.exists(h3) else subprocess.Popen(["node", f"{HERE}/render_short.js", f"{HERE}/short009_blocco{N}.html", FR, str(a), str(b)], stdout=subprocess.PIPE, text=True))
for p in ps: print(p.communicate()[0].strip())
nfile = len([f for f in os.listdir(FR) if f.endswith(".png")]); print("fotogrammi resi:", nfile, "attesi", nf)
# ---- 2) audio ----
def noise(n, seed): return np.random.RandomState(seed).uniform(-1, 1, n)
def env(n, a, r): x = np.arange(n) / SR; return np.minimum(1, x / max(a, 1e-4)) * np.exp(-x / r)
def tone(f, d, a=0.007, r=0.08, f2=None):
    n = int(d * SR); x = np.arange(n) / SR; fr = f if f2 is None else f + (f2 - f) * x / d
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * env(n, a, r)
def lp(x, k): c = np.ones(k) / k; return np.convolve(x, c, "same")
def whoosh(d=0.4): n = int(d * SR); x = noise(n, 1); y = lp(x, 40) - lp(x, 400); return y / np.abs(y).max() * np.sin(np.pi * np.arange(n) / n) ** 2
def riser(d): n = int(d * SR); x = noise(n, 2); y = (lp(x, 8) - lp(x, 200)); return y / np.abs(y).max() * (np.arange(n) / n) ** 2
def pen(d): n = int(d * SR); x = noise(n, 3); y = x - lp(x, 12); m = (np.sin(np.arange(n) / SR * 2 * np.pi * 22) > 0) * 1.0; return y * m * 0.6
def put(buf, t, snd, g=1.0):
    i = int(t * SR); j = min(len(buf), i + len(snd))
    if i < len(buf): buf[i:j] += snd[:j - i] * g
EV = json.load(open(f"{HERE}/short009v2_sfx_b{N}.json"))
L = int(nf / 30 * SR); sfx = np.zeros(L)
for t, kind, g in EV:
    if kind == "pop": put(sfx, t, tone(700, .12, .002, .035, 260), g)
    elif kind == "tick": put(sfx, t, tone(2200, .03, .001, .007), g)
    elif kind == "coin":
        a_ = tone(2900, .1, .001, .03); b_ = tone(4300, .08, .001, .02); a_[:len(b_)] += .5 * b_; put(sfx, t, a_, g)
    elif kind == "ding": put(sfx, t, tone(1318, .6, .003, .16), g)
    elif kind == "thud": put(sfx, t, tone(70, .5, .003, .11, 38), g)
    elif kind == "whoosh": put(sfx, t, whoosh(.4), g)
    elif kind.startswith("riser"): put(sfx, t, riser(float(kind[5:])), g)
    elif kind == "glitch": put(sfx, t, noise(int(.09 * SR), 4) * env(int(.09 * SR), .001, .03), g)
    elif kind.startswith("pen"): put(sfx, t, pen(float(kind[3:])), g)
x = np.arange(L) / SR
music = (np.sin(2*np.pi*55*x) + .6*np.sin(2*np.pi*82.41*x) + .35*np.sin(2*np.pi*110*x + .7)) * (0.7 + 0.3*np.sin(2*np.pi*0.18*x))
music *= np.minimum(1, x / 0.8) * np.minimum(1, (L / SR - x) / 0.5)
raw = subprocess.run(["ffmpeg","-loglevel","error","-i",voce,"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True).stdout
v = np.frombuffer(raw, np.float32); vv = np.zeros(L); vv[:min(L, len(v))] = v[:L]
vv /= max(np.abs(vv).max(), 1e-6)
mix = vv * 0.80 + sfx * 0.30 + music * 0.045
mix = np.clip(mix, -1, 1).astype(np.float32); open(f"{SC}/mix{N}.f32", "wb").write(mix.tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i",f"{SC}/mix{N}.f32","-af","loudnorm=I=-14:TP=-1.5:LRA=11",f"{SC}/mix{N}.wav"],check=True)
# ---- 3) mp4 ----
mp4 = f"{OUT}/S009v2-blocco{N:02d}.mp4"
subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","30","-i",f"{FR}/%05d.png","-i",f"{SC}/mix{N}.wav",
  "-c:v","libx264","-preset","slow","-crf","16","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-ar","48000","-t",f"{nf/30:.4f}","-movflags","+faststart",mp4],check=True)
print("mp4:", mp4, os.path.getsize(mp4) // 1024, "KB", "durata attesa", round(nf / 30, 3), "s,", nf, "fotogrammi")
