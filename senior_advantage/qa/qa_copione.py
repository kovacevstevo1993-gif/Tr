#!/usr/bin/env python3
"""Controllo automatico di un copione The Senior Advantage (righe 'N testo'). Uso: python3 senior_advantage/qa/qa_copione.py <file>
Se stampa ERRORI il copione NON si manda. Fatti e date si controllano a mano sulle fonti originali (CHECKLIST-REGOLE.md punti 2, 10, 11)."""
import re,sys
from collections import defaultdict
s=open(sys.argv[1],encoding='utf-8').read()
b={int(m.group(1)):m.group(2) for m in re.finditer(r"(?m)^(\d+) (.*)$",s)}
err=[]
if sorted(b)!=list(range(1,len(b)+1)): err.append("numerazione blocchi non continua")
for k,t in b.items():
    if len(t)>500: err.append(f"blocco {k}: {len(t)} caratteri (max 500)")
    if re.search(r"[0-9$%&/\-+@#*()\"]",t): err.append(f"blocco {k}: cifre o simboli")
    if re.search(r"\b(SNAP|EBT|SSI|LIHEAP|USDA|CSFP|TSA|PIN|ID)\b",t): err.append(f"blocco {k}: sigla da scrivere a lettere (S S I) o snap minuscolo")
    for g in ["most people","most shoppers","most seniors","everybody","nobody","every day","almost no","never hear","everyone knows"]:
        if g in t.lower(): err.append(f"blocco {k}: frase generica non verificabile '{g}' (ok solo con fonte)")
    ss=[x.strip().lower() for x in re.split(r"[.?!]",t) if len(x.strip())>25]
    if len(ss)!=len(set(ss)): err.append(f"blocco {k}: frase doppia")
seen=defaultdict(set)
names={"the u s d a"}
for k,t in b.items():
    w=re.findall(r"[a-z']+",t.lower())
    for i in range(len(w)-4): seen[" ".join(w[i:i+5])].add(k)
rec=max(b) and [k for k,t in b.items() if re.match(r"So let's put all|Let's recap|Quick recap",t)]
for g,v in seen.items():
    if len(v)>1 and g not in names and not (rec and set(v)&set(rec)): err.append(f"ripetuta in blocchi {sorted(v)}: '{g}'")
words=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"]
txt=" ".join(b[k] for k in sorted(b))
nums=[w for w in words if f"Number {w}." in txt]
pos=[txt.find(f"Number {w}.") for w in nums]
if nums and (nums!=words[:len(nums)] or pos!=sorted(pos)): err.append(f"voci 'Number N.' non in ordine o mancanti: {nums}")
if rec and nums:
    cnt=len(re.findall(r"\b(One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen),",b[rec[0]]))
    if cnt!=len(nums): err.append(f"riepilogo con {cnt} voci, ma le voci sono {len(nums)}")
print(f"blocchi {len(b)}, caratteri {sum(len(t) for t in b.values())}, voci {len(nums)}")
print("ERRORI:\n- "+"\n- ".join(err) if err else "OK: nessun errore automatico. Ora controllo a mano fonti originali e date (punti 2, 10, 11).")
sys.exit(1 if err else 0)
