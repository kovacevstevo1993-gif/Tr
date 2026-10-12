"""Video lungo 5 (AEROPORTO) - blocchi 16 in poi. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AEROPORTO.md.
Durate dalla timeline dell'utente (12/10/2026, fine blocco 15 = 5542): B16 285.
Uso: OUT=cartella python3 long5_b16_20.py <blocco> [fotogrammi]
     python3 long5_b16_20.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long5_b06_15 import *      # motore, icone, card, chip, banner, txt, seq, stamp

DUR = {16: 285, 17: 417, 18: 323, 19: 166, 20: 184}
PHRASES = {
    16: ["And the wheelchair service comes from the airline,", "not from T S A.", "People mix this up,",
         "then stand at the checkpoint", "wondering why nobody showed up."],
    17: ["Here's what many people don't know.", "The federal rule says an airline must not require advance notice",
         "for the services it is required to give you.", "So if you need help on the day,", "you are allowed to ask on the day."],
    18: ["Even so, ask when you book.", "A request in your reservation makes the day smoother.",
         "And you have to say that you need the help,", "because nobody at the airport will guess."],
    19: ["So say it plainly,", "at booking or at the counter.", "I need help from the curb to my gate."],
    20: ["Number three.", "Your cane, your walker, your wheelchair.", "They are not luggage."],
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

# ============================================================ BLOCCO 17
def draw17(img, t):
    ts = starts(17)
    common(img, t, "THE RULE")
    seq(img, t, ts[0], txt("WHAT MANY PEOPLE DON'T KNOW", 58, GOLD, 2), 960, 175, shadow=8)
    seq(img, t, ts[1], card(1500, 230, GOLD), 960, 370, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("scr17", 160, 200, lambda c: ic_scroll(c, 80, 100, 1.4)), 330, 370)
    seq(img, t, ts[1] + 0.4, txt("AN AIRLINE MUST NOT REQUIRE", 44, IVORY, 2), 1030, 330)
    seq(img, t, ts[1] + 0.7, txt("ADVANCE NOTICE", 78, GOLD, 3), 1030, 415)
    seq(img, t, ts[2], card(1500, 130, SAGE), 960, 590, shadow=12)
    seq(img, t, ts[2] + 0.3, txt("FOR THE SERVICES IT MUST GIVE YOU", 46, IVORY, 2), 960, 590)
    seq(img, t, ts[3], sprite("per17", 220, 260, lambda c: ic_person(c, 110, 130, 1.7, col=SAGE)), 330, 840, shadow=8)
    seq(img, t, ts[3] + 0.3, txt("NEED HELP", 44, IVORY, 2), 640, 810)
    seq(img, t, ts[3] + 0.5, txt("ON THE DAY", 44, GOLD, 2), 640, 870)
    p = ease(seg(t, ts[4], 0.8))
    if p > 0:
        put(img, sprite("arr17", 300, 80, lambda c: (c.line([(10, 40), (220, 40)], GOLD, 14), c.poly([(220, 8), (290, 40), (220, 72)], fill=GOLD))), 1000, 840, alpha=p)
    seq(img, t, ts[4] + 0.3, chip("YOU CAN ASK ON THE DAY", 720, 100, GREEN_OK, "ok", 38), 1470, 840, shadow=8)

# ============================================================ BLOCCO 18
def draw18(img, t):
    ts = starts(18)
    common(img, t, "EVEN SO")
    seq(img, t, ts[0], txt("ASK WHEN YOU BOOK", 66, GOLD, 3), 960, 175, shadow=8)
    seq(img, t, ts[1], card(820, 270, GOLD), 480, 430, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("ph18", 160, 220, lambda c: ic_phone(c, 80, 110, 1.6)), 220, 430)
    seq(img, t, ts[1] + 0.4, txt("A REQUEST IN", 38, IVORY, 2), 600, 380)
    seq(img, t, ts[1] + 0.6, txt("YOUR RESERVATION", 44, GOLD, 2), 600, 445)
    seq(img, t, ts[1] + 1.4, chip("A SMOOTHER DAY", 520, 90, GREEN_OK, "ok", 38), 480, 640, shadow=8)
    seq(img, t, ts[2], txt("SAY IT", 60, GOLD, 3), 1420, 280)
    seq(img, t, ts[2] + 0.3, bubble_spr(720, 150, IVORY, ["I NEED", "THE HELP"], DARK, 50), 1420, 470, shadow=10)
    seq(img, t, ts[3], sprite("off18", 220, 220, lambda c: ic_officer(c, 110, 110, 1.5)), 330, 870, shadow=8)
    seq(img, t, ts[3] + 0.3, chip("NOBODY WILL GUESS", 780, 100, RED, "x", 44), 1100, 870, shadow=8)

# ============================================================ BLOCCO 19
def draw19(img, t):
    ts = starts(19)
    common(img, t, "SAY IT")
    seq(img, t, ts[0], txt("SAY IT PLAINLY", 66, GOLD, 3), 960, 175, shadow=8)
    seq(img, t, ts[1], card(600, 240, SAGE), 520, 420, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("ph19", 160, 220, lambda c: ic_phone(c, 80, 110, 1.5)), 330, 420)
    seq(img, t, ts[1] + 0.4, txt("AT BOOKING", 44, IVORY, 2), 640, 420)
    seq(img, t, ts[1] + 0.8, card(600, 240, GOLD), 1400, 420, shadow=12)
    seq(img, t, ts[1] + 1.0, sprite("bag19", 200, 200, lambda c: ic_suitcase(c, 100, 100, 1.1)), 1210, 420)
    seq(img, t, ts[1] + 1.2, txt("AT THE COUNTER", 36, IVORY, 2), 1500, 420)
    seq(img, t, ts[2], bubble_spr(1300, 200, IVORY, ["I NEED HELP FROM", "THE CURB TO MY GATE"], DARK, 64), 960, 770, shadow=12)

# ============================================================ BLOCCO 20
def draw20(img, t):
    ts = starts(20)
    common(img, t, "YOUR CANE")
    show_badge(img, t, 3)
    items = [("YOUR CANE", sprite("cane20", 220, 260, lambda c: ic_cane(c, 110, 130, 1.6)), 360),
             ("YOUR WALKER", walker(), 960),
             ("YOUR WHEELCHAIR", sprite("wc20", 220, 260, lambda c: ic_wheelchair(c, 112, 132, 1.0)), 1560)]
    for k, (name, spr, x) in enumerate(items):
        t0 = ts[1] + k * 1.0
        seq(img, t, t0, card(480, 400, SAGE), x, 430, shadow=12)
        seq(img, t, t0 + 0.2, spr, x, 400, shadow=6)
        seq(img, t, t0 + 0.4, txt(name, 36, GOLD, 2), x, 570)
    seq(img, t, ts[2], sprite("bag20", 200, 200, lambda c: (ic_suitcase(c, 100, 100, 1.3), ic_x(c, 100, 100, 1.5, RED, 16))), 620, 860, shadow=8)
    s, a, p = pop(t, ts[2] + 0.2, 0.5)
    if p > 0:
        put(img, stamp("NOT LUGGAGE", 760, 110, RED, size=56), 1180, 860, scale=s, alpha=a, rot=-3, shadow=10)

DRAW = {16: draw16, 17: draw17, 18: draw18, 19: draw19, 20: draw20}

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
