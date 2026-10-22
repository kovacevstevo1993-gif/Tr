#!/usr/bin/env python3
"""Controllo automatico di un copione The Senior Advantage (righe 'N testo'). Uso: python3 senior_advantage/qa/qa_copione.py <file>
Se stampa ERRORI il copione NON si manda. Stampa anche DA CONTROLLARE A MANO (numeri, date/stagioni, 'free'): vanno verificati uno per uno sulle fonti originali e sulla data di pubblicazione."""
import re,sys,glob,os
from collections import defaultdict
f=sys.argv[1]; s=open(f,encoding='utf-8').read()
b={int(m.group(1)):m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$",s)}
err=[];man=[]
N=len(b)
if sorted(b)!=list(range(1,N+1)): err.append("numerazione blocchi non continua")
for k,t in b.items():
    if len(t)>500: err.append(f"blocco {k}: {len(t)} caratteri (max 500)")
    if len(t)<380 and k<N-2: err.append(f"blocco {k}: solo {len(t)} caratteri (blocchi vicini a 500, regola 20/10)")
    if re.search(r"[0-9$%&/\-+@#*()\"]",t): err.append(f"blocco {k}: cifre o simboli")
    if re.search(r"\b(SNAP|EBT|SSI|LIHEAP|USDA|CSFP|TSA|PIN|ID|AARP|IRS)\b",t): err.append(f"blocco {k}: sigla da scrivere a lettere o snap minuscolo")
    for g in ["most people","most shoppers","most seniors","everybody","nobody","every day","almost no","never hear","everyone knows","guaranteed","always free"]:
        if g in t.lower(): err.append(f"blocco {k}: frase generica/assoluta non verificabile '{g}'")
    ss=[x.strip().lower() for x in re.split(r"[.?!]",t) if len(x.strip())>25]
    if len(ss)!=len(set(ss)): err.append(f"blocco {k}: frase doppia")
# ripetizioni tra blocchi (escluso riepilogo)
rec=[k for k,t in b.items() if re.match(r"So let's put all|Let's recap|Quick recap",t)]
seen=defaultdict(set)
for k,t in b.items():
    w=re.findall(r"[a-z']+",t.lower())
    for i in range(len(w)-4): seen[" ".join(w[i:i+5])].add(k)
for g,v in seen.items():
    if len(v)>1 and g not in {"the u s d a"} and not (set(v)&set(rec)): err.append(f"ripetuta in blocchi {sorted(v)}: '{g}'")
# voci numerate e riepilogo
words=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"]
txt=" ".join(b[k] for k in sorted(b))
nums=[w for w in words if f"Number {w}." in txt]
pos=[txt.find(f"Number {w}.") for w in nums]
if nums and (nums!=words[:len(nums)] or pos!=sorted(pos)): err.append(f"voci 'Number N.' non in ordine o mancanti: {nums}")
if rec and nums:
    cnt=len(re.findall(r"\b(One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen),",b[rec[0]]))
    if cnt!=len(nums): err.append(f"riepilogo con {cnt} voci, ma le voci sono {len(nums)}")
m=re.search(r"\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen) (things|kinds|ways|bills|rules)\b",b.get(1,"")+" "+b.get(2,""))
if m and nums and words.index(m.group(1))+1!=len(nums): err.append(f"gancio annuncia '{m.group(1)} {m.group(2)}' ma le voci sono {len(nums)}")
# rimandi 'number X'
for k,t in b.items():
    for r in re.findall(r"\bnumbers? (one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b",t):
        if nums and r not in nums: err.append(f"blocco {k}: rimanda a 'number {r}' che non esiste")
# finale: like/iscrizione, disclaimer
if not re.search(r"subscribe",txt,re.I): err.append("manca la richiesta di iscrizione")
if not re.search(r"not affiliated",b[N]): err.append("ultimo blocco senza disclaimer 'not affiliated'")
# ortografia (parole minuscole non nel dizionario)
try:
    from spellchecker import SpellChecker
    sp=SpellChecker(); bad=set()
    for k,t in b.items():
        for w in re.findall(r"(?<![A-Za-z'])[a-z][a-z']*",t):
            w2=w.strip("'"); w2=w2[:-2] if w2.endswith("'s") else w2
            if w2 and w2 not in {"app","apps","com","i'd","i'll","snap","pin","walmart"} and sp.unknown([w2]): bad.add((k,w2))
    for k,w in sorted(bad): err.append(f"blocco {k}: parola sospetta (ortografia) '{w}'")
except ImportError:
    man.append("ortografia: pyspellchecker non installato (pip install pyspellchecker), rileggere a mano")
# gancio gia usato in altri copioni
d=os.path.dirname(os.path.abspath(f))
first=" ".join(re.findall(r"[a-z']+",b.get(1,"").lower())[:6])
for g in glob.glob(os.path.join(d,"COPIONE-*.md")):
    if os.path.abspath(g)==os.path.abspath(f): continue
    o=open(g,encoding='utf-8').read(); m1=re.search(r"(?m)^1 (.*)$",o)
    if m1 and " ".join(re.findall(r"[a-z']+",m1.group(1).lower())[:6])==first: err.append(f"gancio uguale a {os.path.basename(g)}")
# da controllare a mano
num=r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|percent|dollars?|cents?)\b"
for k,t in b.items():
    if k in rec: continue
    for x in re.split(r"(?<=[.?!])\s+",t):
        if re.search(num,x,re.I) and not re.match(r"Number \w+\.$",x): man.append(f"NUMERO b{k}: {x}")
        if re.search(r"\b(January|February|March|April|May|June|July|August|September|October|November|December|this season|this winter|this year|right now|today|this week)\b",x): man.append(f"DATA/STAGIONE b{k} (vale alla data di pubblicazione?): {x}")
        if re.search(r"\bfree\b|no charge|no cost",x,re.I): man.append(f"FREE b{k} (scritto dalla fonte ufficiale?): {x}")
print(f"blocchi {N}, caratteri {sum(len(t) for t in b.values())}, voci {len(nums)}")
print("ERRORI:\n- "+"\n- ".join(err) if err else "OK: nessun errore automatico.")
print("\nDA CONTROLLARE A MANO, uno per uno (fonte originale, data, logica):\n- "+"\n- ".join(man))
sys.exit(1 if err else 0)
