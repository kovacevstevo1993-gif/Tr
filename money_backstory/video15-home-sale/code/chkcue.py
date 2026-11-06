"""Controlla che ogni frase-cue (elementi e tagli) esista nella voce del suo blocco."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v15
from v15 import *
bad = 0
for b in sorted(SLIDES):
    for i, fn in enumerate(SLIDES[b], 1):
        for e in (getattr(fn, 'els', None) or []):
            if e['cue']:
                try: V.at(b, e['cue'])
                except KeyError: bad += 1; print('CUE MANCANTE', b, i, repr(e['cue']))
print('cue mancanti', bad)
