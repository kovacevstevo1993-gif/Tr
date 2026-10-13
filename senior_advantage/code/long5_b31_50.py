"""Video lungo 5 (AEROPORTO) - blocchi 31-50. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AEROPORTO.md.
Durate dalla timeline dell'utente (12/10/2026, fine blocco 30 = 9920): B31 189, B32 421, B33 286, B34 348, B35 393, B36 276, B37 258, B38 373, B39 330, B40 118,
B41 390, B42 95, B43 274, B44 269, B45 350, B46 259, B47 331, B48 232, B49 382, B50 141.
Uso: OUT=cartella python3 long5_b31_50.py <blocco> [fotogrammi]
     python3 long5_b31_50.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long5_b21_30 import *      # motore, icone, card, chip, banner, txt, seq, stamp, mini, ic_*

DUR = {31: 189, 32: 421, 33: 286, 34: 348, 35: 393, 36: 276, 37: 258, 38: 373, 39: 330, 40: 118,
       41: 390, 42: 95, 43: 274, 44: 269, 45: 350, 46: 259, 47: 331, 48: 232, 49: 382, 50: 141}
PHRASES = {
    31: ["Number five.", "A T S A helper for the security checkpoint.", "It's called T S A Cares."],
    32: ["If you want a trained T S A officer to help you through screening,", "you contact T S A Cares at least seventy two hours before you leave.",
         "The number is eight five five, seven eight seven, two two two seven."],
    33: ["They answer on weekdays from eight in the morning to eleven at night Eastern time,", "and on weekends and holidays from nine in the morning to eight at night."],
    34: ["Now, what it is not.", "It does not get you a wheelchair, that's the airline.", "It does not get you a faster line, that's T S A PreCheck.", "And you are still screened."],
    35: ["Who does it help?", "Someone who has trouble following instructions,", "who has a medical device,", "or who carries medically necessary liquids.", "Your action is a call, at least three days before you fly."],
    36: ["Number six.", "If you are seventy five or older, security has special steps for you.", "And if you are younger, this one is for your parents."],
    37: ["T S A says passengers seventy five and older may keep their shoes on.", "A light jacket does have to come off for the body scanner."],
    38: ["But here is the catch.", "If an alarm goes off, an officer may still ask you to take off your shoes,", "or give you a pat down.", "Keeping your shoes on is the starting point, not a guarantee."],
    39: ["If you're seventy five or older and you use a wheelchair or a scooter,", "you may stay seated in a standard lane.", "The officer will test your hands for explosives traces."],
    40: ["And if you can't stand during screening,", "you can ask for a chair."],
    41: ["The mistake is taking your shoes off automatically,", "just because everyone around you does.", "Your action is one question at the checkpoint.", "I'm seventy five or older, may I keep my shoes on?"],
    42: ["Number seven.", "Your medications at the checkpoint."],
    43: ["Pills have to go through screening like everything else.", "Clear labels help it go faster.", "They may be looked at, or tested for traces."],
    44: ["T S A says to tell the officer before screening begins", "that you have medically necessary liquids or medications,", "and to put them in a separate bin."],
    45: ["And T S A allows larger amounts of medically necessary liquids, gels and aerosols,", "in reasonable quantities for your flight.", "You declare them, and take them out of your bag."],
    46: ["If you don't want a liquid opened or X rayed, you can ask.", "They will use other steps instead, like a body scan or a pat down."],
    47: ["The common mistake is saying nothing.", "Then it alarms, and now it's a longer search.", "Your action is simple.", "Tell the officer first, and put it in its own bin."],
    48: ["Now a bonus.", "At any moment during screening, you can ask for a private screening,", "and have a witness of your choice with you."],
    49: ["And if something goes wrong at the checkpoint,", "ask for a supervisor right there.", "Afterward, you can contact the T S A Contact Center at eight six six, two eight nine, nine six seven three."],
    50: ["Now number eight, the one I promised.", "The biggest one.", "A cancelled flight."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

# ---------------------------------------------------------------- icone nuove
BROWN = (214, 164, 96)
def ic_shoe(c, cx, cy, s):
    c.poly([(cx - 62 * s, cy - 6 * s), (cx - 62 * s, cy - 44 * s), (cx - 22 * s, cy - 44 * s), (cx - 6 * s, cy - 14 * s), (cx + 48 * s, cy - 2 * s), (cx + 64 * s, cy + 18 * s), (cx - 62 * s, cy + 18 * s)], fill=BROWN)
    c.rrect((cx - 66 * s, cy + 18 * s, cx + 68 * s, cy + 36 * s), 6, fill=IVORY)
def ic_jacket(c, cx, cy, s):
    c.poly([(cx - 50 * s, cy - 52 * s), (cx - 18 * s, cy - 64 * s), (cx, cy - 36 * s), (cx + 18 * s, cy - 64 * s), (cx + 50 * s, cy - 52 * s), (cx + 66 * s, cy + 14 * s), (cx + 42 * s, cy + 18 * s), (cx + 40 * s, cy + 66 * s), (cx - 40 * s, cy + 66 * s), (cx - 42 * s, cy + 18 * s), (cx - 66 * s, cy + 14 * s)], fill=NAVY)
    c.line([(cx, cy - 36 * s), (cx, cy + 66 * s)], IVORY, 4)
def ic_bell(c, cx, cy, s):
    c.poly([(cx - 52 * s, cy + 34 * s), (cx - 40 * s, cy - 20 * s), (cx - 20 * s, cy - 54 * s), (cx + 20 * s, cy - 54 * s), (cx + 40 * s, cy - 20 * s), (cx + 52 * s, cy + 34 * s)], fill=RED)
    c.ell((cx - 14 * s, cy + 36 * s, cx + 14 * s, cy + 62 * s), fill=GOLD)
    c.line([(cx - 70 * s, cy - 40 * s), (cx - 56 * s, cy - 28 * s)], GOLD, 6)
    c.line([(cx + 70 * s, cy - 40 * s), (cx + 56 * s, cy - 28 * s)], GOLD, 6)
def ic_hand(c, cx, cy, s):
    c.rrect((cx - 38 * s, cy - 6 * s, cx + 38 * s, cy + 56 * s), 20 * s, fill=SKIN)
    for k in range(4):
        x = cx - 34 * s + k * 23 * s
        c.rrect((x, cy - 52 * s, x + 16 * s, cy + 10 * s), 8 * s, fill=SKIN)
def ic_chair(c, cx, cy, s):
    c.rrect((cx - 40 * s, cy - 6 * s, cx + 44 * s, cy + 14 * s), 6, fill=BROWN)
    c.rrect((cx - 44 * s, cy - 66 * s, cx - 28 * s, cy + 14 * s), 6, fill=BROWN)
    c.line([(cx - 34 * s, cy + 14 * s), (cx - 34 * s, cy + 64 * s)], BROWN, 10 * s)
    c.line([(cx + 36 * s, cy + 14 * s), (cx + 36 * s, cy + 64 * s)], BROWN, 10 * s)
def ic_bin(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy - 20 * s, cx + 70 * s, cy + 50 * s), 12 * s, fill=(70, 96, 86), outline=IVORY, width=4)
    c.rrect((cx - 58 * s, cy - 8 * s, cx + 58 * s, cy + 38 * s), 8 * s, fill=(30, 56, 48))
def ic_drop(c, cx, cy, s):
    c.poly([(cx, cy - 56 * s), (cx + 36 * s, cy + 8 * s), (cx, cy + 4 * s), (cx - 36 * s, cy + 8 * s)], fill=(110, 176, 200))
    c.ell((cx - 36 * s, cy - 14 * s, cx + 36 * s, cy + 58 * s), fill=(110, 176, 200))
def ic_gel(c, cx, cy, s):
    c.rrect((cx - 30 * s, cy - 40 * s, cx + 30 * s, cy + 56 * s), 14 * s, fill=(110, 200, 170))
    c.rrect((cx - 16 * s, cy - 62 * s, cx + 16 * s, cy - 38 * s), 4, fill=IVORY)
def ic_spray(c, cx, cy, s):
    c.rrect((cx - 26 * s, cy - 20 * s, cx + 26 * s, cy + 58 * s), 10 * s, fill=(214, 120, 100))
    c.rrect((cx - 16 * s, cy - 44 * s, cx + 16 * s, cy - 20 * s), 4, fill=IVORY)
    for k in range(3):
        c.ell((cx + 26 * s + k * 14 * s, cy - 42 * s + k * 10 * s, cx + 34 * s + k * 14 * s, cy - 34 * s + k * 10 * s), fill=IVORY)
def ic_two(c, cx, cy, s):
    ic_person(c, cx - 34 * s, cy, 1.0 * s, col=SAGE); ic_person(c, cx + 34 * s, cy, 1.0 * s, col=GOLD)
def ic_clock(c, cx, cy, s):
    ic_clockface(c, cx, cy, 60 * s, 0.7)
def crown(c, cx, cy, s):
    c.poly([(cx - 52 * s, cy + 38 * s), (cx - 52 * s, cy - 18 * s), (cx - 24 * s, cy + 8 * s), (cx, cy - 36 * s), (cx + 24 * s, cy + 8 * s), (cx + 52 * s, cy - 18 * s), (cx + 52 * s, cy + 38 * s)], fill=GOLD)

def ic(name, fn, w=240, h=200, s=1.0):
    return sprite(("i31", name, s), w, h, lambda c: fn(c, w / 2, h / 2, s))

def info(img, t, t0, x, y, w, h, border, icon, l1, l2, s1=40, s2=64, c1=IVORY, c2=GOLD, ix=None, tx=None):
    ix = ix if ix is not None else x - w / 2 + 170
    tx = tx if tx is not None else x + 110
    seq(img, t, t0, card(w, h, border), x, y, shadow=12)
    seq(img, t, t0 + 0.2, icon, ix, y)
    seq(img, t, t0 + 0.4, txt(l1, s1, c1, 2), tx, y - h * 0.18)
    seq(img, t, t0 + 0.7, txt(l2, s2, c2, 2), tx, y + h * 0.2)

def arrow_r(img, t, t0, x, y, w=240):
    p = ease(seg(t, t0, 0.8))
    if p > 0:
        put(img, sprite(("arr31", w), w, 80, lambda c: (c.line([(10, 40), (w - 80, 40)], GOLD, 14), c.poly([(w - 80, 8), (w - 10, 40), (w - 80, 72)], fill=GOLD))), x, y, alpha=p)

# ============================================================ BLOCCO 31
def draw31(img, t):
    img_ref[0] = img; ts = starts(31)
    common(img, t, "T S A CARES"); show_badge(img, t, 5)
    info(img, t, ts[1], 960, 450, 1500, 300, GOLD, ic("off31", ic_officer, 240, 240, 1.6), "A T S A HELPER", "FOR THE SECURITY CHECKPOINT", 56, 56)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, stamp("IT'S CALLED T S A CARES", 1100, 120, GREEN_OK, size=56), 960, 800, scale=s, alpha=a, rot=-2, shadow=10)

# ============================================================ BLOCCO 32
def draw32(img, t):
    ts = starts(32)
    common(img, t, "T S A CARES")
    info(img, t, ts[0], 960, 300, 1500, 220, SAGE, ic("off32", ic_officer, 220, 220, 1.4), "A TRAINED T S A OFFICER", "HELPS YOU THROUGH SCREENING", 46, 52)
    info(img, t, ts[1], 960, 560, 1500, 200, GOLD, ic("clk32", ic_clock, 200, 200, 1.1), "CONTACT T S A CARES", "AT LEAST 72 HOURS BEFORE YOU LEAVE", 40, 50)
    seq(img, t, ts[2], card(1500, 200, GOLD), 960, 820, shadow=12)
    seq(img, t, ts[2] + 0.2, ic("ph32", ic_phone, 140, 180, 1.3), 330, 820)
    seq(img, t, ts[2] + 0.5, txt("855 787 2227", 100, GOLD, 3), 1050, 820)

# ============================================================ BLOCCO 33
def draw33(img, t):
    ts = starts(33)
    common(img, t, "T S A CARES: WHEN THEY ANSWER")
    seq(img, t, ts[0] + 0.1, txt("EASTERN TIME", 40, SAGE, 3), 960, 200)
    seq(img, t, ts[0], card(1500, 280, GOLD), 960, 400, shadow=12)
    seq(img, t, ts[0] + 0.3, txt("WEEKDAYS", 56, GOLD, 3), 960, 340)
    seq(img, t, ts[0] + 0.8, txt("8 AM TO 11 PM", 90, IVORY, 3), 960, 450)
    seq(img, t, ts[1], card(1500, 280, SAGE), 960, 760, shadow=12)
    seq(img, t, ts[1] + 0.3, txt("WEEKENDS AND HOLIDAYS", 56, GOLD, 3), 960, 700)
    seq(img, t, ts[1] + 0.8, txt("9 AM TO 8 PM", 90, IVORY, 3), 960, 810)

# ============================================================ BLOCCO 34
def draw34(img, t):
    ts = starts(34)
    common(img, t, "WHAT IT IS NOT")
    seq(img, t, ts[1], card(780, 330, RED), 480, 400, shadow=12)
    seq(img, t, ts[1] + 0.2, ic("wc34", lambda c, x, y, s: ic_wheelchair(c, x, y, s), 220, 260, 1.0), 270, 400)
    seq(img, t, ts[1] + 0.4, chip("NOT A WHEELCHAIR", 420, 80, RED, "x", 28), 640, 360, shadow=6)
    seq(img, t, ts[1] + 1.0, txt("THAT'S THE AIRLINE", 36, GOLD, 2), 640, 460)
    seq(img, t, ts[2], card(780, 330, RED), 1440, 400, shadow=12)
    seq(img, t, ts[2] + 0.2, ic("ln34", lambda c, x, y, s: [ic_person(c, x - 60 + 60 * k, y, 0.8, col=SAGE) for k in range(3)], 240, 200, 1.0), 1230, 400)
    seq(img, t, ts[2] + 0.4, chip("NOT A FASTER LINE", 420, 80, RED, "x", 28), 1590, 360, shadow=6)
    seq(img, t, ts[2] + 1.0, txt("THAT'S T S A PRECHECK", 28, GOLD, 1), 1590, 460)
    seq(img, t, ts[3], chip("YOU ARE STILL SCREENED", 900, 110, GOLD, None, 50), 960, 800, shadow=8)

# ============================================================ BLOCCO 35
def draw35(img, t):
    ts = starts(35)
    common(img, t, "WHO DOES IT HELP?")
    items = [("TROUBLE FOLLOWING", "INSTRUCTIONS", lambda c, x, y, s: ic_person(c, x, y, 1.4, col=SAGE), ts[1]),
             ("A MEDICAL", "DEVICE", ic_oxygen, ts[2]), ("MEDICALLY NECESSARY", "LIQUIDS", ic_drop, ts[3])]
    for k, (l1, l2, fn, t0) in enumerate(items):
        x = 340 + k * 620
        seq(img, t, t0, card(560, 380, SAGE), x, 360, shadow=12)
        seq(img, t, t0 + 0.2, ic("w35%d" % k, fn, 240, 200, 1.0), x, 320)
        seq(img, t, t0 + 0.4, txt(l1, 32, IVORY, 1), x, 450)
        seq(img, t, t0 + 0.6, txt(l2, 40, GOLD, 2), x, 500)
    seq(img, t, ts[4], card(1500, 160, GOLD), 960, 800, shadow=12)
    seq(img, t, ts[4] + 0.2, ic("ph35", ic_phone, 120, 160, 1.1), 330, 800)
    seq(img, t, ts[4] + 0.5, txt("A CALL, AT LEAST 3 DAYS BEFORE YOU FLY", 46, GOLD, 2), 1050, 800)

# ============================================================ BLOCCO 36
def draw36(img, t):
    ts = starts(36)
    common(img, t, "AGE 75 AND OLDER"); show_badge(img, t, 6)
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, shield75(), 560, 480, scale=s * 1.0, alpha=a, shadow=14)
    seq(img, t, ts[1] + 0.5, txt("SECURITY HAS", 52, IVORY, 2), 1330, 400)
    seq(img, t, ts[1] + 0.8, txt("SPECIAL STEPS", 76, GOLD, 3), 1330, 490)
    seq(img, t, ts[1] + 1.1, txt("FOR YOU", 52, IVORY, 2), 1330, 575)
    seq(img, t, ts[2], chip("YOUNGER? THIS ONE IS FOR YOUR PARENTS", 1300, 100, GOLD, None, 40), 960, 900, shadow=8)

# ============================================================ BLOCCO 37
def draw37(img, t):
    ts = starts(37)
    common(img, t, "AGE 75 AND OLDER")
    seq(img, t, ts[0], card(780, 420, GREEN_OK), 480, 470, shadow=12)
    seq(img, t, ts[0] + 0.2, ic("sh37", ic_shoe, 240, 200, 1.4), 480, 430)
    seq(img, t, ts[0] + 0.6, chip("SHOES STAY ON", 460, 84, GREEN_OK, "ok", 36), 480, 580, shadow=6)
    seq(img, t, ts[1], card(780, 420, RED), 1440, 470, shadow=12)
    seq(img, t, ts[1] + 0.2, ic("jk37", ic_jacket, 240, 200, 1.3), 1440, 430)
    seq(img, t, ts[1] + 0.6, chip("LIGHT JACKET COMES OFF", 600, 84, RED, "x", 32), 1440, 580, shadow=6)
    seq(img, t, ts[1] + 1.2, txt("FOR THE BODY SCANNER", 36, IVORY, 2), 1440, 700)

# ============================================================ BLOCCO 38
def draw38(img, t):
    ts = starts(38)
    common(img, t, "THE CATCH")
    seq(img, t, ts[0], txt("HERE IS THE CATCH", 70, GOLD, 3), 960, 190, shadow=8)
    seq(img, t, ts[1], ic("bell38", ic_bell, 240, 240, 1.6), 330, 440, shadow=8)
    seq(img, t, ts[1] + 0.4, txt("AN ALARM GOES OFF", 40, IVORY, 2), 330, 600)
    seq(img, t, ts[1] + 1.0, chip("TAKE OFF YOUR SHOES", 640, 90, RED, "x", 36), 960, 360, shadow=6)
    seq(img, t, ts[2], chip("OR A PAT DOWN", 640, 90, RED, "x", 36), 960, 490, shadow=6)
    s, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, stamp("STARTING POINT, NOT A GUARANTEE", 1300, 110, GOLD, size=50), 960, 820, scale=s, alpha=a, rot=-2, shadow=10)

# ============================================================ BLOCCO 39
def draw39(img, t):
    ts = starts(39)
    common(img, t, "AGE 75 AND OLDER")
    info(img, t, ts[0], 960, 300, 1500, 220, SAGE, ic("wc39", lambda c, x, y, s: ic_wheelchair(c, x, y, s), 220, 260, 1.0), "75+ IN A WHEELCHAIR OR SCOOTER", "YOU MAY STAY SEATED", 40, 60)
    seq(img, t, ts[1], chip("IN A STANDARD LANE", 700, 90, GREEN_OK, "ok", 38), 960, 520, shadow=8)
    seq(img, t, ts[2], card(1500, 220, GOLD), 960, 780, shadow=12)
    seq(img, t, ts[2] + 0.2, ic("hd39", ic_hand, 200, 200, 1.4), 330, 780)
    seq(img, t, ts[2] + 0.5, txt("THE OFFICER TESTS YOUR HANDS", 46, IVORY, 2), 1100, 740)
    seq(img, t, ts[2] + 0.9, txt("FOR EXPLOSIVES TRACES", 56, GOLD, 2), 1100, 820)

# ============================================================ BLOCCO 40
def draw40(img, t):
    ts = starts(40)
    common(img, t, "CAN'T STAND?")
    seq(img, t, ts[0], card(700, 420, RED), 540, 480, shadow=12)
    seq(img, t, ts[0] + 0.2, ic("pe40", lambda c, x, y, s: ic_person(c, x, y, 1.8, col=SAGE), 240, 260, 1.0), 540, 440)
    seq(img, t, ts[0] + 0.5, txt("CAN'T STAND", 44, IVORY, 2), 540, 620)
    seq(img, t, ts[1], card(700, 420, GREEN_OK), 1380, 480, shadow=12)
    seq(img, t, ts[1] + 0.2, ic("ch40", ic_chair, 240, 220, 1.6), 1380, 440)
    seq(img, t, ts[1] + 0.5, txt("ASK FOR A CHAIR", 44, GOLD, 2), 1380, 620)

# ============================================================ BLOCCO 41
def draw41(img, t):
    ts = starts(41)
    common(img, t, "THE MISTAKE")
    seq(img, t, ts[0], card(780, 300, RED), 480, 340, shadow=12)
    seq(img, t, ts[0] + 0.2, ic("sh41", ic_shoe, 240, 200, 1.3), 280, 340)
    seq(img, t, ts[0] + 0.5, txt("SHOES OFF", 44, GOLD, 2), 640, 300)
    seq(img, t, ts[0] + 0.8, txt("AUTOMATICALLY", 36, IVORY, 2), 640, 370)
    seq(img, t, ts[1], card(780, 300, SAGE), 1440, 340, shadow=12)
    seq(img, t, ts[1] + 0.2, ic("tw41", ic_two, 240, 200, 1.1), 1240, 340)
    seq(img, t, ts[1] + 0.5, txt("JUST BECAUSE", 40, IVORY, 2), 1560, 300)
    seq(img, t, ts[1] + 0.8, txt("EVERYONE DOES", 44, GOLD, 2), 1560, 370)
    seq(img, t, ts[2], txt("YOUR ACTION: ONE QUESTION", 54, GOLD, 3), 960, 600)
    seq(img, t, ts[3], bubble_spr(1500, 190, IVORY, ["I'M 75 OR OLDER,", "MAY I KEEP MY SHOES ON?"], DARK, 56), 960, 800, shadow=12)

# ============================================================ BLOCCO 42
def draw42(img, t):
    ts = starts(42)
    common(img, t, "YOUR MEDICATIONS"); show_badge(img, t, 7)
    seq(img, t, ts[1], card(1500, 400, GOLD), 960, 500, shadow=12)
    seq(img, t, ts[1] + 0.2, ic("pl42", ic_pills, 260, 220, 1.5), 400, 500)
    seq(img, t, ts[1] + 0.5, txt("YOUR MEDICATIONS", 70, GOLD, 3), 1150, 450)
    seq(img, t, ts[1] + 0.9, txt("AT THE CHECKPOINT", 56, IVORY, 3), 1150, 540)

# ============================================================ BLOCCO 43
def draw43(img, t):
    ts = starts(43)
    common(img, t, "PILLS AT SCREENING")
    seq(img, t, ts[0], card(1500, 300, SAGE), 960, 320, shadow=12)
    seq(img, t, ts[0] + 0.2, ic("pl43", ic_pills, 260, 220, 1.2), 360, 320)
    seq(img, t, ts[0] + 0.5, txt("THROUGH SCREENING", 56, GOLD, 3), 1130, 270)
    seq(img, t, ts[0] + 0.8, txt("LIKE EVERYTHING ELSE", 44, IVORY, 2), 1130, 350)
    seq(img, t, ts[1], chip("CLEAR LABELS = FASTER", 760, 100, GREEN_OK, "ok", 40), 520, 640, shadow=8)
    seq(img, t, ts[2], ic("mg43", lambda c, x, y, s: ic_magnify(c, x, y, s), 200, 200, 1.3), 1230, 640, shadow=6)
    seq(img, t, ts[2] + 0.3, txt("LOOKED AT, OR", 38, IVORY, 2), 1520, 615)
    seq(img, t, ts[2] + 0.6, txt("TESTED FOR TRACES", 38, GOLD, 2), 1520, 670)

# ============================================================ BLOCCO 44
def draw44(img, t):
    ts = starts(44)
    common(img, t, "TELL THE OFFICER FIRST")
    seq(img, t, ts[0], ic("off44", ic_officer, 240, 240, 1.5), 330, 400, shadow=8)
    seq(img, t, ts[0] + 0.4, bubble_spr(900, 230, IVORY, ["I HAVE MEDICALLY", "NECESSARY LIQUIDS", "OR MEDICATIONS"], DARK, 46), 1050, 400, shadow=12)
    seq(img, t, ts[1], ic("pl44", ic_pills, 260, 220, 1.3), 520, 760, shadow=6)
    seq(img, t, ts[2] - 0.3, ic("bin44", ic_bin, 300, 200, 1.6), 960, 770, shadow=8)
    arrow_r(img, t, ts[2], 740, 770, 200)
    seq(img, t, ts[2] + 0.4, chip("A SEPARATE BIN", 560, 100, GOLD, None, 40), 1480, 770, shadow=8)

# ============================================================ BLOCCO 45
def draw45(img, t):
    ts = starts(45)
    common(img, t, "LARGER AMOUNTS ALLOWED")
    items = [("LIQUIDS", ic_drop), ("GELS", ic_gel), ("AEROSOLS", ic_spray)]
    img_ref[0] = img
    for k, (nm, fn) in enumerate(items):
        mini(nm, fn, 340 + k * 620, 330, t, ts[0] + k * 1.1, border=SAGE, w=480, h=320, size=44)
    seq(img, t, ts[1], chip("REASONABLE QUANTITIES FOR YOUR FLIGHT", 1300, 96, GOLD, None, 40), 960, 600, shadow=8)
    seq(img, t, ts[2], chip("DECLARE THEM", 560, 96, GREEN_OK, "ok", 40), 560, 790, shadow=8)
    seq(img, t, ts[2] + 0.8, chip("TAKE THEM OUT OF YOUR BAG", 780, 96, GREEN_OK, "ok", 38), 1380, 790, shadow=8)

# ============================================================ BLOCCO 46
def draw46(img, t):
    ts = starts(46)
    common(img, t, "YOU CAN ASK")
    seq(img, t, ts[0], card(1500, 260, RED), 960, 330, shadow=12)
    seq(img, t, ts[0] + 0.2, ic("dr46", ic_drop, 200, 200, 1.5), 330, 330)
    seq(img, t, ts[0] + 0.5, chip("OPENED", 340, 84, RED, "x", 36), 800, 330, shadow=6)
    seq(img, t, ts[0] + 1.0, chip("X RAYED", 340, 84, RED, "x", 36), 1180, 330, shadow=6)
    seq(img, t, ts[0] + 1.6, txt("YOU CAN ASK", 60, GOLD, 3), 960, 520)
    seq(img, t, ts[1], txt("OTHER STEPS INSTEAD", 54, IVORY, 3), 960, 640)
    seq(img, t, ts[1] + 0.8, chip("A BODY SCAN", 560, 100, GREEN_OK, "ok", 42), 560, 820, shadow=8)
    seq(img, t, ts[1] + 1.5, chip("A PAT DOWN", 560, 100, GREEN_OK, "ok", 42), 1380, 820, shadow=8)

# ============================================================ BLOCCO 47
def draw47(img, t):
    ts = starts(47)
    common(img, t, "THE COMMON MISTAKE")
    seq(img, t, ts[0], chip("SAYING NOTHING", 640, 100, RED, "x", 44), 420, 260, shadow=8)
    seq(img, t, ts[1], ic("bell47", ic_bell, 200, 200, 1.4), 1000, 260, shadow=6)
    seq(img, t, ts[1] + 0.5, chip("A LONGER SEARCH", 600, 100, RED, "x", 40), 1500, 260, shadow=8)
    seq(img, t, ts[2], txt("YOUR ACTION IS SIMPLE", 60, GOLD, 3), 960, 480)
    seq(img, t, ts[3], chip("TELL THE OFFICER FIRST", 720, 100, GREEN_OK, "ok", 40), 520, 700, shadow=8)
    seq(img, t, ts[3] + 1.0, ic("bin47", ic_bin, 260, 160, 1.2), 1230, 700, shadow=6)
    seq(img, t, ts[3] + 1.3, chip("ITS OWN BIN", 420, 100, GREEN_OK, "ok", 40), 1560, 700, shadow=8)

# ============================================================ BLOCCO 48
def draw48(img, t):
    ts = starts(48)
    common(img, t, "A BONUS")
    s, a, p = pop(t, ts[0], 0.5)
    if p > 0:
        put(img, stamp("BONUS", 420, 120, GOLD, size=70), 960, 200, scale=s, alpha=a, shadow=10)
    seq(img, t, ts[1], card(1500, 220, SAGE), 960, 460, shadow=12)
    seq(img, t, ts[1] + 0.2, ic("pr48", lambda c, x, y, s: (c.arc((x - 34, y - 70, x + 34, y + 10), 180, 360, GOLD, 12), c.rrect((x - 52, y - 16, x + 52, y + 62), 12, fill=GOLD), c.ell((x - 9, y + 8, x + 9, y + 26), fill=GREEN_D)), 200, 200, 1.0), 330, 460)
    seq(img, t, ts[1] + 0.5, txt("AT ANY MOMENT, ASK FOR", 40, IVORY, 2), 1100, 420)
    seq(img, t, ts[1] + 0.9, txt("A PRIVATE SCREENING", 66, GOLD, 3), 1100, 500)
    seq(img, t, ts[2], card(1500, 220, GOLD), 960, 760, shadow=12)
    seq(img, t, ts[2] + 0.2, ic("tw48", ic_two, 240, 200, 1.2), 330, 760)
    seq(img, t, ts[2] + 0.5, txt("A WITNESS OF YOUR CHOICE", 62, GOLD, 2), 1100, 760)

# ============================================================ BLOCCO 49
def draw49(img, t):
    ts = starts(49)
    common(img, t, "SOMETHING GOES WRONG")
    seq(img, t, ts[0], txt("AT THE CHECKPOINT", 44, SAGE, 3), 960, 200)
    seq(img, t, ts[1], card(1500, 220, GOLD), 960, 360, shadow=12)
    seq(img, t, ts[1] + 0.2, ic("off49", ic_officer, 220, 220, 1.4), 330, 360)
    seq(img, t, ts[1] + 0.5, txt("ASK FOR A SUPERVISOR", 66, GOLD, 3), 1100, 330)
    seq(img, t, ts[1] + 0.9, txt("RIGHT THERE", 44, IVORY, 2), 1100, 410)
    seq(img, t, ts[2], card(1500, 300, SAGE), 960, 720, shadow=12)
    seq(img, t, ts[2] + 0.2, ic("ph49", ic_phone, 120, 180, 1.3), 300, 720)
    seq(img, t, ts[2] + 0.5, txt("AFTERWARD: T S A CONTACT CENTER", 40, IVORY, 2), 1100, 650)
    seq(img, t, ts[2] + 1.5, txt("866 289 9673", 96, GOLD, 3), 1100, 770)

# ============================================================ BLOCCO 50
def draw50(img, t):
    ts = starts(50)
    common(img, t, "THE BIGGEST ONE"); show_badge(img, t, 8)
    seq(img, t, ts[0] + 0.3, txt("THE ONE I PROMISED", 50, SAGE, 3), 960, 200)
    seq(img, t, ts[1], sprite("cr50", 140, 110, lambda c: crown(c, 70, 55, 1.2)), 960, 340, shadow=8)
    seq(img, t, ts[1] + 0.3, txt("THE BIGGEST ONE", 80, GOLD, 3), 960, 450)
    seq(img, t, ts[2], card(1500, 260, GOLD), 960, 720, shadow=12)
    seq(img, t, ts[2] + 0.2, ic("pl50", lambda c, x, y, s: (ic_plane(c, x, y, 1.1), ic_x(c, x, y, 1.0, RED, 14)), 240, 160, 1.0), 330, 720)
    seq(img, t, ts[2] + 0.5, txt("A CANCELLED FLIGHT", 76, IVORY, 3), 1100, 720)

DRAW = {31: draw31, 32: draw32, 33: draw33, 34: draw34, 35: draw35, 36: draw36, 37: draw37, 38: draw38, 39: draw39, 40: draw40,
        41: draw41, 42: draw42, 43: draw43, 44: draw44, 45: draw45, 46: draw46, 47: draw47, 48: draw48, 49: draw49, 50: draw50}

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
