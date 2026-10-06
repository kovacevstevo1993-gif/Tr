from v3lib import *
from v3b3_10 import POP, new, lerp
from v4b11_20 import calculator, hourglass, ss_card
from v4b2_10 import cal_card
import sys, math

# fine-voce assoluta (fotogrammi a 30 fps) letta dagli screenshot; blocco 1 consegnato = 810
END = {0: 0, 1: 810, 2: 1538, 3: 2410, 4: 3270, 5: 4013, 6: 4659, 7: 5515, 8: 6207, 9: 6893, 10: 7513, 11: 8367, 12: 9117, 13: 9837, 14: 10512, 15: 11235, 16: 11989, 17: 12668, 18: 13469, 19: 14151, 20: 14846, 21: 15494, 22: 16366, 23: 17100, 24: 17633, 25: 18442, 26: 19018, 27: 19757, 28: 20485, 29: 21113, 30: 21955, 31: 22336}

class Blk:
    def __init__(s, n, S, groups):
        s.n = n; s.S = S; s.G = groups; s.tot = END[n] - END[n - 1]
        gw = [sum(len(S[i]) + 10 for i in g) for g in groups]
        fs = [round(w / sum(gw) * s.tot) for w in gw]; fs[-1] = s.tot - sum(fs[:-1]); s.FS = fs
        s.TXT = [' '.join(S[i] for i in g) for g in groups]
    def _w(s, text): return len(text) + 3 * (text.count(',') + text.count(':'))
    def tt(s, g, marker):
        txt_ = s.TXT[g]; i = txt_.index(marker)
        return max(0.2, s._w(txt_[:i]) / s._w(txt_) * s.FS[g] / 30 - 0.1)

def E(t, t0, d=0.8): return ease((t - t0) / d)

def appear(fr, C, box, t, t0, d=0.8):
    e = ease((t - t0) / d)
    if e <= 0: return fr
    x0, y0, x1, y1 = [int(v) for v in box]; x0 = max(0, x0); y0 = max(0, y0); x1 = min(W, x1); y1 = min(H, y1)
    piece = C.crop((x0, y0, x1, y1)); s = 0.92 + 0.08 * e
    w, h = piece.size
    p2 = piece.resize((max(1, int(w * s)), max(1, int(h * s))), Image.BILINEAR)
    a = p2.split()[3].point(lambda v: int(v * e)); p2.putalpha(a)
    fr.alpha_composite(p2, (int((x0 + x1) / 2 - p2.width / 2), int((y0 + y1) / 2 - p2.height / 2)))
    return fr

def title(fr, text, t, size=58, col=None): return title_layer(fr, text, t, size, 90, col)

def label(fr, text, y, size, col, t, t0, x=960, d=0.7, anchor='c', bold=True):
    L = new(); txt(L, text, (BOLD if bold else REG)(size), y, col, 255 * E(t, t0, d), x=x, anchor=anchor)
    return Image.alpha_composite(fr, L)

def person(L, cx, cy, col, s=1.0, alpha=255):
    d = ImageDraw.Draw(L)
    d.ellipse([cx - 18 * s, cy - 52 * s, cx + 18 * s, cy + -16 * s], fill=A(col, alpha))
    d.rounded_rectangle([cx - 30 * s, cy - 10 * s, cx + 30 * s, cy + 46 * s], radius=int(22 * s), fill=A(col, alpha))

def tile(C, x, y, sz, col, label_=None, fill=None, outline=None, alpha=255):
    d = ImageDraw.Draw(C)
    f = fill or col
    d.rounded_rectangle([x, y + 6, x + sz, y + sz + 6], radius=14, fill=A((90, 64, 20) if fill is None else (110, 30, 30), alpha))
    d.rounded_rectangle([x, y, x + sz, y + sz], radius=14, fill=A(f, alpha), outline=A(outline or goldL, alpha), width=3)
    d.rounded_rectangle([x + 8, y + 6, x + sz - 8, y + 18], radius=6, fill=A((255, 255, 255), 60))
    if label_ is not None:
        txt(C, label_, BOLD(int(sz * 0.5)), y + sz * 0.2, navy if fill is None else (255, 255, 255), alpha, x=x + sz / 2)

