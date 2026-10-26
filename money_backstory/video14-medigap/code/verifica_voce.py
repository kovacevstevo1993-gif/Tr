import json,subprocess,numpy as np,re,sys
from faster_whisper import WhisperModel
M=WhisperModel('small.en',device='cpu',compute_type='int8'); J=json.load(open('code/blk.json'))['B']
for b in range(1,21):
    raw=subprocess.run(['ffmpeg','-loglevel','error','-i',f'voce/b{b}.wav','-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout
    segs,_=M.transcribe(np.frombuffer(raw,np.float32),language='en'); t=' '.join(s.text.strip() for s in segs).split()
    sc=J[str(b)].split()
    print(b,'| INIZIO asr:',' '.join(t[:4]),'| copione:',' '.join(sc[:4]),'|| FINE asr:',' '.join(t[-4:]),'| copione:',' '.join(sc[-4:]),'| dur',round(len(raw)/4/16000,1))
