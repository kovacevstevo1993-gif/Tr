#!/bin/bash
# voce di un gruppo (fino a 3 blocchi) con gemini-2.5-flash-preview-tts Fenrir (UNA richiesta), poi taglio ai confini con ritaglia3
g=$1; L=$(python3 -c "print(','.join(str(b) for b in ($g,$g+1,$g+2) if b<=20))")
txt=$(python3 -c "import json;J=json.load(open('code/blk.json'))['B'];print('\n\n'.join(J[b] for b in '$L'.split(',')))")
[ -f voce/g$g.wav ] || python3 code/tts1.py Fenrir "$txt" voce/g$g.wav gemini-2.5-flash-preview-tts || exit 1
python3 code/ritaglia3.py code/blk.json voce/g$g.wav $L
