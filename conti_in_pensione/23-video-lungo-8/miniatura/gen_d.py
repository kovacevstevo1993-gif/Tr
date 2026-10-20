# Miniatura D (21/10): CURIOSITA' (ordine utente: "non ci cliccano, non e' abbastanza curiosa"): paese COPERTO, domanda 0 € di tasse, +5.100 € l'anno
import os,re
src=open('gen.py').read();exec(src[:src.index('# A:')])
D=HEAD+f"""<circle cx="930" cy="330" r="320" fill="#FFD43B" opacity="0.16" filter="url(#gl)"/>
<g class="t" {S} stroke-width="20"><text id="a1" x="34" y="132" font-size="128" fill="#fff">PENSIONE</text></g>
{blocco(38,160,560,104,"0 € DI TASSE?",74,"#FFD43B","#0D2A2F",-2)}
<g class="t" {S} stroke-width="22"><text id="a3" x="34" y="418" font-size="122" fill="#3FE0A6">+5.100 €</text></g>
<g class="t" {S} stroke-width="12"><text id="a4" x="44" y="490" font-size="54" fill="#fff">IN PIÙ OGNI ANNO</text></g>
{blocco(40,520,540,74,"ATTENTO A 3 TRAPPOLE",36,"#E0402A","#fff",-3)}
{flag('IT',890,92,120,-8)}
<path d="M955 110 Q1060 110 1075 205" fill="none" stroke="#FFD43B" stroke-width="9" stroke-dasharray="16 12" stroke-linecap="round"/>
<g transform="translate(940 380) rotate(6)" filter="url(#sh)"><rect x="-230" y="-155" width="460" height="310" rx="24" fill="#2C6E73" stroke="#fff" stroke-width="12"/><rect x="-216" y="-141" width="432" height="70" rx="14" fill="#fff" fill-opacity=".12"/>
<text id="q" x="0" y="95" class="t" font-size="270" fill="#FFD43B" text-anchor="middle" stroke="#06282C" stroke-width="16" paint-order="stroke">?</text></g>
"""+STRIP('IN QUALE PAESE? <tspan fill="#0D5158">IL CONTO VERO</tspan>')+END
open('miniatura-D.html','w').write(D)
