#!/bin/bash
# uso: runblocks7.sh <modulo> <cartella_out> <blocco>   -> render + check_frames (ogni fotogramma) + ffprobe (conteggio)
MOD=$1; OUT=$2; B=$3
cd "$(dirname "$0")"
mkdir -p "$OUT"
F=$(printf "%s/V7-blocco%02d.mp4" "$OUT" "$B")
OUT="$OUT" python3 $MOD.py $B > "$OUT/log$B.txt" 2>&1
python3 check_frames.py $MOD $B >> "$OUT/log$B.txt" 2>&1
N=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$F")
echo "ffprobe fotogrammi: $N" >> "$OUT/log$B.txt"
echo "FINITO $B" >> "$OUT/log$B.txt"
