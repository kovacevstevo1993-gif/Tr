#!/usr/bin/env python3
"""Voce in UNA SOLA richiesta per tutto il copione (stesso timbro in tutti i blocchi), poi taglio ai silenzi tra i blocchi.
Uso: voce_unica.py copione.json cartella_out   -> cartella_out/b01.mp3 ... (+ tutto.mp3). Controlla poi: controllo_voce.py cartella_out"""
import sys, os, json, subprocess, re, time
H = os.path.dirname(os.path.abspath(__file__)); TTS = os.path.join(H, "..", "tts.py")
cop = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
PRE = "Leggi in italiano con tono deciso, calmo e affermativo, da narratore di documentario d'inchiesta, con lo stesso tono dall'inizio alla fine; fai una pausa di circa un secondo e mezzo dopo ogni paragrafo. Testo: "
full = os.path.join(out, "tutto")
if not os.path.exists(full + ".mp3"):
    for k in range(6):
        r = subprocess.run(["python3", TTS, "gemini-2.5-flash-preview-tts", "Charon", full, PRE + "\n\n".join(cop)], capture_output=True, text=True)
        if r.returncode == 0: break
        time.sleep(20 * (k + 1))
    else: sys.exit("ERRORE voce: " + r.stderr[-300:])
dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",full + ".mp3"],capture_output=True,text=True).stdout)
log = subprocess.run(["ffmpeg","-hide_banner","-i",full + ".mp3","-af","silencedetect=noise=-38dB:d=0.3","-f","null","-"],capture_output=True,text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
sil = [(a, b) for a, b in zip(st, en)]
tot = sum(len(t) for t in cop); cum = 0; cuts = []
for t in cop[:-1]:
    cum += len(t); exp = cum / tot * dur
    best = min(sil, key=lambda s: abs((s[0] + s[1]) / 2 - exp)); cuts.append((best[0] + best[1]) / 2)
cuts = sorted(set(cuts))
if len(cuts) != len(cop) - 1: sys.exit(f"ERRORE: trovati {len(cuts)} tagli su {len(cop)-1} attesi: rigenerare")
edges = [0.0] + cuts + [dur]
for i in range(len(cop)):
    a, b = edges[i], edges[i + 1]
    subprocess.run(["ffmpeg","-y","-loglevel","error","-ss",f"{a:.3f}","-to",f"{b:.3f}","-i",full + ".mp3","-c:a","libmp3lame","-q:a","2",os.path.join(out, f"b{i+1:02d}.mp3")],check=True)
    print(f"b{i+1:02d}: {b-a:.2f} s")
