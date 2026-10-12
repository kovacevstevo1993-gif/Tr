"""Ciclo di camminata del topolino da una sola posa: testa+busto, due braccia e due gambe separati.
walk_frame(parts, t) -> RGBA 768x1376.  t in secondi, ciclo di 1.0 s = due passi."""
import math, numpy as np
from PIL import Image

W, H = 768, 1376
def _mask(a, f):
    yy, xx = np.mgrid[0:H, 0:W]
    return f(xx, yy)

def split(path="assets/topo/neutro_full.png"):
    im = np.array(Image.open(path).convert("RGBA"))
    # rimuove la stellina di AI Studio in basso a destra
    im[1260:, 660:, 3] = 0
    r, g, b = [im[..., i].astype(int) for i in range(3)]
    cloth = ((r > 200) & (g > 165) & (b < 100)) | ((g > r + 25) & (b > r + 15) & (g > 150) & (np.mgrid[0:H, 0:W][1] > 0))  # giallo, turchese
    from scipy.ndimage import binary_dilation
    cloth = binary_dilation(cloth, iterations=3)
    def cut(f, arm=False):
        m = _mask(None, f)
        pass
        out = im.copy(); out[~m, 3] = 0
        return Image.fromarray(out)
    # confine braccio/corpo per riga, dalla sagoma (spazio vuoto tra braccio e salopette)
    alpha = im[..., 3] > 40
    bl, br = np.full(H, 266.0), np.full(H, 501.0)
    for y in range(765, 960):
        t = np.flatnonzero(np.diff(alpha[y].astype(int)))
        tl, tr = t[t < 385], t[t >= 385]
        if len(tl) >= 2: bl[y] = (tl[-1] + tl[-2]) / 2
        if len(tr) >= 2: br[y] = (tr[0] + tr[1]) / 2
    for arr in (bl, br):
        arr[765:960] = np.convolve(np.pad(arr[765:960], 3, mode="edge"), np.ones(7) / 7, mode="valid")
    armL = lambda x, y: (y >= 724) & (y < 925) & (x < bl[y])
    armR = lambda x, y: (y >= 724) & (y < 925) & (x > br[y])
    legL = lambda x, y: (y >= 1032) & (x < 385) & (x > 200)
    legR = lambda x, y: (y >= 1032) & (x >= 385) & (x < 530)
    armLm = armL
    armRm = armR
    body = lambda x, y: ~(armLm(x, y) | armRm(x, y)) & ~(((y >= 1040) & (x < 530)))
    # coda: resta col corpo (non nelle gambe)
    tail = lambda x, y: (y >= 1040) & (x >= 530)
    body2 = lambda x, y: body(x, y) | tail(x, y)
    return dict(body=cut(body2), armL=cut(armL, True), armR=cut(armR, True), legL=cut(legL), legR=cut(legR))

def _rot(img, ang, pivot, dx=0, dy=0, sy=1.0):
    # rotazione attorno a pivot (+ scala verticale attorno al pivot) poi traslazione
    a = math.radians(ang)
    c, s = math.cos(a), math.sin(a)
    px, py = pivot
    # matrice inversa (dest->src) per Image.transform AFFINE
    # dest = R * S * (src - p) + p + d  ->  src = S^-1 R^-1 (dest - p - d) + p
    def inv(xd, yd):
        x, y = xd - px - dx, yd - py - dy
        xr, yr = c * x + s * y, -s * x + c * y
        return xr + px, yr / sy + py
    (a0, b0), (a1, b1), (a2, b2) = inv(0, 0), inv(1, 0), inv(0, 1)
    return img.transform((W, H), Image.AFFINE, (a1 - a0, a2 - a0, a0, b1 - b0, b2 - b0, b0), Image.BICUBIC)

def walk_frame(parts, t, amp=1.0):
    ph = 2 * math.pi * t           # 1 ciclo = 1 s
    s = math.sin(ph)               # +1: gamba sx alzata/in avanti, braccio dx avanti
    bob = -abs(math.sin(ph)) * 10 * amp          # rimbalzo due volte per ciclo
    sway = math.sin(ph) * 7 * amp                # dondolio laterale
    tilt = math.sin(ph) * 1.8 * amp
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # gambe: alza il piede che avanza (sin>0 sx), l'altro resta a terra e spinge
    liftL = max(0, s) * 34 * amp; liftR = max(0, -s) * 34 * amp
    swingL = s * 9 * amp; swingR = -s * 9 * amp
    hip = lambda x: (x, 1030)
    for name, lift, swg, xp, sc in (("legR", liftR, swingR, 450, 1.0), ("legL", liftL, swingL, 320, 1.0)):
        stretch = 1.0 - (lift / 34) * 0.10 * amp if lift else 1.0
        g = _rot(parts[name], swg * 0.8, hip(xp), dx=sway * 0.6 + swg * 0.5, dy=-lift + bob * 0.3, sy=stretch)
        out.alpha_composite(g)
    body = _rot(parts["body"], tilt, (385, 1030), dx=sway, dy=bob)
    # braccia: oscillano in opposizione alle gambe
    armLa = _rot(parts["armL"], -s * 13 * amp, (235, 722), dx=sway, dy=bob, sy=1 + 0.03 * s * amp)
    armRa = _rot(parts["armR"], -s * 13 * amp, (540, 728), dx=sway, dy=bob, sy=1 - 0.03 * s * amp)
    # il braccio che va avanti sta davanti al corpo, quello indietro dietro
    for a, front in ((armLa, s < 0), (armRa, s > 0)):
        if not front: out.alpha_composite(a)
    out.alpha_composite(body)
    for a, front in ((armLa, s < 0), (armRa, s > 0)):
        if front: out.alpha_composite(a)
    return out

if __name__ == "__main__":
    import sys
    parts = split()
    bg = Image.new("RGBA", (W, H), (120, 200, 120, 255))
    ts = [0, .125, .25, .375, .5, .625, .75, .875]
    sheet = Image.new("RGB", (W * 4 // 2, H * 2 // 2))
    for i, t in enumerate(ts):
        f = bg.copy(); f.alpha_composite(walk_frame(parts, t))
        sheet.paste(f.convert("RGB").resize((W // 2, H // 2)), ((i % 4) * W // 2, (i // 4) * H // 2))
    sheet.save("/tmp/claude-0/pt/walk_sheet.png")
