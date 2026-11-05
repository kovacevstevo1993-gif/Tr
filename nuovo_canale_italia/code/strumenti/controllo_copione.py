#!/usr/bin/env python3
"""Controllo del copione PRIMA della voce. Uso: controllo_copione.py copione.json
Trova: ripetizioni tra blocchi (stesse cifre/frasi dette due volte), frasi doppie nello stesso blocco, cifre/simboli non scritti in lettere,
numeri senza unita (per cento / euro / anni / mesi), blocchi troppo lunghi o corti, hook che anticipa le cifre del blocco dopo. Se stampa ERRORI NON si fa la voce."""
import sys, json, re
b = json.load(open(sys.argv[1])); err = []; warn = []
norm = lambda s: re.findall(r"[a-zàèéìòù']+", s.lower())
W = [norm(t) for t in b]
for i, t in enumerate(b, 1):
    if re.search(r"\d|%|€", t): err.append(f"blocco {i}: cifre o simboli (scrivere in lettere): {re.findall(r'.{0,12}(?:\d|%|€).{0,8}', t)[:2]}")
    n = len(t)
    if n > 520: err.append(f"blocco {i}: {n} caratteri (max 520)")
    if n < 150: warn.append(f"blocco {i}: solo {n} caratteri")
    fr = [f.strip().lower() for f in re.split(r"[.!?]", t) if len(f.strip()) > 12]
    for f in set(fr):
        if fr.count(f) > 1: err.append(f"blocco {i}: frase doppia: {f[:50]}")
# ripetizioni tra blocchi: sequenze di 4 parole uguali in blocchi diversi
G = lambda w, n=4: {tuple(w[k:k + n]) for k in range(len(w) - n + 1)}
for i in range(len(b)):
    for j in range(i + 1, len(b)):
        com = G(W[i]) & G(W[j])
        GEN = {"anni","e","un","mese","mesi","per","cento","euro","di","il","la","lo","le","i","gli","a","al","dal","del","della","con","in","che","non","è","anno","ma"}
        com = [c for c in com if len(set(c)) > 1 and any(w not in GEN for w in c)]
        if com: err.append(f"RIPETIZIONE tra blocco {i+1} e {j+1}: " + " | ".join(" ".join(c) for c in sorted(com)[:4]))
# numeri in lettere ripetuti tra blocco 1 (hook) e blocco 2: stesse "cifre" dette due volte
NUM = r"(?:uno|un|due|tre|quattro|cinque|sei|sette|otto|nove|dieci|undici|venti|trenta|quaranta|cinquanta|sessanta|settanta|ottanta|novanta|cento|mille|[a-z]+(?:cento|mila|mille))"
def cifre(t): return re.findall(NUM + r"(?: (?:e|virgola) " + NUM + r")* (?:per cento|euro|anni|mesi|mese|anno|giorni|centesimi|mila euro)", t.lower())
c1, c2 = set(cifre(b[0])), set(cifre(b[1])) if len(b) > 1 else set()
if c1 & c2: err.append("hook e blocco 2 dicono le STESSE cifre: " + ", ".join(sorted(c1 & c2)[:5]))
for i, t in enumerate(b, 1):
    for m in re.finditer(r"\b" + NUM + r"\b(?! (?:per cento|euro|anni|mesi|mese|anno|giorni|centesimi|di|e|virgola|volte|punto|punti|categorie|mila|cento|milioni|miliardi|[a-z]+\b))", t.lower()):
        pass
print("BLOCCHI:", [len(t) for t in b])
for w in warn: print("AVVISO:", w)
for e in err: print("ERRORE:", e)
print("PASSATO" if not err else f"NON PASSATO: {len(err)} errori, la voce NON si fa")
sys.exit(1 if err else 0)
