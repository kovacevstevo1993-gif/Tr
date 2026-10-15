"""CONTROLLO TESTI (obbligatorio PRIMA di consegnare titolo/descrizione/tag/commento). Uso: python3 conti_in_pensione/qa/qa_testi.py <file pacchetto.txt>
Il file deve avere le sezioni "=== TITOLO ===", "=== DESCRIZIONE ===", "=== TAG ===", (opz.) "=== COMMENTO ...". Esce con codice 1 se un controllo non passa."""
import re,sys
p=sys.argv[1];t=open(p,encoding='utf-8').read()
def sez(nome):
    m=re.search(r'===\s*'+nome+r'[^\n]*===\n(.*?)(?=\n===|\Z)',t,re.S|re.I);return m.group(1).strip() if m else ''
tit,desc,tag,com=sez('TITOLO'),sez('DESCRIZIONE'),sez('TAG'),sez('COMMENTO')
err=[];warn=[]
def E(m):err.append(m)
def W(m):warn.append(m)
if not tit:E('manca la sezione TITOLO')
if not desc:E('manca la sezione DESCRIZIONE')
if not tag:E('manca la sezione TAG')
tit=tit.split('\n')[0]
tutto=tit+'\n'+desc+'\n'+tag+'\n'+com
# TITOLO
if len(tit)>100:E(f'titolo {len(tit)} caratteri (max 100)')
if '#' in tit:E('titolo con hashtag')
if not re.search(r'pension[ei]',tit,re.I):E('titolo senza la parola PENSIONI/PENSIONE (regola N.19)')
if '?' not in tit and '!' not in tit:W('titolo senza domanda/esclamazione: i virali usano "?"')
if not re.search(r'\b[A-ZÀ-Ý]{5,}\b',tit):W('titolo senza parola calda in MAIUSCOLO')
# PAROLE VIETATE NEI TESTI SCRITTI
for pat,msg in [(r'mai\s*inps','"Mai Inps" scritto: nei testi va "My Inps" (N.20)'),(r'maiinps','#maiinps: deve essere #myinps'),(r'mio\s*inps','"mio inps": deve essere "my inps"'),(r'obis\s+m\b','"Obis M": deve essere "ObisM"'),(r'\[INCOLLA','segnaposto [INCOLLA...] ancora presente'),(r'45 centesimi','"45 centesimi" vietato (N. video 4)')]:
    if re.search(pat,tutto,re.I):E(msg)
for m in re.finditer(r'\binvalidi\b(?! al 100)',tutto,re.I):E('"INVALIDI" da solo come etichetta (offensivo): usare INVALIDITA\'');break
# TAG (conteggio come YouTube)
L=[x.strip() for x in tag.replace('\n',' ').split(', ') if x.strip()]
for x in L:
    if re.search(r'\d,\d|;',x):E(f'tag con virgola/punto e virgola dentro: "{x}" (YouTube lo spezza)')
yt=sum(len(x)+(2 if ' ' in x else 0) for x in L)+max(len(L)-1,0)
if yt>500:E(f'tag: {yt}/500 secondo YouTube (troppi)')
elif yt<480:E(f'tag: {yt}/500: riempire fino a 480-497')
if len(set(L))!=len(L):E('tag duplicati')
# HASHTAG
hs=re.findall(r'#\w+',desc)
if not 5<=len(set(hs))<=12:E(f'hashtag: {len(set(hs))} (devono essere 5-12)')
# DESCRIZIONE
if 'Disclaimer:' not in desc:E('manca "Disclaimer:" nella descrizione')
if not re.search(r"non (è|e'|è) affiliato",desc):E('disclaimer senza "Questo canale non è affiliato all\'Inps"')
if 'Iscriviti' not in desc:E('manca la riga Iscriviti')
for u in re.findall(r'https?://\S+',desc):
    if 'youtube.com/@ContiInPensione' not in u:E(f'link non ammesso nella descrizione: {u}')
short=('#shorts' in desc) or ('Video correlato' in desc)
if short:
    if 'Video correlato' not in desc:E('short senza "tocca il Video correlato" nella descrizione')
    if 'shorts' not in L:W('short senza tag "shorts"')
else:
    cap=re.findall(r'^(\d+):(\d\d)\s+(.+)$',desc,re.M)
    if 'CAPITOLI' not in desc or not cap:E('video lungo senza CAPITOLI')
    else:
        sec=[int(a)*60+int(b) for a,b,_ in cap]
        if sec[0]!=0:E('i capitoli devono partire da 0:00')
        if len(cap)<3:E('servono almeno 3 capitoli')
        for a,b in zip(sec,sec[1:]):
            if b-a<10:E(f'capitoli troppo vicini (<10 s) a {b//60}:{b%60:02d}')
        if sec!=sorted(sec):E('capitoli non in ordine')
if com and re.search(r'https?://',com):E('commento fissato con link (negli short non funzionano)')
import os as _o,sys as _s;_s.path.insert(0,_o.path.dirname(_o.path.abspath(__file__)));from check_data import errori_data
for _e in errori_data(tutto):err.append(_e)
print(f'TITOLO ({len(tit)}): {tit}');print(f'TAG: {len(L)} tag, {yt}/500 (conteggio YouTube) | HASHTAG: {len(set(hs))} | tipo: {"SHORT" if short else "VIDEO LUNGO"}')
for w in warn:print('ATTENZIONE:',w)
for e in err:print('ERRORE:',e)
print('QA TESTI OK' if not err else f'QA TESTI NON PASSATO ({len(err)} errori): NON CONSEGNARE');sys.exit(1 if err else 0)
