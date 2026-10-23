"""Fa ascoltare ogni blocco a Gemini (gemini-3.8-flash, ascolta l'audio) e confronta parola per parola col copione (numeri in parole). Uso: python3 code/ascolta_gemini.py 1,2,3"""
import sys, json, base64, re, time, subprocess, urllib.request, urllib.error, difflib
ONES="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS="_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def num2words(n):
    if isinstance(n, float):
        i = int(n); fr = str(n).split('.')[1]
        return num2words(i) + ' point ' + ' '.join(ONES[int(c)] for c in fr)
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10] + ('' if n % 10 == 0 else ' ' + ONES[n % 10])
    if n < 1000: return ONES[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' ' + num2words(n % 100))
    if n < 1000000: return num2words(n // 1000) + ' thousand' + ('' if n % 1000 == 0 else ' ' + num2words(n % 1000))
    return str(n)
J = json.load(open('code/blk.json'))['B']
def norm_words(t):
    t = t.replace('½', ' and a half').replace('%', ' percent'); t = re.sub(r'\$(\d[\d,]*(?:\.\d+)?)', r'\1 dollars', t)
    t = re.sub(r'(\d),(\d)', r'\1\2', t)
    def nm(m):
        x = m.group(0)
        try: return ' ' + num2words(float(x) if '.' in x else int(x)).replace(' and ', ' ').replace(',', '').replace('-', ' ').replace(' point ', ' point ') + ' '
        except: return x
    t = re.sub(r'\d+(?:\.\d+)?', nm, t)
    t = re.sub(r'\bI\.? ?R\.? ?S\.?\b', 'i r s', t); t = re.sub(r'\bIRAs?\b', 'i r a', t, flags=re.I); t = re.sub(r'\bIRS\b', 'i r s', t)
    t = t.replace('-', ' ')
    w = re.sub(r"[^a-z' ]", ' ', t.lower()).split()
    return w
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
for b in [int(x) for x in sys.argv[1].split(',')]:
    txt = ask(b)
    if not txt: print(b, 'NESSUNA RISPOSTA'); continue
    open(f'voce/gemini_b{b}.txt', 'w').write(txt)
    s = norm_words(J[str(b)]); g = norm_words(txt)
    sm = difflib.SequenceMatcher(None, s, g, autojunk=False); diffs = [(op, ' '.join(s[i1:i2]), ' '.join(g[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
    print(b, 'parole copione', len(s), 'gemini', len(g), 'differenze', len(diffs), flush=True)
    for d in diffs: print('   ', d)
