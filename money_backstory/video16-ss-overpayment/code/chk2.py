"""Secondo ascolto sui dubbi: modelli small.en/base.en/tiny.en su blocchi scelti. Uso: python3 code/chk2.py 1,3,13,14"""
import sys, json, re, difflib, numpy as np, subprocess
from faster_whisper import WhisperModel
J = json.load(open('code/blk.json'))['B']
def norm(s): return re.findall(r"[a-z0-9']+", s.lower().replace('-', ' '))
Ms = {m: WhisperModel(m, device='cpu', compute_type='int8') for m in ('small.en', 'base.en', 'tiny.en')}
for b in sys.argv[1].split(','):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f'voce/b{b}.wav', '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32); ref = norm(re.sub(r'\b([A-Z]) (?=[A-Z]\b)', r'\1', J[b]))
    for m, M in Ms.items():
        segs, _ = M.transcribe(a, language='en', beam_size=5, condition_on_previous_text=False); hyp = norm(' '.join(s.text.strip() for s in segs))
        d = [(op, ' '.join(ref[i1:i2]), ' '.join(hyp[j1:j2])) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes() if op != 'equal']
        print(b, m, d)
