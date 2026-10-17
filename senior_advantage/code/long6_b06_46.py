"""Video lungo 6 (AMTRAK) - blocchi 6-46. 1920x1080, 30 fps. Voce: COPIONE-VIDEO-AMTRAK.md.
Durate dalla timeline dell'utente (16/10/2026), vedi PASSAGGIO-CHAT.md.
Layout nuovi rispetto ai video precedenti: tabellone partenze, linea del treno con 10 fermate (punti 1-10),
vagoni-scheda, telefono con prenotazione, bilancia, barre di rimborso, biglietti, ecc.
Uso: OUT=cartella SA_TMP=/tmp/x python3 long6_b06_46.py <blocco> [fotogrammi]
     python3 long6_b06_46.py frame <blocco> <secondi> <file.png>"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from long6_b02_05 import *
from long5_b16_20 import ic_wheelchair
from long4_b36_50 import ic_cal, ic_cross
from long5_b01_05 import ic_plane

DUR = {6: 341, 7: 267, 8: 369, 9: 634, 10: 425, 11: 409, 12: 533, 13: 228, 14: 321, 15: 470, 16: 300, 17: 503,
       18: 487, 19: 274, 20: 441, 21: 301, 22: 429, 23: 577, 24: 386, 25: 405, 26: 495, 27: 450, 28: 401, 29: 561,
       30: 351, 31: 501, 32: 246, 33: 538, 34: 554, 35: 146, 36: 481, 37: 465, 38: 485, 39: 717, 40: 554, 41: 570,
       42: 429, 43: 297, 44: 167, 45: 202, 46: 454}
PHRASES = {
    6: ["Everything here comes from Amtrak's own pages, on amtrak dot com.", "No rumors.", "I'm not paid by Amtrak,",
        "and rules change,", "so always check before you book."],
    7: ["Number one.", "The senior discount.", "If you're sixty five or older,", "Amtrak gives you ten percent off most rail fares,", "on most trains."],
    8: ["Here's the mistake.", "The discount doesn't appear by itself.", "When you search for a ticket,",
        "you have to choose Senior as the traveler type.", "If you leave it on Adult,", "you pay the adult price."],
    9: ["Two more things.", "It does not apply to the charge for a sleeping room,", "only to the rail fare.",
        "And you need proof of age,", "when you buy the ticket and again on the train.",
        "So keep your I D in your pocket, not in your suitcase.", "And if you ride a train that crosses into Canada with VIA Rail,",
        "the senior discount there starts at sixty."],
    10: ["It also may not combine with other offers, so compare.", "Sometimes a sale fare is cheaper than the discount.",
         "Your action is simple.", "Every time you book, choose Senior,", "then compare the prices before you pay."],
    11: ["Number two.", "Twenty four hours to change your mind.", "If you book a reserved ticket", "and cancel within twenty four hours of buying it,",
         "before the train leaves,", "Amtrak gives you a full refund to your original payment."],
    12: ["Who does this help?", "Anyone who books in a hurry,", "books for a grandchild,", "or isn't sure about the date.",
         "Book the price you like,", "then check your calendar calmly at home.", "You have one full day.",
         "Just know that for unreserved tickets,", "the window is only one hour."],
    13: ["Number three.", "The fare you pick decides what you get back.", "And this is where many seniors lose money without knowing it."],
    14: ["With a Flex fare,", "you can cancel before the train leaves and get all your money back,", "with no fee.",
         "You can also change it with no fee.", "You only pay the difference in price."],
    15: ["With a Value fare, the cheaper one,", "you can't change it.", "If you cancel before departure, you get seventy percent back.",
         "So on a one hundred dollar ticket,", "you get seventy dollars,", "and thirty are gone.", "With a Sale fare,", "you get only half back."],
    16: ["Now the trap.", "If you don't show up,", "and you don't cancel before the train leaves,", "you lose the whole value of that trip.",
         "Every dollar.", "Even on a Flex fare."],
    17: ["So here's your action.", "If your plans might change,", "a doctor's visit, the weather, your health,",
         "look at the Flex price before you choose.", "And if you can't go,", "cancel online, in the app, or by phone,",
         "before the train leaves.", "Never just stay home."],
    18: ["Number four.", "Your bags.", "On Amtrak, each traveler can bring one personal item and two carry on bags,", "at no charge.",
         "The personal item can weigh up to twenty five pounds", "and has to fit under the seat.", "Each carry on can weigh up to fifty pounds."],
    19: ["And on trains with checked baggage,", "two checked bags are free.", "Extra bags cost twenty dollars each.", "Compare that with your last flight."],
    20: ["The mistake is bringing one bag too many,", "or one that's too big.", "That's twenty dollars for each extra piece.",
         "Your action: before you leave, count your bags.", "One small,", "two medium,", "and the big ones checked."],
    21: ["Number five.", "Someone to carry your bags.", "At many big stations, Amtrak has Red Caps.", "They carry your luggage,", "and Amtrak calls this help free."],
    22: ["You'll find them at twelve major stations,", "like Chicago, New York, Washington, Philadelphia, Boston, Los Angeles and Seattle.",
         "They wear red shirts and red caps.", "Only accept help from someone in that uniform."],
    23: ["Every bag they handle gets a claim check,", "so keep that ticket safe.", "A tip is welcome,", "but the service itself costs nothing.",
         "And at a number of stations, Amtrak also has self service handcarts.", "Your action: look for the red cap,",
         "and simply say, can you help me with my bags?"],
    24: ["Number six.", "Help getting to your train.", "If walking far or stairs are hard for you,", "you can ask Amtrak for help at the station.",
         "A station wheelchair,", "or a staff member who takes you to your train."],
    25: ["The best way is to ask when you make your reservation.", "You can do it on amtrak dot com,",
         "or by phone at one, eight hundred, U S A, rail.", "Most staffed stations have courtesy wheelchairs."],
    26: ["Then arrive at least one hour before your train,", "and tell an Amtrak agent you're there.", "They also help you to and from the restroom,",
         "and with stairs.", "The mistake is arriving ten minutes early", "and hoping someone notices you.", "Nobody will guess."],
    27: ["Number seven.", "The things you must reserve before you go.", "If you need a ramp or a lift to get on the train,",
         "Amtrak asks you to reserve it.", "And if you need an accessible seat,", "even without a wheelchair,", "you can reserve that too."],
    28: ["Here's the catch.", "These seats are limited.", "Amtrak says to book early to make sure one is available.",
         "The person who books early gets the seat.", "The person who asks at the platform may find none left."],
    29: ["The same goes for oxygen.", "Amtrak allows it for passengers with a disability,", "but you can't add it on the website.",
         "You call one, eight hundred, U S A, rail,", "and reserve in advance.", "Your machine must run at least four hours without power from the train,",
         "so check your batteries."],
    30: ["Number eight.", "Ice for your medicine.", "If you take medication that must stay cool,",
         "Amtrak says it can give you ice for your cooler or container.", "Most riders never ask."],
    31: ["And keep every pill with you,", "never in a checked bag.", "You can't reach checked bags during the trip,",
         "and you must be able to take your medication by yourself.", "Your action: a small cooler,", "and one sentence to the crew.",
         "Could I get some ice for my medicine?"],
    32: ["Number nine.", "Your own food.", "You're allowed to bring your own food and drinks on board,", "and eat them at your seat", "or in your private room."],
    33: ["Why does this matter?", "Amtrak itself warns that trains are sometimes delayed,", "and food supplies can run low.",
         "If you have diabetes or a special diet,", "it suggests carrying enough food for a delay.", "A sandwich,", "some fruit,", "crackers.", "Pack it at home."],
    34: ["One rule people break.", "Your own alcohol can only be enjoyed inside a private sleeping room,", "never in the public areas.",
         "And food you buy in the dining car is eaten in the dining car.", "Also, the crew can't heat or refrigerate your own food,",
         "so bring things that travel well."],
    35: ["Number ten.", "The one almost nobody knows.", "A note from your doctor."],
    36: ["Remember the Value fare,", "the one you can't change,", "where you lose part of the money if you cancel?", "If you get sick,",
         "Amtrak's rule says that with a note from your doctor,", "it waives the change and cancellation fees",
         "for the sick passenger and the people traveling with them."],
    37: ["Think about what that means.", "You booked the cheaper ticket for you and your partner.", "A week before the trip,",
         "you get the flu,", "or you have a fall.", "Without the note, part of that money is gone.", "With the note, those fees go away for both of you."],
    38: ["The mistake is staying home and saying nothing.", "Remember, if you don't cancel before the train leaves, you lose the whole trip.",
         "So the moment you know you can't go,", "call Amtrak before departure,", "say you're sick,", "and ask what they need from your doctor."],
    39: ["So let's put all ten together.", "Choose Senior when you book.", "Use the twenty four hour window.", "Pick the right fare.",
         "Bring your free bags.", "Let a Red Cap carry them.", "Ask for station help when you book.", "Reserve your seat, ramp or oxygen early.",
         "Ask for ice for your medicine.", "Bring your own food.", "And remember the doctor's note."],
    40: ["And the one sentence that makes almost all of these work?", "Say it when you book,", "not on the platform.",
         "I'm over sixty five, and I need.", "Then finish it.", "A senior fare.", "Help with my bags.", "A wheelchair to the train.",
         "Amtrak can only give you what you ask for."],
    41: ["Now the honest part.", "Fares, stations and services change,", "and they differ from route to route.",
         "What I told you comes from Amtrak's pages today.", "Check amtrak dot com before you book.", "And if something doesn't match,",
         "tell me in the comments, so I can tell everyone else."],
    42: ["Here's what to do this week.", "Put your I D where you'll find it.", "Write down one, eight hundred, U S A, rail.",
         "And next time you look at a ticket,", "choose Senior,", "and compare the Flex price before you pay."],
    43: ["If you know someone over sixty five", "who takes the train to see the grandkids,", "send them this video.",
         "It might save them a heavy suitcase,", "or a whole ticket."],
    44: ["Which of these ten surprised you the most?", "Tell me below.", "I read every comment."],
    45: ["If this helped you,", "like this video", "and subscribe to The Senior Advantage,", "so you don't miss the next one."],
    46: ["Rules, amounts and ages change and differ by route and fare.", "Always confirm with Amtrak before you rely on them.",
         "General information, not financial advice.", "This channel is not affiliated with Amtrak."],
}
def starts(b):
    ph = PHRASES[b]; tot = sum(len(p) for p in ph); dur = DUR[b] / FPS * 0.96
    out, c = [], 0
    for p in ph:
        out.append(0.1 + dur * c / tot); c += len(p)
    return out

def last_t(b, t0):
    return max(t0, DUR[b] / FPS * 0.80)

RED = (214, 108, 96)
RED_D = (176, 70, 62)
AMBER = (246, 190, 80)
BOARD = (12, 30, 26)

# ------------------------------------------------------------------ testo che si adatta
_md = ImageDraw.Draw(Image.new("L", (4, 4)))
def fit(text, size, maxw, track=0, path=None):
    path = path or FONT_SANS
    while size > 16:
        w = _md.textlength(text, font=font(path, int(size))) + track * max(0, len(text) - 1)
        if w <= maxw:
            return size
        size -= 2
    return size

def ftext(c, xy, text, size, col, maxw, anchor="mm", track=1, path=None):
    s = fit(text, size, maxw, track, path)
    c.text(xy, text, path or FONT_SANS, s, col, anchor=anchor, track=track)

def T(text, size, col=IVORY, maxw=1700, track=1):
    s = fit(text, size, maxw, track)
    return txt(text, s, col, track)

def cardt(key, w, h, border, icon=None, iy=None, lines=(), fill=CARD_BG):
    """scheda: icona (funzione c,cx,cy) + righe [(testo, size, colore, y)]"""
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 28, fill=fill, outline=border, width=6)
        if icon:
            icon(c, w / 2, iy)
        for (s_, sz, col, y) in lines:
            ftext(c, (w / 2, y), s_, sz, col, w - 56)
    return sprite(("cardt6", key), w, h, fn)

def pill(text, size, w, h=76, fill=IVORY, ink=GREEN_D, border=GOLD):
    s = fit(text, size, w - 60, 2)
    return pill_spr(text, s, w, h, fill, ink, border=border, track=2)

def bub(text, w, h=120, size=44, fill=IVORY, ink=GREEN_D, tail="left"):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 34), 30, fill=fill, outline=GOLD, width=6)
        tx = 90 if tail == "left" else w - 120
        c.poly([(tx, h - 38), (tx - 10, h - 2), (tx + 50, h - 38)], fill=fill)
        ftext(c, (w / 2, (h - 34) / 2 + 3), text, size, ink, w - 70)
    return sprite(("bub6", text, w, h, fill), w, h, fn)

def stamp6(text, w, h, col):
    def fn(c):
        c.rrect((5, 5, w - 5, h - 5), 20, fill=PANEL_FILL, outline=col, width=8)
        c.rrect((17, 17, w - 17, h - 17), 12, outline=col, width=3)
        ftext(c, (w / 2, h / 2 + 2), text, h * 0.40, col, w - 70, track=3)
    return sprite(("stamp6", text, w, h, col), w, h, fn)

# ------------------------------------------------------------------ icone nuove
def ic_check_c(c, cx, cy, r, col=GREEN_OK):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=col, outline=GREEN_D, width=3)
    check_ic(c, cx, cy + r * 0.05, r / 40, GREEN_D)

def ic_x_c(c, cx, cy, r, col=RED):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=col, outline=RED_D, width=3)
    ic_x(c, cx, cy, r / 70, IVORY, 14)

def ic_browser6(c, cx, cy, s, url="amtrak.com"):
    w, h = 300 * s, 200 * s
    c.rrect((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), 16 * s, fill=IVORY, outline=SAGE_D, width=4)
    c.rrect((cx - w / 2, cy - h / 2, cx + w / 2, cy - h / 2 + 46 * s), 16 * s, fill=(214, 224, 214))
    c.d.rectangle(c._b((cx - w / 2, cy - h / 2 + 24 * s, cx + w / 2, cy - h / 2 + 46 * s)), fill=(214, 224, 214))
    c.rrect((cx - w / 2 + 70 * s, cy - h / 2 + 10 * s, cx + w / 2 - 14 * s, cy - h / 2 + 36 * s), 12 * s, fill=IVORY)
    c.text((cx - w / 2 + 84 * s, cy - h / 2 + 24 * s), url, FONT_SANS_M, 17 * s, GREEN_D, anchor="lm")
    for i, col in enumerate((RED, GOLD, GREEN_OK)):
        c.ell((cx - w / 2 + 12 * s + i * 18 * s, cy - h / 2 + 16 * s, cx - w / 2 + 24 * s + i * 18 * s, cy - h / 2 + 28 * s), fill=col)
    for k in range(4):
        c.rrect((cx - w / 2 + 24 * s, cy - 30 * s + k * 30 * s, cx - w / 2 + 24 * s + (230 if k % 2 == 0 else 170) * s, cy - 18 * s + k * 30 * s), 6, fill=(206, 212, 206))

def ic_speech_x(c, cx, cy, s):
    c.rrect((cx - 60 * s, cy - 44 * s, cx + 60 * s, cy + 30 * s), 20 * s, fill=IVORY)
    c.poly([(cx - 30 * s, cy + 26 * s), (cx - 40 * s, cy + 56 * s), (cx - 6 * s, cy + 26 * s)], fill=IVORY)
    for k in range(3):
        c.ell((cx - 34 * s + k * 28 * s, cy - 14 * s, cx - 20 * s + k * 28 * s, cy), fill=SAGE)
    ic_x(c, cx + 46 * s, cy - 40 * s, 0.55 * s, RED, 16)

def ic_coin_x(c, cx, cy, s):
    ic_coin(c, cx, cy, 46 * s)
    c.line([(cx - 60 * s, cy - 60 * s), (cx + 60 * s, cy + 60 * s)], RED, 14 * s)

def ic_refresh(c, cx, cy, s, col=GOLD):
    c.arc((cx - 50 * s, cy - 50 * s, cx + 50 * s, cy + 50 * s), 30, 330, col, 12 * s)
    ex, ey = cx + 50 * s * math.cos(math.radians(330)), cy + 50 * s * math.sin(math.radians(330))
    c.poly([(ex - 18 * s, ey - 2 * s), (ex + 20 * s, ey - 12 * s), (ex + 8 * s, ey + 24 * s)], fill=col)

def ic_tag10(c, cx, cy, s, text="10% OFF"):
    c.poly([(cx - 150 * s, cy - 80 * s), (cx + 90 * s, cy - 80 * s), (cx + 160 * s, cy), (cx + 90 * s, cy + 80 * s), (cx - 150 * s, cy + 80 * s)], fill=GOLD)
    c.ell((cx + 70 * s, cy - 14 * s, cx + 98 * s, cy + 14 * s), fill=CARD_BG)
    ftext(c, (cx - 40 * s, cy + 4 * s), text, 58 * s, GREEN_D, 190 * s, track=0)

def ic_bed(c, cx, cy, s):
    c.rrect((cx - 80 * s, cy - 10 * s, cx + 80 * s, cy + 30 * s), 8 * s, fill=(118, 150, 206))
    c.rrect((cx - 84 * s, cy - 50 * s, cx - 70 * s, cy + 56 * s), 4, fill=(160, 112, 60))
    c.rrect((cx + 70 * s, cy - 20 * s, cx + 84 * s, cy + 56 * s), 4, fill=(160, 112, 60))
    c.rrect((cx - 66 * s, cy - 34 * s, cx - 20 * s, cy - 8 * s), 10 * s, fill=IVORY)
    c.rrect((cx - 20 * s, cy - 24 * s, cx + 70 * s, cy - 6 * s), 6 * s, fill=(190, 222, 232))

def ic_rail(c, cx, cy, s):
    ic_train6(c, cx, cy, s)

def ic_train6(c, cx, cy, s, col=GREEN_OK):
    c.rrect((cx - 70 * s, cy - 50 * s, cx + 70 * s, cy + 34 * s), 22 * s, fill=col, outline=GREEN_D, width=4)
    c.rrect((cx - 54 * s, cy - 36 * s, cx + 54 * s, cy - 4 * s), 8 * s, fill=(190, 222, 232))
    c.ell((cx - 50 * s, cy + 6 * s, cx - 32 * s, cy + 24 * s), fill=GOLD); c.ell((cx + 32 * s, cy + 6 * s, cx + 50 * s, cy + 24 * s), fill=GOLD)
    c.line([(cx - 44 * s, cy + 60 * s), (cx - 20 * s, cy + 34 * s)], SAGE, 6 * s); c.line([(cx + 44 * s, cy + 60 * s), (cx + 20 * s, cy + 34 * s)], SAGE, 6 * s)

def ic_id6(c, cx, cy, s):
    c.rrect((cx - 80 * s, cy - 52 * s, cx + 80 * s, cy + 52 * s), 10 * s, fill=IVORY, outline=(206, 200, 186), width=3)
    c.ell((cx - 62 * s, cy - 28 * s, cx - 14 * s, cy + 20 * s), fill=SKIN)
    c.d.pieslice(c._b((cx - 66 * s, cy + 6 * s, cx - 10 * s, cy + 60 * s)), 180, 360, fill=SAGE_D)
    for k in range(3):
        c.rrect((cx + 4 * s, cy - 24 * s + k * 22 * s, cx + 62 * s - k * 8 * s, cy - 12 * s + k * 22 * s), 3, fill=(206, 212, 206))
    c.text((cx + 40 * s, cy + 34 * s), "AGE", FONT_SANS, 18 * s, GREEN_D)

def ic_pocket(c, cx, cy, s):
    c.poly([(cx - 70 * s, cy - 60 * s), (cx + 70 * s, cy - 60 * s), (cx + 60 * s, cy + 50 * s), (cx, cy + 74 * s), (cx - 60 * s, cy + 50 * s)], fill=(70, 110, 160))
    c.line([(cx - 70 * s, cy - 30 * s), (cx + 70 * s, cy - 30 * s)], (40, 76, 120), 5 * s)
    c.rrect((cx - 46 * s, cy - 92 * s, cx + 46 * s, cy - 30 * s), 6 * s, fill=IVORY, outline=(206, 200, 186), width=3)
    c.ell((cx - 36 * s, cy - 84 * s, cx - 10 * s, cy - 58 * s), fill=SKIN)

def ic_leaf(c, cx, cy, s, col=RED):
    pts = [(0, -70), (14, -40), (34, -50), (28, -14), (60, -26), (50, 0), (66, 6), (30, 30), (36, 48), (6, 40), (6, 74), (-6, 74),
           (-6, 40), (-36, 48), (-30, 30), (-66, 6), (-50, 0), (-60, -26), (-28, -14), (-34, -50), (-14, -40)]
    c.poly([(cx + x * s, cy + y * s) for x, y in pts], fill=col)

def ic_scale(c, cx, cy, s, tilt):
    c.rrect((cx - 8 * s, cy - 90 * s, cx + 8 * s, cy + 80 * s), 4, fill=GOLD)
    c.rrect((cx - 70 * s, cy + 74 * s, cx + 70 * s, cy + 92 * s), 6, fill=GOLD)
    dy = 30 * s * tilt
    c.line([(cx - 170 * s, cy - 80 * s - dy), (cx + 170 * s, cy - 80 * s + dy)], GOLD, 12 * s)
    c.ell((cx - 18 * s, cy - 98 * s, cx + 18 * s, cy - 62 * s), fill=GOLD)
    for sx, yy in ((-170, -80 * s - dy), (170, -80 * s + dy)):
        x = cx + sx * s
        c.line([(x, cy + yy), (x - 60 * s, cy + yy + 90 * s)], SAGE, 4 * s); c.line([(x, cy + yy), (x + 60 * s, cy + yy + 90 * s)], SAGE, 4 * s)
        c.d.chord(c._b((x - 80 * s, cy + yy + 60 * s, x + 80 * s, cy + yy + 120 * s)), 0, 180, fill=GOLD)

def ic_clock24(c, cx, cy, r, sweep):
    c.ell((cx - r, cy - r, cx + r, cy + r), fill=IVORY, outline=GOLD, width=r * 0.08)
    if sweep > 0:
        c.d.pieslice(c._b((cx - r * 0.86, cy - r * 0.86, cx + r * 0.86, cy + r * 0.86)), -90, -90 + 360 * sweep, fill=(190, 230, 200))
    for k in range(24):
        a = math.pi * k / 12
        L = 0.12 if k % 6 == 0 else 0.06
        c.line([(cx + math.sin(a) * r * (0.88 - L), cy - math.cos(a) * r * (0.88 - L)), (cx + math.sin(a) * r * 0.88, cy - math.cos(a) * r * 0.88)], GREEN_D, r * 0.03)
    c.text((cx, cy - r * 0.08), "24", FONT_SANS, r * 0.62, GREEN_D)
    c.text((cx, cy + r * 0.36), "HOURS", FONT_SANS, r * 0.16, GREEN_D, track=2)

def ic_card6(c, cx, cy, s):
    c.rrect((cx - 80 * s, cy - 50 * s, cx + 80 * s, cy + 50 * s), 12 * s, fill=(70, 110, 160))
    c.rrect((cx - 80 * s, cy - 30 * s, cx + 80 * s, cy - 12 * s), 2, fill=(30, 50, 80))
    c.rrect((cx - 60 * s, cy + 10 * s, cx - 20 * s, cy + 34 * s), 5 * s, fill=GOLD)

def ic_runner(c, cx, cy, s):
    c.ell((cx - 4 * s, cy - 76 * s, cx + 32 * s, cy - 40 * s), fill=SKIN)
    c.line([(cx + 8 * s, cy - 36 * s), (cx - 6 * s, cy + 14 * s)], GOLD, 20 * s)
    c.line([(cx - 6 * s, cy + 14 * s), (cx + 28 * s, cy + 40 * s), (cx + 18 * s, cy + 72 * s)], GREEN_D, 12 * s)
    c.line([(cx - 6 * s, cy + 14 * s), (cx - 34 * s, cy + 44 * s), (cx - 56 * s, cy + 40 * s)], GREEN_D, 12 * s)
    c.line([(cx + 6 * s, cy - 20 * s), (cx + 40 * s, cy - 2 * s)], GOLD, 10 * s)
    c.line([(cx + 6 * s, cy - 20 * s), (cx - 26 * s, cy - 6 * s)], GOLD, 10 * s)
    for k in range(3):
        c.line([(cx - 90 * s, cy - 40 * s + k * 26 * s), (cx - 52 * s, cy - 40 * s + k * 26 * s)], SAGE, 6 * s)

def ic_kid(c, cx, cy, s):
    ic_person(c, cx - 30 * s, cy - 6 * s, 1.0 * s, col=GOLD)
    ic_person(c, cx + 40 * s, cy + 20 * s, 0.62 * s, col=(110, 176, 124))
    c.ell((cx + 54 * s, cy - 54 * s, cx + 78 * s, cy - 30 * s), fill=RED)

def ic_cal_q(c, cx, cy, s):
    ic_cal(c, cx, cy, s, "?")

def ic_cal_check(c, cx, cy, s):
    ic_cal(c, cx, cy, s, "1")
    ic_check_c(c, cx + 50 * s, cy + 50 * s, 24 * s)

def ic_hourglass(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 70 * s, cx + 50 * s, cy - 58 * s), 4, fill=GOLD)
    c.rrect((cx - 50 * s, cy + 58 * s, cx + 50 * s, cy + 70 * s), 4, fill=GOLD)
    c.poly([(cx - 40 * s, cy - 58 * s), (cx + 40 * s, cy - 58 * s), (cx, cy), (cx + 40 * s, cy + 58 * s), (cx - 40 * s, cy + 58 * s), (cx, cy)], fill=(190, 222, 232))
    c.poly([(cx - 26 * s, cy + 58 * s), (cx + 26 * s, cy + 58 * s), (cx, cy + 26 * s)], fill=GOLD)

def ic_fares3(c, cx, cy, s):
    for k, (col, ang) in enumerate(((GREEN_OK, -12), (GOLD, 0), (CORAL, 12))):
        x = cx + (k - 1) * 70 * s
        c.rrect((x - 50 * s, cy - 66 * s + abs(k - 1) * 10 * s, x + 50 * s, cy + 66 * s), 10 * s, fill=col, outline=GREEN_D, width=3)
        c.rrect((x - 34 * s, cy - 40 * s, x + 34 * s, cy - 28 * s), 4, fill=IVORY)

def ic_bigtrain_leave(c, cx, cy, s):
    ic_train6(c, cx, cy, s)
    for k in range(3):
        c.line([(cx - 160 * s, cy - 30 * s + k * 30 * s), (cx - 90 * s, cy - 30 * s + k * 30 * s)], SAGE, 8 * s)

def ic_trap(c, cx, cy, s):
    c.d.chord(c._b((cx - 90 * s, cy - 70 * s, cx + 90 * s, cy + 70 * s)), 180, 360, outline=STEEL6, width=int(10 * s * 2))
    for k in range(7):
        x = cx - 72 * s + k * 24 * s
        c.poly([(x - 10 * s, cy), (x, cy - 34 * s), (x + 10 * s, cy)], fill=STEEL6)
    c.rrect((cx - 100 * s, cy, cx + 100 * s, cy + 16 * s), 4, fill=STEEL6)

STEEL6 = (200, 210, 206)

def ic_doctor(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 50 * s, cx + 50 * s, cy + 50 * s), 16 * s, fill=IVORY)
    c.rrect((cx - 12 * s, cy - 34 * s, cx + 12 * s, cy + 34 * s), 4, fill=RED)
    c.rrect((cx - 34 * s, cy - 12 * s, cx + 34 * s, cy + 12 * s), 4, fill=RED)

def ic_cloud(c, cx, cy, s):
    for (x, y, r) in ((-30, 4, 32), (10, -16, 40), (44, 8, 28)):
        c.ell((cx + (x - r) * s, cy + (y - r) * s, cx + (x + r) * s, cy + (y + r) * s), fill=(214, 224, 230))
    c.rrect((cx - 62 * s, cy + 4 * s, cx + 72 * s, cy + 36 * s), 14 * s, fill=(214, 224, 230))
    for k in range(3):
        c.line([(cx - 30 * s + k * 30 * s, cy + 48 * s), (cx - 38 * s + k * 30 * s, cy + 70 * s)], ICE, 6 * s)

def ic_heart(c, cx, cy, s):
    c.ell((cx - 52 * s, cy - 44 * s, cx + 2 * s, cy + 10 * s), fill=RED)
    c.ell((cx - 2 * s, cy - 44 * s, cx + 52 * s, cy + 10 * s), fill=RED)
    c.poly([(cx - 50 * s, cy - 6 * s), (cx + 50 * s, cy - 6 * s), (cx, cy + 54 * s)], fill=RED)
    c.line([(cx - 40 * s, cy - 10 * s), (cx - 14 * s, cy - 10 * s), (cx - 4 * s, cy - 30 * s), (cx + 8 * s, cy + 10 * s), (cx + 16 * s, cy - 10 * s), (cx + 40 * s, cy - 10 * s)], IVORY, 5 * s)

def ic_laptop(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy - 54 * s, cx + 70 * s, cy + 34 * s), 8 * s, fill=(60, 70, 66))
    c.rrect((cx - 60 * s, cy - 44 * s, cx + 60 * s, cy + 24 * s), 4 * s, fill=(190, 222, 232))
    c.poly([(cx - 90 * s, cy + 50 * s), (cx + 90 * s, cy + 50 * s), (cx + 74 * s, cy + 34 * s), (cx - 74 * s, cy + 34 * s)], fill=(140, 150, 146))

def ic_handset(c, cx, cy, s, col=GOLD):
    c.line([(cx - 40 * s, cy - 50 * s), (cx - 52 * s, cy - 10 * s), (cx - 20 * s, cy + 40 * s), (cx + 30 * s, cy + 60 * s)], col, 28 * s)
    c.ell((cx - 64 * s, cy - 70 * s, cx - 22 * s, cy - 34 * s), fill=col)
    c.ell((cx + 16 * s, cy + 40 * s, cx + 58 * s, cy + 76 * s), fill=col)

def ic_phone_app(c, cx, cy, s):
    ic_phone(c, cx, cy, s * 1.1)
    c.rrect((cx - 22 * s, cy - 40 * s, cx + 22 * s, cy - 10 * s), 6 * s, fill=GOLD)
    c.rrect((cx - 22 * s, cy, cx + 22 * s, cy + 30 * s), 6 * s, fill=GREEN_OK)

def ic_house_x(c, cx, cy, s):
    ic_house(c, cx, cy, s)
    ic_x_c(c, cx + 60 * s, cy - 50 * s, 30 * s)

def ic_smallbag(c, cx, cy, s):
    c.rrect((cx - 36 * s, cy - 20 * s, cx + 36 * s, cy + 40 * s), 12 * s, fill=(110, 176, 124), outline=GREEN_D, width=3)
    c.arc((cx - 22 * s, cy - 44 * s, cx + 22 * s, cy), 180, 360, GREEN_D, 7 * s)

def ic_suit(c, cx, cy, s, col=(214, 164, 96)):
    c.rrect((cx - 22 * s, cy - 66 * s, cx + 22 * s, cy - 46 * s), 6 * s, outline=(160, 112, 60), width=6 * s)
    c.rrect((cx - 46 * s, cy - 50 * s, cx + 46 * s, cy + 56 * s), 12 * s, fill=col, outline=(160, 112, 60), width=4)
    c.rrect((cx - 26 * s, cy - 50 * s, cx - 16 * s, cy + 56 * s), 2, fill=(160, 112, 60))
    c.rrect((cx + 16 * s, cy - 50 * s, cx + 26 * s, cy + 56 * s), 2, fill=(160, 112, 60))
    c.ell((cx - 34 * s, cy + 52 * s, cx - 18 * s, cy + 68 * s), fill=GREEN_D); c.ell((cx + 18 * s, cy + 52 * s, cx + 34 * s, cy + 68 * s), fill=GREEN_D)

def ic_bagtag(c, cx, cy, s, text, col):
    c.poly([(cx - 70 * s, cy - 40 * s), (cx + 40 * s, cy - 40 * s), (cx + 70 * s, cy), (cx + 40 * s, cy + 40 * s), (cx - 70 * s, cy + 40 * s)], fill=col)
    c.ell((cx + 34 * s, cy - 8 * s, cx + 50 * s, cy + 8 * s), fill=CARD_BG)
    c.text((cx - 14 * s, cy + 2 * s), text, FONT_SANS, 32 * s, GREEN_D if col != RED else IVORY)

def ic_redcap(c, cx, cy, s):
    c.ell((cx - 26 * s, cy - 92 * s, cx + 26 * s, cy - 40 * s), fill=SKIN)
    c.d.chord(c._b((cx - 30 * s, cy - 104 * s, cx + 30 * s, cy - 56 * s)), 180, 360, fill=RED)
    c.rrect((cx - 6 * s, cy - 84 * s, cx + 44 * s, cy - 74 * s), 4, fill=RED_D)
    c.rrect((cx - 44 * s, cy - 36 * s, cx + 44 * s, cy + 60 * s), 26 * s, fill=RED)
    c.rrect((cx - 36 * s, cy + 56 * s, cx - 8 * s, cy + 110 * s), 8 * s, fill=GREEN_D)
    c.rrect((cx + 8 * s, cy + 56 * s, cx + 36 * s, cy + 110 * s), 8 * s, fill=GREEN_D)

def ic_cart(c, cx, cy, s):
    c.line([(cx - 60 * s, cy - 70 * s), (cx - 50 * s, cy + 40 * s), (cx + 70 * s, cy + 40 * s)], STEEL6, 8 * s)
    c.ell((cx - 54 * s, cy + 36 * s, cx - 26 * s, cy + 64 * s), fill=GREEN_D, outline=STEEL6, width=3)
    c.ell((cx + 40 * s, cy + 36 * s, cx + 68 * s, cy + 64 * s), fill=GREEN_D, outline=STEEL6, width=3)
    c.rrect((cx - 38 * s, cy - 40 * s, cx + 30 * s, cy + 34 * s), 8 * s, fill=(214, 164, 96), outline=(160, 112, 60), width=3)
    c.rrect((cx - 20 * s, cy - 80 * s, cx + 56 * s, cy - 40 * s), 8 * s, fill=(110, 176, 124), outline=GREEN_D, width=3)

def ic_claim(c, cx, cy, s):
    c.rrect((cx - 60 * s, cy - 80 * s, cx + 60 * s, cy + 80 * s), 10 * s, fill=IVORY, outline=GOLD, width=4)
    c.ell((cx - 10 * s, cy - 70 * s, cx + 10 * s, cy - 50 * s), fill=CARD_BG)
    c.text((cx, cy - 20 * s), "CLAIM", FONT_SANS, 26 * s, GREEN_D, track=1)
    c.text((cx, cy + 20 * s), "CHECK", FONT_SANS, 26 * s, GREEN_D, track=1)
    for k in range(5):
        c.rrect((cx - 40 * s + k * 18 * s, cy + 44 * s, cx - 32 * s + k * 18 * s, cy + 66 * s), 1, fill=GREEN_D)

def ic_tipjar(c, cx, cy, s):
    c.rrect((cx - 50 * s, cy - 50 * s, cx + 50 * s, cy + 70 * s), 20 * s, fill=(190, 222, 232), outline=IVORY, width=4)
    c.rrect((cx - 56 * s, cy - 66 * s, cx + 56 * s, cy - 48 * s), 6 * s, fill=GOLD)
    c.text((cx, cy - 16 * s), "TIPS", FONT_SANS, 26 * s, GREEN_D, track=2)
    ic_coin(c, cx - 18 * s, cy + 40 * s, 18 * s); ic_coin(c, cx + 18 * s, cy + 46 * s, 18 * s)

def ic_stairs(c, cx, cy, s):
    pts = [(-80, 60), (-80, 30), (-40, 30), (-40, 0), (0, 0), (0, -30), (40, -30), (40, -60), (80, -60), (80, 60)]
    c.poly([(cx + x * s, cy + y * s) for x, y in pts], fill=(170, 180, 176))

def ic_staff(c, cx, cy, s):
    ic_person(c, cx, cy, 1.3 * s, col=(70, 110, 160))
    c.rrect((cx - 16 * s, cy + 10 * s, cx + 16 * s, cy + 32 * s), 4, fill=GOLD)

def ic_ramp(c, cx, cy, s):
    c.poly([(cx - 90 * s, cy + 50 * s), (cx + 90 * s, cy + 50 * s), (cx + 90 * s, cy - 30 * s)], fill=GOLD)
    c.rrect((cx + 60 * s, cy - 70 * s, cx + 100 * s, cy + 50 * s), 6 * s, fill=IVORY)

def ic_lift(c, cx, cy, s):
    c.rrect((cx - 70 * s, cy + 30 * s, cx + 70 * s, cy + 46 * s), 4, fill=GOLD)
    c.line([(cx - 60 * s, cy + 30 * s), (cx - 60 * s, cy - 70 * s)], STEEL6, 10 * s)
    c.line([(cx + 60 * s, cy + 30 * s), (cx + 60 * s, cy - 70 * s)], STEEL6, 10 * s)
    c.poly([(cx, cy - 80 * s), (cx - 24 * s, cy - 50 * s), (cx + 24 * s, cy - 50 * s)], fill=IVORY)
    c.poly([(cx, cy + 10 * s), (cx - 24 * s, cy - 20 * s), (cx + 24 * s, cy - 20 * s)], fill=IVORY)

def ic_seat6(c, cx, cy, s, col=SEAT):
    c.rrect((cx - 40 * s, cy - 70 * s, cx + 40 * s, cy + 30 * s), 22 * s, fill=col, outline=(60, 84, 120), width=3)
    c.rrect((cx - 52 * s, cy + 20 * s, cx + 52 * s, cy + 50 * s), 12 * s, fill=col)
    c.rrect((cx - 30 * s, cy + 50 * s, cx - 20 * s, cy + 74 * s), 3, fill=(60, 84, 120))
    c.rrect((cx + 20 * s, cy + 50 * s, cx + 30 * s, cy + 74 * s), 3, fill=(60, 84, 120))

def ic_acc_seat(c, cx, cy, s):
    ic_seat6(c, cx, cy, s, GOLD)
    c.ell((cx - 22 * s, cy - 50 * s, cx + 22 * s, cy - 6 * s), fill=GREEN_D)
    c.ell((cx - 6 * s, cy - 44 * s, cx + 6 * s, cy - 32 * s), fill=IVORY)
    c.line([(cx, cy - 30 * s), (cx, cy - 16 * s), (cx + 10 * s, cy - 16 * s)], IVORY, 4 * s)

def ic_tank(c, cx, cy, s):
    c.rrect((cx - 34 * s, cy - 50 * s, cx + 34 * s, cy + 80 * s), 28 * s, fill=(110, 176, 124), outline=GREEN_D, width=3)
    c.rrect((cx - 14 * s, cy - 72 * s, cx + 14 * s, cy - 48 * s), 4, fill=STEEL6)
    c.text((cx, cy + 18 * s), "O2", FONT_SANS, 34 * s, GREEN_D)

def ic_battery(c, cx, cy, s, level=1.0):
    c.rrect((cx - 80 * s, cy - 40 * s, cx + 70 * s, cy + 40 * s), 12 * s, outline=IVORY, width=7 * s)
    c.rrect((cx + 72 * s, cy - 16 * s, cx + 86 * s, cy + 16 * s), 4, fill=IVORY)
    w = 136 * s * level
    if w > 2:
        c.rrect((cx - 70 * s, cy - 30 * s, cx - 70 * s + w, cy + 30 * s), 6 * s, fill=GREEN_OK)
    c.text((cx - 4 * s, cy + 2 * s), "4 HRS", FONT_SANS, 34 * s, GREEN_D)

def ic_cooler(c, cx, cy, s):
    c.rrect((cx - 80 * s, cy - 40 * s, cx + 80 * s, cy + 56 * s), 14 * s, fill=(70, 120, 176), outline=(36, 76, 128), width=4)
    c.rrect((cx - 86 * s, cy - 56 * s, cx + 86 * s, cy - 30 * s), 10 * s, fill=IVORY)
    c.rrect((cx - 30 * s, cy - 76 * s, cx + 30 * s, cy - 56 * s), 6 * s, outline=IVORY, width=7 * s)

def ic_ice(c, cx, cy, s):
    for (x, y) in ((-26, 10), (22, 0), (0, -34)):
        c.rrect((cx + (x - 22) * s, cy + (y - 22) * s, cx + (x + 22) * s, cy + (y + 22) * s), 8 * s, fill=(210, 236, 248), outline=(150, 205, 232), width=3)

def ic_pillbottle(c, cx, cy, s):
    c.rrect((cx - 34 * s, cy - 40 * s, cx + 34 * s, cy + 60 * s), 10 * s, fill=(236, 150, 64))
    c.rrect((cx - 40 * s, cy - 62 * s, cx + 40 * s, cy - 38 * s), 6 * s, fill=IVORY)
    c.rrect((cx - 26 * s, cy - 10 * s, cx + 26 * s, cy + 30 * s), 4, fill=IVORY)

def ic_sandwich(c, cx, cy, s):
    c.poly([(cx - 70 * s, cy + 40 * s), (cx + 70 * s, cy + 40 * s), (cx, cy - 60 * s)], fill=(236, 200, 140))
    c.line([(cx - 60 * s, cy + 22 * s), (cx + 60 * s, cy + 22 * s)], (110, 176, 124), 10 * s)
    c.line([(cx - 48 * s, cy + 6 * s), (cx + 48 * s, cy + 6 * s)], RED, 8 * s)

def ic_apple(c, cx, cy, s):
    c.ell((cx - 50 * s, cy - 40 * s, cx + 4 * s, cy + 50 * s), fill=RED)
    c.ell((cx - 4 * s, cy - 40 * s, cx + 50 * s, cy + 50 * s), fill=RED)
    c.line([(cx, cy - 40 * s), (cx + 8 * s, cy - 66 * s)], (120, 80, 50), 6 * s)
    c.ell((cx + 8 * s, cy - 70 * s, cx + 40 * s, cy - 50 * s), fill=GREEN_OK)

def ic_crackers(c, cx, cy, s):
    for k in range(3):
        c.rrect((cx - 54 * s + k * 10 * s, cy - 44 * s + k * 18 * s, cx + 30 * s + k * 10 * s, cy + 6 * s + k * 18 * s), 8 * s, fill=(226, 180, 110), outline=(176, 130, 70), width=3)

def ic_drink(c, cx, cy, s):
    c.poly([(cx - 34 * s, cy - 50 * s), (cx + 34 * s, cy - 50 * s), (cx + 24 * s, cy + 60 * s), (cx - 24 * s, cy + 60 * s)], fill=(190, 222, 232))
    c.line([(cx + 10 * s, cy - 50 * s), (cx + 26 * s, cy - 84 * s)], RED, 6 * s)

def ic_lunchbag(c, cx, cy, s):
    c.poly([(cx - 60 * s, cy - 40 * s), (cx + 60 * s, cy - 40 * s), (cx + 50 * s, cy + 70 * s), (cx - 50 * s, cy + 70 * s)], fill=(214, 164, 96))
    c.poly([(cx - 60 * s, cy - 40 * s), (cx + 60 * s, cy - 40 * s), (cx + 48 * s, cy - 64 * s), (cx - 48 * s, cy - 64 * s)], fill=(190, 140, 80))

def ic_board_delay(c, cx, cy, s):
    c.rrect((cx - 110 * s, cy - 50 * s, cx + 110 * s, cy + 50 * s), 10 * s, fill=BOARD, outline=STEEL6, width=4)
    c.text((cx, cy + 2 * s), "DELAYED", FONT_SANS, 40 * s, AMBER, track=3)

def ic_shelf(c, cx, cy, s):
    for k in range(3):
        c.rrect((cx - 90 * s, cy - 50 * s + k * 50 * s, cx + 90 * s, cy - 42 * s + k * 50 * s), 2, fill=STEEL6)
    c.rrect((cx - 70 * s, cy - 88 * s, cx - 40 * s, cy - 50 * s), 4, fill=RED)

def ic_wine(c, cx, cy, s):
    c.d.chord(c._b((cx - 40 * s, cy - 80 * s, cx + 40 * s, cy + 10 * s)), 0, 180, fill=(150, 40, 60))
    c.arc((cx - 40 * s, cy - 120 * s, cx + 40 * s, cy + 10 * s), 0, 180, IVORY, 5 * s)
    c.line([(cx, cy + 10 * s), (cx, cy + 66 * s)], IVORY, 6 * s)
    c.line([(cx - 30 * s, cy + 66 * s), (cx + 30 * s, cy + 66 * s)], IVORY, 6 * s)

def ic_tray(c, cx, cy, s):
    c.rrect((cx - 90 * s, cy + 20 * s, cx + 90 * s, cy + 36 * s), 6 * s, fill=STEEL6)
    c.d.chord(c._b((cx - 60 * s, cy - 50 * s, cx + 60 * s, cy + 70 * s)), 180, 360, fill=IVORY)
    c.ell((cx - 10 * s, cy - 62 * s, cx + 10 * s, cy - 42 * s), fill=IVORY)

def ic_micro(c, cx, cy, s):
    c.rrect((cx - 90 * s, cy - 56 * s, cx + 90 * s, cy + 56 * s), 12 * s, fill=STEEL6)
    c.rrect((cx - 74 * s, cy - 40 * s, cx + 30 * s, cy + 40 * s), 8 * s, fill=(60, 70, 66))
    for k in range(3):
        c.ell((cx + 48 * s, cy - 34 * s + k * 26 * s, cx + 66 * s, cy - 16 * s + k * 26 * s), fill=(60, 70, 66))

def ic_flu(c, cx, cy, s):
    c.ell((cx - 50 * s, cy - 50 * s, cx + 50 * s, cy + 50 * s), fill=SKIN)
    c.ell((cx - 26 * s, cy - 14 * s, cx - 12 * s, cy), fill=GREEN_D); c.ell((cx + 12 * s, cy - 14 * s, cx + 26 * s, cy), fill=GREEN_D)
    c.arc((cx - 20 * s, cy + 14 * s, cx + 20 * s, cy + 40 * s), 200, 340, RED_D, 5 * s)
    c.line([(cx + 40 * s, cy - 40 * s), (cx + 80 * s, cy - 80 * s)], IVORY, 10 * s)
    c.ell((cx + 70 * s, cy - 96 * s, cx + 92 * s, cy - 74 * s), fill=RED)

def ic_fall(c, cx, cy, s):
    ic_cane_fall = [(cx - 70 * s, cy + 50 * s), (cx + 70 * s, cy + 20 * s)]
    c.line(ic_cane_fall, (214, 164, 96), 12 * s)
    c.arc((cx + 50 * s, cy - 10 * s, cx + 100 * s, cy + 40 * s), 180, 360, (214, 164, 96), 12 * s)
    for k in range(3):
        c.line([(cx - 20 * s + k * 30 * s, cy - 50 * s), (cx - 10 * s + k * 30 * s, cy - 20 * s)], GOLD, 6 * s)

def ic_two(c, cx, cy, s):
    ic_person(c, cx - 40 * s, cy, 1.2 * s, col=GOLD)
    ic_person(c, cx + 40 * s, cy, 1.2 * s, col=(118, 150, 206))

def ic_share(c, cx, cy, s):
    c.line([(cx - 50 * s, cy + 50 * s), (cx - 50 * s, cy), (cx + 40 * s, cy)], GOLD, 16 * s)
    c.poly([(cx + 30 * s, cy - 40 * s), (cx + 80 * s, cy), (cx + 30 * s, cy + 40 * s)], fill=GOLD)

def ic_comment(c, cx, cy, s):
    c.rrect((cx - 80 * s, cy - 56 * s, cx + 80 * s, cy + 40 * s), 24 * s, fill=IVORY)
    c.poly([(cx - 40 * s, cy + 36 * s), (cx - 54 * s, cy + 76 * s), (cx - 6 * s, cy + 36 * s)], fill=IVORY)
    c.text((cx, cy - 6 * s), "?", FONT_SANS, 80 * s, GREEN_D)

def ic_thumb(c, cx, cy, s, col=GOLD):
    c.rrect((cx - 70 * s, cy - 10 * s, cx - 36 * s, cy + 70 * s), 8 * s, fill=col)
    c.rrect((cx - 30 * s, cy - 20 * s, cx + 60 * s, cy + 70 * s), 22 * s, fill=col)
    c.poly([(cx - 30 * s, cy - 10 * s), (cx - 6 * s, cy - 80 * s), (cx + 22 * s, cy - 76 * s), (cx + 10 * s, cy - 14 * s)], fill=col)

def ic_bell6(c, cx, cy, s, col=GOLD):
    c.d.chord(c._b((cx - 60 * s, cy - 70 * s, cx + 60 * s, cy + 70 * s)), 180, 360, fill=col)
    c.rrect((cx - 60 * s, cy - 2 * s, cx + 60 * s, cy + 40 * s), 4, fill=col)
    c.rrect((cx - 76 * s, cy + 36 * s, cx + 76 * s, cy + 52 * s), 6 * s, fill=col)
    c.ell((cx - 14 * s, cy + 52 * s, cx + 14 * s, cy + 78 * s), fill=col)

def ic_ok_board(c, cx, cy, s):
    c.rrect((cx - 90 * s, cy - 60 * s, cx + 90 * s, cy + 60 * s), 12 * s, fill=IVORY, outline=GOLD, width=4)
    for k in range(3):
        c.rrect((cx - 64 * s, cy - 34 * s + k * 30 * s, cx - 44 * s, cy - 14 * s + k * 30 * s), 4, outline=GREEN_D, width=3)
        c.rrect((cx - 30 * s, cy - 30 * s + k * 30 * s, cx + 64 * s, cy - 18 * s + k * 30 * s), 4, fill=(206, 212, 206))

# ------------------------------------------------------------------ linea del treno con le 10 fermate (punti 1-10)
def route_spr(n):
    def fn(c):
        w, h = 1500, 90
        c.rrect((20, 40, w - 20, 50), 4, fill=SAGE_D)
        for i in range(10):
            x = 60 + i * 153
            on = i + 1 <= n
            cur = i + 1 == n
            r = 32 if cur else 24
            c.ell((x - r, 45 - r, x + r, 45 + r), fill=GOLD if on else CARD_BG, outline=GOLD if on else SAGE, width=4)
            c.text((x, 47), str(i + 1), FONT_SANS, 28 if cur else 22, GREEN_D if on else SAGE)
    return sprite(("route6", n), 1500, 90, fn)

def num_ticket(n):
    def fn(c):
        w, h = 250, 150
        c.rrect((4, 4, w - 4, h - 4), 22, fill=GOLD, outline=(168, 118, 40), width=5)
        c.ell((-26, h / 2 - 24, 22, h / 2 + 24), fill=(0, 0, 0, 0))
        c.d.ellipse(c._b((-24, h / 2 - 24, 24, h / 2 + 24)), fill=(0, 0, 0, 0))
        c.d.ellipse(c._b((w - 24, h / 2 - 24, w + 24, h / 2 + 24)), fill=(0, 0, 0, 0))
        c.text((w / 2, 40), "NUMBER", FONT_SANS, 26, GREEN_D, track=4)
        c.text((w / 2, 98), str(n), FONT_SANS, 76, GREEN_D)
    return sprite(("numt6", n), 250, 150, fn)

def hero(img, t, ts, n, title, it=1):
    """intestazione dei punti: biglietto col numero + titolo + linea con le 10 fermate"""
    seq(img, t, ts[0], num_ticket(n), 205, 215, shadow=10, rot=-4)
    p = ease(seg(t, ts[it], 0.5))
    if p > 0:
        put(img, T(title, 76, IVORY, maxw=1460), 360 + T(title, 76, IVORY, maxw=1460).width / 2 + 20 * (1 - p) * 0, 215, alpha=p)
    p2 = ease(seg(t, ts[0] + 0.2, 0.6))
    if p2 > 0:
        put(img, route_spr(n), 960, 985, alpha=p2)
        x = 960 - 750 + 60 + (n - 1) * 153
        put(img, sprite("mini_train6", 120, 80, lambda c: ic_train6(c, 60, 40, 0.55)), x, 925 - 14 * (1 - p2), alpha=p2)

# ------------------------------------------------------------------ tabellone partenze
def board_spr(key, rows, w=1100, rh=96, head="DEPARTURES"):
    def fn(c):
        h = 90 + rh * len(rows) + 20
        c.rrect((4, 4, w - 4, h - 4), 26, fill=BOARD, outline=STEEL6, width=6)
        c.text((40, 50), head, FONT_SANS, 34, IVORY, anchor="lm", track=6)
        for i, (a, b, col) in enumerate(rows):
            y = 90 + i * rh
            c.rrect((24, y, w - 24, y + rh - 14), 10, fill=(20, 44, 38))
            ftext(c, (50, y + (rh - 14) / 2 + 2), a, 38, AMBER, w * 0.5, anchor="lm", track=2)
            ftext(c, (w - 50, y + (rh - 14) / 2 + 2), b, 38, col, w * 0.45, anchor="rm", track=2)
    return sprite(("board6", key), w, 90 + rh * len(rows) + 20, fn)

def board_row(key, a, b, col, w=1100, rh=82):
    def fn(c):
        c.rrect((4, 4, w - 4, rh - 4), 12, fill=(20, 44, 38), outline=(40, 70, 60), width=3)
        ftext(c, (34, rh / 2 + 2), a, 38, AMBER, w * 0.5, anchor="lm", track=2)
        ftext(c, (w - 34, rh / 2 + 2), b, 38, col, w * 0.45, anchor="rm", track=2)
    return sprite(("brow6", key), w, rh, fn)

def board_frame(w, h, head):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 4), 26, fill=BOARD, outline=STEEL6, width=6)
        c.text((40, 48), head, FONT_SANS, 34, IVORY, anchor="lm", track=6)
        for k in range(3):
            c.ell((w - 60 - k * 30, 38, w - 44 - k * 30, 54), fill=AMBER if k == 0 else (60, 80, 70))
    return sprite(("bframe6", w, h, head), w, h, fn)

def flip(img, t, t0, spr, cx, cy):
    """riga del tabellone che si gira dall'alto"""
    p = ease(seg(t, t0, 0.45))
    if p > 0:
        h = max(1, int(spr.height * p))
        s = spr.resize((spr.width, h))
        put(img, s, cx, cy, alpha=min(1, p * 2))

