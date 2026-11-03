#!/usr/bin/env python3
"""Stampa il copione GIA' nel formato della chat (titolo, **Blocco N**, riquadro ```), prendendo il testo dal FILE.
Regola 28/10/2026 (errore: 'rrientri' scritto a mano in chat mentre il file era giusto): il copione in chat si COPIA dall'output
di questo script, mai riscritto a mano. Uso: python3 qa/chat_copione.py <cartella>/copione-blocchi.txt "SHORT 15 – Teaser video lungo 12 (v9)" """
import re,sys
f=sys.argv[1]; titolo=sys.argv[2] if len(sys.argv)>2 else 'COPIONE'
print(f'**{titolo}**\n')
for l in open(f,encoding='utf-8'):
    m=re.match(r'^(\d+)\|\s*(.+)$',l.strip())
    if m: print(f'**Blocco {m.group(1)}**\n```\n{m.group(2)}\n```\n')
