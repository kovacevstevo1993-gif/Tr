import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v14m
from v14m import *
sel = set(sys.argv[1:])
for b in sorted(SLIDES):
    off = 0
    for i, (fn, f) in enumerate(zip(SLIDES[b], SPEC[b]), 1):
        t0 = off / 30; off += f
        if f'{b}.{i}' not in sel: continue
        ws = V.words(b); st = V.start(b)
        txt = ' '.join(w[0] for w in ws if t0 - 0.05 <= w[1] - st < t0 + (f / 30) * 0.8)
        print(f'{b}.{i} D={f/30:.1f}s:', txt[:420]); print()
