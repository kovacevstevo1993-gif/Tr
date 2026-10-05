from common2 import *
import shutil, sys
S=["And you can't wait forever.","Required minimum distributions force you to start withdrawing money at age seventy three, or seventy five if you were born in 1960 or later.","Those withdrawals can push you into a higher tax bracket.","They can even make more of your Social Security taxable, and raise your Medicare premiums.","So plan your withdrawals years in advance, not the year the IRS forces you."]
TOTF=814
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2]+fs[3],fs[4]]; print(fs,durs,sum(durs))
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,"YOU CAN'T WAIT FOREVER",SER(70),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    s2=fs[0]/30
    if t>s2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'REQUIRED MINIMUM DISTRIBUTIONS (RMDs)',BOLD(44),220,white,255*ease((t-s2)/0.4)); fr=Image.alpha_composite(fr,L)
        for k,(age,sub,col,dt) in enumerate([('73','start age',gold,0.6),('75','if born in 1960 or later',red,(fs[1]/30)*0.6)]):
            if t<s2+dt: continue
            C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k*2-1)*380; y=560
            cd.rounded_rectangle([x-300,y-230,x+300,y+230],radius=34,fill=card+(255,),outline=col+(255,),width=6)
            txt(C,'AGE',BOLD(44),y-200,grey,255,x=x); txt(C,age,BOLD(200),y-150,col,255,x=x); txt(C,sub,BOLD(36),y+130,white,255,x=x)
            fr=pop(fr,C,(int(x-305),y-235,int(x+305),y+235),back((t-s2-dt)/0.45))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'Source: IRS (SECURE 2.0 Act)',REG(26),985,grey,200); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'THE DOMINO EFFECT',SER(70),100,goldL,255*ease(t/0.4))
    base_=820; x0=260
    for k in range(5):
        h=100+k*80; x=x0+k*140; col=tuple(int(gold[i]+(red[i]-gold[i])*k/4) for i in range(3))
        d.rounded_rectangle([x,base_-h,x+120,base_],radius=10,fill=col+(200,))
    txt(L,'TAX BRACKETS',BOLD(28),base_+16,grey,255,x=x0,anchor='l')
    p=ease((t-0.5)/1.5); yb=base_-100-80*4*p; xb=x0+60+140*4*p
    d.ellipse([xb-26,yb-80,xb+26,yb-28],fill=white+(255,))
    fr=Image.alpha_composite(fr,L)
    items=[('HIGHER TAX BRACKET',red,0.3),('MORE SOCIAL SECURITY TAXED',gold,fs[2]/30),('HIGHER MEDICARE PREMIUMS',purple,fs[2]/30+2.2)] if False else [('HIGHER TAX BRACKET',red,0.3),('MORE SOCIAL SECURITY TAXED',gold,fs[2]/30),('HIGHER MEDICARE PREMIUMS',(170,130,230),fs[2]/30+2.2)]
    for k,(lab,col,st) in enumerate(items):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); y=300+k*180; x0b=950
        cd.rounded_rectangle([x0b,y,x0b+740,y+130],radius=30,fill=card+(255,),outline=col+(255,),width=5)
        cd.polygon([(x0b+40,y+85),(x0b+65,y+40),(x0b+90,y+85)],fill=col+(255,))
        txt(C,lab,BOLD(34),y+46,white,255,x=x0b+110,anchor='l')
        fr=pop(fr,C,(x0b-5,y-5,x0b+745,y+135),back((t-st)/0.4))
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'PLAN YOUR WITHDRAWALS YEARS IN ADVANCE',SER(58),100,goldL,255*ease(t/0.4))
    X0,X1,y=240,1680,520
    def ax(a): return X0+(a-60)/(76-60)*(X1-X0)
    d.line([X0,y,X1,y],fill=gold+(255,),width=4)
    for a in range(60,77,2): d.line([ax(a),y-10,ax(a),y+10],fill=gold+(255,),width=3); txt(L,str(a),REG(28),y+24,grey,255,x=ax(a))
    p=ease((t-0.3)/1.2); d.rounded_rectangle([ax(60),y-150,ax(60)+(ax(72)-ax(60))*p,y-40],radius=30,fill=green+(255,))
    if p>0.9: txt(L,'PLAN HERE',BOLD(44),y-122,navy,255,x=(ax(60)+ax(72))/2)
    if t>1.4:
        q=ease((t-1.4)/0.5); d.rounded_rectangle([ax(73)-40,y-150,ax(73)+40+(ax(75)-ax(73))*0,y-40],radius=20,fill=red+(int(255*q),))
        txt(L,'RMD',BOLD(34),y-116,(255,255,255),255*q,x=ax(73))
    if t>2.0:
        txt(L,'NOT THE YEAR THE IRS FORCES YOU',BOLD(50),y+130,red,255*ease((t-2.0)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b22-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y22{i}.png')
