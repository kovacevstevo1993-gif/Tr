S='stroke="#06242B" paint-order="stroke" stroke-linejoin="round"'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E7C86"/><stop offset=".55" stop-color="#0A5360"/><stop offset="1" stop-color="#041E27"/></linearGradient>
<radialGradient id="spot" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7DE8C4" stop-opacity=".5"/><stop offset="1" stop-color="#7DE8C4" stop-opacity="0"/></radialGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE777"/><stop offset="1" stop-color="#FFB400"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#010d11" flood-opacity=".7"/></filter>
<pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="#fff" stroke-opacity=".06" stroke-width="2"/></pattern>
</defs>
<rect width="1080" height="1920" fill="url(#bg)"/><rect width="1080" height="1920" fill="url(#grid)"/>
<ellipse cx="540" cy="1050" rx="620" ry="620" fill="url(#spot)"/>
<g transform="translate(300 290) rotate(-3)" filter="url(#sh)"><rect width="480" height="84" rx="14" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="240" y="60" font-size="50" fill="#fff" text-anchor="middle">⚠ ATTENZIONE</text></g>
<text x="540" y="520" font-size="104" fill="url(#y)" text-anchor="middle" {S} stroke-width="16" id="a1">PENSIONE 2027</text>
<text x="540" y="670" font-size="128" fill="#fff" text-anchor="middle" {S} stroke-width="18" id="a2">SALE L'ETÀ!</text>
<g transform="translate(90 740) rotate(-1.5)" filter="url(#sh)"><rect width="900" height="190" rx="28" fill="#E9F1F2"/>
<text x="50" y="58" font-size="40" fill="#5B7479" id="b1">OGGI · VECCHIAIA</text>
<text x="50" y="168" font-size="100" fill="#0D5158" id="b2">67 ANNI</text>
<circle cx="800" cy="95" r="60" fill="#B8C9CC"/><text x="800" y="123" font-size="80" fill="#fff" text-anchor="middle">✓</text></g>
<g transform="translate(540 990)"><polygon points="-70,-30 70,-30 0,50" fill="#E0200F" stroke="#fff" stroke-width="8" stroke-linejoin="round"/></g>
<g transform="translate(90 1070) rotate(1.5)" filter="url(#sh)"><rect width="900" height="330" rx="28" fill="#fff" stroke="#FFD43B" stroke-width="12"/>
<rect width="900" height="96" rx="28" fill="#0D5158"/><rect y="66" width="900" height="30" fill="#0D5158"/>
<text x="450" y="68" font-size="46" fill="#FFD43B" text-anchor="middle" id="c1">DAL 1° GENNAIO 2027</text>
<text x="50" y="250" font-size="96" fill="#0D5158" id="c2">67 ANNI +</text>
<circle cx="745" cy="205" r="100" fill="url(#y)" stroke="#fff" stroke-width="10"/>
<text x="745" y="215" font-size="96" fill="#08323A" text-anchor="middle" id="c3">?</text><text x="745" y="262" font-size="40" fill="#08323A" text-anchor="middle" id="c4">MESI</text></g>
<g filter="url(#sh)"><rect x="150" y="1480" width="780" height="130" rx="65" fill="url(#r)" stroke="#fff" stroke-width="8"/>
<text x="540" y="1568" font-size="72" fill="#fff" text-anchor="middle" id="d1">TU CI RIENTRI?</text></g>
</svg>'''
open('reel.html','w').write('<body style="margin:0">'+svg+'</body>')
