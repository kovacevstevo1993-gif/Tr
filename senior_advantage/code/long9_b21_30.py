"""Video lungo 9 (ALDI) - blocchi 21-30."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long9_kit import *
from long9_b01_10 import I, S, mini_icon_card
from long9_b11_20 import ic_warn2
from long8_b21_32 import endbox, disc_panel

def G(img, t, b, key, w, h, icon, title, sub, x, y, col=SAGE_D, tsize=30, ssize=28, mode="right", n=1, **kw):
    return show(img, t, T(b, key, n), glass9((b, key, title), w, h, icon, title, sub, col=col, tsize=tsize, ssize=ssize, **kw), x, y, mode=mode, amp=3)

def XI(c, x, y):
    ic_x(c, x, y, 0.7, CORAL, 14)

def draw21(img, t):
    b = 21
    head9(img, t, 8, "ONLINE PROBLEMS: THREE DAYS")
    show(img, t, T(b, "within three days"), bignum("d21", 380, 200, "3 DAYS", "AFTER PICKUP OR DELIVERY", GOLD, vsize=84, lsize=22), 360, 330, amp=4)
    tt = T(b, "missing")
    show(img, t, tt, mini_icon_card("ms21", 270, 230, lambda c, x, y: (ic_box8(c, x, y - 12, 0.9), ic_x(c, x + 40, y - 8, 0.5, CORAL, 14)), "MISSING", None, accent=CORAL), 210, 600, mode="up", amp=5)
    show(img, t, T(b, "damaged"), mini_icon_card("dm21", 270, 230, I(ic_warn2, 0.8), "DAMAGED", None, accent=AMBER), 510, 600, mode="up", amp=5, ph=1)
    show(img, t, T(b, "spoiled"), mini_icon_card("sp21", 270, 230, I(ic_apple, 1.0), "SPOILED", None, accent=CORAL), 810, 600, mode="up", amp=5, ph=2)
    G(img, t, b, "tell Instacart", 760, 130, I(ic_phone_app, 0.5), "TELL INSTACART", "WITHIN THREE DAYS", 1400, 330, col=GOLD)
    G(img, t, b, "Refunds on online orders", 760, 130, I(ic_repeat, 0.55), "REFUNDS GO THROUGH", "INSTACART", 1400, 500, col=OKG)
    show(img, t, T(b, "returns or exchanges"), stamp9("NO ONLINE RETURNS OR EXCHANGES", 760, 100, CORAL, 30), 1400, 690, rot=-2, amp=3)
    G(img, t, b, "different system", 560, 120, I(ic_phone_app, 0.5), "ONLINE: INSTACART", None, 480, 910, col=SKY, mode="left")
    show(img, t, T(b, "different system") + 0.2, arrow9(110, 52, GOLD), 880, 910, mode="fade", amp=2)
    G(img, t, b, "store system", 640, 120, I(ic_storefront, 0.55), "IN STORE: THE STORE SYSTEM", None, 1300, 910, col=OKG)
    source9(img, t, LAST(b), "help.aldi.us")

def draw22(img, t):
    b = 22
    head9(img, t, 9, "YOUR RECEIPT")
    show(img, t, T(b, "Your receipt"), receipt9("r22", 440, 660, [("MILK", ""), ("EGGS", ""), ("CHEESE", ""), ("TOTAL", "")], hl=1), 330, 590, mode="left", amp=4, rot=-2)
    show(img, t, T(b, "scanned wrong"), stamp9("SCANNED WRONG?", 340, 90, CORAL, 30), 330, 985, rot=-6, amp=3)
    G(img, t, b, "bring the receipt back", 1100, 130, I(ic_receipt, 0.55), "BRING THE RECEIPT BACK TO THE STORE", None, 1250, 290, col=GOLD, tsize=32)
    G(img, t, b, "manager on duty", 1100, 130, I(ic_person, 0.7), "ASK FOR THE MANAGER ON DUTY", None, 1250, 440, col=OKG, tsize=32)
    G(img, t, b, "second charge", 1100, 150, I(ic_paycard, 0.5, col=(60, 112, 88)), "A SECOND CHARGE AFTER A CARD PAYMENT?", "A TEMPORARY PENDING CHARGE CAN APPEAR", 1250, 600, col=SKY, tsize=30, ssize=28)
    show(img, t, T(b, "ten business days"), bignum("bd22", 420, 170, "10", "BUSINESS DAYS TO DROP OFF", GOLD, vsize=84, lsize=22), 920, 790, amp=4)
    show(img, t, T(b, "depending on your bank"), pill9("DEPENDS ON YOUR BANK", 520, 62, fill=IVORY), 1500, 790, mode="right", amp=2)
    show(img, t, T(b, "parking lot"), pill9("LOOK AT IT BEFORE YOU LEAVE THE PARKING LOT", 960, 64, fill=GOLD), 1150, 960, mode="up", amp=2)
    source9(img, t, LAST(b), "help.aldi.us")

def draw23(img, t):
    b = 23
    head9(img, t, 9, "KEEP THE RECEIPT")
    show(img, t, T(b, "keep the receipt"), receipt9("r23", 380, 520, [("MILK", ""), ("EGGS", ""), ("TOTAL", "")], hl=2), 290, 540, mode="left", amp=4, rot=-3)
    show(img, t, T(b, "original form of payment"), paper9("wr23", 1000, 250, "WITH THE RECEIPT", ["REFUND IN THE ORIGINAL", "FORM OF PAYMENT"], accent=OKG, size=38, icon=lambda c, x, y, s: check_ic(c, x, y, 0.7, GREEN_D)), 1230, 330, mode="right", amp=3)
    show(img, t, T(b, "Without one"), paper9("wo23", 1000, 330, "WITHOUT ONE", ["ALDI MERCHANDISE CREDIT GIFT CARD", "AT THE CURRENT RETAIL PRICE", ("MAY NOT MATCH WHAT YOU PAID", (190, 60, 50))], accent=CORAL, size=34, icon=lambda c, x, y, s: ic_x(c, x, y, 0.5, IVORY, 12)), 1230, 650, mode="right", amp=3, ph=1)
    show(img, t, T(b, "in your bag"), pill9("KEEP IT UNTIL THE PRODUCT IS GONE", 800, 62, fill=GOLD), 700, 950, mode="up", amp=2)
    show(img, t, T(b, "difference between"), stamp9("MONEY BACK, NOT CREDIT", 520, 96, OKG, 30), 1500, 950, rot=-2, amp=3)
    source9(img, t, LAST(b), "help.aldi.us", x=1620, y=1040)

def draw24(img, t):
    b = 24
    head9(img, t, 10, "THE TWICE AS NICE GUARANTEE")
    show(img, t, T(b, "Twice as Nice"), mini_icon_card("sh24", 420, 430, lambda c, x, y: ic_shield(c, x, y - 10, 1.5, mark=lambda c2, cx, cy, s2: c2.text((cx, cy + 4), "2x", FONT_SANS, 52, GOLD)), "TWICE AS NICE", "GUARANTEE", glow=True), 300, 520, mode="pop", amp=5)
    G(img, t, b, "not one hundred percent satisfied", 1100, 130, I(ic_cheese, 0.7), "NOT SATISFIED WITH THE QUALITY?", None, 1250, 300, col=CORAL, tsize=32)
    tr = T(b, "replace the product")
    show(img, t, tr, mini_icon_card("rp24", 300, 240, I(ic_repeat, 1.2), "REPLACEMENT", None, accent=OKG), 760, 560, mode="up", amp=5)
    show(img, t, tr + 0.3, txt("+", 90, GOLD, 2), 990, 560, mode="fade", amp=2)
    show(img, t, tr + 0.5, mini_icon_card("rf24", 300, 240, I(ic_bank, 1.0), "REFUND", None, accent=GOLD), 1220, 560, mode="up", amp=5, ph=1)
    show(img, t, T(b, "Both, not one"), stamp9("BOTH, NOT ONE", 400, 100, OKG, 34), 1650, 560, rot=3, amp=3)
    G(img, t, b, "packaging", 1100, 140, I(ic_storefront, 0.55), "BRING THE PACKAGING AND ANY UNUSED PRODUCT", "TO YOUR LOCAL ALDI STORE MANAGER", 1250, 770, col=GOLD, tsize=28, ssize=28)
    show(img, t, T(b, "in the store only"), pill9("PURCHASES MADE IN THE STORE ONLY", 640, 62, fill=SKY), 560, 950, mode="up", amp=2)
    show(img, t, T(b, "not a senior perk"), stamp9("NOT A SENIOR PERK", 420, 92, CORAL, 28), 1130, 950, rot=-2, amp=3)
    show(img, t, T(b, "every shopper"), pill9("IT APPLIES TO EVERY SHOPPER", 520, 62, fill=OKG), 1620, 950, mode="left", amp=2)
    source9(img, t, LAST(b), "aldi.us", x=1620, y=1040)

def draw25(img, t):
    b = 25
    head9(img, t, 10, "THE FINE PRINT")
    G(img, t, b, "non food Aldi Finds", 800, 130, XI, "NON FOOD ALDI FINDS", "NOT COVERED", 480, 300, col=CORAL, tsize=32)
    G(img, t, b, "replacements from an earlier claim", 800, 130, XI, "REPLACEMENTS FROM AN EARLIER CLAIM", "NOT COVERED", 480, 450, col=CORAL, tsize=28)
    G(img, t, b, "nothing to do with quality", 800, 130, XI, "PROBLEMS NOT ABOUT QUALITY", "NOT COVERED", 480, 600, col=CORAL, tsize=32)
    G(img, t, b, "several units", 760, 130, I(ic_box8, 0.6), "SEVERAL UNITS, SAME PROBLEM", None, 1450, 300, col=SKY, tsize=30)
    G(img, t, b, "refund all", 760, 130, lambda c, x, y: check_ic(c, x, y, 0.7, OKG), "ALDI MAY REFUND ALL OF THEM", None, 1450, 450, col=OKG, tsize=30)
    G(img, t, b, "only one replacement", 760, 130, I(ic_repeat, 0.5), "BUT ONLY ONE REPLACEMENT", None, 1450, 600, col=AMBER, tsize=30)
    show(img, t, T(b, "don't wait"), pill9("DON'T WAIT UNTIL THE BOX IS EMPTY", 720, 62, fill=GOLD), 480, 790, mode="up", amp=2)
    show(img, t, T(b, "tastes wrong"), say9("tw25", 560, 100, ["IT TASTES WRONG?"], 36, tail="bl"), 480, 930, mode="up", amp=3)
    show(img, t, T(b, "what's left and your receipt"), checklist9("cl25", 640, ["WHAT'S LEFT OF IT", "YOUR RECEIPT"], size=36, gap=80), 1420, 880, mode="right", amp=3)
    source9(img, t, LAST(b), "aldi.us", x=1620, y=1040)

def numbadge(n):
    return mk(("nb26", n), 72, 72, lambda c: (c.ell((3, 3, 69, 69), fill=GOLD, outline=IVORY, width=3), c.text((36, 38), str(n), FONT_SANS, 40, GREEN_D)), blur=6, dy=4)

def draw26(img, t):
    b = 26
    head9(img, t, -1, "RECAP: THE TEN THINGS", mid="RECAP")
    cpay = lambda c, x, y: ic_paycard(c, x, y, 1.0, (60, 112, 88))
    tiles = [("One, exclusive brands", "EXCLUSIVE BRANDS", "NO COUPONS", I(ic_storefront, 1.2)),
             ("Two, a quarter", "A QUARTER", "AND YOUR BAGS", I(ic_coin25, 1.1)),
             ("Three, the holiday", "HOLIDAY CLOSINGS", "WHAT'S MISSING", I(ic_calendar, 1.3)),
             ("Four, Aldi Finds", "ALDI FINDS", "CHANGE WEEKLY", I(ic_flask, 1.1)),
             ("Five, the weekly ad", "WEEKLY AD", "WEDNESDAY EMAIL", I(ic_envelope, 1.2)),
             ("Six, how you can pay", "HOW YOU PAY", "CASH BACK, SNAP", cpay),
             ("Seven, gift cards", "GIFT CARDS", "NO FEES", I(ic_gift2, 1.1)),
             ("Eight, the real cost", "ONLINE COST", "FEES AND PRICES", I(ic_truck2, 1.1)),
             ("Nine, your receipt", "YOUR RECEIPT", "KEEP IT", I(ic_receipt, 1.2)),
             ("Ten, the Twice", "TWICE AS NICE", "GUARANTEE", I(ic_shield, 1.1))]
    for i, (k, top, bot, ic) in enumerate(tiles):
        x = 215 + (i % 5) * 372; y = 360 + (i // 5) * 420
        tt = T(b, k)
        show(img, t, tt, mini_icon_card(("rc26", i), 330, 360, ic, top, bot, glow=(i == 9)), x, y, mode="pop", amp=4, ph=i * 0.6)
        show(img, t, tt + 0.1, numbadge(i + 1), x - 115, y - 150, mode="pop", amp=2, ph=i)

def draw27(img, t):
    b = 27
    head9(img, t, -1, "YOUR PLAN FOR THE NEXT TRIP", mid="PLAN")
    rows = [("Put a few quarters", I(ic_coin25, 0.8), "A FEW QUARTERS AND YOUR BAGS, READY", None),
            ("Look up your own store", I(ic_pin8, 0.9), "YOUR OWN STORE'S SPECIALS", "WRITE A SHORT LIST"),
            ("Pay with a card", lambda c, x, y: ic_paycard(c, x, y, 0.8, (60, 112, 88)), "PAY WITH A CARD OR CASH", "NOT A CHECK"),
            ("Keep your receipt", I(ic_receipt, 0.6), "KEEP YOUR RECEIPT", "LOOK AT IT BEFORE YOU LEAVE"),
            ("if a product disappoints", I(ic_shield, 0.55), "PRODUCT DISAPPOINTS?", "TAKE THE PACKAGE BACK TO THE MANAGER")]
    for i, (k, ic, a, s_) in enumerate(rows):
        G(img, t, b, k, 1120, 130, ic, a, s_, 700, 290 + i * 160, col=(GOLD, OKG, SKY, GOLD, OKG)[i], tsize=32, mode="left")
    show(img, t, T(b, "none of it depends"), say9("nd27", 440, 330, ["NONE OF IT", "DEPENDS", "ON YOUR AGE"], 46, tail="bl"), 1600, 480, mode="up", amp=4)
    show(img, t, T(b, "whole system"), pill9("THAT'S THE WHOLE SYSTEM", 480, 66, fill=GOLD), 1600, 840, mode="up", amp=2)

def draw28(img, t):
    b = 28
    head9(img, t, -1, "ONE HONEST NOTE", mid="HONEST")
    G(img, t, b, "help center", 900, 130, I(ic_doc, 0.6), "ALL FROM ALDI'S OWN HELP CENTER", "AND CORPORATE PAGES", 520, 290, col=OKG, mode="left", tsize=30)
    G(img, t, b, "dates", 900, 130, I(ic_calendar, 0.5), "THOSE PAGES SHOW NO DATES", None, 520, 440, col=AMBER, mode="left", tsize=32)
    G(img, t, b, "can change", 900, 130, I(ic_clock2, 0.6), "FEES, HOURS AND POLICIES CAN CHANGE", None, 520, 590, col=GOLD, mode="left", tsize=29)
    G(img, t, b, "differ by store", 800, 130, I(ic_storefront, 0.55), "DIFFERENT BY STORE AND BY STATE", None, 1440, 290, col=SKY, tsize=29)
    G(img, t, b, "beer and wine", 800, 130, I(ic_bottle, 0.7), "LIKE BEER AND WINE SALES", None, 1440, 440, col=SKY, tsize=32)
    G(img, t, b, "prices can differ by city", 800, 130, I(ic_pin8, 0.9), "PRICES CAN DIFFER BY CITY", None, 1440, 590, col=SKY, tsize=32)
    G(img, t, b, "your store and Aldi", 1500, 140, I(ic_web, 0.55), "YOUR STORE AND ALDI'S WEBSITE WIN", "OVER ANYTHING IN THIS VIDEO", 960, 810, col=GOLD, tsize=40, ssize=30)
    show(img, t, T(b, "please check"), pill9("PLEASE CHECK BEFORE YOU RELY ON ANY DETAIL", 900, 64, fill=IVORY), 960, 960, mode="up", amp=2)

def draw29(img, t):
    b = 29
    head9(img, t, -1, "THANK YOU FOR WATCHING", mid="THANKS")
    G(img, t, b, "send them", 860, 130, I(ic_envelope, 0.55), "SEND IT TO SOMEONE OVER 60", "WHO SHOPS AT ALDI", 520, 340, col=GOLD, mode="left", tsize=32)
    show(img, t, T(b, "which of these ten"), say9("cm29", 800, 150, ["\"WHICH OF THESE TEN", "DID YOU NOT KNOW ABOUT?\""], 36, tail="bl"), 1420, 340, mode="up", amp=3)
    G(img, t, b, "like the video", 700, 130, I(ic_heart2, 0.6), "LIKE THE VIDEO", None, 520, 620, col=CORAL, tsize=36, mode="left")
    G(img, t, b, "subscribe to", 900, 130, I(ic_bell, 0.6), "SUBSCRIBE TO THE SENIOR ADVANTAGE", None, 1400, 620, col=GOLD, tsize=32)
    G(img, t, b, "practical help", 1500, 130, I(ic_gift2, 0.6), "PRACTICAL HELP AND SAVINGS FOR PEOPLE OVER 60", None, 960, 800, col=OKG, tsize=36, mode="up")
    show(img, t, T(b, "official sources"), pill9("ALWAYS FROM OFFICIAL SOURCES", 700, 64, fill=IVORY), 960, 950, mode="up", amp=2)

DLINES = [("Rules, fees", "Rules, fees and policies change", INK), ("they differ", "and differ by store and by state.", INK),
          ("Always confirm", "Always confirm with the official source", (150, 100, 20)), ("before you rely", "before you rely on them.", (150, 100, 20)),
          ("general information", "General information,", (70, 100, 80)), ("not financial", "not financial advice.", (70, 100, 80)),
          ("not affiliated", "This channel is not affiliated with Aldi", INK), ("or any government", "or any government agency.", INK)]

def draw30(img, t):
    b = 30
    te = DUR[b] / FPS - 20.0
    ap(img, t, 0.3, txt("BEFORE", 120, IVORY, 6), 470, 400, pop_=False, dy=30, dur=0.6, t_out=te - 0.4)
    ap(img, t, 0.5, txt("YOU GO", 120, GOLD, 6), 470, 540, pop_=False, dy=30, dur=0.6, t_out=te - 0.4)
    ap(img, t, te, endbox(), 470, 470, pop_=False, dur=0.4)
    ap(img, t, te + 0.1, txt("WATCH NEXT", 54, GOLD, 3), 470, 780, pop_=False, dur=0.4)
    ap(img, t, 0.2, disc_panel(), 1380, 500, pop_=False, dy=40, dur=0.6, shadow=14)
    for i, (key, s_, col) in enumerate(DLINES):
        ap(img, t, T(b, key) if i else 0.6, tspr(s_, FONT_SANS_M, 34, col), 1380, 340 + i * 62, pop_=False, dy=14, dur=0.5)
    ap(img, t, LAST(b), txt("THANKS FOR WATCHING", 40, IVORY, 4), 960, 950)
