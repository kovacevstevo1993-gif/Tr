"""Video 9 - blocchi 4-30. Uso: python3 v9b4_30.py render|preview|check <blocco>"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v9eng import *

R2 = row(2); R3 = row(3); R4 = row(4)
S = {}
# ---- 4: NUMBER ONE, THE RAISE ----
S[4] = [
    slide('NUMBER 1: THE RAISE', 111, [E('ring', (180, 240, 760, 720), None, val='+3.6%', sub='2027 COLA', col=green),
                                       E('bars', (900, 240, 1760, 720), 'average', vals=[('BEFORE', 2095, '$2,095'), ('AFTER', 2170, '$2,170')], lo=0.6)],
          'THE AVERAGE RETIREMENT CHECK, PER MONTH'),
    slide('ABOUT $75 MORE, EVERY MONTH', 112, [E('big', (160, 280, 1000, 620), None, val='+$75', sub='PER MONTH, ON AVERAGE', size=200, vcol=green),
                                               E('cal', (1180, 270, 1740, 640), 'january', head='FIRST PAYMENT', big='JAN', sub='2027', col=green)],
          'STARTING WITH THE JANUARY PAYMENT', green),
]
# ---- 5: WHERE 3.6% COMES FROM ----
S[5] = [
    slide('WHO PICKS THE RAISE?', 113, [E('icard', R2[0], 'vote', icon='bank', l1='NOT A VOTE', l2='NOBODY PICKS IT', col=red, c2=red),
                                        E('icard', R2[1], 'formula', icon='bulb', l1='A FORMULA', l2='SAME EVERY YEAR', col=green, c2=green)],
          'IT IS A FORMULA, NOT A VOTE', green),
    slide('THE INFLATION INDEX: CPI-W', 114, [E('card', (130, 270, 690, 660), 'compares', head='3RD QUARTER', val='2025', sub='JUL - SEP', col=blue),
                                              E('arrow', (720, 420, 860, 500), 'third quarter of this'),
                                              E('card', (890, 270, 1450, 660), 'this', head='3RD QUARTER', val='2026', sub='JUL - SEP', col=gold),
                                              E('op', (1460, 380, 1540, 540), 'rise', t='='),
                                              E('card', (1550, 270, 1790, 660), 'raise.', head='RISE', val='3.6%', col=green, vsize=80)],
          'THE RISE IN THE INDEX BECOMES YOUR RAISE'),
]
# ---- 6: MARY'S CHECK ----
S[6] = [
    slide("MARY'S CHECK", 115, [E('pay', (160, 270, 860, 650), None, amount='$2,000', head='MARY TODAY', sub='PER MONTH', col=gold, size=130),
                                E('op', (880, 380, 1000, 540), 'three', t='x'),
                                E('card', (1020, 290, 1380, 630), 'three', head='COLA', val='3.6%', col=green),
                                E('op', (1390, 380, 1470, 540), 'seventy-two', t='='),
                                E('card', (1480, 290, 1790, 630), 'seventy-two', head='RAISE', val='+$72', col=green, vcol=green)],
          'THREE POINT SIX PERCENT OF $2,000 = $72'),
    slide('HER NEW CHECK', 116, [E('pay', (150, 270, 900, 650), 'new', amount='$2,072', head='MARY IN 2027', sub='BEFORE DEDUCTIONS', col=green, size=130),
                                 E('icard', (1050, 270, 1760, 650), 'year', icon='coins', l1='+$864', l2='OVER A FULL YEAR', col=gold, size=90)],
          '$864 MORE OVER A FULL YEAR', green),
]
# ---- 7: BEFORE DEDUCTIONS / PART B ----
S[7] = [
    slide('THE PART PEOPLE MISS', 117, [E('pay', (160, 270, 900, 650), None, amount='$2,072', head='THE RAISE ON PAPER', sub='BEFORE DEDUCTIONS', col=gold, size=120),
                                        E('icard', (1040, 270, 1760, 650), 'medicare,', icon='form', l1='MEDICARE PART B', l2='TAKEN FROM THE SAME CHECK', col=red, c2=red)],
          'PART B USUALLY COMES OUT OF THE CHECK', red, (255, 255, 255)),
    slide('2027 PART B PREMIUM', 118, [E('cal', (180, 280, 760, 650), 'separately,', head='PART B 2027', big='TBA', sub='ANNOUNCED SEPARATELY', col=red),
                                       E('step', (900, 300, 1780, 440), 'raise', n=1, text='THE RAISE ON THE NEWS', val='3.6%'),
                                       E('step', (900, 490, 1780, 630), 'bank', n=2, text='WHAT LANDS IN YOUR BANK', val='LESS', vc=red)],
          'YOUR DEPOSIT CAN BE SMALLER THAN THE RAISE', red, (255, 255, 255), psize=48),
]
# ---- 8: HOLD HARMLESS ----
S[8] = [
    slide('THE HOLD HARMLESS RULE', 119, [E('icard', (300, 260, 900, 690), None, icon='lock', l1='A PROTECTION', l2='HOLD HARMLESS', col=green, c2=green),
                                          E('icard', (1020, 260, 1620, 690), 'most', icon='form', l1='PART B TAKEN', l2='FROM SOCIAL SECURITY', col=gold)],
          'IT PROTECTS MOST PEOPLE WITH PART B', green),
    slide('THE PART B INCREASE IS CAPPED', 120, [E('bars', (220, 250, 980, 700), 'increase', vals=[('PART B INCREASE', 60, 'CAPPED'), ('CHECK INCREASE', 100, 'RAISE')]),
                                                 E('icard', (1120, 270, 1720, 660), 'net', icon='check', l1='NET CHECK', l2='DOES NOT GO DOWN', col=green, c2=green)],
          'FOR THEM, THE NET CHECK DOES NOT DROP', green),
]
# ---- 9: TAX ANGLE ----
S[9] = [
    slide('THE TAX ANGLE', 121, [E('card', (130, 270, 560, 650), 'half', head='HALF YOUR BENEFITS', val='1/2', col=gold),
                                 E('op', (570, 380, 650, 540), 'plus', t='+'),
                                 E('card', (660, 270, 1090, 650), 'other', head='OTHER INCOME', val='$', col=gold),
                                 E('op', (1100, 380, 1180, 540), 'above', t='>'),
                                 E('card', (1190, 270, 1790, 650), 'twenty-five', head='THE LINE', val='$25,000', sub='SINGLE  |  $32,000 JOINT', col=red, vsize=88)],
          'ABOVE THE LINE, PART OF IT IS TAXABLE', red, (255, 255, 255)),
    slide('LINES NOT ADJUSTED FOR INFLATION', 122, [E('icard', (160, 270, 840, 660), 'lines', icon='lock', l1='$25,000 / $32,000', l2='NEVER ADJUSTED', col=red, c2=red),
                                                    E('icard', (1000, 270, 1760, 660), 'raise', icon='chart', l1='EVERY RAISE', l2='MOVES YOU CLOSER', col=gold)],
          'EVERY RAISE PUSHES MORE RETIREES CLOSER', gold, psize=48),
]
# ---- 10: NOTICE ----
S[10] = [
    slide('HOW YOU WILL KNOW', 123, [E('icard', R2[0], 'mails', icon='mail', l1='COLA NOTICE BY MAIL', l2='IN DECEMBER', col=blue),
                                     E('icard', R2[1], 'paperless', icon='phone', l1='MY SOCIAL SECURITY', l2='PAPERLESS NOTICES', col=gold)],
          'TWO WAYS TO SEE YOUR NEW AMOUNT'),
    slide('SIGN UP BY NOVEMBER 18', 124, [E('cal', (200, 270, 800, 660), 'november', head='SIGN UP BY', big='NOV 18', sub='2026', col=red, size=120),
                                          E('icard', (1000, 270, 1720, 660), 'weeks', icon='clock', l1='SEE IT ONLINE', l2='UP TO 3 WEEKS EARLIER', col=green, c2=green)],
          'YOUR NEW AMOUNT UP TO 3 WEEKS EARLIER', green),
]
# ---- 11: NUMBER TWO, SSI ----
S[11] = [
    slide('NUMBER 2: SSI', 125, [E('icard', (160, 260, 880, 690), None, icon='wallet', l1='SUPPLEMENTAL', l2='SECURITY INCOME', col=gold),
                                 E('step', (1000, 320, 1780, 450), 'separate', n=1, text='A SEPARATE PROGRAM'),
                                 E('step', (1000, 500, 1780, 630), 'low', n=2, text='VERY LOW INCOME AND SAVINGS')],
          'SSI IS NOT THE SAME AS SOCIAL SECURITY', gold, psize=50),
    slide('SSI FEDERAL PAYMENT', 126, [E('bars', (150, 250, 900, 700), 'person', vals=[('2026', 994, '$994'), ('2027', 1029, '$1,029')], lo=0.6),
                                       E('bars', (1020, 250, 1770, 700), 'couple,', vals=[('2026', 1491, '$1,491'), ('2027', 1544, '$1,544')], lo=0.6)],
          'ONE PERSON: $1,029  |  COUPLE: $1,544', gold, psize=50),
]
# ---- 12: SSI TIMING ----
S[12] = [
    slide('SSI GETS IT FIRST', 127, [E('cal', (180, 270, 780, 660), 'december', head='FIRST HIGHER SSI', big='DEC 31', sub='2026', col=green, size=120),
                                     E('card', (960, 300, 1340, 630), 'resource', head='RESOURCE LIMIT', val='$2,000', sub='ONE PERSON', col=gold),
                                     E('card', (1400, 300, 1780, 630), 'three', head='RESOURCE LIMIT', val='$3,000', sub='COUPLE', col=gold)],
          'THE RESOURCE LIMITS DID NOT CHANGE'),
    slide('HELPING A PARENT?', 128, [E('person', (560, 260, 1360, 700), None, letter='P', name='A PARENT ON SSI', line='CHECK THE NEW AMOUNT', line2='DEC 31: $1,029', col=gold)],
          'WORTH CHECKING THIS MONTH'),
]
# ---- 13: NUMBER THREE, EARNINGS TEST ----
S[13] = [
    slide('NUMBER 3: THE EARNINGS TEST', 129, [E('icard', (500, 260, 1420, 690), None, icon='lock', l1='CAN HOLD BACK', l2='THOUSANDS OF DOLLARS', col=red, c2=red)],
          'IT IS CALLED THE EARNINGS TEST', red, (255, 255, 255)),
    slide('WHO IT APPLIES TO', 130, [E('icard', (130, 270, 620, 660), 'claim', icon='form', l1='CLAIMED', l2='BEFORE FULL AGE', col=blue),
                                     E('op', (630, 390, 700, 530), 'keep', t='+'),
                                     E('icard', (710, 270, 1200, 660), 'working.', icon='brief', l1='STILL', l2='WORKING', col=blue),
                                     E('cal', (1300, 270, 1790, 660), 'nineteen', head='BORN 1960+', big='67', sub='FULL RETIREMENT AGE', col=gold, size=150)],
          'FULL RETIREMENT AGE: 67 IF BORN 1960 OR LATER', gold, psize=46),
]
# ---- 14: THE LIMIT ----
S[14] = [
    slide('THE 2027 EARNINGS LIMIT', 131, [E('big', (160, 260, 1100, 640), None, val='$25,560', sub='PER YEAR', size=190),
                                           E('card', (1240, 300, 1760, 620), 'month.', head='PER MONTH', val='$2,130', col=gold)],
          'YOU CAN EARN UP TO $25,560 A YEAR'),
    slide('ABOVE THE LIMIT', 132, [E('card', (200, 280, 760, 640), 'every', head='YOU EARN OVER', val='$2', sub='ABOVE THE LIMIT', col=blue, vsize=150),
                                   E('arrow', (790, 420, 1000, 500), 'benefits'),
                                   E('card', (1040, 280, 1700, 640), 'benefits', head='HELD BACK', val='$1', sub='OF BENEFITS', col=red, vsize=150, vcol=red)],
          '$1 HELD BACK FOR EVERY $2 OVER', red, (255, 255, 255)),
]
# ---- 15: FRANK'S NUMBERS ----
S[15] = [
    slide("FRANK'S NUMBERS", 133, [E('person', (130, 260, 700, 700), None, letter='F', name='FRANK, 63', line='CLAIMED EARLY', line2='PART TIME JOB', col=blue),
                                   E('step', (820, 290, 1790, 420), 'pays', n=1, text='HIS JOB PAYS', val='$35,560'),
                                   E('step', (820, 460, 1790, 590), 'limit.', n=2, text='OVER THE LIMIT BY', val='$10,000', vc=red)],
          'EXACTLY $10,000 OVER THE LIMIT', red, (255, 255, 255)),
    slide('ONE DOLLAR FOR EVERY TWO', 134, [E('card', (160, 290, 700, 640), None, head='OVER THE LIMIT', val='$10,000', col=blue),
                                            E('op', (720, 390, 840, 540), 'dollar', t='÷2'),
                                            E('card', (870, 290, 1760, 640), 'five', head='HELD BACK FROM FRANK', val='$5,000', sub='OF HIS BENEFITS', col=red, vcol=red, vsize=130)],
          '$5,000 OF HIS BENEFITS HELD BACK', red, (255, 255, 255)),
]
# ---- 16: COMPARE ----
S[16] = [
    slide('NOW COMPARE', 135, [E('card', R2[0], None, head='FRANK EARNS', val='$25,000', sub='INSTEAD OF $35,560', col=blue),
                               E('card', R2[1], 'under', head='HELD BACK', val='$0', sub='UNDER THE LIMIT', col=green, vcol=green)],
          'UNDER THE LIMIT, NOTHING IS HELD BACK', green),
    slide('A CHOICE, NOT A SURPRISE', 136, [E('icard', R3[0], None, icon='brief', l1='SAME JOB', col=blue),
                                            E('icard', R3[1], 'fewer', icon='clock', l1='FEWER HOURS', col=gold),
                                            E('icard', R3[2], 'full', icon='check', l1='FULL CHECK', l2='EVERY MONTH', col=green, c2=green)],
          'MAKE THAT CHOICE ON PURPOSE', green),
]
# ---- 17: 5,000 ----
S[17] = [
    slide('$5,000 FRANK DID NOT SEE', 137, [E('big', (200, 260, 1000, 640), None, val='-$5,000', sub='HELD BACK', size=200, vcol=red),
                                            E('pay', (1100, 280, 1760, 640), 'bigger,', amount='+3.6%', head="FRANK'S CHECK", sub='LOOKED BIGGER', col=gold, size=120)],
          'THE RAISE MADE HIS CHECK LOOK BIGGER', red, (255, 255, 255), psize=50),
    slide('WHAT MARY SAID', 138, [E('person', (500, 260, 1420, 700), None, letter='M', name='MARY', line='THE RAISE IS NOT', line2='THE ONLY NUMBER THAT MATTERS', col=gold)],
          'NOT THE ONLY NUMBER THAT MATTERS'),
]
# ---- 18: YEAR YOU REACH FRA ----
S[18] = [
    slide('THE YEAR YOU REACH FULL AGE', 139, [E('card', (130, 280, 640, 640), None, head='BEFORE', val='$25,560', sub='$1 FOR EVERY $2', col=blue, vsize=86),
                                               E('arrow', (660, 420, 820, 500), 'jumps'),
                                               E('card', (840, 260, 1790, 660), 'jumps', head='YEAR YOU REACH FULL AGE', val='$67,920', sub='$1 FOR EVERY $3 ABOVE', col=green, vcol=green, vsize=130)],
          'THE LIMIT JUMPS TO $67,920', green),
    slide('ONLY THE MONTHS BEFORE', 140, [E('cal', (640, 260, 1280, 680), None, head='ONLY MONTHS', big='BEFORE', sub='YOUR BIRTHDAY MONTH', col=gold, size=110)],
          'ONLY THE MONTHS BEFORE YOUR BIRTHDAY MONTH', gold, psize=48),
]
# ---- 19: NO LIMIT ----
S[19] = [
    slide('FROM FULL RETIREMENT AGE', 141, [E('icard', R2[0], None, icon='lock', l1='NO LIMIT', l2='AT ALL', col=green, c2=green, s=1.0),
                                            E('icard', R2[1], 'any', icon='coins', l1='EARN ANY AMOUNT', l2='KEEP YOUR FULL CHECK', col=gold)],
          'NO LIMIT, FULL CHECK', green),
]
# ---- 20: NOT GONE ----
S[20] = [
    slide('WHAT MOST PEOPLE GET WRONG', 142, [E('icard', (500, 260, 1420, 690), None, icon='cross', l1='THE MONEY IS GONE?', l2='NOT SIMPLY GONE', col=red, c2=green)],
          'HELD BACK IS NOT SIMPLY GONE', green),
    slide('THE RECALCULATION', 143, [E('cal', (130, 270, 620, 660), 'reach', head='AT FULL AGE', big='67', sub='RECALCULATED', col=gold, size=150),
                                     E('arrow', (640, 420, 780, 500), 'credit'),
                                     E('icard', (800, 270, 1290, 660), 'credit', icon='check', l1='CREDIT FOR', l2='WITHHELD MONTHS', col=green, c2=green),
                                     E('arrow', (1310, 420, 1430, 500), 'goes'),
                                     E('icard', (1450, 270, 1790, 660), 'goes', icon='chart', l1='CHECK', l2='GOES UP', col=green, c2=green)],
          'YOUR MONTHLY CHECK GOES UP FROM THEN ON', green, psize=48),
    slide('DELAYED, NOT DELETED', 144, [E('stamp', (300, 330, 900, 500), None, t='DELAYED', col=gold, size=90, ang=-6),
                                        E('stamp', (1020, 330, 1620, 500), 'deleted.', t='NOT DELETED', col=green, size=90, ang=6),
                                        E('line', (360, 590, 1560, 660), 'plan', t='PLAN FOR THE GAP', size=60, col=goldL)],
          'BUT YOU STILL NEED TO PLAN FOR THE GAP'),
]
# ---- 21: NUMBER FOUR, TAXABLE MAX ----
S[21] = [
    slide('NUMBER 4: THE TAXABLE MAXIMUM', 145, [E('icard', (160, 260, 880, 690), None, icon='form', l1='STILL WORKING?', l2='SOCIAL SECURITY TAX', col=gold),
                                                 E('ring', (1040, 240, 1720, 720), 'six', val='6.2%', sub='OF YOUR WAGES', col=red, frac=0.062 * 6)],
          '6.2% ON YOUR WAGES, UP TO A CEILING', red, (255, 255, 255)),
    slide('THE 2027 CEILING', 146, [E('bars', (300, 250, 1620, 700), 'rises', vals=[('2026', 184500, '$184,500'), ('2027', 192300, '$192,300')], lo=0.75)],
          'THE CEILING RISES TO $192,300'),
]
# ---- 22: ABOVE THE LINE ----
S[22] = [
    slide('ABOVE THE CEILING', 147, [E('icard', R2[0], None, icon='check', l1='SOCIAL SECURITY TAX', l2='STOPS FOR THE YEAR', col=green, c2=green),
                                     E('icard', R2[1], 'medicare', icon='form', l1='MEDICARE TAX', l2='NO CEILING', col=red, c2=red)],
          'MEDICARE TAX KEEPS GOING ON EVERY DOLLAR', red, (255, 255, 255), psize=48),
    slide('WHO IT TOUCHES', 148, [E('card', R3[0], None, head='SELF-EMPLOYED', val='12.4%', sub='BOTH HALVES', col=gold),
                                  E('card', R3[1], 'most', head='MOST RETIREES', val='NO CHANGE', col=blue, vsize=70),
                                  E('card', R3[2], 'high', head='HIGH EARNER STILL WORKING', val='+$484', sub='MORE TAX', col=red, vcol=red)],
          'ABOUT $484 MORE FOR A HIGH EARNER', red, (255, 255, 255)),
]
# ---- 23: NUMBER FIVE, WORK CREDIT ----
S[23] = [
    slide('NUMBER 5: A WORK CREDIT', 149, [E('ring', (160, 240, 760, 720), None, val='40', sub='CREDITS NEEDED', col=gold, frac=1.0, size=150),
                                           E('icard', (900, 270, 1760, 660), 'ten', icon='brief', l1='ABOUT 10 YEARS', l2='OF WORK', col=blue)],
          'YOU NEED 40 CREDITS TO QUALIFY'),
    slide('THE PRICE OF ONE CREDIT', 150, [E('bars', (300, 250, 1620, 700), None, vals=[('2026', 1890, '$1,890'), ('2027', 1970, '$1,970')], lo=0.7)],
          'ONE CREDIT = $1,970 OF EARNINGS'),
]
# ---- 24: FOUR A YEAR ----
S[24] = [
    slide('MAX 4 CREDITS A YEAR', 151, [E('card', (160, 290, 560, 640), None, head='CREDITS', val='4', col=gold, vsize=150),
                                        E('op', (570, 390, 650, 540), 'need', t='x'),
                                        E('card', (660, 290, 1060, 640), 'need', head='PER CREDIT', val='$1,970', col=gold),
                                        E('op', (1070, 390, 1150, 540), 'seven', t='='),
                                        E('card', (1160, 290, 1760, 640), 'seven', head='FOR ALL FOUR', val='$7,880', col=green, vcol=green, vsize=120)],
          '$7,880 OF EARNINGS FOR ALL FOUR', green),
    slide('A FEW CREDITS SHORT?', 152, [E('person', (500, 260, 1420, 700), None, letter='?', name='YOU OR YOUR SPOUSE', line='SHORT OF 40 CREDITS?', line2='THIS NUMBER MATTERS', col=gold)],
          'IT MATTERS IF YOU ARE SHORT OF 40'),
]
# ---- 25: MAX BENEFIT ----
S[25] = [
    slide('ONE MORE NUMBER: THE MAXIMUM', 153, [E('bars', (200, 250, 1100, 700), 'maximum', vals=[('2026', 4152, '$4,152'), ('2027', 4188, '$4,188')], lo=0.8),
                                                E('card', (1240, 300, 1760, 640), None, head='AT FULL AGE', val='MAX', sub='PER MONTH', col=gold)],
          'THE MAXIMUM AT FULL AGE: $4,188'),
    slide('VERY FEW PEOPLE GET IT', 154, [E('ring', (180, 240, 760, 720), None, val='35', sub='YEARS', col=gold, size=150),
                                          E('icard', (900, 270, 1760, 660), 'taxable', icon='chart', l1='EARNINGS AT OR ABOVE', l2='THE TAXABLE MAXIMUM', col=blue)],
          '35 YEARS AT THE TAXABLE MAXIMUM', gold, psize=50),
]
# ---- 26: RECAP ----
S[26] = [
    slide('THE 5 NEW NUMBERS', 155, [E('step', (230, 235, 1690, 335), None, n=1, text='THE RAISE', val='+3.6%'),
                                     E('step', (230, 350, 1690, 450), 'two:', n=2, text='SSI, ONE PERSON', val='$1,029'),
                                     E('step', (230, 465, 1690, 565), 'three:', n=3, text='EARNINGS LIMIT', val='$25,560'),
                                     E('step', (230, 580, 1690, 680), 'four:', n=4, text='TAX CEILING', val='$192,300')],
          'FOUR DOWN, ONE TO GO'),
    slide('AND NUMBER 5', 156, [E('step', (330, 300, 1590, 440), None, n=5, text='ONE WORK CREDIT', val='$1,970'),
                                E('line', (330, 520, 1590, 600), 'seventy', t='ALL OFFICIAL FOR 2027', size=56, col=goldL)],
          'FIVE NUMBERS FOR 2027', green),
]
# ---- 27: THREE THINGS ----
S[27] = [
    slide('3 THINGS TO DO THIS WEEK', 157, [E('step', (230, 260, 1690, 400), None, n=1, text='TURN ON PAPERLESS NOTICES', val='BY NOV 18'),
                                            E('step', (230, 430, 1690, 570), 'second,', n=2, text='CLAIMED EARLY? CHECK YOUR EARNINGS', val='$25,560'),
                                            E('step', (230, 600, 1690, 740), 'third,', n=3, text='WATCH THE PART B ANNOUNCEMENT', val='2027')],
          'THAT DECIDES WHAT YOU REALLY KEEP', gold, psize=50),
]
# ---- 28: FRANK & MARY ----
S[28] = [
    slide('WHAT FRANK DID', 158, [E('person', (130, 260, 700, 700), None, letter='F', name='FRANK', line='CALLED SOCIAL SECURITY', line2='REPORTED HIS EARNINGS', col=blue),
                                  E('icard', (850, 270, 1760, 660), 'surprise', icon='check', l1='NO SURPRISE', l2='IN THE MIDDLE OF THE YEAR', col=green, c2=green)],
          'NO MID-YEAR SURPRISE', green),
    slide('SAME RAISE, TWO YEARS', 159, [E('person', R2[0], None, letter='M', name='MARY', line='UPDATED HER BUDGET', line2='WITH THE NEW AMOUNT', col=gold),
                                         E('person', R2[1], 'same', letter='F', name='FRANK', line='PLANNED HIS EARNINGS', line2='UNDER THE RULES', col=blue)],
          'SAME RAISE, TWO VERY DIFFERENT YEARS'),
]
# ---- 29: SHARE + COMMENT ----
S[29] = [
    slide('SEND IT TO ONE PERSON', 160, [E('icard', (500, 260, 1420, 690), None, icon='phone', l1='SOMEONE ON SOCIAL SECURITY', l2='ESPECIALLY IF THEY STILL WORK', col=gold)],
          'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 161, [E('line', (260, 360, 1660, 450), None, t='IS THE RAISE ENOUGH', size=96, col=white),
                                           E('line', (260, 480, 1660, 570), 'enough', t='FOR YOU THIS YEAR?', size=96, col=goldL)],
          'ANSWER IN THE COMMENTS'),
]
# ---- 30: DISCLAIMER (slide finale identica in ogni video) ----
S[30] = [frozen(final_slide)]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
_c = round((V.at(4, 'that is about') - 0.1) * 30); SPEC[4] = [_c, sum(SPEC[4]) - _c]   # taglio alla frase dei $75
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v9', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