# ============================================================ BLOCCO 6 - fonti, tabellone
def draw6(img, t):
    ts = starts(6)
    common(img, t, "WHERE THIS COMES FROM")
    seq(img, t, ts[0], sprite("brw6", 640, 440, lambda c: ic_browser6(c, 320, 220, 2.0)), 420, 520, shadow=14)
    seq(img, t, ts[0] + 0.6, pill("AMTRAK'S OWN PAGES", 40, 560), 420, 810, shadow=8)
    seq(img, t, ts[1] - 0.3, board_frame(1130, 560, "CHECKLIST"), 1290, 520, shadow=14)
    rows = [("RUMORS", "NONE", GREEN_OK, 1), ("PAID BY AMTRAK", "NO", GREEN_OK, 2), ("RULES", "CHANGE", AMBER, 3),
            ("CHECK", "BEFORE YOU BOOK", IVORY, 4)]
    for i, (a, b, col, k) in enumerate(rows):
        tt = last_t(6, ts[k]) if k == 4 else ts[k]
        flip(img, t, tt, board_row(("r6", i), a, b, col, w=1060), 1290, 360 + i * 112)

# ============================================================ BLOCCO 7 - punto 1 sconto senior
def draw7(img, t):
    ts = starts(7)
    common(img, t, "NUMBER ONE")
    hero(img, t, ts, 1, "THE SENIOR DISCOUNT")
    seq(img, t, ts[2], chip65(), 360, 560, scale=1.8, shadow=10)
    seq(img, t, ts[2] + 0.3, T("IF YOU'RE 65 OR OLDER", 44, SAGE), 360, 720)
    s_, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, sprite("tag10_6", 640, 340, lambda c: ic_tag10(c, 320, 170, 1.7)), 1000, 560, scale=s_, alpha=a, shadow=14, rot=-4)
        burst(img, t, ts[3], 1000, 560, n=12, color=GOLD, rad=260, seed=3)
    seq(img, t, ts[3] + 0.6, pill("MOST RAIL FARES", 38, 440), 1560, 500, shadow=8)
    seq(img, t, last_t(7, ts[4]), pill("MOST TRAINS", 38, 440), 1560, 620, shadow=8)

