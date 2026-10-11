import asyncio,os,re
from playwright.async_api import async_playwright
src=open('../../14-video-lungo-4-invalidita-2027/miniatura/vecchie-45cent/gen.py').read()
HEAD=re.search(r"HEAD='''(.*?)'''",src,re.S).group(1)
S='stroke="#06282C" stroke-linejoin="round" paint-order="stroke"'
END='</svg></body></html>'
STRIP=lambda txt:f'<g filter="url(#sh)"><rect x="30" y="630" width="1220" height="68" rx="20" fill="#fff"/><rect x="30" y="630" width="1220" height="68" rx="20" fill="none" stroke="#FFD43B" stroke-width="7"/></g><text x="640" y="681" class="t" font-size="44" fill="#C0200F" text-anchor="middle">{txt}</text>'
def card(x,y,r,sc,lordo,netto):
    return f'''<g transform="translate({x} {y}) rotate({r}) scale({sc})" filter="url(#sh)"><rect x="-190" y="-215" width="380" height="430" rx="26" fill="url(#pp)" stroke="#fff" stroke-width="6"/>
<rect x="-190" y="-215" width="380" height="76" rx="26" fill="#1B9F81"/><rect x="-190" y="-185" width="380" height="46" fill="#1B9F81"/>
<text x="0" y="-160" class="t" font-size="34" fill="#fff" text-anchor="middle">TREDICESIMA</text>
<text x="-150" y="-85" class="t" font-size="30" fill="#5B7A7E">LORDA</text><text x="150" y="-85" class="t" font-size="44" fill="#0B4A50" text-anchor="end">{lordo}</text>
<rect x="-150" y="-55" width="300" height="8" rx="4" fill="#BFD0D3"/>
<text x="-150" y="-5" class="t" font-size="30" fill="#C0200F">IRPEF</text><text x="150" y="-5" class="t" font-size="44" fill="#C0200F" text-anchor="end">-990€</text>
<rect x="-150" y="40" width="300" height="130" rx="24" fill="#E3F6F1" stroke="#1B9F81" stroke-width="6"/>
<text x="0" y="88" class="t" font-size="30" fill="#1B9F81" text-anchor="middle">NETTO</text>
<text x="0" y="146" class="t" font-size="64" fill="#0B4A50" text-anchor="middle">{netto}</text></g>'''
# A: DETASSATA? + timbro SOLO PROPOSTA
A=HEAD+f'''<circle cx="360" cy="400" r="300" fill="#FFD43B" opacity="0.18" filter="url(#gl)"/>
<g class="t" {S} stroke-width="18"><text x="30" y="125" font-size="96" fill="#fff">TREDICESIMA</text><text x="34" y="240" font-size="110" fill="#FFD43B">2026</text></g>
<g class="t" {S} stroke-width="20"><text x="30" y="400" font-size="112" fill="#FF5A43">DETASSATA?</text></g>
<g transform="rotate(-5 330 520)" filter="url(#sh)"><rect x="40" y="440" width="540" height="100" rx="16" fill="none" stroke="#FFD43B" stroke-width="9"/><rect x="40" y="440" width="540" height="100" rx="16" fill="#FFD43B" opacity="0.15"/></g>
<text x="312" y="507" class="t" font-size="44" fill="#FFD43B" text-anchor="middle" transform="rotate(-5 330 520)" {S} stroke-width="10">SOLO UNA PROPOSTA</text>
{card(1040,290,6,0.92,"3.000€","2.010€")}
'''+STRIP('LA TREDICESIMA <tspan fill="#0D5158">NETTA VERA</tspan>')+END
# B: tabella lordo -> netto
rows=[("1.000€","770€",0),("1.500€","1.155€",0),("2.000€","1.540€",0),("3.000€","2.010€",1)]
tb='''<g filter="url(#sh)"><rect x="40" y="40" width="700" height="570" rx="32" fill="url(#pp)" stroke="#fff" stroke-width="6"/><rect x="40" y="40" width="700" height="90" rx="32" fill="#1B9F81"/><rect x="40" y="90" width="700" height="40" fill="#1B9F81"/></g>
<text x="90" y="102" class="t" font-size="38" fill="#fff">LORDA</text><text x="700" y="102" class="t" font-size="38" fill="#fff" text-anchor="end">NETTO</text><text x="390" y="104" class="t" font-size="50" fill="#FFD43B" text-anchor="middle">➜</text>'''
for i,(a,b,h) in enumerate(rows):
    y=215+i*115
    if h: tb+=f'<rect x="55" y="{y-68}" width="690" height="104" rx="20" fill="#FDE3DE"/>'
    tb+=f'<text x="90" y="{y}" class="t" font-size="62" fill="#0B4A50">{a}</text><text x="700" y="{y}" class="t" font-size="{76 if h else 62}" fill="{"#C0200F" if h else "#1B9F81"}" text-anchor="end">{b}</text>'
    if i<3: tb+=f'<line x1="70" y1="{y+22}" x2="730" y2="{y+22}" stroke="#C5D4D7" stroke-width="4"/>'
