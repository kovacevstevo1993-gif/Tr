#!/usr/bin/env python3
"""UserPromptSubmit: se la chat riguarda il canale The Senior Advantage, stampa la checklist delle regole a OGNI messaggio dell'utente (ordine utente 22/10/2026: "mentre lavori cerchi tutto e applichi tutte le regole"). Altri canali: non stampa niente."""
import json,os,re,sys
try: d=json.load(sys.stdin)
except Exception: d={}
sid=str(d.get('session_id','x'));prompt=str(d.get('prompt',''))
marker='/tmp/senior_sessions';os.makedirs(marker,exist_ok=True);mf=os.path.join(marker,sid)
kw=re.compile(r'senior.advantage|senior_advantage|theseniorAdvantage',re.I)  # solo parole SPECIFICHE del canale Senior Advantage, cercate SOLO nei messaggi scritti dall'utente (non nell'output dell'hook di avvio, che nomina tutti i canali)
if not os.path.exists(mf):
    hit=bool(kw.search(prompt))
    tp=d.get('transcript_path')
    if not hit and tp and os.path.exists(tp):
        try:
            for line in open(tp,encoding='utf-8',errors='ignore'):
                try: o=json.loads(line)
                except Exception: continue
                c=o.get('message',{}).get('content') if o.get('type')=='user' else None
                if isinstance(c,str) and not c.lstrip().startswith('<') and kw.search(c): hit=True; break
        except Exception: pass
    if hit: open(mf,'w').write('1')
if os.path.exists(mf):
    root=os.environ.get('CLAUDE_PROJECT_DIR','.')
    f=os.path.join(root,'senior_advantage','CHECKLIST-REGOLE.md')
    if os.path.exists(f):
        print('=== PROMEMORIA OBBLIGATORIO (hook, a ogni messaggio): applica TUTTE queste regole mentre lavori, prima di rispondere e prima di consegnare ===')
        print(open(f,encoding='utf-8').read())
