#!/bin/bash
# solo taglio ai confini dei blocchi (NESSUN atempo, NESSUN rubberband: regola 58). Uso: post.sh 1,2
L=$1; g=${L%%,*}
python3 code/ritaglia3.py code/blk.json voce/g${g}.wav $L
