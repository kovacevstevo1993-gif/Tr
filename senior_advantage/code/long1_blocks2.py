"""Video lungo 1 - blocchi 7-11. Durate dalla timeline CapCut (righello + riga bianca).
Uso: python3 long1_blocks2.py <blocco> [clip ...]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long1_blocks import *  # show, txt_in, footer, bubble, tiles_row, menu_card ... + tutto l'engine

BLOCK_FRAMES2 = {7: 576, 8: 632, 9: 598, 10: 304, 11: 347}


def month_strip(img, t, st, y, hl=12, lab_size=26, x0=210, w=125, h=90, amt=None):
    """12 caselle (mesi) che si accendono una dopo l'altra"""
    names = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    d = ImageDraw.Draw(img)
    for i in range(12):
        on = ease(seg(t, st + i * .25, .25))
        x = x0 + i * (w + 8)
        col = tuple(int(CARD[k] + (GOLD[k] - CARD[k]) * on) for k in range(3))
        d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=col, outline=SAGE_D, width=3)
        d.text((x + w / 2, y + 26), names[i], font=font(FONT_SANS_M, lab_size), fill=GREEN_D if on > .5 else SAGE, anchor="mm")
        if amt:
            d.text((x + w / 2, y + 62), amt, font=font(FONT_SANS, 30), fill=GREEN_D if on > .5 else (60, 110, 90), anchor="mm")


def check_receipt(rgb, mask, x0, y0, x1, y1, title, rows, hl=None, total=None):
    d, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    dm.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=255); d.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=(246, 241, 229))
    d.text(((x0 + x1) / 2, y0 + 55), title, font=font(FONT_SANS, 38), fill=GREEN_D, anchor="mm")
    d.line([x0 + 40, y0 + 95, x1 - 40, y0 + 95], fill=(170, 160, 135), width=3)
    y = y0 + 145
    for a, b in rows:
        d.text((x0 + 50, y), a, font=font(FONT_SANS_M, 36), fill=GREEN_D, anchor="lm"); d.text((x1 - 50, y), b, font=font(FONT_SANS_M, 36), fill=GREEN_D, anchor="rm"); y += 62
    if hl:
        d.rounded_rectangle([x0 + 30, y - 10, x1 - 30, y + 62], radius=16, fill=GOLD)
        d.text((x0 + 48, y + 26), hl[0], font=font(FONT_SANS, 34), fill=GREEN_D, anchor="lm"); d.text((x1 - 48, y + 26), hl[1], font=font(FONT_SANS, 34), fill=GREEN_D, anchor="rm"); y += 90
    if total:
        d.text((x0 + 50, y + 20), "TOTAL", font=font(FONT_SANS, 42), fill=GREEN_D, anchor="lm"); d.text((x1 - 50, y + 20), total, font=font(FONT_SANS, 42), fill=GREEN_D, anchor="rm")


def aarp_card(r, m, cx, cy, w=520, h=290):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    dm.rounded_rectangle(box, radius=32, fill=255); d.rounded_rectangle(box, radius=32, fill=RED)
    T(r, m, (cx, cy - 40), "AARP", font(FONT_SANS, 100), IVORY); T(r, m, (cx, cy + 70), "MEMBER", font(FONT_SANS_M, 48), IVORY)


