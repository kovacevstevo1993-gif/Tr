"""CONTROLLO TEMA GIA' FATTO (regola N.36, errore video 10 del 22/10/2026). Da lanciare PRIMA di proporre un tema all'utente.
Uso (dalla cartella conti_in_pensione): python3 qa/check_tema.py "parola 1" "parola 2" ...
Cerca le parole del tema (meccanismo, non solo titolo) in TUTTI i copioni e in tutti i titoli dei video/short gia' fatti.
Esce con codice 1 se una parola compare: il tema va scartato o va detto all'utente cosa c'e' di diverso."""
import glob,re,sys
parole=[p.lower() for p in sys.argv[1:]]
if not parole:sys.exit(__doc__)
copioni=sorted(glob.glob('[0-9][0-9]-*/copione-blocchi.txt'))
titoli=sorted(glob.glob('[0-9][0-9]-*/pacchetto*.txt')+glob.glob('[0-9][0-9]-*/titolo-descrizione-tag*.txt'))
trovato=False
for p in parole:
    righe=[]
    for f in copioni:
        for n,r in enumerate(open(f,encoding='utf-8',errors='ignore'),1):
            if p in r.lower():righe.append(f'{f}:{n}: {r.strip()[:160]}')
    for f in titoli:
        t=open(f,encoding='utf-8',errors='ignore').read()
        m=re.search(r'===\s*TITOLO[^\n]*===\n([^\n]+)',t,re.I)
        if m and p in m.group(1).lower():righe.append(f'{f}: TITOLO: {m.group(1).strip()}')
    if righe:
        trovato=True
        print(f'GIA PRESENTE "{p}" ({len(righe)} righe):');[print('   '+x) for x in righe[:8]]
    else:print(f'nuovo: "{p}"')
print('ESITO:','TEMA (O PARTE) GIA FATTO: scartare o dire cosa cambia' if trovato else 'nessuna traccia nei video gia fatti')
sys.exit(1 if trovato else 0)