# ============================================================ BLOCCO 8 - telefono con TRAVELER TYPE
def phone_big():
    def fn(c):
        w, h = 520, 820
        c.rrect((4, 4, w - 4, h - 4), 60, fill=(30, 40, 36), outline=STEEL6, width=6)
        c.rrect((26, 70, w - 26, h - 70), 26, fill=IVORY)
        c.rrect((w / 2 - 50, 30, w / 2 + 50, 46), 8, fill=(60, 70, 66))
        c.rrect((26, 70, w - 26, 170), 26, fill=GREEN_L)
        c.d.rectangle(c._b((26, 130, w - 26, 170)), fill=GREEN_L)
        c.text((w / 2, 120), "BOOK A TICKET", FONT_SANS, 34, IVORY, track=3)
        c.text((60, 220), "TRAVELER TYPE", FONT_SANS_M, 28, GREEN_D, anchor="lm", track=2)
    return sprite("phone8", 520, 820, fn)

def opt_row(text, state):
    def fn(c):
        w, h = 420, 100
        col = {"sel_bad": RED, "sel_ok": GREEN_OK, "off": (206, 212, 206)}[state]
        c.rrect((4, 4, w - 4, h - 4), 20, fill=IVORY, outline=col, width=6)
        c.ell((30, 30, 70, 70), outline=GREEN_D, width=4)
        if state != "off":
            c.ell((40, 40, 60, 60), fill=GREEN_D)
        c.text((100, h / 2 + 2), text, FONT_SANS, 44, GREEN_D, anchor="lm", track=2)
    return sprite(("opt8", text, state), 420, 100, fn)

