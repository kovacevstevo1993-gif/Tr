#!/usr/bin/env python3
"""Controllo del VIDEO FINITO prima di mandarlo. Uso: controllo_video.py video.mp4 cartella_voce [montaggio.jpg]
Verifica su TUTTI i fotogrammi: numero = durata voce, neri, fermi, salti forti fuori dalle giunzioni dei blocchi, scene povere (movimento minimo),
volume; e crea il montaggio di un fotogramma ogni 1,5 s da GUARDARE (testo tagliato, oggetti fuori schermo, scene vuote, sovrapposizioni)."""
import sys, glob, math, subprocess, io, numpy as np
from PIL import Image
v = sys.argv[1]; vd = sys.argv[2]; out = sys.argv[3] if len(sys.argv) > 3 else "montaggio.jpg"
dur = [float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout) for p in sorted(glob.glob(vd + "/b[0-9][0-9].mp3"))]
nb = [math.ceil(d * 30 - 1e-6) for d in dur]; J = list(np.cumsum(nb)[:-1])
raw = subprocess.run(["ffmpeg","-loglevel","error","-i",v,"-vf","scale=270:480","-pix_fmt","gray","-f","rawvideo","-"],capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 480, 270).astype(np.float32); n = len(fr)
m = fr.mean((1, 2)); d = np.abs(np.diff(fr, axis=0)).mean((1, 2)); err = []
if abs(n - sum(nb)) > 2: err.append(f"fotogrammi {n} invece di {sum(nb)} (durata voce)")
neri = [i for i in range(n) if m[i] < 6]
if neri: err.append(f"fotogrammi neri: {neri[:6]}")
fermi = [i for i in range(1, len(d)) if d[i] < 0.05 and i < n - 4]
if fermi: err.append(f"fotogrammi fermi (solo gli ultimi 4 del video possono): {fermi[:6]}")
salti = [i + 1 for i in range(6, len(d)) if d[i] > 20 and not any(abs(i + 1 - j) <= 1 for j in J)]
if salti: err.append(f"salti bruschi fuori dalle giunzioni: {salti[:8]}")
pov = sorted((float(d[i:i + 15].mean()), i) for i in range(0, len(d) - 15, 5))[:1]
if pov and pov[0][0] < 0.12: err.append(f"scena quasi ferma (movimento {pov[0][0]:.2f}) al fotogramma {pov[0][1]} = {pov[0][1]/30:.1f} s")
vol = subprocess.run(["ffmpeg","-hide_banner","-i",v,"-af","volumedetect","-vn","-f","null","-"],capture_output=True,text=True).stderr
mv = float(__import__("re").search(r"mean_volume: (-?[\d.]+)", vol).group(1)); pk = float(__import__("re").search(r"max_volume: (-?[\d.]+)", vol).group(1))
if not (-17 <= mv <= -12) or pk > -0.5: err.append(f"audio fuori standard: medio {mv} dB, picco {pk} dB (atteso -17..-12 e picco sotto -0,5)")
T = [0.05] + [round(x * 1.5, 2) for x in range(1, int(sum(dur) / 1.5))] + [round(sum(dur) - .1, 2)]
c = 9; rows = (len(T) + c - 1) // c; M = Image.new("RGB", (180 * c, 320 * rows))
for k, t in enumerate(T):
    g = subprocess.run(["ffmpeg","-loglevel","error","-ss",str(t),"-i",v,"-frames:v","1","-vf","scale=180:320","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
    M.paste(Image.open(io.BytesIO(g)).convert("RGB"), ((k % c) * 180, (k // c) * 320))
M.save(out, quality=80)
print(f"fotogrammi {n} (attesi {sum(nb)}), durata voce {sum(dur):.1f} s, audio {mv} dB picco {pk} dB, montaggio: {out} ({len(T)} fotogrammi)")
for e in err: print("ERRORE:", e)
print("PASSATO (poi GUARDARE il montaggio: testo tagliato, oggetti fuori schermo, scene vuote)" if not err else f"NON PASSATO: {len(err)} errori")
sys.exit(1 if err else 0)
