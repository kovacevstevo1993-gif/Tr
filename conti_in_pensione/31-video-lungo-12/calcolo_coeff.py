#!/usr/bin/env python3
"""Calcoli del video lungo 12 (coefficienti di trasformazione 2027). Tutte le cifre del copione vengono da qui.
Fonti (testi in questa cartella): fonte-decreto-16-10-2026.txt (tabella 2027, Ministero del Lavoro), fonte-decreto-20-11-2024.txt
(tabella 2025-2026), fonte-inps-comunicato-21-12-2022.txt (tabella 2023-2024), fonte-legge-335-1995-art1-c6.txt (frazioni di anno)."""
T2324={57:4.270,58:4.378,59:4.493,60:4.615,61:4.744,62:4.882,63:5.028,64:5.184,65:5.352,66:5.531,67:5.723,68:5.931,69:6.154,70:6.395,71:6.655}
T2526={57:4.204,58:4.308,59:4.419,60:4.536,61:4.661,62:4.795,63:4.936,64:5.088,65:5.250,66:5.423,67:5.608,68:5.808,69:6.024,70:6.258,71:6.510}
T27  ={57:4.153,58:4.254,59:4.361,60:4.475,61:4.596,62:4.725,63:4.863,64:5.009,65:5.166,66:5.334,67:5.514,68:5.707,69:5.914,70:6.139,71:6.382}
# variazioni ufficiali Tab. D della nota tecnica (2025-26 -> 2027), per controllo
TABD={57:-1.21,58:-1.25,59:-1.31,60:-1.34,61:-1.39,62:-1.46,63:-1.48,64:-1.55,65:-1.60,66:-1.64,67:-1.68,68:-1.74,69:-1.83,70:-1.90,71:-1.97}
def coef_mesi(T,eta,mesi):  # legge 335/1995 art. 1 c. 6: + 1/12 della differenza con l'eta' superiore per ogni mese
    return T[eta]+(T[eta+1]-T[eta])/12*mesi
if __name__=='__main__':
    print('controllo Tab. D (variazione 2025-26 -> 2027):')
    for e in T27:
        v=(T27[e]/T2526[e]-1)*100
        print(e, round(v,2), TABD[e], 'OK' if abs(round(v,2)-TABD[e])<0.015 else 'DIVERSO')
    print('67 anni: 23-24 -> 25-26 %.4f%%; 25-26 -> 27 %.4f%%; 23-24 -> 27 %.4f%%'%((T2526[67]/T2324[67]-1)*100,(T27[67]/T2526[67]-1)*100,(T27[67]/T2324[67]-1)*100))
    for M in (100000,150000,250000,300000,400000):
        print('montante',M,'67 anni: 23-24 %.2f | 25-26 %.2f | 27 %.2f | perdita 25-26->27 %.2f/anno (%.2f/mese su 13) | perdita 23-24->27 %.2f/anno'%(
            M*T2324[67]/100,M*T2526[67]/100,M*T27[67]/100,M*(T2526[67]-T27[67])/100,M*(T2526[67]-T27[67])/100/13,M*(T2324[67]-T27[67])/100))
    print('perdita per 100.000 di montante (25-26 -> 27):')
    for e in (62,64,65,66,67,68,70): print(' ',e,'anni: %.0f euro/anno'%(100000*(T2526[e]-T27[e])/100))
    print('mesi di attesa per tornare al coefficiente 2025-26 (solo effetto coefficiente, stesso montante), per ogni eta:')
    for e in range(57,71):
        mesi=(T2526[e]-T27[e])/((T27[e+1]-T27[e])/12)
        print(' ',e,'anni: %.2f mesi'%mesi)
    print('67 anni e 1 mese nel 2027: %.4f%% (2026 a 67 anni: %.3f%%, variazione %.2f%%)'%(coef_mesi(T27,67,1),T2526[67],(coef_mesi(T27,67,1)/T2526[67]-1)*100))
    print('67 anni e 6 mesi nel 2027: %.4f%%'%coef_mesi(T27,67,6))
