# Miniature video 9 (pensioni di dicembre). Stile del canale: sfondo verde acqua a raggi, scritte giganti con contorno scuro,
# palline rosso/verde, striscia bianca con bordo giallo. Layout NUOVI (busta della rata con 3 pagamenti; numero gigante + tre vicini).
# La risposta resta nascosta ("?"): chi prende bonus e 14a lo dice il video.
import asyncio,os,re,json
from playwright.async_api import async_playwright
src=open('../../14-video-lungo-4-invalidita-2027/miniatura/vecchie-45cent/gen.py').read()
HEAD=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
S='stroke="#06282C" stroke-linejoin="round" paint-order="stroke"'
END='</svg></body></html>'
STRIP=lambda txt:f'<g filter="url(#sh)"><rect x="30" y="630" width="1220" height="68" rx="20" fill="#fff"/><rect x="30" y="630" width="1220" height="68" rx="20" fill="none" stroke="#FFD43B" stroke-width="7"/></g><text id="strip" x="640" y="681" class="t" font-size="44" fill="#C0200F" text-anchor="middle">{txt}</text>'
def blocco(x,y,w,h,txt,fs,fill="#FFD43B",col="#0D2A2F",rot=0,i=''):
    cx=x+w/2
    return f'<g transform="rotate({rot} {cx} {y+h/2})"><g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}"/></g><text id="{i}" x="{cx}" y="{y+h*0.72}" class="t" font-size="{fs}" fill="{col}" text-anchor="middle">{txt}</text></g>'
def qball(cx,cy,r,fill='url(#ye)'):
    return f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="{r*0.12}"/></g><text x="{cx}" y="{cy+r*0.42}" class="t" font-size="{r*1.25}" fill="#fff" text-anchor="middle" {S} stroke-width="{r*0.12}">?</text>'
def person(cx,cy,r,kind,col):
    SK='#F1D9C4';u=f'p{kind}{cx}'
    s=f'<g filter="url(#sh)"><clipPath id="{u}"><circle cx="0" cy="0" r="{r}"/></clipPath><circle cx="{cx}" cy="{cy}" r="{r}" fill="#0E5A60"/><g transform="translate({cx} {cy})"><g clip-path="url(#{u})">'
    s+=f'<path d="M{-r*0.9} {r} Q{-r*0.85} {r*0.3} 0 {r*0.26} Q{r*0.85} {r*0.3} {r*0.9} {r} Z" fill="{col}"/><rect x="{-r*0.12}" y="{r*0.02}" width="{r*0.24}" height="{r*0.28}" fill="{SK}"/>'
    if kind=='A':s+=f'<circle cx="0" cy="{-r*0.6}" r="{r*0.19}" fill="#6B4A3A"/>'
    s+=f'<ellipse cx="0" cy="{-r*0.18}" rx="{r*0.3}" ry="{r*0.35}" fill="{SK}"/>'
    if kind=='A':s+=f'<path d="M{-r*0.33} {-r*0.1} Q{-r*0.38} {-r*0.58} 0 {-r*0.58} Q{r*0.38} {-r*0.58} {r*0.33} {-r*0.1} Q{r*0.22} {-r*0.42} 0 {-r*0.42} Q{-r*0.22} {-r*0.42} {-r*0.33} {-r*0.1} Z" fill="#6B4A3A"/>'
    if kind=='L':s+=f'<path d="M{-r*0.38} {r*0.06} Q{-r*0.44} {-r*0.62} 0 {-r*0.58} Q{r*0.44} {-r*0.62} {r*0.38} {r*0.06} L{r*0.27} {r*0.06} Q{r*0.27} {-r*0.38} 0 {-r*0.38} Q{-r*0.27} {-r*0.38} {-r*0.27} {r*0.06} Z" fill="#D5DBDE"/>'
    if kind=='F':
        for k in (-1,1):s+=f'<path d="M{k*r*0.31} {-r*0.16} Q{k*r*0.34} {-r*0.46} {k*r*0.16} {-r*0.5}" fill="none" stroke="#C9D3D6" stroke-width="{r*0.1}" stroke-linecap="round"/><circle cx="{k*r*0.13}" cy="{-r*0.2}" r="{r*0.09}" fill="none" stroke="#0B4A50" stroke-width="{r*0.035}"/>'
    for k in (-1,1):s+=f'<circle cx="{k*r*0.12}" cy="{-r*0.2}" r="{r*0.032}" fill="#0B4A50"/>'
    s+=f'<path d="M{-r*0.1} {-r*0.01} Q0 {r*0.07} {r*0.1} {-r*0.01}" fill="none" stroke="#0B4A50" stroke-width="{r*0.032}" stroke-linecap="round"/></g></g>'
    s+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#fff" stroke-width="{r*0.08}"/><circle cx="{cx}" cy="{cy}" r="{r*1.09}" fill="none" stroke="{col}" stroke-width="{r*0.07}"/></g>'
    return s
