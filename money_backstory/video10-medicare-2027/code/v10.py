"""Video 10 - Medicare 2027 Changes - tutti i 30 blocchi. Uso: python3 v10.py render|preview|check|spec <blocco>"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v10eng import *

R2 = row(2); R3 = row(3)
S = {}
# ---- 1: HOOK ----
S[1] = [
    slide('ONE DECISION FOR ALL OF 2027', 301, [E('cal', (180, 260, 760, 690), None, head='OPEN ENROLLMENT ENDS', big='DEC 7', sub='2026', col=red, size=130),
                                                 E('icard', (960, 270, 1740, 680), 'pay', icon='form', l1='WHAT YOU PAY', l2='FOR MEDICARE IN 2027', col=gold)],
          'ONE CHOICE SETS NEXT YEAR', gold),
    slide('5 CONFIRMED CHANGES', 302, [E('ring', (160, 240, 720, 720), None, val='5', sub='CHANGES', col=gold, size=150),
                                       E('icard', (900, 270, 1760, 680), 'drugs', icon='bag', l1='15 POPULAR DRUGS', l2='UP TO 85% CHEAPER', col=green, c2=green)],
          'ONE CUTS 15 DRUG PRICES BY UP TO 85%', green, psize=48),
]
# ---- 2: FRANK AND MARY ----
S[2] = [
    slide('MEET FRANK AND MARY', 303, [E('person', R2[0], None, letter='F', name='FRANK, 66', line='ORIGINAL MEDICARE', line2='+ DRUG PLAN, DIABETES DRUG', col=blue),
                                       E('person', R2[1], 'mary', letter='M', name='MARY, 68', line='MEDICARE ADVANTAGE', line2='ONE PLAN, ALL IN ONE', col=gold)],
          'TWO NEIGHBORS, TWO KINDS OF MEDICARE'),
    slide('TWO DIFFERENT LETTERS', 304, [E('icard', R2[0], 'street,', icon='mail', l1="FRANK'S LETTER", l2='DRUG PLAN CHANGES', col=blue),
                                         E('icard', R2[1], 'different', icon='mail', l1="MARY'S LETTER", l2='ADVANTAGE PLAN CHANGES', col=gold)],
          'SAME MAILBOX, DIFFERENT NEWS'),
]
# ---- 3: SOURCES ----
S[3] = [
    slide('STRAIGHT FROM MEDICARE', 305, [E('icard', R2[0], None, icon='doc', l1='MEDICARE.GOV', l2='2027 FACT SHEET', col=gold),
                                          E('icard', R2[1], 'centers', icon='bank', l1='CMS', l2='OFFICIAL 2027 NUMBERS', col=gold)],
          'EVERY NUMBER IS OFFICIAL'),
]
# ---- 4: NUMBER 1, DRUG CAP ----
S[4] = [
    slide('NUMBER 1: THE YEARLY DRUG CAP', 306, [E('card', (160, 280, 760, 660), None, head='2026 CAP', val='$2,100', sub='OUT OF POCKET', col=blue, vsize=110),
                                                 E('icard', (960, 280, 1740, 660), 'nothing', icon='check', l1='THEN YOU PAY $0', l2='FOR THE REST OF THE YEAR', col=green, c2=green)],
          'AFTER THE CAP, COVERED DRUGS COST $0', green, psize=48),
    slide('THE 2027 CAP', 307, [E('bars', (200, 250, 1000, 700), None, vals=[('2026', 2100, '$2,100'), ('2027', 2400, '$2,400')], lo=0.6),
                                E('big', (1100, 300, 1760, 600), 'rises', val='$2,400', sub='NEW YEARLY CAP', size=150)],
          'THE CAP RISES TO $2,400 IN 2027'),
]
# ---- 5: DEDUCTIBLE ----
S[5] = [
    slide('THE DEDUCTIBLE MOVES TOO', 308, [E('card', (160, 280, 700, 660), None, head='2026 MAX', val='$615', sub='DEDUCTIBLE', col=blue),
                                            E('arrow', (730, 430, 900, 510), 'above'),
                                            E('card', (930, 280, 1470, 660), 'above', head='2027 MAX', val='$700', sub='DEDUCTIBLE', col=red, vcol=red),
                                            E('stamp', (1500, 380, 1780, 560), 'some', t='$0 PLANS', col=green, ang=8, size=50)],
          'SOME PLANS HAVE NO DEDUCTIBLE AT ALL', green),
]
# ---- 6: FRANK'S CASE ----
S[6] = [
    slide("FRANK'S WORST CASE", 309, [E('person', (130, 260, 700, 700), None, letter='F', name='FRANK', line='EXPENSIVE DRUGS', line2='COVERED BY PART D', col=blue),
                                      E('step', (820, 300, 1790, 430), 'most', n=1, text='MOST HE CAN PAY IN 2027', val='$2,400'),
                                      E('step', (820, 480, 1790, 610), 'hundred', n=2, text="MORE THAN THIS YEAR'S LIMIT", val='+$300', vc=red)],
          'THEN $0 UNTIL JANUARY', green),
]
# ---- 7: PRESCRIPTION PAYMENT PLAN ----
S[7] = [
    slide('PRESCRIPTION PAYMENT PLAN', 310, [E('icard', R2[0], None, icon='bill', l1='A BIG BILL', l2='EARLY IN THE YEAR', col=red, c2=red),
                                             E('icard', R2[1], 'spreads', icon='clock', l1='MONTHLY PAYMENTS', l2='SPREAD ACROSS THE YEAR', col=green, c2=green)],
          'IT SPREADS YOUR DRUG COSTS', green),
    slide('WHAT MEDICARE SAYS', 311, [E('icard', R2[0], None, icon='cross', l1='DOES NOT LOWER', l2='YOUR COSTS', col=red, c2=red),
                                      E('icard', R2[1], 'spreads', icon='check', l1='ONLY SPREADS', l2='THEM OUT', col=gold)],
          'SAME TOTAL, SMALLER MONTHLY BILLS'),
]
# ---- 8: NUMBER 2, NEGOTIATED PRICES ----
S[8] = [
    slide('NUMBER 2: NEGOTIATED DRUG PRICES', 312, [E('ring', (180, 240, 760, 720), None, val='15', sub='MORE DRUGS', col=green, size=150),
                                                    E('cal', (1000, 270, 1700, 680), 'january', head='NEW PRICES START', big='JAN 1', sub='2027', col=green, size=130)],
          '15 MORE DRUGS, NEW PRICES IN JANUARY', green, psize=48),
    slide('WHAT THEY TREAT', 313, [E('step', (230, 260, 1690, 360), None, n=1, text='DIABETES'),
                                   E('step', (230, 380, 1690, 480), 'asthma,', n=2, text='ASTHMA AND COPD'),
                                   E('step', (230, 500, 1690, 600), 'cancer', n=3, text='CANCER'),
                                   E('step', (230, 620, 1690, 720), 'heart', n=4, text='HEART DISEASE')],
          'COMMON CONDITIONS AFTER 65', gold),
]
# ---- 9: OZEMPIC ----
S[9] = [
    slide('THE BIGGEST ONE', 314, [E('icard', (500, 260, 1420, 690), None, icon='bag', l1='OZEMPIC, RYBELSUS, WEGOVY', l2='30-DAY SUPPLY', col=gold)],
          'ONE DRUG FAMILY, MILLIONS OF USERS'),
    slide('LIST PRICE VS NEGOTIATED PRICE', 315, [E('card', (160, 280, 720, 660), None, head='LIST PRICE (2024)', val='$959', sub='30 DAYS', col=red, vcol=red, vsize=120),
                                                  E('arrow', (750, 430, 930, 510), 'negotiated'),
                                                  E('card', (960, 280, 1520, 660), 'negotiated', head='2027 PRICE', val='$274', sub='30 DAYS', col=green, vcol=green, vsize=120),
                                                  E('stamp', (1530, 380, 1790, 560), 'lower.', t='-71%', col=green, ang=-8, size=70)],
          '71% LOWER THAN THE LIST PRICE', green),
]
# ---- 10: MORE DRUGS ----
S[10] = [
    slide('NOT THE ONLY ONE', 316, [E('bars', (150, 250, 900, 700), None, vals=[('LIST', 654, '$654'), ('2027', 175, '$175')]),
                                    E('icard', (1040, 270, 1760, 660), 'asthma', icon='bag', l1='TRELEGY', l2='ASTHMA AND COPD', col=gold)],
          'TRELEGY: $654 TO $175', green),
    slide('UP TO 85% LOWER', 317, [E('icard', (160, 270, 860, 660), None, icon='bag', l1='JANUMET', l2='TYPE 2 DIABETES', col=gold),
                                   E('bars', (980, 250, 1500, 700), 'eighty', vals=[('LIST', 526, '$526'), ('2027', 80, '$80')]),
                                   E('stamp', (1510, 380, 1790, 560), 'lower.', t='-85%', col=green, ang=8, size=70)],
          'JANUMET: $526 TO $80', green),
]
# ---- 11: WHO SAVES ----
S[11] = [
    slide('WHO USES THESE DRUGS', 318, [E('big', (160, 280, 1000, 620), None, val='5.3M', sub='PEOPLE WITH MEDICARE (2024)', size=200),
                                        E('icard', (1100, 270, 1760, 660), 'save', icon='coins', l1='$685 MILLION', l2='OUT-OF-POCKET SAVINGS', col=green, c2=green)],
          'ESTIMATED SAVINGS IN 2027', green),
]
# ---- 12: THE CATCH ----
S[12] = [
    slide('THE CATCH', 319, [E('icard', R2[0], 'negotiated', icon='bank', l1='NEGOTIATED PRICE', l2='WHAT YOUR PLAN PAYS', col=gold),
                             E('icard', R2[1], 'depends', icon='form', l1='YOUR COPAY', l2='DEPENDS ON YOUR PLAN', col=red, c2=red)],
          'YOUR COST DEPENDS ON YOUR PLAN', red, (255, 255, 255)),
    slide("MEDICARE'S ADVICE", 320, [E('icard', (500, 260, 1420, 690), None, icon='phone', l1='CALL YOUR PLAN', l2='ASK HOW THESE PRICES AFFECT YOU', col=green, c2=green)],
          'ONE PHONE CALL', green),
]
# ---- 13: NUMBER 3, GLP-1 BRIDGE ----
S[13] = [
    slide('NUMBER 3: THE GLP-1 BRIDGE', 321, [E('icard', (500, 260, 1420, 690), None, icon='bulb', l1='NEW FOR 2027', l2='MEDICARE GLP-1 BRIDGE', col=gold)],
          'A NEW WAY TO GET GLP-1 DRUGS'),
    slide('WHO CAN USE IT', 322, [E('step', (230, 270, 1690, 390), 'drug', n=1, text='YOU HAVE A MEDICARE DRUG PLAN'),
                                  E('step', (230, 420, 1690, 540), 'already', n=2, text='NOT ALREADY COVERED BY YOUR PLAN'),
                                  E('step', (230, 570, 1690, 690), 'requirements,', n=3, text='YOU MEET THE OTHER RULES')],
          'CERTAIN GLP-1 DRUGS FOR WEIGHT LOSS', gold, psize=48),
]
# ---- 14: $50 COPAY ----
S[14] = [
    slide('THE COST', 323, [E('big', (160, 280, 1000, 620), None, val='$50', sub='COPAY, ONE-MONTH SUPPLY', size=220, vcol=green),
                            E('icard', (1100, 270, 1760, 660), 'qualifies,', icon='doc', l1='CHECK THE RULES', l2='ON MEDICARE.GOV', col=gold)],
          'NOT EVERYONE QUALIFIES', gold),
]
# ---- 15: NUMBER 4, PREMIUMS ----
S[15] = [
    slide('NUMBER 4: THE PREMIUM', 324, [E('icard', (500, 260, 1420, 690), None, icon='bill', l1='THE MONTHLY PREMIUM', l2='THE NUMBER MOST PEOPLE NEVER CHECK', col=gold)],
          'WHAT YOU PAY JUST TO HAVE A PLAN'),
    slide('MEDICARE ADVANTAGE, AVERAGE', 325, [E('bars', (300, 250, 1100, 700), 'drops', vals=[('2026', 14.37, '$14.37'), ('2027', 12.0, '$12.00')], lo=0.6),
                                              E('card', (1250, 300, 1700, 620), 'twelve', head='PER MONTH', val='-16.5%', col=green, vcol=green)],
          'AVERAGE ADVANTAGE PREMIUM GOES DOWN', green, psize=48),
]
# ---- 16: STAND-ALONE PART D ----
S[16] = [
    slide('STAND-ALONE DRUG PLANS', 326, [E('bars', (200, 250, 1000, 700), None, vals=[('2026', 35.09, '$35.09'), ('2027', 36.0, '$36')], lo=0.7),
                                          E('card', (1150, 300, 1700, 620), 'less', head='ON AVERAGE', val='< $1', sub='MORE PER MONTH', col=gold)],
          'LESS THAN $1 MORE A MONTH'),
    slide('AVERAGES HIDE A LOT', 327, [E('icard', (500, 260, 1420, 690), 'averages', icon='chart', l1='YOUR PLAN', l2='CAN MOVE DIFFERENTLY', col=red, c2=red)],
          'CHECK YOUR OWN PLAN', red, (255, 255, 255)),
]
# ---- 17: 8 IN 10 ----
S[17] = [
    slide('8 IN 10 vs 2 IN 10', 328, [E('card', R2[0], None, head='ADVANTAGE MEMBERS', val='8 IN 10', sub='SAME OR LOWER PREMIUM', col=green, vcol=green, vsize=110),
                                      E('card', R2[1], 'cannot.', head='ADVANTAGE MEMBERS', val='2 IN 10', sub='CANNOT KEEP THAT PRICE', col=red, vcol=red, vsize=110)],
          'MARY HAD TO CHECK HER GROUP', gold),
]
# ---- 18: PART B ----
S[18] = [
    slide('PART B: NOT ANNOUNCED YET', 329, [E('cal', (180, 280, 760, 650), None, head='PART B 2027', big='TBA', sub='COMING SOON', col=red),
                                             E('card', (900, 280, 1300, 640), 'ninety', head='2026 PREMIUM', val='$202.90', sub='PER MONTH', col=gold, vsize=80),
                                             E('card', (1360, 280, 1760, 640), 'deductible.', head='2026 DEDUCTIBLE', val='$283', sub='PER YEAR', col=gold, vsize=80)],
          'THE 2027 PART B NUMBER IS STILL COMING', red, (255, 255, 255), psize=46),
    slide('WHERE IT COMES FROM', 330, [E('pay', (160, 270, 900, 650), 'straight', amount='$ - B', head='SOCIAL SECURITY CHECK', sub='PART B TAKEN OUT', col=gold, size=120),
                                       E('icard', (1040, 270, 1760, 650), 'check.', icon='form', l1='MEDICARE PART B', l2='STRAIGHT OUT OF THE CHECK', col=red, c2=red)],
          'FOR MOST PEOPLE, IT IS AUTOMATIC'),
]
# ---- 19: NUMBER 5, THE TRAP ----
S[19] = [
    slide('NUMBER 5: THE TRAP', 331, [E('icard', R2[0], None, icon='bill', l1='DISCOUNT CARDS', l2='AND COUPON SITES', col=gold),
                                      E('icard', R2[1], 'cash', icon='coins', l1='LOW CASH PRICE', l2='AT THE PHARMACY', col=gold)],
          'IT LOOKS LIKE A GOOD DEAL'),
    slide('WHAT DOES NOT COUNT', 332, [E('icard', R2[0], 'deductible', icon='cross', l1='NOT YOUR DEDUCTIBLE', col=red, c2=red),
                                       E('icard', R2[1], 'cap.', icon='cross', l1='NOT YOUR YEARLY CAP', col=red, c2=red)],
          'COUPON MONEY DOES NOT COUNT', red, (255, 255, 255)),
]
# ---- 20: COUPON VS PLAN ----
S[20] = [
    slide('SAVE TODAY, PAY LATER?', 333, [E('icard', R2[0], None, icon='bill', l1='COUPON TODAY', l2='CHEAPER AT THE COUNTER', col=gold),
                                          E('card', R2[1], 'further', head='DISTANCE TO THE CAP', val='$2,400', sub='STILL FAR AWAY', col=red, vcol=red)],
          'FURTHER FROM YOUR CAP', red, (255, 255, 255)),
    slide('WHEN EACH ONE MAKES SENSE', 334, [E('icard', R2[0], 'generic,', icon='bag', l1='CHEAP GENERIC', l2='A COUPON CAN MAKE SENSE', col=gold),
                                             E('icard', R2[1], 'expensive', icon='check', l1='EXPENSIVE DRUG', l2='USE YOUR PLAN', col=green, c2=green)],
          'FOR BIG BILLS, USE YOUR PLAN', green),
]
# ---- 21: TWO MORE CHANGES ----
S[21] = [
    slide('TWO MORE CHANGES', 335, [E('icard', R2[0], None, icon='phone', l1='TELEHEALTH FROM HOME', l2='COVERED THROUGH DEC 31, 2027', col=green, c2=green),
                                    E('icard', R2[1], 'starting', icon='doc', l1='ELECTRONIC PRIOR APPROVALS', l2='ADVANTAGE PLANS, FROM JANUARY', col=gold)],
          'DECISIONS IN YOUR PATIENT PORTAL', gold, psize=50),
]
# ---- 22: THE LETTER ----
S[22] = [
    slide('THE ANNUAL NOTICE OF CHANGE', 336, [E('icard', (160, 260, 860, 690), None, icon='mail', l1='EVERY FALL', l2='FROM YOUR PLAN', col=gold),
                                               E('step', (980, 260, 1790, 360), 'premium,', n=1, text='PREMIUM'),
                                               E('step', (980, 380, 1790, 480), 'deductible,', n=2, text='DEDUCTIBLE'),
                                               E('step', (980, 500, 1790, 600), 'list', n=3, text='DRUG LIST'),
                                               E('step', (980, 620, 1790, 720), 'doctors', n=4, text='DOCTORS IN NETWORK')],
          'WHAT CHANGES IN JANUARY', gold),
    slide('MOST PEOPLE NEVER READ IT', 337, [E('icard', (500, 260, 1420, 690), 'throw', icon='cross', l1='THROWN AWAY', l2='WITHOUT READING IT', col=red, c2=red)],
          "DON'T THROW IT AWAY", red, (255, 255, 255)),
]
# ---- 23: MARY'S LETTER ----
S[23] = [
    slide("MARY READ HERS", 338, [E('person', (130, 260, 700, 700), None, letter='M', name='MARY', line='READ THE LETTER', line2='LINE BY LINE', col=gold),
                                  E('step', (820, 300, 1790, 430), 'premium', n=1, text='PREMIUM', val='SAME', vc=green),
                                  E('step', (820, 480, 1790, 610), 'tier.', n=2, text='ONE DRUG, HIGHER TIER', val='MORE', vc=red)],
          'ONE LINE THAT COST MORE', red, (255, 255, 255)),
    slide('WHY IT MATTERS', 339, [E('icard', (500, 260, 1420, 690), 'opened', icon='mail', l1='SHE OPENED THE LETTER', l2='AND FOUND IT IN TIME', col=green, c2=green)],
          'ONE LETTER, ONE CHANGE CAUGHT', green),
]
# ---- 24: THE DATES ----
S[24] = [
    slide('THE DATES', 340, [E('cal', (130, 270, 620, 660), None, head='OPEN ENROLLMENT', big='OCT 15', col=green, size=110),
                             E('arrow', (640, 430, 780, 510), 'december'),
                             E('cal', (800, 270, 1290, 660), 'december', head='LAST DAY', big='DEC 7', col=red, size=110),
                             E('cal', (1310, 270, 1790, 660), 'starts', head='CHANGES START', big='JAN 1', col=gold, size=110)],
          'ANY CHANGE STARTS ON JANUARY 1'),
    slide('MISS DECEMBER 7?', 341, [E('icard', (500, 260, 1420, 690), 'keep', icon='lock', l1='YOU KEEP YOUR PLAN', l2='WITH ALL ITS NEW COSTS', col=red, c2=red)],
          'DECEMBER 7 IS THE DEADLINE', red, (255, 255, 255)),
]
# ---- 25: MA OPEN ENROLLMENT ----
S[25] = [
    slide('ONE MORE WINDOW', 342, [E('cal', (180, 270, 780, 660), None, head='ADVANTAGE ONLY', big='JAN 1-MAR 31', col=gold, size=80),
                                   E('step', (900, 330, 1790, 460), 'switch', n=1, text='SWITCH ADVANTAGE PLANS'),
                                   E('step', (900, 500, 1790, 630), 'original', n=2, text='BACK TO ORIGINAL + DRUG PLAN')],
          'FOR MEDICARE ADVANTAGE MEMBERS', gold),
]
# ---- 26: RECAP ----
S[26] = [
    slide('THE 5 CHANGES', 343, [E('step', (230, 250, 1690, 340), None, n=1, text='DRUG CAP', val='$2,400'),
                                 E('step', (230, 360, 1690, 450), 'two:', n=2, text='15 NEGOTIATED PRICES', val='UP TO -85%'),
                                 E('step', (230, 470, 1690, 560), 'three:', n=3, text='GLP-1 BRIDGE', val='$50'),
                                 E('step', (230, 580, 1690, 670), 'four:', n=4, text='PREMIUMS MOVE', val='PART B TBA')],
          'FOUR DOWN, ONE TO GO'),
    slide('AND NUMBER 5', 344, [E('step', (330, 320, 1590, 460), None, n=5, text='COUPONS DO NOT COUNT TOWARD YOUR CAP', val='TRAP', vc=red),
                                E('line', (330, 540, 1590, 620), 'cap.', t='ALL OFFICIAL FOR 2027', size=56, col=goldL)],
          'FIVE CHANGES FOR 2027', green),
]
# ---- 27: THREE THINGS ----
S[27] = [
    slide('3 THINGS TO DO THIS WEEK', 345, [E('step', (230, 260, 1690, 400), None, n=1, text='READ YOUR ANNUAL NOTICE OF CHANGE', val='CIRCLE'),
                                            E('step', (230, 430, 1690, 570), 'second,', n=2, text='YOUR DRUGS IN THE PLAN FINDER', val='MEDICARE.GOV'),
                                            E('step', (230, 600, 1690, 740), 'third,', n=3, text='FREE STATE SHIP COUNSELOR', val='FREE')],
          'DO IT BEFORE DECEMBER 7', gold),
]
# ---- 28: FRANK & MARY ----
S[28] = [
    slide('WHAT FRANK DID', 346, [E('person', (130, 260, 700, 700), None, letter='F', name='FRANK', line='CALLED HIS PLAN', line2='DIABETES DRUG', col=blue),
                                  E('icard', (850, 270, 1760, 660), 'less', icon='check', l1='CONFIRMED', l2='LOWER COST IN 2027', col=green, c2=green)],
          'ONE CALL, NO GUESSING', green),
    slide('WHAT MARY DID', 347, [E('person', R2[0], None, letter='M', name='MARY', line='USED THE PLAN FINDER', line2='SWITCHED PLANS', col=gold),
                                 E('icard', R2[1], 'doctors.', icon='check', l1='LOWER DRUG TIER', l2='SAME DOCTORS', col=green, c2=green)],
          'SAME STREET, TWO SMARTER YEARS'),
]
# ---- 29: SHARE + COMMENT ----
S[29] = [
    slide('SEND IT TO ONE PERSON', 348, [E('icard', (500, 260, 1420, 690), None, icon='mail', l1='SOMEONE ON MEDICARE', l2='WHO THROWS AWAY THE PLAN MAIL', col=gold)],
          'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 349, [E('line', (260, 360, 1660, 450), None, t='DID YOUR PREMIUM GO', size=96, col=white),
                                           E('line', (260, 480, 1660, 570), 'down', t='UP OR DOWN FOR 2027?', size=96, col=goldL)],
          'ANSWER IN THE COMMENTS'),
]
# ---- 30: DISCLAIMER ----
S[30] = [frozen(final_slide)]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v10', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
