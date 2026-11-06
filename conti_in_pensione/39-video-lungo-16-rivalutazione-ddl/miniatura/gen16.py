# Miniature video 16 (rivalutazione 2027, art. 55): A scala a 6 gradini, B quadrante, C cartello limite. Uso: python3 gen16.py
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
# ---------------- A: LA SCALA A 6 GRADINI ----------------
def step(i,x,top,w=125,base=598):
    h=base-top
    o=f'<polygon points="{x},{top} {x+w},{top} {x+w+30},{top-20} {x+30},{top-20}" fill="#6CF0C2" stroke="#fff" stroke-width="4" stroke-linejoin="round"/>'
    if i==5:
        o+=f'<polygon points="{x+w},{top} {x+w+30},{top-20} {x+w+30},{base-20} {x+w},{base}" fill="#0A5F44" stroke="#fff" stroke-width="4" stroke-linejoin="round"/>'
    o+=f'<g filter="url(#sh)"><rect x="{x}" y="{top}" width="{w}" height="{h}" fill="url(#gr)" stroke="#fff" stroke-width="4"/></g>'
    o+=T('? %',x+w/2,top+h/2+17,46,'#fff',6,maxw=w-26,box=(x,top,w,h))
    # bandierina numerata sopra il gradino
    cx,cy=x+w/2+15,top-58
    o+=f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="29" fill="url(#go)" stroke="#fff" stroke-width="5"/></g>'
    o+=T(str(i+1),cx,cy+15,40,INK,maxw=34)
    return o
def A():
    o=T('PENSIONI 2027',40,104,104,'#fff',12,'start',maxw=760)
    o+=T('RIVALUTAZIONE',40,196,92,YEL,12,'start',maxw=760)
    o+=R(840,38,400,104,'url(#rd)',r=14,stroke='#fff',sw=5,rot=-3)+T('TAGLIO',1040,38+52+30,84,'#fff',maxw=360,rot=-3)
    o+=pill_small(960,168,280,40,'DISEGNO DI LEGGE',24)
    for i in range(6):
        o+=step(i,462+i*125,290+i*46)
    o+=T('6',165,508,330,YEL,16,maxw=260)
    o+=T('SCALINI',185,576,62,'#fff',9,maxw=300)
    o+=R(40,614,1200,86,YEL,r=20,stroke=INK,sw=6)+T('SU QUALE SCALINO SEI?',640,614+43+19,58,INK,maxw=1130,box=(40,614,1200,86))
    return page(o,(300,420))
# ---------------- B: QUADRANTE 100% -> ?% ----------------
def sector(cx,cy,R0,R1,a0,a1,fill):
    p=lambda r,a:(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))
    x0,y0=p(R1,a0);x1,y1=p(R1,a1);x2,y2=p(R0,a1);x3,y3=p(R0,a0)
    return f'<path d="M{x0:.1f} {y0:.1f} A{R1} {R1} 0 0 1 {x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} A{R0} {R0} 0 0 0 {x3:.1f} {y3:.1f}Z" fill="{fill}" stroke="#fff" stroke-width="5" stroke-linejoin="round"/>'
def B():
    cx,cy=640,558
    o=T('PENSIONI 2027',560,128,118,'#fff',13,maxw=880)
    o+=R(330,150,620,62,'url(#rd)',r=14,stroke='#fff',sw=4,rot=-2)+T('RIVALUTAZIONE TAGLIATA',640,150+31+15,40,'#fff',maxw=580,rot=-2)
    o+=f'<g filter="url(#sh)">'+sector(cx,cy,215,315,180,252,'url(#gr)')+sector(cx,cy,215,315,252,360,'url(#rd)')+'</g>'
    for a in range(180,361,18):
        r=math.radians(a)
        o+=f'<line x1="{cx+322*math.cos(r):.1f}" y1="{cy+322*math.sin(r):.1f}" x2="{cx+338*math.cos(r):.1f}" y2="{cy+338*math.sin(r):.1f}" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    # lancetta verso la zona rossa
    ang=math.radians(318)
    tx,ty=cx+262*math.cos(ang),cy+262*math.sin(ang)
    o+=f'<g filter="url(#sh)"><line x1="{cx}" y1="{cy}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="#fff" stroke-width="26" stroke-linecap="round"/><line x1="{cx}" y1="{cy}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="{INK}" stroke-width="14" stroke-linecap="round"/></g>'
    o+=f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="46" fill="url(#go)" stroke="#fff" stroke-width="6"/></g>'+T('€',cx,cy+22,60,'#7A4D00',maxw=50)
    bx,by=cx+262*math.cos(ang),cy+262*math.sin(ang)
    # numeri laterali
    o+=T('100%',170,430,116,'#fff',12,maxw=290)+T('AUMENTO PIENO',170,484,38,'#fff',5,maxw=280)
    o+=T('? %',1110,430,132,YEL,14,maxw=290)+T('COL TAGLIO',1110,484,38,'#fff',5,maxw=280)
    o+=pill_small(1010,50,236,40,'DISEGNO DI LEGGE',22)
    o+=R(40,614,1200,86,YEL,r=20,stroke=INK,sw=6)+T('QUANTO PERDI COL TAGLIO?',640,614+43+19,58,INK,maxw=1130,box=(40,614,1200,86))
    return page(o,(640,566))
# ---------------- C: CARTELLO LIMITE ----------------
def C():
    o=R(30,24,1220,86,'url(#rd)',r=16,stroke='#fff',sw=5,rot=-1)+T('RIVALUTAZIONE PENSIONI 2027',640,24+43+19,58,'#fff',maxw=1140,rot=-1)
    # palo + cartello
    o+=f'<rect x="318" y="570" width="26" height="60" fill="#9FB3B8" stroke="#fff" stroke-width="3"/>'
    o+=f'<g filter="url(#sh)"><circle cx="330" cy="372" r="200" fill="#fff" stroke="{RED}" stroke-width="40"/></g>'
    o+=T('? €',330,420,150,INK,0,maxw=290)+T('SOGLIA',330,500,46,INK,0,maxw=240)
    # testo a destra
    o+=T('OLTRE',900,280,150,YEL,16,maxw=520)
    o+=T('QUESTA SOGLIA',900,376,80,'#fff',10,maxw=600)
    o+=R(640,414,520,96,'url(#rd)',r=14,stroke='#fff',sw=6,rot=-4)+T('SCATTA IL TAGLIO?',900,414+48+19,50,'#fff',maxw=470,rot=-4)
    o+=pill_small(960,540,280,42,'DISEGNO DI LEGGE',24)
    o+=arrow(626,452,566,424,18)
    o+=R(40,614,1200,86,YEL,r=20,stroke=INK,sw=6)+T('DA QUALE IMPORTO? IL CONTO VERO',640,614+43+19,56,INK,maxw=1130,box=(40,614,1200,86))
    return page(o,(330,372))
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
