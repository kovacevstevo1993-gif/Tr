#!/usr/bin/env python3
"""Controllo automatico del PACCHETTO di uno SHORT Senior Advantage (26/10/2026). Uso: python3 senior_advantage/qa/qa_pacchetto_short.py <PACCHETTO-SHORT-*.md>
Regole: titolo max 100 e senza hashtag; descrizione con unico link Subscribe, riga Sources solo con nomi di siti, Disclaimer con 'not affiliated', ultima riga hashtag (#Shorts + 3);
tag con virgola e spazio, max 500 caratteri; commento senza disclaimer e che rimanda al video sotto; impostazioni con Video correlato e copertina."""
import re, sys
txt = open(sys.argv[1], encoding="utf-8").read()
sec = {}
for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", txt, re.S | re.M):
    sec[m.group(1).strip().lower()] = m.group(2).strip()
err, warn = [], []
def get(p):
    for k, v in sec.items():
        if k.startswith(p): return v
    err.append(f"manca la sezione '{p}'"); return ""
title, desc, tags, com, st = get("titolo"), get("descrizione"), get("tag"), get("commento"), get("impostazioni")
SUB = "https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1"
title = title.split("\n")[0]
if len(title) > 100: err.append(f"titolo {len(title)} caratteri (max 100)")
if "#" in title: err.append("hashtag nel titolo")
if len(desc) > 5000: err.append("descrizione oltre 5000 caratteri")
if "aldi" not in desc[:125].lower(): warn.append("parola chiave non nei primi 125 caratteri")
urls = [u.rstrip(".,)") for u in re.findall(r"https?://\S+|www\.\S+", desc)]
if SUB not in desc: err.append("manca il link Subscribe")
if [u for u in urls if u != SUB]: err.append("URL non ammessi nella descrizione")
if not re.search(r"^Subscribe for more help most seniors never claim: ", desc, re.M): err.append("riga Subscribe non nel formato del modello short")
if not re.search(r"^Disclaimer: .*not financial.*not affiliated", desc, re.M | re.S): err.append("Disclaimer mancante o incompleto")
m = re.search(r"^Sources: official pages of .*$", desc, re.M)
if not m: err.append("manca 'Sources: official pages of ...'")
elif re.search(r"https?://|www\.", m.group(0)): err.append("URL nella riga Sources")
last = [l for l in desc.split("\n") if l.strip()][-1]
h = re.findall(r"#\w+", last)
if not last.startswith("#Shorts") or len(h) != 4: err.append(f"ultima riga: serve '#Shorts' + 3 hashtag, trovati {h}")
tl = [t.strip() for t in tags.replace("\n", " ").split(",") if t.strip()]
if ", " not in tags: err.append("tag senza spazio dopo la virgola (modello short)")
if len(tags) > 500: err.append(f"tag {len(tags)} caratteri (max 500)")
if len(tl) != len(set(tl)): err.append("tag duplicati")
if re.search(r"disclaimer|not affiliated", com, re.I): err.append("disclaimer nel commento fissato")
if "right below" not in com: err.append("il commento deve rimandare al video sotto lo short")
if "Video correlato" not in st or "copertina" not in st.lower(): err.append("impostazioni senza Video correlato o copertina")
if "IA No" not in st or "Promozione No" not in st: err.append("impostazioni senza IA No / Promozione No")
print(f"titolo {len(title)} car; tag {len(tags)} car ({len(tl)}); descrizione {len(desc)} car")
print("ERRORI:\n- " + "\n- ".join(err) if err else "OK: nessun errore automatico.")
if warn: print("AVVISI:\n- " + "\n- ".join(warn))
sys.exit(1 if err else 0)