def card(x,y,w,h,rot,fill,big,fs,sub,col='#fff'):
    return f'<g transform="rotate({rot} {x} {y})"><g filter="url(#sh)"><rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="#fff" stroke-width="7"/></g><text x="{x}" y="{y+fs*0.1}" class="t" font-size="{fs}" fill="{col}" text-anchor="middle" {S if col=='#fff' else ''} stroke-width="{max(3,fs*0.12)}">{big}</text><text x="{x}" y="{y+h/2-22}" class="t" font-size="26" fill="{col}" text-anchor="middle">{sub}</text></g>'
# A: LA BUSTA DELLA RATA DI DICEMBRE con 3 pagamenti che escono (due coperti da "?")
ENV=f'''<g filter="url(#sh)"><path d="M770 360 L1240 360 L1240 600 L770 600 Z" fill="url(#pp)"/></g>'''
ENVF=f'''<path d="M770 360 L1005 500 L1240 360 L1240 600 L770 600 Z" fill="#E9F1F3" stroke="#B9CDD2" stroke-width="4"/><path d="M770 600 L1005 470 L1240 600" fill="none" stroke="#B9CDD2" stroke-width="4"/>
<g filter="url(#sh)"><rect x="830" y="540" width="350" height="46" rx="23" fill="#0D5158"/></g><text x="1005" y="573" class="t" font-size="26" fill="#fff" text-anchor="middle">RATA DI DICEMBRE</text>'''
A=HEAD+f"""<circle cx="1000" cy="330" r="290" fill="#FFD43B" opacity="0.14" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text id="a1" x="30" y="128" font-size="124" fill="#fff">PENSIONI</text></g>
{blocco(36,156,430,92,"DICEMBRE",70,"#E0402A","#fff",-2,'a2')}
<g class="t" {S} stroke-width="16"><text id="a3" x="38" y="350" font-size="84" fill="#FFD43B">3 PAGAMENTI</text><text id="a4" x="38" y="440" font-size="84" fill="#fff">IN UNA RATA?</text></g>
{blocco(40,470,560,70,"CHI RESTA A ZERO?",44,"#0D5158","#fff",-2,'a5')}
{ENV}
{card(830,260,120,190,-4,"url(#gr)","13ª",60,"")}
{card(1000,235,190,230,0,"url(#ye)","154,94€",36,"BONUS","#0D2A2F")}
{card(1170,260,120,190,4,"url(#re)","14ª",60,"")}
{ENVF}
{qball(1080,130,36)}{qball(1215,170,36)}
"""+STRIP('A CHI SPETTANO <tspan fill="#0D5158">DAVVERO?</tspan>')+END
# B: NUMERO GIGANTE + TRE VICINI con "?" (chi lo prende?)
B=HEAD+f"""<circle cx="640" cy="300" r="330" fill="#25D08C" opacity="0.13" filter="url(#gl)"/>
<g class="t" text-anchor="middle" {S} stroke-width="18"><text id="b1" x="640" y="112" font-size="98" fill="#fff">PENSIONI <tspan fill="#FFD43B">DICEMBRE</tspan></text></g>
<g class="t" text-anchor="middle" {S} stroke-width="22"><text id="b2" x="640" y="300" font-size="176" fill="#3BE39A">+154,94€</text></g>
{blocco(280,332,720,74,"BONUS: TI SPETTA O NO?",46,"#FFD43B","#0D2A2F",-1,'b3')}
<g filter="url(#sh)"><circle cx="90" cy="380" r="44" fill="url(#gr)" stroke="#fff" stroke-width="6"/></g><text x="90" y="393" class="t" font-size="36" fill="#fff" text-anchor="middle" {S} stroke-width="6">13ª</text><g filter="url(#sh)"><circle cx="1190" cy="380" r="44" fill="url(#re)" stroke="#fff" stroke-width="6"/></g><text x="1190" y="393" class="t" font-size="36" fill="#fff" text-anchor="middle" {S} stroke-width="6">14ª</text>{person(250,520,78,'F','#2B8FA0')}{person(640,520,78,'A','#1B9F81')}{person(1030,520,78,'L','#E39A1C')}
{qball(322,452,34,'url(#re)')}{qball(712,452,34,'url(#gr)')}{qball(1102,452,34,'url(#ye)')}

"""+STRIP('PER 10 € IN PIÙ AL MESE <tspan fill="#0D5158">LO PERDI</tspan>')+END
JS="""()=>{const o=[];for(const t of document.querySelectorAll('text')){const r=t.getBoundingClientRect();if(r.width<2)continue;o.push([t.textContent.slice(0,22),Math.round(r.x),Math.round(r.y),Math.round(r.right),Math.round(r.bottom)]);}return o;}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html')
            for r in await pg.evaluate(JS):
                flag='' if r[1]>=8 and r[3]<=1272 and r[2]>=0 and r[4]<=716 else '  <<< FUORI'
                print(n,r,flag)
            await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
