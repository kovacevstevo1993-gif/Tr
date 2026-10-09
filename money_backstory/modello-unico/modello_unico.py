"""MODELLO UNICO slide The Money Backstory (06/10/2026). Vale per TUTTI i video nuovi (dal video 8).
Un solo stile: stesse funzioni, stesse posizioni, stessa regola 80%. Vedi MODELLO-UNICO.md.
Uso: creare v8b1_5.py con `from modello_unico import *`, definire SPEC (fotogrammi dallo screenshot dell'utente),
SLIDES e chiamare run(SPEC, SLIDES, prefisso, OUT)."""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__)); MB = os.path.dirname(HERE)
for p in ['kit-02-10/04-codice', 'video6-2027-cola/code', 'video7-500k/code']:
    sys.path.insert(0, os.path.join(MB, p))
import common
common.F = os.path.join(MB, 'kit-02-10/08-font') + '/'
from v3lib import *
from v3b3_10 import POP, new, lerp, person_box
from v5b1 import amb, sparks, shake, tile
from v5lib import arrow_r, arrow_d, paycheck, magnifier
from v6b1 import A_, E_, chip_src
from v6b2 import chip, logo
import v7b6_15 as _M
from v7b6_15 import fit, stage, card_, eq, P2, pill_last, sp, ring_, bars3, CUR, D, LASTA, LASTP, tt_
from v7b2_5 import tracker, numcard, ic_med, ic_ss, ic_coins, ic_time, ic_levers
from v7b46_53 import dashed, dashed_circle, warn, thumb

from sync_voce import Voice
_V = {'v': None}; CUE = {'blk': None, 't0': 0.0}
def cue(phrase):
    """Istante (s dall'inizio della SLIDE) in cui la voce dice `phrase` (parole del copione). Mai oltre l'80% della slide.
    Se manca il file di sincronia: errore (non si stima piu' a occhio)."""
    if _V['v'] is None: raise SystemExit('manca il file di sincronia voce (sync_voce.py): niente audio, niente slide')
    return max(0.15, min(_V['v'].at(CUE['blk'], phrase) - CUE['t0'], LASTA()))

# ---- POSIZIONI FISSE (uguali in tutti i video) ----
TITLE_Y = 90          # titolo Gloock oro, centrato, size 56-64 (stage lo fa)
PILL_Y = 800          # pillola-didascalia grande: SEMPRE l'ultimo elemento, compare all'80%
SRC_Y = 920           # chip fonte ufficiale in basso
# ---- REGOLA 80%: usare sp(n) per distribuire n elementi fino all'80%, pill_last() per la didascalia ----

def final_slide(t, seed=211):
    """Slide finale disclaimer (identica in ogni video lungo). Durata = fine voce dell'ultimo blocco."""
    Dd = CUR['D']
    fr = base(t); fr = amb(fr, t, seed, 7, 55); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('Rules, amounts and ages change', white, 250), ('and differ by location and plan.', white, 315), ('Always confirm with the official', goldL, 410),
             ('source before you rely on them.', goldL, 475), ('General information,', white, 570), ('not financial advice.', white, 635)]
    groups = [lines[0:2], lines[2:4], lines[4:6]]; tg = [0.3, 0.3 + (0.6 * Dd - 0.3) / 2, 0.6 * Dd]
    for g, ts in zip(groups, tg):
        if t > ts:
            C = new()
            for tx, cl, yy in g: txt(C, tx, BOLD(52), yy, cl, 255, x=650)
            fr = A_(fr, C, (140, 240, 1160, 770), t, ts)
    if t > 0.68 * Dd:
        C = new(); dashed(C, 1220, 280, 1780, 640); txt(C, 'WATCH NEXT', BOLD(56), 430, goldL, 255, x=1500); fr = A_(fr, C, (1200, 260, 1800, 660), t, 0.68 * Dd)
    if t > 0.8 * Dd - 0.4:
        C = new(); dashed_circle(C, 260, 860, 85); txt(C, 'SUBSCRIBE', BOLD(44), 835, goldL, 255, x=560); fr = A_(fr, C, (160, 760, 760, 960), t, 0.8 * Dd - 0.4)
    return frame(fr)

def check80(fn, n, first=0.8):
    """controllo: fotogramma a 0.78D e a 0.82D devono essere uguali nella parte che conta (nessun elemento nuovo dopo l'80%)."""
    import numpy as np
    CUR['D'] = n / 30
    a = np.asarray(fn(n / 30 * 0.84).convert('RGB'), dtype='int16'); b = np.asarray(fn(n / 30 * 0.97).convert('RGB'), dtype='int16')
    diff = np.abs(a - b).max(axis=2); return float((diff > 40).mean())   # frazione di pixel cambiati dopo l'84%

def run(SPEC, SLIDES, prefix, OUT, argv=None, voice=None):
    """python3 v8b1_5.py preview|render|check <blocco> [slide,slide]. SPEC[blocco]=[fotogrammi per slide] (somma = durata dallo screenshot)."""
    argv = argv or sys.argv
    mode = argv[1]; blk = int(argv[2]); sel = [int(x) for x in argv[3].split(',')] if len(argv) > 3 else None
    os.makedirs(OUT, exist_ok=True)
    if voice: _V['v'] = Voice(voice)
    CUE['blk'] = blk; off = 0
    for i, (fn, f) in enumerate(zip(SLIDES[blk], SPEC[blk]), 1):
        CUE['t0'] = off / 30; off += f
        if sel and i not in sel: continue
        CUR['D'] = f / 30
        if mode == 'preview':
            for fq in [0.25, 0.5, 0.8, 0.97]:
                fn(f / 30 * fq).convert('RGB').resize((960, 540)).save(f'{OUT}pv{blk}_{i}_{int(fq*100)}.png')
        elif mode == 'check':
            print(blk, i, f, 'pixel cambiati dopo l\'84%:', round(check80(fn, f), 4), flush=True)
        else:
            render_fast(fn, f, f'{OUT}{prefix}-b{blk}-{i:02d}.mp4'); print('done', blk, i, f, flush=True)
    if mode == 'preview': print(blk, SPEC[blk], sum(SPEC[blk]))
