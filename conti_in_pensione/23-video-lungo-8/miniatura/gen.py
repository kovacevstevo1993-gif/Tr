import asyncio,os,re
from playwright.async_api import async_playwright
src=open('../../14-video-lungo-4-invalidita-2027/miniatura/vecchie-45cent/gen.py').read()
HEAD=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
S='stroke="#06282C" stroke-linejoin="round" paint-order="stroke"'
END='</svg></body></html>'
STRIP=lambda txt:f'<g filter="url(#sh)"><rect x="30" y="630" width="1220" height="68" rx="20" fill="#fff"/><rect x="30" y="630" width="1220" height="68" rx="20" fill="none" stroke="#FFD43B" stroke-width="7"/></g><text x="640" y="681" class="t" font-size="44" fill="#C0200F" text-anchor="middle">{txt}</text>'
def blocco(x,y,w,h,txt,fs,fill="#FFD43B",col="#0D2A2F",rot=0):
    cx=x+w/2;cy=y+h/2
    return f'<g transform="rotate({rot} {cx} {cy})"><g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}"/></g><text x="{cx}" y="{y+h*0.72}" class="t" font-size="{fs}" fill="{col}" text-anchor="middle">{txt}</text></g>'
def flag(code,x,y,w,rot=0):
    h=w*2/3;x0=-w/2;y0=-h/2;R=lambda a,b,c,d,f:f'<rect x="{a}" y="{b}" width="{c}" height="{d}" fill="{f}"/>'
    if code=='IT':b=R(x0,y0,w/3+1,h,'#1F9A4B')+R(x0+w/3,y0,w/3+1,h,'#F7F7F2')+R(x0+2*w/3,y0,w/3+1,h,'#D7322B')
    elif code=='PT':b=R(x0,y0,w*0.4+1,h,'#0B6E3B')+R(x0+w*0.4,y0,w*0.6+1,h,'#D52B1E')+f'<circle cx="{x0+w*0.4}" cy="0" r="{h*0.21}" fill="#F4C430" stroke="#fff" stroke-width="3"/><circle cx="{x0+w*0.4}" cy="0" r="{h*0.1}" fill="#D52B1E"/>'
    elif code=='TN':b=R(x0,y0,w,h,'#D21F2A')+f'<circle r="{h*0.31}" fill="#fff"/><circle r="{h*0.23}" fill="#D21F2A"/><circle cx="{h*0.07}" r="{h*0.19}" fill="#fff"/>'
    elif code=='AL':
        s=h/220;b=R(x0,y0,w,h,'#E41E20')+f'<g transform="scale({s})" fill="#111"><path d="M0 -45 L20 0 L0 62 L-20 0 Z"/><path d="M-16 -30 L-92 -66 L-80 -34 L-104 -22 L-78 -4 L-96 14 L-66 18 L-74 36 L-16 22 Z"/><path d="M16 -30 L92 -66 L80 -34 L104 -22 L78 -4 L96 14 L66 18 L74 36 L16 22 Z"/><circle cx="-15" cy="-58" r="12"/><circle cx="15" cy="-58" r="12"/><path d="M-14 58 L0 92 L14 58 Z"/></g>'
    cid=f'c{code}{int(x)}{int(y)}'
    return f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#sh)"><clipPath id="{cid}"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="10"/></clipPath><g clip-path="url(#{cid})">{b}</g><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="10" fill="none" stroke="#fff" stroke-width="7"/></g>'
