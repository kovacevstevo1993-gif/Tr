"""Voci: narratrice dolce (Isabella) + voci da bambino diverse per ogni personaggio (Praat: altezza + formanti)."""
import subprocess, json, asyncio, certifi
certifi.where = lambda: "/root/.ccr/ca-bundle.crt"
import edge_tts, parselmouth
from parselmouth.praat import call

# chiave: (testo, voce sorgente, rate, bambino? (mediana Hz, rapporto formanti))
NARR = ("it-IT-IsabellaNeural", "-12%", None)
MOUSE = ("it-IT-DiegoNeural", "-2%", (265, 1.30))       # topolino: bambino sveglio
CHIP = ("it-IT-ElsaNeural", "-2%", (300, 1.14))         # Chip: bambina vivace
SPIKE = ("it-IT-GiuseppeMultilingualNeural", "-6%", (235, 1.24))   # Spike: bimbo piccolo, più calmo
LINES = {
 "N1": ("In un bellissimo parco, il piccolo topolino scopre una brutta sorpresa.", NARR),
 "M1": ("Oh no! Quanti rifiuti!", MOUSE),
 "N2": ("Ma il topolino non si arrende! Chiama i suoi amici.", NARR),
 "M2": ("Chip! Spike! Venite ad aiutarmi!", MOUSE),
 "C1": ("Arrivo!", CHIP),
 "S1": ("Eccomi!", SPIKE),
 "M3": ("Puliamo il parco insieme!", MOUSE),
 "N3": ("Prima, la bottiglia.", NARR),
 "M4": ("La plastica va nel giallo!", MOUSE),
 "N4": ("Poi, la carta.", NARR),
 "C2": ("La carta va nel blu!", CHIP),
 "N5": ("E adesso, la buccia di banana.", NARR),
 "S2": ("L'umido va nel marrone!", SPIKE),
 "N6": ("Ancora un pochino...", NARR),
 "M5": ("Forza, amici!", MOUSE),
 "N7": ("Ed ecco il parco... pulito e bellissimo!", NARR),
 "C3": ("Evviva!", CHIP),
 "S3": ("Evviva!", SPIKE),
 "M6": ("Grazie, amici! Ciao ciao, bambini!", MOUSE),
}
async def gen():
    for k, (txt, (v, rate, kid)) in LINES.items():
        await edge_tts.Communicate(txt, v, rate=rate).save(f"audio3/{k}_raw.mp3")
asyncio.run(gen())
TRIM = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,"
        "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse")
dur = {}
for k, (txt, (v, rate, kid)) in LINES.items():
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"audio3/{k}_raw.mp3", "-ac", "1", "-ar", "44100", f"audio3/{k}_a.wav"], check=True)
    src = f"audio3/{k}_a.wav"
    if kid:
        snd = parselmouth.Sound(src)
        out = call(snd, "Change gender", 75, 600, kid[1], kid[0], 1.12, 1.0)
        out.save(f"audio3/{k}_b.wav", "WAV"); src = f"audio3/{k}_b.wav"
        eq = "highpass=f=180,equalizer=f=3200:t=q:w=1.2:g=2.5,acompressor=threshold=-20dB:ratio=3:attack=5:release=80"
    else:  # narratrice: calda, morbida, un filo di eco da fiaba
        eq = "highpass=f=90,equalizer=f=220:t=q:w=1:g=2,equalizer=f=6500:t=q:w=1:g=-2.5,acompressor=threshold=-22dB:ratio=3:attack=8:release=120,aecho=0.85:0.5:42|71:0.10|0.06"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af", f"{TRIM},{eq},loudnorm=I=-17:TP=-1.5,aresample=44100",
                    "-c:a", "pcm_s16le", f"audio3/{k}.wav"], check=True)
    dur[k] = round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"audio3/{k}.wav"])), 2)
json.dump(dur, open("audio3/durate.json", "w"), indent=1); print(dur)
