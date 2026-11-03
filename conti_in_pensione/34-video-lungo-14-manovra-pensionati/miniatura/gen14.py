# Miniature video 14 (manovra 2027 e pensionati): A tabella (copia dei virali), B tre misure, C 500 euro + PER CHI?
# Risposte nascoste ("? €"), niente volti, niente logo Inps, testi misurati dentro i riquadri. Uso: python3 gen14.py
import asyncio,math,json
from playwright.async_api import async_playwright
W,H=1280,720
INK='#06282C';YEL='#FFD43B';RED='#E0402A'
DEFS='''<defs>
<radialGradient id="bg" cx="0.5" cy="0.55" r="0.95"><stop offset="0" stop-color="#2DB8BC"/><stop offset="0.5" stop-color="#0D5158"/><stop offset="1" stop-color="#03181B"/></radialGradient>
<linearGradient id="go" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF6B8"/><stop offset="0.35" stop-color="#FFD43B"/><stop offset="0.7" stop-color="#E5A100"/><stop offset="1" stop-color="#9A6400"/></linearGradient>
<linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22C48A"/><stop offset="1" stop-color="#0A5F44"/></linearGradient>
<linearGradient id="rd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0553D"/><stop offset="1" stop-color="#B02A18"/></linearGradient>
<linearGradient id="bl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3C8FD6"/><stop offset="1" stop-color="#1B4E8C"/></linearGradient>
<linearGradient id="am" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC940"/><stop offset="1" stop-color="#D98A00"/></linearGradient>
<radialGradient id="vig" cx="0.5" cy="0.5" r="0.78"><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.45"/></radialGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#000" flood-opacity="0.55"/></filter>
</defs>'''
def rays(cx,cy,n=22,op=0.11):
    o=f'<g opacity="{op}" fill="#fff">'
    for k in range(n):
        a=k*2*math.pi/n;b=a+math.pi/n*0.9;R=1700
        o+=f'<path d="M{cx} {cy} L{cx+R*math.cos(a):.0f} {cy+R*math.sin(a):.0f} L{cx+R*math.cos(b):.0f} {cy+R*math.sin(b):.0f}Z"/>'
    return o+'</g>'
def HEADP(x,y,w,h,fill,r=22):
    return f'<path d="M{x} {y+h} V{y+r} Q{x} {y} {x+r} {y} H{x+w-r} Q{x+w} {y} {x+w} {y+r} V{y+h} Z" fill="{fill}"/>'
_id=[0]
def T(txt,x,y,fs,fill,sw=0,anchor='middle',maxw=None,rot=0,box=None):
    _id[0]+=1
    st=f' stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" paint-order="stroke"' if sw else ''
    d=(f' data-w="{maxw}"' if maxw else '')+(f' data-box="{box[0]},{box[1]},{box[2]},{box[3]}"' if box else '')
    tr=f' transform="rotate({rot} {x} {y})"' if rot else ''
    return f'<text id="t{_id[0]}" x="{x}" y="{y}" class="t" font-size="{fs}" fill="{fill}" text-anchor="{anchor}"{st}{d}{tr}>{txt}</text>'
def R(x,y,w,h,fill,r=16,stroke='#fff',sw=5,rot=0,shadow=True):
    f=' filter="url(#sh)"' if shadow else ''
    g=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if rot: return f'<g transform="rotate({rot} {x+w/2} {y+h/2})"{f}>{g}</g>'
    return f'<g{f}>{g}</g>'
def coin(cx,cy,r,txt=True):
    o=(f'<g transform="translate({cx} {cy})" filter="url(#sh)"><circle r="{r}" fill="url(#go)" stroke="#fff" stroke-width="{r*0.07}"/>'
       f'<circle r="{r*0.78}" fill="none" stroke="#B87800" stroke-width="{r*0.05}"/>')
    if txt: o+=f'<text y="{r*0.3}" class="t" font-size="{r*0.95}" fill="#B87800" text-anchor="middle">€</text>'
    return o+'</g>'
def arrow(x1,y1,x2,y2,w=16,col=RED):
    a=math.atan2(y2-y1,x2-x1);L=34
    hx=[x2-L*math.cos(a-0.5),y2-L*math.sin(a-0.5)];hy=[x2-L*math.cos(a+0.5),y2-L*math.sin(a+0.5)]
    return (f'<g filter="url(#sh)"><line x1="{x1}" y1="{y1}" x2="{x2-18*math.cos(a)}" y2="{y2-18*math.sin(a)}" stroke="#fff" stroke-width="{w+8}" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2-18*math.cos(a)}" y2="{y2-18*math.sin(a)}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {hx[0]},{hx[1]} {hy[0]},{hy[1]}" fill="{col}" stroke="#fff" stroke-width="6" stroke-linejoin="round"/></g>')
