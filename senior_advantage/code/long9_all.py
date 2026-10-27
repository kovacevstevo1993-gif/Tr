"""Video lungo 9 (ALDI) - tutti i 30 blocchi. Uso: OUT=cartella python3 long9_all.py <blocco>   |   python3 long9_all.py frame <blocco> <secondi> <file.png>"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long9_kit import *
DRAW = {}
for _m in ("long9_b01_10", "long9_b11_20", "long9_b21_30"):
    try:
        mod = __import__(_m)
    except ModuleNotFoundError as e:
        if _m not in str(e): raise
        continue
    for k, fn in mod.__dict__.items():
        if k.startswith("draw") and k[4:].isdigit() and getattr(fn, "__module__", "") == mod.__name__:
            DRAW[int(k[4:])] = fn

def _wrap(b, fn):
    def f(img, t):
        END[0] = DUR[b] / FPS
        fn(img, t)
    return f
DRAW = {b: _wrap(b, fn) for b, fn in DRAW.items()}

def render9(draw_fn, nframes, out):
    import subprocess
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes):
        t = i / FPS
        img = background9(t); draw_fn(img, t)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background9(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render9(DRAW[b], n, f"{out}/SA-aldi-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
