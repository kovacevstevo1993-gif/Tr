from common2 import *
import shutil, sys
S=["Let's put that into numbers.","Say you need forty thousand dollars a year from your savings.","If you plan for twenty years, you think you need eight hundred thousand dollars.","But if you live thirty years, you need one point two million.","That's four hundred thousand dollars missing, right at the age when you can't go back to work."]
TOTF=606
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2]+fs[3],fs[4]]; print(fs,durs,sum(durs)); s2=fs[0]/30; s4=fs[2]/30
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"LET'S PUT IT INTO NUMBERS",SER(68),120,goldL,255*ease(t/0.4))
    # calculator icon
    cx,cy=560,560; a=ease((t-0.3)/0.4)
    d.rounded_rectangle([cx-130,cy-190,cx+130,cy+190],radius=26,fill=card+(int(255*a),),outline=gold+(int(255*a),),width=5)
    d.rounded_rectangle([cx-100,cy-160,cx+100,cy-90],radius=10,fill=(10,20,34,int(255*a)))
    for r in range(4):
        for c in range(3):
            x=cx-80+c*80; y=cy-50+r*60; col=gold if (r==3 and c==2) else (60,90,130)
            d.rounded_rectangle([x-28,y-20,x+28,y+20],radius=8,fill=col+(int(255*a),))
    fr=Image.alpha_composite(fr,L)
    if t>s2:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); p=ease((t-s2)/1.2); v=int(40000*p/100)*100
        txt(L,f'${v:,}',BOLD(150),400,green,255,x=1230); txt(L,'PER YEAR',BOLD(56),580,white,255*p,x=1230); txt(L,'from your savings',REG(40),660,grey,255*p,x=1230)
        fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'$40,000 × YEARS OF RETIREMENT',SER(62),100,goldL,255*ease(t/0.4))
    base_=900; bw=300; xA=W/2-300; xB=W/2+300; unit=19
    d.line([380,base_,1540,base_],fill=gold+(255,),width=4)
    fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    nA=int(20*ease((t-0.3)/1.8))
    for k in range(nA):
        y=base_-(k+1)*unit; d.rounded_rectangle([xA-bw/2,y+2,xA+bw/2,y+unit-1],radius=4,fill=gold+(255,))
    txt(L,'PLAN: 20 YEARS',BOLD(36),base_+20,white,255,x=xA)
    if nA>=20: txt(L,'$800,000',BOLD(72),base_-20*unit-100,gold,255,x=xA)
    if t>s4:
        nB=int(30*ease((t-s4)/2.0))
        for k in range(nB):
            y=base_-(k+1)*unit; col=gold if k<20 else red
            d.rounded_rectangle([xB-bw/2,y+2,xB+bw/2,y+unit-1],radius=4,fill=col+(255,))
        txt(L,'REALITY: 30 YEARS',BOLD(36),base_+20,white,255,x=xB)
        if nB>=30: txt(L,'$1,200,000',BOLD(72),base_-30*unit-100,red,255,x=xB)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawC(t):
    fr=base(t)
    p=ease((t-0.2)/1.4); v=int(400000*p/1000)*1000
    G=Image.new('RGBA',(W,H),(0,0,0,0)); txt(G,f'-${v:,}',BOLD(200),260,red,200); fr=Image.alpha_composite(fr,G.filter(ImageFilter.GaussianBlur(28)))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'-${v:,}',BOLD(200),260,red); txt(L,'MISSING',BOLD(70),520,white,255*ease((t-0.8)/0.4))
    fr=Image.alpha_composite(fr,L)
    if t>1.8:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(44); lab="RIGHT WHEN YOU CAN'T GO BACK TO WORK"; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=(W-bw)/2; y=700
        cd.rounded_rectangle([bx,y,bx+bw,y+96],radius=48,fill=gold+(255,)); cd.text((bx+40-b[0],y+48-(b[3]-b[1])/2-b[1]),lab,font=f,fill=navy+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+101),back((t-1.8)/0.45))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b4-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y4{i}.png')
