"""Controllo di OGNI fotogramma dello short 13 (con zoom come nel video finale): contenuto tagliato dal bordo (margine <=2 px)
e ultimi fotogrammi fermi (senza zoom). Uso: python3 check13.py <blocco>"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes13 as S
from scenes5 import zoomed
from PIL import Image
W, H = S.W, S.H
b = int(sys.argv[1]); S.S._cur["b"] = b; n = S.DUR[b]
z = zoomed(S.DRAW[b]); raw = S.DRAW[b]
bad = []; minm = 9999
for i in range(n):
    img = Image.new("RGB", (W, H), (0, 0, 0)); z(img, i / 30)
    a = np.asarray(img); ys, xs = np.where(a.max(axis=2) > 45)
    if len(xs):
        mm = int(min(xs.min(), W - 1 - xs.max(), ys.min(), H - 1 - ys.max())); minm = min(minm, mm)
        if mm <= 2: bad.append(i)
frames = []
for i in range(n - 16, n):
    img = Image.new("RGB", (W, H), (0, 0, 0)); raw(img, i / 30); frames.append(np.asarray(img).copy())
unsettled = None
for k in range(len(frames) - 1):
    if not np.array_equal(frames[k], frames[-1]): unsettled = n - 16 + k
print(f"clip {b}: {n} fotogrammi controllati; tagliati: {len(bad)} {bad[:5]}; margine minimo {minm}px; ultimo movimento al fotogramma: {unsettled} (fine {n-1})")
