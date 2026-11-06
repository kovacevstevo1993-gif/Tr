#!/bin/bash
# gruppi in ordine; ritenta su errore (502) con pausa crescente
for g in 7 10 13 16 19; do
  ok=0
  for try in 1 2 3 4 5 6 7 8; do
    if ./code/gen.sh $g; then ok=1; break; fi
    sleep $((try*20))
  done
  [ $ok = 1 ] || { echo "STOP al gruppo $g"; exit 1; }
  echo "GRUPPO $g FATTO"
done
echo TUTTO
