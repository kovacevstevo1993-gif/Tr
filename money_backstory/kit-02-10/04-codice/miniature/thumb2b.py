from common import *
W2,H2=1280,720
navy2=(10,24,40)
im=Image.new('RGBA',(W2,H2),navy2+(255,))
g=Image.new('RGBA',(W2,H2),(0,0,0,0)); ImageDraw.Draw(g).ellipse([100,-120,1180,700],fill=(34,66,104,255))
im=Image.alpha_composite(im,g.filter(ImageFilter.GaussianBlur(160)))
# grid
gr=Image.new('RGBA',(W2,H2),(0,0,0,0)); gd=ImageDraw.Draw(gr)
for y in range(0,H2,44): gd.line([0,y,W2,y],fill=(255,255,255,9),width=1)
for x in range(0,W2,44): gd.line([x,0,x,H2],fill=(255,255,255,9),width=1)
im=Image.alpha_composite(im,gr)
# gold 3D frame
M=22
glow=Image.new('RGBA',(W2,H2),(0,0,0,0)); ImageDraw.Draw(glow).rounded_rectangle([M-4,M-4,W2-M+4,H2-M+4],radius=26,outline=(230,185,90,210),width=18)
im=Image.alpha_composite(im,glow.filter(ImageFilter.GaussianBlur(16)))
grad=Image.new('RGBA',(W2,H2)); g2=ImageDraw.Draw(grad)
for y in range(H2):
    t=y/H2; g2.line([0,y,W2,y],fill=(int(255-95*t),int(226-100*t),int(150-95*t),255))
ring=Image.new('L',(W2,H2),0); rd=ImageDraw.Draw(ring)
rd.rounded_rectangle([M,M,W2-M,H2-M],radius=24,fill=255); rd.rounded_rectangle([M+11,M+11,W2-M-11,H2-M-11],radius=16,fill=0)
bev=Image.new('RGBA',(W2,H2),(0,0,0,0)); bev.paste(grad,(0,0),ring); im=Image.alpha_composite(im,bev)
d=ImageDraw.Draw(im)
d.rounded_rectangle([M+2,M+2,W2-M-2,H2-M-2],radius=23,outline=(255,245,200,150),width=2)
d.rounded_rectangle([M+11,M+11,W2-M-11,H2-M-11],radius=16,outline=(90,60,15,255),width=3)
def T(s,f,x,y,col,anchor='c',stroke=0):
    b=d.textbbox((0,0),s,font=f,stroke_width=stroke); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=(0,0,0))
gold_=(212,172,82); goldL_=(246,214,140); white_=(236,240,245); red_=(232,84,84)
T('RETIREMENT MISTAKES',BOLD(42),W2/2,62,goldL_)
T('5',BOLD(190),225,120,white_,'c',stroke=6)
T('THAT QUIETLY RUIN',BOLD(50),390,155,white_,'l')
T('YOUR RETIREMENT',BOLD(50),390,218,goldL_,'l')
# descending savings chart
X0,X1,Y0,Y1=150,1130,530,370
d.line([X0,Y0,X1,Y0],fill=gold_+(255,),width=3)
pts=[]
for k in range(101):
    x=X0+(X1-X0)*k/100; y=Y1+(Y0-Y1-18)*(k/100)**1.6; pts.append((x,y))
poly=pts+[(pts[-1][0],Y0),(X0,Y0)]
A=Image.new('RGBA',(W2,H2),(0,0,0,0)); ImageDraw.Draw(A).polygon(poly,fill=red_+(60,)); im=Image.alpha_composite(im,A); d=ImageDraw.Draw(im)
d.line(pts,fill=red_+(255,),width=8)
for m in range(5):
    k=12+m*20; x,y=pts[k]; d.ellipse([x-16,y-16,x+16,y+16],fill=red_+(255,),outline=(255,255,255,255),width=3)
    b=d.textbbox((0,0),f'#{m+1}',font=BOLD(26)); d.text((x-(b[2]-b[0])/2,y-52),f'#{m+1}',font=BOLD(26),fill=white_)
T('YOUR SAVINGS',BOLD(26),X1,Y1-40,(170,185,205),'r')
# bottom pill
f=BOLD(50); lab='#3 SURPRISES ALMOST EVERYONE'
b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+70; bx=(W2-bw)/2; by=600
d.rounded_rectangle([bx,by,bx+bw,by+78],radius=39,fill=red_)
d.text((bx+35-b[0],by+39-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255))
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video2-stile-slide.png')
