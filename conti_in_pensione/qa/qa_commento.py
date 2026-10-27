#!/usr/bin/env python3
"""Controllo di una risposta a un commento YouTube.
Uso: python3 conti_in_pensione/qa/qa_commento.py <commento.txt> <risposta.txt>
Nato il 24/10/2026 (9 versioni di una risposta): REGOLE-FISSE.md, N.26, N.41, errori 18/10, 20/10, 22/10, 24/10.
Se stampa ERRORI non si consegna; gli AVVISI vanno risolti o giustificati prima di consegnare."""
import re, sys, datetime

def leggi(p):
    return open(p, encoding='utf-8').read()

def main():
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    com = leggi(sys.argv[1]).lower()
    ris = leggi(sys.argv[2]); r = ris.lower()
    err, avv = [], []
    # C2: solo i dati scritti dalla persona (errore 24/10: elenco di condizioni mai dichiarate)
    cat = ['handicap', 'invalid', 'disabil', r'\b104\b', 'disoccupat', 'caregiver', 'licenzi', 'naspi', 'gravos', 'usurant', 'malatt', 'vedov']
    for c in cat:
        if re.search(c, r) and not re.search(c, com):
            err.append('condizione/categoria non scritta dalla persona: "%s" (rispondi solo con i suoi dati)' % c.replace(r'\b', ''))
    # N.20: "Mai Inps" solo a voce
    if 'mai inps' in r:
        err.append('"Mai Inps" nei testi scritti: scrivere "My Inps" (N.20)')
    # C4: anni futuri senza spiegare perche' (errore 24/10: "nel 2028" nel 2026)
    oggi = datetime.date.today().year
    fut = sorted({int(y) for y in re.findall(r'\b(20[2-9]\d)\b', ris) if int(y) > oggi})
    if fut and not re.search(r'fissat|stabilit', r):
        avv.append('anni futuri %s senza spiegare perche\' (es. "uso i requisiti piu\' alti gia\' fissati dalla legge")' % fut)
    # N.48: parole assolute
    t = re.sub(r'il canale è solo informativo', '', r)
    ass = sorted({w for w in re.findall(r'\b(solo|mai|tutti|tutte|nessun\w*|sempre)\b', t)})
    if ass:
        avv.append('parole assolute %s: cercare l\'eccezione su inps.it o toglierle (N.48)' % ass)
    if len(ris) > 1800:
        avv.append('risposta lunga (%d caratteri): rispondere solo a cio\' che chiede' % len(ris))
    for e in err: print('ERRORE:', e)
    for a in avv: print('AVVISO:', a)
    if err:
        print('COMMENTO NON OK: non consegnare'); sys.exit(1)
    print('COMMENTO OK' + (' (con avvisi da risolvere)' if avv else ''))

main()
