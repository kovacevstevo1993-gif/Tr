#!/usr/bin/env python3
"""Ascolta un file audio con Pollinations (whisper) -> testo. Serve a controllare la pronuncia delle voci."""
import requests, sys
def trascrivi(path, model="openai/whisper-large-v3", lang="it"):
    for n in range(4):
        r = requests.post("https://gen.pollinations.ai/v1/audio/transcriptions",
            data={"model": model, "language": lang, "response_format": "json"},
            files={"file": (path.split("/")[-1], open(path, "rb"), "audio/wav")}, timeout=120)
        if r.status_code == 200: return r.json().get("text", "").strip()
        err = f"HTTP {r.status_code} {r.text[:150]}"
    return err
if __name__ == "__main__":
    for p in sys.argv[1:]: print(p.split("/")[-1], "→", trascrivi(p))
