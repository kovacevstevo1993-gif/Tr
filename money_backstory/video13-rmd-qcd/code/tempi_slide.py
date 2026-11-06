"""Stampa in JSON, per ogni slide, i fotogrammi e il momento di comparsa di ogni elemento (con il sync scelto da SYNCJSON). Serve a confrontare due allineamenti."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('OUT', '/tmp/claude-0/x/')
import v13
from v13 import *
out = {}
for b in sorted(SLIDES):
    off = 0; L = []
    for i, (fn, f) in enumerate(zip(SLIDES[b], SPEC[b]), 1):
        CUE['blk'] = b; CUE['t0'] = off / 30; off += f; CUR['D'] = f / 30
        els = getattr(fn, 'els', None); L.append({'f': f, 't': [round(t, 2) for t in el_times(els)] if els else []})
    out[b] = L
json.dump(out, open(sys.argv[1], 'w'))