def draw8(img, t):
    ts = starts(8)
    common(img, t, "THE MISTAKE")
    seq(img, t, ts[0], pill("THE MISTAKE", 44, 480, 86, RED, IVORY, RED_D), 400, 220, shadow=8)
    seq(img, t, ts[1], T("THE DISCOUNT DOESN'T", 50, IVORY, 700), 400, 380)
    seq(img, t, ts[1] + 0.2, T("APPEAR BY ITSELF", 50, GOLD, 700), 400, 450)
    slide_in(img, t, ts[2], phone_big(), 1060, 560, dy=60, dur=0.5, shadow=16)
    adult_sel = t < ts[3] + 0.6 or t >= ts[4]
    if t >= ts[2] + 0.4:
        a = ease(seg(t, ts[2] + 0.4, 0.4))
        put(img, opt_row("ADULT", "sel_bad" if (t >= ts[4]) else ("off" if t >= ts[3] + 0.6 else "sel_bad")), 1060, 450, alpha=a)
        put(img, opt_row("SENIOR", "sel_ok" if (ts[3] + 0.6 <= t < ts[4]) else ("off" if t < ts[4] else "sel_ok")), 1060, 580, alpha=a)
    seq(img, t, ts[3], sprite("arr8", 160, 100, lambda c: c.poly([(6, 34), (96, 34), (96, 6), (154, 50), (96, 94), (96, 66), (6, 66)], fill=GOLD)), 1400, 580, rot=180, shadow=6)
    seq(img, t, ts[3] + 0.3, T("CHOOSE SENIOR", 50, GREEN_OK, 330), 1650, 580)
    tl = last_t(8, ts[5])
    s_, a, p = pop(t, tl, 0.5)
    if p > 0:
        put(img, stamp6("ADULT PRICE", 460, 110, RED), 1600, 780, scale=s_, alpha=a, rot=-6, shadow=10)
    seq(img, t, ts[4], T("LEAVE IT ON ADULT?", 44, IVORY, 600), 400, 640)

# ============================================================ BLOCCO 9 - 4 vagoni-scheda
def wagon(key, w, h, icon, lines, border=GREEN_OK):
    def fn(c):
        c.rrect((4, 4, w - 4, h - 44), 30, fill=CARD_BG, outline=border, width=6)
        c.rrect((4, h - 120, w - 4, h - 108), 2, fill=border)
        for x in (70, w - 70):
            c.ell((x - 26, h - 52, x + 26, h), fill=GREEN_D, outline=IVORY, width=4)
        icon(c, w / 2, 130)
        for (s_, sz, col, y) in lines:
            ftext(c, (w / 2, y), s_, sz, col, w - 50)
    return sprite(("wagon6", key), w, h, fn)

def draw9(img, t):
    ts = starts(9)
    common(img, t, "TWO MORE THINGS")
    seq(img, t, ts[0], pill("TWO MORE THINGS", 44, 560, 86, GOLD, GREEN_D, (168, 118, 40)), 960, 190, shadow=8)
    W9, H9 = 420, 560
    xs = [270, 730, 1190, 1650]
    slide_in(img, t, ts[1], wagon("w1", W9, H9, lambda c, x, y: (ic_bed(c, x, y, 1.1), ic_x_c(c, x + 90, y - 50, 26)),
                                   [("SLEEPING ROOM", 40, IVORY, 270), ("NO DISCOUNT", 40, RED, 326)]), xs[0], 590, dy=50, shadow=12)
    seq(img, t, ts[2], pill("RAIL FARE: YES", 34, 360, 70, GREEN_OK, GREEN_D, GREEN_D), xs[0], 760, shadow=6)
    slide_in(img, t, ts[3], wagon("w2", W9, H9, lambda c, x, y: ic_id6(c, x, y, 1.1),
                                   [("PROOF OF AGE", 40, IVORY, 270), ("WHEN YOU BUY", 34, GOLD, 330), ("+ ON THE TRAIN", 34, GOLD, 378)]), xs[1], 590, dy=50, shadow=12)
    slide_in(img, t, ts[5], wagon("w3", W9, H9, lambda c, x, y: ic_pocket(c, x, y + 20, 0.9),
                                   [("ID IN YOUR POCKET", 36, IVORY, 270), ("NOT IN YOUR", 34, RED, 330), ("SUITCASE", 34, RED, 378)]), xs[2], 590, dy=50, shadow=12)
    tl = last_t(9, ts[7])
    slide_in(img, t, ts[6], wagon("w4", W9, H9, lambda c, x, y: ic_leaf(c, x, y, 1.1),
                                   [("TO CANADA", 40, IVORY, 270), ("WITH VIA RAIL", 34, SAGE, 326)], border=GOLD), xs[3], 590, dy=50, shadow=12)
    seq(img, t, tl, pill("FROM AGE 60", 38, 360, 76, GOLD, GREEN_D, (168, 118, 40)), xs[3], 760, shadow=8)

# ============================================================ BLOCCO 10 - bilancia + azione
def draw10(img, t):
    ts = starts(10)
    common(img, t, "COMPARE")
    seq(img, t, ts[0], pill("MAY NOT COMBINE WITH OTHER OFFERS", 38, 900), 960, 190, shadow=8)
    tilt = ease(seg(t, ts[1], 0.8))
    if t >= ts[0] + 0.3:
        a = ease(seg(t, ts[0] + 0.3, 0.5))
        img2 = sprite(("scale6", round(tilt, 2)), 520, 330, lambda c: ic_scale(c, 260, 170, 1.15, tilt))
        put(img, img2, 960, 470, alpha=a, shadow=8)
        dy = 34 * tilt
        put(img, pill("SENIOR -10%", 34, 300, 66), 960 - 196, 470 + 120 - dy, alpha=a)
        put(img, pill("SALE FARE", 34, 300, 66, GOLD, GREEN_D, (168, 118, 40)), 960 + 196, 470 + 120 + dy, alpha=a)
    seq(img, t, ts[1] + 0.8, T("SOMETIMES CHEAPER", 40, GOLD), 1520, 560)
    seq(img, t, ts[2], T("YOUR ACTION", 40, SAGE), 960, 760)
    steps = [("CHOOSE SENIOR", ts[3]), ("COMPARE", last_t(10, ts[4])), ("THEN PAY", last_t(10, ts[4]) + 0.4)]
    for i, (s_, tt) in enumerate(steps):
        seq(img, t, tt, pill(s_, 40, 440, 84, GREEN_OK if i == 0 else IVORY, GREEN_D, GREEN_D if i == 0 else GOLD), 470 + i * 490, 870, shadow=8)
        if i:
            seq(img, t, tt, sprite("arr10", 70, 50, lambda c: c.poly([(4, 16), (40, 16), (40, 4), (66, 25), (40, 46), (40, 34), (4, 34)], fill=GOLD)), 470 + i * 490 - 245, 870)

