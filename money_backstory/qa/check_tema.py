"""PRIMA DI SCEGLIERE UN TEMA (regola utente 26/10): cerca ogni parola chiave in TUTTI i copioni/pacchetti/fonti dei video 1-N e nei kit.
Uso: python3 money_backstory/qa/check_tema.py "earnings test" "earnings limit" ...   Se stampa HIT, il tema (anche in parte) e' GIA' FATTO: non proporlo."""
import sys, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ('chat/', 'RICERCH', 'video14-earnings-limit', 'PASSAGGIO', 'START-QUI', 'REGOLE-UTENTE')
hits = 0
for kw in sys.argv[1:]:
    print('==', kw)
    for dp, dn, fn in os.walk(ROOT):
        for f in fn:
            if not f.endswith(('.md', '.json', '.txt', '.py')): continue
            p = os.path.join(dp, f); rp = os.path.relpath(p, ROOT)
            if any(s in rp for s in SKIP) or '/slide' in rp or 'voce' in rp: continue
            try: t = open(p, encoding='utf-8', errors='ignore').read()
            except Exception: continue
            n = len(re.findall(re.escape(kw), t, re.I))
            if n: hits += 1; print('  HIT', n, rp)
print('TOTALE FILE CON HIT:', hits, '-> tema GIA TOCCATO' if hits else '-> nessun hit')
