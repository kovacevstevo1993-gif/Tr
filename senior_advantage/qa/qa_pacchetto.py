#!/usr/bin/env python3
"""Controllo automatico del PACCHETTO di un video lungo Senior Advantage (26/10/2026).
uso: python3 senior_advantage/qa/qa_pacchetto.py senior_advantage/PACCHETTO-VIDEO-ALDI.md [durata_video_in_secondi]
Regole ufficiali YouTube verificate il 26/10/2026 (pagine support.google.com/youtube):
 - capitoli: primo 0:00, almeno 3, in ordine crescente, minimo 10 secondi ciascuno (answer/9884579);
 - hashtag: i primi 3 compaiono sopra il titolo, senza spazi, oltre 60 vengono ignorati tutti (answer/6390658);
 - tag: poco peso, niente eccessi (answer/146402).
Regole del canale (CLAUDE.md, CHECKLIST-REGOLE.md): disclaimer con 'Disclaimer:' e 'not affiliated', solo il link Subscribe, niente URL nelle fonti,
 3 hashtag, tag senza spazi dopo la virgola e max 500 caratteri, commento fissato senza disclaimer, numero nel titolo = voci elencate.
Stampa ERRORI (non si consegna) e AVVISI."""
import re, sys

path = sys.argv[1]
dur = float(sys.argv[2]) if len(sys.argv) > 2 else None
txt = open(path, encoding="utf-8").read()
sec = {}
for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", txt, re.S | re.M):
    sec[m.group(1).strip().lower()] = m.group(2).strip()
err, warn = [], []


def get(prefix):
    for k, v in sec.items():
        if k.startswith(prefix):
            return v
    err.append(f"manca la sezione '{prefix}'"); return ""


title, desc, tags, comment, setts = get("titolo"), get("descrizione"), get("tag"), get("commento"), get("impostazioni")
SUB = "https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1"

# ---------------- titolo
title = title.split("\n")[0].strip()
if len(title) > 100: err.append(f"titolo troppo lungo: {len(title)} caratteri (max 100)")
elif len(title) > 80: warn.append(f"titolo lungo: {len(title)} caratteri (in ricerca si vede circa 60-70)")
if "#" in title: err.append("hashtag nel titolo")
if re.search(r"[\U0001F300-\U0001FAFF]", title): warn.append("emoji nel titolo di un video lungo (i lunghi non le hanno)")
caps = [w for w in re.findall(r"\b[A-Z]{4,}\b", title)]
if caps: warn.append(f"parole tutte maiuscole nel titolo: {caps}")

# ---------------- descrizione
if len(desc) > 5000: err.append(f"descrizione troppo lunga: {len(desc)} caratteri (max 5000)")
first = desc[:125].lower()
kw = re.sub(r"[^a-z ]", "", title.lower().split("(")[0].replace("has no", "")).strip()
if "senior discount" not in first: warn.append("parola chiave 'senior discount' non nei primi 125 caratteri")
urls = re.findall(r"https?://\S+|www\.\S+", desc)
extra = [u for u in urls if u.rstrip(".,)") != SUB]
if SUB not in desc: err.append("manca la riga Subscribe con il link ufficiale")
if extra: err.append(f"URL non ammessi nella descrizione: {extra}")
if "Subscribe to The Senior Advantage:" not in desc: err.append("riga Subscribe non nel formato 'Subscribe to The Senior Advantage: <link>'")
if not re.search(r"^Disclaimer: .*not financial.*not affiliated", desc, re.M | re.S): err.append("Disclaimer mancante o incompleto (serve 'Disclaimer:', 'not financial', 'not affiliated')")
if not re.search(r"^Sources: official pages of ", desc, re.M): err.append("manca la riga 'Sources: official pages of ...'")
else:
    srcline = re.search(r"^Sources:.*$", desc, re.M).group(0)
    if re.search(r"https?://|www\.", srcline): err.append("URL nella riga Sources (solo il nome del sito)")
