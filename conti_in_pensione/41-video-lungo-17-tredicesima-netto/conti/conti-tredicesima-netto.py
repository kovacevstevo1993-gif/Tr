# Conto del netto per rata (13 rate uguali, metodo Inps dal 2021: messaggio 1359/2021), SENZA addizionali, SENZA altri redditi.
# Aliquote Irpef 2026: 23% fino a 28.000, 33% da 28.001 a 50.000, 43% oltre (Agenzia Entrate, Mef, legge 199/2025).
# Detrazione redditi di pensione: Tabella 7 istruzioni 730/2026 Agenzia Entrate (redditi 2025):
#   fino a 8.500: 1.955 (minimo 713); 8.501-28.000: 700 + 1.255 x (28.000 - R) / 19.500; 28.001-50.000: 700 x (50.000 - R) / 22.000; oltre 50.000: 0; +50 euro se R tra 25.001 e 29.000.
from decimal import Decimal as D
def irpef_lorda(R):
    R=D(R); t=min(R,D(28000))*D("0.23")
    if R>28000: t+=(min(R,D(50000))-28000)*D("0.33")
    if R>50000: t+=(R-50000)*D("0.43")
    return t
def detrazione(R):
    R=D(R)
    if R<=8500: d=max(D(1955),D(713))
    elif R<=28000: d=D(700)+D(1255)*(D(28000)-R)/D(19500)
    elif R<=50000: d=D(700)*(D(50000)-R)/D(22000)
    else: d=D(0)
    if D(25001)<=R<=D(29000): d+=50
    return d
def q(x): return x.quantize(D("0.01"))
if __name__=="__main__":
    for m in (600,700,800,1000,1200,1500,1800,2000,2500,3000):
        R=D(m)*13; i=irpef_lorda(R); d=detrazione(R); n=max(i-d,D(0)); net=R-n
        print(f"lordo/mese {m:>5} | reddito annuo {R:>7} | Irpef lorda {q(i):>9} | detrazione {q(d):>8} | Irpef netta annua {q(n):>9} | netto annuo {q(net):>9} | NETTO PER RATA {q(net/13):>9} | Irpef per rata {q(n/13):>8}")
