#!/bin/bash
# voce di un gruppo (fino a 3 blocchi): UNA richiesta gemini-2.5-flash-preview-tts Fenrir, poi rallentata (atempo 0.82, altezza invariata) e tagliata ai confini con ritaglia3
g=$1; L=$(python3 -c "print(','.join(str(b) for b in ($g,$g+1,$g+2) if b<=17))")
txt=$(python3 -c "import json;J=json.load(open('code/blk.json'))['B'];print('\n\n'.join(J[b] for b in '$L'.split(',')))")
[ -f voce/g$g.wav ] || python3 code/tts1.py Fenrir "$txt" voce/g$g.wav gemini-2.5-flash-preview-tts || exit 1
ffmpeg -y -loglevel error -i voce/g$g.wav -af atempo=0.82 voce/g${g}_s.wav
python3 code/ritaglia3.py code/blk.json voce/g${g}_s.wav $L