lines = [l for l in desc.split("\n") if l.strip()]
hashtags = re.findall(r"#\w+", lines[-1]) if lines else []
if lines and not lines[-1].startswith("#"): err.append("l'ultima riga deve essere quella degli hashtag")
elif len(hashtags) != 3: err.append(f"servono esattamente 3 hashtag, trovati {len(hashtags)}")
if any(h != h.lower() for h in hashtags): warn.append("hashtag non tutti minuscoli")
if "$" in desc: warn.append("compare '$' nella descrizione: prezzi/cifre non verificati nel video? controllare")

# ---------------- capitoli
chap = re.findall(r"^(\d{1,2}):(\d{2}) (.+)$", desc, re.M)
secs = [int(m) * 60 + int(s) for m, s, _ in chap]
if not chap: err.append("nessun capitolo")
else:
    if secs[0] != 0: err.append("il primo capitolo deve essere 0:00")
    if len(chap) < 3: err.append("servono almeno 3 capitoli")
    for i in range(1, len(secs)):
        if secs[i] <= secs[i - 1]: err.append(f"capitoli non in ordine crescente: {chap[i-1][0]}:{chap[i-1][1]} -> {chap[i][0]}:{chap[i][1]}")
        elif secs[i] - secs[i - 1] < 10: err.append(f"capitolo sotto i 10 secondi: {chap[i-1][0]}:{chap[i-1][1]} {chap[i-1][2]}")
    if dur and secs[-1] >= dur - 10: err.append("ultimo capitolo troppo vicino alla fine del video")
    if dur and dur - secs[-1] < 10: err.append("ultimo capitolo sotto i 10 secondi")
    nums = [int(n) for n in re.findall(r"#(\d+) ", "\n".join(c[2] for c in [(a, b, "#" + c.split("#")[1]) if "#" in c else (a, b, c) for a, b, c in chap]))] if False else [int(m.group(1)) for c in chap for m in [re.match(r"#(\d+) ", c[2])] if m]
    mt = re.search(r"\b(\d+) (?:Things|Rules|Ways|Kinds)\b", title)
    if mt and nums and int(mt.group(1)) != max(nums): err.append(f"numero nel titolo ({mt.group(1)}) diverso dalle voci numerate nei capitoli ({max(nums)})")
    if nums and nums != list(range(1, max(nums) + 1)): err.append(f"voci numerate nei capitoli non consecutive: {nums}")

# ---------------- tag
tl = tags.strip()
if ", " in tl or " ," in tl: err.append("i tag devono essere separati da virgola SENZA spazi")
tlist = tl.split(",")
if len(tl) > 500: err.append(f"tag troppo lunghi: {len(tl)} caratteri (max 500)")
if len(tlist) != len(set(t.lower() for t in tlist)): err.append("tag doppi")
if len(tlist) > 25: warn.append(f"{len(tlist)} tag: YouTube dice che i tag contano poco e gli eccessi sono spam")
if "\n" in tl: err.append("i tag devono stare su una riga")

# ---------------- commento
if re.search(r"disclaimer|https?://|www\.", comment, re.I): err.append("il commento fissato non deve avere disclaimer ne link")
if "?" not in comment: warn.append("il commento fissato dovrebbe contenere una domanda al pubblico")

# ---------------- impostazioni
for need in ("IA: No", "Promozione a pagamento: No", "Miniatura", "Schermata finale", "Video correlato", "notifica"):
    if need not in setts: err.append(f"nelle Impostazioni manca: {need}")

print(f"{path}: titolo {len(title)} car., descrizione {len(desc)} car., {len(chap)} capitoli, {len(tlist)} tag = {len(tl)} car., hashtag {hashtags}")
for w in warn: print("AVVISO:", w)
for e in err: print("ERRORE:", e)
if err:
    print(f"ERRORI: {len(err)}"); sys.exit(1)
print("OK: pacchetto controllato")
