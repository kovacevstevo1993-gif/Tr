from common2 import *
import shutil, sys
S=["Here's a simple rule.","Divide seventy two by the inflation rate, and you get the number of years it takes for prices to double.","At three percent inflation, prices double in about twenty four years.","At four percent, in just eighteen.","So if you need fifty thousand dollars a year at sixty five, you could need around one hundred thousand dollars a year at eighty nine, just to live the same life."]
TOTF=795
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2]+fs[3],fs[4]]; print(fs,durs,sum(durs)); s2=fs[0]/30; s4=fs[2]/30
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'THE RULE OF 72',SER(96),130,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    if t>s2:
        parts=[('72',gold,0),('÷',white,0.5),('INFLATION RATE',blue,1.0),('=',white,1.8),('YEARS TO DOUBLE PRICES',red,2.4)]
        xs=[330,520,860,1210,1540]
        for (s,col,dt),x in zip(parts,xs):
            if t<s2+dt: continue
            C=Image.new('RGBA',(W,H),(0,0,0,0)); f=BOLD(150 if len(s)<=2 else 44)
            if len(s)>2:
                cd=ImageDraw.Draw(C); words=s.split(' ')
                lines=[' '.join(words[:len(words)//2+len(words)%2]),' '.join(words[len(words)//2+len(words)%2:])] if len(words)>2 else [s]
                cd.rounded_rectangle([x-170,440,x+170,640],radius=28,fill=card+(255,),outline=col+(255,),width=5)
                for k,ln in enumerate(lines): txt(C,ln,BOLD(40),(518 if len(lines)==1 else 490)+k*55,col,255,x=x)
            else:
                txt(C,s,f,450,col,255,x=x)
            fr=pop(fr,C,(int(x-180),420,int(x+180),660),back((t-s2-dt)/0.4))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'HOW FAST PRICES DOUBLE',SER(66),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    rows=[('3% INFLATION','72 ÷ 3 = 24 YEARS',24,gold,0.2,330),('4% INFLATION','72 ÷ 4 = 18 YEARS',18,red,s4,620)]
    X0,X1=680,1640
    for lab,eq,yrs,col,st,y in rows:
        if t<st: continue
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); p=ease((t-st)/1.2); a=ease((t-st)/0.3)
        txt(L,lab,BOLD(44),y+24,col,255*a,x=230,anchor='l')
        xe=X0+(X1-X0)*(yrs/24)*p; d.rounded_rectangle([X0,y,xe,y+100],radius=50,fill=col+(255,))
        txt(L,eq,BOLD(42),y+130,white,255*ease((t-st-0.8)/0.4),x=X0,anchor='l')
        if p>0.9: txt(L,f'{yrs} YRS',BOLD(46),y+24,navy,255,x=xe-110)
        fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'SAME LIFE, DOUBLE THE COST',SER(64),90,goldL,255*ease(t/0.4))
    X0,X1,Y0,Y1=300,1620,860,300
    def px(a): return X0+(a-65)/(89-65)*(X1-X0)
    def py(v): return Y0-(v-40000)/(110000-40000)*(Y0-Y1)
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3)
    for a in [65,70,75,80,85,89]: txt(L,str(a),REG(30),Y0+16,grey,255,x=px(a))
    txt(L,'AGE',BOLD(26),Y0+56,grey,255,x=X1,anchor='r')
    fr=Image.alpha_composite(fr,L)
    p=ease((t-0.4)/(fs[4]/30-2.0)); n=int(p*96)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    pts=[(px(65+k/4),py(50000*1.03**(k/4))) for k in range(n+1)]
    if len(pts)>1: d.line(pts,fill=red+(255,),width=9)
    d.ellipse([px(65)-14,py(50000)-14,px(65)+14,py(50000)+14],fill=green+(255,)); txt(L,'$50,000 / year',BOLD(44),py(50000)+30,green,255,x=px(65)+20,anchor='l')
    if p>0.98:
        x,y=px(89),py(50000*1.03**24); d.ellipse([x-16,y-16,x+16,y+16],fill=red+(255,),outline=white+(255,),width=4)
        txt(L,'~$100,000 / year',BOLD(52),y-80,red,255,x=x,anchor='r')
    txt(L,'At 3% inflation per year',REG(28),985,grey,220)
    fr=Image.alpha_composite(fr,L); return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b13-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y13{i}.png')
