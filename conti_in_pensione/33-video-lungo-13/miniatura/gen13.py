# Miniature video 13 (reversibilita'): A torta tagliata, B mappa famiglia. Risposte nascoste. Uso: python3 gen13.py
import asyncio,os,re,sys,math
from playwright.async_api import async_playwright
src=open('../../14-video-lungo-4-invalidita-2027/miniatura/vecchie-45cent/gen.py').read()
HEAD0=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
g9=open('../../25-video-lungo-9/miniatura/gen9.py').read()
exec(g9[g9.index("S='stroke"):g9.index("# A: LA BUSTA")])
BASE=HEAD0[:HEAD0.index('<g opacity="0.10"')]
EXTRA='''<defs>
<radialGradient id="bgA" cx="0.5" cy="0.58" r="0.95"><stop offset="0" stop-color="#2DB8BC"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="lcard" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22C48A"/><stop offset="1" stop-color="#0A5F44"/></linearGradient>
<linearGradient id="go" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF6B8"/><stop offset="0.35" stop-color="#FFD43B"/><stop offset="0.7" stop-color="#E5A100"/><stop offset="1" stop-color="#9A6400"/></linearGradient>
<linearGradient id="goS" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#A36B00"/><stop offset="0.45" stop-color="#FFD43B"/><stop offset="1" stop-color="#8A5A00"/></linearGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.5"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="vig" cx="0.5" cy="0.5" r="0.78"><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.45"/></radialGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFF3A8" stop-opacity="0.55"/><stop offset="1" stop-color="#FFF3A8" stop-opacity="0"/></radialGradient>
</defs>'''
def rays(cx,cy,n=20,op=0.11):
    o=f'<g opacity="{op}" fill="#fff">'
    for k in range(n):
        a=k*2*math.pi/n;b=a+math.pi/n*0.9;R=1700
        o+=f'<path d="M{cx} {cy} L{cx+R*math.cos(a):.0f} {cy+R*math.sin(a):.0f} L{cx+R*math.cos(b):.0f} {cy+R*math.sin(b):.0f}Z"/>'
    return o+'</g>'
def stack(cx,by,r,n):
    o='';h=r*0.30
    for i in range(n):
        y=by-i*h
        o+=(f'<ellipse cx="{cx}" cy="{y+h}" rx="{r}" ry="{r*0.36}" fill="#7A4D00"/><rect x="{cx-r}" y="{y}" width="{2*r}" height="{h}" fill="url(#goS)"/>'
            f'<ellipse cx="{cx}" cy="{y}" rx="{r}" ry="{r*0.36}" fill="url(#go)" stroke="#B87800" stroke-width="2"/>')
    return f'<g filter="url(#sh)">{o}</g>'
def coin(cx,cy,r,rot=0):
    return (f'<g transform="translate({cx} {cy}) rotate({rot})" filter="url(#sh)"><circle r="{r}" fill="url(#go)" stroke="#fff" stroke-width="{r*0.08}"/>'
            f'<circle r="{r*0.72}" fill="none" stroke="#B87800" stroke-width="{r*0.07}"/>'
            f'<text y="{r*0.3}" class="t" font-size="{r*0.95}" fill="#B87800" text-anchor="middle">€</text></g>')
def T(i,x,y,txt,fs,fill,sw=0,anchor='middle',maxw=None,extra=''):
    st=f'{S} stroke-width="{sw}"' if sw else ''
    mw=f' data-w="{maxw}"' if maxw else ''
    return f'<text id="{i}" x="{x}" y="{y}" class="t" font-size="{fs}" fill="{fill}" text-anchor="{anchor}" {st}{mw} {extra}>{txt}</text>'
def banner(x,y,w,h,rot,fill):
    return f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="#fff" stroke-width="6"/></g></g>'


EXTRA+="""<defs><linearGradient id="blade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#AEBCC1"/></linearGradient></defs>"""
def pt(cx,cy,r,a):
    return cx+r*math.sin(math.radians(a)),cy-r*math.cos(math.radians(a))
