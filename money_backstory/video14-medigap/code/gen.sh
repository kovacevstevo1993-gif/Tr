#!/bin/bash
# voce di un gruppo (fino a 3 blocchi): UNA richiesta gemini-2.5-flash-preview-tts Fenrir, poi rallentata con atempo calcolato dalla velocita' reale del gruppo (obiettivo 145 parole/minuto, fattore tra 0.70 e 0.90, altezza invariata) e tagliata ai confini con ritaglia3
g=$1; L=$(python3 -c "print(','.join(str(b) for b in ($g,$g+1,$g+2) if b<=18))")
txt=$(python3 -c "import json;J=json.load(open('code/blk.json'))['B'];print('\n\n'.join(J[b] for b in '$L'.split(',')))")
[ -f voce/g$g.wav ] || python3 code/tts1.py Fenrir "$txt" voce/g$g.wav gemini-2.5-flash-preview-tts || exit 1
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
