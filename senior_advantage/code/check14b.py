"""Controllo 'ultimo elemento entro l'80%': mascherina degli elementi (fondo nero) a 80%+0.5 s confrontata con l'ultimo fotogramma. Uso: python3 check14b.py"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes14 as S
from PIL import Image
for b in range(1, 8):
    S.S._cur["b"] = b; n = S.DUR[b]
    def mask(i):
        img = Image.new("RGB", (S.W, S.H), (0, 0, 0)); S.DRAW[b](img, i / 30)
        return np.asarray(img).max(axis=2) > 45
    a = mask(min(n - 1, int(n * 0.8) + 15)); z = mask(n - 1)
    new = int((z & ~a).sum()); tot = int(z.sum())
    print(f"blocco {b}: pixel comparsi dopo 80%+0,5s: {new} su {tot} ({100*new/tot:.2f}%)")
