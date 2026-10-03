import subprocess, json, asyncio, certifi
certifi.where = lambda: "/root/.ccr/ca-bundle.crt"
import edge_tts
LINES = {
 "n1": "Oh no! Quanti rifiuti nel parco!",
 "n2": "Ma io so cosa fare! Raccolgo tutto!",
 "n3": "La bottiglia va nel giallo!",
 "n4": "La carta va nel blu!",
 "n5": "La buccia va nel marrone!",
 "n6": "Ancora un po'!",
 "n7": "Il parco è pulito!",
 "n8": "Ciao ciao bambini!",
}
async def gen():
    for k, t in LINES.items(): await edge_tts.Communicate(t, "it-IT-IsabellaNeural", rate="-6%").save(f"audio/{k}_raw.mp3")
asyncio.run(gen())
dur = json.load(open("audio/durate.json"))
for k in LINES:
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"audio/{k}_raw.mp3","-ac","1","-ar","44100","-af",
     "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.1,areverse,loudnorm=I=-16:TP=-1.5,aresample=44100","-c:a","pcm_s16le",f"audio/{k}.wav"],check=True)
    dur[k] = round(float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"audio/{k}.wav"])),2)
json.dump(dur, open("audio/durate.json","w")); print({k:dur[k] for k in LINES})
