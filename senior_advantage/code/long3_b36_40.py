"""Video lungo 3 (Costco) - blocchi 36-40 (gomme: garanzia e costo, punto 8 prezzo scende, punto 9 resi).
Durate dalla timeline dell'utente (07/10/2026): B36 275, B37 338, B38 255, B39 418, B40 309 fotogrammi.
Uso: OUT=cartella python3 long3_b36_40.py <blocco 36..40> [fotogrammi]
     python3 long3_b36_40.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long3_b31_35 import *

DUR.update({36: 304, 37: 338, 38: 255, 39: 418, 40: 309})
PHRASES.update({
    36: ["There is also a five year road hazard warranty.", "All of this applies only to tires", "you bought from the Costco tire center,", "so keep your paperwork."],
    37: ["Tires are one of the biggest bills a retired driver faces.", "Knowing that rotation, balancing and flat repairs are already included",
         "can change where you decide to buy them."],
    38: ["Eight.", "Money back when a price drops.", "If something you bought at Costco", "goes down in price within thirty days,", "you can ask for the difference."],
    39: ["In the warehouse, go to the returns counter", "of the Costco where you bought it,", "and bring your receipt.",
         "For online orders, the credit usually comes back in five to ten business days.", "Promotional item limits can apply."],
    40: ["Nine.", "The return policy.", "Costco calls it a risk free,", "one hundred percent satisfaction guarantee", "on membership and merchandise,", "with a few exceptions."],
})

# ------------------------------------------------------------------ icone nuove
def i_road(c, cx, cy, s=1.0):
    c.poly([(cx - 30 * s, cy - 60 * s), (cx + 30 * s, cy - 60 * s), (cx + 66 * s, cy + 60 * s), (cx - 66 * s, cy + 60 * s)], fill=(70, 78, 76))
    for k in range(3):
        c.rrect((cx - 4 * s, cy - 50 * s + k * 38 * s, cx + 4 * s, cy - 32 * s + k * 38 * s), 2 * s, fill=GOLD)
    c.poly([(cx + 26 * s, cy + 6 * s), (cx + 46 * s, cy + 40 * s), (cx + 6 * s, cy + 40 * s)], fill=(230, 160, 70))
def i_five(c, cx, cy, s=1.0):
    c.ell((cx - 58 * s, cy - 58 * s, cx + 58 * s, cy + 58 * s), fill=GOLD, outline=(168, 118, 40), width=5 * s)
    c.text((cx, cy - 6 * s), "5", FONT_SERIF, 74 * s, GREEN_D)
    c.text((cx, cy + 34 * s), "YEARS", FONT_SANS, 17 * s, GREEN_D)
def i_garage(c, cx, cy, s=1.0):
    c.poly([(cx - 70 * s, cy - 14 * s), (cx, cy - 64 * s), (cx + 70 * s, cy - 14 * s)], fill=CORAL)
    c.rrect((cx - 58 * s, cy - 16 * s, cx + 58 * s, cy + 58 * s), 4 * s, fill=IVORY)
    c.rrect((cx - 38 * s, cy + 6 * s, cx + 38 * s, cy + 58 * s), 3 * s, fill=(176, 188, 180))
    for k in range(3): c.line([(cx - 38 * s, cy + (18 + k * 14) * s), (cx + 38 * s, cy + (18 + k * 14) * s)], (140, 152, 144), 3 * s)
def i_folder(c, cx, cy, s=1.0):
    c.rrect((cx - 56 * s, cy - 40 * s, cx - 8 * s, cy - 22 * s), 6 * s, fill=(236, 188, 108))
    c.rrect((cx - 62 * s, cy - 30 * s, cx + 62 * s, cy + 48 * s), 8 * s, fill=(236, 188, 108))
    c.rrect((cx - 46 * s, cy - 18 * s, cx + 46 * s, cy + 36 * s), 4 * s, fill=IVORY)
    for k in range(3): c.line([(cx - 32 * s, cy + (-4 + k * 14) * s), (cx + 32 * s - k * 10 * s, cy + (-4 + k * 14) * s)], (150, 160, 152), 3 * s)
def i_driver(c, cx, cy, s=1.0):
    person_ic(c, cx, cy + 6 * s, 1.3 * s, (150, 150, 150), head=SKIN)
    c.arc((cx - 62 * s, cy - 8 * s, cx + 62 * s, cy + 68 * s), 200, 340, IVORY, 7 * s)
def i_receipt_s(c, cx, cy, s=1.0): ic_receipt(c, cx, cy, s)
def i_down(c, cx, cy, s=1.0):
    c.poly([(cx - 18 * s, cy - 56 * s), (cx + 18 * s, cy - 56 * s), (cx + 18 * s, cy + 6 * s), (cx + 48 * s, cy + 6 * s), (cx, cy + 58 * s), (cx - 48 * s, cy + 6 * s), (cx - 18 * s, cy + 6 * s)], fill=GOLD)
def i_30(c, cx, cy, s=1.0):
    c.rrect((cx - 58 * s, cy - 50 * s, cx + 58 * s, cy + 56 * s), 12 * s, fill=IVORY)
    c.rrect((cx - 58 * s, cy - 50 * s, cx + 58 * s, cy - 14 * s), 12 * s, fill=CORAL)
    c.d.rectangle(c._b((cx - 58 * s, cy - 30 * s, cx + 58 * s, cy - 14 * s)), fill=CORAL)
    c.text((cx, cy + 20 * s), "30", FONT_SERIF, 54 * s, GREEN_D)
    c.text((cx, cy - 30 * s), "DAYS", FONT_SANS, 20 * s, IVORY)
def i_counter(c, cx, cy, s=1.0):
    c.rrect((cx - 66 * s, cy - 10 * s, cx + 66 * s, cy + 54 * s), 8 * s, fill=IVORY, outline=SAGE_D, width=4 * s)
    c.rrect((cx - 66 * s, cy - 24 * s, cx + 66 * s, cy - 6 * s), 6 * s, fill=GOLD)
    person_ic(c, cx, cy - 34 * s, 0.7 * s, (190, 140, 66))
    c.text((cx, cy + 22 * s), "RETURNS", FONT_SANS, 20 * s, GREEN_D)
def i_parcel(c, cx, cy, s=1.0):
    ic_box(c, cx, cy, s)
    c.ell((cx + 22 * s, cy + 6 * s, cx + 70 * s, cy + 54 * s), fill=GOLD)
    c.text((cx + 46 * s, cy + 32 * s), "$", FONT_SANS, 34 * s, GREEN_D)
def i_online(c, cx, cy, s=1.0):
    ic_laptop(c, cx, cy, s * 0.9)
def i_days(c, cx, cy, s=1.0):
    calendar(c, cx, cy, s)
    c.text((cx, cy + 24 * s), "5-10", FONT_SANS, 24 * s, GREEN_D)
def i_tag(c, cx, cy, s=1.0):
    c.poly([(cx - 60 * s, cy - 8 * s), (cx - 14 * s, cy - 54 * s), (cx + 58 * s, cy - 54 * s), (cx + 58 * s, cy + 18 * s), (cx + 12 * s, cy + 64 * s)], fill=GOLD)
    c.ell((cx + 22 * s, cy - 40 * s, cx + 44 * s, cy - 18 * s), fill=GREEN_D)
    c.text((cx + 6 * s, cy + 6 * s), "%", FONT_SANS, 44 * s, GREEN_D)
def i_heart(c, cx, cy, s=1.0):
    c.ell((cx - 56 * s, cy - 50 * s, cx + 2 * s, cy + 8 * s), fill=CORAL)
    c.ell((cx - 2 * s, cy - 50 * s, cx + 56 * s, cy + 8 * s), fill=CORAL)
    c.poly([(cx - 54 * s, cy - 6 * s), (cx + 54 * s, cy - 6 * s), (cx, cy + 58 * s)], fill=CORAL)
def i_hundred(c, cx, cy, s=1.0):
    c.ell((cx - 60 * s, cy - 60 * s, cx + 60 * s, cy + 60 * s), fill=GOLD, outline=(168, 118, 40), width=5 * s)
    c.text((cx, cy - 4 * s), "100%", FONT_SANS, 40 * s, GREEN_D)
    check_ic(c, cx, cy + 30 * s, 0.45 * s, GREEN_D)
def i_member(c, cx, cy, s=1.0): ic_cardm(c, cx, cy, s)
def i_goods(c, cx, cy, s=1.0): ic_box(c, cx, cy, s)
def i_exc(c, cx, cy, s=1.0): warn_tri(c, cx, cy, 1.0 * s, GOLD, GREEN_D)
def i_phone_s(c, cx, cy, s=1.0): ic_phone_contact(c, cx, cy, s)
def i_watch(c, cx, cy, s=1.0):
    c.rrect((cx - 20 * s, cy - 64 * s, cx + 20 * s, cy + 64 * s), 8 * s, fill=(110, 120, 116))
    c.rrect((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), 18 * s, fill=GREEN_D, outline=IVORY, width=6 * s)
    c.line([(cx, cy), (cx, cy - 24 * s)], IVORY, 5 * s); c.line([(cx, cy), (cx + 18 * s, cy + 8 * s)], GOLD, 5 * s)
def i_music(c, cx, cy, s=1.0):
    c.ell((cx - 48 * s, cy + 14 * s, cx - 6 * s, cy + 50 * s), fill=IVORY); c.ell((cx + 16 * s, cy + 2 * s, cx + 58 * s, cy + 38 * s), fill=IVORY)
    c.line([(cx - 10 * s, cy + 30 * s), (cx - 10 * s, cy - 44 * s), (cx + 54 * s, cy - 56 * s), (cx + 54 * s, cy + 20 * s)], IVORY, 7 * s)
def i_cell(c, cx, cy, s=1.0): ic_phone(c, cx, cy, s)

# ============================================================ BLOCCO 36
def draw36(img, t):
    ts = starts(36)
    common4(img, t, "TIRE PROTECTION", 7 if False else None)
    s_, a_, p_ = pop(t, 0.2, 0.4)
    put(img, num_badge(7, 120, 70), 96, 78, scale=s_, alpha=a_, shadow=5)
    show(img, t, ts[0], card_big("c36a", 620, 440, GOLD, i_five, 1.15, "FIVE YEAR", "ROAD HAZARD WARRANTY", 46, 36, cy=140, r=108), 480, 340, sh=14)
    ar = seg(t, ts[0] + 0.7, 0.4)
    show(img, t, ts[0] + 0.9, card_big("c36b", 520, 440, SAGE_D, i_road, 1.0, "ROAD", "HAZARDS", 46, 56, cy=140, r=104), 1160, 340, sh=14)
    show(img, t, ts[1], mk_chip("c36c", 1500, 170, GREEN_L, GOLD, i_garage, 0.8, ("ONLY FOR TIRES YOU BOUGHT", "FROM THE COSTCO TIRE CENTER"), (42, 50), (IVORY, GOLD)), 960, 700, sh=12)
    show(img, t, ts[3], mk_chip("c36d", 1500, 170, GOLD, (168, 118, 40), i_folder, 0.8, ("KEEP YOUR PAPERWORK",), (64,), (GREEN_D,)), 960, 920, sh=12)
    if t > ts[3]: burst(img, t, ts[3] + 0.3, 960, 920, n=10, seed=3, rad=110)

# ============================================================ BLOCCO 37
def draw37(img, t):
    ts = starts(37)
    common4(img, t, "WHERE TO BUY YOUR TIRES", None)
    show(img, t, ts[0], card_big("c37a", 560, 440, CORAL, i_driver, 1.0, "TIRES: ONE OF THE", "BIGGEST BILLS", 38, 56, c2=CORAL, circle=(PANEL_FILL,), cy=140, r=104), 480, 320, sh=14)
    show(img, t, ts[0] + 0.7, pill_spr("FOR A RETIRED DRIVER", 46, 780, 96, PANEL_FILL, CORAL, CORAL), 480, 640, sh=8)
    items = [(i_rot, "ROTATIONS"), (i_bal, "BALANCING"), (i_patch, "FLAT REPAIRS")]
    for i, (fn, tx) in enumerate(items):
        def mk(i=i, fn=fn, tx=tx):
            return card_big(("c37i", i), 330, 330, GOLD, fn, 0.85, tx, "INCLUDED", 34, 40, cy=105, r=80)
        show(img, t, ts[1] + 0.3 + i * 0.7, mk(), 1010 + i * 350, 330, sh=10)
    ar = seg(t, ts[2], 0.4)
    if ar > 0: put(img, arrow_spr(), 960, 790, scale=1.0 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3), rot=90)
    show(img, t, ts[2] + 0.3, mk_chip("c37d", 1620, 190, GREEN_L, GOLD, i_cart_pin, 0.8, ("ALREADY INCLUDED CAN CHANGE", "WHERE YOU DECIDE TO BUY"), (44, 54), (IVORY, GOLD)), 960, 930, sh=14)

def i_cart_pin(c, cx, cy, s=1.0):
    ic_cart(c, cx - 8 * s, cy + 10 * s)

# ============================================================ BLOCCO 38
def draw38(img, t):
    ts = starts(38)
    common4(img, t, "SAVING NUMBER 8", None)
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(8), 330, 300, scale=0.8 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 300, n=14, seed=3, rad=240)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("MONEY BACK", FONT_SANS, 110, GOLD), 590, 260, 110, alpha=h1)
        put_left(img, tspr("WHEN A PRICE DROPS", FONT_SANS, 76, IVORY), 590, 370, 76, alpha=h1)
    show(img, t, ts[2], card_big("c38a", 440, 400, SAGE_D, i_receipt_s, 0.95, "YOU BOUGHT IT", "AT COSTCO", 34, 44, cy=130, r=94), 330, 650, sh=12)
    def drop(c, x, y, s=1.0):
        i_down(c, x, y, s)
    show(img, t, ts[3], card_big("c38b", 440, 400, GOLD, i_30, 1.0, "PRICE GOES DOWN", "WITHIN 30 DAYS", 34, 42, cy=130, r=94), 960, 650, sh=12)
    show(img, t, ts[4], card_big("c38c", 440, 400, GOLD, i_dollar_back, 1.0, "ASK FOR", "THE DIFFERENCE", 40, 48, cy=130, r=94), 1590, 650, sh=12)
    for i in range(2):
        ar = seg(t, ts[3] - 0.05 + i * (ts[4] - ts[3]), 0.35)
        if ar > 0: put(img, arrow_spr(), 645 + i * 630, 650, scale=0.6 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    if t > ts[4] + 0.3: burst(img, t, ts[4] + 0.3, 1590, 650, n=10, seed=5, rad=140)

def i_dollar_back(c, cx, cy, s=1.0):
    ic_dollar(c, cx, cy, s)
    c.arc((cx - 66 * s, cy - 66 * s, cx + 66 * s, cy + 66 * s), 200, 340, GOLD, 8 * s)
    c.poly([(cx - 66 * s, cy - 10 * s), (cx - 48 * s, cy - 36 * s), (cx - 82 * s, cy - 40 * s)], fill=GOLD)

# ============================================================ BLOCCO 39
def draw39(img, t):
    ts = starts(39)
    common4(img, t, "HOW TO GET IT", 8)
    show(img, t, ts[0], card_big("c39a", 520, 400, GOLD, i_counter, 1.0, "RETURNS COUNTER", "IN THE WAREHOUSE", 34, 38, cy=130, r=94), 330, 300, sh=12)
    show(img, t, ts[1], card_big("c39b", 520, 400, GOLD, ic_store, 1.0, "THE COSTCO WHERE", "YOU BOUGHT IT", 34, 40, cy=130, r=94), 960, 300, sh=12)
    show(img, t, ts[2], card_big("c39c", 520, 400, GOLD, i_receipt_s, 0.95, "BRING YOUR", "RECEIPT", 44, 56, cy=130, r=94), 1590, 300, sh=12)
    for i in range(2):
        ar = seg(t, ts[1] - 0.05 + i * (ts[2] - ts[1]), 0.35)
        if ar > 0: put(img, arrow_spr(), 645 + i * 630, 300, scale=0.55 * max(ease_back(ar), 0.01), alpha=min(1, ar * 3))
    show(img, t, ts[3], mk_chip("c39d", 1000, 180, GREEN_L, SAGE, i_online, 0.8, ("ONLINE ORDERS:", "CREDIT USUALLY IN"), (44, 50), (SAGE, IVORY)), 570, 700, sh=12)
    show(img, t, ts[3] + 0.8, mk_chip("c39e", 620, 180, GOLD, (168, 118, 40), i_days, 0.8, ("5 TO 10", "BUSINESS DAYS"), (60, 40), (GREEN_D, GREEN_D)), 1500, 700, sh=12)
    show(img, t, ts[4], mk_chip("c39f", 1620, 150, PANEL_FILL, CORAL, w_coral, 1.0, ("PROMOTIONAL ITEM LIMITS CAN APPLY",), (54,), (CORAL,)), 960, 930, sh=12)

# ============================================================ BLOCCO 40
def draw40(img, t):
    ts = starts(40)
    common4(img, t, "SAVING NUMBER 9", None)
    b = pop(t, ts[0] + 0.3, 0.55)
    put(img, num_badge(9), 330, 300, scale=0.8 * b[0], alpha=b[1], shadow=16)
    burst(img, t, ts[0] + 0.6, 330, 300, n=14, seed=3, rad=240)
    h1 = fade(t, ts[1])
    if h1 > 0:
        put_left(img, tspr("THE RETURN", FONT_SANS, 110, GOLD), 590, 260, 110, alpha=h1)
        put_left(img, tspr("POLICY", FONT_SANS, 110, IVORY), 590, 380, 110, alpha=h1)
    show(img, t, ts[2], mk_chip("c40a", 540, 160, GREEN_L, GOLD, i_shield_free, 0.8, ("RISK FREE",), (66,), (GOLD,)), 1600, 330, sh=10)
    show(img, t, ts[3], mk_chip("c40b", 1500, 190, GOLD, (168, 118, 40), i_hundred, 0.8, ("100% SATISFACTION", "GUARANTEE"), (66, 50), (GREEN_D, GREEN_D)), 960, 650, sh=14)
    show(img, t, ts[4], card_big("c40c", 420, 300, GOLD, i_member, 0.8, "MEMBERSHIP", "", 42, 40, cy=100, r=76), 400, 895, sh=10)
    show(img, t, ts[4] + 0.5, card_big("c40d", 420, 300, GOLD, i_goods, 0.8, "MERCHANDISE", "", 42, 40, cy=100, r=76), 880, 895, sh=10)
    show(img, t, ts[5], mk_chip("c40e", 680, 150, PANEL_FILL, GOLD, w_gold, 1.0, ("A FEW EXCEPTIONS",), (48,), (GOLD,)), 1480, 895, sh=10)

def i_shield_free(c, cx, cy, s=1.0): shield(c, cx, cy, 1.0 * s)

DRAW.update({36: draw36, 37: draw37, 38: draw38, 39: draw39, 40: draw40})

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
