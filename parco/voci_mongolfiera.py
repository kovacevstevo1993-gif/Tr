#!/usr/bin/env python3
"""Voci ITALIANE native per lo Short "La mongolfiera dei quattro amici" -> audioF/*.wav + durate.json (+ controllo pronuncia).
Solo voci it-IT native (Isabella, Diego, Elsa): la 'GiuseppeMultilingual' sbaglia le doppie ('Aspatami') ed è esclusa.
Bambini: edge-tts a tono quasi naturale + Praat (altezza, timbro, ampiezza dell'intonazione) -> suono da bambino senza effetto robot.
Ogni battuta viene riascoltata con la trascrizione (Pollinations whisper) e rifatta con impostazioni alternative se non coincide.
Uso: python3 voci_cucina3.py [chiave ...] [--rifai]"""
import certifi
certifi.where = lambda: "/root/.ccr/ca-bundle.crt"      # sandbox: bundle del proxy (va tolto altrove)
import asyncio, json, os, re, subprocess, sys, wave
import edge_tts
import parselmouth
from parselmouth.praat import call
from trascrivi import trascrivi

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "audioH")

# voce, rate, pitch edge (Hz), Praat: (rapporto formanti, altezza mediana Hz, escursione intonazione) o None
VOCE = {
    "narr":  ("it-IT-IsabellaNeural", "-4%", "+3Hz", None),
    "mouse": ("it-IT-DiegoNeural", "+6%", "+20Hz", (1.24, 250, 1.25)),
    "chip":  ("it-IT-ElsaNeural", "+8%", "+14Hz", (1.10, 292, 1.30)),
    "ele":   ("it-IT-DiegoNeural", "-6%", "-2Hz", (1.10, 184, 1.20)),
    "spike": ("it-IT-DiegoNeural", "-2%", "+4Hz", (1.14, 206, 1.15)),
}
# alternative se la trascrizione non coincide: (rate, pitch edge)
ALT = [("+0%", "+0Hz"), ("-6%", "+10Hz"), ("+12%", "+0Hz")]

RIGHE = [
    ("n1", "narr", "Quattro amici vogliono volare! L'elefantino gonfia la mongolfiera."),
    ("t1", "mouse", "Si parte!"),
    ("n2", "narr", "Su, su, su, sempre più in alto, tra le nuvole!"),
    ("c1", "chip", "Che bello!"),
    ("n3", "narr", "Ma Spike salta di gioia... e Pop! La mongolfiera si buca!"),
    ("s1", "spike", "Ops!"),
    ("n4", "narr", "Scendono veloci verso il mare!"),
    ("t2", "mouse", "Aiuto!"),
    ("n5", "narr", "Chip si arrampica sulla corda e attacca una toppa."),
    ("c2", "chip", "Ci penso io!"),
    ("n6", "narr", "L'elefantino soffia forte... e la mongolfiera torna a volare!"),
    ("e1", "ele", "Tocca a me!"),
    ("n7", "narr", "Salvi! Al tramonto tornano a casa. Insieme è più bello!"),
    ("s2", "spike", "Evviva!"),
    ("t3", "mouse", "Evviva!"),
    ("end", "mouse", "Bambini Ciao Ciao! Iscrivetevi al canale!"),
]
NUM = {"uno": "1", "due": "2", "tre": "3"}


def norm(s):
    w = re.sub(r"[^a-zàèéìòù0-9 ]", " ", s.lower().replace("'", " ")).split()
    return [NUM.get(x, x) for x in w]


def uguale(atteso, sentito):
    a, b = norm(atteso), norm(sentito)
    if a == b: return True
    if a and b and len(a) == len(b):           # tollera una sola parola diversa ma "vicina" (es. 'c è' / 'ce')
        return False
    return "".join(a) == "".join(b)


async def sintetizza(testo, voce, rate, pitch, path):
    for n in range(5):
        try:
            await edge_tts.Communicate(testo, voce, rate=rate, pitch=pitch).save(path)
            if os.path.getsize(path) > 1000: return
        except Exception as e:
            print("   riprovo:", str(e)[:80]); await asyncio.sleep(2 * (n + 1))
    raise RuntimeError("edge-tts non risponde")


def post(mp3, wav, praat, pausa):
    tmp = wav + ".tmp.wav"
    filt = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,"
            "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.10,areverse,"
            f"silenceremove=stop_periods=-1:stop_duration=0.22:stop_threshold=-40dB:stop_silence={pausa}")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-af", filt, "-ac", "1", "-ar", "44100", tmp])
    if praat:
        ratio, med, rng = praat
        out = call(parselmouth.Sound(tmp), "Change gender", 75, 450, ratio, med, rng, 1.0)
        out.save(tmp, "WAV")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-af", "loudnorm=I=-16:TP=-1.5:LRA=7,aresample=44100",
                           "-ac", "1", "-sample_fmt", "s16", wav])
    os.remove(tmp)
    with wave.open(wav) as w: return w.getnframes() / w.getframerate()


async def main():
    os.makedirs(OUT, exist_ok=True)
    pj = os.path.join(OUT, "durate.json")
    dur = json.load(open(pj)) if os.path.exists(pj) else {}
    scelte = [a for a in sys.argv[1:] if not a.startswith("--")]
    for k, chi, txt in RIGHE:
        if scelte and k not in scelte: continue
        wav = os.path.join(OUT, f"{k}.wav")
        if os.path.exists(wav) and k in dur and "--rifai" not in sys.argv: continue
        v, rate, pitch, praat = VOCE[chi]
        prove = [(rate, pitch)] + ALT
        for n, (rt, pt) in enumerate(prove):
            mp3 = os.path.join(OUT, f"{k}_raw.mp3")
            await sintetizza(txt, v, rt, pt, mp3)
            d = post(mp3, wav, praat, 0.26 if chi == "narr" else 0.12)
            os.remove(mp3)
            sentito = trascrivi(wav)
            ok = uguale(txt, sentito)
            print(f"🎙️  {k} ({chi}) {'✓' if ok else '✗'} «{sentito}»" + ("" if ok else f"  (voluto «{txt}») prova {n + 1}"))
            if ok or n == len(prove) - 1: break
        dur[k] = round(d, 3)
        json.dump(dur, open(pj, "w"), indent=1)
    print("✅", dur)


if __name__ == "__main__":
    asyncio.run(main())
