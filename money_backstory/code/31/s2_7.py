import sys
sys.path.insert(0, "/home/claude/slides")
from engine import *

# ---------- oggetti extra ----------
def tag_label(img, t_in, text, y, color=SAGE):
    a = seg(t_in, 0, 0.5)
    if a <= 0: return
    lay = new_layer(); rgb, mask = lay
    dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    f = font(FONT_SANS, 40)
    tw = dr.textlength(text, font=f) + 11 * (len(text) - 1)
    x = W//2 - (tw + 70) / 2
    for dd, c in ((dr, color), (dm, 255)):
        dd.polygon([(x, y), (x+16, y-16), (x+32, y), (x+16, y+16)], fill=c)
    cx = x + 70
    for ch in text:
        dr.text((cx, y), ch, font=f, fill=color, anchor="lm")
        dm.text((cx, y), ch, font=f, fill=255, anchor="lm")
        cx += dr.textlength(ch, font=f) + 11
    alpha_layer(img, lay, ease(a))

def cross(d, cx, cy, r, col, w=12):
    d.line([cx-r, cy-r, cx+r, cy+r], fill=col, width=w)
    d.line([cx-r, cy+r, cx+r, cy-r], fill=col, width=w)

def tick(d, cx, cy, r, col, w=13):
    d.line([cx-r, cy, cx-r*0.2, cy+r*0.7], fill=col, width=w)
    d.line([cx-r*0.2, cy+r*0.7, cx+r, cy-r*0.8], fill=col, width=w)

def row_item(img, t_in, y, text, kind="cross"):
    a = seg(t_in, 0, 0.55)
    if a <= 0: return
    lay = new_layer(); rgb, mask = lay
    dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    dx = int(70 * (1 - ease(a)))
    box = [110 - dx, y - 78, W - 110 - dx, y + 78]
    for dd, c in ((dr, CARD), (dm, 255)):
        dd.rounded_rectangle(box, radius=28, fill=c)
    dr.rounded_rectangle(box, radius=28, outline=(52, 104, 84), width=3)
    col = (214, 108, 96) if kind == "cross" else SAGE
    cxc = box[0] + 92
    for dd, c in ((dr, col), (dm, 255)):
        dd.ellipse([cxc-52, y-52, cxc+52, y+52], fill=(28, 74, 60) if dd is dr else 255)
    if kind == "cross": cross(dr, cxc, y, 24, col)
    else: tick(dr, cxc, y, 26, col)
    f = font(FONT_SANS, 46)
    dr.text((box[0] + 176, y), text, font=f, fill=IVORY, anchor="lm")
    dm.text((box[0] + 176, y), text, font=f, fill=255, anchor="lm")
    alpha_layer(img, lay, ease(a))

