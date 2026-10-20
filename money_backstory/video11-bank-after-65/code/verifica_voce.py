"""Controllo voce: trascrive ogni blocco e confronta con il copione (prime/ultime parole, parole mancanti)."""
import sys, re, json, subprocess, difflib
import numpy as np
from faster_whisper import WhisperModel
J = json.load(open(sys.argv[1]))['B']; M = WhisperModel('base.en', device='cpu', compute_type='int8')
def norm(w): return re.sub(r"[^a-z]", '', w.lower())
for b in map(int, sys.argv[2].split(',')):
    f = f'voce/b{b}.wav'
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    segs, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en')
    ws = [w for s in segs for w in s.words]; got = ' '.join(w.word.strip() for w in ws)
    dur = len(raw) / 4 / 16000; tail = dur - ws[-1].end
    a = [norm(x) for x in J[str(b)].split() if norm(x)]; g = [norm(x) for x in got.split() if norm(x)]
    r = difflib.SequenceMatcher(None, a, g).ratio()
    print(f'b{b} {dur:.2f}s coda {tail:.2f}s somiglianza {r:.2f} | {" ".join(got.split()[:5])} ... {" ".join(got.split()[-5:])}', flush=True)