# ============================== BLOCCO 7: perche' conta ==============================
def b7c1(img, t):
    spaced(img, "HERE'S WHY IT MATTERS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: aarp_card(r, m, 520, 380), .6, angle=-4)
    show(img, t, 1.1, lambda r, m: check_receipt(r, m, 1000, 200, 1500, 600, "DENNY'S", [("Meal", "$30.00")], total="$30.00"), .6, angle=3)
    txt_in(img, t, 2.0, (520, 590), "AARP MEMBER", 46, IVORY)
    txt_in(img, t, 2.4, (W // 2, 740), "ONCE A MONTH", 62, GOLD)
    month_strip(img, t, 3.0, 800)


def b7c2(img, t):
    spaced(img, "THE MATH", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: check_receipt(r, m, 220, 180, 760, 700, "DENNY'S", [("Meal", "$30.00")], hl=("15% AARP", "−$4.50"), total="$25.50"), .6, angle=-3)
    n = min(12, int((t - 3.2) / .3) + 1) if t > 3.2 else 0
    show(img, t, 3.0, lambda r, m: T(r, m, (1330, 330), "$4.50 × 12", font(FONT_SANS, 68), IVORY), .5)
    val = 4.5 * n
    shadow_text(img, (1330, 560), f"${val:.0f}" if n > 0 else "$0", font(FONT_SERIF, 250), GOLD)
    txt_in(img, t, 5.5, (1330, 770), "A YEAR", 70, IVORY)
    txt_in(img, t, 6.4, (1330, 880), "FOR SCANNING A CARD", 46, SAGE)


def b7c3(img, t):
    spaced(img, "SAY IT BEFORE THE CHECK", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: person(r, m, 400, 640, 1.5, tie=True, badge="SERVER"), .6)
    def b(r, m):
        bubble(r, m, 1050, 330, 760, 190, tail="left"); T(r, m, (1050, 330), "I'm an AARP member.", font(FONT_SERIF, 60), IVORY)
    show(img, t, .9, b, .5)
    steps = [(880, "SAY IT", GOLD, "1"), (1200, "SERVER RUNS THE CHECK", SAGE_D, "2")]
    for i, (x, lab, col, num) in enumerate(steps):
        def disc(r, m, x=x, col=col, num=num, lab=lab):
            d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
            for dr, c in ((d, CARD), (dm, 255)): dr.ellipse([x - 90, 610, x + 90, 790], fill=c)
            d.ellipse([x - 90, 610, x + 90, 790], outline=col, width=8); T(r, m, (x, 700), num, font(FONT_SERIF, 100), IVORY if col == GOLD else SAGE)
            T(r, m, (x, 850), lab, font(FONT_SANS, 32), col)
        show(img, t, 2.0 + i * 1.0, disc, .5)
    a = ease(seg(t, 3.2, .4))
    if a > 0:
        d = ImageDraw.Draw(img); d.polygon([(1010, 700), (1060, 680), (1060, 720)], fill=SAGE_D)
    txt_in(img, t, 4.2, (1540, 700), "NOT AFTER", 60, RED)


# ============================== BLOCCO 8: Walgreens ==============================
def calendar(r, m, x0, y0, cw, ch, hl=(1, 1), rows=5, month_days=31, start=3, title="OCTOBER"):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    w, h = cw * 7, ch * (rows + 1) + 70
    dm.rounded_rectangle([x0 - 20, y0 - 80, x0 + w + 20, y0 + h - 40], radius=30, fill=255)
    d.rounded_rectangle([x0 - 20, y0 - 80, x0 + w + 20, y0 + h - 40], radius=30, fill=(246, 241, 229))
    d.text((x0 + w / 2, y0 - 38), title, font=font(FONT_SANS, 40), fill=GREEN_D, anchor="mm")
    for i, dn in enumerate(["M", "T", "W", "T", "F", "S", "S"]):
        d.text((x0 + i * cw + cw / 2, y0 + 20), dn, font=font(FONT_SANS, 30), fill=(120, 110, 90), anchor="mm")
    day = 1
    for k in range(rows * 7):
        c, rw = k % 7, k // 7
        if k < start: continue
        if day > month_days: break
        cx, cy = x0 + c * cw + cw / 2, y0 + 70 + rw * ch + ch / 2
        if (c, rw) == hl:
            d.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], fill=GOLD)
        d.text((cx, cy), str(day), font=font(FONT_SANS, 30), fill=GREEN_D, anchor="mm"); day += 1


def b8c1(img, t):
    spaced(img, "NUMBER TWO  ·  WALGREENS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    # il primo martedi' del mese: ottobre 2026 inizia di giovedi' -> primo martedi' = 6 (riga 1, colonna 1)
    show(img, t, .3, lambda r, m: calendar(r, m, 220, 280, 100, 88, hl=(1, 1), start=3), .6, angle=-2)
    txt_in(img, t, 1.6, (570, 140 + 20), "FIRST TUESDAY OF EVERY MONTH", 40, GOLD)
    cx, cy, rr = 1380, 470, 230
    d = ImageDraw.Draw(img)
    a = ease(seg(t, 2.4, .5))
    if a > 0:
        lay = new_layer(); L, M = lay; dd, dm = ImageDraw.Draw(L), ImageDraw.Draw(M)
        for dr, c in ((dd, CARD), (dm, 255)): dr.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c)
        dd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=SAGE_D, width=6); alpha_layer(img, lay, a)
        d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, 270, fill=(30, 80, 64), width=28)
        d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, -90 + 360 * .20 * ease(seg(t, 2.8, 1.2)), fill=GOLD, width=28)
    show(img, t, 2.6, lambda r, m: T(r, m, (cx, cy - 10), "20%", font(FONT_SERIF, 160), IVORY), .5)
    txt_in(img, t, 3.2, (cx, cy + 110), "OFF REGULAR PRICE", 34, SAGE)
    show(img, t, 4.2, lambda r, m: price_tag(r, m, 1000, 800, "55+", 300, 170), .5, angle=-7)
    show(img, t, 5.0, lambda r, m: tile_icon("pharmacy", r, m, 1520, 820), .5)
    txt_in(img, t, 6.0, (W // 2, 1000), "IN THE STORE", 46, IVORY)
    footer(img, t)


def b8c2(img, t):
    spaced(img, "NUMBER TWO  ·  WALGREENS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    def phone(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, (230, 230, 225)), (dm, 255)): dr.rounded_rectangle([380, 220, 700, 860], radius=46, fill=c)
        d.rounded_rectangle([402, 262, 678, 820], radius=26, fill=GREEN_D)
        d.rounded_rectangle([422, 310, 658, 420], radius=16, fill=GOLD); T(r, m, (540, 365), "myWalgreens", font(FONT_SANS, 30), GREEN_D)
        T(r, m, (540, 500), "FREE", font(FONT_SANS, 70), IVORY); T(r, m, (540, 580), "ACCOUNT", font(FONT_SANS_M, 40), SAGE)
        d.rounded_rectangle([450, 660, 630, 730], radius=30, fill=GREEN_L); T(r, m, (540, 695), "JOIN", font(FONT_SANS, 34), IVORY)
    show(img, t, .4, phone, .6, angle=-3)
    txt_in(img, t, 1.4, (540, 930), "YOU NEED ONE", 52, GOLD)
    def pills(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, (214, 150, 60)), (dm, 255)): dr.rounded_rectangle([1130, 380, 1330, 760], radius=30, fill=c)
        d.rounded_rectangle([1110, 330, 1350, 410], radius=20, fill=IVORY)
        d.rounded_rectangle([1150, 500, 1310, 650], radius=14, fill=(246, 241, 229)); d.rectangle([1218, 520, 1242, 630], fill=RED); d.rectangle([1170, 563, 1290, 587], fill=RED)
    show(img, t, 2.8, pills, .6, angle=4)
    show(img, t, 3.8, lambda r, m: stamp_x(img, 1480, 360, 1.0) if False else None, .1)
    stamp_x(img, 1390, 340, seg(t, 3.8, .5))
    txt_in(img, t, 4.4, (1230, 860), "PRESCRIPTIONS", 52, IVORY); txt_in(img, t, 4.8, (1230, 930), "NOT INCLUDED", 52, RED)


def b8c3(img, t):
    spaced(img, "SHOPPING ONLINE?", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    def laptop(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        for dr, c in ((d, (200, 200, 195)), (dm, 255)):
            dr.rounded_rectangle([330, 230, 1590, 800], radius=30, fill=c); dr.rounded_rectangle([200, 800, 1720, 850], radius=24, fill=c)
        d.rounded_rectangle([370, 270, 1550, 760], radius=16, fill=GREEN_D)
        T(r, m, (960, 340), "CHECKOUT", font(FONT_SANS, 44), SAGE)
        d.rounded_rectangle([560, 420, 1360, 540], radius=16, fill=(246, 241, 229))
    show(img, t, .3, laptop, .6)
    code = "SENIOR20"
    n = max(0, min(len(code), int((t - 1.4) / .35)))
    d = ImageDraw.Draw(img)
    d.text((960, 480), code[:n] + ("|" if int(t * 3) % 2 == 0 and n < len(code) else ""), font=font(FONT_SANS, 64), fill=GREEN_D, anchor="mm")
    txt_in(img, t, .8, (960, 398), "PROMO CODE", 26, (120, 110, 90))
    if n == len(code):
        show(img, t, 1.4 + len(code) * .35 + .2, lambda r, m: price_tag(r, m, 960, 640, "20% OFF", 440, 150), .5, angle=-3)
    txt_in(img, t, 5.0, (W // 2, 935), "CODE FOR THAT WEEK:  S-E-N-I-O-R  2  0", 54, GOLD)
    footer(img, t, 5.4)


# ============================== BLOCCO 9: i conti ==============================
def chip(r, m, cx, cy, s, size=110, w=420, h=210, fill=CARD, fg=IVORY, outline=GOLD):
    d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    dm.rounded_rectangle(box, radius=36, fill=255); d.rounded_rectangle(box, radius=36, fill=fill, outline=outline, width=6)
    T(r, m, (cx, cy), s, font(FONT_SERIF, size), fg)


def b9c1(img, t):
    spaced(img, "DO THE MATH", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: chip(r, m, 420, 480, "$50", 130), .5)
    show(img, t, 1.4, lambda r, m: T(r, m, (760, 480), "×", font(FONT_SANS, 120), SAGE), .4)
    show(img, t, 1.9, lambda r, m: chip(r, m, 1060, 480, "20%", 130), .5)
    show(img, t, 3.0, lambda r, m: T(r, m, (1360, 480), "=", font(FONT_SANS, 120), SAGE), .4)
    show(img, t, 3.6, lambda r, m: chip(r, m, 1620, 480, "$10", 130, fill=GOLD, fg=GREEN_D, outline=IVORY), .5)
    txt_in(img, t, 1.0, (420, 650), "FIRST TUESDAY", 42, SAGE); txt_in(img, t, 2.3, (1060, 650), "TWENTY PERCENT", 42, SAGE); txt_in(img, t, 4.0, (1620, 650), "BACK", 42, GOLD)
    txt_in(img, t, 4.6, (W // 2, 900), "TEN DOLLARS BACK", 70, GOLD)


def b9c2(img, t):
    spaced(img, "TWELVE FIRST TUESDAYS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    month_strip(img, t, .6, 250, amt="$10", w=125, h=100)
    n = min(12, int((t - .6) / .25) + 1) if t > .6 else 0
    shadow_text(img, (W // 2, 620), f"${10 * n}", font(FONT_SERIF, 260), GOLD)
    txt_in(img, t, 4.4, (W // 2, 830), "A YEAR", 80, IVORY)
    txt_in(img, t, 5.4, (W // 2, 940), "ONE HUNDRED AND TWENTY DOLLARS", 52, SAGE)


def b9c3(img, t):
    spaced(img, "ADD THE DENNY'S HABIT", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .4, lambda r, m: chip(r, m, 380, 420, "$120", 110, w=420, h=200), .5)
    show(img, t, 1.1, lambda r, m: T(r, m, (700, 420), "+", font(FONT_SANS, 120), SAGE), .4)
    show(img, t, 1.7, lambda r, m: chip(r, m, 1000, 420, "$54", 110, w=420, h=200), .5)
    show(img, t, 3.0, lambda r, m: T(r, m, (1290, 420), "=", font(FONT_SANS, 120), SAGE), .4)
    show(img, t, 3.6, lambda r, m: chip(r, m, 1620, 420, "$174", 110, w=420, h=200, fill=GOLD, fg=GREEN_D, outline=IVORY), .5)
    txt_in(img, t, 0.9, (380, 560), "WALGREENS", 40, SAGE); txt_in(img, t, 1.9, (1000, 560), "DENNY'S", 40, SAGE); txt_in(img, t, 3.9, (1620, 560), "A YEAR", 44, GOLD)
    txt_in(img, t, 5.0, (W // 2, 820), "AND WE'RE ONLY AT NUMBER TWO", 64, IVORY)
    show(img, t, 6.0, lambda r, m: T(r, m, (W // 2, 930), "10 MORE TO GO", font(FONT_SANS, 56), GOLD), .5)


# ============================== BLOCCO 10: i giorni ==============================
def b10c1(img, t):
    spaced(img, "THE NEXT THREE PLACES", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    d = ImageDraw.Draw(img)
    for i, dn in enumerate(days):
        x = 190 + i * 235
        hl = {1: ("ROSS", 1.2), 2: ("KOHL'S", 2.0)}.get(i)
        on = ease(seg(t, hl[1], .4)) if hl else 0
        col = tuple(int(CARD[k] + (GOLD[k] - CARD[k]) * on) for k in range(3))
        d.rounded_rectangle([x, 330, x + 205, 640], radius=30, fill=col, outline=SAGE_D, width=4)
        d.text((x + 102, 380), dn, font=font(FONT_SANS, 44), fill=GREEN_D if on > .5 else IVORY, anchor="mm")
        if hl and on > 0:
            d.text((x + 102, 520), hl[0], font=font(FONT_SANS, 36), fill=GREEN_D, anchor="mm")
        if i == 1 and on > 0:
            d.text((x + 102, 580), "+ SAVERS", font=font(FONT_SANS_M, 28), fill=GREEN_D, anchor="mm")
    a = ease(seg(t, 3.4, .6))
    if a > 0:
        lay = new_layer(); rgb, mask = lay; dd, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
        for dr, c in ((dd, SAGE), (dm, 255)): dr.rounded_rectangle([190, 700, 190 + 7 * 235 - 30, 790], radius=40, fill=c)
        T(rgb, mask, (960, 745), "MICHAELS: EVERY DAY", font(FONT_SANS, 50), GREEN_D)
        alpha_layer(img, lay, a)
    txt_in(img, t, 2.8, (W // 2, 230), "ONE SPECIFIC DAY OF THE WEEK", 56, IVORY)
    txt_in(img, t, 4.4, (W // 2, 900), "AND A FOURTH WORKS EVERY DAY", 58, GOLD)


def b10c2(img, t):
    spaced(img, "ALMOST NOBODY KNOWS IT", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    for i in range(7):
        x = 230 + i * 245
        show(img, t, .3 + i * .25, lambda r, m, x=x, i=i: (person(r, m, x, 560, .95), T(r, m, (x + 70, 360), "?", font(FONT_SERIF, 90), GOLD if i % 2 == 0 else IVORY)), .5)
    show(img, t, 2.6, lambda r, m: price_tag(r, m, W // 2, 800, "SENIOR DAY", 560, 170), .5, angle=-4)
    txt_in(img, t, 3.4, (W // 2, 960), "THEY NEVER ASK", 58, IVORY)


# ============================== BLOCCO 11: Ross ==============================
def b11c1(img, t):
    spaced(img, "NUMBER THREE  ·  ROSS DRESS FOR LESS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    tiles_row(img, t, ["shirt", "hanger"], ["", ""], 430, 400, 260, .4)
    def day(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        box = [260, 590, 700, 800]
        dm.rounded_rectangle(box, radius=28, fill=255); d.rounded_rectangle(box, radius=28, fill=GOLD)
        T(r, m, (480, 650), "EVERY", font(FONT_SANS_M, 36), GREEN_D); T(r, m, (480, 730), "TUESDAY", font(FONT_SANS, 70), GREEN_D)
    show(img, t, 1.6, day, .5, angle=-3)
    cx, cy, rr = 1300, 470, 240
    d = ImageDraw.Draw(img)
    a = ease(seg(t, 2.4, .5))
    if a > 0:
        lay = new_layer(); L, M = lay; dd, dm = ImageDraw.Draw(L), ImageDraw.Draw(M)
        for dr, c in ((dd, CARD), (dm, 255)): dr.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c)
        dd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=SAGE_D, width=6); alpha_layer(img, lay, a)
        d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, 270, fill=(30, 80, 64), width=28)
        d.arc([cx - rr + 26, cy - rr + 26, cx + rr - 26, cy + rr - 26], -90, -90 + 360 * .10 * ease(seg(t, 2.8, 1.0)), fill=GOLD, width=28)
    show(img, t, 2.6, lambda r, m: T(r, m, (cx, cy - 10), "10%", font(FONT_SERIF, 170), IVORY), .5)
    txt_in(img, t, 3.2, (cx, cy + 115), "OFF", 46, SAGE)
    show(img, t, 4.2, lambda r, m: price_tag(r, m, 1300, 820, "55+", 320, 170), .5, angle=-6)
    footer(img, t)


def b11c2(img, t):
    spaced(img, "NUMBER THREE  ·  ROSS DRESS FOR LESS", W // 2, 90, 42, a=ease(seg(t, 0, .5)))
    show(img, t, .3, lambda r, m: (person(r, m, 1450, 520, 1.4), register(r, m, 1390, 760)), .6)
    show(img, t, .9, lambda r, m: person(r, m, 400, 620, 1.5), .6)
    def b(r, m):
        bubble(r, m, 880, 320, 720, 190, tail="left"); T(r, m, (880, 320), "It's Tuesday. I'm 55+.", font(FONT_SERIF, 56), IVORY)
    show(img, t, 1.6, b, .5)
    def idc(r, m):
        d, dm = ImageDraw.Draw(r), ImageDraw.Draw(m)
        box = [760, 600, 1160, 840]
        dm.rounded_rectangle(box, radius=26, fill=255); d.rounded_rectangle(box, radius=26, fill=(246, 241, 229))
        d.rectangle([760, 600, 1160, 650], fill=GREEN_L); T(r, m, (960, 626), "ID", font(FONT_SANS, 32), IVORY)
        d.rounded_rectangle([790, 670, 900, 800], radius=10, fill=SAGE)
        for i in range(3): d.rounded_rectangle([925, 680 + i * 40, 1130, 700 + i * 40], radius=6, fill=(190, 184, 160))
    show(img, t, 3.0, idc, .5, angle=-4)
    txt_in(img, t, 3.8, (W // 2, 960), "TELL THE CASHIER  ·  BE READY TO SHOW AN ID", 50, GOLD)
    footer(img, t, 4.2)


BLOCKS2 = {
    7: [("Here's why it matters. Say you're an AARP member and you eat at Denny's once a month, and the check is thirty dollars.", b7c1),
        ("Fifteen percent is four dollars and fifty cents. That's fifty-four dollars a year, for scanning a card.", b7c2),
        ("And you say it before the server runs the check, not after.", b7c3)],
    8: [("Number two: Walgreens. On the first Tuesday of every month, customers fifty-five and older get twenty percent off regular-priced items in the store.", b8c1),
        ("You need a free myWalgreens account, and prescriptions are not included.", b8c2),
        ("Shopping online? There's a code for that week: S-E-N-I-O-R, two, zero.", b8c3)],
    9: [("Do the math on this one. Say you spend fifty dollars on the first Tuesday. Twenty percent is ten dollars back.", b9c1),
        ("Twelve first Tuesdays in a year, that's one hundred and twenty dollars.", b9c2),
        ("Add the Denny's habit, and you're already at one hundred and seventy-four dollars a year, and we're only at number two.", b9c3)],
    10: [("Now, the next three places drop the price on one specific day of the week, and a fourth works every day.", b10c1),
         ("And almost nobody who shops there knows it.", b10c2)],
    11: [("Number three: Ross Dress for Less. Ten percent off every Tuesday for shoppers fifty-five and older.", b11c1),
         ("Tell the cashier when you check out, and be ready to show an ID.", b11c2)],
}


def split_frames2(block):
    total = BLOCK_FRAMES2[block]; w = [len(s) for s, _ in BLOCKS2[block]]
    fr = [round(total * x / sum(w)) for x in w]; fr[-1] = total - sum(fr[:-1])
    return fr


if __name__ == "__main__":
    b = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    fr = split_frames2(b)
    for i, ((s, fn), n) in enumerate(zip(BLOCKS2[b], fr), 1):
        if only and i not in only: continue
        render(fn, n / FPS, f"{OUT}/bloco{b:02d}-slide{i:02d}.mp4")
        print("ok blocco", b, "clip", i, n, "fotogrammi", flush=True)