# ============================================================ BLOCCO 11 - punto 2, 24 ore
def draw11(img, t):
    ts = starts(11)
    common(img, t, "NUMBER TWO")
    hero(img, t, ts, 2, "24 HOURS TO CHANGE YOUR MIND")
    sw = ease(seg(t, ts[2], 2.5))
    put(img, sprite(("clk24", round(sw, 2)), 340, 340, lambda c: ic_clock24(c, 170, 170, 160, sw)), 340, 570, alpha=ease(seg(t, ts[1], 0.5)), shadow=10)
    conds = [("RESERVED TICKET", 2), ("CANCEL WITHIN 24 HOURS", 3), ("BEFORE THE TRAIN LEAVES", 4)]
    for i, (s_, k) in enumerate(conds):
        slide_in(img, t, ts[k], sprite(("c11", i), 760, 96, lambda c, s_=s_: (c.rrect((4, 4, 756, 92), 24, fill=CARD_BG, outline=GREEN_OK, width=5),
                 ic_check_c(c, 52, 48, 28), ftext(c, (410, 50), s_, 40, IVORY, 600))), 980, 430 + i * 120, dx=60, shadow=8)
    tl = last_t(11, ts[5])
    s_, a, p = pop(t, tl, 0.5)
    if p > 0:
        put(img, sprite("ref11", 380, 240, lambda c: (c.rrect((4, 4, 376, 236), 30, fill=GOLD, outline=(168, 118, 40), width=6), ic_card6(c, 190, 86, 0.9),
                 c.text((190, 192), "FULL REFUND", FONT_SANS, 40, GREEN_D, track=2))), 1610, 550, scale=s_, alpha=a, shadow=12)

# ============================================================ BLOCCO 12 - chi aiuta + 1 giorno
def draw12(img, t):
    ts = starts(12)
    common(img, t, "WHO IT HELPS")
    items = [(ic_runner, "BOOKS IN A HURRY", 1), (ic_kid, "BOOKS FOR A GRANDCHILD", 2), (ic_cal_q, "NOT SURE ABOUT THE DATE", 3)]
    for i, (ic, s_, k) in enumerate(items):
        seq(img, t, ts[k], sprite(("p12", i), 300, 300, lambda c, ic=ic: (c.ell((10, 10, 290, 290), fill=CARD_BG, outline=GOLD, width=6), ic(c, 150, 150, 1.2))), 340 + i * 0, 260 + i * 0, shadow=0) if False else None
        seq(img, t, ts[k], sprite(("p12", i), 240, 240, lambda c, ic=ic: (c.ell((8, 8, 232, 232), fill=CARD_BG, outline=GOLD, width=6), ic(c, 120, 124, 1.0))), 180, 260 + i * 245, shadow=8)
        seq(img, t, ts[k] + 0.2, T(s_, 40, IVORY, 520), 330 + 280, 260 + i * 245)
    seq(img, t, ts[4], pill("BOOK THE PRICE YOU LIKE", 38, 640), 1420, 230, shadow=8)
    seq(img, t, ts[5], sprite("cal12", 320, 300, lambda c: (ic_cal_check(c, 160, 150, 2.0))), 1420, 450, shadow=10)
    seq(img, t, ts[5] + 0.3, T("CHECK YOUR CALENDAR AT HOME", 34, SAGE, 640), 1420, 630)
    seq(img, t, ts[6], pill("1 FULL DAY", 48, 440, 90, GOLD, GREEN_D, (168, 118, 40)), 1420, 730, shadow=10)
    tl = last_t(12, ts[8])
    seq(img, t, ts[7], cardt("w12", 900, 120, RED, lines=[("UNRESERVED TICKETS:", 38, IVORY, 62)]), 1000, 900, shadow=8) if False else None
    seq(img, t, ts[7], sprite("un12", 1000, 110, lambda c: (c.rrect((4, 4, 996, 106), 26, fill=CARD_BG, outline=RED, width=6),
                                                            ic_hourglass(c, 70, 55, 0.6), ftext(c, (330, 57), "UNRESERVED TICKETS", 38, IVORY, 420))), 1180, 920, shadow=8)
    seq(img, t, tl, pill("ONLY 1 HOUR", 40, 330, 76, RED, IVORY, RED_D), 1500, 920, shadow=8)

# ============================================================ BLOCCO 13 - punto 3
def draw13(img, t):
    ts = starts(13)
    common(img, t, "NUMBER THREE")
    hero(img, t, ts, 3, "THE FARE YOU PICK")
    seq(img, t, ts[1], sprite("fares13", 360, 300, lambda c: ic_fares3(c, 180, 150, 1.6)), 420, 560, shadow=12)
    seq(img, t, ts[1] + 0.4, sprite("arr13", 200, 100, lambda c: c.poly([(6, 34), (130, 34), (130, 6), (194, 50), (130, 94), (130, 66), (6, 66)], fill=GOLD)), 780, 560)
    seq(img, t, ts[1] + 0.7, sprite("back13", 440, 300, lambda c: (c.rrect((4, 4, 436, 296), 30, fill=CARD_BG, outline=GOLD, width=6),
                                                                  ic_coin(c, 160, 120, 44), ic_coin(c, 280, 120, 44), ftext(c, (220, 232), "WHAT YOU GET BACK", 36, IVORY, 400))), 1120, 560, shadow=10)
    tl = last_t(13, ts[2])
    s_, a, p = pop(t, tl, 0.5)
    if p > 0:
        put(img, sprite("warn13", 440, 300, lambda c: (c.rrect((4, 4, 436, 296), 30, fill=CARD_BG, outline=RED, width=6),
                     warn_tri(c, 220, 110, 1.1, RED, IVORY), ftext(c, (220, 214), "MANY LOSE MONEY", 38, RED, 400), ftext(c, (220, 262), "WITHOUT KNOWING", 30, IVORY, 400))), 1600, 560, scale=s_, alpha=a, shadow=10)

# ============================================================ BLOCCO 14 - Flex
def fare_card(key, name, col, sub):
    def fn(c):
        w, h = 520, 640
        c.rrect((4, 4, w - 4, h - 4), 34, fill=CARD_BG, outline=col, width=8)
        c.rrect((4, 4, w - 4, 150), 34, fill=col)
        c.d.rectangle(c._b((4, 100, w - 4, 150)), fill=col)
        c.text((w / 2, 70), name, FONT_SANS, 76, GREEN_D, track=6)
        c.text((w / 2, 126), sub, FONT_SANS_M, 26, GREEN_D, track=3)
        ic_refund6(c, w / 2, 380, 2.4)
    return sprite(("fare6", key), 520, 640, fn)

def row14(key, ic, text, col=GREEN_OK):
    def fn(c):
        w, h = 760, 110
        c.rrect((4, 4, w - 4, h - 4), 26, fill=CARD_BG, outline=col, width=5)
        ic(c, 60, h / 2)
        ftext(c, (110, h / 2 + 2), text, 42, IVORY, w - 140, anchor="lm")
    return sprite(("row14", key), 760, 110, fn)

def draw14(img, t):
    ts = starts(14)
    common(img, t, "THE FLEX FARE")
    slide_in(img, t, ts[0], fare_card("flex", "FLEX", GREEN_OK, "FARE"), 440, 560, dx=-60, shadow=14)
    rows = [("CANCEL BEFORE THE TRAIN LEAVES", 1), ("ALL YOUR MONEY BACK", 1.5), ("NO FEE", 2), ("CHANGE IT: NO FEE", 3)]
    for i, (s_, k) in enumerate(rows):
        tk = ts[int(k)] + (0.9 if k % 1 else 0)
        slide_in(img, t, tk, row14(("f", i), lambda c, x, y: ic_check_c(c, x, y, 30), s_), 1220, 300 + i * 130, dx=50, shadow=8)
    tl = last_t(14, ts[4])
    seq(img, t, tl, pill("YOU ONLY PAY THE DIFFERENCE IN PRICE", 38, 900, 86, GOLD, GREEN_D, (168, 118, 40)), 1180, 880, shadow=10)

# ============================================================ BLOCCO 15 - Value 70/30, Sale 50/50
def bar15(key, frac, l, r):
    def fn(c):
        w, h = 1100, 120
        c.rrect((4, 4, w - 4, h - 4), 30, fill=RED, outline=IVORY, width=4)
        c.rrect((4, 4, 4 + (w - 8) * frac, h - 4), 30, fill=GREEN_OK)
        if frac < 1:
            c.d.rectangle(c._b((4 + (w - 8) * frac - 30, 4, 4 + (w - 8) * frac, h - 4)), fill=GREEN_OK)
        ftext(c, ((w - 8) * frac / 2, h / 2 + 2), l, 46, GREEN_D, (w - 8) * frac - 30)
        ftext(c, (4 + (w - 8) * frac + (w - 8) * (1 - frac) / 2, h / 2 + 2), r, 46, IVORY, (w - 8) * (1 - frac) - 30)
    return sprite(("bar15", key), 1100, 120, fn)

def grow(img, t, t0, spr, cx, cy, dur=0.7):
    p = ease(seg(t, t0, dur))
    if p > 0:
        w = max(2, int(spr.width * p))
        put(img, spr.crop((0, 0, w, spr.height)), cx - spr.width / 2 + w / 2, cy, alpha=min(1, p * 3))

def draw15(img, t):
    ts = starts(15)
    common(img, t, "VALUE AND SALE FARES")
    slide_in(img, t, ts[0], sprite("vcard15", 440, 220, lambda c: (c.rrect((4, 4, 436, 216), 30, fill=GOLD, outline=(168, 118, 40), width=6),
             c.text((220, 80), "VALUE", FONT_SANS, 70, GREEN_D, track=6), c.text((220, 160), "THE CHEAPER ONE", FONT_SANS_M, 30, GREEN_D, track=2))), 330, 300, dx=-50, shadow=10)
    seq(img, t, ts[1], pill("CAN'T CHANGE IT", 38, 440, 80, RED, IVORY, RED_D), 330, 470, shadow=8)
    seq(img, t, ts[2], T("CANCEL BEFORE DEPARTURE", 38, SAGE, 900), 1240, 220)
    seq(img, t, ts[3], sprite("tk15", 300, 140, lambda c: (c.rrect((4, 4, 296, 136), 20, fill=IVORY, outline=GOLD, width=5),
                                                          c.text((150, 72), "$100", FONT_SANS, 64, GREEN_D))), 1240, 320, shadow=8)
    if t >= ts[4]:
        grow(img, t, ts[4], bar15("v", 0.7, "$70 BACK", "$30 GONE" if t >= ts[5] else ""), 1240, 470)
    seq(img, t, ts[6], sprite("scard15", 440, 160, lambda c: (c.rrect((4, 4, 436, 156), 30, fill=CORAL, outline=RED_D, width=6),
             c.text((220, 82), "SALE", FONT_SANS, 70, IVORY, track=6))), 330, 760, shadow=10)
    tl = last_t(15, ts[7])
    if t >= tl:
        grow(img, t, tl, bar15("s", 0.5, "HALF BACK", "HALF GONE"), 1240, 760)

# ============================================================ BLOCCO 16 - la trappola
def draw16(img, t):
    ts = starts(16)
    common(img, t, "THE TRAP")
    seq(img, t, ts[0], sprite("trap16", 260, 180, lambda c: ic_trap(c, 130, 110, 1.1)), 260, 260, shadow=8)
    seq(img, t, ts[0] + 0.2, T("THE TRAP", 70, RED), 620, 260)
    seq(img, t, ts[1], pill("YOU DON'T SHOW UP", 40, 620, 86, IVORY, GREEN_D, RED), 520, 470, shadow=8)
    seq(img, t, ts[2], pill("YOU DON'T CANCEL", 40, 620, 86, IVORY, GREEN_D, RED), 520, 590, shadow=8)
    p = ease(seg(t, ts[2] + 0.5, 1.2))
    if p > 0:
        put(img, sprite("tleave16", 340, 180, lambda c: ic_bigtrain_leave(c, 200, 90, 1.1)), 1150 + 380 * p, 420, alpha=min(1, p * 3))
    seq(img, t, ts[3], sprite("tk16", 500, 240, lambda c: (c.rrect((4, 4, 496, 236), 26, fill=IVORY, outline=GOLD, width=6),
             c.rrect((4, 4, 496, 70), 26, fill=GREEN_L), c.d.rectangle(c._b((4, 40, 496, 70)), fill=GREEN_L),
             c.text((250, 40), "YOUR TRIP", FONT_SANS, 36, IVORY, track=4), ic_coin(c, 250, 156, 52))), 1340, 640, shadow=10)
    s_, a, pp = pop(t, ts[4], 0.5)
    if pp > 0:
        put(img, stamp6("LOST: EVERY DOLLAR", 560, 120, RED), 1340, 650, scale=s_, alpha=a, rot=-8, shadow=10)
    seq(img, t, last_t(16, ts[5]), pill("EVEN ON A FLEX FARE", 44, 740, 92, GOLD, GREEN_D, (168, 118, 40)), 960, 880, shadow=10)

# ============================================================ BLOCCO 17 - azione: Flex / cancella
def draw17(img, t):
    ts = starts(17)
    common(img, t, "YOUR ACTION")
    slide_in(img, t, ts[1], panel(860, 640, border=GOLD), 490, 540, dx=-50, shadow=14)
    seq(img, t, ts[1] + 0.3, T("PLANS MIGHT CHANGE?", 48, GOLD, 760), 490, 300)
    for i, ic in enumerate((ic_doctor, ic_cloud, ic_heart)):
        seq(img, t, ts[2] + i * 0.5, sprite(("p17", i), 200, 200, lambda c, ic=ic: (c.ell((6, 6, 194, 194), fill=(18, 66, 52), outline=SAGE, width=4), ic(c, 100, 100, 1.0))), 250 + i * 240, 480, shadow=6)
    seq(img, t, ts[3], pill("LOOK AT THE FLEX PRICE", 40, 700, 90, GREEN_OK, GREEN_D, GREEN_D), 490, 730, shadow=8)
    slide_in(img, t, ts[4], panel(860, 640, border=RED), 1430, 540, dx=50, shadow=14)
    seq(img, t, ts[4] + 0.3, T("CAN'T GO?", 48, RED, 760), 1430, 300)
    for i, (ic, s_) in enumerate(((ic_laptop, "ONLINE"), (ic_phone_app, "APP"), (ic_handset, "PHONE"))):
        seq(img, t, ts[5] + i * 0.4, sprite(("c17", i), 200, 250, lambda c, ic=ic, s_=s_: (c.ell((6, 6, 194, 194), fill=(18, 66, 52), outline=SAGE, width=4), ic(c, 100, 100, 0.9), c.text((100, 230), s_, FONT_SANS, 34, IVORY, track=2))), 1190 + i * 240, 500, shadow=6)
    seq(img, t, ts[6], pill("BEFORE THE TRAIN LEAVES", 38, 700, 90, IVORY, GREEN_D, GOLD), 1430, 730, shadow=8)
    ban(img, t, last_t(17, ts[7]), "NEVER JUST STAY HOME", cy=1000, w=980, h=84, size=46)

