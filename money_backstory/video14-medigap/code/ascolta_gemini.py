"""Fa ascoltare ogni blocco a Gemini (gemini-3.8-flash, ascolta l'audio) e confronta parola per parola col copione (numeri in parole). Uso: python3 code/ascolta_gemini.py 1,2,3"""
import sys, json, base64, re, time, subprocess, urllib.request, urllib.error, difflib
from numw import num2words, norm_words
J = json.load(open('code/blk.json'))['B']
def ask(b):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'voce/b{b}.wav', '-ac', '1', '-ar', '16000', f'/tmp/claude-0/g_b{b}.wav'], check=True)
    a = base64.b64encode(open(f'/tmp/claude-0/g_b{b}.wav', 'rb').read()).decode()
    body = {"contents": [{"parts": [{"inline_data": {"mime_type": "audio/wav", "data": a}}, {"text": "Transcribe exactly what is said, word for word, including every number and every repeated or missing word. Do not correct or summarize. Output only the transcript."}]}]}
    for t in range(12):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}), timeout=180))
            return d['candidates'][0]['content']['parts'][0]['text']
        except Exception as e: time.sleep(15)
    return None
if __name__ == '__main__':
  for b in [int(x) for x in sys.argv[1].split(',')]:
      txt = ask(b)
      if not txt: print(b, 'NESSUNA RISPOSTA'); continue
      open(f'voce/gemini_b{b}.txt', 'w').write(txt)
      s = norm_words(J[str(b)]); g = norm_words(txt)
      sm = difflib.SequenceMatcher(None, s, g, autojunk=False); diffs = [(op, ' '.join(s[i1:i2]), ' '.join(g[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
      print(b, 'parole copione', len(s), 'gemini', len(g), 'differenze', len(diffs), flush=True)
      for d in diffs: print('   ', d)
