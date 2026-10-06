from common2 import *
import shutil, sys
S=["If this video helped you, hit like and subscribe to The Money Backstory.","And if you haven't seen it yet, watch our video on when to claim Social Security at sixty two versus seventy.","It could be worth more than one hundred thousand dollars to you.","It's right here on your screen."]
TOTF=488
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1]+fs[2]+fs[3]]; print(fs,durs,sum(durs)); s3=fs[1]/30; s4=(fs[1]+fs[2])/30
logo=Image.open('/mnt/user-data/outputs/logo-the-money-backstory-pro2.png').convert('RGBA').resize((300,300))
m=Image.new('L',(300,300),0); ImageDraw.Draw(m).ellipse([0,0,299,299],fill=255); logo.putalpha(m)
def drawA(t):
    fr=base(t); C=Image.new('RGBA',(W,H),(0,0,0,0)); C.alpha_composite(logo,(int(W/2-150),150))
    fr=pop(fr,C,(int(W/2-155),145,int(W/2+155),455),back(t/0.45))
    L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'THE MONEY BACKSTORY',SER(64),490,goldL,255*ease((t-0.3)/0.4)); fr=Image.alpha_composite(fr,L)
    for i,(lab,col,fg,st) in enumerate([('LIKE',(236,240,245),navy,0.8),('SUBSCRIBE',(204,0,0),(255,255,255),1.4)]):
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(C); f=BOLD(56); b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+(150 if i==0 else 110); x=W/2+(i*2-1)*260; bx=x-bw/2; y=650
        d.rounded_rectangle([bx,y,bx+bw,y+120],radius=60,fill=col+(255,))
        if i==0:
            tx=bx+45; d.rounded_rectangle([tx,y+50,tx+22,y+92],radius=5,fill=navy+(255,)); d.rounded_rectangle([tx+28,y+44,tx+70,y+92],radius=10,fill=navy+(255,)); d.rounded_rectangle([tx+34,y+24,tx+52,y+56],radius=8,fill=navy+(255,))
            d.text((bx+125-b[0],y+60-(b[3]-b[1])/2-b[1]),lab,font=f,fill=fg+(255,))
        else: d.text((bx+55-b[0],y+60-(b[3]-b[1])/2-b[1]),lab,font=f,fill=fg+(255,))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+125),back((t-st)/0.4))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0))
    txt(L,'WATCH NEXT',BOLD(44),190,gold,255*ease(t/0.4),x=130,anchor='l')
    for k,line in enumerate(['WHEN TO CLAIM','SOCIAL SECURITY:','62 VS 70']):
        txt(L,line,SER(76),270+k*100,white if k<2 else goldL,255*ease((t-0.3-k*0.25)/0.4),x=130,anchor='l')
    fr=Image.alpha_composite(fr,L)
    bx0,by0,bx1,by1=1020,300,1800,739
    B=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(B); a=ease((t-0.4)/0.5)
    bd.rounded_rectangle([bx0,by0,bx1,by1],radius=20,fill=(8,18,30,int(230*a)))
    for x in range(bx0+20,bx1-20,40): bd.line([x,by0,x+20,by0],fill=gold+(int(255*a),),width=4); bd.line([x,by1,x+20,by1],fill=gold+(int(255*a),),width=4)
    for y in range(by0+20,by1-20,40): bd.line([bx0,y,bx0,y+20],fill=gold+(int(255*a),),width=4); bd.line([bx1,y,bx1,y+20],fill=gold+(int(255*a),),width=4)
    fr=Image.alpha_composite(fr,B)
    if t>s3:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(44); lab='A $100,000+ DECISION'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; x0=130; y=640
        cd.rounded_rectangle([x0,y,x0+bw,y+100],radius=50,fill=red+(255,)); cd.text((x0+40-b[0],y+50-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=pop(fr,C,(x0-5,y-5,int(x0+bw)+5,y+105),back((t-s3)/0.45))
    if t>s4:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); p=ease((t-s4)/0.5)
        ax0,ay=880,520; ax1=ax0+(bx0-40-ax0)*p; d.line([ax0,ay,ax1,ay],fill=gold+(255,),width=14)
        if p>0.9: d.polygon([(bx0-20,ay),(bx0-60,ay-30),(bx0-60,ay+30)],fill=gold+(255,))
        txt(L,'WATCH NOW',BOLD(40),by1+40,gold,255*p,x=(bx0+bx1)/2); fr=Image.alpha_composite(fr,L)
    return frame(fr)
for i,(fn,f) in enumerate(zip([drawA,drawB],durs),1):
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b25-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y25{i}.png')
