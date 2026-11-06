"""Correzione LOCALE e GRATIS della voce (regola 30/10): per ogni blocco ffmpeg rubberband: velocita' verso 145 parole/min e altezza verso la mediana (cap +-6%).
Parte sempre da voce/orig/bN.wav. Uso (dalla cartella del video): python3 code/fixvoce.py 1-15  (stampa i fattori)"""
import sys, json, subprocess, numpy as np
J = json.load(open('code/blk.json'))['B']
a, b = [int(x) for x in sys.argv[1].split('-')]
def load(p):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)
def f0(x, sr=16000):
    o = []
    for i in range(0, len(x) - 1024, 800):
        s = x[i:i + 1024]
        if np.sqrt((s ** 2).mean()) < 0.02: continue
        s = s - s.mean(); c = np.correlate(s, s, 'full')[1023:]; lo, hi = int(sr / 300), int(sr / 70); k = np.argmax(c[lo:hi]) + lo
        if c[k] > 0.4 * c[0]: o.append(sr / k)
    return float(np.median(o))
TW, TF = 145.0, float(sys.argv[2]) if len(sys.argv) > 2 else 118.0
for n in range(a, b + 1):
    x = load(f'voce/orig/b{n}.wav'); w = len(J[str(n)].split()) / (len(x) / 16000) * 60; f = f0(x)
    tempo = w / TW          # >1 = piu' veloce del target: rallenta (durata aumenta di 1/tempo ... rubberband tempo<1 = piu' lento)
    pitch = max(0.94, min(1.06, TF / f))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'voce/orig/b{n}.wav', '-af', f'rubberband=tempo={TW / w:.4f}:pitch={pitch:.4f}:formant=preserved', f'voce/b{n}.wav'], check=True)
    print(n, 'wpm', round(w), '->145  Hz', round(f), 'x', round(pitch, 3))
