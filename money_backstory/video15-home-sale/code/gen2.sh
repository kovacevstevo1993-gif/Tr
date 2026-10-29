#!/bin/bash
# voce di un gruppo (lista blocchi, es. 1,2,3): UNA richiesta gemini-2.5-flash-preview-tts Fenrir; poi atempo (obiettivo 145 parole/minuto, fattore 0.70-0.90) e ritaglia3 ai confini
L=$1; g=${L%%,*}
txt=$(python3 -c "import json;J=json.load(open('code/blk.json'))['B'];print('\n\n'.join(J[b] for b in '$L'.split(',')))")
[ -f voce/g$g.wav ] || python3 code/tts1.py Fenrir "$txt" voce/g$g.wav gemini-2.5-flash-preview-tts || exit 1
