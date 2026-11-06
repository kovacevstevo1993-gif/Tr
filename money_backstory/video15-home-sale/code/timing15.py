"""Controllo tempi: per ogni slide, istante di comparsa di ogni elemento (s) rispetto alla durata e all'80%. Segnala elementi oltre l'80% o cue fuori slide."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v15
from v15 import *
import v8b1
bad = 0
for b in [x for x in sorted(SLIDES) if x >= 19]:
    off = 0
    for i, (fn, f) in enumerate(zip(SLIDES[b], SPEC[b]), 1):
        CUE['blk'] = b; CUE['t0'] = off / 30; off += f; CUR['D'] = f / 30
        els = getattr(fn, 'els', None)
        if not els: continue
        ts = el_times(els); D = f / 30
        line = ' '.join(f"{t:.1f}" for t in ts)
        flag = ''
        if ts[-1] > 0.8 * D + 0.01: flag += ' ULTIMO>80%'
        if any(e['cue'] and (V.at(b, e['cue']) - CUE['t0'] > D + 0.2 or V.at(b, e['cue']) - CUE['t0'] < -0.3) for e in els): flag += ' CUE_FUORI_SLIDE'
        allt = sorted(ts + [tp for _, tp in pulse_sched(els, ts, LASTP())] + [LASTP()]); gaps = [round(y - x, 1) for x, y in zip(allt, allt[1:])]
        if gaps and max(gaps) > 3.4: flag += ' BUCO>3.4s(%s)' % max(gaps)
        if flag: bad += 1
        print(f"{b}.{i} D={D:.1f}s 80%={0.8*D:.1f} el: {line}{flag}")
print('segnalate', bad)
