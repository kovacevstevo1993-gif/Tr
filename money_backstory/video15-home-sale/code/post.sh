#!/bin/bash
# dopo la generazione: atempo calcolato (145 parole/min, 0.70-0.90) e taglio ai confini. Uso: post.sh 1,2,3
L=$1; g=${L%%,*}
f=$(python3 - <<PY
import json,subprocess
J=json.load(open('code/blk.json'))['B']; w=sum(len(J[b].split()) for b in '$L'.split(','))
d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','voce/g$g.wav'],capture_output=True,text=True).stdout)
print(round(min(0.90,max(0.70,145/(w/d*60))),3))
PY
)
echo "fattore atempo gruppo $g: $f"
ffmpeg -y -loglevel error -i voce/g$g.wav -af atempo=$f voce/g${g}_s.wav
python3 code/ritaglia3.py code/blk.json voce/g${g}_s.wav $L
