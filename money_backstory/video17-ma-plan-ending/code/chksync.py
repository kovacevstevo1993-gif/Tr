"""Controllo della sincronia parola per parola: ogni pausa vera (silencedetect >=0.25 s) deve cadere in un varco tra due parole del sync.json; ultima parola entro la durata. Uso: python3 code/chksync.py 1-15"""
import sys, json, re, subprocess
j = json.load(open('sync.json'))['blocks']; a, b = [int(x) for x in sys.argv[1].split('-')]; bad = 0
for n in range(a, b + 1):
    d = j[str(n)]; st = d['start']; D = d['end'] - st; ws = [(w[0], w[1] - st, w[2] - st) for w in d['words']]
    o = subprocess.run(['ffmpeg', '-i', f'voce/b{n}.wav', '-af', 'silencedetect=noise=-38dB:d=0.25', '-f', 'null', '-'], capture_output=True, text=True).stderr
    S = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', o)]; E = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', o)]
    probs = []
    for s0, e0 in zip(S, E):
        if s0 < 0.2 or e0 > D - 0.2: continue
        mid = (s0 + e0) / 2
        for w, ws0, we0 in ws:
            if ws0 + 0.05 < mid < we0 - 0.05: probs.append((round(mid, 1), w, round(ws0, 1), round(we0, 1)))
    over = ws[-1][2] > D + 0.05
    print(n, 'D', round(D, 1), 'ultima', round(ws[-1][2], 1), 'OVER' if over else '', 'pause dentro parole:', probs[:4]); bad += bool(probs) or over
print('PROBLEMI', bad)
