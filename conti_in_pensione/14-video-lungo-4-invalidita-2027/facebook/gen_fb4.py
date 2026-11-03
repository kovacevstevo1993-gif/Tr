S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
def card(x,name,i):
    return f'''<g transform="translate({x} 410)" filter="url(#sh)"><rect width="740" height="400" rx="34" fill="#FBFDFD"/>
<rect width="740" height="120" rx="34" fill="#0D5158"/><rect y="86" width="740" height="34" fill="#0D5158"/>
<text x="370" y="82" font-size="50" fill="#FFD43B" text-anchor="middle" id="n{i}">{name}</text>
<text x="370" y="190" font-size="40" fill="#5B7479" text-anchor="middle" id="s{i}">IL TUO AUMENTO A GENNAIO</text>
<rect x="150" y="225" width="440" height="140" rx="26" fill="#0B1A1F"/>
<text x="370" y="332" font-size="96" fill="#FFD43B" text-anchor="middle" id="v{i}">+ ? €</text></g>'''
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B6B75"/><stop offset=".6" stop-color="#0A4A57"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="dots" width="48" height="48" patternUnits="userSpaceOnUse"><circle cx="24" cy="24" r="3" fill="#fff" fill-opacity=".08"/></pattern>
</defs>
<rect width="1920" height="1080" fill="url(#bg)"/><rect width="1920" height="1080" fill="url(#dots)"/>
<g transform="translate(90 60) rotate(-3)" filter="url(#sh)"><rect width="420" height="76" rx="14" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="210" y="54" font-size="42" fill="#fff" text-anchor="middle" id="t0">⚠ ATTENZIONE</text></g>
<text x="960" y="170" font-size="76" fill="#fff" text-anchor="middle" {S} stroke-width="12" id="t1">PENSIONI 2027</text>
<text x="960" y="335" font-size="150" fill="url(#y)" text-anchor="middle" {S} stroke-width="18" id="t2">INVALIDITÀ</text>
{card(140,"ACCOMPAGNAMENTO",1)}{card(1040,"ASSEGNO MENSILE",2)}
<g filter="url(#sh)"><circle cx="960" cy="610" r="82" fill="url(#r)" stroke="#fff" stroke-width="8"/><text x="960" y="642" font-size="82" fill="#fff" text-anchor="middle" id="vs">VS</text></g>
<g filter="url(#sh)"><rect x="210" y="890" width="1500" height="120" rx="60" fill="#fff" stroke="#FFD43B" stroke-width="10"/>
<text x="960" y="975" font-size="64" fill="#C0200F" text-anchor="middle" id="d1">CHI PERDE <tspan fill="#0D5158">DAVVERO NEL 2027?</tspan></text></g>
</svg>'''
open('fb4.html','w').write('<body style="margin:0">'+svg+'</body>')
