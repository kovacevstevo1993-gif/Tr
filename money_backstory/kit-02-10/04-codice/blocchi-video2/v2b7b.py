from common2 import *
import shutil, sys
S=["And living longer brings us straight to the second mistake,","because the longer you live, the more you spend on one thing most people completely ignore."]
TOTF=299
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1]); print(fs,sum(fs))
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0))
    txt(L,'NEXT',BOLD(44),260,grey,255*ease(t/0.3)); fr=Image.alpha_composite(fr,L)
    S2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S2,'MISTAKE #2',BOLD(170),340,blue)
    fr=pop(fr,S2.filter(ImageFilter.GaussianBlur(24)),(300,320,1620,560),back((t-0.1)/0.45)); fr=pop(fr,S2,(300,320,1620,560),back((t-0.1)/0.45))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); p=ease((t-0.6)/0.8)
    d.line([W/2-400,640,W/2-400+800*p,640],fill=blue+(255,),width=6); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'THE LONGER YOU LIVE, THE MORE YOU SPEND',SER(58),100,goldL,255*ease(t/0.4))
    X0,X1,Y0,Y1=240,1150,860,280
    d.line([X0,Y0,X1,Y0],fill=gold+(255,),width=3); d.line([X0,Y0,X0,Y1],fill=gold+(255,),width=3)
    for a,lab in [(0,'65'),(0.5,'80'),(1,'95')]: txt(L,lab,REG(30),Y0+16,grey,255,x=X0+(X1-X0)*a)
    txt(L,'AGE',BOLD(26),Y0+56,grey,255,x=X1,anchor='r'); txt(L,'TOTAL SPENT',BOLD(26),Y1-40,grey,255,x=X0,anchor='l')
    p=ease((t-0.3)/2.2); n=int(p*100)
    pts=[(X0+(X1-X0)*k/100, Y0-(Y0-Y1)*((k/100)**1.8)*0.95) for k in range(n+1)]
    if len(pts)>1:
        A=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(A).polygon(pts+[(pts[-1][0],Y0),(X0,Y0)],fill=red+(50,)); fr=Image.alpha_composite(fr,A)
        d.line(pts,fill=red+(255,),width=8)
    fr=Image.alpha_composite(fr,L)
    if t>2.6:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=1480,560
        cd.rounded_rectangle([cx-230,cy-230,cx+230,cy+230],radius=34,fill=card+(255,),outline=blue+(255,),width=5)
        txt(C,'?',BOLD(200),cy-150,blue,255*(0.7+0.3*math.sin(t*6)),x=cx); txt(C,'ONE THING',BOLD(38),cy+95,white,255,x=cx); txt(C,'MOST PEOPLE IGNORE',BOLD(30),cy+150,grey,255,x=cx)
        fr=pop(fr,C,(cx-235,cy-235,cx+235,cy+235),back((t-2.6)/0.45))
    return frame(fr)
render(drawB,fs[1]/30,'/mnt/user-data/outputs/v2-b7-02.mp4')