# ============================================================ BLOCCO 18 - punto 4 bagagli
def draw18(img, t):
    ts = starts(18)
    common(img, t, "NUMBER FOUR")
    hero(img, t, ts, 4, "YOUR BAGS")
    seq(img, t, ts[2], sprite("sb18", 220, 200, lambda c: ic_smallbag(c, 110, 110, 1.9)), 360, 520, shadow=10)
    seq(img, t, ts[2] + 0.2, T("1 PERSONAL ITEM", 40, IVORY, 460), 360, 680)
    for k in range(2):
        seq(img, t, ts[2] + 0.5 + k * 0.25, sprite("su18", 220, 280, lambda c: ic_suit(c, 110, 140, 1.7)), 1180 + k * 260, 500, shadow=10)
    seq(img, t, ts[2] + 1.0, T("2 CARRY ON BAGS", 40, IVORY, 560), 1310, 680)
    seq(img, t, ts[3], pill("NO CHARGE", 44, 380, 86, GOLD, GREEN_D, (168, 118, 40)), 790, 420, shadow=10)
    seq(img, t, ts[4], pill("UP TO 25 LB", 38, 360, 76), 360, 770, shadow=6)
    seq(img, t, ts[5], pill("UNDER THE SEAT", 34, 360, 70, CARD_BG, IVORY, SAGE), 360, 850, shadow=6)
    seq(img, t, last_t(18, ts[6]), pill("UP TO 50 LB EACH", 38, 460, 76), 1310, 770, shadow=6)

# ============================================================ BLOCCO 19 - etichette bagagli
def draw19(img, t):
    ts = starts(19)
    common(img, t, "CHECKED BAGS")
    seq(img, t, ts[0], T("ON TRAINS WITH CHECKED BAGGAGE", 44, SAGE, 1200), 960, 220)
    for k in range(2):
        seq(img, t, ts[1] + k * 0.3, sprite("tagf19", 320, 200, lambda c: ic_bagtag(c, 160, 100, 2.0, "FREE", GREEN_OK)), 330 + k * 360, 470, shadow=10, rot=-6 + k * 8)
    seq(img, t, ts[1] + 0.8, T("2 CHECKED BAGS", 46, IVORY, 700), 510, 660)
    seq(img, t, ts[2], sprite("tag20_19", 320, 200, lambda c: ic_bagtag(c, 160, 100, 2.0, "$20", RED)), 1300, 470, shadow=10, rot=5)
    seq(img, t, ts[2] + 0.3, T("EXTRA BAGS: $20 EACH", 46, RED, 700), 1300, 660)
    tl = last_t(19, ts[3])
    seq(img, t, tl, sprite("pl19", 1000, 110, lambda c: (c.rrect((4, 4, 996, 106), 26, fill=CARD_BG, outline=GOLD, width=6),
                                                        ic_plane(c, 90, 56, 0.6, IVORY), ftext(c, (540, 58), "COMPARE WITH YOUR LAST FLIGHT", 40, GOLD, 760))), 960, 860, shadow=10)

# ============================================================ BLOCCO 20 - lista: conta i bagagli
def draw20(img, t):
    ts = starts(20)
    common(img, t, "COUNT YOUR BAGS")
    seq(img, t, ts[0], pill("THE MISTAKE", 40, 440, 82, RED, IVORY, RED_D), 420, 220, shadow=8)
    seq(img, t, ts[0] + 0.3, sprite("x20a", 360, 230, lambda c: (ic_suit(c, 90, 120, 1.0), ic_suit(c, 190, 120, 1.0), ic_suit(c, 290, 120, 1.0), ic_x_c(c, 320, 40, 30))), 300, 440, shadow=8)
    seq(img, t, ts[0] + 0.6, T("ONE TOO MANY", 36, IVORY, 360), 300, 590)
    seq(img, t, ts[1], sprite("x20b", 260, 260, lambda c: (ic_suit(c, 130, 140, 1.7, (190, 140, 66)), ic_x_c(c, 220, 40, 30))), 640, 430, shadow=8)
    seq(img, t, ts[1] + 0.3, T("TOO BIG", 36, IVORY, 300), 640, 590)
    seq(img, t, ts[2], pill("$20 FOR EACH EXTRA PIECE", 36, 640, 80, IVORY, RED_D, RED), 470, 720, shadow=8)
    seq(img, t, ts[3], sprite("clip20", 760, 760, lambda c: (c.rrect((10, 40, 750, 750), 30, fill=IVORY, outline=(206, 200, 186), width=6),
             c.rrect((260, 10, 500, 80), 16, fill=GOLD), c.text((380, 150), "BEFORE YOU LEAVE", FONT_SANS, 40, GREEN_D, track=2))), 1380, 560, shadow=14)
    items = [("1 SMALL", 4), ("2 MEDIUM", 5), ("BIG ONES CHECKED", 6)]
    for i, (s_, k) in enumerate(items):
        tt = last_t(20, ts[k]) if k == 6 else ts[k]
        seq(img, t, tt, sprite(("li20", i), 620, 120, lambda c, s_=s_: (c.rrect((4, 4, 616, 116), 20, fill=(236, 240, 232)), ic_check_c(c, 64, 60, 34), ftext(c, (360, 62), s_, 46, GREEN_D, 470))), 1380, 400 + i * 150, shadow=4)

# ============================================================ BLOCCO 21 - punto 5 Red Cap
def draw21(img, t):
    ts = starts(21)
    common(img, t, "NUMBER FIVE")
    hero(img, t, ts, 5, "SOMEONE TO CARRY YOUR BAGS")
    seq(img, t, ts[2], sprite("rc21", 260, 360, lambda c: ic_redcap(c, 130, 200, 1.5)), 480, 570, shadow=12)
    seq(img, t, ts[2] + 0.3, pill("RED CAPS", 46, 380, 86, RED, IVORY, RED_D), 480, 820, shadow=8)
    seq(img, t, ts[2] + 0.1, T("AT MANY BIG STATIONS", 40, SAGE, 600), 1200, 380)
    seq(img, t, ts[3], sprite("cart21", 300, 260, lambda c: ic_cart(c, 150, 140, 1.5)), 1000, 600, shadow=10)
    seq(img, t, ts[3] + 0.2, T("THEY CARRY YOUR LUGGAGE", 34, IVORY, 520), 1000, 780)
    s_, a, p = pop(t, last_t(21, ts[4]), 0.5)
    if p > 0:
        put(img, stamp6("FREE", 340, 150, GREEN_OK), 1460, 600, scale=s_, alpha=a, rot=-8, shadow=10)

# ============================================================ BLOCCO 22 - 12 stazioni sulla linea
CITIES = ["CHICAGO", "NEW YORK", "WASHINGTON", "PHILADELPHIA", "BOSTON", "LOS ANGELES", "SEATTLE"]
def draw22(img, t):
    ts = starts(22)
    common(img, t, "WHERE TO FIND THEM")
    seq(img, t, ts[0], pill("12 MAJOR STATIONS", 46, 620, 92, GOLD, GREEN_D, (168, 118, 40)), 960, 200, shadow=10)
    p = ease(seg(t, ts[1], 0.6))
    if p > 0:
        put(img, sprite("line22", 1640, 20, lambda c: c.rrect((0, 4, 1640, 16), 6, fill=SAGE_D)), 960, 450, alpha=p)
    for i, cty in enumerate(CITIES):
        x = 220 + i * 246
        tt = ts[1] + 0.3 + i * 0.55
        seq(img, t, tt, sprite("pin22", 60, 60, lambda c: c.ell((6, 6, 54, 54), fill=GOLD, outline=IVORY, width=5)), x, 450, dur=0.35)
        seq(img, t, tt + 0.1, T(cty, 30, IVORY, 300), x, 380 if i % 2 == 0 else 520)
    seq(img, t, ts[2], sprite("rc22", 220, 300, lambda c: ic_redcap(c, 110, 170, 1.25)), 380, 760, shadow=10)
    seq(img, t, ts[2] + 0.3, pill("RED SHIRTS + RED CAPS", 40, 680, 86, RED, IVORY, RED_D), 920, 730, shadow=8)
    seq(img, t, last_t(22, ts[3]), pill("ONLY ACCEPT HELP FROM THIS UNIFORM", 38, 980, 86), 1080, 860, shadow=8)

# ============================================================ BLOCCO 23 - 3 schede + frase
def draw23(img, t):
    ts = starts(23)
    common(img, t, "RED CAP TIPS")
    cards = [("cl", lambda c, x, y: ic_claim(c, x, y, 1.0), "CLAIM CHECK", "KEEP IT SAFE", 0, 1), ("tip", lambda c, x, y: ic_tipjar(c, x, y, 1.1), "TIP IS WELCOME", "SERVICE COSTS NOTHING", 2, 3),
             ("hc", lambda c, x, y: ic_cart(c, x, y, 1.1), "SELF SERVICE", "HANDCARTS", 4, 4)]
    for i, (k, ic, l1, l2, k1, k2) in enumerate(cards):
        slide_in(img, t, ts[k1], cardt(("c23", k), 520, 480, GOLD if i != 1 else GREEN_OK, ic, 170, [(l1, 40, IVORY, 360)]), 360 + i * 600, 450, dy=50, shadow=12)
        seq(img, t, ts[k2] + (0.6 if k1 == k2 else 0), T(l2, 32, GOLD, 460), 360 + i * 600, 640)
    seq(img, t, ts[5], sprite("rc23", 160, 220, lambda c: ic_redcap(c, 80, 124, 0.9)), 300, 870, shadow=8)
    s_, a, p = pop(t, last_t(23, ts[6]), 0.5)
    if p > 0:
        put(img, bub("CAN YOU HELP ME WITH MY BAGS?", 1180, 150, 50), 1000, 860, scale=s_, alpha=a, shadow=10)

# ============================================================ BLOCCO 24 - punto 6 aiuto in stazione
def draw24(img, t):
    ts = starts(24)
    common(img, t, "NUMBER SIX")
    hero(img, t, ts, 6, "HELP GETTING TO YOUR TRAIN")
    seq(img, t, ts[2], sprite("st24", 240, 180, lambda c: ic_stairs(c, 120, 90, 1.2)), 280, 470, shadow=8)
    seq(img, t, ts[2] + 0.3, T("WALKING FAR OR STAIRS?", 34, SAGE, 400), 280, 600)
    seq(img, t, ts[3], pill("ASK FOR HELP AT THE STATION", 38, 740, 86, GOLD, GREEN_D, (168, 118, 40)), 960, 760, shadow=8)
    seq(img, t, ts[4], sprite("wc24", 260, 260, lambda c: (c.ell((6, 6, 254, 254), fill=CARD_BG, outline=GOLD, width=6), ic_wheelchair(c, 140, 120, 1.1))), 760, 480, shadow=10)
    seq(img, t, ts[4] + 0.2, T("STATION WHEELCHAIR", 32, IVORY, 360), 760, 640)
    s_, a, p = pop(t, last_t(24, ts[5]), 0.5)
    if p > 0:
        put(img, sprite("sf24", 260, 260, lambda c: (c.ell((6, 6, 254, 254), fill=CARD_BG, outline=GOLD, width=6), ic_staff(c, 130, 130, 1.2))), 1200, 480, scale=s_, alpha=a, shadow=10)
        put(img, T("A STAFF MEMBER", 32, IVORY, 360), 1200, 640, alpha=a)
        put(img, sprite("tr24", 220, 160, lambda c: ic_train6(c, 110, 80, 1.1)), 1620, 480, scale=s_, alpha=a)
        put(img, T("TO YOUR TRAIN", 32, GOLD, 360), 1620, 640, alpha=a)

# ============================================================ BLOCCO 25 - chiedilo prenotando
def draw25(img, t):
    ts = starts(25)
    common(img, t, "HOW TO ASK")
    seq(img, t, ts[0], pill("ASK WHEN YOU MAKE YOUR RESERVATION", 40, 1100, 92, GOLD, GREEN_D, (168, 118, 40)), 960, 210, shadow=10)
    slide_in(img, t, ts[1], cardt("web25", 700, 420, GREEN_OK, lambda c, x, y: ic_browser6(c, x, y, 1.1), 180, [("AMTRAK.COM", 54, GOLD, 350)]), 520, 520, dx=-50, shadow=12)
    slide_in(img, t, ts[2], cardt("tel25", 700, 420, GREEN_OK, lambda c, x, y: ic_handset(c, x, y, 1.2), 170, [("1-800-USA-RAIL", 54, GOLD, 350)]), 1400, 520, dx=50, shadow=12)
    seq(img, t, last_t(25, ts[3]), sprite("cw25", 1300, 120, lambda c: (c.rrect((4, 4, 1296, 116), 30, fill=CARD_BG, outline=SAGE, width=5),
             ic_wheelchair(c, 90, 44, 0.55), ftext(c, (700, 62), "COURTESY WHEELCHAIRS AT MOST STAFFED STATIONS", 38, IVORY, 1060))), 960, 860, shadow=10)

# ============================================================ BLOCCO 26 - 1 ora contro 10 minuti
def clock_card(key, label, ang, border, ok):
    def fn(c):
        w, h = 760, 520
        c.rrect((4, 4, w - 4, h - 4), 34, fill=CARD_BG, outline=border, width=7)
        ic_clock(c, 180, 200, 120, ang)
        ftext(c, (500, 160), label[0], 54, border, 460)
        ftext(c, (500, 230), label[1], 34, IVORY, 460)
        (ic_check_c if ok else ic_x_c)(c, 640, 400, 46)
    return sprite(("ck26", key), 760, 520, fn)

def draw26(img, t):
    ts = starts(26)
    common(img, t, "ARRIVE EARLY")
    slide_in(img, t, ts[0], clock_card("ok", ("1 HOUR", "BEFORE YOUR TRAIN"), 0.0, GREEN_OK, True), 500, 420, dx=-50, shadow=12)
    seq(img, t, ts[1], pill("TELL THE AGENT YOU'RE THERE", 36, 700, 82), 500, 750, shadow=8)
    seq(img, t, ts[2], pill("RESTROOM", 36, 330, 72, CARD_BG, IVORY, SAGE), 330, 860, shadow=6)
    seq(img, t, ts[3], pill("STAIRS", 36, 300, 72, CARD_BG, IVORY, SAGE), 680, 860, shadow=6)
    slide_in(img, t, ts[4], clock_card("bad", ("10 MINUTES", "EARLY, HOPING"), 2.1, RED, False), 1420, 420, dx=50, shadow=12)
    seq(img, t, ts[5], T("SOMEONE NOTICES YOU?", 40, IVORY, 700), 1420, 750)
    s_, a, p = pop(t, last_t(26, ts[6]), 0.5)
    if p > 0:
        put(img, stamp6("NOBODY WILL GUESS", 560, 120, RED), 1420, 870, scale=s_, alpha=a, rot=-5, shadow=10)

# ============================================================ BLOCCO 27 - punto 7 prenotare
def draw27(img, t):
    ts = starts(27)
    common(img, t, "NUMBER SEVEN")
    hero(img, t, ts, 7, "RESERVE BEFORE YOU GO")
    seq(img, t, ts[2], cardt("ramp27", 420, 380, GOLD, lambda c, x, y: ic_ramp(c, x, y, 1.3), 160, [("A RAMP", 44, IVORY, 320)]), 330, 560, shadow=10)
    seq(img, t, ts[2] + 0.5, cardt("lift27", 420, 380, GOLD, lambda c, x, y: ic_lift(c, x, y, 1.2), 160, [("A LIFT", 44, IVORY, 320)]), 790, 560, shadow=10)
    seq(img, t, ts[3], pill("RESERVE IT", 40, 400, 76, GOLD, GREEN_D, (168, 118, 40)), 560, 800, shadow=8)
    seq(img, t, ts[4], cardt("acc27", 560, 380, GREEN_OK, lambda c, x, y: ic_acc_seat(c, x, y, 1.3), 160, [("ACCESSIBLE SEAT", 40, IVORY, 320)]), 1430, 560, shadow=10)
    seq(img, t, ts[5], T("EVEN WITHOUT A WHEELCHAIR", 34, SAGE, 600), 1430, 775)
    seq(img, t, last_t(27, ts[6]), pill("RESERVE THAT TOO", 36, 440, 72, GREEN_OK, GREEN_D, GREEN_D), 1520, 840, shadow=8)

