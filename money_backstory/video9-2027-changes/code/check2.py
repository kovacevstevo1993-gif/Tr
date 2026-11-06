import sys, json, re, subprocess, numpy as np
from faster_whisper import WhisperModel
J = json.load(open(sys.argv[1]))['B']; M = WhisperModel('small.en', device='cpu', compute_type='int8')
for b in map(int, sys.argv[2].split(',')):
    raw = subprocess.run(['ffmpeg','-loglevel','error','-i',f'voce/b{b}.wav','-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout
    s,_ = M.transcribe(np.frombuffer(raw,np.float32), language='en'); t = ' '.join(x.text.strip() for x in s).split()
    e = J[str(b)].split()
    print(f'b{b} {len(raw)/4/16000:.2f}s\n  GOT: {" ".join(t[:6])} ... {" ".join(t[-6:])}\n  EXP: {" ".join(e[:6])} ... {" ".join(e[-6:])}', flush=True)
