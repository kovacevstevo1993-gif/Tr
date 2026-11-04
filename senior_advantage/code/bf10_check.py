"""Controllo di OGNI fotogramma di un blocco (solo primo piano su nero): contenuto tagliato dal bordo, ultimi 20 fotogrammi identici, tempi di comparsa <= 80%.
Uso: python3 bf10_check.py <blocco>"""
import os, sys
os.environ.setdefault("SA_W", "1920"); os.environ.setdefault("SA_H", "1080")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image
import bf10_all as A
import bf10_kit as K
b = int(sys.argv[1])
n = K.DUR[b]
# tempi di comparsa
rec = []
mods = [m for m in (sys.modules.get("bf10_b01_10"), sys.modules.get("bf10_b11_20")) if m]
def wrap(f, idx):
    def g(*a, **k):
        try:
            rec.append((float(a[idx]), getattr(f, "__name__", "?")))
        except Exception:
            pass
        return f(*a, **k)
    return g
for m in mods:
    for nm, idx in (("show", 2), ("grow_bar", 2), ("dial_show", 2), ("source10", 2), ("ap", 2)):
        if hasattr(m, nm):
            setattr(m, nm, wrap(getattr(m, nm), idx))
img = Image.new("RGB", (K.W, K.H), (0, 0, 0))
A.DRAW[b](img, n / 30 - 0.05)
late = sorted(set(round(x, 2) for x, nm in rec if x > n / 30 * 0.8 + 0.02))
print(f"blocco {b}: durata {n} f = {n/30:.2f} s; ultimo elemento compare a {max(x for x,_ in rec):.2f} s (80% = {n/30*0.8:.2f} s); oltre l'80%: {late}")
if len(sys.argv) > 2 and sys.argv[2] == 'timing':
    sys.exit()
# fotogrammi
for m in mods:
    pass
bad = []; minm = 9999; hist = {}
for i in range(n):
    im = Image.new("RGB", (K.W, K.H), (0, 0, 0))
    A.DRAW[b](im, i / 30)
    a = np.asarray(im)
    mk_ = a.max(axis=2) > 10
    ys, xs = np.where(mk_)
    if len(xs):
        l, r, t_, bt = xs.min(), K.W - 1 - xs.max(), ys.min(), K.H - 1 - ys.max()
        mm = min(l, r, t_, bt); minm = min(minm, mm)
        if mm <= 2: bad.append(i)
    if i >= n - 21: hist[i] = a.copy()
last = hist[n - 1]
uns = None
for k in range(n - 21, n - 1):
    if not np.array_equal(hist[k], last): uns = k
print(f"  fotogrammi controllati {n}; tagliati dal bordo: {len(bad)}; margine minimo {minm}px; ultimo movimento al fotogramma: {uns} (ultimi 20 = {n-20}..{n-1})")
