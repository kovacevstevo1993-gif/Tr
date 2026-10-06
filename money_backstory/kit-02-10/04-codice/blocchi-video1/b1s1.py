from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, subprocess
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); grey=(150,165,185)
FPS=30; DUR=6.4; N=int(FPS*DUR)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
bg=Image.new('RGBA',(W,H),navy+(255,))
g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,120)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
fP=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',34); fT=ImageFont.truetype(F+'Gloock-Regular.ttf',66)
fN=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',250); fS=ImageFont.truetype(F+'InstrumentSans-Regular.ttf',44)
def txt(L,t,f,y,col,alpha=255,x=None):
    d=ImageDraw.Draw(L); b=d.textbbox((0,0),t,font=f); w=b[2]-b[0]
    d.text(((W-w)/2-b[0] if x is None else x-w/2-b[0], y-b[1]),t,font=f,fill=col+(int(alpha),)); return b[3]-b[1]
for fn in range(N):
    t=fn/FPS*1.3281; fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.5); oy=int((1-a)*-25)
    pill='SOCIAL SECURITY'; b=d.textbbox((0,0),pill,font=fP); pw=b[2]-b[0]+60
    d.rounded_rectangle([(W-pw)/2,150+oy,(W+pw)/2,202+oy],radius=26,fill=(38,48,52,int(255*a)),outline=gold+(int(255*a),),width=3)
    txt(L,pill,fP,160+oy,gold,255*a)
    a2=ease((t-0.3)/0.6); txt(L,'CLAIMING AT THE WRONG AGE CAN COST YOU',fT,262+int((1-a2)*25),goldL,255*a2)
    fr=Image.alpha_composite(fr,L)
    # number count 1.0 -> 3.2
    p=ease((t-1.0)/2.2)
    if t>1.0:
        val=int(100000*p/1000)*1000
        s=f'${val:,}' + ('+' if p>=0.999 else '')
        # glow
        G=Image.new('RGBA',(W,H),(0,0,0,0)); txt(G,s,fN,430,red,200)
        fr=Image.alpha_composite(fr,G.filter(ImageFilter.GaussianBlur(30)))
        sc=1.0
        if t>3.2: sc=1+0.08*math.sin(min(1,(t-3.2)/0.35)*math.pi)
        N2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(N2,s,fN,430,red,255)
        if sc!=1.0:
            N2=N2.resize((int(W*sc),int(H*sc))); ox=(N2.width-W)//2; oy2=(N2.height-H)//2; N2=N2.crop((ox,oy2,ox+W,oy2+H))
        fr=Image.alpha_composite(fr,N2)
    a3=ease((t-3.6)/0.6)
    if a3>0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        d.line([W/2-360,760,W/2+360,760],fill=gold+(int(255*a3),),width=4)
        txt(L,'in lifetime benefits',fS,800,white,255*a3)
        fr=Image.alpha_composite(fr,L)
    fr.convert('RGB').save(f'fr1/{fn:04d}.png')
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i','fr1/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','/mnt/user-data/outputs/v1-b1-01.mp4'],check=True)
