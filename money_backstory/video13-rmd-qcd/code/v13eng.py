"""Motore slide video 13 (copia del 12 + curva dei fattori RMD, marcatori sulla curva, flusso a nodi con freccia barrata, colonna di barre con valori). Motore video 12 (copia del motore 11 + elementi: modulo Schedule 1-A, pila di deduzioni, grafico fase-out, scala delle aliquote, bilancia)
(ex video 11: (copia del motore del video 10 + elementi nuovi: conto, barra copertura, albero beneficiari, scudo, linea del tempo, tabella, indicatore soglia, etichette REGOLA e FONTE) (modello unico: stessa cornice, sfondo, titolo, pillola all'80%), layout diversi per ogni slide.
Ogni slide = titolo + elementi (cue = parola detta dalla voce) + pillola finale. Elementi fermi dall'80%, sfondo sempre vivo."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); MB = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(MB, 'video8-bills-after-65/code'))
import v8b1
from v8b1 import *
from v8b2_5 import initials, house
from v4b2_10 import cal_card
from v5lib import paycheck
from sync_voce import Voice
VID = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = Voice(os.path.join(VID, 'sync.json')); v8b1.V = V

# ---------- layout: box (x0, y0, x1, y1) dentro l'area utile 120..1800 x 230..720 ----------
def row(n, y0=250, y1=700, x0=130, x1=1790, gap=50):
    w = (x1 - x0 - gap * (n - 1)) / n
    return [(x0 + k * (w + gap), y0, x0 + k * (w + gap) + w, y1) for k in range(n)]
def col(n, x0=1000, x1=1790, y0=240, y1=710, gap=26):
    h = (y1 - y0 - gap * (n - 1)) / n
    return [(x0, y0 + k * (h + gap), x1, y0 + k * (h + gap) + h) for k in range(n)]
LEFT = (130, 250, 880, 700)

# ---------- elementi ----------
def ic(C, name, cx, cy, s=1.0, c=gold):
    if name == 'check': check(C, cx, cy, 52 * s, green)
    elif name == 'cross': cross(C, cx, cy, 52 * s, red)
    elif name == 'lock': padlock(C, cx, cy, 0.9 * s, red)
    elif name == 'brief': briefcase(C, cx, cy, 1.3 * s)
    elif name == 'bank': bank_ic(C, cx, cy, s, c)
    elif name == 'coins': coin_stack(C, cx - 40 * s, cy + 60 * s, 5, int(46 * s))
    elif name == 'bill': bill(C, cx, cy, int(230 * s), int(112 * s), 0, 255)
    elif name == 'phone': phone(C, cx, cy, 1.2 * s, 255, 0.0, False)
    elif name == 'clock': clock(C, cx, cy, int(80 * s), 0.0)
    elif name == 'bag': money_bag(C, cx, cy, 1.2 * s)
    elif name == 'house': house(C, cx, cy, 1.0 * s)
    elif name == 'wallet': wallet(C, cx, cy, 1.4 * s)
    elif name == 'bulb': bulb(C, cx, cy, 1.2 * s)
    elif name == 'form': tax_form(C, cx - 90 * s, cy - 110 * s, 180 * s, 220 * s, 255, 'TAX')
    elif name == 'mail':
        d = ImageDraw.Draw(C); w, h = 200 * s, 130 * s
        d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=12, fill=(236, 240, 245, 255), outline=c + (255,), width=5)
        d.line([cx - w / 2, cy - h / 2, cx, cy + 10 * s, cx + w / 2, cy - h / 2], fill=c + (255,), width=6)
    elif name == 'chart':
        d = ImageDraw.Draw(C)
        for k, hh in enumerate([60, 95, 80, 130]):
            d.rounded_rectangle([cx - 110 * s + k * 58 * s, cy + 70 * s - hh * s, cx - 70 * s + k * 58 * s, cy + 70 * s], radius=6, fill=(green if k == 3 else c) + (255,))
    elif name == 'doc':
        d = ImageDraw.Draw(C); w, h = 170 * s, 220 * s
        d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=12, fill=(236, 240, 245, 255), outline=c + (255,), width=5)
        for k in range(4): d.rectangle([cx - w * 0.36, cy - h * 0.28 + k * h * 0.17, cx + w * 0.36 - (k % 2) * 30 * s, cy - h * 0.22 + k * h * 0.17], fill=(170, 180, 200, 255))

def E(kind, box, cue=None, **k):
    x0, y0, x1, y1 = box; box = (max(x0, 150), y0, min(x1, 1770), y1)   # margine: l'animazione di comparsa non tocca la cornice
    return dict(kind=kind, box=box, cue=cue, k=k)
def el_times(els):
    lim = LASTP() - 0.3; n = len(els); times = []
    for i, e in enumerate(els):
        mx = lim - 0.3 * (n - 1 - i)
        tc = 0.25 if (i == 0 and e['cue'] is None) else (tm(e['cue'], mx) if e['cue'] else (times[-1] + 0.35 if times else 0.35))
        if i == 0: tc = min(tc, 0.25)
        if times: tc = max(tc, times[-1] + 0.3)
        times.append(min(tc, mx))
    return times

def draw_el(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']
    c = k.get('col', gold)
    if kind == 'card':
        card_(C, x0, y0, x1, y1, c, k.get('head'), k.get('val'), k.get('sub'), k.get('vsize', 96), k.get('vcol', white))
        if k.get('icon'): ic(C, k['icon'], cx, y0 + (y1 - y0) * 0.62, k.get('s', 0.8), c)
    elif kind == 'icard':   # card con icona in alto, testo sotto
        d = ImageDraw.Draw(C); d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=card + (255,), outline=c + (255,), width=6)
        sz = k.get('size', 50); sc = k.get('s', 1.0) * (0.75 if k['icon'] in ('form', 'phone', 'doc') else 1.0)
        ytxt = y1 - 86 - sz - 16 if k.get('l2') else y1 - 40 - sz
        ic(C, k['icon'], cx, y0 + (ytxt - y0) * 0.5, sc, c)
        txt(C, k['l1'], fit(k['l1'], x1 - x0 - 40, sz), ytxt, white, 255, x=cx)
        if k.get('l2'): txt(C, k['l2'], fit(k['l2'], x1 - x0 - 40, 42), y1 - 86, k.get('c2', goldL), 255, x=cx)
    elif kind == 'pay': paycheck(C, x0, y0, x1, y1, c, k['amount'], k.get('sub', 'PER MONTH'), k.get('head', 'MONTHLY CHECK'), k.get('size', 120))
    elif kind == 'cal':
        cal_card(C, x0, y0, x1, y1, k['head'], k['big'], k.get('size', 110), c)
        if k.get('sub'): txt(C, k['sub'], fit(k['sub'], x1 - x0 - 40, 50), y1 - 90, navy, 255, x=cx)
    elif kind == 'ring':
        r = min(x1 - x0, y1 - y0) / 2 - 30; ring_(C, cx, cy, r, k.get('frac', 1.0), c, 36)
        vs = k.get('size', 96); txt(C, k['val'], fit(k['val'], r * 1.5, vs), cy - vs * 0.8, goldL, 255, x=cx)
        if k.get('sub'): txt(C, k['sub'], fit(k['sub'], r * 1.3, 40), cy + vs * 0.35, white, 255, x=cx)
    elif kind == 'person':
        d = ImageDraw.Draw(C); d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=card + (255,), outline=c + (255,), width=6)
        initials(C, cx, y0 + 95, k['letter'], 62, c); txt(C, k['name'], fit(k['name'], x1 - x0 - 40, 56), y0 + 175, white, 255, x=cx)
        if k.get('line'): txt(C, k['line'], fit(k['line'], x1 - x0 - 40, 46), y0 + 250, goldL, 255, x=cx)
        if k.get('line2'): txt(C, k['line2'], fit(k['line2'], x1 - x0 - 40, 40), y0 + 315, grey, 255, x=cx)
    elif kind == 'step':    # riga numerata (lista)
        d = ImageDraw.Draw(C); d.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=card + (255,), outline=c + (255,), width=5)
        h = y1 - y0; d.ellipse([x0 + 18, y0 + h / 2 - 38, x0 + 94, y0 + h / 2 + 38], fill=c + (255,)); txt(C, str(k['n']), BOLD(48), y0 + h / 2 - 30, navy, 255, x=x0 + 56)
        txt(C, k['text'], fit(k['text'], x1 - x0 - (330 if k.get('val') else 150), 44), y0 + h / 2 - 26, white, 255, x=x0 + 120, anchor='l')
        if k.get('val'): txt(C, k['val'], fit(k['val'], 300, 50), y0 + h / 2 - 30, k.get('vc', goldL), 255, x=x1 - 30, anchor='r')
    elif kind == 'bars':    # due barre prima/dopo
        d = ImageDraw.Draw(C); base_y = y1 - 60; mh = y1 - y0 - 170; vals = k['vals']; mx = max(v for _, v, _ in vals)
        bw = (x1 - x0) / (len(vals) * 2)
        for i, (lab, v, txtv) in enumerate(vals):
            bx = x0 + bw / 2 + i * 2 * bw; hh = mh * (k.get('lo', 0.55) + (1 - k.get('lo', 0.55)) * v / mx) if k.get('lo') is not None else mh * v / mx
            cc = green if i == len(vals) - 1 else (110, 130, 160)
            d.rounded_rectangle([bx, base_y - hh, bx + bw, base_y], radius=14, fill=cc + (255,), outline=white + (255,), width=3)
            txt(C, txtv, fit(txtv, bw * 1.8, 54), base_y - hh - 70, goldL if i == len(vals) - 1 else white, 255, x=bx + bw / 2)
            txt(C, lab, fit(lab, bw * 1.8, 36), base_y + 12, white, 255, x=bx + bw / 2)
    elif kind == 'big':     # numero gigante con didascalia
        txt(C, k['val'], fit(k['val'], x1 - x0, k.get('size', 170)), cy - k.get('size', 170) * 0.62, k.get('vcol', goldL), 255, x=cx)
        if k.get('sub'): txt(C, k['sub'], fit(k['sub'], x1 - x0, 48), cy + k.get('size', 170) * 0.5, white, 255, x=cx)
    elif kind == 'op': txt(C, k['t'], BOLD(k.get('size', 110)), cy - k.get('size', 110) * 0.62, k.get('col', goldL), 255, x=cx)
    elif kind == 'arrow': arrow_r(C, x0, x1, cy, k.get('col', goldL), 255)
    elif kind == 'stamp': pass
    elif kind == 'line': txt(C, k['t'], fit(k['t'], x1 - x0, k.get('size', 50)), y0, k.get('col', white), 255, x=cx)
    else: draw_new(C, e)


import math
PULSE_KINDS = {'curve', 'flow', 'vbars', 'card', 'icard', 'person', 'step', 'rule', 'numcol', 'ring', 'cal', 'seg', 'pan', 'formrow', 'gridrow', 'form1a', 'grid', 'tline', 'big', 'line', 'phase', 'meter', 'gauge', 'pay', 'ledger', 'shield', 'scale'}
def pulse_sched(els, times, tp, step=2.4, gap_min=0.7):
    """lampi di evidenziazione sull'ultimo elemento comparso: riempiono i buchi (> step) tra un elemento e il successivo (o la pillola finale)"""
    out = []
    for i, (e, tc) in enumerate(zip(els, times)):
        nx = times[i + 1] if i + 1 < len(times) else tp
        k = 1
        while tc + step * k < nx - gap_min:
            if e['kind'] in PULSE_KINDS: out.append((e, tc + step * k))
            k += 1
    return out
