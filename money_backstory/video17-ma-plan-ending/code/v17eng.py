"""Motore slide video 17 (piano Medicare Advantage non rinnovato, Gloria). Parte dal motore v16 (modello unico: cornice oro 3D, blu notte e oro, titolo, pillola all'80%, schede)
e CAMBIA UN PO' l'aspetto (regola utente 30/10 "cambia un po'"): sfondo blu-petrolio con righe orizzontali "registro" e grande croce-scudo tenue a destra,
luce che sale dal basso, cerchietti con anello al posto dei quadratini, filetto con tre punti sotto il titolo, schede con banda LATERALE colorata.
Elementi realistici per il tema Medicare: tessera Medicare, lettera di non rinnovo con busta, pagine di calendario vere (dicembre 2026), flacone Rx, telefono, portatile con Plan Finder,
pittogramma 8 su 10, striscia dei giorni (59 su 63), due piani che si fondono, piano che passa a Original Medicare."""
import math, random, datetime
import v16eng
from v16eng import *
import v13eng as _E
import v8b1
from PIL import Image, ImageDraw, ImageFilter

TEAL = (22, 78, 112)
# ---------------- SFONDO (stessa palette, aspetto un po' diverso dal video 16) ----------------
def _make_bg17():
    bg = Image.new('RGBA', (W, H), navy + (255,))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse([W * 0.30 - 800, H * 0.30 - 480, W * 0.30 + 800, H * 0.30 + 480], fill=TEAL + (255,))
    bg = Image.alpha_composite(bg, g.filter(ImageFilter.GaussianBlur(230)))                        # alone petrolio in alto a sinistra (prima: a destra)
    g2 = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g2).ellipse([W - 650, H - 400, W + 250, H + 300], fill=(64, 50, 22, 255))
    bg = Image.alpha_composite(bg, g2.filter(ImageFilter.GaussianBlur(190)))                       # alone caldo in basso a destra (prima: a sinistra)
    v = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(v).rectangle([0, 0, W, H], fill=(0, 0, 0, 120))
    ImageDraw.Draw(v).ellipse([-200, -150, W + 200, H + 150], fill=(0, 0, 0, 0))
    bg = Image.alpha_composite(bg, v.filter(ImageFilter.GaussianBlur(120)))
    pat = Image.new('RGBA', (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(pat)
    for k in range(0, H, 54): pd.line([0, k, W, k], fill=(255, 255, 255, 8), width=1)             # righe orizzontali (prima: diagonali)
    bg = Image.alpha_composite(bg, pat)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)                          # grande croce dentro uno scudo, molto tenue, a destra
    cx, cy = 1560, 560
    sd.polygon([(cx - 250, cy - 300), (cx + 250, cy - 300), (cx + 250, cy + 60), (cx, cy + 330), (cx - 250, cy + 60)], outline=(246, 214, 140, 12), width=4)
    sd.rectangle([cx - 38, cy - 190, cx + 38, cy + 90], outline=(246, 214, 140, 12), width=4); sd.rectangle([cx - 140, cy - 88, cx + 140, cy - 12], outline=(246, 214, 140, 12), width=4)
    return Image.alpha_composite(bg, sh)
BG17 = _make_bg17()
_SW17 = Image.new('RGBA', (W, H + 1000), (0, 0, 0, 0)); ImageDraw.Draw(_SW17).polygon([(0, 300), (W, 100), (W, 300), (0, 500)], fill=(255, 230, 160, 16)); _SW17 = _SW17.filter(ImageFilter.GaussianBlur(46))
random.seed(17)
PARTS17 = [(random.uniform(0, W), random.uniform(0, H), random.uniform(5, 9), random.uniform(7, 18), random.uniform(0, 6.28)) for _ in range(40)]
def base17(t):
    fr = BG17.copy()
    y = int(1000 - (t * 90) % 1000)
    fr.alpha_composite(_SW17.crop((0, y, W, y + H)))                                                  # la luce sale dal basso verso l'alto (prima: correva di lato)
    P = Image.new('RGBA', (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(P)
    for (px, py, r, sp_, ph) in PARTS17:
        yy = (py - t * sp_) % H; a = int(55 + 50 * math.sin(t * 1.3 + ph))
        pd.ellipse([px - r, yy - r, px + r, yy + r], outline=(246, 214, 140, a), width=2)               # cerchietti con anello (prima: quadratini pieni)
        pd.ellipse([px - 2, yy - 2, px + 2, yy + 2], fill=(246, 214, 140, a))
    return Image.alpha_composite(fr, P)
def stage_live17(t, title, seed, size=60):
    fr = base17(v8b1.LIVE['t']); fr = amb(fr, v8b1.LIVE['t'], seed, 5, 40)
    fr = title_layer(fr, title, t, size=size)
    a = int(255 * min(1.0, max(0.0, t / 0.5))); L = new(); d = ImageDraw.Draw(L)                    # filetto con tre punti sotto il titolo (prima: rombo)
    d.line([300, 172, 880, 172], fill=gold + (a,), width=3); d.line([1040, 172, 1620, 172], fill=gold + (a,), width=3)
    for dx in (-26, 0, 26): d.ellipse([960 + dx - 6, 166, 960 + dx + 6, 178], fill=goldL + (a,))
    return Image.alpha_composite(fr, L)
_E.stage_live = stage_live17
v8b1.base = base17

# ---------------- SCHEDE: banda LATERALE colorata ----------------
def card17(C, x0, y0, x1, y1, col, head=None, val=None, sub=None, vsize=96, vcol=white, fill=card):
    d = ImageDraw.Draw(C); cx = (x0 + x1) / 2 + 10
    d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=fill + (255,), outline=col + (255,), width=6)
    d.rounded_rectangle([x0 + 9, y0 + 9, x0 + 30, y1 - 9], radius=9, fill=col + (255,))                # banda a sinistra
    if head: txt(C, head, fit(head, x1 - x0 - 90, 38), y0 + 34, col, 255, x=cx)
    if val: txt(C, val, fit(val, x1 - x0 - 90, vsize), y0 + (92 if head else 54), vcol, 255, x=cx)
    if sub: txt(C, sub, fit(sub, x1 - x0 - 90, 34), y1 - 56, grey, 255, x=cx)
_E.card_ = card17

# ---------------- ELEMENTI NUOVI ----------------
INK = (24, 48, 86); PAPERC = (238, 241, 246); LINE = (200, 207, 220); MID = (70, 82, 104)
RED2 = (200, 40, 50); GRN2 = (30, 130, 80); BLU2 = (30, 90, 170)
def shadow(d, b, r=16, off=14, a=120): d.rounded_rectangle([b[0] + off, b[1] + off, b[2] + off, b[3] + off], radius=r, fill=(0, 0, 0, a))
def envelope(C, x0, y0, x1, y1, col, flap_col=None, seal=None):
    d = ImageDraw.Draw(C); shadow(d, (x0, y0, x1, y1), 14, 12)
    rr(d, [x0, y0, x1, y1], 14, PAPERC, col, 6)
    d.line([x0 + 6, y0 + 8, (x0 + x1) / 2, (y0 + y1) / 2 + 14, x1 - 6, y0 + 8], fill=col + (255,), width=6)
    d.line([x0 + 8, y1 - 8, (x0 + x1) / 2 - 20, (y0 + y1) / 2 + 20], fill=LINE + (255,), width=3); d.line([x1 - 8, y1 - 8, (x0 + x1) / 2 + 20, (y0 + y1) / 2 + 20], fill=LINE + (255,), width=3)
    if seal:
        sx, sy = (x0 + x1) / 2, (y0 + y1) / 2 + 14
        d.ellipse([sx - 40, sy - 40, sx + 40, sy + 40], fill=seal + (255,), outline=white + (255,), width=4)
def person_icon(d, cx, top, s, col):
    d.ellipse([cx - 9 * s, top, cx + 9 * s, top + 18 * s], fill=col + (255,))
    d.rounded_rectangle([cx - 15 * s, top + 22 * s, cx + 15 * s, top + 58 * s], radius=int(9 * s), fill=col + (255,))
def draw_new17(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'medcard':        # tessera Medicare (rossa/bianca/blu), numero d'esempio ufficiale CMS
        w, h = x1 - x0, y1 - y0
        shadow(d, (x0, y0, x1, y1), 22, 14)
        rr(d, [x0, y0, x1, y1], 22, (252, 252, 252), (170, 180, 200), 4)
        d.rounded_rectangle([x0 + 4, y0 + 4, x1 - 4, y0 + h * 0.22], radius=18, fill=(0, 71, 155, 255)); d.rectangle([x0 + 4, y0 + h * 0.12, x1 - 4, y0 + h * 0.22], fill=(0, 71, 155, 255))
        d.rectangle([x0 + 4, y0 + h * 0.22, x1 - 4, y0 + h * 0.255], fill=(200, 30, 45, 255))
        T(C, 'MEDICARE', int(h * 0.15), y0 + h * 0.025, white, x=x0 + w * 0.5, anchor='c', maxw=w * 0.5)
        T(C, 'HEALTH INSURANCE', int(h * 0.06), y0 + h * 0.275, (0, 71, 155), x=x0 + 26, anchor='l', maxw=w * 0.7)
        T(C, k.get('name', 'GLORIA SAMPLE'), int(h * 0.085), y0 + h * 0.37, INK, x=x0 + 26, anchor='l', maxw=w - 52)
        T(C, 'MEDICARE NUMBER', int(h * 0.05), y0 + h * 0.52, MID, x=x0 + 26, anchor='l'); T(C, '1EG4-TE5-MK72', int(h * 0.1), y0 + h * 0.58, INK, x=x0 + 26, anchor='l', maxw=w - 52)
        T(C, 'ENTITLED TO', int(h * 0.05), y0 + h * 0.76, MID, x=x0 + 26, anchor='l'); T(C, 'HOSPITAL (PART A)', int(h * 0.062), y0 + h * 0.82, INK, x=x0 + 26, anchor='l', maxw=w * 0.5)
        T(C, 'MEDICAL (PART B)', int(h * 0.062), y0 + h * 0.89, INK, x=x0 + 26, anchor='l', maxw=w * 0.5)
        d.ellipse([x1 - w * 0.2, y1 - h * 0.34, x1 - 26, y1 - 26 - h * 0.02], outline=(0, 71, 155, 255), width=4)
        d.rectangle([x1 - w * 0.125 - 8, y1 - h * 0.27, x1 - w * 0.125 + 8, y1 - h * 0.1], fill=(200, 30, 45, 255)); d.rectangle([x1 - w * 0.125 - 28, y1 - h * 0.2, x1 - w * 0.125 + 28, y1 - h * 0.17], fill=(200, 30, 45, 255))
        if k.get('badge'): rr(d, [x0 + w * 0.55, y0 + h * 0.38, x1 - 24, y0 + h * 0.5], 14, gold, None); T(C, k['badge'], int(h * 0.06), y0 + h * 0.405, navy, x=x0 + w * 0.55 + (w * 0.45 - 24) / 2, maxw=w * 0.4)
    elif kind == 'notice':       # lettera con intestazione del piano, busta dietro, data di ottobre
        lx0, ly0, lx1, ly1 = x0 + 70, y0, x1, y1 - 30
        envelope(C, x0, y0 + (y1 - y0) * 0.25, x0 + (x1 - x0) * 0.62, y1, INK)
        shadow(d, (lx0 + 120, ly0, lx1, ly1), 16, 14)
        rr(d, [lx0 + 120, ly0, lx1, ly1], 16, PAPERC, (186, 194, 210), 4)
        rr(d, [lx0 + 120, ly0, lx1, ly0 + 92], 16, INK); d.rectangle([lx0 + 120, ly0 + 56, lx1, ly0 + 92], fill=INK + (255,))
        d.ellipse([lx0 + 142, ly0 + 14, lx0 + 200, ly0 + 72], outline=goldL + (255,), width=4); T(C, 'MA', 24, ly0 + 30, goldL, x=lx0 + 171)
        T(C, k.get('agency', 'YOUR MEDICARE ADVANTAGE PLAN'), 22, ly0 + 12, (190, 205, 230), x=lx0 + 222, anchor='l', maxw=lx1 - lx0 - 250)
        T(C, k.get('head', 'PLAN NON-RENEWAL NOTICE'), 34, ly0 + 44, goldL, x=lx0 + 222, anchor='l', maxw=lx1 - lx0 - 250)
        T(C, k.get('date', 'OCTOBER 2026'), 28, ly0 + 110, MID, x=lx0 + 146, anchor='l')
        for j, ww in enumerate((0.8, 0.66, 0.74, 0.5, 0.7)):
            yy = ly0 + 166 + j * 48
            d.rounded_rectangle([lx0 + 146, yy, lx0 + 146 + (lx1 - lx0 - 190) * ww, yy + 16], radius=8, fill=(200, 206, 218, 255))
        if k.get('stamp'): rr(d, [lx0 + 146, ly1 - 90, lx1 - 30, ly1 - 26], 12, (255, 226, 226), RED2, 4); T(C, k['stamp'], 32, ly1 - 76, RED2, x=(lx0 + 146 + lx1 - 30) / 2, maxw=lx1 - lx0 - 230)
    elif kind == 'calpage':      # pagina di calendario vera: giorni, giorno evidenziato, intervallo colorato
        yr, mo = k['year'], k['month']; first = datetime.date(yr, mo, 1); nd = (datetime.date(yr + (mo == 12), mo % 12 + 1, 1) - first).days; wd0 = (first.weekday() + 1) % 7
        w = x1 - x0; shadow(d, (x0, y0, x1, y1), 18, 12)
        rr(d, [x0, y0, x1, y1], 18, PAPERC, (186, 194, 210), 4); rr(d, [x0, y0, x1, y0 + 78], 18, k.get('hc', RED2)); d.rectangle([x0, y0 + 40, x1, y0 + 78], fill=k.get('hc', RED2) + (255,))
        T(C, first.strftime('%B').upper() + ' ' + str(yr), 44, y0 + 16, white, x=(x0 + x1) / 2, maxw=w - 40)
        for j, nm in enumerate('SMTWTFS'): T(C, nm, 24, y0 + 90, MID, x=x0 + 24 + (w - 48) * (j + 0.5) / 7)
        cw = (w - 48) / 7; ch = (y1 - y0 - 150) / 6
        for dn in range(1, nd + 1):
            idx = wd0 + dn - 1; r_, c_ = divmod(idx, 7); bx = x0 + 24 + c_ * cw; by = y0 + 124 + r_ * ch
            col = k.get('hl', {}).get(dn)
            if col is None:
                for (a, b, cc) in k.get('ranges', ()):
                    if a <= dn <= b: col = cc
            if col: d.rounded_rectangle([bx + 3, by + 2, bx + cw - 3, by + ch - 4], radius=10, fill=col + (255,))
            T(C, str(dn), int(min(34, ch * 0.62)), by + ch * 0.12, white if col else INK, x=bx + cw / 2)
    elif kind == 'rx':           # flacone con etichetta Rx
        w, h = x1 - x0, y1 - y0; bw = min(w, h * 0.7); bx0 = cx - bw / 2
        d.rounded_rectangle([bx0 - 6, y0, bx0 + bw + 6, y0 + h * 0.2], radius=14, fill=(250, 250, 250, 255), outline=(190, 195, 205, 255), width=3)
        for j in range(5): d.line([bx0 + 14 + j * bw / 5.5, y0 + 6, bx0 + 14 + j * bw / 5.5, y0 + h * 0.2 - 6], fill=(200, 205, 215, 255), width=2)
        shadow(d, (bx0, y0 + h * 0.18, bx0 + bw, y1), 20, 10, 100)
        d.rounded_rectangle([bx0, y0 + h * 0.18, bx0 + bw, y1], radius=20, fill=(228, 132, 28, 255), outline=(250, 190, 100, 255), width=4)
        rr(d, [bx0 + 12, y0 + h * 0.32, bx0 + bw - 12, y0 + h * 0.86], 10, white)
        T(C, 'Rx', int(h * 0.22), y0 + h * 0.34, RED2, x=cx); T(C, k.get('l1', 'YOUR DRUGS'), int(h * 0.085), y0 + h * 0.6, INK, x=cx, maxw=bw - 40); T(C, k.get('l2', ''), int(h * 0.07), y0 + h * 0.72, MID, x=cx, maxw=bw - 40)
        if k.get('lbl'): T(C, k['lbl'], 44, y1 + 14, white, x=cx, maxw=w + 60)
    elif kind == 'phone17':      # telefono con il numero
        w, h = x1 - x0, y1 - y0; pw = min(w, h * 0.5); px0 = cx - pw / 2
        shadow(d, (px0, y0, px0 + pw, y1), 34, 12)
        d.rounded_rectangle([px0, y0, px0 + pw, y1], radius=34, fill=(26, 32, 46, 255), outline=(120, 135, 160, 255), width=5)
        d.rounded_rectangle([px0 + 14, y0 + 44, px0 + pw - 14, y1 - 44], radius=18, fill=(20, 60, 100, 255))
        d.rounded_rectangle([cx - 30, y0 + 16, cx + 30, y0 + 28], radius=6, fill=(70, 80, 100, 255))
        d.ellipse([cx - 30, y1 - 40, cx + 30, y1 - 6], outline=(120, 135, 160, 255), width=3)
        T(C, k.get('top', 'CALLING'), int(pw * 0.1), y0 + 78, (170, 200, 235), x=cx, maxw=pw - 40)
        T(C, k.get('num', '1-800-MEDICARE'), int(pw * 0.115), y0 + 130, white, x=cx, maxw=pw - 36); T(C, k.get('num2', ''), int(pw * 0.08), y0 + 190, goldL, x=cx, maxw=pw - 36)
        d.ellipse([cx - 44, y1 - 190, cx + 44, y1 - 102], fill=(40, 170, 90, 255)); T(C, 'OK', 30, y1 - 163, white, x=cx)
    elif kind == 'laptop':       # portatile con la pagina Plan Finder: righe di medici/farmaci/piani con spunta
        w, h = x1 - x0, y1 - y0; sx0, sy0, sx1, sy1 = x0 + 30, y0, x1 - 30, y1 - 44
        shadow(d, (sx0, sy0, sx1, sy1), 20, 12)
        d.rounded_rectangle([sx0, sy0, sx1, sy1], radius=20, fill=(30, 36, 52, 255), outline=(120, 135, 160, 255), width=5)
        d.rounded_rectangle([x0, sy1 - 2, x1, y1], radius=14, fill=(160, 170, 190, 255)); d.rounded_rectangle([cx - 90, sy1 - 2, cx + 90, sy1 + 12], radius=6, fill=(120, 130, 150, 255))
        rr(d, [sx0 + 16, sy0 + 16, sx1 - 16, sy1 - 16], 10, (246, 248, 252), None)
        d.rectangle([sx0 + 16, sy0 + 16, sx1 - 16, sy0 + 76], fill=BLU2 + (255,)); T(C, k.get('bar', 'MEDICARE PLAN FINDER'), 34, sy0 + 28, white, x=(sx0 + sx1) / 2, maxw=sx1 - sx0 - 60)
        rows = k.get('rows', [])
        rh_ = (sy1 - sy0 - 130) / max(1, len(rows))
        for j, (lab, ok) in enumerate(rows):
            ry = sy0 + 92 + j * rh_
            d.rounded_rectangle([sx0 + 40, ry, sx1 - 40, ry + rh_ - 12], radius=12, fill=(226, 234, 246, 255))
            T(C, lab, int(min(34, rh_ * 0.46)), ry + (rh_ - 12) * 0.22, INK, x=sx0 + 64, anchor='l', maxw=sx1 - sx0 - 220)
            check(C, sx1 - 78, ry + (rh_ - 12) / 2, 17, GRN2) if ok else cross(C, sx1 - 78, ry + (rh_ - 12) / 2, 17, RED2)
    elif kind == 'pictos':       # N persone, le prime n colorate
        n, hi = k.get('n', 10), k.get('hi', 8); gap = (x1 - x0) / n; s = min(gap / 38, (y1 - y0 - 120) / 62)
        for j in range(n):
            px = x0 + gap * (j + 0.5); person_icon(d, px, y0 + 6, s, green if j < hi else (110, 130, 160))
        T(C, k.get('l1', ''), 56, y0 + 62 * s + 22, white, x=cx, maxw=x1 - x0)
        if k.get('l2'): T(C, k['l2'], 40, y0 + 62 * s + 96, goldL, x=cx, maxw=x1 - x0)
    elif kind == 'daybar':       # striscia di giorni: i giorni senza copertura contro la soglia di 63
        total, used, line = k.get('total', 63), k.get('used', 59), k.get('line', 63); gw = (x1 - x0) / total
        for j in range(total):
            bx = x0 + j * gw; d.rounded_rectangle([bx + 1, y0 + 70, bx + gw - 1, y0 + 150], radius=3, fill=((255, 190, 70) if j < used else (60, 82, 112)) + (255,))
        lx = x0 + gw * line; d.line([lx, y0 + 40, lx, y0 + 182], fill=red + (255,), width=8)
        T(C, k.get('mark', '63-DAY LINE'), 38, y0 - 2, red, x=min(lx, x1 - 110), maxw=300); T(C, k.get('cnt', '59 DAYS'), 70, y0 + 186, goldL, x=x0 + gw * used / 2 + 60, maxw=500)
        for (a, b, lab, col) in k.get('months', ()):
            rr(d, [x0 + gw * a, y0 + 262, x0 + gw * b - 4, y0 + 330], 14, col, None); T(C, lab, 36, y0 + 272, navy if col == gold else white, x=x0 + gw * (a + b) / 2, maxw=gw * (b - a) - 20)
    elif kind == 'merge':        # due piani che diventano uno solo
        w = (x1 - x0)
        for j, (lab, cc) in enumerate(k['left']):
            yy = y0 + j * ((y1 - y0 - 40) / 2 + 40) ; hh = (y1 - y0 - 40) / 2
            rr(d, [x0, yy, x0 + w * 0.36, yy + hh], 22, card, cc, 6); T(C, lab, 40, yy + hh / 2 - 24, white, x=x0 + w * 0.18, maxw=w * 0.32)
            d.line([x0 + w * 0.36, yy + hh / 2, x0 + w * 0.5, cy], fill=goldL + (255,), width=8)
        arrow_r(C, x0 + w * 0.5, x0 + w * 0.62, cy, goldL, 255)
        rr(d, [x0 + w * 0.64, y0 + 20, x1, y1 - 20], 26, card, c, 7); T(C, k['right'], 52, cy - 62, white, x=x0 + w * 0.82, maxw=w * 0.32); T(C, k.get('right2', ''), 36, cy + 20, goldL, x=x0 + w * 0.82, maxw=w * 0.32)
    elif kind == 'planswap':     # piano Advantage (con farmaci) -> Original Medicare (A+B) con casella farmaci vuota tratteggiata
        w = x1 - x0
        rr(d, [x0, y0, x0 + w * 0.42, y1], 26, card, gold, 7); T(C, k.get('l1', 'ADVANTAGE PLAN'), 40, y0 + 18, goldL, x=x0 + w * 0.21, maxw=w * 0.38)
        for j, lab in enumerate(k.get('inside', ('HOSPITAL', 'DOCTOR', 'DRUGS'))):
            rr(d, [x0 + 30, y0 + 86 + j * 82, x0 + w * 0.42 - 30, y0 + 156 + j * 82], 12, (46, 70, 104), (110, 130, 160), 3); T(C, lab, 34, y0 + 100 + j * 82, white, x=x0 + w * 0.21, maxw=w * 0.3)
        arrow_r(C, x0 + w * 0.44, x0 + w * 0.56, cy, goldL, 255)
        rr(d, [x0 + w * 0.58, y0, x1, y1], 26, card, c, 7); T(C, k.get('r1', 'ORIGINAL MEDICARE'), 40, y0 + 18, white, x=x0 + w * 0.79, maxw=w * 0.38)
        for j, lab in enumerate(k.get('in2', ('PART A  HOSPITAL', 'PART B  DOCTOR'))):
            rr(d, [x0 + w * 0.58 + 30, y0 + 86 + j * 82, x1 - 30, y0 + 156 + j * 82], 12, (46, 70, 104), c, 3); T(C, lab, 32, y0 + 100 + j * 82, white, x=x0 + w * 0.79, maxw=w * 0.34)
        j = len(k.get('in2', ('', ''))); bx0, by0, bx1, by1 = x0 + w * 0.58 + 30, y0 + 86 + j * 82, x1 - 30, y0 + 156 + j * 82
        for kx in range(int(bx0), int(bx1), 22): d.line([kx, by0, kx + 11, by0], fill=red + (255,), width=4); d.line([kx, by1, kx + 11, by1], fill=red + (255,), width=4)
        d.line([bx0, by0, bx0, by1], fill=red + (255,), width=4); d.line([bx1, by0, bx1, by1], fill=red + (255,), width=4)
        T(C, k.get('gap', 'NO DRUG PLAN'), 32, by0 + 16, red, x=(bx0 + bx1) / 2, maxw=w * 0.34)
    elif kind == 'bluenotice':   # busta blu dell'avviso di riassegnazione (Extra Help)
        w, h = x1 - x0, y1 - y0
        envelope(C, x0, y0, x1, y1 - 70, (30, 100, 200), seal=(30, 100, 200))
        rr(d, [cx - w * 0.38, y1 - 66, cx + w * 0.38, y1], 18, (30, 100, 200), white, 4); T(C, k.get('t', 'BLUE NOTICE'), 40, y1 - 54, white, x=cx, maxw=w * 0.7)
    elif kind == 'sample':       # etichetta con elenco corto (spunte o croci) dentro una scheda scura
        for j, (lab, ok) in enumerate(k['items']):
            yy = y0 + j * ((y1 - y0) / len(k['items']))
            rr(d, [x0, yy, x1, yy + (y1 - y0) / len(k['items']) - 12], 16, card, (green if ok else red), 5)
            (check(C, x0 + 52, yy + ((y1 - y0) / len(k['items']) - 12) / 2, 22, green) if ok else cross(C, x0 + 52, yy + ((y1 - y0) / len(k['items']) - 12) / 2, 22, red))
            T(C, lab, int(k.get('size', 40)), yy + ((y1 - y0) / len(k['items']) - 12) / 2 - 24, white, x=x0 + 100, anchor='l', maxw=x1 - x0 - 130)
    else: _orig17(C, e)
_orig17 = _E.draw_new
_E.draw_new = draw_new17
PULSE_KINDS.update({'medcard', 'notice', 'calpage', 'rx', 'phone17', 'laptop', 'pictos', 'daybar', 'merge', 'planswap', 'bluenotice', 'sample'})
