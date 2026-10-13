"""Video lungo 5 (AEROPORTO) - blocchi 21-30. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AEROPORTO.md.
Durate dalla timeline dell'utente (12/10/2026, fine blocco 20 = 6917): B21 459, B22 235, B23 324, B24 200, B25 356, B26 131, B27 345, B28 341, B29 284, B30 328.
Uso: OUT=cartella python3 long5_b21_30.py <blocco> [fotogrammi]
     python3 long5_b21_30.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long5_b16_20 import *      # motore, icone, card, chip, banner, txt, seq, stamp, ic_wheelchair

DUR = {21: 459, 22: 235, 23: 324, 24: 200, 25: 356, 26: 131, 27: 345, 28: 341, 29: 284, 30: 328}
PHRASES = {
    21: ["The federal rule says airlines must not count these toward your carry on limit.", "Canes, crutches, walkers, a folding wheelchair.",
         "As long as they fit in the priority storage area, the overhead bin, or under a seat."],
    22: ["The common mistake is paying a bag fee,", "or arguing at the gate about the carry on limit,", "for something that was never supposed to count."],
    23: ["And if your wheelchair or mobility device has to be taken apart to be stored,", "the airline must put it back together,",
         "and return it promptly,", "in the condition it was received."],
    24: ["If it comes back damaged,", "take a photo before you leave,", "and report it to the airline right there at the airport."],
    25: ["So, who does this help?", "Anyone who flies with a cane or a walker.", "Your action is one sentence at the gate.",
         "This is my mobility aid, it doesn't count as my carry on."],
    26: ["Number four.", "One of only two things on this list that need advance notice."],
    27: ["If you use a portable oxygen concentrator, a ventilator, a respirator, or a C P A P machine on the plane,",
         "federal rules let the airline ask you for forty eight hours notice."],
    28: ["That is the exception, not the rule.", "And here's the mistake.", "People arrive with the machine, assume it's allowed,",
         "and learn at the gate that the airline needed to know two days earlier."],
    29: ["Not every airline allows every oxygen model, either.", "T S A says to check with your airline and the maker of your device before you fly."],
    30: ["Who does this help?", "Anyone who sleeps with a machine, or breathes with help.", "Your action is a phone call when you book.",
         "Ask, what do you need from me, and by when?"],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def ic_crutch(c, cx, cy, s):
    c.line([(cx - 20 * s, cy - 70 * s), (cx + 10 * s, cy + 80 * s)], (214, 164, 96), 10 * s)
    c.line([(cx - 44 * s, cy - 40 * s), (cx + 6 * s, cy - 40 * s)], (214, 164, 96), 10 * s)
    c.rrect((cx - 34 * s, cy - 76 * s, cx + 4 * s, cy - 56 * s), 6, fill=GOLD)

def ic_camera(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy - 40 * s, cx + 70 * s, cy + 50 * s), 14 * s, fill=IVORY, outline=SAGE_D, width=4)
    c.rrect((cx - 30 * s, cy - 58 * s, cx + 20 * s, cy - 38 * s), 6, fill=IVORY)
    c.ell((cx - 34 * s, cy - 24 * s, cx + 34 * s, cy + 44 * s), fill=GREEN_D, outline=GOLD, width=6)
    c.ell((cx - 14 * s, cy - 4 * s, cx + 14 * s, cy + 24 * s), fill=(110, 176, 200))

def ic_mask(c, cx, cy, s):
    c.ell((cx - 44 * s, cy - 40 * s, cx + 44 * s, cy + 40 * s), fill=(110, 176, 200), outline=IVORY, width=5)
    c.ell((cx - 18 * s, cy - 14 * s, cx + 18 * s, cy + 22 * s), fill=IVORY)
    c.line([(cx - 44 * s, cy), (cx - 76 * s, cy - 30 * s)], IVORY, 7 * s)
    c.line([(cx + 44 * s, cy), (cx + 76 * s, cy - 30 * s)], IVORY, 7 * s)

def mini(name, fn, x, y, t, t0, border=SAGE, w=400, h=300, size=34, col=GOLD):
    seq(img_ref[0], t, t0, card(w, h, border), x, y, shadow=12)
    seq(img_ref[0], t, t0 + 0.2, sprite(("mn", name), 240, 200, lambda c: fn(c, 120, 100, 1.0)), x, y - 30, shadow=6)
    seq(img_ref[0], t, t0 + 0.4, txt(name, size, col, 1), x, y + h / 2 - 40)
img_ref = [None]

# ============================================================ BLOCCO 21
def draw21(img, t):
    img_ref[0] = img
    ts = starts(21)
    common(img, t, "CARRY ON LIMIT")
    seq(img, t, ts[0], card(1500, 200, GOLD), 960, 270, shadow=12)
    seq(img, t, ts[0] + 0.2, sprite("scr21", 160, 200, lambda c: ic_scroll(c, 80, 100, 1.4)), 330, 270)
    seq(img, t, ts[0] + 0.4, txt("AIRLINES MUST NOT COUNT THESE", 44, GOLD, 2), 1030, 235)
    seq(img, t, ts[0] + 0.7, txt("TOWARD YOUR CARRY ON LIMIT", 44, IVORY, 2), 1030, 310)
    items = [("CANES", ic_cane), ("CRUTCHES", ic_crutch), ("WALKERS", lambda c, x, y, s: ic_person(c, x, y, 1.1 * s, col=SAGE)),
             ("FOLDING WHEELCHAIR", lambda c, x, y, s: ic_wheelchair(c, x, y + 10, 0.85 * s))]
    for k, (nm, fn) in enumerate(items):
        mini(nm, fn, 300 + k * 440, 590, t, ts[1] + k * 0.7, size=30 if k == 3 else 36)
    for k, nm in enumerate(["PRIORITY STORAGE AREA", "OVERHEAD BIN", "UNDER A SEAT"]):
        seq(img, t, ts[2] + k * 0.9, chip(nm, 560, 90, GREEN_OK, "ok", 32), 330 + k * 630, 900, shadow=8)

# ============================================================ BLOCCO 22
def draw22(img, t):
    ts = starts(22)
    common(img, t, "THE COMMON MISTAKE")
    seq(img, t, ts[0], card(800, 320, RED), 500, 400, shadow=12)
    seq(img, t, ts[0] + 0.2, sprite("bag22", 220, 220, lambda c: ic_suitcase(c, 110, 110, 1.4)), 290, 400)
    seq(img, t, ts[0] + 0.4, sprite("coin22", 160, 160, lambda c: (c.ell((10, 10, 150, 150), fill=GOLD, outline=(168, 118, 40), width=6), c.text((80, 84), "$", FONT_SANS, 90, GREEN_D))), 470, 330)
    seq(img, t, ts[0] + 0.6, txt("PAYING A", 44, IVORY, 2), 660, 380)
    seq(img, t, ts[0] + 0.8, txt("BAG FEE", 64, GOLD, 2), 660, 450)
    seq(img, t, ts[1], card(800, 320, RED), 1420, 400, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("per22", 200, 240, lambda c: ic_person(c, 100, 120, 1.6, col=SAGE)), 1190, 410)
    seq(img, t, ts[1] + 0.5, txt("ARGUING AT THE GATE", 38, GOLD, 2), 1520, 370)
    seq(img, t, ts[1] + 0.7, txt("ABOUT THE CARRY ON LIMIT", 30, IVORY, 1), 1520, 440)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, stamp("NEVER SUPPOSED TO COUNT", 1100, 120, GREEN_OK, size=56), 960, 800, scale=s, alpha=a, rot=-2, shadow=10)

# ============================================================ BLOCCO 23
def draw23(img, t):
    ts = starts(23)
    common(img, t, "TAKEN APART")
    seq(img, t, ts[0], card(560, 340, SAGE), 330, 370, shadow=12)
    seq(img, t, ts[0] + 0.2, sprite("wcA23", 200, 240, lambda c: ic_wheelchair(c, 100, 120, 0.9)), 230, 360)
    seq(img, t, ts[0] + 0.4, sprite("wcB23", 200, 240, lambda c: (c.ell((30, 110, 130, 210), outline=IVORY, width=9), c.line([(30, 40), (30, 100)], IVORY, 9))), 430, 380)
    seq(img, t, ts[0] + 0.8, txt("TAKEN APART TO STORE", 32, GOLD, 1), 330, 500)
    p = ease(seg(t, ts[1], 0.8))
    if p > 0:
        put(img, sprite("arr23", 240, 80, lambda c: (c.line([(10, 40), (160, 40)], GOLD, 14), c.poly([(160, 8), (230, 40), (160, 72)], fill=GOLD))), 740, 370, alpha=p)
    seq(img, t, ts[1] + 0.3, card(560, 340, GOLD), 1150, 370, shadow=12)
    seq(img, t, ts[1] + 0.5, sprite("wcC23", 220, 260, lambda c: ic_wheelchair(c, 110, 132, 1.1)), 1150, 350)
    seq(img, t, ts[1] + 0.8, txt("PUT BACK TOGETHER", 34, GOLD, 1), 1150, 500)
    seq(img, t, ts[2], sprite("clk23", 140, 140, lambda c: ic_clockface(c, 70, 70, 54, 0.6)), 1600, 330, shadow=6)
    seq(img, t, ts[2] + 0.3, txt("PROMPTLY", 38, IVORY, 2), 1600, 440)
    seq(img, t, ts[3], chip("IN THE CONDITION IT WAS RECEIVED", 1100, 100, GREEN_OK, "ok", 42), 960, 800, shadow=8)

# ============================================================ BLOCCO 24
def draw24(img, t):
    ts = starts(24)
    common(img, t, "IF IT COMES BACK DAMAGED")
    seq(img, t, ts[0], card(500, 440, RED), 330, 460, shadow=12)
    seq(img, t, ts[0] + 0.2, sprite("wcD24", 220, 260, lambda c: (ic_wheelchair(c, 110, 132, 1.1), ic_x(c, 170, 80, 0.8, RED, 16))), 330, 400)
    seq(img, t, ts[0] + 0.5, txt("DAMAGED", 44, RED, 2), 330, 590)
    seq(img, t, ts[1], card(500, 440, GOLD), 960, 460, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("cam24", 240, 200, lambda c: ic_camera(c, 120, 100, 1.4)), 960, 400)
    seq(img, t, ts[1] + 0.5, txt("TAKE A PHOTO", 40, GOLD, 2), 960, 570)
    seq(img, t, ts[1] + 0.8, txt("BEFORE YOU LEAVE", 28, IVORY, 1), 960, 615)
    seq(img, t, ts[2], card(500, 440, SAGE), 1590, 460, shadow=12)
    seq(img, t, ts[2] + 0.2, sprite("pl24", 200, 140, lambda c: ic_plane(c, 100, 70, 1.5)), 1590, 400)
    seq(img, t, ts[2] + 0.5, txt("REPORT IT TO", 36, IVORY, 2), 1590, 560)
    seq(img, t, ts[2] + 0.7, txt("THE AIRLINE", 44, GOLD, 2), 1590, 615)
    ban(img, t, ts[2] + 1.6, "RIGHT THERE AT THE AIRPORT", cy=930, w=1100, h=90, size=48)

# ============================================================ BLOCCO 25
def draw25(img, t):
    ts = starts(25)
    common(img, t, "WHO DOES THIS HELP?")
    seq(img, t, ts[1], card(1500, 220, SAGE), 960, 300, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("cane25", 160, 220, lambda c: ic_cane(c, 80, 110, 1.3)), 360, 300)
    seq(img, t, ts[1] + 0.5, walker(), 560, 300, scale=0.8)
    seq(img, t, ts[1] + 0.7, txt("ANYONE WHO FLIES WITH", 38, IVORY, 2), 1130, 265)
    seq(img, t, ts[1] + 0.9, txt("A CANE OR A WALKER", 56, GOLD, 2), 1130, 335)
    seq(img, t, ts[2], chip("YOUR ACTION: ONE SENTENCE AT THE GATE", 1300, 96, GOLD, None, 40), 960, 530, shadow=8)
    seq(img, t, ts[3], bubble_spr(1500, 240, IVORY, ["THIS IS MY MOBILITY AID,", "IT DOESN'T COUNT AS MY CARRY ON"], DARK, 56), 960, 760, shadow=12)

# ============================================================ BLOCCO 26
def draw26(img, t):
    ts = starts(26)
    common(img, t, "NEED ADVANCE NOTICE")
    show_badge(img, t, 4)
    seq(img, t, ts[1], card(1500, 340, GOLD), 960, 480, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("ox26", 240, 260, lambda c: ic_oxygen(c, 120, 130, 1.8)), 330, 480)
    seq(img, t, ts[1] + 0.4, txt("ONE OF ONLY TWO THINGS", 54, IVORY, 2), 1130, 420)
    seq(img, t, ts[1] + 0.7, txt("THAT NEED ADVANCE NOTICE", 58, GOLD, 2), 1130, 510)

# ============================================================ BLOCCO 27
def draw27(img, t):
    ts = starts(27)
    common(img, t, "ON THE PLANE")
    items = [("PORTABLE OXYGEN", ic_oxygen), ("VENTILATOR", ic_mask), ("RESPIRATOR", ic_mask), ("C P A P MACHINE", ic_mask)]
    img_ref[0] = img
    for k, (nm, fn) in enumerate(items):
        mini(nm, fn, 300 + k * 440, 340, t, ts[0] + k * 1.0, size=30)
    seq(img, t, ts[1], card(1500, 260, GOLD), 960, 760, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("clk27", 200, 200, lambda c: ic_clockface(c, 100, 100, 80, 0.8)), 330, 760)
    seq(img, t, ts[1] + 0.4, txt("THE AIRLINE MAY ASK FOR", 44, IVORY, 2), 1130, 710)
    seq(img, t, ts[1] + 0.7, txt("48 HOURS NOTICE", 84, GOLD, 3), 1130, 805)

# ============================================================ BLOCCO 28
def draw28(img, t):
    ts = starts(28)
    common(img, t, "THE MISTAKE")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, stamp("THE EXCEPTION, NOT THE RULE", 1200, 110, GOLD, size=52), 960, 210, scale=s, alpha=a, shadow=10)
    seq(img, t, ts[1], txt("AND HERE'S THE MISTAKE", 56, RED, 3), 960, 360)
    seq(img, t, ts[2], card(780, 280, SAGE), 480, 600, shadow=12)
    seq(img, t, ts[2] + 0.2, sprite("per28", 200, 240, lambda c: ic_person(c, 100, 120, 1.6, col=SAGE)), 270, 600)
    seq(img, t, ts[2] + 0.4, sprite("ox28", 160, 200, lambda c: ic_oxygen(c, 80, 100, 1.2)), 440, 600)
    seq(img, t, ts[2] + 0.6, txt("ASSUME IT'S", 36, IVORY, 2), 660, 570)
    seq(img, t, ts[2] + 0.8, txt("ALLOWED", 56, GOLD, 2), 660, 640)
    seq(img, t, ts[3], card(780, 280, RED), 1440, 600, shadow=12)
    seq(img, t, ts[3] + 0.2, sprite("clk28", 160, 160, lambda c: ic_clockface(c, 80, 80, 64, 0.8)), 1210, 600)
    seq(img, t, ts[3] + 0.4, txt("AT THE GATE:", 34, IVORY, 2), 1500, 560)
    seq(img, t, ts[3] + 0.6, txt("NEEDED TWO", 46, GOLD, 2), 1500, 625)
    seq(img, t, ts[3] + 0.8, txt("DAYS EARLIER", 46, GOLD, 2), 1500, 685)

# ============================================================ BLOCCO 29
def draw29(img, t):
    ts = starts(29)
    common(img, t, "NOT EVERY AIRLINE")
    seq(img, t, ts[0], card(1500, 260, RED), 960, 330, shadow=12)
    seq(img, t, ts[0] + 0.2, sprite("ox29", 200, 240, lambda c: (ic_oxygen(c, 100, 120, 1.5), ic_x(c, 150, 60, 0.7, RED, 14))), 330, 330)
    seq(img, t, ts[0] + 0.5, txt("NOT EVERY AIRLINE ALLOWS", 46, IVORY, 2), 1130, 290)
    seq(img, t, ts[0] + 0.8, txt("EVERY OXYGEN MODEL", 62, GOLD, 2), 1130, 370)
    seq(img, t, ts[1], txt("T S A SAYS CHECK WITH", 54, GOLD, 3), 960, 600)
    seq(img, t, ts[1] + 0.6, chip("YOUR AIRLINE", 600, 100, GOLD, None, 42), 560, 740, shadow=8)
    seq(img, t, ts[1] + 1.2, chip("THE MAKER OF YOUR DEVICE", 820, 100, GOLD, None, 38), 1400, 740, shadow=8)
    ban(img, t, ts[1] + 2.2, "BEFORE YOU FLY", cy=930, w=800, h=90, size=52)

# ============================================================ BLOCCO 30
def draw30(img, t):
    ts = starts(30)
    common(img, t, "WHO DOES THIS HELP?")
    seq(img, t, ts[1], card(1500, 220, SAGE), 960, 300, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("ox30", 200, 240, lambda c: ic_oxygen(c, 100, 120, 1.4)), 330, 300)
    seq(img, t, ts[1] + 0.5, txt("ANYONE WHO SLEEPS WITH A MACHINE,", 40, IVORY, 2), 1130, 265)
    seq(img, t, ts[1] + 0.9, txt("OR BREATHES WITH HELP", 56, GOLD, 2), 1130, 335)
    seq(img, t, ts[2], card(1500, 140, GOLD), 960, 520, shadow=12)
    seq(img, t, ts[2] + 0.2, sprite("ph30", 120, 160, lambda c: ic_phone(c, 60, 80, 1.1)), 280, 520)
    seq(img, t, ts[2] + 0.4, txt("YOUR ACTION: A PHONE CALL WHEN YOU BOOK", 42, GOLD, 2), 1050, 520)
    seq(img, t, ts[3], bubble_spr(1500, 230, IVORY, ["WHAT DO YOU NEED FROM ME,", "AND BY WHEN?"], DARK, 60), 960, 770, shadow=12)

DRAW = {21: draw21, 22: draw22, 23: draw23, 24: draw24, 25: draw25, 26: draw26, 27: draw27, 28: draw28, 29: draw29, 30: draw30}

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
