#!/usr/bin/env python3
"""Controllo numerico di TUTTI i fotogrammi (a 160x90, veloce) + un solo montaggio di fotogrammi chiave.
Uso: controllo_video.py cartella_pratica  -> stampa esito, salva _tmp/montaggio.jpg"""
import sys, os, json, subprocess, numpy as np
from PIL import Image, ImageDraw
PR = os.path.abspath(sys.argv[1]); v = os.path.join(PR, "video.mp4"); T = json.load(open(os.path.join(PR, "tempi.json")))
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", v, "-vf", "scale=160:90", "-pix_fmt", "gray", "-f", "rawvideo", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(np.float32); n = len(fr)
mean = fr.mean((1, 2)); diff = np.abs(np.diff(fr, axis=0)).mean((1, 2))
neri = [i for i in range(n) if mean[i] < 6 and i > 20]; fermi = [i for i in range(1, n) if diff[i - 1] < 0.02]
salti = [i + 1 for i in range(n - 1) if diff[i] > 25]; starts = [int(s[0] * 30) for s in T["scene"]]
fuori = [i for i in salti if min(abs(i - s) for s in starts) > 2]
print(f"fotogrammi {n} attesi {T['frames']}:", "OK" if abs(n - T["frames"]) <= 1 else "DIVERSI")
print("neri:", neri[:10], "| congelati:", len(fermi), fermi[:10], "| salti fuori dai cambi scena:", fuori[:10])
mini = os.path.join(PR, "_tmp", "mini"); sel = []
for s_ in T["scene"]:
    a = int(s_[0] * 30) + 14; sel.append(round(a / 15) * 15)
cols = 8; tw, th = 360, 203; rows = (len(sel) + cols - 1) // cols; M = Image.new("RGB", (cols * tw, rows * th))
for k, i in enumerate(sel):
    f = os.path.join(mini, f"{min(i, (n - 1) // 15 * 15):05d}.jpg")
    M.paste(Image.open(f).convert("RGB").resize((tw, th)), ((k % cols) * tw, (k // cols) * th))
M.save(os.path.join(PR, "_tmp", "montaggio.jpg"), quality=78); print("montaggio:", len(sel), "fotogrammi chiave")