def slice_(cx,cy,r,a0,a1):
    x0,y0=pt(cx,cy,r,a0);x1,y1=pt(cx,cy,r,a1);big=1 if (a1-a0)%360>180 else 0
    return f'M{cx:.1f} {cy:.1f} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z'
def scissors(cx,cy,s,rot):
    o=f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})"><g filter="url(#sh)">'
    for k in (1,-1):
        pl=f'M192 {-30*k} L0 0 L-62 {18*k} L-112 {60*k}'
        o+=f'<path d="{pl}" fill="none" stroke="#06282C" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>'
        o+=f'<path d="{pl}" fill="none" stroke="url(#blade)" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>'
        o+=f'<circle cx="-122" cy="{70*k}" r="32" fill="none" stroke="#06282C" stroke-width="22"/><circle cx="-122" cy="{70*k}" r="32" fill="none" stroke="#E0402A" stroke-width="12"/>'
    o+='<circle r="13" fill="url(#go)" stroke="#06282C" stroke-width="4"/></g></g>'
    return o
def sticker(x,y,w,h,rot,fill='#E0402A'):
    return banner(x,y,w,h,rot,fill)
def pill(x,y,w,h):
    return f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2 if h<90 else 28}" fill="#06282C" fill-opacity="0.92" stroke="#FFD43B" stroke-width="6"/></g>'
def wcard(cx,cy,w,h,label,big,i):
    h=h+14
    s=f'<g filter="url(#sh)"><rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="18" fill="url(#pp)" stroke="#fff" stroke-width="6"/></g>'
    s+=T(i+'a',cx,cy-h/2+30,label,24,'#0D5158',maxw=w-24)+T(i+'b',cx,cy+h/2-14,big,56,'#E0402A',6,maxw=w-30)
    return s
# ============ A: LA TORTA TAGLIATA
PX,PY,R=985,350,205
A=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#bgA)"/>'+rays(985,350,22,0.11)+f'<circle cx="{PX}" cy="{PY}" r="430" fill="url(#glow)"/>'
A+=T('a1',40,142,'PENSIONE',124,'#fff',16,'start',maxw=650)+T('a2',40,230,'REVERSIBILITÀ',84,'#FFD43B',12,'start',maxw=660)
A+=pill(740,22,510,92)+T('a3',995,56,'SE IL CONIUGE PRENDEVA',26,'#FFD43B',maxw=470)+T('a4',995,100,'2.000 € LORDI AL MESE',40,'#fff',maxw=470)
mid=200;dx=46*math.sin(math.radians(mid));dy=-46*math.cos(math.radians(mid))
A+=f'<g filter="url(#sh)"><path d="{slice_(PX,PY,R,250,510-100+0)}" fill="none"/></g>'
A+=f'<g filter="url(#sh)"><path d="{slice_(PX,PY,R,250,150+360)}" fill="url(#lcard)" stroke="#fff" stroke-width="8" stroke-linejoin="round"/></g>'
A+=f'<path d="{slice_(PX,PY,R,150,250)}" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="14 12" opacity="0.7"/>'
A+=f'<g transform="translate({dx:.1f} {dy:.1f})"><g filter="url(#sh)"><path d="{slice_(PX,PY,R,150,250)}" fill="url(#re)" stroke="#fff" stroke-width="8" stroke-linejoin="round"/></g></g>'
A+=T('a5',PX,PY-118,'TI RESTANO',34,'#fff',7,maxw=250)+T('a6',PX,PY-8,'? €',124,'#fff',14,maxw=250)
wx=PX+126*math.sin(math.radians(mid))+dx;wy=PY-126*math.cos(math.radians(mid))+dy
A+=T('a7',wx,wy+14,'− ? €',50,'#fff',8,maxw=150)
A+=pill(36,268,600,172)+T('a8',336,340,'QUANTO TI RESTA',62,'#fff',maxw=560)+T('a9',336,418,'DAVVERO?',84,'#FFD43B',10,maxw=520)
A+='<g transform="rotate(-3 330 560)">'+banner(30,500,600,126,0,'#E0402A')+T('a10',330,552,'ATTENZIONE',58,'#FFD43B',maxw=540)+T('a11',330,604,"AL TAGLIO DELL'INPS",44,'#fff',maxw=540)+'</g>'
A+=scissors(752,432,0.72,-14)
A+=stack(110,690,46,3)+stack(220,700,46,2)+coin(320,672,30,10)
A+='<rect width="1280" height="720" fill="url(#vig)"/>'+END
# ============ B: LA MAPPA DELLA FAMIGLIA
B=BASE+EXTRA+'<rect width="1280" height="720" fill="url(#bgA)"/>'+rays(640,430,18,0.11)+'<circle cx="640" cy="430" r="470" fill="url(#glow)"/>'
B+=T('b1',640,134,'PENSIONE',124,'#fff',16,maxw=700)+T('b2',640,222,'DI REVERSIBILITÀ',80,'#FFD43B',12,maxw=860)
HX,HY=640,430
for (ax,ay) in ((262,380),(1076,340),(1076,520)):
    B+=f'<line x1="{HX}" y1="{HY}" x2="{ax}" y2="{ay}" stroke="#fff" stroke-width="9" stroke-dasharray="8 16" stroke-linecap="round" opacity="0.85"/>'
