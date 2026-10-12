"""Video lungo 5 (AEROPORTO) - blocchi 16 in poi. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AEROPORTO.md.
Durate dalla timeline dell'utente (12/10/2026, fine blocco 15 = 5542): B16 285.
Uso: OUT=cartella python3 long5_b16_20.py <blocco> [fotogrammi]
     python3 long5_b16_20.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long5_b06_15 import *      # motore, icone, card, chip, banner, txt, seq, stamp

DUR = {16: 285}
PHRASES = {
    16: ["And the wheelchair service comes from the airline,", "not from T S A.", "People mix this up,",
         "then stand at the checkpoint", "wondering why nobody showed up."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def ic_wheelchair(c, cx, cy, s):
    c.ell((cx - 62 * s, cy - 8 * s, cx + 28 * s, cy + 82 * s), outline=IVORY, width=int(10 * s))
    c.ell((cx - 22 * s, cy + 32 * s, cx - 12 * s, cy + 42 * s), fill=IVORY)
    c.ell((cx + 34 * s, cy + 60 * s, cx + 62 * s, cy + 88 * s), outline=IVORY, width=int(8 * s))
    c.line([(cx - 40 * s, cy - 50 * s), (cx - 40 * s, cy + 26 * s), (cx + 40 * s, cy + 26 * s), (cx + 56 * s, cy + 70 * s)], IVORY, int(10 * s))
    c.line([(cx - 40 * s, cy - 50 * s), (cx - 56 * s, cy - 56 * s)], IVORY, int(10 * s))
    c.ell((cx - 58 * s, cy - 92 * s, cx - 28 * s, cy - 62 * s), fill=GOLD)

# ============================================================ BLOCCO 16
def draw16(img, t):
    ts = starts(16)
    common(img, t, "HELP AT THE AIRPORT")
    seq(img, t, ts[0], card(780, 300, GOLD), 520, 400, shadow=12)
    seq(img, t, ts[0] + 0.2, sprite("wc16c", 220, 220, lambda c: ic_wheelchair(c, 118, 112, 0.95)), 275, 400)
    seq(img, t, ts[0] + 0.4, txt("THE AIRLINE", 52, GOLD, 2), 710, 345)
    seq(img, t, ts[0] + 0.6, txt("WHEELCHAIR SERVICE", 30, IVORY, 1), 710, 415)
    seq(img, t, ts[0] + 0.8, sprite("pl16", 140, 100, lambda c: ic_plane(c, 70, 50, 1.0)), 440, 400, scale=0.8)
    seq(img, t, ts[1], card(780, 300, SAGE), 1400, 400, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("off16", 220, 220, lambda c: ic_officer(c, 110, 110, 1.5)), 1170, 400)
    seq(img, t, ts[1] + 0.4, txt("T S A", 64, GOLD, 3), 1520, 350)
    seq(img, t, ts[1] + 0.7, chip("NOT T S A", 400, 84, RED, "x", 38), 1520, 465, shadow=8)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, stamp("PEOPLE MIX THIS UP", 760, 100, RED, size=48), 960, 650, scale=s, alpha=a, rot=-3, shadow=10)
    seq(img, t, ts[3], sprite("per16", 220, 260, lambda c: ic_person(c, 110, 130, 1.7, col=SAGE)), 330, 880, shadow=8)
    seq(img, t, ts[3] + 0.3, txt("AT THE CHECKPOINT", 40, SAGE, 2), 700, 880)
    seq(img, t, ts[4], bubble_spr(760, 150, IVORY, ["WHY DID NOBODY", "SHOW UP?"], DARK, 46), 1430, 855, shadow=10)

DRAW = {16: draw16}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/V5-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
