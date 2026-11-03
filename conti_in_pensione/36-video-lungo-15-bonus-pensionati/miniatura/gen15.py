# Miniature video 15 (Carta Dedicata a te e pensionati): A carta prepagata 500 euro + LA PRENDI?, B elenco del Comune con lente + C'E' IL TUO NOME?
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
<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22C1BB"/><stop offset="0.55" stop-color="#0B5E6B"/><stop offset="1" stop-color="#052C33"/></linearGradient>
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

def pcard(x,y,w,h,rot,amt,amtfs,title,second=False,cx=None,cy=None):
    cx=cx if cx is not None else x+w/2;cy=cy if cy is not None else y+h/2
    o=f'<g transform="rotate({rot} {cx} {cy})" filter="url(#sh)">'
    o+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="30" fill="url(#cg)" stroke="#fff" stroke-width="6"/>'
    o+=f'<polygon points="{x},{y+h*0.32} {x+w*0.55},{y} {x+w*0.78},{y} {x},{y+h*0.62}" fill="#fff" opacity="0.08"/>'
    o+=f'<rect x="{x+34}" y="{y+88}" width="84" height="62" rx="10" fill="#F2C96B" stroke="#B88A1F" stroke-width="3"/>'
    for k in (-1,0,1):o+=f'<line x1="{x+34}" y1="{y+119+k*18}" x2="{x+118}" y2="{y+119+k*18}" stroke="#B88A1F" stroke-width="3"/>'
    o+=f'<line x1="{x+76}" y1="{y+88}" x2="{x+76}" y2="{y+150}" stroke="#B88A1F" stroke-width="3"/>'
    o+=f'<circle cx="{x+w-96}" cy="{y+h-58}" r="40" fill="#E0402A" opacity="0.92"/><circle cx="{x+w-58}" cy="{y+h-58}" r="40" fill="#FFB838" opacity="0.92"/>'
    o+='</g>'
    return o
def pcard_text(x,y,w,h,rot,amt,amtfs,title,cx=None,cy=None):
    cx=cx if cx is not None else x+w/2;cy=cy if cy is not None else y+h/2
    o=f'<g transform="rotate({rot} {cx} {cy})">'
    o+=T(title,x+34,y+58,42,'#fff',0,'start',maxw=w-70,box=None)
    o+=T(amt,x+34,y+h-36,amtfs,'#fff',10,'start',maxw=w*0.66)
    return o+'</g>'
# ---------------- A: CARTA PREPAGATA + LA PRENDI? ----------------
def A():
    o=''
    # seconda carta dietro (+500 da aprile)
    o+=pcard(130,200,470,296,5,'',0,'')
    o+=f'<g transform="rotate(5 365 348)">'+T('+500 €',600-34,200+78,70,YEL,8,'end',maxw=300)+'</g>'
    # prima carta davanti
    o+=pcard(40,300,470,296,-7,'',0,'')
    o+=pcard_text(40,300,470,296,-7,'500 €',150,'DEDICATA A TE')
    o+=T('PENSIONI',40,168,128,'#fff',14,'start',maxw=620)
    o+=R(700,96,320,54,'url(#rd)',r=12,stroke='#fff',sw=4,rot=-2)+T('DAL 4 NOVEMBRE',860,96+27+11,30,'#fff',maxw=290,rot=-2)
    # destra: LA PRENDI?
    o+=T('LA',930,300,96,'#fff',12,maxw=300)
    o+=T('PRENDI?',930,430,138,YEL,16,maxw=600)
    o+=R(640,462,590,84,'url(#rd)',r=14,stroke='#fff',sw=6,rot=-3)+T('NON PER TUTTI',935,462+42+19,54,'#fff',maxw=520,rot=-3)
    o+=pill_small(1000,22,240,42,'DAL DECRETO',24)
    o+=R(0,612,1280,108,YEL,r=0,stroke=INK,sw=6,shadow=False)
    o+=T('FAMIGLIE PICCOLE: UNA REGOLA IN PIÙ',640,612+54+19,56,INK,maxw=1200,box=(0,612,1280,108))
    return page(o,(300,330))