B+=f'<circle cx="{HX}" cy="{HY}" r="150" fill="url(#glow)"/>'+coin(HX,HY,112,0)
B+=pill(480,548,320,52)+T('b3',640,586,'LA PENSIONE DA DIVIDERE',26,'#FFD43B',maxw=290)
B+=person(170,380,92,'L','#E0402A')+wcard(170,540,260,112,'CONIUGE','? %','b4')
B+=person(1000,340,66,'A','#22C48A')+wcard(1160,340,200,100,'FIGLI','? %','b5')
B+=person(1000,520,66,'F','#FFD43B')+wcard(1160,520,200,100,'GENITORI','? %','b6')
B+=scissors(405,412,0.62,8)
B+='<g transform="rotate(-4 405 318)">'+banner(325,286,160,66,0,'#E0402A')+T('b7',405,334,'− ? %',44,'#fff',8,maxw=130)+'</g>'
B+=pill(110,628,1060,76)+T('b8',640,680,"QUANTO SPETTA? QUANDO L'INPS <tspan fill=\"#fff\">TAGLIA</tspan>?",46,'#FFD43B',maxw=1000)
B+='<rect width="1280" height="720" fill="url(#vig)"/>'+END
JS="""()=>{for(const t of document.querySelectorAll('text[data-w]')){const mw=parseFloat(t.getAttribute('data-w'));const fs=parseFloat(t.getAttribute('font-size'));const w=t.getBBox().width;if(w>mw)t.setAttribute('font-size',fs*mw/w);}
const o=[];for(const t of document.querySelectorAll('text')){const r=t.getBoundingClientRect();if(r.width<2)continue;o.push([t.id||'-',t.textContent.slice(0,24),Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom),+t.getAttribute('font-size')]);}return o;}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html')
            boxes=await pg.evaluate(JS)
            for r in boxes:
                flag='' if r[2]>=8 and r[4]<=1272 and r[3]>=0 and r[5]<=716 else '  <<< FUORI'
                print(n,r,flag)
            ids=[r for r in boxes if r[0]!='-']
            for i in range(len(ids)):
                for j in range(i+1,len(ids)):
                    a,c=ids[i],ids[j]
                    ox=min(a[4],c[4])-max(a[2],c[2]);oy=min(a[5],c[5])-max(a[3],c[3])
                    if ox>2 and oy>2: print(n,'SOVRAPPOSTI',a[0],a[1],'<->',c[0],c[1],ox,oy)
            await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
