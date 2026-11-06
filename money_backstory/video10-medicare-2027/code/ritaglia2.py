"""Taglio ai confini dei blocchi usando le pause (silencedetect) vicino al punto atteso (proporzione caratteri), poi controllo con small.en.
Uso: ritaglia2.py blk.json g13.wav 13,14,15"""
import sys, re, json, subprocess
J = json.load(open(sys.argv[1]))['B']; gw = sys.argv[2]; g = [int(x) for x in sys.argv[3].split(',')]
dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',gw],capture_output=True,text=True).stdout)
o = subprocess.run(['ffmpeg','-i',gw,'-af','silencedetect=noise=-38dB:d=0.28','-f','null','-'],capture_output=True,text=True).stderr
st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', o)]; en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', o)]
gaps = [(s, e) for s, e in zip(st, en) if s > 0.3 and e < dur - 0.1]
L = [len(J[str(b)]) for b in g]; tot = sum(L); lead = 0.0; acc = 0; cuts = [0.0]
for i in range(len(g) - 1):
    acc += L[i]; est = dur * acc / tot
    s, e = min(gaps, key=lambda x: abs((x[0] + x[1]) / 2 - est))
    cuts.append(max(s + 0.35, (s + e) / 2) if e - s > 0.7 else (s + e) / 2)
    print('confine', g[i], g[i+1], 'gap', round(s,2), round(e,2), 'est', round(est,2))
cuts.append(dur)
for b, a, e in zip(g, cuts, cuts[1:]):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',gw,'-ss',f'{a:.3f}','-to',f'{e:.3f}',f'voce/b{b}.wav'],check=True)
