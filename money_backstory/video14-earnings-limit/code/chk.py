"""Controllo voce: trascrive ogni blocco con medium.en e large-v3 e confronta col copione (numeri in parole -> cifre ignorate: si confronta solo il testo lettera per lettera dopo normalizzazione). Stampa la trascrizione intera e le differenze. Uso: chk.py 1,2,3"""
import sys, json, re, difflib, numpy as np, subprocess
from faster_whisper import WhisperModel
J = json.load(open('code/blk.json'))['B']
def norm(s): return re.findall(r"[a-z0-9']+", s.lower().replace('-', ' '))
Ms = {m: WhisperModel(m, device='cpu', compute_type='int8') for m in ('medium.en', 'large-v3')}
for b in sys.argv[1].split(','):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f'voce/b{b}.wav', '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32); ref = norm(re.sub(r'\b([A-Z]) (?=[A-Z]\b)', r'\1', J[b]))
    for m, M in Ms.items():
        segs, _ = M.transcribe(a, language='en', beam_size=5, condition_on_previous_text=False)
        txt = ' '.join(s.text.strip() for s in segs); hyp = norm(txt)
        print(f'--- b{b} {m}: {txt}')
        sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal': print('   DIFF', op, 'copione:', ' '.join(ref[i1:i2]), '| sentito:', ' '.join(hyp[j1:j2]))
    sys.stdout.flush()
