from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, subprocess
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); green=(84,200,124); grey=(150,165,185)
FPS=30; DUR=6.74; N=int(FPS*DUR)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
# background
bg=Image.new('RGBA',(W,H),navy+(255,))
g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,110)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
gr=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(gr)
for y in range(320,880,90): gd.line([140,y,W-140,y],fill=(255,255,255,11),width=2)
bg=Image.alpha_composite(bg,gr)
fT=ImageFont.truetype(F+'Gloock-Regular.ttf',74); fB=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',42)
fN=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',104); fS=ImageFont.truetype(F+'InstrumentSans-Regular.ttf',34)
fX=ImageFont.truetype(F+'InstrumentSans-Regular.ttf',25); fP=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',32)
fC=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',32)
base=880; bw=280; gap=540
cols=[('CLAIM AT 62',1400,red,'−30% for life'),('CLAIM AT 67',2000,white,'full benefit'),('CLAIM AT 70',2480,green,'+24% for life')]
def bx(i): return W/2+(i-1)*gap
def txt(layer,t,f,y,col,x=None,alpha=255):
    d=ImageDraw.Draw(layer); b=d.textbbox((0,0),t,font=f); w=b[2]-b[0]
    d.text(((W-w)/2-b[0] if x is None else x-w/2-b[0], y-b[1]),t,font=f,fill=col+(int(alpha),))
# pre-render full bars
barimg=[]
for i,(lab,val,col,sub) in enumerate(cols):
    h=int(val/2480*430); im=Image.new('RGBA',(bw,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    for y in range(h):
        t=y/h; cc=tuple(int(col[k]*(1-0.38*t)) for k in range(3)); d.line([0,y,bw,y],fill=cc+(255,))
    m=Image.new('L',(bw,h),0); ImageDraw.Draw(m).rounded_rectangle([0,0,bw-1,h-1],radius=20,fill=255); im.putalpha(m)
    barimg.append(im)
shadow=[]
for i,im in enumerate(barimg):
    s=Image.new('RGBA',(W,H),(0,0,0,0)); shadow.append(None)
h62=1400/2480*430; h70=430; y1=base-h62; y2=base-h70; gx=(bx(1)+bx(2))/2
for fnum in range(N):
    t=fnum/FPS*(8.0/6.74); fr=bg.copy()
    # header
    a=ease((t-0.0)/0.6); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    pill='SOCIAL SECURITY'; b=d.textbbox((0,0),pill,font=fP); pw=b[2]-b[0]+60; oy=int((1-a)*-30)
    d.rounded_rectangle([(W-pw)/2,46+oy,(W+pw)/2,96+oy],radius=25,fill=(38,48,52,int(255*a)),outline=gold+(int(255*a),),width=3)
    txt(L,pill,fP,55+oy,gold,alpha=255*a)
    a2=ease((t-0.25)/0.6); txt(L,'SAME WORKER. DIFFERENT CHECK.',fT,122+int((1-a2)*25),goldL,alpha=255*a2)
    fr=Image.alpha_composite(fr,L)
    # bars
    L=Image.new('RGBA',(W,H),(0,0,0,0))
    for i,(lab,val,col,sub) in enumerate(cols):
        p=ease((t-0.8-i*0.3)/1.3)
        if p<=0: continue
        full=barimg[i]; h=full.height; ch=max(2,int(h*p))
        crop=full.crop((0,h-ch,bw,h)) if False else full.resize((bw,ch))
        cx=bx(i)
        if i==2 and t>4.2:
            pul=0.5+0.5*math.sin((t-4.2)*2.5)
            gl=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(gl).rounded_rectangle([cx-bw/2-10,base-ch-10,cx+bw/2+10,base],radius=26,fill=green+(int(70+70*pul),))
            fr=Image.alpha_composite(fr,gl.filter(ImageFilter.GaussianBlur(28)))
        if ch>30:
            sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([cx-bw/2+14,base-ch+18,cx+bw/2+14,base],radius=20,fill=(0,0,0,150))
            fr=Image.alpha_composite(fr,sh.filter(ImageFilter.GaussianBlur(14)))
        L.paste(full.resize((bw,ch)),(int(cx-bw/2),int(base-ch)),full.resize((bw,ch)))
        num=int(round(val*p/10)*10)
        txt(L,f'${num:,}',fN,base-ch-160,col,cx,alpha=255*min(1,p*3))
        txt(L,'per month',fS,base-ch-50,grey,cx,alpha=255*min(1,p*3))
        la=ease((t-1.6-i*0.3)/0.5)
        txt(L,lab,fB,base+26,white,cx,alpha=255*la); txt(L,sub,fS,base+82,col,cx,alpha=255*la)
    d=ImageDraw.Draw(L); d.line([140,base,W-140,base],fill=gold+(255,),width=4)
    # dashed lines draw
    def dash(xa,xb,y,col,pp):
        end=xa+(xb-xa)*pp
        for x in range(int(xa),int(end),28): d.line([x,y,min(x+14,end),y],fill=col+(255,),width=3)
    pd=ease((t-3.3)/0.7)
    if pd>0:
        dash(bx(0)+bw/2+12,bx(1)-bw/2-12,y1,red,pd); dash(bx(1)+bw/2+12,gx+10,y1,red,pd)
    pd2=ease((t-3.6)/0.5)
    if pd2>0: dash(gx-10,bx(2)-bw/2-12,y2,green,pd2)
    pa=ease((t-3.9)/0.5)
    if pa>0:
        ytop=y1-(y1-(y2+20))*pa; d.line([gx,y1,gx,ytop],fill=goldL+(255,),width=5)
        if pa>0.95: d.polygon([(gx-15,y2+28),(gx+15,y2+28),(gx,y2+2)],fill=goldL+(255,))
    fr=Image.alpha_composite(fr,L)
    pb=back((t-4.3)/0.45)
    if t>4.3:
        B=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(B)
        badge='+$1,080/mo'; bb=bd.textbbox((0,0),badge,font=fC); bwid=bb[2]-bb[0]+40; bh=58; by0=(y1+y2)/2-bh/2+20
        bd.rounded_rectangle([gx-bwid/2,by0,gx+bwid/2,by0+bh],radius=29,fill=gold+(255,))
        bd.text((gx-(bb[2]-bb[0])/2-bb[0],by0+bh/2-(bb[3]-bb[1])/2-bb[1]),badge,font=fC,fill=navy+(255,))
        s=max(0.01,pb); box=(int(gx-bwid/2-10),int(by0-10),int(gx+bwid/2+10),int(by0+bh+10))
        piece=B.crop(box); pw_,ph_=piece.size; nw,nh=max(1,int(pw_*s)),max(1,int(ph_*s))
        piece=piece.resize((nw,nh)); cxp,cyp=(box[0]+box[2])/2,(box[1]+box[3])/2
        fr.alpha_composite(piece,(int(cxp-nw/2),int(cyp-nh/2)))
    fa=ease((t-2.4)/0.6); F2=Image.new('RGBA',(W,H),(0,0,0,0))
    txt(F2,'Example: $2,000 benefit at full retirement age (67). Source: SSA.gov',fX,H-46,grey,alpha=255*fa)
    fr=Image.alpha_composite(fr,F2)
    fr.convert('RGB').save(f'frames/{fnum:04d}.png')
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i','frames/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','/mnt/user-data/outputs/v1-b3-04.mp4'],check=True)
