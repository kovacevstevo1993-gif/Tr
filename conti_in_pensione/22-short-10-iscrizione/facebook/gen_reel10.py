S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
def bar(y,w): return f'<circle cx="80" cy="{y+17}" r="14" fill="#C9D6D8"/><rect x="120" y="{y}" width="{w}" height="34" rx="8" fill="#0B1A1F"/>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B6B75"/><stop offset=".6" stop-color="#0A4A57"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="#fff" stroke-opacity=".06" stroke-width="2"/></pattern>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/><rect width="1080" height="1920" fill="url(#grid)"/>
<text x="540" y="400" font-size="62" fill="#fff" text-anchor="middle" {S} stroke-width="10" id="t0">CEDOLINO</text>
<text x="540" y="545" font-size="136" fill="url(#y)" text-anchor="middle" {S} stroke-width="16" id="t1">PENSIONE</text>
<g transform="translate(110 640) rotate(-3)" filter="url(#sh)"><rect width="640" height="520" rx="28" fill="#FBFDFD"/>
<rect width="640" height="90" rx="28" fill="#0D5158"/><rect y="60" width="640" height="30" fill="#0D5158"/>
<text x="320" y="64" font-size="38" fill="#FFD43B" text-anchor="middle" id="c1">IL TUO CEDOLINO</text>
{bar(140,420)}{bar(215,340)}{bar(290,400)}{bar(365,300)}{bar(440,380)}</g>
<g transform="translate(640 960)" filter="url(#sh)"><circle r="190" fill="#fff" fill-opacity=".92" stroke="#FFD43B" stroke-width="22"/>
<text y="45" font-size="110" fill="#C0200F" text-anchor="middle" id="m1">− ? €</text>
<path d="M135 135 L300 300" stroke="#FFD43B" stroke-width="44" stroke-linecap="round"/></g>
<g filter="url(#sh)"><rect x="70" y="1330" width="940" height="130" rx="65" fill="#fff" stroke="#FFD43B" stroke-width="10"/>
<text x="540" y="1415" font-size="40" fill="#C0200F" text-anchor="middle" id="d1">DOVE SPARISCONO <tspan fill="#0D5158">I TUOI SOLDI?</tspan></text></g>
<g transform="translate(150 1500) rotate(-2)" filter="url(#sh)"><rect width="780" height="110" rx="55" fill="url(#r)" stroke="#fff" stroke-width="6"/><text x="390" y="74" font-size="44" fill="#fff" text-anchor="middle" id="d2">IL CONTO VERO, GRATIS</text></g>
</svg>'''
open('reel10.html','w').write('<body style="margin:0">'+svg+'</body>')
