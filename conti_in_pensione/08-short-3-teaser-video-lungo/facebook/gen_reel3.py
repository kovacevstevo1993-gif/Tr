S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
def bar(y,w,i): return f'<rect x="60" y="{y}" width="{w}" height="34" rx="8" fill="#0B1A1F"/><rect x="800" y="{y-8}" width="50" height="50" rx="10" fill="#fff" stroke="#9FB4B8" stroke-width="5"/>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0C7480"/><stop offset=".6" stop-color="#094A57"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="stripes" width="60" height="60" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><rect width="30" height="60" fill="#fff" fill-opacity=".04"/></pattern>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/><rect width="1080" height="1920" fill="url(#stripes)"/>
<g transform="translate(560 270) rotate(3)" filter="url(#sh)"><rect width="440" height="76" rx="14" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="220" y="54" font-size="42" fill="#fff" text-anchor="middle" id="t0">⚠ ATTENZIONE</text></g>
<text x="540" y="470" font-size="96" fill="#fff" text-anchor="middle" {S} stroke-width="14" id="t1">NON LASCIARE</text>
<text x="540" y="580" font-size="96" fill="#fff" text-anchor="middle" {S} stroke-width="14" id="t2">IL LAVORO</text>
<text x="540" y="720" font-size="124" fill="url(#y)" text-anchor="middle" {S} stroke-width="16" id="t3">A 64 ANNI?</text>
<g transform="translate(80 800) rotate(-2)" filter="url(#sh)"><rect width="920" height="520" rx="30" fill="#FBFDFD"/>
<rect width="920" height="110" rx="30" fill="#0D5158"/><rect y="80" width="920" height="30" fill="#0D5158"/>
<text x="460" y="76" font-size="44" fill="#FFD43B" text-anchor="middle" id="b1">PENSIONE A 64 ANNI · 2027</text>
<g transform="translate(30 0)">{bar(190,640,1)}{bar(290,500,2)}{bar(390,580,3)}</g>
<g transform="translate(640 330) rotate(-12)"><circle r="95" fill="#fff" stroke="#E0200F" stroke-width="14"/><text y="52" font-size="140" fill="#E0200F" text-anchor="middle" id="b2">?</text></g>
</g>
<g filter="url(#sh)"><rect x="70" y="1410" width="940" height="130" rx="65" fill="#fff" stroke="#FFD43B" stroke-width="10"/>
<text x="540" y="1498" font-size="40" fill="#C0200F" text-anchor="middle" id="d1">PRIMA DI FIRMARE, <tspan fill="#0D5158">GUARDA QUESTO</tspan></text></g>
</svg>'''
open('reel3.html','w').write('<body style="margin:0">'+svg+'</body>')
