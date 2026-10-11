#!/bin/bash
# Eseguito a ogni avvio chat: cerca in TUTTI i branch dove sta il lavoro piu' recente di ogni canale. Non unisce niente.
cd "$(dirname "$0")" || exit 0
git fetch -q origin 2>/dev/null
echo "=== LAVORO PIU' RECENTE PER CANALE, su qualsiasi branch (ultimo commit che tocca la cartella). Per leggere un file: git show origin/<branch>:<percorso> ==="
for d in money_backstory senior_advantage conti_in_pensione parco; do
  best=""; bt=0
  for b in $(git branch -r | grep -v HEAD | sed 's/^ *//'); do
    t=$(git log -1 --format=%ct "$b" -- "$d" 2>/dev/null); t=${t:-0}
    [ "$t" -gt "$bt" ] && bt=$t && best=$b
  done
  [ -n "$best" ] && echo "$d -> $best ($(date -d @$bt '+%d/%m %H:%M')) : $(git log -1 --format=%s "$best" -- "$d")"
done
echo "--- Ultimi 12 commit su TUTTI i branch (cosa e' stato fatto per ultimo, in qualsiasi chat):"
git log --all --remotes --no-walk=unsorted --format='%cd %h %s' --date=format:'%d/%m %H:%M' $(git branch -r | grep -v HEAD | sed 's/^ *//') 2>/dev/null | sort -t' ' -k1.7,1.8 -k1.4,1.5 -k1.1,1.2 -r | head -12
echo "--- Se manca un dato (screenshot, voce, durate): cercarlo in TIMELINE.md/file di stato del canale, in git show origin/<branch>:..., poi nelle chat (list_sessions/list_events). MAI chiederlo all'utente prima."
