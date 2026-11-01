#!/usr/bin/env python3
"""Controllo numerico di TUTTI i fotogrammi di un clip + montaggio di fotogrammi chiave. Uso: qa_clip.py clip.mp4 montaggio.jpg [tempi in s separati da virgola]"""
import sys, subprocess, numpy as np
from PIL import Image
mp4, out = sys.argv[1], sys.argv[2]
raw = subprocess.run(["ffmpeg","-loglevel","error","-i",mp4,"-vf","scale=270:480","-pix_fmt","gray","-f","rawvideo","-"],capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 480, 270).astype(np.float32); n = len(fr)
mean = fr.mean((1, 2)); diff = np.abs(np.diff(fr, axis=0)).mean((1, 2))
pr = lambda c: subprocess.run(["ffprobe","-v","error","-select_streams",c,"-show_entries","stream=duration","-of","csv=p=0",mp4],capture_output=True,text=True).stdout.strip()
print(f"fotogrammi {n} | durata video {pr('v:0')} s, audio {pr('a:0')} s")
print("neri (media<6):", [i for i in range(n) if mean[i] < 6][:10])
print("salti forti (>12):", [i + 1 for i in range(n - 1) if diff[i] > 12][:10], "| max salto", round(float(diff.max()), 2))
print("fermi (diff<0.02):", [i + 1 for i in range(n - 1) if diff[i] < 0.02][:20])
vol = subprocess.run(["ffmpeg","-i",mp4,"-af","volumedetect","-f","null","-"],capture_output=True,text=True).stderr
print([l.split("]")[1].strip() for l in vol.splitlines() if "mean_volume" in l or "max_volume" in l])
ts = [float(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [0.1, 1.0, 2.0, 3.6, 4.6, 5.4, 6.4, 7.4, 8.3, 9.0, 9.5, (n - 1) / 30]
W, H = 270, 480; cols = 6; rows = (len(ts) + cols - 1) // cols; M = Image.new("RGB", (W * cols, H * rows))
for k, t in enumerate(ts):
    i = min(n - 1, int(round(t * 30)))
    rgb = subprocess.run(["ffmpeg","-loglevel","error","-i",mp4,"-vf",f"select=eq(n\\,{i}),scale=270:480","-frames:v","1","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    M.paste(Image.frombytes("RGB", (W, H), rgb), ((k % cols) * W, (k // cols) * H))
M.save(out, quality=85); print("montaggio:", len(ts), "fotogrammi chiave")
