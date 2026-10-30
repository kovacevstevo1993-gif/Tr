"""CONTROLLO VOCE (30/10/2026) - da lanciare PRIMA delle slide, dopo ritaglia3. Uso (dalla cartella del video): python3 ../qa/qa_voce.py <N blocchi>
Per ogni voce/bN.wav: parole/minuto e altezza media (Hz). ERRORE se un blocco e' oltre +-8% di velocita' o +-12% di altezza dalla mediana del video: prima si corregge in locale e gratis con ffmpeg rubberband (tempo=145/wpm, pitch=mediana/Hz per blocco), poi si rilancia; si rigenera con Gemini solo cio' che resta fuori."""
import sys, json, subprocess, numpy as np
J = json.load(open('code/blk.json'))['B']; N = int(sys.argv[1]); R = []
def f0(a, sr=16000):
    o = []
    for i in range(0, len(a) - 1024, 800):
        x = a[i:i + 1024]
        if np.sqrt((x ** 2).mean()) < 0.02: continue
        x = x - x.mean(); c = np.correlate(x, x, 'full')[1023:]; lo, hi = int(sr / 300), int(sr / 70); k = np.argmax(c[lo:hi]) + lo
        if c[k] > 0.4 * c[0]: o.append(sr / k)
    return float(np.median(o))
for b in range(1, N + 1):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f'voce/b{b}.wav', '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32); R.append((b, len(J[str(b)].split()) / (len(a) / 16000) * 60, f0(a)))
mw = np.median([r[1] for r in R]); mf = np.median([r[2] for r in R]); bad = 0
for b, w, f in R:
    fl = ''
    if abs(w / mw - 1) > 0.08: fl += ' VELOCITA'
    if abs(f / mf - 1) > 0.12: fl += ' ALTEZZA'
    bad += bool(fl); print(b, round(w), 'wpm', round(f), 'Hz', fl)
print('mediana', round(mw), 'wpm', round(mf), 'Hz;', 'ERRORI:' if bad else 'OK', bad)
