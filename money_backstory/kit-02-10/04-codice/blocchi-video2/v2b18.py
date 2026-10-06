from common2 import *
import shutil, sys
S=["Here's what shocks most families.","Medicare does not pay for this kind of care, called custodial care.","It only covers skilled nursing for a short time, after a qualifying hospital stay, and never more than one hundred days.","After that, the bill goes to you.","And the numbers are huge.","A semi private room in a nursing home costs a median of about one hundred fifteen thousand dollars a year."]
TOTF=840
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2]+fs[3],fs[4]+fs[5]]; print(fs,durs,sum(durs))
purple=(170,130,230)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,"HERE'S WHAT SHOCKS MOST FAMILIES",SER(62),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    s2=fs[0]/30
    if t>s2:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,520
        cd.rounded_rectangle([cx-420,cy-200,cx+420,cy+200],radius=34,fill=card+(255,),outline=purple+(255,),width=5)
        txt(C,'CUSTODIAL CARE',BOLD(76),cy-150,purple,255,x=cx); txt(C,'help with bathing, dressing, eating',REG(38),cy-50,white,255,x=cx)
        fr=pop(fr,C,(int(cx-425),cy-205,int(cx+425),cy+205),back((t-s2)/0.45))
        if t>s2+1.2:
            S2=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(S2); f=BOLD(60); lab='MEDICARE: NOT COVERED'; b=sd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=(W-bw)/2; by=cy+60
            sd.rounded_rectangle([bx,by,bx+bw,by+110],radius=20,fill=red+(255,)); sd.text((bx+40-b[0],by+55-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
            fr=pop(fr,S2,(int(bx)-5,by-5,int(bx+bw)+5,by+115),back((t-s2-1.2)/0.35))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WHAT MEDICARE DOES COVER',SER(64),100,goldL,255*ease(t/0.4))
    X0,X1,y=260,1660,420
    def dx(day): return X0+day/130*(X1-X0)
    # hospital icon
    a=ease((t-0.3)/0.4); d.rounded_rectangle([X0-10,y-150,X0+280,y-40],radius=16,fill=blue+(int(255*a),)); txt(L,'HOSPITAL STAY',BOLD(32),y-112,(255,255,255),255*a,x=X0+135)
    p=ease((t-1.0)/2.2)
    d.rounded_rectangle([dx(0),y,dx(0)+(dx(100)-dx(0))*p,y+110],radius=24,fill=green+(255,))
    if p>0.3: txt(L,'SKILLED NURSING',BOLD(40),y+35,navy,255,x=dx(50))
    for day in [0,20,50]: txt(L,f'DAY {day}',REG(28),y+130,grey,255,x=dx(day))
    txt(L,'short-term only, after a qualifying hospital stay',REG(34),y+200,white,255*ease((t-1.6)/0.4),x=dx(50))
    s4=fs[2]/30
    if t>s4:
        q=ease((t-s4)/0.8); d.rounded_rectangle([dx(100),y,dx(100)+(dx(130)-dx(100))*q,y+110],radius=24,fill=red+(255,))
        d.line([dx(100),y-40,dx(100),y+150],fill=white+(255,),width=4); txt(L,'DAY 100 MAX',BOLD(30),y-80,white,255,x=dx(100)); txt(L,'YOU PAY',BOLD(36),y+35,(255,255,255),255*q,x=(dx(100)+dx(130))/2)
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(56); lab='AFTER THAT: YOU PAY'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=(W-bw)/2; by=820
        cd.rounded_rectangle([bx,by,bx+bw,by+110],radius=55,fill=red+(255,)); cd.text((bx+40-b[0],by+55-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=Image.alpha_composite(fr,L); L=Image.new('RGBA',(W,H),(0,0,0,0)); fr=pop(fr,C,(int(bx)-5,by-5,int(bx+bw)+5,by+115),back((t-s4-0.3)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'NURSING HOME · SEMI-PRIVATE ROOM',SER(58),110,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    s6=fs[4]/30
    if t>s6:
        p=ease((t-s6)/1.8); v=int(114975*p)
        G=Image.new('RGBA',(W,H),(0,0,0,0)); txt(G,f'${v:,}',BOLD(180),260,red,200); fr=Image.alpha_composite(fr,G.filter(ImageFilter.GaussianBlur(28)))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${v:,}',BOLD(180),260,red); txt(L,'PER YEAR (MEDIAN)',BOLD(48),490,white,255*p)
        fr=Image.alpha_composite(fr,L)
        for k,(v2,lab) in enumerate([('~$9,580','PER MONTH'),('~$315','PER DAY')]):
            st=s6+2.0+k*0.8
            if t<st: continue
            C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=W/2+(k*2-1)*300; y=620
            cd.rounded_rectangle([x-250,y,x+250,y+200],radius=30,fill=card+(255,),outline=red+(255,),width=4)
            txt(C,v2,BOLD(76),y+30,red,255,x=x); txt(C,lab,BOLD(36),y+130,white,255,x=x)
            fr=pop(fr,C,(int(x-255),y-5,int(x+255),y+205),back((t-st)/0.4))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'Source: CareScout (Genworth) Cost of Care Survey 2025',REG(26),985,grey,200); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b18-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y18{i}.png')
