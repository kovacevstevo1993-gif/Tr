"""Ritaglia un gruppo di voce nei blocchi: per ogni confine cerca la pausa piu' lunga vicino al punto atteso
(proporzione dei caratteri) dove la parola successiva e' la prima parola del blocco dopo. Uso: ritaglia.py blk.json g10.wav 10,11,12"""
import sys, re, json, subprocess
import numpy as np
from faster_whisper import WhisperModel
J = json.load(open(sys.argv[1]))['B']; gw = sys.argv[2]; g = [int(x) for x in sys.argv[3].split(',')]
def norm(w): return re.sub(r"[^a-z0-9]", '', w.lower())
NUM = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'}
raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', gw, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
dur = len(raw) / 4 / 16000
M = WhisperModel('base.en', device='cpu', compute_type='int8')
segs, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en')
ws = [(norm(w.word), w.start, w.end) for s in segs for w in s.words if norm(w.word)]
L = [len(J[str(b)]) for b in g]; tot = sum(L); cuts = [0.0]; acc = 0
for i in range(len(g) - 1):
    acc += L[i]; est = ws[0][1] + (ws[-1][2] - ws[0][1]) * acc / tot
    fw = norm(J[str(g[i + 1])].split()[0]); fw2 = NUM.get(fw, fw)
    best = None
    for k in range(1, len(ws)):
        gap = ws[k][1] - ws[k - 1][2]; dist = abs(ws[k][1] - est)
        if dist > 4.0: continue
        score = gap - 0.05 * dist + (1.0 if ws[k][0] in (fw, fw2) else 0)
        if best is None or score > best[0]: best = (score, ws[k - 1][2], ws[k][1], ws[k][0])
    le, fs = best[1], best[2]; cut = min(max(le + 0.35, (le + fs) / 2), fs - 0.05) if fs - le > 0.45 else (le + fs) / 2
    cuts.append(cut); print('confine', g[i], '->', g[i + 1], 'pausa', round(fs - le, 2), 'parola dopo:', best[3])
cuts.append(dur)
for b, a, e in zip(g, cuts, cuts[1:]):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', gw, '-ss', f'{a:.3f}', '-to', f'{e:.3f}', f'voce/b{b}.wav'], check=True)