# ============================================================ BLOCCO 28 - posti limitati: mappa posti
def draw28(img, t):
    ts = starts(28)
    common(img, t, "THE CATCH")
    seq(img, t, ts[0], pill("THE CATCH", 42, 400, 82, RED, IVORY, RED_D), 330, 210, shadow=8)
    slide_in(img, t, ts[1], panel(900, 520, border=SAGE), 560, 560, dy=40, shadow=12)
    for r in range(3):
        for q in range(6):
            acc = (r, q) in ((0, 1), (2, 4))
            seq(img, t, ts[1] + 0.2 + (r * 6 + q) * 0.03, sprite(("seat28", acc), 110, 130, lambda c, acc=acc: ic_seat6(c, 55, 60, 0.85, GOLD if acc else (70, 90, 110))), 210 + q * 140, 400 + r * 150, dur=0.3)
    seq(img, t, ts[1] + 0.9, pill("ACCESSIBLE SEATS ARE LIMITED", 34, 760, 76), 560, 860, shadow=8)
    seq(img, t, ts[2], pill("BOOK EARLY", 44, 460, 90, GOLD, GREEN_D, (168, 118, 40)), 1460, 230, shadow=10)
    seq(img, t, ts[3], sprite("ok28", 800, 220, lambda c: (c.rrect((4, 4, 796, 216), 30, fill=CARD_BG, outline=GREEN_OK, width=6),
             ic_cal(c, 110, 110, 1.1, "1"), ftext(c, (440, 86), "BOOKS EARLY", 44, IVORY, 480), ftext(c, (440, 150), "GETS THE SEAT", 40, GREEN_OK, 480), ic_check_c(c, 730, 110, 40))), 1460, 470, shadow=10)
    seq(img, t, last_t(28, ts[4]), sprite("bad28", 800, 220, lambda c: (c.rrect((4, 4, 796, 216), 30, fill=CARD_BG, outline=RED, width=6),
             ic_person(c, 110, 110, 1.4, col=SAGE), ftext(c, (440, 86), "ASKS AT THE PLATFORM", 40, IVORY, 480), ftext(c, (440, 150), "NONE LEFT", 44, RED, 480), ic_x_c(c, 730, 110, 40))), 1460, 740, shadow=10)

# ============================================================ BLOCCO 29 - ossigeno
def draw29(img, t):
    ts = starts(29)
    common(img, t, "TRAVELING WITH OXYGEN")
    seq(img, t, ts[0], sprite("tank29", 220, 300, lambda c: ic_tank(c, 110, 160, 1.6)), 220, 470, shadow=10)
    seq(img, t, ts[1], T("FOR PASSENGERS", 36, SAGE, 400), 220, 690)
    seq(img, t, ts[1] + 0.2, T("WITH A DISABILITY", 36, IVORY, 400), 220, 740)
    steps = [("web", lambda c, x, y: (ic_browser6(c, x, y, 0.75), ic_x_c(c, x + 110, y - 70, 34)), [("NOT ON THE", 34, IVORY, 300), ("WEBSITE", 40, RED, 350)], RED, 2),
             ("tel", lambda c, x, y: ic_handset(c, x, y, 1.0), [("CALL", 40, IVORY, 300), ("1-800-USA-RAIL", 34, GOLD, 350)], GOLD, 3),
             ("cal", lambda c, x, y: ic_cal(c, x, y, 1.0, "!"), [("RESERVE", 40, IVORY, 300), ("IN ADVANCE", 38, GREEN_OK, 350)], GREEN_OK, 4),
             ("bat", lambda c, x, y: ic_battery(c, x, y, 0.95), [("4 HOURS WITHOUT", 32, IVORY, 300), ("TRAIN POWER", 38, GOLD, 350)], GOLD, 5)]
    for i, (k, ic, lines, col, j) in enumerate(steps):
        slide_in(img, t, ts[j], cardt(("o29", k), 340, 400, col, ic, 150, lines), 590 + i * 370, 520, dy=50, shadow=10)
    seq(img, t, last_t(29, ts[6]), pill("CHECK YOUR BATTERIES", 44, 760, 92, GOLD, GREEN_D, (168, 118, 40)), 1150, 860, shadow=10)

# ============================================================ BLOCCO 30 - punto 8 ghiaccio
def draw30(img, t):
    ts = starts(30)
    common(img, t, "NUMBER EIGHT")
    hero(img, t, ts, 8, "ICE FOR YOUR MEDICINE")
    seq(img, t, ts[2], sprite("pb30", 200, 240, lambda c: ic_pillbottle(c, 100, 130, 1.6)), 360, 560, shadow=10)
    seq(img, t, ts[2] + 0.3, T("MUST STAY COOL", 36, SAGE, 400), 360, 760)
    seq(img, t, ts[3], sprite("co30", 400, 300, lambda c: ic_cooler(c, 200, 170, 1.8)), 860, 580, shadow=12)
    for k in range(3):
        p = ease(seg(t, ts[3] + 0.5 + k * 0.25, 0.5))
        if p > 0:
            put(img, sprite("ice30", 120, 120, lambda c: ic_ice(c, 60, 60, 1.0)), 860 + (k - 1) * 90, 380 + 60 * p, alpha=min(1, p * 2))
    seq(img, t, ts[3] + 0.4, T("AMTRAK CAN GIVE YOU ICE", 38, IVORY, 600), 860, 780)
    s_, a, p = pop(t, last_t(30, ts[4]), 0.5)
    if p > 0:
        put(img, stamp6("MOST RIDERS NEVER ASK", 520, 120, GOLD), 1450, 580, scale=s_, alpha=a, rot=-6, shadow=10)

# ============================================================ BLOCCO 31 - pillole con te
def draw31(img, t):
    ts = starts(31)
    common(img, t, "KEEP YOUR PILLS WITH YOU")
    slide_in(img, t, ts[0], cardt("ok31", 560, 420, GREEN_OK, lambda c, x, y: (ic_smallbag(c, x - 40, y, 1.6), ic_pillbottle(c, x + 70, y + 10, 0.8)), 160,
                                  [("WITH YOU", 50, GREEN_OK, 330)]), 380, 420, dx=-50, shadow=12)
    slide_in(img, t, ts[1], cardt("bad31", 560, 420, RED, lambda c, x, y: (ic_suit(c, x, y, 1.3), ic_x_c(c, x + 110, y - 60, 36)), 170,
                                  [("NEVER IN A", 34, IVORY, 316), ("CHECKED BAG", 40, RED, 362)]), 1000, 420, dx=50, shadow=12)
    seq(img, t, ts[2], T("CAN'T REACH IT DURING THE TRIP", 34, IVORY, 560), 1000, 680)
    seq(img, t, ts[3], cardt("self31", 520, 300, GOLD, lambda c, x, y: ic_pillbottle(c, x, y, 0.9), 110, [("TAKE IT", 36, IVORY, 205), ("BY YOURSELF", 36, GOLD, 250)]), 1600, 420, shadow=10)
    seq(img, t, ts[4], sprite("co31", 260, 200, lambda c: ic_cooler(c, 130, 110, 1.1)), 260, 860, shadow=8)
    s_, a, p = pop(t, last_t(31, ts[6]), 0.5)
    if p > 0:
        put(img, bub("COULD I GET SOME ICE FOR MY MEDICINE?", 1340, 150, 46), 1110, 860, scale=s_, alpha=a, shadow=10)

# ============================================================ BLOCCO 32 - punto 9 cibo
def draw32(img, t):
    ts = starts(32)
    common(img, t, "NUMBER NINE")
    hero(img, t, ts, 9, "YOUR OWN FOOD")
    seq(img, t, ts[2], sprite("lb32", 240, 240, lambda c: ic_lunchbag(c, 120, 130, 1.5)), 380, 560, shadow=10)
    seq(img, t, ts[2] + 0.3, sprite("dr32", 160, 240, lambda c: ic_drink(c, 80, 140, 1.4)), 620, 560, shadow=10)
    seq(img, t, ts[2] + 0.5, T("FOOD AND DRINKS ON BOARD", 36, SAGE, 600), 500, 770)
    seq(img, t, ts[3], cardt("seat32", 420, 360, GREEN_OK, lambda c, x, y: ic_seat6(c, x, y, 1.3), 150, [("AT YOUR SEAT", 40, IVORY, 300)]), 1100, 560, shadow=10)
    seq(img, t, last_t(32, ts[4]), cardt("room32", 420, 360, GREEN_OK, lambda c, x, y: ic_bed(c, x, y, 1.3), 150, [("IN YOUR ROOM", 40, IVORY, 300)]), 1580, 560, shadow=10)

# ============================================================ BLOCCO 33 - ritardi, cibo da casa
def draw33(img, t):
    ts = starts(33)
    common(img, t, "WHY IT MATTERS")
    seq(img, t, ts[1], sprite("bd33", 500, 240, lambda c: ic_board_delay(c, 250, 120, 2.1)), 330, 330, shadow=10)
    seq(img, t, ts[2], sprite("sh33", 420, 260, lambda c: ic_shelf(c, 210, 140, 2.0)), 330, 620, shadow=8)
    seq(img, t, ts[2] + 0.3, T("FOOD CAN RUN LOW", 38, RED, 460), 330, 790)
    seq(img, t, ts[3], pill("DIABETES OR A SPECIAL DIET?", 38, 760), 1240, 230, shadow=8)
    seq(img, t, ts[4], T("CARRY ENOUGH FOOD FOR A DELAY", 40, GOLD, 900), 1240, 330)
    foods = [(ic_sandwich, "SANDWICH", 5), (ic_apple, "FRUIT", 6), (ic_crackers, "CRACKERS", 7)]
    for i, (ic, s_, k) in enumerate(foods):
        seq(img, t, ts[k], cardt(("f33", i), 300, 300, GREEN_OK, lambda c, x, y, ic=ic: ic(c, x, y, 1.0), 130, [(s_, 36, IVORY, 250)]), 920 + i * 320, 560, shadow=10)
    seq(img, t, last_t(33, ts[8]), pill("PACK IT AT HOME", 46, 600, 92, GOLD, GREEN_D, (168, 118, 40)), 1240, 830, shadow=10)

# ============================================================ BLOCCO 34 - 3 regole
def draw34(img, t):
    ts = starts(34)
    common(img, t, "ONE RULE PEOPLE BREAK")
    seq(img, t, ts[1], cardt("al34", 560, 560, GOLD, lambda c, x, y: ic_wine(c, x, y, 1.3), 170,
                            [("YOUR OWN ALCOHOL", 34, IVORY, 330), ("ONLY IN A PRIVATE", 32, GREEN_OK, 390), ("SLEEPING ROOM", 32, GREEN_OK, 432)]), 340, 520, shadow=12)
    seq(img, t, ts[2], pill("NEVER IN PUBLIC AREAS", 32, 520, 72, RED, IVORY, RED_D), 340, 860, shadow=8)
    seq(img, t, ts[3], cardt("dc34", 560, 560, GOLD, lambda c, x, y: ic_tray(c, x, y, 1.4), 170,
                            [("DINING CAR FOOD", 36, IVORY, 330), ("STAYS IN THE", 32, GOLD, 390), ("DINING CAR", 32, GOLD, 432)]), 960, 520, shadow=12)
    seq(img, t, ts[4], cardt("mw34", 560, 560, RED, lambda c, x, y: (ic_micro(c, x, y, 1.2), ic_x_c(c, x + 100, y - 60, 34)), 170,
                            [("THE CREW CAN'T HEAT", 32, IVORY, 330), ("OR REFRIGERATE", 32, IVORY, 374), ("YOUR OWN FOOD", 32, RED, 418)]), 1580, 520, shadow=12)
    seq(img, t, last_t(34, ts[5]), pill("BRING THINGS THAT TRAVEL WELL", 36, 700, 82, GOLD, GREEN_D, (168, 118, 40)), 1300, 860, shadow=8)

# ============================================================ BLOCCO 35 - punto 10 (breve)
def draw35(img, t):
    ts = starts(35)
    common(img, t, "NUMBER TEN")
    hero(img, t, ts, 10, "A NOTE FROM YOUR DOCTOR", it=2)
    seq(img, t, ts[1], pill("THE ONE ALMOST NOBODY KNOWS", 40, 820, 86, IVORY, GREEN_D, GOLD), 1120, 560, shadow=8)
    s_, a, p = pop(t, last_t(35, ts[2]), 0.22)
    if p > 0:
        put(img, sprite("note35", 300, 360, lambda c: ic_doc_note(c, 150, 180, 2.4)), 430, 560, scale=s_, alpha=a, shadow=12, rot=-5)

# ============================================================ BLOCCO 36 - Value + nota = niente penali
def draw36(img, t):
    ts = starts(36)
    common(img, t, "THE DOCTOR'S NOTE")
    seq(img, t, ts[0], sprite("vc36", 440, 200, lambda c: (c.rrect((4, 4, 436, 196), 30, fill=GOLD, outline=(168, 118, 40), width=6),
             c.text((220, 100), "VALUE", FONT_SANS, 70, GREEN_D, track=6))), 330, 280, shadow=10)
    seq(img, t, ts[1], T("CAN'T CHANGE IT", 34, IVORY, 420), 330, 420)
    seq(img, t, ts[2], T("LOSE PART IF YOU CANCEL", 34, RED, 420), 330, 470)
    seq(img, t, ts[3], sprite("flu36", 220, 220, lambda c: ic_flu(c, 100, 120, 1.1)), 330, 650, shadow=8)
    seq(img, t, ts[3] + 0.2, T("YOU GET SICK", 34, IVORY, 400), 330, 790)
    seq(img, t, ts[4], sprite("+36", 100, 100, lambda c: (c.rrect((40, 10, 60, 90), 6, fill=GOLD), c.rrect((10, 40, 90, 60), 6, fill=GOLD))), 700, 520)
    seq(img, t, ts[4] + 0.2, sprite("note36", 300, 360, lambda c: ic_doc_note(c, 150, 180, 2.4)), 960, 520, shadow=12, rot=-4)
    s_, a, p = pop(t, ts[5], 0.5)
    if p > 0:
        put(img, stamp6("FEES WAIVED", 460, 130, GREEN_OK), 1480, 450, scale=s_, alpha=a, rot=-7, shadow=10)
    seq(img, t, last_t(36, ts[6]), sprite("two36", 780, 200, lambda c: (c.rrect((4, 4, 776, 196), 30, fill=CARD_BG, outline=GREEN_OK, width=6),
             ic_two(c, 120, 110, 1.0), ftext(c, (470, 76), "THE SICK PASSENGER", 36, IVORY, 520), ftext(c, (470, 136), "+ THE PEOPLE WITH THEM", 34, GREEN_OK, 520))), 1460, 820, shadow=10)

# ============================================================ BLOCCO 37 - con e senza nota
def draw37(img, t):
    ts = starts(37)
    common(img, t, "WHAT THAT MEANS")
    for k in range(2):
        seq(img, t, ts[1] + k * 0.3, sprite("tk37", 260, 130, lambda c: (c.rrect((4, 4, 256, 126), 18, fill=IVORY, outline=GOLD, width=5),
                 c.text((130, 50), "VALUE", FONT_SANS, 36, GREEN_D, track=3), c.text((130, 94), "TICKET", FONT_SANS_M, 24, GREEN_D, track=3))), 250 + k * 290, 260, shadow=8, rot=-4 + k * 8)
    seq(img, t, ts[1] + 0.7, T("YOU AND YOUR PARTNER", 36, SAGE, 600), 395, 380)
    seq(img, t, ts[2], sprite("cal37", 200, 200, lambda c: ic_cal(c, 100, 100, 1.4, "7")), 960, 270, shadow=8)
    seq(img, t, ts[2] + 0.2, T("A WEEK BEFORE", 36, IVORY, 400), 960, 400)
    seq(img, t, ts[3], sprite("flu37", 220, 220, lambda c: ic_flu(c, 100, 120, 1.0)), 1430, 270, shadow=8)
    seq(img, t, ts[4], sprite("fall37", 240, 200, lambda c: ic_fall(c, 110, 110, 1.1)), 1680, 270, shadow=8)
    seq(img, t, ts[4] + 0.2, T("FLU OR A FALL", 36, IVORY, 400), 1550, 400)
    slide_in(img, t, ts[5], sprite("no37", 820, 300, lambda c: (c.rrect((4, 4, 816, 296), 34, fill=CARD_BG, outline=RED, width=7),
             ftext(c, (410, 70), "WITHOUT THE NOTE", 44, RED, 740), ftext(c, (410, 150), "PART OF THE MONEY", 40, IVORY, 740), ftext(c, (410, 210), "IS GONE", 40, IVORY, 740))), 500, 700, dx=-50, shadow=12)
    slide_in(img, t, last_t(37, ts[6]), sprite("yes37", 820, 300, lambda c: (c.rrect((4, 4, 816, 296), 34, fill=CARD_BG, outline=GREEN_OK, width=7),
             ftext(c, (410, 70), "WITH THE NOTE", 44, GREEN_OK, 740), ftext(c, (410, 150), "THE FEES GO AWAY", 40, IVORY, 740), ftext(c, (410, 210), "FOR BOTH OF YOU", 40, GOLD, 740))), 1420, 700, dx=50, shadow=12)

