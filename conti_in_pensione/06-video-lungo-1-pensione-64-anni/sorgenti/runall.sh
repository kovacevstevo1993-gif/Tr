#!/bin/bash
cd "$(dirname "$0")"
(for b in 26 28 30 32 34 36 38 40 42; do python3 render2.py $b > r$b.log 2>&1; done) &
(for b in 27 29 31 33 35 37 39 41; do python3 render2.py $b > r$b.log 2>&1; done) &
wait
echo ALLDONE > done.flag
