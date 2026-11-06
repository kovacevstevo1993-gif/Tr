"""sync.json + fine_blocchi.txt dalla voce dei blocchi (voce/bN.wav): parole del copione con i tempi misurati (small.en), fotogrammi = ceil(durata*30).
Blocchi senza voce: segnaposto 15 s (si rifa' quando c'e' la voce)."""
import sys, os, json, math, subprocess, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../modello-unico'))
from sync_voce import align, norm
import numpy as np
from faster_whisper import WhisperModel
J = json.load(open('code/blk.json'))['B']; M = WhisperModel('small.en', device='cpu', compute_type='int8')
old = json.load(open('sync.json'))['blocks'] if os.path.exists('sync.json') else {}
res = {'blocks': {}}; t0 = 0.0; fins = []; tot = 0
for b in range(1, 21):
    f = f'voce/b{b}.wav'
    if os.path.exists(f):
        raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
        dur = len(raw) / 4 / 16000; fr = math.ceil(dur * 30)
        key = f'{b}:{os.path.getmtime(f)}'
        if old.get(str(b), {}).get('key') == key: rel = old[str(b)]['rel']
        else:
            segs, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en')
            asr = [(norm(w.word), w.start, w.end) for s in segs for w in s.words if norm(w.word)]
            words, cov = align({b: J[str(b)]}, asr); rel = words[b]; print('b', b, 'copertura', round(cov, 2), flush=True)
    else: fr = 450; rel = [[w, 0.5 * i, 0.5 * i + 0.4] for i, w in enumerate(J[str(b)].split())]; key = None
    st = tot / 30; tot += fr; fins.append(tot)
    res['blocks'][str(b)] = {'start': round(st, 3), 'end': round(tot / 30, 3), 'key': key, 'rel': rel,
                             'words': [[w, round(st + a, 3), round(st + e, 3)] for w, a, e in rel]}
json.dump(res, open('sync.json', 'w'), indent=0); open('fine_blocchi.txt', 'w').write('\n'.join(map(str, fins)) + '\n')
print('fine', tot, round(tot / 30, 1), 's')
