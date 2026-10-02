#!/bin/bash
cd "$(dirname "$0")"
(for b in 16 18 20 22 24; do python3 render2.py $b > r$b.log 2>&1; done) &
(for b in 17 19 21 23 25; do python3 render2.py $b > r$b.log 2>&1; done) &
wait
echo ALLDONE > done.flag
