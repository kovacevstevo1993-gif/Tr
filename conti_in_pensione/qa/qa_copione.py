#!/usr/bin/env python3
"""Controllo copione (blocchi di voce) - Conti in Pensione.
Uso: python3 qa/qa_copione.py <copione-blocchi.txt> <parola-tema> [short|lungo]
Regole: N.14/N.16 (numeri in lettere), N.20 (Mai Inps a voce), N.27 (tema nel blocco 1),
chiusura short (video correlato, iscriviti, mi piace), niente INVALIDI da solo / 45 centesimi, blocchi <= 250 caratteri."""
import re, sys, glob, os
f, tema = sys.argv[1], sys.argv[2].lower()
modo = sys.argv[3] if len(sys.argv) > 3 else 'short'
maxc = int(sys.argv[4]) if len(sys.argv) > 4 else 250  # 4o argomento opzionale: limite caratteri a blocco (video 6: 500, su ordine utente 13/10)
righe = [l.rstrip('\n') for l in open(f, encoding='utf-8')]
blocchi = []
for l in righe:
    m = re.match(r'^(\d+)[ |]\s*(.+)$', l)
    if m: blocchi.append((int(m.group(1)), m.group(2)))
err = []
if not blocchi: err.append('nessun blocco trovato')
for n, t in blocchi:
    if re.search(r'\d', t): err.append(f'blocco {n}: cifre nel testo di voce (numeri in lettere)')
    if len(t) > maxc: err.append(f'blocco {n}: {len(t)} caratteri (max {maxc})')
    if re.search(r'my inps', t, re.I): err.append(f'blocco {n}: "My Inps" a voce (si dice Mai Inps)')
    if re.search(r'\binvalidi\b', t, re.I) and not re.search(r'invalidi al', t, re.I): err.append(f'blocco {n}: INVALIDI da solo')
    if re.search(r'45 centesimi|quarantacinque centesimi', t, re.I): err.append(f'blocco {n}: 45 centesimi')
if blocchi:
    prime = ' '.join(blocchi[0][1].lower().split()[:8])
    if tema not in prime: err.append(f'blocco 1: la parola del tema "{tema}" non e\' nelle prime 8 parole (N.27)')
    if modo == 'short':
        u = blocchi[-1][1].lower()
        for k in ('video correlato', 'iscriviti', 'mi piace'):
            if k not in u: err.append(f'ultimo blocco: manca "{k}"')
        mio = os.path.abspath(f)
        for g in glob.glob('*-short-*/copione-blocchi.txt'):
            if os.path.abspath(g) == mio: continue
            for l in open(g, encoding='utf-8'):
                m = re.match(r'^1[ |]\s*(.+)$', l)
                if m and ' '.join(m.group(1).lower().split()[:3]) == ' '.join(blocchi[0][1].lower().split()[:3]):
                    err.append(f'gancio uguale a {g}')
# --- controlli aggiunti il 22/10/2026 (N.42/N.48, short 12: difetti trovati solo dopo l'invio) ---
def _w(t): return re.findall(r"[a-zàèéìòù']+", t.lower())
_stop = set("il lo la i gli le un una di a da in con su per tra fra e o ma che chi non è ti ci ne si al del della dei delle nel nella sul sulla questo questa quello l' un'".split())
def _sh(t, n=3):
    w = _w(t); return {tuple(w[i:i+n]) for i in range(len(w)-n+1) if any(x not in _stop for x in w[i:i+n])}
# 1) stessa espressione (3 parole) in due blocchi diversi dello stesso copione
visti = {}
for n, t in blocchi:
    for g in _sh(t):
        if g in visti and visti[g] != n: err.append(f'ripetizione: "{" ".join(g)}" nei blocchi {visti[g]} e {n}')
        visti.setdefault(g, n)
# 2) espressioni di 4 parole gia' usate nei copioni degli altri video/short (formule ripetute, regola N.41/N.23)
mio = os.path.abspath(f); gia = {}
for g in glob.glob('*/copione-blocchi.txt'):
    if os.path.abspath(g) == mio: continue
    for l in open(g, encoding='utf-8'):
        for sh in _sh(re.sub(r'^\d+[ |]\s*', '', l), 4): gia.setdefault(sh, g.split('/')[0])
ripetute = sorted({(" ".join(sh), gia[sh]) for _, t in blocchi for sh in _sh(t, 4) if sh in gia})
for fr, d in ripetute[:12]: print(f'VERIFICARE formula gia usata ({d}): "{fr}"')
# 3) parole assolute: cercare l'eccezione su inps.it o togliere (N.48)
for n, t in blocchi:
    for m in re.finditer(r"\b(solo|soltanto|mai|tutti|tutte|nessuno|nessuna|sempre|nulla|niente|ogni volta)\b", t, re.I):
        print(f'VERIFICARE parola assoluta "{m.group(1)}" nel blocco {n}: eccezione su inps.it?')
import os as _o,sys as _s;_s.path.insert(0,_o.path.dirname(_o.path.abspath(__file__)));from check_data import errori_data
from qa_italiano import controlla as _ci
_e1,_a1=_ci(blocchi)
for _x in _a1:print('VERIFICARE italiano:',_x)
err.extend(_e1)
for _e in errori_data(' '.join(t for _,t in blocchi)):err.append(_e)
print(f'{len(blocchi)} blocchi, {sum(len(t) for _, t in blocchi)} caratteri')
for e in err: print('ERRORE:', e)
print('QA COPIONE OK' if not err else f'QA COPIONE NON PASSATO ({len(err)} errori): NON CONSEGNARE')
sys.exit(1 if err else 0)
