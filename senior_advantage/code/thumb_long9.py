"""Miniature video lungo 9 (ALDI), 2 versioni diverse per il test A/B. 1280x720.
Logo Aldi vero (SVG ufficiale scaricato da corporate.aldi.us: https://dm.cms.aldi.cx/is/content/prod1amer/aldius-logo,
salvato in riferimenti/aldi/aldi-us-logo.svg e .png), su richiesta dell'utente 23/10 e 26/10.
Titolo video: Aldi Has No Senior Discount (Aldi Says So). 10 Things To Know Before You Shop
Modelli virali Aldi guardati il 26/10 (4,1M, 1,19M, 1,3M, 1,1M, 946K, 705K, 441K, 329K, 242K, 241K view):
 logo Aldi enorme come eroe, striscia bianca in basso con testo nero grande e targhetta rossa, cerchio giallo + freccia rossa
 sul quarto di dollaro nel blocco del carrello, pochi testi grandi.
A = ricerca "aldi senior discount" -> risposta gigante "NO." (domanda che il pubblico scrive davvero), logo grande, targhetta rossa
    "ALDI SAYS SO" + striscia bianca "10 THINGS TO KNOW BEFORE YOU SHOP". Sfondo blu notte Aldi con strisce oblique (come il logo).
B = primo piano del quarto di dollaro che apre il carrello (punto 2 del video), cerchio giallo e freccia rossa, "BEFORE YOU / SHOP AT ALDI",
    striscia bianca "10 RULES FROM ALDI'S OWN PAGES". Sfondo arancio-rosso Aldi.
Tutte le scritte sono vere e dette nel video (Aldi dice che non offre sconti; deposito di un quarto; regole dalle pagine Aldi).
uso: OUT=cartella python3 thumb_long9.py"""
import os, math, random
from PIL import Image, ImageDraw, ImageFilter, ImageChops
from thumb_long3 import *

OUT = os.environ.get("OUT", "/home/user/Tr/senior_advantage/miniature")
os.makedirs(OUT, exist_ok=True)
REF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "riferimenti", "aldi")
ANAVY = (2, 32, 95); AORG = (244, 125, 32); AYEL = (255, 194, 14); ARED = (225, 27, 34); ABLUE = (0, 112, 214)
INK = (16, 18, 24); PAPER = (255, 255, 255)


# ------------------------------------------------------------------ ombre senza bordo tagliato
def comp(base, lay, xy):
    """alpha_composite che accetta posizioni fuori dal quadro"""
    x, y = int(xy[0]), int(xy[1])
    sx0, sy0 = max(0, -x), max(0, -y); sx1, sy1 = min(lay.width, base.width - x), min(lay.height, base.height - y)
    if sx1 > sx0 and sy1 > sy0:
        base.alpha_composite(lay.crop((sx0, sy0, sx1, sy1)), (x + sx0, y + sy0))


def sp(im, lay, xy, off=(8, 12), blur=10, alpha=150, col=(0, 0, 0)):
    base = im.convert("RGBA")
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
    solid = Image.new("RGBA", lay.size, col + (alpha,))
    sh.paste(solid, (int(xy[0] + off[0]), int(xy[1] + off[1])), lay.split()[3])
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(sh)
    comp(base, lay, xy)
    return base.convert("RGB")


def text3d(im, xy, s, size, fill, depth_col, stroke=16, sc=BLK, anchor="m", w="Black", dep=14, rot_deg=0):
    """testo con spessore (estrusione) e contorno nero"""
    f = F(size, w)
    bb = ImageDraw.Draw(Image.new("L", (4, 4))).textbbox((0, 0), s, font=f, stroke_width=stroke)
    tw, th = bb[2] - bb[0] + 60 + dep, bb[3] - bb[1] + 60 + dep
    lay = Image.new("RGBA", (tw, th), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cx, cy = (tw - dep) / 2, (th - dep) / 2
    for k in range(dep, 0, -2):
        d.text((cx + k * .6, cy + k), s, font=f, fill=depth_col, anchor="mm", stroke_width=stroke, stroke_fill=sc)
    d.text((cx, cy), s, font=f, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=sc)
    if rot_deg: lay = rot(lay, rot_deg)
    ax = {"l": 0, "m": .5, "r": 1}[anchor[0]]
    return sp(im, lay, (int(xy[0] - lay.width * ax), int(xy[1] - lay.height / 2)), off=(6, 10), blur=8, alpha=140)


# ------------------------------------------------------------------ logo (vero, dal sito ufficiale)
def aldi_logo(h):
    im = Image.open(os.path.join(REF, "aldi-us-logo.png")).convert("RGBA")
    return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)


