#!/usr/bin/env python3
"""REVISORE ESTERNO (28/10/2026, short 15: 9 versioni; utente: 'non in parte, tutto devi risolvere').
Un secondo modello (Gemini, via proxy) legge il copione come madrelingua italiano e segnala SOLO difetti CERTI
(errori, frasi non naturali, riferimenti ambigui, persona mista, refusi, incoerenze, ripetizioni). Cattura anche i difetti
di tipo nuovo che qa_italiano.py non conosce. Registra l'esito in revisore-esterno.log legato all'impronta del testo:
revisione.py controlla (cartelle 32+) blocca la consegna se manca l'esito 'NESSUN DIFETTO CERTO' per il testo attuale.
Uso: python3 qa/revisore_esterno.py <cartella>/copione-blocchi.txt"""
import json,os,re,sys,time,hashlib,urllib.request
MODELLI=['gemini-3.5-flash','gemini-2.5-pro','gemini-3.1-pro-preview','gemini-3.8-flash']
def blocchi(f):
    return [(int(m.group(1)),m.group(2)) for m in (re.match(r'^(\d+)\|\s*(.+)$',l.strip()) for l in open(f,encoding='utf-8')) if m]
def impronta(bl): return hashlib.sha1(' '.join(t for _,t in bl).strip().encode()).hexdigest()[:10]
PROMPT="""Sei un revisore madrelingua italiano molto severo. Qui sotto c'e' il copione di uno SHORT YouTube sulle pensioni, letto da una voce sintetica a un pubblico di persone anziane ("tu" allo spettatore, "noi" per il canale). Controlla blocco per blocco e frase per frase: grammatica, refusi, frasi che un italiano non direbbe, espressioni ambigue (a chi/cosa si riferisce?), cambi di persona (tu/impersonale/noi) nello stesso blocco, frasi senza verbo usate come apertura, incoerenze logiche, ripetizioni fastidiose tra blocchi vicini, numeri o date scritti in modo strano. NON proporre varianti di stile e NON fare osservazioni sul contenuto fiscale. ATTENZIONE: numeri, anni e date sono scritti volutamente in LETTERE perche' li legge una voce sintetica: NON segnalarli. L'uso di 'loro' per cose, 'noi' del canale e le domande retoriche sono voluti. Cita la frase ESATTAMENTE come e' scritta, copiandola carattere per carattere. Segnala SOLO difetti che ti sembrano CERTI (un italiano li noterebbe e li giudicherebbe sbagliati o poco naturali); se hai solo un dubbio mettilo con gravita "dubbio". Rispondi SOLO con JSON: {"difetti":[{"blocco":N,"frase":"testo esatto","problema":"cosa non va","gravita":"certo|dubbio","correzione":"frase corretta"}]}. Se non trovi difetti certi: {"difetti":[]}.

COPIONE:
"""
def chiedi(bl):
    corpo={"contents":[{"parts":[{"text":PROMPT+'\n'.join(f'Blocco {n}: {t}' for n,t in bl)}]}],"generationConfig":{"temperature":0,"responseMimeType":"application/json"}}
    ultimo=None
    for tent in range(3):
        for m in MODELLI:
            rq=urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent',data=json.dumps(corpo).encode(),headers={'Content-Type':'application/json','x-goog-api-key':'dummy'})
            try:
                r=json.load(urllib.request.urlopen(rq,timeout=180))
                d=json.loads(r['candidates'][0]['content']['parts'][0]['text']); d['_modello']=m; return d
            except Exception as e: ultimo=f'{m}: {e}'
        time.sleep(20)
    raise SystemExit('REVISORE ESTERNO NON RAGGIUNGIBILE: '+str(ultimo))
if __name__=='__main__':
    if os.environ.get('GEMINI_OK')!='1': sys.exit('BLOCCATO: usa Gemini, lo stesso limite del canale Money Backstory. Lanciare solo se l utente conferma (GEMINI_OK=1). Vedi REGOLE-FISSE.md 28/10.')
    f=sys.argv[1]; bl=blocchi(f); d=chiedi(bl); dif=d.get('difetti',[])
    testo={n:t for n,t in bl}
    certi=[x for x in dif if x.get('gravita')=='certo' and str(x.get('frase','')).strip()[:40] in testo.get(x.get('blocco'),'')]
    print('modello:',d.get('_modello'))
    for x in dif: print(f"[{x.get('gravita')}] blocco {x.get('blocco')}: \"{x.get('frase')}\" -> {x.get('problema')} | proposta: {x.get('correzione')}")
    if '--prova' not in sys.argv:
        open(os.path.join(os.path.dirname(os.path.abspath(f)),'revisore-esterno.log'),'a').write(f"{impronta(bl)}|{len(certi)}|{time.time()}\n")
    print('NESSUN DIFETTO CERTO' if not certi else f'{len(certi)} DIFETTI CERTI: correggere e rilanciare')
    sys.exit(1 if certi else 0)
