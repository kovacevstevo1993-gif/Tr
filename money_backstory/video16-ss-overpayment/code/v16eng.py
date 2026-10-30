"""Motore slide video 16 (lettera di sovrapagamento Social Security, Carol). Parte dal motore v14 (modello unico: cornice oro 3D, stessi colori blu notte e oro,
titolo, pillola all'80%, schede) e CAMBIA UN PO' l'aspetto (regola utente 30/10 "cambia un po'"): sfondo a righe diagonali con alone spostato e riflesso che corre al contrario,
particelle quadrate d'oro, filetto con rombo sotto il titolo, schede con banda colorata in alto. Elementi nuovi: lettera ufficiale con righe, assegno diviso a meta',
linea dei giorni con zone, porte numerate, modulo SSA, cartellina con ricevute."""
import math, random
import v14eng
from v14eng import *
import v13eng as _E
import v8b1
from PIL import Image, ImageDraw, ImageFilter

# ---------------- SFONDO NUOVO (stessa palette) ----------------
def _make_bg16():
    bg = Image.new('RGBA', (W, H), navy + (255,))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse([W * 0.62 - 900, H * 0.42 - 500, W * 0.62 + 900, H * 0.42 + 500], fill=(30, 60, 100, 255))
    bg = Image.alpha_composite(bg, g.filter(ImageFilter.GaussianBlur(220)))
    g2 = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g2).ellipse([-250, H - 420, 650, H + 300], fill=(60, 48, 20, 255))
    bg = Image.alpha_composite(bg, g2.filter(ImageFilter.GaussianBlur(190)))      # alone caldo in basso a sinistra
    v = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(v).rectangle([0, 0, W, H], fill=(0, 0, 0, 120))
    ImageDraw.Draw(v).ellipse([-200, -150, W + 200, H + 150], fill=(0, 0, 0, 0))
    bg = Image.alpha_composite(bg, v.filter(ImageFilter.GaussianBlur(120)))
    pat = Image.new('RGBA', (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(pat)
    for k in range(-H, W, 64): pd.line([k, 0, k + H, H], fill=(255, 255, 255, 9), width=1)      # righe diagonali (prima: griglia)
    bg = Image.alpha_composite(bg, pat)
    ring = Image.new('RGBA', (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(ring)                       # sigillo molto tenue a destra
    for r in (330, 300, 270, 190): rd.ellipse([1500 - r, 560 - r, 1500 + r, 560 + r], outline=(246, 214, 140, 11), width=3)
    return Image.alpha_composite(bg, ring)
BG16 = _make_bg16()
_SW16 = Image.new('RGBA', (W + 1400, H), (0, 0, 0, 0)); ImageDraw.Draw(_SW16).polygon([(300, 0), (520, 0), (920, H), (700, H)], fill=(255, 230, 160, 17)); _SW16 = _SW16.filter(ImageFilter.GaussianBlur(40))
random.seed(16)
PARTS16 = [(random.uniform(0, W), random.uniform(0, H), random.uniform(3, 6), random.uniform(7, 20), random.uniform(0, 6.28)) for _ in range(46)]
def base16(t):
    fr = BG16.copy()
    off = int((t * 130) % (W + 800)); x = max(0, min(1400, off))
    fr.alpha_composite(_SW16.crop((x, 0, x + W, H)))                                                  # il riflesso corre da sinistra a destra (prima: al contrario)
    P = Image.new('RGBA', (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(P)
    for (px, py, r, sp_, ph) in PARTS16:
        y = (py - t * sp_) % H; a = int(60 + 55 * math.sin(t * 1.4 + ph))
        pd.rectangle([px - r, y - r, px + r, y + r], fill=(246, 214, 140, a))                          # quadratini (prima: cerchi)
    return Image.alpha_composite(fr, P)

ORNAMENT = True
def stage_live16(t, title, seed, size=60):
    fr = base16(v8b1.LIVE['t']); fr = amb(fr, v8b1.LIVE['t'], seed, 5, 40)
    fr = title_layer(fr, title, t, size=size)
    if not ORNAMENT: return fr
    a = int(255 * min(1.0, max(0.0, t / 0.5))); L = new(); d = ImageDraw.Draw(L)                    # filetto con rombo sotto il titolo
    d.line([300, 172, 900, 172], fill=gold + (a,), width=3); d.line([1020, 172, 1620, 172], fill=gold + (a,), width=3)
    d.polygon([(960, 158), (974, 172), (960, 186), (946, 172)], fill=goldL + (a,))
    return Image.alpha_composite(fr, L)
_E.stage_live = stage_live16
v8b1.base = base16

# ---------------- SCHEDE: banda colorata in alto ----------------
def card16(C, x0, y0, x1, y1, col, head=None, val=None, sub=None, vsize=96, vcol=white, fill=card):
    d = ImageDraw.Draw(C); cx = (x0 + x1) / 2
    d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=fill + (255,), outline=col + (255,), width=6)
    d.rounded_rectangle([x0 + 9, y0 + 9, x1 - 9, y0 + 24], radius=7, fill=col + (255,))                # banda colorata
    if head: txt(C, head, fit(head, x1 - x0 - 40, 38), y0 + 34, col, 255, x=cx)
    if val: txt(C, val, fit(val, x1 - x0 - 40, vsize), y0 + (92 if head else 54), vcol, 255, x=cx)
    if sub: txt(C, sub, fit(sub, x1 - x0 - 40, 34), y1 - 56, grey, 255, x=cx)
_E.card_ = card16

# ---------------- ELEMENTI NUOVI ----------------
PAPER = (150, 245, 960, 715)
def nrow_box(pbox, i, n):
    x0, y0, x1, y1 = pbox; top = y0 + 108; rh = (y1 - top - 24) / n
    return (x0 + 24, top + i * rh, x1 - 24, top + (i + 1) * rh - 8)

def draw_new16(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'paper':          # lettera ufficiale: carta, ombra, testata blu con sigillo
        d.rounded_rectangle([x0 + 12, y0 + 14, x1 + 12, y1 + 14], radius=16, fill=(0, 0, 0, 120))
        rr(d, [x0, y0, x1, y1], 16, (238, 241, 246), (186, 194, 210), 4)
        rr(d, [x0, y0, x1, y0 + 92], 16, (24, 48, 86)); d.rectangle([x0, y0 + 56, x1, y0 + 92], fill=(24, 48, 86, 255))
        d.ellipse([x0 + 24, y0 + 14, x0 + 82, y0 + 72], outline=goldL + (255,), width=4); T(C, 'SSA', 24, y0 + 30, goldL, x=x0 + 53)
        T(C, k.get('agency', 'SOCIAL SECURITY ADMINISTRATION'), 26, y0 + 12, (190, 205, 230), x=x0 + 104, anchor='l', maxw=x1 - x0 - 130)
        T(C, k.get('head', 'NOTICE OF OVERPAYMENT'), 40, y0 + 42, goldL, x=x0 + 104, anchor='l', maxw=x1 - x0 - 130)
        if k.get('fold'): d.line([x0 + 10, y0 + (y1 - y0) * 0.5, x1 - 10, y0 + (y1 - y0) * 0.5], fill=(205, 212, 226, 255), width=3)
    elif kind == 'nrow':         # una riga della lettera (stessa geometria: pbox, i, n)
        pb = k['pbox']; r = nrow_box(pb, k['i'], k['n']); hl = k.get('hl')
        if hl: rr(d, list(r), 14, (255, 226, 226), red, 5)
        else: d.line([r[0] + 6, r[3], r[2] - 6, r[3]], fill=(200, 207, 220, 255), width=2)
        rh = r[3] - r[1]
        T(C, k['label'], int(min(40, rh * 0.5)), r[1] + rh / 2 - min(40, rh * 0.5) * 0.6, (70, 82, 104), x=r[0] + 14, anchor='l', maxw=(r[2] - r[0]) * 0.52)
        vc = {'red': (200, 40, 50), 'green': (30, 130, 80), 'navy': (24, 48, 86)}.get(k.get('vc', 'navy'), (24, 48, 86))
        T(C, k['val'], int(min(54 if hl else 46, rh * 0.62)), r[1] + rh / 2 - min(54 if hl else 46, rh * 0.62) * 0.6, vc, x=r[2] - 14, anchor='r', maxw=(r[2] - r[0]) * 0.46)
    elif kind == 'paycut':       # assegno mensile diviso: trattenuto (rosso) / ricevuto (verde)
        T(C, k['head'], 44, y0 + 6, goldL, x=x0, anchor='l'); T(C, k['total'], 74, y0 - 4, white, x=x1, anchor='r')
        by0, by1 = y0 + 96, y0 + 236; frac = k.get('frac', 0.5); mx_ = x0 + (x1 - x0) * (1 - frac)
        rr(d, [x0, by0, x1, by1], 26, (40, 58, 86), white, 4)
        rr(d, [x0, by0, mx_, by1], 26, green, white, 3)
        if frac > 0:
            rr(d, [mx_, by0, x1, by1], 26, red, white, 3)
            for kx in range(int(mx_) + 20, int(x1) - 8, 34): d.line([kx, by1 - 10, kx + 26, by0 + 10], fill=(255, 255, 255, 60), width=4)
        d.line([mx_, by0 - 28, mx_, by1 + 28], fill=goldL + (255,), width=8)
        T(C, k['kept'], 70, by0 + 34, white, x=x0 + (mx_ - x0) / 2, maxw=mx_ - x0 - 30); T(C, k['held'], 70, by0 + 34, white, x=mx_ + (x1 - mx_) / 2, maxw=x1 - mx_ - 30)
        T(C, k['kept_l'], 40, by1 + 22, green, x=x0 + (mx_ - x0) / 2, maxw=mx_ - x0 - 20); T(C, k['held_l'], 40, by1 + 22, red, x=mx_ + (x1 - mx_) / 2, maxw=x1 - mx_ - 20)
    elif kind == 'dtl':          # linea dei giorni: zone colorate e bandierine (giorno 0, 30, 60)
        mx_ = k['mx']; lx0, lx1 = x0 + 30, x1 - 30; by0, by1 = y0 + 190, y0 + 300
        def X(v): return lx0 + (lx1 - lx0) * v / mx_
        for (a, b, col, lab) in k['zones']:
            rr(d, [X(a), by0, X(b), by1], 18, col, white, 3); T(C, lab, 40, by0 + 30, white if col != gold else navy, x=(X(a) + X(b)) / 2, maxw=X(b) - X(a) - 24)
        for (dv, lab, sub, col) in k['marks']:
            d.line([X(dv), by0 - 70, X(dv), by1 + 18], fill=col + (255,), width=7); d.ellipse([X(dv) - 15, by0 - 86, X(dv) + 15, by0 - 56], fill=col + (255,), outline=white + (255,), width=3)
            T(C, lab, 44, by0 - 150, col, x=min(max(X(dv), x0 + 160), x1 - 160), maxw=360); T(C, sub, 34, by1 + 34, white, x=min(max(X(dv), x0 + 170), x1 - 170), maxw=360)
    elif kind == 'door':         # porta ad arco numerata
        w = x1 - x0; ah = w / 2
        rr(d, [x0, y0 + ah, x1, y1 - 120], 12, (46, 70, 104), c, 7)
        d.pieslice([x0, y0, x1, y0 + w], 180, 360, fill=(46, 70, 104, 255), outline=c + (255,), width=7)
        d.rectangle([x0 + 4, y0 + ah, x1 - 4, y0 + ah + 6], fill=(46, 70, 104, 255))
        d.ellipse([x1 - 62, (y0 + ah + y1 - 120) / 2 - 14, x1 - 34, (y0 + ah + y1 - 120) / 2 + 14], fill=goldL + (255,))
        T(C, str(k['n']), 120, y0 + ah - 46, goldL, x=cx)
        T(C, k['l1'], 48, y1 - 104, white, x=cx, maxw=w + 40); T(C, k['l2'], 36, y1 - 48, c if c != gold else goldL, x=cx, maxw=w + 40)
    elif kind == 'ssaform':      # modulo SSA con codice
        d.rounded_rectangle([x0 + 10, y0 + 12, x1 + 10, y1 + 12], radius=14, fill=(0, 0, 0, 110))
        rr(d, [x0, y0, x1, y1], 14, (238, 241, 246), c, 6); rr(d, [x0, y0, x1, y0 + 88], 14, (24, 48, 86)); d.rectangle([x0, y0 + 52, x1, y0 + 88], fill=(24, 48, 86, 255))
        T(C, k['code'], 44, y0 + 20, goldL, x=cx, maxw=x1 - x0 - 30)
        T(C, k['name'], 30, y0 + 104, (70, 82, 104), x=cx, maxw=x1 - x0 - 30)
        for j in range(k.get('lines', 4)):
            yy = y0 + 170 + j * 52
            d.rounded_rectangle([x0 + 36, yy, x0 + 66, yy + 30], radius=5, outline=(24, 48, 86, 255), width=3)
            if j in k.get('ticks', ()): check(C, x0 + 51, yy + 15, 11, (30, 130, 80))
            d.line([x0 + 84, yy + 24, x1 - 40 - (j % 2) * 70, yy + 24], fill=(170, 180, 200, 255), width=5)
        d.line([x0 + 40, y1 - 46, x0 + (x1 - x0) * 0.6, y1 - 46], fill=(24, 48, 86, 255), width=3); T(C, 'SIGNATURE', 22, y1 - 40, (110, 122, 144), x=x0 + 40, anchor='l')
    elif kind == 'folder':       # cartellina con ricevute
        w = x1 - x0; h = y1 - y0 - 90
        d.rounded_rectangle([x0 + 20, y0 + 30, x0 + w * 0.42, y0 + 80], radius=14, fill=(196, 150, 60, 255))
        for j in range(3):
            d.rounded_rectangle([x0 + 50 + j * 22, y0 + 20 + (2 - j) * 8, x1 - 50 - j * 22, y0 + h * 0.6], radius=8, fill=(238, 241, 246, 255), outline=(170, 180, 200, 255), width=2)
        d.rounded_rectangle([x0, y0 + 70, x1, y0 + h + 10], radius=22, fill=gold + (255,), outline=goldL + (255,), width=5)
        T(C, k['l1'], 52, y0 + h * 0.52, navy, x=cx, maxw=w - 40)
        T(C, k['l2'], 40, y1 - 62, white, x=cx, maxw=w + 40)
    elif kind == 'bigvs':        # due numeri grandi a confronto con barra colorata (es. 10% / 50%)
        w = (x1 - x0 - 100) / 2
        for j, (hd, big, sub, cc) in enumerate(k['cols']):
            bx = x0 + j * (w + 100); rr(d, [bx, y0, bx + w, y1], 28, card, cc, 6); rr(d, [bx, y0, bx + w, y0 + 78], 28, cc); d.rectangle([bx, y0 + 44, bx + w, y0 + 78], fill=cc + (255,))
            T(C, hd, 36, y0 + 17, navy if cc in (gold, green) else white, x=bx + w / 2, maxw=w - 30); T(C, big, 150, y0 + 100, white, x=bx + w / 2, maxw=w - 30); T(C, sub, 38, y1 - 80, cc if cc != gold else goldL, x=bx + w / 2, maxw=w - 30)
        if k.get('mid'): T(C, k['mid'], 70, cy - 40, goldL, x=x0 + w + 50)
    elif kind == 'ovsel':        # busta con timbro/alert: busta grande e punto esclamativo
        w, h = x1 - x0, y1 - y0
        d.rounded_rectangle([x0 + 10, y0 + 16, x1 + 10, y1 + 16], radius=18, fill=(0, 0, 0, 110))
        rr(d, [x0, y0, x1, y1], 18, (238, 241, 246), c, 6)
        d.line([x0 + 6, y0 + 6, cx, cy + 20, x1 - 6, y0 + 6], fill=c + (255,), width=7)
        d.ellipse([cx - 62, cy - 14, cx + 62, cy + 110], fill=red + (255,), outline=white + (255,), width=5); T(C, '!', 100, cy - 14, white, x=cx)
        if k.get('l1'): T(C, k['l1'], 44, y1 + 20, white, x=cx, maxw=w + 80)
    elif kind == 'subbtn':       # pulsante SUBSCRIBE con campanella
        w, h = x1 - x0, y1 - y0
        rr(d, [x0, y0, x1, y1], int(h / 2), red, white, 5)
        bx = x0 + h * 0.62; by = cy; r = h * 0.26
        d.ellipse([bx - r, by - r * 1.3, bx + r, by + r * 0.7], fill=white + (255,)); d.rectangle([bx - r, by - r * 0.2, bx + r, by + r * 0.7], fill=white + (255,))
        d.polygon([(bx - r * 1.35, by + r * 0.75), (bx + r * 1.35, by + r * 0.75), (bx + r, by + r * 0.4), (bx - r, by + r * 0.4)], fill=white + (255,))
        d.ellipse([bx - r * 0.3, by + r * 0.8, bx + r * 0.3, by + r * 1.25], fill=goldL + (255,))
        T(C, k.get('t', 'SUBSCRIBE'), int(h * 0.42), cy - h * 0.25, white, x=cx + h * 0.4, maxw=w - h * 1.4)
    else: _orig16(C, e)
_orig16 = _E.draw_new
_E.draw_new = draw_new16
PULSE_KINDS.update({'paper', 'nrow', 'paycut', 'dtl', 'door', 'ssaform', 'folder', 'bigvs', 'ovsel', 'subbtn'})
