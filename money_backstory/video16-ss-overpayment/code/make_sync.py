"""sync.json + fine_blocchi.txt dalla voce dei blocchi (voce/bN.wav): parole del copione con i tempi misurati (small.en), fotogrammi = ceil(durata*30).
Blocchi senza voce: segnaposto 15 s (si rifa' quando c'e' la voce)."""
import sys, os, json, math, subprocess, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../modello-unico')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sync_voce import align, norm
import numpy as np
from faster_whisper import WhisperModel
J = json.load(open('code/blk.json'))['B']; M = WhisperModel('small.en', device='cpu', compute_type='int8')
old = json.load(open('sync.json'))['blocks'] if os.path.exists('sync.json') else {}
res = {'blocks': {}}; t0 = 0.0; fins = []; tot = 0
for b in range(1, 18):
    f = f'voce/b{b}.wav'
    if os.path.exists(f):
        raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
        dur = len(raw) / 4 / 16000; fr = math.ceil(dur * 30)
        key = f'p2:{b}:{os.path.getmtime(f)}'
        if old.get(str(b), {}).get('key') == key: rel = old[str(b)]['rel']
        else:
            segs, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en', beam_size=5, initial_prompt=J[str(b)], condition_on_previous_text=False)
            from numw import norm_words, num2words
            def _year(m):
                n = int(m.group(0))
                if 1900 <= n <= 2099:
                    a, b = divmod(n, 100); return ' ' + num2words(a) + ' ' + (num2words(b) if b >= 10 else ('oh ' + num2words(b) if b else 'hundred')) + ' '
                return m.group(0)
            asr = []
            for s_ in segs:
                for w in s_.words:
                    if re.search(r'\d', w.word):
                        txt_ = re.sub(r'\b(?:19|20)\d\d\b(?![,.]\d)', _year, w.word)
                        ex = norm_words(txt_)
                        if ex:
                            dd = (w.end - w.start) / len(ex)
                            for i_, x in enumerate(ex): asr.append((norm(x), w.start + i_ * dd, w.start + (i_ + 1) * dd))
                    elif norm(w.word): asr.append((norm(w.word), w.start, w.end))
            words, cov = align({b: J[str(b)]}, asr)
            if cov < 0.85:   # il testo come prompt a volte fa saltare l'inizio: riprova senza prompt e tieni il migliore
                segs2, _ = M.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
                asr2 = []
                for s_ in segs2:
                    for w in s_.words:
                        if re.search(r'\d', w.word):
                            ex = norm_words(re.sub(r'\b(?:19|20)\d\d\b(?![,.]\d)', _year, w.word))
                            if ex:
                                dd = (w.end - w.start) / len(ex)
                                for i_, x in enumerate(ex): asr2.append((norm(x), w.start + i_ * dd, w.start + (i_ + 1) * dd))
                        elif norm(w.word): asr2.append((norm(w.word), w.start, w.end))
                w2, c2 = align({b: J[str(b)]}, asr2)
                if c2 > cov: words, cov = w2, c2
            rel = words[b]; print('b', b, 'copertura', round(cov, 2), flush=True)
    else: fr = 450; rel = [[w, 0.5 * i, 0.5 * i + 0.4] for i, w in enumerate(J[str(b)].split())]; key = None
    st = tot / 30; tot += fr; fins.append(tot)
    res['blocks'][str(b)] = {'start': round(st, 3), 'end': round(tot / 30, 3), 'key': key, 'rel': rel,
                             'words': [[w, round(st + a, 3), round(st + e, 3)] for w, a, e in rel]}
json.dump(res, open('sync.json', 'w'), indent=0); open('fine_blocchi.txt', 'w').write('\n'.join(map(str, fins)) + '\n')
print('fine', tot, round(tot / 30, 1), 's')
