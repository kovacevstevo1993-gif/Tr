"""Secondo ascolto locale: riconoscimento vocale (medium.en, fallback small.en) di ogni blocco, confronto parola per parola col copione (numeri in parole). Stampa le differenze.
Il riconoscimento puo' sbagliare (es. 'growing' sentito 'crying'): ogni differenza va riguardata, non e' per forza un errore della voce."""
import sys, os, json, subprocess, difflib, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from numw import norm_words
from faster_whisper import WhisperModel
try: M = WhisperModel('medium.en', device='cpu', compute_type='int8'); nm = 'medium.en'
except Exception as e: M = WhisperModel('small.en', device='cpu', compute_type='int8'); nm = 'small.en'
print('modello', nm, flush=True)
J = json.load(open('code/blk.json'))['B']
for b in [int(x) for x in sys.argv[1].split(',')]:
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f'voce/b{b}.wav', '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    segs, _ = M.transcribe(np.frombuffer(raw, np.float32), language='en', beam_size=5); txt = ' '.join(s.text.strip() for s in segs)
    s = norm_words(J[str(b)]); g = norm_words(txt)
    sm = difflib.SequenceMatcher(None, s, g, autojunk=False); diffs = [(op, ' '.join(s[i1:i2]), ' '.join(g[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
    print(b, 'copione', len(s), 'ascoltate', len(g), 'differenze', len(diffs), flush=True)
    for d in diffs: print('   ', d, flush=True)