def pulse_layer(fr, t, sched, dur=0.7):
    for e, tp in sched:
        if tp <= t < tp + dur:
            u = (t - tp) / dur; a = int(235 * math.sin(math.pi * u)); x0, y0, x1, y1 = e['box']
            C = new(); d = ImageDraw.Draw(C); pad = 10
            d.rounded_rectangle([x0 - pad, y0 - pad, x1 + pad, y1 + pad], radius=34, outline=goldL + (a,), width=9)
            fr = Image.alpha_composite(fr, C)
    return fr

def slide(title, seed, els, pill, pcol=gold, tcol=None, tsize=58, psize=52, tag=None, src=None):
    tcol = tcol or (navy if pcol in (gold, goldL, green) else (255, 255, 255))
    dd = ImageDraw.Draw(Image.new('RGBA', (10, 10))); half = 860
    if tag: half = min(half, 960 - (100 + dd.textlength(tag, font=BOLD(34)) + 56) - 30)
    if src: half = min(half, (1820 - dd.textlength('SOURCE: ' + src, font=BOLD(30)) - 52) - 960 - 30)
    ts = tsize
    while ts > 40 and dd.textlength(title, font=SER(ts)) > 2 * half: ts -= 2
    def fn(t):
        fr = stage_live(t, title, seed, ts); fr = badges(fr, t, tag, src)
        times = el_times(els)
        for e, tc in zip(els, times):
            if t > tc:
                C = new(); x0, y0, x1, y1 = e['box']
                if e['kind'] == 'stamp':
                    fr = stamp(fr, e['k']['t'], (x0 + x1) / 2, (y0 + y1) / 2, e['k'].get('ang', 8), e['k'].get('col', green), min(1.0, ease((t - tc) / 0.35)), e['k'].get('size', 60)); continue
                draw_el(C, e)
                pad = 40 if e['kind'] in ('arrow', 'op', 'line', 'big') else 20
                if x1 - x0 > 600: fr = POP(fr, C, (x0 - pad, y0 - pad, x1 + pad, y1 + pad), ease((t - tc) / 0.35))   # elementi larghi: comparsa senza rimbalzo (non toccano la cornice)
                else: fr = P2(fr, C, (x0 - pad, y0 - pad, x1 + pad, y1 + pad), t, tc)
        fr = pulse_layer(fr, t, pulse_sched(els, times, LASTP()))
        return frame(pill_last(fr, t, pill, PILL_Y, pcol, tcol, psize))
    f = frozen(fn); f.els = els; f.title = title; return f

