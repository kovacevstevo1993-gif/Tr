from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); green=(84,200,124); grey=(150,165,185); blue=(110,160,230)
FPS=30; DUR=16.2; N=int(round(FPS*DUR))
sents=["We'll answer four questions.","How much you really get at 62, 67 and 70.","At what age waiting finally pays off.","The hidden traps nobody warns you about.","And who should claim early, and who should wait."]
w=[len(s)+10 for s in sents]; tot=sum(w); starts=[]; acc=0
for x in w: starts.append(acc/tot*DUR); acc+=x
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
bg=Image.new('RGBA',(W,H),navy+(255,))
g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,120)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
fT=ImageFont.truetype(F+'Gloock-Regular.ttf',86); fN=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',110)
fL=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',44); fS=ImageFont.truetype(F+'InstrumentSans-Regular.ttf',32)
tiles=[('01','WHAT YOU REALLY GET','at 62, 67 and 70',gold),('02','THE BREAK-EVEN AGE','when waiting pays off',green),('03','THE HIDDEN TRAPS','nobody warns you about',red),('04','EARLY OR WAIT?','who should do what',blue)]
TW,TH=780,300; pos=[(W/2-TW-25,250),(W/2+25,250),(W/2-TW-25,590),(W/2+25,590)]
def tile(num,lab,sub,col,active):
    im=Image.new('RGBA',(TW+60,TH+60),(0,0,0,0))
    sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([38,42,TW+38,TH+42],radius=30,fill=(0,0,0,160)); im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(16)))
    d=ImageDraw.Draw(im); fill=(30,54,86,255) if active else (22,40,64,255)
    d.rounded_rectangle([30,30,TW+30,TH+30],radius=30,fill=fill,outline=col+(255,),width=6 if active else 3)
    b=d.textbbox((0,0),num,font=fN); d.text((80-b[0],30+TH/2-(b[3]-b[1])/2-b[1]),num,font=fN,fill=col+(255,))
    d.text((270,115),lab,font=fL,fill=white+(255,)); d.text((270,185),sub,font=fS,fill=grey+(255,))
    return im
act=[tile(*t,True) for t in tiles]; ina=[tile(*t,False) for t in tiles]
for fn in range(N):
    t=fn/FPS; fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.5); b=d.textbbox((0,0),'4 QUESTIONS WE\'LL ANSWER',font=fT)
    d.text(((W-(b[2]-b[0]))/2-b[0],95+int((1-a)*-25)-b[1]),"4 QUESTIONS WE'LL ANSWER",font=fT,fill=goldL+(int(255*a),))
    fr=Image.alpha_composite(fr,L)
    cur=max([i for i in range(4) if t>=starts[i+1]] or [-1])
    for i in range(4):
        st=starts[i+1]
        if t<st: continue
        p=back((t-st)/0.45); s=max(0.01,0.85+0.15*p); al=min(1,(t-st)/0.25)
        im=act[i] if i==cur else ina[i]
        r=im.resize((int(im.width*s),int(im.height*s)))
        if al<1: r.putalpha(r.split()[3].point(lambda px:int(px*al)))
        cx=pos[i][0]+TW/2; cy=pos[i][1]+TH/2
        fr.alpha_composite(r,(int(cx-r.width/2),int(cy-r.height/2)))
    fr.convert('RGB').save(f'fr5/{fn:04d}.png')
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i','fr5/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','/mnt/user-data/outputs/v1-b2-01.mp4'],check=True)
print([round(s,1) for s in starts])