# ============================================================ BLOCCO 38 - 3 passi al telefono
def draw38(img, t):
    ts = starts(38)
    common(img, t, "DON'T STAY SILENT")
    seq(img, t, ts[0], sprite("hx38", 260, 240, lambda c: ic_house_x(c, 120, 140, 1.5)), 330, 340, shadow=10)
    seq(img, t, ts[0] + 0.3, T("STAYING HOME,", 38, IVORY, 520), 330, 520)
    seq(img, t, ts[0] + 0.5, T("SAYING NOTHING", 38, RED, 520), 330, 570)
    seq(img, t, ts[1], pill("= YOU LOSE THE WHOLE TRIP", 34, 560, 80, RED, IVORY, RED_D), 330, 690, shadow=8)
    seq(img, t, ts[2], T("THE MOMENT YOU KNOW YOU CAN'T GO", 38, GOLD, 1000), 1240, 220)
    steps = [("CALL AMTRAK BEFORE DEPARTURE", 3), ("SAY YOU'RE SICK", 4), ("ASK WHAT THEY NEED FROM YOUR DOCTOR", 5)]
    for i, (s_, k) in enumerate(steps):
        tt = last_t(38, ts[k]) if k == 5 else ts[k]
        slide_in(img, t, tt, sprite(("s38", i), 1040, 140, lambda c, i=i, s_=s_: (c.rrect((4, 4, 1036, 136), 30, fill=CARD_BG, outline=GOLD, width=6),
                 c.ell((24, 24, 116, 116), fill=GOLD), c.text((70, 72), str(i + 1), FONT_SANS, 56, GREEN_D), ftext(c, (580, 72), s_, 42, IVORY, 860))), 1240, 380 + i * 175, dx=50, shadow=8)
    seq(img, t, ts[3], sprite("ph38", 140, 140, lambda c: ic_handset(c, 70, 70, 0.9)), 1690, 900) if False else None

# ============================================================ BLOCCO 39 - riepilogo: 10 fermate
RECAP = ["CHOOSE SENIOR", "24 HOUR WINDOW", "THE RIGHT FARE", "FREE BAGS", "RED CAP", "STATION HELP", "RESERVE EARLY", "ICE FOR MEDICINE", "YOUR OWN FOOD", "DOCTOR'S NOTE"]
def stop_card(i):
    def fn(c):
        w, h = 320, 230
        c.rrect((4, 4, w - 4, h - 4), 26, fill=CARD_BG, outline=GOLD if i == 9 else GREEN_OK, width=6)
        c.ell((w / 2 - 40, 18, w / 2 + 40, 98), fill=GOLD)
        c.text((w / 2, 60), str(i + 1), FONT_SANS, 46, GREEN_D)
        words = RECAP[i].split(" ")
        if len(words) > 1 and len(RECAP[i]) > 11:
            mid = len(words) // 2 if len(words) > 2 else 1
            ftext(c, (w / 2, 140), " ".join(words[:mid]), 36, IVORY, w - 40)
            ftext(c, (w / 2, 186), " ".join(words[mid:]), 36, GOLD, w - 40)
        else:
            ftext(c, (w / 2, 160), RECAP[i], 38, IVORY, w - 40)
    return sprite(("stop39", i), 320, 230, fn)

def draw39(img, t):
    ts = starts(39)
    common(img, t, "ALL TEN TOGETHER")
    p = ease(seg(t, ts[0], 0.6))
    if p > 0:
        put(img, route_spr(0), 960, 175, alpha=p)
    for i in range(10):
        tt = ts[i + 1]
        if i == 9:
            tt = last_t(39, tt)
        x = 220 + (i % 5) * 370
        y = 420 + (i // 5) * 300
        seq(img, t, tt, stop_card(i), x, y, shadow=10)
        if t >= tt:
            put(img, sprite("dot39", 70, 70, lambda c: (c.ell((6, 6, 64, 64), fill=GOLD, outline=IVORY, width=4))), 960 - 750 + 60 + i * 153, 175 + 2, alpha=ease(seg(t, tt, 0.3)))

# ============================================================ BLOCCO 40 - la frase
def draw40(img, t):
    ts = starts(40)
    common(img, t, "THE ONE SENTENCE")
    seq(img, t, ts[1], pill("WHEN YOU BOOK", 40, 460, 84, GREEN_OK, GREEN_D, GREEN_D), 360, 230, shadow=8)
    seq(img, t, ts[2], pill("NOT ON THE PLATFORM", 40, 560, 84, RED, IVORY, RED_D), 960, 230, shadow=8) if False else None
    seq(img, t, ts[2], sprite("np40", 600, 84, lambda c: (c.rrect((4, 4, 596, 80), 42, fill=CARD_BG, outline=RED, width=5),
             ftext(c, (300, 44), "NOT ON THE PLATFORM", 38, RED, 520), c.line([(40, 44), (560, 44)], RED, 5))), 980, 230, shadow=8)
    s_, a, p = pop(t, ts[3], 0.5)
    if p > 0:
        put(img, bub("“I'M OVER 65, AND I NEED...”", 1300, 190, 72), 960, 440, scale=s_, alpha=a, shadow=14)
    seq(img, t, ts[4], T("THEN FINISH IT", 36, SAGE), 960, 600)
    ends = [("A SENIOR FARE", 5), ("HELP WITH MY BAGS", 6), ("A WHEELCHAIR TO THE TRAIN", 7)]
    for (s_, k), x, w in zip(ends, (300, 830, 1490), (480, 520, 760)):
        slide_in(img, t, ts[k], pill(s_, 40, w, 92, IVORY, GREEN_D, GOLD), x, 720, dy=40, shadow=8)
    ban(img, t, last_t(40, ts[8]), "AMTRAK CAN ONLY GIVE YOU WHAT YOU ASK FOR", cy=905, w=1400, h=92, size=46)

# ============================================================ BLOCCO 41 - la parte onesta
def draw41(img, t):
    ts = starts(41)
    common(img, t, "THE HONEST PART")
    items = [("FARES", ic_tag, ), ("STATIONS", None), ("SERVICES", None)]
    icons = [lambda c, x, y: ic_ticket6(c, x, y), lambda c, x, y: ic_train6(c, x, y, 1.0), lambda c, x, y: ic_redcap(c, x, y + 10, 0.7)]
    for i, (s_, ic) in enumerate(zip(("FARES", "STATIONS", "SERVICES"), icons)):
        seq(img, t, ts[1] + i * 0.35, cardt(("h41", i), 340, 330, GOLD, lambda c, x, y, ic=ic: (ic(c, x, y), ic_refresh(c, x + 110, y - 70, 0.4)), 140, [(s_, 40, IVORY, 270)]), 260 + i * 380, 420, shadow=10)
    seq(img, t, ts[2], pill("DIFFER FROM ROUTE TO ROUTE", 36, 760, 80), 640, 660, shadow=8)
    seq(img, t, ts[3], sprite("br41", 520, 360, lambda c: ic_browser6(c, 260, 180, 1.6)), 1550, 380, shadow=12)
    seq(img, t, ts[4], pill("CHECK BEFORE YOU BOOK", 36, 600, 80, GOLD, GREEN_D, (168, 118, 40)), 1550, 620, shadow=8)
    seq(img, t, ts[5], T("SOMETHING DOESN'T MATCH?", 38, IVORY, 760), 640, 820)
    s_, a, p = pop(t, last_t(41, ts[6]), 0.5)
    if p > 0:
        put(img, bub("TELL ME IN THE COMMENTS", 820, 140, 44, tail="right"), 1400, 830, scale=s_, alpha=a, shadow=10)

def ic_ticket6(c, cx, cy, s=1.0):
    c.rrect((cx - 80 * s, cy - 46 * s, cx + 80 * s, cy + 46 * s), 12 * s, fill=IVORY, outline=GOLD, width=4)
    c.rrect((cx - 80 * s, cy - 46 * s, cx + 80 * s, cy - 18 * s), 12 * s, fill=GREEN_L)
    c.text((cx, cy + 12 * s), "$", FONT_SANS, 44 * s, GREEN_D)

# ============================================================ BLOCCO 42 - lista della settimana
def draw42(img, t):
    ts = starts(42)
    common(img, t, "THIS WEEK")
    slide_in(img, t, ts[0], sprite("pad42", 1300, 820, lambda c: (c.rrect((10, 40, 1290, 810), 30, fill=IVORY, outline=(206, 200, 186), width=6),
             c.rrect((530, 10, 770, 80), 16, fill=GOLD), c.text((650, 150), "TO DO THIS WEEK", FONT_SANS, 52, GREEN_D, track=4))), 960, 560, dy=40, shadow=16)
    items = [("PUT YOUR ID WHERE YOU'LL FIND IT", 1, lambda c, x, y: ic_id6(c, x, y, 0.6)),
             ("WRITE DOWN 1-800-USA-RAIL", 2, lambda c, x, y: ic_handset(c, x, y, 0.6)),
             ("CHOOSE SENIOR + COMPARE THE FLEX PRICE", 4, lambda c, x, y: ic_tag(c, x, y, 0.8, GREEN_OK, False))]
    for i, (s_, k, ic) in enumerate(items):
        tt = last_t(42, ts[k]) if i == 2 else ts[k]
        seq(img, t, tt, sprite(("td42", i), 1120, 150, lambda c, s_=s_, ic=ic: (c.rrect((4, 4, 1116, 146), 24, fill=(236, 240, 232)),
                 ic_check_c(c, 70, 75, 40), ic(c, 190, 75), ftext(c, (680, 77), s_, 44, GREEN_D, 820))), 960, 400 + i * 175, shadow=4)

# ============================================================ BLOCCO 43 - mandalo
def draw43(img, t):
    ts = starts(43)
    common(img, t, "SEND IT")
    seq(img, t, ts[0], sprite("gp43", 300, 300, lambda c: (c.ell((6, 6, 294, 294), fill=CARD_BG, outline=GOLD, width=6), ic_person(c, 150, 150, 2.2, col=GOLD))), 1460, 420, shadow=10)
    seq(img, t, ts[0] + 0.2, chip65(), 1580, 300, scale=0.9, shadow=6)
    seq(img, t, ts[1], sprite("tr43", 260, 170, lambda c: ic_train6(c, 130, 80, 1.3)), 1460, 680, shadow=8)
    seq(img, t, ts[1] + 0.3, T("TO SEE THE GRANDKIDS", 34, SAGE, 500), 1460, 800)
    seq(img, t, ts[2], sprite("ph43", 260, 380, lambda c: ic_phone(c, 130, 190, 2.4)), 420, 480, shadow=12)
    p = ease(seg(t, ts[2] + 0.3, 0.8))
    if p > 0:
        put(img, sprite("sh43", 200, 160, lambda c: ic_share(c, 90, 90, 1.3)), 640 + 500 * p, 430, alpha=min(1, p * 3))
    seq(img, t, ts[2] + 0.2, pill("SEND THEM THIS VIDEO", 40, 600, 86, GOLD, GREEN_D, (168, 118, 40)), 820, 720, shadow=8) if False else None
    seq(img, t, ts[2] + 0.2, pill("SEND THEM THIS VIDEO", 40, 560, 86, GOLD, GREEN_D, (168, 118, 40)), 420, 760, shadow=8)
    seq(img, t, ts[3], pill("A HEAVY SUITCASE", 36, 460, 80), 640, 900, shadow=8)
    seq(img, t, last_t(43, ts[4]), pill("A WHOLE TICKET", 36, 420, 80, GOLD, GREEN_D, (168, 118, 40)), 1140, 900, shadow=8)

# ============================================================ BLOCCO 44 - commenti
def draw44(img, t):
    ts = starts(44)
    common(img, t, "YOUR TURN")
    seq(img, t, ts[0], sprite("cm44", 460, 380, lambda c: ic_comment(c, 230, 180, 2.4)), 520, 500, shadow=12)
    seq(img, t, ts[0] + 0.4, T("WHICH ONE SURPRISED YOU MOST?", 44, IVORY, 900), 1260, 400)
    seq(img, t, ts[1], pill("TELL ME BELOW", 44, 500, 92, GOLD, GREEN_D, (168, 118, 40)), 1260, 560, shadow=10)
    seq(img, t, last_t(44, ts[2]), T("I READ EVERY COMMENT", 40, SAGE, 800), 1260, 700, dur=0.33)

# ============================================================ BLOCCO 45 - like e iscriviti
def draw45(img, t):
    ts = starts(45)
    common(img, t, "IF THIS HELPED YOU")
    seq(img, t, ts[1], sprite("lk45", 560, 380, lambda c: (c.rrect((4, 4, 556, 376), 40, fill=CARD_BG, outline=GOLD, width=7), ic_thumb(c, 280, 160, 1.4),
             c.text((280, 320), "LIKE", FONT_SANS, 56, GOLD, track=6))), 560, 520, shadow=12)
    seq(img, t, ts[2], sprite("sb45", 680, 380, lambda c: (c.rrect((4, 4, 676, 376), 40, fill=RED, outline=RED_D, width=7), ic_bell6(c, 340, 150, 1.2, IVORY),
             c.text((340, 320), "SUBSCRIBE", FONT_SANS, 56, IVORY, track=6))), 1300, 520, shadow=12)
    seq(img, t, ts[2] + 0.3, T("THE SENIOR ADVANTAGE", 40, SAGE, 800), 1300, 770)
    ban(img, t, last_t(45, ts[3]), "SO YOU DON'T MISS THE NEXT ONE", cy=920, w=1100, h=90, size=46)

# ============================================================ BLOCCO 46 - disclaimer finale (modello video precedenti)
def draw46(img, t):
    ts = starts(46)
    a0 = ease(seg(t, 0, .5))
    put(img, tspr("BEFORE YOU GO", FONT_SANS, 44, SAGE, track=18), 960, 100, alpha=a0)
    put(img, tspr("ALWAYS CONFIRM", FONT_SANS, 112, IVORY), 560, 340 - 30 * (1 - ease(seg(t, .3, .5))), alpha=ease(seg(t, .3, .5)))
    put(img, tspr("BEFORE YOU RELY", FONT_SANS, 112, GOLD), 560, 480 - 30 * (1 - ease(seg(t, .9, .5))), alpha=ease(seg(t, .9, .5)))
    bp = pop(t, 1.4, 0.5)
    def panel_():
        c = Cv(990, 400)
        c.rrect((3, 3, 987, 397), 36, fill=CARD, outline=SAGE_D, width=5)
        return c.done()
    if bp[2] > 0:
        put(img, cache("p46_6", panel_), 595, 790, scale=bp[0], alpha=bp[1], shadow=16)
    lines = [("Rules, amounts and ages change", IVORY, ts[0] + 0.3), ("and differ by route and fare.", IVORY, ts[0] + 1.6),
             ("Always confirm with Amtrak", GOLD, ts[1] + 0.2), ("before you rely on them.", GOLD, ts[1] + 1.3),
             ("General information, not financial advice.", SAGE, ts[2] + 0.2), ("Not affiliated with Amtrak.", SAGE, last_t(46, ts[3]))]
    for i, (s_, col, st) in enumerate(lines):
        a = ease(seg(t, st, .5))
        if a > 0:
            put(img, tspr(s_, FONT_SANS_M if i > 3 else FONT_SANS, 36, col), 595, 650 + i * 58 - 20 * (1 - a), alpha=a)
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

DRAW = {b: globals()[f"draw{b}"] for b in range(6, 47)}

if __name__ == "__main__":
    if sys.argv[1] == "frame":
        b, sec = int(sys.argv[2]), float(sys.argv[3])
        img = background(sec); DRAW[b](img, sec); img.save(sys.argv[4]); sys.exit()
    b = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else DUR[b]
    out = os.environ.get("OUT", ".")
    os.makedirs(out, exist_ok=True)
    render_seq(DRAW[b], n, f"{out}/V6-blocco{b:02d}.mp4")
    print("ok blocco", b, n, "fotogrammi")
