#!/bin/bash
# uso: runblocks10.sh <cartella_out> <blocco>   -> render + bf10_check (ogni fotogramma) + ffprobe (conteggio)
OUT=$1; B=$2
cd "$(dirname "$0")"
export SA_W=1920 SA_H=1080
mkdir -p "$OUT"
F=$(printf "%s/SA-blackfriday-blocco%02d.mp4" "$OUT" "$B")
OUT="$OUT" python3 bf10_all.py $B > "$OUT/log$B.txt" 2>&1
python3 bf10_check.py $B >> "$OUT/log$B.txt" 2>&1
N=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$F")
echo "ffprobe fotogrammi: $N" >> "$OUT/log$B.txt"
echo "FINITO $B" >> "$OUT/log$B.txt"
