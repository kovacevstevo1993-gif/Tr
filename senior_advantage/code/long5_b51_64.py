"""Video lungo 5 (AEROPORTO) - blocchi 51-64. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AEROPORTO.md.
Durate dalla timeline dell'utente (12/10/2026, fine blocco 50 = 15635): B51 332, B52 195, B53 125, B54 210, B55 385.
Uso: OUT=cartella python3 long5_b51_64.py <blocco> [fotogrammi]
     python3 long5_b51_64.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long5_b31_50 import *      # motore, icone, card, chip, banner, txt, seq, stamp, info, ic

DUR = {51: 332, 52: 195, 53: 125, 54: 210, 55: 385, 56: 423, 57: 309, 58: 306, 59: 327, 60: 396, 61: 526, 62: 433, 63: 186, 64: 410}
PHRASES = {
    51: ["When an airline cancels your flight, or changes it a lot, and you don't take what they offer instead,", "federal rules say you are owed your money back, as a refund.", "Not a voucher."],
    52: ["A voucher is allowed only if you choose it.", "It can't be pushed on you.", "You are allowed to say no."],
    53: ["The refund also covers the taxes and the extra fees you paid."],
    54: ["The common mistake is saying yes to the first thing offered at the counter,", "because you're tired, and the line is long."],
    55: ["Who does this help?", "Anyone who books ahead, and a cancelled flight is exactly when it matters.", "Your action is one sentence.", "I'd like a refund to my original payment method, not a voucher."],
    56: ["Quick recap.", "The star on your I D.", "Help from the curb to your gate.", "Your cane doesn't count as a bag.", "Notice for oxygen and C P A P.", "T S A Cares.", "The seventy five rule.", "Your pills.", "And the refund."],
    57: ["Eight things, from official federal pages.", "And now, the sentence I promised.", "Almost every one of these starts the same way.", "You have to say it out loud."],
    58: ["Because here's the truth.", "Being allowed to do something doesn't change what happens to you at the airport.", "Only asking does.", "And nobody is paid to remind you."],
    59: ["So write down three sentences before you travel.", "I need help from the curb to my gate.", "May I keep my shoes on?", "And, I'd like a refund, not a voucher."],
    60: ["And one more thing.", "This won't work every single time.", "An agent may be busy, or may not know the rule.", "If that happens, stay calm, ask for a supervisor, and say the rule by name."],
    61: ["So here is what to do this week, and most of it costs nothing.", "Check your license for the star.", "Save the T S A Cares number in your phone.", "Write the three sentences on a card.", "And if you use oxygen or a C P A P, call your airline now."],
    62: ["Which of these eight did you not know about?", "Tell me in the comments.", "And send this video to one person over sixty who flies, a parent, a brother, a friend at church.", "It could save them a bad day at the airport."],
    63: ["If this helped you, tap like and subscribe to The Senior Advantage, so you don't miss the next one."],
    64: ["Rules, amounts and ages change and differ by location and plan.", "Always confirm with the official source before you rely on them.", "This is general information, not financial advice."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def ic_ticket(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy - 40 * s, cx + 70 * s, cy + 40 * s), 10 * s, fill=CORAL)
    c.ell((cx - 82 * s, cy - 14 * s, cx - 56 * s, cy + 14 * s), fill=GREEN_D)
    c.ell((cx + 56 * s, cy - 14 * s, cx + 82 * s, cy + 14 * s), fill=GREEN_D)
    c.text((cx, cy + 2 * s), "VOUCHER", FONT_SANS, 20 * s, IVORY, track=0)
def ic_coin(c, cx, cy, s):
    c.ell((cx - 60 * s, cy - 60 * s, cx + 60 * s, cy + 60 * s), fill=GOLD, outline=(168, 118, 40), width=6)
    c.text((cx, cy + 3 * s), "$", FONT_SANS, 80 * s, GREEN_D)

# ============================================================ BLOCCO 51
def draw51(img, t):
    ts = starts(51)
    common(img, t, "THE REFUND"); show_badge(img, t, 8)
    info(img, t, ts[0], 960, 300, 1500, 200, RED, ic("pl51", lambda c, x, y, s: (ic_plane(c, x, y, 1.3), ic_x(c, x, y, 1.1, RED, 14)), 240, 160, 1.0), "THE AIRLINE CANCELS YOUR FLIGHT", "OR CHANGES IT A LOT", 42, 56)
    seq(img, t, ts[0] + 1.6, chip("YOU DON'T TAKE WHAT THEY OFFER INSTEAD", 1300, 90, RED, "x", 36), 960, 480, shadow=6)
    info(img, t, ts[1], 960, 690, 1500, 220, GOLD, ic("co51", ic_coin, 200, 200, 1.1), "YOU ARE OWED YOUR MONEY BACK", "A REFUND", 46, 80)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, stamp("NOT A VOUCHER", 760, 100, RED, size=52), 960, 920, scale=s, alpha=a, rot=-2, shadow=10)

# ============================================================ BLOCCO 52
def draw52(img, t):
    ts = starts(52)
    common(img, t, "THE VOUCHER")
    info(img, t, ts[0], 960, 320, 1500, 220, GOLD, ic("tk52", ic_ticket, 240, 160, 1.3), "A VOUCHER IS ALLOWED", "ONLY IF YOU CHOOSE IT", 44, 60)
    seq(img, t, ts[1], chip("IT CAN'T BE PUSHED ON YOU", 1100, 100, RED, "x", 44), 960, 560, shadow=8)
    seq(img, t, ts[2], ic("pe52", lambda c, x, y, s: ic_person(c, x, y, 1.8, col=SAGE), 240, 260, 1.0), 460, 800, shadow=8)
    seq(img, t, ts[2] + 0.3, bubble_spr(760, 170, IVORY, ["YOU ARE ALLOWED", "TO SAY NO"], DARK, 56), 1160, 790, shadow=12)

# ============================================================ BLOCCO 53
def draw53(img, t):
    ts = starts(53)
    common(img, t, "THE REFUND ALSO COVERS")
    seq(img, t, ts[0], card(1500, 240, GOLD), 960, 340, shadow=12)
    seq(img, t, ts[0] + 0.2, ic("co53", ic_coin, 200, 200, 1.2), 330, 340)
    seq(img, t, ts[0] + 0.5, txt("THE REFUND ALSO COVERS", 64, GOLD, 3), 1130, 340)
    seq(img, t, ts[0] + 1.2, chip("THE TAXES", 560, 110, GREEN_OK, "ok", 48), 560, 640, shadow=8)
    seq(img, t, ts[0] + 2.2, chip("THE EXTRA FEES YOU PAID", 800, 110, GREEN_OK, "ok", 44), 1400, 640, shadow=8)

# ============================================================ BLOCCO 54
def draw54(img, t):
    ts = starts(54)
    common(img, t, "THE COMMON MISTAKE")
    seq(img, t, ts[0], card(1500, 260, RED), 960, 320, shadow=12)
    seq(img, t, ts[0] + 0.2, ic("pe54", lambda c, x, y, s: ic_person(c, x, y, 1.6, col=SAGE), 220, 240, 1.0), 330, 320)
    seq(img, t, ts[0] + 0.5, txt("SAYING YES TO", 44, IVORY, 2), 1100, 270)
    seq(img, t, ts[0] + 0.9, txt("THE FIRST THING OFFERED", 64, GOLD, 2), 1100, 350)
    seq(img, t, ts[0] + 1.6, txt("AT THE COUNTER", 34, SAGE, 2), 1100, 420)
    seq(img, t, ts[1], chip("YOU'RE TIRED", 520, 100, GOLD, None, 44), 480, 700, shadow=8)
    seq(img, t, ts[1] + 0.8, card(840, 220, SAGE), 1380, 700, shadow=12)
    seq(img, t, ts[1] + 1.0, ic("ln54", lambda c, x, y, s: [ic_person(c, x - 120 + 60 * k, y, 0.9, col=SAGE) for k in range(5)], 400, 160, 1.0), 1120, 690)
    seq(img, t, ts[1] + 1.2, txt("THE LINE IS LONG", 40, GOLD, 2), 1560, 700)

# ============================================================ BLOCCO 55
def draw55(img, t):
    ts = starts(55)
    common(img, t, "WHO DOES THIS HELP?")
    info(img, t, ts[1], 960, 330, 1500, 240, SAGE, ic("pl55", lambda c, x, y, s: ic_plane(c, x, y, 1.4), 240, 160, 1.0), "ANYONE WHO BOOKS AHEAD", "A CANCELLED FLIGHT: EXACTLY WHEN IT MATTERS", 56, 38)
    seq(img, t, ts[2], chip("YOUR ACTION: ONE SENTENCE", 1000, 96, GOLD, None, 42), 960, 580, shadow=8)
    seq(img, t, ts[3], bubble_spr(1560, 240, IVORY, ["I'D LIKE A REFUND TO MY ORIGINAL", "PAYMENT METHOD, NOT A VOUCHER"], DARK, 56), 960, 800, shadow=12)

# ============================================================ BLOCCO 56
def draw56(img, t):
    ts = starts(56)
    common(img, t, "QUICK RECAP")
    for i, (n, fn, name) in enumerate(TILES):
        x, y = tile_pos(i)
        s2, a2, p2 = pop(t, ts[n], 0.45)
        if p2 > 0:
            put(img, tile2e(n, fn, name), x, y, scale=s2, alpha=a2, shadow=10)
            if p2 < 1:
                burst(img, t, ts[n], x, y, n=8, color=GOLD, rad=150, seed=n)

# ============================================================ BLOCCO 57
def draw57(img, t):
    ts = starts(57)
    common(img, t, "THE SENTENCE")
    info(img, t, ts[0], 960, 300, 1500, 220, GOLD, ic("gv57", lambda c, x, y, s: ic_gov(c, x, y, 1.5), 240, 200, 1.0), "EIGHT THINGS", "FROM OFFICIAL FEDERAL PAGES", 52, 52)
    seq(img, t, ts[1], chip("THE SENTENCE I PROMISED", 900, 100, GOLD, None, 46), 960, 500, shadow=8)
    for k in range(8):
        seq(img, t, ts[2] + k * 0.18, badge(k + 1), 330 + k * 180, 650, scale=0.7, shadow=4)
    seq(img, t, ts[2] + 1.8, txt("ALMOST EVERY ONE STARTS THE SAME WAY", 40, SAGE, 2), 960, 740)
    seq(img, t, ts[3], bubble_spr(1100, 150, IVORY, ["YOU HAVE TO SAY IT", "OUT LOUD"], DARK, 52), 960, 890, shadow=12)

# ============================================================ BLOCCO 58
def draw58(img, t):
    ts = starts(58)
    common(img, t, "THE TRUTH")
    seq(img, t, ts[1], card(1500, 240, RED), 960, 320, shadow=12)
    seq(img, t, ts[1] + 0.2, sprite("ck58", 200, 200, lambda c: check_ic(c, 100, 100, 1.6, GREEN_OK)), 330, 320)
    seq(img, t, ts[1] + 0.5, txt("BEING ALLOWED TO DO SOMETHING", 44, IVORY, 2), 1130, 270)
    seq(img, t, ts[1] + 1.2, txt("DOESN'T CHANGE WHAT HAPPENS TO YOU", 44, GOLD, 2), 1130, 350)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, stamp("ONLY ASKING DOES", 900, 130, GOLD, size=64), 960, 590, scale=s, alpha=a, rot=-2, shadow=10)
    seq(img, t, ts[3], ic("off58", ic_officer, 220, 220, 1.3), 330, 860, shadow=8)
    seq(img, t, ts[3] + 0.3, chip("NOBODY IS PAID TO REMIND YOU", 1000, 100, RED, "x", 44), 1100, 860, shadow=8)

# ============================================================ BLOCCO 59
def draw59(img, t):
    ts = starts(59)
    common(img, t, "THREE SENTENCES")
    seq(img, t, ts[0], txt("WRITE DOWN THREE SENTENCES", 56, GOLD, 3), 960, 190, shadow=8)
    lines = [("I NEED HELP FROM THE CURB TO MY GATE", ts[1]), ("MAY I KEEP MY SHOES ON?", ts[2]), ("I'D LIKE A REFUND, NOT A VOUCHER", ts[3])]
    for k, (tx, t0) in enumerate(lines):
        y = 380 + k * 220
        seq(img, t, t0, card(1500, 160, GOLD), 960, y, shadow=12)
        seq(img, t, t0 + 0.2, badge(k + 1), 290, y)
        seq(img, t, t0 + 0.4, txt(tx, 52, IVORY, 2), 1050, y)

# ============================================================ BLOCCO 60
def draw60(img, t):
    ts = starts(60)
    common(img, t, "ONE MORE THING")
    seq(img, t, ts[1], chip("IT WON'T WORK EVERY SINGLE TIME", 1100, 100, RED, "x", 44), 960, 300, shadow=8)
    info(img, t, ts[2], 960, 520, 1500, 220, SAGE, ic("off60", ic_officer, 220, 220, 1.4), "AN AGENT MAY BE BUSY", "OR MAY NOT KNOW THE RULE", 46, 56)
    for k, nm in enumerate(["STAY CALM", "ASK FOR A SUPERVISOR", "SAY THE RULE BY NAME"]):
        seq(img, t, ts[3] + k * 1.5, chip(nm, 520 if k == 0 else 560, 100, GREEN_OK, "ok", 30), 320 + k * 640, 820, shadow=8)

# ============================================================ BLOCCO 61
def draw61(img, t):
    ts = starts(61)
    common(img, t, "THIS WEEK")
    seq(img, t, ts[0], txt("WHAT TO DO THIS WEEK", 62, GOLD, 3), 960, 190, shadow=8)
    items = [("CHECK YOUR LICENSE", "FOR THE STAR", ic_idcard, ts[1]), ("SAVE THE T S A CARES", "NUMBER IN YOUR PHONE", ic_phone, ts[2]),
             ("WRITE THE THREE SENTENCES", "ON A CARD", lambda c, x, y, s: ic_scroll(c, x, y, 1.0 * s), ts[3]), ("OXYGEN OR C P A P?", "CALL YOUR AIRLINE NOW", ic_oxygen, ts[4])]
    for k, (l1, l2, fn, t0) in enumerate(items):
        x = 500 + (k % 2) * 920; y = 450 + (k // 2) * 330
        seq(img, t, t0, card(840, 280, GOLD), x, y, shadow=12)
        seq(img, t, t0 + 0.2, badge(k + 1), x - 340, y - 90, scale=0.7)
        seq(img, t, t0 + 0.3, ic("w61%d" % k, fn, 200, 200, 1.0), x - 230, y + 10)
        seq(img, t, t0 + 0.5, txt(l1, 32, IVORY, 1), x + 120, y - 30)
        seq(img, t, t0 + 0.8, txt(l2, 36, GOLD, 1), x + 120, y + 40)

# ============================================================ BLOCCO 62
def draw62(img, t):
    ts = starts(62)
    common(img, t, "YOUR TURN")
    seq(img, t, ts[0], txt("WHICH OF THESE EIGHT DID YOU NOT KNOW ABOUT?", 48, GOLD, 2), 960, 190, shadow=8)
    for k in range(8):
        seq(img, t, ts[0] + 0.5 + k * 0.15, badge(k + 1), 330 + k * 180, 320, scale=0.7, shadow=4)
    seq(img, t, ts[1], chip("TELL ME IN THE COMMENTS", 1000, 100, GOLD, None, 46), 960, 500, shadow=8)
    seq(img, t, ts[2], txt("SEND THIS VIDEO TO ONE PERSON OVER SIXTY WHO FLIES", 42, IVORY, 2), 960, 660)
    for k, (nm, w) in enumerate([("A PARENT", 460), ("A BROTHER", 460), ("A FRIEND AT CHURCH", 600)]):
        seq(img, t, ts[2] + 1.8 + k * 0.9, chip(nm, w, 100, SAGE, None, 42), 340 + k * 620, 780, shadow=8)
    ban(img, t, ts[3], "IT COULD SAVE THEM A BAD DAY AT THE AIRPORT", cy=950, w=1500, h=96, size=44)

# ============================================================ BLOCCO 63
def thumb(c, cx, cy, s):
    c.poly([(cx - 40 * s, cy - 6 * s), (cx - 10 * s, cy - 6 * s), (cx + 14 * s, cy - 60 * s), (cx + 40 * s, cy - 50 * s), (cx + 26 * s, cy - 6 * s), (cx + 62 * s, cy - 6 * s), (cx + 56 * s, cy + 56 * s), (cx - 40 * s, cy + 56 * s)], fill=GOLD)
    c.rrect((cx - 64 * s, cy - 6 * s, cx - 38 * s, cy + 56 * s), 6, fill=(168, 118, 40))

def draw63(img, t):
    ts = starts(63)
    common(img, t, "BEFORE YOU GO")
    seq(img, t, ts[0] + 0.2, ic("th63", thumb, 220, 220, 1.8), 560, 400, shadow=10)
    seq(img, t, ts[0] + 0.5, txt("LIKE", 80, GOLD, 4), 560, 600)
    seq(img, t, ts[0] + 1.5, chip("SUBSCRIBE", 560, 130, RED, None, 64), 1340, 400, shadow=10)
    seq(img, t, ts[0] + 3.0, txt("THE SENIOR ADVANTAGE", 64, IVORY, 3), 960, 760)
    ban(img, t, ts[0] + 4.4, "SO YOU DON'T MISS THE NEXT ONE", cy=930, w=1300, h=96, size=48)

# ============================================================ BLOCCO 64
def draw64(img, t):
    ts = starts(64)
    a0 = ease(seg(t, 0, .5))
    put(img, tspr("BEFORE YOU GO", FONT_SANS, 44, SAGE, track=18), 960, 100, alpha=a0)
    put(img, tspr("ALWAYS CONFIRM", FONT_SANS, 112, IVORY), 560, 340 - 30 * (1 - ease(seg(t, .3, .5))), alpha=ease(seg(t, .3, .5)))
    put(img, tspr("BEFORE YOU RELY", FONT_SANS, 112, GOLD), 560, 480 - 30 * (1 - ease(seg(t, .9, .5))), alpha=ease(seg(t, .9, .5)))
    bp = pop(t, 1.4, 0.5)
    def panel_():
        c = Cv(990, 400)
        c.rrect((3, 3, 987, 397), 36, fill=CARD, outline=SAGE_D, width=5)
        return c.done()
    if bp[2] > 0:
        put(img, cache("p64", panel_), 595, 790, scale=bp[0], alpha=bp[1], shadow=16)
    lines = [("Rules, amounts and ages change", IVORY, ts[0] + 0.3), ("and differ by location and plan.", IVORY, ts[0] + 1.6),
             ("Always confirm with the official source", GOLD, ts[1] + 0.2), ("before you rely on them.", GOLD, ts[1] + 1.3),
             ("This is general information,", SAGE, ts[2] + 0.2), ("not financial advice.", SAGE, ts[2] + 1.2)]
    for i, (s_, col, st) in enumerate(lines):
        a = ease(seg(t, st, .5))
        if a > 0:
            put(img, tspr(s_, FONT_SANS_M if i > 3 else FONT_SANS, 36, col), 595, 650 + i * 58 - 20 * (1 - a), alpha=a)
    a = ease(seg(t, 2.0, .6))
    if a > 0:
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(lay)
        for x in range(1170, 1800, 60):
            g.line([(x, 250), (x + 34, 250)], fill=GOLD + (255,), width=5); g.line([(x, 710), (x + 34, 710)], fill=GOLD + (255,), width=5)
        for y in range(250, 710, 60):
            g.line([(1150, y), (1150, y + 34)], fill=GOLD + (255,), width=5); g.line([(1830, y), (1830, y + 34)], fill=GOLD + (255,), width=5)
        lay.putalpha(lay.getchannel("A").point(lambda v: int(v * a)))
        img.paste(lay, (0, 0), lay)
        put(img, tspr("WATCH NEXT", FONT_SANS, 54, GOLD), 1490, 790, alpha=a)
    put(img, tspr("THANK YOU FOR WATCHING", FONT_SANS, 40, SAGE), 1490, 880, alpha=ease(seg(t, 5.5, .5)))

DRAW = {51: draw51, 52: draw52, 53: draw53, 54: draw54, 55: draw55, 56: draw56, 57: draw57, 58: draw58, 59: draw59, 60: draw60, 61: draw61, 62: draw62, 63: draw63, 64: draw64}

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
