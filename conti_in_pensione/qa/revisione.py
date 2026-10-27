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
def fidelizzazione(f):
    """BLOCCO FIDELIZZAZIONE (25/10/2026, errore video 11: risposta data nel primo minuto, utente: 'ma che senso ha scrivere regole se non le segui?').
    Vale per i copioni LUNGHI (>= 10 blocchi) in cartelle dal 30 in poi (dal video 12). File fidelizzazione-copione.txt con:
    PRIMO_MINUTO_RIVELA: <cosa si scopre nei blocchi 1-4> (almeno 20 caratteri)
    RISPOSTA_TENUTA: blocco N   (N oltre meta' del video)
    CERCHIO_1: aperto in blocco A, chiuso in blocco B   (A <= 4, B oltre meta')
    CERCHIO_2: aperto in blocco A, chiuso in blocco B
    CIFRA_GANCIO: <la cifra piu' grande vera, per anno se serve>
    IMPRONTA_PRIMI4: <impronta dei blocchi 1-4>   (cambia se cambia uno dei primi 4 blocchi)"""
    bl=blocchi(f); cart=os.path.basename(os.path.dirname(os.path.abspath(f)))
    m=re.match(r'^(\d+)-',cart)
    if len(bl)<10 or not m or int(m.group(1))<30: return []
    fp=os.path.join(os.path.dirname(f),'fidelizzazione-copione.txt')
    if not os.path.exists(fp): return [f'manca {fp} (controllo fidelizzazione: vedi qa/revisione.py)']
    T=open(fp,encoding='utf-8').read(); n=len(bl); err=[]
    def campo(k):
        mm=re.search(r'^'+k+r':\s*(.+)$',T,re.M); return mm.group(1).strip() if mm else None
    v=campo('PRIMO_MINUTO_RIVELA')
    if not v or len(v)<20: err.append('PRIMO_MINUTO_RIVELA mancante o troppo corto')
    v=campo('RISPOSTA_TENUTA')
    mm=re.search(r'blocco\s+(\d+)',v or '')
    if not mm or int(mm.group(1))<=n/2: err.append('RISPOSTA_TENUTA: la risposta deve arrivare oltre meta\' video')
    for k in ('CERCHIO_1','CERCHIO_2'):
        v=campo(k); mm=re.search(r'aperto in blocco\s+(\d+).*chiuso in blocco\s+(\d+)',v or '')
        if not mm or int(mm.group(1))>4 or int(mm.group(2))<=n/2: err.append(f'{k}: aperto nei primi 4 blocchi e chiuso oltre meta\'')
    if not campo('CIFRA_GANCIO'): err.append('CIFRA_GANCIO mancante')
    h=impronta(' '.join(t for _,t in bl[:4]))
    if campo('IMPRONTA_PRIMI4')!=h: err.append('i blocchi 1-4 sono cambiati dopo il controllo di fidelizzazione (rifarlo): impronta attesa '+h)
    return err
def controlla(f):
    rev=os.path.join(os.path.dirname(f),'revisione-copione.txt')
    if not os.path.exists(rev): return [f'manca {rev}']
    righe={}
    for l in open(rev,encoding='utf-8'):
        p=[x.strip() for x in l.split('|')]
        if len(p)>=6 and p[0].isdigit(): righe[int(p[0])]=p
    err=fidelizzazione(f)
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
