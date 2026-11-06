"""Video 17 - Piano Medicare Advantage non rinnovato (Gloria) - 16 blocchi. Uso: python3 v17.py render|preview|spec <blocco> [slide,slide]
Sfondo/testata/schede cambiati un po' rispetto al video 16 (v17eng.py), elementi realistici: tessera Medicare, lettera di non rinnovo con busta, calendari veri, flacone Rx, telefono, portatile Plan Finder.
Solo cio' che la voce dice, ogni elemento compare sulla sua parola (max 80%)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v17eng import *
import v17eng

R2 = row(2); R3 = row(3); R4 = row(4, y1=560)
SRC = 'MEDICARE.GOV'
G1, G2, G3, G4, G5 = 'THE LETTER', 'THE DATES', 'THE GAP', 'THE TRAPS', 'WHAT TO DO'
def CH(box, cue, t, good=True, size=40): return E('chip', box, cue, t=t, good=good, ic=(green if good else red), size=size)
def RULE(i, cue, n, text, val, col=gold, vc=goldL, nrows=4, y0=245, y1=720):
    h = (y1 - y0 - 25 * (nrows - 1)) / nrows; yy = y0 + i * (h + 25)
    return E('rule', (170, yy, 1750, yy + h), cue, n=n, text=text, val=val, col=col, vc=vc)
S = {}
# ---- 1: GANCIO ----
S[1] = [
    slide('THE PLAN ENDS', 5101, [E('card', (160, 340, 800, 560), 'if your medicare advantage plan', head='MEDICARE ADVANTAGE PLAN', val='NOT RENEWED', vsize=70, vcol=red, col=red),
                                 E('calpage', (900, 250, 1400, 710), 'ends on december', year=2026, month=12, hl={31: RED2}, ranges=[(1, 30, (60, 90, 140))]),
                                 E('stamp', (1440, 400, 1760, 510), 'thirty-first', t='DEC 31', col=red, ang=-8, size=76)],
          'IT ENDS ON DECEMBER 31', red, (255, 255, 255), tag=G1, src=SRC),
    slide('IF YOU JOIN NOTHING', 5102, [E('planswap', (170, 250, 1750, 640), 'moves you into original medicare', l1='ADVANTAGE PLAN', inside=('HOSPITAL', 'DOCTOR', 'DRUGS'), r1='ORIGINAL MEDICARE', in2=('PART A  HOSPITAL', 'PART B  DOCTOR'), gap='NO DRUG PLAN', col=blue)],
          'YOUR DRUG COVERAGE ENDS TOO', gold, tag=G1, src=SRC),
    slide('THE WARNING', 5103, [E('notice', (150, 250, 800, 700), 'a letter in october', date='OCTOBER 2026'),
                               E('card', (880, 250, 1770, 410), 'second window', head='THE SAME RULES NAME', val='A SECOND WINDOW', vsize=64, vcol=goldL, col=gold),
                               CH((880, 440, 1770, 530), 'its own dates', 'ITS OWN DATES', True, 40),
                               CH((880, 550, 1770, 640), 'its own trap', 'ITS OWN TRAP', False, 40),
                               CH((880, 660, 1770, 750), 'a penalty', 'A PENALTY ADDED PERMANENTLY', False, 40)],
          'A LETTER, A WINDOW, A TRAP', gold, tag=G1, src=SRC),
]
# ---- 2: ISCRIZIONE + GLORIA ----
S[2] = [
    slide('THE MONEY BACKSTORY', 5104, [E('line', (200, 280, 1720, 360), 'where we turn official rules', t='OFFICIAL RULES  >  REAL NUMBERS', size=70, col=goldL),
                                       E('subbtn', (600, 450, 1320, 600), 'subscribe now', t='SUBSCRIBE')],
          'IF THIS HELPS, SUBSCRIBE', gold),
    slide('MEET GLORIA', 5105, [E('person', (160, 250, 640, 690), 'now meet gloria', letter='G', name='GLORIA, 71', line='RETIRED', line2='ADVANTAGE PLAN', col=blue),
                               E('medcard', (720, 270, 1480, 680), 'she has a medicare advantage plan', name='GLORIA SAMPLE', badge='PLUS DRUG COVERAGE')],
          'HER PLAN INCLUDES DRUGS', gold, tag=G1, src=SRC),
    slide('THEN THE LETTER', 5106, [E('notice', (150, 250, 860, 700), 'in october a letter arrives', date='OCTOBER 2026'),
                                   E('card', (940, 280, 1770, 480), 'will leave the medicare program', head='HER PLAN WILL LEAVE', val='MEDICARE NEXT YEAR', vsize=56, vcol=red, col=red),
                                   E('card', (940, 520, 1770, 700), 'the date everyone repeats', head='THE DATE EVERYONE REPEATS', val='DEC 7', vsize=84, vcol=goldL, col=gold)],
          'GLORIA IS ABOUT TO LEARN', gold, tag=G1, src=SRC),
]
# ---- 3: LA LETTERA ----
S[3] = [
    slide('THE PLAN NON-RENEWAL NOTICE', 5107, [E('notice', (150, 250, 800, 700), 'what this letter actually is', head='PLAN NON-RENEWAL NOTICE'),
                                               E('card', (880, 270, 1770, 520), 'medicare calls it', head='MEDICARE CALLS IT', val='NON-RENEWAL NOTICE', vsize=58, vcol=goldL, col=gold, sub='SOURCE: MEDICARE.GOV')],
          'THE NOTICE HAS A NAME', gold, tag=G1, src=SRC),
    slide('WHAT MEDICARE SAYS', 5108, [E('step', (170, 250, 1750, 380), 'you get it if your plan', n=1, text='YOUR PLAN IS LEAVING THE PROGRAM', val='NEXT YEAR', col=gold),
                                      E('step', (170, 410, 1750, 540), 'it comes in october', n=2, text='WHEN IT COMES', val='OCTOBER', col=gold),
                                      E('step', (170, 570, 1750, 700), 'your plan sends it', n=3, text='WHO SENDS IT', val='YOUR PLAN', col=gold)],
          'THREE FACTS ABOUT THE NOTICE', gold, tag=G1, src=SRC),
    slide('THE ONE INSTRUCTION', 5109, [E('big', (170, 250, 1050, 560), 'you must look for a new plan', val='MUST', sub='LOOK FOR A NEW PLAN', size=240, vcol=goldL),
                                       CH((1100, 290, 1770, 390), 'not may', 'NOT "MAY"', False, 46),
                                       CH((1100, 420, 1770, 520), 'advertisement', 'NOT AN ADVERTISEMENT', False, 40),
                                       CH((1100, 550, 1770, 650), 'reminder', 'NOT A REMINDER', False, 40)],
          'IT IS THE START OF A DEADLINE', red, (255, 255, 255), tag=G1, src=SRC),
]
# ---- 4: QUADRO NAZIONALE ----
S[4] = [
    slide('THE NATIONAL PICTURE', 5110, [E('card', (160, 310, 620, 560), 'number of advantage plans', head='ADVANTAGE PLANS, THIS YEAR', val='5,553', vsize=130, vcol=white, col=blue),
                                        E('arrow', (640, 380, 770, 490), 'to about'),
                                        E('card', (790, 310, 1250, 560), 'next year', head='ABOUT, NEXT YEAR', val='5,532', vsize=130, vcol=goldL, col=gold),
                                        E('stamp', (1330, 390, 1750, 490), 'september twenty-eighth', t='CMS  SEP 28', col=blue, ang=6, size=60)],
          'THE NUMBER BARELY MOVES', gold, tag=G1, src='CMS.GOV'),
    slide('STAY IN YOUR PLAN', 5111, [E('pictos', (170, 250, 1750, 690), 'about eight in ten', n=10, hi=8, l1='ABOUT 8 IN 10 CAN STAY IN THEIR CURRENT PLAN', l2='WITH THE SAME OR A LOWER PREMIUM')],
          'CMS: 8 IN 10 STAY', green, navy, tag=G1, src='CMS.GOV'),
    slide('YOUR OWN LETTER', 5112, [E('card', (160, 270, 860, 560), 'a national average', head='A NATIONAL AVERAGE', val='ONE NUMBER', vsize=84, vcol=white, col=grey, sub='CANNOT TELL YOU ABOUT YOUR PLAN'),
                                   E('notice', (950, 250, 1750, 700), 'only your own letter', head='PLAN NON-RENEWAL NOTICE')],
          'ONLY YOUR LETTER CAN TELL YOU', gold, tag=G1, src='CMS.GOV'),
]
# ---- 5: LE DATE ----
S[5] = [
    slide('THE ORDINARY WINDOW', 5113, [E('dtl', (150, 240, 1770, 640), 'open enrollment runs', zones=[(0, 53, green, 'OPEN ENROLLMENT')], marks=[(0, 'OCT 15', 'START', goldL), (53, 'DEC 7', 'END', red)], mx=62),
                                       E('card', (1200, 560, 1770, 720), 'start on january first', head='CHANGES START', val='JAN 1', vsize=70, vcol=goldL, col=gold)],
          'THE DATE EVERYONE REPEATS', gold, tag=G2, src=SRC),
    slide('THE SECOND WINDOW', 5114, [E('calpage', (150, 250, 760, 720), 'a second window', year=2026, month=12, hl={7: RED2}, ranges=[(1, 6, (60, 90, 140)), (8, 31, GRN2)]),
                                     E('card', (860, 260, 1770, 420), 'it opens on december eighth', head='IT OPENS', val='DEC 8', vsize=84, vcol=goldL, col=green),
                                     E('card', (860, 460, 1770, 620), 'closes on the last day', head='IT CLOSES', val='LAST DAY OF FEBRUARY', vsize=50, vcol=goldL, col=green)],
          'FOR PLANS THAT WILL NOT CONTINUE', green, navy, tag=G2, src=SRC),
    slide('NOT THE END OF THE ROAD', 5115, [E('card', (160, 280, 760, 600), 'december seventh is not', head='DEC 7', val='ORDINARY', vsize=84, vcol=white, col=grey, sub='THE END OF THE ORDINARY WINDOW'),
                                           E('arrow', (790, 400, 940, 490), 'the end of the ordinary window'),
                                           E('card', (970, 280, 1770, 600), 'for gloria', head='THE SECOND WINDOW', val='STILL OPEN', vsize=84, vcol=goldL, col=green, sub='UNTIL THE LAST DAY OF FEBRUARY')],
          'DECEMBER 7 IS NOT YOUR LAST CHANCE', gold, tag=G2, src=SRC),
]
# ---- 6: DATE DI INIZIO ----
S[6] = [
    slide('WHEN IT STARTS', 5116, [E('rule', (170, 250, 1750, 380), 'received from december eighth', n=1, text='REQUEST: DEC 8 - DEC 31', val='STARTS JAN 1', col=green, vc=goldL),
                                  E('rule', (170, 410, 1750, 540), 'received in january', n=2, text='REQUEST: IN JANUARY', val='STARTS FEB 1', col=gold, vc=goldL),
                                  E('rule', (170, 570, 1750, 700), 'received in february', n=3, text='REQUEST: IN FEBRUARY', val='STARTS MAR 1', col=red, vc=goldL)],
          'THE LATER YOU ASK, THE LATER IT STARTS', gold, tag=G2, src='CMS.GOV'),
    slide('GLORIA MAY WAIT', 5117, [E('card', (160, 280, 860, 600), 'gloria is allowed to wait', head='GLORIA MAY WAIT', val='ALLOWED', vsize=96, vcol=green, col=green, sub='THE WINDOW STAYS OPEN'),
                                   E('card', (940, 280, 1770, 600), 'every month she waits', head='EVERY MONTH SHE WAITS', val='NO ADVANTAGE PLAN', vsize=54, vcol=red, col=red, sub='ANOTHER MONTH WITHOUT ONE')],
          'WAITING HAS A COST', red, (255, 255, 255), tag=G2, src='CMS.GOV'),
]
# ---- 7: IL DEFAULT ----
S[7] = [
    slide('THE DEFAULT', 5118, [E('planswap', (170, 250, 1750, 640), 'you will be enrolled in original medicare', l1='YOUR ADVANTAGE PLAN', inside=('HOSPITAL', 'DOCTOR', 'DRUGS'), r1='ORIGINAL MEDICARE', in2=('PART A  HOSPITAL', 'PART B  DOCTOR'), gap='NO DRUG PLAN', col=blue)],
          'JOIN NOTHING: ORIGINAL MEDICARE', red, (255, 255, 255), tag=G3, src=SRC),
    slide('ORIGINAL MEDICARE', 5119, [E('card', (160, 270, 640, 600), 'part a', head='PART A', val='HOSPITAL', vsize=64, vcol=white, col=blue),
                                     E('card', (700, 270, 1180, 600), 'and part b', head='PART B', val='DOCTOR', vsize=64, vcol=white, col=blue),
                                     E('card', (1240, 270, 1770, 600), 'drug coverage is not inside', head='DRUG COVERAGE', val='NOT INSIDE', vsize=60, vcol=red, col=red, sub='A SEPARATE PLAN'),
                                     CH((560, 630, 1360, 720), 'a separate plan that you join', 'YOU JOIN IT YOURSELF', True, 42)],
          'DRUGS ARE A SEPARATE PLAN', gold, tag=G3, src=SRC),
    slide('IF GLORIA DOES NOTHING', 5120, [E('medcard', (160, 250, 880, 650), 'if gloria does nothing', name='GLORIA SAMPLE', badge='JAN 1'),
                                          E('rx', (1000, 250, 1300, 650), 'and no drug plan', l1='YOUR DRUGS', l2='NO PLAN'),
                                          E('stamp', (1300, 500, 1740, 600), 'no drug plan', t='NO DRUGS', col=red, ang=-8, size=72)],
          'JANUARY 1: NO DRUG PLAN', red, (255, 255, 255), tag=G3, src=SRC),
]
# ---- 8: PENALE PART D ----
S[8] = [
    slide('THE PART D PENALTY', 5121, [E('card', (160, 340, 860, 560), 'a part d late enrollment penalty', head='PART D', val='LATE ENROLLMENT PENALTY', vsize=50, vcol=red, col=red),
                                      E('ring', (950, 250, 1330, 650), 'sixty-three days', val='63', sub='DAYS IN A ROW', size=130, frac=1.0, col=red),
                                      E('rx', (1420, 270, 1700, 620), 'without medicare drug coverage', l1='NO DRUG', l2='COVERAGE')],
          'SIXTY-THREE DAYS IN A ROW', red, (255, 255, 255), tag=G3, src=SRC),
    slide('THE FORMULA', 5122, [E('card', (160, 290, 520, 590), 'one percent', head='RATE', val='1%', vsize=140, vcol=goldL, col=gold, sub='PER MONTH'),
                               E('op', (530, 380, 620, 500), None, t='x', size=100),
                               E('card', (630, 290, 1170, 590), 'national base beneficiary premium', head='NATIONAL BASE PREMIUM', val='$38.99', vsize=110, vcol=white, col=blue, sub='LISTED FOR 2026'),
                               E('op', (1180, 380, 1270, 500), None, t='x', size=100),
                               E('card', (1280, 290, 1770, 590), 'each full month without coverage', head='EACH FULL MONTH', val='UNCOVERED', vsize=62, vcol=red, col=red, sub='WITHOUT DRUG COVERAGE')],
          'ONE PERCENT, TIMES THE BASE PREMIUM', gold, tag=G3, src=SRC),
    slide('ADDED PERMANENTLY', 5123, [E('card', (160, 280, 900, 600), 'added to your premium', head='ADDED TO YOUR PREMIUM', val='EVERY MONTH', vsize=84, vcol=goldL, col=gold, sub='ON TOP OF THE PLAN PRICE'),
                                     E('stamp', (1000, 360, 1740, 500), 'permanently', t='PERMANENT', col=red, ang=-6, size=90),
                                     CH((1000, 560, 1750, 650), 'for as long as you have', 'FOR AS LONG AS YOU HAVE DRUG COVERAGE', False, 34)],
          'MEDICARE SAYS: PERMANENTLY', red, (255, 255, 255), tag=G3, src=SRC),
]
# ---- 9: CONTA DEI GIORNI ----
S[9] = [
    slide('COUNT THE DAYS', 5124, [E('card', (160, 330, 760, 570), 'coverage stops at the end of december', head='COVERAGE STOPS', val='DEC 31', vsize=100, vcol=red, col=red),
                                  E('arrow', (790, 380, 940, 490), 'joins a drug plan'),
                                  E('card', (970, 330, 1770, 570), 'starts on march first', head='DRUG PLAN STARTS', val='MAR 1', vsize=100, vcol=green, col=green)],
          'GLORIA JOINS A DRUG PLAN FOR MARCH 1', gold, tag=G3, src=SRC),
    slide('JANUARY + FEBRUARY', 5125, [E('calpage', (150, 250, 640, 700), 'january has thirty-one', year=2027, month=1, ranges=[(1, 31, (255, 170, 60))], hc=BLU2),
                                      E('calpage', (680, 250, 1170, 700), 'and february has twenty-eight', year=2027, month=2, ranges=[(1, 28, (255, 170, 60))], hc=BLU2),
                                      E('card', (1230, 330, 1770, 620), 'so the gap is fifty-nine', head='THE GAP', val='59 DAYS', vsize=110, vcol=goldL, col=gold, sub='31 + 28')],
          'THE GAP IS 59 DAYS', gold, tag=G3, src=SRC),
    slide('UNDER THE LINE', 5126, [E('daybar', (170, 250, 1750, 640), 'that is under the', total=63, used=59, line=63, mark='63-DAY LINE', cnt='59 DAYS', months=[(0, 31, 'JANUARY', gold), (31, 59, 'FEBRUARY', gold)])],
          'UNDER THE SIXTY-THREE DAY LINE', green, navy, tag=G3, src=SRC),
    slide('MEDICARE\'S OWN EXAMPLE', 5127, [E('card', (160, 330, 640, 560), 'fourteen months without coverage', head='WITHOUT COVERAGE', val='14 MONTHS', vsize=70, vcol=white, col=red),
                                           E('arrow', (670, 400, 800, 490), 'you owe'),
                                           E('card', (830, 280, 1310, 600), 'fourteen percent penalty', head='PENALTY', val='14%', vsize=140, vcol=red, col=red, sub='ON TOP OF THE PREMIUM'),
                                           CH((1340, 340, 1770, 470), 'who get extra help', 'EXTRA HELP: NO PENALTY', True, 28)],
          'CROSS THE LINE: 14 MONTHS = 14%', red, (255, 255, 255), tag=G3, src=SRC),
]
# ---- 10: CONSOLIDAMENTO ----
S[10] = [
    slide('NOT EVERY CHANGE IS THE SAME', 5128, [E('merge', (170, 260, 1750, 680), 'merged into another plan', left=[('YOUR PLAN', blue), ('ANOTHER PLAN', gold)], right='ONE MERGED PLAN', right2='A CONSOLIDATION', col=gold)],
          'A MERGER IS NOT A NON-RENEWAL', gold, tag=G4, src='CMS.GOV'),
    slide('READ THE WORDING', 5129, [E('sample', (170, 250, 1750, 640), 'leaving the medicare program', items=[('LEAVING THE MEDICARE PROGRAM:  SPECIAL WINDOW', True), ('MOVED INTO A DIFFERENT PLAN:  ORDINARY DATES', False)], size=44)],
          'READ THE WORDING OF YOUR LETTER', gold, tag=G4, src='CMS.GOV'),
]
# ---- 11: AVVISO BLU EXTRA HELP ----
S[11] = [
    slide('THE BLUE NOTICE', 5130, [E('bluenotice', (160, 250, 760, 700), 'a second letter', t='BLUE NOTICE'),
                                   E('card', (840, 270, 1770, 430), 'if you get extra help', head='IF YOU GET', val='EXTRA HELP', vsize=76, vcol=goldL, col=blue),
                                   E('card', (840, 470, 1770, 640), 'late october or early november', head='IT ARRIVES', val='LATE OCT / EARLY NOV', vsize=54, vcol=white, col=gold)],
          'A SECOND LETTER, IN BLUE', gold, tag=G4, src=SRC),
    slide('IF YOU CHOOSE NOTHING', 5131, [E('card', (160, 270, 760, 560), 'reassign you', head='IF YOU CHOOSE NOTHING', val='REASSIGNED', vsize=70, vcol=red, col=red, sub='TO A MEDICARE DRUG PLAN'),
                                         E('step', (840, 270, 1770, 370), 'keep the notice', n=1, text='KEEP THE NOTICE', col=gold),
                                         E('step', (840, 400, 1770, 500), 'compare plans', n=2, text='COMPARE PLANS', col=gold),
                                         E('step', (840, 530, 1770, 630), 'change in early december', n=3, text='CHANGE IN EARLY DECEMBER', col=gold)],
          'MEDICARE\'S ADVICE: KEEP, COMPARE, CHANGE', gold, tag=G4, src=SRC),
]
# ---- 12: PASSO 1 ----
S[12] = [
    slide('STEP 1: FIND THE DATE', 5132, [E('card', (160, 280, 560, 560), 'step one', head='STEP', val='1', vsize=170, vcol=goldL, col=gold, sub='FIND THE DATE'),
                                         E('notice', (640, 250, 1280, 700), 'the effective date', head='PLAN NON-RENEWAL NOTICE', stamp='END DATE + OTHER OPTIONS'),
                                         E('card', (1340, 300, 1770, 620), 'a description of other ways', head='THE PLAN MUST GIVE', val='THE DATE', vsize=64, vcol=white, col=blue, sub='+ OTHER WAYS TO GET COVERAGE')],
          'THE RULES REQUIRE IT', gold, tag=G5, src='CMS.GOV'),
    slide('STILL UNCLEAR? CALL', 5133, [E('card', (160, 330, 760, 560), 'call your plan', head='IF THE DATE IS UNCLEAR', val='CALL YOUR PLAN', vsize=66, vcol=white, col=gold),
                                       E('phone17', (900, 240, 1250, 720), 'one eight hundred medicare', top='CALLING', num='1-800-MEDICARE', num2='24 / 7'),
                                       E('card', (1330, 300, 1770, 620), 'twenty-four hours a day', head='OPEN', val='24 / 7', vsize=110, vcol=goldL, col=green, sub='EVERY DAY')],
          'CALL YOUR PLAN OR 1-800-MEDICARE', gold, tag=G5, src='CMS.GOV'),
]
# ---- 13: PASSO 2 ----
S[13] = [
    slide('STEP 2: COMPARE', 5134, [E('laptop', (150, 250, 1000, 720), 'the medicare plan finder', bar='MEDICARE PLAN FINDER', rows=[('YOUR DOCTORS', True), ('YOUR DRUGS', True), ('PREMIUMS AND COSTS', True), ('BENEFITS', True)]),
                                   E('card', (1080, 320, 1770, 590), 'including premiums costs and benefits', head='COMPARE', val='HEALTH + DRUG PLANS', vsize=44, vcol=goldL, col=gold, sub='ON MEDICARE.GOV')],
          'COMPARE BEFORE YOU PICK', gold, tag=G5, src='MEDICARE.GOV'),
    slide('WHAT IT NOW SHOWS', 5135, [E('sample', (170, 250, 1100, 640), 'save your doctors', items=[('SAVE YOUR DOCTORS', True), ('DRUG LIST + SUMMARY OF BENEFITS', True), ('CHANGES TO YOUR CURRENT PLAN FOR 2027', True)], size=40),
                                     E('rx', (1300, 270, 1580, 620), 'check her doctors and her drugs', l1='YOUR DRUGS', l2='IN ONE SITTING')],
          'GLORIA CHECKS IN ONE SITTING', gold, tag=G5, src='CMS.GOV'),
]
# ---- 14: PASSO 3 ----
S[14] = [
    slide('STEP 3: ORIGINAL MEDICARE?', 5136, [E('rule', (170, 250, 1750, 380), 'she must add a drug plan', n=1, text='ADD A DRUG PLAN', val='YOURSELF', col=gold),
                                              E('rule', (170, 410, 1750, 540), 'a medigap policy is a separate', n=2, text='MEDIGAP', val='SEPARATE DECISION', col=gold),
                                              CH((400, 590, 1520, 690), 'its own rules', 'IT HAS ITS OWN RULES', True, 44)],
          'IF GLORIA WANTS ORIGINAL MEDICARE', gold, tag=G5, src=SRC),
    slide('MEDIGAP TIMING', 5137, [E('dtl', (150, 240, 1770, 660), 'sixty days before', zones=[(0, 60, gold, '60 DAYS BEFORE'), (60, 123, green, 'UP TO 63 DAYS AFTER')], marks=[(60, 'COVERAGE ENDS', '', red)], mx=123),
                                  CH((900, 640, 1770, 720), 'your state may give you more', 'YOUR STATE MAY GIVE MORE TIME', True, 36)],
          'MEDICARE: 60 BEFORE TO 63 AFTER', gold, tag=G5, src=SRC),
    slide('KEEP EVERY LETTER', 5138, [E('folder', (200, 260, 780, 640), 'keep every letter', l1='LETTERS', l2='FROM YOUR PLAN'),
                                     E('card', (900, 340, 1770, 560), 'prove when the coverage ended', head='YOU MAY NEED THEM', val='TO PROVE THE END DATE', vsize=46, vcol=goldL, col=gold)],
          'KEEP PROOF OF THE END DATE', gold, tag=G5, src=SRC),
]
# ---- 15: RIEPILOGO ----
S[15] = [
    slide('FIVE FACTS (1 - 2)', 5139, [RULE(0, 'a non-renewal letter arrives', 1, 'THE LETTER COMES IN OCTOBER', 'YOU HAVE TO FIND A PLAN', nrows=2, y0=260, y1=700),
                                      RULE(1, 'december seventh is the ordinary', 2, 'DEC 7 IS ORDINARY. A 2ND WINDOW', 'ENDS IN FEBRUARY', nrows=2, y0=260, y1=700)],
          'FACTS 1 AND 2', gold, tag='RECAP', src=SRC),
    slide('FIVE FACTS (3 - 5)', 5140, [RULE(0, 'join nothing', 3, 'JOIN NOTHING', 'ORIGINAL MEDICARE', nrows=3, y0=250, y1=710),
                                      RULE(1, 'original medicare has no drug plan', 4, 'NO DRUG PLAN + 63 DAYS', 'CAN START A PENALTY', col=red, nrows=3, y0=250, y1=710),
                                      RULE(2, 'a merged plan', 5, 'A MERGED PLAN', 'IS NOT A NON-RENEWAL', nrows=3, y0=250, y1=710)],
          'FACTS 3, 4 AND 5', gold, tag='RECAP', src=SRC),
]
# ---- 16: CTA + FINALE ----
def final17(t, seed=217):
    Dd = CUR['D']
    fr = v17eng.base17(t); fr = amb(fr, t, seed, 5, 40); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('General information,', white, 240), ('not insurance advice.', white, 296), ('Rules and plans differ by plan', goldL, 372),
             ('and by state. Confirm with Medicare', goldL, 428), ('or your plan before you act.', white, 504), ('Not affiliated with Medicare', white, 560), ('or any government agency.', white, 616)]
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
S[16] = [
    slide('SEND IT TO SOMEONE', 5141, [E('icard', (500, 260, 1420, 690), 'send it to someone', icon='mail', l1='SOMEONE WITH', l2='AN ADVANTAGE PLAN', col=gold)], 'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 5142, [E('line', (200, 310, 1720, 410), 'tell me in the comments', t='WHICH DATE', size=88, col=white), E('line', (200, 450, 1720, 550), 'surprised you', t='SURPRISED YOU?', size=88, col=goldL)],
          'ANSWER IN THE COMMENTS'),
    frozen(final17),
]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
CUTS = {}
def _clause_starts(b):
    ws = V.words(b); s0 = V.start(b)
    return [ws[i][1] - s0 for i in range(1, len(ws)) if ws[i - 1][0][-1:] in ',.;:?!']
for _b in SLIDES:
    _tot = sum(SPEC[_b]); n = len(SLIDES[_b]); auto = []
    for i in range(1, n):
        els = getattr(SLIDES[_b][i], 'els', None) or []; cue = els[0]['cue'] if els else None
        if cue is None: auto.append(round(_tot * i / n)); continue
        t = V.at(_b, cue); cand = [x for x in _clause_starts(_b) if t - 1.4 <= x <= t + 0.1]
        c = max(cand) if cand else t - 0.1
        auto.append(round((c - 0.15) * 30))
    _c = [0] + auto + [_tot]
    if min(_c[k + 1] - _c[k] for k in range(len(_c) - 1)) < 72: _c = [round(_tot * k / n) for k in range(n + 1)]
    SPEC[_b] = [_c[k + 1] - _c[k] for k in range(len(_c) - 1)]
if os.environ.get('PV'):
    for _b in SLIDES:
        if not os.path.exists(os.path.join(VID, 'voce', f'b{_b}.wav')): SPEC[_b] = [750 // len(SLIDES[_b])] * len(SLIDES[_b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v17', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
