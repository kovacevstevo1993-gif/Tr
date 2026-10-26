#!/usr/bin/env python3
"""Guardia automatica (25/10/2026, ordine utente: "risolvilo", "devi eseguire solo i miei ordini"):
1) blocca l'invio di slide (mp4 in senior_advantage/) se il controllo colori da ERRORI;
2) blocca l'avvio di render slide Senior Advantage se non esiste il file .ordine-render (si crea SOLO dopo un ordine esplicito dell'utente e si cancella a fine render)."""
import json, os, re, subprocess, sys
ROOT = os.environ.get("CLAUDE_PROJECT_DIR", "/home/user/Tr")
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
tool = d.get("tool_name", ""); ti = d.get("tool_input", {}) or {}
if tool == "SendUserFile":
    mp4 = [f for f in ti.get("files", []) if f.lower().endswith(".mp4") and "senior_advantage" in os.path.abspath(f if os.path.isabs(f) else os.path.join(ROOT, f))]
    if mp4:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "senior_advantage/qa/qa_palette_slide.py")] + mp4, capture_output=True, text=True)
        if r.returncode != 0:
            print("BLOCCATO dalla guardia colori (regola 38): non mandare queste slide.\n" + r.stdout[-1500:], file=sys.stderr)
            sys.exit(2)
if tool == "Bash":
    cmd = ti.get("command", "")
    cmd = cmd.split("\n")[0]          # solo la prima riga: il testo dentro heredoc/echo non conta
    if not re.match(r"\s*(git|echo|grep|cat|sed|ls)\b", cmd) and re.search(r"runblocks9\.sh|long9_all\.py\s+\d", cmd) and not os.path.exists(os.path.join(ROOT, ".ordine-render")):
        print("BLOCCATO dalla guardia ordini (regola 39): render slide NON ordinato dall'utente. Se l'utente lo ha ordinato con parole esplicite, creare il file .ordine-render e riprovare; altrimenti non fare niente.", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