def pallina(cx,cy,r,fill,t1,f1,t2,f2):return f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="9"/></g><g class="t" text-anchor="middle" {S} stroke-width="10"><text x="{cx}" y="{cy+f1*0.3}" font-size="{f1}" fill="#fff">{t1}</text><text x="{cx}" y="{cy+f1*0.3+f2+8}" font-size="{f2}" fill="#fff">{t2}</text></g>'
def passaporto(x,y,rot,sc):return f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})" filter="url(#sh)"><rect x="-150" y="-210" width="300" height="420" rx="26" fill="#0E4F3A" stroke="#fff" stroke-width="7"/><rect x="-150" y="-210" width="30" height="420" rx="12" fill="#0A3A2B"/><circle cx="15" cy="10" r="70" fill="none" stroke="#E9C46A" stroke-width="8"/><path d="M15 -34 L25 -4 L57 -4 L31 14 L41 44 L15 26 L-11 44 L-1 14 L-27 -4 L5 -4 Z" fill="#E9C46A"/><rect x="-75" y="-150" width="180" height="16" rx="8" fill="#E9C46A"/><rect x="-60" y="120" width="150" height="40" rx="8" fill="none" stroke="#E9C46A" stroke-width="5"/></g>'
# A: PASSAPORTO con bandiere-timbro a destra, testo a sinistra
A=HEAD+f"""<circle cx="960" cy="330" r="300" fill="#FFD43B" opacity="0.13" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text x="34" y="140" font-size="138" fill="#fff">PENSIONE</text></g>
{blocco(40,170,520,96,"ALL'ESTERO",66,"#FFD43B","#0D2A2F",-2)}
<g class="t" {S} stroke-width="16"><text x="40" y="385" font-size="86" fill="#fff">QUANTO TI</text><text x="40" y="480" font-size="86" fill="#FFD43B">RESTA?</text></g>
{blocco(36,505,640,78,"3 TRAPPOLE NASCOSTE",44,"#E0402A","#fff",-3)}
{passaporto(930,350,8,1.05)}
{flag('PT',1150,140,150,12)}{flag('TN',1170,330,150,-8)}{flag('AL',1140,520,150,10)}
"""+STRIP('IL CONTO VERO: <tspan fill="#0D5158">1.000, 1.500 E 2.000 €</tspan>')+END
# B: ITALIA contro ALBANIA con le palline rosso/verde e VS
B=HEAD+f"""<circle cx="640" cy="390" r="330" fill="#FF5A43" opacity="0.12" filter="url(#gl)"/>
<g class="t" text-anchor="middle" {S} stroke-width="20"><text x="640" y="128" font-size="94" fill="#fff">PENSIONE <tspan fill="#FFD43B">ALL'ESTERO</tspan></text></g>
{flag('IT',250,300,250,-5)}{flag('AL',1030,300,250,5)}
{pallina(250,500,122,"url(#re)","-5.100€",50,"IRPEF L'ANNO",26)}
{pallina(1030,500,118,"url(#gr)","0€",86,"OGGI?",32)}
<g filter="url(#sh)"><circle cx="640" cy="400" r="80" fill="#FFD43B" stroke="#fff" stroke-width="8"/></g><g class="t" text-anchor="middle" {S} stroke-width="10"><text x="640" y="430" font-size="84" fill="#fff">VS</text></g>
{blocco(470,175,340,62,"2.000 € LORDI",40,"#0D5158","#fff")}
"""+STRIP('DOVE TI RESTANO <tspan fill="#0D5158">PIÙ SOLDI?</tspan>')+END

# C: ITALIA (pallina rossa -5.100) contro i 3 PAESI con il loro verdetto, frecce tratteggiate
def pill(x,y,w,h,txt,fs,fill,col="#fff"):return f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" stroke="#fff" stroke-width="5"/></g><text x="{x+w/2}" y="{y+h*0.68}" class="t" font-size="{fs}" fill="{col}" text-anchor="middle">{txt}</text>'
FR=lambda y:f'<path d="M440 430 C560 430 560 {y} 660 {y}" fill="none" stroke="#FFD43B" stroke-width="9" stroke-dasharray="20 14" stroke-linecap="round"/><path d="M660 {y-16} L688 {y} L660 {y+16} Z" fill="#FFD43B"/>'
C=HEAD+f"""<circle cx="300" cy="420" r="300" fill="#FF5A43" opacity="0.12" filter="url(#gl)"/>
<g class="t" text-anchor="middle" {S} stroke-width="18"><text x="640" y="118" font-size="96" fill="#fff">PENSIONE <tspan fill="#FFD43B">ALL'ESTERO</tspan></text></g>
{FR(225)}{FR(395)}{FR(565)}
{flag('IT',290,282,200,-4)}
{pill(160,152,260,50,"2.000 € LORDI",28,"#0D5158")}
{pallina(290,470,118,"url(#re)","-5.100€",50,"IRPEF L'ANNO",26)}
{flag('PT',770,225,130,4)}{pill(860,197,390,58,"TASSE A SCAGLIONI",30,"#E0402A")}
{flag('TN',770,395,130,-4)}{pill(860,367,390,58,"TASSATO SOLO 1/5",30,"#F2A900","#0D2A2F")}
{flag('AL',770,565,130,4)}{pill(860,537,390,58,"0 € DI TASSE OGGI?",30,"#1B9F81")}
"""+STRIP('DOVE TI CONVIENE? <tspan fill="#0D5158">+ 3 TRAPPOLE</tspan>')+END
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('C',C),):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html'); await pg.screenshot(path=f'miniatura-{n}.png')
            r=await pg.evaluate("()=>[...document.querySelectorAll('text')].map(t=>{const b=t.getBoundingClientRect();return [t.textContent,Math.round(b.left),Math.round(b.right),Math.round(b.top),Math.round(b.bottom)]})")
            print(n,[x for x in r if x[1]<0 or x[2]>1280 or x[3]<0 or x[4]>720])
        await b.close()
asyncio.run(main())
