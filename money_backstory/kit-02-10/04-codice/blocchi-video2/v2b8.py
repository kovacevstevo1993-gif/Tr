from common2 import *
import shutil, sys
S=["Mistake number two: underestimating health care.","Many people think Medicare covers almost everything.","It doesn't.","According to Fidelity's 2026 estimate, a sixty five year old retiring today may need about one hundred eighty five thousand five hundred dollars, after taxes, just for health care in retirement.","And that's for one person.","For a couple, it's roughly double."]
TOTF=775
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1]+fs[2],fs[3],fs[4]+fs[5]]; print(fs,durs,sum(durs))
def person(d,cx,cy,col,s=1.0):
    d.ellipse([cx-40*s,cy-120*s,cx+40*s,cy-40*s],fill=col); d.rounded_rectangle([cx-70*s,cy-25*s,cx+70*s,cy+100*s],radius=int(50*s),fill=col)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.35); txt(L,'MISTAKE #2',BOLD(110),160,blue,255*a)
    cx,cy=W/2,520; s=1+0.05*math.sin(t*4)
    d.rounded_rectangle([cx-30*s,cy-100*s,cx+30*s,cy+100*s],radius=10,fill=blue+(255,)); d.rounded_rectangle([cx-100*s,cy-30*s,cx+100*s,cy+30*s],radius=10,fill=blue+(255,))
    txt(L,'UNDERESTIMATING HEALTH CARE',BOLD(56),720,white,255*ease((t-0.3)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'"MEDICARE COVERS ALMOST EVERYTHING"',SER(60),120,white,255*ease(t/0.4))
    cx,cy=W/2,560; p=ease((t-0.3)/1.0)
    # shield
    sh=[(cx,cy-230),(cx+200,cy-150),(cx+180,cy+80),(cx,cy+230),(cx-180,cy+80),(cx-200,cy-150)]
    d.polygon(sh,fill=(40,70,110,int(255*p)),outline=blue+(int(255*p),)); d.line(sh+[sh[0]],fill=blue+(int(255*p),),width=8)
    txt(L,'MEDICARE',BOLD(48),cy-30,white,255*p,x=cx)
    fr=Image.alpha_composite(fr,L)
    s3=fs[1]/30
    if t>s3:
        q=ease((t-s3)/0.3); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        cr=[(cx-20,cy-230),(cx+30,cy-120),(cx-40,cy-30),(cx+40,cy+60),(cx-10,cy+230)]
        d.line(cr[:max(2,int(len(cr)*q))],fill=red+(255,),width=10)
        fr=Image.alpha_composite(fr,L)
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(80); lab="IT DOESN'T."; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+90; bx=(W-bw)/2; by=820
        cd.rounded_rectangle([bx,by,bx+bw,by+130],radius=30,fill=red+(255,)); cd.text((bx+45-b[0],by+65-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=pop(fr,C,(int(bx)-5,by-5,int(bx+bw)+5,by+135),back((t-s3)/0.35))
    return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"WHAT MEDICARE STILL LEAVES YOU TO PAY",SER(56),95,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    # receipt
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x0,x1,y0=W/2-620,W/2-40,200
    cd.rectangle([x0,y0,x1,y0+700],fill=(240,236,225,255))
    for k in range(0,int(x1-x0),30): cd.polygon([(x0+k,y0+700),(x0+k+15,y0+720),(x0+k+30,y0+700)],fill=(240,236,225,255))
    txt(C,'HEALTH CARE BILL',BOLD(40),y0+30,navy,255,x=(x0+x1)/2)
    items=['Medicare premiums','Deductibles','Copays','Prescription drugs','Dental & vision*']
    for k,it in enumerate(items):
        st=0.5+k*0.7; a=ease((t-st)/0.3)
        if a<=0: continue
        yy=y0+110+k*90; txt(C,it,REG(36),yy,navy,255*a,x=x0+40,anchor='l'); txt(C,'$ ✓' if False else '$$$',BOLD(38),yy,red,255*a,x=x1-40,anchor='r')
        cd.line([x0+40,yy+60,x1-40,yy+60],fill=(190,185,170,int(255*a)),width=2)
    fr=Image.alpha_composite(fr,C)
    if t>4.0:
        p=ease((t-4.0)/1.4); v=int(185500*p/100)*100
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'LIFETIME TOTAL',BOLD(40),330,goldL,255,x=W/2+380)
        txt(L,f'${v:,}',BOLD(120),400,red,255,x=W/2+380); txt(L,'per person · after taxes',REG(34),560,white,255,x=W/2+380)
        txt(L,'Source: Fidelity Retiree Health Care Cost Estimate 2026',REG(26),980,grey,200); txt(L,'*mostly not covered by Original Medicare',REG(24),945,grey,200,x=x0,anchor='l')
        fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawD(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'ONE PERSON VS A COUPLE',SER(66),110,goldL,255*ease(t/0.4))
    person(d,520,470,(236,240,245,255),1.3); txt(L,'$185,500',BOLD(84),650,white,255,x=520); txt(L,'ONE PERSON',BOLD(34),760,grey,255,x=520)
    fr=Image.alpha_composite(fr,L)
    s6=fs[4]/30
    if t>s6:
        p=ease((t-s6)/1.2); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        person(d,1300,470,(236,240,245,255),1.3); person(d,1470,470,(230,140,190,255),1.3)
        v=int(185500+185500*p); txt(L,f'~${v//1000*1000:,}',BOLD(84),650,red,255,x=1385); txt(L,'A COUPLE',BOLD(34),760,grey,255,x=1385)
        fr=Image.alpha_composite(fr,L)
        if t>s6+1.2:
            L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'ROUGHLY DOUBLE',880,col=red,alpha=255*ease((t-s6-1.2)/0.4),size=46); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b8-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y8{i}.png')
