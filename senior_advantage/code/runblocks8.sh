#!/bin/bash
# uso: runblocks8.sh <cartella_out> <blocco>   -> render + check_frames (ogni fotogramma) + ffprobe (conteggio)
OUT=$1; B=$2
cd "$(dirname "$0")"
export SA_W=1920 SA_H=1080
mkdir -p "$OUT"
F=$(printf "%s/V8-blocco%02d.mp4" "$OUT" "$B")
OUT="$OUT" python3 ${MOD:-long8_b01_20}.py $B > "$OUT/log$B.txt" 2>&1
python3 check_frames.py ${MOD:-long8_b01_20} $B >> "$OUT/log$B.txt" 2>&1
N=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$F")
echo "ffprobe fotogrammi: $N" >> "$OUT/log$B.txt"
echo "FINITO $B" >> "$OUT/log$B.txt"
