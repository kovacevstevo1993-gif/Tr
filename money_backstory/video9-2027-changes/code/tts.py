import json,sys,base64,subprocess,urllib.request,urllib.error,time
voice,text,out=sys.argv[1],sys.argv[2],sys.argv[3]
model=sys.argv[4] if len(sys.argv)>4 else 'gemini-3.8-flash-tts'
body={"contents":[{"parts":[{"text":text}]}],"generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":voice}}}}}
for i in range(8):
    try:
        req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
        d=json.load(urllib.request.urlopen(req,timeout=300)); break
    except urllib.error.HTTPError as e:
        print('err',e.code,e.read()[:200],file=sys.stderr); time.sleep(15*(i+1))
p=d['candidates'][0]['content']['parts'][0]['inlineData']
raw=base64.b64decode(p['data'])
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','s16le','-ar','24000','-ac','1','-i','-',out],input=raw,check=True)
print(out)
