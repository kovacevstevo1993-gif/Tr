"""Video 14 - Medigap / Plan G - 18 blocchi. Uso: python3 v14m.py render|preview|check|spec <blocco> [slide,slide]  (PV=1: durate finte per blocchi senza voce)
Layout nuovi rispetto ai video 8-13: tessere dei piani A-N con il G evidenziato, freccia a senso unico, sei mesi della finestra, pannelli del prezzo con mini grafico, chip con spunta/croce."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medeng import *

R2 = row(2); R3 = row(3); R4 = row(4, gap=36); R3b = row(3, y1=620); R3c = row(3, y0=335, y1=700); R3d = row(3, y0=325, y1=705); R2c = row(2, y0=335, y1=705)
SRC = 'MEDICARE.GOV'
G1, G2, G3, G4, G5, G6, G7 = 'THE BASICS', 'PLAN G', 'THE COST', 'THE WINDOW', 'BEN\'S RIGHTS', 'YOUR PLAN', 'RECAP'
def CH(box, cue, t, good=True, size=40): return E('chip', box, cue, t=t, good=good, ic=(green if good else red), size=size)
S = {}
# ---- 1: HOOK ----
S[1] = [
    slide('OPEN ENROLLMENT ENDS DEC 7', 2401, [E('cal', (150, 250, 900, 700), 'open enrollment ends', head='OPEN ENROLLMENT ENDS', big='DEC 7', size=190, col=red),
                                              E('card', (960, 270, 1770, 690), 'hard to undo', head='ONE CHOICE THIS FALL', val='HARD TO UNDO', vsize=62, vcol=red, col=red, icon='lock', s=0.7)],
          'ONE CHOICE CAN BE HARD TO UNDO', red, (255, 255, 255), src=SRC),
    slide('ADVANTAGE OR MEDIGAP?', 2402, [E('vs', (150, 260, 1770, 690), 'it is the choice', cols=[('OPTION 1', 'ADVANTAGE', 'MEDICARE ADVANTAGE', blue), ('OPTION 2', 'MEDIGAP', 'A MEDIGAP PLAN', gold)], size=84)],
          'THE CHOICE', gold, src=SRC),
    slide('DROP MEDIGAP, JOIN ADVANTAGE', 2403, [E('line', (150, 245, 1770, 300), 'medicare itself warns', t='MEDICARE ITSELF WARNS', size=52, col=goldL),
                                              E('oneway', (150, 312, 1770, 610), 'if you drop', l1='MEDIGAP', l2='ADVANTAGE', fwd='DROP IT AND JOIN', back='MAY NOT GET IT BACK', c1=gold, c2=blue),
                                              CH((330, 640, 1590, 740), 'any medigap policy', 'IN SOME CASES: NO MEDIGAP POLICY AT ALL', False, 38)],
          'HERE IS WHAT THE OFFICIAL RULES SAY', red, (255, 255, 255), src=SRC),
]
# ---- 2: MEET ----
S[2] = [
    slide('MEET CAROL', 2404, [E('person', (150, 250, 640, 700), None, letter='C', name='CAROL', line='TURNS 65 THIS SPRING', col=green),
                              E('card', (720, 270, 1770, 690), 'very first', head='HER FIRST MEDICARE COVERAGE', val='A BIG CHOICE', vsize=84, vcol=green, col=green, icon='form', s=0.7)],
          'ABOUT TO CHOOSE', green, src=SRC),
    slide('MEET BEN', 2405, [E('person', (150, 250, 640, 700), None, letter='B', name='BEN, 68', line='MEDICARE ADVANTAGE', col=blue),
                            E('card', (720, 270, 1770, 690), 'wondering whether', head='HE IS WONDERING ABOUT', val='ORIGINAL MEDICARE + MEDIGAP', vsize=54, vcol=goldL, col=gold, icon='chart', s=0.7)],
          'THINKING OF SWITCHING', gold, src=SRC),
    slide('RULES LEARNED TOO LATE', 2406, [E('icard', (400, 260, 1520, 690), 'both of them', icon='doc', l1='RULES MOST PEOPLE LEARN', l2='AFTER IT IS TOO LATE', col=red, c2=red)],
          'LEARN THEM NOW', red, (255, 255, 255), src=SRC),
]
# ---- 3: SOURCES ----
S[3] = [
    slide('EVERY FACT IS OFFICIAL', 2407, [E('line', (150, 245, 1770, 305), 'every fact in this', t='EVERY FACT COMES FROM OFFICIAL SOURCES', size=48, col=goldL),
                                          E('icard', R3c[0], 'the government guide', icon='doc', l1='CHOOSING A', l2='MEDIGAP POLICY', col=gold),
                                          E('icard', R3c[1], 'the medicare website', icon='phone', l1='MEDICARE.GOV', l2='THE OFFICIAL SITE', col=gold),
                                          E('icard', R3c[2], 'centers for medicare', icon='bank', l1='CMS.GOV', l2='MEDICARE AND MEDICAID', col=gold)],
          'OFFICIAL SOURCES ONLY', gold, src=SRC),
    slide('NO SALES PAGES', 2408, [E('chip', (200, 290, 940, 410), 'no sales pages', t='SALES PAGES', good=False, ic=red),
                                  E('chip', (200, 450, 940, 570), 'no insurance agents', t='INSURANCE AGENTS', good=False, ic=red),
                                  E('big', (1000, 270, 1770, 620), 'first what medigap', val='MEDIGAP?', sub='FIRST, WHAT IT ACTUALLY IS', size=140, vcol=goldL)],
          'FIRST, WHAT MEDIGAP IS', gold, src=SRC),
]
# ---- 4: WHAT IS MEDIGAP ----
S[4] = [
    slide('MEDICARE SUPPLEMENT INSURANCE', 2409, [E('big', (150, 250, 900, 620), 'medigap officially', val='MEDIGAP', sub='MEDICARE SUPPLEMENT INSURANCE', size=170, vcol=goldL),
                                                E('icard', (980, 270, 1770, 690), 'extra insurance', icon='bank', l1='EXTRA INSURANCE', l2='FROM A PRIVATE COMPANY', col=gold)],
          'SOLD BY PRIVATE COMPANIES', gold, tag=G1, src=SRC),
    slide('WHAT YOU STILL OWE', 2410, [E('line', (150, 245, 1770, 305), 'original medicare which', t='ORIGINAL MEDICARE = PART A + PART B', size=50, col=goldL),
                                      E('icard', R3c[0], 'deductibles', icon='bill', l1='DEDUCTIBLES', l2='YOU STILL OWE', col=red, c2=red),
                                      E('icard', R3c[1], 'coinsurance', icon='coins', l1='COINSURANCE', l2='YOU STILL OWE', col=red, c2=red),
                                      E('icard', R3c[2], 'and copayments', icon='wallet', l1='COPAYMENTS', l2='YOU STILL OWE', col=red, c2=red)],
          'ORIGINAL MEDICARE: PART A + PART B', red, (255, 255, 255), tag=G1, src=SRC),
    slide('MEDIGAP PAYS YOUR SHARE', 2411, [E('icard', (150, 260, 800, 690), 'medigap helps', icon='bank', l1='MEDIGAP', l2='HELPS PAY', col=gold),
                                           E('arrow', (840, 400, 1040, 540), 'your share', col=goldL),
                                           E('icard', (1080, 260, 1770, 690), 'those costs', icon='wallet', l1='YOUR SHARE', l2='OF THOSE COSTS', col=green, c2=green)],
          'THE GAP IT FILLS', green, tag=G1, src=SRC),
    slide('MEDICARE PAYS NOTHING', 2412, [E('big', (150, 250, 1770, 560), 'and medicare itself', val='$0', sub='MEDICARE PAYS TOWARD THE COST OF THE POLICY', size=230, vcol=red),
                                         E('line', (150, 620, 1770, 680), 'buying a medigap', t='YOU BUY IT FROM THE PRIVATE COMPANY', size=48, col=goldL)],
          'MEDICARE DOES NOT PAY FOR THE POLICY', red, (255, 255, 255), tag=G1, src=SRC),
]
# ---- 5: STANDARDIZED ----
S[5] = [
    slide('STANDARDIZED PLANS', 2413, [E('plans', (150, 330, 1770, 560), 'in most states', letters=list('ABCDFGKLMN'), hi='G', cap='NAMED BY LETTERS IN MOST STATES')],
          'PLANS A, B, C, D, F, G, K, L, M, N', gold, tag=G1, src=SRC),
    slide('SAME LETTER, SAME BENEFITS', 2414, [E('vs', (150, 250, 1770, 570), 'all plans with the same', cols=[('COMPANY X', 'PLAN G', 'SAME BENEFITS', gold), ('COMPANY Y', 'PLAN G', 'SAME BENEFITS', gold)], size=110),
                                              CH((330, 610, 1590, 710), 'massachusetts', 'EXCEPTIONS: MASSACHUSETTS, MINNESOTA, WISCONSIN', False, 36)],
          'NO MATTER WHICH COMPANY', gold, tag=G1, src=SRC),
    slide('ONLY THE PRICE DIFFERS', 2415, [E('big', (150, 250, 1000, 560), 'only difference', val='PRICE', sub='THE ONLY DIFFERENCE', size=190, vcol=goldL),
                                          CH((1040, 290, 1770, 410), 'compare plan g with plan g', 'PLAN G VS PLAN G', True, 38),
                                          CH((1040, 450, 1770, 570), 'not with plan n', 'PLAN G VS PLAN N', False, 38)],
          'COMPARE THE SAME LETTER', green, tag=G1, src=SRC),
]
# ---- 6: PLAN G COVERS ----
S[6] = [
    slide('PLAN G COVERS', 2416, [E('idcard', (150, 260, 780, 690), 'let us look', plan='G', col=gold),
                                 CH((820, 270, 1770, 440), 'part a coinsurance', 'PART A COINSURANCE + HOSPITAL COSTS', True, 38),
                                 CH((820, 480, 1770, 650), 'additional three hundred', 'UP TO 365 EXTRA DAYS', True, 40)],
          'THE HOSPITAL COSTS', green, tag=G2, src=SRC),
    slide('PLAN G ALSO COVERS', 2417, [CH((150, 260, 940, 400), 'part b coinsurance', 'PART B COINSURANCE OR COPAY', True, 36), CH((980, 260, 1770, 400), 'first three pints', 'FIRST 3 PINTS OF BLOOD', True, 36),
                                      CH((150, 440, 940, 580), 'hospice coinsurance', 'HOSPICE COINSURANCE', True, 38), CH((980, 440, 1770, 580), 'skilled nursing facility', 'SKILLED NURSING COINSURANCE', True, 36)],
          'DOCTOR, BLOOD, HOSPICE, NURSING', green, tag=G2, src=SRC),
    slide('PLUS THREE MORE', 2418, [CH((150, 260, 940, 400), 'the part a deductible', 'PART A DEDUCTIBLE', True, 40), CH((980, 260, 1770, 400), 'part b excess charges', 'PART B EXCESS CHARGES', True, 40),
                                   E('card', (460, 440, 1460, 690), 'foreign travel emergency', head='FOREIGN TRAVEL EMERGENCY', val='80%', vsize=110, vcol=goldL, col=gold)],
          'WHAT PLAN G COVERS', green, tag=G2, src=SRC),
]
# ---- 7: NOT COVERED ----
S[7] = [
    slide('PLAN G DOES NOT COVER THIS', 2419, [CH((1040, 340, 1770, 500), 'now what plan g', 'NOT COVERED BY PLAN G', False, 40),
                                              E('big', (150, 250, 1000, 600), 'two hundred eighty-three', val='$283', sub='PART B DEDUCTIBLE IN 2026', size=210, vcol=red)],
          'THE PART B DEDUCTIBLE', red, (255, 255, 255), tag=G2, src='CMS.GOV'),
    slide('NEW TO MEDICARE IN 2020 OR LATER', 2420, [E('cal', (150, 260, 860, 690), 'medigap plans sold', head='NEW TO MEDICARE ON OR AFTER', big='JAN 1, 2020', size=100, col=gold),
                                                    E('card', (920, 270, 1770, 690), 'not allowed', head='MEDIGAP PLANS', val='CANNOT COVER THE PART B DEDUCTIBLE', vsize=46, vcol=red, col=red, icon='cross', s=0.7)],
          'A RULE SINCE 2020', gold, tag=G2, src=SRC),
    slide('PLANS C AND F ARE CLOSED', 2421, [E('vs', (150, 260, 1770, 690), 'that is why', cols=[('CLOSED TO NEW PEOPLE', 'C + F', 'NO LONGER SOLD TO THEM', red), ('THEY CAN BUY INSTEAD', 'D + G', 'SAME BENEFITS, NO PART B DEDUCTIBLE', green)], size=120)],
          'PLANS D AND G INSTEAD', green, tag=G2, src=SRC),
]
# ---- 8: LEAVES OUT ----
S[8] = [
    slide('WHAT MEDIGAP LEAVES OUT', 2422, [E('line', (150, 245, 1770, 305), 'medigap also leaves', t='MEDIGAP ALSO LEAVES SOME THINGS OUT', size=50, col=goldL),
                                           CH((150, 335, 940, 440), 'long-term care', 'LONG-TERM CARE', False), CH((980, 335, 1770, 440), 'vision or dental', 'VISION OR DENTAL', False),
                                           CH((150, 470, 940, 575), 'hearing aids', 'HEARING AIDS', False), CH((980, 470, 1770, 575), 'glasses', 'GLASSES', False),
                                           CH((500, 605, 1420, 710), 'private-duty nursing', 'PRIVATE-DUTY NURSING', False)],
          'GENERALLY NOT COVERED', red, (255, 255, 255), tag=G2, src=SRC),
    slide('DRUGS NEED PART D', 2423, [E('vs', (150, 260, 1770, 690), 'sold after two thousand five', cols=[('MEDIGAP SOLD AFTER 2005', 'NO DRUGS', 'NOT INCLUDED', red), ('PRESCRIPTIONS', 'PART D', 'A SEPARATE PLAN', gold)], size=110)],
          'FOR DRUGS: A SEPARATE PLAN', gold, tag=G2, src=SRC),
    slide('ONE POLICY, ONE PERSON', 2424, [E('icard', R2[0], 'one policy covers', icon='check', l1='ONE POLICY', l2='COVERS ONE PERSON', col=gold),
                                          E('icard', R2[1], 'spouses each', icon='check', l1='SPOUSES', l2='EACH NEED THEIR OWN', col=green, c2=green)],
          'EACH PERSON BUYS HIS OWN', gold, tag=G2, src=SRC),
]
# ---- 9: COST ----
S[9] = [
    slide('TWO MONTHLY PREMIUMS', 2425, [E('vs', (150, 260, 1770, 690), 'what does it cost', cols=[('PRIVATE COMPANY', 'MEDIGAP', 'MONTHLY PREMIUM', gold), ('MEDICARE', 'PART B', 'MONTHLY PREMIUM, ON TOP', blue)], size=96)],
          'TWO PREMIUMS, NOT ONE', gold, tag=G3, src='CMS.GOV'),
    slide('THE 2026 PART B PREMIUM', 2426, [E('line', (150, 250, 1770, 330), 'in twenty twenty-six', t='IN 2026', size=76, col=white),
                                    E('big', (150, 340, 1770, 640), 'two hundred two dollars', val='$202.90', sub='STANDARD PART B PREMIUM, 2026', size=210, vcol=goldL)],
          'PAID TO MEDICARE EVERY MONTH', gold, tag=G3, src='CMS.GOV'),
    slide('GET MORE THAN ONE QUOTE', 2427, [E('icard', R3[0], 'and the premium for', icon='bill', l1='COMPANY 1', l2='SAME LETTER, ONE PRICE', col=gold),
                                           E('icard', R3[1], 'from one company', icon='bill', l1='COMPANY 2', l2='SAME LETTER, ANOTHER PRICE', col=gold),
                                           E('icard', R3[2], 'quotes from more', icon='bill', l1='COMPANY 3', l2='SAME LETTER, ANOTHER PRICE', col=green, c2=green)],
          'ASK MORE THAN ONE COMPANY', green, tag=G3, src=SRC),
]
# ---- 10: PRICING ----
S[10] = [
    slide('HOW THE PRICE IS SET', 2428, [E('line', (150, 245, 1770, 305), 'there is a second', t='A SECOND PRICE TRAP: HOW THE PRICE IS SET', size=48, col=goldL),
                                        E('agecol', (560, 325, 1360, 705), 'community-rated', title='COMMUNITY-RATED', mode='flat', line1='SAME FOR EVERYONE', line2='WHATEVER THEIR AGE', col=green)],
          'THREE WAYS TO PRICE', gold, tag=G3, src=SRC),
    slide('PRICE BY AGE', 2450, [E('agecol', R2c[0], 'issue-age-rated means', title='ISSUE-AGE-RATED', mode='low', line1='SET BY AGE WHEN YOU BUY', line2='DOES NOT RISE WITH AGE', col=gold),
                                E('agecol', R2c[1], 'attained-age-rated', title='ATTAINED-AGE-RATED', mode='rise', line1='RISES AS YOU AGE', line2='CHEAP AT FIRST', col=red)],
          'WHAT YOUR AGE DOES TO THE PRICE', gold, tag=G3, src=SRC),
    slide("MEDICARE'S OWN EXAMPLE", 2429, [E('line', (150, 250, 1770, 310), "in medicare's own", t="MEDICARE'S OWN EXAMPLE", size=54, col=goldL),
                                          E('stamp', (560, 590, 1360, 710), 'not an actual price', t='NOT AN ACTUAL PRICE', col=gold, ang=-4, size=70),
                                          E('calc', (150, 340, 1770, 550), 'one hundred twenty dollars', parts=[('AGE 65', white, 52), ('$120', goldL, 90), ('→', white, 80), ('AGE 66', white, 52), ('$126', red, 90)], col=gold)],
          'A RISING PRICE', red, (255, 255, 255), tag=G3, src=SRC),
]
# ---- 11: OPEN ENROLLMENT ----
S[11] = [
    slide('MEDIGAP OPEN ENROLLMENT', 2430, [E('line', (150, 245, 1770, 305), 'now the most important', t='THE MEDIGAP OPEN ENROLLMENT PERIOD', size=52, col=goldL),
                                          E('sixm', (150, 335, 1770, 575), 'it lasts six months', label='STARTS THE FIRST MONTH YOU HAVE PART B AND ARE 65 OR OLDER'),
                                          CH((330, 620, 1590, 720), 'first month you have', 'FIRST MONTH WITH PART B + AGE 65 OR OLDER', True, 36)],
          'SIX MONTHS', gold, tag=G4, src=SRC),
    slide('ONE TIME ONLY', 2431, [E('big', (150, 250, 1770, 600), 'it is a one-time', val='ONE TIME', sub='IT DOES NOT REPEAT EVERY YEAR', size=220, vcol=red)],
          'A ONE-TIME WINDOW', red, (255, 255, 255), tag=G4, src=SRC),
    slide('DURING THE WINDOW', 2432, [CH((200, 270, 1720, 400), 'during it', 'CANNOT REFUSE ANY POLICY IT OFFERS', True, 46),
                                     CH((200, 440, 1720, 570), 'medical underwriting', 'NO MEDICAL UNDERWRITING', True, 46),
                                     CH((200, 610, 1720, 740), 'charge you more', 'NO HIGHER PRICE FOR YOUR HEALTH', True, 46)],
          'YOUR BEST CHANCE', green, tag=G4, src=SRC),
]
# ---- 12: OUTSIDE ----
S[12] = [
    slide('OUTSIDE THAT WINDOW', 2433, [E('line', (150, 245, 1770, 310), 'outside that window', t='THE RULES CHANGE', size=60, col=goldL),
                                       CH((200, 340, 1720, 450), 'pay more', 'YOU MAY PAY MORE', False, 46), CH((200, 475, 1720, 585), 'fewer plans', 'FEWER PLANS TO CHOOSE FROM', False, 46),
                                       CH((200, 610, 1720, 720), 'no guarantee', 'NO GUARANTEE THEY WILL SELL YOU ONE', False, 42)],
          'THE RULES CHANGE', red, (255, 255, 255), tag=G4, src=SRC),
    slide("CAROL'S SIX MONTHS", 2434, [E('person', (150, 250, 560, 700), 'this matters for carol', letter='C', name='CAROL', line='PART B + AGE 65', col=green),
                                      E('sixm', (620, 250, 1770, 500), 'her six months', label='START THE MONTH PART B STARTS'),
                                      E('stamp', (700, 580, 1700, 700), 'cannot be changed', t='CANNOT BE CHANGED OR REPEATED', col=red, ang=-3, size=64)],
          'MEDICARE SAYS SO', red, (255, 255, 255), tag=G4, src=SRC),
]
# ---- 13: BEN ----
S[13] = [
    slide('BEN WANTS TO SWITCH', 2435, [E('oneway', (150, 250, 1770, 700), 'now ben', l1='ADVANTAGE', l2='MEDIGAP', fwd='BEN WANTS THIS', back='ILLEGAL TO SELL IT TO HIM', c1=blue, c2=gold)],
          'UNLESS HE IS SWITCHING BACK', red, (255, 255, 255), tag=G5, src=SRC),
    slide('NO WINDOW, NO GUARANTEE', 2436, [CH((150, 300, 940, 430), 'not in his open', 'NOT IN OPEN ENROLLMENT', False, 36), CH((150, 470, 940, 600), 'no guaranteed issue right', 'NO GUARANTEED ISSUE RIGHT', False, 36),
                                               CH((980, 300, 1770, 430), 'deny him', 'MAY DENY HIM A POLICY', False, 36), CH((980, 470, 1770, 600), 'charge him more', 'OR CHARGE HIM MORE', False, 36)],
          'WITHOUT A GUARANTEED ISSUE RIGHT', red, (255, 255, 255), tag=G5, src=SRC),
]
# ---- 14: GUARANTEED ISSUE ----
S[14] = [
    slide('WHEN BEN IS PROTECTED', 2437, [E('line', (150, 245, 1770, 305), 'but there are situations', t='BEN IS PROTECTED WHEN...', size=54, col=goldL),
                                         E('icard', R3c[0], 'leaves medicare', icon='doc', l1='PLAN LEAVES', l2='MEDICARE', col=gold),
                                         E('icard', R3c[1], 'stops giving care', icon='cross', l1='PLAN STOPS CARE', l2='IN HIS AREA', col=gold),
                                         E('icard', R3c[2], 'moves out', icon='house', l1='HE MOVES OUT', l2='OF THE SERVICE AREA', col=gold)],
          'GUARANTEED ISSUE RIGHTS', gold, tag=G5, src=SRC),
    slide('THEN THE COMPANY MUST', 2438, [CH((200, 270, 1720, 400), 'then the company', 'MUST SELL HIM A POLICY', True, 46), CH((200, 440, 1720, 570), 'pre-existing', 'MUST COVER PRE-EXISTING CONDITIONS', True, 44),
                                         CH((200, 610, 1720, 740), 'cannot charge him', 'CANNOT CHARGE MORE FOR HIS HEALTH', True, 44)],
          'THREE PROTECTIONS', green, tag=G5, src=SRC),
    slide('APPLY WITHIN 63 DAYS', 2439, [E('big', (150, 250, 800, 640), 'he must apply', val='63', sub='DAYS AFTER ADVANTAGE ENDS', size=250, vcol=goldL),
                                        E('card', (860, 290, 1770, 660), 'his state', head='HIS STATE MAY GIVE', val='EVEN MORE RIGHTS', vsize=64, vcol=goldL, col=green, icon='check', s=0.6)],
          'DO NOT WAIT', gold, tag=G5, src=SRC),
]
# ---- 15: TRIAL RIGHT ----
S[15] = [
    slide('TRIAL RIGHT 1', 2440, [E('line', (150, 245, 1770, 305), 'there is also a trial', t='THERE IS ALSO A TRIAL RIGHT', size=54, col=goldL),
                                 E('icard', R3c[0], 'joined an advantage', icon='doc', l1='JOINED ADVANTAGE', l2='FIRST ELIGIBLE AT 65', col=blue),
                                 E('icard', R3c[1], 'go back to original', icon='clock', l1='WITHIN 1 YEAR', l2='BACK TO ORIGINAL MEDICARE', col=gold),
                                 E('icard', R3c[2], 'any medigap policy', icon='check', l1='ANY MEDIGAP', l2='SOLD IN YOUR STATE', col=green, c2=green)],
          'THE FIRST TRIAL RIGHT', gold, tag=G5, src=SRC),
    slide('TRIAL RIGHT 2', 2441, [E('icard', R3[0], 'dropped a medigap', icon='cross', l1='DROPPED MEDIGAP', l2='TO TRY ADVANTAGE', col=red, c2=red),
                                 E('icard', R3[1], 'less than a year', icon='clock', l1='LESS THAN A YEAR', l2='IN THE PLAN', col=gold),
                                 E('icard', R3[2], 'old policy back', icon='check', l1='ASK FOR THE OLD ONE', l2='IF THE COMPANY SELLS IT', col=green, c2=green)],
          'THE SECOND TRIAL RIGHT', green, tag=G5, src=SRC),
]
# ---- 16: WHAT TO DO ----
S[16] = [
    slide('WHAT TO DO: 1 AND 2', 2442, [E('line', (150, 245, 1770, 305), 'so what should you', t='WHAT SHOULD YOU DO THIS FALL?', size=54, col=goldL),
                                       E('numcol', R2c[0], 'one before', n=1, icon='lock', l1='BEFORE YOU DROP', l2='ANY MEDIGAP POLICY'),
                                       E('numcol', R2c[1], 'two before', n=2, icon='clock', l1='CHECK YOUR WINDOW', l2='OR GUARANTEED RIGHT')],
          'MEDICARE SAYS YOU MAY NOT GET IT BACK', gold, tag=G6, src=SRC),
    slide('WHAT TO DO: 3 AND 4', 2443, [E('numcol', R2[0], 'three compare', n=3, icon='chart', l1='COMPARE ONE LETTER', l2='AT 2+ COMPANIES'),
                                       E('numcol', R2[1], 'four call', n=4, icon='phone', l1='CALL YOUR STATE', l2='HEALTH INSURANCE PROGRAM')],
          'FREE HELP, NOT TIED TO ANY INSURER', green, tag=G6, src=SRC),
]
# ---- 17: RECAP ----
S[17] = [
    slide('RECAP: 1 AND 2', 2444, [E('line', (150, 250, 1770, 320), 'to sum up', t='FIVE FACTS', size=64, col=goldL),
                                  E('rule', (180, 350, 1740, 490), 'one medigap pays', n=1, text='MEDIGAP PAYS YOUR SHARE', val='SOLD BY PRIVATE COMPANIES'),
                                  E('rule', (180, 520, 1740, 660), 'two plan g covers', n=2, text='PLAN G COVERS A LOT', val='NOT THE PART B DEDUCTIBLE', vc=red)],
          'TWO FACTS', gold, tag=G7, src=SRC),
    slide('RECAP: 3 AND 4', 2445, [E('rule', (180, 290, 1740, 450), 'three your medigap', n=3, text='OPEN ENROLLMENT: 6 MONTHS', val='ONLY ONCE', vc=red),
                                  E('rule', (180, 500, 1740, 660), 'four after it', n=4, text='AFTER IT: DENIED OR HIGHER PRICE', val='UNLESS A RIGHT APPLIES', vc=red)],
          'TWO MORE', gold, tag=G7, src=SRC),
    slide('RECAP: 5', 2446, [E('rule', (180, 330, 1740, 530), 'five if you drop', n=5, text='DROP MEDIGAP FOR ADVANTAGE?', val='MAY NOT GET IT BACK', vc=red)],
          'THE FIFTH FACT', red, (255, 255, 255), tag=G7, src=SRC),
]
# ---- 18: CTA + DISCLAIMER ----
def final14m(t, seed=215):
    Dd = CUR['D']
    fr = base(t); fr = amb(fr, t, seed, 7, 55); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('General information,', white, 250), ('not insurance advice.', white, 315), ('Rules, prices and plans differ', goldL, 410),
             ('by state. Confirm with Medicare', goldL, 475), ('or your State Insurance Department.', white, 570), ('Not affiliated with Medicare.', white, 635)]
    groups = [lines[0:2], lines[2:4], lines[4:6]]; tg = [0.3, 0.3 + (0.6 * Dd - 0.3) / 2, 0.6 * Dd]
    for g, ts in zip(groups, tg):
        if t > ts:
            C = new()
            for tx, cl, yy in g: txt(C, tx, BOLD(48), yy, cl, 255, x=650)
            fr = A_(fr, C, (140, 240, 1160, 770), t, ts)
    if t > 0.68 * Dd:
        C = new(); dashed(C, 1220, 280, 1780, 640); txt(C, 'WATCH NEXT', BOLD(56), 430, goldL, 255, x=1500); fr = A_(fr, C, (1200, 260, 1800, 660), t, 0.68 * Dd)
    if t > 0.8 * Dd - 0.4:
        import modello_unico as _m
        C = new(); _m.dashed_circle(C, 260, 860, 85); txt(C, 'SUBSCRIBE', BOLD(44), 835, goldL, 255, x=560); fr = A_(fr, C, (160, 760, 760, 960), t, 0.8 * Dd - 0.4)
    return frame(fr)
S[18] = [
    slide('SEND IT TO SOMEONE', 2447, [E('icard', (500, 260, 1420, 690), None, icon='mail', l1='SOMEONE ABOUT', l2='TO TURN 65', col=gold)], 'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 2448, [E('line', (200, 330, 1720, 430), None, t='WHICH PLAN WERE YOU', size=88, col=white), E('line', (200, 470, 1720, 570), 'which plan', t='THINKING ABOUT?', size=88, col=goldL)],
          'ANSWER IN THE COMMENTS'),
    frozen(final14m),
]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
CUTS = {1: ['it is the choice', 'medicare itself warns'], 2: ['ben is sixty-eight', 'both of them'], 3: ['no sales pages'],
        4: ['original medicare which', 'medigap helps pay', 'and medicare itself'], 5: ['all plans with', 'the only difference'],
        6: ['it covers part b', 'the part a deductible'], 7: ['medigap plans sold', 'that is why'], 8: ['medigap plans sold after', 'and one policy'],
        9: ['in twenty twenty-six', 'and the premium'], 10: ['issue-age-rated means', 'in medicare\'s own'], 11: ['it is a one-time', 'during it'], 12: ['this matters for carol'],
        13: ['and if ben'], 14: ['then the company', 'he must apply'], 15: ['if you dropped'], 16: ['three compare'], 17: ['three your medigap', 'five if you drop'], 18: ['and tell me', 'one last thing']}
for _b, _ph in CUTS.items():
    _tot = sum(SPEC[_b]); _c = [0] + [round((V.at(_b, p) - 0.2) * 30) for p in _ph] + [_tot]
    SPEC[_b] = [_c[i + 1] - _c[i] for i in range(len(_c) - 1)]
if os.environ.get('PV'):   # solo anteprima layout dei blocchi senza voce: durate finte uguali (750 fotogrammi = 25 s)
    for _b in SLIDES:
        if not os.path.exists(os.path.join(VID, 'voce', f'b{_b}.wav')): SPEC[_b] = [750 // len(SLIDES[_b])] * len(SLIDES[_b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v14', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
