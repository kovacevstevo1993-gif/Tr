"""Per ogni slide: istante (s dall'inizio slide) in cui la voce dice la parola del PRIMO elemento e di ogni elemento, confrontato con l'istante in cui compare. Segnala elementi che compaiono piu' di 0.8 s PRIMA della parola o piu' di 1.5 s DOPO."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v16
from v16 import *
bad = 0
for b in [x for x in sorted(SLIDES) if x >= 1]:
    off = 0
    for i, (fn, f) in enumerate(zip(SLIDES[b], SPEC[b]), 1):
        CUE['blk'] = b; CUE['t0'] = off / 30; off += f; CUR['D'] = f / 30
        els = getattr(fn, 'els', None)
        if not els: continue
        ts = el_times(els)
        for e, t in zip(els, ts):
            if not e['cue']: continue
            w = V.at(b, e['cue']) - CUE['t0']
            if t < w - 1.5 or t > w + 1.5:
                bad += 1; print(f"{b}.{i} {e['kind']} cue '{e['cue']}': voce {w:.1f}s, compare {t:.1f}s")
print('segnalati', bad)
