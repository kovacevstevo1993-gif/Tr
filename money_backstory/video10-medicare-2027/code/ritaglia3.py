"""Taglio ai confini dei blocchi con le parole riconosciute (small.en): il confine e' la pausa dove la parola prima = ultima parola del blocco
e le parole dopo = prime parole del blocco seguente (numeri in cifre o in lettere accettati). Uso: ritaglia3.py blk.json gNN.wav a,b,c"""
import sys, re, json, subprocess, numpy as np
from faster_whisper import WhisperModel
J = json.load(open(sys.argv[1]))['B']; gw = sys.argv[2]; g = [int(x) for x in sys.argv[3].split(',')]
NUMW = set('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million percent first second third seventh'.split())
def n(w): w = re.sub(r"[^a-z0-9]", '', w.lower()); return {'no': 'number'}.get(w, w)
def isnum(w): return bool(re.search(r'\d', w)) or any(p in NUMW for p in w.split('-')) or w in NUMW
def eq(a, b): return a == b or (isnum(a) and isnum(b)) or (len(a) > 4 and a[:5] == b[:5])
raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', gw, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
dur = len(raw) / 4 / 16000
M = WhisperModel('small.en', device='cpu', compute_type='int8')
segs, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en')
ws = [(n(w.word), w.start, w.end) for s in segs for w in s.words if n(w.word)]
o = subprocess.run(['ffmpeg', '-i', gw, '-af', 'silencedetect=noise=-38dB:d=0.12', '-f', 'null', '-'], capture_output=True, text=True).stderr
SIL = list(zip([float(x) for x in re.findall(r'silence_start: ([\d.]+)', o)], [float(x) for x in re.findall(r'silence_end: ([\d.]+)', o)]))
cuts = [0.0]
for i in range(len(g) - 1):
    last = [n(x) for x in J[str(g[i])].split()][-1]; first = [n(x) for x in J[str(g[i + 1])].split()][:3]
    best = None
    for k in range(1, len(ws)):
        gap = ws[k][1] - ws[k - 1][2]
        if ws[k][1] <= cuts[-1] + 1: continue
        sc = 2 * eq(ws[k - 1][0], last) + sum(eq(ws[k + j][0], first[j]) for j in range(3) if k + j < len(ws)) + min(gap, 1.0)
        if best is None or sc > best[0]: best = (sc, ws[k - 1][2], ws[k][1], ws[k - 1][0], [w for w, _, _ in ws[k:k + 3]])
    sc, le, fs, lw, nx = best
    sil = [x for x in SIL if fs - 0.6 <= x[1] <= fs + 0.7]          # pausa vera prima della prima parola del blocco dopo
    if sil: le, fs = max(sil, key=lambda x: x[1] - x[0])
    cut = min(max(le + 0.35, (le + fs) / 2), fs - 0.05) if fs - le > 0.45 else (le + fs) / 2
    cuts.append(cut); print('confine', g[i], '->', g[i + 1], 'pausa', round(fs - le, 2), 'punteggio', round(sc, 2), '|', lw, '/', ' '.join(nx))
cuts.append(dur)
for b, a, e in zip(g, cuts, cuts[1:]):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', gw, '-ss', f'{a:.3f}', '-to', f'{e:.3f}', f'voce/b{b}.wav'], check=True)
