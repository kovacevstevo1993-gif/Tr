#!/usr/bin/env python3
"""Stop hook (22/10/2026, utente: "continui a ripetere che non lo rifarai e lo rifai"): nelle chat di Conti in Pensione
impedisce di chiudere la risposta se un copione cambiato (non committato, o committato dopo DAL) non ha la revisione
scritta di ogni blocco (conti_in_pensione/qa/revisione.py). Usa git, non le date dei file (un clone nuovo le cambia tutte).
Altri canali: non fa niente."""
import json,os,subprocess,sys
DAL='2026-10-22T21:00:00Z'  # i copioni gia' consegnati prima di questa data non si toccano
try: d=json.load(sys.stdin)
except Exception: d={}
if not os.path.exists(os.path.join('/tmp/conti_sessions',str(d.get('session_id','x')))): sys.exit(0)
root=os.environ.get('CLAUDE_PROJECT_DIR','.')
def git(*a): return subprocess.run(['git',*a],cwd=root,capture_output=True,text=True).stdout
cambiati=set(l[3:].strip() for l in git('status','--porcelain').splitlines())
cambiati|=set(l.strip() for l in git('log','--since='+DAL,'--name-only','--format=').splitlines())
err=[]
for f in sorted(x for x in cambiati if x.startswith('conti_in_pensione/') and x.endswith('/copione-blocchi.txt')):
    p=os.path.join(root,f)
    if not os.path.exists(p): continue
    r=subprocess.run([sys.executable,os.path.join(root,'conti_in_pensione','qa','revisione.py'),'controlla',p],capture_output=True,text=True)
    if r.returncode!=0: err.append(f+':\n'+r.stdout.strip())
if err:
    sys.stderr.write('BLOCCO REVISIONE (non consegnare): rileggi italiano, logica, persona e numeri di ogni blocco e scrivi revisione-copione.txt (python3 qa/revisione.py modello <copione>).\n'+'\n'.join(err)+'\n')
    sys.exit(2)
sys.exit(0)
