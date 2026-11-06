"""Motore slide video 14 (Medigap). Motore v14 (-> v13, modello unico) + elementi nuovi: tessere dei piani A-N con il G evidenziato,
freccia a senso unico (si puo' andare, non tornare), sei mesi della finestra, pannelli del prezzo con mini grafico (stesso per tutti / per eta' / cresce)."""
import v14eng
from v14eng import *
import v13eng as _E2

def draw_new_med(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'plans':      # tessere A B C D F G K L M N
        L = k['letters']; n = len(L); gap = 14; w = (x1 - x0 - gap * (n - 1)) / n; hh = y1 - y0 - (70 if k.get('cap') else 0); y1c = y1; y1 = y0 + hh
        for i, ch in enumerate(L):
            bx = x0 + i * (w + gap); hi = (ch == k.get('hi'))
            rr(d, [bx, y0 + (0 if hi else 30), bx + w, y1], 18, (card if not hi else (120, 98, 30)), goldL if hi else (110, 130, 160), 7 if hi else 3)
            T(C, ch, 96 if hi else 70, y0 + (hh * 0.22 if hi else hh * 0.3), goldL if hi else white, x=bx + w / 2, maxw=w - 10)
        if k.get('cap'): T(C, k['cap'], 38, y1 + 22, goldL, x=cx, maxw=x1 - x0)
    elif kind == 'oneway':   # due nodi: freccia avanti verde, indietro rossa barrata
        w = (x1 - x0) * 0.30; ax0, ax1 = x0 + w + 40, x1 - w - 40
        for bx, lab, sub, cc in [(x0, k['l1'], k.get('s1', ''), k.get('c1', blue)), (x1 - w, k['l2'], k.get('s2', ''), k.get('c2', gold))]:
            rr(d, [bx, y0, bx + w, y1], 30, card, cc, 7); T(C, lab, 54, cy - 60, white, x=bx + w / 2, maxw=w - 30)
            if sub: T(C, sub, 36, cy + 10, goldL, x=bx + w / 2, maxw=w - 30)
        ay = y0 + (y1 - y0) * 0.28; arrow_h(d, ax0, ax1, ay, green, 12); T(C, k['fwd'], 40, ay - 74, green, x=(ax0 + ax1) / 2, maxw=ax1 - ax0 + 60)
        by = y0 + (y1 - y0) * 0.72; d.line([ax1, by, ax0 + 30, by], fill=red + (255,), width=12); d.polygon([(ax0, by), (ax0 + 36, by - 24), (ax0 + 36, by + 24)], fill=red + (255,))
        cross(C, (ax0 + ax1) / 2, by, 44, red); T(C, k['back'], 40, by + 62, red, x=(ax0 + ax1) / 2, maxw=ax1 - ax0 + 120)
    elif kind == 'sixm':     # sei mesi in fila
        n = 6; gap = 16; w = (x1 - x0 - gap * (n - 1)) / n; hh = min(y1 - y0 - 120, 190)
        for i in range(n):
            bx = x0 + i * (w + gap); rr(d, [bx, y0, bx + w, y0 + hh], 18, (120, 98, 30), goldL, 5)
            T(C, 'MONTH', 32, y0 + 26, white, x=bx + w / 2, maxw=w - 10); T(C, str(i + 1), 84, y0 + hh * 0.38, goldL, x=bx + w / 2)
        d.line([x0, y0 + hh + 24, x0, y0 + hh + 46, x1, y0 + hh + 46, x1, y0 + hh + 24], fill=goldL + (255,), width=7, joint='curve')
        T(C, k['label'], 44, y0 + hh + 66, goldL, x=cx, maxw=x1 - x0)
    elif kind == 'idcard':   # tessera della polizza: intestazione, lettera del piano, banda
        rr(d, [x0, y0, x1, y1], 30, (236, 240, 245), c, 7); rr(d, [x0, y0, x1, y0 + 96], 30, navy); d.rectangle([x0, y0 + 56, x1, y0 + 96], fill=navy + (255,))
        T(C, 'MEDICARE SUPPLEMENT INSURANCE', 34, y0 + 30, goldL, x=cx, maxw=x1 - x0 - 40)
        d.ellipse([x0 + 40, y0 + 150, x0 + 40 + 190, y0 + 150 + 190], fill=gold + (255,), outline=navy + (255,), width=8); T(C, k['plan'], 150, y0 + 170, navy, x=x0 + 135)
        T(C, 'PLAN ' + k['plan'], 84, y0 + 168, navy, x=x0 + 260, anchor='l', maxw=x1 - x0 - 300); T(C, 'MEDIGAP POLICY', 40, y0 + 270, (60, 72, 92), x=x0 + 260, anchor='l', maxw=x1 - x0 - 300)
        d.rectangle([x0, y1 - 120, x1, y1 - 50], fill=(40, 48, 66, 255))
    elif kind == 'agecol':   # pannello prezzo: titolo, mini grafico, spiegazione
        rr(d, [x0, y0, x1, y1], 28, card, c, 6); rr(d, [x0, y0, x1, y0 + 84], 28, c); d.rectangle([x0, y0 + 50, x1, y0 + 84], fill=c + (255,))
        T(C, k['title'], 36, y0 + 22, navy, x=cx, maxw=x1 - x0 - 24)
        gx0, gx1, gy0, gy1 = x0 + 44, x1 - 44, y0 + 120, y0 + (y1 - y0) * 0.58
        d.line([gx0, gy0, gx0, gy1], fill=(150, 165, 190, 255), width=4); d.line([gx0, gy1, gx1, gy1], fill=(150, 165, 190, 255), width=4)
        m = k['mode']; pts = {'flat': [(gx0, gy0 + (gy1 - gy0) * 0.45), (gx1, gy0 + (gy1 - gy0) * 0.45)], 'low': [(gx0, gy0 + (gy1 - gy0) * 0.65), (gx1, gy0 + (gy1 - gy0) * 0.65)],
                                'rise': [(gx0, gy0 + (gy1 - gy0) * 0.8), (gx1, gy0 + (gy1 - gy0) * 0.1)]}[m]
        d.line(pts, fill=(red if m == 'rise' else green) + (255,), width=10); 
        T(C, 'AGE', 28, gy1 + 6, grey, x=gx1, anchor='r'); T(C, 'PRICE', 28, gy0 - 8, grey, x=gx0 + 10, anchor='l')
        T(C, k['line1'], 40, y1 - 132, white, x=cx, maxw=x1 - x0 - 24); T(C, k['line2'], 34, y1 - 76, goldL, x=cx, maxw=x1 - x0 - 24)
    else: _orig_med(C, e)

_orig_med = _E2.draw_new
_E2.draw_new = draw_new_med
PULSE_KINDS.update({'idcard', 'plans', 'oneway', 'sixm', 'agecol'})
