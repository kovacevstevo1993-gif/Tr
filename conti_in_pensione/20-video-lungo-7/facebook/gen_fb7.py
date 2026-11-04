S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
def card(cx,year,i,last=False):
    x=cx-135
    head='url(#r)' if last else '#0D5158'
    body='<text x="135" y="270" font-size="170" fill="#C0200F" text-anchor="middle" id="q%d">?</text>'%i if last else f'<rect x="25" y="150" width="220" height="140" rx="22" fill="#0B1A1F"/><text x="135" y="248" font-size="58" fill="#FFD43B" text-anchor="middle" id="m{i}">− ? €</text>'
    lab='RISCHIO' if last else 'TAGLIO'
    return f'''<g transform="translate({x} 480)" filter="url(#sh)"><rect width="270" height="340" rx="30" fill="#FBFDFD"/><rect width="270" height="110" rx="30" fill="{head}"/><rect y="80" width="270" height="30" fill="{head}"/>
<text x="135" y="76" font-size="62" fill="{'#fff' if last else '#FFD43B'}" text-anchor="middle" id="y{i}">{year}</text>
{body}<text x="135" y="322" font-size="30" fill="#5B7479" text-anchor="middle" id="l{i}">{lab if last else 'ANNO'}</text></g>'''
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E7C86"/><stop offset=".55" stop-color="#0A4F5C"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="rays" width="120" height="120" patternUnits="userSpaceOnUse" patternTransform="rotate(-20)"><rect width="60" height="120" fill="#fff" fill-opacity=".045"/></pattern>
</defs>
<rect width="1920" height="1080" fill="url(#bg)"/><rect width="1920" height="1080" fill="url(#rays)"/>
<g transform="translate(90 60) rotate(-3)" filter="url(#sh)"><rect width="420" height="76" rx="14" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="210" y="54" font-size="42" fill="#fff" text-anchor="middle" id="t0">⚠ ATTENZIONE</text></g>
<text x="1040" y="190" font-size="76" fill="#fff" text-anchor="middle" {S} stroke-width="12" id="t1">PENSIONI 2027</text>
<text x="960" y="345" font-size="116" fill="url(#y)" text-anchor="middle" {S} stroke-width="16" id="t2">QUANTO HAI PERSO?</text>
<rect x="150" y="640" width="1620" height="14" rx="7" fill="#7DE8C4" fill-opacity=".5"/>
{card(300,2023,1)}{card(630,2024,2)}{card(960,2025,3)}{card(1290,2026,4)}{card(1620,2027,5,True)}
<g filter="url(#sh)"><rect x="310" y="900" width="1300" height="120" rx="60" fill="#fff" stroke="#FFD43B" stroke-width="10"/>
<text x="960" y="985" font-size="64" fill="#C0200F" text-anchor="middle" id="d1">E NEL 2027 <tspan fill="#0D5158">SI RIPETE?</tspan></text></g>
</svg>'''
open('fb7.html','w').write('<body style="margin:0">'+svg+'</body>')
