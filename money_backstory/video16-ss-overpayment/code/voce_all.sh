#!/bin/bash
# genera in ordine i gruppi (una richiesta ciascuno, max 2 tentativi) e li taglia; fermarsi al primo errore di quota
cd "$(dirname "$0")/.."
mapfile -t GR < code/gruppi.txt
for L in "${GR[@]}"; do
  g=${L%%,*}
  [ -f voce/b${g}.wav ] && continue
  ok=0
  for t in 1 2; do
    ./code/gen2.sh $L </dev/null && ok=1 && break
    echo "tentativo $t fallito gruppo $L"; sleep 20
  done
  [ $ok = 1 ] || { echo "STOP gruppo $L"; exit 1; }
  ./code/post.sh $L </dev/null || { echo "POST FALLITO $L"; exit 1; }
  echo "GRUPPO $L FATTO"
done
echo TUTTO FATTO
