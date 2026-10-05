from common2 import *
import shutil, sys
S=["Mistake number three: playing it too safe.","This one feels completely wrong.","Most retirees think the safest thing to do is to keep their money in cash, or in a savings account, where it can never go down.","But there's a silent thief that takes a little every single year: inflation."]
TOTF=590
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0]+fs[1],fs[2],fs[3]]; print(fs,durs,sum(durs)); s2=fs[0]/30
def drawA(t):
    fr=base(t); C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=W/2,400
    cd.rounded_rectangle([cx-200,cy-200,cx+200,cy+200],radius=40,fill=card+(255,),outline=red+(255,),width=8)
    txt(C,'#3',BOLD(190),cy-170,red,255,x=cx)
    op=ease((t-0.5)/0.5); lift=int(40*op)
    cd.rounded_rectangle([cx-45,cy+80,cx+45,cy+160],radius=10,fill=gold+(255,)); cd.arc([cx-35-10*op,cy+35-lift,cx+35-10*op,cy+105-lift],180,360 if op<0.5 else 330,fill=gold+(255,),width=11)
    fr=Image.alpha_composite(fr,C)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'MISTAKE #3: PLAYING IT TOO SAFE',BOLD(64),690,white,255*ease((t-0.8)/0.4))
    if t>s2: txt(L,'"This one feels completely wrong"',SER(52),800,goldL,255*ease((t-s2)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'THE "SAFEST" MOVE?',SER(70),100,goldL,255*ease(t/0.4))
    # bank vault icon
    cx,cy=560,560; a=ease((t-0.2)/0.4)
    d.polygon([(cx-230,cy-120),(cx,cy-230),(cx+230,cy-120)],fill=gold+(int(255*a),))
    for k in range(4): d.rectangle([cx-190+k*110,cy-100,cx-140+k*110,cy+110],fill=gold+(int(255*a),))
    d.rectangle([cx-240,cy+120,cx+240,cy+160],fill=gold+(int(255*a),)); txt(L,'CASH & SAVINGS',BOLD(40),cy+190,white,255*a,x=cx)
    fr=Image.alpha_composite(fr,L)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    X0,X1,Y=1000,1640,520; p=ease((t-1.0)/2.0)
    d.line([X0,Y+200,X1,Y+200],fill=gold+(255,),width=3)
    d.line([X0,Y,X0+(X1-X0)*p,Y],fill=green+(255,),width=10)
    txt(L,'$100,000',BOLD(60),Y-100,green,255*p,x=(X0+X1)/2); txt(L,'the number never goes down',REG(34),Y+40,white,255*p,x=(X0+X1)/2)
    if t>3.0:
        txt(L,'...so it feels safe',BOLD(44),Y+120,goldL,255*ease((t-3.0)/0.4),x=(X0+X1)/2)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'A SILENT THIEF, EVERY SINGLE YEAR',SER(60),90,goldL,255*ease(t/0.4))
    base_=830; yrs=[0,1,5,10]; vals=[100000,100000/1.03,100000/1.03**5,100000/1.03**10]
    d.line([300,base_,1620,base_],fill=gold+(255,),width=3); fr=Image.alpha_composite(fr,L)
    for i,(y,v) in enumerate(zip(yrs,vals)):
        st=0.3+i*0.45; p=ease((t-st)/0.6)
        if p<=0: continue
        x=460+i*330; h=v/100000*460*p; col=tuple(int(green[k]+(red[k]-green[k])*i/3) for k in range(3))
        im=bar(h,col,200); fr.alpha_composite(im,(int(x-100),int(base_-im.height)))
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${int(v/100)*100:,}',BOLD(44),base_-im.height-70,col,255*p,x=x); txt(L,'TODAY' if y==0 else f'YEAR {y}',BOLD(32),base_+18,white,255,x=x); fr=Image.alpha_composite(fr,L)
    if t>2.3:
        S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,'INFLATION',BOLD(110),170,red); fr=pop(fr,S2.filter(ImageFilter.GaussianBlur(20)),(560,150,1360,320),back((t-2.3)/0.45)); fr=pop(fr,S2,(560,150,1360,320),back((t-2.3)/0.45))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'What $100,000 can buy, at 3% inflation per year',REG(28),900,grey,230); fr=Image.alpha_composite(fr,L)
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b12-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y12{i}.png')
