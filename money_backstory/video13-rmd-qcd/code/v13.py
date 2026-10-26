"""Video 13 - RMD a 73 anni + Q C D - 20 blocchi. Uso: python3 v13.py render|preview|check|spec <blocco> [slide,slide]
Layout nuovi rispetto ai video 8-12: curva del fattore con marcatori, flusso a nodi con freccia barrata, barre verticali, equazioni a schede, tabelle riga per riga, modulo 1040, anelli prima/dopo."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v13eng import *

R2 = row(2); R3 = row(3); R4 = row(4, gap=36); R3b = row(3, y1=620); R3c = row(3, y1=590)
IRS = 'IRS.GOV'
T1, T2, T3, T4, T5, T6, T7 = 'THE BASICS', 'THE FORMULA', 'THE PENALTY', 'SOCIAL SECURITY TAX', 'THE Q C D MOVE', 'MORE RULES', 'YOUR CHECKLIST'
S = {}
# ---- 1: HOOK ----
S[1] = [
    slide('FORCED OUT OF YOUR I R A', 601, [E('icard', (150, 270, 700, 690), None, icon='bank', l1='YOUR I R A', l2='TRADITIONAL MONEY', col=gold),
                                            E('arrow', (730, 400, 900, 540), 'pull money', col=goldL),
                                            E('icard', (930, 270, 1770, 690), 'whether they', icon='wallet', l1='YOUR TAXABLE INCOME', l2='NEED IT OR NOT', col=red, c2=red)],
          'THE I R S FORCES IT OUT', red, (255, 255, 255), src=IRS),
    slide('REQUIRED MINIMUM DISTRIBUTION', 602, [E('big', (150, 250, 1000, 640), None, val='R M D', sub='REQUIRED MINIMUM DISTRIBUTION', size=210, vcol=gold),
                                                 E('stamp', (1060, 330, 1740, 520), 'every dollar', t='100% TAXABLE', col=red, ang=-6, size=90),
                                                 E('line', (150, 665, 1770, 720), 'of it is taxable', t='EVERY DOLLAR COUNTS AS INCOME', size=46, col=goldL)],
          'A FORCED WITHDRAWAL', gold, src=IRS),
    slide("WALTER'S NUMBER", 603, [E('person', (150, 250, 640, 700), None, letter='W', name='WALTER, 75', line='SINGLE', line2='TRADITIONAL I R A', col=gold),
                                   E('big', (720, 260, 1770, 690), 'thirty-two thousand five', val='$32,520', sub='MUST COME OUT THIS YEAR', size=220, vcol=red)],
          'HIS MINIMUM FOR THIS YEAR', red, (255, 255, 255), src=IRS),
    slide('ONE MOVE CAN CUT THE TAX', 604, [E('card', (150, 270, 860, 690), None, head='ONE MOVE', val='ALLOWED BY THE I R S', col=green, vsize=44, icon='check', s=0.8),
                                           E('big', (950, 260, 1770, 650), 'more than two thousand', val='$2,000+', sub='LESS TAX FOR WALTER', size=190, vcol=green)],
          'HERE ARE THE EXACT NUMBERS', green, src=IRS),
]
# ---- 2: MEET ----
S[2] = [
    slide('MEET WALTER', 605, [E('person', R3[0], None, letter='W', name='WALTER, 75', line='SINGLE', col=gold),
                               E('card', R3[1], 'eight hundred thousand', head='TRADITIONAL I R A', val='$800,000', col=gold, vsize=80, icon='bank', s=0.5),
                               E('card', R3[2], 'thirty thousand', head='SOCIAL SECURITY', val='$30,000', sub='A YEAR', col=blue, vsize=80, icon='coins', s=0.6)],
          'ONE I R A, ONE SOCIAL SECURITY CHECK', gold),
    slide('MEET LINDA', 606, [E('person', R3[0], None, letter='L', name='LINDA, 73', line='REACHES 73 THIS YEAR', col=green),
                              E('card', R3[1], 'five hundred thousand', head='HER I R A', val='$500,000', col=green, vcol=green, vsize=80, icon='bank', s=0.5),
                              E('card', R3[2], 'very first', head='FIRST EVER', val='REQUIRED DISTRIBUTION', col=red, vsize=40, icon='form', s=0.8)],
          'ABOUT TO FACE HER FIRST ONE', green),
    slide('TWO LESSONS', 607, [E('icard', (250, 260, 920, 700), 'how the tax works', icon='chart', l1="WALTER'S LESSON", l2='HOW THE TAX WORKS', col=gold),
                               E('icard', (1000, 260, 1670, 700), 'deadline trap', icon='clock', l1="LINDA'S LESSON", l2='THE DEADLINE TRAP', col=red, c2=red)],
          'WATCH BOTH', gold),
]
# ---- 3: SOURCES ----
S[3] = [
    slide('ALL FROM THE IRS', 608, [E('icard', R4[0], 'five ninety-b', icon='doc', l1='PUB. 590-B', l2='I R A DISTRIBUTIONS', col=gold),
                                    E('icard', R4[1], 'questions and answers', icon='doc', l1='I R S Q AND A', l2='RMD QUESTIONS', col=gold),
                                    E('icard', R4[2], 'fifty-three twenty-nine', icon='form', l1='FORM 5329', l2='THE PENALTY FORM', col=gold),
                                    E('icard', R4[3], 'nine fifteen', icon='doc', l1='PUB. 915', l2='SOCIAL SECURITY TAXES', col=gold)],
          'EVERY NUMBER IS OFFICIAL', gold, src=IRS),
    slide('NOT FROM THE NEWS', 609, [E('icard', R3b[0], None, icon='cross', l1='NEWS ARTICLES', l2='NOT A SOURCE', col=red, c2=red),
                                     E('icard', R3b[1], 'no guesses', icon='cross', l1='GUESSES', l2='NOT A SOURCE', col=red, c2=red),
                                     E('icard', R3b[2], 'exact steps', icon='check', l1='IRS FORMS', l2='EXACT STEPS', col=green, c2=green),
                                     E('line', (150, 665, 1770, 720), "let's start", t="FIRST: WHO HAS TO TAKE THE MONEY OUT?", size=46, col=goldL)],
          'EVERY EXAMPLE FOLLOWS THE FORMS', gold, src=IRS),
]
# ---- 4: BASICS ----
S[4] = [
    slide('PART ONE: THE BASICS', 610, [E('ring', (150, 250, 720, 700), 'seventy-three', val='73', sub='THE YEAR YOU REACH', frac=1.0, col=gold, size=130),
                                        E('tline', (800, 250, 1770, 700), 'you must start', pts=[('72', 'NO RMD YET', grey), ('73', 'FIRST RMD', gold), ('74', 'EVERY YEAR', green)])],
          'RMDs START THE YEAR YOU REACH 73', gold, tag=T1, src=IRS),
    slide('WHO MUST TAKE IT', 611, [E('icard', R2[0], 'traditional i r as', icon='bank', l1='TRADITIONAL I R A', l2='RMD APPLIES', col=green, c2=green),
                                    E('icard', R2[1], 'four oh one', icon='brief', l1='WORKPLACE PLANS', l2='LIKE A 401(K)', col=green, c2=green)],
          'BOTH ARE COVERED', green, tag=T1, src=IRS),
    slide('NO RMD IN YOUR LIFETIME', 612, [E('icard', R2[0], 'roth i r a', icon='check', l1='ROTH I R A', l2='NO RMD WHILE ALIVE', col=blue, c2=blue),
                                           E('icard', R2[1], 'designated roth', icon='check', l1='DESIGNATED ROTH', l2='NO RMD WHILE ALIVE', col=blue, c2=blue)],
          'ROTH MONEY IS EXEMPT', blue, (255, 255, 255), tag=T1, src=IRS),
    slide('TRADITIONAL MONEY ONLY', 613, [E('stamp', (250, 300, 1670, 520), 'hits traditional', t='TRADITIONAL ONLY', col=gold, ang=-4, size=100),
                                          E('line', (150, 640, 1770, 710), 'everything else', t='THE REST OF THE VIDEO IS ABOUT THIS MONEY', size=48, col=goldL)],
          'THIS RULE HITS ONE KIND OF MONEY', gold, tag=T1, src=IRS),
]
# ---- 5: FORMULA ----
S[5] = [
    slide('THE I R S FORMULA', 614, [E('card', (150, 280, 560, 690), 'account balance', head='BALANCE', val='DEC. 31', sub='OF LAST YEAR', col=gold, vsize=70),
                                     E('op', (560, 420, 640, 540), 'divide it', t='÷', size=120),
                                     E('card', (640, 280, 1060, 690), 'life expectancy', head='FACTOR', val='TABLE III', sub='UNIFORM LIFETIME', col=blue, vsize=56),
                                     E('op', (1060, 420, 1140, 540), 'uniform lifetime', t='=', size=120),
                                     E('card', (1140, 280, 1770, 690), 'lifetime table', head='YOUR MINIMUM', val='RMD', sub='FOR THIS YEAR', col=green, vcol=green, vsize=100)],
          'BALANCE ÷ FACTOR = YOUR RMD', gold, tag=T2, src='IRS PUB. 590-B'),
    slide('THE FACTOR KEEPS SHRINKING', 615, [E('curve', (150, 240, 1230, 720), 'at seventy-three', top=' '),
                                              E('cmark', (150, 240, 1230, 720), 'twenty-six point five', gbox=(150, 240, 1230, 720), age=73, label='AGE 73', sub='26.5', mc=goldL, dx=-10),
                                              E('cmark', (150, 240, 1230, 720), 'twenty-four point six', gbox=(150, 240, 1230, 720), age=75, label='AGE 75', sub='24.6', mc=goldL, dx=70),
                                              E('cmark', (150, 240, 1230, 720), 'twenty point two', gbox=(150, 240, 1230, 720), age=80, label='AGE 80', sub='20.2', mc=goldL),
                                              E('cmark', (150, 240, 1230, 720), 'sixteen', gbox=(150, 240, 1230, 720), age=85, label='AGE 85', sub='16.0', mc=goldL),
                                              E('cmark', (150, 240, 1230, 720), 'twelve point two', gbox=(150, 240, 1230, 720), age=90, label='AGE 90', sub='12.2', mc=red, up=True, dx=-10),
                                              E('card', (1300, 270, 1770, 470), 'keeps shrinking', head='THE FACTOR', val='SHRINKS', col=red, vcol=red, vsize=58),
                                              E('card', (1300, 500, 1770, 700), 'keeps growing', head='YOUR SHARE', val='GROWS', col=green, vcol=green, vsize=58)],
          'EVERY YEAR YOU TAKE A BIGGER SHARE', gold, tag=T2, src='IRS PUB. 590-B'),
]
# ---- 6: WALTER ----
S[6] = [
    slide("WALTER'S TWO NUMBERS", 616, [E('person', (150, 250, 600, 700), None, letter='W', name='WALTER', line='AGE 75', col=gold),
                                        E('card', (680, 270, 1200, 690), 'eight hundred thousand', head='I R A ON DEC. 31', val='$800,000', col=gold, vsize=76, icon='bank', s=0.5),
                                        E('card', (1250, 270, 1770, 690), 'twenty-four point six', head='FACTOR, AGE 75', val='24.6', col=blue, vsize=120, icon='chart', s=0.5)],
          'TWO NUMBERS TO DIVIDE', gold, tag=T2, src='IRS PUB. 590-B'),
    slide('THE DIVISION', 617, [E('card', (150, 330, 640, 640), 'eight hundred thousand divided', head='BALANCE', val='$800,000', col=gold, vsize=70),
                                E('op', (640, 420, 720, 540), 'divided', t='÷', size=120),
                                E('card', (720, 330, 1110, 640), 'by twenty-four point six', head='FACTOR', val='24.6', col=blue, vsize=100),
                                E('op', (1110, 420, 1190, 540), 'point six is', t='=', size=120),
                                E('card', (1190, 330, 1770, 640), 'five hundred twenty dollars', head="WALTER'S RMD", val='$32,520', col=green, vcol=green, vsize=88)],
          'THE ANSWER IS $32,520', green, tag=T2, src='IRS PUB. 590-B'),
    slide('ABOUT 4% OF THE ACCOUNT', 618, [E('ring', R4[0], 'about four percent', val='4%', sub='OF THE ACCOUNT', frac=0.05, col=gold, size=90),
                                           E('card', R4[1], 'his minimum', head='HIS MINIMUM', val='$32,520', sub='THIS YEAR', col=green, vcol=green, vsize=58),
                                           E('icard', R4[2], 'take more', icon='check', l1='TAKE MORE', l2='ALLOWED', col=green, c2=green),
                                           E('icard', R4[3], 'never less', icon='cross', l1='TAKE LESS', l2='NEVER', col=red, c2=red)],
          'MORE IS FINE, LESS IS NOT', gold, tag=T2, src='IRS PUB. 590-B'),
]
# ---- 7: LINDA ----
S[7] = [
    slide("LINDA'S TWO NUMBERS", 619, [E('person', (150, 250, 600, 700), None, letter='L', name='LINDA', line='TURNS 73', col=green),
                                       E('card', (680, 270, 1200, 690), 'five hundred thousand', head='I R A ON DEC. 31', val='$500,000', col=green, vcol=green, vsize=76, icon='bank', s=0.5),
                                       E('card', (1250, 270, 1770, 690), 'twenty-six point five', head='FACTOR, AGE 73', val='26.5', col=blue, vsize=120, icon='chart', s=0.5)],
          'SAME FORMULA, NEW NUMBERS', green, tag=T2, src='IRS PUB. 590-B'),
    slide('HER FIRST RMD', 620, [E('card', (150, 330, 640, 640), None, head='BALANCE', val='$500,000', col=green, vcol=green, vsize=70),
                                 E('op', (640, 420, 720, 540), 'divided', t='÷', size=120),
                                 E('card', (720, 330, 1110, 640), 'by twenty-six point five', head='FACTOR', val='26.5', col=blue, vsize=100),
                                 E('op', (1110, 420, 1190, 540), 'point five is', t='=', size=120),
                                 E('card', (1190, 330, 1770, 640), 'eighteen thousand', head='HER FIRST RMD', val='$18,868', col=gold, vcol=goldL, vsize=88)],
          'THAT IS HER FIRST DISTRIBUTION', gold, tag=T2, src='IRS PUB. 590-B'),
    slide('THE SURPRISE', 621, [E('tline', (150, 260, 1770, 700), 'april first', pts=[('THIS YEAR', 'LINDA TURNS 73', gold), ('APRIL 1', 'NEXT YEAR: DUE DATE', green)], span=(0, 1, 'TIME TO TAKE THE FIRST ONE', green))],
          'THE I R S GIVES HER EXTRA TIME', green, tag=T2, src='IRS PUB. 590-B'),
]
# ---- 8: TWO IN ONE YEAR ----
S[8] = [
    slide('THE APRIL 1 TRAP', 622, [E('stamp', (150, 250, 700, 370), None, t='A TRAP', col=red, ang=-5, size=90),
                                    E('tline', (150, 330, 1770, 700), 'after the first year', pts=[('APRIL 1', '1ST RMD DUE', gold), ('DEC. 31', '2ND RMD DUE', red)], span=(0, 1, 'TWO IN ONE YEAR', red))],
          'EVERY LATER RMD IS DUE DEC. 31', red, (255, 255, 255), tag=T2, src='IRS PUB. 590-B'),
    slide('HER SECOND RMD', 623, [E('card', (150, 330, 640, 640), 'five hundred ten thousand', head='BALANCE', val='$510,000', col=green, vcol=green, vsize=70),
                                  E('op', (640, 420, 720, 540), 'next factor', t='÷', size=120),
                                  E('card', (720, 330, 1110, 640), 'twenty-five point five', head='FACTOR', val='25.5', col=blue, vsize=100),
                                  E('op', (1110, 420, 1190, 540), 'second one', t='=', size=120),
                                  E('card', (1190, 330, 1770, 640), 'twenty thousand', head='2ND RMD', val='$20,000', col=gold, vcol=goldL, vsize=88)],
          'SAME YEAR, SECOND DISTRIBUTION', gold, tag=T2, src='IRS PUB. 590-B'),
    slide('TWO RMDs IN ONE YEAR', 624, [E('seg', (150, 430, 900, 550), 'together', label='1ST RMD', val='$18,868', fill=gold),
                                       E('seg', (150, 570, 900, 690), 'thirty-eight thousand', label='2ND RMD', val='$20,000', fill=blue, tc=white),
                                       E('big', (980, 280, 1770, 600), 'sixty-eight dollars', val='$38,868', sub='TAXABLE INCOME IN ONE YEAR', size=170, vcol=red),
                                       E('stamp', (160, 260, 900, 380), 'single year', t='ONE TAX YEAR', col=red, ang=-4, size=76)],
          'ONE BIG TAX BILL', red, (255, 255, 255), tag=T2, src='IRS PUB. 590-B'),
]
# ---- 9: PENALTY ----
S[9] = [
    slide('THE MISSED-RMD PENALTY', 625, [E('icard', (150, 270, 700, 690), None, icon='cross', l1='LESS THAN REQUIRED', l2='YOU TAKE TOO LITTLE', col=red, c2=red),
                                         E('ring', (780, 250, 1280, 700), 'twenty-five percent', val='25%', sub='EXCISE TAX', frac=0.25, col=red, size=130),
                                         E('line', (1300, 440, 1770, 560), 'did not take out', t='ON THE AMOUNT SKIPPED', size=40, col=goldL)],
          'THE I R S CHARGES 25%', red, (255, 255, 255), tag=T3, src='IRS PUB. 590-B'),
    slide("WALTER'S PENALTY", 626, [E('card', (150, 330, 640, 640), 'thirty-two thousand five', head='AMOUNT MISSED', val='$32,520', col=gold, vsize=70),
                                    E('op', (640, 420, 720, 540), 'would cost', t='×', size=120),
                                    E('card', (720, 330, 1110, 640), 'would cost', head='PENALTY RATE', val='25%', col=red, vcol=red, vsize=110),
                                    E('op', (1110, 420, 1190, 540), 'would cost', t='=', size=120),
                                    E('card', (1190, 330, 1770, 640), 'eight thousand one hundred', head='THE COST', val='$8,130', col=red, vcol=red, vsize=88)],
          'MISSING IT ALL COSTS $8,130', red, (255, 255, 255), tag=T3, src='IRS PUB. 590-B'),
    slide('FIX IT IN TIME', 627, [E('vbars', (150, 250, 940, 720), 'rate drops', vals=[('25%', 8130, '$8,130', red), ('10%', 3252, '$3,252', green)]),
                                  E('icard', (1030, 270, 1770, 690), 'fix it in time', icon='clock', l1='FIXED IN TIME', l2='10% INSTEAD OF 25%', col=green, c2=green)],
          'THE RATE DROPS TO 10%', green, tag=T3, src='IRS PUB. 590-B'),
    slide('HOW TO REPORT IT', 628, [E('icard', R2[0], 'fifty-three twenty-nine', icon='form', l1='FORM 5329', l2='REPORT IT HERE', col=gold),
                                    E('icard', R2[1], 'waiver', icon='doc', l1='ASK FOR A WAIVER', l2='IF THE MISTAKE WAS REASONABLE', col=green, c2=green)],
          'THERE IS A WAY OUT', gold, tag=T3, src='IRS PUB. 590-B'),
]
# ---- 10: SOCIAL SECURITY ----
S[10] = [
    slide('THE PART NOBODY EXPLAINS', 629, [E('icard', (150, 270, 580, 690), 'required distribution', icon='bank', l1='YOUR RMD', l2='COMES OUT', col=gold),
                                            E('arrow', (600, 400, 720, 540), 'taxable income', col=goldL),
                                            E('icard', (740, 270, 1170, 690), 'is taxable income', icon='wallet', l1='TAXABLE INCOME', l2='GOES UP', col=red, c2=red),
                                            E('arrow', (1190, 400, 1310, 540), 'pulls', col=goldL),
                                            E('icard', (1330, 270, 1760, 690), 'your social security', icon='coins', l1='SOCIAL SECURITY', l2='NOW TAXED TOO', col=red, c2=red)],
          'AN RMD CAN TAX YOUR BENEFITS', red, (255, 255, 255), tag=T4, src='IRS PUB. 915'),
    slide('HOW THE I R S ADDS IT UP', 630, [E('card', (150, 340, 700, 690), None, head='HALF OF SS', val='$15,000', col=blue, vsize=88, icon='coins', s=0.6),
                                            E('op', (700, 460, 800, 580), 'to his', t='+', size=130),
                                            E('card', (800, 340, 1350, 690), 'thirty-two thousand', head='HIS RMD', val='$32,520', col=gold, vsize=88, icon='bank', s=0.5),
                                            E('line', (150, 250, 1770, 300), 'dollar distribution', t="THE I R S ADDS HALF OF WALTER'S BENEFITS", size=44, col=goldL)],
          'HALF THE BENEFITS + THE RMD', gold, tag=T4, src='IRS PUB. 915'),
    slide('FAR ABOVE THE LINE', 631, [E('gauge', (150, 240, 1100, 720), 'forty-seven thousand', limit=34000, val=47520, top=60000, lim_l='$34,000 LINE', label='$47,520', col=red),
                                      E('ring', (1200, 260, 1740, 700), 'eighty-five percent', val='85%', sub='UP TO 85% TAXED', frac=0.85, col=red, size=120)],
          'ABOVE $34,000 (SINGLE), UP TO 85%', red, (255, 255, 255), tag=T4, src='IRS PUB. 915'),
]
# ---- 11: WALTER'S RETURN ----
S[11] = [
    slide("WALTER'S INCOME", 632, FORM((150, 250, 1770, 710), "WALTER  ·  2026  ·  FEDERAL", [('A', 'SOCIAL SECURITY', '$30,000'), ('B', 'TAXABLE PART (PUB. 915)', '$15,992'), ('C', '+ I R A DISTRIBUTION', '$32,520'), ('D', '= INCOME ON THE RETURN', '$48,512')],
                                      ['social security', 'fifteen thousand nine hundred', 'add his distribution', 'forty-eight thousand'], right='SINGLE', first='using the', hl=(3,)),
          'FROM RMD TO INCOME ON THE RETURN', gold, tag=T4, src='IRS PUB. 915'),
    slide('HIS FEDERAL TAX', 633, [E('step', (150, 260, 1120, 380), None, n=1, text='INCOME ON THE RETURN', val='$48,512'),
                                   E('step', (150, 410, 1120, 530), 'twenty-four thousand one', n=2, text='− DEDUCTIONS', val='$24,150', vc=green),
                                   E('step', (150, 560, 1120, 680), 'taxed on', n=3, text='= TAXED ON', val='$24,362'),
                                   E('big', (1190, 300, 1780, 650), 'federal income tax', val='$2,675', sub="WALTER'S TAX", size=180, vcol=red)],
          'TAX BEFORE ANY MOVE: $2,675', red, (255, 255, 255), tag=T4, src='IRS PUB. 915'),
]
# ---- 12: QCD ----
S[12] = [
    slide('QUALIFIED CHARITABLE DISTRIBUTION', 634, [E('big', (150, 260, 760, 650), None, val='Q C D', sub='THE MOVE', size=200, vcol=green),
                                                     E('flow', (830, 250, 1770, 590), 'directly from', nodes=[('bank', 'YOUR I R A', 'PAYS DIRECTLY', gold), ('house', 'A CHARITY', 'RECEIVES IT', green)], s=0.55),
                                                     E('stamp', (900, 625, 1740, 715), 'not counted', t='NOT COUNTED AS INCOME', col=green, ang=-3, size=50)],
          'FROM YOUR I R A STRAIGHT TO CHARITY', green, tag=T5, src='IRS PUB. 590-B'),
    slide('THE AGE RULE', 635, [E('ring', (150, 260, 650, 700), 'seventy and a half', val='70.5', sub='MINIMUM AGE', frac=1.0, col=green, size=108),
                                E('arrow', (690, 400, 860, 540), 'earlier than', col=goldL),
                                E('ring', (900, 260, 1400, 700), 'seventy-three', val='73', sub='RMDs START', frac=1.0, col=gold, size=130),
                                E('stamp', (1440, 360, 1790, 560), 'earlier than', t='EARLIER', col=green, ang=-8, size=70)],
          'YOU CAN START BEFORE 73', green, tag=T5, src='IRS PUB. 590-B'),
    slide('THE LIMIT', 636, GRID((150, 250, 1000, 600), ['YEAR', 'Q C D LIMIT'], [0.4, 0.6], [('2025', '$108,000'), ('2026', '$111,000')], ['twenty twenty-five', 'twenty twenty-six'], first='the limit', col=green) +
          [E('card', (1080, 270, 1770, 470), 'per person', head='PER PERSON', val='EACH SPOUSE', col=gold, vsize=48),
           E('stamp', (1080, 520, 1770, 650), 'counts toward', t='COUNTS TOWARD YOUR RMD', col=green, ang=-4, size=40)],
          'THE ANNUAL LIMIT', green, tag=T5, src='IRS PUB. 590-B'),
]
# ---- 13: QCD MATH ----
S[13] = [
    slide('WALTER GIVES $10,000', 637, [E('flow', (150, 260, 900, 700), None, nodes=[('bank', 'HIS I R A', '$32,520 RMD', gold), ('house', 'CHARITY', '$10,000 Q C D', green)], s=0.7),
                                        E('vbars', (990, 250, 1770, 720), 'drops from', vals=[('RMD', 32520, '$32,520', blue), ('TO CHARITY', 10000, '$10,000', green), ('TAXABLE', 22520, '$22,520', gold)])],
          'TAXABLE I R A INCOME: $22,520', green, tag=T5, src='IRS PUB. 590-B'),
    slide('LESS SOCIAL SECURITY TAXED', 638, [E('card', (150, 330, 760, 640), None, head='BEFORE', val='$15,992', sub='TAXABLE SOCIAL SECURITY', col=red, vcol=red, vsize=100),
                                              E('arrow', (790, 400, 960, 540), 'now the worksheet', col=goldL),
                                              E('card', (990, 330, 1770, 640), 'seven thousand four hundred', head='AFTER THE Q C D', val='$7,492', sub='TAXABLE SOCIAL SECURITY', col=green, vcol=green, vsize=110)],
          'THE WORKSHEET NOW GIVES LESS', green, tag=T5, src='IRS PUB. 915'),
    slide('HIS NEW TAXED INCOME', 639, [E('card', (250, 330, 920, 640), 'thirty thousand twelve', head='INCOME ON THE RETURN', val='$30,012', col=gold, vsize=100),
                                        E('card', (1000, 330, 1670, 640), 'five thousand eight hundred', head='TAXED ON ONLY', val='$5,862', col=green, vcol=green, vsize=110)],
          'FROM $24,362 DOWN TO $5,862', green, tag=T5, src='IRS PUB. 915'),
]
# ---- 14: RESULT ----
S[14] = [
    slide('THE TAX DROPS', 640, [E('vbars', (150, 250, 940, 720), 'falls from', vals=[('WITHOUT Q C D', 2675, '$2,675', red), ('WITH Q C D', 586, '$586', green)]),
                                 E('big', (1000, 290, 1780, 650), 'two thousand eighty-nine', val='$2,089', sub='SAVED', size=190, vcol=green)],
          'FROM $2,675 TO $586', green, tag=T5, src=IRS),
    slide('SOCIAL SECURITY TAXED', 641, [E('ring', (250, 250, 760, 700), 'fifty-three percent', val='53%', sub='BEFORE', frac=0.53, col=red, size=130),
                                         E('arrow', (790, 400, 960, 540), 'drops from', col=goldL),
                                         E('ring', (990, 250, 1500, 700), 'twenty-five percent', val='25%', sub='AFTER', frac=0.25, col=green, size=130)],
          'SHARE OF BENEFITS THAT IS TAXED', green, tag=T5, src=IRS),
    slide('BE HONEST ABOUT THE TRADE', 642, [E('icard', R2[0], None, icon='house', l1='$10,000 GOES TO CHARITY', l2='BEST IF YOU ALREADY GIVE', col=gold),
                                              E('icard', R2[1], 'the same gift', icon='bank', l1='SAME GIFT FROM BANK', l2='DOES NOT LOWER INCOME', col=red, c2=red)],
          'IT WORKS BEST IF YOU ALREADY PLANNED TO GIVE', gold, tag=T5, src=IRS),
]
# ---- 15: QCD RULES ----
S[15] = [
    slide('GO DIRECT', 643, [E('flow', (150, 250, 1770, 590), 'directly from', nodes=[('bank', 'YOUR I R A', 'TRUSTEE', gold), ('wallet', 'YOUR POCKET', 'NEVER HERE', red), ('house', 'CHARITY', 'MUST RECEIVE IT', green)], cross=0, s=0.5),
                             E('line', (150, 640, 1770, 700), 'never through', t='THE TRUSTEE MUST PAY THE CHARITY DIRECTLY', size=46, col=goldL)],
          'NEVER THROUGH YOUR OWN POCKET', red, (255, 255, 255), tag=T5, src='IRS PUB. 590-B'),
    slide('WHICH ACCOUNTS WORK', 644, GRID((250, 260, 1670, 690), ['ACCOUNT', 'Q C D?'], [0.7, 0.3], [('TRADITIONAL I R A', 'Y'), ('ONGOING SEP I R A', 'N'), ('ONGOING SIMPLE I R A', 'N')], ['traditional i r a', 'sep', 'simple'], first='it works from', col=gold),
          'TRADITIONAL I R As WORK', gold, tag=T5, src='IRS PUB. 590-B'),
    slide('RECEIPT, NO DOUBLE DEDUCTION', 645, [E('icard', R2[0], None, icon='doc', l1='WRITTEN RECEIPT', l2='LIKE ANY DONATION', col=green, c2=green),
                                                E('icard', R2[1], 'cannot also deduct', icon='cross', l1='NO SECOND DEDUCTION', l2='ON THE SAME GIFT', col=red, c2=red)],
          'PAPERWORK MATTERS', gold, tag=T5, src='IRS PUB. 590-B'),
    slide('ON YOUR TAX RETURN', 646, FORM((150, 250, 1770, 700), 'FORM 1040  ·  I R A DISTRIBUTIONS', [('4A', 'I R A DISTRIBUTIONS', '$32,520'), ('4B', 'ONLY THE TAXABLE PART', '$22,520'), ('4C', 'MARK THE Q C D BOX', 'X')],
                                         ['form ten forty', 'four b', 'four c'], right='LINE 4', first='and on form', hl=(1, 2)),
          'THREE BOXES TO FILL IN', gold, tag=T5, src='IRS PUB. 590-B'),
]
# ---- 16: MORE RULES ----
S[16] = [
    slide('SEVERAL I R As', 647, [E('icard', R3c[0], 'several i r as', icon='bank', l1='I R A #1', l2='SEPARATE CALCULATION', col=gold),
                                  E('icard', R3c[1], 'each one separately', icon='bank', l1='I R A #2', l2='SEPARATE CALCULATION', col=gold),
                                  E('icard', R3c[2], 'but you can', icon='bank', l1='I R A #3', l2='SEPARATE CALCULATION', col=gold),
                                  E('line', (150, 650, 1770, 710), 'withdraw the total', t='WITHDRAW THE TOTAL FROM ANY ONE OF THEM', size=44, col=goldL)],
          'CALCULATE EACH, TAKE IT FROM ANY', gold, tag=T6, src='IRS.GOV'),
    slide('401(K) AND 457(B)', 648, [E('icard', R2[0], 'four oh one', icon='brief', l1='401(K)', l2='EACH PLAN PAYS ITS OWN', col=red, c2=red),
                                     E('icard', R2[1], 'four fifty-seven', icon='brief', l1='457(B)', l2='EACH PLAN PAYS ITS OWN', col=red, c2=red)],
          'PLANS ARE DIFFERENT', red, (255, 255, 255), tag=T6, src='IRS.GOV'),
    slide('STILL WORKING?', 649, [E('card', R3[0], 'delay', head='EMPLOYER PLAN', val='CAN DELAY', sub='UNTIL YOU RETIRE', col=green, vcol=green, vsize=56, icon='check', s=1.0),
                                  E('card', R3[1], 'five percent', head='5% OWNER', val='NO DELAY', sub='OF THE COMPANY', col=red, vcol=red, vsize=56, icon='cross', s=1.0),
                                  E('card', R3[2], 'cover i r as', head='I R As', val='NOT COVERED', sub='EXCEPTION DOES NOT APPLY', col=red, vcol=red, vsize=46, icon='cross', s=1.0)],
          'THE WORK EXCEPTION HAS LIMITS', gold, tag=T6, src='IRS.GOV'),
]
# ---- 17: WITHHOLDING ----
S[17] = [
    slide('TEN PERCENT BY DEFAULT', 650, [E('icard', R3[0], 'ten percent', icon='check', l1='10% WITHHELD', l2='THE I R S DEFAULT', col=gold),
                                           E('icard', R3[1], 'form w four r', icon='form', l1='FORM W-4R', l2='PICK A DIFFERENT RATE', col=gold),
                                           E('icard', R3[2], 'as you go', icon='check', l1='PAID AS YOU GO', l2='NO APRIL SURPRISE', col=green, c2=green)],
          'YOU CAN CHOOSE THE RATE', gold, tag=T6, src='IRS PUB. 590-B'),
    slide('NO CARRYOVER', 651, [E('icard', R2[0], 'estimated tax', icon='clock', l1='ESTIMATED TAX', l2='IF TOO LITTLE IS WITHHELD', col=gold),
                                E('card', R2[1], 'cannot be counted', head='TAKE MORE THAN THE MINIMUM', val='EXTRA DOES NOT CARRY OVER', col=red, vcol=red, vsize=36, icon='cross', s=1.2)],
          'THE EXTRA DOES NOT COUNT NEXT YEAR', red, (255, 255, 255), tag=T6, src='IRS PUB. 590-B'),
]
# ---- 18: CHECKLIST ----
S[18] = [
    slide('YOUR CHECKLIST: 1 AND 2', 652, [E('numcol', R2[0], 'find last', n=1, icon='chart', l1='FIND YOUR BALANCE', l2='÷ THE FACTOR'),
                                           E('numcol', R2[1], 'first year', n=2, icon='clock', l1='FIRST YEAR?', l2='AVOID TWO IN ONE')],
          'THIS YEAR', gold, tag=T7, src=IRS),
    slide('YOUR CHECKLIST: 3 AND 4', 653, [E('numcol', R2[0], None, n=3, icon='house', l1='ASK ABOUT A Q C D', l2='BEFORE DEC. 31'),
                                           E('numcol', R2[1], 'choose your', n=4, icon='form', l1='CHOOSE WITHHOLDING', l2='FORM W-4R')],
          'NO SURPRISES IN APRIL', green, tag=T7, src=IRS),
]
# ---- 19: RECAP ----
S[19] = [
    slide('RECAP: 1 TO 3', 654, [E('rule', (180, 290, 1740, 420), 'one', n=1, text='MINIMUM = BALANCE ÷ FACTOR', val="WALTER: $32,520"),
                                 E('rule', (180, 440, 1740, 570), 'two', n=2, text='FIRST RMD CAN WAIT UNTIL APRIL 1', val='THEN TWO IN ONE YEAR', vc=red),
                                 E('rule', (180, 590, 1740, 720), 'three', n=3, text='MISSING IT COSTS 25%', val='10% IF FIXED', vc=red)],
          'THREE NUMBERS TO KEEP', gold, tag='RECAP', src=IRS),
    slide('RECAP: 4 AND 5', 655, [E('rule', (180, 290, 1740, 460), 'four a', n=4, text='AN RMD CAN TAX UP TO 85% OF YOUR BENEFITS', val='UP TO 85%', vc=red),
                                  E('rule', (180, 500, 1740, 670), 'five a', n=5, text='A Q C D CAN CUT THAT', val='WALTER SAVED $2,089', vc=green)],
          'TWO MORE TO KEEP', green, tag='RECAP', src=IRS),
]
# ---- 20: CTA + DISCLAIMER ----
def final13(t, seed=213):
    Dd = CUR['D']
    fr = base(t); fr = amb(fr, t, seed, 7, 55); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('General information,', white, 250), ('not tax advice.', white, 315), ('Rules, amounts and ages change,', goldL, 410),
             ('so always confirm with the I R S', goldL, 475), ('or a qualified tax professional', white, 570), ('before you act.', white, 635)]
    groups = [lines[0:2], lines[2:4], lines[4:6]]; tg = [0.3, 0.3 + (0.6 * Dd - 0.3) / 2, 0.6 * Dd]
    for g, ts in zip(groups, tg):
        if t > ts:
            C = new()
            for tx, cl, yy in g: txt(C, tx, BOLD(52), yy, cl, 255, x=650)
            fr = A_(fr, C, (140, 240, 1160, 770), t, ts)
    if t > 0.68 * Dd:
        C = new(); dashed(C, 1220, 280, 1780, 640); txt(C, 'WATCH NEXT', BOLD(56), 430, goldL, 255, x=1500); fr = A_(fr, C, (1200, 260, 1800, 660), t, 0.68 * Dd)
    if t > 0.8 * Dd - 0.4:
        import modello_unico as _m
        C = new(); _m.dashed_circle(C, 260, 860, 85); txt(C, 'SUBSCRIBE', BOLD(44), 835, goldL, 255, x=560); fr = A_(fr, C, (160, 760, 760, 960), t, 0.8 * Dd - 0.4)
    return frame(fr)
S[20] = [
    slide('SEND IT TO ONE PERSON', 656, [E('icard', (500, 260, 1420, 690), None, icon='mail', l1='SOMEONE OVER 70', l2='WHO HAS AN I R A', col=gold)],
          'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 657, [E('line', (260, 340, 1660, 440), None, t='DO YOU GIVE TO CHARITY?', size=92, col=white),
                                           E('line', (260, 480, 1660, 580), 'anyone ever told', t='EVER HEARD OF A Q C D?', size=92, col=goldL)],
          'ANSWER IN THE COMMENTS'),
    frozen(final13),
]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
CUTS = {1: ['it is called', 'walter is seventy-five', 'but one move'], 2: ['linda reaches', 'walter will show'], 3: ['no news'],
        4: ['the rule applies', 'but a roth', 'so this rule'], 5: ['at seventy-three'], 6: ['eight hundred thousand divided', 'that is about four'],
        7: ['five hundred thousand divided', 'and here is the surprise'], 8: ['suppose her balance', 'together'], 9: ['for walter', 'if you fix it', 'you report it'],
        10: ['the i r s adds', 'that makes'], 11: ['his deductions'], 12: ['you must be', 'the limit'], 13: ['now the worksheet', 'his income on the return'],
        14: ['and the share', 'be honest'], 15: ['it works from', 'you need a written', 'and on form'], 16: ['a four oh one', 'and if you are still'], 17: ['if too little'],
        18: ['three if you give'], 19: ['four a distribution'], 20: ['and tell me', 'one last thing']}
for _b, _ph in CUTS.items():
    _tot = sum(SPEC[_b]); _c = [0] + [round((V.at(_b, p) - 0.2) * 30) for p in _ph] + [_tot]
    SPEC[_b] = [_c[i + 1] - _c[i] for i in range(len(_c) - 1)]
if os.environ.get('PV'):   # solo anteprima layout dei blocchi senza voce: durate finte uguali
    for _b in SLIDES:
        if not os.path.exists(os.path.join(VID, 'voce', f'b{_b}.wav')): SPEC[_b] = [750 // len(SLIDES[_b])] * len(SLIDES[_b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v13', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
