"""Controllo automatico di OGNI fotogramma di un blocco (solo primo piano, sfondo nero, senza polvere animata).
Uso: python3 check_frames.py <modulo> <blocco>
Controlla per ogni fotogramma: contenuto TAGLIATO dal bordo (margine <= 2 px) e margine minimo registrato e che gli ultimi 20 fotogrammi siano identici (niente ancora in animazione)."""
import sys, importlib, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
mod = importlib.import_module(sys.argv[1]); b = int(sys.argv[2])
from PIL import Image
import eng2
W, H = eng2.W, eng2.H
for _m in list(sys.modules.values()):
    if _m is not None and hasattr(_m, 'ambient') and getattr(_m, '__name__', '').startswith(('long3', 'eng2')):
        _m.ambient = lambda *a, **k: None
n = mod.DUR[b]
fn = mod.DRAW[b]
prev = None; bad = []; hist = []; minm = 9999
for i in range(n):
    img = Image.new("RGB", (W, H), (0, 0, 0))
    fn(img, i / 30)
    a = np.asarray(img)
    m = a.max(axis=2) > 10
    ys, xs = np.where(m)
    if len(xs):
        l, r, t_, bt = xs.min(), W - 1 - xs.max(), ys.min(), H - 1 - ys.max()
        mm = min(l, r, t_, bt)
        minm = min(minm, mm)
        if mm <= 2:
            bad.append((i, "TAGLIATO", int(l), int(r), int(t_), int(bt)))
    hist.append(a.copy() if i >= n - 21 else None)
    if i == n - 1: pass
last = hist[-1]
unsettled = None
for k in range(n - 21, n - 1):
    if not np.array_equal(hist[k], last):
        unsettled = k
print(f"blocco {b}: {n} fotogrammi controllati; fotogrammi con contenuto tagliato dal bordo: {len(bad)}; margine minimo {minm}px; ultimo movimento al fotogramma: {unsettled}")
for x in bad[:8]:
    print("  ", x)