B=HEAD+f'''<circle cx="1000" cy="330" r="300" fill="#FFD43B" opacity="0.18" filter="url(#gl)"/>
{tb}
<g transform="rotate(5 1020 90)" filter="url(#sh)"><rect x="800" y="40" width="440" height="90" rx="12" fill="#E0402A" stroke="#fff" stroke-width="5"/></g>
<text x="1020" y="104" class="t" font-size="50" fill="#fff" text-anchor="middle" transform="rotate(5 1020 90)">⚠ ATTENZIONE</text>
<g class="t" {S} stroke-width="16" text-anchor="middle"><text x="1020" y="260" font-size="58" fill="#fff">TREDICESIMA</text><text x="1020" y="365" font-size="86" fill="#FFD43B">QUANTO</text><text x="1020" y="465" font-size="86" fill="#FF5A43">ARRIVA?</text></g>
<g filter="url(#sh)"><circle cx="1060" cy="545" r="78" fill="url(#ye)" stroke="#fff" stroke-width="6"/></g><text x="1060" y="540" class="t" font-size="22" fill="#7A3B00" text-anchor="middle">TUA PENSIONE?</text><text x="1060" y="575" class="t" font-size="22" fill="#7A3B00" text-anchor="middle">ECCO IL NETTO</text>
'''+STRIP('DA 1.000 A 3.000€: <tspan fill="#0D5158">IL NETTO DI DICEMBRE</tspan>')+END
# C: -990 gigante
C=HEAD+f'''<circle cx="640" cy="330" r="330" fill="#FF5A43" opacity="0.18" filter="url(#gl)"/>
<g filter="url(#sh)"><circle cx="150" cy="150" r="115" fill="url(#re)" stroke="#fff" stroke-width="8"/><circle cx="1130" cy="150" r="115" fill="url(#gr)" stroke="#fff" stroke-width="8"/></g>
<g class="t" text-anchor="middle" {S} stroke-width="10"><text x="150" y="170" font-size="52" fill="#fff">3.000€</text><text x="1130" y="170" font-size="52" fill="#fff">2.010€</text></g>
<g class="t" text-anchor="middle" font-size="36" fill="#fff" {S} stroke-width="8"><text x="150" y="300">LORDA</text><text x="1130" y="300">NETTA</text></g>
<path d="M300 150 L520 150" stroke="#FFD43B" stroke-width="22" stroke-linecap="round" stroke-dasharray="1 40"/><path d="M760 150 L930 150" stroke="#FFD43B" stroke-width="22" stroke-linecap="round" stroke-dasharray="1 40"/><path d="M930 112 L995 150 L930 188Z" fill="#FFD43B" stroke="#06282C" stroke-width="6" stroke-linejoin="round"/>
<g class="t" text-anchor="middle" {S} stroke-width="14"><text x="640" y="95" font-size="58" fill="#fff">TREDICESIMA</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="26"><text x="640" y="470" font-size="270" fill="#FF5A43" letter-spacing="-8">-990€</text></g>
<g class="t" text-anchor="middle" {S} stroke-width="12"><text x="640" y="580" font-size="66" fill="#FFD43B">QUASI MILLE EURO IN MENO</text></g>
'''+STRIP('LA TREDICESIMA DA 3.000€: <tspan fill="#0D5158">IL CONTO VERO</tspan>')+END
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        for n,h in (('A',A),('B',B),('C',C)):
            open(f'miniatura-{n}.html','w').write(h)
            await pg.goto(f'file://{os.getcwd()}/miniatura-{n}.html'); await pg.screenshot(path=f'miniatura-{n}.png')
        await b.close()
asyncio.run(main())
