#!/bin/bash
# Uso: render_sicuro.sh NNN "1 2 3 4"   (es. 007)  - lancia i blocchi uno alla volta, riparte dai fotogrammi gia fatti se il processo si ferma (fino a 6 tentativi per blocco). Log: /tmp/claude-0/render_NNN.log
N=$1; BL=${2:-"1 2 3 4"}; D="$(cd "$(dirname "$0")/.." && pwd)"; LOG=/tmp/claude-0/render_$N.log
for b in $BL; do
  for k in 1 2 3 4 5 6; do
    echo "INIZIO b$b tentativo $k $(date +%T)" >> $LOG
    RESUME=1 python3 $D/short${N}_monta.py $b >> $LOG 2>&1 && { echo "FINE b$b $(date +%T)" >> $LOG; break; }
    echo "ERRORE b$b tentativo $k $(date +%T)" >> $LOG; sleep 5
  done
done
echo "TUTTO FINITO $(date +%T)" >> $LOG
