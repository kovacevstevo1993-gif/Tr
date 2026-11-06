"""Voce dei blocchi a gruppi (meno richieste a Google): una richiesta per gruppo, poi taglio ai confini dei blocchi
nel silenzio tra l'ultima parola di un blocco e la prima del successivo (coda >= 0,35 s). Modello gemini-2.5-flash-preview-tts, Fenrir."""
import json, sys, os, subprocess, re, difflib
import numpy as np
S = sys.argv[1]; J = json.load(open(sys.argv[2])); VOCE = sys.argv[3]
TTS = os.path.join(S, 'tts.py')
from faster_whisper import WhisperModel
M = WhisperModel('base.en', device='cpu', compute_type='int8')
def norm(w): return re.sub(r"[^a-z0-9]", '', w.lower())
for g in J['groups']:
    if all(os.path.exists(f'{VOCE}/b{b}.wav') for b in g): continue
    text = '\n\n'.join(J['B'][str(b)] for b in g)
    gw = f'{VOCE}/g{g[0]}.wav'
    if not os.path.exists(gw):
        subprocess.run(['python3', TTS, 'Fenrir', text, gw, os.environ.get('TTSM', 'gemini-2.5-flash-preview-tts')], check=True)
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', gw, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    segs, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en')
    asr = [(norm(w.word), w.start, w.end) for s in segs for w in s.words if norm(w.word)]
    cw = [(b, norm(w)) for b in g for w in J['B'][str(b)].split() if norm(w)]
    sm = difflib.SequenceMatcher(None, [w for _, w in cw], [w for w, _, _ in asr], autojunk=False)
    t = [None] * len(cw)
    for m in sm.get_matching_blocks():
        for k in range(m.size): t[m.a + k] = asr[m.b + k]
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', gw], capture_output=True, text=True).stdout)
    cuts = [0.0]
    for b0, b1 in zip(g, g[1:]):
        last = max(i for i, (b, _) in enumerate(cw) if b == b0); first = last + 1
        # ultima parola agganciata del blocco e prima agganciata del successivo
        le = next(t[i][2] for i in range(last, -1, -1) if t[i]); fs = next(t[i][1] for i in range(first, len(t)) if t[i])
        cuts.append(max(le + 0.35, (le + fs) / 2) if fs - le > 0.5 else (le + fs) / 2)
    cuts.append(dur)
    for b, a, e in zip(g, cuts, cuts[1:]):
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', gw, '-ss', f'{a:.3f}', '-to', f'{e:.3f}', f'{VOCE}/b{b}.wav'], check=True)
        print('b', b, round(e - a, 2), flush=True)
    print('copertura', round(sum(1 for x in t if x) / len(t), 3), flush=True)
