#!/bin/bash
# uso: runblocks13.sh <cartella_out> <blocco>   -> render + check13 (ogni fotogramma) + ffprobe (conteggio)
OUT=$1; B=$2
cd "$(dirname "$0")"
mkdir -p "$OUT"
F=$(printf "%s/SA-aldi-short-blocco%02d.mp4" "$OUT" "$B")
S13_OUT="$OUT" python3 scenes13.py $B > "$OUT/log$B.txt" 2>&1
python3 check13.py $B >> "$OUT/log$B.txt" 2>&1
N=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$F")
echo "ffprobe fotogrammi: $N" >> "$OUT/log$B.txt"
echo "FINITO $B" >> "$OUT/log$B.txt"
