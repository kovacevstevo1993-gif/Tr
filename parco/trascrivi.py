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
        if r.status_code == 402: break
    return trascrivi_locale(path, lang)


_wm = None
def trascrivi_locale(path, lang="it"):
    """Whisper 'medium' in locale (gratis, faster-whisper): usato quando il saldo Pollinations è finito"""
    global _wm
    if _wm is None:
        from faster_whisper import WhisperModel
        _wm = WhisperModel("medium", device="cpu", compute_type="int8", download_root="/tmp/claude-0/whisper")
    import subprocess, numpy as np
    pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    seg, _ = _wm.transcribe(np.frombuffer(pcm, np.int16).astype(np.float32) / 32768, language=lang, beam_size=5)
    return " ".join(s.text.strip() for s in seg).strip()
if __name__ == "__main__":
    for p in sys.argv[1:]: print(p.split("/")[-1], "→", trascrivi(p))
