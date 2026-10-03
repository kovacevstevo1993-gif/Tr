import subprocess, json
from gtts import gTTS
LINES = {
 "m1": ("Oh no! Quanti rifiuti nel parco!", 1.15),
 "m2": ("Chiamiamo gli amici! Chip! Spike!", 1.15),
 "c1": ("Eccomi!", 1.4),
 "s1": ("Siamo qui!", 0.95),
 "m3": ("Puliamo tutto insieme!", 1.15),
 "m4": ("La bottiglia va nel giallo!", 1.15),
 "c2": ("La carta va nel blu!", 1.4),
 "s2": ("La buccia va nel marrone!", 0.95),
 "m5": ("Bravissimi! Ancora un po'!", 1.15),
 "m6": ("Il parco è pulito!", 1.15),
 "c3": ("Evviva!", 1.4),
 "s3": ("Grazie amici!", 0.95),
 "m7": ("Ciao ciao bambini!", 1.15),
}
for k,(txt,p) in LINES.items():
    gTTS(txt, lang="it", slow=False).save(f"audio/{k}_raw.mp3")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"audio/{k}_raw.mp3","-af",
      f"asetrate=24000*{p},atempo={1/p},aresample=44100,loudnorm=I=-16:TP=-1.5","audio/%s.wav"%k],check=True)
    d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"audio/{k}.wav"]))
    print(k,round(d,2),txt)
