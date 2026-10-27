S='stroke="#08323A" paint-order="stroke" stroke-linejoin="round"'
def paper(x,y,rot,label,labcol,seal,sealcol,w=380,h=470):
    lines=''.join(f'<rect x="30" y="{150+i*34}" width="{w-60-(i%3)*40}" height="14" rx="7" fill="#C9D6D8"/>' for i in range(5))
    return f'''<g transform="translate({x} {y}) rotate({rot}) scale(.95)" filter="url(#sh)">
<rect width="{w}" height="{h}" rx="22" fill="#FFFFFF"/>
<rect width="{w}" height="104" rx="22" fill="{labcol}"/><rect y="70" width="{w}" height="34" fill="{labcol}"/>
<text x="{w/2}" y="72" font-size="54" fill="#fff" text-anchor="middle" {S} stroke-width="7">{label}</text>
{lines}
<circle cx="{w/2}" cy="365" r="68" fill="{sealcol}" stroke="#fff" stroke-width="8"/>
<text x="{w/2}" y="397" font-size="100" fill="#fff" text-anchor="middle">?</text></g>'''
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" style="font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:900">
<defs>
<radialGradient id="g" cx="40%" cy="45%" r="75%"><stop offset="0" stop-color="#22A3A0"/><stop offset=".55" stop-color="#0F6670"/><stop offset="1" stop-color="#062C35"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#9BEBB8" stop-opacity=".55"/><stop offset="1" stop-color="#9BEBB8" stop-opacity="0"/></radialGradient>
<linearGradient id="y" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE36B"/><stop offset="1" stop-color="#FFB81C"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A55"/><stop offset="1" stop-color="#C21808"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#021a20" flood-opacity=".6"/></filter>
</defs>
<rect width="1920" height="1080" fill="url(#g)"/>
<g opacity=".13" fill="#fff"><polygon points="760,540 0,0 330,0"/><polygon points="760,540 1100,0 1500,0"/><polygon points="760,540 1920,180 1920,520"/><polygon points="760,540 1920,900 1920,1080 1500,1080"/><polygon points="760,540 0,720 0,1010"/></g>
<ellipse cx="760" cy="520" rx="760" ry="460" fill="url(#glow)"/>
<g transform="translate(60 50) rotate(-3)" filter="url(#sh)"><rect width="560" height="96" rx="16" fill="url(#r)" stroke="#fff" stroke-width="5"/><text x="280" y="68" font-size="58" fill="#fff" text-anchor="middle">⚠ ATTENZIONE</text></g>
<text x="50" y="745" font-size="560" fill="url(#y)" letter-spacing="-26" {S} stroke-width="30" id="n64">64</text>
<text x="70" y="290" font-size="96" fill="#FFD43B" {S} stroke-width="14" id="t1">PENSIONE A</text>
<text x="830" y="672" font-size="170" fill="#fff" {S} stroke-width="20" id="t2">ANNI?</text>
<g filter="url(#sh)"><rect x="60" y="800" width="1060" height="190" rx="40" fill="#fff" stroke="#FFD43B" stroke-width="12"/>
<text x="590" y="887" font-size="84" fill="#C0200F" text-anchor="middle" id="l1">NON TI DICONO</text>
<text x="590" y="968" font-size="84" fill="#0D5158" text-anchor="middle" id="l2">LA VERITÀ!</text></g>
{paper(1440,60,-5,"LEGGE","#1E9E5A","#1E9E5A","#1E9E5A")}
{paper(1500,545,5,"PROPOSTA","#E0A100","#E0A100","#E0A100")}
<g transform="translate(1150 790) rotate(-8)" filter="url(#sh)"><rect width="250" height="250" rx="22" fill="#fff"/><rect width="250" height="72" rx="22" fill="#D8281A"/><rect y="40" width="250" height="32" fill="#D8281A"/><text x="125" y="56" font-size="40" fill="#fff" text-anchor="middle">ANNO</text><text x="125" y="190" font-size="78" fill="#0D5158" text-anchor="middle" id="y27">2027</text></g>
</svg>'''
open('orizz.html','w').write('<body style="margin:0">'+svg+'</body>')
