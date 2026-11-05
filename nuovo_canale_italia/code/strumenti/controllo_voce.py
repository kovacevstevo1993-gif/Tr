#!/usr/bin/env python3
"""Controllo della VOCE PRIMA delle scene. Uso: controllo_voce.py cartella_voce  (legge b*.mp3)
Misura l'altezza media (Hz) di ogni blocco e il volume: se la differenza tra blocchi supera 6 Hz o 2 dB = voce diversa tra i blocchi = ERRORE."""
import sys, glob, subprocess, numpy as np
def f0(p):
    raw = subprocess.run(["ffmpeg","-loglevel","error","-i",p,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; fr = 640; v = []
    for i in range(0, len(x) - fr, 320):
        s = x[i:i + fr]
        if np.sqrt((s ** 2).mean()) < 0.02: continue
        s = s - s.mean(); ac = np.correlate(s, s, "full")[fr - 1:]; lo, hi = 53, 228; k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] / ac[0] > .4: v.append(16000 / k)
    return float(np.median(v)), 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-9)
R = {p.split("/")[-1][:-4]: f0(p) for p in sorted(glob.glob(sys.argv[1] + "/b[0-9][0-9].mp3"))}
for k, (h, db) in R.items(): print(f"{k}: altezza {h:.0f} Hz, volume {db:.1f} dB")
H = [h for h, _ in R.values()]; D = [d for _, d in R.values()]
ok = max(H) - min(H) <= 6 and max(D) - min(D) <= 2
print("PASSATO" if ok else f"ERRORE: voce diversa tra i blocchi (altezza {max(H)-min(H):.0f} Hz, volume {max(D)-min(D):.1f} dB): rifare la voce in UNA richiesta")
sys.exit(0 if ok else 1)
