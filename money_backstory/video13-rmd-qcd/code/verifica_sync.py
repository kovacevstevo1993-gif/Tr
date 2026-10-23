"""Confronta i tempi parola per parola di sync.json (agganciati dal riconoscimento, numeri interpolati) con un secondo allineamento che converte le cifre del riconoscimento in parole.
Segnala le parole degli indicatori (cue) con differenza > 0,25 s. Uso: python3 code/verifica_sync.py"""
import sys, os, json, re, subprocess, difflib, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, '../modello-unico')
from ascolta_gemini import num2words
from sync_voce import norm
from faster_whisper import WhisperModel
M = WhisperModel('small.en', device='cpu', compute_type='int8'); S = json.load(open('sync.json'))['blocks']; J = json.load(open('code/blk.json'))['B']
def expand(tok, a, e):
    t = tok.replace('%', ' percent'); t = re.sub(r'(\d),(\d)', r'\1\2', t); t = t.replace('$', ' ')
    out = []
    for p in t.split():
        for q in re.split(r'(\d+(?:\.\d+)?)', p):
            if not q: continue
            if re.fullmatch(r'\d+(?:\.\d+)?', q):
                try: out += num2words(float(q) if '.' in q else int(q)).split()
                except: out.append(q)
            else: out.append(q)
    out = [norm(w.replace('-', '')) for w in out if norm(w.replace('-', ''))]
    if not out: return []
    d = (e - a) / len(out); return [(w, a + i * d, a + (i + 1) * d) for i, w in enumerate(out)]
worst = {}
for b in range(1, 21):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f'voce/b{b}.wav', '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    segs, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en')
    asr = []
    for s in segs:
        for w in s.words: asr += expand(w.word.strip(), w.start, w.end)
    sw = [norm(w.replace('-', '')) for w in J[str(b)].split()]; ow = [norm(w[0]) for w in S[str(b)]['rel'] if isinstance(w, list)] if 'rel' in S[str(b)] else []
    old = S[str(b)]['rel']
    # le parole del copione con il trattino sono un token solo: spezzo come fa l'allineamento nuovo (confronto per indice di parola dello script)
    new_t = [None] * len(sw); sm = difflib.SequenceMatcher(None, [norm(w) for w in J[str(b)].split()], [w for w, _, _ in asr], autojunk=False)
    # allineamento "ricco": i token del copione con trattino vengono espansi come nel riconoscimento
    exp = []
    for i, w in enumerate(J[str(b)].split()):
        parts = [norm(p) for p in w.split('-') if norm(p)] or [norm(w)]
        exp.append(parts)
    flat = [(i, p) for i, parts in enumerate(exp) for p in parts]
    sm = difflib.SequenceMatcher(None, [p for _, p in flat], [w for w, _, _ in asr], autojunk=False); tt = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            i = flat[blk.a + k][0]; tt.setdefault(i, asr[blk.b + k][1])
    cov = len(tt) / len(sw); diffs = [(i, round(abs(tt[i] - old[i][1]), 2)) for i in tt if abs(tt[i] - old[i][1]) > 0.25]
    print(b, 'copertura nuova', round(cov, 2), 'parole con differenza >0.25 s:', len(diffs), [(J[str(b)].split()[i], d) for i, d in diffs[:12]], flush=True)
