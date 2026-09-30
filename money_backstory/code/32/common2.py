from PIL import Image, ImageDraw, ImageFont
import common as C
from common import W, H, GOLD, GOLD_LIGHT, WHITE, RED, GREEN, font, ease
import math

def wrap_center(d, text, f, cy, max_w, fill, line_gap=14):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    heights = [f.getbbox(l)[3] - f.getbbox(l)[1] for l in lines]
    total = sum(heights) + line_gap * (len(lines) - 1)
    y = cy - total / 2
    for l, h in zip(lines, heights):
        d.text((W/2, y + h/2), l, font=f, fill=fill, anchor="mm")
        y += h + line_gap

# ---------- SLIDE 1: HOOK ----------
def slide1(img, t, i, n):
    d = ImageDraw.Draw(img, "RGBA")
    dur = n / C.FPS
    a1 = min(1, max(0, (t - 0.2) / 0.8))
    d.text((W/2, H*0.30), "AGE", font=font(58), fill=(GOLD_LIGHT[0], GOLD_LIGHT[1], GOLD_LIGHT[2], int(255*a1)), anchor="mm")
    a2 = min(1, max(0, (t - 0.5) / 0.9))
    d.text((W/2, H*0.30+80), "59\u00bd", font=font(140), fill=(WHITE[0], WHITE[1], WHITE[2], int(255*a2)), anchor="mm")

    # bar comparison appears mid-slide
    bt = min(1, max(0, (t - dur*0.35) / (dur*0.35)))
    if bt > 0:
        e = ease(bt)
        base_y = H*0.72
        bar_w = 300
        gap = 220
        cx1 = W/2 - gap
        cx2 = W/2 + gap
        max_h = 260
        h1 = max_h * e
        h2 = max_h * 0.0  # penalty erased -> stays flat near-zero once fully shown
        col_before = RED
        col_after = GREEN
        # BEFORE bar (penalty) shrinking to zero as e -> 1 to show "it disappears"
        shrink = max_h * e * (1 - min(1, max(0, (bt-0.6)/0.4)))
        d.rectangle([cx1-bar_w/2, base_y-shrink, cx1+bar_w/2, base_y], fill=col_before+(230,))
        d.text((cx1, base_y+40), "$10,000", font=font(40), fill=col_before+(int(255*e)), anchor="mm")
        d.text((cx1, base_y+90), "PENALTY BEFORE", font=font(24, False), fill=WHITE+(int(200*e)), anchor="mm")
        # AFTER bar (zero) with green check
        d.rectangle([cx2-bar_w/2, base_y-6, cx2+bar_w/2, base_y], fill=col_after+(int(230*e)))
        d.text((cx2, base_y+40), "$0", font=font(40), fill=col_after+(int(255*e)), anchor="mm")
        d.text((cx2, base_y+90), "AFTER 59\u00bd", font=font(24, False), fill=WHITE+(int(200*e)), anchor="mm")

def build_slide1(path, n_frames):
    C.render(path, n_frames, slide1, source="Source: IRC \u00a772(t)")

# ---------- SLIDE 2: MAP OF 5 POINTS ----------
POINTS = [
    "10% PENALTY\nDISAPPEARS",
    "HIDDEN WITHDRAWAL\nDOOR",
    "ROTH 5-YEAR\nCLOCK",
    "THE TRAP\n(#4)",
    "BIGGER\nCONTRIBUTION LIMIT",
]

def slide2(img, t, i, n):
    d = ImageDraw.Draw(img, "RGBA")
    dur = n / C.FPS
    per = dur / 5.2
    y = H*0.22
    d.text((W/2, y), "5 THINGS THAT CHANGE", font=font(46), fill=GOLD_LIGHT+(255,), anchor="mm")
    start_y = H*0.38
    step = (H*0.92 - start_y) / 5
    for idx, label in enumerate(POINTS):
        appear_t = idx * per
        a = min(1, max(0, (t - appear_t) / 0.5))
        if a <= 0:
            continue
        slide_x = (1 - ease(a)) * 60
        cy = start_y + idx*step
        highlight = (idx == 3)
        num_col = RED if highlight else GOLD
        d.ellipse([80-slide_x, cy-28, 136-slide_x, cy+28], outline=num_col+(int(255*a),), width=5)
        d.text((108-slide_x, cy), str(idx+1), font=font(34), fill=num_col+(int(255*a),), anchor="mm")
        d.text((175-slide_x, cy), label.replace("\n", "  "), font=font(30, False), fill=WHITE+(int(230*a),), anchor="lm")

def build_slide2(path, n_frames):
    C.render(path, n_frames, slide2)

# ---------- SLIDE 3: FRANK & MARY ----------
def avatar(d, cx, cy, r, color, alpha, label):
    d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=color+(int(255*alpha),), width=8)
    d.ellipse([cx-r*0.32, cy-r*0.55, cx+r*0.32, cy-r*0.08], fill=color+(int(160*alpha),))  # head
    d.pieslice([cx-r*0.62, cy-r*0.05, cx+r*0.62, cy+r*0.85], 180, 360, fill=color+(int(160*alpha),))  # shoulders
    d.text((cx, cy+r+50), label, font=font(38), fill=WHITE+(int(255*alpha),), anchor="mm")

def slide3(img, t, i, n):
    d = ImageDraw.Draw(img, "RGBA")
    dur = n / C.FPS
    a1 = min(1, max(0, (t-0.2)/0.8))
    slide1x = (1-ease(a1))*220
    avatar(d, W*0.30-slide1x, H*0.42, 150, (110,170,255), a1, "FRANK")

    a2 = min(1, max(0, (t-0.9)/0.8))
    slide2x = (1-ease(a2))*220
    avatar(d, W*0.70+slide2x, H*0.42, 150, GOLD, a2, "MARY")

    a3 = min(1, max(0, (t-1.6)/0.6))
    d.text((W/2, H*0.42), "59\u00bd", font=font(54), fill=WHITE+(int(255*a3)), anchor="mm")
