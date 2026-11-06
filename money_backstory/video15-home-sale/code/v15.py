"""Video 15 - Vendere casa dopo i 65 anni (Ray e Donna) - 22 blocchi. Uso: python3 v15.py render|preview|spec <blocco> [slide,slide]
Layout nuovi rispetto ai video 8-14: casa con cartello SOLD, cascata del guadagno, striscia dei 60 mesi, barra divisa esclusione/tassabile, scala delle aliquote,
barre a zone (Social Security), fascia dei due anni della vedova. Solo cio' che la voce dice, compare sulla sua parola (max 80%)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from homeeng import *

R2 = row(2); R3 = row(3); R3b = row(3, y1=620); R3c = row(3, y0=335, y1=700)
SRC = 'IRS.GOV'
G1, G2, G3, G4, G5, G6 = 'WHO QUALIFIES', 'THE MATH', 'THE RIPPLES', 'EXCEPTIONS', 'YOUR FAMILY', 'RECAP'
def CH(box, cue, t, good=True, size=40): return E('chip', box, cue, t=t, good=good, ic=(green if good else red), size=size)
S = {}
# ---- 1: HOOK ----
S[1] = [
    slide('A HOUSE SOLD AFTER 65', 3101, [E('househero', (150, 240, 720, 710), None),
                                         E('card', (800, 330, 1250, 580), 'one hundred forty thousand', head='BOUGHT FOR', val='$140,000', vsize=84, vcol=white, col=blue),
                                         E('arrow', (1260, 410, 1340, 500), None),
                                         E('card', (1350, 330, 1770, 580), 'nine hundred thousand', head='BUYER PAYS', val='$900,000', vsize=84, vcol=green, col=green)],
          'A BIG PROFIT', gold, src=SRC),
    slide('TAX FREE AFTER 65?', 3102, [E('big', (170, 270, 960, 660), 'it is easy', val='TAX FREE?', sub='AFTER 65, IS THE PROFIT TAX FREE?', size=150, vcol=goldL),
                                       E('stamp', (1000, 300, 1700, 640), 'it is not', t='NOT TRUE', col=red, ang=8, size=100)],
          'THE ANSWER IS NO', red, (255, 255, 255), src=SRC),
    slide('EXCLUSION, BUT NOT ALL', 3103, [E('icard', R3[0], 'allows a big exclusion', icon='form', l1='A BIG EXCLUSION', l2='FROM THE I R S', col=green, c2=green),
                                          E('icard', R3[1], 'part of this couple\'s', icon='coins', l1='PART IS STILL TAXED', l2='ON THE PROFIT', col=red, c2=red),
                                          E('icard', R3[2], 'raise their medicare', icon='bill', l1='MEDICARE BILL', l2='UP 2 YEARS LATER', col=blue, c2=goldL)],
          'THE EXACT NUMBERS', gold, src=SRC),
]
# ---- 2: MEET RAY AND DONNA ----
S[2] = [
    slide('MEET RAY AND DONNA', 3104, [E('person', R3[0], 'meet ray', letter='R', name='RAY, 72', line='RETIRED', col=blue),
                                      E('person', R3[1], 'and donna', letter='D', name='DONNA, 72', line='RETIRED', col=green),
                                      E('icard', R3[2], 'married filing jointly', icon='doc', l1='MARRIED', l2='FILING JOINTLY', col=gold)],
          'TWO PEOPLE, ONE HOME', gold, src=SRC),
    slide('THEIR HOME', 3105, [E('househero', (150, 240, 640, 710), None),
                              E('seg', (720, 280, 1770, 410), 'one hundred forty thousand for their home', label='PAID FOR THE HOME', val='$140,000', fill=gold, tc=navy),
                              E('seg', (720, 450, 1770, 580), 'another sixty thousand', label='NEW ROOF + KITCHEN', val='$60,000', fill=(60, 110, 170), tc=white)],
          'LONG AGO', gold, src=SRC),
    slide('THE PLAN', 3106, [E('card', row(3, y0=290, y1=620)[0], 'now they plan', head='THEY SELL FOR', val='$900,000', vsize=80, vcol=green, col=green),
                            E('icard', R3[1], 'move closer', icon='house', l1='MOVE CLOSER', l2='TO THEIR DAUGHTER', col=blue),
                            E('card', row(3, y0=290, y1=620)[2], 'their other income', head='OTHER INCOME', val='$90,000', sub='A YEAR', vsize=80, vcol=goldL, col=gold)],
          'PENSIONS + WITHDRAWALS', gold, src=SRC),
]
# ---- 3: SOURCES + FIVE THINGS ----
S[3] = [
    slide('OFFICIAL SOURCES ONLY', 3107, [E('icard', R3[0], 'publication five twenty-three', icon='doc', l1='I R S PUB 523', l2='SELLING YOUR HOME', col=gold),
                                         E('icard', R3[1], 'tax topic pages', icon='form', l1='I R S TOPIC PAGES', l2='SALE OF YOUR HOME', col=gold),
                                         E('icard', R3[2], 'social security administration\'s', icon='bank', l1='S S A + MEDICARE', l2='PREMIUM RULES', col=gold)],
          'NO AGENTS, NO SALES PAGES', gold, src='IRS + SSA + CMS'),
    slide('FIVE THINGS', 3108, [E('rule', (170, 245, 1750, 322), 'who qualifies', n=1, text='WHO QUALIFIES', val='THE TESTS', col=gold),
                               E('rule', (170, 337, 1750, 414), 'how the gain', n=2, text='HOW THE GAIN IS COUNTED', val='THE MATH', col=gold),
                               E('rule', (170, 429, 1750, 506), 'what it does', n=3, text='MEDICARE + SOCIAL SECURITY', val='THE RIPPLES', col=gold),
                               E('rule', (170, 521, 1750, 598), 'the cases that', n=4, text='CASES THAT CHANGE THE AMOUNT', val='EXCEPTIONS', col=gold),
                               E('rule', (170, 613, 1750, 690), 'what happens to your family', n=5, text='WHAT HAPPENS TO YOUR FAMILY', val='HEIRS', col=gold)],
          'FIVE THINGS TO KNOW', gold, src=SRC),
]
# ---- 4: WHO QUALIFIES ----
S[4] = [
    slide('THE EXCLUSION', 3109, [E('card', (150, 250, 940, 560), 'up to two hundred fifty', head='SINGLE OWNER', val='$250,000', sub='OF PROFIT EXCLUDED', vsize=110, vcol=white, col=blue),
                                 CH((420, 590, 1500, 700), 'your main home', 'WHEN YOU SELL YOUR MAIN HOME', True, 46),
                                 E('card', (980, 250, 1770, 560), 'up to five hundred', head='MARRIED, JOINT RETURN', val='$500,000', sub='OF PROFIT EXCLUDED', vsize=110, vcol=green, col=green)],
          'NUMBER ONE: WHO QUALIFIES', gold, tag=G1, src='IRS PUB 523'),
    slide('TWO TESTS, 5 YEARS', 3110, [E('step', (150, 245, 950, 385), 'you owned the home', n=1, text='OWNED IT', val='24 MONTHS', col=gold),
                                      E('step', (970, 245, 1770, 385), 'you lived in it', n=2, text='LIVED IN IT', val='24 MONTHS', col=green),
                                      E('fivebar', (150, 430, 1770, 720), 'all within the five years', rows=[('OWNED', [(20, 24)], gold, '24 MONTHS'), ('LIVED IN IT', [(30, 24)], green, '24 MONTHS')], end='DAY OF THE SALE')],
          'BOTH TESTS, LAST 5 YEARS', gold, tag=G1, src='IRS PUB 523'),
]
# ---- 5: DETAILS ----
S[5] = [
    slide('NOT IN A ROW', 3111, [E('fivebar', (150, 250, 1770, 500), 'do not have to be in a row', rows=[('LIVED IN IT', [(8, 11), (31, 13)], green, 'ADDS UP TO 24 MONTHS')], end='DAY OF THE SALE'),
                                E('big', (350, 540, 1570, 700), 'seven hundred thirty', val='24 MONTHS = 730 DAYS', sub='', size=100, vcol=goldL)],
          'THE DAYS JUST ADD UP', gold, tag=G1, src='IRS PUB 523'),
    slide('MARRIED COUPLES', 3112, [E('icard', R2[0], 'only one spouse', icon='doc', l1='OWNERSHIP TEST', l2='ONE SPOUSE IS ENOUGH', col=gold),
                                   E('icard', R2[1], 'but both must pass', icon='house', l1='LIVING-IN-IT TEST', l2='BOTH SPOUSES MUST PASS', col=green, c2=green)],
          'ONE OWNS, BOTH LIVE THERE', gold, tag=G1, src='IRS PUB 523'),
    slide('LIMITS TO KNOW', 3113, [E('cal', (150, 260, 760, 690), 'once every two years', head='THE EXCLUSION, ONCE EVERY', big='2 YEARS', size=130, col=gold),
                                  E('icard', (850, 260, 1770, 690), 'only on your main home', icon='house', l1='ONLY YOUR MAIN HOME', l2='NOT A VACATION HOUSE', col=blue, c2=goldL)],
          'ONE MAIN HOME AT A TIME', gold, tag=G1, src='IRS PUB 523'),
    slide('NURSING HOME COUNTS', 3114, [E('flow', (150, 250, 1770, 700), 'cannot care for yourself', nodes=[('house', 'MAIN HOME', '12+ OF LAST 5 YEARS', gold), ('bank', 'LICENSED CARE', 'NURSING HOME', blue), ('check', 'STILL COUNTS', 'AS LIVING THERE', green)], s=0.8)],
          'MOVING INTO CARE IS OK', green, tag=G1, src='IRS PUB 523'),
]
# ---- 6: THE FORMULA ----
S[6] = [
    slide('THE I R S FORMULA', 3165, [E('big', (170, 270, 1750, 560), 'the i r s formula', val='THE GAIN FORMULA', sub='THE I R S FORMULA IS SIMPLE', size=110, vcol=goldL)],
          'NEXT: THE MATH', gold, tag=G2, src='IRS PUB 523'),
    slide('PRICE MINUS SELLING COSTS', 3115, [E('icard', (150, 260, 620, 690), 'selling price', icon='house', l1='SELLING PRICE', l2='', col=gold, size=44),
                                             E('op', (620, 380, 720, 560), None, t='-', size=130, col=red),
                                             E('icard', (720, 260, 1190, 690), 'selling costs', icon='coins', l1='SELLING COSTS', l2='AGENT · ADS · LEGAL', col=red, c2=red, size=44)],
          'START WITH THE PRICE', gold, tag=G2, src='IRS PUB 523'),
    slide('THE AMOUNT REALIZED', 3162, [E('icard', (150, 260, 620, 690), None, icon='house', l1='SELLING PRICE', l2='', col=gold, size=44),
                                       E('op', (620, 380, 720, 560), None, t='-', size=130, col=red),
                                       E('icard', (720, 260, 1190, 690), None, icon='coins', l1='SELLING COSTS', l2='AGENT · ADS · LEGAL', col=red, c2=red, size=44),
                                       E('op', (1190, 380, 1290, 560), None, t='=', size=130, col=goldL),
                                       E('icard', (1290, 260, 1760, 690), 'amount realized', icon='bag', l1='AMOUNT REALIZED', l2='', col=green, size=40)],
          'PRICE - COSTS = AMOUNT REALIZED', gold, tag=G2, src='IRS PUB 523'),
    slide('THEN THE BASIS', 3116, [E('icard', (150, 260, 620, 690), None, icon='bag', l1='AMOUNT REALIZED', l2='', col=green, size=40),
                                  E('op', (620, 380, 720, 560), None, t='-', size=130, col=red),
                                  E('icard', (720, 260, 1190, 690), 'adjusted basis', icon='doc', l1='ADJUSTED BASIS', l2='WHAT YOU INVESTED', col=blue, c2=goldL, size=44),
                                  E('op', (1190, 380, 1290, 560), None, t='=', size=130, col=goldL),
                                  E('icard', (1290, 260, 1760, 690), 'what is left is your gain', icon='chart', l1='YOUR GAIN', l2='WHAT IS LEFT', col=gold, size=48)],
          'AMOUNT REALIZED MINUS BASIS', gold, tag=G2, src='IRS PUB 523'),
    slide('A LOSS IS NOT DEDUCTIBLE', 3117, [E('icard', (150, 260, 860, 690), 'if it is negative', icon='cross', l1='A LOSS ON YOUR HOME', l2='GAIN BELOW ZERO', col=red, c2=red),
                                            E('big', (940, 290, 1770, 660), 'you cannot deduct', val='NO DEDUCTION', sub='THE I R S: CANNOT DEDUCT IT', size=88, vcol=red)],
          'LOSSES DO NOT COUNT', red, (255, 255, 255), tag=G2, src='IRS PUB 523'),
]
# ---- 7: BASIS ----
S[7] = [
    slide('WHAT IS IN YOUR BASIS', 3118, [CH((150, 260, 950, 410), 'the price you paid', 'THE PRICE YOU PAID', True, 44), CH((970, 260, 1770, 410), 'legal fees', 'LEGAL + RECORDING FEES', True, 40),
                                         CH((150, 450, 950, 600), 'transfer taxes', 'TRANSFER TAXES', True, 44), CH((970, 450, 1770, 600), 'owner\'s title insurance', 'OWNER\'S TITLE INSURANCE', True, 40)],
          'PRICE + CLOSING COSTS', green, tag=G2, src='IRS PUB 523'),
    slide('IMPROVEMENTS COUNT', 3119, [E('icard', (150, 255, 560, 700), 'a new roof', icon='house', l1='NEW ROOF', l2='', col=green, size=44, s=0.7),
                                      E('icard', (590, 255, 1000, 700), 'a kitchen remodel', icon='bulb', l1='KITCHEN', l2='REMODEL', col=green, size=44, s=0.7),
                                      E('icard', (1030, 255, 1440, 700), 'an addition', icon='doc', l1='AN ADDITION', l2='', col=green, size=44, s=0.7),
                                      E('icard', (1470, 255, 1770, 700), 'a new heating system', icon='clock', l1='NEW HEATING', l2='SYSTEM', col=green, size=40, s=0.7)],
          'IMPROVEMENTS RAISE BASIS', green, tag=G2, src='IRS PUB 523'),
    slide('NOT IN YOUR BASIS', 3120, [CH((300, 260, 1620, 380), 'repairs like painting', 'REPAIRS LIKE PAINTING', False, 44), CH((300, 410, 1620, 530), 'fixing a leak', 'FIXING A LEAK', False, 44),
                                     CH((300, 560, 1620, 680), 'loan fees and points', 'LOAN FEES AND POINTS', False, 44)],
          'REPAIRS DO NOT COUNT', red, (255, 255, 255), tag=G2, src='IRS PUB 523'),
    slide('KEEP YOUR RECEIPTS', 3121, [E('icard', (150, 260, 860, 690), 'keep your receipts', icon='doc', l1='KEEP YOUR RECEIPTS', l2='PROOF OF YOUR BASIS', col=gold),
                                      E('big', (940, 290, 1770, 660), 'three years after', val='3 YEARS', sub='AFTER THE RETURN DUE DATE', size=130, vcol=goldL)],
          'KEEP THEM LONG ENOUGH', gold, tag=G2, src='IRS PUB 523'),
]
# ---- 8: RAY AND DONNA MATH (cascata) ----
WFA = [('SALE PRICE', 900, 'total'), ('SELLING COSTS', 54, 'minus'), ('AMOUNT REALIZED', 846, 'final')]
WFB = [('AMOUNT REALIZED', 846, 'total'), ('ADJUSTED BASIS', 200, 'minus'), ('GAIN', 646, 'final')]
def WF(box, steps, fmt, cues):
    x0, y0, x1, y1 = box; return [E('wfbar', box, cu, steps=steps, i=i, fmt=fmt, gbox=box) for i, cu in enumerate(cues)]
S[8] = [
    slide('THEIR BASIS', 3122, [E('seg', (150, 270, 1770, 390), 'one hundred forty thousand they paid', label='THEY PAID FOR THE HOME', val='$140,000', fill=gold, tc=navy),
                               E('seg', (150, 420, 1770, 540), 'sixty thousand in improvements', label='PLUS IMPROVEMENTS', val='+ $60,000', fill=(60, 110, 170), tc=white),
                               E('seg', (150, 590, 1770, 710), 'so two hundred thousand', label='THEIR BASIS', val='$200,000', fill=green, tc=white)],
          'BASIS: $200,000', gold, tag=G2, src='IRS PUB 523'),
    slide('SALE PRICE TO AMOUNT REALIZED', 3123, WF((150, 235, 1770, 720), WFA, ['$900,000', '$54,000', '$846,000'], ['sell at nine hundred thousand', 'fifty-four thousand', 'amount realized is']),
          'AMOUNT REALIZED: $846,000', gold, tag=G2, src='IRS PUB 523'),
    slide('FROM REALIZED TO GAIN', 3124, WF((150, 235, 1770, 720), WFB, ['$846,000', '$200,000', '$646,000'], [None, 'subtract the basis', 'their gain is']),
          'THEIR GAIN: $646,000', gold, tag=G2, src='IRS PUB 523'),
    slide('EXCLUDED VS TAXABLE', 3125, [E('splitbar', (150, 240, 1770, 500), 'their exclusion', head='THEIR GAIN', tot='$646,000', parts=[('EXCLUDED', 500, green, '$500,000'), ('TAXABLE', 146, red, '$146,000')]),
                                       E('card', (560, 540, 1360, 710), 'so one hundred forty-six', head='TAXABLE GAIN', val='$146,000', vsize=70, vcol=red, col=red)],
          'ONLY $146,000 IS TAXABLE', red, (255, 255, 255), tag=G2, src='IRS PUB 523'),
]
# ---- 9: RECEIPTS ----
S[9] = [
    slide('WITH AND WITHOUT RECEIPTS', 3126, [E('card', row(2, y0=290, y1=590)[0], 'notice what the receipts', head='WITH RECEIPTS', val='$146,000', sub='TAXABLE GAIN · BASIS $200,000', vsize=100, vcol=green, col=green),
                                             E('card', row(2, y0=290, y1=590)[1], 'two hundred six', head='WITHOUT RECEIPTS', val='$206,000', sub='TAXABLE GAIN · BASIS $140,000', vsize=100, vcol=red, col=red)],
          'THE SAME HOUSE, TWO RESULTS', gold, tag=G2, src='IRS PUB 523'),
    slide('LOST RECEIPTS COST', 3127, [E('big', (150, 270, 960, 660), 'that is sixty thousand', val='+$60,000', sub='EXTRA PROFIT ON PAPER', size=170, vcol=red),
                                      CH((1020, 330, 1770, 450), 'receipts for the roof', 'ROOF RECEIPTS LOST', False, 40), CH((1020, 490, 1770, 610), 'and the kitchen', 'KITCHEN RECEIPTS LOST', False, 40)],
          'KEEP EVERY RECEIPT', red, (255, 255, 255), tag=G2, src='IRS PUB 523'),
]
# ---- 10: TAX RATES ----
S[10] = [
    slide('LONG-TERM CAPITAL GAIN', 3128, [E('cal', (150, 300, 700, 620), 'more than a year', head='OWNED MORE THAN', big='1 YEAR', size=120, col=gold, sub='A LONG-TERM GAIN'),
                                          E('rates', (770, 245, 1770, 700), 'taxed at zero', steps=[('0%', 'LOWEST', green), ('15%', 'MIDDLE', gold), ('20%', 'TOP', red)])],
          'LONG-TERM RATES: 0, 15, 20', gold, tag=G2, src='IRS TOPIC 409'),
    slide('2026 JOINT RETURN', 3129, [E('line', (150, 240, 1770, 290), 'for twenty twenty-six', t='2026 · JOINT RETURN · TAXABLE INCOME', size=40, col=goldL),
                                     E('rates', (170, 305, 1750, 710), 'a joint return pays zero', steps=[('0%', 'UP TO $98,900', green), ('15%', 'UP TO $613,700', gold), ('20%', 'ABOVE THAT', red)], hi=1)],
          'THE 2026 BRACKETS', gold, tag=G2, src='IRS REV. PROC. 2025-32'),
    slide('THE MOST THEY OWE', 3130, [E('calc', (150, 270, 1770, 420), 'so ray and donna owe', parts=[('$146,000', white, 64), ('x', goldL, 64), ('15%', gold, 64), ('=', goldL, 64), ('$21,900', green, 70)]),
                                     CH((300, 480, 1620, 600), 'and less if part', 'LESS IF PART FALLS IN THE 0% BRACKET', True, 40)],
          'AT MOST $21,900', green, tag=G2, src='IRS PUB 523'),
]
# ---- 11: NIIT, STATE, DEPRECIATION ----
S[11] = [
    slide('NET INVESTMENT INCOME TAX', 3131, [E('big', (150, 260, 640, 600), 'three point eight percent', val='3.8%', sub='EXTRA TAX', size=150, vcol=red),
                                             E('card', (700, 250, 1770, 400), 'joint return', head='JOINT RETURN', val='OVER $250,000', vsize=72, vcol=white, col=gold),
                                             E('card', (700, 430, 1770, 580), 'two hundred thousand if single', head='SINGLE', val='OVER $200,000', vsize=72, vcol=white, col=blue),
                                             CH((700, 610, 1770, 720), 'the excluded profit', 'EXCLUDED PROFIT DOES NOT COUNT', True, 38)],
          'ONLY ABOVE THE INCOME LIMIT', gold, tag=G2, src='IRS TOPIC 559'),
    slide('RAY AND DONNA, STATE TAXES', 3132, [CH((200, 290, 1720, 420), 'ray and donna stay under', 'RAY AND DONNA STAY UNDER THE LIMIT', True, 46), CH((200, 470, 1720, 600), 'state taxes are separate', 'STATE TAXES ARE SEPARATE', False, 46)],
          'THE I R S RULES ONLY', gold, tag=G2, src='IRS TOPIC 559'),
    slide('RENTAL USE AFTER 1997', 3133, [E('icard', (150, 260, 860, 690), 'claim depreciation', icon='house', l1='DEPRECIATION CLAIMED', l2='RENTAL OR BUSINESS PART', col=gold),
                                         E('stamp', (960, 330, 1730, 620), 'cannot be excluded', t='NO EXCLUSION', col=red, ang=8, size=76)],
          'THAT GAIN IS TAXED', red, (255, 255, 255), tag=G2, src='IRS PUB 523'),
]
# ---- 12: PAPERWORK ----
S[12] = [
    slide('REPORT THE SALE', 3134, [E('flow', (150, 250, 1770, 700), 'form ten ninety-nine', nodes=[('mail', 'FORM 1099-S', 'YOU RECEIVE IT', gold), ('form', 'FORM 8949', 'REPORT THE SALE', gold), ('check', 'EVEN IF', 'ALL GAIN IS EXCLUDED', green)], s=0.8)],
          'REPORT IT EVEN IF EXCLUDED', gold, tag=G2, src='IRS TOPIC 701'),
    slide('PAY AS YOU GO', 3135, [E('icard', R2[0], 'raise your withholding', icon='form', l1='RAISE WITHHOLDING', l2='OR', col=gold),
                                 E('icard', R2[1], 'estimated payments', icon='bill', l1='ESTIMATED PAYMENTS', l2='DURING THE YEAR', col=blue, c2=goldL)],
          'NO SURPRISE NEXT SPRING', gold, tag=G2, src='IRS PUB 523'),
]
# ---- 13: THE RIPPLES (Medicare, two years) ----
S[13] = [
    slide('NUMBER THREE: THE RIPPLES', 3136, [E('line', (150, 245, 1770, 295), None, t='THE TAXABLE GAIN LANDS ON THE TAX RETURN', size=44, col=goldL),
                                             E('vbars', (250, 310, 1670, 710), 'jumps from ninety thousand', vals=[('INCOME BEFORE', 90000, '$90,000', blue), ('INCOME IN THE SALE YEAR', 236000, '$236,000', red)])],
          'INCOME JUMPS FOR ONE YEAR', red, (255, 255, 255), tag=G3, src='IRS PUB 523'),
    slide('MEDICARE LOOKS BACK', 3137, [E('cal', (260, 290, 860, 640), 'medicare generally sets', head='YOUR TAX RETURN', big='YEAR 1', size=110, col=gold, sub='THE INCOME COUNTED'),
                                       E('arrow', (890, 420, 1000, 510), 'two years earlier'),
                                       E('cal', (1030, 290, 1630, 640), 'two years earlier', head='PART B PREMIUM', big='YEAR 3', size=110, col=blue, sub='SET BY THAT INCOME')],
          'PREMIUM USES INCOME 2 YEARS BACK', gold, tag=G3, src='SSA + MEDICARE'),
    slide('THE S S A EXAMPLE', 3138, [E('cal', (260, 290, 860, 640), 'twenty twenty-six premiums', head='TAX RETURN OF', big='2024', size=150, col=gold, sub='THE INCOME COUNTED'),
                                     E('arrow', (890, 420, 1000, 510), 'based on twenty twenty-four'),
                                     E('cal', (1030, 290, 1630, 640), 'based on twenty twenty-four', head='PART B PREMIUMS OF', big='2026', size=150, col=blue, sub='SET BY THAT RETURN')],
          'THE S S A\'S OWN EXAMPLE', gold, tag=G3, src='SSA POMS HI 01101.010'),
]
# ---- 14: IRMAA ----
GR14 = (170, 250, 1750, 560)
S[14] = [
    slide('PART B PREMIUM, 2026', 3139, GRID(GR14, ['JOINT RETURN INCOME', 'PART B PREMIUM'], [0.55, 0.45],
                                                  [['UP TO $218,000', '$202.90'], [('$218,000 TO $274,000', goldL), ('$284.10  (+$81.20)', red)]], ['a joint return above', 'between two hundred eighteen'], first='using the twenty twenty-six', col=gold) +
          [E('rowhl', (170, 250, 1750, 560), 'each person pays', gbox=GR14, nrows=2, i=1)],
          'ABOVE $218,000: PAYS MORE', red, (255, 255, 255), tag=G3, src='CMS 2026 FACT SHEET'),
    slide('RAY AND DONNA: THE EXTRA', 3140, [E('calc', (150, 260, 1770, 410), 'for ray and donna', parts=[('$81.20', white, 56), ('x 2 PEOPLE', goldL, 50), ('x 12', goldL, 56), ('=', white, 56), ('$1,948.80', red, 62)]),
                                           E('big', (350, 450, 1570, 620), 'one thousand nine hundred', val='$1,948.80 EXTRA', sub='FOR THE YEAR', size=90, vcol=red),
                                           CH((300, 640, 1620, 725), 'future brackets', 'FUTURE BRACKETS WILL DIFFER: AN ILLUSTRATION', False, 34)],
          'ONE YEAR OF HIGHER PREMIUMS', red, (255, 255, 255), tag=G3, src='CMS 2026 FACT SHEET'),
]
# ---- 15: SOCIAL SECURITY TAX ----
S[15] = [
    slide('WHEN BENEFITS BECOME TAXABLE', 3141, [E('line', (150, 250, 1770, 300), 'the i r s says', t='THE I R S SAYS', size=46, col=goldL),
                                                E('calc', (150, 330, 1770, 470), 'half of your benefits', parts=[('HALF OF BENEFITS', goldL, 40), ('+', white, 60), ('OTHER INCOME', goldL, 40), ('>', white, 60), ('BASE AMOUNT', red, 44)]),
                                                CH((300, 530, 1620, 640), 'above a base amount', 'ABOVE A BASE AMOUNT, BENEFITS BECOME TAXABLE', False, 38)],
          'THE BASE AMOUNT', gold, tag=G3, src='IRS PUB 915'),
    slide('TWO BASE AMOUNTS', 3163, [E('zonebar', (170, 330, 1750, 460), 'twenty-five thousand for a single', label='SINGLE', t1=25000, t2=25000, mx=60000, z1='UNDER: NOT TAXED', z2='', z3='OVER: TAXABLE', l1='$25,000', l2='', stage=1),
                                    E('zonebar', (170, 520, 1750, 650), 'thirty-two thousand', label='JOINT', t1=32000, t2=32000, mx=60000, z1='UNDER: NOT TAXED', z2='', z3='OVER: TAXABLE', l1='$32,000', l2='', stage=1)],
          'SINGLE $25,000 · JOINT $32,000', gold, tag=G3, src='IRS PUB 915'),
    slide('UP TO 85% TAXABLE', 3142, [E('zonebar', (170, 300, 1750, 450), 'above thirty-four thousand', label='SINGLE', t1=25000, t2=34000, mx=60000, z1='0%', z2='50%', z3='UP TO 85%', l1='$25,000', l2='$34,000'),
                                     E('zonebar', (170, 500, 1750, 650), 'forty-four thousand', label='JOINT', t1=32000, t2=44000, mx=60000, z1='0%', z2='50%', z3='UP TO 85%', l1='$32,000', l2='$44,000')],
          'UP TO 85% OF YOUR BENEFITS', red, (255, 255, 255), tag=G3, src='IRS PUB 915'),
    slide('A BIG GAIN PUSHES YOU HIGHER', 3143, [E('vbars', (350, 255, 1570, 710), 'a big gain can push', vals=[('NORMAL YEAR', 45, 'LESS TAXABLE', blue), ('YEAR OF THE SALE', 100, 'MORE TAXABLE', red)])],
          'THE SALE YEAR RAISES IT', red, (255, 255, 255), tag=G3, src='IRS PUB 915'),
]
# ---- 16: PARTIAL EXCLUSION ----
S[16] = [
    slide('EXCEPTIONS TO THE LIMIT', 3164, [E('big', (170, 270, 1750, 560), 'the first is a partial', val='PARTIAL EXCLUSION', sub='THE FIRST EXCEPTION', size=120, vcol=goldL)],
          'NUMBER FOUR: THE EXCEPTIONS', gold, tag=G4, src='IRS PUB 523'),
    slide('A PARTIAL EXCLUSION', 3144, [E('numcol', R3[0], 'a work move', n=1, icon='brief', l1='A WORK MOVE', l2='', col=gold, s=0.6),
                                       E('numcol', R3[1], 'a health reason', n=2, icon='doc', l1='A HEALTH REASON', l2='', col=green, s=0.6),
                                       E('numcol', R3[2], 'an unforeseeable event', n=3, icon='clock', l1='AN UNFORESEEABLE', l2='EVENT', col=blue, s=0.6)],
          'A PARTIAL EXCLUSION', gold, tag=G4, src='IRS PUB 523'),
    slide('WHAT HEALTH INCLUDES', 3145, [CH((220, 260, 1700, 380), 'moving for treatment', 'MOVING FOR TREATMENT', True, 44), CH((220, 410, 1700, 530), 'caring for a sick family member', 'CARING FOR A SICK FAMILY MEMBER', True, 44),
                                        CH((220, 560, 1700, 680), 'a doctor\'s advice', 'A DOCTOR\'S ADVICE', True, 44)],
          'HEALTH REASONS COUNT', green, tag=G4, src='IRS PUB 523'),
    slide('THE PARTIAL FORMULA', 3146, [E('calc', (150, 260, 1770, 410), 'months lived there', parts=[('MONTHS LIVED', white, 48), ('/ 24', goldL, 56), ('x $250,000', gold, 56)]),
                                       E('calc', (150, 450, 1770, 620), 'twelve months gives', parts=[('12 / 24', white, 64), ('x $250,000', goldL, 56), ('=', white, 60), ('$125,000', green, 70)])],
          '12 MONTHS = $125,000', green, tag=G4, src='IRS PUB 523'),
]
# ---- 17: SURVIVING SPOUSE ----
S[17] = [
    slide('THE SURVIVING SPOUSE', 3147, [E('person', (150, 260, 640, 690), 'suppose ray passes away', letter='D', name='DONNA', line='SURVIVING SPOUSE', col=green),
                                        E('card', (720, 280, 1770, 670), 'decides to sell', head='RAY HAS PASSED AWAY', val='DONNA SELLS', vsize=84, vcol=goldL, col=gold, icon='house', s=0.6)],
          'SECOND: THE SURVIVOR', gold, tag=G4, src='IRS PUB 523'),
    slide('THE TWO-YEAR WINDOW', 3148, [E('wband', (150, 235, 1770, 600), 'within two years of his death', a1='$500,000', a2='SELLS WITHIN 2 YEARS', b1='$250,000', b2='AFTER 2 YEARS', m0='RAY\'S DEATH', m1='2 YEARS LATER', foot=''),
                                       CH((150, 630, 900, 720), 'is not remarried', 'NOT REMARRIED', True, 38), CH((920, 630, 1770, 720), 'count the time ray', 'COUNTS RAY\'S TIME IN THE HOME', True, 34)],
          'WITHIN 2 YEARS: $500,000', green, tag=G4, src='IRS PUB 523'),
    slide('THE DATE MATTERS', 3149, [E('cal', (150, 290, 760, 640), 'after the two years', head='THE DEADLINE', big='2 YEARS', size=130, col=red, sub='AFTER THE DEATH'),
                                    E('card', (850, 290, 1770, 640), 'the limit falls back', head='AFTER THAT', val='$250,000', sub='THE SINGLE AMOUNT', vsize=120, vcol=red, col=red)],
          'THE DATE ON THE CALENDAR MATTERS', red, (255, 255, 255), tag=G4, src='IRS PUB 523'),
]
# ---- 18: STEP-UP FOR THE SURVIVOR ----
S[18] = [
    slide('A NEW BASIS FOR HALF', 3150, [E('card', row(2, y0=290, y1=610)[0], 'for a jointly owned', head='THE SURVIVOR\'S HALF', val='SAME BASIS', vsize=64, vcol=white, col=blue, icon='house', s=0.5),
                                        E('card', row(2, y0=290, y1=610)[1], 'gets a new basis', head='THE HALF OF THE SPOUSE WHO DIED', val='NEW BASIS', sub='= VALUE ON THE DATE OF DEATH', vsize=64, vcol=green, col=green)],
          'BASIS RESETS FOR ONE HALF', green, tag=G4, src='IRS PUB 523'),
    slide('THE I R S EXAMPLE', 3151, [E('card', row(3, y0=300, y1=580)[0], 'a basis of fifty thousand', head='BASIS', val='$50,000', vsize=84, vcol=white, col=blue),
                                     E('card', row(3, y0=300, y1=580)[1], 'is worth one hundred thousand', head='WORTH AT DEATH', val='$100,000', vsize=84, vcol=goldL, col=gold),
                                     E('card', row(3, y0=300, y1=580)[2], 'new basis becomes', head='SURVIVOR\'S NEW BASIS', val='$75,000', vsize=84, vcol=green, col=green)],
          'FROM $50,000 TO $75,000', green, tag=G4, src='IRS PUB 523'),
    slide('COMMUNITY PROPERTY STATES', 3152, [E('big', (150, 260, 780, 680), 'in the nine community', val='9 STATES', sub='COMMUNITY PROPERTY', size=140, vcol=goldL),
                                             E('icard', (860, 260, 1770, 690), 'the whole home usually', icon='house', l1='THE WHOLE HOME', l2='USUALLY GETS THE NEW BASIS', col=green, c2=green, s=0.7)],
          'NINE STATES, WHOLE HOME', green, tag=G4, src='IRS PUB 523'),
]
# ---- 19: YOUR FAMILY ----
S[19] = [
    slide('YOUR FAMILY', 3166, [E('big', (170, 270, 1750, 560), 'number five', val='YOUR FAMILY', sub='THE RULES DEPEND ON HOW THE HOME PASSES ON', size=120, vcol=goldL)],
          'NUMBER FIVE', green, tag=G5, src='IRS PUB 523'),
    slide('IF YOUR CHILDREN INHERIT', 3153, [E('icard', (150, 260, 590, 690), 'if your children inherit', icon='house', l1='THE HOME', l2='WHEN YOU DIE', col=gold, size=46),
                                            E('arrow', (600, 420, 730, 510), 'their basis is its value'),
                                            E('icard', (740, 260, 1180, 690), 'their basis is its value', icon='chart', l1='NEW BASIS', l2='= VALUE THEN', col=green, c2=green, size=46),
                                            E('arrow', (1190, 420, 1320, 510), 'not taxed when'),
                                            E('icard', (1330, 260, 1770, 690), 'not taxed when', icon='check', l1='NOT TAXED', l2='PROFIT BEFORE DEATH', col=green, c2=green, size=46)],
          'NUMBER FIVE: YOUR FAMILY', green, tag=G5, src='IRS PUB 523'),
    slide('IF YOU GIVE THE HOME', 3154, [E('icard', (150, 260, 590, 690), 'but if you give', icon='house', l1='GIFT OF THE HOME', l2='WHILE YOU LIVE', col=gold, size=40),
                                        E('arrow', (600, 420, 730, 510), 'they take your basis'),
                                        E('icard', (740, 260, 1180, 690), 'they take your basis', icon='bag', l1='YOUR BASIS', l2='THEY TAKE IT', col=red, c2=red, size=46),
                                        E('arrow', (1190, 420, 1320, 510), 'as a general rule'),
                                        E('icard', (1330, 260, 1770, 690), 'as a general rule', icon='cross', l1='NO NEW BASIS', l2='GENERAL RULE', col=red, c2=red, size=46)],
          'A GIFT KEEPS YOUR BASIS', red, (255, 255, 255), tag=G5, src='IRS PUB 523'),
    slide('RAY AND DONNA\'S HOME', 3155, [E('card', (150, 280, 940, 600), 'in ray and donna\'s', head='GIFT BASIS', val='$200,000', sub='THEIR BASIS', vsize=96, vcol=red, col=red),
                                         E('card', (980, 280, 1770, 600), 'not nine hundred', head='INHERITED BASIS', val='$900,000', sub='VALUE AT DEATH', vsize=96, vcol=green, col=green),
                                         E('line', (150, 640, 1770, 700), 'a child who never lived', t='A CHILD WHO NEVER LIVED THERE MAY NOT GET THE EXCLUSION', size=40, col=goldL)],
          'GIFT VS INHERITANCE', gold, tag=G5, src='IRS PUB 523'),
]
# ---- 20: CHECKLIST ----
S[20] = [
    slide('BEFORE YOU SIGN', 3156, [E('step', (170, 250, 1750, 380), 'one count your dates', n=1, text='COUNT YOUR DATES', val='YOUR DATES', col=gold),
                                   E('step', (170, 410, 1750, 540), 'two gather your closing', n=2, text='GATHER CLOSING PAPERS AND RECEIPTS', val='YOUR BASIS', col=gold),
                                   E('step', (170, 570, 1750, 700), 'three estimate your gain', n=3, text='ESTIMATE THE GAIN: PUB 523', val='WORKSHEETS', col=gold)],
          'THREE THINGS TO DO FIRST', gold, tag=G6, src='IRS PUB 523'),
    slide('THEN CHECK THE RIPPLES', 3157, [E('step', (170, 270, 1750, 430), 'four check what', n=4, text='CHECK MEDICARE + SOCIAL SECURITY TAX', val='THE RIPPLES', col=gold),
                                          E('step', (170, 480, 1750, 640), 'five the sale date', n=5, text='SALE DATE = USUALLY CLOSING DATE', val='THE TAX YEAR', col=gold)],
          'TWO MORE CHECKS', gold, tag=G6, src='IRS PUB 523'),
]
# ---- 21: RECAP ----
S[21] = [
    slide('RECAP: 1 TO 3', 3158, [E('rule', (170, 250, 1750, 390), 'one owning and living', n=1, text='OWN + LIVE 24 MONTHS IN 5 YEARS', val='$250,000 / $500,000', col=gold),
                                 E('rule', (170, 410, 1750, 550), 'two gain is price', n=2, text='GAIN = PRICE - COSTS - BASIS', val='+ IMPROVEMENTS', col=gold),
                                 E('rule', (170, 570, 1750, 710), 'three a taxable gain', n=3, text='A TAXABLE GAIN', val='MEDICARE + S.S. TAX', col=gold)],
          'THE FIRST THREE FACTS', gold, tag=G6, src='IRS PUB 523'),
    slide('RECAP: 4 AND 5', 3159, [E('rule', (170, 280, 1750, 440), 'four partial and survivor', n=4, text='PARTIAL + SURVIVOR RULES', val='CHANGE THE LIMIT', col=gold),
                                  E('rule', (170, 490, 1750, 650), 'five an inherited home', n=5, text='INHERITED = NEW BASIS', val='GIFT = YOURS', col=gold)],
          'THE LAST TWO FACTS', gold, tag=G6, src='IRS PUB 523'),
]
# ---- 22: CTA + DISCLAIMER ----
def final15(t, seed=215):
    Dd = CUR['D']
    fr = base(t); fr = amb(fr, t, seed, 7, 55); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('General information,', white, 240), ('not tax advice.', white, 296), ('Rules, amounts and ages change', goldL, 372),
             ('and differ by location. Confirm with', goldL, 428), ('the I R S or a tax professional.', white, 504), ('Not affiliated with the I R S,', white, 560), ('Medicare or Social Security.', white, 616)]
    tg = [0.3 + k * (0.58 * Dd - 0.3) / 6 for k in range(7)]
    for (tx, cl, yy), ts in zip(lines, tg):
        if t > ts:
            C = new(); txt(C, tx, BOLD(46), yy, cl, 255, x=650)
            fr = A_(fr, C, (140, yy - 20, 1160, yy + 60), t, ts)
    if t > 0.68 * Dd:
        C = new(); dashed(C, 1220, 280, 1780, 640); txt(C, 'WATCH NEXT', BOLD(56), 430, goldL, 255, x=1500); fr = A_(fr, C, (1200, 260, 1800, 660), t, 0.68 * Dd)
    if t > 0.8 * Dd - 0.4:
        import modello_unico as _m
        C = new(); _m.dashed_circle(C, 260, 860, 85); txt(C, 'SUBSCRIBE', BOLD(44), 835, goldL, 255, x=560); fr = A_(fr, C, (160, 760, 760, 960), t, 0.8 * Dd - 0.4)
    return frame(fr)
S[22] = [
    slide('SEND IT TO SOMEONE', 3160, [E('icard', (500, 260, 1420, 690), None, icon='mail', l1='SOMEONE SELLING', l2='THEIR HOME', col=gold)], 'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 3161, [E('line', (200, 330, 1720, 430), None, t='WOULD YOU SELL,', size=88, col=white), E('line', (200, 470, 1720, 570), 'would you sell', t='OR STAY?', size=88, col=goldL)],
          'ANSWER IN THE COMMENTS'),
    frozen(final15),
]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
CUTS = {1: ['it is easy', 'the i r s allows'], 2: ['long ago', 'now they plan'], 3: ['we will cover'], 4: ['to get it'], 5: ['only one spouse', 'you can use the exclusion', 'and if you cannot care'],
        6: ['take the selling price', 'that gives you', 'then subtract', 'if it is negative'], 7: ['plus improvements', 'it does not include', 'keep your receipts'], 8: ['they sell at', 'subtract the basis', 'their exclusion is'],
        9: ['that is sixty thousand'], 10: ['for twenty twenty-six', 'so ray and donna'], 11: ['ray and donna stay under', 'and if you claim'], 12: ['and if you owe tax'],
        13: ['medicare generally sets', 'the social security administration\'s'], 14: ['for ray and donna'], 15: ['twenty-five thousand for a single', 'above thirty-four', 'a big gain can'], 16: ['if you miss', 'health includes', 'the formula'],
        17: ['if she sells within', 'after the two years'], 18: ['in the i r s example', 'in the nine community'], 19: ['if your children inherit', 'but if you give', 'in ray and donna\'s'], 20: ['four check'],
        21: ['four partial and survivor'], 22: ['and tell me', 'one last thing']}
for _b, _ph in CUTS.items():
    _tot = sum(SPEC[_b]); _c = [0] + [round((V.at(_b, p) - 0.2) * 30) for p in _ph] + [_tot]
    SPEC[_b] = [_c[i + 1] - _c[i] for i in range(len(_c) - 1)]
if os.environ.get('PV'):   # solo anteprima layout dei blocchi senza voce: durate finte uguali (750 fotogrammi = 25 s)
    for _b in SLIDES:
        if not os.path.exists(os.path.join(VID, 'voce', f'b{_b}.wav')): SPEC[_b] = [750 // len(SLIDES[_b])] * len(SLIDES[_b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v15', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
