#!/bin/bash
# uso: runblocks11.sh <cartella_out> <blocco>   -> render + check11 (ogni fotogramma) + ffprobe (conteggio)
OUT=$1; B=$2
cd "$(dirname "$0")"
mkdir -p "$OUT"
F=$(printf "%s/short11-blocco%02d.mp4" "$OUT" "$B")
S11_OUT="$OUT" SA_TMP="/tmp/s11_$B" python3 scenes11.py $B > "$OUT/log$B.txt" 2>&1
SA_TMP="/tmp/s11c_$B" python3 check11.py $B >> "$OUT/log$B.txt" 2>&1
N=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$F")
echo "ffprobe fotogrammi: $N" >> "$OUT/log$B.txt"
echo "FINITO $B" >> "$OUT/log$B.txt"
