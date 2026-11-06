#!/usr/bin/env python3
"""GUARDIA ORDINI - THE MONEY BACKSTORY (06/11/2026, ordine utente: "Crea" dopo "devi eseguire solo i miei ordini... ogni chat devo sempre ripetere le stesse cose").
Il sistema (non la mia memoria) impedisce le iniziative:
- modo `prompt` (UserPromptSubmit): ad ogni messaggio dell'utente decide se e' un ORDINE (verbo di ordine, senza '?' e senza parole di stop) e scrive/cancella i flag della sessione:
    ordine  -> flag 'ordine' (lavori pesanti permessi: voce, render, pacchetto, miniature, consegna)
    ordine + parola 'vidiq' o 'ricerche' -> anche flag 'vidiq' (crediti vidIQ permessi)
    domanda / critica / stop ('fermati', 'non cambiare', 'basta', 'aspetta') -> TUTTI i flag cancellati
- modo `guard` (PreToolUse su Bash, SendUserFile, strumenti vidIQ): senza flag NEGA l'avvio di voce Gemini, render, pacchetto, miniature, unione/consegna e ogni strumento vidIQ a pagamento.
Resta sempre permesso: leggere, anteprime, controlli, commit/push delle regole. I lavori gia' avviati in background non vengono uccisi."""
import json, os, re, sys
modo = sys.argv[1] if len(sys.argv) > 1 else 'prompt'
try: d = json.load(sys.stdin)
except Exception: d = {}
sid = str(d.get('session_id', 'x')); base = '/tmp/money_ordini'; os.makedirs(base, exist_ok=True)
F_ORD = os.path.join(base, 'ordine-' + sid); F_VID = os.path.join(base, 'vidiq-' + sid)
ORDINI = r"\b(crea|creiamo|creare|fai|fallo|falla|facciamo|fammi|rifai|rifallo|procedi|prosegui|continua|vai|avanti|genera|lancia|renderizza|monta|consegna|manda|mandami|mandalo|invia|scrivi|scrivimi|aggiungi|metti|mettilo|correggi|correggilo|cambia|cambialo|salva|salvalo|togli|toglilo|sistema|sistemalo|elimina|cancella|ordino|controlla|cerca|cercami|verifica|applica|usa)\b"
STOP = r"(non\s+(cambi|cambiare|fare|fai|toccare|tocchi|creare|crei|rifare|rifai|mandare|mandi)|fermati|\bstop\b|\bbasta\b|aspetta|non\s+iniziare)"
cwd = str(d.get('cwd', ''))
MARK = os.path.join(base, 'attivo-' + sid)
if modo == 'prompt':
    p = str(d.get('prompt', ''))
    if 'money_backstory' in cwd or re.search(r"money\s*backstory|money_backstory", p, re.I): open(MARK, 'w').write('1')
    ordine = bool(re.search(ORDINI, p, re.I)) and '?' not in p and not re.search(STOP, p, re.I)
    for f in (F_ORD, F_VID):
        if os.path.exists(f): os.remove(f)
    if not os.path.exists(MARK): sys.exit(0)
    if ordine:
        open(F_ORD, 'w').write('1')
        if re.search(r"vidiq|ricerch", p, re.I): open(F_VID, 'w').write('1')
        print("=== GUARDIA ORDINI (Money Backstory): ORDINE rilevato. Fai SOLO quello che l'utente ha ordinato, nell'ordine giusto. Miniature, pacchetto e vidIQ solo se ordinati e solo a video finito. ===")
    else:
        print("=== GUARDIA ORDINI (Money Backstory): questo messaggio NON e' un ordine (domanda, critica o stop). Rispondi in 1-2 righe. VIETATO avviare voce, render, pacchetto, miniature, vidIQ, consegne: il sistema li blocca finche' l'utente non scrive un ordine. ===")
    sys.exit(0)
# ---- guard ----
tool = str(d.get('tool_name', '')); ti = d.get('tool_input', {}) or {}
if not os.path.exists(MARK) and 'money_backstory' not in cwd + str(ti.get('command', '')) + ' '.join(str(f) for f in ti.get('files', [])): sys.exit(0)
if tool.startswith('mcp__vidIQ__'):
    GRATIS = ('balance', 'user_channels', 'get_profile', 'bookmarks_list', 'jobs_list', 'job_poll')
    if not any(g in tool for g in GRATIS) and not os.path.exists(F_VID):
        sys.stderr.write("BLOCCATO dalla guardia ordini: vidIQ costa crediti e l'utente non l'ha ordinato in questo messaggio (serve un ordine con la parola 'vidiq' o 'ricerche').")
        sys.exit(2)
    sys.exit(0)
if os.path.exists(F_ORD): sys.exit(0)
if tool == 'SendUserFile':
    fs = [str(f) for f in ti.get('files', [])]
    if any('money_backstory' in os.path.abspath(f) for f in fs):
        sys.stderr.write("BLOCCATO dalla guardia ordini (Money Backstory): consegna di file non ordinata dall'utente."); sys.exit(2)
if tool == 'Bash':
    c = str(ti.get('command', '')).split('\n')[0]
    if re.match(r"\s*(git|echo|grep|cat|sed|ls|head|tail|wc|python3 -c|ffprobe)\b", c): sys.exit(0)
    PESANTI = r"gen2\.sh|voce_all\.sh|tts1\.py|gen\.sh|\bv\d+\.py\s+render|v\d+(?:b\d+_\d+)?\.py\s+render|xargs.*render|mkpack\.py|thumbs_video\d+\.py|unisci\.py|pad\.py|ritaglia\d*\.py|make_sync\.py"
    if re.search(PESANTI, c):
        sys.stderr.write("BLOCCATO dalla guardia ordini (Money Backstory): voce, render, pacchetto, miniature o consegna NON ordinati dall'utente in questo messaggio. Non fare niente finche' non c'e' un ordine.")
        sys.exit(2)
sys.exit(0)
