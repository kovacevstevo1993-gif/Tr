"""SINCRONIA CON LA VOCE (06/10/2026). Problema dell'utente: "le slide non stanno dietro alla voce, saltano".
Causa: i tagli delle slide e i tempi degli elementi erano stimati dal testo. Qui si MISURANO dall'audio reale.
1) L'utente esporta l'audio della voce (tutto il video, mp3/wav, voce 1.0 come nella timeline).
2) python3 sync_voce.py voce.mp3 copione.md out.json [fine_blocchi.txt]   (riconoscimento vocale locale, gratis, niente crediti)
3) Il modello usa out.json: tagli ai confini delle frasi, ogni elemento compare quando la voce dice la sua parola chiave (max 80%).
fine_blocchi.txt (opzionale): una riga per blocco, fine voce in fotogrammi (dagli screenshot dell'utente): se c'e', i confini dei blocchi vengono da li."""
import sys, re, json, difflib

def parse_copione(path):
    blocks = {}; cur = None
    for line in open(path, encoding='utf-8'):
        m = re.match(r'\s*\**BLOCCO\s+(\d+)\**\s*$', line)
        if m: cur = int(m.group(1)); blocks[cur] = []; continue
        if cur and line.strip() and not line.startswith('#'): blocks[cur].append(line.strip())
    return {b: ' '.join(v) for b, v in blocks.items()}

def norm(w): return re.sub(r"[^a-z0-9']", '', w.lower())

def transcribe(audio, model='base.en'):
    import subprocess, numpy as np
    from faster_whisper import WhisperModel
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', audio, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True, check=True).stdout
    pcm = np.frombuffer(raw, dtype=np.float32)      # qualsiasi formato (mp3, wav, mp4) via ffmpeg
    m = WhisperModel(model, device='cpu', compute_type='int8')
    segs, _ = m.transcribe(pcm, word_timestamps=True, language='en', beam_size=5, vad_filter=False)
    return [(norm(w.word), w.start, w.end) for s in segs for w in s.words if norm(w.word)]

def align(blocks, asr):
    """copione (parole in ordine) <-> parole riconosciute: tempo di ogni parola del copione (interpolato dove manca)."""
    cw = []   # (blocco, indice, parola)
    for b in sorted(blocks):
        for i, w in enumerate(blocks[b].split()): cw.append((b, i, w))
    a = [norm(w) for _, _, w in cw]; r = [w for w, _, _ in asr]
    sm = difflib.SequenceMatcher(None, a, r, autojunk=False); t = [None] * len(cw)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): t[blk.a + k] = (asr[blk.b + k][1], asr[blk.b + k][2])
    # interpolazione fra parole agganciate
    idx = [i for i, x in enumerate(t) if x]
    if not idx: raise SystemExit('nessuna parola riconosciuta: audio sbagliato?')
    for i in range(len(t)):
        if t[i]: continue
        p = max([j for j in idx if j < i], default=None); n = min([j for j in idx if j > i], default=None)
        if p is None: s = max(0, t[n][0] - 0.3 * (n - i)); t[i] = (s, s + 0.3)
        elif n is None: s = t[p][1] + 0.3 * (i - p - 1); t[i] = (s, s + 0.3)
        else:
            f = (i - p) / (n - p); s = t[p][1] + (t[n][0] - t[p][1]) * f * 0.98; t[i] = (s, s + 0.25)
    out = {}
    for (b, i, w), (s, e) in zip(cw, t): out.setdefault(b, []).append([w, round(s, 3), round(e, 3)])
    cov = len(idx) / len(cw)
    return out, cov

def main():
    audio, cop, outp = sys.argv[1:4]
    blocks = parse_copione(cop); asr = transcribe(audio); words, cov = align(blocks, asr)
    ends = None
    if len(sys.argv) > 4: ends = [int(x.strip()) for x in open(sys.argv[4]) if x.strip()]
    res = {'coverage': round(cov, 3), 'blocks': {}}
    for b, ws in words.items():
        start = (ends[b - 2] / 30 if ends and b > 1 else (words[b - 1][-1][2] if b > 1 else 0.0)) if b > 1 else 0.0
        res['blocks'][b] = {'start': round(start, 3), 'end': round(ends[b - 1] / 30, 3) if ends else ws[-1][2], 'words': ws}
    json.dump(res, open(outp, 'w'), indent=1); print('parole agganciate:', round(cov * 100, 1), '%', '->', outp)

class Voice:
    """Uso nelle slide: V = Voice('out.json'); V.at(blocco, 'frase') = secondi (dall'inizio del blocco) in cui la voce dice la frase."""
    def __init__(self, path): self.j = json.load(open(path))['blocks']
    def words(self, b): return self.j[str(b)]['words']
    def start(self, b): return self.j[str(b)]['start']
    def at(self, b, phrase, rel=True):
        ph = [norm(x) for x in phrase.split()]; ws = self.words(b); nw = [norm(w[0]) for w in ws]
        for i in range(len(nw) - len(ph) + 1):
            if nw[i:i + len(ph)] == ph: return ws[i][1] - (self.start(b) if rel else 0)
        raise KeyError(f'frase non trovata nel blocco {b}: {phrase}')
    def sentences(self, b):
        """(inizio, fine) di ogni frase, in secondi dall'inizio del blocco"""
        ws = self.words(b); s0 = self.start(b); out = []; st = 0
        for i, (w, a, e) in enumerate(ws):
            if i == len(ws) - 1 or (i + 1 < len(ws) and ws[i + 1][1] - e > 0.28):
                out.append((ws[st][1] - s0, e - s0)); st = i + 1
        return out
    def plan(self, b, n):
        """SPEC del blocco: n slide, tagli = inizio frase piu' vicino ai punti equidistanti; somma = durata dal blocco (fotogrammi)."""
        d = self.j[str(b)]; D = d['end'] - d['start']; sen = [s for s, _ in self.sentences(b)] + [D]
        cuts = [0.0]
        for k in range(1, n):
            target = D * k / n; c = min(sen[1:-1] or [target], key=lambda x: abs(x - target))
            if c > cuts[-1] + 3.0: cuts.append(c)
        cuts.append(D); fr = [round(c * 30) for c in cuts]; fr[-1] = round(D * 30)
        return [fr[i + 1] - fr[i] for i in range(len(fr) - 1)]

if __name__ == '__main__': main()
