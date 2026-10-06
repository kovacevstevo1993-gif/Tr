from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, subprocess
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); green=(84,200,124); grey=(150,165,185)
FPS=30; DUR=8.7; N=int(FPS*DUR)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
bg=Image.new('RGBA',(W,H),navy+(255,))
g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,120)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
fA=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',150); fL=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',46)
fQ=ImageFont.truetype(F+'InstrumentSans-Regular.ttf',44); fT=ImageFont.truetype(F+'Gloock-Regular.ttf',84)
def card(age,label,quote,col):
    cw,ch=640,520; im=Image.new('RGBA',(cw+80,ch+80),(0,0,0,0))
    sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([50,55,cw+50,ch+55],radius=34,fill=(0,0,0,170))
    im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(18)))
    d=ImageDraw.Draw(im); d.rounded_rectangle([40,40,cw+40,ch+40],radius=34,fill=(22,40,64,255),outline=col+(255,),width=5)
    def c(t,f,y,cl):
        b=d.textbbox((0,0),t,font=f); d.text((40+cw/2-(b[2]-b[0])/2-b[0],y-b[1]),t,font=f,fill=cl+(255,))
    c(label,fL,110,white); c(age,fA,190,col); c(quote,fQ,420,grey)
    return im
c62=card('62','CLAIM AT','"It\'s a mistake"',red)
c70=card('70','WAIT UNTIL','"Always the smart move"',green)
def place(fr,im,cx,cy,s,a):
    if s<=0.01 or a<=0: return fr
    w,h=im.size; r=im.resize((max(1,int(w*s)),max(1,int(h*s))))
    if a<1:
        al=r.split()[3].point(lambda p:int(p*a)); r.putalpha(al)
    fr.alpha_composite(r,(int(cx-r.width/2),int(cy-r.height/2))); return fr
def txt(L,t,f,y,col,alpha=255):
    d=ImageDraw.Draw(L); b=d.textbbox((0,0),t,font=f); d.text(((W-(b[2]-b[0]))/2-b[0],y-b[1]),t,font=f,fill=col+(int(alpha),))
for fn in range(N):
    t=fn/FPS*1.2644; fr=bg.copy()
    fr=place(fr,c62,W/2-420,470,back((t-0.1)/0.5),min(1,t/0.3))
    fr=place(fr,c70,W/2+420,470,back((t-3.9)/0.5),min(1,max(0,(t-3.9)/0.3)))
    # X marks
    for i,cx in enumerate([W/2-420,W/2+420]):
        p=ease((t-8.3-i*0.25)/0.35)
        if p>0:
            L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); s=230*p
            d.line([cx-s,470-s,cx+s,470+s],fill=red+(235,),width=26); d.line([cx-s,470+s,cx+s,470-s],fill=red+(235,),width=26)
            fr=Image.alpha_composite(fr,L)
    a=ease((t-8.9)/0.5)
    if a>0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'BOTH CAN BE WRONG.',fT,880+int((1-a)*30),goldL,255*a); fr=Image.alpha_composite(fr,L)
    fr.convert('RGB').save(f'fr2/{fn:04d}.png')
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i','fr2/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','/mnt/user-data/outputs/v1-b1-02.mp4'],check=True)
