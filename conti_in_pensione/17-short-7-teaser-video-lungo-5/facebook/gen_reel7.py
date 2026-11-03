S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E7C86"/><stop offset=".55" stop-color="#0A4F5C"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="rays" width="120" height="120" patternUnits="userSpaceOnUse" patternTransform="rotate(-20)"><rect width="60" height="120" fill="#fff" fill-opacity=".045"/></pattern>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/><rect width="1080" height="1920" fill="url(#rays)"/>
<g transform="translate(70 270) rotate(-3)" filter="url(#sh)"><rect width="420" height="76" rx="14" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="210" y="54" font-size="42" fill="#fff" text-anchor="middle" id="t0">⚠ ATTENZIONE</text></g>
<text x="540" y="500" font-size="72" fill="#fff" text-anchor="middle" {S} stroke-width="12" id="t1">PENSIONI</text>
<text x="540" y="640" font-size="108" fill="url(#y)" text-anchor="middle" {S} stroke-width="16" id="t2">TREDICESIMA</text>
<g transform="translate(180 720) rotate(2)" filter="url(#sh)"><rect width="720" height="640" rx="64" fill="#0B1A1F" stroke="#7DE8C4" stroke-width="6"/>
<rect x="28" y="28" width="664" height="584" rx="44" fill="#F4FAFA"/>
<rect x="28" y="28" width="664" height="110" rx="44" fill="#0D5158"/><rect x="28" y="90" width="664" height="48" fill="#0D5158"/>
<text x="360" y="100" font-size="44" fill="#FFD43B" text-anchor="middle" id="p1">DICEMBRE · BANCA</text>
<circle cx="110" cy="230" r="38" fill="#1E9E5A"/><path d="M92 230 l14 15 l26 -32" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
<text x="170" y="222" font-size="36" fill="#5B7479" id="p2">ACCREDITO INPS</text>
<text x="170" y="266" font-size="30" fill="#5B7479" id="p3">SU 1.000 € LORDI</text>
<rect x="90" y="330" width="540" height="190" rx="30" fill="#0B1A1F"/>
<text x="360" y="472" font-size="130" fill="url(#y)" text-anchor="middle" id="p4">+ ? €</text>
<text x="360" y="575" font-size="34" fill="#0D5158" text-anchor="middle" id="p5">NETTO IN BANCA</text></g>
<g filter="url(#sh)"><rect x="70" y="1450" width="940" height="140" rx="70" fill="#fff" stroke="#FFD43B" stroke-width="10"/>
<text x="540" y="1540" font-size="42" fill="#C0200F" text-anchor="middle" id="d1">ARRIVA MENO <tspan fill="#0D5158">DI QUANTO PENSI?</tspan></text></g>
</svg>'''
open('reel7.html','w').write('<body style="margin:0">'+svg+'</body>')
