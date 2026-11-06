"""Video 12 - The $6,000 Senior Tax Deduction - 20 blocchi. Uso: python3 v12.py render|preview|check|spec <blocco> [slide,slide]
Layout nuovi rispetto ai video 8-11: modulo Schedule 1-A che si compila riga per riga, pila di deduzioni, bilancia, grafico del fase-out con marcatori,
equazioni a schede, tabelle, anello 85%, fonte IRS in alto a destra e etichetta di sezione in alto a sinistra."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v12eng import *

R2 = row(2); R3 = row(3); R4 = row(4, gap=36)
IRS = 'IRS.GOV'
T1, T2, T3, T4, T5, T6 = 'THE DEDUCTION', 'YOUR NUMBER', 'SOCIAL SECURITY', 'THE LIMIT', 'NO DEDUCTION', 'THIS YEAR'
S = {}
# ---- 1: HOOK ----
S[1] = [
    slide('A NEW TAX DEDUCTION', 501, [E('big', (150, 250, 800, 690), 'six thousand', val='$6,000', sub='EXTRA DEDUCTION', size=200, vcol=gold),
                                       E('ring', (850, 250, 1290, 690), 'people over', val='65+', sub='OR OLDER', frac=1.0, col=green, size=110),
                                       E('tline', (1330, 250, 1770, 700), 'twenty twenty-eight', pts=[('2025', None, gold), ('2028', None, green)], span=(0, 1, 'YEARS', green))],
          'FOR PEOPLE OVER 65', gold, src=IRS),
    slide('WHO GETS IT?', 502, [E('icard', R3[0], 'get all', icon='check', l1='ALL OF IT', l2='SOME SENIORS', col=green, c2=green),
                                E('icard', R3[1], 'only part', icon='chart', l1='PART OF IT', l2='SOME SENIORS', col=gold, c2=gold),
                                E('icard', R3[2], 'nothing at', icon='cross', l1='NOTHING', l2='SOME SENIORS', col=red, c2=red)],
          'WHICH ONE ARE YOU?', gold),
    slide('STRAIGHT FROM THE IRS', 503, [E('icard', (150, 260, 760, 700), 'every number', icon='form', l1='EVERY NUMBER', l2='FROM THE IRS', col=gold, s=1.0),
                                         E('big', (900, 280, 1500, 640), 'one line', val='1 LINE', sub='MOST PEOPLE FORGET', size=170, vcol=goldL),
                                         E('stamp', (1560, 560, 1790, 690), 'forget', t='?', col=red, ang=8, size=120)],
          'THE ONE LINE MOST PEOPLE MISS', red, (255, 255, 255), src=IRS),
]
# ---- 2: THREE PEOPLE ----
S[2] = [
    slide('MEET THE THREE', 504, [E('person', R3[0], 'dolores', letter='D', name='DOLORES, 67', line='SINGLE', line2='SOCIAL SECURITY + IRA', col=gold),
                                  E('person', R3[1], 'tom is', letter='T', name='TOM 70 + RUTH 62', line='MARRIED', line2='RUTH STILL WORKS', col=blue),
                                  E('person', R3[2], 'hank', letter='H', name='HANK, 68', line='BIG PENSION', line2='BIG IRA', col=green)],
          'THREE VERY DIFFERENT RESULTS', gold),
    slide('WHAT EACH WANTS TO KNOW', 505, [E('card', R3[0], 'dolores wants', head='DOLORES', val='HOW MUCH TAX?', sub='SHE PAYS', col=gold, vsize=52),
                                           E('card', R3[1], 'tom and ruth', head='TOM AND RUTH', val='WHAT CAN WE CLAIM?', sub='AS A COUPLE', col=blue, vsize=46),
                                           E('card', R3[2], 'hank wants', head='HANK', val='WHY IS IT SO SMALL?', sub='HIS DEDUCTION', col=green, vsize=46)],
          'KEEP AN EYE ON RUTH', gold),
]
# ---- 3: SOURCES ----
S[3] = [
    slide('ALL FROM THE IRS', 507, [E('icard', R4[0], 'publication five', icon='doc', l1='PUB. 554', l2='TAX GUIDE FOR SENIORS', col=gold),
                                    E('icard', R4[1], 'schedule one', icon='form', l1='SCHEDULE 1-A', l2='THE FORM ITSELF', col=gold),
                                    E('icard', R4[2], 'nine fifteen', icon='doc', l1='PUB. 915', l2='SOCIAL SECURITY TAXES', col=gold),
                                    E('icard', R4[3], 'inflation', icon='chart', l1='2026 RULES', l2='INFLATION NUMBERS', col=gold)],
          'EVERY NUMBER IS OFFICIAL', gold, src=IRS),
    slide('NOT FROM THE NEWS', 508, [E('icard', (250, 260, 920, 700), 'nothing here', icon='cross', l1='THE NEWS', l2='NOT A SOURCE', col=red, c2=red),
                                     E('icard', (1000, 260, 1670, 700), 'every example', icon='check', l1='IRS FORMS', l2='EXACT STEPS', col=green, c2=green)],
          "FIRST: WHAT IT IS", gold, src=IRS),
]
# ---- 4: PART ONE ----
S[4] = [
    slide('PART ONE: THE DEDUCTION', 509, [E('tline', (1290, 250, 1770, 700), 'running through', pts=[('2025', None, gold), ('2028', None, green)], span=(0, 1, 'THESE YEARS', green)),
                                           E('ring', (800, 250, 1240, 690), 'sixty-five or', val='65+', sub='AGE', frac=1.0, col=green, size=110),
                                           E('big', (150, 250, 760, 690), 'six thousand dollars', val='$6,000', sub='PER PERSON', size=190, vcol=gold)],
          'EXTRA DEDUCTION FOR SENIORS', gold, tag=T1, src=IRS),
    slide('COUPLES', 510, [E('card', (150, 280, 650, 690), 'married couple', head='SPOUSE 1', val='$6,000', sub='AGE 65+', col=gold, vsize=100),
                           E('card', (710, 280, 1210, 690), 'both spouses', head='SPOUSE 2', val='$6,000', sub='AGE 65+', col=gold, vsize=100),
                           E('card', (1270, 280, 1770, 690), 'twelve thousand', head='TOTAL', val='$12,000', sub='BOTH QUALIFY', col=green, vcol=green, vsize=90)],
          'BOTH MUST QUALIFY', gold, tag=T1, src=IRS),
    slide('WHEN YOU COUNT AS 65', 511, [E('cal', (150, 270, 780, 680), 'counts you', head='THE DAY BEFORE', big='BIRTHDAY', sub='IRS COUNTS YOU AS 65', size=90, col=gold),
                                        E('arrow', (790, 400, 960, 540), 'what matters', col=goldL),
                                        E('cal', (980, 270, 1770, 680), 'by the last', head='BY THE LAST DAY', big='TAX YEAR', sub='AGE 65 REACHED', size=100, col=green)],
          'REACH 65 BY THE END OF THE YEAR', gold, tag=T1, src=IRS),
    slide('STANDARD OR ITEMIZE', 512, [E('icard', (250, 260, 920, 700), 'whether you take', icon='check', l1='STANDARD DEDUCTION', l2='YOU CAN CLAIM IT', col=green, c2=green),
                                       E('icard', (1000, 260, 1670, 700), 'or itemize', icon='check', l1='ITEMIZE', l2='YOU CAN CLAIM IT', col=green, c2=green)],
          'WORKS EITHER WAY', green, tag=T1, src=IRS),
]
# ---- 5: HOW TO CLAIM ----
S[5] = [
    slide('WHERE YOU CLAIM IT', 513, FORM((150, 250, 1280, 700), 'SCHEDULE 1-A', [('V', 'ENHANCED DEDUCTION FOR SENIORS', '$ ______')],
                                          ['part five'], right='PART 5', first='schedule one', hl=(0,)) +
          [E('icard', (1350, 260, 1770, 700), 'form ten', icon='form', l1='FORM 1040', l2='YOUR TAX RETURN', col=gold, s=0.9)],
          'ONE LINE ON ONE FORM', gold, tag=T1, src=IRS),
    slide('IT IS NOT AUTOMATIC', 514, [E('icard', (250, 260, 920, 700), 'does not apply', icon='cross', l1='THE IRS', l2='DOES NOT APPLY IT', col=red, c2=red),
                                       E('icard', (1000, 260, 1670, 700), 'social security check', icon='cross', l1='YOUR SS CHECK', l2='DOES NOT INCLUDE IT', col=red, c2=red)],
          'NOBODY ADDS IT FOR YOU', red, (255, 255, 255), tag=T1, src=IRS),
    slide('ASK FOR IT BY NAME', 515, [E('card', (150, 290, 880, 640), 'ask your', head='THE OFFICIAL NAME', val='ENHANCED DEDUCTION', sub='FOR SENIORS', col=gold, vsize=66),
                                      E('icard', (960, 270, 1770, 690), 'make sure', icon='doc', l1='MAKE SURE THE BOX', l2='IS FILLED IN', col=green, c2=green)],
          'SAY IT TO YOUR PREPARER', gold, tag=T1, src=IRS),
]
# ---- 6: DOLORES STACK ----
S[6] = [
    slide("DOLORES' DEDUCTION STACK", 516, [E('person', (150, 250, 560, 700), None, letter='D', name='DOLORES', line='67, SINGLE', col=gold),
                                            E('seg', (640, 540, 1260, 700), 'sixteen thousand', label='STANDARD', val='$16,100', fill=blue, tc=white),
                                            E('seg', (640, 440, 1260, 530), 'two thousand', label='AGE 65+ EXTRA', val='$2,050', fill=gold),
                                            E('seg', (640, 290, 1260, 430), 'new six', label='NEW SENIOR', val='$6,000', fill=green)],
          'THREE LAYERS, ONE DEDUCTION', gold, tag=T2, src=IRS),
    slide('ADD IT UP', 517, [E('big', (250, 260, 1670, 560), 'twenty-four thousand', val='$24,150', sub="DOLORES' INCOME THAT IS NOT TAXED", size=230, vcol=green),
                             E('stamp', (1250, 600, 1700, 720), 'write', t='WRITE IT DOWN', col=gold, ang=-5, size=70)],
          'THE FIRST NUMBER', green, tag=T2, src=IRS),
]
# ---- 7: COUPLE STACK ----
S[7] = [
    slide('A COUPLE FILING JOINTLY', 518, [E('card', (150, 260, 560, 700), 'thirty-two thousand', head='STANDARD', val='$32,200', sub='JOINTLY', col=blue, vsize=70),
                                           E('op', (560, 420, 640, 540), 'add sixteen', t='+', size=100),
                                           E('card', (640, 260, 1060, 700), 'add sixteen', head='AGE 65+', val='2 × $1,650', sub='ONE EACH', col=gold, vsize=62),
                                           E('op', (1060, 420, 1140, 540), 'six thousand dollars each', t='+', size=100),
                                           E('card', (1140, 260, 1550, 700), 'six thousand dollars each', head='SENIOR', val='2 × $6,000', sub='ONE EACH', col=green, vsize=62),
                                           E('big', (1560, 330, 1790, 650), 'forty-seven', val='$47,500', sub='TOTAL', size=60, vcol=goldL)],
          'BOTH SPOUSES 65 OR OLDER', gold, tag=T2, src=IRS),
    slide('ONLY ONE SPOUSE 65+?', 519, [E('person', (150, 260, 880, 700), 'if only one', letter='+', name='SPOUSE OVER 65', line='THEIR EXTRA AMOUNTS COUNT', col=green),
                                        E('person', (950, 260, 1770, 700), 'only that', letter='-', name='SPOUSE UNDER 65', line='NO EXTRA AMOUNTS', col=red)],
          'ONLY THAT SPOUSE COUNTS', gold, tag=T2, src=IRS),
    slide('MOSTLY SOCIAL SECURITY?', 520, [E('icard', (200, 270, 930, 690), 'mostly on', icon='coins', l1='MANY COUPLES', l2='LIVING ON SOCIAL SECURITY', col=gold),
                                           E('big', (1020, 260, 1740, 640), 'no federal', val='$0', sub='FEDERAL INCOME TAX', size=250, vcol=green)],
          'FOR MANY COUPLES, THIS CAN MEAN', green, tag=T2, src=IRS),
]
# ---- 8: NOT A CHECK ----
S[8] = [
    slide('A DEDUCTION IS NOT A CHECK', 521, [E('big', (150, 260, 760, 640), 'six thousand dollar', val='$6,000', sub='NOT A CHECK', size=180, vcol=red),
                                                                                            E('arrow', (790, 400, 960, 540), 'lowers', col=goldL),
                                              E('icard', (1000, 260, 1770, 700), 'lowers', icon='form', l1='LOWERS THE INCOME', l2='YOU ARE TAXED ON', col=green, c2=green)],
          'WHAT IT SAVES DEPENDS ON YOUR BRACKET', gold, tag=T2, src=IRS),
    slide('WHAT IT REALLY SAVES', 522, [E('card', (150, 260, 880, 620), 'twelve percent', head='12% BRACKET', val='$720', sub='$6,000 × 12%', col=gold, vsize=170, icon=None),
                                        E('card', (960, 260, 1770, 620), 'twenty-two percent', head='22% BRACKET', val='$1,320', sub='$6,000 × 22%', col=green, vcol=green, vsize=150),
                                        E('line', (150, 650, 1770, 710), 'real money', t='REAL MONEY, BUT NOT $6,000', size=52, col=goldL)],
          'SAVINGS = $6,000 × YOUR RATE', gold, tag=T2, src=IRS),
    slide('NOT WHAT THE FORM DOES', 523, [E('icard', (250, 260, 920, 700), 'many videos', icon='cross', l1='"YOU SAVE $6,000"', l2='NOT WHAT THE FORM DOES', col=red, c2=red),
                                          E('icard', (1000, 260, 1670, 700), 'that is not', icon='check', l1='$6,000 × YOUR RATE', l2='WHAT YOU REALLY SAVE', col=green, c2=green)],
          'DO NOT BELIEVE THE HYPE', red, (255, 255, 255), tag=T2, src=IRS),
]
# ---- 9: DOLORES' YEAR ----
S[9] = [
    slide("DOLORES' YEAR", 524, [E('seg', (150, 280, 1000, 380), 'twenty-four thousand dollars a year', label='SOCIAL SECURITY', val='$24,000', fill=blue, tc=white),
                                 E('seg', (150, 400, 1000, 500), 'thirty thousand', label='IRA WITHDRAWALS', val='$30,000', fill=gold),
                                 E('card', (1080, 260, 1770, 690), 'eleven thousand three', head='IRS WORKSHEET', val='$11,300', sub='OF HER SOCIAL SECURITY IS TAXABLE', col=red, vcol=red, vsize=100)],
          'ONLY PART OF IT IS TAXABLE', gold, tag=T2, src='IRS PUB. 915'),
    slide('HER TAX RETURN', 525, FORM((150, 250, 1770, 710), "DOLORES  ·  2026  ·  FEDERAL", [('A', 'IRA WITHDRAWALS', '$30,000'), ('B', '+ TAXABLE SOCIAL SECURITY', '$11,300'), ('C', '= INCOME ON THE RETURN', '$41,300'),
                                                                                             ('D', '− DEDUCTIONS ($16,100 + $2,050 + $6,000)', '$24,150'), ('E', '= TAXED ON', '$17,150')],
                                     ['her income', 'return is', 'forty-one thousand', 'after her', 'she is taxed'], right='SINGLE', hl=(4,)),
          'FROM INCOME TO TAXED INCOME', gold, tag=T2, src=IRS),
]
# ---- 10: HER TAX ----
S[10] = [
    slide('HER FEDERAL INCOME TAX', 526, [E('scale', (150, 240, 1250, 720), None, xs=[360, 1040]),
                                          E('pan', (170, 430, 550, 660), 'eighteen hundred', label='WITH THE DEDUCTION', val='$1,810', col=green),
                                          E('pan', (850, 430, 1230, 660), 'without the', label='WITHOUT IT', val='$2,530', col=red),
                                          E('big', (1290, 290, 1780, 650), 'seven hundred', val='$720', sub='SAVED EVERY YEAR', size=150, vcol=goldL)],
          'FROM ONE LINE ON ONE FORM', green, tag=T2, src=IRS),
    slide('STILL TAXED', 527, [E('icard', (150, 260, 760, 700), 'part of her', icon='coins', l1='HER SOCIAL SECURITY', l2='PART IS STILL TAXED', col=red, c2=red),
                               E('stamp', (880, 330, 1500, 520), 'tax free', t='NOT TAX FREE', col=red, ang=-6, size=100),
                               E('line', (820, 590, 1770, 660), 'your own', t='RUN YOUR OWN NUMBERS', size=56, col=goldL)],
          'THE DEDUCTION DOES NOT CHANGE THAT', red, (255, 255, 255), tag=T2, src=IRS),
]
# ---- 11: SS ONLY ----
S[11] = [
    slide('ONLY SOCIAL SECURITY?', 528, [E('card', (150, 260, 560, 700), 'thirty thousand', head='SINGLE PERSON', val='$30,000', sub='IN BENEFITS', col=gold, vsize=80),
                                         E('gauge', (620, 240, 1560, 720), 'counts half', limit=25000, val=15000, top=30000, lim_l='$25,000 LINE', label='HALF = $15,000', col=green),
                                         E('stamp', (1300, 540, 1740, 690), 'none of', t='NOT TAXED', col=green, ang=-6, size=76)],
          'FAR BELOW THE LINE', green, tag=T3, src='IRS PUB. 915'),
    slide('WHAT ADDS THE TAX', 529, [E('icard', R4[0], 'i r a', icon='bank', l1='AN IRA', col=gold, s=0.6),
                                     E('icard', R4[1], 'pension', icon='brief', l1='A PENSION', col=gold),
                                     E('icard', R4[2], 'interest', icon='coins', l1='INTEREST', col=gold),
                                     E('icard', R4[3], 'work income', icon='wallet', l1='WORK INCOME', col=gold)],
          'ON TOP OF THE BENEFITS', gold, tag=T3, src='IRS PUB. 915'),
]
# ---- 12: HOW SS IS TAXED ----
S[12] = [
    slide('HOW THE IRS TAXES BENEFITS', 530, [E('card', (150, 280, 880, 640), 'adds half', head='HALF OF', val='YOUR BENEFITS', col=gold, vsize=60, icon='coins', s=0.7),
                                              E('op', (880, 400, 1040, 520), 'other income', t='+', size=150),
                                              E('card', (1040, 280, 1770, 640), 'other income', head='YOUR', val='OTHER INCOME', col=blue, vsize=60, icon='wallet', s=0.7),
                                              E('line', (150, 665, 1770, 725), 'the i r s adds', t='THE IRS ADDS THEM TOGETHER', size=50, col=goldL)],
          'THE IRS ADDS THEM UP', gold, tag=T3, src='IRS PUB. 915'),
    slide('THE TWO LINES', 531, GRID((150, 250, 1180, 710), ['TOTAL ABOVE', 'SINGLE', 'COUPLE'], [0.34, 0.33, 0.33], [('PART TAXABLE', '$25,000', '$32,000'), ('UP TO 85%', '$34,000', '$44,000')],
                                     ['above twenty-five', 'above thirty-four'], first='if that total') +
          [E('ring', (1250, 260, 1770, 700), 'never more', val='85%', sub='NEVER MORE', frac=0.85, col=red, size=110)],
          'UP TO 85% CAN BE TAXED', red, (255, 255, 255), tag=T3, src='IRS PUB. 915'),
]
# ---- 13: THE LIMIT ----
S[13] = [
    slide('WHO LOSES PART OF IT', 532, [E('phase', (150, 240, 1100, 720), 'shrinks', a_l='$75K', b_l='$175K'),
                                        E('card', (1180, 260, 1770, 440), 'seventy-five thousand', head='SINGLE', val='$75,000', col=gold, vsize=64),
                                        E('card', (1180, 480, 1770, 660), 'one hundred fifty', head='JOINT', val='$150,000', col=blue, vsize=64)],
          'THE DEDUCTION SHRINKS ABOVE THE LINE', gold, tag=T4, src=IRS),
    slide('SIX PERCENT', 533, [E('big', (150, 260, 760, 640), 'six percent', val='6%', sub='OF EVERY DOLLAR ABOVE THE LINE', size=240, vcol=red),
                               E('arrow', (790, 400, 960, 540), 'off your', col=goldL),
                               E('card', (1000, 280, 1770, 690), 'off your', head='COMES OFF YOUR', val='$6,000', sub='SCHEDULE 1-A', col=gold, vsize=140)],
          'THE FORM TAKES IT OFF', red, (255, 255, 255), tag=T4, src=IRS),
    slide('COMPLETELY GONE AT', 534, [E('card', (250, 280, 920, 690), 'one hundred seventy-five', head='SINGLE', val='$175,000', sub='DEDUCTION = $0', col=red, vcol=red, vsize=100),
                                      E('card', (1000, 280, 1670, 690), 'two hundred fifty', head='COUPLE', val='$250,000', sub='DEDUCTION = $0', col=red, vcol=red, vsize=100)],
          'ABOVE THESE, NOTHING LEFT', red, (255, 255, 255), tag=T4, src=IRS),
]
# ---- 14: HANK ----
S[14] = [
    slide("HANK'S MATH", 535, [E('person', (150, 250, 560, 700), None, letter='H', name='HANK', line='68', col=green)] +
          FORM((620, 250, 1770, 700), 'HANK  ·  SINGLE', [('1', 'INCOME', '$140,000'), ('2', 'OVER THE $75,000 LINE', '$65,000'), ('3', '6% OF THAT', '$3,900'), ('4', '$6,000 − $3,900', '$2,100')],
               ['one hundred forty', 'sixty-five thousand', 'six percent of', 'twenty-one hundred'], right='2026', first='look at', hl=(3,)),
          'HIS DEDUCTION: $2,100', gold, tag=T4, src=IRS),
    slide('THE TRAP', 536, [E('phase', (150, 240, 1250, 720), 'the trap', a_l='$75K', b_l='$175K'),
                            E('pmark', (150, 240, 1250, 720), 'every extra', gbox=(150, 240, 1250, 720), inc=140000, val=2100, label='HANK $140K', sub='$2,100', mc=red, up=False, dx=-120),
                            E('card', (1330, 260, 1770, 500), 'sixty dollars', head='EVERY EXTRA $1,000', val='−$60', sub='OF THE DEDUCTION', col=red, vcol=red, vsize=80),
                            E('pmark', (150, 240, 1250, 720), 'twenty thousand dollars less', gbox=(150, 240, 1250, 720), inc=120000, val=3300, label='$120K', sub='$3,300', mc=green, dx=130),
                            E('card', (1330, 530, 1770, 710), 'twelve hundred', head='$20,000 LESS', val='+$1,200', col=green, vcol=green, vsize=60)],
          'EVERY EXTRA $1,000 COSTS $60', red, (255, 255, 255), tag=T4, src=IRS),
]
# ---- 15: WHO GETS NOTHING ----
S[15] = [
    slide('WHO GETS NOTHING', 537, [E('step', (150, 260, 1770, 380), 'married filing', n=1, text='MARRIED FILING SEPARATELY', val='NO DEDUCTION', vc=red),
                                    E('step', (150, 400, 1770, 520), 'each person needs', n=2, text='NO VALID SOCIAL SECURITY NUMBER', val='NO DEDUCTION', vc=red),
                                    E('step', (150, 540, 1770, 660), 'the age test', n=3, text='UNDER 65 (EACH PERSON)', val='NO DEDUCTION', vc=red)],
          'THREE WAYS TO LOSE IT', red, (255, 255, 255), tag=T5, src=IRS),
    slide('TOM AND RUTH', 538, [E('person', (150, 250, 700, 700), 'tom is seventy', letter='T', name='TOM, 70', line='CLAIMS $6,000', col=green),
                                E('person', (780, 250, 1330, 700), 'ruth is only', letter='R', name='RUTH, 62', line='CLAIMS $0', line2='UNTIL SHE REACHES 65', col=red),
                                E('big', (1360, 330, 1790, 620), 'claims nothing', val='$6,000', sub='FOR THE COUPLE', size=90, vcol=goldL)],
          'THE AGE TEST IS PER PERSON', gold, tag=T5, src=IRS),
]
# ---- 16: THIS YEAR ----
S[16] = [
    slide('STEP 1: CHECK YOUR INCOME', 539, [E('numcol', (150, 260, 600, 700), None, n=1, icon='clock', l1='BEFORE DEC. 31', l2='CHECK YOUR INCOME'),
                                              E('card', (680, 270, 1200, 690), 'withdrawal', head='AN IRA WITHDRAWAL', val='RAISES INCOME', col=gold, vsize=48, icon='bank', s=0.6),
                                              E('card', (1240, 270, 1770, 690), 'roth', head='A ROTH CONVERSION', val='RAISES INCOME', col=gold, vsize=48, icon='chart', s=0.7)],
          'CLOSE TO $75K OR $150K?', gold, tag=T6, src=IRS),
    slide('STEPS 2 AND 3', 540, [E('numcol', (250, 260, 900, 700), 'two if', n=2, icon='form', l1='REVIEW WITHHOLDING', l2='FORM W-4P'),
                                 E('numcol', (1020, 260, 1670, 700), 'ask for free', n=3, icon='bulb', l1='ASK FOR FREE HELP', l2='BEFORE YOU FILE')],
          'NO SURPRISE IN APRIL', green, tag=T6, src=IRS),
]
# ---- 17: W-4V ----
S[17] = [
    slide('TAX FROM YOUR SS CHECK', 541, [E('icard', (150, 270, 700, 690), 'form w four v', icon='form', l1='FORM W-4V', l2='VOLUNTARY WITHHOLDING', col=gold),
                                          E('arrow', (730, 400, 900, 540), 'from your', col=goldL),
                                          E('icard', (930, 270, 1770, 690), 'from your', icon='coins', l1='YOUR SOCIAL SECURITY CHECK', l2='TAX TAKEN OUT FOR YOU', col=green, c2=green)],
          'YOU CAN CHOOSE TO WITHHOLD', gold, tag=T6, src=IRS),
    slide('IF YOU DO NOT', 542, [E('icard', (250, 260, 920, 700), 'more withholding', icon='doc', l1='MORE WITHHOLDING', l2='FROM OTHER INCOME', col=gold),
                                 E('icard', (1000, 260, 1670, 700), 'estimated tax', icon='clock', l1='ESTIMATED TAX', l2='PAID DURING THE YEAR', col=gold)],
          'THE IRS SAYS YOU MAY HAVE TO', gold, tag=T6, src='IRS PUB. 915'),
    slide('PAY IT EVENLY', 543, [E('icard', (250, 260, 920, 700), 'evenly', icon='check', l1='PAID EVENLY', l2='ALL YEAR', col=green, c2=green),
                                 E('icard', (1000, 260, 1670, 700), 'one big', icon='cross', l1='ONE BIG PAYMENT', l2='IN APRIL', col=red, c2=red)],
          'THE DEDUCTION LOWERS YOUR BILL', gold, tag=T6, src=IRS),
]
# ---- 18: FREE HELP ----
S[18] = [
    slide('FREE HELP FROM THE IRS', 544, [E('icard', (150, 260, 860, 650), 'volunteer income', icon='doc', l1='VITA', l2='VOLUNTEER INCOME TAX ASSISTANCE', col=gold),
                                          E('icard', (910, 260, 1620, 650), 'tax counseling', icon='doc', l1='TCE', l2='TAX COUNSELING FOR THE ELDERLY', col=gold),
                                          E('line', (150, 670, 1770, 715), 'trained volunteers', t='TRAINED VOLUNTEERS AT SITES NEAR YOU', size=40, col=goldL)],
          'FREE, FROM THE IRS', green, tag=T6, src=IRS),
    slide('REMEMBER THE CLOCK', 545, [E('tline', (150, 260, 1250, 700), 'twenty twenty-five', pts=[('2025', None, green), ('2026', None, green), ('2027', None, green), ('2028', None, green)], span=(0, 3, 'CHECK IT EVERY YEAR', green)),
                                      E('card', (1330, 280, 1770, 690), 'hundreds', head='WORTH', val='$100s', sub='OF DOLLARS', col=gold, vsize=100)],
          'DEDUCTION YEARS: 2025 – 2028', gold, tag=T6, src=IRS),
]
# ---- 19: RECAP ----
S[19] = [
    slide('RECAP: 1 TO 3', 546, [E('rule', (180, 310, 1740, 440), 'one six', n=1, text='PER PERSON, AGE 65 OR OLDER', val='$6,000'),
                                 E('rule', (180, 460, 1740, 590), 'two it', n=2, text='STACKS ON YOUR STANDARD DEDUCTION', val='ON TOP'),
                                 E('rule', (180, 610, 1740, 740), 'three it', n=3, text='SAVES YOUR BRACKET × $6,000', val='NOT $6,000', vc=red)],
          'THREE NUMBERS TO KEEP', gold, tag=T1, src=IRS),
    slide('RECAP: 4 AND 5', 547, [E('rule', (180, 290, 1740, 460), 'four it shrinks', n=4, text='SHRINKS 6% ABOVE THE LINE', val='$75K / $150K', vc=red),
                                  E('rule', (180, 500, 1740, 670), 'five you need', n=5, text='JOINT FILING + SSN + AGE 65', val='EACH PERSON')],
          'TWO LIMITS TO CHECK', gold, tag=T1, src=IRS),
]
# ---- 20: CTA + DISCLAIMER ----
S[20] = [
    slide('SEND IT TO ONE PERSON', 548, [E('icard', (500, 260, 1420, 690), None, icon='mail', l1='SOMEONE OVER 65', l2='WHO FILES THEIR OWN TAXES', col=gold)],
          'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 549, [E('line', (260, 360, 1660, 450), None, t='SINGLE OR MARRIED?', size=96, col=white),
                                           E('line', (260, 480, 1660, 570), 'do you think', t='WILL YOU LOSE PART OF IT?', size=84, col=goldL)],
          'ANSWER IN THE COMMENTS'),
    frozen(final12),
]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
# tagli tra le slide sulla frase che apre la slide dopo (misurata sulla voce)
CUTS = {1: ['but the i r s rules', 'every number comes'], 2: ['dolores wants'], 3: ['nothing here comes'], 4: ['a married couple', 'the i r s counts', 'it works whether'],
        5: ['it does not come', 'ask your tax preparer'], 6: ['that is twenty-four'], 7: ['if only one spouse', 'for many couples'], 8: ['in the twelve percent', 'many videos say'],
        9: ['her income on'], 10: ['and notice that'], 11: ['the taxes come'], 12: ['if that total'], 13: ['the schedule one a takes', 'for a single person'],
        14: ['and here is the trap'], 15: ['tom is seventy'], 16: ['two if you have'], 17: ['if you do not', 'the deduction lowers'], 18: ['and remember the clock'],
        19: ['four it shrinks'], 20: ['and tell me', 'one last thing']}
for _b, _ph in CUTS.items():
    _tot = sum(SPEC[_b]); _c = [0] + [round((V.at(_b, p) - 0.2) * 30) for p in _ph] + [_tot]
    SPEC[_b] = [_c[i + 1] - _c[i] for i in range(len(_c) - 1)]
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v12', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
