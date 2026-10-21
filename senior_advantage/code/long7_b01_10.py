"""Video lungo 7 (AIUTI IN CASA, INVERNO) - blocchi 1-10. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-CASA-INVERNO.md.
Durate dalla timeline dell'utente (20/10/2026): B1 892, B2 868, B3 939, B4 814, B5 855, B6 965, B7 869, B8 905, B9 951, B10 872.
Layout NUOVI rispetto ai video precedenti: casa in sezione, facciata di finestre, trittico, porta, sigilli, guida numerata sul lato (1-9).
Uso: OUT=cartella python3 long7_b01_10.py <blocco> [fotogrammi]
     python3 long7_b01_10.py frame <blocco> <secondi> <file.png>"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long4_b01_10 import *      # 1920x1080, motore, sprite comuni, ic_*, stamp, banner, panel, txt, seq, slide_in, ban, sprite, common
from long6_b01 import portrait

DUR = {1: 892, 2: 868, 3: 939, 4: 814, 5: 855, 6: 965, 7: 869, 8: 905, 9: 951, 10: 872}
PHRASES = {
    1: ["It's January.", "It's nine degrees outside,", "and at two in the morning the furnace goes quiet.",
        "You're over sixty, you live on a fixed income,", "and the first thing you think is, I can't afford this.",
        "But all across the country, there are people whose job is to help with exactly this moment,",
        "and with eight other problems at home this winter.", "Most seniors never call them.",
        "Not because they don't qualify, but because nobody ever told them these people exist."],
    2: ["Today I'll show you nine kinds of help that can come to your home this winter if you're over sixty.",
        "One of them installs smoke alarms in your house at no charge.", "One brings a hot meal to your door.",
        "One can help protect your heat from being shut off.",
        "And number nine is for that night in January, when the furnace stops.",
        "Keep it in mind, because it's the most expensive problem on this whole list,",
        "and the one people pay for most often without asking."],
    3: ["Now, some of you are thinking, this is only for people with no money at all.",
        "Others are thinking, I'm fine, I don't need anybody in my house.", "Stay with me.",
        "Several of these start with your age, not your bank account.",
        "And for some of them, by federal law, nobody can turn you away just because you didn't give a donation.",
        "And if you rent, don't click away.",
        "Most of these work for renters too, and one of them can even help you deal with a landlord who won't fix the heat."],
    4: ["Stay until the end, because there is one phone call that opens the door to most of what's in this video.",
        "It's the same call for most of these nine, and making it doesn't cost you anything.",
        "Most people only find out about it after a hard winter, when they've already paid.",
        "At the end, I'll give you the number, and the exact sentence to say when someone answers,",
        "so you don't have to explain your whole life to a stranger on the phone."],
    5: ["Everything here comes from official pages.",
        "The Administration for Community Living, the U S Department of Energy, the U S Fire Administration, the American Red Cross,",
        "the federal law called the Older Americans Act, and the national groups that run these programs.",
        "I'm not paid by any of them.",
        "And rules change from state to state and from town to town,",
        "so always check with your local office before you count on anything you hear in this video."],
    6: ["Number one. A smoke alarm, installed in your home, at no charge.",
        "The American Red Cross runs a program where volunteers come to your house, install smoke alarms for free,",
        "and help you make a plan to get out if there's ever a fire.",
        "Why does this matter so much after sixty?",
        "Because the U S Fire Administration says people sixty five and older are two and a half times more likely to die in a fire than the general population.",
        "At eighty five and older, it's more than three times."],
    7: ["The Red Cross says working smoke alarms can cut the risk of dying in a home fire by half.",
        "Here's the mistake. Many seniors have an alarm on the ceiling that stopped working years ago.",
        "Or they took the battery out because it kept beeping, and they can't climb a ladder to fix it.",
        "That's exactly who this visit is for.",
        "And winter is when it matters most, because that's when the heaters, the blankets and the candles come out, and the windows stay closed."],
    8: ["Your action. Go to sound the alarm dot org, type your zip code, and sign up for a home fire safety visit from your local Red Cross.",
        "If you don't use the internet, ask a family member or a neighbor to do it with you.",
        "Availability depends on where you live, so if there's nothing near you today, check again in a few weeks.",
        "And while the volunteers are in your home, ask them to test every alarm you already have, and to show you the fastest way out of each room."],
    9: ["Number two. Help with the housework.",
        "Through your local Area Agency on Aging, many areas offer what's called homemaker help, for people sixty and older.",
        "Someone comes to your home and helps with things like laundry, washing the dishes and light housekeeping.",
        "For a lot of people, this small help is the difference between staying in their own home and having to leave it.",
        "And most families never hear that it exists until a doctor or a social worker mentions it, often too late."],
    10: ["Number three. Help with the heavy jobs.",
         "The same offices often have what's called chore help.",
         "That's the heavier work, like deep cleaning, hauling things out of the house, or washing the windows.",
         "These are exactly the jobs that cause falls, when you try to do them alone on a step stool.",
         "What's offered depends on your local agency, so ask exactly what they cover in your area, how often someone can come, and how long the waiting list is right now."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

SNOW = (228, 236, 240)
NIGHT = (14, 30, 54)
WOOD = (110, 78, 54)
CREAM = (214, 190, 150)
CONC = (62, 70, 82)
GREEN_OK = (110, 200, 130)

# ------------------------------------------------------------------ utilita comuni
def ap(img, t, t0, spr, cx, cy, scale=1.0, shadow=0, rot=0.0, t_out=None, dur=0.45, dx=0, dy=0, pop_=True):
    """compare a t0 (pop o scivolamento), sparisce a t_out"""
    if t < t0:
        return 0.0
    if pop_:
        s, a, p = pop(t, t0, dur); ox = oy = 0
    else:
        p = ease(seg(t, t0, dur)); s = 1.0; a = min(1.0, p * 2.5); ox, oy = dx * (1 - p), dy * (1 - p)
    fo = 1.0
    if t_out is not None:
        fo = 1 - ease(seg(t, t_out, 0.35))
        if fo <= 0:
            return 0.0
    put(img, spr, cx + ox, cy + oy, scale=scale * s, alpha=a * fo, shadow=shadow, rot=rot)
    return p

def fit(s, size, maxw, col=IVORY, track=0):
    """sprite di testo che sta dentro maxw"""
    while True:
        sp = txt(s, size, col, track)
        if sp.width - int(size * 0.35) * 2 <= maxw or size <= 16:
            return sp
        size -= 2

def tag(text, w, h, fill, ink, size=None, border=None, track=2):
    return pill_spr(text, size or int(h * 0.46), w, h, fill, ink, border=border, track=track)

def card(key, w, h, icon, lines, col=GOLD, size=38, fill=PANEL_FILL, ih=0.52, ink=IVORY, ink2=None):
    """scheda con icona in alto e 1-3 righe di testo"""
    def mk():
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 30, fill=fill, outline=col, width=6)
        if icon:
            icon(c, w / 2, h * ih * 0.58)
        n = len(lines)
        y0 = h * (0.20 + 0.76 * ih) if icon else h / 2 - (n - 1) * size * 0.6
        for i, ln in enumerate(lines):
            colr = ink if (ink2 is None or i < n - 1) else ink2
            s_ = size
            while tw(ln, s_, 2) > w - 50 and s_ > 16:
                s_ -= 2
            c.text((w / 2, y0 + i * size * 1.22), ln, FONT_SANS, s_, colr, track=2)
        return c.done()
    return cache(("card7", key, w, h), mk)

def tw(s, size, track=0):
    f = font(FONT_SANS, int(size * 2))
    d0 = ImageDraw.Draw(Image.new("L", (4, 4)))
    return sum(d0.textlength(ch, font=f) for ch in s) / 2 + track * max(0, len(s) - 1)

def lerp(a, b, p):
    return a + (b - a) * p

# ------------------------------------------------------------------ icone nuove
def ic_wrench(c, cx, cy, s, col=SAGE):
    c.line([(cx - 26 * s, cy + 26 * s), (cx + 14 * s, cy - 14 * s)], col, 12 * s)
    c.ell((cx + 4 * s, cy - 36 * s, cx + 38 * s, cy - 2 * s), outline=col, width=9 * s)
    c.poly([(cx + 18 * s, cy - 38 * s), (cx + 40 * s, cy - 38 * s), (cx + 24 * s, cy - 18 * s)], fill=PANEL_FILL)

def ic_alarm_ceiling(c, cx, cy, s, on=True):
    c.ell((cx - 46 * s, cy - 46 * s, cx + 46 * s, cy + 46 * s), fill=IVORY, outline=(190, 184, 170), width=5)
    c.ell((cx - 30 * s, cy - 30 * s, cx + 30 * s, cy + 30 * s), outline=(200, 196, 184), width=3)
    c.ell((cx - 10 * s, cy - 10 * s, cx + 10 * s, cy + 10 * s), fill=(214, 108, 96) if on else (150, 150, 146))
    for k in range(4):
        a = math.radians(45 + 90 * k)
        c.ell((cx + 22 * s * math.cos(a) - 3 * s, cy + 22 * s * math.sin(a) - 3 * s,
               cx + 22 * s * math.cos(a) + 3 * s, cy + 22 * s * math.sin(a) + 3 * s), fill=(150, 150, 146))

def ic_meal(c, cx, cy, s):
    c.ell((cx - 52 * s, cy - 8 * s, cx + 52 * s, cy + 40 * s), fill=IVORY, outline=(190, 184, 170), width=4)
    c.ell((cx - 36 * s, cy - 2 * s, cx + 36 * s, cy + 28 * s), fill=(220, 150, 80))
    for dx in (-20, 0, 20):
        c.arc((cx + dx * s - 8 * s, cy - 56 * s, cx + dx * s + 8 * s, cy - 14 * s), 270, 90, SAGE, 5 * s)

def ic_shield_heat(c, cx, cy, s):
    c.poly([(cx, cy - 56 * s), (cx + 46 * s, cy - 36 * s), (cx + 42 * s, cy + 14 * s), (cx, cy + 58 * s),
            (cx - 42 * s, cy + 14 * s), (cx - 46 * s, cy - 36 * s)], fill=GREEN_OK)
    ic_flame(c, cx, cy + 2 * s, 0.42 * s)

def ic_furnace(c, cx, cy, s, flame=True):
    c.rrect((cx - 56 * s, cy - 56 * s, cx + 56 * s, cy + 56 * s), 12 * s, fill=(130, 138, 150), outline=(86, 92, 104), width=4)
    c.rrect((cx - 34 * s, cy - 24 * s, cx + 34 * s, cy + 34 * s), 8 * s, fill=(28, 28, 32), outline=(190, 190, 196), width=3)
    if flame:
        ic_flame(c, cx, cy + 8 * s, 0.36 * s)
    c.line([(cx - 20 * s, cy - 40 * s), (cx + 20 * s, cy - 40 * s)], (96, 104, 116), 6 * s)

def ic_snowflake(c, cx, cy, s, col=ICE):
    for k in range(3):
        a = math.radians(60 * k)
        dx, dy = math.cos(a) * 30 * s, math.sin(a) * 30 * s
        c.line([(cx - dx, cy - dy), (cx + dx, cy + dy)], col, 6 * s)

def fade_alpha(t, t0, t_out=None, dur=0.4):
    a = ease(seg(t, t0, dur))
    if t_out is not None:
        a *= 1 - ease(seg(t, t_out, 0.35))
    return a

# ============================================================ BLOCCO 1 - casa in sezione + termometro + mappa
HOX, HOY = 140, 200       # angolo in alto a sinistra dello sprite casa (960x800)

def house_bg():
    def fn(c):
        Wd, Hd = 960, 800
        c.rrect((0, 0, Wd, Hd), 40, fill=NIGHT, outline=SAGE_D, width=5)
        rnd = random.Random(4)
        for i in range(30):
            x = rnd.uniform(40, 920); y = rnd.uniform(26, 260); r = rnd.choice([2, 3, 3, 4])
            c.ell((x - r, y - r, x + r, y + r), fill=(236, 230, 200))
        c.ell((640, 50, 720, 130), fill=(240, 236, 214)); c.ell((664, 42, 746, 124), fill=NIGHT)
        c.rrect((4, 650, Wd - 4, Hd - 4), 36, fill=SNOW)
        c.d.rectangle(c._b((4, 650, Wd - 4, 700)), fill=SNOW)
        # tetto con neve + camino
        c.rrect((560, 108, 612, 210), 6, fill=(120, 78, 66))
        c.rrect((552, 98, 620, 122), 6, fill=SNOW)
        c.poly([(76, 266), (405, 92), (734, 266)], fill=(64, 76, 100))
        c.poly([(76, 266), (405, 92), (734, 266), (702, 266), (405, 128), (108, 266)], fill=SNOW)
        # pareti e piani
        c.rrect((104, 262, 706, 650), 8, fill=WOOD)
        c.rrect((130, 282, 680, 456), 6, fill=CREAM)
        c.rrect((130, 470, 680, 632), 6, fill=CONC)
        c.rrect((120, 456, 690, 470), 3, fill=(80, 56, 40))
        # finestra
        c.rrect((548, 310, 664, 426), 8, fill=IVORY)
        c.rrect((558, 320, 654, 416), 4, fill=(24, 44, 80))
        c.line([(606, 320), (606, 416)], IVORY, 6); c.line([(558, 368), (654, 368)], IVORY, 6)
        for (x, y) in ((572, 336), (630, 346), (580, 392), (636, 396), (600, 352)):
            c.ell((x - 3, y - 3, x + 3, y + 3), fill=SNOW)
        # letto
        c.rrect((160, 380, 440, 456), 14, fill=(150, 90, 86))
        c.rrect((160, 360, 232, 392), 14, fill=IVORY)
        c.rrect((160, 400, 440, 456), 14, fill=(176, 104, 98))
        c.rrect((152, 372, 166, 456), 5, fill=(80, 56, 40))
        c.rrect((222, 488, 358, 626), 14, fill=(132, 140, 152), outline=(86, 92, 104), width=5)
        c.rrect((248, 520, 332, 596), 10, fill=(26, 26, 30), outline=(196, 196, 202), width=4)
        c.rrect((256, 498, 324, 512), 5, fill=(96, 104, 116))
        # condotto e termostato
        c.rrect((420, 520, 660, 556), 10, fill=(104, 112, 124))
        for x in (470, 540, 610):
            c.rrect((x, 556, x + 34, 584), 4, fill=(86, 92, 104))
        c.ell((590, 488, 628, 526), fill=IVORY, outline=(150, 150, 146), width=3)
        # fondazione
        c.rrect((96, 632, 714, 654), 6, fill=(70, 74, 84))
    return sprite("house7", 960, 800, fn)

def thermo(q):
    def fn(c):
        temp = q / 2.0
        c.rrect((60, 20, 120, 470), 30, fill=IVORY, outline=SAGE_D, width=4)
        c.ell((34, 424, 146, 536), fill=IVORY, outline=SAGE_D, width=4)
        c.ell((52, 442, 128, 518), fill=ICE)
        top = 470 - (max(0.0, temp) / 30.0) * 400
        c.rrect((78, top, 102, 486), 12, fill=ICE)
        for k in (0, 10, 20, 30):
            y = 470 - 400 * k / 30
            c.line([(124, y), (146, y)], SAGE, 4)
            c.text((176, y), str(k), FONT_SANS_M, 26, SAGE)
    return sprite(("thermo7", q), 210, 560, fn)

def flame_spr():
    return sprite("flame7", 160, 180, lambda c: ic_flame(c, 80, 100, 1.15))

def digital_clock():
    def fn(c):
        w, h = 270, 110
        c.rrect((4, 4, w - 4, h - 4), 20, fill=(20, 20, 24), outline=(120, 120, 128), width=5)
        c.text((w / 2 - 28, h / 2 + 2), "2:00", FONT_SANS, 62, (232, 90, 80), track=2)
        c.text((w - 52, h / 2 + 12), "AM", FONT_SANS, 28, (232, 90, 80))
    return sprite("clock7", 270, 110, fn)

def us_map():
    pts = [(-124.7, 48.4), (-123.0, 49.0), (-95.2, 49.0), (-94.6, 48.7), (-89.6, 48.0), (-84.8, 46.5), (-82.5, 45.3), (-82.4, 43.0),
           (-79.0, 43.3), (-76.5, 43.6), (-74.7, 45.0), (-71.5, 45.0), (-69.2, 47.4), (-67.8, 47.0), (-67.0, 44.8), (-70.2, 43.6),
           (-70.8, 42.5), (-70.0, 41.7), (-73.7, 41.0), (-74.0, 40.5), (-74.0, 39.3), (-75.5, 38.4), (-75.9, 37.0), (-75.5, 35.3),
           (-77.0, 34.6), (-79.0, 33.5), (-81.0, 32.0), (-81.4, 30.4), (-80.0, 26.8), (-80.4, 25.2), (-81.2, 25.2), (-82.7, 27.5),
           (-82.7, 29.0), (-84.0, 30.1), (-86.5, 30.4), (-89.0, 30.2), (-89.6, 29.0), (-91.5, 29.3), (-94.0, 29.6), (-97.0, 27.8),
           (-97.2, 25.9), (-99.2, 26.5), (-101.0, 29.8), (-104.5, 29.6), (-106.5, 31.8), (-108.2, 31.8), (-111.0, 31.3),
           (-114.8, 32.5), (-117.1, 32.5), (-118.5, 34.0), (-120.6, 34.6), (-121.9, 36.6), (-123.0, 38.0), (-124.3, 40.4),
           (-124.2, 43.0), (-124.1, 46.2)]
    return pts

def map_xy(lon, lat, k=11.6):
    return (lon + 125) * 0.788 * k, (49.5 - lat) * k

def map_sprite():
    def fn(c):
        pts = [map_xy(lo, la) for lo, la in us_map()]
        c.poly(pts, fill=(34, 92, 72))
        c.line(pts + [pts[0]], SAGE_D, 4)
    return sprite("usmap7", 560, 310, fn)

PINS = [(-122.3, 47.6), (-118.2, 34.0), (-105.0, 39.7), (-96.8, 32.8), (-93.3, 45.0), (-87.6, 41.9), (-84.4, 33.7), (-74.0, 40.7), (-80.2, 25.8), (-71.0, 42.4)]

def pin_spr():
    return sprite("pin7", 90, 110, lambda c: (ic_pin(c, 45, 50, 0.9, GOLD)))

def thought(w, h, lines, size, key):
    def mk():
        c = Cv(w, h + 120)
        # tail verso l'alto-sinistra
        c.ell((40, 94, 84, 138), fill=IVORY, outline=GOLD, width=5)
        c.ell((14, 44, 40, 70), fill=IVORY, outline=GOLD, width=4)
        c.ell((0, 8, 14, 22), fill=IVORY, outline=GOLD, width=3)
        c.rrect((6, 120, w - 6, h + 114), 60, fill=IVORY, outline=GOLD, width=7)
        n = len(lines)
        for i, ln in enumerate(lines):
            c.text((w / 2, 120 + (h - 6) / 2 + (i - (n - 1) / 2) * size * 1.2), ln, FONT_SANS, size, DARK, track=2)
        return c.done()
    return cache(("thought7", key, w, h), mk)

def draw1(img, t):
    ts = starts(1)
    common(img, t, "A COLD NIGHT AT HOME")
    ap(img, t, 0.1, house_bg(), HOX + 480, HOY + 400, dx=-70, pop_=False, dur=0.8, shadow=18)
    # 1 gennaio
    ap(img, t, ts[0], tag("JANUARY", 280, 76, GOLD, GREEN_D, 40, track=4), 330, 262, shadow=8)
    # 2 termometro che scende a 9
    if t >= ts[1]:
        p = ease(seg(t, ts[1], 0.5))
        temp = lerp(26, 9, ease(seg(t, ts[1] + 0.3, 1.3)))
        q = int(round(temp * 2))
        put(img, thermo(q), 985, 650, alpha=p, shadow=8)
        put(img, txt("%d°F" % int(round(temp)), 70, ICE, 1), 985, 270, alpha=p)
        put(img, txt("OUTSIDE", 26, SAGE, 4), 985, 330, alpha=p)
    # 3 ore 2 di notte, il forno si spegne
    ap(img, t, ts[2], digital_clock(), 475, 528, scale=0.74, shadow=8)
    ap(img, t, ts[2] + 0.2, tag("FURNACE", 210, 56, IVORY, GREEN_D, 28, track=3), 430, 700, shadow=6)
    off_t = ts[2] + 1.6
    if 0.9 <= t < off_t:
        put(img, flame_spr(), 430, 772, scale=0.42 + 0.03 * math.sin(t * 14), alpha=ease(seg(t, 0.9, 0.3)))
    else:
        k = 1 - ease(seg(t, off_t, 0.5))
        if k > 0:
            put(img, flame_spr(), 430, 772, scale=0.42 * k, alpha=k)
    if t >= off_t:
        s_, a_, p_ = pop(t, off_t + 0.3, 0.45)
        put(img, stamp("OFF", 190, 80, RED, 44), 590, 800, scale=s_, alpha=a_, rot=-8, shadow=8)
    # colonna destra A: il pensiero
    tA = ts[5]
    pr = portrait("man", "sad")
    ap(img, t, ts[3], pr, 1300, 380, scale=0.95, shadow=14, t_out=tA)
    ap(img, t, ts[3] + 0.3, tag("OVER 60", 400, 80, IVORY, GREEN_D, 40, border=GOLD, track=3), 1655, 330, shadow=8, t_out=tA)
    ap(img, t, ts[3] + 0.6, tag("FIXED INCOME", 400, 80, IVORY, GREEN_D, 40, border=GOLD, track=3), 1655, 440, shadow=8, t_out=tA)
    ap(img, t, ts[4], thought(640, 200, ["I CAN'T", "AFFORD THIS"], 58, "afford"), 1500, 740, shadow=12, t_out=tA)
    # colonna destra B: le persone che aiutano
    if t >= ts[5]:
        ap(img, t, ts[5] + 0.2, panel(700, 400, border=GOLD), 1500, 360, pop_=False, dx=60, dur=0.6, shadow=14)
        mx0, my0 = 1500 - 280, 360 - 135
        ap(img, t, ts[5] + 0.5, map_sprite(), 1500, 398, pop_=False, dy=20, dur=0.5)
        ap(img, t, ts[5] + 0.7, txt("PEOPLE WHOSE JOB IS TO HELP", 30, GOLD, 3), 1500, 200)
        for i, (lo, la) in enumerate(PINS):
            x, y = map_xy(lo, la)
            tp = ts[5] + 0.9 + i * 0.28
            ap(img, t, tp, pin_spr(), 1500 - 280 + x, 398 - 155 + y - 18, scale=0.62, dur=0.4)
            if tp <= t < tp + 0.6:
                a = (t - tp) / 0.6
                r = 10 + 40 * a
                put(img, sprite(("ring7"), 130, 130, lambda c: c.ell((6, 6, 124, 124), outline=GOLD, width=6)), 1500 - 280 + x, 398 - 155 + y,
                    scale=r / 60, alpha=1 - a)
    t6 = ts[6]
    if t >= t6:
        ap(img, t, t6, txt("THIS MOMENT + 8 OTHER PROBLEMS", 28, SAGE, 3), 1500, 618)
        for i in range(9):
            cx_ = 1500 + (i - 4) * 78
            if i == 0:
                spr = sprite("dotf7", 74, 74, lambda c: (c.ell((2, 2, 72, 72), fill=GOLD), ic_flame(c, 37, 40, 0.36, GREEN_D, GOLD)))
            else:
                spr = sprite("dotw7", 74, 74, lambda c: (c.ell((2, 2, 72, 72), fill=CARD, outline=SAGE_D, width=4), ic_wrench(c, 37, 38, 0.46)))
            ap(img, t, t6 + 0.4 + i * 0.12, spr, cx_, 680, dur=0.35)
    t7 = ts[7]
    if t >= t7:
        ap(img, t, t7, sprite("phx7", 200, 180, lambda c: (ic_phone(c, 100, 90, 1.25), ic_x(c, 140, 120, 1.5))), 1250, 810, shadow=8)
        ap(img, t, t7 + 0.3, txt("MOST SENIORS", 40, IVORY, 3), 1560, 785)
        ap(img, t, t7 + 0.45, txt("NEVER CALL", 40, GOLD, 3), 1560, 840)
    t8 = ts[8]
    ban(img, t, t8, "NOBODY EVER TOLD THEM", cy=958, cx=1500, w=700, h=92, size=40)


def tsub(b, i, k):
    """secondo in cui la voce arriva al carattere k della frase i (voce circa 96% del blocco)"""
    ph = PHRASES[b]; tot = sum(len(p_) for p_ in ph); dur = DUR[b] / FPS * 0.96
    return starts(b)[i] + k * dur / tot

def ic_lock(c, cx, cy, s, col=GOLD):
    c.arc((cx - 18 * s, cy - 44 * s, cx + 18 * s, cy + 6 * s), 180, 360, col, 9 * s)
    c.rrect((cx - 28 * s, cy - 6 * s, cx + 28 * s, cy + 42 * s), 8 * s, fill=col)
    c.ell((cx - 6 * s, cy + 8 * s, cx + 6 * s, cy + 20 * s), fill=GREEN_D)
    c.rrect((cx - 2.5 * s, cy + 16 * s, cx + 2.5 * s, cy + 30 * s), 2, fill=GREEN_D)

def ic_key(c, cx, cy, s, col=GOLD):
    c.ell((cx - 44 * s, cy - 20 * s, cx - 4 * s, cy + 20 * s), outline=col, width=10 * s)
    c.line([(cx - 4 * s, cy), (cx + 44 * s, cy)], col, 10 * s)
    c.line([(cx + 28 * s, cy), (cx + 28 * s, cy + 18 * s)], col, 9 * s)
    c.line([(cx + 44 * s, cy), (cx + 44 * s, cy + 14 * s)], col, 9 * s)

# ============================================================ BLOCCO 2 - il 9 e le quattro schede
def big9():
    def fn(c):
        S = 480
        c.ell((10, 10, S - 10, S - 10), fill=GREEN_L, outline=GOLD, width=10)
        c.ell((34, 34, S - 34, S - 34), outline=SAGE_D, width=4)
        c.text((S / 2, S / 2 + 14), "9", FONT_SANS, 330, GOLD)
    return sprite("big9_7", 480, 480, fn)

def draw2(img, t):
    ts = starts(2)
    common(img, t, "NINE KINDS OF HELP AT HOME")
    ap(img, t, ts[0], big9(), 450, 470, shadow=16, dur=0.6)
    if ts[0] < t < ts[0] + 0.9:
        burst(img, t, ts[0] + 0.15, 450, 470, n=14, color=GOLD, rad=300, seed=2)
    ap(img, t, ts[0] + 0.5, txt("KINDS OF HELP", 56, IVORY, 4), 450, 765)
    ap(img, t, ts[0] + 0.7, txt("AT HOME THIS WINTER", 38, SAGE, 3), 450, 830)
    ap(img, t, ts[0] + 1.0, tag("IF YOU'RE OVER 60", 440, 74, GOLD, GREEN_D, 34, track=3), 450, 925, shadow=8)
    CW, CH = 500, 400
    c1 = card("c2a", CW, CH, lambda c, x, y: ic_alarm_ceiling(c, x, y, 1.7), ["SMOKE ALARMS", "INSTALLED", "AT NO CHARGE"], SAGE_D, 42, ink=IVORY, ink2=SAGE)
    c2 = card("c2b", CW, CH, lambda c, x, y: ic_meal(c, x, y + 6, 1.6), ["A HOT MEAL", "AT YOUR DOOR"], SAGE_D, 44, ink=IVORY, ink2=SAGE)
    c3 = card("c2c", CW, CH, lambda c, x, y: ic_shield_heat(c, x, y, 1.45), ["HELP PROTECT", "YOUR HEAT FROM", "BEING SHUT OFF"], SAGE_D, 42, ink=IVORY, ink2=SAGE)
    c4 = card("c2d", CW, CH, lambda c, x, y: (ic_furnace(c, x - 56, y + 6, 1.3, False), ic_snowflake(c, x + 86, y - 14, 1.7)),
              ["NUMBER 9", "THE FURNACE STOPS"], GOLD, 46, ink=GOLD, ink2=IVORY)
    ap(img, t, ts[1], c1, 1070, 350, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[2], c2, 1620, 350, pop_=False, dx=50, dur=0.6, shadow=12)
    ap(img, t, ts[3], c3, 1070, 790, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[4], c4, 1620, 790, pop_=False, dx=50, dur=0.6, shadow=14)
    if ts[4] + 0.3 < t < ts[4] + 1.2:
        burst(img, t, ts[4] + 0.3, 1620, 790, n=12, color=GOLD, rad=230, seed=5)
    ap(img, t, ts[5], tag("MOST EXPENSIVE ON THE LIST", 460, 60, GOLD, GREEN_D, 26, border=(168, 118, 40), track=2), 1620, 590, shadow=8)
    ap(img, t, ts[6], tag("PAID WITHOUT ASKING", 420, 64, CORAL, IVORY, 28, track=3), 1620, 990, shadow=8)

# ============================================================ BLOCCO 3 - trittico: cosa pensi / cosa conta / affittuari
def id_card7(key, text, big, sub, ok=True, tsize=34):
    def fn(c):
        w, h = 470, 140
        col = IVORY if ok else (70, 98, 88)
        c.rrect((4, 4, w - 4, h - 4), 24, fill=col, outline=GOLD if ok else SAGE_D, width=6)
        c.ell((24, 26, 100, 102), fill=GREEN_D if ok else (62, 90, 80))
        c.text((62, 64), big, FONT_SANS, 30, GOLD if ok else (190, 206, 196), track=0)
        c.text((124, 52), sub, FONT_SANS_M, 24, GREEN_D if ok else (214, 226, 218), anchor="lm", track=2)
        c.text((124, 92), text, FONT_SANS, tsize, GREEN_D if ok else (214, 226, 218), anchor="lm", track=1)
        if ok:
            c.ell((384, 40, 444, 100), fill=GREEN_OK); check_ic(c, 414, 70, 0.7, GREEN_D)
        else:
            c.line([(18, 122), (w - 18, 18)], CORAL, 9)
    return sprite(("id7", key, ok), 470, 140, fn)

def jar7():
    def fn(c):
        c.rrect((40, 56, 160, 216), 30, fill=(188, 226, 226), outline=IVORY, width=6)
        c.rrect((40, 56, 160, 120), 30, fill=(214, 240, 240))
        c.rrect((52, 28, 148, 66), 12, fill=GOLD, outline=(168, 118, 40), width=4)
        c.rrect((84, 40, 116, 48), 4, fill=(168, 118, 40))
        c.text((100, 146), "$", FONT_SANS, 70, (120, 160, 160))
    return sprite("jar7", 200, 240, fn)

def apartment7():
    def fn(c):
        c.rrect((40, 40, 260, 260), 10, fill=(176, 112, 90), outline=(120, 76, 62), width=5)
        for r_ in range(3):
            for k in range(3):
                lit = (r_, k) == (1, 1)
                c.rrect((66 + k * 62, 62 + r_ * 56, 100 + k * 62, 100 + r_ * 56), 5, fill=(255, 226, 150) if lit else (60, 78, 110))
        c.rrect((124, 200, 176, 260), 6, fill=(104, 66, 52))
        c.rrect((28, 258, 272, 274), 5, fill=(80, 56, 40))
    return sprite("apt7", 300, 290, fn)

def radiator7():
    def fn(c):
        for k in range(7):
            c.rrect((20 + k * 32, 66, 46 + k * 32, 176), 12, fill=(206, 210, 216), outline=(150, 156, 166), width=3)
        c.rrect((12, 54, 248, 74), 8, fill=(186, 192, 200)); c.rrect((12, 168, 248, 188), 8, fill=(186, 192, 200))
        ic_snowflake(c, 130, 24, 0.9)
    return sprite("rad7", 260, 200, fn)

def col_panel(h=800):
    return panel(560, h, border=SAGE_D)

def draw3(img, t):
    ts = starts(3)
    common(img, t, "TWO THOUGHTS, ONE ANSWER")
    X1, X2, X3, YC = 330, 960, 1590, 575
    for i, (x, name) in enumerate(((X1, "WHAT YOU MIGHT THINK"), (X2, "WHAT COUNTS"), (X3, "RENTERS TOO"))):
        t0 = (0.1, ts[3] - 0.2, ts[5] - 0.2)[i]
        ap(img, t, t0, col_panel(), x, YC, pop_=False, dy=40, dur=0.6, shadow=14)
        ap(img, t, t0 + 0.3, tag(name, 470, 66, GOLD, GREEN_D, 30, track=2), x, 240, shadow=6)
    # colonna 1: i due pensieri
    ap(img, t, ts[0], bubble_spr(470, 200, IVORY, ["ONLY FOR PEOPLE", "WITH NO MONEY", "AT ALL"], DARK, 40), X1, 410, shadow=10)
    ap(img, t, ts[1], bubble_spr(470, 200, IVORY, ["I'M FINE. I DON'T", "NEED ANYBODY", "IN MY HOUSE"], DARK, 40), X1, 675, shadow=10)
    ap(img, t, ts[2], tag("STAY WITH ME", 380, 70, GOLD, GREEN_D, 34, track=3), X1, 905, shadow=8)
    # colonna 2: eta' vs conto in banca, donazione
    ap(img, t, ts[3], id_card7("age", "YOUR AGE", "60+", "IT STARTS WITH"), X2, 365, pop_=False, dx=0, dy=-30, dur=0.5, shadow=8)
    ap(img, t, ts[3] + 1.4, id_card7("bank", "YOUR BANK ACCOUNT", "$", "NOT", ok=False, tsize=25), X2, 520, pop_=False, dy=-30, dur=0.5, shadow=8, scale=1.0)
    ap(img, t, ts[4], tag("BY FEDERAL LAW", 340, 56, IVORY, GREEN_D, 26, border=GOLD, track=2), X2, 640, shadow=6)
    ap(img, t, ts[4] + 0.4, jar7(), X2, 765, scale=0.95, shadow=8)
    ap(img, t, ts[4] + 1.0, txt("NO DONATION?", 40, GOLD, 3), X2, 900)
    ap(img, t, tsub(3, 4, 44), txt("NOBODY CAN TURN YOU AWAY", 29, IVORY, 2), X2, 945)
    # colonna 3: affittuari
    ap(img, t, ts[5], apartment7(), X3, 420, scale=0.85, shadow=8)
    ap(img, t, ts[5] + 0.5, sprite("key7", 140, 80, lambda c: ic_key(c, 70, 40, 1.0)), X3 + 125, 320, rot=-20)
    ap(img, t, ts[5] + 0.3, tag("IF YOU RENT", 340, 60, IVORY, GREEN_D, 30, border=GOLD, track=2), X3, 585, shadow=6)
    ap(img, t, ts[6], sprite("okr7", 90, 90, lambda c: (c.ell((4, 4, 86, 86), fill=GREEN_OK), check_ic(c, 45, 45, 1.0, GREEN_D))), X3 - 205, 668)
    ap(img, t, ts[6] + 0.2, txt("MOST WORK FOR", 36, IVORY, 2), X3 + 25, 664)
    ap(img, t, ts[6] + 0.35, txt("RENTERS TOO", 42, GOLD, 3), X3 + 25, 716)
    tl = tsub(3, 6, 36)
    ap(img, t, tl, radiator7(), X3, 835, scale=0.85, shadow=6)
    ap(img, t, tl + 0.5, tag("LANDLORD WON'T FIX THE HEAT", 500, 60, CORAL, IVORY, 26, track=1), X3, 950, shadow=6)

# ============================================================ BLOCCO 4 - la porta che si apre con una telefonata
def door7(q):
    def fn(c):
        p = q / 20.0
        w, h = 460, 720
        c.rrect((6, 6, w - 6, h - 6), 18, fill=(70, 50, 38), outline=(48, 34, 26), width=6)
        c.rrect((28, 28, w - 28, h - 6), 8, fill=(255, 236, 178))
        c.ell((70, 120, w - 70, h - 40), fill=(255, 246, 210))
        hx, top, bot = 44, 30, h - 8
        wl = 380 * (1 - 0.62 * p)
        d = 70 * p
        pts = [(hx, top), (hx + wl, top + d), (hx + wl, bot - d), (hx, bot)]
        c.poly(pts, fill=(150, 100, 62))
        c.poly([(hx + wl * 0.12, top + 40 + d * 0.3), (hx + wl * 0.88, top + 40 + d * 0.8), (hx + wl * 0.88, top + 290 - d * 0.3), (hx + wl * 0.12, top + 290 - d * 0.3)], fill=(176, 122, 80))
        c.poly([(hx + wl * 0.12, top + 340 + d * 0.2), (hx + wl * 0.88, top + 340 + d * 0.1), (hx + wl * 0.88, bot - 40 - d * 0.8), (hx + wl * 0.12, bot - 40 - d * 0.3)], fill=(176, 122, 80))
        c.ell((hx + wl * 0.84 - 14, 395 - 14, hx + wl * 0.84 + 14, 395 + 14), fill=GOLD)
    return sprite(("door7", q), 460, 720, fn)

def draw4(img, t):
    ts = starts(4)
    common(img, t, "ONE PHONE CALL")
    # porta (si apre durante la prima frase)
    ap(img, t, 0.1, panel(520, 800, border=GOLD), 400, 570, pop_=False, dx=-60, dur=0.6, shadow=14)
    q = int(round(20 * ease(seg(t, ts[0] + 0.5, 1.8))))
    if t > 0.5:
        put(img, door7(q), 400, 570, alpha=ease(seg(t, 0.4, 0.4)))
    # telefono con onde
    s_, a_, pp = pop(t, ts[0] + 0.2, 0.5)
    if pp > 0:
        put(img, sprite("ph4_7", 220, 300, lambda c: ic_phone(c, 110, 150, 2.0)), 400, 760, scale=s_, alpha=a_, shadow=12, rot=-12)
        for k in range(3):
            ph = ((t - ts[0]) * 1.6 + k / 3.0) % 1.0
            if t < ts[1] - 0.5:
                put(img, sprite("wv7", 200, 200, lambda c: c.arc((10, 10, 190, 190), 200, 340, GOLD, 10)), 400, 640, scale=0.5 + ph, alpha=(1 - ph) * 0.9)
    ap(img, t, 0.5, txt("ONE PHONE CALL", 104, GOLD, 4), 1300, 400, t_out=ts[1], pop_=False, dx=60, dur=0.7)
    ap(img, t, 1.0, txt("OPENS THE DOOR TO", 56, IVORY, 4), 1300, 540, t_out=ts[1], pop_=False, dx=60, dur=0.7)
    ap(img, t, 1.4, txt("MOST OF WHAT'S IN THIS VIDEO", 50, SAGE, 3), 1300, 625, t_out=ts[1], pop_=False, dx=60, dur=0.7)
    ap(img, t, ts[0] + 0.8, tag("ONE CALL OPENS THE DOOR", 500, 66, GOLD, GREEN_D, 30, track=2), 400, 960, shadow=8)
    # riga A: stessa telefonata per quasi tutti e nove
    X0 = 1300
    ap(img, t, ts[1], panel(1020, 190, border=SAGE_D), X0, 215, pop_=False, dx=50, dur=0.5, shadow=10)
    ap(img, t, ts[1] + 0.2, txt("THE SAME CALL FOR MOST OF THESE NINE", 36, IVORY, 2), X0 - 40, 158)
    for i in range(9):
        on = i < 7
        spr = sprite(("d4", on), 68, 68, lambda c, on=on: (c.ell((2, 2, 66, 66), fill=GOLD if on else CARD, outline=GOLD if on else SAGE_D, width=4),
                                                           check_ic(c, 34, 34, 0.5, GREEN_D) if on else None))
        ap(img, t, ts[1] + 0.5 + i * 0.1, spr, X0 - 440 + i * 70, 225, dur=0.35)
    ap(img, t, tsub(4, 1, 52), tag("COSTS YOU NOTHING", 330, 62, GREEN_OK, GREEN_D, 22, track=1), X0 + 345, 225, shadow=6)
    # riga B: dopo un inverno duro, quando hanno gia pagato
    ap(img, t, ts[2], panel(1020, 190, border=SAGE_D), X0, 440, pop_=False, dx=50, dur=0.5, shadow=10)
    ap(img, t, ts[2] + 0.2, sprite("snowc7", 130, 130, lambda c: (c.rrect((8, 8, 122, 122), 16, fill=IVORY, outline=SAGE_D, width=4),
                                                            c.rrect((8, 8, 122, 46), 16, fill=CORAL), ic_snowflake(c, 65, 86, 1.0, (96, 150, 190)))), X0 - 440, 440)
    ap(img, t, ts[2] + 0.4, txt("AFTER A HARD WINTER", 38, IVORY, 3), X0 - 80, 440)
    ap(img, t, tsub(4, 2, 50), stamp("ALREADY PAID", 300, 90, RED, 30), X0 + 355, 440, rot=-6, shadow=8)
    # riga C: numero e frase esatta (bloccati)
    ap(img, t, ts[3], panel(1020, 215, border=GOLD), X0, 670, pop_=False, dx=50, dur=0.5, shadow=10)
    ap(img, t, ts[3] + 0.3, sprite("lk1_7", 460, 130, lambda c: (c.rrect((4, 4, 456, 126), 22, fill=IVORY),
                                                           c.text((40, 64), "THE NUMBER", FONT_SANS, 34, GREEN_D, anchor="lm", track=2),
                                                           ic_lock(c, 400, 62, 1.0, GREEN_D))), X0 - 255, 637, shadow=8)
    ap(img, t, ts[3] + 0.6, sprite("lk2_7", 460, 130, lambda c: (c.rrect((4, 4, 456, 126), 22, fill=IVORY),
                                                           c.text((34, 64), "THE EXACT SENTENCE", FONT_SANS, 30, GREEN_D, anchor="lm", track=1),
                                                           ic_lock(c, 410, 62, 1.0, GREEN_D))), X0 + 255, 637, shadow=8)
    ap(img, t, ts[3] + 0.9, txt("AT THE END OF THE VIDEO", 30, GOLD, 3), X0, 740)
    # riga D: senza dover raccontare tutta la tua vita
    ap(img, t, ts[4], sprite("chat7", 1020, 200, lambda c: (
        c.rrect((6, 6, 1014, 194), 40, fill=PANEL_FILL, outline=SAGE_D, width=5),
        c.rrect((40, 30, 300, 100), 30, fill=IVORY), c.text((170, 66), "HELLO?", FONT_SANS, 34, DARK, track=2),
        c.rrect((330, 100, 700, 170), 30, fill=(60, 110, 90)), c.text((515, 136), "NO LONG STORY", FONT_SANS, 30, IVORY, track=2),
        ic_person(c, 900, 110, 0.9, SAGE), c.text((900, 172), "A STRANGER", FONT_SANS_M, 24, SAGE, track=3))), X0, 940, pop_=False, dx=50, dur=0.5, shadow=10)


# ------------------------------------------------------------------ icone aggiuntive
def ic_heart(c, cx, cy, s, col=CORAL):
    c.ell((cx - 44 * s, cy - 40 * s, cx + 2 * s, cy + 6 * s), fill=col); c.ell((cx - 2 * s, cy - 40 * s, cx + 44 * s, cy + 6 * s), fill=col)
    c.poly([(cx - 42 * s, cy - 8 * s), (cx + 42 * s, cy - 8 * s), (cx, cy + 48 * s)], fill=col)

def ic_scroll(c, cx, cy, s, col=IVORY):
    c.rrect((cx - 34 * s, cy - 44 * s, cx + 34 * s, cy + 44 * s), 8 * s, fill=col, outline=(190, 184, 170), width=3)
    for k in range(4):
        c.line([(cx - 20 * s, cy - 26 * s + k * 16 * s), (cx + 20 * s, cy - 26 * s + k * 16 * s)], (150, 150, 146), 4 * s)
    c.ell((cx + 14 * s, cy + 20 * s, cx + 44 * s, cy + 50 * s), fill=CORAL)

def ic_people(c, cx, cy, s):
    ic_person(c, cx - 38 * s, cy + 8 * s, 0.7 * s, SAGE)
    ic_person(c, cx + 38 * s, cy + 8 * s, 0.7 * s, SAGE)
    ic_person(c, cx, cy, 0.9 * s, GOLD)

def ic_battery(c, cx, cy, s, col=GREEN_OK):
    c.rrect((cx - 44 * s, cy - 24 * s, cx + 38 * s, cy + 24 * s), 8 * s, fill=col, outline=IVORY, width=4)
    c.rrect((cx + 38 * s, cy - 10 * s, cx + 50 * s, cy + 10 * s), 3, fill=IVORY)
    c.text((cx - 4 * s, cy + 1 * s), "+", FONT_SANS, 34 * s, GREEN_D)

def ic_ladder(c, cx, cy, s, col=(190, 192, 198)):
    c.line([(cx - 34 * s, cy + 60 * s), (cx - 10 * s, cy - 62 * s)], col, 8 * s)
    c.line([(cx + 34 * s, cy + 60 * s), (cx + 10 * s, cy - 62 * s)], col, 8 * s)
    for k in range(5):
        y = cy - 40 * s + k * 26 * s
        c.line([(cx - 28 * s + k * 1.6 * s, y), (cx + 28 * s - k * 1.6 * s, y)], col, 6 * s)

def ic_heater(c, cx, cy, s):
    c.rrect((cx - 44 * s, cy - 30 * s, cx + 44 * s, cy + 40 * s), 10 * s, fill=(206, 96, 70), outline=(150, 60, 50), width=4)
    for k in range(5):
        c.line([(cx - 28 * s + k * 14 * s, cy - 14 * s), (cx - 28 * s + k * 14 * s, cy + 26 * s)], (255, 190, 120), 5 * s)
    for k in range(3):
        x0 = cx - 26 * s + k * 26 * s
        c.line([(x0, cy - 36 * s), (x0 + 8 * s, cy - 48 * s), (x0, cy - 60 * s), (x0 + 8 * s, cy - 72 * s)], (255, 190, 120), 5 * s)

def ic_blanket(c, cx, cy, s):
    c.rrect((cx - 46 * s, cy - 30 * s, cx + 46 * s, cy + 34 * s), 8 * s, fill=(176, 104, 98), outline=(120, 66, 62), width=4)
    for k in range(4):
        c.line([(cx - 46 * s, cy - 14 * s + k * 16 * s), (cx + 46 * s, cy - 14 * s + k * 16 * s)], (214, 150, 140), 4 * s)
    for k in range(5):
        c.line([(cx - 32 * s + k * 16 * s, cy - 30 * s), (cx - 32 * s + k * 16 * s, cy + 34 * s)], (150, 84, 80), 3 * s)

def ic_candle(c, cx, cy, s):
    c.rrect((cx - 18 * s, cy - 10 * s, cx + 18 * s, cy + 50 * s), 5 * s, fill=IVORY, outline=(190, 184, 170), width=3)
    c.line([(cx, cy - 10 * s), (cx, cy - 20 * s)], (60, 50, 44), 4 * s)
    ic_flame(c, cx, cy - 42 * s, 0.4 * s)

def ic_window_closed(c, cx, cy, s):
    c.rrect((cx - 40 * s, cy - 48 * s, cx + 40 * s, cy + 48 * s), 6 * s, fill=(92, 130, 168), outline=IVORY, width=6)
    c.line([(cx, cy - 48 * s), (cx, cy + 48 * s)], IVORY, 5 * s); c.line([(cx - 40 * s, cy), (cx + 40 * s, cy)], IVORY, 5 * s)
    c.ell((cx + 8 * s, cy - 4 * s, cx + 16 * s, cy + 4 * s), fill=GOLD)

# ============================================================ BLOCCO 5 - le fonti ufficiali (sigilli)
def seal_card(key, icon, l1, l2, col=GOLD):
    def mk():
        w, h = 390, 270
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 30, fill=PANEL_FILL, outline=SAGE_D, width=5)
        c.ell((195 - 66, 22, 195 + 66, 154), fill=GREEN_L, outline=col, width=7)
        c.ell((195 - 54, 34, 195 + 54, 142), outline=SAGE_D, width=3)
        icon(c, 195, 88)
        s1 = 30
        while tw(l1, s1, 2) > w - 40 and s1 > 16: s1 -= 2
        s2 = 28
        while tw(l2, s2, 2) > w - 40 and s2 > 16: s2 -= 2
        c.text((w / 2, 190), l1, FONT_SANS, s1, IVORY, track=2)
        c.text((w / 2, 232), l2, FONT_SANS, s2, GOLD, track=2)
        return c.done()
    return cache(("seal7", key), mk)

def doc7():
    def fn(c):
        w, h = 440, 640
        c.rrect((6, 6, w - 6, h - 6), 26, fill=IVORY, outline=(206, 200, 186), width=6)
        c.rrect((6, 6, w - 6, 120), 26, fill=GREEN_L)
        c.d.rectangle(c._b((6, 80, w - 6, 120)), fill=GREEN_L)
        c.text((w / 2, 48), "OFFICIAL", FONT_SANS, 44, IVORY, track=4)
        c.text((w / 2, 92), "PAGES", FONT_SANS, 40, GOLD, track=6)
        for k in range(7):
            c.rrect((46, 160 + k * 46, 46 + (340 if k % 3 != 2 else 250), 176 + k * 46), 8, fill=(206, 212, 206))
        c.ell((w / 2 - 62, 486, w / 2 + 62, 610), fill=GOLD, outline=(168, 118, 40), width=6)
        c.text((w / 2, 548), "OK", FONT_SANS, 62, GREEN_D)
    return sprite("doc7", 440, 640, fn)

def draw5(img, t):
    ts = starts(5)
    common(img, t, "WHERE THE FACTS COME FROM")
    ap(img, t, ts[0], doc7(), 335, 590, pop_=False, dx=-60, dur=0.7, shadow=14)
    ap(img, t, ts[0] + 0.7, sprite("mag7", 200, 200, lambda c: magnifier(c, 80, 80, 54, GOLD, 12)), 470, 840, shadow=8)
    P2, P3 = PHRASES[5][1], PHRASES[5][2]
    GX = (815, 1235, 1655); GY = (315, 610)
    items = [
        (tsub(5, 1, 0), "acl", lambda c, x, y: ic_house(c, x, y + 4, 1.05, IVORY, CORAL), "ADMINISTRATION FOR", "COMMUNITY LIVING"),
        (tsub(5, 1, P2.index("the U S Department")), "doe", lambda c, x, y: ic_bolt(c, x, y, 0.8), "U S DEPARTMENT", "OF ENERGY"),
        (tsub(5, 1, P2.index("the U S Fire")), "fire", lambda c, x, y: ic_flame(c, x, y + 4, 0.75), "U S FIRE", "ADMINISTRATION"),
        (tsub(5, 1, P2.index("the American")), "rc", lambda c, x, y: ic_heart(c, x, y - 2, 1.1), "AMERICAN", "RED CROSS"),
        (tsub(5, 2, 0), "oaa", lambda c, x, y: ic_scroll(c, x, y, 1.0), "OLDER AMERICANS ACT", "FEDERAL LAW"),
        (tsub(5, 2, P3.index("and the national")), "grp", lambda c, x, y: ic_people(c, x, y + 6, 1.0), "NATIONAL GROUPS", "RUNNING THE PROGRAMS"),
    ]
    for i, (tt, k, ic, l1, l2) in enumerate(items):
        ap(img, t, tt, seal_card(k, ic, l1, l2), GX[i % 3], GY[i // 3], shadow=10, dur=0.5)
    # non pagato
    ap(img, t, ts[3], sprite("np7", 540, 110, lambda c: (c.rrect((4, 4, 536, 106), 30, fill=PANEL_FILL, outline=CORAL, width=6),
                                                      ic_coin(c, 70, 55, 32), ic_x(c, 70, 55, 1.2, CORAL, 10),
                                                      c.text((120, 40), "NOT PAID BY", FONT_SANS, 32, IVORY, anchor="lm", track=2),
                                                      c.text((120, 76), "ANY OF THEM", FONT_SANS, 32, GOLD, anchor="lm", track=2))), 890, 850, shadow=8)
    # regole cambiano
    ap(img, t, ts[4], sprite("rc7", 660, 110, lambda c: (c.rrect((4, 4, 656, 106), 30, fill=PANEL_FILL, outline=GOLD, width=6),
                                                      ic_pin(c, 62, 52, 0.8, GOLD), ic_pin(c, 110, 62, 0.62, SAGE),
                                                      c.text((160, 40), "RULES CHANGE STATE TO STATE", FONT_SANS, 25, IVORY, anchor="lm", track=1),
                                                      c.text((160, 76), "AND FROM TOWN TO TOWN", FONT_SANS, 25, GOLD, anchor="lm", track=1))), 1520, 850, shadow=8)
    ban(img, t, ts[5], "ALWAYS CHECK WITH YOUR LOCAL OFFICE FIRST", cy=988, cx=1235, w=1230, h=84, size=38)

# ------------------------------------------------------------------ guida numerata 1-9 sul lato
def rail_spr(active):
    def fn(c):
        c.line([(70, 40), (70, 820)], LINE, 8)
        for i in range(9):
            y = 40 + i * 97.5
            n = i + 1
            if n == active:
                c.ell((70 - 40, y - 40, 70 + 40, y + 40), fill=GOLD, outline=IVORY, width=5)
                c.text((70, y + 3), str(n), FONT_SANS, 44, GREEN_D)
            elif n < active:
                c.ell((70 - 30, y - 30, 70 + 30, y + 30), fill=GREEN_OK, outline=GREEN_D, width=4)
                check_ic(c, 70, y, 0.6, GREEN_D)
            else:
                c.ell((70 - 30, y - 30, 70 + 30, y + 30), fill=CARD, outline=SAGE_D, width=4)
                c.text((70, y + 2), str(n), FONT_SANS, 30, SAGE_D)
    return sprite(("rail7", active), 140, 860, fn)

def rail(img, t, active, t0=0.1):
    ap(img, t, t0, rail_spr(active), 110, 570, pop_=False, dx=-60, dur=0.6, shadow=8)

# ============================================================ BLOCCO 6 - numero 1: l'allarme antifumo
def room_scene():
    def fn(c):
        w, h = 820, 460
        c.rrect((0, 0, w, h), 34, fill=(214, 190, 150), outline=SAGE_D, width=5)
        c.rrect((6, 6, w - 6, 50), 30, fill=(240, 232, 218))
        c.d.rectangle(c._b((6, 30, w - 6, 50)), fill=(240, 232, 218))
        c.rrect((6, 386, w - 6, h - 6), 30, fill=(150, 106, 70))
        c.d.rectangle(c._b((6, 386, w - 6, 420)), fill=(150, 106, 70))
        c.rrect((560, 100, 760, 290), 10, fill=IVORY); c.rrect((572, 112, 748, 278), 6, fill=(150, 205, 232))
        c.line([(660, 112), (660, 278)], IVORY, 6); c.line([(572, 195), (748, 195)], IVORY, 6)
        # scala
        lad = (190, 192, 198)
        c.line([(250, 410), (318, 150)], lad, 10); c.line([(410, 410), (342, 150)], lad, 10)
        for k in range(6):
            yy = 190 + k * 40
            c.line([(318 - (yy - 150) * 0.26 + 4, yy), (342 + (yy - 150) * 0.26 - 4, yy)], lad, 7)
        # volontario sulla scala
        c.rrect((300, 222, 360, 310), 14, fill=(236, 132, 52))
        c.rrect((300, 246, 360, 256), 2, fill=(246, 240, 150)); c.rrect((300, 276, 360, 286), 2, fill=(246, 240, 150))
        c.ell((304, 170, 356, 224), fill=SKIN)
        c.d.pieslice(c._b((300, 160, 360, 224)), 180, 360, fill=(246, 200, 60))
        c.line([(354, 236), (338, 96)], SKIN, 14)
        c.line([(312, 310), (312, 372)], (50, 70, 110), 16); c.line([(348, 310), (348, 372)], (50, 70, 110), 16)
    return sprite("room7", 820, 460, fn)

def plan_scene():
    def fn(c):
        w, h = 770, 460
        c.rrect((0, 0, w, h), 34, fill=(232, 238, 232), outline=SAGE_D, width=5)
        wall = (86, 96, 92)
        c.rrect((60, 60, 710, 400), 6, outline=wall, width=10)
        c.line([(290, 60), (290, 190)], wall, 8); c.line([(290, 250), (290, 400)], wall, 8)
        c.line([(60, 230), (200, 230)], wall, 8); c.line([(260, 230), (480, 230)], wall, 8)
        c.line([(480, 230), (480, 400)], wall, 8)
        c.rrect((84, 84, 200, 150), 8, fill=(176, 104, 98))
        c.rrect((330, 84, 440, 140), 8, fill=(200, 150, 90))
        c.rrect((500, 270, 660, 360), 8, fill=(150, 170, 190))
        c.rrect((702 - 14, 290, 718, 350), 4, fill=GREEN_OK)
        c.text((620, 422), "EXIT", FONT_SANS_M, 24, GREEN_D, track=3)
    return sprite("plan7", 770, 460, fn)

def bar7(wq, col):
    def fn(c):
        w = max(8, wq * 10)
        c.rrect((0, 0, w, 56), 16, fill=col)
    return sprite(("bar7", wq, col), max(8, wq * 10), 56, fn)

def draw6(img, t):
    ts = starts(6)
    common(img, t, "NUMBER ONE: A SMOKE ALARM")
    rail(img, t, 1)
    ap(img, t, 0.3, room_scene(), 640, 380, pop_=False, dy=40, dur=0.7, shadow=14)
    # allarme installato (appare, lampeggia)
    ta = ts[0] + 1.2
    if t >= ta:
        s_, a_, pp = pop(t, ta, 0.5)
        put(img, sprite("al6_7", 120, 120, lambda c: ic_alarm_ceiling(c, 60, 60, 1.0)), 568, 210, scale=s_ * 0.8, alpha=a_, shadow=6)
        if int(t * 2) % 2 == 0 or t > ts[1]:
            put(img, sprite("led7", 40, 40, lambda c: c.ell((6, 6, 34, 34), fill=(250, 80, 70))), 568, 210, scale=0.5, alpha=0.9)
    ap(img, t, ts[0] + 0.8, tag("NO CHARGE", 250, 66, GOLD, GREEN_D, 34, track=3), 900, 215, shadow=8, rot=6)
    ap(img, t, ts[1], tag("VOLUNTEERS COME TO YOUR HOUSE", 640, 62, IVORY, GREEN_D, 28, border=GOLD, track=2), 640, 600, shadow=8)
    ap(img, t, ts[2], plan_scene(), 1475, 380, pop_=False, dx=60, dur=0.6, shadow=14)
    tp = ts[2] + 0.9
    ap(img, t, tp, sprite("fl6_7", 100, 110, lambda c: ic_flame(c, 50, 60, 0.7)), 1230, 330, shadow=4)
    if t >= tp + 0.5:
        p_ = ease(seg(t, tp + 0.5, 1.4))
        pts = [(1250, 335), (1250, 450), (1500, 450), (1500, 540), (1760, 540)]
        # percorso tratteggiato verso l'uscita
        n = len(pts); total = sum(math.dist(pts[i], pts[i + 1]) for i in range(n - 1)); dist = total * p_; acc = 0
        for i in range(n - 1):
            L = math.dist(pts[i], pts[i + 1])
            if acc >= dist: break
            seg_len = min(L, dist - acc)
            for k in range(int(seg_len // 26)):
                f = (k * 26 + 8) / L
                x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f; y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f
                put(img, dot_spr(GREEN_OK, 7), x, y)
            acc += L
    ap(img, t, tp + 0.3, tag("A PLAN TO GET OUT", 440, 62, IVORY, GREEN_D, 28, border=GOLD, track=2), 1475, 600, shadow=8)
    # statistiche
    ap(img, t, ts[3], panel(1630, 370, border=GOLD), 1045, 835, pop_=False, dy=40, dur=0.6, shadow=14)
    ap(img, t, ts[3] + 0.3, txt("PEOPLE 65 AND OLDER VS A FIRE", 36, GOLD, 3), 1045, 700)
    rows = [("GENERAL POPULATION", 1.0, SAGE, "1×", tsub(6, 4, PHRASES[6][4].index("the general")), 780),
            ("AGE 65 AND OLDER", 2.5, GOLD, "2.5× MORE LIKELY", tsub(6, 4, PHRASES[6][4].index("sixty five")), 865),
            ("AGE 85 AND OLDER", 3.4, CORAL, "MORE THAN 3×", ts[5], 950)]
    for lab, v, col, val, t0, y in rows:
        if t < t0:
            continue
        put_left(img, txt(lab, 32, IVORY, 2), 260, y, 32, alpha=fade(t, t0))
        wq = int(round(v * 200 * ease(seg(t, t0 + 0.2, 0.9)) / 10))
        if wq > 0:
            put(img, bar7(wq, col), 700 + wq * 5, y, alpha=1.0)
        if t >= t0 + 1.0:
            put_left(img, txt(val, 38, col, 2), 700 + int(v * 200) + 24, y, 38, alpha=fade(t, t0 + 1.0))

# ============================================================ BLOCCO 7 - mezzo rischio, gli errori, l'inverno
def gauge7():
    def fn(c):
        w, h = 530, 390
        c.rrect((4, 4, w - 4, h - 4), 30, fill=PANEL_FILL, outline=GOLD, width=6)
        c.text((w / 2, 46), "WORKING SMOKE ALARMS", FONT_SANS, 30, GOLD, track=2)
        c.text((46, 104), "RISK WITHOUT A WORKING ALARM", FONT_SANS_M, 22, SAGE, anchor="lm", track=1)
        c.rrect((46, 124, 484, 174), 14, fill=CORAL)
        c.text((46, 218), "RISK WITH A WORKING ALARM", FONT_SANS_M, 22, SAGE, anchor="lm", track=1)
        c.rrect((46, 238, 265, 288), 14, fill=GREEN_OK)
        c.text((w / 2, 340), "CUT BY HALF", FONT_SANS, 54, IVORY, track=3)
    return sprite("gauge7", 530, 390, fn)

def draw7(img, t):
    ts = starts(7)
    common(img, t, "A SMOKE ALARM THAT DOES NOT WORK")
    rail(img, t, 1)
    ap(img, t, ts[0], gauge7(), 495, 345, pop_=False, dx=-50, dur=0.6, shadow=12)
    CW, CH = 340, 390
    m1 = card("m1", CW, CH, lambda c, x, y: (ic_alarm_ceiling(c, x, y, 1.45, False)), ["STOPPED", "WORKING", "YEARS AGO"], CORAL, 36, ink=IVORY, ink2=SAGE)
    m2 = card("m2", CW, CH, lambda c, x, y: (ic_battery(c, x, y, 1.5), ic_x(c, x + 40, y + 24, 1.6, CORAL, 14)), ["BATTERY OUT:", "IT KEPT", "BEEPING"], CORAL, 36, ink=IVORY, ink2=SAGE)
    m3 = card("m3", CW, CH, lambda c, x, y: (ic_ladder(c, x, y, 1.15), ic_x(c, x + 50, y + 30, 1.5, CORAL, 14)), ["CAN'T CLIMB", "A LADDER"], CORAL, 38, ink=IVORY, ink2=SAGE)
    tm = ts[1]
    ap(img, t, tm, tag("THE MISTAKE", 300, 56, CORAL, IVORY, 28, track=3), 1325, 128, shadow=8)
    ap(img, t, tm + 0.3, m1, 960, 345, shadow=10)
    ap(img, t, tsub(7, 2, 0), m2, 1325, 345, shadow=10)
    ap(img, t, tsub(7, 2, PHRASES[7][2].index("and they can't")), m3, 1690, 345, shadow=10)
    t3 = ts[3]
    ap(img, t, t3, panel(770, 400, border=GOLD), 615, 805, pop_=False, dy=40, dur=0.6, shadow=12)
    ap(img, t, t3 + 0.3, portrait("man", "happy"), 430, 805, scale=0.9, shadow=12)
    ap(img, t, t3 + 0.5, txt("THAT'S EXACTLY", 42, IVORY, 2), 770, 740)
    ap(img, t, t3 + 0.65, txt("WHO THIS VISIT", 42, IVORY, 2), 770, 805)
    ap(img, t, t3 + 0.8, txt("IS FOR", 52, GOLD, 4), 700, 880)
    t4 = ts[4]
    ap(img, t, t4, panel(810, 400, border=SAGE_D), 1450, 805, pop_=False, dy=40, dur=0.6, shadow=12)
    ap(img, t, t4 + 0.2, txt("WINTER: WHEN IT MATTERS MOST", 32, GOLD, 3), 1450, 640)
    P4 = PHRASES[7][4]
    items = [("HEATERS", lambda c, x, y: ic_heater(c, x, y, 1.5), 1130, tsub(7, 4, P4.index("the heaters"))),
             ("BLANKETS", lambda c, x, y: ic_blanket(c, x, y, 1.5), 1330, tsub(7, 4, P4.index("the blankets"))),
             ("CANDLES", lambda c, x, y: ic_candle(c, x, y, 1.5), 1530, tsub(7, 4, P4.index("the candles"))),
             ("WINDOWS CLOSED", lambda c, x, y: ic_window_closed(c, x, y, 1.3), 1740, tsub(7, 4, P4.index("the windows")))]
    for nm, ic, x, tt in items:
        ap(img, t, tt, sprite(("w7", nm), 190, 170, lambda c, ic=ic: ic(c, 95, 85)), x, 790, shadow=6, dur=0.45)
        if nm == "WINDOWS CLOSED":
            ap(img, t, tt + 0.15, txt("WINDOWS", 28, IVORY, 1), x, 890); ap(img, t, tt + 0.2, txt("CLOSED", 28, IVORY, 1), x, 928)
        else:
            ap(img, t, tt + 0.15, txt(nm, 28, IVORY, 1), x, 905)


# ------------------------------------------------------------------ altre icone
def ic_basket(c, cx, cy, s):
    c.ell((cx - 36 * s, cy - 40 * s, cx + 4 * s, cy - 6 * s), fill=(120, 170, 210)); c.ell((cx - 6 * s, cy - 48 * s, cx + 34 * s, cy - 10 * s), fill=(236, 200, 120))
    c.poly([(cx - 46 * s, cy - 12 * s), (cx + 46 * s, cy - 12 * s), (cx + 34 * s, cy + 44 * s), (cx - 34 * s, cy + 44 * s)], fill=(200, 160, 100))
    c.rrect((cx - 50 * s, cy - 18 * s, cx + 50 * s, cy - 4 * s), 5 * s, fill=(170, 130, 80))
    for k in range(3):
        c.line([(cx - 26 * s + k * 26 * s, cy), (cx - 22 * s + k * 22 * s, cy + 38 * s)], (150, 110, 70), 4 * s)

def ic_dishes(c, cx, cy, s):
    for k, w in enumerate((50, 46, 42)):
        c.ell((cx - w * s, cy + 24 * s - k * 22 * s, cx + w * s, cy + 46 * s - k * 22 * s), fill=IVORY, outline=(170, 176, 170), width=3)
    c.ell((cx - 20 * s, cy - 54 * s, cx - 4 * s, cy - 38 * s), fill=ICE); c.ell((cx + 6 * s, cy - 62 * s, cx + 22 * s, cy - 46 * s), fill=ICE)

def ic_broom(c, cx, cy, s):
    c.line([(cx + 36 * s, cy - 56 * s), (cx - 10 * s, cy + 18 * s)], (170, 126, 80), 9 * s)
    c.poly([(cx - 28 * s, cy + 6 * s), (cx + 6 * s, cy + 28 * s), (cx - 6 * s, cy + 58 * s), (cx - 46 * s, cy + 40 * s)], fill=(228, 190, 100))
    for k in range(4):
        c.line([(cx - 20 * s - k * 6 * s, cy + 18 * s + k * 5 * s), (cx - 8 * s - k * 6 * s, cy + 46 * s + k * 3 * s)], (176, 130, 60), 3 * s)

def ic_bucket(c, cx, cy, s):
    c.poly([(cx - 38 * s, cy - 14 * s), (cx + 38 * s, cy - 14 * s), (cx + 28 * s, cy + 46 * s), (cx - 28 * s, cy + 46 * s)], fill=(90, 140, 190))
    c.arc((cx - 38 * s, cy - 56 * s, cx + 38 * s, cy + 6 * s), 180, 360, (190, 196, 204), 5 * s)
    c.ell((cx - 38 * s, cy - 22 * s, cx + 38 * s, cy - 6 * s), fill=(170, 210, 236))

def ic_box(c, cx, cy, s):
    c.rrect((cx - 44 * s, cy - 36 * s, cx + 44 * s, cy + 40 * s), 6 * s, fill=(190, 140, 86), outline=(140, 98, 58), width=4)
    c.rrect((cx - 8 * s, cy - 36 * s, cx + 8 * s, cy + 40 * s), 2, fill=(226, 196, 140))
    c.ell((cx - 40 * s, cy + 40 * s, cx - 20 * s, cy + 60 * s), fill=(80, 84, 92)); c.ell((cx + 20 * s, cy + 40 * s, cx + 40 * s, cy + 60 * s), fill=(80, 84, 92))

def ic_squeegee(c, cx, cy, s):
    c.rrect((cx - 40 * s, cy - 44 * s, cx + 40 * s, cy + 44 * s), 6 * s, fill=(150, 205, 232), outline=IVORY, width=6)
    c.line([(cx - 28 * s, cy + 10 * s), (cx + 28 * s, cy - 20 * s)], IVORY, 5 * s)
    c.rrect((cx - 18 * s, cy - 6 * s, cx + 30 * s, cy + 12 * s), 5 * s, fill=(250, 200, 90))

def ic_calendar7(c, cx, cy, s):
    c.rrect((cx - 42 * s, cy - 42 * s, cx + 42 * s, cy + 46 * s), 10 * s, fill=IVORY, outline=(190, 184, 170), width=4)
    c.rrect((cx - 42 * s, cy - 42 * s, cx + 42 * s, cy - 14 * s), 10 * s, fill=CORAL)
    for r_ in range(2):
        for k in range(3):
            c.ell((cx - 26 * s + k * 26 * s - 5 * s, cy + 6 * s + r_ * 22 * s - 5 * s, cx - 26 * s + k * 26 * s + 5 * s, cy + 6 * s + r_ * 22 * s + 5 * s), fill=GREEN_D)

def ic_hourglass(c, cx, cy, s):
    c.poly([(cx - 30 * s, cy - 46 * s), (cx + 30 * s, cy - 46 * s), (cx, cy)], fill=IVORY); c.poly([(cx - 30 * s, cy + 46 * s), (cx + 30 * s, cy + 46 * s), (cx, cy)], fill=IVORY)
    c.poly([(cx - 16 * s, cy - 38 * s), (cx + 16 * s, cy - 38 * s), (cx, cy - 8 * s)], fill=GOLD); c.poly([(cx - 22 * s, cy + 42 * s), (cx + 22 * s, cy + 42 * s), (cx, cy + 22 * s)], fill=GOLD)
    c.rrect((cx - 38 * s, cy - 54 * s, cx + 38 * s, cy - 44 * s), 3, fill=GOLD); c.rrect((cx - 38 * s, cy + 44 * s, cx + 38 * s, cy + 54 * s), 3, fill=GOLD)

def ic_clipboard(c, cx, cy, s):
    c.rrect((cx - 36 * s, cy - 46 * s, cx + 36 * s, cy + 48 * s), 8 * s, fill=IVORY, outline=(190, 184, 170), width=4)
    c.rrect((cx - 16 * s, cy - 54 * s, cx + 16 * s, cy - 36 * s), 5 * s, fill=GOLD)
    for k in range(4):
        c.ell((cx - 26 * s, cy - 22 * s + k * 18 * s - 3 * s, cx - 20 * s, cy - 22 * s + k * 18 * s + 3 * s), fill=GREEN_D)
        c.line([(cx - 12 * s, cy - 22 * s + k * 18 * s), (cx + 26 * s, cy - 22 * s + k * 18 * s)], (150, 156, 150), 4 * s)

def ic_doctor(c, cx, cy, s):
    c.d.pieslice(c._b((cx - 40 * s, cy - 4 * s, cx + 40 * s, cy + 76 * s)), 180, 360, fill=IVORY)
    c.ell((cx - 20 * s, cy - 52 * s, cx + 20 * s, cy - 12 * s), fill=SKIN)
    c.arc((cx - 22 * s, cy + 6 * s, cx + 22 * s, cy + 50 * s), 20, 160, (90, 96, 108), 5 * s)

def row_card(key, w, h, icon, lines, col=SAGE_D, size=34, ink=IVORY, ink2=GOLD):
    def mk():
        c = Cv(w, h)
        c.rrect((4, 4, w - 4, h - 4), 28, fill=PANEL_FILL, outline=col, width=6)
        r = min(70, h / 2 - 22)
        c.ell((26, h / 2 - r, 26 + 2 * r, h / 2 + r), fill=GREEN_L, outline=col, width=5)
        icon(c, 26 + r, h / 2)
        n = len(lines)
        x0 = 26 + 2 * r + 26
        for i, ln in enumerate(lines):
            s_ = size
            while tw(ln, s_, 2) > w - x0 - 24 and s_ > 16:
                s_ -= 2
            c.text((x0, h / 2 + (i - (n - 1) / 2) * size * 1.28), ln, FONT_SANS, s_, ink if (i < n - 1 or n == 1) else ink2, anchor="lm", track=2)
        return c.done()
    return cache(("rowc7", key, w, h), mk)

# ============================================================ BLOCCO 8 - la tua azione: zip code e visita
def browser7():
    def fn(c):
        w, h = 900, 620
        c.rrect((3, 3, w - 3, h - 3), 30, fill=IVORY, outline=SAGE_D, width=5)
        c.rrect((3, 3, w - 3, 76), 30, fill=(214, 224, 214)); c.d.rectangle(c._b((3, 40, w - 3, 76)), fill=(214, 224, 214))
        for i, col in enumerate(((214, 108, 96), GOLD, (110, 190, 130))):
            c.ell((30 + i * 36, 26, 52 + i * 36, 48), fill=col)
        c.rrect((170, 16, w - 40, 60), 22, fill=IVORY)
        c.text((200, 38), "soundthealarm.org", FONT_SANS_M, 30, GREEN_D, anchor="lm")
        c.d.rectangle(c._b((3, 76, w - 3, 170)), fill=GREEN_D)
        c.text((w / 2, 123), "HOME FIRE SAFETY VISIT", FONT_SANS, 42, IVORY, track=3)
        c.text((90, 232), "ENTER YOUR ZIP CODE", FONT_SANS, 30, GREEN_D, anchor="lm", track=2)
        c.rrect((90, 270, 590, 350), 18, fill=(255, 255, 255), outline=SAGE_D, width=5)
        c.rrect((620, 270, 810, 350), 18, fill=(214, 220, 214), outline=SAGE_D, width=4)
        for k in range(3):
            c.rrect((90, 410 + k * 56, 90 + (620 if k != 2 else 430), 432 + k * 56), 10, fill=(214, 220, 214))
    return sprite("browser7", 900, 620, fn)

def cursor7():
    return sprite("cur7", 80, 90, lambda c: (c.poly([(8, 6), (8, 64), (24, 50), (36, 76), (48, 70), (36, 46), (58, 46)], fill=(250, 250, 250)),
                                              c.line([(8, 6), (8, 64), (24, 50), (36, 76), (48, 70), (36, 46), (58, 46), (8, 6)], (30, 30, 30), 4)))

def step_row(n, text):
    def fn(c):
        w, h = 900, 64
        c.rrect((3, 3, w - 3, h - 3), 24, fill=PANEL_FILL, outline=GOLD, width=4)
        c.ell((10, 8, 58, 56), fill=GOLD); c.text((34, 33), str(n), FONT_SANS, 30, GREEN_D)
        c.text((80, 34), text, FONT_SANS, 28, IVORY, anchor="lm", track=2)
    return sprite(("step7", n, text), 900, 64, fn)

def mini_plan():
    def fn(c):
        wall = (150, 160, 156)
        c.rrect((26, 40, 120, 130), 4, outline=wall, width=6)
    return None

def draw8(img, t):
    ts = starts(8)
    P0 = PHRASES[8][0]
    common(img, t, "YOUR ACTION: SIGN UP")
    rail(img, t, 1)
    ap(img, t, ts[0], browser7(), 680, 460, pop_=False, dy=40, dur=0.6, shadow=14)
    # digitazione dello zip e click
    tz = tsub(8, 0, P0.index("type your zip"))
    ts_ = tsub(8, 0, P0.index("and sign up"))
    if t >= tz:
        n = min(5, int((t - tz) / 0.28) + 1)
        for k in range(n):
            put(img, dot_spr(GREEN_D, 14), 360 + k * 54, 460)
        if int(t * 2) % 2 == 0 and n < 5:
            put(img, sprite("caret7", 8, 56, lambda c: c.rrect((0, 0, 8, 56), 3, fill=GREEN_D)), 360 + n * 54 - 4, 460)
    if t >= ts_:
        p = ease(seg(t, ts_, 0.4))
        put(img, sprite("btn7", 190, 80, lambda c: (c.rrect((2, 2, 188, 78), 18, fill=GOLD, outline=(168, 118, 40), width=4),
                                                    c.text((95, 41), "SIGN UP", FONT_SANS, 30, GREEN_D, track=2))), 945, 460, scale=1 + 0.05 * math.sin(p * 3.14))
        cx_ = 1180 - 220 * p; cy_ = 640 - 140 * p
        put(img, cursor7(), cx_, cy_, alpha=min(1, p * 3))
        if t > ts_ + 0.45:
            burst(img, t, ts_ + 0.45, 945, 460, n=10, color=GOLD, rad=150, seed=9)
    # passi sotto il browser
    ap(img, t, tsub(8, 0, P0.index("Go to")), step_row(1, "GO TO SOUNDTHEALARM.ORG"), 680, 830, shadow=6, dur=0.4)
    ap(img, t, tz, step_row(2, "TYPE YOUR ZIP CODE"), 680, 905, shadow=6, dur=0.4)
    ap(img, t, ts_, step_row(3, "SIGN UP FOR A HOME FIRE SAFETY VISIT"), 680, 980, shadow=6, dur=0.4)
    # colonna destra
    RC = 1520
    r1 = row_card("r8a", 680, 250, lambda c, x, y: (ic_person(c, x - 22, y + 4, 0.9, SAGE), ic_person(c, x + 24, y + 12, 0.7, GOLD)), ["NO INTERNET?", "ASK A FAMILY MEMBER", "OR A NEIGHBOR"], GOLD, 34, ink=IVORY, ink2=IVORY)
    r2 = row_card("r8b", 680, 250, lambda c, x, y: ic_calendar7(c, x, y, 1.15), ["NOTHING NEAR YOU TODAY?", "CHECK AGAIN IN", "A FEW WEEKS"], GOLD, 34, ink=IVORY, ink2=GOLD)
    r3 = row_card("r8c", 680, 250, lambda c, x, y: (ic_alarm_ceiling(c, x - 8, y - 4, 1.1), check_ic(c, x + 34, y + 30, 0.9, GREEN_OK)),
                  ["VOLUNTEERS IN YOUR HOME:", "TEST EVERY ALARM +", "FASTEST WAY OUT"], GOLD, 34, ink=IVORY, ink2=GOLD)
    ap(img, t, ts[1], r1, RC, 270, pop_=False, dx=60, dur=0.6, shadow=10)
    ap(img, t, ts[2], r2, RC, 545, pop_=False, dx=60, dur=0.6, shadow=10)
    ap(img, t, ts[3], r3, RC, 820, pop_=False, dx=60, dur=0.6, shadow=10)

# ============================================================ BLOCCO 9 - numero 2: aiuto con le faccende
def home_helper():
    def fn(c):
        ic_house(c, 130, 130, 1.9, IVORY, GREEN_OK)
        ic_broom(c, 240, 150, 1.1)
    return sprite("hhelp7", 320, 260, fn)

def draw9(img, t):
    ts = starts(9)
    P1, P2 = PHRASES[9][1], PHRASES[9][2]
    common(img, t, "NUMBER TWO: HELP WITH THE HOUSEWORK")
    rail(img, t, 2)
    # riga 1
    ap(img, t, ts[0], panel(500, 320, border=GOLD), 500, 310, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[0] + 0.3, home_helper(), 500, 285, scale=0.9, shadow=6)
    ap(img, t, ts[0] + 0.6, txt("HOMEMAKER HELP", 40, GOLD, 3), 500, 425)
    ta = tsub(9, 1, P1.index("Through"))
    ap(img, t, ta, card("ag9", 440, 320, lambda c, x, y: ic_building(c, x, y + 6, 1.1), ["AREA AGENCY", "ON AGING"], SAGE_D, 40, ink=IVORY, ink2=GOLD, ih=0.6), 1090, 310, shadow=12)
    ap(img, t, ta + 0.6, sprite("arL7", 140, 110, lambda c: c.poly([(134, 40), (60, 40), (60, 10), (6, 56), (60, 102), (60, 72), (134, 72)], fill=GOLD)), 800, 310)
    ap(img, t, tsub(9, 1, P1.index("for people")), sprite("a609", 320, 320, lambda c: (c.ell((10, 10, 310, 310), fill=GREEN_L, outline=GOLD, width=10),
                                                                              c.text((160, 140), "60+", FONT_SANS, 110, GOLD),
                                                                              c.text((160, 232), "AND OLDER", FONT_SANS, 34, IVORY, track=3))), 1640, 310, shadow=12)
    # riga 2: le faccende
    jobs = [("laundry", ic_basket, "LAUNDRY", 500), ("the dishes", ic_dishes, "WASHING THE DISHES", 1045), ("light housekeeping", ic_broom, "LIGHT HOUSEKEEPING", 1590)]
    for key, ic, lab, x in jobs:
        tt = tsub(9, 2, P2.index(key) if key in P2 else 0)
        ap(img, t, tt, row_card(("j9", lab), 520, 220, lambda c, xx, yy, ic=ic: ic(c, xx, yy, 1.1), lab.split(" ", 1) if len(lab) > 14 else [lab], SAGE_D, 34, ink=IVORY, ink2=GOLD), x, 640, shadow=10, dur=0.45)
    # riga 3: restare a casa / dover andare via
    t3 = ts[3]
    ap(img, t, t3, panel(800, 210, border=SAGE_D), 630, 915, pop_=False, dy=40, dur=0.6, shadow=10)
    ap(img, t, t3 + 0.3, sprite("stay9", 340, 200, lambda c: (ic_house(c, 170, 62, 0.95, IVORY, GREEN_OK), c.ell((222, 40, 270, 88), fill=GREEN_OK), check_ic(c, 246, 64, 0.7, GREEN_D),
                                                           c.text((170, 172), "STAY IN YOUR HOME", FONT_SANS, 26, IVORY, track=1))), 450, 915)
    ap(img, t, t3 + 1.4, sprite("leave9", 340, 200, lambda c: (ic_house(c, 170, 62, 0.95, SAGE_D, CORAL), c.poly([(208, 52), (258, 52), (258, 34), (300, 70), (258, 106), (258, 88), (208, 88)], fill=CORAL),
                                                            c.text((170, 172), "OR HAVE TO LEAVE IT", FONT_SANS, 26, IVORY, track=1))), 810, 915)
    t4 = ts[4]
    ap(img, t, t4, panel(780, 210, border=CORAL), 1470, 915, pop_=False, dy=40, dur=0.6, shadow=10)
    ap(img, t, t4 + 0.3, sprite("doc9", 420, 190, lambda c: (ic_doctor(c, 62, 90, 0.95), ic_person(c, 150, 96, 0.85, GOLD),
                                                          c.text((212, 56), "DOCTOR OR", FONT_SANS, 32, IVORY, anchor="lm", track=1),
                                                          c.text((212, 98), "SOCIAL", FONT_SANS, 32, IVORY, anchor="lm", track=1),
                                                          c.text((212, 140), "WORKER", FONT_SANS, 32, IVORY, anchor="lm", track=1))), 1300, 915)
    ap(img, t, tsub(9, 4, PHRASES[9][4].index("often too late")), stamp("OFTEN TOO LATE", 320, 100, RED, 30), 1690, 915, rot=-6, shadow=8)

# ============================================================ BLOCCO 10 - numero 3: lavori pesanti
def stool_scene():
    def fn(c):
        w, h = 800, 440
        c.rrect((4, 4, w - 4, h - 4), 34, fill=(214, 190, 150), outline=CORAL, width=7)
        c.rrect((10, 360, w - 10, h - 10), 28, fill=(150, 106, 70))
        c.d.rectangle(c._b((10, 360, w - 10, 390)), fill=(150, 106, 70))
        c.rrect((560, 70, 750, 270), 8, fill=IVORY); c.rrect((572, 82, 738, 258), 5, fill=(150, 205, 232))
        c.line([(655, 82), (655, 258)], IVORY, 6)
        # sgabello
        c.rrect((220, 250, 360, 270), 6, fill=(200, 160, 100))
        c.line([(232, 270), (216, 380)], (170, 130, 80), 10); c.line([(348, 270), (366, 380)], (170, 130, 80), 10)
        # persona anziana in equilibrio
        c.ell((262, 80, 318, 140), fill=SKIN)
        c.d.pieslice(c._b((258, 68, 322, 140)), 180, 360, fill=HAIR)
        c.rrect((252, 140, 328, 240), 20, fill=(190, 140, 66))
        c.line([(322, 156), (352, 60)], SKIN, 14); c.line([(258, 156), (232, 70)], SKIN, 14)
        c.line([(272, 240), (262, 262)], (50, 70, 110), 16); c.line([(308, 240), (318, 262)], (50, 70, 110), 16)
        # segni di instabilita'
        for k in range(3):
            c.arc((380 + k * 26, 170 - k * 12, 430 + k * 26, 280 + k * 12), 300, 60, CORAL, 6)
            c.arc((200 - k * 26, 170 - k * 12, 250 - k * 26, 280 + k * 12), 120, 240, CORAL, 6)
    return sprite("stool10", 800, 440, fn)

def draw10(img, t):
    ts = starts(10)
    P2, P4 = PHRASES[10][2], PHRASES[10][4]
    common(img, t, "NUMBER THREE: HELP WITH THE HEAVY JOBS")
    rail(img, t, 3)
    # colonna destra in alto: gli stessi uffici, poi lo sgabello
    t_fall = ts[3]
    ap(img, t, tsub(10, 1, 0), card("off10", 800, 440, lambda c, x, y: ic_building(c, x, y + 4, 1.9), ["THE SAME OFFICES", "OFFER CHORE HELP"], GOLD, 44, ink=IVORY, ink2=GOLD, ih=0.62), 1460, 370, shadow=12, t_out=t_fall)
    ap(img, t, t_fall, stool_scene(), 1460, 370, shadow=12, dur=0.5)
    ap(img, t, t_fall + 0.7, tag("ALONE ON A STEP STOOL", 560, 70, CORAL, IVORY, 32, track=3), 1460, 590, shadow=8)
    # titolo in basso a destra, poi le domande
    t_q = tsub(10, 4, 0)
    ap(img, t, 0.4, panel(800, 390, border=SAGE_D), 1460, 810, pop_=False, dx=60, dur=0.6, shadow=12, t_out=t_q)
    ap(img, t, 0.8, txt("HEAVY JOBS", 100, GOLD, 4), 1460, 780, t_out=t_q)
    ap(img, t, 1.2, txt("HELP WITH THE", 44, IVORY, 4), 1460, 700, t_out=t_q)
    ap(img, t, 1.6, sprite("hv10", 200, 140, lambda c: ic_box(c, 100, 70, 1.3)), 1460, 905, t_out=t_q)
    qs = [("what they cover", ic_clipboard, ["WHAT DO THEY COVER", "IN YOUR AREA?"], 690),
          ("how often", ic_calendar7, ["HOW OFTEN CAN", "SOMEONE COME?"], 815),
          ("how long", ic_hourglass, ["HOW LONG IS THE", "WAITING LIST NOW?"], 940)]
    for key, ic, lines, y in qs:
        ap(img, t, tsub(10, 4, P4.index(key)), row_card(("q10", key), 800, 115, lambda c, x, yy, ic=ic: ic(c, x, yy, 0.62), lines, GOLD, 30, ink=IVORY, ink2=GOLD), 1460, y, pop_=False, dx=60, dur=0.5, shadow=8)
    # colonna sinistra: intestazione e tre lavori pesanti
    ap(img, t, ts[0], tag("CHORE HELP", 560, 76, GOLD, GREEN_D, 40, track=4), 620, 190, shadow=8)
    jobs = [("deep cleaning", ic_bucket, ["DEEP CLEANING"], 345), ("hauling things", ic_box, ["HAULING THINGS", "OUT OF THE HOUSE"], 580), ("washing the windows", ic_squeegee, ["WASHING", "THE WINDOWS"], 815)]
    for key, ic, lines, y in jobs:
        ap(img, t, tsub(10, 2, P2.index(key)), row_card(("j10", key), 780, 220, lambda c, x, yy, ic=ic: ic(c, x, yy, 1.1), lines, SAGE_D, 44, ink=IVORY, ink2=GOLD), 620, y, pop_=False, dx=-60, dur=0.5, shadow=10)

DRAW = {1: draw1, 2: draw2, 3: draw3, 4: draw4, 5: draw5, 6: draw6, 7: draw7, 8: draw8, 9: draw9, 10: draw10}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/V7-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
