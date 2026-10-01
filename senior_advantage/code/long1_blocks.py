"""Video lungo 1 - blocchi 2-6. Durate dei blocchi dalla timeline CapCut (righello + riga bianca).
Uso: python3 long1_blocks.py <blocco> [clip ...]   es.  python3 long1_blocks.py 2   |   python3 long1_blocks.py 5 1 3"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long1_b01 import *  # engine 1920x1080, pop, T, spaced, person, register, stamp_x, tile_icon, cart, ...

BLOCK_FRAMES = {2: 554, 3: 576, 4: 465, 5: 752, 6: 631}


def show(img, t, st, fn, dur=.5, rise=40, scale0=.9, **kw):
    """fa comparire un oggetto: dissolvenza + piccola salita + zoom"""
    p = seg(t, st, dur)
    if p <= 0: return
    pop(img, fn, scale0 + (1 - scale0) * ease_back(p), a=ease(seg(t, st, dur * .6)), dy=rise * (1 - ease(p)) + kw.pop("dy", 0), **kw)


def txt_in(img, t, st, xy, s, size, fill, serif=False, dur=.45, sans_m=False):
    a = ease(seg(t, st, dur))
    if a <= 0: return
    lay = new_layer(); f = font(FONT_SERIF if serif else (FONT_SANS_M if sans_m else FONT_SANS), size)
    T(lay[0], lay[1], (xy[0], xy[1] + 24 * (1 - a)), s, f, fill); alpha_layer(img, lay, a)


def footer(img, t, st=.6, s="Varies by location · confirm with the business"):
    txt_in(img, t, st, (W // 2, 1042), s, 26, SAGE, sans_m=True)


def bubble(rgb, mask, cx, cy, w, h, tail="left"):
    dm, d = ImageDraw.Draw(mask), ImageDraw.Draw(rgb)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    tx = cx - w / 2 + 90 if tail == "left" else cx + w / 2 - 90
    pts = [(tx - 30, cy + h / 2 - 4), (tx + 40 * (-1 if tail == "left" else 1) * -1, cy + h / 2 + 60), (tx + 40, cy + h / 2 - 4)]
    for dr, c in ((dm, 255), (d, CARD)):
        dr.rounded_rectangle(box, radius=40, fill=c); dr.polygon(pts, fill=c)
    d.rounded_rectangle(box, radius=40, outline=GOLD, width=5)


# ============================== BLOCCO 2: il problema ==============================
def b2c1(img, t):
    spaced(img, "THE PROBLEM", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    def shop(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, CARD), (dm, 255)):
            dr.rounded_rectangle([300, 330, 980, 860], radius=22, fill=c)
        d.rounded_rectangle([300, 330, 980, 860], radius=22, outline=SAGE_D, width=5)
        for i in range(8):
            x0 = 300 + i * 85
            for dr, c in ((d, IVORY if i % 2 == 0 else RED), (dm, 255)):
                dr.polygon([(x0, 250), (x0 + 85, 250), (x0 + 85, 330), (x0, 330)], fill=c)
        d.rounded_rectangle([420, 500, 660, 860], radius=10, fill=(120, 80, 45)); d.ellipse([625, 680, 645, 700], fill=GOLD)
        d.rounded_rectangle([720, 450, 940, 650], radius=14, fill=GREEN_L, outline=SAGE, width=4)
        T(r, m, (830, 520), "SALE", font(FONT_SANS, 64), IVORY)
        T(r, m, (830, 590), "20% OFF", font(FONT_SANS_M, 40), GOLD)
    show(img, t, .3, shop, .7, rise=60)
    # il cartello "SENIOR DISCOUNT" non c'e': contorno tratteggiato che lampeggia
    a = ease(seg(t, 1.6, .5))
    if a > 0:
        lay = new_layer(); rgb, mask = lay; d = ImageDraw.Draw(rgb); dm = ImageDraw.Draw(mask)
        x0, y0, x1, y1 = 1140, 400, 1760, 700
        for x in range(x0, x1, 40):
            for dr, c in ((d, GOLD), (dm, 255)):
                dr.line([x, y0, x + 22, y0], fill=c, width=5); dr.line([x, y1, x + 22, y1], fill=c, width=5)
        for y in range(y0, y1, 40):
            for dr, c in ((d, GOLD), (dm, 255)):
                dr.line([x0, y, x0, y + 22], fill=c, width=5); dr.line([x1, y, x1, y + 22], fill=c, width=5)
        T(rgb, mask, ((x0 + x1) / 2, 520), "SENIOR DISCOUNT", font(FONT_SANS, 54), GOLD)
        T(rgb, mask, ((x0 + x1) / 2, 610), "?", font(FONT_SERIF, 110), IVORY)
        alpha_layer(img, lay, a * (0.35 + 0.25 * math.sin(t * 4)))
    txt_in(img, t, 2.4, (1450, 790), "NOWHERE ON THE SIGN", 50, IVORY)
    txt_in(img, t, 3.2, (W // 2, 960), "ALMOST NEVER ADVERTISED", 62, GOLD)


def b2c2(img, t):
    spaced(img, "IT ONLY EXISTS IF YOU ASK", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: person(r, m, 480, 600, 1.5), .6)
    show(img, t, 1.0, lambda r, m: bubble(r, m, 880, 360, 760, 190) or (T(r, m, (880, 335), "Do you offer a", font(FONT_SERIF, 54), IVORY), T(r, m, (880, 395), "senior discount?", font(FONT_SERIF, 54), GOLD)), .5)
    show(img, t, 2.2, lambda r, m: (person(r, m, 1500, 560, 1.3), register(r, m, 1430, 790)), .6)
    show(img, t, 3.6, lambda r, m: price_tag(r, m, 1230, 560, "55+", 280, 160), .5, angle=-8)
    show(img, t, 4.4, lambda r, m: T(r, m, (1500, 360), "YES!", font(FONT_SERIF, 120), GOLD), .5)
    txt_in(img, t, 5.4, (W // 2, 960), "SAY ONE SENTENCE AND IT APPEARS", 56, IVORY)


def b2c3(img, t):
    spaced(img, "EVERY SINGLE DAY", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    def receipt_big(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, (246, 241, 229)), (dm, 255)):
            dr.rounded_rectangle([1050, 220, 1560, 860], radius=24, fill=c)
        for i, (a_, b_) in enumerate((("Item", "$12.00"), ("Item", "$5.00"), ("Item", "$3.00"))):
            d.text((1100, 350 + i * 70), a_, font=font(FONT_SANS_M, 38), fill=GREEN_D, anchor="lm"); d.text((1510, 350 + i * 70), b_, font=font(FONT_SANS_M, 38), fill=GREEN_D, anchor="rm")
        d.line([1100, 560, 1510, 560], fill=(170, 160, 135), width=3)
        d.text((1100, 620), "TOTAL", font=font(FONT_SANS, 46), fill=GREEN_D, anchor="lm"); d.text((1510, 620), "$20.00", font=font(FONT_SANS, 46), fill=GREEN_D, anchor="rm")
        d.text((1305, 270), "RECEIPT", font=font(FONT_SANS, 40), fill=GREEN_D, anchor="mm")
    show(img, t, 2.0, receipt_big, .6, angle=3)
    # il cliente cammina verso destra con la borsa
    x = 250 + 650 * ease(seg(t, .4, 4.5))
    def walker(r, m):
        person(r, m, int(x), 600, 1.4)
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, GOLD), (dm, 255)):
            dr.rounded_rectangle([x + 70, 690, x + 190, 830], radius=10, fill=c)
        d.arc([x + 90, 650, x + 170, 730], 180, 360, fill=GOLD, width=8)
    pop(img, walker, 1.0, a=ease(seg(t, .3, .5)))
    show(img, t, 4.4, lambda r, m: (T(r, m, (1305, 500), "FULL PRICE", font(FONT_SANS, 74), RED)), .45, angle=-10)
    txt_in(img, t, 5.4, (W // 2, 960), "JUST BECAUSE THEY NEVER ASKED", 58, GOLD)


# ============================== BLOCCO 3: il piano ==============================
def tiles_row(img, t, kinds, labels, y, x0, gap, st, color=IVORY, lsz=34):
    for i, (k, lab) in enumerate(zip(kinds, labels)):
        x = x0 + i * gap
        show(img, t, st + i * .35, lambda r, m, k=k, x=x: tile_icon(k, r, m, x, y), .45)
        txt_in(img, t, st + .15 + i * .35, (x, y + 130), lab, lsz, color)


def b3c1(img, t):
    spaced(img, "HERE'S THE PLAN", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: T(r, m, (400, 330), "1", font(FONT_SERIF, 240), GOLD), .5)
    tiles_row(img, t, ["plate", "pharmacy"], ["RESTAURANTS", "DRUGSTORES"], 520, 900, 400, 1.0, lsz=44)
    # il piano: percorso con tappe
    a = ease(seg(t, 2.2, .6))
    if a > 0:
        d = ImageDraw.Draw(img)
        for x in range(260, 1660, 70): d.ellipse([x, 880, x + 14, 894], fill=SAGE_D)
        for i, x in enumerate((400, 1050, 1500)):
            d.ellipse([x - 24, 862, x + 24, 910], fill=GOLD if i == 0 else SAGE_D)
    txt_in(img, t, 2.6, (W // 2, 975), "FIRST STOPS ON THE LIST", 50, IVORY)


def b3c2(img, t):
    spaced(img, "THEN", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .2, (W // 2, 200), "STORES WITH A SPECIAL SENIOR DAY", 56, GOLD)
    tiles_row(img, t, ["shirt", "tag", "hanger", "craft"], ["", "", "", ""], 420, 560, 270, .6)
    txt_in(img, t, 3.2, (W // 2, 640), "YOUR PHONE BILL · THE MOVIES · THE TRAIN", 56, GOLD)
    tiles_row(img, t, ["phone", "ticket", "train"], ["", "", ""], 840, 690, 270, 3.7)


def b3c3(img, t):
    spaced(img, "STAY UNTIL THE END", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    txt_in(img, t, .2, (W // 2, 200), "THE LAST THREE SAVE THE MOST OVER TIME", 56, IVORY)
    tiles_row(img, t, ["bus", "park", "aarp"], ["#10", "#11", "#12"], 520, 560, 400, .8, lsz=60)
    # la stella sul numero 11
    def star(r, m):
        pts = []
        for i in range(10):
            ang = -math.pi / 2 + i * math.pi / 5; rr = 62 if i % 2 == 0 else 26
            pts.append((960 + rr * math.cos(ang), 360 + rr * math.sin(ang)))
        ImageDraw.Draw(m).polygon(pts, fill=255); ImageDraw.Draw(r).polygon(pts, fill=GOLD)
    show(img, t, 3.0, star, .6, angle=0)
    txt_in(img, t, 4.4, (W // 2, 880), "NUMBER ELEVEN: THE ONE I WOULD PICK FIRST", 56, GOLD)
    footer(img, t, 5.0, "Stay until the end")


# ============================== BLOCCO 4: la regola ==============================
def b4c1(img, t):
    spaced(img, "ONE RULE THAT WORKS EVERYWHERE", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    steps = [(480, "ASK", "?"), (960, "TOTAL RUNG UP", "$20"), (1440, "YOU PAY", "✓")]
    for i, (x, lab, sym) in enumerate(steps):
        st = .4 + i * .9
        on = i == 0
        col = GOLD if on else SAGE_D
        def disc(r, m, x=x, sym=sym, col=col, lab=lab):
            d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
            for dr, c in ((d, CARD), (dm, 255)): dr.ellipse([x - 150, 380, x + 150, 680], fill=c)
            d.ellipse([x - 150, 380, x + 150, 680], outline=col, width=9)
            T(r, m, (x, 530), sym, font(FONT_SERIF, 120), IVORY if col == GOLD else SAGE)
            T(r, m, (x, 760), lab, font(FONT_SANS, 46), col)
        show(img, t, st, disc, .5)
    for x in (720, 1200):
        a = ease(seg(t, 1.4 if x == 720 else 2.2, .4))
        if a > 0:
            d = ImageDraw.Draw(img); d.polygon([(x, 510), (x + 50, 530), (x, 550)], fill=SAGE_D)
    txt_in(img, t, 3.4, (W // 2, 930), "ASK BEFORE THE TOTAL IS RUNG UP", 66, GOLD)
    # freccia che evidenzia il passo 1
    a = ease(seg(t, 3.0, .5))
    if a > 0:
        d = ImageDraw.Draw(img); d.rounded_rectangle([320, 350, 640, 710], radius=40, outline=GOLD, width=6)


def b4c2(img, t):
    spaced(img, "SAY THIS", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: person(r, m, 420, 620, 1.6), .6)
    def big_bubble(r, m):
        bubble(r, m, 1130, 470, 1100, 420)
        T(r, m, (1130, 400), "Do you offer a", font(FONT_SERIF, 92), IVORY)
        T(r, m, (1130, 500), "senior discount,", font(FONT_SERIF, 92), GOLD)
        T(r, m, (1130, 600), "and at what age does it start?", font(FONT_SANS, 54), IVORY)
    show(img, t, 1.0, big_bubble, .6)


def b4c3(img, t):
    spaced(img, "THAT'S ALL YOU NEED", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: T(r, m, (W // 2, 480), "ONE QUESTION", font(FONT_SANS, 170), IVORY), .6)
    show(img, t, 1.3, lambda r, m: price_tag(r, m, W // 2, 700, "55+", 340, 190), .5, angle=-6)
    a = ease(seg(t, 2.6, .5))
    if a > 0:
        d = ImageDraw.Draw(img); x = 1500 + 30 * math.sin(t * 5)
        d.polygon([(x, 700), (x - 60, 650), (x - 60, 750)], fill=GOLD)
    txt_in(img, t, 2.8, (W // 2, 930), "NOW, THE FIRST PLACE", 62, GOLD)


# ============================== BLOCCO 5: cosa portare ==============================
def b5c1(img, t):
    spaced(img, "WHAT TO BRING  ·  1", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    def idcard(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        box = [560, 280, 1360, 760]
        dm.rounded_rectangle(box, radius=36, fill=255); d.rounded_rectangle(box, radius=36, fill=(246, 241, 229))
        d.rectangle([560, 280, 1360, 360], fill=GREEN_L)
        T(r, m, (960, 320), "PHOTO ID", font(FONT_SANS, 44), IVORY)
        d.rounded_rectangle([610, 400, 800, 620], radius=14, fill=SAGE); d.ellipse([665, 420, 745, 500], fill=SAGE_D); d.pieslice([630, 500, 780, 660], 180, 360, fill=SAGE_D)
        for i in range(4): d.rounded_rectangle([850, 410 + i * 56, 1300 - (i % 2) * 120, 436 + i * 56], radius=8, fill=(190, 184, 160))
        d.rounded_rectangle([850, 640, 1310, 700], radius=10, fill=GOLD); T(r, m, (1080, 670), "DATE OF BIRTH", font(FONT_SANS, 32), GREEN_D)
    show(img, t, .4, idcard, .7, angle=-3)
    txt_in(img, t, 2.2, (W // 2, 880), "SOME PLACES WILL ASK FOR IT", 60, IVORY)


def b5c2(img, t):
    spaced(img, "WHAT TO BRING  ·  2", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    def phone(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, (230, 230, 225)), (dm, 255)): dr.rounded_rectangle([520, 250, 820, 840], radius=44, fill=c)
        d.rounded_rectangle([540, 290, 800, 800], radius=26, fill=GREEN_D)
        d.rounded_rectangle([560, 330, 780, 420], radius=14, fill=GOLD); T(r, m, (670, 375), "REWARDS", font(FONT_SANS, 30), GREEN_D)
        for i in range(3): d.rounded_rectangle([560, 450 + i * 90, 780, 520 + i * 90], radius=12, fill=GREEN_L)
        d.ellipse([650, 760, 690, 790], outline=SAGE, width=3)
    show(img, t, .4, phone, .6, angle=-4)
    def card(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        box = [980, 380, 1600, 700]
        dm.rounded_rectangle(box, radius=32, fill=255); d.rounded_rectangle(box, radius=32, fill=GOLD)
        T(r, m, (1290, 470), "REWARDS CARD", font(FONT_SANS, 46), GREEN_D)
        T(r, m, (1290, 570), "FREE ACCOUNT", font(FONT_SANS_M, 52), GREEN_D)
        d.rounded_rectangle([1040, 630, 1540, 660], radius=8, fill=GREEN_D)
    show(img, t, 1.4, card, .6, angle=5)
    txt_in(img, t, 3.6, (1290, 800), "A FEW DISCOUNTS NEED ONE", 52, IVORY)
    txt_in(img, t, 4.6, (1290, 880), "LIKE WALGREENS", 46, GOLD)


def b5c3(img, t):
    spaced(img, "WHAT TO BRING  ·  3", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    cx, cy, r = 600, 520, 260
    def dial(rr, mm):
        d, dm = ImageDraw.Draw(rr), ImageDraw.Draw(mm)
        for dr, c in ((d, CARD), (dm, 255)): dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=SAGE_D, width=8)
        d.rounded_rectangle([cx - 30, cy - r - 50, cx + 30, cy - r], radius=8, fill=SAGE_D)
        for i in range(12):
            a_ = i * math.pi / 6; d.line([cx + (r - 40) * math.sin(a_), cy - (r - 40) * math.cos(a_), cx + (r - 14) * math.sin(a_), cy - (r - 14) * math.cos(a_)], fill=SAGE, width=6)
    show(img, t, .3, dial, .6)
    sweep = min(1, max(0, (t - 1.0) / 4.0)) * 5
    d = ImageDraw.Draw(img)
    d.arc([cx - r + 30, cy - r + 30, cx + r - 30, cy + r - 30], -90, -90 + 360 * (sweep / 5), fill=GOLD, width=26)
    shadow_text(img, (cx, cy - 10), f"{int(math.ceil(sweep)) if sweep > 0 else 0}", font(FONT_SERIF, 200), IVORY)
    d.text((cx, cy + 140), "SECONDS", font=font(FONT_SANS, 48), fill=SAGE, anchor="mm")
    show(img, t, 1.2, lambda r_, m_: (person(r_, m_, 1360, 560, 1.4), register(r_, m_, 1400, 780)), .6)
    txt_in(img, t, 3.0, (1380, 330), "“Hmm... one moment”", 50, IVORY, serif=True)
    txt_in(img, t, 5.0, (W // 2, 960), "ABOUT FIVE SECONDS OF PATIENCE", 60, GOLD)


def b5c4(img, t):
    spaced(img, "WHAT TO BRING  ·  4", W // 2, 100, 44, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: person(r, m, 560, 600, 1.7, tie=True, badge="MANAGER"), .6)
    def b(r, m):
        bubble(r, m, 1230, 450, 920, 330, tail="left")
        T(r, m, (1230, 400), "Could you check", font(FONT_SERIF, 74), IVORY)
        T(r, m, (1230, 490), "with a manager?", font(FONT_SERIF, 74), GOLD)
    show(img, t, 1.0, b, .6)
    txt_in(img, t, 2.6, (W // 2, 930), "POLITELY ASK THEM TO CHECK", 60, IVORY)


# ============================== BLOCCO 6: ristoranti ==============================
def menu_card(r, m, cx, cy, name, tint):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - 270, cy - 330, cx + 270, cy + 330]
    dm.rounded_rectangle(box, radius=30, fill=255); d.rounded_rectangle(box, radius=30, fill=(246, 241, 229))
    d.rounded_rectangle([cx - 270, cy - 330, cx + 270, cy - 220], radius=30, fill=tint); d.rectangle([cx - 270, cy - 260, cx + 270, cy - 220], fill=tint)
    T(r, m, (cx, cy - 275), name, font(FONT_SANS, 50), IVORY)
    d.rounded_rectangle([cx - 110, cy - 190, cx + 110, cy - 130], radius=28, fill=GOLD); T(r, m, (cx, cy - 160), "55+ MENU", font(FONT_SANS, 32), GREEN_D)
    for i in range(4):
        d.rounded_rectangle([cx - 220, cy - 70 + i * 82, cx + 20, cy - 40 + i * 82], radius=8, fill=(190, 184, 160))
        d.rounded_rectangle([cx + 70, cy - 70 + i * 82, cx + 220, cy - 40 + i * 82], radius=8, fill=tint)


def b6c1(img, t):
    spaced(img, "PLACE #1  ·  RESTAURANTS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: menu_card(r, m, 560, 590, "DENNY'S", (160, 50, 44)), .6, angle=-3)
    show(img, t, 1.4, lambda r, m: menu_card(r, m, 1360, 590, "IHOP", (36, 82, 140)), .6, angle=3)
    def low(r, m):
        ImageDraw.Draw(m).rounded_rectangle([700, 150, 1220, 250], radius=34, fill=255)
        ImageDraw.Draw(r).rounded_rectangle([700, 150, 1220, 250], radius=34, fill=GOLD)
        T(r, m, (960, 200), "LOWER PRICES", font(FONT_SANS, 52), GREEN_D)
    show(img, t, 2.6, low, .5, angle=-3)
    txt_in(img, t, 3.2, (W // 2, 960), "A MENU MADE FOR GUESTS 55 AND OLDER", 54, IVORY)
    footer(img, t)


def b6c2(img, t):
    spaced(img, "PLACE #1  ·  RESTAURANTS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    def aarp(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        box = [330, 330, 930, 650]
        dm.rounded_rectangle(box, radius=32, fill=255); d.rounded_rectangle(box, radius=32, fill=RED)
        T(r, m, (630, 440), "AARP", font(FONT_SANS, 110), IVORY); T(r, m, (630, 560), "MEMBER", font(FONT_SANS_M, 52), IVORY)
    show(img, t, .4, aarp, .6, angle=-4)
    cx, cy, rr = 1400, 480, 240
    d = ImageDraw.Draw(img)
    a = ease(seg(t, 1.4, .5))
    if a > 0:
        lay = new_layer(); L, M = lay; dd, dm = ImageDraw.Draw(L), ImageDraw.Draw(M)
        for dr, c in ((dd, CARD), (dm, 255)): dr.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c)
        dd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=SAGE_D, width=6)
        alpha_layer(img, lay, a)
        d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, 270, fill=(30, 80, 64), width=28)
        d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, -90 + 360 * .15 * ease(seg(t, 1.8, 1.2)), fill=GOLD, width=28)
    show(img, t, 1.6, lambda r, m: T(r, m, (cx, cy - 10), "15%", font(FONT_SERIF, 170), IVORY), .5)
    txt_in(img, t, 2.4, (cx, cy + 120), "OFF THE CHECK", 40, SAGE)
    show(img, t, 3.2, lambda r, m: price_tag(r, m, 630, 800, "UP TO $10", 440, 150), .5, angle=-6)
    txt_in(img, t, 4.0, (W // 2, 960), "AT PARTICIPATING LOCATIONS", 54, IVORY)
    footer(img, t)


def b6c3(img, t):
    spaced(img, "PLACE #1  ·  RESTAURANTS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: person(r, m, 520, 640, 1.7), .6)
    def b(r, m):
        bubble(r, m, 1230, 470, 960, 330, tail="left")
        T(r, m, (1230, 420), "Which one", font(FONT_SERIF, 90), IVORY); T(r, m, (1230, 520), "fits me?", font(FONT_SERIF, 90), GOLD)
    show(img, t, .8, b, .6)
    txt_in(img, t, 1.8, (W // 2, 930), "ASK YOUR SERVER", 70, GOLD)
    footer(img, t, .8)


BLOCKS = {
    2: [("Here's the problem. Senior discounts are almost never advertised.", b2c1),
        ("A store doesn't hand out savings on its own, so the discount only exists if you ask for it.", b2c2),
        ("And people walk out every single day paying full price, just because they never said one sentence.", b2c3)],
    3: [("So here's the plan. First, restaurants and drugstores.", b3c1),
        ("Then stores with a special senior day. Then your phone bill, the movies and the train.", b3c2),
        ("And the last three can save you the most over time, so stay until the end, because number eleven is the one I would pick first.", b3c3)],
    4: [("Before we start, one rule that works everywhere. Ask before the total is rung up.", b4c1),
        ("Say this: do you offer a senior discount, and at what age does it start?", b4c2),
        ("That one question is all you need. Now, the first place.", b4c3)],
    5: [("Here's what to bring. First, a photo ID, because some places will ask for it.", b5c1),
        ("Second, the free app or rewards account of the stores you use, because a few of these discounts, like Walgreens, need one.", b5c2),
        ("And third, about five seconds of patience, because the cashier may need to press a button they've never pressed.", b5c3),
        ("If they don't know, politely ask them to check with a manager.", b5c4)],
    6: [("Number one: restaurants. Denny's has a menu made for guests fifty-five and older, and IHOP has one too, with lower prices on classic dishes.", b6c1),
        ("Denny's also gives AARP members fifteen percent off the check at participating locations, up to ten dollars.", b6c2),
        ("Ask your server which one fits you.", b6c3)],
}


def split_frames(block):
    total = BLOCK_FRAMES[block]; w = [len(s) for s, _ in BLOCKS[block]]
    fr = [round(total * x / sum(w)) for x in w]; fr[-1] = total - sum(fr[:-1])
    return fr


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = split_frames(b)
    for i, ((s, fn), n) in enumerate(zip(BLOCKS[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco0{b}-slide0{i}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
