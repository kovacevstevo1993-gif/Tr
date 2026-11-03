S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
def row(y,w,col=None):
    d=f'<circle cx="70" cy="{y+17}" r="16" fill="{col}"/>' if col else '<circle cx="70" cy="%d" r="16" fill="#C9D6D8"/>'%(y+17)
    return d+f'<rect x="110" y="{y}" width="{w}" height="34" rx="8" fill="#0B1A1F"/>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0C7480"/><stop offset=".55" stop-color="#094A57"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#37C47E"/><stop offset="1" stop-color="#17895A"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="dots" width="48" height="48" patternUnits="userSpaceOnUse"><circle cx="24" cy="24" r="3" fill="#fff" fill-opacity=".08"/></pattern>
</defs>
<rect width="1920" height="1080" fill="url(#bg)"/><rect width="1920" height="1080" fill="url(#dots)"/>
<g transform="translate(90 60) rotate(-3)" filter="url(#sh)"><rect width="420" height="76" rx="14" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="210" y="54" font-size="42" fill="#fff" text-anchor="middle" id="t0">⚠ ATTENZIONE</text></g>
<text x="1030" y="190" font-size="88" fill="#fff" text-anchor="middle" {S} stroke-width="12" id="t1">PENSIONI</text>
<text x="960" y="350" font-size="150" fill="url(#y)" text-anchor="middle" {S} stroke-width="18" id="t2">NOVEMBRE</text>
<g transform="translate(150 400) rotate(-3)" filter="url(#sh)"><rect width="700" height="440" rx="26" fill="#FBFDFD"/>
<rect width="700" height="96" rx="26" fill="#0D5158"/><rect y="66" width="700" height="30" fill="#0D5158"/>
<text x="350" y="68" font-size="42" fill="#FFD43B" text-anchor="middle" id="c1">CEDOLINO · NOVEMBRE</text>
<g transform="translate(20 0)">{row(140,420)}{row(210,330,"#E0200F")}{row(280,380,"#1E9E5A")}{row(350,300)}</g></g>
<g transform="translate(930 410) rotate(2)" filter="url(#sh)"><rect width="860" height="190" rx="34" fill="url(#r)" stroke="#fff" stroke-width="6"/>
<text x="50" y="82" font-size="46" fill="#fff" id="a1">UNA VOCE ARRIVA</text><text x="50" y="148" font-size="44" fill="#FFE2DC" id="a2">E TOGLIE</text>
<text x="810" y="150" font-size="84" fill="#fff" text-anchor="end" id="a3">− ? €</text></g>
<g transform="translate(910 668) rotate(-2)" filter="url(#sh)"><rect width="860" height="190" rx="34" fill="url(#g)" stroke="#fff" stroke-width="6"/>
<text x="50" y="82" font-size="46" fill="#fff" id="b1">UNA VOCE FINISCE</text><text x="50" y="148" font-size="44" fill="#D9F5E6" id="b2">E LASCIA A TE</text>
<text x="810" y="150" font-size="84" fill="#fff" text-anchor="end" id="b3">+ ? €</text></g>
<g filter="url(#sh)"><rect x="210" y="910" width="1500" height="120" rx="60" fill="#fff" stroke="#FFD43B" stroke-width="10"/>
<text x="960" y="995" font-size="62" fill="#C0200F" text-anchor="middle" id="d1">COSA CAMBIA <tspan fill="#0D5158">NEL TUO CEDOLINO?</tspan></text></g>
</svg>'''
open('fb6.html','w').write('<body style="margin:0">'+svg+'</body>')
