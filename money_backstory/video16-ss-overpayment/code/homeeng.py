"""Motore slide video 15 (vendere casa dopo i 65 anni). Parte dal motore v14 (modello unico, cornice, sfondo, titolo, pillola all'80%)
e aggiunge elementi nuovi: casa con cartello SOLD, cascata (waterfall) del guadagno, striscia dei 60 mesi, barra divisa esclusione/tassabile,
tabella a scaglioni con riga evidenziata, barre a zone (Social Security), fascia dei due anni della vedova."""
import v14eng
from v14eng import *
import v13eng as _E2
from v8b2_5 import house as _house

WF_COL = {'total': (205, 165, 60), 'minus': (200, 55, 60), 'final': (30, 140, 90)}

def _two(s):
    """etichetta su due righe: spezza vicino alla meta' sugli spazi"""
    w = s.split(' ')
    if len(w) < 2: return [s]
    best = min(range(1, len(w)), key=lambda i: abs(len(' '.join(w[:i])) - len(' '.join(w[i:]))))
    return [' '.join(w[:best]), ' '.join(w[best:])]

def draw_new15(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'househero':          # casa grande con cartello SOLD piantato davanti
        s = min((y1 - y0) / 215, (x1 - x0) / 335)
        _house(C, cx - 55 * s, cy + 10, s, c)
        px = cx + 105 * s
        d.rectangle([px - 6, cy - 5 * s, px + 6, cy + 95 * s], fill=grey + (255,))
        rr(d, [px - 62 * s, cy - 62 * s, px + 62 * s, cy - 2 * s], 12, red, white, 4)
        T(C, k.get('sold', 'SOLD'), int(38 * s), cy - 54 * s, white, x=px, maxw=110 * s)
    elif kind == 'wfbar':            # una barra della cascata; steps = [(etichetta, valore, 'total'|'minus'|'final')], i = indice, gbox = area comune
        steps = k['steps']; i = k['i']; n = len(steps); run = 0; segs = []
        for lab, val, kd in steps:
            if kd == 'minus': segs.append((run - val, run)); run -= val
            else: segs.append((0, val)); run = val
        mx = max(b for a, b in segs); gx0, gy0, gx1, gy1 = k['gbox']; base = gy1 - 100; top = gy0 + 70; sc = (base - top) / mx
        slot = (gx1 - gx0) / n; bw = slot * 0.64; a, b = segs[i]; bx = gx0 + slot * i + (slot - bw) / 2
        d.line([gx0 + slot * i + 6, base, gx0 + slot * (i + 1) - 6, base], fill=(150, 165, 190, 255), width=4)
        lab, val, kd = steps[i]
        if i > 0:
            prev_top = base - (segs[i - 1][1] if steps[i - 1][2] != 'minus' else segs[i - 1][0]) * sc
            cur_y = base - (b if kd == 'minus' else (b)) * sc
            d.line([gx0 + slot * (i - 1) + (slot + bw) / 2, prev_top, bx, prev_top], fill=(150, 165, 190, 255), width=3)
        rr(d, [bx, base - b * sc, bx + bw, base - a * sc + (0 if kd != 'minus' else 0)], 10, WF_COL[kd], white, 3)
        txt_v = ('-' if kd == 'minus' else '') + k['fmt'][i]
        T(C, txt_v, 42, base - b * sc - 56, white if kd != 'final' else goldL, x=bx + bw / 2, maxw=slot - 8)
        for j, ln in enumerate(_two(lab)): T(C, ln, 32, base + 14 + j * 38, white if kd != 'final' else goldL, x=bx + bw / 2, maxw=slot - 8)
    elif kind == 'fivebar':          # 60 mesi (5 anni) con righe evidenziate: rows = [(etichetta, [(inizio, durata)...], colore, testo a destra)]
        lw = 270; gx0 = x0 + lw; gx1 = x1 - 10; cw = (gx1 - gx0) / 60; rows = k['rows']; rh = (y1 - y0 - 110) / len(rows)
        for yr in range(5):
            xa = gx0 + cw * 12 * yr; T(C, f'YEAR {yr + 1}', 30, y0 + 2, grey, x=xa + cw * 6, maxw=cw * 12 - 6)
        for r, (lab, segs, col, note) in enumerate(rows):
            ty = y0 + 56 + r * rh; T(C, lab, 38, ty + 4, white, x=x0 + 8, anchor='l', maxw=lw - 20)
            if note: T(C, note, 27, ty + 50, col, x=x0 + 8, anchor='l', maxw=lw - 14)
            for m in range(60):
                on = any(a <= m < a + ln for a, ln in segs)
                xa = gx0 + cw * m; rr(d, [xa + 1.5, ty + 12, xa + cw - 1.5, ty + rh - 22], 4, col if on else (36, 52, 78), None)
            for yr in range(1, 5): d.line([gx0 + cw * 12 * yr, ty + 4, gx0 + cw * 12 * yr, ty + rh - 14], fill=(150, 165, 190, 255), width=3)
        d.polygon([(gx1 - 4, y1 - 44), (gx1 - 22, y1 - 8), (gx1 + 14, y1 - 8)], fill=goldL + (255,)); T(C, k.get('end', 'DAY OF THE SALE'), 32, y1 - 48, goldL, x=gx1 - 34, anchor='r')
    elif kind == 'splitbar':         # barra divisa: parts = [(etichetta, valore, colore, testo)]; sopra il totale
        parts = k['parts']; tot = sum(v for _, v, _, _ in parts); by0 = y0 + 64; by1 = y0 + 144; xx = x0
        T(C, k['head'], 42, y0 + 8, goldL, x=x0, anchor='l'); T(C, k['tot'], 46, y0 + 6, white, x=x1, anchor='r')
        for lab, v, col, tx in parts:
            w = (x1 - x0) * v / tot; rr(d, [xx, by0, xx + w, by1], 20, col, white, 3)
            T(C, tx, 50, by1 + 14, col if col != gold else goldL, x=xx + w / 2, maxw=max(w, 360)); T(C, lab, 36, by1 + 74, white, x=xx + w / 2, maxw=max(w, 360)); xx += w
    elif kind == 'rowhl':            # evidenzia una riga di una tabella 'grid' (stessa geometria): gbox, nrows, i
        gx0, gy0, gx1, gy1 = k['gbox']; rh = (gy1 - gy0) / (k['nrows'] + 1); ry = gy0 + rh * (k['i'] + 1)
        rr(d, [gx0 + 8, ry + 4, gx1 - 8, ry + rh - 4], 14, None, goldL, 8)
        if k.get('label'): T(C, k['label'], 36, ry + rh - 4 + 10, goldL, x=gx1 - 20, anchor='r')
    elif kind == 'zonebar':          # barra a zone: verde fino a t1, oro fino a t2, rosso oltre; scala 0..mx (t2 == t1: solo verde e rosso)
        mx = k.get('mx', 60000); t1, t2 = k['t1'], k['t2']; lx0 = x0 + 230; lx1 = x1 - 10; by0 = y0 + 12; by1 = y0 + 92
        def X(v): return lx0 + (lx1 - lx0) * min(v, mx) / mx
        T(C, k['label'], 44, by0 + 14, white, x=x0 + 4, anchor='l', maxw=210)
        rr(d, [X(0), by0, X(t1), by1], 12, green, white, 2)
        if t2 > t1:
            rr(d, [X(t1), by0, X(t2), by1], 6, gold, white, 2); T(C, k.get('z2', '50%'), 34, by0 + 20, navy, x=(X(t1) + X(t2)) / 2, maxw=X(t2) - X(t1) - 8)
        rr(d, [X(t2), by0, X(mx), by1], 12, red, white, 2)
        T(C, k.get('z1', '0%'), 34, by0 + 20, white, x=(X(0) + X(t1)) / 2, maxw=X(t1) - X(0) - 10)
        T(C, k.get('z3', '85%'), 34, by0 + 20, white, x=(X(t2) + X(mx)) / 2, maxw=X(mx) - X(t2) - 10)
        T(C, k['l1'], 36, by1 + 8, goldL, x=X(t1))
        if t2 > t1 and k.get('l2'): T(C, k['l2'], 36, by1 + 8, goldL, x=X(t2))
    elif kind == 'rates':            # scalini delle aliquote: rate, sub, colore; hi = indice evidenziato
        steps = k['steps']; n = len(steps); gap = 40; bw = (x1 - x0 - gap * (n - 1)) / n; base = y1 - 10
        for i, (rate, sub, col) in enumerate(steps):
            hh = (y1 - y0 - 10) * (0.55 + 0.225 * i); hl = (i == k.get('hi', -1)); bx = x0 + i * (bw + gap)
            rr(d, [bx, base - hh, bx + bw, base], 22, (60, 52, 20) if hl else card, goldL if hl else col, 9 if hl else 6)
            T(C, rate, 96, base - hh + 20, goldL if hl else white, x=bx + bw / 2, maxw=bw - 30); T(C, sub, 40, base - hh + 140, goldL if hl else grey, x=bx + bw / 2, maxw=bw - 30)
    elif kind == 'wband':            # fascia: da un evento a +2 anni (verde) e oltre (rosso)
        bx0, bx1 = x0 + 10, x1 - 10; mid = bx0 + (bx1 - bx0) * 0.5; by0 = y0 + 140; by1 = y0 + 300
        rr(d, [bx0, by0, mid, by1], 20, green, white, 3); rr(d, [mid, by0, bx1, by1], 20, red, white, 3)
        T(C, k['a1'], 56, by0 + 26, white, x=(bx0 + mid) / 2, maxw=mid - bx0 - 30); T(C, k['a2'], 36, by0 + 82, white, x=(bx0 + mid) / 2, maxw=mid - bx0 - 30)
        T(C, k['b1'], 56, by0 + 26, white, x=(mid + bx1) / 2, maxw=bx1 - mid - 30); T(C, k['b2'], 36, by0 + 82, white, x=(mid + bx1) / 2, maxw=bx1 - mid - 30)
        for xx, lab in ((bx0 + 4, k['m0']), (mid, k['m1'])):
            d.line([xx, by0 - 50, xx, by1 + 14], fill=goldL + (255,), width=7); d.ellipse([xx - 15, by0 - 66, xx + 15, by0 - 36], fill=goldL + (255,), outline=white + (255,), width=3)
            T(C, lab, 40, by0 - 112, goldL, x=xx if xx > bx0 + 50 else bx0 + 40, anchor='c' if xx > bx0 + 50 else 'l', maxw=520)
        T(C, k.get('foot', ''), 40, by1 + 44, goldL, x=cx, maxw=x1 - x0)
    else: _prev(C, e)

_prev = _E2.draw_new
_E2.draw_new = draw_new15
PULSE_KINDS.update({'rates', 'househero', 'wfbar', 'fivebar', 'splitbar', 'zonebar', 'wband'})
