#!/usr/bin/env python3
"""UserPromptSubmit: se la chat riguarda il canale Conti in Pensione, stampa la checklist delle regole a OGNI messaggio dell'utente (cosi' le regole sono sempre davanti, non a memoria). Altri canali: non stampa niente."""
import json,os,re,sys
try: d=json.load(sys.stdin)
except Exception: d={}
sid=str(d.get('session_id','x'));prompt=str(d.get('prompt',''))
marker='/tmp/conti_sessions';os.makedirs(marker,exist_ok=True);mf=os.path.join(marker,sid)
kw=re.compile(r'contiinpensione|conti_in_pensione|\binps\b|tredicesima|rivalutazion|REGOLE-FISSE',re.I)  # solo parole SPECIFICHE del canale Conti (14/10/2026: prima 'miniatur', 'short N', 'video N' attivavano la checklist anche sugli altri canali e costava ~1.3k token a ogni messaggio)
if kw.search(prompt) and not os.path.exists(mf): open(mf,'w').write('1')
if os.path.exists(mf):
    root=os.environ.get('CLAUDE_PROJECT_DIR','.')
    f=os.path.join(root,'conti_in_pensione','CHECKLIST-REGOLE.md')
    if os.path.exists(f):
        print('=== PROMEMORIA OBBLIGATORIO (hook, a ogni messaggio): applica TUTTE queste regole prima di rispondere e prima di consegnare. Regole complete: conti_in_pensione/REGOLE-FISSE.md ===')
        print(open(f,encoding='utf-8').read())
        t=os.path.join(root,'conti_in_pensione','TEMI-FATTI.md')  # 22/10/2026: errore video 10 (tema gia' fatto proposto come nuovo): la lista dei temi fatti sempre davanti
        if os.path.exists(t): print(open(t,encoding='utf-8').read())
