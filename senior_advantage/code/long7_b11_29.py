"""Video lungo 7 (AIUTI IN CASA, INVERNO) - blocchi 11-29. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-CASA-INVERNO.md.
Durate dalla timeline dell'utente (20/10/2026): B11 953, B12 927, B13 909, B14 991, B15 946, B16 968, B17 973, B18 920, B19 976, B20 999,
B21 975, B22 1016, B23 1033, B24 1032, B25 1042, B26 970, B27 926, B28 377, B29 677 (totale video 26540 fotogrammi).
Uso: OUT=cartella python3 long7_b11_29.py <blocco> [fotogrammi]
     python3 long7_b11_29.py frame <blocco> <secondi> <file.png>"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long7_b01_10 import *

DUR = {11: 953, 12: 927, 13: 909, 14: 991, 15: 946, 16: 968, 17: 973, 18: 920, 19: 976, 20: 999,
       21: 975, 22: 1016, 23: 1033, 24: 1032, 25: 1042, 26: 970, 27: 926, 28: 377, 29: 677}
PHRASES = {
    11: ["So what does this help cost?", "Here's what the Older Americans Act says.",
         "Your local agency can ask some people to share the cost, on a sliding scale based on income.",
         "But if your income is at or below the federal poverty line, they can't ask you to share the cost.",
         "They can't count your savings, your house or any other property.",
         "And if they ask for a donation, you can say no, and they still can't refuse you the service.",
         "Most people never hear that part."],
    12: ["Number four. A hot meal brought to your door.",
         "Meals on Wheels programs bring meals to the homes of adults sixty and older, usually people who find it hard to shop or cook.",
         "Meals on Wheels America says these meals may be free, may have a suggested donation, or may be paid on a sliding scale,",
         "depending on your area, your income and your need.",
         "And for meals paid for by the Older Americans Act, the law does not allow them to make you share the cost."],
    13: ["Here's the part most people miss. It's not just the food.",
         "Meals on Wheels says local programs may also offer pet food, rides, programs to keep you connected with other people, and even home repairs.",
         "And the person who brings the meal also sees how you're doing.",
         "In the middle of winter, that knock on the door can matter more than the meal.",
         "The mistake is waiting until you can't cook at all.",
         "Call while you're still well, and ask what your local program offers."],
    14: ["Number five. Grab bars, railings and small repairs.",
         "Some Area Agencies on Aging list home repair and grab bar installation among their services.",
         "And there's a national nonprofit called Rebuilding Together, with local groups across the country.",
         "Many of them say they make repairs at no charge to the homeowner, and they put older adults, people with disabilities and veterans near the top of their list.",
         "Who qualifies is based on income, and every local group has its own rules."],
    15: ["One of their top priorities for older homeowners is preventing falls.",
         "That means grab bars in the bathroom, a second rail on the stairs, a higher toilet and brighter lights.",
         "Some local groups also step in during emergencies, when a problem would leave someone without heat, water or electricity.",
         "Your action.",
         "Search for Rebuilding Together and the name of your city or county, and ask when they take applications, because many of them plan their repair days months ahead."],
    16: ["Number six. A lawyer, without a lawyer's bill.", "Under the Older Americans Act, there is legal help for people sixty and older who need it.",
         "The government lists the main problems it covers.", "Housing, eviction and foreclosure.", "Fraud and scams that take your money.",
         "Guardianship, and the papers that say who decides for you if one day you can't.", "And here's the key line in the law.",
         "Legal assistance is one of the services where they are not allowed to make you share the cost."],
    17: ["Think about who this helps.", "A landlord who won't fix the heat.", "A contractor who took the deposit and never came back.",
         "A phone call that emptied a savings account.",
         "Most seniors in these situations do nothing at all, because they think a lawyer costs too much.",
         "Your action is to ask your Area Agency on Aging for the legal assistance program in your area.",
         "Help goes first to the people with the greatest need, so explain your situation clearly, and bring every paper you have."],
    18: ["Number seven. A break for the person who does the caring.", "If you're caring for a husband, a wife or a parent who is sixty or older,",
         "there's a federal program called the National Family Caregiver Support Program.", "It can give you what's called respite.",
         "That means someone takes over for a while, at home or at an adult day center,",
         "so you can rest, see your own doctor, or simply sleep through the night.",
         "Many caregivers never use it, simply because no one tells them it's there."],
    19: ["And here's the part grandparents need to hear.",
         "The same program also covers relatives fifty five and older who are raising children under eighteen, like grandparents raising their grandchildren.",
         "Besides respite, it can offer counseling, support groups and training.", "The cost depends on your local program and your income.",
         "The mistake is thinking you have to be at the end of your strength before you're allowed to ask.", "You don't.",
         "Ask your Area Agency on Aging about caregiver support."],
    20: ["Number eight. Protection from having your heat shut off.", "Many states have rules that limit when a utility can disconnect you.",
         "Some protect homes during certain winter months.", "Some stop shutoffs on days when it's freezing outside.",
         "And some give extra protection to older adults, or to a home where someone is seriously ill.", "But here's the catch.",
         "These rules are not the same everywhere, and they usually don't protect you if you simply stop paying.",
         "Many of them require a payment plan that you keep."],
    21: ["And the state rules often don't apply to city owned utilities or rural electric co ops.",
         "So call your utility before winter, ask what winter protection they offer, and ask if you can be listed as an older or medical customer.",
         "If they tell you no, call your state's public utility commission, the office that makes the rules for most utilities.",
         "Ask them one question.", "What protects a senior from a winter shutoff in this state?",
         "Write down the name of the person, and the date."],
    22: ["Number nine. The furnace that stops in January.", "Remember the night from the start of this video?",
         "Here's the help most people never hear about.",
         "The federal heating program, called L I H E A P, allows money to be used for energy related home repairs.",
         "And according to the national L I H E A P Clearinghouse, most states offer furnace repair or replacement through the weatherization part of their program.",
         "Some states also do it through crisis help, because losing your heat in winter is an emergency."],
    23: ["And the U S Department of Energy says its weatherization program gives priority to the elderly, and that renters can apply too.",
         "Here's the mistake.", "People call a repair company first, pay a huge bill, and only later find out there was help.",
         "Before you sign anything, call the energy help line.", "The number is one, eight six six, six seven four, six three two seven.",
         "Or go to energy help dot u s.", "Tell them you're over sixty, your heat is out or failing, and ask what your state offers."],
    24: ["Money for these programs can run out during the winter, so apply in the fall if you can, even before anything breaks.",
         "If there's a waiting list, ask to be put on it today, not when it's already cold.", "So let's put all nine together.",
         "A smoke alarm installed in your home.", "Homemaker help.", "Chore help for the heavy jobs.", "A hot meal at your door.",
         "Grab bars and repairs.", "A lawyer for housing and scams.", "A break for caregivers.", "Protection from a winter shutoff.",
         "And help when the furnace stops."],
    25: ["And here's that one phone call.", "It's the Eldercare Locator, a public service of the Administration for Community Living.",
         "The number is one, eight hundred, six seven seven, one one one six.", "You can call it or send a text.", "Say this.",
         "I'm over sixty, I live in, and say your city, and I need help at home this winter.",
         "Please connect me to my Area Agency on Aging.",
         "That one sentence opens the door to homemaker help, chore help, meals, repairs, legal help and caregiver support."],
    26: ["Now the honest part.", "Not every service exists in every town.", "Some have waiting lists, some have income limits, and money can run out.",
         "What I told you comes from official pages today.", "So call, ask, and get the answer for your area in writing if you can.",
         "And if something doesn't match what you were told, tell me in the comments, so I can tell everyone else who's watching.",
         "The more we share, the fewer people spend this winter cold and alone without knowing there was help."],
    27: ["Here's what to do this week.", "Push the test button on every smoke alarm in your home.",
         "Write the Eldercare Locator number on a piece of paper, and put it on your fridge.",
         "And call your utility to ask about winter protection, before the first cold night.",
         "None of these three things costs you a dollar.",
         "If you know someone over sixty who lives alone, especially someone who would never ask for help, send them this video, or better, sit with them and make that call together."],
    28: ["Which of these nine surprised you the most?", "Tell me below, I read every comment.",
         "If this helped you, like this video and subscribe to The Senior Advantage,", "so you don't miss the next one."],
    29: ["Rules, amounts and ages change and differ by location and program.", "Always confirm with the official source before you rely on them.",
         "General information, not financial or legal advice.",
         "This channel is not affiliated with the American Red Cross, Meals on Wheels, Rebuilding Together or any government agency."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def tsub(b, i, k):
    ph = PHRASES[b]; tot = sum(len(p_) for p_ in ph); dur = DUR[b] / FPS * 0.96
    return starts(b)[i] + k * dur / tot

def at(b, i, s):
    """secondo in cui la voce arriva alla parola s dentro la frase i"""
    return tsub(b, i, PHRASES[b][i].index(s))

def icirc(key, icon, r=70, col=GOLD, fill=GREEN_L):
    def fn(c):
        c.ell((4, 4, 2 * r - 4, 2 * r - 4), fill=fill, outline=col, width=6)
        icon(c, r, r)
    return sprite(("icirc7", key, r), 2 * r, 2 * r, fn)

def arrow_r():
    return sprite("arR7", 140, 110, lambda c: c.poly([(6, 40), (80, 40), (80, 10), (134, 56), (80, 102), (80, 72), (6, 72)], fill=GOLD))

def no_cross(c, cx, cy, s, col=CORAL):
    c.line([(cx - 40 * s, cy - 40 * s), (cx + 40 * s, cy + 40 * s)], col, 12 * s)
    c.line([(cx + 40 * s, cy - 40 * s), (cx - 40 * s, cy + 40 * s)], col, 12 * s)

# ============================================================ BLOCCO 11 - quanto costa
def scale_bar():
    def fn(c):
        w, h = 1500, 64
        c.rrect((0, 0, 420, h), 20, fill=GREEN_OK)
        c.d.rectangle(c._b((300, 0, 420, h)), fill=GREEN_OK)
        n = 80
        for i in range(n):
            x0 = 420 + i * (w - 420) / n
            f = i / (n - 1)
            col = (int(236 + (214 - 236) * f), int(200 + (108 - 200) * f), int(100 + (96 - 100) * f))
            c.d.rectangle(c._b((x0, 0, x0 + (w - 420) / n + 1, h)), fill=col)
        c.rrect((w - 40, 0, w, h), 20, fill=(214, 108, 96))
    return sprite("sbar7", 1500, 64, fn)

def draw11(img, t):
    ts = starts(11)
    common(img, t, "WHAT DOES THIS HELP COST?")
    rail(img, t, 3)
    ap(img, t, ts[1], panel(1630, 340, border=GOLD), 1045, 320, pop_=False, dy=40, dur=0.6, shadow=14)
    ap(img, t, ts[1] + 0.3, txt("THE OLDER AMERICANS ACT: THE SLIDING SCALE", 36, GOLD, 3), 1045, 195)
    ap(img, t, ts[2], scale_bar(), 1045, 335, pop_=False, dy=20, dur=0.6)
    ap(img, t, ts[2] + 0.5, txt("LOWER INCOME", 28, SAGE, 3), 400, 392)
    ap(img, t, ts[2] + 0.5, txt("HIGHER INCOME", 28, SAGE, 3), 1670, 392)
    tm = at(11, 2, "on a sliding")
    if t >= tm:
        p = ease(seg(t, tm, 1.6))
        ap(img, t, tm, tag("SHARE THE COST", 300, 54, IVORY, GREEN_D, 26, track=2), 1330, 243, shadow=6)
        put(img, sprite("mk11", 90, 100, lambda c: c.poly([(45, 90), (10, 20), (80, 20)], fill=IVORY)), 700 + 900 * p, 285)
    tp = ts[3]
    if t >= tp:
        ap(img, t, tp, sprite("nocs11", 120, 120, lambda c: (ic_coin(c, 60, 60, 36), no_cross(c, 60, 60, 1.0))), 300, 452, scale=0.62)
        ap(img, t, tp, tag("AT OR BELOW THE FEDERAL POVERTY LINE", 700, 56, GREEN_OK, GREEN_D, 22, track=1), 760, 452, shadow=6)
        ap(img, t, tp + 0.8, txt("NO COST SHARING", 40, GREEN_OK, 3), 1380, 452)
    items = [("savings", lambda c, x, y: (ic_coin(c, x - 22, y + 14, 34), ic_coin(c, x + 24, y - 6, 30)), ["YOUR", "SAVINGS"], 500, at(11, 4, "your savings")),
             ("house", lambda c, x, y: ic_house(c, x, y + 4, 1.1, IVORY, CORAL), ["YOUR", "HOUSE"], 1045, at(11, 4, "your house")),
             ("prop", lambda c, x, y: ic_box(c, x, y, 1.0), ["ANY OTHER", "PROPERTY"], 1590, at(11, 4, "any other"))]
    ap(img, t, tsub(11, 4, 0), txt("THEY CAN'T COUNT", 34, GOLD, 3), 1045, 512)
    for key, ic, lines, x, tt in items:
        ap(img, t, tt, row_card(("n11", key), 520, 200, lambda c, xx, yy, ic=ic: ic(c, xx, yy), lines, SAGE_D, 40, ink=IVORY, ink2=GOLD), x, 672, shadow=10, dur=0.45)
        ap(img, t, tt + 0.5, stamp("NOT COUNTED", 230, 58, RED, 24), x + 140, 590, rot=-8, shadow=6)
    t5 = ts[5]
    ap(img, t, t5, panel(1630, 215, border=SAGE_D), 1045, 912, pop_=False, dy=40, dur=0.6, shadow=10)
    ap(img, t, t5 + 0.3, jar7(), 360, 915, scale=0.7, shadow=6)
    ap(img, t, t5 + 0.4, txt("ASKED FOR A DONATION?", 32, IVORY, 3), 790, 850)
    ap(img, t, at(11, 5, "you can say no"), bubble_spr(330, 66, IVORY, ["NO, THANK YOU"], DARK, 32), 790, 940, shadow=8)
    ap(img, t, at(11, 5, "and they still"), sprite("ok11", 90, 90, lambda c: (c.ell((4, 4, 86, 86), fill=GREEN_OK), check_ic(c, 45, 45, 1.0, GREEN_D))), 1150, 915)
    ap(img, t, at(11, 5, "and they still") + 0.2, txt("THEY STILL CAN'T REFUSE", 34, IVORY, 2), 1545, 892)
    ap(img, t, at(11, 5, "and they still") + 0.35, txt("YOU THE SERVICE", 34, GOLD, 2), 1490, 940)
    ap(img, t, ts[6], tag("MOST PEOPLE NEVER HEAR THAT PART", 640, 66, GOLD, GREEN_D, 28, border=(168, 118, 40), track=2), 1400, 806, shadow=8, rot=-2)

# ============================================================ BLOCCO 12 - pasto a domicilio
def meal_scene():
    def fn(c):
        w, h = 670, 570
        c.rrect((4, 4, w - 4, h - 4), 34, fill=(214, 190, 150), outline=SAGE_D, width=5)
        c.rrect((8, 440, w - 8, h - 8), 30, fill=(150, 106, 70)); c.d.rectangle(c._b((8, 440, w - 8, 480)), fill=(150, 106, 70))
        c.rrect((470, 60, 640, 460), 10, fill=(70, 50, 38)); c.rrect((484, 74, 626, 460), 6, fill=(255, 236, 178))
        c.poly([(484, 74), (540, 90), (540, 460), (484, 460)], fill=(150, 100, 62))
        # volontario con vassoio
        c.ell((90, 110, 160, 180), fill=SKIN); c.d.pieslice(c._b((84, 98, 166, 176)), 180, 360, fill=(70, 100, 150))
        c.rrect((78, 182, 172, 340), 26, fill=(70, 120, 176))
        c.line([(160, 220), (250, 250)], SKIN, 16)
        c.rrect((210, 246, 350, 262), 6, fill=(190, 192, 198))
        ic_meal(c, 280, 236, 0.85)
        c.line([(100, 340), (100, 440)], (50, 70, 110), 20); c.line([(150, 340), (150, 440)], (50, 70, 110), 20)
        # anziana alla porta
        c.ell((390, 180, 450, 240), fill=SKIN); c.d.pieslice(c._b((386, 168, 454, 240)), 180, 360, fill=HAIR)
        c.rrect((380, 244, 460, 400), 24, fill=(190, 140, 66))
        c.line([(384, 280), (330, 262)], SKIN, 14)
        c.line([(395, 400), (395, 450)], (90, 90, 110), 16); c.line([(445, 400), (445, 450)], (90, 90, 110), 16)
    return sprite("meal12", 670, 570, fn)

def draw12(img, t):
    ts = starts(12)
    common(img, t, "NUMBER FOUR: A HOT MEAL AT YOUR DOOR")
    rail(img, t, 4)
    ap(img, t, 0.3, meal_scene(), 565, 435, pop_=False, dx=-50, dur=0.7, shadow=14)
    ap(img, t, ts[1], tag("ADULTS 60 AND OLDER", 520, 64, GOLD, GREEN_D, 30, track=2), 565, 785, shadow=8)
    ap(img, t, at(12, 1, "usually"), tag("FIND IT HARD TO SHOP OR COOK", 620, 64, IVORY, GREEN_D, 28, border=GOLD, track=1), 565, 865, shadow=8)
    P2 = PHRASES[12][2]
    tk = [("MAY BE FREE", lambda c, x, y: (c.ell((x - 36, y - 36, x + 36, y + 36), fill=GREEN_OK), check_ic(c, x, y, 0.9, GREEN_D)), 250, at(12, 2, "may be free")),
          ("MAY HAVE A SUGGESTED DONATION", lambda c, x, y: ic_coin(c, x, y, 38), 435, at(12, 2, "may have")),
          ("MAY BE PAID ON A SLIDING SCALE", lambda c, x, y: (c.rrect((x - 44, y - 16, x + 44, y + 16), 10, fill=GOLD), c.poly([(x + 8, y + 40), (x - 8, y + 18), (x + 24, y + 18)], fill=IVORY)), 620, at(12, 2, "or may be paid"))]
    for i, (lab, ic, y, tt) in enumerate(tk):
        w_ = 900
        words = lab.split(" ")
        lines = [lab] if len(lab) < 16 else [" ".join(words[:3]), " ".join(words[3:])] if len(words) > 3 else [lab]
        ap(img, t, tt, row_card(("tk12", i), w_, 150, lambda c, x, yy, ic=ic: ic(c, x, yy), [lab] if len(lab) < 28 else [lab[:lab.rindex(" ", 0, 22)], lab[lab.rindex(" ", 0, 22) + 1:]], GOLD if i == 0 else SAGE_D, 36, ink=IVORY, ink2=IVORY), 1410, y, pop_=False, dx=60, dur=0.5, shadow=8)
    t3 = ts[3]
    for k, (lab, x) in enumerate((("YOUR AREA", 1110), ("YOUR INCOME", 1410), ("YOUR NEED", 1710))):
        ap(img, t, t3 + 0.3 * k, tag(lab, 280, 64, IVORY, GREEN_D, 28, border=SAGE_D, track=2), x, 790, shadow=6)
    ap(img, t, ts[4], tag("MEALS PAID BY THE OLDER AMERICANS ACT: NO COST SHARING", 1520, 88, GOLD, GREEN_D, 38, border=(168, 118, 40), track=2), 1060, 965, shadow=10)

# ============================================================ BLOCCO 13 - non solo il cibo
def ic_bowl(c, cx, cy, s):
    c.poly([(cx - 40 * s, cy - 6 * s), (cx + 40 * s, cy - 6 * s), (cx + 28 * s, cy + 34 * s), (cx - 28 * s, cy + 34 * s)], fill=CORAL)
    c.ell((cx - 40 * s, cy - 14 * s, cx + 40 * s, cy + 2 * s), fill=(150, 70, 62))
    c.rrect((cx - 22 * s, cy - 40 * s, cx + 22 * s, cy - 24 * s), 8 * s, fill=IVORY)
    c.ell((cx - 30 * s, cy - 46 * s, cx - 14 * s, cy - 30 * s), fill=IVORY); c.ell((cx + 14 * s, cy - 46 * s, cx + 30 * s, cy - 30 * s), fill=IVORY)

def ic_car(c, cx, cy, s):
    c.rrect((cx - 48 * s, cy - 6 * s, cx + 48 * s, cy + 30 * s), 10 * s, fill=(90, 140, 190))
    c.poly([(cx - 30 * s, cy - 6 * s), (cx - 16 * s, cy - 34 * s), (cx + 22 * s, cy - 34 * s), (cx + 38 * s, cy - 6 * s)], fill=(90, 140, 190))
    c.poly([(cx - 22 * s, cy - 8 * s), (cx - 12 * s, cy - 28 * s), (cx + 18 * s, cy - 28 * s), (cx + 30 * s, cy - 8 * s)], fill=(190, 226, 242))
    c.ell((cx - 38 * s, cy + 16 * s, cx - 14 * s, cy + 40 * s), fill=(40, 44, 52)); c.ell((cx + 14 * s, cy + 16 * s, cx + 38 * s, cy + 40 * s), fill=(40, 44, 52))

def draw13(img, t):
    ts = starts(13)
    common(img, t, "NOT JUST THE FOOD")
    rail(img, t, 4)
    HX, HY = 790, 575
    ap(img, t, ts[0], icirc("hub13", lambda c, x, y: ic_meal(c, x, y + 6, 1.5), 130, GOLD), HX, HY, shadow=12, dur=0.6)
    ap(img, t, ts[0] + 0.4, txt("IT'S NOT JUST", 30, IVORY, 3), HX, HY + 170)
    ap(img, t, ts[0] + 0.55, txt("THE FOOD", 40, GOLD, 4), HX, HY + 215)
    P1 = PHRASES[13][1]
    sats = [("pet", lambda c, x, y: ic_bowl(c, x, y + 4, 1.3), "PET FOOD", -1, -1, at(13, 1, "pet food")), ("ride", lambda c, x, y: ic_car(c, x, y, 1.2), "RIDES", 1, -1, at(13, 1, "rides")),
            ("conn", lambda c, x, y: ic_people(c, x, y + 4, 0.9), "STAYING CONNECTED", -1, 1, at(13, 1, "programs to keep")),
            ("rep", lambda c, x, y: ic_wrench(c, x, y, 1.4, IVORY), "HOME REPAIRS", 1, 1, at(13, 1, "even home"))]
    for key, ic, lab, sx, sy, tt in sats:
        cx_, cy_ = HX + sx * 300, HY + sy * 230 - (30 if sy < 0 else 0) * 0
        # filo tra il centro e il satellite
        if t >= tt:
            p = ease(seg(t, tt, 0.5))
            put(img, dot_spr(GOLD, 6), lerp(HX, cx_, 0.38 * p + 0.0), lerp(HY, cy_, 0.38 * p))
            put(img, dot_spr(GOLD, 6), lerp(HX, cx_, 0.56 * p), lerp(HY, cy_, 0.56 * p))
        ap(img, t, tt, icirc(("s13", key), ic, 90, SAGE_D), cx_, cy_, shadow=10, dur=0.5)
        ap(img, t, tt + 0.25, txt(lab, 28, IVORY, 2), cx_, cy_ + 118)
    # colonna destra
    X = 1570
    ap(img, t, ts[2], row_card("see13", 570, 230, lambda c, x, y: (ic_person(c, x - 20, y + 6, 0.85, (70, 120, 176)), ic_heart(c, x + 36, y - 30, 0.55)), ["THE PERSON WHO", "BRINGS THE MEAL", "SEES HOW YOU'RE DOING"], GOLD, 28, ink=IVORY, ink2=GOLD), X, 265, pop_=False, dx=60, dur=0.5, shadow=10)
    ap(img, t, ts[3], row_card("knock13", 570, 230, lambda c, x, y: (c.rrect((x - 32, y - 46, x + 32, y + 46), 6, fill=(150, 100, 62)), ic_snowflake(c, x + 44, y - 36, 0.8)), ["IN MIDDLE OF WINTER:", "THAT KNOCK ON THE DOOR", "CAN MATTER MORE"], SAGE_D, 28, ink=IVORY, ink2=GOLD), X, 515, pop_=False, dx=60, dur=0.5, shadow=10)
    ap(img, t, ts[4], row_card("mist13", 570, 160, lambda c, x, y: warn_tri(c, x, y, 0.8, CORAL), ["THE MISTAKE: WAITING", "UNTIL YOU CAN'T COOK"], CORAL, 30, ink=IVORY, ink2=IVORY), X, 740, pop_=False, dx=60, dur=0.5, shadow=10)
    ap(img, t, ts[5], row_card("call13", 570, 160, lambda c, x, y: ic_phone(c, x, y, 0.9), ["CALL WHILE YOU'RE", "STILL WELL"], GREEN_OK, 30, ink=IVORY, ink2=GREEN_OK), X, 925, pop_=False, dx=60, dur=0.5, shadow=10)

# ============================================================ BLOCCO 14 - Rebuilding Together
def draw14(img, t):
    ts = starts(14)
    common(img, t, "NUMBER FIVE: GRAB BARS AND SMALL REPAIRS")
    rail(img, t, 5)
    ap(img, t, ts[1], row_card("aaa14", 620, 300, lambda c, x, y: ic_building(c, x, y + 4, 1.0), ["AREA AGENCIES", "ON AGING"], SAGE_D, 38, ink=IVORY, ink2=GOLD), 540, 300, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[1] + 0.5, tag("HOME REPAIR", 440, 58, IVORY, GREEN_D, 28, border=GOLD, track=2), 540, 470, shadow=6)
    ap(img, t, ts[1] + 0.9, tag("GRAB BAR INSTALLATION", 520, 58, IVORY, GREEN_D, 28, border=GOLD, track=2), 540, 545, shadow=6)
    t2 = ts[2]
    ap(img, t, t2, panel(960, 470, border=GOLD), 1380, 385, pop_=False, dx=50, dur=0.6, shadow=14)
    ap(img, t, t2 + 0.3, txt("REBUILDING TOGETHER", 52, GOLD, 3), 1380, 205)
    ap(img, t, t2 + 0.5, txt("A NATIONAL NONPROFIT", 30, SAGE, 3), 1380, 258)
    ap(img, t, t2 + 0.7, map_sprite(), 1210, 420, scale=0.8)
    for i, (lo, la) in enumerate(PINS):
        x, y = map_xy(lo, la)
        ap(img, t, t2 + 1.2 + i * 0.2, pin_spr(), 1210 - 224 + x * 0.8, 420 - 124 + y * 0.8 - 14, scale=0.5, dur=0.35)
    ap(img, t, at(14, 2, "with local"), tag("LOCAL GROUPS ACROSS THE COUNTRY", 560, 56, IVORY, GREEN_D, 24, border=GOLD, track=1), 1210, 560, shadow=6)
    P3 = PHRASES[14][3]
    t3 = ts[3]
    ap(img, t, t3, row_card("free14", 380, 250, lambda c, x, y: (ic_house(c, x, y + 4, 1.0, IVORY, GREEN_OK), c.line([(x + 26, y - 40), (x + 56, y - 8)], GOLD, 10)), ["REPAIRS AT NO", "CHARGE TO THE", "HOMEOWNER"], GOLD, 24, ink=IVORY, ink2=GOLD), 1650, 410, pop_=False, dx=40, dur=0.5, shadow=8)
    ap(img, t, t3 + 0.6, tag("MANY SAY", 200, 50, GOLD, GREEN_D, 26, track=2), 1650, 545, shadow=6)
    # priorita'
    ap(img, t, at(14, 3, "and they put"), txt("NEAR THE TOP OF THEIR LIST", 32, GOLD, 3), 620, 690)
    pr = [("OLDER ADULTS", lambda c, x, y: ic_person(c, x, y, 0.55, GOLD), at(14, 3, "older adults"), 770),
          ("PEOPLE WITH DISABILITIES", lambda c, x, y: ic_person(c, x, y, 0.55, SAGE), at(14, 3, "people with"), 865),
          ("VETERANS", lambda c, x, y: ic_scroll(c, x, y, 0.5), at(14, 3, "veterans"), 960)]
    for nm, ic, tt, y in pr:
        ap(img, t, tt, row_card(("pr14", nm), 770, 80, lambda c, x, yy, ic=ic: ic(c, x, yy), [nm], SAGE_D, 32, ink=IVORY, ink2=IVORY), 620, y, pop_=False, dx=-50, dur=0.45, shadow=6)
    t4 = ts[4]
    ap(img, t, t4, panel(780, 330, border=GOLD), 1470, 830, pop_=False, dy=40, dur=0.6, shadow=12)
    ap(img, t, t4 + 0.3, txt("WHO QUALIFIES?", 40, GOLD, 4), 1470, 710)
    ap(img, t, t4 + 0.6, row_card("inc14", 700, 100, lambda c, x, y: ic_coin(c, x, y, 36), ["BASED ON INCOME"], SAGE_D, 34, ink=IVORY, ink2=IVORY), 1470, 800, shadow=6)
    ap(img, t, at(14, 4, "and every"), row_card("rul14", 700, 100, lambda c, x, y: ic_scroll(c, x, y, 0.5), ["EVERY GROUP HAS ITS OWN RULES"], SAGE_D, 28, ink=IVORY, ink2=IVORY), 1470, 920, shadow=6)

# ============================================================ BLOCCO 15 - prevenire le cadute
def bath_scene():
    def fn(c):
        w, h = 860, 600
        c.rrect((4, 4, w - 4, h - 4), 34, fill=(184, 208, 218), outline=SAGE_D, width=5)
        c.rrect((8, 470, w - 8, h - 8), 30, fill=(130, 110, 96)); c.d.rectangle(c._b((8, 470, w - 8, 510)), fill=(130, 110, 96))
        c.line([(440, 8), (440, 590)], (150, 170, 178), 6)
        # vasca
        c.rrect((50, 360, 330, 480), 24, fill=IVORY, outline=(180, 186, 188), width=4)
        c.rrect((60, 340, 320, 372), 12, fill=(214, 224, 228))
        # wc alto
        c.rrect((356, 236, 420, 330), 8, fill=IVORY, outline=(180, 186, 188), width=4)
        c.ell((330, 330, 430, 372), fill=IVORY, outline=(180, 186, 188), width=4)
        c.rrect((344, 370, 416, 480), 14, fill=IVORY, outline=(180, 186, 188), width=4)
        # barra d'appoggio
        c.line([(86, 290), (270, 290)], (160, 164, 170), 14); c.line([(86, 290), (86, 340)], (160, 164, 170), 10); c.line([(270, 290), (270, 340)], (160, 164, 170), 10)
        # scala
        for k in range(6):
            c.rrect((470 + k * 56, 470 - k * 56, 846, 484 - k * 56 + 56), 4, fill=(170, 130, 90), outline=(120, 90, 60), width=3)
        c.line([(470, 380), (846, 44)], (160, 164, 170), 12)     # corrimano a muro
        c.line([(470, 440), (846, 104)], GOLD, 12)               # secondo corrimano
        # luci
        for x in (230, 640):
            c.line([(x, 8), (x, 52)], (90, 90, 96), 6)
            c.ell((x - 28, 52, x + 28, 108), fill=(255, 244, 190), outline=(230, 200, 100), width=4)
    return sprite("bath15", 860, 600, fn)

def draw15(img, t):
    ts = starts(15)
    common(img, t, "PREVENTING FALLS AT HOME")
    rail(img, t, 5)
    P1, P4 = PHRASES[15][1], PHRASES[15][4]
    ap(img, t, ts[0], bath_scene(), 660, 450, pop_=False, dx=-50, dur=0.7, shadow=14)
    ap(img, t, ts[0] + 0.7, tag("A TOP PRIORITY: PREVENTING FALLS", 700, 62, CORAL, IVORY, 28, track=2), 660, 168, shadow=8)
    callouts = [("GRAB BARS", 470, 440, at(15, 1, "grab bars")), ("A SECOND RAIL", 1010, 300, at(15, 1, "a second rail")),
                ("A HIGHER TOILET", 560, 330, at(15, 1, "a higher")), ("BRIGHTER LIGHTS", 880, 200, at(15, 1, "brighter"))]
    cp = [("GRAB BARS", 390, 500), ("A HIGHER TOILET", 640, 540), ("A SECOND RAIL", 940, 650), ("BRIGHTER LIGHTS", 640, 705)]
    cp = [("GRAB BARS", 330, 560, at(15, 1, "grab bars")), ("A SECOND RAIL", 930, 560, at(15, 1, "a second rail")),
          ("A HIGHER TOILET", 600, 650, at(15, 1, "a higher")), ("BRIGHTER LIGHTS", 700, 250, at(15, 1, "brighter"))]
    for lab, x, y, tt in cp:
        ap(img, t, tt, tag(lab, 330, 58, GOLD, GREEN_D, 24, border=(168, 118, 40), track=1), x, y, shadow=8, dur=0.4)
    # emergenze
    t2 = ts[2]
    ap(img, t, t2, panel(730, 320, border=CORAL), 1495, 305, pop_=False, dx=50, dur=0.6, shadow=12)
    ap(img, t, t2 + 0.3, txt("SOME GROUPS STEP IN FOR EMERGENCIES", 28, GOLD, 2), 1495, 180)
    em = [("NO HEAT", lambda c, x, y: (ic_flame(c, x, y, 0.55), no_cross(c, x, y, 0.8)), 1275, at(15, 2, "heat")),
          ("NO WATER", lambda c, x, y: (c.poly([(x, y - 40), (x + 26, y + 6), (x - 26, y + 6)], fill=ICE), c.ell((x - 26, y - 12, x + 26, y + 40), fill=ICE), no_cross(c, x, y, 0.8)), 1495, at(15, 2, "water")),
          ("NO ELECTRICITY", lambda c, x, y: (ic_bolt(c, x, y, 0.55), no_cross(c, x, y, 0.8)), 1715, at(15, 2, "electricity"))]
    for lab, ic, x, tt in em:
        ap(img, t, tt, icirc(("e15", lab), ic, 70, CORAL), x, 300, shadow=8, dur=0.45)
        ap(img, t, tt + 0.2, fit(lab, 26, 200, IVORY, 1), x, 410)
    # azione: ricerca
    t3 = ts[3]
    ap(img, t, t3, tag("YOUR ACTION", 340, 60, GOLD, GREEN_D, 30, track=3), 1495, 520, shadow=8)
    ap(img, t, ts[4], sprite("srch15", 730, 130, lambda c: (c.rrect((4, 4, 726, 126), 60, fill=IVORY, outline=GOLD, width=6),
                                                       magnifier(c, 70, 60, 22, GREEN_D, 7),
                                                       c.text((120, 52), "Rebuilding Together", FONT_SANS, 34, GREEN_D, anchor="lm"),
                                                       c.text((120, 92), "+ your city or county", FONT_SANS_M, 28, (90, 110, 100), anchor="lm"))), 1495, 625, shadow=10)
    ap(img, t, at(15, 4, "and ask when"), row_card("appl15", 860, 150, lambda c, x, y: ic_calendar7(c, x, y, 1.0), ["ASK WHEN THEY TAKE", "APPLICATIONS"], GOLD, 38, ink=IVORY, ink2=GOLD), 660, 895, pop_=False, dy=40, dur=0.5, shadow=10)
    tm = at(15, 4, "because many")
    ap(img, t, tm, panel(740, 170, border=SAGE_D), 1490, 895, pop_=False, dy=40, dur=0.5, shadow=10)
    ap(img, t, tm + 0.3, txt("MANY PLAN THEIR REPAIR DAYS", 26, IVORY, 2), 1490, 840)
    for k in range(6):
        on = k == 5
        ap(img, t, tm + 0.5 + k * 0.18, sprite(("mo15", on), 100, 54, lambda c, on=on: c.rrect((2, 2, 98, 52), 14, fill=GOLD if on else CARD, outline=GOLD if on else SAGE_D, width=4)), 1250 + k * 106, 895, dur=0.3)
    ap(img, t, tm + 1.7, txt("MONTHS AHEAD", 28, GOLD, 4), 1490, 945)


# ------------------------------------------------------------------ icone ancora
def ic_scale(c, cx, cy, s, col=GOLD):
    c.line([(cx, cy - 56 * s), (cx, cy + 52 * s)], col, 8 * s)
    c.rrect((cx - 30 * s, cy + 46 * s, cx + 30 * s, cy + 60 * s), 6 * s, fill=col)
    c.line([(cx - 56 * s, cy - 44 * s), (cx + 56 * s, cy - 44 * s)], col, 8 * s)
    for sx in (-1, 1):
        x = cx + sx * 56 * s
        c.line([(x, cy - 44 * s), (x - 22 * s, cy + 2 * s)], col, 4 * s); c.line([(x, cy - 44 * s), (x + 22 * s, cy + 2 * s)], col, 4 * s)
        c.d.pieslice(c._b((x - 28 * s, cy - 14 * s, x + 28 * s, cy + 30 * s)), 0, 180, fill=col)

def ic_moon(c, cx, cy, s):
    c.ell((cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s), fill=(240, 236, 214))
    c.ell((cx - 16 * s, cy - 48 * s, cx + 56 * s, cy + 28 * s), fill=GREEN_L)
    c.text((cx + 40 * s, cy - 30 * s), "z", FONT_SANS, 30 * s, IVORY)

def ic_armchair(c, cx, cy, s):
    c.rrect((cx - 34 * s, cy - 46 * s, cx + 34 * s, cy + 6 * s), 14 * s, fill=(176, 104, 98))
    c.rrect((cx - 50 * s, cy - 14 * s, cx - 26 * s, cy + 34 * s), 10 * s, fill=(150, 84, 80)); c.rrect((cx + 26 * s, cy - 14 * s, cx + 50 * s, cy + 34 * s), 10 * s, fill=(150, 84, 80))
    c.rrect((cx - 36 * s, cy - 2 * s, cx + 36 * s, cy + 28 * s), 10 * s, fill=(206, 130, 120))
    c.line([(cx - 40 * s, cy + 34 * s), (cx - 40 * s, cy + 52 * s)], (90, 60, 46), 7 * s); c.line([(cx + 40 * s, cy + 34 * s), (cx + 40 * s, cy + 52 * s)], (90, 60, 46), 7 * s)

def ic_thermo(c, cx, cy, s):
    c.rrect((cx - 12 * s, cy - 50 * s, cx + 12 * s, cy + 24 * s), 12 * s, fill=IVORY)
    c.ell((cx - 24 * s, cy + 6 * s, cx + 24 * s, cy + 54 * s), fill=IVORY)
    c.rrect((cx - 5 * s, cy - 10 * s, cx + 5 * s, cy + 34 * s), 4 * s, fill=ICE); c.ell((cx - 15 * s, cy + 16 * s, cx + 15 * s, cy + 46 * s), fill=ICE)
    ic_snowflake(c, cx + 46 * s, cy - 30 * s, 0.6 * s)

def step_card(n, head, subs, w, h, col=GOLD, hs=36, ss=28):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 28, fill=PANEL_FILL, outline=col, width=6)
        c.ell((24, 24, 24 + 72, 24 + 72), fill=col); c.text((60, 62), str(n), FONT_SANS, 44, GREEN_D)
        x0 = 124
        s_ = hs
        while tw(head, s_, 2) > w - x0 - 24 and s_ > 16: s_ -= 2
        c.text((x0, 58), head, FONT_SANS, s_, IVORY, anchor="lm", track=2)
        for i, ln in enumerate(subs):
            s2 = ss
            while tw(ln, s2, 1) > w - x0 - 24 and s2 > 14: s2 -= 2
            c.text((x0, 112 + i * (ss + 14)), ln, FONT_SANS_M, s2, SAGE, anchor="lm", track=1)
    return sprite(("stepc7", n, head, w, h), w, h, fn)

# ============================================================ BLOCCO 16 - l'avvocato
def draw16(img, t):
    ts = starts(16)
    common(img, t, "NUMBER SIX: A LAWYER, WITHOUT A LAWYER'S BILL")
    rail(img, t, 6)
    ap(img, t, ts[0], panel(530, 850, border=GOLD), 505, 575, pop_=False, dx=-50, dur=0.6, shadow=14)
    ap(img, t, ts[0] + 0.3, sprite("sc16", 320, 300, lambda c: ic_scale(c, 160, 150, 2.4)), 505, 360, shadow=6)
    ap(img, t, ts[0] + 0.6, txt("LEGAL HELP", 60, GOLD, 4), 505, 580)
    ap(img, t, ts[1], tag("AGE 60 AND OLDER", 430, 66, IVORY, GREEN_D, 32, border=GOLD, track=2), 505, 680, shadow=8)
    ap(img, t, at(16, 1, "who need it"), tag("WHO NEED IT", 330, 60, GREEN_OK, GREEN_D, 30, track=3), 505, 770, shadow=8)
    ap(img, t, ts[2], txt("THE MAIN PROBLEMS IT COVERS", 36, GOLD, 4), 1330, 190)
    cards = [("house16", lambda c, x, y: (ic_house(c, x, y + 4, 1.1, IVORY, CORAL), ), ["HOUSING, EVICTION", "AND FORECLOSURE"], 320, ts[3]),
             ("fraud16", lambda c, x, y: (ic_phone(c, x - 16, y, 0.9), warn_tri(c, x + 36, y - 20, 0.5)), ["FRAUD AND SCAMS", "THAT TAKE YOUR MONEY"], 555, ts[4]),
             ("guard16", lambda c, x, y: (ic_scroll(c, x, y, 0.9),), ["GUARDIANSHIP, AND THE PAPERS", "THAT SAY WHO DECIDES FOR YOU"], 790, ts[5])]
    for key, ic, lines, y, tt in cards:
        ap(img, t, tt, row_card(("c16", key), 1060, 215, lambda c, x, yy, ic=ic: ic(c, x, yy), lines, SAGE_D, 40, ink=IVORY, ink2=GOLD), 1330, y, pop_=False, dx=60, dur=0.5, shadow=10)
    ap(img, t, ts[6], stamp("THE KEY LINE", 330, 74, RED, 32), 505, 890, rot=-4, shadow=8)
    ap(img, t, ts[7], tag("NOT ALLOWED TO MAKE YOU SHARE THE COST", 1060, 84, GOLD, GREEN_D, 34, border=(168, 118, 40), track=2), 1330, 960, shadow=10)

# ============================================================ BLOCCO 17 - tre scene e l'azione
def draw17(img, t):
    ts = starts(17)
    common(img, t, "WHO THIS HELPS")
    rail(img, t, 6)
    sc = [("l17", lambda c, x, y: (ic_person(c, x - 70, y + 4, 1.0, CORAL), c.rrect((x + 6, y - 26, x + 100, y + 50), 8, fill=(206, 210, 216), outline=(150, 156, 166), width=3),
                                    ic_snowflake(c, x + 54, y - 52, 0.8)), ["A LANDLORD WHO", "WON'T FIX THE HEAT"], 500, ts[1]),
          ("c17", lambda c, x, y: (ic_person(c, x - 60, y + 4, 1.0, (70, 120, 176)), ic_coin(c, x + 60, y + 2, 34), c.poly([(x + 14, y - 40), (x + 40, y - 40), (x + 40, y - 54), (x + 74, y - 30), (x + 40, y - 6), (x + 40, y - 20), (x + 14, y - 20)], fill=CORAL)),
           ["A CONTRACTOR WHO", "TOOK THE DEPOSIT"], 1045, ts[2]),
          ("p17", lambda c, x, y: (ic_phone(c, x - 50, y, 1.0), ic_coin(c, x + 40, y + 4, 28), c.poly([(x + 70, y - 28), (x + 96, y - 28), (x + 96, y - 42), (x + 128, y - 14), (x + 96, y + 14), (x + 96, y), (x + 70, y)], fill=CORAL)),
           ["A PHONE CALL THAT", "EMPTIED A SAVINGS", "ACCOUNT"], 1590, ts[3])]
    for key, ic, lines, x, tt in sc:
        ap(img, t, tt, card(("s17", key), 520, 340, ic, lines, CORAL, 36, ink=IVORY, ink2=GOLD, ih=0.5), x, 345, shadow=12, dur=0.5)
    ap(img, t, ts[0], txt("THINK ABOUT WHO THIS HELPS", 34, GOLD, 4), 1045, 138)
    t4 = ts[4]
    ap(img, t, t4, portrait("man", "sad"), 380, 690, scale=0.6, shadow=10)
    ap(img, t, t4 + 0.3, tag("MOST DO NOTHING AT ALL", 520, 58, CORAL, IVORY, 28, track=2), 1000, 585, shadow=8)
    ap(img, t, t4 + 0.6, thought(900, 110, ["A LAWYER COSTS TOO MUCH"], 46, "law17"), 1010, 690, shadow=10)
    ap(img, t, ts[5], row_card("ask17", 760, 190, lambda c, x, y: ic_building(c, x, y + 4, 0.8), ["ASK YOUR AREA AGENCY", "ON AGING FOR THE", "LEGAL ASSISTANCE PROGRAM"], GOLD, 30, ink=IVORY, ink2=GOLD), 620, 910, pop_=False, dy=40, dur=0.5, shadow=10)
    ap(img, t, ts[6], row_card("need17", 820, 190, lambda c, x, y: ic_clipboard(c, x, y, 0.9), ["GREATEST NEED FIRST:", "EXPLAIN CLEARLY AND", "BRING EVERY PAPER"], GREEN_OK, 30, ink=IVORY, ink2=GREEN_OK), 1450, 910, pop_=False, dy=40, dur=0.5, shadow=10)

# ============================================================ BLOCCO 18 - il sollievo per chi assiste
def draw18(img, t):
    ts = starts(18)
    common(img, t, "NUMBER SEVEN: A BREAK FOR CAREGIVERS")
    rail(img, t, 7)
    c1 = card("cg1", 480, 290, lambda c, x, y: ic_people(c, x, y + 4, 1.1), ["CARING FOR A HUSBAND,", "A WIFE OR A PARENT 60+"], SAGE_D, 28, ink=IVORY, ink2=GOLD, ih=0.5)
    c2 = card("cg2", 480, 290, lambda c, x, y: ic_scroll(c, x, y, 1.0), ["NATIONAL FAMILY", "CAREGIVER SUPPORT", "PROGRAM"], GOLD, 30, ink=IVORY, ink2=GOLD, ih=0.5)
    c3 = card("cg3", 480, 290, lambda c, x, y: (ic_person(c, x - 40, y + 4, 0.9, GOLD), ic_person(c, x + 40, y + 4, 0.9, (70, 120, 176)), c.poly([(x - 10, y - 40), (x + 14, y - 40), (x + 14, y - 54), (x + 44, y - 30), (x + 14, y - 8), (x + 14, y - 22), (x - 10, y - 22)], fill=GREEN_OK)),
              ["RESPITE: SOMEONE", "TAKES OVER FOR A WHILE"], GREEN_OK, 28, ink=IVORY, ink2=GREEN_OK, ih=0.5)
    ap(img, t, ts[1], c1, 500, 300, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[1] + 0.8, arrow_r(), 770, 300, scale=0.6)
    ap(img, t, ts[2], c2, 1045, 300, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[2] + 0.8, tag("FEDERAL", 220, 52, GOLD, GREEN_D, 26, track=3), 1045, 455, shadow=6)
    ap(img, t, ts[2] + 1.0, arrow_r(), 1318, 300, scale=0.6)
    ap(img, t, ts[3], c3, 1590, 300, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[4], tag("AT HOME OR AT AN ADULT DAY CENTER", 800, 60, IVORY, GREEN_D, 28, border=GOLD, track=2), 1360, 530, shadow=8)
    items = [("rest", lambda c, x, y: ic_armchair(c, x, y, 1.2), ["SO YOU CAN", "REST"], 500, at(18, 5, "rest")),
             ("doc", lambda c, x, y: ic_doctor(c, x, y - 4, 0.8), ["SEE YOUR OWN", "DOCTOR"], 1045, at(18, 5, "see your")),
             ("sleep", lambda c, x, y: ic_moon(c, x, y, 1.0), ["SLEEP THROUGH", "THE NIGHT"], 1590, at(18, 5, "simply sleep"))]
    for key, ic, lines, x, tt in items:
        ap(img, t, tt, row_card(("b18", key), 520, 230, lambda c, xx, yy, ic=ic: ic(c, xx, yy), lines, SAGE_D, 40, ink=IVORY, ink2=GOLD), x, 690, shadow=10, dur=0.45)
    ap(img, t, ts[6], tag("MANY CAREGIVERS NEVER USE IT: NO ONE TELLS THEM", 1560, 90, GOLD, GREEN_D, 38, border=(168, 118, 40), track=2), 1045, 925, shadow=10)

# ============================================================ BLOCCO 19 - nonni che crescono i nipoti
def draw19(img, t):
    ts = starts(19)
    common(img, t, "GRANDPARENTS RAISING GRANDCHILDREN")
    rail(img, t, 7)
    ap(img, t, ts[0], panel(760, 500, border=GOLD), 620, 400, pop_=False, dx=-50, dur=0.6, shadow=14)
    ap(img, t, ts[1], sprite("fam19", 640, 240, lambda c: (ic_person(c, 150, 130, 1.5, GOLD), ic_person(c, 300, 130, 1.5, SAGE), ic_person(c, 440, 170, 0.95, (70, 120, 176)), ic_person(c, 520, 170, 0.8, CORAL))), 620, 330, shadow=8)
    ap(img, t, ts[1] + 0.4, txt("RELATIVES 55 AND OLDER", 40, IVORY, 2), 620, 490)
    ap(img, t, ts[1] + 0.7, txt("RAISING CHILDREN UNDER 18", 40, GOLD, 2), 620, 545)
    ap(img, t, at(19, 1, "like grandparents"), tag("LIKE GRANDPARENTS RAISING GRANDCHILDREN", 700, 56, IVORY, GREEN_D, 24, border=GOLD, track=1), 620, 620, shadow=6)
    sv = [("RESPITE", lambda c, x, y: ic_moon(c, x, y, 0.7), 215, at(19, 2, "respite")), ("COUNSELING", lambda c, x, y: ic_people(c, x, y + 4, 0.6), 335, at(19, 2, "counseling")),
          ("SUPPORT GROUPS", lambda c, x, y: ic_heart(c, x, y - 4, 0.8), 455, at(19, 2, "support groups")), ("TRAINING", lambda c, x, y: ic_clipboard(c, x, y, 0.62), 575, at(19, 2, "training"))]
    ap(img, t, ts[2], txt("BESIDES RESPITE IT CAN OFFER", 32, GOLD, 3), 1450, 160)
    for nm, ic, y, tt in sv:
        ap(img, t, tt, row_card(("sv19", nm), 820, 100, lambda c, x, yy, ic=ic: ic(c, x, yy), [nm], SAGE_D, 36, ink=IVORY, ink2=IVORY), 1450, y + 20, pop_=False, dx=60, dur=0.45, shadow=8)
    ap(img, t, ts[3], row_card("cost19", 760, 190, lambda c, x, y: ic_coin(c, x, y, 40), ["THE COST DEPENDS ON YOUR", "LOCAL PROGRAM AND", "YOUR INCOME"], SAGE_D, 30, ink=IVORY, ink2=GOLD), 620, 770, pop_=False, dy=40, dur=0.5, shadow=10)
    ap(img, t, ts[4], row_card("mist19", 820, 190, lambda c, x, y: warn_tri(c, x, y, 0.8, CORAL), ["THE MISTAKE: WAITING UNTIL", "YOU'RE AT THE END", "OF YOUR STRENGTH"], CORAL, 30, ink=IVORY, ink2=IVORY), 1450, 770, pop_=False, dy=40, dur=0.5, shadow=10)
    ap(img, t, ts[5], stamp("YOU DON'T", 280, 58, GREEN_OK, 30), 1690, 893, rot=-4, shadow=8)
    ap(img, t, ts[6], tag("ASK YOUR AREA AGENCY ON AGING ABOUT CAREGIVER SUPPORT", 1620, 86, GOLD, GREEN_D, 34, border=(168, 118, 40), track=2), 1045, 965, shadow=10, pop_=False, dy=24, dur=0.5)

# ============================================================ BLOCCO 20 - protezione dai distacchi
def draw20(img, t):
    ts = starts(20)
    common(img, t, "NUMBER EIGHT: PROTECTION FROM A SHUTOFF")
    rail(img, t, 8)
    ap(img, t, ts[1], tag("RULES THAT LIMIT WHEN A UTILITY CAN DISCONNECT YOU", 1100, 62, GOLD, GREEN_D, 30, track=2), 1045, 165, shadow=8)
    pr = [("mon", lambda c, x, y: (ic_calendar7(c, x - 14, y, 1.1), ic_snowflake(c, x + 50, y - 30, 0.9)), ["CERTAIN WINTER", "MONTHS"], 500, ts[2]),
          ("frz", lambda c, x, y: ic_thermo(c, x, y, 1.1), ["DAYS WHEN IT'S", "FREEZING OUTSIDE"], 1045, ts[3]),
          ("old", lambda c, x, y: (ic_person(c, x - 30, y + 6, 0.9, GOLD), ic_heart(c, x + 40, y - 20, 0.7)), ["OLDER ADULTS, OR A HOME", "WITH SOMEONE SERIOUSLY ILL"], 1590, ts[4])]
    for key, ic, lines, x, tt in pr:
        ap(img, t, tt, card(("p20", key), 520, 320, ic, lines, GREEN_OK, 34, ink=IVORY, ink2=GOLD, ih=0.5), x, 360, shadow=12, dur=0.5)
    t5 = ts[5]
    ap(img, t, t5, tag("BUT HERE'S THE CATCH", 520, 70, CORAL, IVORY, 34, track=3), 1045, 565, shadow=10)
    ap(img, t, ts[6], card("evw20", 760, 330, lambda c, x, y: (c.poly([(x - 120, y - 40), (x - 40, y - 60), (x + 40, y - 40), (x + 120, y - 60), (x + 120, y + 30), (x + 40, y + 50), (x - 40, y + 30), (x - 120, y + 50)], fill=(34, 92, 72)),
                                                                 ic_pin(c, x - 70, y - 10, 0.6, GOLD), ic_pin(c, x + 10, y + 6, 0.6, CORAL), ic_pin(c, x + 90, y - 20, 0.6, ICE)),
                                ["THESE RULES ARE NOT THE", "SAME EVERYWHERE"], CORAL, 32, ink=IVORY, ink2=GOLD, ih=0.5), 620, 800, pop_=False, dy=40, dur=0.6, shadow=12)
    ap(img, t, at(20, 6, "and they usually"), row_card("stop20", 860, 150, lambda c, x, y: (ic_coin(c, x, y, 34), no_cross(c, x, y, 0.9)), ["USUALLY NOT IF YOU", "SIMPLY STOP PAYING"], CORAL, 34, ink=IVORY, ink2=IVORY), 1430, 720, pop_=False, dx=60, dur=0.5, shadow=10)
    ap(img, t, ts[7], row_card("plan20", 860, 150, lambda c, x, y: ic_calendar7(c, x, y, 0.95), ["MANY REQUIRE A PAYMENT", "PLAN THAT YOU KEEP"], GREEN_OK, 34, ink=IVORY, ink2=GREEN_OK), 1430, 900, pop_=False, dx=60, dur=0.5, shadow=10)

# ============================================================ BLOCCO 21 - chiama l'utility, poi la commissione
def draw21(img, t):
    ts = starts(21)
    common(img, t, "WHAT TO DO: CALL AND ASK")
    rail(img, t, 8)
    ap(img, t, ts[0], row_card("warn21", 640, 330, lambda c, x, y: (ic_building(c, x - 34, y + 4, 0.8), ic_bolt(c, x + 44, y, 0.7)), ["STATE RULES OFTEN DON'T", "APPLY TO CITY OWNED", "UTILITIES OR RURAL", "ELECTRIC CO OPS"], CORAL, 30, ink=IVORY, ink2=GOLD), 560, 315, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[1], step_card(1, "CALL YOUR UTILITY", ["ASK WHAT WINTER PROTECTION THEY OFFER", "ASK TO BE LISTED AS AN OLDER OR MEDICAL CUSTOMER"], 1000, 250, GOLD, 40, 26), 1360, 280, pop_=False, dx=60, dur=0.6, shadow=10)
    ap(img, t, ts[2], step_card(2, "IF THEY SAY NO", ["CALL YOUR STATE'S PUBLIC UTILITY COMMISSION", "THE OFFICE THAT MAKES THE RULES FOR MOST UTILITIES"], 1000, 250, GOLD, 40, 26), 1360, 560, pop_=False, dx=60, dur=0.6, shadow=10)
    ap(img, t, ts[3], step_card(3, "ASK ONE QUESTION", [], 1000, 250, GOLD, 40, 26), 1360, 840, pop_=False, dx=60, dur=0.6, shadow=10)
    ap(img, t, ts[4], bubble_spr(840, 96, IVORY, ["WHAT PROTECTS A SENIOR FROM A WINTER", "SHUTOFF IN THIS STATE?"], DARK, 30), 1420, 893, shadow=8)
    ap(img, t, ts[5], sprite("pad21", 640, 340, lambda c: (c.rrect((6, 6, 634, 334), 24, fill=(246, 236, 190), outline=(200, 180, 110), width=6),
                                                      c.rrect((6, 6, 634, 70), 24, fill=(232, 196, 90)), c.d.rectangle(c._b((6, 40, 634, 70)), fill=(232, 196, 90)),
                                                      c.text((320, 40), "WRITE IT DOWN", FONT_SANS, 34, GREEN_D, track=3),
                                                      c.text((60, 130), "THE NAME", FONT_SANS, 40, GREEN_D, anchor="lm", track=2), c.line([(60, 160), (580, 160)], (150, 140, 90), 4),
                                                      c.text((60, 230), "THE DATE", FONT_SANS, 40, GREEN_D, anchor="lm", track=2), c.line([(60, 260), (580, 260)], (150, 140, 90), 4))), 540, 790, shadow=12, rot=-2)

# ============================================================ BLOCCO 22 - la caldaia
def draw22(img, t):
    ts = starts(22)
    common(img, t, "NUMBER NINE: THE FURNACE THAT STOPS")
    rail(img, t, 9)
    ap(img, t, ts[0], card("fur22", 560, 400, lambda c, x, y: (ic_furnace(c, x - 20, y + 6, 1.7, False), ic_snowflake(c, x + 100, y - 40, 1.6)), ["THE FURNACE THAT", "STOPS IN JANUARY"], GOLD, 40, ink=IVORY, ink2=GOLD, ih=0.55), 530, 350, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[1], panel(560, 420, border=SAGE_D), 530, 790, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[1] + 0.3, house_bg(), 530, 790, scale=0.42, shadow=6)
    ap(img, t, ts[1] + 0.6, tag("THAT NIGHT: 9°F, 2:00 AM", 480, 56, ICE, GREEN_D, 26, track=2), 530, 610, shadow=8)
    ap(img, t, ts[2], tag("THE HELP MOST PEOPLE NEVER HEAR ABOUT", 900, 64, GOLD, GREEN_D, 32, border=(168, 118, 40), track=2), 1360, 180, shadow=8)
    ap(img, t, ts[3], row_card("lih22", 1000, 190, lambda c, x, y: ic_flame(c, x, y + 4, 0.9), ["L I H E A P", "THE FEDERAL HEATING PROGRAM"], GOLD, 52, ink=GOLD, ink2=IVORY), 1360, 330, pop_=False, dx=60, dur=0.6, shadow=12)
    ap(img, t, at(22, 3, "allows money"), tag("MONEY FOR ENERGY RELATED HOME REPAIRS", 900, 64, IVORY, GREEN_D, 30, border=GOLD, track=2), 1360, 490, shadow=8)
    ap(img, t, ts[4], card("wea22", 490, 400, lambda c, x, y: (ic_furnace(c, x - 30, y + 4, 1.1), ic_wrench(c, x + 56, y + 14, 1.0, GOLD)), ["MOST STATES:", "FURNACE REPAIR OR", "REPLACEMENT THROUGH", "WEATHERIZATION"], GOLD, 32, ink=IVORY, ink2=GOLD, ih=0.5), 1110, 790, pop_=False, dy=50, dur=0.6, shadow=12)
    ap(img, t, ts[5], card("cri22", 490, 400, lambda c, x, y: (ic_flame(c, x - 24, y + 4, 0.9), warn_tri(c, x + 52, y - 6, 0.6, CORAL)), ["SOME STATES ALSO:", "THROUGH CRISIS HELP", "LOSING HEAT IN WINTER", "IS AN EMERGENCY"], CORAL, 32, ink=IVORY, ink2=GOLD, ih=0.5), 1610, 790, pop_=False, dy=50, dur=0.6, shadow=12)


def ic_fridge(c, cx, cy, s):
    c.rrect((cx - 34 * s, cy - 54 * s, cx + 34 * s, cy + 54 * s), 10 * s, fill=(226, 232, 236), outline=(170, 176, 182), width=4)
    c.line([(cx - 34 * s, cy - 8 * s), (cx + 34 * s, cy - 8 * s)], (170, 176, 182), 4 * s)
    c.rrect((cx + 18 * s, cy - 40 * s, cx + 24 * s, cy - 18 * s), 3, fill=(140, 146, 152)); c.rrect((cx + 18 * s, cy + 6 * s, cx + 24 * s, cy + 28 * s), 3, fill=(140, 146, 152))
    c.rrect((cx - 24 * s, cy - 36 * s, cx + 6 * s, cy - 18 * s), 3, fill=(250, 230, 130))

def ic_thumb(c, cx, cy, s, col=GOLD):
    c.poly([(cx - 40 * s, cy - 6 * s), (cx - 10 * s, cy - 6 * s), (cx + 14 * s, cy - 60 * s), (cx + 40 * s, cy - 50 * s), (cx + 26 * s, cy - 6 * s), (cx + 62 * s, cy - 6 * s), (cx + 56 * s, cy + 56 * s), (cx - 40 * s, cy + 56 * s)], fill=col)
    c.rrect((cx - 64 * s, cy - 6 * s, cx - 38 * s, cy + 56 * s), 6, fill=(168, 118, 40))

def ic_bell(c, cx, cy, s, col=GOLD):
    c.d.pieslice(c._b((cx - 36 * s, cy - 50 * s, cx + 36 * s, cy + 22 * s)), 180, 360, fill=col)
    c.rrect((cx - 36 * s, cy - 14 * s, cx + 36 * s, cy + 30 * s), 4, fill=col)
    c.rrect((cx - 46 * s, cy + 24 * s, cx + 46 * s, cy + 36 * s), 6 * s, fill=col)
    c.ell((cx - 10 * s, cy + 36 * s, cx + 10 * s, cy + 56 * s), fill=col)

# ============================================================ BLOCCO 23 - priorita' agli anziani, l'errore, il numero
def draw23(img, t):
    ts = starts(23)
    common(img, t, "BEFORE YOU SIGN ANYTHING, CALL")
    rail(img, t, 9)
    ap(img, t, ts[0], card("doe23", 640, 290, lambda c, x, y: (ic_bolt(c, x - 44, y, 0.7), ic_house(c, x + 44, y + 4, 0.85, IVORY, CORAL)), ["WEATHERIZATION: PRIORITY", "TO THE ELDERLY", "RENTERS CAN APPLY TOO"], GOLD, 32, ink=IVORY, ink2=GOLD, ih=0.5), 560, 295, pop_=False, dx=-50, dur=0.6, shadow=12)
    ap(img, t, ts[1], tag("THE MISTAKE", 330, 56, CORAL, IVORY, 28, track=3), 560, 485, shadow=8)
    st = [("call", lambda c, x, y: ic_phone(c, x, y, 0.8), ["CALL A REPAIR", "COMPANY FIRST"], 590, at(23, 2, "People call")),
          ("bill", lambda c, x, y: ic_coin(c, x, y, 34), ["PAY A HUGE BILL"], 730, at(23, 2, "pay a huge")),
          ("late", lambda c, x, y: (c.ell((x - 30, y - 30, x + 30, y + 30), fill=GREEN_OK), check_ic(c, x, y, 0.8, GREEN_D)), ["LATER FIND OUT", "THERE WAS HELP"], 870, at(23, 2, "only later"))]
    for key, ic, lines, y, tt in st:
        ap(img, t, tt, row_card(("m23", key), 640, 120, lambda c, x, yy, ic=ic: ic(c, x, yy), lines, CORAL if key != "late" else GREEN_OK, 30, ink=IVORY, ink2=IVORY), 560, y, pop_=False, dx=-50, dur=0.45, shadow=8)
    for y, tt in ((660, at(23, 2, "pay a huge")), (800, at(23, 2, "only later"))):
        ap(img, t, tt, sprite("dn23", 60, 50, lambda c: c.poly([(8, 8), (52, 8), (30, 44)], fill=CORAL)), 560, y, dur=0.3)
    ap(img, t, ts[3], panel(920, 640, border=GOLD), 1400, 470, pop_=False, dx=50, dur=0.6, shadow=14)
    ap(img, t, ts[3] + 0.2, tag("BEFORE YOU SIGN ANYTHING", 600, 62, CORAL, IVORY, 30, track=2), 1400, 205, shadow=8)
    ap(img, t, ts[3] + 0.5, sprite("ph23", 160, 200, lambda c: ic_phone(c, 80, 100, 1.6)), 1085, 330)
    ap(img, t, ts[3] + 0.7, txt("CALL THE ENERGY", 46, IVORY, 3), 1500, 310)
    ap(img, t, ts[3] + 0.9, txt("HELP LINE", 60, GOLD, 4), 1440, 375)
    NUM = "1-866-674-6327"
    t4 = ts[4]
    if t >= t4:
        n = min(len(NUM), int((t - t4) / 0.2) + 1)
        put_left(img, txt(NUM[:n], 92, GOLD, 2), 1400 - tw(NUM, 92, 2) / 2 - 20, 520, 92)
    ap(img, t, ts[5], tag("OR GO TO", 220, 52, IVORY, GREEN_D, 28, track=3), 1130, 650, shadow=6)
    ap(img, t, ts[5] + 0.3, sprite("url23", 560, 96, lambda c: (c.rrect((4, 4, 556, 92), 46, fill=IVORY, outline=GOLD, width=6), magnifier(c, 60, 46, 17, GREEN_D, 6),
                                                         c.text((100, 48), "energyhelp.us", FONT_SANS, 46, GREEN_D, anchor="lm"))), 1500, 650, shadow=8)
    ap(img, t, ts[6], bubble_spr(880, 120, IVORY, ["I'M OVER 60. MY HEAT IS OUT OR FAILING.", "WHAT DOES MY STATE OFFER?"], DARK, 32), 1400, 915, shadow=10)
    ap(img, t, ts[6] + 0.3, tag("TELL THEM", 250, 50, GOLD, GREEN_D, 26, track=3), 1030, 805, shadow=6)

# ============================================================ BLOCCO 24 - il riepilogo dei nove
def num_badge(n):
    return sprite(("nb24", n), 60, 60, lambda c: (c.ell((3, 3, 57, 57), fill=GOLD, outline=GREEN_D, width=4), c.text((30, 31), str(n), FONT_SANS, 30, GREEN_D)))

def draw24(img, t):
    ts = starts(24)
    common(img, t, "ALL NINE, TOGETHER")
    rail(img, t, 10)
    ap(img, t, ts[0], tag("MONEY CAN RUN OUT DURING THE WINTER", 740, 60, CORAL, IVORY, 24, track=1), 640, 190, shadow=8)
    ap(img, t, ts[0] + 1.6, tag("APPLY IN THE FALL, EVEN BEFORE ANYTHING BREAKS", 800, 60, GOLD, GREEN_D, 22, track=1), 1440, 190, shadow=8)
    ap(img, t, ts[1], tag("WAITING LIST? ASK TO BE PUT ON IT TODAY, NOT WHEN IT'S COLD", 1180, 60, GREEN_OK, GREEN_D, 24, track=1), 1040, 265, shadow=8)
    ap(img, t, ts[2], txt("ALL NINE TOGETHER", 44, GOLD, 5), 1045, 335)
    items = [(lambda c, x, y: ic_alarm_ceiling(c, x, y, 1.0), ["SMOKE ALARM", "INSTALLED"], 500, 465),
             (lambda c, x, y: ic_broom(c, x, y, 1.0), ["HOMEMAKER", "HELP"], 1045, 465),
             (lambda c, x, y: ic_bucket(c, x, y, 1.0), ["CHORE HELP:", "THE HEAVY JOBS"], 1590, 465),
             (lambda c, x, y: ic_meal(c, x, y + 4, 1.0), ["A HOT MEAL", "AT YOUR DOOR"], 500, 680),
             (lambda c, x, y: ic_wrench(c, x, y, 1.2, IVORY), ["GRAB BARS", "AND REPAIRS"], 1045, 680),
             (lambda c, x, y: ic_scale(c, x, y, 0.9), ["A LAWYER:", "HOUSING, SCAMS"], 1590, 680),
             (lambda c, x, y: ic_people(c, x, y + 4, 0.8), ["A BREAK FOR", "CAREGIVERS"], 500, 895),
             (lambda c, x, y: ic_shield_heat(c, x, y, 0.95), ["PROTECTION FROM", "A WINTER SHUTOFF"], 1045, 895),
             (lambda c, x, y: ic_furnace(c, x, y + 2, 0.95), ["HELP WHEN THE", "FURNACE STOPS"], 1590, 895)]
    for i, (ic, lines, x, y) in enumerate(items):
        tt = ts[3 + i]
        ap(img, t, tt, row_card(("g24", i), 520, 190, lambda c, xx, yy, ic=ic: ic(c, xx, yy), lines, GOLD if i == 8 else SAGE_D, 32, ink=IVORY, ink2=GOLD), x, y, shadow=8, dur=0.45)
        ap(img, t, tt + 0.15, num_badge(i + 1), x - 245, y - 82, dur=0.35)

# ============================================================ BLOCCO 25 - la telefonata
def draw25(img, t):
    ts = starts(25)
    common(img, t, "THE ONE PHONE CALL")
    ap(img, t, ts[0], panel(770, 470, border=GOLD), 625, 385, pop_=False, dx=-50, dur=0.6, shadow=14)
    ap(img, t, ts[1], txt("ELDERCARE LOCATOR", 54, GOLD, 3), 625, 215)
    ap(img, t, ts[1] + 0.4, txt("A PUBLIC SERVICE OF THE ADMINISTRATION", 24, SAGE, 2), 625, 275)
    ap(img, t, ts[1] + 0.6, txt("FOR COMMUNITY LIVING", 24, SAGE, 2), 625, 308)
    NUM = "1-800-677-1116"
    if t >= ts[2]:
        n = min(len(NUM), int((t - ts[2]) / 0.18) + 1)
        put_left(img, txt(NUM[:n], 86, IVORY, 2), 625 - tw(NUM, 86, 2) / 2 - 20, 410, 86)
    ap(img, t, ts[3], tag("CALL", 240, 66, GOLD, GREEN_D, 34, track=4), 480, 540, shadow=8)
    ap(img, t, ts[3] + 0.3, tag("OR SEND A TEXT", 360, 66, IVORY, GREEN_D, 30, border=GOLD, track=2), 790, 540, shadow=8)
    lines = [("I'M OVER 60.", ts[5], IVORY, 270), ("I LIVE IN [YOUR CITY].", at(25, 5, "I live in"), IVORY, 355), ("AND I NEED HELP AT HOME THIS WINTER.", at(25, 5, "and I need"), IVORY, 440),
             ("PLEASE CONNECT ME TO MY AREA AGENCY ON AGING.", ts[6], GOLD, 540)]
    ap(img, t, ts[4], panel(810, 470, border=SAGE_D), 1455, 385, pop_=False, dx=50, dur=0.6, shadow=14)
    ap(img, t, ts[4] + 0.3, tag("SAY THIS", 260, 66, CORAL, IVORY, 34, track=4), 1455, 195, shadow=8)
    for s_, tt, col, y in lines:
        w_ = 740
        sz = 36
        while tw(s_, sz, 1) > w_ - 60 and sz > 16: sz -= 2
        ap(img, t, tt, tag(s_, w_, 76 if y < 500 else 96, IVORY if col == IVORY else GOLD, GREEN_D, sz, track=1), 1455, y, shadow=8, dur=0.4)
    ap(img, t, ts[7], txt("THAT ONE SENTENCE OPENS THE DOOR TO:", 40, GOLD, 4), 960, 665)
    P7 = PHRASES[25][7]
    six = [("HOMEMAKER", "HELP", lambda c, x, y: ic_broom(c, x, y, 1.1), "homemaker"), ("CHORE", "HELP", lambda c, x, y: ic_bucket(c, x, y, 1.1), "chore"),
           ("MEALS", "", lambda c, x, y: ic_meal(c, x, y + 4, 1.1), "meals"), ("REPAIRS", "", lambda c, x, y: ic_wrench(c, x, y, 1.3, IVORY), "repairs"),
           ("LEGAL", "HELP", lambda c, x, y: ic_scale(c, x, y, 1.0), "legal"), ("CAREGIVER", "SUPPORT", lambda c, x, y: ic_people(c, x, y + 4, 0.9), "caregiver")]
    for i, (l1, l2, ic, key) in enumerate(six):
        x = 360 + i * 280
        lines_ = [l1, l2] if l2 else [l1]
        ap(img, t, at(25, 7, key), card(("six25", i), 260, 250, ic, lines_, GOLD, 30, ink=IVORY, ink2=GOLD, ih=0.5), x, 840, shadow=8, dur=0.45)

# ============================================================ BLOCCO 26 - la parte onesta
def draw26(img, t):
    ts = starts(26)
    common(img, t, "THE HONEST PART")
    ap(img, t, ts[0], stamp("THE HONEST PART", 760, 100, GOLD, 54), 960, 185, shadow=10)
    ap(img, t, ts[1], card("a26", 540, 280, lambda c, x, y: (ic_pin(c, x - 70, y, 0.9, GOLD), ic_pin(c, x, y + 6, 0.9, SAGE), ic_pin(c, x + 70, y, 0.9, SAGE), no_cross(c, x + 70, y + 4, 0.7)), ["NOT EVERY SERVICE", "EXISTS IN EVERY TOWN"], GOLD, 34, ink=IVORY, ink2=GOLD, ih=0.5), 420, 430, shadow=12)
    ap(img, t, ts[2], card("b26", 540, 280, lambda c, x, y: (ic_hourglass(c, x - 70, y, 0.9), ic_clipboard(c, x, y, 0.8), ic_coin(c, x + 70, y, 32)), ["WAITING LISTS, INCOME", "LIMITS, MONEY RUNS OUT"], GOLD, 32, ink=IVORY, ink2=GOLD, ih=0.5), 960, 430, shadow=12)
    ap(img, t, ts[3], card("c26", 540, 280, lambda c, x, y: ic_scroll(c, x, y, 1.1), ["WHAT I TOLD YOU:", "OFFICIAL PAGES TODAY"], GOLD, 34, ink=IVORY, ink2=GOLD, ih=0.5), 1500, 430, shadow=12)
    ap(img, t, ts[4], row_card("d26", 780, 240, lambda c, x, y: (ic_phone(c, x - 20, y, 0.9), ic_clipboard(c, x + 40, y + 10, 0.5)), ["CALL, ASK, AND GET THE", "ANSWER FOR YOUR AREA", "IN WRITING"], SAGE_D, 34, ink=IVORY, ink2=GOLD), 650, 730, shadow=12, pop_=False, dy=40, dur=0.5)
    ap(img, t, ts[5], row_card("e26", 780, 240, lambda c, x, y: (c.rrect((x - 40, y - 34, x + 40, y + 24), 18, fill=IVORY), c.poly([(x - 20, y + 20), (x - 6, y + 20), (x - 30, y + 46)], fill=IVORY), c.text((x, y - 5), "...", FONT_SANS, 40, DARK)), ["SOMETHING DOESN'T MATCH?", "TELL ME IN THE COMMENTS"], GOLD, 34, ink=IVORY, ink2=GOLD), 1470, 730, shadow=12, pop_=False, dy=40, dur=0.5)
    ap(img, t, ts[6], tag("THE MORE WE SHARE, THE FEWER PEOPLE SPEND THIS WINTER COLD AND ALONE", 1740, 90, GOLD, GREEN_D, 34, border=(168, 118, 40), track=2), 960, 950, shadow=10)

# ============================================================ BLOCCO 27 - cosa fare questa settimana
def draw27(img, t):
    ts = starts(27)
    common(img, t, "WHAT TO DO THIS WEEK")
    ap(img, t, ts[0], tag("THIS WEEK", 420, 70, GOLD, GREEN_D, 38, track=5), 685, 185, shadow=8)
    tk = [("t1", lambda c, x, y: ic_alarm_ceiling(c, x, y, 1.1), ["PUSH THE TEST BUTTON", "ON EVERY SMOKE ALARM"], 320, ts[1]),
          ("t2", lambda c, x, y: ic_fridge(c, x, y, 1.1), ["WRITE THE ELDERCARE LOCATOR", "NUMBER: 1-800-677-1116", "PUT IT ON YOUR FRIDGE"], 545, ts[2]),
          ("t3", lambda c, x, y: ic_phone(c, x, y, 1.0), ["CALL YOUR UTILITY: ASK ABOUT", "WINTER PROTECTION BEFORE", "THE FIRST COLD NIGHT"], 770, ts[3])]
    for key, ic, lines, y, tt in tk:
        ap(img, t, tt, row_card(("tk27", key), 890, 200, lambda c, x, yy, ic=ic: ic(c, x, yy), lines, GOLD, 34, ink=IVORY, ink2=GOLD), 685, y, pop_=False, dx=-60, dur=0.5, shadow=10)
        ap(img, t, tt + 0.8, sprite("cb27", 70, 70, lambda c: (c.rrect((4, 4, 66, 66), 12, fill=IVORY, outline=GOLD, width=5), check_ic(c, 36, 38, 0.9, GREEN_OK))), 1085, y, dur=0.4)
    ap(img, t, ts[4], tag("NONE OF THESE COSTS A DOLLAR", 890, 76, GREEN_OK, GREEN_D, 34, track=2), 685, 940, shadow=10)
    ap(img, t, ts[5], card("sh27", 670, 450, lambda c, x, y: (ic_house(c, x - 60, y + 6, 1.1, IVORY, GOLD), ic_person(c, x + 20, y + 10, 0.9, SAGE), ic_phone(c, x + 100, y, 0.8)),
                          ["SOMEONE OVER 60", "WHO LIVES ALONE", "SEND THEM THIS VIDEO"], GOLD, 38, ink=IVORY, ink2=GOLD, ih=0.5), 1525, 375, shadow=12, pop_=False, dx=50, dur=0.6)
    ap(img, t, at(27, 5, "or better"), card("tg27", 670, 360, lambda c, x, y: (ic_person(c, x - 56, y + 6, 0.9, GOLD), ic_person(c, x + 8, y + 6, 0.9, SAGE), ic_phone(c, x + 84, y, 0.9)),
                                           ["OR BETTER: SIT WITH THEM", "AND MAKE THE CALL TOGETHER"], GREEN_OK, 32, ink=IVORY, ink2=GREEN_OK, ih=0.5), 1525, 800, shadow=12, pop_=False, dx=50, dur=0.6)

# ============================================================ BLOCCO 28 - domanda, like, iscrizione
def draw28(img, t):
    ts = starts(28)
    common(img, t, "BEFORE YOU GO")
    ap(img, t, ts[0], bubble_spr(780, 290, IVORY, ["WHICH OF THESE", "NINE SURPRISED", "YOU THE MOST?"], DARK, 62), 590, 380, shadow=12)
    for i in range(9):
        ap(img, t, ts[0] + 0.8 + i * 0.12, num_badge(i + 1), 255 + i * 86, 690, scale=1.2, dur=0.35)
    ap(img, t, ts[1], tag("TELL ME BELOW", 440, 70, GOLD, GREEN_D, 36, track=3), 480, 790, shadow=8)
    ap(img, t, ts[1] + 0.3, tag("I READ EVERY COMMENT", 560, 70, IVORY, GREEN_D, 32, border=GOLD, track=2), 590, 880, shadow=8)
    ap(img, t, ts[2], sprite("th28", 260, 260, lambda c: ic_thumb(c, 130, 120, 2.0)), 1220, 320, shadow=12)
    ap(img, t, ts[2] + 0.3, txt("LIKE", 76, GOLD, 4), 1220, 500)
    ap(img, t, ts[2] + 0.9, sprite("sub28", 460, 130, lambda c: (c.rrect((4, 4, 456, 126), 64, fill=RED, outline=(255, 255, 255), width=6), c.text((230, 66), "SUBSCRIBE", FONT_SANS, 58, (255, 255, 255), track=3))), 1600, 320, shadow=12)
    ap(img, t, ts[2] + 1.6, txt("THE SENIOR ADVANTAGE", 46, IVORY, 3), 1460, 640)
    ap(img, t, ts[3], sprite("bell28", 160, 160, lambda c: ic_bell(c, 80, 76, 1.6)), 1460, 790, shadow=8)
    ap(img, t, ts[3] + 0.3, tag("SO YOU DON'T MISS THE NEXT ONE", 780, 90, GOLD, GREEN_D, 32, border=(168, 118, 40), track=2), 1460, 930, shadow=10)

# ============================================================ BLOCCO 29 - slide finale col disclaimer
def draw29(img, t):
    ts = starts(29)
    a0 = ease(seg(t, 0, .5))
    put(img, tspr("BEFORE YOU GO", FONT_SANS, 44, SAGE, track=18), 960, 100, alpha=a0)
    put(img, tspr("ALWAYS CONFIRM", FONT_SANS, 112, IVORY), 560, 290 - 30 * (1 - ease(seg(t, .3, .5))), alpha=ease(seg(t, .3, .5)))
    put(img, tspr("BEFORE YOU RELY", FONT_SANS, 112, GOLD), 560, 420 - 30 * (1 - ease(seg(t, .9, .5))), alpha=ease(seg(t, .9, .5)))
    bp = pop(t, 1.4, 0.5)
    def panel_():
        c = Cv(1000, 500)
        c.rrect((3, 3, 997, 497), 36, fill=CARD, outline=SAGE_D, width=5)
        return c.done()
    if bp[2] > 0:
        put(img, cache("p29", panel_), 580, 760, scale=bp[0], alpha=bp[1], shadow=16)
    lines = [("Rules, amounts and ages change", IVORY, ts[0] + 0.3), ("and differ by location and program.", IVORY, ts[0] + 1.6),
             ("Always confirm with the official source", GOLD, ts[1] + 0.2), ("before you rely on them.", GOLD, ts[1] + 1.3),
             ("General information,", SAGE, ts[2] + 0.2), ("not financial or legal advice.", SAGE, ts[2] + 1.2),
             ("This channel is not affiliated with", IVORY, ts[3] + 0.3), ("the American Red Cross, Meals on Wheels,", IVORY, ts[3] + 1.6),
             ("Rebuilding Together or any government agency.", IVORY, ts[3] + 2.8)]
    for i, (s_, col, st) in enumerate(lines):
        a = ease(seg(t, st, .5))
        if a > 0:
            put(img, tspr(s_, FONT_SANS_M if i > 3 else FONT_SANS, 32, col), 580, 575 + i * 48 - 20 * (1 - a), alpha=a)
    a = ease(seg(t, 2.0, .6))
    if a > 0:
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(lay)
        for x in range(1170, 1800, 60):
            g.line([(x, 250), (x + 34, 250)], fill=GOLD + (255,), width=5); g.line([(x, 710), (x + 34, 710)], fill=GOLD + (255,), width=5)
        for y in range(250, 710, 60):
            g.line([(1150, y), (1150, y + 34)], fill=GOLD + (255,), width=5); g.line([(1830, y), (1830, y + 34)], fill=GOLD + (255,), width=5)
        lay.putalpha(lay.getchannel("A").point(lambda v: int(v * a)))
        img.paste(lay, (0, 0), lay)
        put(img, tspr("WATCH NEXT", FONT_SANS, 54, GOLD), 1490, 790, alpha=a)
    put(img, tspr("THANK YOU FOR WATCHING", FONT_SANS, 40, SAGE), 1490, 880, alpha=ease(seg(t, 5.5, .5)))

DRAW = {11: draw11, 12: draw12, 13: draw13, 14: draw14, 15: draw15, 16: draw16, 17: draw17, 18: draw18, 19: draw19, 20: draw20, 21: draw21, 22: draw22, 23: draw23, 24: draw24, 25: draw25, 26: draw26, 27: draw27, 28: draw28, 29: draw29}

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