def paycheck(C, x0, y0, x1, y1, col, amount, sub='PER MONTH', head='MONTHLY CHECK', size=120):
    d = ImageDraw.Draw(C)
    d.rounded_rectangle([x0, y0, x1, y1], radius=30, fill=(236, 240, 245, 255), outline=A(col, 255), width=6)
    d.rounded_rectangle([x0, y0, x1, y0 + 78], radius=30, fill=A(col, 255)); d.rectangle([x0, y0 + 48, x1, y0 + 78], fill=A(col, 255))
    txt(C, head, BOLD(40), y0 + 16, (255, 255, 255), 255, x=(x0 + x1) / 2)
    txt(C, amount, BOLD(size), y0 + 105, navy, 255, x=(x0 + x1) / 2)
    txt(C, sub, BOLD(44), y1 - 78, (70, 84, 108), 255, x=(x0 + x1) / 2)

def magnifier(C, cx, cy, r, col=goldL, alpha=255):
    d = ImageDraw.Draw(C)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=A(col, alpha), width=max(6, int(r * 0.16)))
    d.line([cx + r * 0.72, cy + r * 0.72, cx + r * 1.6, cy + r * 1.6], fill=A(col, alpha), width=max(8, int(r * 0.24)))

def arrow_r(C, x0, x1, y, col=goldL, alpha=255, w=10):
    d = ImageDraw.Draw(C)
    d.line([x0, y, x1 - 16, y], fill=A(col, alpha), width=w)
    d.polygon([(x1, y), (x1 - 34, y - 26), (x1 - 34, y + 26)], fill=A(col, alpha))

def arrow_d(C, x, y0, y1, col=red, alpha=255, w=12):
    d = ImageDraw.Draw(C)
    d.line([x, y0, x, y1 - 20], fill=A(col, alpha), width=w)
    d.polygon([(x, y1), (x - 30, y1 - 40), (x + 30, y1 - 40)], fill=A(col, alpha))

def money(v, cents=False):
    return f'${v:,.2f}' if cents else f'${int(round(v)):,}'

def render_slide(draw, n_frames, out):
    render_fast(draw, n_frames, out)

def chip(fr, text, cx, y, t, t0, col=goldL, size=40, filled=None, tcol=None, d=0.8):
    C = new(); dr = ImageDraw.Draw(C); f = BOLD(size); b = dr.textbbox((0, 0), text, font=f)
    w = b[2] - b[0] + 80; h = size * 1.95
    dr.rounded_rectangle([cx - w / 2, y, cx + w / 2, y + h], radius=int(h / 2), fill=A(filled or card, 255), outline=A(col, 255), width=4)
    dr.text((cx - (b[2] - b[0]) / 2 - b[0], y + h / 2 - (b[3] - b[1]) / 2 - b[1]), text, font=f, fill=A(tcol or col, 255))
    return appear(fr, C, (cx - w / 2 - 8, y - 8, cx + w / 2 + 8, y + h + 8), t, t0, d)

def strike(L, x0, x1, y, col=red, alpha=255, w=10):
    ImageDraw.Draw(L).line([x0, y, x1, y], fill=A(col, alpha), width=w)

def run_cli(name, SL, FSD, mod_blocks):
    mode = sys.argv[1]; bsel = [int(x) for x in sys.argv[2].split(',')]
    for b in bsel:
        fns = SL[b]; fss = FSD[b]
        if mode == 'preview':
            im = Image.new('RGB', (1920, 360 * len(fns)))
            for i, (fn, f) in enumerate(zip(fns, fss)):
                for c, q in enumerate([0.25, 0.6, 0.97]):
                    im.paste(fn(f / 30 * q).convert('RGB').resize((640, 360)), (c * 640, i * 360))
            im.save(f'/home/claude/pv5b{b}.png'); print(b, fss, sum(fss))
        else:
            for i, (fn, f) in enumerate(zip(fns, fss), 1):
                render_fast(fn, f, f'/mnt/user-data/outputs/v5-b{b}-0{i}.mp4'); print('done', b, i, f, flush=True)
