"""Motore slide video 9 (modello unico: stessa cornice, sfondo, titolo, pillola all'80%), layout diversi per ogni slide.
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
    elif name == 'bank': building(C, cx, cy, 240 * s, 190 * s, gold)
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

def E(kind, box, cue=None, **k): return dict(kind=kind, box=box, cue=cue, k=k)

def draw_el(C, e):
    x0, y0, x1, y1 = e['box']; k = e['k']; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2; kind = e['kind']
    c = k.get('col', gold)
    if kind == 'card':
        card_(C, x0, y0, x1, y1, c, k.get('head'), k.get('val'), k.get('sub'), k.get('vsize', 96), k.get('vcol', white))
        if k.get('icon'): ic(C, k['icon'], cx, y0 + (y1 - y0) * 0.36, k.get('s', 0.8), c)
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

def slide(title, seed, els, pill, pcol=gold, tcol=None, tsize=58, psize=52):
    tcol = tcol or (navy if pcol in (gold, goldL, green) else (255, 255, 255))
    def fn(t):
        fr = stage_live(t, title, seed, tsize)
        lim = LASTP() - 0.3; n = len(els); times = []
        for i, e in enumerate(els):
            mx = lim - 0.3 * (n - 1 - i)
            tc = 0.35 if (i == 0 and e['cue'] is None) else (tm(e['cue'], mx) if e['cue'] else (times[-1] + 0.35 if times else 0.35))
            if i == 0: tc = min(tc, 0.4)
            if times: tc = max(tc, times[-1] + 0.3)
            times.append(min(tc, mx))
        for e, tc in zip(els, times):
            if t > tc:
                C = new(); x0, y0, x1, y1 = e['box']
                if e['kind'] == 'stamp':
                    fr = stamp(fr, e['k']['t'], (x0 + x1) / 2, (y0 + y1) / 2, e['k'].get('ang', 8), e['k'].get('col', green), min(1.0, ease((t - tc) / 0.35)), e['k'].get('size', 60)); continue
                draw_el(C, e)
                pad = 40 if e['kind'] in ('arrow', 'op', 'line', 'big') else 20
                fr = P2(fr, C, (x0 - pad, y0 - pad, x1 + pad, y1 + pad), t, tc)
        return frame(pill_last(fr, t, pill, PILL_Y, pcol, tcol, psize))
    return frozen(fn)