# ---------------- B: ELENCO DEL COMUNE + LENTE ----------------
def B():
    o=T('PENSIONI',1240,150,128,'#fff',14,'end',maxw=620)
    # moneta 500
    o+=coin(960,370,160,False)+T('500 €',960,405,96,'#7A4D00',0,maxw=250)
    o+=pill_small(800,548,320,46,'NESSUNA DOMANDA',26)
    # elenco del Comune
    X,Y,Wd,Hd=50,40,560,540
    o+=R(X,Y,Wd,Hd,'#fff',r=24,stroke='#fff',sw=5)
    o+=HEADP(X,Y,Wd,86,'#1B9F81')
    o+=T('ELENCO DEL COMUNE',X+Wd/2,Y+58,44,'#fff',maxw=Wd-50,box=(X,Y,Wd,86))
    for i in range(6):
        ry=Y+112+i*74
        on=(i==3)
        if on:o+=f'<rect x="{X+16}" y="{ry-8}" width="{Wd-32}" height="64" rx="14" fill="#FFF1CC" stroke="{YEL}" stroke-width="5"/>'
        o+=f'<circle cx="{X+56}" cy="{ry+24}" r="20" fill="{YEL if on else "#B7C7CA"}"/>'
        o+=f'<rect x="{X+96}" y="{ry+14}" width="{[300,240,330,270,210,280][i]}" height="20" rx="10" fill="{INK if on else "#C3D3D7"}"/>'
        if on:o+=f'<path d="M{X+Wd-92} {ry+26} l20 22 l40 -44" fill="none" stroke="#1B9F81" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>'
    # lente sopra la riga evidenziata
    o+=f'<g filter="url(#sh)"><circle cx="{X+330}" cy="{Y+112+3*74+24}" r="74" fill="rgba(255,255,255,0.16)" stroke="#fff" stroke-width="12"/><line x1="{X+384}" y1="{Y+112+3*74+78}" x2="{X+452}" y2="{Y+112+3*74+146}" stroke="{YEL}" stroke-width="22" stroke-linecap="round"/></g>'
    o+=f'<ellipse cx="{X+Wd/2}" cy="{Y+112+3*74+24}" rx="{Wd/2-6}" ry="48" fill="none" stroke="{RED}" stroke-width="8"/>'
    o+=R(X+20,Y+Hd-70,Wd-40,92,'url(#rd)',r=16,stroke='#fff',sw=6,rot=-2)+T('C\'È IL TUO NOME?',X+Wd/2,Y+Hd-70+46+20,52,'#fff',maxw=Wd-90,rot=-2)
    o+=R(0,612,1280,108,YEL,r=0,stroke=INK,sw=6,shadow=False)
    o+=T('LE CARTE SONO LIMITATE: CONTA DOVE ABITI',640,612+54+19,54,INK,maxw=1200,box=(0,612,1280,108))
    return page(o,(960,360))
FIT='''()=>{const bad=[];document.querySelectorAll('text').forEach(t=>{const mw=+t.dataset.w;let fs=+t.getAttribute('font-size');
 let b=t.getBBox();if(mw&&b.width>mw){fs=fs*mw/b.width;t.setAttribute('font-size',fs.toFixed(1));b=t.getBBox();}
 if(t.dataset.box){const [x,y,w,h]=t.dataset.box.split(',').map(Number);if(b.x<x+6||b.x+b.width>x+w-6||b.y<y+2||b.y+b.height>y+h-2)bad.push([t.textContent,Math.round(b.x),Math.round(b.y),Math.round(b.width),Math.round(b.height)]);}
 if(b.x<8||b.x+b.width>1272||b.y<4||b.y+b.height>716)bad.push(['FUORI',t.textContent,Math.round(b.x),Math.round(b.y)]);});
 return bad;}'''
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
        pg=await br.new_page(viewport={'width':W,'height':H})
        for k,f in (('A',A),('B',B)):
            open(f'miniatura-{k}.html','w',encoding='utf-8').write(f())
            await pg.goto(f'file://{__import__("os").getcwd()}/miniatura-{k}.html')
            bad=await pg.evaluate(FIT)
            print(k,'PROBLEMI:' if bad else 'testi ok',bad if bad else '')
            await pg.screenshot(path=f'miniatura-{k}.png')
        await br.close()
asyncio.run(main())
