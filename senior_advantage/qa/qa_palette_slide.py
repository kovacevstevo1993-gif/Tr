"""Controllo colori slide Senior Advantage (regola 38): sfondo verde bosco come Walmart, niente blu/viola nelle schede.
Uso: python3 qa_palette_slide.py <video.mp4> [altri.mp4 ...]   -> stampa OK o ERRORI per ogni file (se ERRORI non si manda)."""
import sys, subprocess, io
import numpy as np
from PIL import Image

def frames(path):
    out = []
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip() or 1)
    for k in (0.3, 0.6, 0.9):
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", str(dur * k), "-i", path, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
        out.append(np.asarray(Image.open(io.BytesIO(raw)).convert("RGB")).astype(int))
    return out

def check(path):
    err = []
    for i, a in enumerate(frames(path)):
        strip = a[1000:1080, :, :].reshape(-1, 3)
        r, g, b = np.median(strip, axis=0)
        if not (r < 28 and 30 <= g <= 75 and 0.68 <= b / g <= 0.92):
            err.append("fotogramma %d: sfondo (%d,%d,%d) non e verde bosco Walmart (circa 9,39,32 / 17,56,43)" % (i + 1, r, g, b))
        R, G, B = a[..., 0], a[..., 1], a[..., 2]
        bluish = ((B > G + 25) & (B > R + 25)).mean() * 100
        purple = ((R > G + 25) & (B > G + 25)).mean() * 100
        if bluish > 0.3 or purple > 0.3:
            err.append("fotogramma %d: colori blu/viola fuori palette (blu %.2f%%, viola %.2f%%)" % (i + 1, bluish, purple))
    return err

if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        e = check(p)
        print(("OK      " if not e else "ERRORI  ") + p)
        for x in e: print("   ", x)
        bad += bool(e)
    sys.exit(1 if bad else 0)
