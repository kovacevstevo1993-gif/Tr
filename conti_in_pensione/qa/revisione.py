#!/usr/bin/env python3
"""REVISIONE OBBLIGATORIA DEL COPIONE (22/10/2026, utente: "continui a ripetere che non lo rifarai e lo rifai").
Le promesse non bastano: un copione si consegna solo se esiste la revisione scritta di OGNI blocco, legata al testo
con un'impronta (hash). Se cambia anche una parola di un blocco, l'impronta non torna piu' e quel blocco va riletto.
Uso (dalla cartella conti_in_pensione):
  python3 qa/revisione.py modello  <cartella>/copione-blocchi.txt   -> stampa le righe da compilare
  python3 qa/revisione.py controlla <cartella>/copione-blocchi.txt  -> exit 1 se la revisione manca o non torna
File di revisione: <cartella>/revisione-copione.txt, una riga per blocco:
  N | impronta | italiano OK | logica OK | persona OK | numeri OK | nota
(italiano = suona come lo direbbe un italiano a voce; logica = soggetti, riferimenti e promesse giusti;
 persona = stessa persona tu/lei/noi nel blocco; numeri = conti rifatti e numeri annunciati contati)"""
import hashlib,os,re,sys
CAMPI=('italiano','logica','persona','numeri')
def blocchi(f):
    out=[]
    for l in open(f,encoding='utf-8'):
        m=re.match(r'^(\d+)\|\s*(.+)$',l.strip())
        if m: out.append((int(m.group(1)),m.group(2)))
    return out
def impronta(t): return hashlib.sha1(t.strip().encode('utf-8')).hexdigest()[:10]
def controlla(f):
    rev=os.path.join(os.path.dirname(f),'revisione-copione.txt')
    if not os.path.exists(rev): return [f'manca {rev}']
    righe={}
    for l in open(rev,encoding='utf-8'):
        p=[x.strip() for x in l.split('|')]
        if len(p)>=6 and p[0].isdigit(): righe[int(p[0])]=p
    err=[]
    for n,t in blocchi(f):
        p=righe.get(n)
        if not p: err.append(f'blocco {n}: nessuna riga di revisione'); continue
        if p[1]!=impronta(t): err.append(f'blocco {n}: testo cambiato dopo la revisione (rileggerlo)')
        for i,c in enumerate(CAMPI):
            if p[2+i].lower()!=f'{c} ok': err.append(f'blocco {n}: {c} non confermato ("{p[2+i]}")')
        if 'DA CORREGGERE' in '|'.join(p).upper(): err.append(f'blocco {n}: segnato DA CORREGGERE')
    return err
if __name__=='__main__':
    if len(sys.argv)<3: sys.exit(__doc__)
    modo,f=sys.argv[1],sys.argv[2]
    if modo=='modello':
        for n,t in blocchi(f): print(f'{n} | {impronta(t)} | italiano ? | logica ? | persona ? | numeri ? | ')
    else:
        e=controlla(f)
        for x in e: print('REVISIONE:',x)
        print('REVISIONE OK' if not e else f'REVISIONE NON FATTA ({len(e)}): NON CONSEGNARE'); sys.exit(1 if e else 0)
