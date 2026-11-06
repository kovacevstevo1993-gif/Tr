#!/usr/bin/env python3
"""CONTROLLO "UNA DOMANDA = SOLO UNA RISPOSTA" (Conti in Pensione, 05/11/2026, ordine utente: "metti il controllo").
Errore ripetuto: l'utente fa una domanda o una critica con "?" e io modifico file, rimando il copione, faccio commit.
- modo `prompt` (UserPromptSubmit): se il messaggio contiene "?" e NESSUN verbo di ordine, crea il blocco per la sessione e stampa l'avviso.
- modo `guard` (PreToolUse su Edit/Write/NotebookEdit/SendUserFile/Bash): se il blocco c'e', NEGA scritture, commit, push, invii di file.
  Eccezione: scrivere le regole (REGOLE-FISSE.md, CHECKLIST-REGOLE.md), perche' ogni errore va salvato subito (regola N.4).
Il blocco cade al primo messaggio dell'utente senza "?" o con un verbo di ordine. Vale solo nelle sessioni del canale Conti in Pensione."""
import json,os,re,sys
modo=sys.argv[1] if len(sys.argv)>1 else 'prompt'
try: d=json.load(sys.stdin)
except Exception: d={}
sid=str(d.get('session_id','x'))
base='/tmp/conti_sessions'; os.makedirs(base,exist_ok=True)
conti=os.path.exists(os.path.join(base,sid)); flag=os.path.join(base,'solo-'+sid)
ORDINI=r"\b(manda|mandami|mandalo|mandala|invia|fai|fallo|falla|fammi|rifai|rifallo|crea|procedi|scrivi|scrivimi|aggiungi|metti|mettilo|correggi|correggilo|cambia|cambialo|salva|salvalo|collega|togli|toglilo|sistema|sistemalo|elimina|cancella|ordino|vai|controlla|cerca|cercami|verifica|prosegui|continua|applica)\b"
if modo=='prompt':
    p=str(d.get('prompt',''))
    if '?' in p and not re.search(ORDINI,p,re.I) and conti:
        open(flag,'w').write('1')
        print("=== BLOCCO ATTIVO (hook solo-risposta): questo messaggio dell'utente e' una DOMANDA. Rispondi in 1-2 righe. VIETATO: modificare file, fare commit/push, mandare copioni o file, avviare lavori. Le scritture sono bloccate dal sistema finche' l'utente non scrive un ordine (senza '?' o con un verbo di ordine). Unica eccezione: salvare una regola in REGOLE-FISSE.md. ===")
    elif os.path.exists(flag):
        os.remove(flag)
    sys.exit(0)
# modo guard
if not os.path.exists(flag): sys.exit(0)
tool=str(d.get('tool_name','')); ti=d.get('tool_input',{}) or {}
RULES=('REGOLE-FISSE.md','CHECKLIST-REGOLE.md')
blocca=False
if tool in('Edit','Write','NotebookEdit'):
    fp=str(ti.get('file_path',''))
    blocca=not any(fp.endswith(r) for r in RULES)
elif tool=='SendUserFile':
    blocca=True
elif tool=='Bash':
    c=str(ti.get('command',''))
    scrive=re.search(r"git (commit|push|add|merge)|>>|(?<![0-9&=>-])>(?![&>=])\s*(?!/dev/null)\S|\btee\b|sed -i|\brm\b|\bmv\b|\bcp\b|open\([^)]*['\"][wa]",c)
    blocca=bool(scrive) and not any(r in c for r in RULES)
if blocca:
    sys.stderr.write("BLOCCATO dall'hook solo-risposta: l'ultimo messaggio dell'utente e' una DOMANDA (ha il '?'). Rispondi in 1-2 righe senza modificare file, fare commit o mandare copioni. Si sblocca quando l'utente scrive un ordine.")
    sys.exit(2)
sys.exit(0)
