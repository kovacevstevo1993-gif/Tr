"""Video lungo 4 (BOLLETTE) - blocchi 56-72 (USDA 504, bonus, ordine giusto, chiusura, disclaimer). 1920x1080, 30 fps.
Durate (timeline utente 08/10/2026): B56 359, B57 300, B58 357, B59 422, B60 333, B61 311, B62 327, B63 281, B64 392, B65 324, B66 390, B67 299, B68 288, B69 477, B70 429, B71 218, B72 378.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long4_b56_72.py <blocco>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b51_55 import *

DUR = {56: 359, 57: 300, 58: 357, 59: 422, 60: 333, 61: 311, 62: 327, 63: 281, 64: 392, 65: 324, 66: 390, 67: 299, 68: 288, 69: 477, 70: 429, 71: 218, 72: 378}
PHRASES = {
    56: ["The grant can be up to ten thousand dollars.", "It's used to remove health and safety hazards from your home.", "And if you don't sell the house within three years, you don't pay it back."],
    57: ["If you need more, there's also a loan of up to forty thousand dollars,", "at a fixed one percent interest, over twenty years.", "Together, up to fifty thousand dollars."],
    58: ["Now, who qualifies?", "You must own the home and live in it.", "Your income must be under the very low limit for your county.", "And you must be unable to get affordable credit somewhere else."],
    59: ["And here's the part people miss.", "It's for rural areas, and the U S D A decides what counts as rural.", "So don't guess.", "Type your address on the U S D A eligibility map, and you'll know in one minute."],
    60: ["Applications are accepted all year at your local Rural Development office.", "But funding depends on your area,", "so don't wait until the furnace is already broken."],
    61: ["Who does this help most?", "Older homeowners in small towns, with a house that's paid off but getting old.", "The house is worth something, but the repairs are not affordable."],
    62: ["Quick recap.", "Heat, energy, phone, groceries, the food box, the bus, and home repairs.", "Seven bills, seven programs, all official."],
    63: ["Now, the bonus I promised.", "If all of this feels like too many phone calls,", "there's one number that can point you to your local help for older adults."],
    64: ["It's the Eldercare Locator.", "One, eight hundred, six seven seven, one one one six.", "They connect you with your local agency on aging,", "and those people know these programs in your area."],
    65: ["And now, the thing that connects these bills.", "Most people apply for these one at a time, in random order.", "And they miss help they had already qualified for."],
    66: ["Here's the right order.", "Start with snap.", "Because a snap approval can qualify you for Lifeline without proving your income again.", "And S S I counts for Lifeline and for weatherization too."],
    67: ["Then do heating help in the fall, because the money runs out.", "Some states use that same income limit for weatherization.", "One yes can lead to the next one."],
    68: ["Because here's the truth.", "Being eligible doesn't lower a single bill.", "Only the application does.", "And no agency is going to fill it out for you."],
    69: ["So here's what to do this week, and none of it costs a dollar.", "Call the energy line.", "Check your address on the U S D A map.", "Ask your transit agency for the senior card.", "And if you are close to the snap limits, apply."],
    70: ["Which of these seven did you not know about?", "Tell me in the comments.", "And send this video to one person over sixty, a parent, a neighbor, a friend at church.", "It could save them hundreds of dollars this winter."],
    71: ["If this helped you, tap like and subscribe to The Senior Advantage,", "so you don't miss the next one."],
    72: ["Rules, amounts and ages change and differ by location and plan.", "Always confirm with the official source before you rely on them.", "This is general information, not financial advice."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def thumb_up():
    def fn(c):
        c.rrect((8, 130, 90, 308), 16, fill=GOLD, outline=(190, 140, 60), width=6)
        c.poly([(104, 142), (176, 20), (214, 26), (196, 122), (284, 122), (294, 150), (278, 290), (250, 308), (104, 308)], fill=GOLD)
        for y in (178, 220, 262):
            c.line([(128, y), (252, y)], (190, 140, 60), 4)
    return sprite("thumb4", 300, 320, fn)

def bell4():
    def fn(c):
        c.ell((90, 2, 120, 32), fill=(190, 140, 60))
        c.ell((30, 18, 180, 170), fill=GOLD, outline=(190, 140, 60), width=5)
        c.poly([(30, 96), (180, 96), (200, 174), (10, 174)], fill=GOLD)
        c.rrect((8, 166, 202, 188), 10, fill=(214, 160, 80), outline=(190, 140, 60), width=4)
        c.ell((84, 182, 126, 224), fill=(190, 140, 60))
    return sprite("bell4", 210, 230, fn)

def row_card(w, h, icon, l1, l2, col):
    def fn(c):
        c.rrect((5, 5, w - 5, h - 5), 34, fill=PANEL_FILL, outline=col, width=7)
        icon(c, 120, h / 2, 1.1)
        c.text((w / 2 + 70, h / 2 - 22), l1, FONT_SANS, 40, IVORY, track=2)
        c.text((w / 2 + 70, h / 2 + 28), l2, FONT_SANS, 28, col, track=1)
    return sprite(("rowc", w, h, l1, l2), w, h, fn)

# ============================================================ BLOCCO 56
def draw56(img, t):
    ts = starts(56)
    common(img, t, "THE GRANT")
    seq(img, t, ts[0] - 0.05, txt("THE GRANT", 80, GOLD, 6), 960, 190, shadow=10)
    slide_in(img, t, ts[0], panel(760, 420, border=GOLD), 500, 520, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.2, txt("UP TO", 44, SAGE, 6), 500, 400)
    counter(img, t, ts[0] + 0.4, 1.6, "$", 10000, "", 130, GOLD, 500, 520)
    seq(img, t, ts[0] + 1.2, stamp("A GRANT, NOT A LOAN", 520, 90, SAGE, size=34), 500, 650, rot=-2, shadow=8)
    slide_in(img, t, ts[1], panel(900, 420, border=SAGE), 1400, 520, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.3, sprite("hz56", 260, 240, lambda c: (ic_house(c, 130, 130, 2.0, col=IVORY), warn_tri(c, 200, 70, 0.9))), 1130, 480, shadow=8)
    seq(img, t, ts[1] + 0.7, sprite("sf56", 220, 240, lambda c: (c.poly([(110, 10), (200, 40), (200, 130), (110, 230), (20, 130), (20, 40)], fill=GOLD, ), check_ic(c, 110, 120, 1.7, GREEN_D))), 1470, 480, shadow=8)
    seq(img, t, ts[1] + 1.1, txt("REMOVE HEALTH AND", 36, IVORY, 3), 1400, 620)
    seq(img, t, ts[1] + 1.25, txt("SAFETY HAZARDS", 44, GOLD, 3), 1400, 675)
    seq(img, t, ts[2], sprite("c3y56", 520, 220, lambda c: (c.rrect((5, 5, 515, 215), 36, fill=PANEL_FILL, outline=GOLD, width=7), ic_cal(c, 110, 110, 1.3, "3"), c.text((340, 82), "YEARS", FONT_SANS, 44, GOLD, track=4), c.text((340, 136), "NO REPAYMENT", FONT_SANS, 28, IVORY, track=2))), 330, 900, shadow=10, scale=0.8)
    ban(img, t, ts[2] + 0.6, "DON'T SELL WITHIN 3 YEARS? YOU KEEP IT", cy=985, cx=1250, w=1180, size=34)

# ============================================================ BLOCCO 57
def draw57(img, t):
    ts = starts(57)
    common(img, t, "THE LOAN")
    seq(img, t, ts[0] - 0.05, txt("NEED MORE?", 70, IVORY, 6), 960, 190, shadow=10)
    slide_in(img, t, ts[0], panel(760, 420, border=SAGE), 500, 520, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.2, txt("A LOAN OF UP TO", 38, SAGE, 4), 500, 400)
    counter(img, t, ts[0] + 0.4, 1.6, "$", 40000, "", 120, GOLD, 500, 520)
    slide_in(img, t, ts[1], panel(900, 420, border=GOLD), 1400, 520, dx=60, dur=0.55, shadow=14)
    seq(img, t, ts[1] + 0.2, txt("1%", 150, GOLD, 4), 1200, 480)
    seq(img, t, ts[1] + 0.5, txt("FIXED INTEREST", 34, IVORY, 3), 1200, 610)
    seq(img, t, ts[1] + 0.9, sprite("y20", 300, 280, lambda c: ic_cal(c, 150, 130, 2.1, "20")), 1600, 470, shadow=8)
    seq(img, t, ts[1] + 1.2, txt("YEARS", 44, GOLD, 5), 1600, 640)
    pa = ease(seg(t, ts[2], 0.6))
    if pa > 0:
        w1 = int(280 * pa)
        put(img, sprite(("g57", w1), max(8, w1), 100, lambda c: c.rrect((2, 2, max(8, w1) - 2, 98), 16, fill=SAGE_D)), 330 + w1 / 2, 860)
    pb = ease(seg(t, ts[2] + 0.6, 0.8))
    if pb > 0:
        w2 = int(1100 * pb)
        put(img, sprite(("l57", w2), max(8, w2), 100, lambda c: c.rrect((2, 2, max(8, w2) - 2, 98), 16, fill=GOLD)), 640 + w2 / 2, 860)
    seq(img, t, ts[2] + 0.3, txt("GRANT $10K", 32, GREEN_D, 2), 470, 860)
    seq(img, t, ts[2] + 1.2, txt("LOAN $40K", 40, GREEN_D, 3), 1190, 860)
    seq(img, t, ts[2] + 1.5, stamp("TOGETHER: UP TO $50,000", 760, 100, GOLD, size=40), 1220, 960, rot=-1, shadow=10)

# ============================================================ BLOCCO 58
def draw58(img, t):
    ts = starts(58)
    common(img, t, "WHO QUALIFIES")
    seq(img, t, ts[0], stamp("WHO QUALIFIES?", 640, 120, GOLD, size=56), 960, 200, shadow=12)
    cards = [(lambda c, x, y, s: (ic_house(c, x - 40, y, 1.0, col=IVORY), ic_person(c, x + 50, y + 12, 0.9, col=GOLD)), "OWN IT", "AND LIVE IN IT", GOLD, ts[1]),
             (lambda c, x, y, s: [ic_coin(c, x - 50 + k * 50, y + (k % 2) * 8, 30) for k in range(3)], "INCOME UNDER", "THE VERY LOW LIMIT", SAGE, ts[2]),
             (lambda c, x, y, s: (c.rrect((x - 60, y - 50, x + 60, y + 50), 12, fill=SAGE_D), c.text((x, y), "BANK", FONT_SANS, 30, IVORY), ic_x(c, x, y, 1.6, RED, 12)), "NO AFFORDABLE", "CREDIT ELSEWHERE", CORAL, ts[3])]
    for k, (ic, l1, l2, col, st) in enumerate(cards):
        slide_in(img, t, st, sprite(("q58", k), 560, 560, lambda c, ic=ic, l1=l1, l2=l2, col=col: (c.rrect((5, 5, 555, 555), 40, fill=PANEL_FILL, outline=col, width=8), ic(c, 280, 210, 1.0), c.text((280, 400), l1, FONT_SANS, 44, IVORY, track=2), c.text((280, 460), l2, FONT_SANS, 32, col, track=2))), 340 + k * 620, 600, dy=50, dur=0.55, shadow=14, scale=0.93)
        check_at(img, t, st + 0.8, 340 + k * 620 + 210, 380, 1.1)

# ============================================================ BLOCCO 59
def draw59(img, t):
    ts = starts(59)
    common(img, t, "RURAL AREAS")
    seq(img, t, ts[0], stamp("THE PART PEOPLE MISS", 760, 120, RED, size=48), 960, 200, shadow=12, rot=-1)
    seq(img, t, ts[1], pin_map(), 520, 560, shadow=14)
    for k, (dx, dy, col) in enumerate(((-180, -70, GOLD), (60, 30, SAGE), (180, -60, CORAL))):
        seq(img, t, ts[1] + 0.5 + k * 0.3, sprite(("p59", k), 90, 130, lambda c, col=col: ic_pin(c, 45, 55, 1.0, col=col)), 520 + dx, 560 + dy)
    seq(img, t, ts[1] + 1.5, txt("RURAL, AS THE U S D A DEFINES IT", 32, IVORY, 2), 520, 830)
    seq(img, t, ts[2], stamp("DON'T GUESS", 400, 100, GOLD, size=44), 1100, 380, rot=-3, shadow=10)
    slide_in(img, t, ts[3], sprite("sb59", 760, 130, lambda c: (c.rrect((4, 4, 756, 126), 60, fill=IVORY, outline=GOLD, width=7), magnifier(c, 82, 64, 26, GREEN_D, 9), c.text((420, 66), "TYPE YOUR ADDRESS", FONT_SANS_M, 40, GREEN_D))), 1400, 560, dy=40, dur=0.5, shadow=10)
    seq(img, t, ts[3] + 0.5, txt("U S D A ELIGIBILITY MAP", 40, GOLD, 3), 1400, 680)
    seq(img, t, ts[3] + 1.2, sprite("cl59", 200, 200, lambda c: ic_clock(c, 100, 100, 90, 0.5)), 1100, 850, shadow=8, scale=0.8)
    seq(img, t, ts[3] + 1.5, txt("YOU'LL KNOW IN ONE MINUTE", 40, IVORY, 3), 1560, 850)

# ============================================================ BLOCCO 60
def draw60(img, t):
    ts = starts(60)
    common(img, t, "HOW AND WHEN")
    slide_in(img, t, ts[0], panel(1000, 440, border=GOLD), 560, 440, dx=-60, dur=0.55, shadow=14)
    for k in range(12):
        s, a, p = pop(t, ts[0] + 0.2 + k * 0.08, 0.3)
        if p > 0:
            put(img, sprite(("mo60", k), 90, 100, lambda c, k=k: (c.rrect((3, 3, 87, 97), 14, fill=IVORY), c.text((45, 50), "JFMAMJJASOND"[k], FONT_SANS, 46, GREEN_D))), 200 + (k % 6) * 120, 340 + (k // 6) * 130, scale=s, alpha=a)
    seq(img, t, ts[0] + 1.4, txt("ALL YEAR", 56, GOLD, 5), 560, 600)
    seq(img, t, ts[0] + 1.8, sprite("rd60", 300, 240, lambda c: ic_gov(c, 150, 110, 1.6)), 1500, 380, shadow=8)
    seq(img, t, ts[0] + 2.2, txt("YOUR LOCAL", 36, SAGE, 3), 1500, 540)
    seq(img, t, ts[0] + 2.4, txt("RURAL DEVELOPMENT OFFICE", 36, IVORY, 3), 1500, 590)
    seq(img, t, ts[1], sprite("fund60", 640, 220, lambda c: (c.rrect((5, 5, 635, 215), 36, fill=PANEL_FILL, outline=SAGE, width=7), c.text((320, 80), "FUNDING DEPENDS", FONT_SANS, 40, IVORY, track=2), c.text((320, 140), "ON YOUR AREA", FONT_SANS, 40, GOLD, track=2))), 560, 760, shadow=10)
    seq(img, t, ts[2], sprite("fur60", 400, 300, lambda c: (ic_furnace(c, 200, 150, 2.0, cold=True), ic_x(c, 200, 150, 2.4, RED, 14))), 1380, 780, shadow=10, scale=0.85)
    ban(img, t, ts[2] + 0.4, "DON'T WAIT UNTIL IT'S ALREADY BROKEN", cy=985, w=1240, size=48)

# ============================================================ BLOCCO 61
def draw61(img, t):
    ts = starts(61)
    common(img, t, "WHO IT HELPS MOST")
    seq(img, t, ts[0], stamp("WHO IT HELPS MOST", 760, 120, GOLD, size=52), 960, 200, shadow=12)
    seq(img, t, ts[1], sprite("sm61", 480, 360, lambda c: (ic_house(c, 130, 200, 2.0, col=(220, 214, 196)), ic_house(c, 320, 220, 1.4, col=(200, 194, 176), roof=(150, 100, 90)), ic_person(c, 220, 260, 1.0, col=GOLD))), 460, 560, shadow=12)
    seq(img, t, ts[1] + 0.6, txt("SMALL TOWN", 40, IVORY, 4), 460, 790)
    seq(img, t, ts[1] + 0.9, stamp("PAID OFF", 300, 90, SAGE, size=40), 460, 870, rot=-3, shadow=8)
    seq(img, t, ts[1] + 1.3, sprite("old61", 200, 200, lambda c: ic_house(c, 100, 100, 1.5, col=(170, 160, 140), roof=(120, 90, 80))), 820, 380, shadow=8, scale=0.8)
    seq(img, t, ts[1] + 1.5, txt("GETTING OLD", 28, SAGE, 3), 820, 500)
    slide_in(img, t, ts[2], sprite("sc61", 900, 480, lambda c: (c.rrect((5, 5, 895, 475), 40, fill=PANEL_FILL, outline=GOLD, width=7), c.line([(450, 120), (450, 250)], SAGE, 10), c.line([(200, 250), (700, 250)], SAGE, 10), c.line([(200, 250), (200, 300)], SAGE, 6), c.line([(700, 250), (700, 300)], SAGE, 6), c.rrect((90, 300, 310, 360), 10, fill=GOLD), c.text((200, 330), "WORTH SOMETHING", FONT_SANS, 24, GREEN_D, track=1), c.rrect((590, 300, 810, 360), 10, fill=CORAL), c.text((700, 330), "NOT AFFORDABLE", FONT_SANS, 24, GREEN_D, track=1), ic_house(c, 200, 190, 0.6, col=IVORY), ic_repair(c, 700, 190, 0.6), c.text((450, 430), "THE HOUSE VS THE REPAIRS", FONT_SANS, 30, SAGE, track=3))), 1400, 600, dx=60, dur=0.55, shadow=14, scale=0.95)

# ============================================================ BLOCCO 62
def draw62(img, t):
    ts = starts(62)
    common(img, t, "QUICK RECAP")
    seq(img, t, ts[0] - 0.05, stamp("QUICK RECAP", 520, 120, GOLD, size=58), 960, 200, shadow=12, rot=-1)
    items = [(ic_flame, "HEAT"), (ic_bolt, "ENERGY"), (ic_phone, "PHONE"), (ic_bag, "GROCERIES"), (ic_box, "FOOD BOX"), (ic_bus, "THE BUS"), (ic_repair, "REPAIRS")]
    for k, (fn, name) in enumerate(items):
        x, y = 260 + (k % 4) * 470, 420 + (k // 4) * 330
        s, a, p = pop(t, ts[1] + 0.1 + k * 0.38, 0.4)
        if p > 0:
            put(img, sprite(("rc62", k), 330, 270, lambda c, fn=fn, name=name: (c.rrect((5, 5, 325, 265), 36, fill=PANEL_FILL, outline=GOLD, width=7), fn(c, 165, 110, 1.1), c.text((165, 220), name, FONT_SANS, 38, IVORY, track=2))), x, y, scale=s, alpha=a, shadow=10)
            check_at(img, t, ts[1] + 0.45 + k * 0.38, x + 120, y - 100, 0.8)
    ban(img, t, ts[2] + 0.2, "7 BILLS, 7 PROGRAMS, ALL OFFICIAL", cy=985, w=1180, size=54)

# ============================================================ BLOCCO 63
def draw63(img, t):
    ts = starts(63)
    common(img, t, "THE BONUS")
    seq(img, t, ts[0], stamp("THE BONUS", 460, 120, GOLD, size=58), 960, 200, shadow=12, rot=-2)
    for k in range(5):
        s, a, p = pop(t, ts[1] + 0.2 + k * 0.3, 0.4)
        if p > 0:
            put(img, sprite(("ph63", k), 140, 200, lambda c: ic_phone(c, 70, 100, 1.2)), 380 + k * 170, 560 + (k % 2) * 40, scale=s, alpha=a * 0.8, rot=(-8 if k % 2 else 8))
    seq(img, t, ts[1] + 1.8, txt("TOO MANY PHONE CALLS?", 44, IVORY, 3), 800, 760)
    s, a, p = pop(t, ts[2], 0.5)
    if p > 0:
        put(img, sprite("one63", 640, 300, lambda c: (c.rrect((5, 5, 635, 295), 44, fill=PANEL_FILL, outline=GOLD, width=9), ic_phone(c, 120, 150, 1.5), c.text((390, 120), "ONE", FONT_SANS, 90, GOLD, track=4), c.text((390, 210), "NUMBER", FONT_SANS, 70, IVORY, track=4))), 1500, 560, scale=s, alpha=a, shadow=16)
        burst(img, t, ts[2], 1500, 560, n=12, color=GOLD, rad=260, seed=63)
    seq(img, t, ts[2] + 0.8, txt("LOCAL HELP FOR OLDER ADULTS", 36, SAGE, 3), 1500, 760)

# ============================================================ BLOCCO 64
def draw64(img, t):
    ts = starts(64)
    common(img, t, "ELDERCARE LOCATOR")
    seq(img, t, ts[0], txt("ELDERCARE", 120, GOLD, 6), 960, 220, shadow=10)
    seq(img, t, ts[0] + 0.4, txt("LOCATOR", 120, IVORY, 6), 960, 350, shadow=10)
    slide_in(img, t, ts[1], panel(1240, 220, border=GOLD), 960, 570, dy=40, dur=0.5, shadow=14)
    typed(img, t, ts[1] + 0.2, ts[2] - 0.3, "1-800-677-1116", 130, GOLD, 960, 570, track=4)
    seq(img, t, ts[2], sprite("ph64", 200, 200, lambda c: ic_phone(c, 100, 100, 1.5)), 420, 850, shadow=8)
    p = ease(seg(t, ts[2] + 0.4, 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 620, 850, alpha=p)
    seq(img, t, ts[2] + 0.8, sprite("aoa64", 760, 260, lambda c: (c.rrect((5, 5, 755, 255), 40, fill=PANEL_FILL, outline=SAGE, width=7), ic_gov(c, 130, 130, 1.2), c.text((470, 100), "YOUR LOCAL AGENCY", FONT_SANS, 38, IVORY, track=2), c.text((470, 160), "ON AGING", FONT_SANS, 52, GOLD, track=3))), 1150, 850, shadow=12, scale=0.9)
    ban(img, t, ts[3] + 0.3, "THEY KNOW THESE PROGRAMS WHERE YOU LIVE", cy=985, w=1320, size=46)

# ============================================================ BLOCCO 65
def draw65(img, t):
    ts = starts(65)
    common(img, t, "WHAT CONNECTS THEM")
    icons = [ic_flame, ic_bolt, ic_phone, ic_bag, ic_box, ic_bus, ic_repair]
    xs = [200, 460, 720, 980, 1240, 1500, 1760]
    p = ease(seg(t, ts[0], 0.6))
    if p > 0:
        put(img, sprite("ch65", 1700, 60, lambda c: link_chain(c, 20, 30, 44)), 980, 380, alpha=p)
    for k, fn in enumerate(icons):
        s, a, pp = pop(t, ts[0] + 0.2 + k * 0.2, 0.4)
        if pp > 0:
            put(img, sprite(("ic65", k), 200, 200, lambda c, fn=fn: (c.ell((6, 6, 194, 194), fill=PANEL_FILL, outline=GOLD, width=6), fn(c, 100, 98, 0.9))), xs[k], 380, scale=s, alpha=a, shadow=8)
    seq(img, t, ts[1], txt("ONE AT A TIME", 56, IVORY, 5), 560, 620)
    for k, n in enumerate((4, 1, 6, 2)):
        s, a, pp = pop(t, ts[1] + 0.3 + k * 0.25, 0.4)
        if pp > 0:
            put(img, sprite(("rn65", n), 120, 120, lambda c, n=n: (c.ell((6, 6, 114, 114), fill=(70, 38, 36), outline=RED, width=6), c.text((60, 64), str(n), FONT_SERIF, 64, IVORY))), 360 + k * 170, 760, scale=s, alpha=a)
    seq(img, t, ts[1] + 1.4, stamp("RANDOM ORDER", 460, 100, RED, size=44), 1250, 760, rot=-3, shadow=8)
    seq(img, t, ts[2], stamp("HELP ALREADY QUALIFIED FOR: MISSED", 1100, 120, RED, size=40), 1100, 940, rot=-1, shadow=12)

# ============================================================ BLOCCO 66
def draw66(img, t):
    ts = starts(66)
    common(img, t, "THE RIGHT ORDER")
    seq(img, t, ts[0], stamp("THE RIGHT ORDER", 760, 120, GOLD, size=54), 960, 200, shadow=12)
    s, a, p = pop(t, ts[1], 0.5)
    if p > 0:
        put(img, numbadge(1, 200), 260, 480, scale=s, alpha=a, shadow=12)
    slide_in(img, t, ts[1] + 0.2, ebt(), 620, 480, dx=-40, dur=0.5, shadow=14, scale=0.7)
    p = ease(seg(t, ts[2], 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 930, 480, alpha=p)
    s, a, p = pop(t, ts[2] + 0.2, 0.5)
    if p > 0:
        put(img, row_card(760, 240, lambda c, x, y, sc: ic_phone(c, x, y, 1.0), "LIFELINE", "NO NEW PROOF OF INCOME", GOLD), 1400, 480, scale=s, alpha=a, shadow=14)
    s, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, sprite("ssi66", 400, 220, lambda c: (c.rrect((5, 5, 395, 215), 40, fill=PANEL_FILL, outline=SAGE, width=7), c.text((200, 110), "S S I", FONT_SANS, 100, GOLD, track=6))), 360, 800, scale=s, alpha=a, shadow=12)
    for k, (fn, name, x) in enumerate(((ic_phone, "LIFELINE", 1000), (ic_house_w, "WEATHERIZATION", 1480))):
        st = ts[3] + 0.5 + k * 0.5
        pp = ease(seg(t, st, 0.5))
        if pp > 0:
            put(img, rarrow(GOLD, 120, 80), 640 + k * 0, 800 + (k * 0), alpha=pp * (1 if k == 0 else 0), scale=0.8)
        s, a, p = pop(t, st + 0.1, 0.45)
        if p > 0:
            put(img, sprite(("t66", k), 440, 200, lambda c, fn=fn, name=name: (c.rrect((5, 5, 435, 195), 36, fill=PANEL_FILL, outline=GOLD, width=7), fn(c, 90, 100, 0.9), c.text((285, 100), name, FONT_SANS, 24, IVORY, track=1))), x, 800, scale=s, alpha=a, shadow=10)
            check_at(img, t, st + 0.5, x + 190, 710, 0.8)

def ic_house_w(c, cx, cy, s):
    ic_house(c, cx, cy, s, col=IVORY)
    ic_flame(c, cx, cy + 14 * s, 0.35 * s)

# ============================================================ BLOCCO 67
def draw67(img, t):
    ts = starts(67)
    common(img, t, "THEN THE FALL")
    slide_in(img, t, ts[0], sprite("heat67", 640, 460, lambda c: (c.rrect((5, 5, 635, 455), 40, fill=PANEL_FILL, outline=FLAME, width=8), ic_flame(c, 150, 190, 1.8), ic_cal(c, 450, 190, 1.4, "OCT"), c.text((320, 390), "HEATING HELP IN THE FALL", FONT_SANS, 32, IVORY, track=2))), 500, 540, dx=-60, dur=0.55, shadow=14)
    seq(img, t, ts[0] + 0.8, txt("THE MONEY RUNS OUT", 34, RED, 3), 500, 830)
    slide_in(img, t, ts[1], sprite("limit67", 640, 460, lambda c: (c.rrect((5, 5, 635, 455), 40, fill=PANEL_FILL, outline=GOLD, width=8), c.text((320, 120), "SAME", FONT_SANS, 60, SAGE, track=5), c.text((320, 200), "INCOME LIMIT", FONT_SANS, 60, GOLD, track=3), c.text((320, 300), "IN SOME STATES", FONT_SANS, 34, IVORY, track=3), ic_house_w(c, 320, 390, 0.5))), 1400, 540, dx=60, dur=0.55, shadow=14)
    p = ease(seg(t, ts[1] + 0.4, 0.5))
    if p > 0:
        put(img, rarrow(GOLD, 150, 100), 950, 540, alpha=p)
    seq(img, t, ts[1] + 0.8, txt("FOR WEATHERIZATION", 36, GOLD, 3), 1400, 830)
    ban(img, t, ts[2] + 0.2, "ONE YES CAN LEAD TO THE NEXT ONE", cy=985, w=1220, size=50)

# ============================================================ BLOCCO 68
def draw68(img, t):
    ts = starts(68)
    common(img, t, "THE TRUTH")
    seq(img, t, ts[0], stamp("HERE'S THE TRUTH", 640, 120, GOLD, size=54), 960, 200, shadow=12, rot=-1)
    slide_in(img, t, ts[1], sprite("elig68", 520, 360, lambda c: (c.rrect((5, 5, 515, 355), 40, fill=PANEL_FILL, outline=SAGE, width=7), c.text((260, 100), "ELIGIBLE", FONT_SANS, 64, IVORY, track=4), check_ic(c, 260, 220, 2.2, GOLD))), 400, 520, dx=-50, dur=0.55, shadow=14)
    s, a, p = pop(t, ts[1] + 0.7, 0.45)
    if p > 0:
        put(img, bill_paper(), 960, 520, scale=0.62 * s, alpha=a, shadow=12)
        put(img, stamp("STILL FULL PRICE", 440, 90, RED, size=36), 960, 780, scale=s, alpha=a, rot=-3, shadow=8)
    seq(img, t, ts[2], sprite("form68", 300, 380, lambda c: (c.rrect((6, 6, 294, 374), 20, fill=IVORY, outline=(206, 200, 186), width=5), c.rrect((6, 6, 294, 80), 20, fill=GREEN_L), c.text((150, 44), "APPLY", FONT_SANS, 42, IVORY, track=4), [c.rrect((40, 112 + k * 52, 260, 126 + k * 52), 6, fill=(206, 212, 206)) for k in range(4)], c.ell((190, 280, 270, 360), fill=GOLD), c.line([(208, 322), (226, 340), (254, 300)], GREEN_D, 10))), 1480, 480, shadow=14)
    seq(img, t, ts[2] + 0.6, txt("ONLY THE APPLICATION", 36, GOLD, 3), 1480, 730)
    seq(img, t, ts[2] + 0.8, txt("LOWERS A BILL", 36, GOLD, 3), 1480, 780)
    seq(img, t, ts[3], stamp("NO AGENCY FILLS IT OUT FOR YOU", 940, 110, RED, size=38), 960, 940, rot=-1, shadow=12)

# ============================================================ BLOCCO 69
def draw69(img, t):
    ts = starts(69)
    common(img, t, "THIS WEEK")
    seq(img, t, ts[0], stamp("THIS WEEK", 480, 110, GOLD, size=56), 560, 190, shadow=12, rot=-1)
    seq(img, t, ts[0] + 0.8, stamp("NONE OF IT COSTS A DOLLAR", 780, 90, SAGE, size=36), 1400, 190, rot=2, shadow=8)
    rows = [(lambda c, x, y, s: ic_phone(c, x, y, 0.9), "CALL THE ENERGY LINE", "1-866-674-6327", ts[1]),
            (lambda c, x, y, s: ic_pin(c, x, y, 1.0), "CHECK YOUR ADDRESS", "ON THE U S D A MAP", ts[2]),
            (lambda c, x, y, s: ic_bus(c, x, y, 0.8), "ASK FOR THE SENIOR CARD", "AT YOUR TRANSIT AGENCY", ts[3]),
            (lambda c, x, y, s: c.text((x, y), "snap", FONT_SANS, 40, GOLD, track=2), "CLOSE TO THE snap LIMITS?", "APPLY", ts[4])]
    for k, (ic, l1, l2, st) in enumerate(rows):
        slide_in(img, t, st, sprite(("r69", k), 1500, 170, lambda c, ic=ic, l1=l1, l2=l2: (c.rrect((5, 5, 1495, 165), 36, fill=PANEL_FILL, outline=GOLD, width=7), ic(c, 130, 85, 1.0), c.text((760, 62), l1, FONT_SANS, 46, IVORY, track=3), c.text((760, 120), l2, FONT_SANS, 36, GOLD, track=3))), 960, 330 + k * 190, dx=-60, dur=0.5, shadow=10)
        check_at(img, t, st + 0.9, 1640, 330 + k * 190, 0.9)

# ============================================================ BLOCCO 70
def draw70(img, t):
    ts = starts(70)
    common(img, t, "YOUR TURN")
    seq(img, t, ts[0], sprite("q70", 1080, 190, lambda c: (c.rrect((6, 6, 1074, 160), 60, fill=PANEL_FILL, outline=GOLD, width=8), c.poly([(100, 156), (170, 156), (80, 188)], fill=PANEL_FILL), c.text((540, 84), "WHICH ONE DID YOU NOT KNOW?", FONT_SANS, 58, GOLD, track=2))), 960, 230, shadow=12)
    icons = [ic_flame, ic_bolt, ic_phone, ic_bag, ic_box, ic_bus, ic_repair]
    for k, fn in enumerate(icons):
        s, a, p = pop(t, ts[0] + 0.5 + k * 0.15, 0.35)
        if p > 0:
            put(img, sprite(("i70", k), 170, 170, lambda c, fn=fn: (c.ell((4, 4, 166, 166), fill=PANEL_FILL, outline=SAGE, width=5), fn(c, 85, 85, 0.75))), 260 + k * 235, 440, scale=s, alpha=a, shadow=6)
    seq(img, t, ts[1], txt("TELL ME IN THE COMMENTS", 52, IVORY, 4), 960, 600, shadow=8)
    seq(img, t, ts[1] + 0.2, sprite("cm70", 200, 160, lambda c: (c.rrect((6, 6, 194, 120), 30, fill=GOLD), c.poly([(40, 116), (80, 116), (36, 154)], fill=GOLD), [c.ell((50 + k * 44, 54, 74 + k * 44, 78), fill=GREEN_D) for k in range(3)])), 1560, 600, scale=0.9)
    for k, (name, x) in enumerate((("A PARENT", 420), ("A NEIGHBOR", 860), ("A FRIEND AT CHURCH", 1380))):
        s, a, p = pop(t, ts[2] + 0.3 + k * 0.5, 0.4)
        if p > 0:
            put(img, sprite(("fr70", k), 400, 250, lambda c, k=k, name=name: (c.rrect((5, 5, 395, 245), 36, fill=PANEL_FILL, outline=GOLD, width=7), ic_person(c, 200, 110, 1.3, col=[GOLD, SAGE, CORAL][k]), c.text((200, 210), name, FONT_SANS, 28, IVORY, track=2))), x, 835, scale=s * 0.85, alpha=a, shadow=10)
    seq(img, t, ts[2], txt("SEND THIS VIDEO TO ONE PERSON OVER 60", 40, GOLD, 3), 960, 685)
    ban(img, t, ts[3] + 0.3, "COULD SAVE THEM HUNDREDS THIS WINTER", cy=985, w=1180, size=46)

# ============================================================ BLOCCO 71
def draw71(img, t):
    ts = starts(71)
    common(img, t, "THE SENIOR ADVANTAGE")
    seq(img, t, ts[0], thumb_up(), 560, 440, shadow=14, scale=1.1, rot=-8 + 3 * math.sin(t * 5) * max(0.0, 1 - max(0.0, t - ts[0] - 0.3) / 3.0))
    seq(img, t, ts[0] + 0.3, tag_spr_big("LIKE"), 560, 740, shadow=12, rot=-3)
    sw = 10 * math.sin((t - ts[0] - 0.7) * 18) * max(0.0, 1 - (t - ts[0] - 0.7) / 1.2) if t > ts[0] + 0.7 else 0
    seq(img, t, ts[0] + 0.6, bell4(), 1360, 440, shadow=14, scale=1.5, rot=sw)
    seq(img, t, ts[0] + 0.9, tag_spr_big("SUBSCRIBE", 520), 1360, 740, shadow=12, rot=3)
    ban(img, t, ts[1] + 0.1, "SO YOU DON'T MISS THE NEXT ONE", cy=950, w=1100, size=52)

def tag_spr_big(text, w=340):
    def fn(c):
        c.rrect((5, 5, w - 5, 135), 38, fill=GOLD, outline=(168, 118, 40), width=7)
        c.text((w / 2, 72), text, FONT_SANS, 62, GREEN_D, track=3)
    return sprite(("tagb", text, w), w, 140, fn)

# ============================================================ BLOCCO 72
def draw72(img, t):
    ts = starts(72)
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
        put(img, cache("p72", panel_), 595, 790, scale=bp[0], alpha=bp[1], shadow=16)
    lines = [("Rules, amounts and ages change", IVORY, ts[0] + 0.3), ("and differ by location and plan.", IVORY, ts[0] + 1.6),
             ("Always confirm with the official source", GOLD, ts[1] + 0.2), ("before you rely on them.", GOLD, ts[1] + 1.3),
             ("General information, not financial advice.", SAGE, ts[2] + 0.2), ("This channel is not affiliated with any agency.", SAGE, ts[2] + 1.6)]
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

DRAW = {56: draw56, 57: draw57, 58: draw58, 59: draw59, 60: draw60, 61: draw61, 62: draw62, 63: draw63, 64: draw64, 65: draw65, 66: draw66, 67: draw67, 68: draw68, 69: draw69, 70: draw70, 71: draw71, 72: draw72}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/bollette-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
