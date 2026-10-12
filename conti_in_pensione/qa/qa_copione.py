#!/usr/bin/env python3
"""Controllo copione (blocchi di voce) - Conti in Pensione.
Uso: python3 qa/qa_copione.py <copione-blocchi.txt> <parola-tema> [short|lungo]
Regole: N.14/N.16 (numeri in lettere), N.20 (Mai Inps a voce), N.27 (tema nel blocco 1),
chiusura short (video correlato, iscriviti, mi piace), niente INVALIDI da solo / 45 centesimi, blocchi <= 250 caratteri."""
import re, sys, glob, os
f, tema = sys.argv[1], sys.argv[2].lower()
modo = sys.argv[3] if len(sys.argv) > 3 else 'short'
righe = [l.rstrip('\n') for l in open(f, encoding='utf-8')]
blocchi = []
for l in righe:
    m = re.match(r'^(\d+)[ |]\s*(.+)$', l)
    if m: blocchi.append((int(m.group(1)), m.group(2)))
err = []
if not blocchi: err.append('nessun blocco trovato')
for n, t in blocchi:
    if re.search(r'\d', t): err.append(f'blocco {n}: cifre nel testo di voce (numeri in lettere)')
    if len(t) > 250: err.append(f'blocco {n}: {len(t)} caratteri (max 250)')
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
print(f'{len(blocchi)} blocchi, {sum(len(t) for _, t in blocchi)} caratteri')
for e in err: print('ERRORE:', e)
print('QA COPIONE OK' if not err else f'QA COPIONE NON PASSATO ({len(err)} errori): NON CONSEGNARE')
sys.exit(1 if err else 0)
