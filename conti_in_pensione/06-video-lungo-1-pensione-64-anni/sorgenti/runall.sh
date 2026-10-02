#!/bin/bash
cd "$(dirname "$0")"
(for b in 6 8 10 12 14; do python3 render2.py $b > r$b.log 2>&1; done) &
(for b in 7 9 11 13 15; do python3 render2.py $b > r$b.log 2>&1; done) &
wait
echo ALLDONE > done.flag
