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
# ===== VIDEO 7: RIVALUTAZIONE TAGLIATA (3 layout nuovi, diversi da video 3-6: niente cedolino a destra) =====
def scontrino(x,y,r,sc):
    zz=''.join(f'L{170-(i+0.5)*340/14} 262 L{170-(i+1)*340/14} 276 ' for i in range(14))
    righe=''.join(f'<text x="-140" y="{-95+i*62}" class="t" font-size="34" fill="#0B4A50">{a}</text><text x="140" y="{-95+i*62}" class="t" font-size="38" fill="#C0200F" text-anchor="end">{b}</text><rect x="-140" y="{-80+i*62}" width="280" height="4" rx="2" fill="#C9D6D8"/>' for i,(a,b) in enumerate([("2023","-1.482€"),("2024","-2.597€"),("2025","-2.630€"),("2026","-2.688€")]))
    return f'''<g transform="translate({x} {y}) rotate({r}) scale({sc})" filter="url(#sh)"><path d="M-170 -250 H170 V276 {zz} Z" fill="url(#pp)" stroke="#fff" stroke-width="5"/>
<rect x="-170" y="-250" width="340" height="80" rx="10" fill="#1B9F81"/><text x="0" y="-197" class="t" font-size="25" fill="#fff" text-anchor="middle">SCONTRINO PENSIONE</text>
{righe}<rect x="-150" y="150" width="300" height="7" rx="3" fill="#0B4A50"/>
<text x="0" y="238" class="t" font-size="68" fill="#C0200F" text-anchor="middle">-9.400€</text></g>'''
# A: scontrino a SINISTRA, testo a destra
A=HEAD+f"""<circle cx="330" cy="340" r="300" fill="#FF5A43" opacity="0.15" filter="url(#gl)"/>
{scontrino(300,330,-5,1.05)}
<g class="t" {S} stroke-width="18"><text x="575" y="140" font-size="122" fill="#fff">PENSIONI</text></g>
{blocco(575,170,680,100,"RIVALUTAZIONE",64,"#FFD43B","#0D2A2F")}
<g class="t" {S} stroke-width="16"><text x="575" y="385" font-size="88" fill="#FF5A43">QUANTO HAI</text><text x="575" y="485" font-size="88" fill="#FF5A43">PERSO?</text></g>
{blocco(580,510,330,74,"IN 4 ANNI",48,"#E0402A","#fff",-3)}
"""+STRIP('IL CONTO <tspan fill="#0D5158">ANNO PER ANNO</tspan>')+END
# B: la FORBICE tra pensione piena e tagliata (grafico)
B=HEAD+f"""<circle cx="640" cy="360" r="320" fill="#FFD43B" opacity="0.12" filter="url(#gl)"/>
<g class="t" text-anchor="middle" {S} stroke-width="20"><text x="640" y="135" font-size="132" fill="#fff">PENSIONI</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="14"><text x="640" y="215" font-size="66" fill="#FFD43B">RIVALUTAZIONE TAGLIATA</text></g>
<g filter="url(#sh)"><rect x="60" y="250" width="640" height="350" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/></g>
<path d="M110 545 L250 470 L400 360 L520 335 L650 300" fill="none" stroke="#1B9F81" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M110 545 L250 495 L400 445 L520 440 L650 430" fill="none" stroke="#E0402A" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M650 312 V418" stroke="#0B4A50" stroke-width="7" stroke-dasharray="12 8"/>
<text x="120" y="300" class="t" font-size="32" fill="#1B9F81">PIENA</text><text x="120" y="340" class="t" font-size="32" fill="#E0402A">TAGLIATA</text>
<text x="110" y="585" class="t" font-size="26" fill="#5B7A7E">2022</text><text x="650" y="585" class="t" font-size="26" fill="#5B7A7E" text-anchor="middle">2026</text>
<g filter="url(#sh)"><circle cx="985" cy="410" r="175" fill="url(#re)" stroke="#fff" stroke-width="10"/></g>
<g class="t" text-anchor="middle" {S} stroke-width="12"><text x="985" y="420" font-size="90" fill="#fff">-207€</text><text x="985" y="485" font-size="44" fill="#fff">AL MESE</text></g>
"""+STRIP('IL BUCO <tspan fill="#0D5158">CHE NON SI RICHIUDE</tspan>')+END
# C: il TEST - numero gigante + 3 palline (niente, poco, tanto)
def pallina(cx,cy,r,fill,txt,fs):return f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="8"/></g><g class="t" text-anchor="middle" {S} stroke-width="9"><text x="{cx}" y="{cy+fs*0.36}" font-size="{fs}" fill="#fff">{txt}</text></g>'
C=HEAD+f"""<circle cx="380" cy="380" r="320" fill="#FF5A43" opacity="0.14" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text x="30" y="140" font-size="140" fill="#fff">PENSIONI</text></g>
<g class="t" {S} stroke-width="22"><text x="30" y="350" font-size="196" fill="#FFD43B">-9.400€</text></g>
{blocco(36,385,640,84,"RIVALUTAZIONE TAGLIATA",44,"#E0402A","#fff",-3)}
<g class="t" {S} stroke-width="14"><text x="40" y="575" font-size="76" fill="#fff">E TU QUANTO?</text></g>
{pallina(1080,150,92,"url(#gr)","NIENTE",34)}
{pallina(1080,345,92,"#F2A900","POCO",44)}
{pallina(1080,540,92,"url(#re)","TANTO",38)}
"""+STRIP('FAI IL TEST: <tspan fill="#0D5158">IN QUALE FASCIA SEI?</tspan>')+END
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html'); await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
