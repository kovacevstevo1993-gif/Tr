"""Video 11 - Never Keep More Than This in One Bank Account After 65 - tutti i 29 blocchi. Uso: python3 v11.py render|preview|check|spec <blocco>
Layout nuovi rispetto ai video 8-10: estratto conto, barra di copertura, albero dei beneficiari, scudo, linea del tempo, tabelle, serbatoio soglia,
etichetta RULE N OF 5 in alto a sinistra e fonte ufficiale in alto a destra su ogni slide."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v11eng import *

R2 = row(2); R3 = row(3); R4 = row(4, gap=36)
FD, CF, SS, MC = 'FDIC.GOV', 'CFPB', 'SSA.GOV', 'MEDICARE.GOV'
R1, R2T, R3T, R4T, R5T = 'RULE 1 OF 5', 'RULE 2 OF 5', 'RULE 3 OF 5', 'RULE 4 OF 5', 'RULE 5 OF 5'
S = {}
# ---- 1: HOOK ----
S[1] = [
    slide('THE NUMBER EVERY SENIOR KNOWS', 401, [E('shield', (150, 230, 650, 720), None, val='$250,000', sub='AT YOUR BANK', col=gold, size=80),
                                                 E('line', (720, 245, 1770, 300), 'most', t='MOST PEOPLE OVER 65 HAVE HEARD IT', size=46, col=goldL),
                                                 E('card', (720, 330, 1225, 710), 'not', head='IT IS NOT A LIMIT ON', val='YOUR MONEY', sub='HOW MUCH YOU HAVE', col=red, vcol=red, vsize=66),
                                                 E('card', (1265, 330, 1770, 710), 'set', head='IT IS A LIMIT ON', val='THE SETUP', sub='HOW IT IS ARRANGED', col=green, vcol=green, vsize=66)],
          'NOT HOW MUCH, BUT HOW', gold, src=FD),
    slide('5 RULES BEHIND IT', 402, [E('card', b, 'five' if i == 0 else None, head='RULE', val=str(i + 1), col=gold, vsize=130, icon='lock', s=0.7) for i, b in enumerate(row(5, gap=34))],
          'MOST SENIORS NEVER CHECK THEM', red, (255, 255, 255)),
]
# ---- 2: FRANK AND MARY ----
S[2] = [
    slide('MEET FRANK', 403, [E('person', (150, 250, 700, 700), None, letter='F', name='FRANK, 67', line='ONE BANK IN TOWN', line2='KEEPS EVERYTHING THERE', col=blue),
                              E('ledger', (780, 250, 1770, 570), 'keeps', head="FRANK'S BANK", rows=[('OWNER', 'FRANK', None), ('ACCOUNTS', 'ALL AT ONE BANK', None), ('FROM', 'SELLING HIS HOUSE', None)], col=blue),
                              E('line', (780, 610, 1770, 690), 'three', t='BALANCE: $380,000', size=70, col=green)],
          'ALL HIS MONEY IN ONE PLACE', gold),
    slide('MEET MARY', 404, [E('person', (150, 250, 700, 700), None, letter='M', name='MARY, 70', line='A WIDOW', line2='NEEDS HELP WITH BILLS', col=gold),
                             E('ledger', (780, 250, 1770, 700), 'son', head="MARY'S CHECKING", rows=[('OWNER', 'MARY', None), ('ALSO ON IT', 'HER SON', red), ('WHY', 'TO PAY THE BILLS', None)], col=gold)],
          'HER SON IS ON HER ACCOUNT', gold),
]
# ---- 3: SOURCES ----
S[3] = [
    slide('EVERY NUMBER IS OFFICIAL', 405, [E('icard', R4[0], None, icon='bank', l1='FDIC', l2='FDIC.GOV', col=gold, s=0.7),
                                            E('icard', R4[1], 'social', icon='coins', l1='SOCIAL SECURITY', l2='SSA.GOV', col=gold),
                                            E('icard', R4[2], 'consumer', icon='doc', l1='CFPB', l2='CONSUMERFINANCE.GOV', col=gold),
                                            E('icard', R4[3], 'medicare', icon='check', l1='MEDICARE', l2='MEDICARE.GOV', col=gold)],
          'FIRST: THE FAMOUS NUMBER', gold),
]
# ---- 4: RULE 1 ----
S[4] = [
    slide('THE $250,000 RULE', 406, [E('line', (720, 245, 1770, 305), None, t='RULE NUMBER ONE', size=56, col=goldL),
                                     E('shield', (150, 230, 650, 720), 'insures', val='$250,000', sub='AT LEAST', sub2='FDIC INSURED', col=gold, size=80),
                                     E('step', (720, 330, 1770, 450), 'depositor', n=1, text='PER DEPOSITOR'),
                                     E('step', (720, 465, 1770, 585), 'bank', n=2, text='PER INSURED BANK'),
                                     E('step', (720, 600, 1770, 720), 'ownership', n=3, text='PER OWNERSHIP CATEGORY')],
          'THREE CONDITIONS, NOT ONE', gold, tag=R1, src=FD),
    slide('CREDIT UNIONS TOO', 407, [E('card', (160, 270, 800, 680), None, head='BANKS: FDIC', val='$250,000', sub='PER DEPOSITOR', col=gold, icon='bank', s=0.5, vsize=100),
                                     E('op', (820, 420, 1100, 540), 'credit', t='=', size=140),
                                     E('card', (1120, 270, 1760, 680), 'credit', head='CREDIT UNIONS: NCUA', val='$250,000', sub='PER DEPOSITOR', col=gold, icon='bank', s=0.5, vsize=100)],
          'SAME COVERAGE AT CREDIT UNIONS', green, tag=R1, src='NCUA.GOV'),
]
# ---- 5: SINCE 1934 ----
S[5] = [
    slide('SINCE 1934', 408, [E('cal', (150, 270, 560, 660), None, head='FDIC BEGINS', big='1934', sub='THE START', col=gold, size=110),
                              E('tline', (600, 250, 1200, 700), 'nineteen', pts=[('1934', None, gold), ('TODAY', None, green)], span=(0, 1, 'NO LOSSES', green)),
                              E('big', (1230, 280, 1770, 620), 'penny', val='$0', sub='INSURED DEPOSITS LOST', size=200, vcol=green)],
          'THE KEY WORD IS INSURED', green, tag=R1, src=FD),
    slide('ABOVE THE LIMIT', 409, [E('icard', R2[0], None, icon='check', l1='UP TO THE LIMIT', l2='COVERED', col=green, c2=green),
                                   E('icard', R2[1], 'above', icon='cross', l1='ABOVE THE LIMIT', l2='SAME NAME, SAME CATEGORY', col=red, c2=red)],
          'NOT COVERED IF THE BANK FAILS', red, (255, 255, 255), tag=R1, src=FD),
]
# ---- 6: FRANK'S MONEY ----
S[6] = [
    slide("FRANK'S SETUP", 410, [E('ledger', (150, 250, 1000, 700), None, head="FRANK'S BANK", rows=[('BANKS', 'ONE', None), ('NAMES', 'ONE', None), ('ACCOUNT TYPE', 'SINGLE', None), ('BALANCE', '$380,000', goldL)], col=blue),
                                 E('big', (1080, 300, 1770, 620), 'single', val='$380,000', sub='IN ONE SINGLE ACCOUNT', size=150)],
          'ONE BANK, ONE NAME, ONE ACCOUNT', gold, tag=R1),
    slide('WHAT IS COVERED', 411, [E('meter', (180, 250, 1740, 640), None, total=380, limit=250, head="FRANK'S $380,000", tot_l='ONE BANK', lim_l='$250,000 LIMIT',
                                     g1='$250,000', g2='COVERED', r1=None, r2=None),
                                   E('big', (1230, 480, 1730, 600), 'other', val='$130,000', sub='NOT COVERED', size=66, vcol=red),
                                   E('stamp', (1440, 640, 1770, 740), 'risk', t='AT RISK', col=red, ang=-6, size=56)],
          '$130,000 AT RISK IF THE BANK FAILS', red, (255, 255, 255), psize=48, tag=R1, src=FD),
]
# ---- 7: NO MAGIC NUMBER ----
S[7] = [
    slide('NO MAGIC NUMBER', 412, [E('icard', (150, 330, 670, 720), None, icon='cross', l1='ONE NUMBER', l2='FOR EVERYONE', col=red, c2=red),
                                   E('line', (150, 245, 1770, 300), 'how much', t='HOW MUCH YOU CAN SAFELY KEEP IN ONE BANK DEPENDS ON:', size=44, col=goldL),
                                   E('icard', (700, 330, 1220, 720), 'names', icon='doc', l1='THE NAMES', l2='ON THE ACCOUNT', col=gold),
                                   E('icard', (1250, 330, 1770, 720), 'type', icon='bank', l1='THE TYPE', l2='OF ACCOUNT', col=gold, s=0.6)],
          'NEXT: RULE NUMBER TWO', gold),
]
# ---- 8: RULE 2, CATEGORIES ----
S[8] = [
    slide('EACH CATEGORY IS SEPARATE', 413, [E('line', (150, 245, 1770, 300), None, t='SAME BANK, DIFFERENT CATEGORIES', size=50, col=goldL),
                                             E('card', (150, 330, 670, 720), 'single', head='SINGLE', val='$250,000', sub='YOUR NAME ONLY', col=blue, icon='wallet', s=0.6, vsize=86),
                                             E('card', (700, 330, 1220, 720), 'joint', head='JOINT', val='$250,000', sub='PER CO-OWNER', col=gold, icon='house', s=0.6, vsize=86),
                                             E('card', (1250, 330, 1770, 720), 'retirement', head='RETIREMENT', val='$250,000', sub='IRA DEPOSITS', col=green, icon='coins', s=0.6, vsize=86)],
          'EACH ONE INSURED SEPARATELY', gold, tag=R2T, src=FD),
]
# ---- 9: JOINT ----
S[9] = [
    slide('A JOINT ACCOUNT', 414, [E('card', (130, 290, 540, 650), None, head='CO-OWNER 1', val='$250,000', sub='HIS SHARE', col=blue, vsize=76),
                                   E('op', (550, 420, 660, 520), 'share', t='+', size=110),
                                   E('card', (670, 290, 1080, 650), 'share', head='CO-OWNER 2', val='$250,000', sub='HER SHARE', col=gold, vsize=76),
                                   E('op', (1090, 420, 1200, 520), 'couple', t='=', size=110),
                                   E('shield', (1220, 230, 1790, 720), 'five', val='$500,000', sub='ONE BANK', col=green, size=76)],
          'ON TOP OF THEIR SINGLE ACCOUNTS', green, tag=R2T, src=FD),
]
# ---- 10: TRUST / POD ----
S[10] = [
    slide('PAYABLE ON DEATH ACCOUNTS', 415, [E('icard', (150, 250, 880, 465), None, icon='doc', l1='TRUST ACCOUNTS', col=gold, s=0.45, size=48),
                                             E('icard', (150, 495, 880, 710), 'payable', icon='mail', l1='PAYABLE ON DEATH', col=gold, s=0.55, size=48),
                                             E('shield', (1000, 230, 1700, 720), 'coverage', val='$250,000', sub='PER BENEFICIARY', col=green, size=80)],
          'COVERAGE GROWS WITH BENEFICIARIES', green, psize=48, tag=R2T, src=FD),
    slide('THE TRUST ACCOUNT TABLE', 416, [E('grid', (330, 240, 1590, 730), None, head=['BENEFICIARIES', 'COVERAGE PER OWNER'], w=[0.5, 0.5],
                                             rows=[['1', '$250,000'], ['2', '$500,000'], ['3', '$750,000'], ['4', '$1,000,000'], ['5 OR MORE', ('$1,250,000', green)]])],
          'MAX $1.25 MILLION PER OWNER, PER BANK', gold, psize=46, tag=R2T, src=FD),
]
# ---- 11: FRANK'S FIX ----
S[11] = [
    slide('FRANK NAMES HIS DAUGHTERS', 417, [E('tree', (360, 240, 1560, 720), None, owner='FRANK', letter='F', col=blue, kids=[('DAUGHTER 1', '$250,000'), ('DAUGHTER 2', '$250,000')])],
          'PAYABLE ON DEATH BENEFICIARIES', gold, tag=R2T),
    slide('SAME BANK, SAME MONEY', 418, [E('bars', (150, 250, 900, 700), None, vals=[('BEFORE', 250, '$250,000'), ('AFTER', 500, '$500,000')], lo=0.4),
                                         E('stamp', (790, 410, 1010, 530), 'five', t='2X', col=green, ang=-8, size=70),
                                         E('icard', (1040, 270, 1770, 680), 'all', icon='check', l1='ALL $380,000', l2='NOW COVERED', col=green, c2=green)],
          'ALL OF IT IS COVERED', green, tag=R2T),
]
# ---- 12: EDIE ----
S[12] = [
    slide("THE FDIC'S FREE TOOL: EDIE", 419, [E('app', (170, 230, 650, 720), None, l1='EDIE', l2='FDIC', l3='ESTIMATOR', col=green),
                                             E('line', (720, 240, 1770, 295), 'free', t='FREE TOOL FROM THE FDIC', size=50, col=goldL),
                                             E('line', (720, 305, 1770, 350), 'electronic', t='ELECTRONIC DEPOSIT INSURANCE ESTIMATOR', size=38, col=white),
                                             E('step', (720, 385, 1770, 490), 'enter', n=1, text='ENTER YOUR ACCOUNTS'),
                                             E('step', (720, 500, 1770, 605), 'shows', n=2, text='SEE WHAT IS INSURED', val='YES', vc=green),
                                             E('step', (720, 615, 1770, 720), 'not', n=3, text='AND WHAT IS NOT', val='NO', vc=red)],
          'CHECK BEFORE YOU CHANGE ANYTHING', gold, psize=48, tag=R2T, src='EDIE.FDIC.GOV'),
]
# ---- 13: JOINT WARNING ----
S[13] = [
    slide('THE JOINT ACCOUNT WARNING', 420, [E('card', (150, 240, 700, 465), None, head='THE WARNING', val='JOINT', sub='ACCOUNTS', col=gold, vsize=80),
                                             E('card', (150, 495, 700, 720), 'consumer', head='THE CFPB SAYS', val='MOST CASES', sub='', col=gold, vsize=64),
                                             E('card', (740, 260, 1240, 700), 'either', head='EITHER OWNER CAN', val='WITHDRAW', sub='THE MONEY', col=red, vcol=red, vsize=70),
                                             E('card', (1270, 260, 1770, 700), 'close', head='AND EVEN', val='CLOSE IT', sub='THE ACCOUNT', col=red, vcol=red, vsize=70)],
          'ANY OWNER CAN EMPTY IT', red, (255, 255, 255), tag=R2T, src=CF),
]
# ---- 14: MARY ----
S[14] = [
    slide("MARY'S SITUATION", 421, [E('person', (150, 250, 700, 700), None, letter='M', name='MARY', line='ADDED HER SON', line2='ONLY TO PAY BILLS', col=gold),
                                    E('ledger', (780, 250, 1770, 700), 'son', head='JOINT CHECKING', rows=[('OWNER', 'MARY', None), ('JOINT OWNER', 'HER SON', red), ('HIS RIGHTS', 'SAME AS HERS', red)], col=gold)],
          'ON PAPER, HE IS AN OWNER', gold, tag=R2T, src=CF),
    slide('THE TWO RISKS', 422, [E('icard', (150, 260, 600, 700), None, icon='cross', l1='A JOINT OWNER', l2='HAS THE SAME RIGHTS', col=red, c2=red),
                                 E('rule', (640, 290, 1770, 450), 'take', n=1, text='MONEY TAKEN FOR THEIR OWN USE', val='RISK', vc=red, col=red),
                                 E('rule', (640, 510, 1770, 670), 'exposed', n=2, text="THE JOINT OWNER'S CREDITORS", val='RISK', vc=red, col=red)],
          'THE RISK THE CFPB WARNS ABOUT', red, (255, 255, 255), tag=R2T, src=CF),
]
# ---- 15: OPTIONS ----
S[15] = [
    slide('SAFER WAYS TO GET HELP', 423, [E('line', (150, 240, 1770, 295), None, t='THE CFPB POINTS TO OTHER OPTIONS', size=48, col=goldL),
                                          E('grid', (150, 320, 1300, 500), 'convenience', head=['OPTION', 'HELPS PAY BILLS', 'OWNS THE MONEY'], w=[0.44, 0.28, 0.28],
                                              rows=[['CONVENIENCE SIGNER', 'Y', 'N']]),
                                          E('stamp', (1330, 330, 1770, 490), 'own', t='NOT AN OWNER', col=green, ang=-6, size=46),
                                          E('icard', (150, 525, 940, 725), 'power', icon='doc', l1='POWER OF ATTORNEY', col=gold, size=46, s=0.5),
                                          E('icard', (980, 525, 1770, 725), 'alerts', icon='phone', l1='ALERTS + LIMITS', col=gold, size=46, s=0.5)],
          'HELP WITHOUT GIVING AWAY OWNERSHIP', green, psize=46, tag=R2T, src=CF),
]
# ---- 16: RULE 3 ----
S[16] = [
    slide('NOT EVERYTHING IS INSURED', 424, [E('icard', (150, 250, 600, 710), None, icon='bank', l1='NOT EVERYTHING', l2='YOU BUY AT A BANK', col=gold, s=0.6),
                                             E('line', (640, 250, 1770, 310), 'insured.', t='NOT COVERED BY THE FDIC:', size=52, col=red),
                                             E('tagset', (640, 350, 1770, 510), 'stocks', items=['STOCKS', 'BONDS', 'MUTUAL FUNDS']),
                                             E('tagset', (640, 550, 1770, 710), 'annuities', items=['ANNUITIES', 'LIFE INSURANCE', 'CRYPTO'])],
          'ONLY DEPOSITS ARE INSURED', red, (255, 255, 255), tag=R3T, src=FD),
    slide('EVEN IN THE SAME BUILDING', 425, [E('icard', R2[0], None, icon='lock', l1='SAFE DEPOSIT BOX', l2='NOT INSURED', col=red, c2=red),
                                             E('icard', R2[1], 'building', icon='bank', l1='BOUGHT AT THE BANK', l2='STILL NOT A DEPOSIT', col=gold, s=0.6)],
          'THE BUILDING DOES NOT MATTER', gold, tag=R3T, src=FD),
]
# ---- 17: APPS ----
S[17] = [
    slide('WATCH THE APPS', 426, [E('app', (200, 230, 680, 720), None, l1='MONEY APP', l2='$', l3='INSURED?', col=red),
                                  E('card', (800, 250, 1760, 590), 'nonbank', head='NONBANK COMPANIES', val='NEVER', sub='FDIC INSURED THEMSELVES', col=red, vcol=red, vsize=130),
                                  E('stamp', (1080, 610, 1480, 740), 'never', t='NOT A BANK', col=red, ang=-6, size=52)],
          'AN APP IS NOT A BANK', red, (255, 255, 255), tag=R3T, src=FD),
    slide('TWO QUICK CHECKS', 427, [E('step', (180, 300, 1740, 450), None, n=1, text='ASK: WHICH BANK HOLDS MY MONEY?', val='ASK'),
                                    E('step', (180, 510, 1740, 660), 'check', n=2, text="CHECK IT ON THE FDIC'S BANKFIND", val='FREE', vc=green)],
          'NAME THE BANK, THEN CHECK IT', green, tag=R3T, src=FD),
]
# ---- 18: RULE 4 ----
S[18] = [
    slide('IF A DEBT COLLECTOR COMES', 428, [E('icard', (150, 260, 590, 690), None, icon='mail', l1='SOCIAL SECURITY', l2='YOUR CHECK', col=gold, size=44),
                                             E('icard', (630, 260, 1170, 690), 'debt', icon='doc', l1='COURT ORDER', l2='AGAINST YOUR ACCOUNT', col=red, c2=red),
                                             E('icard', (1210, 260, 1770, 690), 'bank must', icon='bank', l1='YOUR BANK', l2='MUST LOOK BACK 2 MONTHS', col=gold, s=0.6)],
          'THE BANK MUST CHECK FIRST', gold, tag=R4T, src=CF),
    slide('TWO MONTHS PROTECTED', 429, [E('tline', (160, 260, 1760, 700), None, pts=[('MONTH 1', 'DIRECT DEPOSIT', green), ('MONTH 2', 'DIRECT DEPOSIT', green), ('ORDER', 'BANK CHECKS', red)], span=(0, 1, 'PROTECTED', green))],
          'THOSE BENEFITS STAY IN YOUR ACCOUNT', green, psize=48, tag=R4T, src=CF),
]
# ---- 19: COVERED + PAPER CHECK ----
S[19] = [
    slide('WHICH BENEFITS', 430, [E('icard', R4[0], None, icon='check', l1='SOCIAL SECURITY', col=green, size=40),
                                  E('icard', R4[1], 's s i', icon='check', l1='SSI', col=green, size=40),
                                  E('icard', R4[2], 'veterans', icon='check', l1='VETERANS', col=green, size=40),
                                  E('icard', R4[3], 'retirement', icon='check', l1='FEDERAL RETIREMENT', col=green, size=40)],
          'FEDERAL BENEFITS, DIRECT DEPOSITED', green, psize=48, tag=R4T, src=CF),
    slide('THE PAPER CHECK CATCH', 431, [E('card', (150, 260, 640, 690), None, head='DIRECT DEPOSIT', val='PROTECTED', sub='2 MONTHS', col=green, vcol=green, vsize=66),
                                         E('icard', (670, 260, 1200, 690), 'paper', icon='bill', l1='PAPER CHECK', l2='YOU DEPOSIT YOURSELF', col=gold, s=0.7),
                                         E('card', (1230, 260, 1770, 690), 'protect', head='BANK DOES NOT HAVE TO', val='PROTECT', sub='', col=red, vcol=red, vsize=78),
                                         E('stamp', (1300, 520, 1700, 660), 'frozen', t='FROZEN', col=red, ang=8, size=58)],
          'YOU WOULD HAVE TO PROVE IT', red, (255, 255, 255), tag=R4T, src=CF),
]
# ---- 20: LIMITS ----
S[20] = [
    slide('WHAT CAN STILL BE TAKEN', 432, GRID((150, 240, 1770, 730), ['DEBT', 'SOCIAL SECURITY', 'SSI'], [0.44, 0.28, 0.28],
                                              [['BACK TAXES', ('CAN BE TAKEN', red), ('PROTECTED', green)], ['FEDERAL STUDENT LOANS', ('CAN BE TAKEN', red), ('PROTECTED', green)],
                                               ['CHILD OR SPOUSAL SUPPORT', ('CAN BE TAKEN', red), ('PROTECTED', green)]], ['taken', 'student', 'child']),
          'SSI IS PROTECTED EVEN FROM THOSE', green, psize=48, tag=R4T, src=CF),
]
# ---- 21: RULE 5 ----
S[21] = [
    slide('THE LIMIT NOBODY TALKS ABOUT', 433, [E('card', (160, 270, 800, 680), None, head='FDIC LIMIT', val='$250,000', sub='PER CATEGORY', col=blue, vsize=96),
                                                E('arrow', (830, 430, 1000, 510), 'lower'),
                                                E('card', (1030, 270, 1760, 680), 'lower', head='A MUCH LOWER LIMIT', val='?', sub='FOR HELP PROGRAMS', col=red, vcol=red, vsize=150)],
          'IT IS MUCH LOWER', red, (255, 255, 255), tag=R5T, src=SS),
    slide('SSI RESOURCE LIMIT', 434, [E('line', (150, 240, 1770, 295), None, t='SUPPLEMENTAL SECURITY INCOME (SSI)', size=50, col=goldL),
                                      E('shield', (320, 305, 860, 725), 'countable', val='$2,000', sub='ONE PERSON', col=red, size=96),
                                      E('shield', (1060, 305, 1600, 725), 'three thousand', val='$3,000', sub='A COUPLE', col=red, size=96)],
          'COUNTABLE RESOURCES, MAXIMUM', red, (255, 255, 255), tag=R5T, src=SS),
]
# ---- 22: WHAT COUNTS ----
S[22] = [
    slide('WHAT COUNTS FOR SSI', 435, [E('grid', (230, 240, 1690, 720), None, head=['WHAT YOU HAVE', 'FOR THE LIMIT'], w=[0.55, 0.45],
                                           rows=[['YOUR HOME', ('DOES NOT COUNT', green)], ['ONE CAR', ('DOES NOT COUNT', green)], ['MONEY IN THE BANK', ('COUNTS', red)]])],
          'BANK MONEY COUNTS', red, (255, 255, 255), tag=R5T, src=SS),
    slide('ONE DEPOSIT TOO MANY', 436, [E('icard', (130, 260, 760, 690), None, icon='bag', l1='A GIFT FROM FAMILY', l2='SITTING IN CHECKING', col=gold),
                                        E('gauge', (820, 230, 1400, 720), 'push', limit=2000, val=2600, top=3000, lim_l='$2,000', label='CHECKING'),
                                        E('stamp', (1420, 380, 1780, 560), 'risk', t='SSI AT RISK', col=red, ang=-8, size=50)],
          'OVER THE LINE, PAYMENT AT RISK', red, (255, 255, 255), tag=R5T, src=SS),
]
# ---- 23: MSP ----
S[23] = [
    slide('MEDICARE SAVINGS PROGRAMS', 437, [E('icard', (400, 260, 1520, 690), None, icon='doc', l1='CAN HELP PAY', l2='YOUR PART B PREMIUM', col=green, c2=green)],
          'SAME IDEA, ANOTHER LIMIT', gold, tag=R5T, src=MC),
    slide('2026 FEDERAL RESOURCE LIMITS', 438, [E('line', (150, 245, 1770, 300), None, t='MEDICARE SAVINGS PROGRAMS', size=50, col=goldL),
                                                E('card', (150, 330, 940, 720), 'nine thousand', head='ONE PERSON', val='$9,950', sub='RESOURCE LIMIT', col=gold, vsize=110, icon='wallet', s=0.5),
                                                E('card', (980, 330, 1770, 720), 'fourteen', head='MARRIED COUPLE', val='$14,910', sub='RESOURCE LIMIT', col=gold, vsize=110, icon='house', s=0.5)],
          'FEDERAL LIMITS FOR 2026', gold, tag=R5T, src=MC),
]
# ---- 24: STATES ----
S[24] = [
    slide('CHECK WITH YOUR STATE', 439, [E('icard', R2[0], None, icon='chart', l1='SOME STATES', l2='USE HIGHER LIMITS', col=green, c2=green),
                                         E('icard', R2[1], 'count', icon='check', l1='SOME RESOURCES', l2='DO NOT COUNT', col=green, c2=green)],
          'CHECK BEFORE YOU DECIDE', green, tag=R5T, src=MC),
]
# ---- 25: RECAP ----
S[25] = [
    slide('THE 5 RULES', 440, [E('line', (150, 236, 1770, 286), None, t='WHAT TO REMEMBER', size=46, col=goldL),
                               E('rule', (180, 300, 1740, 380), 'one', n=1, text='PER BANK, PER OWNER, PER CATEGORY', val='$250,000'),
                               E('rule', (180, 390, 1740, 470), 'two categories', n=2, text='CATEGORIES + BENEFICIARIES', val='MORE COVERAGE'),
                               E('rule', (180, 480, 1740, 560), 'three investments', n=3, text='INVESTMENTS AND APPS', val='NOT INSURED', vc=red),
                               E('rule', (180, 570, 1740, 650), 'four direct', n=4, text='DIRECT DEPOSIT PROTECTS', val='2 MONTHS'),
                               E('rule', (180, 660, 1740, 740), 'five help', n=5, text='HELP PROGRAMS', val='MUCH LOWER', vc=red)],
          'FIVE RULES, ONE SAFER SETUP', gold),
]
# ---- 26: THREE THINGS ----
S[26] = [
    slide('3 THINGS TO DO THIS WEEK', 441, [E('numcol', (150, 290, 680, 730), None, n=1, icon='coins', l1='ADD UP EACH BANK'),
                                            E('line', (150, 640, 680, 690), 'name', t='BY NAME AND TYPE', size=40, col=goldL),
                                            E('numcol', (695, 290, 1225, 730), 'second,', n=2, icon='phone', l1='RUN THEM IN EDIE'),
                                            E('line', (695, 640, 1225, 690), 'edie', t='FREE FDIC TOOL', size=40, col=goldL),
                                            E('numcol', (1240, 290, 1770, 730), 'third,', n=3, icon='doc', l1='CHECK THE NAMES'),
                                            E('line', (1240, 640, 1770, 690), 'beneficiaries', t='AND BENEFICIARIES', size=40, col=goldL)],
          'DO ALL THREE THIS WEEK', gold),
]
# ---- 27: FRANK & MARY ----
S[27] = [
    slide('WHAT FRANK DID', 442, [E('person', (130, 250, 700, 700), None, letter='F', name='FRANK', line='NAMED HIS DAUGHTERS', line2='AS BENEFICIARIES', col=blue),
                                  E('icard', (820, 270, 1790, 680), 'every', icon='check', l1='EVERY DOLLAR', l2='AT HIS BANK IS COVERED', col=green, c2=green)],
          'SAME BANK, ALL COVERED', green),
    slide('WHAT MARY DID', 443, [E('person', (130, 250, 700, 700), None, letter='M', name='MARY', line='SON: HELPER', line2='NOT AN OWNER', col=gold),
                                 E('icard', (820, 270, 1790, 680), 'alerts', icon='phone', l1='ALERTS ON', l2='FOR EVERY WITHDRAWAL', col=green, c2=green)],
          'SAME MONEY, A MUCH SAFER SETUP', gold),
]
# ---- 28: SHARE + COMMENT ----
S[28] = [
    slide('SEND IT TO ONE PERSON', 444, [E('icard', (500, 260, 1420, 690), None, icon='mail', l1='SOMEONE OVER 65', l2='WHO KEEPS EVERYTHING AT ONE BANK', col=gold)],
          'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 445, [E('line', (260, 360, 1660, 450), None, t='DO YOU USE ONE BANK', size=96, col=white),
                                           E('line', (260, 480, 1660, 570), 'more', t='OR MORE THAN ONE?', size=96, col=goldL)],
          'ANSWER IN THE COMMENTS'),
]
# ---- 29: DISCLAIMER ----
S[29] = [frozen(final11)]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
# tagli tra le slide sulla frase che apre la slide dopo (misurata sulla voce), cosi' ogni slide mostra cio' che la voce dice in quel momento
CUTS = {1: ['and there are five'], 2: ['mary is seventy'], 4: ['credit unions'], 5: ['money above the limit'], 6: ['two hundred fifty thousand is'],
        10: ['up to one point'], 11: ['that moved his coverage'], 14: ['but a joint owner'], 16: ['or what you keep'], 17: ['if an app tells'],
        18: ['federal benefits that were'], 19: ['but here is the catch'], 21: ['if you get supplemental'], 22: ['one large deposit'],
        23: ['in twenty twenty-six'], 27: ['mary changed'], 28: ['and tell me']}
for _b, _ph in CUTS.items():
    _tot = sum(SPEC[_b]); _c = [0] + [round((V.at(_b, p) - 0.2) * 30) for p in _ph] + [_tot]
    SPEC[_b] = [_c[i + 1] - _c[i] for i in range(len(_c) - 1)]
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v11', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
