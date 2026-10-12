#!/usr/bin/env python3
"""Controllo pronuncia: trascrive un audio con Gemini (gratis). Uso: trascrivi_gemini.py file [modello]"""
import json, base64, sys, urllib.request, mimetypes
def trascrivi(path, model="gemini-3.8-flash"):
    mt = "audio/wav" if path.endswith(".wav") else "audio/mp3"
    b = base64.b64encode(open(path, "rb").read()).decode()
    body = {"contents": [{"parts": [{"inlineData": {"mimeType": mt, "data": b}},
            {"text": "Trascrivi parola per parola, in italiano, esattamente come viene pronunciato (anche se ci sono errori di pronuncia). Solo la trascrizione."}]}]}
    r = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                               data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(r, timeout=180)); return d["candidates"][0]["content"]["parts"][0]["text"].strip()
if __name__ == "__main__":
    m = sys.argv[2] if len(sys.argv) > 2 else "gemini-3.8-flash"
    print(sys.argv[1], m, "->", trascrivi(sys.argv[1], m))
