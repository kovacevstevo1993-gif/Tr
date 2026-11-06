"""Una sola richiesta TTS (niente ripetizioni): stampa l'errore di quota se c'e'."""
import json,sys,base64,subprocess,urllib.request,urllib.error
voice,text,out,model=sys.argv[1:5]
body={"contents":[{"parts":[{"text":text}]}],"generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":voice}}}}}
try:
    d=json.load(urllib.request.urlopen(urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"}),timeout=300))
except urllib.error.HTTPError as e:
    m=e.read().decode(); import re; print('ERR',e.code,re.findall(r'quotaId": "([^"]+)',m),re.findall(r'retry in ([^"]+?)\.',m)); sys.exit(1)
raw=base64.b64decode(d['candidates'][0]['content']['parts'][0]['inlineData']['data'])
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','s16le','-ar','24000','-ac','1','-i','-',out],input=raw,check=True); print('OK',out)