def pill_small(x,y,w,h,txt,fs=26):
    return R(x,y,w,h,'#0B3A40',r=h/2,stroke='#7FF0D2',sw=3,shadow=False)+T(txt,x+w/2,y+h/2+fs*0.36,fs,'#fff',maxw=w-30,box=(x,y,w,h))
def qbox(x,y,w,h,fs=40):
    return R(x,y,w,h,'url(#rd)',r=14,stroke='#fff',sw=4)+T('? €',x+w/2,y+h/2+fs*0.36,fs,'#fff',maxw=w-24,box=(x,y,w,h))
def page(body,bgrays=(640,360)):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#000}}svg{{display:block}}'
            f'.t{{font-family:\'DejaVu Sans\',\'Liberation Sans\',Arial,sans-serif;font-weight:900}}</style></head><body>'
            f'<svg id="s" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}'
            f'<rect width="{W}" height="{H}" fill="url(#bg)"/>{rays(*bgrays)}{body}<rect width="{W}" height="{H}" fill="url(#vig)"/></svg></body></html>')
# ---------------- A: TABELLA (copia dei virali) ----------------
def A():
    o=R(40,30,470,52,'url(#rd)',r=12,stroke='#fff',sw=4)+T('DAI DOCUMENTI UFFICIALI',275,66,28,'#fff',maxw=440,box=(40,30,470,52))
    o+=T('PENSIONI',40,200,128,'#fff',14,'start',maxw=600)
    o+=T('2027',40,322,128,YEL,14,'start',maxw=640)
    o+=R(40,352,520,66,YEL,r=12,stroke=INK,sw=5)+T('300 € OVER 75',300,352+33+16,44,INK,maxw=480,box=(40,352,520,66))
    o+=R(40,430,580,66,YEL,r=12,stroke=INK,sw=5)+T('FONDO 850 MILIONI',330,430+33+16,44,INK,maxw=540,box=(40,430,580,66))
    o+=R(40,508,520,66,YEL,r=12,stroke=INK,sw=5)+T('TAGLIO IRPEF 33%',300,508+33+16,44,INK,maxw=480,box=(40,508,520,66))
    # tabella a destra
    X,Y,Wd=680,34,560
    o+=R(X,Y,Wd,548,'#fff',r=22,stroke='#fff',sw=5)
    o+=HEADP(X,Y,Wd,84,'url(#rd)')
    o+=T('TABELLA IMPORTI',X+Wd/2,Y+58,46,'#fff',maxw=Wd-50,box=(X,Y,Wd,84))
    o+=f'<rect x="{X}" y="{Y+84}" width="{Wd}" height="52" fill="#0D5158"/>'
    o+=T('PENSIONE LORDA',X+150,Y+120,26,'#fff',maxw=250,box=(X,Y+84,300,52))+T('RISPARMIO ALL\'ANNO',X+430,Y+120,26,'#fff',maxw=240,box=(X+300,Y+84,260,52))
    rows=['50.000 €','52.000 €','54.000 €','55.000 €']
    for i,rw in enumerate(rows):
        y=Y+136+i*100
        if i%2==0:o+=f'<rect x="{X}" y="{y}" width="{Wd}" height="100" fill="#E7F6F4"/>'
        o+=T(rw,X+150,y+66,44,INK,maxw=250,box=(X,y,300,100))
        o+=qbox(X+300,y+14,230,72,46)
    # cerchio rosso + freccia sulla riga 55.000
    ry=Y+136+3*100
    o+=f'<ellipse cx="{X+415}" cy="{ry+50}" rx="150" ry="62" fill="none" stroke="{RED}" stroke-width="9"/>'
    # barra in basso
    o+=R(40,614,1200,86,'#0B3A40',r=20,stroke=YEL,sw=6)+T('CHI PRENDE DAVVERO QUALCOSA?',640,614+43+19,56,YEL,maxw=1130,box=(40,614,1200,86))
    return page(o,(300,300))
# ---------------- B: TRE MISURE ----------------
def card(x,y,w,h,col,head,big,sub,q):
    o=R(x,y,w,h,'#fff',r=22,stroke='#fff',sw=5)
    o+=HEADP(x,y,w,76,col)
    o+=T(head,x+w/2,y+55,44,'#fff',3,maxw=w-40,box=(x,y,w,76))
    o+=T(big,x+w/2,y+180,92,INK,maxw=w-36,box=(x,y+80,w,132))
    o+=T(sub,x+w/2,y+228,32,'#0B6A55',maxw=w-36,box=(x,y+192,w,56))
    o+=R(x+16,y+h-90,w-32,70,'url(#rd)',r=14,stroke='#fff',sw=4)+T(q,x+w/2,y+h-90+35+13,34,'#fff',maxw=w-70,box=(x+16,y+h-90,w-32,70))
    return o
