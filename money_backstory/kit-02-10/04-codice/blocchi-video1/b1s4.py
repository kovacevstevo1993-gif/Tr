from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, subprocess
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); grey=(150,165,185)
FPS=30; DUR=6.8; N=int(round(FPS*DUR))
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
bg=Image.new('RGBA',(W,H),navy+(255,))
g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,120)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
fT=ImageFont.truetype(F+'Gloock-Regular.ttf',76); fB=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',46); fX=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',150)
fK=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',60)
def txt(L,t,f,y,col,alpha=255,x=None):
    d=ImageDraw.Draw(L); b=d.textbbox((0,0),t,font=f); w=b[2]-b[0]
    d.text(((W-w)/2-b[0] if x is None else x-w/2-b[0],y-b[1]),t,font=f,fill=col+(int(alpha),))
def person(d,cx,cy,col,a):
    c=col+(int(255*a),)
    d.ellipse([cx-50,cy-190,cx+50,cy-90],fill=c)
    d.rounded_rectangle([cx-85,cy-70,cx+85,cy+110],radius=60,fill=c)
# blurred secret card prerender
sec=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sec)
txt(sec,'THE SURVIVOR CHECK RULE',fK,760,white)
secb=sec.filter(ImageFilter.GaussianBlur(14))
for fn in range(N):
    t=fn/FPS*1.2353; fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.5); txt(L,'1 RULE MOST MARRIED COUPLES MISS',fT,90+int((1-a)*-25),goldL,255*a)
    p=ease((t-0.4)/0.6); person(d,W/2-150,420,white,p); person(d,W/2+150,420,gold,p)
    q=back((t-1.3)/0.45)
    if t>1.3:
        s=max(0.01,q); r=int(70*s)
        d.ellipse([W/2-r,300-r,W/2+r,300+r],fill=red+(255,))
        fx=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',max(8,int(96*s)))
        b=d.textbbox((0,0),'!',font=fx); d.text((W/2-(b[2]-b[0])/2-b[0],300-(b[3]-b[1])/2-b[1]),'!',font=fx,fill=(255,255,255,255))
    fr=Image.alpha_composite(fr,L)
    c=ease((t-2.4)/0.6)
    if c>0:
        Cd=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(Cd)
        cd.rounded_rectangle([W/2-560,690,W/2+560,860],radius=30,fill=(22,40,64,int(240*c)),outline=gold+(int(255*c),),width=4)
        fr=Image.alpha_composite(fr,Cd)
        sb=secb.copy(); al=sb.split()[3].point(lambda px:int(px*c)); sb.putalpha(al); fr=Image.alpha_composite(fr,sb)
        # lock icon
        Lk=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(Lk); lx,ly=W/2+500,775
        ld.rounded_rectangle([lx-34,ly-10,lx+34,ly+42],radius=8,fill=gold+(int(255*c),))
        ld.arc([lx-24,ly-50,lx+24,ly+6],180,360,fill=gold+(int(255*c),),width=9)
        fr=Image.alpha_composite(fr,Lk)
    e=ease((t-4.5)/0.5)
    if e>0:
        E=Image.new('RGBA',(W,H),(0,0,0,0)); txt(E,'REVEALED LATER IN THIS VIDEO',fB,930+int((1-e)*20),gold,255*e); fr=Image.alpha_composite(fr,E)
    fr.convert('RGB').save(f'fr4/{fn:04d}.png')
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i','fr4/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','/mnt/user-data/outputs/v1-b1-04.mp4'],check=True)