# ======================= ELEMENTI NUOVI VIDEO 11 =======================
from v7b46_53 import dashed
def rr(d, b, r, fill=None, out=None, w=5): d.rounded_rectangle(b, radius=r, fill=(fill + (255,)) if fill else None, outline=(out + (255,)) if out else None, width=w)
def T(C, s, size, y, col=white, x=960, anchor='c', maxw=None): txt(C, s, fit(s, maxw, size) if maxw else BOLD(size), y, col, 255, x=x, anchor=anchor)

def badges(fr, t, tag, src):
    """etichetta della sezione in alto a sinistra (es. RULE 1 OF 5) e fonte ufficiale in alto a destra: ferme dall'inizio"""
    if not (tag or src) or t < 0.12: return fr
    C = new(); d = ImageDraw.Draw(C)
    if tag:
        f = BOLD(34); w = d.textlength(tag, font=f) + 56
        rr(d, [100, 70, 100 + w, 128], 29, gold, None); d.text((128, 99), tag, font=f, fill=navy + (255,), anchor='lm')
    if src:
        f = BOLD(30); s2 = 'SOURCE: ' + src; w = d.textlength(s2, font=f) + 52
        rr(d, [1820 - w, 72, 1820, 126], 27, card, grey, 3); d.text((1820 - w / 2, 99), s2, font=f, fill=goldL + (255,), anchor='mm')
    return A_(fr, C, (80, 55, 1840, 145), t, 0.12, 0.35)

def bank_ic(C, cx, cy, s, col):
    d = ImageDraw.Draw(C); w = 130 * s
    d.polygon([(cx - w, cy - 40 * s), (cx, cy - 110 * s), (cx + w, cy - 40 * s)], fill=col + (255,))
    d.rectangle([cx - w + 10 * s, cy - 36 * s, cx + w - 10 * s, cy - 22 * s], fill=col + (255,))
    for k in range(5): xx = cx - w + 28 * s + k * (2 * w - 56 * s) / 4; d.rectangle([xx - 11 * s, cy - 16 * s, xx + 11 * s, cy + 70 * s], fill=col + (255,))
    d.rectangle([cx - w, cy + 76 * s, cx + w, cy + 96 * s], fill=col + (255,)); txt(C, '$', BOLD(max(20, int(44 * s))), cy - 96 * s, navy, 255, x=cx)

def minibank(d, cx, cy, col):
    d.polygon([(cx - 34, cy - 10), (cx, cy - 30), (cx + 34, cy - 10)], fill=col + (255,))
    for k in range(4): d.rectangle([cx - 28 + k * 16, cy - 6, cx - 20 + k * 16, cy + 20], fill=col + (255,))
    d.rectangle([cx - 34, cy + 22, cx + 34, cy + 30], fill=col + (255,))

