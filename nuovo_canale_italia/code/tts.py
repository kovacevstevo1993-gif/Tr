import sys,json,base64,subprocess,urllib.request
model,voice,out,text=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
body={"contents":[{"parts":[{"text":text}]}],"generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":voice}}}}}
r=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
d=json.load(urllib.request.urlopen(r,timeout=180))
pcm=base64.b64decode(d["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
open(out+".pcm","wb").write(pcm)
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","s16le","-ar","24000","-ac","1","-i",out+".pcm","-b:a","128k",out+".mp3"],check=True)
print(out, len(pcm)/48000,"s")
