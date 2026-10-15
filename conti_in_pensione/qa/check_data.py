"""Regola N.33: blocca frasi al passato su un mese che non e' ancora arrivato (es. 'a novembre ti hanno trattenuto' scritto a ottobre)."""
import re,datetime
MESI=['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
PASS=r"(ti hanno|vi hanno|hai (ricevuto|visto|trovato|preso|avuto)|avete (ricevuto|visto|trovato)|è (arrivat|stat)|e' (arrivat|stat)|sono (arrivat|stat)|ti è|ti e')"
def errori_data(testo,oggi=None):
    oggi=oggi or datetime.date.today();err=[]
    for frase in re.split(r'(?<=[.!?\n])',testo):
        f=frase.lower()
        for i,m in enumerate(MESI):
            if re.search(r'\b'+m+r'\b',f) and re.search(PASS,f) and (i+1)>=oggi.month and not re.search(r'\b(scors|passat|20\d\d)',f):
                err.append(f'N.33: frase al passato su {m} (mese non ancora finito/arrivato): "{frase.strip()[:90]}"')
    return err