def shield(C, cx, cy, s, col, fill=card):
    d = ImageDraw.Draw(C); w, h = 150 * s, 180 * s
    pts = [(cx - w, cy - h * 0.75), (cx, cy - h), (cx + w, cy - h * 0.75), (cx + w, cy + h * 0.05), (cx, cy + h), (cx - w, cy + h * 0.05)]
    d.polygon(pts, fill=fill + (255,), outline=col + (255,)); d.line(pts + [pts[0]], fill=col + (255,), width=int(9 * s), joint='curve')

def draw_rows(C, box, k):
    x0, y0, x1, y1 = box; d = ImageDraw.Draw(C); rows = k['rows']; nc = len(k['head']); cw = [(x1 - x0) * w for w in k.get('w', [1 / nc] * nc)]
    rh = (y1 - y0) / (k.get('nrows', len(rows)) + 1)
    for i, r in enumerate(rows):
        i = k.get('ri', i); yy = y0 + rh * (i + 1); xx = x0
        if i: d.line([x0 + 20, yy, x1 - 20, yy], fill=(60, 82, 112, 255), width=2)
        for j, v in enumerate(r):
            mx = xx + cw[j] / 2
            if v == 'Y': check(C, mx, yy + rh / 2, min(34, rh * 0.33), green)
            elif v == 'N': cross(C, mx, yy + rh / 2, min(30, rh * 0.3), red)
            elif isinstance(v, tuple): T(C, v[0], 40, yy + rh / 2 - 25, v[1], x=mx, maxw=cw[j] - 30)
            else: T(C, v, 40, yy + rh / 2 - 25, white if j == 0 else goldL, x=(xx + 30) if j == 0 else mx, anchor='l' if j == 0 else 'c', maxw=cw[j] - 40)
            xx += cw[j]

