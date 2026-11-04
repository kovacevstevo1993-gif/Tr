#!/usr/bin/env python3
"""Genera copione-blocchi.txt del video lungo 12 (coefficienti di trasformazione 2027).
Ogni numero detto a voce e' CALCOLATO da calcolo_coeff.py e convertito in lettere da qui (mai scritto a mano)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calcolo_coeff import T2324, T2526, T27, TABD, coef_mesi

U = ['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici',
     'quattordici','quindici','sedici','diciassette','diciotto','diciannove']
D = {2:'venti',3:'trenta',4:'quaranta',5:'cinquanta',6:'sessanta',7:'settanta',8:'ottanta',9:'novanta'}

def it(n):
    n = int(n)
    if n < 20: return U[n]
    if n < 100:
        t, u = divmod(n, 10); b = D[t]
        if u == 0: return b
        if u in (1, 8): b = b[:-1]
        return b + ('tré' if u == 3 else U[u])
    if n < 1000:
        h, r = divmod(n, 100)
        b = 'cento' if h == 1 else U[h] + 'cento'
        if r == 0: return b
        if 80 <= r < 90 or r == 8: b = b[:-1]
        return b + it(r)
    if n < 1000000:
        th, r = divmod(n, 1000)
        p = 'mille' if th == 1 else it(th).replace('é', 'e') + 'mila'
        return p if r == 0 else p + it(r)
    raise ValueError(n)

def dec(x, nd):
    s = f'{x:.{nd}f}'; i, d = s.split('.')
    z = len(d) - len(d.lstrip('0'))
    w = ' '.join(['zero'] * z) + ((' ' if z else '') + it(int(d)) if int(d) > 0 else '')
    return f'{it(int(i))} virgola {w}'

def P3(x): return dec(x, 3)      # coefficiente, tre decimali
def P2(x): return dec(abs(x), 2)  # variazione percentuale, due decimali
def E(x): return it(round(x))      # euro, intero

# ---- dati calcolati ----
c23, c25, c27 = T2324[67], T2526[67], T27[67]
tagli_25 = (c25 / c23 - 1) * 100
tagli_27 = (c27 / c25 - 1) * 100
tagli_tot = (c27 / c23 - 1) * 100
hook = 400000 * (c23 - c27) / 100           # 836
per100k = {e: 100000 * (T2526[e] - T27[e]) / 100 for e in (62, 64, 67, 70)}
M = {m: m * (c25 - c27) / 100 for m in (150000, 250000, 400000)}
mesi_min = min((T2526[e] - T27[e]) / ((T27[e + 1] - T27[e]) / 12) for e in range(57, 71))
mesi_max = max((T2526[e] - T27[e]) / ((T27[e + 1] - T27[e]) / 12) for e in range(57, 71))
mesi67 = (T2526[67] - T27[67]) / ((T27[68] - T27[67]) / 12)
mesi23 = [(T2324[e] - T27[e]) / ((T27[e + 1] - T27[e]) / 12) for e in range(57, 71)]
assert 12 < min(mesi23) and max(mesi23) < 14   # 'poco piu' di un anno'
c67_1 = coef_mesi(T27, 67, 1)
var67_1 = (c67_1 / c25 - 1) * 100
assert round(hook) == 836 and round(per100k[67]) == 94 and 5.8 < mesi_min and mesi_max < 6.2
assert all(abs(round((T27[e] / T2526[e] - 1) * 100, 2) - TABD[e]) < 0.015 for e in T27)

B = []
B.append(f"Pensione dal primo gennaio: a parità di contributi e di età, l'assegno sarà più basso di {E(hook)} euro all'anno rispetto a chi è uscito nel duemilaventitré. Parliamo di {it(400000)} euro di contributi e di un'uscita a {it(67)} anni. Non è una voce di corridoio: è un decreto di ottobre. E c'è un conto per recuperare quella cifra: lo trovi prima della fine.")
B.append(f"Il decreto è datato sedici ottobre. Lo ha emanato il Ministero del Lavoro, di concerto con quello dell'Economia, e il Ministero lo ha reso noto il venti. Cambia una tabella di quindici righe: i coefficienti di trasformazione. Entrano in vigore con il nuovo anno, il primo gennaio duemilaventisette. Ma non toccano tutti: tra poco ti diciamo chi è dentro e chi è fuori. Prima, i numeri.")
B.append(f"Prendi {it(67)} anni: il coefficiente era {P3(c23)} per cento nel duemilaventitré e duemilaventiquattro. Poi {P3(c25)} nel duemilaventicinque e duemilaventisei. Da gennaio, {P3(c27)}. Due tagli: meno {P2(tagli_25)} per cento, poi meno {P2(tagli_27)}. Totale: meno {P2(tagli_tot)} per cento.")
B.append(f"Il taglio non riguarda un'età sola: il decreto ha toccato ogni riga, dai {it(57)} ai {it(71)} anni, e il numero nuovo è più basso del vecchio. La riduzione parte da {dec(abs(TABD[57]),2)} per cento per chi esce a {it(57)} anni e arriva a {dec(abs(TABD[71]),2)} per chi esce a {it(71)}. I ministeri spiegano anche il perché, e lo leggiamo più avanti. Prima, però, il numero in euro.")
B.append(f"Un attimo, prima di continuare. Se ti serve qualcuno che i decreti li legge al posto tuo, iscriviti al canale: basta un tocco, e ci avvicina ai mille iscritti. Così possiamo continuare a fare conti veri sui testi ufficiali e a spiegarti cosa c'è scritto davvero. Attiva anche la campanella: quando esce il decreto sull'aumento di gennaio, rifacciamo la tabella con la percentuale vera.")
B.append(f"Come si usa la tabella. Hai versato contributi per una vita: la somma, rivalutata, si chiama montante. Lo moltiplichi per il coefficiente della tua età e ottieni la pensione annua. Oggi, all'età di {it(67)} anni, ogni {it(100000)} euro di montante valgono {E(100000*c25/100)} euro l'anno. Da gennaio, {E(100000*c27/100)}. Differenza: {E(per100k[67])} euro l'anno.")
B.append(f"Tre esempi, stessa età, {it(67)} anni, confrontati con chi esce quest'anno. Montante da {it(150000)} euro: perdi {E(M[150000])} euro l'anno, circa {E(M[150000]/13)} al mese. Da {it(250000)}: {E(M[250000])}, circa {E(M[250000]/13)}. Da {it(400000)}: {E(M[400000])}, circa {E(M[400000]/13)}. Cifre lorde, tredici mensilità. Scrivici nei commenti montante ed età: ti rispondiamo con il conto.")
B.append(f"In euro, il taglio cresce con l'età. Con un montante di {it(100000)} euro, la perdita è di {E(per100k[62])} euro all'anno se esci a {it(62)} anni, {E(per100k[64])} a {it(64)}, {E(per100k[67])} a {it(67)}, {E(per100k[70])} a {it(70)}. Il motivo è doppio: più tardi esci, più alto è il coefficiente, e più grande è la percentuale di taglio. Chi esce prima perde meno, ma parte da un assegno più basso.")
B.append(f"Il tuo montante, dove lo trovi? La legge dice che ogni anno l'Inps deve mandarti un estratto conto con la progressione del montante contributivo. L'estratto conto lo apri su Mai Inps, con Spid, carta d'identità elettronica o carta nazionale dei servizi, nel fascicolo previdenziale. Se non c'è, chiedilo a una sede Inps o a un patronato. Senza quel numero, ogni conto è una stima.")
B.append(f"Chi rientra? Per l'Inps, i coefficienti riguardano solo le pensioni, o le quote di pensione, calcolate con il contributivo. Rientra per intero chi ha iniziato a versare da gennaio millenovecentonovantasei. Chi versava già prima rientra per la quota contributiva, cioè i periodi dal duemiladodici, se a fine novantacinque aveva almeno diciotto anni di contributi; dal novantasei, negli altri casi.")
B.append(f"Rientra anche chi sceglie l'opzione donna e chi ha una pensione in cumulo calcolata col sistema contributivo. Resta fuori la parte calcolata con il retributivo, che da questo decreto non cambia. Fuori anche chi è già pensionato: l'Inps spiega che il coefficiente dipende dall'età nel momento in cui parte la pensione. Per chi è già in pensione, quel momento è passato.")
B.append(f"Ed ecco il conto promesso. Per ogni mese in più, dice la legge, il coefficiente cresce di un dodicesimo della differenza con quello dell'età successiva. Lo abbiamo rifatto per ogni età da {it(57)} a {it(70)} anni. Per tornare al coefficiente di quest'anno servono circa sei mesi, per quello del duemilaventitré poco più di un anno. I contributi, in questo conto, restano quelli di prima.")
B.append(f"Attenzione, non è un consiglio: rimandare vuol dire anche mesi di assegno in meno, e il conto completo va fatto sul tuo caso. C'è poi un altro effetto: dal duemilaventisette, per la vecchiaia, servono {it(67)} anni e un mese. Con quel mese il coefficiente è circa {P3(c67_1)}, contro il valore di oggi per quell'età: una perdita dell'{dec(abs(var67_1),2)} per cento.")
B.append(f"Il perché. Secondo la nota tecnica, il tasso di sconto, uno virgola cinque per cento, resta quello di prima. Cambiano i dati demografici dell'Istat, come le probabilità di morte. Il coefficiente si ottiene dividendo uno per un divisore: nella riga dei {it(67)} il divisore sale da {dec(17.831,3)} a {dec(18.136,3)}. Come se la pensione durasse di più.")
B.append(f"Riepilogo in tre punti. Uno: da gennaio la tabella è più bassa a ogni età. Due: la perdita in euro dipende dal tuo montante e dall'età di uscita, e adesso sai come calcolarla. Tre: riguarda la parte contributiva di chi va in pensione dal duemilaventisette. Canale informativo, non consulenza, non affiliato all'Inps: verifica su inps punto it o con un patronato.")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'copione-blocchi.txt')
with open(out, 'w', encoding='utf-8') as f:
    for i, t in enumerate(B, 1): f.write(f'{i}|{t}\n')
for i, t in enumerate(B, 1): print(i, len(t))
print('mesi min/max/67:', round(mesi_min, 2), round(mesi_max, 2), round(mesi67, 2), '| coef 67a1m', round(c67_1, 4), round(var67_1, 2))
