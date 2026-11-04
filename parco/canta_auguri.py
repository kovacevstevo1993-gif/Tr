#!/usr/bin/env python3
"""Voce CANTATA 'Tanti auguri a te': edge-tts (voce parlata, tempi delle parole) + Praat (altezza per sillaba = melodia di Happy Birthday, sillabe tenute).
Uscita: audioY/canto.wav (4 versi) + audioY/versi.json (inizio/fine di ogni verso nel file)."""
import certifi
certifi.where = lambda: "/root/.ccr/ca-bundle.crt"
import asyncio, json, os, subprocess, wave
import numpy as np
import edge_tts, parselmouth
from parselmouth.praat import call

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "audioY"); SR = 44100
NOTE = {"D4": 293.7, "E4": 329.6, "F#4": 370.0, "G4": 392.0, "A4": 440.0, "B4": 493.9, "C5": 523.3, "D5": 587.3}
# verso: (testo, [(parola, [sillabe])], note per sillaba, sillaba tenuta = ultima)
VERSI = [
    ("Tanti auguri, a te", [["tan", "ti"], ["au", "gu", "ri"], ["a"], ["te"]], "D4 D4 E4 D4 G4 F#4 F#4"),
    ("Tanti auguri, a te", [["tan", "ti"], ["au", "gu", "ri"], ["a"], ["te"]], "D4 D4 E4 D4 A4 G4 G4"),
    ("Tanti auguri, a te", [["tan", "ti"], ["au", "gu", "ri"], ["a"], ["te"]], "D5 D5 B4 G4 F#4 E4 E4"),
    ("Tanti auguri, a te", [["tan", "ti"], ["au", "gu", "ri"], ["a"], ["te"]], "C5 C5 B4 G4 A4 G4 G4"),
]


async def sintetizza(txt, mp3):
    com = edge_tts.Communicate(txt, "it-IT-ElsaNeural", rate="-30%", pitch="+0Hz", boundary="WordBoundary")
    wb = []
    with open(mp3, "wb") as f:
        async for ch in com.stream():
            if ch["type"] == "audio": f.write(ch["data"])
            elif ch["type"] == "WordBoundary": wb.append((ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7, ch["text"]))
    return wb


def canta(k, txt, sill, note):
    mp3 = os.path.join(OUT, f"v{k}.mp3"); wav = os.path.join(OUT, f"v{k}_raw.wav")
    wb = asyncio.run(sintetizza(txt, mp3))
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-ac", "1", "-ar", str(SR), wav])
    snd = parselmouth.Sound(wav); assert len(wb) == len(sill), (wb, sill)
    notes = [NOTE[n] for n in note.split()]; ns = sum(len(s) for s in sill); assert ns == len(notes), (ns, len(notes))
    pt = call("Create PitchTier", "p", 0, snd.duration); dt = call("Create DurationTier", "d", 0, snd.duration)
    i = 0; last_end = 0; marks = []
    for (a, b, w), sy in zip(wb, sill):
        n = len(sy); w0 = [len(s) for s in sy]; tot = sum(w0); t = a
        for j, s in enumerate(sy):
            d = (b - a) * w0[j] / tot; s0, s1 = t, t + d; t = s1; f = notes[i]; i += 1
            call(pt, "Add point", s0 + d * 0.08, f); call(pt, "Add point", s1 - d * 0.08, f)
            marks.append((s0, s1, i == len(notes), s1 - s0 < 0.1))
    # durata: sillabe normali x1.5, ultima tenuta x1.9 (oltre, "te" diventa "etti")
    call(dt, "Add point", 0.0, 1.0)
    for s0, s1, last, corta in marks:
        fct = 1.9 if last else (3.0 if corta else 1.5)
        call(dt, "Add point", max(s0, 1e-4), fct); call(dt, "Add point", s1 - 1e-4, fct)
    call(dt, "Add point", snd.duration, 1.0)
    man = call(snd, "To Manipulation", 0.01, 75, 700)
    call([pt, man], "Replace pitch tier"); call([dt, man], "Replace duration tier")
    out = call(man, "Get resynthesis (overlap-add)")
    res = os.path.join(OUT, f"v{k}.wav"); out.save(res, "WAV")
    return res


def main():
    os.makedirs(OUT, exist_ok=True)
    parts = []; info = []; t = 0.0
    for k, (txt, sill, note) in enumerate(VERSI):
        w = canta(k, txt, sill, note)
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", w, "-af", "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,loudnorm=I=-16:TP=-1.5:LRA=7,aresample=44100", "-ac", "1", "-sample_fmt", "s16", os.path.join(OUT, f"verso{k}.wav")])
        with wave.open(os.path.join(OUT, f"verso{k}.wav")) as f: d = f.getnframes() / f.getframerate()
        info.append(round(d, 2)); print("verso", k, "durata", round(d, 2))
    json.dump(info, open(os.path.join(OUT, "versi.json"), "w"))


if __name__ == "__main__":
    main()
