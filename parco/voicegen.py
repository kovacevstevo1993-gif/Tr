"""Generatore di voci: narratrice dolce + bambini diversi (Praat). Uso: voicegen.gen(LINES, 'audioA')"""
import subprocess, json, asyncio, os, certifi
certifi.where = lambda: "/root/.ccr/ca-bundle.crt"
import edge_tts, parselmouth
from parselmouth.praat import call
NARR = ("it-IT-IsabellaNeural", "-12%", None)
MOUSE = ("it-IT-DiegoNeural", "-2%", (265, 1.30))
CHIP = ("it-IT-ElsaNeural", "-2%", (300, 1.14))
SPIKE = ("it-IT-GiuseppeMultilingualNeural", "-6%", (235, 1.24))
P = {"narr": NARR, "mouse": MOUSE, "chip": CHIP, "spike": SPIKE}
TRIM = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,"
        "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse")
def gen(lines, outdir):
    os.makedirs(outdir, exist_ok=True)
    async def g():
        for k, (who, txt) in lines.items():
            v, rate, kid = P[who]; await edge_tts.Communicate(txt, v, rate=rate).save(f"{outdir}/{k}_raw.mp3")
    asyncio.run(g()); dur = {}
    for k, (who, txt) in lines.items():
        v, rate, kid = P[who]
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{outdir}/{k}_raw.mp3", "-ac", "1", "-ar", "44100", f"{outdir}/{k}_a.wav"], check=True)
        src = f"{outdir}/{k}_a.wav"
        if kid:
            out = call(parselmouth.Sound(src), "Change gender", 75, 600, kid[1], kid[0], 1.12, 1.0); out.save(f"{outdir}/{k}_b.wav", "WAV"); src = f"{outdir}/{k}_b.wav"
            eq = "highpass=f=180,equalizer=f=3200:t=q:w=1.2:g=2.5,acompressor=threshold=-20dB:ratio=3:attack=5:release=80"
        else:
            eq = "highpass=f=90,equalizer=f=220:t=q:w=1:g=2,equalizer=f=6500:t=q:w=1:g=-2.5,acompressor=threshold=-22dB:ratio=3:attack=8:release=120,aecho=0.85:0.5:42|71:0.10|0.06"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af", f"{TRIM},{eq},loudnorm=I=-17:TP=-1.5,aresample=44100", "-c:a", "pcm_s16le", f"{outdir}/{k}.wav"], check=True)
        dur[k] = round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{outdir}/{k}.wav"])), 2)
    json.dump(dur, open(f"{outdir}/durate.json", "w"), indent=1); return dur
