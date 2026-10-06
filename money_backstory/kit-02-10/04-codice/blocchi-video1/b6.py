from common import *
import shutil
bg=make_bg(); bgg=make_bg(grid=True)
def cardpop(fr,cx,cy,w,h,col,lines,t,st):
    if t<st: return fr
    C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C)
    d.rounded_rectangle([cx-w/2,cy-h/2,cx+w/2,cy+h/2],radius=34,fill=card+(255,),outline=col+(255,),width=5)
    y=cy-h/2+60
    for text,f,c in lines:
        txt(C,text,f,y,c,255,x=cx); y+=f.size+30
    return pop(fr,C,(int(cx-w/2-5),int(cy-h/2-5),int(cx+w/2+5),int(cy+h/2+5)),back((t-st)/0.45))
def drawA(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    txt(L,'THE REAL QUESTION ISN\'T "WHICH AGE?"',SER(66),110,goldL,255*ease(t/0.5)); fr=Image.alpha_composite(fr,L)
    fr=cardpop(fr,W/2-430,560,760,420,gold,[('1',BOLD(110),gold),('HOW LONG WILL',BOLD(52),white),('YOU LIVE?',BOLD(52),white)],t,3.7)
    fr=cardpop(fr,W/2+430,560,760,420,blue,[('2',BOLD(110),blue),('HOW MUCH DO YOU',BOLD(52),white),('NEED RIGHT NOW?',BOLD(52),white)],t,6.3)
    return fr
def person(d,cx,cy,col,s=1):
    d.ellipse([cx-40*s,cy-120*s,cx+40*s,cy-40*s],fill=col+(255,)); d.rounded_rectangle([cx-70*s,cy-25*s,cx+70*s,cy+100*s],radius=int(50*s),fill=col+(255,))
def drawB(t):
    fr=bgg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'MOST PEOPLE UNDERESTIMATE THIS',SER(66),90,goldL,255*ease(t/0.5))
    x0,x1=560,1700
    def ax(a): return x0+(a-65)/(95-65)*(x1-x0)
    if t>3.7:
        a=ease((t-3.7)/0.5)
        for age in range(65,96,5):
            d.line([ax(age),820,ax(age),835],fill=(255,255,255,int(120*a)),width=3); txt(L,str(age),REG(30),850,grey,255*a,x=ax(age))
        d.line([x0,820,x1,820],fill=gold+(int(255*a),),width=4)
        txt(L,'LIFE EXPECTANCY AT 65',BOLD(40),250,white,255*a)
    fr=Image.alpha_composite(fr,L)
    rows=[('MEN',blue,84,400,3.9),('WOMEN',(230,140,190),87,620,12.2)]
    for lab,col,age,y,st in rows:
        if t<st: continue
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        person(d,250,y+60,col,1.0); txt(L,lab,BOLD(40),y+180,col,255,x=250)
        p=ease((t-st-0.3)/2.0); cur=65+(age-65)*p
        d.rounded_rectangle([x0,y+10,ax(cur),y+120],radius=24,fill=col+(255,))
        txt(L,f'~{int(round(cur))}',BOLD(80),y+22,navy if p>0.5 else col,255,x=max(ax(cur)-110,x0+110))
        fr=Image.alpha_composite(fr,L)
    if t>6:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'Source: SSA.gov',REG(28),1010,grey,255*ease((t-6)/0.5)); fr=Image.alpha_composite(fr,L)
    return fr
def drawC(t):
    fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0))
    a=ease(t/0.4); txt(L,'THOSE ARE ONLY AVERAGES.',SER(90),250,white,255*a); fr=Image.alpha_composite(fr,L)
    if t>2.49:
        s=back((t-2.49)/0.45); S=Image.new('RGBA',(W,H),(0,0,0,0)); txt(S,'90+',BOLD(260),430,gold)
        G=S.filter(ImageFilter.GaussianBlur(28)); fr=pop(fr,G,(560,400,1360,760),s); fr=pop(fr,S,(560,400,1360,760),s)
        L=Image.new('RGBA',(W,H),(0,0,0,0)); pill(L,'MILLIONS OF AMERICANS WILL GET THERE',840,alpha=255*ease((t-3.0)/0.5),size=44); fr=Image.alpha_composite(fr,L)
    return fr
render(drawA,9.22,'/mnt/user-data/outputs/v1-b6-01.mp4'); shutil.copy('/home/claude/_fr/0260.png','/home/claude/x6a.png')
render(drawB,14.25,'/mnt/user-data/outputs/v1-b6-02.mp4'); shutil.copy('/home/claude/_fr/0420.png','/home/claude/x6b.png')
render(drawC,6.54,'/mnt/user-data/outputs/v1-b6-03.mp4'); shutil.copy('/home/claude/_fr/0190.png','/home/claude/x6c.png')
