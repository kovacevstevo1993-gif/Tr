import subprocess, json, asyncio, certifi
certifi.where = lambda: "/root/.ccr/ca-bundle.crt"
import edge_tts
# (testo, voce, pitch-shift) - tutte voci femminili neurali
LINES = {
 "m1": ("Oh no! Quanti rifiuti nel parco!", "it-IT-IsabellaNeural", 1.0),
 "m2": ("Chiamiamo gli amici! Chip! Spike!", "it-IT-IsabellaNeural", 1.0),
 "c1": ("Eccomi!", "it-IT-ElsaNeural", 1.12),
 "s1": ("Siamo qui!", "it-IT-IsabellaNeural", 0.93),
 "m3": ("Puliamo tutto insieme!", "it-IT-IsabellaNeural", 1.0),
 "m4": ("La bottiglia va nel giallo!", "it-IT-IsabellaNeural", 1.0),
 "c2": ("La carta va nel blu!", "it-IT-ElsaNeural", 1.12),
 "s2": ("La buccia va nel marrone!", "it-IT-IsabellaNeural", 0.93),
 "m5": ("Bravissimi! Ancora un po'!", "it-IT-IsabellaNeural", 1.0),
 "m6": ("Il parco è pulito!", "it-IT-IsabellaNeural", 1.0),
 "c3": ("Evviva!", "it-IT-ElsaNeural", 1.12),
 "s3": ("Grazie amici!", "it-IT-IsabellaNeural", 0.93),
 "m7": ("Ciao ciao bambini!", "it-IT-IsabellaNeural", 1.0),
}
async def gen():
    for k, (txt, v, p) in LINES.items():
        await edge_tts.Communicate(txt, v, rate="-6%").save(f"audio/{k}_raw.mp3")
asyncio.run(gen())
dur = {}
for k, (txt, v, p) in LINES.items():
    af = f"asetrate=24000*{p},atempo={1/p},aresample=44100," if p != 1.0 else ""
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"audio/{k}_raw.mp3","-ac","1","-ar","44100","-af",
        "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.1,areverse,"+af+"loudnorm=I=-16:TP=-1.5,aresample=44100","-c:a","pcm_s16le",f"audio/{k}.wav"],check=True)
    dur[k] = round(float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"audio/{k}.wav"])), 2)
json.dump(dur, open("audio/durate.json","w")); print(dur)
