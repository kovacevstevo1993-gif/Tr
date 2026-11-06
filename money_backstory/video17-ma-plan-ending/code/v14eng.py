"""Motore slide video 14 (earnings test). Parte dal motore v13 (modello unico) e aggiunge elementi nuovi:
calendario dei mesi con mesi che cambiano stato (trattenuto / pagato), linea dell'anno con zone e marcatore, barre mensili con la linea del limite,
etichette con spunta o croce, bilancia limite/guadagno (gauge), pannello 'prima/dopo' e catene di calcolo."""
import v13eng
from v13eng import *
import v13eng as _E

MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
HELD = (200, 55, 60); PAID = (30, 140, 90)

def mgeo(gb, i, ncols=6, nrows=2, gap=16, hmax=None):
    x0, y0, x1, y1 = gb; w = (x1 - x0 - gap * (ncols - 1)) / ncols; h = (y1 - y0 - gap * (nrows - 1)) / nrows
    if hmax: h = min(h, hmax)
    r, c = divmod(i, ncols); return (x0 + c * (w + gap), y0 + r * (h + gap), x0 + c * (w + gap) + w, y0 + r * (h + gap) + h)
def bbox(boxes): return (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))

def draw_tile(C, b, i, status, amt=None, sub=None, small=False):
    d = ImageDraw.Draw(C); x0, y0, x1, y1 = b; cx = (x0 + x1) / 2; h = y1 - y0
    fill, out = {None: (card, (110, 130, 160)), 'held': (HELD, white), 'paid': (PAID, white), 'gold': ((120, 98, 30), goldL), 'free': (PAID, white)}[status]
    rr(d, [x0, y0, x1, y1], 18, fill, out, 4)
    fs = 34 if small else 40
    T(C, MONTHS[i], fs, y0 + 12, white if status else grey, x=cx, maxw=x1 - x0 - 14)
    if status == 'held' and not small:
        cross(C, cx, y0 + h * 0.60, min(30, h * 0.15), white); 
        if amt: T(C, amt, 40, y1 - 62, white, x=cx, maxw=x1 - x0 - 14)
    elif status == 'paid' and not small:
        check(C, cx, y0 + h * 0.60, min(34, h * 0.17), white)
        if amt: T(C, amt, 40, y1 - 62, white, x=cx, maxw=x1 - x0 - 14)
    elif amt and not small: T(C, amt, 40, y0 + h * 0.5, white, x=cx, maxw=x1 - x0 - 14)
    if sub: T(C, sub, 28, y1 - 40, white, x=cx, maxw=x1 - x0 - 10)

