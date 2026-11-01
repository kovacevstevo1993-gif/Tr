S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
def chip(x,n,col,t1,t2,fs=50):
    return f'''<g transform="translate({x} 730)"><rect width="310" height="270" rx="26" fill="#fff"/><circle cx="58" cy="58" r="42" fill="{col}" stroke="#fff" stroke-width="6"/><text x="58" y="82" font-size="62" fill="#fff" text-anchor="middle">{n}</text><text x="155" y="170" font-size="{fs}" fill="#0D5158" text-anchor="middle" id="t{n}">{t1}</text><text x="155" y="226" font-size="27" fill="#5B7479" text-anchor="middle" id="u{n}">{t2}</text></g>'''
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E7C86"/><stop offset=".5" stop-color="#0A5360"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<radialGradient id="spot" cx="78%" cy="55%" r="45%"><stop offset="0" stop-color="#7DE8C4" stop-opacity=".55"/><stop offset="1" stop-color="#7DE8C4" stop-opacity="0"/></radialGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="#fff" stroke-opacity=".06" stroke-width="2"/></pattern>
</defs>
<rect width="1920" height="1080" fill="url(#bg)"/><rect width="1920" height="1080" fill="url(#grid)"/>
<ellipse cx="1500" cy="600" rx="700" ry="620" fill="url(#spot)"/>
<g transform="translate(60 44) rotate(-1.5)" filter="url(#sh)"><rect width="640" height="80" rx="40" fill="url(#r)" stroke="#fff" stroke-width="6"/><text x="320" y="56" font-size="44" fill="#fff" text-anchor="middle" id="p1">⚠ PENSIONI 2027</text></g>
<text x="60" y="400" font-size="300" fill="url(#y)" {S} stroke-width="26" id="a1">IL 3%</text>
<text x="60" y="560" font-size="118" fill="#fff" {S} stroke-width="16" id="a2">NON È IL 3%!</text>
<g filter="url(#sh)"><rect x="60" y="600" width="1000" height="90" rx="20" fill="#08171C" stroke="#FFD43B" stroke-width="6"/><text x="560" y="662" font-size="52" fill="#FFD43B" text-anchor="middle" id="b1">LE 3 TRAPPOLE DELL'AUMENTO</text></g>
<g filter="url(#sh)">
{chip(60,1,"#1E9E5A","FASCE","100% · 90% · 75%",62)}
{chip(405,2,"#E0A100","TITOLI","LA % CHE LEGGI",62)}
{chip(750,3,"#E0200F","GENNAIO","IL CONGUAGLIO",48)}
</g>
<g filter="url(#sh)"><rect x="1130" y="100" width="730" height="250" rx="28" fill="#FBFDFD"/><rect x="1130" y="100" width="730" height="80" rx="28" fill="#0D5158"/><rect x="1130" y="150" width="730" height="30" fill="#0D5158"/>
<text x="1495" y="158" font-size="42" fill="#FFD43B" text-anchor="middle" id="c1">PENSIONE 4.000 € LORDI</text>
<text x="1170" y="285" font-size="44" fill="#0D5158" id="c2">AUMENTO</text>
<g fill="#0B1A1F"><rect x="1450" y="205" width="110" height="110" rx="18"/><rect x="1575" y="205" width="110" height="110" rx="18"/><rect x="1700" y="205" width="110" height="110" rx="18"/></g><g fill="#fff" font-size="90" text-anchor="middle"><text x="1505" y="295">?</text><text x="1630" y="295">?</text><text x="1755" y="295">?</text></g></g>
<g filter="url(#sh)">
<rect x="1130" y="440" width="230" height="540" rx="22" fill="#1E9E5A" stroke="#fff" stroke-width="6"/><text x="1245" y="740" font-size="62" fill="#fff" text-anchor="middle" id="d1">100%</text>
<rect x="1385" y="540" width="230" height="440" rx="22" fill="#E0A100" stroke="#fff" stroke-width="6"/><text x="1500" y="790" font-size="62" fill="#fff" text-anchor="middle" id="d2">90%</text>
<rect x="1640" y="640" width="220" height="340" rx="22" fill="#C0200F" stroke="#fff" stroke-width="6"/><text x="1750" y="840" font-size="62" fill="#fff" text-anchor="middle" id="d3">75%</text></g>
</svg>'''
open('fb.html','w').write('<body style="margin:0">'+svg+'</body>')
