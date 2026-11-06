#!/bin/bash
# genera la voce di un gruppo (3 blocchi) con gemini-2.5-flash-preview-tts Fenrir, poi taglia ai confini
g=$1
txt=$(python3 -c "import json;J=json.load(open('code/blk.json'))['B'];print('\n\n'.join(J[str(b)] for b in ($g,$g+1,$g+2)))")
[ -f voce/g$g.wav ] || python3 code/tts.py Fenrir "$txt" voce/g$g.wav gemini-2.5-flash-preview-tts
python3 code/ritaglia2.py code/blk.json voce/g$g.wav $g,$((g+1)),$((g+2))