def draw_new11(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'meter':      # barra di copertura: verde fino al limite, rosso oltre
        tot, lim = k['total'], k['limit']; by0, by1 = y0 + 110, y0 + 210; lx = x0 + (x1 - x0) * lim / tot
        T(C, k['head'], 46, y0 + 8, goldL, x=x0, anchor='l')
        T(C, k['tot_l'], 46, y0 + 8, white, x=x1, anchor='r')
        rr(d, [x0, by0, x1, by1], 22, (40, 58, 86), white, 3)
        rr(d, [x0, by0, lx, by1], 22, green); 
        if lx < x1 - 10: rr(d, [lx, by0, x1, by1], 22, red); d.rectangle([lx - 10, by0, lx + 10, by1], fill=green + (255,)); d.rectangle([lx, by0, lx + 10, by1], fill=red + (255,))
        d.line([lx, by0 - 30, lx, by1 + 30], fill=goldL + (255,), width=6)
        T(C, k['lim_l'], 36, by0 - 78, goldL, x=lx)
        T(C, k['g1'], 54, by1 + 40, green, x=(x0 + lx) / 2); T(C, k['g2'], 38, by1 + 108, white, x=(x0 + lx) / 2)
        if lx < x1 - 10 and k.get('r1'): T(C, k['r1'], 54, by1 + 40, red, x=(lx + x1) / 2); T(C, k['r2'], 38, by1 + 108, white, x=(lx + x1) / 2)
    elif kind == 'ledger':   # estratto conto: intestazione + righe
        rr(d, [x0, y0, x1, y1], 26, (236, 240, 245), c, 6); rr(d, [x0, y0, x1, y0 + 96], 26, c); d.rectangle([x0, y0 + 60, x1, y0 + 96], fill=c + (255,))
        minibank(d, x0 + 66, y0 + 48, navy); T(C, k['head'], 44, y0 + 24, navy, x=x0 + 125, anchor='l', maxw=x1 - x0 - 160)
        rows = k['rows']; rh = (y1 - y0 - 120) / len(rows)
        for i, (a, b, bc) in enumerate(rows):
            yy = y0 + 112 + i * rh
            if i: d.line([x0 + 30, yy - 4, x1 - 30, yy - 4], fill=(190, 198, 212, 255), width=2)
            T(C, a, 40, yy + rh / 2 - 26, (60, 72, 92), x=x0 + 36, anchor='l', maxw=(x1 - x0) * 0.55)
            T(C, b, 46, yy + rh / 2 - 30, {goldL: (150, 110, 40), green: (30, 140, 80), red: (200, 50, 50)}.get(bc, bc or navy), x=x1 - 36, anchor='r', maxw=(x1 - x0) * 0.4)
    elif kind == 'tree':     # proprietario -> beneficiari
        names = k['kids']; n = len(names); ow = min(420, x1 - x0); oy1 = y0 + 120
        rr(d, [cx - ow / 2, y0, cx + ow / 2, oy1], 26, card, c, 6); initials(C, cx - ow / 2 + 66, y0 + 60, k['letter'], 40, c)
        T(C, k['owner'], 48, y0 + 32, white, x=cx + 40, maxw=ow - 150)
        ky0 = y1 - 170; kw = (x1 - x0 - 40 * (n - 1)) / n; my = (oy1 + ky0) / 2
        d.line([cx, oy1, cx, my], fill=goldL + (255,), width=6)
        if n > 1: d.line([x0 + kw / 2, my, x1 - kw / 2, my], fill=goldL + (255,), width=6)
        for i, (nm, v) in enumerate(names):
            kx = x0 + i * (kw + 40); kc = kx + kw / 2
            d.line([kc, my, kc, ky0], fill=goldL + (255,), width=6)
            rr(d, [kx, ky0, kx + kw, y1], 24, card, green, 5); T(C, nm, 44, ky0 + 22, white, x=kc, maxw=kw - 30); T(C, v, 54, ky0 + 82, green, x=kc, maxw=kw - 30)
    elif kind == 'shield':
        s = min(x1 - x0, y1 - y0) / 400; shield(C, cx, cy + 10 * s, s * 1.15, c)
        T(C, k['val'], int(k.get('size', 90) * s * 1.1), cy - 100 * s, k.get('vcol', goldL), x=cx, maxw=270 * s)
        if k.get('sub'): T(C, k['sub'], int(40 * s * 1.1), cy + 20 * s, white, x=cx, maxw=230 * s)
        if k.get('sub2'): T(C, k['sub2'], int(32 * s * 1.1), cy + 78 * s, grey, x=cx, maxw=200 * s)
    elif kind == 'tline':    # linea del tempo con punti
        pts = k['pts']; n = len(pts); ay = y0 + (y1 - y0) * 0.45; d.line([x0, ay, x1, ay], fill=(120, 140, 170, 255), width=8)
        xs = [x0 + (x1 - x0) * (i + 0.5) / n for i in range(n)]
        if k.get('span'):
            a, b, lab, sc = k['span']; rr(d, [xs[a] - 30, ay - 70, xs[b] + 30, ay + 70], 34, None, sc, 6)
            T(C, lab, 44, ay - 140, sc, x=(xs[a] + xs[b]) / 2)
        for xx, (lab, sub, pc) in zip(xs, pts):
            d.ellipse([xx - 30, ay - 30, xx + 30, ay + 30], fill=pc + (255,), outline=white + (255,), width=4)
            T(C, lab, 46, ay + 90, white, x=xx, maxw=(x1 - x0) / n - 20)
            if sub: T(C, sub, 36, ay + 150, grey, x=xx, maxw=(x1 - x0) / n - 20)
    elif kind == 'grid':     # tabella: intestazione + righe con spunta/croce
        if k.get('frame_only'): k = dict(k); k['rows'] = []
        hd = k['head']; rows = k['rows']; nc = len(hd); cw = [(x1 - x0) * w for w in k.get('w', [1 / nc] * nc)]
        rh = (y1 - y0) / (k.get('nrows', len(rows)) + 1); rr(d, [x0, y0, x1, y1], 24, card, c, 5); rr(d, [x0, y0, x1, y0 + rh], 24, c); d.rectangle([x0, y0 + rh - 24, x1, y0 + rh], fill=c + (255,))
        xx = x0
        for j, h in enumerate(hd): T(C, h, 38, y0 + rh / 2 - 24, navy, x=xx + cw[j] / 2, maxw=cw[j] - 20); xx += cw[j]
        draw_rows(C, e['box'], k)
    elif kind == 'gridrow':  # una riga della tabella (stessa geometria della 'grid'), compare da sola sulla sua parola
        k2 = dict(k); k2['rows'] = [k['row']]; k2['ri'] = k['i']; draw_rows(C, k['gbox'], k2)
    elif kind == 'gauge':    # serbatoio verticale con linea di soglia
        lim, val, top = k['limit'], k['val'], k['top']; gx0, gx1 = cx - 90, cx + 90; gy0, gy1 = y0 + 20, y1 - 70
        rr(d, [gx0, gy0, gx1, gy1], 30, (40, 58, 86), white, 4)
        fy = gy1 - (gy1 - gy0) * min(val, top) / top; ly = gy1 - (gy1 - gy0) * lim / top; fc = red if val > lim else green
        rr(d, [gx0 + 8, fy, gx1 - 8, gy1 - 8], 24, fc)
        d.line([gx0 - 60, ly, gx1 + 60, ly], fill=goldL + (255,), width=7)
        T(C, k['lim_l'], 42, ly - 26, goldL, x=gx1 + 70, anchor='l'); T(C, k['label'], 44, y1 - 54, white, x=cx)
    elif kind == 'tagset':   # gruppo di etichette con croce (non assicurato)
        items = k['items']; per = k.get('per', 3); rows_ = (len(items) + per - 1) // per; th = (y1 - y0 - 20 * (rows_ - 1)) / rows_; tw = (x1 - x0 - 24 * (per - 1)) / per
        for i, it in enumerate(items):
            r_, c_ = divmod(i, per); tx0 = x0 + c_ * (tw + 24); ty0 = y0 + r_ * (th + 20)
            rr(d, [tx0, ty0, tx0 + tw, ty0 + th], 22, card, k.get('ic', red), 5); cross(C, tx0 + 52, ty0 + th / 2, 22, k.get('ic', red))
            T(C, it, 42, ty0 + th / 2 - 26, white, x=tx0 + 92, anchor='l', maxw=tw - 110)
    elif kind == 'app':      # telefono con schermata "insured?"
        s = (y1 - y0) / 470; pw, ph = 230 * s, 430 * s
        rr(d, [cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2], int(36 * s), (30, 36, 48), white, 6); rr(d, [cx - pw / 2 + 16, cy - ph / 2 + 40, cx + pw / 2 - 16, cy + ph / 2 - 40], int(18 * s), (236, 240, 245))
        T(C, k.get('l1', 'MY APP'), int(34 * s), cy - ph / 2 + 70, navy, x=cx, maxw=pw - 50); T(C, k.get('l2', '$'), int(56 * s), cy - 60 * s, navy, x=cx, maxw=pw - 50)
        rr(d, [cx - pw / 2 + 34, cy + 40 * s, cx + pw / 2 - 34, cy + 110 * s], int(30 * s), k.get('col', red)); T(C, k.get('l3', 'INSURED?'), int(30 * s), cy + 56 * s, white, x=cx, maxw=pw - 90)

    elif kind == 'rule':     # riga del riepilogo: blocco numero a sinistra, testo, valore a destra
        h = y1 - y0; rr(d, [x0, y0, x1, y1], 20, card, c, 4); rr(d, [x0, y0, x0 + h * 1.1, y1], 20, c); d.rectangle([x0 + h * 0.6, y0, x0 + h * 1.1, y1], fill=c + (255,))
        T(C, str(k['n']), int(h * 0.55), y0 + h * 0.18, navy, x=x0 + h * 0.55)
        T(C, k['text'], 42, y0 + h / 2 - 26, white, x=x0 + h * 1.1 + 34, anchor='l', maxw=(x1 - x0) * 0.58)
        T(C, k['val'], 46, y0 + h / 2 - 29, k.get('vc', goldL), x=x1 - 34, anchor='r', maxw=(x1 - x0) * 0.3)
    elif kind == 'numcol':   # colonna numerata con icona (cose da fare)
        rr(d, [x0, y0, x1, y1], 30, card, c, 6); d.ellipse([cx - 46, y0 + 18, cx + 46, y0 + 110], fill=c + (255,))
        T(C, str(k['n']), 60, y0 + 30, navy, x=cx); ic(C, k['icon'], cx, (y0 + 110 + y1 - 160) / 2, k.get('s', 0.5), c)
        T(C, k['l1'], 44, y1 - 150, white, x=cx, maxw=x1 - x0 - 40)
        if k.get('l2'): T(C, k['l2'], 40, y1 - 90, goldL, x=cx, maxw=x1 - x0 - 40)

import modello_unico as _mu
def final12(t, seed=212):
    """slide finale disclaimer del modello unico, con le stesse parole della voce del blocco 29"""
    return _final(t, seed)
def _final(t, seed):
    Dd = CUR['D']
    fr = base(t); fr = amb(fr, t, seed, 7, 55); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('Rules, amounts and ages change', white, 250), ('and differ from person to person.', white, 315), ('Always confirm with the I R S', goldL, 410),
             ('or a tax professional before you file.', goldL, 475), ('General information,', white, 570), ('not tax advice.', white, 635)]
    groups = [lines[0:2], lines[2:4], lines[4:6]]; tg = [0.3, 0.3 + (0.6 * Dd - 0.3) / 2, 0.6 * Dd]
    for g, ts in zip(groups, tg):
        if t > ts:
            C = new()
            for tx, cl, yy in g: txt(C, tx, BOLD(52), yy, cl, 255, x=650)
            fr = A_(fr, C, (140, 240, 1160, 770), t, ts)
    if t > 0.68 * Dd:
        C = new(); dashed(C, 1220, 280, 1780, 640); txt(C, 'WATCH NEXT', BOLD(56), 430, goldL, 255, x=1500); fr = A_(fr, C, (1200, 260, 1800, 660), t, 0.68 * Dd)
    if t > 0.8 * Dd - 0.4:
        C = new(); _mu.dashed_circle(C, 260, 860, 85); txt(C, 'SUBSCRIBE', BOLD(44), 835, goldL, 255, x=560); fr = A_(fr, C, (160, 760, 760, 960), t, 0.8 * Dd - 0.4)
    return frame(fr)

