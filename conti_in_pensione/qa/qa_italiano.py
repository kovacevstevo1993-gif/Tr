#!/usr/bin/env python3
"""CONTROLLO ITALIANO PER LA VOCE (28/10/2026, short 15: 8 versioni mandate con difetti di italiano trovati uno alla volta).
Cerca i difetti che ho gia' fatto: frammenti come apertura, persona che cambia (tu / impersonale) nello stesso blocco,
frasi ellittiche ("Per i tre esempi ... tocca"), possessivo dopo il nome ("numeri tuoi"), domande senza oggetto
("Quanto vale in euro?"), "rifatto" senza un conto gia' fatto, "chiunque" dopo "non tocca", due "per + infinito" vicini.
Uso: importato da qa_copione.py (ERRORE blocca, VERIFICARE e' un avviso da risolvere). Aggiungere qui ogni difetto nuovo."""
import re
TU=r"\b(hai|sei|vai|tuo|tua|tuoi|tue|ti|conosci|potresti|dovresti|devi|rientri|controlla|toccalo|scrivi|lascia|iscriviti|vuoi|puoi|scopri)\b"
IMP=r"\b(si perde|si deve|si può|si paga|si prende|si ottiene|bisognerebbe|bisogna|ci si|uno deve)\b|\bquanto si [a-zàèéìòù]+"
def controlla(blocchi):
    err=[];av=[]
    for n,t in blocchi:
        fr=[x for x in re.split(r'(?<=[.?!:])\s+',t.strip()) if x]
        if fr and len(re.findall(r"[A-Za-zàèéìòù']+",fr[0]))<=2 and fr[0].endswith('?') and n==1:
            err.append(f'blocco {n}: apertura a frammento senza verbo ("{fr[0]}")')
        if re.search(TU,t,re.I) and re.search(IMP,t,re.I):
            err.append(f'blocco {n}: persona mista (tu + forma impersonale "{re.search(IMP,t,re.I).group(0)}")')
        if re.search(r"^Per (i|le|gli|il|la|lo|l')\s[^,:.]*\btocca\b",t):
            err.append(f'blocco {n}: frase ellittica "Per ... tocca" (manca "vedere" e la virgola)')
        m=re.search(r"\b(numeri|dati|cifre|importi) (tuoi|tue)\b",t,re.I)
        if m: err.append(f'blocco {n}: possessivo dopo il nome ("{m.group(0)}"): "i tuoi numeri"/"due tuoi numeri"')
        if re.search(r"che (hai|avete) tu\b",t,re.I): err.append(f'blocco {n}: "che hai tu" non e\' naturale')
        if re.search(r"Quanto vale in euro\?",t): err.append(f'blocco {n}: "Quanto vale in euro?" senza dire cosa vale')
        if re.search(r"non (tocca|riguarda) chiunque",t,re.I) and re.search(r"non tocca chiunque",t,re.I):
            err.append(f'blocco {n}: "Non tocca chiunque" suona male (usare "Non riguarda chiunque")')
        if re.search(r"\b(rifatto|rifatta|rifare|rifatti)\b",t,re.I): av.append(f'blocco {n}: "rifatto": il conto esisteva gia\'? se e\' nuovo scrivere "calcolato"')
        if re.search(r"\bdi attesa\b",t,re.I): av.append(f'blocco {n}: "di attesa": attesa di chi/cosa? dirlo chiaro')
        if re.search(r"\bper \w+re\b.{0,90}\bper \w+re\b",t,re.I): av.append(f'blocco {n}: due "per + infinito" vicini: frase pesante, riscrivere')
    return err,av
