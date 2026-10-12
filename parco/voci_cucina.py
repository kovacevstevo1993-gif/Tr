#!/usr/bin/env python3
"""Voci dello Short 'Il barattolo misterioso' con Gemini TTS (voce con stile) -> audioC/*.wav + durate.json.
Narratrice: giovane donna dolce e affettuosa. Bambini: timbri diversi, battute brevissime.
Uso: python3 voci_cucina.py [chiave ...]   (salta le battute già generate; --rifai per rigenerarle)"""
import base64, json, os, subprocess, sys, time, wave, urllib.request, urllib.error
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "audioC")
MODEL = "gemini-2.5-flash-preview-tts"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# voci dei bambini: Pollinations (OpenAI tts-1-hd), timbri diversi, tono alzato per farle da bambino
PL = {"narr": ("shimmer", 1.0), "mouse": ("nova", 1.20), "chip": ("fable", 1.34), "spike": ("echo", 1.48)}
USA_GEMINI_NARR = os.environ.get("GEMINI_NARR") == "1"   # Gemini ha quota giornaliera bassa: di default tutto Pollinations
VEL_PL_NARR = 0.96     # narratrice un filo più lenta e dolce
VEL_NARR = 1.10      # la narratrice di Gemini è lenta: +10% per tenere vivo l'hook

STILE = {
    "narr": ("Sulafat", 1.0, "Parla in italiano con la voce di una giovane donna dolce, calda e affettuosa, come una maestra "
             "che racconta una storia a bambini piccoli: ritmo lento e musicale, sorriso nella voce, piccole pause, meraviglia e tenerezza. Testo: "),
    "mouse": ("Leda", 1.16, "Parla in italiano come un bambino piccolo, voce acuta, allegra ed entusiasta, con stupore genuino. Testo: "),
    "chip": ("Puck", 1.28, "Parla in italiano come un bambino piccolissimo, vivace e scattante, voce molto acuta e curiosa. Testo: "),
    "spike": ("Fenrir", 1.36, "Parla in italiano come un bambino timido ma felice, voce un po' buffa e dolce. Testo: "),
}

# chiave, chi, testo
RIGHE = [
    ("n1", "narr", "Shhh... sentite anche voi? Qualcosa si muove, nella cucina!"),
    ("t1", "mouse", "Cosa sarà?"),
    ("n2", "narr", "Chip e Spike corrono a vedere."),
    ("c1", "chip", "Che curiosità!"),
    ("s1", "spike", "Cos'è, cos'è?"),
    ("n3", "narr", "Piano piano... aprono il barattolo dei biscotti."),
    ("c2", "chip", "Wow!"),
    ("s2", "spike", "Evviva!"),
    ("t2", "mouse", "Una farfalla magica!"),
    ("n4", "narr", "E i biscotti? Uno per ciascuno, perché condividere è bellissimo!"),
    ("end", "mouse", "Bambini Ciao Ciao! Iscrivetevi al canale!"),
]


def tts(testo, voce, prompt, tentativi=6):
    body = {"contents": [{"parts": [{"text": prompt + testo}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voce}}}}}
    for n in range(tentativi):
        try:
            req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
            r = json.load(urllib.request.urlopen(req, timeout=180))
            return base64.b64decode(r["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])  # PCM16 24 kHz
        except (urllib.error.HTTPError, KeyError, urllib.error.URLError) as e:
            print("   ", getattr(e, "code", e), "- riprovo tra", 15 * (n + 1), "s")
            time.sleep(15 * (n + 1))
    raise RuntimeError("TTS non disponibile")


def tts_pl(testo, voce, tentativi=6, speed=1.0):
    import requests
    for n in range(tentativi):
        try:
            r = requests.post("https://gen.pollinations.ai/v1/audio/speech", timeout=120,
                              json={"model": "openai/tts-1-hd", "input": testo, "voice": voce, "response_format": "mp3", "speed": speed})
            if r.status_code == 200: return r.content
            print("    pollinations", r.status_code)
        except requests.RequestException as e: print("    rete", e)
        time.sleep(3 * (n + 1))
    raise RuntimeError("TTS pollinations non disponibile")


def post(pcm, pitch, out_wav, vel=1.0, mp3=False):
    """PCM 24k -> wav 44.1k mono, toglie il silenzio ai bordi, alza il tono per le voci dei bambini."""
    raw = out_wav + ".raw"
    open(raw, "wb").write(pcm)
    ingresso = ["-f", "mp3"] if mp3 else ["-f", "s16le", "-ar", "24000", "-ac", "1"]
    filt = "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse," \
           "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.12,areverse"
    if pitch != 1.0:
        filt += f",rubberband=pitch={pitch}:formant=preserved" if False else f",rubberband=pitch={pitch}"
    if vel != 1.0: filt += f",atempo={vel}"
    filt += ",loudnorm=I=-16:TP=-1.5:LRA=7,aresample=44100"
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", *ingresso, "-i", raw,
                           "-af", filt, "-ac", "1", "-sample_fmt", "s16", out_wav])
    os.remove(raw)
    with wave.open(out_wav) as w:
        return w.getnframes() / w.getframerate()


def main():
    os.makedirs(OUT, exist_ok=True)
    pj = os.path.join(OUT, "durate.json")
    dur = json.load(open(pj)) if os.path.exists(pj) else {}
    scelte = [a for a in sys.argv[1:] if not a.startswith("--")]
    for k, chi, txt in RIGHE:
        if scelte and k not in scelte:
            continue
        wav = os.path.join(OUT, f"{k}.wav")
        if os.path.exists(wav) and k in dur and "--rifai" not in sys.argv:
            continue
        print(f"🎙️  {k} ({chi}): {txt}")
        if chi == "narr" and USA_GEMINI_NARR:
            voce, pitch, prompt = STILE[chi]
            dur[k] = round(post(tts(txt, voce, prompt), pitch, wav, VEL_NARR), 3)
        else:
            voce, pitch = PL[chi]
            dur[k] = round(post(tts_pl(txt, voce, speed=VEL_PL_NARR if chi == "narr" else 1.0), pitch, wav, 1.0, mp3=True), 3)
        json.dump(dur, open(pj, "w"), indent=1)
        time.sleep(7)
    print("✅", dur)


if __name__ == "__main__":
    main()
