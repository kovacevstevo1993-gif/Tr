#!/usr/bin/env python3
"""Sottotitoli italiani .srt/.txt per lo Short 'La mongolfiera dei quattro amici' (tempi dalle voci)."""
import short_mongolfiera as R

def ts(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

rows = sorted(R.VOICES, key=lambda r: r[1])
with open("sottotitoli_mongolfiera.it.srt", "w", encoding="utf-8") as f:
    for i, (k, t0, who, txt, d) in enumerate(rows, 1):
        end = t0 + d + 0.15
        if i < len(rows): end = min(end, rows[i][1] - 0.02)
        f.write(f"{i}\n{ts(t0)} --> {ts(end)}\n{txt}\n\n")
with open("sottotitoli_mongolfiera.it.txt", "w", encoding="utf-8") as f:
    for k, t0, who, txt, d in rows: f.write(txt + "\n")
print("ok", len(rows))
