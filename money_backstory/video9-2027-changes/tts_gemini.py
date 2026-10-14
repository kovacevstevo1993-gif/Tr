import json,sys,base64,subprocess,urllib.request
voice,text,out=sys.argv[1],sys.argv[2],sys.argv[3]
model=sys.argv[4] if len(sys.argv)>4 else 'gemini-3.8-flash-tts'
body={"contents":[{"parts":[{"text":text}]}],"generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":voice}}}}}
req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
d=json.load(urllib.request.urlopen(req,timeout=300))
p=d['candidates'][0]['content']['parts'][0]['inlineData']
raw=base64.b64decode(p['data'])
open(out+'.pcm','wb').write(raw)
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','s16le','-ar','24000','-ac','1','-i',out+'.pcm',out],check=True)
print(out,p['mimeType'])
