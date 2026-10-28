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
        # 28/10/2026: il promemoria intero (13,7 KB) superava il limite dell'output dell'hook e a Claude arrivavano solo i primi 2 KB (regole 1-4): le regole sui copioni non venivano mai viste (utente: 'devi leggerli anche te'). Ora due parti, ciascuna sotto i 10 KB: parte 1 = come lavorare, ricerca, copioni, testi; parte 2 = slide, miniature, commenti, temi gia' fatti.
        parte=sys.argv[1] if len(sys.argv)>1 else '1'
        righe=open(f,encoding='utf-8').read().split('\n')
        teste=['COME LAVORARE','RICERCA E SCELTA','COPIONI','TESTI (','SLIDE / CLIP','MINIATURE','RISPOSTE AI COMMENTI']
        sez={};cur='intro'
        for l in righe:
            for h in teste:
                if l.startswith(h):cur=h
            sez.setdefault(cur,[]).append(l)
        p1=['intro','COME LAVORARE','RICERCA E SCELTA','COPIONI','TESTI (']
        p2=['SLIDE / CLIP','MINIATURE','RISPOSTE AI COMMENTI']
        scelte=p1 if parte=='1' else p2
        print('=== PROMEMORIA OBBLIGATORIO parte '+parte+'/2 (hook, a ogni messaggio): LEGGERLO PER INTERO e applicare TUTTE queste regole prima di rispondere e prima di consegnare. Regole complete: conti_in_pensione/REGOLE-FISSE.md ===')
        for s in scelte: print('\n'.join(sez.get(s,[])))
        if parte=='2':
            t=os.path.join(root,'conti_in_pensione','TEMI-FATTI.md')  # 22/10/2026: errore video 10 (tema gia' fatto proposto come nuovo): la lista dei temi fatti sempre davanti
            if os.path.exists(t): print(open(t,encoding='utf-8').read())
