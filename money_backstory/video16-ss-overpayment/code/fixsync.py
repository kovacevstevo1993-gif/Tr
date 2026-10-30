"""Correzioni a mano del sync.json dove l'allineamento automatico sbaglia (verificate con silencedetect): da rilanciare dopo ogni make_sync.py.
Blocco 2: la frase 'The total she owes: nine thousand dollars.' e' reale tra 26,04 s e 28,60 s (pausa vera prima e fine voce), il riconoscimento l'aveva messa a 28,9-30,7 s."""
import json
J = json.load(open('sync.json')); b = J['blocks']['2']; st = b['start']
fix = ['The', 'total', 'she', 'owes:', 'nine', 'thousand', 'dollars.']; ws = b['words']
if [w[0] for w in ws[-7:]] == fix:
    t0, t1 = 26.04, 28.60; L = [len(w) + 1 for w in fix]; tot = sum(L); x = t0
    for k, w in enumerate(fix):
        ws[len(ws) - 7 + k][1] = round(st + x, 3); x += (t1 - t0) * L[k] / tot; ws[len(ws) - 7 + k][2] = round(st + x, 3)
    b['rel'] = [[w[0], round(w[1] - st, 3), round(w[2] - st, 3)] for w in ws]
    json.dump(J, open('sync.json', 'w'), indent=0); print('sync blocco 2 corretto')
else: print('niente da correggere')
