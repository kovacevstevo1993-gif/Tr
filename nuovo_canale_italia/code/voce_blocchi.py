#!/usr/bin/env python3
"""Voce A per ogni blocco del copione, con controllo pronuncia (Gemini). Uso: voce_blocchi.py copione.json cartella"""
import json, sys, os, time, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trascrivi_gemini import trascrivi
cop, out = json.load(open(sys.argv[1])), sys.argv[2]; os.makedirs(out, exist_ok=True)
PRE = "Leggi in italiano con tono deciso, calmo e affermativo, da narratore di documentario d'inchiesta. Testo: "
TTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tts.py")
for i, t in enumerate(cop, 1):
    base = os.path.join(out, f"b{i:02d}")
    if os.path.exists(base + ".mp3"): continue
    for k in range(6):
        r = subprocess.run(["python3", TTS, "gemini-2.5-flash-preview-tts", "Charon", base, PRE + t], capture_output=True, text=True)
        if r.returncode == 0: break
        time.sleep(20 * (k + 1))
    for k in range(4):
        try: tr = trascrivi(base + ".mp3", "gemini-3.5-flash"); break
        except Exception: time.sleep(10)
    else: tr = "?"
    print(f"b{i:02d}", r.stdout.strip().split()[-2] if r.returncode == 0 else "ERR", "|", tr, flush=True)