def GRID(box, head, w, rows, cues, first=None, col=gold):
    """tabella che si costruisce riga per riga: intestazione (cue first), poi ogni riga sulla sua parola"""
    x0, y0, x1, y1 = box; x0, x1 = max(x0, 150), min(x1, 1770); box = (x0, y0, x1, y1); rh = (y1 - y0) / (len(rows) + 1)
    out = [E('grid', box, first, head=head, w=w, rows=[], nrows=len(rows), col=col)]
    for i, (r, cu) in enumerate(zip(rows, cues)):
        out.append(E('gridrow', (x0, y0 + rh * (i + 1), x1, y0 + rh * (i + 2)), cu, gbox=box, head=head, w=w, row=r, i=i, nrows=len(rows)))
    return out


# ======================= ELEMENTI NUOVI VIDEO 12 =======================
def phase_xy(box, inc, val, lo=50000, hi=200000):
    x0, y0, x1, y1 = box; px0, px1 = x0 + 190, x1 - 40; py0, py1 = y0 + 70, y1 - 90
    return px0 + (px1 - px0) * (min(max(inc, lo), hi) - lo) / (hi - lo), py1 - (py1 - py0) * val / 6000.0

def draw_new12(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'form1a':      # modulo (carta chiara) con intestazione
        rr(d, [x0, y0, x1, y1], 22, (240, 243, 248), c, 6); rr(d, [x0, y0, x1, y0 + 78], 22, navy); d.rectangle([x0, y0 + 40, x1, y0 + 78], fill=navy + (255,))
        T(C, k['head'], 40, y0 + 18, goldL, x=x0 + 30, anchor='l', maxw=(x1 - x0) * 0.62); T(C, k.get('right', 'FORM 1040'), 34, y0 + 22, white, x=x1 - 28, anchor='r', maxw=(x1 - x0) * 0.3)
        d.line([x0 + 20, y0 + 78 + 6, x1 - 20, y0 + 78 + 6], fill=(170, 180, 200, 255), width=2)
    elif kind == 'formrow':   # riga del modulo: numero, testo, importo
        h = y1 - y0; hl = k.get('hl')
        if hl: rr(d, [x0 + 8, y0 + 2, x1 - 8, y1 - 2], 12, (255, 244, 205), c, 4)
        rr(d, [x0 + 22, y0 + h * 0.18, x0 + 22 + 74, y1 - h * 0.18], 8, None, (120, 130, 150), 3); T(C, k['no'], int(h * 0.42), y0 + h * 0.24, (60, 72, 92), x=x0 + 22 + 37)
        T(C, k['text'], int(h * 0.38), y0 + h * 0.27, (30, 40, 60), x=x0 + 120, anchor='l', maxw=(x1 - x0) * 0.62)
        T(C, k['val'], int(h * 0.44), y0 + h * 0.22, k.get('vc', (30, 120, 70)), x=x1 - 34, anchor='r', maxw=(x1 - x0) * 0.2)
    elif kind == 'seg':       # blocco pieno (pila): etichetta a sinistra, importo a destra
        rr(d, [x0, y0, x1, y1], 18, k.get('fill', c), white, 3); h = y1 - y0
        T(C, k['label'], min(46, int(h * 0.5)), y0 + h / 2 - min(46, int(h * 0.5)) * 0.58, k.get('tc', navy), x=x0 + 28, anchor='l', maxw=(x1 - x0) * 0.62)
        T(C, k['val'], min(50, int(h * 0.55)), y0 + h / 2 - min(50, int(h * 0.55)) * 0.58, k.get('tc', navy), x=x1 - 28, anchor='r', maxw=(x1 - x0) * 0.34)
    elif kind == 'phase':     # grafico: deduzione in funzione del reddito
        px0, py0 = phase_xy(e['box'], 50000, 6000); px1, py1 = phase_xy(e['box'], 200000, 0); xa, _ = phase_xy(e['box'], k.get('start', 75000), 6000); xb, _ = phase_xy(e['box'], k.get('end', 175000), 0)
        d.line([px0, py0 - 20, px0, py1 + 8], fill=(150, 165, 190, 255), width=5); d.line([px0 - 8, py1, px1 + 10, py1], fill=(150, 165, 190, 255), width=5)
        poly = [(px0, py0), (xa, py0), (xb, py1), (px0, py1)]; d.polygon(poly, fill=(46, 160, 100, 70))
        d.line([(px0, py0), (xa, py0), (xb, py1), (px1, py1)], fill=c + (255,), width=11, joint='curve')
        T(C, '$6,000', 42, py0 - 22, goldL, x=px0 - 14, anchor='r'); T(C, '$0', 42, py1 - 22, white, x=px0 - 14, anchor='r')
        T(C, k.get('a_l', '$75,000'), 40, py1 + 22, goldL, x=xa); T(C, k.get('b_l', '$175,000'), 40, py1 + 22, red, x=xb)
        d.line([xa, py0, xa, py1], fill=goldL + (120,), width=3); d.line([xb, py1 - 140, xb, py1], fill=red + (160,), width=3)
        T(C, k.get('top', 'YOUR INCOME  >'), 34, y0 + 4, grey, x=px1, anchor='r')
    elif kind == 'pmark':     # marcatore sul grafico
        pgx, pgy = phase_xy(k['gbox'], k['inc'], k['val']); mc = k.get('mc', goldL)
        d.line([pgx, pgy, pgx, phase_xy(k['gbox'], k['inc'], 0)[1]], fill=mc + (255,), width=5)
        d.ellipse([pgx - 22, pgy - 22, pgx + 22, pgy + 22], fill=mc + (255,), outline=white + (255,), width=5)
        T(C, k['label'], 40, pgy - 100 if k.get('up', True) else pgy + 36, white, x=pgx + k.get('dx', 0), maxw=300); T(C, k['sub'], 44, pgy - 58 if k.get('up', True) else pgy + 76, mc, x=pgx + k.get('dx', 0), maxw=300)
    elif kind == 'ladder':    # scala delle aliquote 10 / 12 / 22
        steps = k['steps']; n = len(steps); bw = (x1 - x0 - 30 * (n - 1)) / n; base = y1 - 20
        for i, (rate, sub, col) in enumerate(steps):
            hh = (y1 - y0 - 150) * (0.34 + 0.33 * i); bx = x0 + i * (bw + 30); hl = (i == k.get('hi', -1))
            rr(d, [bx, base - hh, bx + bw, base], 20, (card if not hl else (60, 52, 20)), col if not hl else goldL, 6 if not hl else 9)
            T(C, rate, 78, base - hh + 18, goldL if hl else white, x=bx + bw / 2, maxw=bw - 30); T(C, sub, 34, base - hh + 112, grey, x=bx + bw / 2, maxw=bw - 24)
            if hl and k.get('save'): T(C, k['save'], 52, base - hh - 70, green, x=bx + bw / 2, maxw=bw + 80)
    elif kind == 'scale':     # bilancia: trave, base e due appendini (i piatti sono elementi 'pan')
        d.line([cx, y0 + 40, cx, y1 - 20], fill=grey + (255,), width=10); d.polygon([(cx - 90, y1 - 20), (cx + 90, y1 - 20), (cx, y1 - 90)], fill=grey + (255,))
        d.line([x0 + 160, y0 + 90, x1 - 160, y0 + 90], fill=goldL + (255,), width=10)
        for xx in k['xs']:
            d.line([xx, y0 + 90, xx - 120, y0 + 190], fill=grey + (255,), width=5); d.line([xx, y0 + 90, xx + 120, y0 + 190], fill=grey + (255,), width=5)
    elif kind == 'pan':       # piatto della bilancia
        rr(d, [x0, y0, x1, y1], 22, card, c, 6); T(C, k['label'], 40, y0 + 20, white, x=cx, maxw=x1 - x0 - 30); T(C, k['val'], 100, y0 + 90, c, x=cx, maxw=x1 - x0 - 30)
    elif kind == 'eq':        # operazione stampata: a  op  b  =  r
        xs = [x0 + (x1 - x0) * (i + 0.5) / len(k['parts']) for i in range(len(k['parts']))]
        for xx, (t_, col, sz) in zip(xs, k['parts']): T(C, t_, sz, cy - sz * 0.6, col, x=xx, maxw=(x1 - x0) / len(k['parts']) - 10)
    else: draw_new11(C, e)

def FORM(box, head, rows, cues, right='FORM 1040', first=None, hl=()):
    """modulo che si compila riga per riga: ogni riga (no, testo, importo) compare sulla sua parola"""
    x0, y0, x1, y1 = box; x0, x1 = max(x0, 150), min(x1, 1770); rh = min((y1 - y0 - 96) / len(rows), 96); y1 = y0 + 96 + rh * len(rows) + 8; box = (x0, y0, x1, y1)
    out = [E('form1a', box, first, head=head, right=right)]
    for i, (r, cu) in enumerate(zip(rows, cues)):
        no, tx, vl = r[:3]; vc = r[3] if len(r) > 3 else (30, 120, 70)
        out.append(E('formrow', (x0, y0 + 90 + rh * i, x1, y0 + 90 + rh * (i + 1)), cu, no=no, text=tx, val=vl, vc=vc, hl=(i in hl)))
    return out


# ======================= ELEMENTI NUOVI VIDEO 13 =======================
TABLE3 = {73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7, 77: 22.9, 78: 22.0, 79: 21.1, 80: 20.2, 81: 19.4, 82: 18.5, 83: 17.7, 84: 16.8, 85: 16.0, 86: 15.2, 87: 14.4, 88: 13.7, 89: 12.9, 90: 12.2}
def curve_xy(box, age, f):
    x0, y0, x1, y1 = box; px0, px1 = x0 + 120, x1 - 50; py0, py1 = y0 + 60, y1 - 90
    return px0 + (px1 - px0) * (age - 72) / (91 - 72), py1 - (py1 - py0) * (f - 10) / (28 - 10)

def arrow_h(d, xa, xb, y, col, w=10):
    d.line([xa, y, xb - 26, y], fill=col + (255,), width=w); d.polygon([(xb, y), (xb - 34, y - 24), (xb - 34, y + 24)], fill=col + (255,))

def draw_new(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']; c = k.get('col', gold)
    d = ImageDraw.Draw(C)
    if kind == 'curve':       # curva del fattore (Tavola III) per eta' 73..90
        px0, py_top = curve_xy(e['box'], 72, 28); px1, py1 = curve_xy(e['box'], 91, 10)
        for f in (12, 16, 20, 24, 28):
            yy = curve_xy(e['box'], 72, f)[1]; d.line([px0, yy, px1, yy], fill=(60, 82, 112, 255), width=2); T(C, str(f), 32, yy - 20, grey, x=px0 - 14, anchor='r')
        d.line([px0, py_top - 10, px0, py1 + 6], fill=(150, 165, 190, 255), width=5); d.line([px0 - 6, py1, px1 + 6, py1], fill=(150, 165, 190, 255), width=5)
        pts = [curve_xy(e['box'], a, f) for a, f in TABLE3.items()]
        d.polygon(pts + [(pts[-1][0], py1), (pts[0][0], py1)], fill=c + (50,)); d.line(pts, fill=c + (255,), width=11, joint='curve')
        for a in (75, 80, 85, 90): T(C, str(a), 34, py1 + 14, white, x=curve_xy(e['box'], a, 10)[0])
        T(C, 'AGE', 30, py1 + 54, grey, x=px1, anchor='r'); T(C, k.get('top', 'FACTOR'), 32, y0 + 4, grey, x=px0, anchor='l')
    elif kind == 'cmark':     # marcatore su un punto della curva
        gx, gy = curve_xy(k['gbox'], k['age'], TABLE3[k['age']]); mc = k.get('mc', goldL)
        d.line([gx, gy, gx, curve_xy(k['gbox'], k['age'], 10)[1]], fill=mc + (200,), width=4)
        d.ellipse([gx - 20, gy - 20, gx + 20, gy + 20], fill=mc + (255,), outline=white + (255,), width=5)
        up = k.get('up', True); T(C, k['label'], 38, gy - (104 if up else -34), mc, x=gx + k.get('dx', 0), maxw=250); T(C, k['sub'], 34, gy - (62 if up else -76), white, x=gx + k.get('dx', 0), maxw=250)
    elif kind == 'flow':      # nodi in fila con frecce; k['cross'] = indice della freccia barrata
        nodes = k['nodes']; n = len(nodes); aw = 120; w = (x1 - x0 - aw * (n - 1)) / n
        for i, (icn, l1, l2, nc) in enumerate(nodes):
            bx = x0 + i * (w + aw); rr(d, [bx, y0, bx + w, y1], 30, card, nc, 6)
            ic(C, icn, bx + w / 2, y0 + (y1 - y0) * 0.36, k.get('s', 0.8), nc)
            T(C, l1, 44, y1 - 150, white, x=bx + w / 2, maxw=w - 30)
            if l2: T(C, l2, 36, y1 - 88, nc if nc != card else goldL, x=bx + w / 2, maxw=w - 30)
            if i < n - 1:
                ax0, ax1 = bx + w + 12, bx + w + aw - 12; ay = y0 + (y1 - y0) * 0.36
                bad = (k.get('cross') == i); arrow_h(d, ax0, ax1, ay, red if bad else goldL, 9)
                if bad: cross(C, (ax0 + ax1) / 2, ay, 40, red)
    elif kind == 'vbars':     # barre verticali con valore sopra e etichetta sotto: vals = [(label, value, text, color)]
        vals = k['vals']; n = len(vals); mx = max(v for _, v, _, _ in vals); base = y1 - 70; mh = y1 - y0 - 160; bw = (x1 - x0) / (n * 1.6)
        for i, (lab, v, tx, vc) in enumerate(vals):
            bx = x0 + (x1 - x0) * (i + 0.5) / n - bw / 2; hh = max(14, mh * v / mx)
            rr(d, [bx, base - hh, bx + bw, base], 16, vc, white, 3); T(C, tx, 54, base - hh - 72, white, x=bx + bw / 2, maxw=bw * 1.9)
            T(C, lab, 36, base + 12, white, x=bx + bw / 2, maxw=bw * 1.9)
    else: draw_new12(C, e)
