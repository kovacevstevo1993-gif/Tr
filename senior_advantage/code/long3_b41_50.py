"""Video lungo 3 (Costco) - blocchi 41-50 (resi: eccezioni, come si fa; punti 10 tessera famiglia, 11 libretto, 12 ricevute online; sintesi).
Durate dalla timeline dell'utente (07/10/2026): B41 613, B42 398, B43 314, B44 446, B45 362, B46 297, B47 448, B48 382, B49 328, B50 403 fotogrammi.
Uso: OUT=cartella python3 long3_b41_50.py <blocco 41..50> [fotogrammi]
     python3 long3_b41_50.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b36_40 import *

DUR.update({41: 613, 42: 398, 43: 314, 44: 446, 45: 362, 46: 297, 47: 448, 48: 382, 49: 328, 50: 403})
PHRASES.update({
    41: ["Most things can be returned.", "But some electronics have a ninety day limit:",
         "televisions, projectors, major appliances, computers, tablets, smart watches, cameras, camcorders, music players and cell phones.",
         "So do not wait.", "Always read the exceptions on Costco's website."],
    42: ["To return something, you take it to a Costco warehouse,", "and the member services team helps you.",
         "Keep the item, the box if you can, and your receipt,", "or use the online receipt we will talk about in a minute."],
    43: ["Ten.", "A second card at no extra cost.", "Your membership includes one free household card,", "for someone over sixteen", "who lives at the same address as you."],
    44: ["That can be your spouse,", "or an adult son or daughter who lives with you.", "You add them in your account details on the Costco website,",
         "and they pick up their card at the membership counter.", "Two people shop,", "and you pay for one membership."],
    45: ["Eleven.", "The savings booklet.", "Costco sends a savings booklet to the primary member", "of active memberships.",
         "It has coupons on everyday items,", "from chips to laundry detergent."],
    46: ["There is nothing to cut out.", "The savings apply at checkout.", "You can also find the same savings on the Costco website", "and in the Costco app."],
    47: ["If the booklet never arrives,", "there can be simple reasons:", "you opted out of mailers,", "your address is wrong or changed in the last three months,",
         "or your membership is new or expired.", "Ask at the membership counter,", "and they can fix it."],
    48: ["Twelve.", "Your receipts, online.", "Costco keeps your in warehouse receipts for two years.", "Sign in to your Costco account,",
         "select Orders and Purchases,", "and open the In Warehouse tab."],
    49: ["Why does this matter?", "Because the receipt is what you need for a return,", "a price adjustment,", "and the Concierge phone number.",
         "No more looking for a faded paper in a drawer."],
    50: ["Let me say it plainly.", "None of these twelve things is a discount for your age.", "They are tools that Costco already offers to every member,",
         "and many seniors never use them", "because nobody explains them."],
})

# ------------------------------------------------------------------ icone nuove (sempre funzioni con nome: la cache usa il nome)
def i_camcorder(c, cx, cy, s=1.0):
    c.rrect((cx - 62 * s, cy - 34 * s, cx + 30 * s, cy + 36 * s), 12 * s, fill=IVORY)
    c.poly([(cx + 34 * s, cy - 8 * s), (cx + 68 * s, cy - 26 * s), (cx + 68 * s, cy + 26 * s), (cx + 34 * s, cy + 8 * s)], fill=IVORY)
    c.ell((cx - 44 * s, cy - 18 * s, cx - 4 * s, cy + 22 * s), fill=GREEN_D, outline=GOLD, width=5 * s)
    c.ell((cx + 12 * s, cy - 26 * s, cx + 24 * s, cy - 14 * s), fill=CORAL)

def i_chips(c, cx, cy, s=1.0):
    pts = [(cx - 46 * s, cy - 56 * s), (cx - 30 * s, cy - 48 * s), (cx - 14 * s, cy - 56 * s), (cx, cy - 48 * s), (cx + 14 * s, cy - 56 * s),
           (cx + 30 * s, cy - 48 * s), (cx + 46 * s, cy - 56 * s), (cx + 52 * s, cy + 58 * s), (cx - 52 * s, cy + 58 * s)]
    c.poly(pts, fill=GOLD)
    c.ell((cx - 28 * s, cy - 14 * s, cx + 28 * s, cy + 42 * s), fill=CORAL)
    c.text((cx, cy + 14 * s), "CHIPS", FONT_SANS, 17 * s, IVORY)

def i_detergent(c, cx, cy, s=1.0):
    c.rrect((cx - 40 * s, cy - 30 * s, cx + 40 * s, cy + 60 * s), 14 * s, fill=BLUE)
    c.rrect((cx - 14 * s, cy - 52 * s, cx + 30 * s, cy - 28 * s), 6 * s, fill=IVORY)
    c.rrect((cx + 14 * s, cy - 60 * s, cx + 54 * s, cy - 46 * s), 5 * s, fill=IVORY)
    c.rrect((cx - 28 * s, cy - 2 * s, cx + 28 * s, cy + 40 * s), 6 * s, fill=IVORY)
    c.ell((cx - 12 * s, cy + 8 * s, cx + 12 * s, cy + 32 * s), fill=BLUE)

def i_scissors_x(c, cx, cy, s=1.0):
    c.line([(cx - 44 * s, cy + 40 * s), (cx + 40 * s, cy - 40 * s)], IVORY, 9 * s)
    c.line([(cx - 44 * s, cy - 40 * s), (cx + 40 * s, cy + 40 * s)], IVORY, 9 * s)
    c.ell((cx - 62 * s, cy + 20 * s, cx - 26 * s, cy + 56 * s), outline=GOLD, width=8 * s)
    c.ell((cx - 62 * s, cy - 56 * s, cx - 26 * s, cy - 20 * s), outline=GOLD, width=8 * s)
    crossed(c, cx, cy, 70 * s)

def i_register(c, cx, cy, s=1.0):
    c.rrect((cx - 60 * s, cy - 10 * s, cx + 60 * s, cy + 54 * s), 8 * s, fill=IVORY)
    c.rrect((cx - 42 * s, cy - 56 * s, cx + 42 * s, cy - 14 * s), 6 * s, fill=GREEN_D, outline=IVORY, width=5 * s)
    c.text((cx, cy - 35 * s), "SAVE", FONT_SANS, 22 * s, GOLD)
    for r_ in range(2):
        for k in range(4):
            c.rrect((cx - 48 * s + k * 26 * s, cy + 2 * s + r_ * 22 * s, cx - 30 * s + k * 26 * s, cy + 16 * s + r_ * 22 * s), 3 * s, fill=(176, 188, 180))

def i_web(c, cx, cy, s=1.0):
    laptop(c, cx, cy + 8 * s, 0.8 * s, GREEN_D)
    c.ell((cx - 28 * s, cy - 50 * s, cx + 28 * s, cy + 6 * s), outline=BLUE, width=5 * s)
    c.line([(cx - 28 * s, cy - 22 * s), (cx + 28 * s, cy - 22 * s)], BLUE, 4 * s)
    c.line([(cx, cy - 50 * s), (cx, cy + 6 * s)], BLUE, 4 * s)

def i_app(c, cx, cy, s=1.0):
    c.rrect((cx - 42 * s, cy - 64 * s, cx + 42 * s, cy + 64 * s), 12 * s, fill=GREEN_D, outline=IVORY, width=6 * s)
    cols = [GOLD, CORAL, BLUE, SAGE, IVORY, GOLD]
    for r_ in range(3):
        for k in range(2):
            c.rrect((cx - 28 * s + k * 34 * s, cy - 44 * s + r_ * 34 * s, cx - 4 * s + k * 34 * s, cy - 22 * s + r_ * 34 * s), 5 * s, fill=cols[r_ * 2 + k])

def i_mailbox(c, cx, cy, s=1.0):
    c.rrect((cx - 50 * s, cy - 36 * s, cx + 50 * s, cy + 30 * s), 22 * s, fill=BLUE)
    c.rrect((cx - 6 * s, cy + 28 * s, cx + 6 * s, cy + 62 * s), 2 * s, fill=IVORY)
    c.rrect((cx - 40 * s, cy - 8 * s, cx + 10 * s, cy + 8 * s), 4 * s, fill=GREEN_D)
    c.rrect((cx + 30 * s, cy - 62 * s, cx + 36 * s, cy - 30 * s), 2 * s, fill=CORAL)
    c.rrect((cx + 30 * s, cy - 62 * s, cx + 58 * s, cy - 48 * s), 2 * s, fill=CORAL)

def i_envelope_x(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 38 * s, cx + 56 * s, cy + 38 * s), 8 * s, fill=IVORY)
    c.line([(cx - 56 * s, cy - 34 * s), (cx, cy + 8 * s), (cx + 56 * s, cy - 34 * s)], (150, 160, 152), 5 * s)
    crossed(c, cx, cy, 70 * s)

def i_house_pin(c, cx, cy, s=1.0):
    house(c, cx - 14 * s, cy + 6 * s, 0.85 * s)
    pin(c, cx + 46 * s, cy - 8 * s, 0.7 * s)

def i_card_cal(c, cx, cy, s=1.0):
    ic_cardm(c, cx - 14 * s, cy + 14 * s, 0.8 * s)
    calendar(c, cx + 34 * s, cy - 14 * s, 0.5 * s)

def i_pair(c, cx, cy, s=1.0):
    person_ic(c, cx - 32 * s, cy + 8 * s, 0.95 * s, (190, 140, 66))
    person_ic(c, cx + 34 * s, cy + 16 * s, 0.8 * s, SAGE, head=(226, 190, 160))

def i_pair2(c, cx, cy, s=1.0):
    person_ic(c, cx - 30 * s, cy + 8 * s, 0.95 * s, (80, 96, 120))
    person_ic(c, cx + 34 * s, cy + 14 * s, 0.9 * s, CORAL, head=(226, 190, 160))

def i_account(c, cx, cy, s=1.0):
    laptop(c, cx, cy + 10 * s, 0.8 * s, GREEN_D)
    person_ic(c, cx, cy - 22 * s, 0.55 * s, IVORY)

def i_wh(c, cx, cy, s=1.0):
    c.poly([(cx - 66 * s, cy - 18 * s), (cx, cy - 56 * s), (cx + 66 * s, cy - 18 * s)], fill=GREEN_L)
    c.rrect((cx - 62 * s, cy - 18 * s, cx + 62 * s, cy + 56 * s), 4 * s, fill=IVORY)
    c.rrect((cx - 34 * s, cy + 6 * s, cx + 34 * s, cy + 56 * s), 3 * s, fill=(176, 188, 180))
    for k in range(4):
        c.line([(cx - 34 * s, cy + (14 + k * 11) * s), (cx + 34 * s, cy + (14 + k * 11) * s)], (140, 152, 144), 3 * s)

def i_receipt_big(c, cx, cy, s=1.0):
    ic_receipt(c, cx, cy, 1.0 * s)

def i_online_receipt(c, cx, cy, s=1.0):
    laptop(c, cx - 14 * s, cy + 10 * s, 0.75 * s, GREEN_D)
    ic_receipt(c, cx + 34 * s, cy - 14 * s, 0.55 * s)

def i_tabs(c, cx, cy, s=1.0):
    c.rrect((cx - 64 * s, cy - 40 * s, cx + 64 * s, cy + 50 * s), 8 * s, fill=IVORY)
    c.rrect((cx - 64 * s, cy - 40 * s, cx - 4 * s, cy - 14 * s), 6 * s, fill=(190, 200, 192))
    c.rrect((cx - 2 * s, cy - 40 * s, cx + 64 * s, cy - 14 * s), 6 * s, fill=GOLD)
    for k in range(3):
        c.line([(cx - 46 * s, cy + (0 + k * 16) * s), (cx + 46 * s - k * 12 * s, cy + (0 + k * 16) * s)], (150, 160, 152), 4 * s)

def i_list(c, cx, cy, s=1.0):
    c.rrect((cx - 46 * s, cy - 60 * s, cx + 46 * s, cy + 62 * s), 8 * s, fill=IVORY)
    c.rrect((cx - 20 * s, cy - 70 * s, cx + 20 * s, cy - 50 * s), 6 * s, fill=GOLD)
    for k in range(3):
        c.line([(cx - 34 * s, cy + (-26 + k * 30) * s), (cx - 24 * s, cy + (-16 + k * 30) * s), (cx - 8 * s, cy + (-36 + k * 30) * s)], GREEN_L, 6 * s)
        c.rrect((cx + 2 * s, cy + (-30 + k * 30) * s, cx + 34 * s, cy + (-22 + k * 30) * s), 3 * s, fill=(176, 188, 180))

def i_signin(c, cx, cy, s=1.0):
    c.ell((cx - 52 * s, cy - 52 * s, cx + 52 * s, cy + 52 * s), fill=IVORY)
    person_ic(c, cx, cy + 6 * s, 1.0 * s, GREEN_L)

def i_drawer_x(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 48 * s, cx + 56 * s, cy + 52 * s), 6 * s, fill=IVORY)
    c.line([(cx - 56 * s, cy + 2 * s), (cx + 56 * s, cy + 2 * s)], (150, 160, 152), 4 * s)
    c.rrect((cx - 16 * s, cy - 24 * s, cx + 16 * s, cy - 14 * s), 3 * s, fill=GREEN_D)
    c.rrect((cx - 16 * s, cy + 26 * s, cx + 16 * s, cy + 36 * s), 3 * s, fill=GREEN_D)
    crossed(c, cx, cy, 70 * s)

def i_bubble_x(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 44 * s, cx + 56 * s, cy + 28 * s), 22 * s, fill=IVORY)
    c.poly([(cx - 30 * s, cy + 24 * s), (cx - 10 * s, cy + 24 * s), (cx - 38 * s, cy + 56 * s)], fill=IVORY)
    c.text((cx, cy - 8 * s), "?", FONT_SANS, 52 * s, GREEN_D)
    crossed(c, cx, cy, 70 * s)

def i_over16(c, cx, cy, s=1.0):
    person_ic(c, cx - 14 * s, cy + 8 * s, 1.1 * s, IVORY)
    c.ell((cx + 6 * s, cy - 50 * s, cx + 62 * s, cy + 6 * s), fill=GOLD)
    c.text((cx + 34 * s, cy - 22 * s), "16+", FONT_SANS, 24 * s, GREEN_D)

def i_house_s(c, cx, cy, s=1.0):
    house(c, cx, cy, 1.0 * s)

def i_ok(c, cx, cy, s=1.0):
    shield(c, cx, cy, 0.95 * s)

def i_clock_s(c, cx, cy, s=1.0):
    clock(c, cx, cy, 54 * s)

def i_tool(c, cx, cy, s=1.0):
    ic_cardm(c, cx, cy, 0.95 * s)

def i_tag_s(c, cx, cy, s=1.0):
    i_tag(c, cx, cy, 1.0 * s)

def i_seniors_q(c, cx, cy, s=1.0):
    person_ic(c, cx, cy + 10 * s, 1.2 * s, IVORY, head=(240, 224, 200))
    c.text((cx + 46 * s, cy - 34 * s), "?", FONT_SANS, 58 * s, GOLD)

# ------------------------------------------------------------------ generatori
def tile_x(key, fn, l1, l2, w=190, h=215, sc=0.56, cy=84, s1=24):
    def mk():
        c = Cv(w, h)
        c.rrect((3, 3, w - 3, h - 3), 26, fill=CARD, outline=GOLD, width=5)
        sz = s1 if len(l1) < 9 else s1 - 4
        if l2:
            c.text((w / 2, h - 57), l1, FONT_SANS, sz, IVORY)
            c.text((w / 2, h - 27), l2, FONT_SANS, sz, GOLD)
        else:
            c.text((w / 2, h - 43), l1, FONT_SANS, sz + (2 if len(l1) < 9 else 0), GOLD)
        im = c.done()
        paste_c(im, mini(fn, sc), w / 2, cy)
        return im
    return cache(key, mk)

def common5(img, t, text, n=None):
    common4(img, t, text, n)

def title_lines(img, t, t0, l1, l2, s1=100, s2=100, x=590, y1=260, y2=380, c1=IVORY, c2=GOLD):
    h1 = fade(t, t0)
    if h1 > 0:
        put_left(img, tspr(l1, FONT_SANS, s1, c1), x, y1, s1, alpha=h1)
        put_left(img, tspr(l2, FONT_SANS, s2, c2), x, y2, s2, alpha=h1)

def big_badge(img, t, t0, n, fs=190, x=330, y=300, sc=0.8):
    b = pop(t, t0, 0.55)
    put(img, num_badge(n, 380, fs), x, y, scale=sc * b[0], alpha=b[1], shadow=16)
    burst(img, t, t0 + 0.3, x, y, n=14, seed=3, rad=240)

# ============================================================ BLOCCO 41
TILES41 = [(ic_tv, "TELEVISION", ""), (ic_projector, "PROJECTOR", ""), (ic_fridge, "MAJOR", "APPLIANCE"), (ic_computer, "COMPUTER", ""),
           (ic_tablet, "TABLET", ""), (i_watch, "SMART", "WATCH"), (ic_camera, "CAMERA", ""), (i_camcorder, "CAMCORDER", ""),
           (i_music, "MUSIC", "PLAYER"), (i_phone_s, "CELL", "PHONE")]

def draw41(img, t):
    ts = starts(41)
    common5(img, t, "THE 90 DAY LIMIT", 9)
    show(img, t, ts[0], chipx("c41a", 1500, 130, GREEN_L, SAGE, i_ok, 0.5, ("MOST THINGS CAN BE RETURNED",), (52,), (IVORY,)), 960, 190, sh=10)
    show(img, t, ts[1], num_badge(90, 330, 170), 270, 580, sh=14)
    show(img, t, ts[1] + 0.5, pill_spr("DAY LIMIT", 44, 380, 84, GOLD, GREEN_D), 270, 800, sh=8)
    for i, (fn, a, b) in enumerate(TILES41):
        show(img, t, ts[2] + 0.1 + i * 0.5, tile_x(("t41", i), fn, a, b), 640 + (i % 5) * 230, 450 + (i // 5) * 240, sh=6, dur=0.4)
    show(img, t, ts[3], chipx("c41b", 700, 150, PANEL_FILL, CORAL, i_clock_s, 0.55, ("DO NOT WAIT",), (60,), (CORAL,)), 480, 930, sh=10)
    show(img, t, ts[4], chipx("c41c", 1000, 150, GREEN_L, GOLD, i_list, 0.5, ("READ THE EXCEPTIONS", "ON COSTCO'S WEBSITE"), (38, 38), (IVORY, GOLD)), 1360, 930, sh=10)

# ============================================================ BLOCCO 42
def draw42(img, t):
    ts = starts(42)
    common5(img, t, "HOW TO RETURN", 9)
    show(img, t, ts[0], card_big("c42a", 520, 400, GOLD, i_wh, 1.0, "TAKE IT TO A", "COSTCO WAREHOUSE", 36, 36, cy=130, r=94), 480, 300, sh=12)
    ar = seg(t, ts[1] - 0.05, 0.35)
    if ar > 0: put(img, arrow_spr(), 960, 300, scale=0.8 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[1], card_big("c42b", 520, 400, GOLD, i_counter, 1.0, "MEMBER SERVICES", "HELPS YOU", 36, 44, cy=130, r=94), 1440, 300, sh=12)
    items = [(ic_tv, "KEEP", "THE ITEM"), (ic_box, "KEEP THE BOX", "IF YOU CAN"), (ic_receipt, "KEEP", "YOUR RECEIPT")]
    for i, (fn, a, b) in enumerate(items):
        show(img, t, ts[2] + 0.1 + i * 0.7, card_big(("c42i", i), 380, 300, SAGE_D, fn, 0.8, a, b, 36, 40, cy=100, r=76), 215 + i * 430, 760, sh=10)
    show(img, t, ts[3] - 0.0, tspr("OR", FONT_SANS, 60, GOLD), 1322, 760, 1.0, sh=0, dur=0.3) if False else None
    o = fade(t, ts[3])
    if o > 0: put(img, tspr("OR", FONT_SANS, 60, GOLD), 1322, 760, alpha=o)
    show(img, t, ts[3] + 0.3, card_big("c42d", 460, 300, GOLD, i_online_receipt, 0.8, "USE THE", "ONLINE RECEIPT", 36, 40, cy=100, r=76), 1610, 760, sh=10)

# ============================================================ BLOCCO 43
def draw43(img, t):
    ts = starts(43)
    common5(img, t, "SAVING NUMBER 10", None)
    big_badge(img, t, ts[0] + 0.2, 10, 170)
    title_lines(img, t, ts[1], "A SECOND CARD", "AT NO EXTRA COST", 90, 76, y1=255, y2=370)
    show(img, t, ts[1] + 0.3, card_spr(), 440, 690, 0.62, -4, sh=14)
    show(img, t, ts[2] - 0.2, card_spr(), 880, 690, 0.62, 4, sh=14)
    show(img, t, ts[2] + 0.4, pill_spr("FREE", 50, 220, 96, CORAL, IVORY), 1010, 515, rot=-8, sh=8)
    show(img, t, ts[2] + 0.9, pill_spr("ONE FREE HOUSEHOLD CARD", 42, 880, 92, GOLD, GREEN_D), 640, 900, sh=8)
    show(img, t, ts[3], chipx("c43a", 760, 150, GREEN_L, GOLD, i_over16, 0.6, ("SOMEONE", "OVER 16"), (38, 56), (SAGE, IVORY)), 1500, 600, sh=10)
    show(img, t, ts[4], chipx("c43b", 760, 150, GREEN_L, GOLD, i_house_s, 0.6, ("LIVES AT THE", "SAME ADDRESS"), (38, 50), (SAGE, IVORY)), 1500, 800, sh=10)

# ============================================================ BLOCCO 44
def draw44(img, t):
    ts = starts(44)
    common5(img, t, "ADDING THE SECOND CARD", 10)
    show(img, t, ts[0], card_big("c44a", 410, 400, GOLD, i_pair, 1.0, "YOUR", "SPOUSE", 40, 56, cy=125, r=92), 255, 330, sh=12)
    show(img, t, ts[1], card_big("c44b", 410, 400, GOLD, i_pair2, 1.0, "ADULT SON OR", "DAUGHTER", 36, 46, cy=125, r=92), 715, 330, sh=12)
    show(img, t, ts[2], card_big("c44c", 410, 400, SAGE_D, i_account, 1.0, "ADD THEM IN YOUR", "ONLINE ACCOUNT", 30, 36, cy=125, r=92), 1175, 330, sh=12)
    ar = seg(t, ts[3] - 0.05, 0.35)
    if ar > 0: put(img, arrow_spr(), 1405, 330, scale=0.55 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[3], card_big("c44d", 410, 400, SAGE_D, i_counter, 1.0, "PICK UP THE CARD", "AT THE COUNTER", 30, 34, cy=125, r=92), 1635, 330, sh=12)
    show(img, t, ts[4], chipx("c44e", 680, 150, GREEN_L, SAGE, i_pair, 0.55, ("TWO PEOPLE", "SHOP"), (36, 56), (SAGE, IVORY)), 470, 770, sh=10)
    show(img, t, ts[5], chipx("c44f", 960, 150, GOLD, (168, 118, 40), i_tool, 0.6, ("YOU PAY FOR", "ONE MEMBERSHIP"), (38, 52), (GREEN_D, GREEN_D)), 1370, 770, sh=12)

# ============================================================ BLOCCO 45
def booklet_spr():
    def mk():
        w, h = 320, 400
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 20, fill=(236, 188, 108), outline=(168, 118, 40), width=5)
        c.rrect((18, 18, w - 18, 96), 12, fill=GREEN_D)
        c.text((w / 2, 57), "SAVINGS", FONT_SANS, 50, GOLD)
        for k in range(2):
            for j in range(2):
                x0 = 28 + j * 138; y0 = 120 + k * 120
                c.rrect((x0, y0, x0 + 124, y0 + 104), 10, fill=IVORY, outline=CORAL, width=3)
                c.line([(x0 + 8, y0 + 90), (x0 + 116, y0 + 90)], CORAL, 3)
                c.text((x0 + 62, y0 + 46), ("%", "$", "$", "%")[k * 2 + j], FONT_SANS, 44, GREEN_D)
        for k in range(8):
            c.ell((6, 24 + k * 46, 20, 38 + k * 46), fill=GREEN_D)
        return c.done()
    return cache("booklet", mk)

def draw45(img, t):
    ts = starts(45)
    common5(img, t, "SAVING NUMBER 11", None)
    big_badge(img, t, ts[0] + 0.2, 11, 190)
    title_lines(img, t, ts[1], "THE SAVINGS", "BOOKLET", 100, 110, y1=260, y2=385)
    show(img, t, ts[2], booklet_spr(), 330, 760, 0.95, -5, sh=14)
    show(img, t, ts[2] + 0.2, chipx("c45a", 1000, 150, GREEN_L, GOLD, i_mailbox, 0.55, ("SENT TO THE", "PRIMARY MEMBER"), (38, 50), (SAGE, IVORY)), 1170, 560, sh=10)
    show(img, t, ts[3], chipx("c45b", 1000, 150, GREEN_L, SAGE, i_tool, 0.6, ("OF ACTIVE", "MEMBERSHIPS"), (38, 50), (SAGE, IVORY)), 1170, 730, sh=10)
    show(img, t, ts[4], chipx("c45c", 520, 140, GOLD, (168, 118, 40), i_chips, 0.5, ("COUPONS: CHIPS",), (40,), (GREEN_D,)), 800, 910, sh=10)
    ar = seg(t, ts[5] - 0.05, 0.35)
    if ar > 0: put(img, arrow_spr(), 1090, 910, scale=0.5 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[5], chipx("c45d", 700, 140, GOLD, (168, 118, 40), i_detergent, 0.5, ("LAUNDRY DETERGENT",), (36,), (GREEN_D,)), 1480, 910, sh=10)

# ============================================================ BLOCCO 46
def draw46(img, t):
    ts = starts(46)
    common5(img, t, "NOTHING TO CUT OUT", 11)
    show(img, t, ts[0], card_big("c46a", 520, 400, CORAL, i_scissors_x, 1.0, "NOTHING TO", "CUT OUT", 40, 56, c2=CORAL, circle=(PANEL_FILL,), cy=130, r=94), 480, 300, sh=12)
    ar = seg(t, ts[1] - 0.05, 0.35)
    if ar > 0: put(img, arrow_spr(), 960, 300, scale=0.8 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[1], card_big("c46b", 520, 400, GOLD, i_register, 1.0, "SAVINGS APPLY", "AT CHECKOUT", 38, 46, cy=130, r=94), 1440, 300, sh=12)
    show(img, t, ts[2], pill_spr("THE SAME SAVINGS ARE ALSO FOUND", 40, 1100, 90, GOLD, GREEN_D), 960, 600, sh=8)
    show(img, t, ts[2] + 0.6, chipx("c46c", 760, 170, GREEN_L, GOLD, i_web, 0.62, ("ON THE", "COSTCO WEBSITE"), (38, 50), (SAGE, IVORY)), 480, 810, sh=12)
    show(img, t, ts[3], chipx("c46d", 760, 170, GREEN_L, GOLD, i_app, 0.62, ("IN THE", "COSTCO APP"), (38, 56), (SAGE, IVORY)), 1440, 810, sh=12)

# ============================================================ BLOCCO 47
def draw47(img, t):
    ts = starts(47)
    common5(img, t, "IF THE BOOKLET NEVER ARRIVES", 11)
    show(img, t, ts[0], chipx("c47a", 1500, 150, GREEN_L, GOLD, i_mailbox, 0.55, ("THE BOOKLET NEVER ARRIVES?",), (56,), (IVORY,)), 960, 200, sh=10)
    cards = [(i_envelope_x, "YOU OPTED OUT", "OF MAILERS", CORAL), (i_house_pin, "ADDRESS WRONG OR", "CHANGED IN 3 MONTHS", GOLD), (i_card_cal, "MEMBERSHIP IS", "NEW OR EXPIRED", GOLD)]
    for i, (fn, a, b, col) in enumerate(cards):
        show(img, t, ts[2 + i], card_big(("c47", i), 520, 400, col, fn, 1.0, a, b, 34, 32, cy=130, r=94), 300 + i * 660, 530, sh=12)
    show(img, t, ts[5], chipx("c47d", 1100, 150, GREEN_L, SAGE, i_counter, 0.55, ("ASK AT THE", "MEMBERSHIP COUNTER"), (36, 40), (SAGE, IVORY)), 640, 900, sh=10)
    show(img, t, ts[6], chipx("c47e", 600, 150, GOLD, (168, 118, 40), i_ok, 0.55, ("THEY CAN", "FIX IT"), (36, 56), (GREEN_D, GREEN_D)), 1520, 900, sh=10)

# ============================================================ BLOCCO 48
def draw48(img, t):
    ts = starts(48)
    common5(img, t, "SAVING NUMBER 12", None)
    big_badge(img, t, ts[0] + 0.2, 12, 190)
    title_lines(img, t, ts[1], "YOUR RECEIPTS,", "ONLINE", 90, 110, y1=255, y2=380)
    show(img, t, ts[2], chipx("c48a", 760, 140, GREEN_L, GOLD, i_card_cal, 0.5, ("KEPT FOR TWO YEARS",), (46,), (IVORY,)), 960, 525, sh=10)
    steps = [(i_signin, "SIGN IN TO YOUR", "COSTCO ACCOUNT", 34, 36), (i_list, "SELECT", "ORDERS AND PURCHASES", 40, 30), (i_tabs, "OPEN THE", "IN WAREHOUSE TAB", 40, 32)]
    for i, (fn, a, b, s1, s2) in enumerate(steps):
        show(img, t, ts[3 + i], card_big(("c48", i), 520, 400, GOLD, fn, 1.0, a, b, s1, s2, cy=120, r=90), 300 + i * 660, 805, sh=12)
        if i > 0:
            ar = seg(t, ts[3 + i] - 0.05, 0.35)
            if ar > 0: put(img, arrow_spr(), 300 + i * 660 - 330, 805, scale=0.6 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))

# ============================================================ BLOCCO 49
def draw49(img, t):
    ts = starts(49)
    common5(img, t, "WHY THE RECEIPT MATTERS", 12)
    intro(img, t, "WHY DOES", "THIS MATTER?", ts[1], size=140)
    show(img, t, ts[1], chipx("c49a", 1400, 130, GREEN_L, GOLD, i_receipt_big, 0.5, ("THE RECEIPT IS WHAT YOU NEED FOR:",), (46,), (IVORY,)), 960, 200, sh=10)
    items = [(i_counter, "A RETURN", ""), (i_tag_s, "A PRICE", "ADJUSTMENT"), (ic_headset, "THE CONCIERGE", "PHONE NUMBER")]
    for i, (fn, a, b) in enumerate(items):
        show(img, t, ts[1 + i] + (0.8 if i == 0 else 0.0), card_big(("c49", i), 520, 400, GOLD, fn, 1.0, a, b, 40 if i == 0 else 38, 46 if i == 0 else 38, cy=130, r=94), 300 + i * 660, 520, sh=12)
    show(img, t, ts[4], chipx("c49b", 1500, 150, PANEL_FILL, CORAL, i_drawer_x, 0.55, ("NO MORE LOOKING FOR A", "FADED PAPER IN A DRAWER"), (36, 44), (IVORY, CORAL)), 960, 890, sh=12)

# ============================================================ BLOCCO 50
def draw50(img, t):
    ts = starts(50)
    common5(img, t, "PLAINLY", None)
    intro(img, t, "LET ME SAY IT", "PLAINLY", ts[1], size=140)
    s_, a_, p_ = pop(t, ts[1] + 0.1, 0.5)
    if p_ > 0:
        put(img, senior_tag(), 430, 320, scale=0.8 * s_, rot=-4, alpha=a_, shadow=14)
        sg = seg(t, ts[1] + 0.9, 0.4)
        if sg > 0:
            put(img, no_sign(), 430, 320, scale=max(ease_back(sg), 0.01) * 0.62, alpha=min(1, sg * 3))
    show(img, t, ts[1] + 0.6, chipx("c50a", 1000, 150, PANEL_FILL, CORAL, i_tag_s, 0.55, ("NONE OF THESE 12 THINGS", "IS AN AGE DISCOUNT"), (40, 44), (IVORY, CORAL)), 1330, 320, sh=12)
    show(img, t, ts[2], chipx("c50b", 1700, 150, GREEN_L, GOLD, i_tool, 0.6, ("TOOLS COSTCO ALREADY OFFERS", "TO EVERY MEMBER"), (44, 44), (IVORY, GOLD)), 960, 610, sh=12)
    show(img, t, ts[3], chipx("c50c", 900, 150, PANEL_FILL, SAGE_D, i_seniors_q, 0.55, ("MANY SENIORS", "NEVER USE THEM"), (38, 52), (SAGE, IVORY)), 520, 830, sh=10)
    show(img, t, ts[4], chipx("c50d", 800, 150, PANEL_FILL, CORAL, i_bubble_x, 0.55, ("NOBODY", "EXPLAINS THEM"), (38, 52), (IVORY, CORAL)), 1450, 830, sh=10)

DRAW.update({41: draw41, 42: draw42, 43: draw43, 44: draw44, 45: draw45, 46: draw46, 47: draw47, 48: draw48, 49: draw49, 50: draw50})

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
