#!/bin/sh
python3 ../../qa/qa_slide.py index.html $1 $2 1080 1920 2>&1 | sed "s/^/B$(($1+1)) /"
