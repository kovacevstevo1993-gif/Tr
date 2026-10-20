import sys, v11, v11eng
from v11eng import *
for b in v11.SLIDES:
    off = 0
    for i, (fn, n) in enumerate(zip(v11.SLIDES[b], v11.SPEC[b]), 1):
        v11eng.CUE['blk'] = b; v11eng.CUE['t0'] = off / 30; v11eng.CUR['D'] = n / 30; off += n
        if not hasattr(fn, 'els'): continue
        ts = el_times(fn.els) + [LASTP()]; pts = [0.12] + ts
        g = max(b_ - a for a, b_ in zip(pts, pts[1:]))
        if g > 3.7: print(b, i, round(n / 30, 1), 's', fn.title, [round(x, 1) for x in ts], 'buco', round(g, 1))
