"""Calcolo aumento NETTO pensioni gennaio 2027 (video 11). Parametri: Irpef 2026 (23% fino a 28.000, 33% fino a 50.000, 43% oltre),
detrazione pensionati art. 13 c.3 TUIR come da Agenzia Entrate circolare 4/E 2022 (1.955 fino a 8.500; 700+1.255*(28.000-R)/19.500 fino a 28.000;
700*(50.000-R)/22.000 fino a 50.000) + 50 euro tra 25.001 e 29.000. Solo reddito da pensione, 13 mensilita', niente altre detrazioni.
Rivalutazione per scaglioni: 100% fino a 4 x minimo, 90% tra 4 e 5 x, 75% oltre 5 x (minimo 2026 = 611,85, soglie 2027 approssimate)."""
M=611.85
def irpef_lorda(R):
    t=0.23*min(R,28000)
    if R>28000: t+=0.33*(min(R,50000)-28000)
    if R>50000: t+=0.43*(R-50000)
    return t
def detr(R):
    if R<=8500: d=max(1955,713)
    elif R<=28000: d=700+1255*(28000-R)/19500
    elif R<=50000: d=700*(50000-R)/22000
    else: d=0
    if 25000<R<=29000: d+=50
    return d
def netto_anno(P):
    R=13*P
    return R-max(0,irpef_lorda(R)-detr(R))
def aumento_lordo(P,r):
    a=min(P,4*M)*r
    a+=max(0,min(P,5*M)-4*M)*0.9*r
    a+=max(0,P-5*M)*0.75*r
    return a
def riga(P,r):
    d=aumento_lordo(P,r)
    dn=(netto_anno(P+d)-netto_anno(P))/13
    return d,dn
if __name__=='__main__':
    print('pensione lorda | r | aumento lordo/mese | aumento netto/mese | quota netta | netto/anno')
    for P in (611.85,700,800,1000,1200,1500,1800,2000,2200,2500,3000,3500,4000):
        for r in (0.026,0.029):
            d,dn=riga(P,r)
            print(f'{P:8.2f} | {r*100:.1f}% | {d:6.2f} | {dn:6.2f} | {dn/d*100:5.1f}% | {dn*13:7.0f}')
    print('netto mensile oggi (media su 13):')
    for P in (1000,1500,2000,2500,3000): print(P, round(netto_anno(P)/13,2), 'Irpef anno', round(13*P-netto_anno(P)))
