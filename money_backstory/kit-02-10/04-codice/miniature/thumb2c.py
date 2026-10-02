from common import *
W2,H2=1280,720
im=Image.new('RGBA',(W2,H2),(0,0,0,255))
# dark dramatic bg
L=Image.new('RGBA',(W2,H2)); ld=ImageDraw.Draw(L)
for y in range(H2):
    t=y/H2; ld.line([0,y,W2,y],fill=(int(60-30*t),int(10+6*t),int(16+6*t),255))
im=L
G=Image.new('RGBA',(W2,H2),(0,0,0,0)); gd=ImageDraw.Draw(G); gd.ellipse([380,60,1180,720],fill=(255,60,60,120))
im=Image.alpha_composite(im,G.filter(ImageFilter.GaussianBlur(120)))
d=ImageDraw.Draw(im)
def T(s,f,x,y,col,anchor='l',stroke=9,sc=(0,0,0)):
    b=d.textbbox((0,0),s,font=f,stroke_width=stroke); w=b[2]-b[0]
    X=x-b[0] if anchor=='l' else (x-w/2-b[0] if anchor=='c' else x-w-b[0])
    d.text((X,y-b[1]),s,font=f,fill=col,stroke_width=stroke,stroke_fill=sc)
# falling money chart (right)
X0,X1,Y0,Y1=560,1230,640,120
pts=[]
for k in range(101):
    x=X0+(X1-X0)*k/100; y=Y1+(Y0-Y1)*(k/100)**1.5; pts.append((x,y))
A=Image.new('RGBA',(W2,H2),(0,0,0,0)); ImageDraw.Draw(A).polygon(pts+[(pts[-1][0],Y0),(X0,Y0)],fill=(255,60,60,70)); im=Image.alpha_composite(im,A); d=ImageDraw.Draw(im)
d.line(pts,fill=(255,70,70),width=16,joint='curve')
# big down arrow at end
ex,ey=pts[-1]
d.polygon([(ex-70,ey-60),(ex+70,ey-60),(ex,ey+60)],fill=(255,70,70),outline=(0,0,0))
d.line([(ex-70,ey-60),(ex+70,ey-60),(ex,ey+60),(ex-70,ey-60)],fill=(0,0,0),width=6)
# left: big number
T('5',BOLD(340),60,60,(255,255,255),'l',stroke=14)
T('MISTAKES',BOLD(86),60,420,(255,214,70),'l',stroke=10)
T('THAT DRAIN YOUR',BOLD(50),60,530,(255,255,255),'l',stroke=7)
T('RETIREMENT',BOLD(64),60,595,(255,255,255),'l',stroke=8)
# shock badge top-right
f=BOLD(60); lab='#3 SHOCKS'
b=d.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+70; bx=W2-bw-40; by=40
d.rounded_rectangle([bx+8,by+10,bx+bw+8,by+104],radius=22,fill=(0,0,0,170))
d.rounded_rectangle([bx,by,bx+bw,by+94],radius=22,fill=(255,214,70),outline=(0,0,0),width=7)
d.text((bx+35-b[0],by+47-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(15,15,15))
f2=BOLD(54); lab2='EVERYONE'
b2=d.textbbox((0,0),lab2,font=f2); bw2=b2[2]-b2[0]+70; bx2=W2-bw2-40; by2=146
d.rounded_rectangle([bx2,by2,bx2+bw2,by2+86],radius=22,fill=(255,214,70),outline=(0,0,0),width=7)
d.text((bx2+35-b2[0],by2+43-(b2[3]-b2[1])/2-b2[1]),lab2,font=f2,fill=(15,15,15))
im.convert('RGB').save('/mnt/user-data/outputs/miniatura-video2-clickbait.png')
