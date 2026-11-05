from decimal import Decimal as D, ROUND_HALF_UP
m=D("611.85"); I=D("0.03")
T={k:m*k for k in (4,5,6,8,10)}
PCT=[(T[4],100),(T[5],85),(T[6],53),(T[8],47),(T[10],37),(None,32)]
def old(P):
    P=D(P); b=min(P,T[4])
    if P>T[4]: b+=D("0.9")*(min(P,T[5])-T[4])
    if P>T[5]: b+=D("0.75")*(P-T[5])
    return I*b
def pct(P):
    P=D(P)
    if P<=T[4]: return D(100)
    if P<=T[5]: return D(85)
    if P<=T[6]: return D(53)
    if P<=T[8]: return D(47)
    if P<=T[10]: return D(37)
    return D(32)
def new(P):
    P=D(P); a=I*P*pct(P)/100
    # limite maggiorato: soglia k con percentuale della fascia sopra la soglia
    for t,p in ((T[4],85),(T[5],53),(T[6],47),(T[8],37),(T[10],32)):
        # limite = soglia + quota di rivalutazione sulla soglia secondo la fascia sotto la soglia
        pass
    return a
def L(k,pctbelow): return T[k]*(1+I*D(pctbelow)/100)
def new_floor(P):
    P=D(P); a=new(P)
    for k,pb in ((4,100),(5,85),(6,53),(8,47),(10,37)):
        if T[k]<P<L(k,pb): a=max(a,L(k,pb)-P)
    return a
def r(x): return int(D(x).quantize(D(1),rounding=ROUND_HALF_UP))
if __name__=="__main__":
    for P in (7000,5000,5100,3800,3300,2700,2450,2500,1500,2000):
        o,n=old(P),new_floor(P); d=o-n
        print(P,"old",o.quantize(D("0.01")),"new",n.quantize(D("0.01")),"diff",d.quantize(D("0.01")),"x13",(d*13).quantize(D("0.01")),"| r:",r(o),r(n),r(d),r(d*13))
    print("L4",L(4,100).quantize(D("0.01")))
