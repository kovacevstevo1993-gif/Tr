#!/usr/bin/env python3
"""Tempi parola per parola di ogni blocco voce (faster-whisper 'small', locale, gratis). Uso: tempi_parole.py cartella_voce out.json"""
import sys, json, glob, os, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8", download_root="/tmp/claude-0/whisper")
out = {}
for f in sorted(glob.glob(os.path.join(sys.argv[1], "b*.mp3"))):
    pcm = subprocess.run(["ffmpeg","-loglevel","error","-i",f,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout
    dur = len(pcm)/32000
    seg,_ = m.transcribe(np.frombuffer(pcm,np.int16).astype(np.float32)/32768, language="it", word_timestamps=True, beam_size=5)
    w = [(x.word.strip(), round(x.start,2), round(x.end,2)) for s in seg for x in s.words]
    out[os.path.basename(f)[:-4]] = {"durata": round(dur,2), "parole": w}
    print(os.path.basename(f), round(dur,2), flush=True)
    print("  ", " ".join(f"{a}[{b}]" for a,b,c in w), flush=True)
json.dump(out, open(sys.argv[2],"w"), ensure_ascii=False, indent=1)