def sheen(lay, strength=70, ang=-28):
    """riflesso lucido diagonale che segue la forma del livello (alpha)"""
    w, h = lay.size
    g = Image.new("L", (w, h), 0); d = ImageDraw.Draw(g)
    d.polygon([(-w * .1, h * .08), (w * .55, -h * .1), (w * .85, -h * .1), (-w * .1, h * .62)], fill=strength)
    g = g.filter(ImageFilter.GaussianBlur(max(2, w // 40)))
    mask = ImageChops.multiply(g, lay.split()[3])
    out = lay.copy(); white = Image.new("RGBA", (w, h), (255, 255, 255, 255)); out.paste(white, (0, 0), mask)
    return out


# ------------------------------------------------------------------ sfondi
def vgrad(c0, c1, w=W, h=H, ang=0):
    im = Image.new("RGB", (w, h)); px = im.load()
    ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    span = abs(w * ca) + abs(h * sa)
    for y in range(h):
        for x in range(w):
            t = ((x - w / 2) * ca + (y - h / 2) * sa) / span + .5
            t = min(1, max(0, t))
            px[x, y] = tuple(int(c0[i] + (c1[i] - c0[i]) * t) for i in range(3))
    return im


def glow(im, cx, cy, r, col, alpha=200):
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([cx - r, cy - r, cx + r, cy + r], fill=alpha)
    m = m.filter(ImageFilter.GaussianBlur(r * .5))
    return Image.composite(Image.new("RGB", (W, H), col), im, m)


def stripes(im, col=(120, 200, 255), alpha=46):
    """tre strisce oblique morbide, come nel logo Aldi"""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for x0, wd, a in ((470, 70, alpha), (590, 120, int(alpha * .8)), (780, 210, int(alpha * .55))):
        d.polygon([(x0 + 280, -10), (x0 + 280 + wd, -10), (x0 + wd - 380, H + 10), (x0 - 380, H + 10)], fill=col + (a,))
    lay = lay.filter(ImageFilter.GaussianBlur(5))
    base = im.convert("RGBA"); base.alpha_composite(lay); return base.convert("RGB")


def vignette(im, strength=120):
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([-220, -170, W + 220, H + 170], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(170))
    return Image.composite(im, Image.blend(im, Image.new("RGB", (W, H), (0, 0, 0)), strength / 255), m)


# ------------------------------------------------------------------ elementi comuni
def white_band(text, w, h, size, ink=INK, ang=0, tag=None, tag_fill=ARED, tag_size=34):
    """striscia bianca con testo nero (stile virale) e targhetta rossa in alto a sinistra"""
    pad = 40
    lay = Image.new("RGBA", (w, h + pad), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([0, pad, w - 1, h + pad - 1], radius=16, fill=(255, 255, 255, 255), outline=BLK, width=6)
    d.text((w / 2, pad + h / 2 + 2), text, font=F(size, "ExtraBold"), fill=ink, anchor="mm")
    if tag:
        f = F(tag_size, "Black"); tw = d.textbbox((0, 0), tag, font=f)[2]
        d.rounded_rectangle([14, 2, 14 + tw + 44, pad + 24], radius=10, fill=tag_fill, outline=BLK, width=5)
        d.text((14 + 22 + tw / 2, 2 + (pad + 22) / 2 + 1), tag, font=f, fill=(255, 255, 255), anchor="mm")
    return rot(lay, ang) if ang else lay


def search_bar(w, h, text):
    s = SS
    lay = canvas(w, h); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([6 * s, 6 * s, (w - 6) * s, (h - 6) * s], radius=(h // 2) * s, fill=(255, 255, 255, 255), outline=(30, 40, 60), width=5 * s)
    f = F(h * 0.44 * s, "SemiBold")
    d.text((int(h * 0.62) * s, (h // 2 + 2) * s), text, font=f, fill=(32, 33, 36), anchor="lm")
    tw = d.textbbox((0, 0), text, font=f)[2]
    cx = int(h * 0.62) * s + tw + 14 * s
    d.rounded_rectangle([cx, int(h * .24) * s, cx + 7 * s, int(h * .76) * s], radius=3 * s, fill=(30, 110, 230))   # cursore
    # lente d'ingrandimento a destra
    mx, my, r = (w - int(h * .62)), h // 2 - 4, int(h * .20)
    d.ellipse([(mx - r) * s, (my - r) * s, (mx + r) * s, (my + r) * s], outline=(30, 110, 230), width=int(h * .085) * s)
    d.line([((mx + r * .72) * s, (my + r * .72) * s), ((mx + r * 1.75) * s, (my + r * 1.75) * s)], fill=(30, 110, 230), width=int(h * .10) * s)
    return done(lay, w, h)


def red_ring(w, h, col=AYEL, wd=14):
    s = SS
    lay = canvas(w, h); d = ImageDraw.Draw(lay)
    d.ellipse([wd * s, wd * s, (w - wd) * s, (h - wd) * s], outline=BLK, width=(wd + 10) * s)
    d.ellipse([wd * s, wd * s, (w - wd) * s, (h - wd) * s], outline=col, width=wd * s)
    return done(lay, w, h)


def fat_arrow(w, h, col, ang=0):
    s = SS
    lay = canvas(w, h); d = ImageDraw.Draw(lay)
    pts = [(8, h * .34), (w * .58, h * .34), (w * .58, h * .08), (w - 8, h * .5), (w * .58, h * .92), (w * .58, h * .66), (8, h * .66)]
    pp = [(x * s, y * s) for x, y in pts]
    d.polygon(pp, fill=col); d.line(pp + [pp[0]], fill=BLK, width=9 * s, joint="curve")
    # luce sul bordo alto della freccia
    d.line([(14 * s, (h * .36) * s), ((w * .56) * s, (h * .36) * s)], fill=tuple(min(255, c + 60) for c in col), width=5 * s)
    return rot(done(lay, w, h), ang)


# ------------------------------------------------------------------ A: ricerca -> NO.
def thumb_a():
    im = vgrad((2, 22, 78), (14, 96, 205), ang=-35)
    im = glow(im, 330, 330, 430, (34, 120, 230), 150)
    im = stripes(im)
    im = vignette(im, 105)
    # logo gigante, inclinato, con riflesso
    lg = rot(sheen(aldi_logo(500), 85), 5)
    im = sp(im, lg, (24, 40), off=(18, 26), blur=24, alpha=190)
    # barra di ricerca (la domanda che la gente scrive davvero)
    sb = rot(search_bar(690, 104, "aldi senior discount"), -2)
    im = sp(im, sb, (528, 62), off=(8, 14), blur=14, alpha=170)
    # risposta gigante con spessore
    im = text3d(im, (868, 338), "NO.", 384, AYEL, (176, 112, 0), stroke=22, dep=16)
    # striscia bianca + targhetta rossa
    wb = white_band("10 THINGS TO KNOW BEFORE YOU SHOP", 1210, 100, 55, tag="ALDI SAYS SO")
    im = sp(im, wb, (35, 568), off=(0, 10), blur=12, alpha=170)
    return im


def coin(d_px):
    """moneta d'argento lucida (stilizzata) con bordo zigrinato, anello interno e rilievo; sprite RGBA quadrato"""
    S2 = 4
    n = d_px * S2; R = n / 2
    lay = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    # corpo: gradiente radiale argento
    body = Image.new("RGBA", (n, n), (0, 0, 0, 0)); px = body.load()
    for y in range(n):
        for x in range(n):
            dx, dy = x - R, y - R
            r = math.hypot(dx, dy)
            if r <= R:
                t = (dx * .55 + dy * .85) / R * .5 + .5        # luce da alto-sinistra
                t = min(1, max(0, t))
                g = int(236 - 92 * t)
                px[x, y] = (g, g + 3, g + 10, 255)
    lay.alpha_composite(body)
    dr = ImageDraw.Draw(lay)
    # bordo zigrinato
    for k in range(120):
        a = 2 * math.pi * k / 120
        x0, y0 = R + (R * .955) * math.cos(a), R + (R * .955) * math.sin(a)
        x1, y1 = R + (R * .995) * math.cos(a), R + (R * .995) * math.sin(a)
        dr.line([(x0, y0), (x1, y1)], fill=(110, 116, 126, 255) if k % 2 else (226, 230, 236, 255), width=int(S2 * 1.6))
    dr.ellipse([R * .035, R * .035, n - R * .035, n - R * .035], outline=(80, 86, 96, 255), width=S2 * 3)
    dr.ellipse([R * .12, R * .12, n - R * .12, n - R * .12], outline=(246, 248, 252, 255), width=S2 * 4)     # anello rialzato (luce)
    dr.ellipse([R * .145, R * .145, n - R * .145, n - R * .145], outline=(120, 126, 138, 255), width=S2 * 3)  # ombra interna
    # campo interno leggermente piu scuro
    inner = Image.new("RGBA", (n, n), (0, 0, 0, 0)); idr = ImageDraw.Draw(inner)
    idr.ellipse([R * .17, R * .17, n - R * .17, n - R * .17], fill=(150, 156, 168, 70))
    lay.alpha_composite(inner)
    # numero in rilievo "25"
    f = F(int(R * 0.92), "Black")
    dr.text((R + S2 * 5, R + R * .02 + S2 * 5), "25", font=f, fill=(92, 98, 110, 255), anchor="mm")     # ombra
    dr.text((R - S2 * 3, R + R * .02 - S2 * 3), "25", font=f, fill=(250, 251, 253, 255), anchor="mm")   # luce
    dr.text((R, R + R * .02), "25", font=f, fill=(176, 182, 194, 255), anchor="mm")
    f2 = F(int(R * 0.26), "ExtraBold")
    dr.text((R, R * 1.50), "CENTS", font=f2, fill=(110, 116, 128, 255), anchor="mm")
    # riflesso lucido
    gl = Image.new("L", (n, n), 0); gd = ImageDraw.Draw(gl)
    gd.ellipse([R * .16, R * .08, R * 1.18, R * .86], fill=88)
    gl = gl.filter(ImageFilter.GaussianBlur(R * .09))
    gl = ImageChops.multiply(gl, lay.split()[3])
    lay.paste(Image.new("RGBA", (n, n), (255, 255, 255, 255)), (0, 0), gl)
    # scintilla a 4 punte
    sx, sy, sr = R * .46, R * .40, R * .20
    gd2 = ImageDraw.Draw(lay)
    gd2.polygon([(sx, sy - sr), (sx + sr * .13, sy - sr * .13), (sx + sr, sy), (sx + sr * .13, sy + sr * .13), (sx, sy + sr), (sx - sr * .13, sy + sr * .13), (sx - sr, sy), (sx - sr * .13, sy - sr * .13)], fill=(255, 255, 255, 235))
    return lay.resize((d_px, d_px), Image.LANCZOS)


# ------------------------------------------------------------------ B: il quarto nel carrello
def lock_scene(w, h):
    """maniglia rossa del carrello + scatola della moneta + quarto che entra nella fessura + cerchio giallo.
    Tutto disegnato in un solo livello (poi ruotato) cosi la moneta e la fessura restano allineate."""
    s = SS
    # 1) maniglia rossa dietro
    bar = canvas(w, h); d = ImageDraw.Draw(bar)
    d.rounded_rectangle([0, 96 * s, w * s, 250 * s], radius=64 * s, fill=(206, 26, 32, 255), outline=BLK, width=9 * s)
    d.rounded_rectangle([20 * s, 112 * s, (w - 20) * s, 150 * s], radius=19 * s, fill=(250, 96, 84, 255))
    d.rounded_rectangle([20 * s, 214 * s, (w - 20) * s, 236 * s], radius=11 * s, fill=(150, 14, 20, 255))
    bar = done(bar, w, h)
    # 2) scatola grafite con fessura
    box = canvas(w, h); d = ImageDraw.Draw(box)
    bx0, by0, bx1, by1 = 70, 168, w - 70, h - 6
    d.rounded_rectangle([bx0 * s, by0 * s, bx1 * s, by1 * s], radius=48 * s, fill=(62, 66, 78, 255), outline=BLK, width=9 * s)
    d.rounded_rectangle([(bx0 + 12) * s, (by0 + 12) * s, (bx1 - 12) * s, (by0 + 70) * s], radius=34 * s, fill=(104, 110, 126, 255))
    d.rounded_rectangle([(bx0 + 12) * s, (by0 + 70) * s, (bx1 - 12) * s, (by1 - 14) * s], radius=34 * s, fill=(44, 47, 58, 255))
    for sx_ in (bx0 + 52, bx1 - 52):
        d.ellipse([(sx_ - 15) * s, (by0 + 26) * s, (sx_ + 15) * s, (by0 + 56) * s], fill=(160, 166, 180, 255), outline=BLK, width=4 * s)
        d.line([((sx_ - 9) * s, (by0 + 41) * s), ((sx_ + 9) * s, (by0 + 41) * s)], fill=BLK, width=4 * s)
    sy = 440                                   # centro fessura
    d.rounded_rectangle([(bx0 + 70) * s, (sy - 24) * s, (bx1 - 70) * s, (sy + 24) * s], radius=24 * s, fill=(6, 6, 10, 255), outline=(150, 156, 170, 255), width=5 * s)
    box = done(box, w, h)
    # 3) quarto (piu grande della fessura, la parte bassa e dentro)
    cd = 372
    cn = coin(cd)
    ccx, ccy = w // 2, 296                     # centro moneta
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    lay.alpha_composite(bar); lay.alpha_composite(box)
    # luce gialla dietro la moneta
    gl = Image.new("L", (w, h), 0); ImageDraw.Draw(gl).ellipse([ccx - 250, ccy - 250, ccx + 250, ccy + 250], fill=120)
    gl = gl.filter(ImageFilter.GaussianBlur(60))
    lay.paste(Image.new("RGBA", (w, h), (255, 236, 150, 255)), (0, 0), gl)
    # ombra della moneta sulla scatola
    sh = Image.new("RGBA", (w, h), (0, 0, 0, 0)); sh.paste(Image.new("RGBA", cn.size, (0, 0, 0, 170)), (ccx - cd // 2 + 8, ccy - cd // 2 + 16), cn.split()[3])
    sh = sh.filter(ImageFilter.GaussianBlur(14)); lay.alpha_composite(sh)
    lay.alpha_composite(cn, (ccx - cd // 2, ccy - cd // 2))
    # 4) bordo anteriore della fessura: copre la parte bassa della moneta
    front = box.crop((0, sy, w, h)); lay.alpha_composite(front, (0, sy))
    d2 = ImageDraw.Draw(lay)
    d2.rounded_rectangle([(bx0 + 70) * 1, sy - 24, (bx1 - 70) * 1, sy + 24], radius=24, outline=(170, 176, 190, 255), width=4)
    # 5) cerchio giallo con contorno nero attorno al quarto
    rg = red_ring(cd + 96, cd + 96, AYEL, 15)
    lay.alpha_composite(rg, (ccx - (cd + 96) // 2, ccy - (cd + 96) // 2))
    return lay


def thumb_b():
    im = vgrad((255, 168, 20), (232, 46, 28), ang=62)
    im = glow(im, 930, 280, 430, (255, 224, 96), 175)
    # bokeh di luci dietro (profondita)
    rnd = random.Random(9)
    bk = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(bk)
    for _ in range(26):
        r = rnd.randint(22, 70); x = rnd.randint(340, W); y = rnd.randint(0, H)
        bd.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, rnd.randint(14, 38)))
    bk = bk.filter(ImageFilter.GaussianBlur(7))
    base = im.convert("RGBA"); base.alpha_composite(bk); im = vignette(base.convert("RGB"), 95)
    # scena del carrello a destra, leggermente inclinata
    sc = rot(lock_scene(700, 640), -7)
    sc = sc.resize((int(sc.width * .9), int(sc.height * .9)), Image.LANCZOS)
    im = sp(im, sc, (712, 70), off=(16, 24), blur=22, alpha=170)
    # logo vero (in alto a sinistra)
    lg = sheen(aldi_logo(144), 70)
    im = sp(im, lg, (40, 22), off=(8, 12), blur=12, alpha=170)
    # testo grande
    im = text_stroke(im, (36, 246), "BEFORE YOU", 100, (255, 255, 255), stroke=14, anchor="l", w="Black")
    im = text_stroke(im, (36, 372), "SHOP AT ALDI", 100, AYEL, stroke=14, anchor="l", w="Black")
    # freccia blu Aldi che indica il quarto
    im = sp(im, fat_arrow(290, 150, ABLUE, 12), (470, 428), off=(10, 14), blur=12, alpha=160)
    # striscia bianca + targhetta rossa
    wb = white_band("10 RULES FROM ALDI'S OWN PAGES", 1210, 100, 55, tag="NO TRICKS")
    im = sp(im, wb, (35, 568), off=(0, 10), blur=12, alpha=170)
    return im


if __name__ == "__main__":
    for name, fn in (("a", thumb_a), ("b", thumb_b)):
        fn().save(f"{OUT}/aldi-miniatura-{name}.png"); print("ok", name)
