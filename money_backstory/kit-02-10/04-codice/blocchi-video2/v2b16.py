from common2 import *
import shutil, sys
S=["One simple way many retirees do this is called the bucket approach.","Bucket one holds cash for the next two or three years of spending.","Bucket two holds safer, steady investments for the years after that.","And bucket three holds long term growth for your seventies, eighties and beyond.","When the market drops, you spend from bucket one, and you never have to sell your growth at the worst possible moment.","And speaking of rising prices, the next mistake is the most expensive bill most families never see coming."]
TOTF=991
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[sum(fs[:4]),fs[4],fs[5]]; st=[sum(fs[:i])/30 for i in range(4)]; print(fs,durs,sum(durs))
purple=(170,130,230)
BK=[('BUCKET 1','CASH','next 2-3 years of spending',blue),('BUCKET 2','SAFER, STEADY','the years after that',gold),('BUCKET 3','LONG-TERM GROWTH','your 70s, 80s and beyond',green)]
def bucket(d,cx,cy,col,fill,label):
    w1,w2,h=170,130,300
    d.polygon([(cx-w1,cy-h/2),(cx+w1,cy-h/2),(cx+w2,cy+h/2),(cx-w2,cy+h/2)],outline=col+(255,),fill=(20,38,62,255))
    d.line([(cx-w1,cy-h/2),(cx+w1,cy-h/2),(cx+w2,cy+h/2),(cx-w2,cy+h/2),(cx-w1,cy-h/2)],fill=col+(255,),width=8)
    if fill>0:
        top=cy+h/2-h*fill; wt=w2+(w1-w2)*fill
        d.polygon([(cx-wt,top),(cx+wt,top),(cx+w2,cy+h/2-6),(cx-w2,cy+h/2-6)],fill=col+(210,))
    d.arc([cx-w1,cy-h/2-110,cx+w1,cy-h/2+110],200,340,fill=col+(255,),width=8)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'THE BUCKET APPROACH',SER(72),90,goldL,255*ease(t/0.4))
    for i,(n,a,b,col) in enumerate(BK):
        s0=st[i+1]; cx=W/2+(i-1)*520; cy=560
        on=t>=s0; fill=ease((t-s0)/1.2) if on else 0
        bucket(d,cx,cy,col if on else (90,110,140),fill,n)
        txt(L,n,BOLD(34),cy+180,col if on else grey,255,x=cx)
        if on:
            a_=ease((t-s0)/0.4); txt(L,a,BOLD(44),cy+230,white,255*a_,x=cx); txt(L,b,REG(30),cy+290,grey,255*a_,x=cx)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WHEN THE MARKET DROPS...',SER(66),90,red,255*ease(t/0.4))
    X0,X1,Y0,Y1=220,900,640,260
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3)
    p=ease((t-0.2)/1.4); n=int(p*60)
    pts=[(X0+(X1-X0)*k/60, Y1+60+ (0 if k<25 else (k-25)*9 if k<40 else 135-(k-40)*4)+math.sin(k*0.7)*8) for k in range(n+1)]
    if len(pts)>1: d.line(pts,fill=red+(255,),width=7)
    txt(L,'MARKET',BOLD(30),Y0+16,grey,255,x=(X0+X1)/2)
    fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    q=ease((t-1.0)/0.6)
    bucket(d,1120,560,blue,0.7-0.35*ease((t-2.0)/1.5),'1'); bucket(d,1520,560,green,0.9,'3')
    txt(L,'BUCKET 1',BOLD(32),740,blue,255*q,x=1120); txt(L,'BUCKET 3',BOLD(32),740,green,255*q,x=1520)
    if t>2.0:
        txt(L,'YOU SPEND FROM HERE',BOLD(30),790,blue,255*ease((t-2.0)/0.4),x=1120)
        d.polygon([(1090,300),(1150,300),(1120,350)],fill=blue+(255,))
    if t>3.2:
        txt(L,'UNTOUCHED',BOLD(30),790,green,255*ease((t-3.2)/0.4),x=1520)
    fr=Image.alpha_composite(fr,L)
    if t>4.2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'NEVER SELL YOUR GROWTH AT THE WORST MOMENT',880,col=green,alpha=255*ease((t-4.2)/0.4),size=40); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'NEXT',BOLD(44),220,grey,255*ease(t/0.3)); fr=Image.alpha_composite(fr,L)
    S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,'MISTAKE #4',BOLD(160),290,purple)
    fr=pop(fr,S2.filter(ImageFilter.GaussianBlur(24)),(330,270,1590,480),back((t-0.2)/0.45)); fr=pop(fr,S2,(330,270,1590,480),back((t-0.2)/0.45))
    if t>1.4:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,700
        cd.rounded_rectangle([cx-90,cy-110,cx+90,cy+110],radius=12,fill=(240,236,225,255))
        for k in range(4): cd.line([cx-60,cy-60+k*35,cx+60,cy-60+k*35],fill=(170,165,150,255),width=6)
        txt(C,'$$$',BOLD(40),cy+60,red,255,x=cx)
        fr=pop(fr,C,(int(cx-95),cy-115,int(cx+95),cy+115),back((t-1.4)/0.45))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'THE MOST EXPENSIVE BILL FAMILIES NEVER SEE COMING',BOLD(40),860,white,255*ease((t-1.8)/0.4)); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b16-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y16{i}.png')