def B():
    o=T('PENSIONI',745,138,124,'#fff',14,'end',maxw=630)+T('2027',775,138,124,YEL,14,'start',maxw=420)
    o+=R(330,160,620,60,'url(#rd)',r=14,stroke='#fff',sw=4,rot=-2)+T('LA MANOVRA IN 3 MISURE',640,160+30+14,40,'#fff',maxw=580,rot=-2)
    o+=card(50,236,370,360,'url(#gr)','BUONO','300 €','OVER 75','CHI LO PRENDE?')
    o+=card(455,236,370,360,'url(#bl)','FONDO','850 MLN','PER USCIRE DAL LAVORO','DA CHE ETÀ?')
    o+=card(860,236,370,360,'url(#am)','IRPEF','33%','FINO A 55.000 €','QUANTO RISPARMI?')
    o+=R(40,612,1200,88,YEL,r=20,stroke=INK,sw=6)+T('UNA DELLE TRE VALE FINO A 500 €: QUALE?',640,612+44+18,52,INK,maxw=1140,box=(40,612,1200,88))
    o+=pill_small(990,172,250,40,'DISEGNO DI LEGGE',24)
    return page(o,(640,300))
# ---------------- C: 500 € + PER CHI? ----------------
def C():
    o=T('FINO A',400,68,64,'#fff',9,maxw=300)
    o+=coin(400,330,215,False)
    o+=T('500 €',400,375,118,'#7A4D00',0,maxw=330)
    o+=T('ALL\'ANNO',400,440,40,'#7A4D00',0,maxw=260)
    o+=f'<circle cx="400" cy="330" r="238" fill="none" stroke="{RED}" stroke-width="12" stroke-dasharray="40 18"/>'
    o+=T('PER CHI?',930,230,150,YEL,16,maxw=520)
    o+=R(700,262,460,92,'url(#rd)',r=14,stroke='#fff',sw=6,rot=-6)+T('NON PER TUTTI',930,262+46+20,56,'#fff',maxw=410,rot=-6)
    o+=R(700,400,520,64,'#0B3A40',r=32,stroke='#7FF0D2',sw=4)+T('+ BUONO 300 € OVER 75',960,400+32+15,38,'#fff',maxw=480,box=(700,400,520,64))
    o+=R(700,480,520,64,'#0B3A40',r=32,stroke='#7FF0D2',sw=4)+T('+ FONDO 850 MILIONI',960,480+32+15,38,'#fff',maxw=480,box=(700,480,520,64))
    o+=arrow(700,330,630,330,18)
    o+=R(0,590,1280,130,YEL,r=0,stroke=INK,sw=6,shadow=False)
    o+=T('PENSIONI 2027 ➜ MANOVRA',640,590+65+30,84,INK,maxw=1200,box=(0,590,1280,130))
    o+=pill_small(1000,20,240,42,'DISEGNO DI LEGGE',24)
    return page(o,(400,330))
FIT='''()=>{const bad=[];document.querySelectorAll('text').forEach(t=>{const mw=+t.dataset.w;let fs=+t.getAttribute('font-size');
 let b=t.getBBox();if(mw&&b.width>mw){fs=fs*mw/b.width;t.setAttribute('font-size',fs.toFixed(1));b=t.getBBox();}
 if(t.dataset.box){const [x,y,w,h]=t.dataset.box.split(',').map(Number);if(b.x<x+6||b.x+b.width>x+w-6||b.y<y+2||b.y+b.height>y+h-2)bad.push([t.textContent,Math.round(b.x),Math.round(b.y),Math.round(b.width),Math.round(b.height)]);}
 if(b.x<8||b.x+b.width>1272||b.y<4||b.y+b.height>716)bad.push(['FUORI',t.textContent,Math.round(b.x),Math.round(b.y)]);});
 return bad;}'''
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
        pg=await br.new_page(viewport={'width':W,'height':H})
        for k,f in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{k}.html','w',encoding='utf-8').write(f())
            await pg.goto(f'file://{__import__("os").getcwd()}/miniatura-{k}.html')
            bad=await pg.evaluate(FIT)
            print(k,'PROBLEMI:' if bad else 'testi ok',bad if bad else '')
            await pg.screenshot(path=f'miniatura-{k}.png')
        await br.close()
asyncio.run(main())
