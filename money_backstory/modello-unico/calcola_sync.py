"""SINCRONIA CALCOLATA (10/10/2026): quando NON c'e' l'audio, si calcola il tempo di ogni parola del copione dalla
durata del blocco (screenshot dell'utente). Peso di ogni parola = sillabe (gruppi di vocali) + pausa dopo la punteggiatura
(virgola 0,22 s, punto/due punti 0,5 s). I tempi sono scalati in modo che l'ultima parola finisca esattamente alla fine voce.
Stesso formato di sync_voce.py (classe Voice). Quando arriva l'audio vero, sync_voce.py sostituisce questo file.
Uso: python3 calcola_sync.py copione.md fine_blocchi.txt sync.json"""
import sys, re, json
from sync_voce import parse_copione

def syl(w):
    w = re.sub(r'[^a-z]', '', w.lower())
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1 and not w.endswith(('le', 'ee')): n -= 1
    return max(1, n)

def calc_block(text, start, end):
    ws = text.split(); W = []; pauses = []
    for w in ws:
        W.append(0.07 + 0.105 * syl(w) + 0.012 * len(re.sub(r'[^A-Za-z]', '', w)))   # sec per parola (a ritmo naturale)
        pauses.append(0.5 if w[-1] in '.:?!' else 0.22 if w[-1] in ',;' else 0.0)
    ends_pause = pauses[-1]; pauses[-1] = 0.0
    total = sum(W) + sum(pauses); dur = end - start; k = dur / total
    t = start; out = []
    for w, a, p in zip(ws, W, pauses):
        out.append([re.sub(r"[^A-Za-z0-9']", '', w) or w, round(t, 3), round(t + a * k, 3)]); t += (a + p) * k
    out[-1][2] = round(end, 3)
    return out

if __name__ == '__main__':
    cop, fb, outp = sys.argv[1:4]
    blocks = parse_copione(cop); ends = [int(x.strip()) for x in open(fb) if x.strip()]
    res = {'coverage': 0.0, 'metodo': 'calcolato dalla durata (non misurato dall audio)', 'blocks': {}}
    for b in sorted(blocks):
        if b > len(ends): continue
        s = ends[b - 2] / 30 if b > 1 else 0.0; e = ends[b - 1] / 30
        res['blocks'][b] = {'start': round(s, 3), 'end': round(e, 3), 'words': calc_block(blocks[b], s, e)}
    json.dump(res, open(outp, 'w'), indent=1); print('blocchi:', list(res['blocks']), '->', outp)
