"""Video lungo 3 (Costco) - blocchi 51-63 (nota sui soldi, punti 13 vaccini e 14 Executive, riepilogo, regola, chiusura, disclaimer).
Durate dalla timeline dell'utente (07/10/2026): B51 403, B52 178, B53 364, B54 404, B55 270, B56 582, B57 484, B58 760, B59 471, B60 217, B61 188, B62 197, B63 465.
Uso: OUT=cartella python3 long3_b51_63.py <blocco 51..63> [fotogrammi]
     python3 long3_b51_63.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b41_50 import *

DUR.update({51: 403, 52: 178, 53: 364, 54: 404, 55: 270, 56: 582, 57: 484, 58: 760, 59: 471, 60: 217, 61: 188, 62: 197, 63: 465})
PHRASES.update({
    51: ["Also, a quick note on money.", "Seniors on a fixed income should never feel pushed to spend.",
         "Costco membership is worth it only if you will really use these things,", "and you are the only one who can judge that."],
    52: ["Now, two more that are worth knowing.", "They are not free,", "so I will tell you the costs plainly."],
    53: ["Thirteen.", "Vaccines at the pharmacy.", "Costco's pharmacists give many C D C recommended vaccines,",
         "including the flu shot, covid boosters,", "shingles and pneumonia vaccines."],
    54: ["You can walk in, depending on the wait,", "or book through the Costco app.", "Non members are welcome to use the pharmacy too.",
         "Ask the pharmacist what the vaccine costs for you,", "and whether your insurance covers it."],
    55: ["Fourteen.", "The Executive membership.", "And here is the honest math.", "It costs sixty five dollars more than the basic card."],
    56: ["In return, you get a two percent reward on eligible purchases,", "up to one thousand two hundred fifty dollars in any twelve months.",
         "Sixty five divided by two percent is three thousand two hundred fifty dollars.",
         "That is how much you have to spend in a year,", "just to get back what you paid for the upgrade."],
    57: ["And Costco itself says the reward is not guaranteed", "to be equal to or greater than the upgrade fee.",
         "If your yearly spending is below that number,", "stay with the basic card.", "Do the math with your own receipts,", "not with a promise."],
    58: ["So, let's put it together.", "No senior discount.", "But a prescription program, a pharmacy that needs no membership,",
         "a free hearing test, an eye exam, free tech support,", "a second year of warranty, lifetime tire care,",
         "price adjustment, easy returns, a free household card,", "a savings booklet, online receipts, vaccines,", "and an upgrade you can now calculate."],
    59: ["If you want to get ready for your next visit,", "bring four things:", "your membership card,", "your receipts,",
         "the model numbers of the appliances you own,", "and your list of medications.",
         "With those four things in your bag,", "you are ready to use almost everything in this video."],
    60: ["Here is the one rule to remember.", "Before you pay for any extra,", "find out what already comes with what you own."],
    61: ["Which of these did you already know?", "And which one will you try first?", "Tell me in the comments."],
    62: ["If this helped you,", "please like the video,", "and follow The Senior Advantage,", "so you don't miss the next one."],
    63: ["Rules, prices and services change and differ by warehouse.", "Always confirm with Costco before you rely on them.",
         "This is general information, not financial advice.", "This channel is not affiliated with Costco."],
})

# ------------------------------------------------------------------ icone nuove
def i_wallet(c, cx, cy, s=1.0):
    c.rrect((cx - 60 * s, cy - 40 * s, cx + 60 * s, cy + 46 * s), 14 * s, fill=(176, 120, 70))
    c.rrect((cx - 60 * s, cy - 40 * s, cx + 60 * s, cy - 14 * s), 14 * s, fill=(150, 98, 56))
    c.rrect((cx + 20 * s, cy - 6 * s, cx + 66 * s, cy + 24 * s), 10 * s, fill=GOLD)
    c.ell((cx + 36 * s, cy + 2 * s, cx + 50 * s, cy + 16 * s), fill=GREEN_D)

def i_hand_stop(c, cx, cy, s=1.0):
    c.ell((cx - 56 * s, cy - 56 * s, cx + 56 * s, cy + 56 * s), fill=CORAL)
    c.rrect((cx - 8 * s, cy - 36 * s, cx + 8 * s, cy + 8 * s), 6 * s, fill=IVORY)
    c.ell((cx - 8 * s, cy + 18 * s, cx + 8 * s, cy + 34 * s), fill=IVORY)

def i_scale_judge(c, cx, cy, s=1.0): ic_scale(c, cx, cy, s)

def i_syringe(c, cx, cy, s=1.0):
    c.line([(cx - 52 * s, cy + 52 * s), (cx + 28 * s, cy - 28 * s)], IVORY, 24 * s)
    c.line([(cx - 52 * s, cy + 52 * s), (cx - 30 * s, cy + 30 * s)], BLUE, 24 * s)
    c.line([(cx + 28 * s, cy - 28 * s), (cx + 52 * s, cy - 52 * s)], GOLD, 10 * s)
    c.line([(cx + 20 * s, cy - 52 * s), (cx + 56 * s, cy - 16 * s)], GOLD, 12 * s)
    cross_ic(c, cx - 8 * s, cy + 4 * s, 16 * s, GREEN_D, None)

def i_flu(c, cx, cy, s=1.0):
    c.ell((cx - 36 * s, cy - 36 * s, cx + 36 * s, cy + 36 * s), fill=CORAL)
    for k in range(10):
        a = k * math.pi / 5
        c.line([(cx + math.cos(a) * 36 * s, cy + math.sin(a) * 36 * s), (cx + math.cos(a) * 54 * s, cy + math.sin(a) * 54 * s)], CORAL, 7 * s)
        c.ell((cx + math.cos(a) * 54 * s - 6 * s, cy + math.sin(a) * 54 * s - 6 * s, cx + math.cos(a) * 54 * s + 6 * s, cy + math.sin(a) * 54 * s + 6 * s), fill=CORAL)

def i_covid(c, cx, cy, s=1.0):
    c.ell((cx - 34 * s, cy - 34 * s, cx + 34 * s, cy + 34 * s), fill=BLUE)
    for k in range(12):
        a = k * math.pi / 6
        c.line([(cx + math.cos(a) * 34 * s, cy + math.sin(a) * 34 * s), (cx + math.cos(a) * 52 * s, cy + math.sin(a) * 52 * s)], IVORY, 6 * s)
        c.ell((cx + math.cos(a) * 52 * s - 5 * s, cy + math.sin(a) * 52 * s - 5 * s, cx + math.cos(a) * 52 * s + 5 * s, cy + math.sin(a) * 52 * s + 5 * s), fill=IVORY)

def i_shingles(c, cx, cy, s=1.0):
    person_ic(c, cx, cy + 8 * s, 1.3 * s, IVORY)
    for dx, dy in ((-30, -4), (-14, 14), (6, -10), (24, 10)):
        c.ell((cx + (dx - 6) * s, cy + (dy - 6) * s, cx + (dx + 6) * s, cy + (dy + 6) * s), fill=CORAL)

def i_lungs(c, cx, cy, s=1.0):
    c.ell((cx - 58 * s, cy - 40 * s, cx - 4 * s, cy + 52 * s), fill=CORAL)
    c.ell((cx + 4 * s, cy - 40 * s, cx + 58 * s, cy + 52 * s), fill=CORAL)
    c.line([(cx, cy - 56 * s), (cx, cy - 6 * s)], IVORY, 9 * s)

def i_walkin(c, cx, cy, s=1.0):
    person_ic(c, cx - 14 * s, cy + 8 * s, 1.0 * s, IVORY)
    c.poly([(cx + 14 * s, cy - 12 * s), (cx + 54 * s, cy + 6 * s), (cx + 14 * s, cy + 24 * s)], fill=GOLD)

def i_award(c, cx, cy, s=1.0):
    c.ell((cx - 40 * s, cy - 56 * s, cx + 40 * s, cy + 24 * s), fill=GOLD, outline=(168, 118, 40), width=5 * s)
    c.text((cx, cy - 16 * s), "2%", FONT_SANS, 32 * s, GREEN_D)
    c.poly([(cx - 24 * s, cy + 18 * s), (cx - 38 * s, cy + 62 * s), (cx - 14 * s, cy + 50 * s), (cx - 4 * s, cy + 62 * s), (cx + 2 * s, cy + 22 * s)], fill=CORAL)
    c.poly([(cx + 24 * s, cy + 18 * s), (cx + 38 * s, cy + 62 * s), (cx + 14 * s, cy + 50 * s), (cx + 4 * s, cy + 62 * s), (cx - 2 * s, cy + 22 * s)], fill=CORAL)

def i_percent(c, cx, cy, s=1.0):
    c.ell((cx - 52 * s, cy - 52 * s, cx + 52 * s, cy + 52 * s), fill=GOLD)
    c.text((cx, cy + 2 * s), "%", FONT_SANS, 66 * s, GREEN_D)

def i_calc(c, cx, cy, s=1.0):
    c.rrect((cx - 40 * s, cy - 58 * s, cx + 40 * s, cy + 58 * s), 10 * s, fill=GOLD)
    c.rrect((cx - 30 * s, cy - 48 * s, cx + 30 * s, cy - 20 * s), 5 * s, fill=GREEN_D)
    for r_ in range(3):
        for k in range(3):
            c.rrect((cx - 30 * s + k * 22 * s, cy - 10 * s + r_ * 22 * s, cx - 12 * s + k * 22 * s, cy + 6 * s + r_ * 22 * s), 4 * s, fill=(190, 140, 66))

def i_basic_card(c, cx, cy, s=1.0): ic_cardm(c, cx, cy, s)
def i_star_card(c, cx, cy, s=1.0):
    c.rrect((cx - 66 * s, cy - 42 * s, cx + 66 * s, cy + 42 * s), 10 * s, fill=(24, 78, 62), outline=GOLD, width=5 * s)
    pts = []
    for k in range(10):
        r = 28 if k % 2 == 0 else 12
        a = -math.pi / 2 + k * math.pi / 5
        pts.append((cx + r * s * math.cos(a), cy + r * s * math.sin(a)))
    c.poly(pts, fill=GOLD)

def i_receipts_pile(c, cx, cy, s=1.0): ic_receipt(c, cx, cy, s)
def i_models(c, cx, cy, s=1.0):
    ic_tv(c, cx - 22 * s, cy - 10 * s, 0.6 * s)
    ic_fridge(c, cx + 40 * s, cy + 4 * s, 0.6 * s)
def i_meds(c, cx, cy, s=1.0): bottle(c, cx, cy, 1.0 * s)
def i_bag(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 30 * s, cx + 56 * s, cy + 58 * s), 12 * s, fill=(196, 150, 98))
    c.arc((cx - 30 * s, cy - 62 * s, cx + 30 * s, cy + 6 * s), 180, 360, (160, 118, 72), 9 * s)
def i_comment(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 44 * s, cx + 56 * s, cy + 28 * s), 22 * s, fill=IVORY)
    c.poly([(cx - 30 * s, cy + 24 * s), (cx - 10 * s, cy + 24 * s), (cx - 38 * s, cy + 56 * s)], fill=IVORY)
    for k in range(3):
        c.ell((cx - 28 * s + k * 28 * s, cy - 10 * s, cx - 14 * s + k * 28 * s, cy + 4 * s), fill=GREEN_D)
def i_thumb(c, cx, cy, s=1.0):
    c.rrect((cx - 54 * s, cy - 6 * s, cx - 22 * s, cy + 54 * s), 6 * s, fill=BLUE)
    c.poly([(cx - 18 * s, cy - 6 * s), (cx + 6 * s, cy - 58 * s), (cx + 26 * s, cy - 50 * s), (cx + 18 * s, cy - 14 * s), (cx + 56 * s, cy - 14 * s),
            (cx + 56 * s, cy + 50 * s), (cx - 18 * s, cy + 54 * s)], fill=IVORY)
def i_bell(c, cx, cy, s=1.0):
    c.arc((cx - 40 * s, cy - 56 * s, cx + 40 * s, cy + 24 * s), 180, 360, GOLD, 12 * s)
    c.poly([(cx - 40 * s, cy - 16 * s), (cx + 40 * s, cy - 16 * s), (cx + 54 * s, cy + 30 * s), (cx - 54 * s, cy + 30 * s)], fill=GOLD)
    c.ell((cx - 12 * s, cy + 28 * s, cx + 12 * s, cy + 52 * s), fill=GOLD)
def i_chat(c, cx, cy, s=1.0): i_comment(c, cx, cy, s)
def i_disc_i(c, cx, cy, s=1.0): info_i(c, cx, cy, 52 * s)
def i_rules_change(c, cx, cy, s=1.0):
    calendar(c, cx, cy, s)
    c.arc((cx - 62 * s, cy - 62 * s, cx + 62 * s, cy + 62 * s), 200, 340, GOLD, 7 * s)
def i_confirm(c, cx, cy, s=1.0): ic_store(c, cx, cy, s)
def i_notaffil(c, cx, cy, s=1.0):
    ic_cardm(c, cx, cy, 0.9 * s)
    crossed(c, cx, cy, 68 * s)
def i_advice(c, cx, cy, s=1.0): warn_tri(c, cx, cy, 0.9 * s, GOLD, GREEN_D)

def draw_n(img, t, ts, lines, y0=300, dy=190, w=1600):
    pass

# ============================================================ BLOCCO 51
def draw51(img, t):
    ts = starts(51)
    common5(img, t, "A QUICK NOTE ON MONEY", None)
    show(img, t, ts[0], card_big("c51a", 520, 400, GOLD, i_wallet, 1.0, "A QUICK NOTE", "ON MONEY", 40, 56, cy=130, r=94), 480, 300, sh=12)
    show(img, t, ts[1], card_big("c51b", 520, 400, CORAL, i_hand_stop, 0.95, "NEVER FEEL", "PUSHED TO SPEND", 38, 42, c2=CORAL, circle=(PANEL_FILL,), cy=130, r=94), 1440, 300, sh=12)
    show(img, t, ts[1] + 0.5, pill_spr("SENIORS ON A FIXED INCOME", 40, 880, 84, PANEL_FILL, SAGE, SAGE_D), 960, 600, sh=8)
    show(img, t, ts[2], chipx("c51c", 1700, 150, GREEN_L, GOLD, i_tool, 0.6, ("WORTH IT ONLY IF YOU", "WILL REALLY USE THESE THINGS"), (38, 50), (SAGE, IVORY)), 960, 790, sh=12)
    show(img, t, ts[3], chipx("c51d", 1400, 150, GOLD, (168, 118, 40), i_scale_judge, 0.5, ("YOU ARE THE ONLY ONE", "WHO CAN JUDGE THAT"), (38, 50), (GREEN_D, GREEN_D)), 960, 960, sh=12)

# ============================================================ BLOCCO 52
def draw52(img, t):
    ts = starts(52)
    common5(img, t, "TWO MORE", None)
    intro(img, t, "TWO MORE", "WORTH KNOWING", ts[1], size=150)
    for i in range(2):
        show(img, t, ts[1] + 0.1 + i * 0.4, num_badge(13 + i, 260, 130), 560 + i * 800, 400, sh=14)
    show(img, t, ts[1] + 0.6, pill_spr("NOT FREE", 80, 560, 130, CORAL, IVORY), 960, 640, rot=-4, sh=12)
    show(img, t, ts[2], chipx("c52a", 1500, 150, PANEL_FILL, CORAL, ic_dollar, 0.6, ("THE COSTS, PLAINLY",), (66,), (CORAL,)), 960, 860, sh=12)

# ============================================================ BLOCCO 53
VACC = [(i_flu, "FLU", "SHOT"), (i_covid, "COVID", "BOOSTERS"), (i_shingles, "SHINGLES", ""), (i_lungs, "PNEUMONIA", "")]

def draw53(img, t):
    ts = starts(53)
    common5(img, t, "SAVING NUMBER 13", None)
    big_badge(img, t, ts[0] + 0.2, 13, 190)
    title_lines(img, t, ts[1], "VACCINES AT", "THE PHARMACY", 90, 100, y1=255, y2=375)
    show(img, t, ts[2], chipx("c53a", 1300, 150, GREEN_L, GOLD, i_syringe, 0.6, ("MANY C D C RECOMMENDED", "VACCINES"), (38, 52), (SAGE, IVORY)), 960, 580, sh=12)
    for i, (fn, a, b) in enumerate(VACC):
        st = ts[3] + 0.1 + i * 0.5 if i < 2 else ts[4] + (i - 2) * 0.6
        show(img, t, st, card_big(("v53", i), 410, 360, GOLD, fn, 0.9, a, b, 40, 40, cy=115, r=84), 255 + i * 470, 840, sh=12)

# ============================================================ BLOCCO 54
def draw54(img, t):
    ts = starts(54)
    common5(img, t, "HOW TO GET IT", 13)
    show(img, t, ts[0], card_big("c54a", 410, 400, GOLD, i_walkin, 1.0, "WALK IN,", "DEPENDING ON THE WAIT", 40, 28, cy=125, r=92), 255, 350, sh=12)
    show(img, t, ts[1], card_big("c54b", 410, 400, GOLD, i_app, 1.0, "OR BOOK IN THE", "COSTCO APP", 38, 46, cy=125, r=92), 715, 350, sh=12)
    show(img, t, ts[2], card_big("c54c", 410, 400, SAGE_D, i_pair, 1.0, "NON MEMBERS", "ARE WELCOME TOO", 40, 36, cy=125, r=92), 1175, 350, sh=12)
    show(img, t, ts[3], card_big("c54d", 410, 400, GOLD, ic_dollar, 1.0, "ASK WHAT THE", "VACCINE COSTS", 38, 44, cy=125, r=92), 1635, 350, sh=12)
    show(img, t, ts[4], chipx("c54e", 1500, 150, GREEN_L, GOLD, i_ok, 0.6, ("DOES YOUR INSURANCE COVER IT?",), (56,), (IVORY,)), 960, 820, sh=12)
    if t > ts[4]: burst(img, t, ts[4] + 0.3, 960, 820, n=8, seed=3, rad=100)

# ============================================================ BLOCCO 55
def draw55(img, t):
    ts = starts(55)
    common5(img, t, "SAVING NUMBER 14", None)
    big_badge(img, t, ts[0] + 0.2, 14, 190)
    title_lines(img, t, ts[1], "THE EXECUTIVE", "MEMBERSHIP", 90, 100, y1=255, y2=375)
    show(img, t, ts[2], pill_spr("THE HONEST MATH", 56, 760, 110, GOLD, GREEN_D), 960, 560, sh=10)
    show(img, t, ts[3] - 0.3, card5("gold"), 440, 780, 0.55, -2, sh=12)
    show(img, t, ts[3] + 0.2, card5("exec"), 1480, 780, 0.55, 2, sh=12)
    ar = seg(t, ts[3] + 0.5, 0.4)
    if ar > 0: put(img, arrow_spr(), 960, 780, scale=1.2 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[3] + 0.9, pill_spr("+ $65", 90, 340, 130, CORAL, IVORY), 960, 930, rot=-4, sh=12)

# ============================================================ BLOCCO 56
def draw56(img, t):
    ts = starts(56)
    common5(img, t, "THE EXECUTIVE MATH", 14)
    show(img, t, ts[0], card_big("c56a", 520, 400, GOLD, i_award, 1.0, "2% REWARD ON", "ELIGIBLE PURCHASES", 36, 36, cy=130, r=94), 330, 330, sh=12)
    show(img, t, ts[1], card_big("c56b", 520, 400, GOLD, i_calc, 0.95, "UP TO $1,250", "IN ANY 12 MONTHS", 40, 40, cy=130, r=94), 960, 330, sh=12)
    show(img, t, ts[2], pill_spr("$65  ÷  2%  =  $3,250", 66, 1100, 120, PANEL_FILL, GOLD, GOLD), 960, 640, sh=14)
    show(img, t, ts[3], chipx("c56c", 1500, 150, GREEN_L, GOLD, i_wallet, 0.6, ("YOU MUST SPEND $3,250 IN A YEAR", ), (50,), (IVORY,)), 960, 790, sh=12)
    show(img, t, ts[4], chipx("c56d", 1500, 150, GOLD, (168, 118, 40), i_tool, 0.6, ("JUST TO GET BACK", "WHAT YOU PAID FOR THE UPGRADE"), (46, 40), (GREEN_D, GREEN_D)), 960, 950, sh=12)

# ============================================================ BLOCCO 57
def draw57(img, t):
    ts = starts(57)
    common5(img, t, "DO THE MATH YOURSELF", 14)
    show(img, t, ts[0], card_big("c57a", 520, 400, CORAL, i_hand_stop, 0.95, "THE REWARD IS", "NOT GUARANTEED", 40, 44, c2=CORAL, circle=(PANEL_FILL,), cy=130, r=94), 480, 290, sh=12)
    show(img, t, ts[1], card_big("c57b", 520, 400, CORAL, i_percent, 0.9, "EQUAL TO OR GREATER", "THAN THE UPGRADE FEE", 32, 32, c2=CORAL, circle=(PANEL_FILL,), cy=130, r=94), 1440, 290, sh=12)
    show(img, t, ts[2], pill_spr("SPENDING BELOW $3,250 A YEAR?", 46, 1200, 100, PANEL_FILL, CORAL, CORAL), 960, 600, sh=10)
    show(img, t, ts[3], chipx("c57c", 1300, 150, GREEN_L, GOLD, i_star_card, 0.6, ("STAY WITH THE BASIC CARD",), (56,), (IVORY,)), 960, 780, sh=12)
    show(img, t, ts[4], chipx("c57d", 800, 150, GOLD, (168, 118, 40), i_receipt_big, 0.5, ("USE YOUR", "OWN RECEIPTS"), (38, 56), (GREEN_D, GREEN_D)), 540, 960, sh=10)
    show(img, t, ts[5], chipx("c57e", 800, 150, PANEL_FILL, CORAL, i_hand_stop, 0.55, ("NOT A", "PROMISE"), (38, 56), (IVORY, CORAL)), 1380, 960, sh=10)

# ============================================================ BLOCCO 58 (riepilogo 14 punti)
def booklet_mini(c, cx, cy, s=1.0):
    c.rrect((cx - 44 * s, cy - 56 * s, cx + 44 * s, cy + 56 * s), 8 * s, fill=(236, 188, 108))
    c.rrect((cx - 34 * s, cy - 44 * s, cx + 34 * s, cy - 18 * s), 4 * s, fill=GREEN_D)
    for k in range(2):
        for j in range(2):
            c.rrect((cx - 32 * s + j * 34 * s, cy - 8 * s + k * 30 * s, cx - 4 * s + j * 34 * s, cy + 18 * s + k * 30 * s), 4 * s, fill=IVORY)

RECAP = [(ic_pill, "PRESCRIPTION", "PROGRAM"), (ic_store, "PHARMACY,", "NO MEMBERSHIP"), (ic_hear_s, "FREE HEARING", "TEST"), (ic_eyechart, "EYE", "EXAM"),
         (ic_headset, "FREE TECH", "SUPPORT"), (i_cal2, "SECOND YEAR", "WARRANTY"), (i_tire, "LIFETIME", "TIRE CARE"), (i_down, "PRICE", "ADJUSTMENT"),
         (i_counter, "EASY", "RETURNS"), (i_pair, "FREE", "HOUSEHOLD CARD"), (booklet_mini, "SAVINGS", "BOOKLET"), (i_online_receipt, "ONLINE", "RECEIPTS"),
         (i_syringe, "VACCINES", ""), (i_calc, "UPGRADE YOU", "CAN CALCULATE")]

def tile14(i, w=270, h=210):
    def mk():
        fn, a, b = RECAP[i]
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 24, fill=CARD, outline=GOLD, width=5)
        c.ell((w - 62, 10, w - 10, 62), fill=GOLD)
        c.text((w - 36, 37), str(i + 1), FONT_SERIF, 30, GREEN_D)
        if b:
            c.text((w / 2, h - 52), a, FONT_SANS, 24 if len(a) < 12 else 21, IVORY)
            c.text((w / 2, h - 24), b, FONT_SANS, 24 if len(b) < 12 else 21, GOLD)
        else:
            c.text((w / 2, h - 36), a, FONT_SANS, 28, GOLD)
        im = c.done()
        paste_c(im, mini(fn, 0.5), w / 2 - 6, 78)
        return im
    return cache(("t14", i), mk)

def draw58(img, t):
    ts = starts(58)
    common5(img, t, "PUTTING IT ALL TOGETHER", None)
    show(img, t, ts[1], chipx("c58a", 800, 110, PANEL_FILL, CORAL, i_tag_s, 0.4, ("NO SENIOR DISCOUNT",), (44,), (CORAL,)), 960, 215, sh=10)
    # 14 tessere: 7 + 7, tempi dalle frasi 2-7
    starts_t = [ts[2], ts[2] + 0.8, ts[3], ts[3] + 0.7, ts[3] + 1.4, ts[4], ts[4] + 0.8, ts[5], ts[5] + 0.7, ts[5] + 1.4, ts[6], ts[6] + 0.8, ts[6] + 1.6, ts[7]]
    for i in range(14):
        col, row = i % 7, i // 7
        show(img, t, starts_t[i], tile14(i), 150 + col * 270, 500 + row * 250, 0.95, sh=6, dur=0.4)

# ============================================================ BLOCCO 59
BAG4 = [(i_basic_card, "MEMBERSHIP", "CARD"), (i_receipts_pile, "YOUR", "RECEIPTS"), (i_models, "MODEL NUMBERS OF", "YOUR APPLIANCES"), (i_meds, "YOUR LIST OF", "MEDICATIONS")]

def draw59(img, t):
    ts = starts(59)
    common5(img, t, "BEFORE YOUR NEXT VISIT", None)
    show(img, t, ts[1], card_big("c59bag", 440, 440, GOLD, i_bag, 1.3, "BRING", "FOUR THINGS", 42, 56, cy=140, r=100), 275, 400, sh=12)
    for i, (fn, a, b) in enumerate(BAG4):
        def mk(i=i, fn=fn, a=a, b=b):
            return card_big(("b59", i), 330, 330, GOLD, fn, 0.8, a, b, 30 if len(a) > 12 else 36, 32 if len(a) > 12 else 38, cy=105, r=78)
        pos = (640 + i * 360, 330)
        show(img, t, ts[2 + i] + 0.1, mk(), pos[0], pos[1], sh=10)
        ck = pop(t, ts[2 + i] + 0.6, 0.3)
        if ck[2] > 0:
            put(img, check_spr(), pos[0] + 120, pos[1] - 130, scale=0.7 * ck[0], alpha=ck[1])
    show(img, t, ts[6], chipx("c59z", 1700, 150, GREEN_L, GOLD, i_ok, 0.6, ("FOUR THINGS IN YOUR BAG:", "READY TO USE ALMOST EVERYTHING"), (36, 48), (SAGE, IVORY)), 960, 800, sh=12)
    if t > ts[7]: pass

# ============================================================ BLOCCO 60
def draw60(img, t):
    ts = starts(60)
    common5(img, t, "THE ONE RULE", None)
    show(img, t, ts[0], pill_spr("THE ONE RULE TO REMEMBER", 60, 1100, 130, GOLD, GREEN_D), 960, 250, sh=12)
    show(img, t, ts[1], chipx("c60a", 1500, 170, GREEN_L, SAGE, i_wallet, 0.65, ("BEFORE YOU PAY", "FOR ANY EXTRA"), (44, 66), (SAGE, IVORY)), 960, 520, sh=12)
    show(img, t, ts[2], chipx("c60b", 1700, 190, GOLD, (168, 118, 40), i_tool, 0.7, ("FIND OUT WHAT ALREADY", "COMES WITH WHAT YOU OWN"), (52, 56), (GREEN_D, GREEN_D)), 960, 830, sh=14)
    if t > ts[2]: burst(img, t, ts[2] + 0.3, 960, 830, n=12, seed=5, rad=130)

# ============================================================ BLOCCO 61
def draw61(img, t):
    ts = starts(61)
    common5(img, t, "YOUR TURN", None)
    show(img, t, ts[0], chipx("c61a", 1700, 170, GREEN_L, GOLD, i_ok, 0.65, ("WHICH OF THESE DID YOU", "ALREADY KNOW?"), (46, 64), (SAGE, IVORY)), 960, 300, sh=12)
    show(img, t, ts[1], chipx("c61b", 1700, 170, GREEN_L, GOLD, i_tag_s, 0.55, ("WHICH ONE WILL YOU", "TRY FIRST?"), (46, 64), (SAGE, IVORY)), 960, 540, sh=12)
    show(img, t, ts[2], chipx("c61c", 1200, 190, GOLD, (168, 118, 40), i_comment, 0.8, ("TELL ME IN", "THE COMMENTS"), (48, 70), (GREEN_D, GREEN_D)), 960, 830, sh=14)

# ============================================================ BLOCCO 62
def draw62(img, t):
    ts = starts(62)
    common5(img, t, "THANK YOU", None)
    show(img, t, ts[0], pill_spr("IF THIS HELPED YOU", 56, 900, 110, PANEL_FILL, GOLD, GOLD), 960, 220, sh=10)
    show(img, t, ts[1], chipx("c62a", 840, 200, GREEN_L, GOLD, i_thumb, 0.8, ("LIKE", "THE VIDEO"), (46, 70), (SAGE, IVORY)), 470, 520, sh=12)
    show(img, t, ts[2], chipx("c62b", 840, 200, GOLD, (168, 118, 40), i_bell, 0.8, ("FOLLOW THE", "SENIOR ADVANTAGE"), (44, 50), (GREEN_D, GREEN_D)), 1440, 520, sh=12)
    show(img, t, ts[3], pill_spr("SO YOU DON'T MISS THE NEXT ONE", 50, 1300, 110, PANEL_FILL, SAGE, SAGE_D), 960, 820, sh=10)

# ============================================================ BLOCCO 63: slide finale col disclaimer (modello anteprima/3-finale-disclaimer.png)
def draw63(img, t):
    ts = starts(63)
    d = ImageDraw.Draw(img)
    a0 = ease(seg(t, 0, .5))
    put(img, tspr("BEFORE YOU GO", FONT_SANS, 44, SAGE, track=18), 960, 100, alpha=a0)
    put(img, tspr("ALWAYS CONFIRM", FONT_SANS, 112, IVORY), 560, 340 - 30 * (1 - ease(seg(t, .3, .5))), alpha=ease(seg(t, .3, .5)))
    put(img, tspr("BEFORE YOU RELY", FONT_SANS, 112, GOLD), 560, 480 - 30 * (1 - ease(seg(t, .9, .5))), alpha=ease(seg(t, .9, .5)))
    bp = pop(t, 1.4, 0.5)
    def panel():
        c = Cv(990, 400)
        c.rrect((3, 3, 987, 397), 36, fill=CARD, outline=SAGE_D, width=5)
        return c.done()
    if bp[2] > 0:
        put(img, cache("p63", panel), 595, 790, scale=bp[0], alpha=bp[1], shadow=16)
    lines = [("Rules, prices and services change", IVORY, ts[0] + 0.3), ("and differ by warehouse.", IVORY, ts[0] + 1.6),
             ("Always confirm with Costco", GOLD, ts[1] + 0.2), ("before you rely on them.", GOLD, ts[1] + 1.3),
             ("General information, not financial advice.", SAGE, ts[2] + 0.2), ("This channel is not affiliated with Costco.", SAGE, ts[3] + 0.2)]
    for i, (s, col, st) in enumerate(lines):
        a = ease(seg(t, st, .5))
        if a > 0:
            put(img, tspr(s, FONT_SANS_M if i > 3 else FONT_SANS, 36, col), 595, 650 + i * 58 - 20 * (1 - a), alpha=a)
    # riquadro schermata finale
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
    put(img, tspr("THANK YOU FOR WATCHING", FONT_SANS, 40, SAGE), 1490, 880, alpha=ease(seg(t, 8.0, .5)))

DRAW.update({51: draw51, 52: draw52, 53: draw53, 54: draw54, 55: draw55, 56: draw56, 57: draw57, 58: draw58,
             59: draw59, 60: draw60, 61: draw61, 62: draw62, 63: draw63})

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/costco-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
