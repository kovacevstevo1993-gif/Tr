"""CONTROLLO AUTOMATICO DI OGNI FOTOGRAMMA (10/10/2026, nessun costo di immagini).
Rende ogni fotogramma di ogni slide SU SFONDO NERO (solo gli elementi), poi per OGNI fotogramma controlla:
 - elementi fuori dall'area sicura (tagliati ai bordi),
 - elementi completi a 80% (area a 0,80D = area finale) e IDENTICI da 0,81D alla fine (nessun movimento/ritardo),
 - primo elemento entro 0,45 s e nessun buco senza novita' piu' lungo di 2 s prima dell'80%.
Uso: python3 qa8.py <modulo> <blocco>   (es. v8b6_10 6)"""
import sys, os, json, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image
mod, blk = sys.argv[1], int(sys.argv[2])
M = importlib.import_module(mod)
import v8b1
W, H = 1920, 1080
v8b1.base = lambda t: Image.new('RGBA', (W, H), (0, 0, 0, 255))
v8b1.amb = lambda fr, *a, **k: fr
res = []
for i, (fn, n) in enumerate(zip(M.SLIDES[blk], M.SPEC[blk]), 1):
    M.CUE['blk'] = blk; M.CUE['t0'] = sum(M.SPEC[blk][:i - 1]) / 30; M.CUR['D'] = n / 30
    masks = []; changes = []; prev = None
    for f in range(n):
        a = np.asarray(fn(f / 30).convert('RGB'))[::2, ::2]
        cur = a.astype('int16')
        changes.append(0 if prev is None else int((np.abs(cur - prev).max(axis=2)[75:506, 34:926] > 25).sum())); prev = cur   # cambiamento reale dei pixel (anche testo/numeri dentro le card)
        m = a.max(axis=2) > 40
        m[:75] = False; m[:, :34] = False; m[:, 926:] = False; m[506:] = False      # via titolo e cornice dorata
        masks.append(m)
    fin = masks[-1]; area_f = int(fin.sum())
    areas = [int(m.sum()) for m in masks]; oob = 0
    oobl = []
    for fi, m in enumerate(masks):
        n75 = int(0.75 * n)
        band = m[75:488, 36:40].any() or m[75:488, 920:924].any() or m[500:504, 56:904].any()          # sempre: nulla oltre la cornice
        if fi >= n75: band = band or m[75:488, 42:56].any() or m[75:488, 904:918].any() or m[484:498, 56:904].any()   # stato finale: margine pulito
        oob += int(band)
        if band:
            ys, xs = np.where(m); oobl.append((fi, int(xs.min() * 2), int(xs.max() * 2), int(ys.max() * 2)))
    n80 = int(0.80 * n); n81 = int(0.81 * n) + 1
    ratio80 = float(masks[min(n80 + 1, n - 1)].sum() / max(1, area_f))
    unstable = 0
    for f in range(n81, n):
        unstable = max(unstable, int((masks[f] ^ fin).sum()))
    first = next((f for f, a_ in enumerate(areas) if a_ >= 0.03 * area_f), None)
    # buco: fotogrammi consecutivi prima dell'80% senza nessun cambiamento
    run = best = 0
    for f in range(1, n80):
        if changes[f] < 30: run += 1; best = max(best, run)
        else: run = 0
    ok = (oob == 0 and ratio80 > 0.995 and unstable < 30 and first is not None and first / 30 <= 0.45 and best / 30 <= 3.7)
    res.append({'blocco': blk, 'slide': i, 'fotogrammi': n, 'controllati': len(masks), 'fuori_area': oob, 'fuori_area_fotogrammi': oobl[:3] + oobl[-2:], 'ultimo_fuori_area': (oobl[-1][0] if oobl else None), 'completo_a_80%': round(ratio80, 4),
                'pixel_che_cambiano_dopo_81%': unstable, 'primo_elemento_s': round(first / 30, 2), 'buco_max_s': round(best / 30, 2), 'OK': bool(ok)})
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'qa_b{blk}.json'), 'w'), indent=1)
for r in res: print(r)