def receipt(img, t_in, cx, cy, progress):
    a = seg(t_in, 0, 0.5)
    if a <= 0: return
    lay = new_layer(); rgb, mask = lay
    dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
    w = 430
    h = int(120 + 380 * ease(progress))
    box = [cx - w//2, cy - 260, cx + w//2, cy - 260 + h]
    for dd, c in ((dr, IVORY), (dm, 255)):
        dd.rounded_rectangle(box, radius=16, fill=c)
    # righe
    yy = box[1] + 54
    dr.text((cx, box[1] + 34), "RECEIPT", font=font(FONT_SANS, 30), fill=(120, 130, 120), anchor="mm")
    n = 0
    while yy < box[3] - 90 and n < 7:
        dr.line([box[0]+40, yy, box[2]-40, yy], fill=(198, 196, 186), width=5)
        yy += 46; n += 1
    if h > 300:
        dr.line([box[0]+34, box[3]-86, box[2]-34, box[3]-86], fill=(150, 150, 140), width=4)
        dr.text((box[0]+40, box[3]-48), "TOTAL", font=font(FONT_SANS, 34), fill=(60, 70, 62), anchor="lm")
        dr.text((box[2]-40, box[3]-48), "$ 41.80", font=font(FONT_SANS, 38), fill=(30, 40, 34), anchor="rm")
    alpha_layer(img, lay, ease(a))

def big_tag(img, t_in, cx, cy, text):
    a = seg(t_in, 0, 0.5)
    if a <= 0: return
    p = min(1.0, ease_back(a))
    lay = new_layer()
    price_tag(lay[0], lay[1], cx, cy + int(40 * (1 - ease(a))), text, w=int(260*p) or 1, h=int(150*p) or 1)
    alpha_layer(img, lay, ease(a))

def wrapped(img, t_in, lines, y0, size=64, color=IVORY, lh=86, start_gap=0.35):
    for i, ln in enumerate(lines):
        a = seg(t_in, i * start_gap, 0.55)
        if a <= 0: continue
        lay = new_layer(); rgb, mask = lay
        for dd, c in ((ImageDraw.Draw(rgb), color), (ImageDraw.Draw(mask), 255)):
            dd.text((W//2, y0 + i * lh + int(26 * (1 - ease(a)))), ln,
                    font=font(FONT_SANS, size), fill=c, anchor="mm")
        alpha_layer(img, lay, ease(a))

# =======================================================
def s2(img, t):
    tag_label(img, t, "THE CATCH", 420, GOLD)
    wrapped(img, t - 0.3, ["NO SIGN.", "NO ANNOUNCEMENT."], 720, size=88, lh=118)
    a = seg(t, 1.1, 0.6)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
        box = [190, 1130, W-190, 1420]
        for dd, c in ((dr, CARD), (dm, 255)):
            dd.rounded_rectangle(box, radius=30, fill=c)
        dr.rounded_rectangle(box, radius=30, outline=SAGE_D, width=4)
        # insegna negozio
        for dd, c in ((dr, (28, 74, 60)), (dm, 255)):
            dd.rounded_rectangle([250, 1190, W-250, 1300], radius=14, fill=c)
        dr.text((W//2, 1245), "STORE", font=font(FONT_SANS, 52), fill=SAGE, anchor="mm")
        dr.text((W//2, 1360), "no discount listed", font=font(FONT_SANS_M, 36), fill=(200, 150, 140), anchor="mm")
        alpha_layer(img, lay, ease(a))

def s3(img, t):
    tag_label(img, t, "WHY YOU MISS IT", 380, GOLD)
    row_item(img, t - 0.5, 720, "Not posted on the door")
    row_item(img, t - 1.4, 940, "Never asked at the register")
    row_item(img, t - 2.3, 1160, "Cashiers are not trained to offer it")
    a = seg(t, 3.2, 0.6)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        for dd, c in ((ImageDraw.Draw(rgb), GOLD), (ImageDraw.Draw(mask), 255)):
            dd.text((W//2, 1430), "IT IS ON YOU TO ASK", font=font(FONT_SANS, 62), fill=c, anchor="mm")
        alpha_layer(img, lay, ease(a))

def s4(img, t):
    tag_label(img, t, "TIMING", 330, GOLD)
    receipt(img, t - 0.3, W//2, 1000, seg(t, 0.5, 1.8))
    a = seg(t, 2.3, 0.6)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
        box = [120, 1420, W-120, 1600]
        for dd, c in ((dr, CARD), (dm, 255)):
            dd.rounded_rectangle(box, radius=30, fill=c)
        dr.rounded_rectangle(box, radius=30, outline=GOLD, width=5)
        dr.text((W//2, 1478), "ASK BEFORE THE TOTAL", font=font(FONT_SANS, 58), fill=GOLD, anchor="mm")
        dm.text((W//2, 1478), "ASK BEFORE THE TOTAL", font=font(FONT_SANS, 58), fill=255, anchor="mm")
        dr.text((W//2, 1548), "after it is rung up, it is gone", font=font(FONT_SANS_M, 36), fill=SAGE, anchor="mm")
        alpha_layer(img, lay, ease(a))

def s5(img, t):
    tag_label(img, t, "THE ONE QUESTION", 330, GOLD)
    a = seg(t, 0.4, 0.7)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
        box = [95, 540, W-95, 1360]
        for dd, c in ((dr, CARD), (dm, 255)):
            dd.rounded_rectangle(box, radius=40, fill=c)
        dr.rounded_rectangle(box, radius=40, outline=SAGE_D, width=5)
        dr.text((160, 640), "\u201C", font=font(FONT_SERIF, 200), fill=(52, 104, 84), anchor="lm")
        alpha_layer(img, lay, ease(a))
    wrapped(img, t - 1.2, ["Do you offer", "a senior discount", "\u2014 and at what age", "does it start?"],
            760, size=72, lh=112, color=IVORY, start_gap=0.45)
    a = seg(t, 3.9, 0.7)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
        f = font(FONT_SANS, 46)
        dr.text((W//2, 1480), "SAY IT EXACTLY LIKE THIS", font=f, fill=GOLD, anchor="mm")
        dm.text((W//2, 1480), "SAY IT EXACTLY LIKE THIS", font=f, fill=255, anchor="mm")
        alpha_layer(img, lay, ease(a))

def s6(img, t):
    tag_label(img, t, "IT CHANGES EVERYWHERE", 360, GOLD)
    big_tag(img, t - 0.5, W//2, 700, "55")
    big_tag(img, t - 1.3, W//2, 1000, "60")
    big_tag(img, t - 2.1, W//2, 1300, "62")
    a = seg(t, 3.0, 0.6)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        for dd, c in ((ImageDraw.Draw(rgb), IVORY), (ImageDraw.Draw(mask), 255)):
            dd.text((W//2, 1560), "NEVER ASSUME THE AGE", font=font(FONT_SANS, 56), fill=c, anchor="mm")
        alpha_layer(img, lay, ease(a))

def s7(img, t):
    tag_label(img, t, "WHAT TO DO", 330, SAGE)
    row_item(img, t - 0.4, 640, "Your grocery store", "tick")
    row_item(img, t - 1.1, 850, "Your pharmacy", "tick")
    row_item(img, t - 1.8, 1060, "Restaurants you like", "tick")
    row_item(img, t - 2.5, 1270, "Hardware and auto shops", "tick")
    a = seg(t, 3.6, 0.7)
    if a > 0:
        lay = new_layer(); rgb, mask = lay
        dr, dm = ImageDraw.Draw(rgb), ImageDraw.Draw(mask)
        box = [110, 1440, W-110, 1650]
        for dd, c in ((dr, CARD), (dm, 255)):
            dd.rounded_rectangle(box, radius=34, fill=c)
        dr.rounded_rectangle(box, radius=34, outline=GOLD, width=5)
        dr.text((W//2, 1508), "ASK ONCE.", font=font(FONT_SANS, 62), fill=IVORY, anchor="mm")
        dm.text((W//2, 1508), "ASK ONCE.", font=font(FONT_SANS, 62), fill=255, anchor="mm")
        dr.text((W//2, 1588), "SAVE FOR YEARS.", font=font(FONT_SANS, 62), fill=GOLD, anchor="mm")
        dm.text((W//2, 1588), "SAVE FOR YEARS.", font=font(FONT_SANS, 62), fill=255, anchor="mm")
        alpha_layer(img, lay, ease(a))

JOBS = [(s2, 2.73, 2), (s3, 4.40, 3), (s4, 4.60, 4), (s5, 6.87, 5), (s6, 4.33, 6), (s7, 6.14, 7)]
for fn, dur, n in JOBS:
    render(fn, dur, f"/mnt/user-data/outputs/slide-0{n}.mp4")
    print("slide", n, "ok")