def draw_new14(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'mgrid':     # calendario: tessere dei mesi neutre
        nc, nr = k.get('ncols', 6), k.get('nrows', 2)
        for i in range(12): draw_tile(C, mgeo(k['gbox'], i, nc, nr, hmax=k.get('hmax')), i, None, small=k.get('small', False))
    elif kind == 'mtile':   # mesi che cambiano stato (idx = elenco), ognuno con la sua importo
        nc, nr = k.get('ncols', 6), k.get('nrows', 2)
        for i in k['idx']: draw_tile(C, mgeo(k['gbox'], i, nc, nr, hmax=k.get('hmax')), i, k['status'], k.get('amt'), k.get('sub'), k.get('small', False))
    elif kind == 'ymark':   # bandierina su un mese della linea dell'anno
        nc, nr = k.get('ncols', 12), k.get('nrows', 1); b = mgeo(k['gbox'], k['i'], nc, nr, hmax=k.get('hmax')); mx = (b[0] + b[2]) / 2
        d.line([mx, y0 + 70, mx, b[1]], fill=goldL + (255,), width=7)
        rr(d, [x0, y0, x1, y0 + 70], 18, gold, white, 3); T(C, k['label'], 38, y0 + 14, navy, x=(x0 + x1) / 2, maxw=x1 - x0 - 20)
    elif kind == 'ybrace':  # parentesi sotto una zona con etichetta
        d.line([x0, y0 + 8, x0, y0 + 30, x1, y0 + 30, x1, y0 + 8], fill=c + (255,), width=7, joint='curve')
        T(C, k['label'], k.get('size', 42), y0 + 44, c, x=cx, maxw=max(x1 - x0, 520)); 
        if k.get('sub'): T(C, k['sub'], 34, y0 + 100, white, x=cx, maxw=max(x1 - x0, 520))
    elif kind == 'mbars':   # barre mensili: asse, linea del limite
        gb = k['gbox']; gx0, gy0, gx1, gy1 = gb; base = gy1 - 56; top = gy0 + 20; ly = base - (base - top) * k.get('limit_h', 0.22)
        d.line([gx0, base, gx1, base], fill=(150, 165, 190, 255), width=5)
        d.line([gx0, ly, gx1, ly], fill=goldL + (255,), width=6)
        for i in range(12):
            b = mgeo((gx0, gy0, gx1, gy1), i, 12, 1); T(C, MONTHS[i], 28, base + 10, white, x=(b[0] + b[2]) / 2, maxw=b[2] - b[0] - 2)
        T(C, k['limit_label'], 36, ly - 46, goldL, x=gx0 + 8, anchor='l')
    elif kind == 'mbar':    # barre di alcuni mesi (idx) con altezza relativa
        gx0, gy0, gx1, gy1 = k['gbox']; base = gy1 - 56; top = gy0 + 20
        for j, i in enumerate(k['idx']):
            b = mgeo((gx0, gy0, gx1, gy1), i, 12, 1); bw = (b[2] - b[0]) * 0.66; mx = (b[0] + b[2]) / 2; hh = (base - top) * (k['h'][j] if isinstance(k['h'], list) else k['h'])
            col = k.get('col', red)
            rr(d, [mx - bw / 2, base - max(hh, 8), mx + bw / 2, base], 10, col, white, 3)
            if k.get('lab'): T(C, k['lab'], 32, base - max(hh, 8) - 46, white, x=mx, maxw=(b[2] - b[0]) + 20)
    elif kind == 'chip':    # etichetta con spunta o croce
        rr(d, [x0, y0, x1, y1], 22, card, k.get('ic', red), 5)
        (check if k.get('good') else cross)(C, x0 + 56, cy, 24, green if k.get('good') else red)
        T(C, k['t'], k.get('size', 42), cy - k.get('size', 42) * 0.58, white, x=x0 + 104, anchor='l', maxw=x1 - x0 - 120)
    elif kind == 'vs':      # due colonne a confronto con testata colorata
        w = (x1 - x0 - 40) / 2
        for j, (hd, big, sub, cc) in enumerate(k['cols']):
            bx = x0 + j * (w + 40); rr(d, [bx, y0, bx + w, y1], 28, card, cc, 6); rr(d, [bx, y0, bx + w, y0 + 84], 28, cc); d.rectangle([bx, y0 + 50, bx + w, y0 + 84], fill=cc + (255,))
            T(C, hd, 38, y0 + 20, navy, x=bx + w / 2, maxw=w - 30); T(C, big, k.get('size', 110), y0 + 120, white, x=bx + w / 2, maxw=w - 30); T(C, sub, 40, y1 - 90, cc if cc != gold else goldL, x=bx + w / 2, maxw=w - 30)
    elif kind == 'calc':    # catena di calcolo su una riga, ogni pezzo con colore proprio: parts = [(testo, colore, size)]
        n = len(k['parts']); xs = [x0 + (x1 - x0) * (i + 0.5) / n for i in range(n)]
        rr(d, [x0, y0, x1, y1], 26, card, c, 5)
        for xx, (t_, col, sz) in zip(xs, k['parts']): T(C, t_, sz, cy - sz * 0.6, col, x=xx, maxw=(x1 - x0) / n - 14)
    else: _orig_new(C, e)

_orig_new = _E.draw_new
_E.draw_new = draw_new14
PULSE_KINDS.update({'mgrid', 'mtile', 'chip', 'vs', 'calc', 'mbar'})
