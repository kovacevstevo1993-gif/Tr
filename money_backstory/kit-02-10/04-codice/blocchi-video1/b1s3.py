from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, subprocess
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); green=(84,200,124); grey=(150,165,185)
FPS=30; DUR=9.9; N=int(round(FPS*DUR))
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
bg=Image.new('RGBA',(W,H),navy+(255,))
g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,120)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
gr=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(gr)
for y in range(0,H,60): gd.line([0,y,W,y],fill=(255,255,255,8),width=1)
for x in range(0,W,60): gd.line([x,0,x,H],fill=(255,255,255,8),width=1)
bg=Image.alpha_composite(bg,gr)
fT=ImageFont.truetype(F+'Gloock-Regular.ttf',92); fR=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',60)
fQ=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',70); fS=ImageFont.truetype(F+'InstrumentSans-Regular.ttf',36); fB=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',40)
def txt(L,t,f,y,col,alpha=255,x=None,anchor='c'):
    d=ImageDraw.Draw(L); b=d.textbbox((0,0),t,font=f); w=b[2]-b[0]
    X=(W-w)/2-b[0] if x is None else (x-w/2-b[0] if anchor=='c' else x-b[0])
    d.text((X,y-b[1]),t,font=f,fill=col+(int(alpha),)); return w
rows=[('CLAIM AT 62',red),('CLAIM AT 67',white),('CLAIM AT 70',green)]
for fn in range(N):
    t=fn/FPS*1.2323; fr=bg.copy(); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.6); txt(L,'THE EXACT MATH',fT,110+int((1-a)*-30),goldL,255*a)
    a=ease((t-0.4)/0.6); d.line([W/2-260,235,W/2+260,235],fill=gold+(int(255*a),),width=4)
    for i,(lab,col) in enumerate(rows):
        p=ease((t-1.0-i*0.6)/0.5)
        if p<=0: continue
        y=320+i*150; x0=W/2-560+int((1-p)*-60)
        d.rounded_rectangle([x0,y,x0+1120,y+118],radius=24,fill=(22,40,64,int(235*p)),outline=col+(int(255*p),),width=4)
        txt(L,lab,fR,y+28,col,255*p,x=x0+50,anchor='l')
        # animated monthly->years counter
        q=ease((t-1.5-i*0.6)/1.6)
        yrs=int(q*[28,23,20][i])
        txt(L,f'× 12 × {yrs} years = ?',fQ,y+24,white,255*p,x=x0+1070-560+120,anchor='l') if False else None
        s=f'× 12 months × {yrs} years (to age 90)'
        dd=ImageDraw.Draw(L); b=dd.textbbox((0,0),s,font=fB); dd.text((x0+1070-(b[2]-b[0])-b[0],y+40-b[1]),s,font=fB,fill=grey+(int(255*p),))
    a=ease((t-4.6)/0.6)
    if a>0:
        pill='REAL NUMBERS  ·  SOURCE: SSA.GOV'; b=d.textbbox((0,0),pill,font=fS); pw=b[2]-b[0]+70
        d.rounded_rectangle([(W-pw)/2,790,(W+pw)/2,850],radius=30,fill=(38,48,52,int(255*a)),outline=gold+(int(255*a),),width=3)
        txt(L,pill,fS,802,gold,255*a)
    fr=Image.alpha_composite(fr,L)
    a=back((t-8.0)/0.5)
    if t>8.0:
        B=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(B)
        s='WHICH AGE IS RIGHT FOR YOU?'; b=bd.textbbox((0,0),s,font=fQ); bw=b[2]-b[0]+90; bh=110; bx=(W-bw)/2; by=905
        bd.rounded_rectangle([bx,by,bx+bw,by+bh],radius=55,fill=gold+(255,))
        bd.text((bx+45-b[0],by+bh/2-(b[3]-b[1])/2-b[1]),s,font=fQ,fill=navy+(255,))
        box=(int(bx-5),int(by-5),int(bx+bw+5),int(by+bh+5)); piece=B.crop(box); sc=max(0.01,a)
        piece=piece.resize((max(1,int(piece.width*sc)),max(1,int(piece.height*sc))))
        fr.alpha_composite(piece,(int((box[0]+box[2])/2-piece.width/2),int((box[1]+box[3])/2-piece.height/2)))
    fr.convert('RGB').save(f'fr3/{fn:04d}.png')
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i','fr3/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','/mnt/user-data/outputs/v1-b1-03.mp4'],check=True)
