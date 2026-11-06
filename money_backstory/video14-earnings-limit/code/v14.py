"""Video 14 - earnings test 2027 - 17 blocchi. Uso: python3 v14.py render|preview|check|spec|cues <blocco> [slide,slide]
Layout nuovi rispetto ai video 8-13: calendario dei mesi che cambia stato, linea dell'anno con zone e bandierina, barre mensili con linea del limite, colonne a confronto, catene di calcolo."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v14eng import *

R2 = row(2); R3 = row(3); R4 = row(4, gap=36); R3b = row(3, y1=620)
SSA = 'SSA.GOV'
T1, T2, T3, T4, T5, T6 = 'THE BASICS', 'LIMIT ONE', 'DAN', 'LIMIT TWO', 'THE MONTHLY TEST', 'YOUR CHECKLIST'
GB = (150, 270, 1770, 690)          # calendario 6 x 2
GY = (150, 390, 1770, 560)          # linea dell'anno, 12 mesi in fila
GBAR = (150, 260, 1770, 700)        # barre mensili
def MT(idx, cue, status, amt=None, nc=6, nr=2, gb=GB, hmax=None, small=False, sub=None):
    return E('mtile', bbox([mgeo(gb, i, nc, nr, hmax=hmax) for i in idx]), cue, gbox=gb, idx=idx, status=status, amt=amt, ncols=nc, nrows=nr, hmax=hmax, small=small, sub=sub)
def MG(cue, gb=GB, nc=6, nr=2, hmax=None, small=False): return E('mgrid', gb, cue, gbox=gb, ncols=nc, nrows=nr, hmax=hmax, small=small)
def YG(cue): return MG(cue, GY, 12, 1, 170, True)
def YT(idx, cue, status='gold'): return MT(idx, cue, status, None, 12, 1, GY, 170, True)
def YB(a, b, cue, label, sub=None, col=gold):
    ba, bb = mgeo(GY, a, 12, 1, 170), mgeo(GY, b, 12, 1, 170); return E('ybrace', (ba[0], 575, bb[2], 700), cue, label=label, sub=sub, col=col)
def YM(i, cue, label): 
    b = mgeo(GY, i, 12, 1, 170); mx = (b[0] + b[2]) / 2; return E('ymark', (mx - 250, 262, mx + 250, 390), cue, gbox=GY, i=i, label=label, ncols=12, nrows=1, hmax=170)

S = {}
# ---- 1: HOOK ----
S[1] = [
    slide('WHAT IF WORK COST YOU 4 CHECKS?', 1401, [E('icard', R4[0], 'one more year', icon='bill', l1='CHECK 1', l2='HELD BACK', col=red, c2=red),
                                                   E('icard', R4[1], 'cost you', icon='bill', l1='CHECK 2', l2='HELD BACK', col=red, c2=red),
                                                   E('icard', R4[2], 'four full', icon='bill', l1='CHECK 3', l2='HELD BACK', col=red, c2=red),
                                                   E('icard', R4[3], 'social security checks', icon='bill', l1='CHECK 4', l2='HELD BACK', col=red, c2=red)],
          'ONE MORE YEAR OF WORK', red, (255, 255, 255)),
    slide('SAME PAYCHECK, TWO RESULTS', 1402, [E('icard', R2[0], 'for some people', icon='cross', l1='FOR SOME PEOPLE', l2='CHECKS ARE HELD BACK', col=red, c2=red),
                                              E('icard', R2[1], 'for others', icon='check', l1='FOR OTHERS', l2='NOTHING IS HELD BACK', col=green, c2=green)],
          'THE VERY SAME PAYCHECK', gold),
    slide('TWO LIMITS, ONE BIRTHDAY, ONE RULE', 1403, [E('icard', R3[0], 'two limits', icon='chart', l1='TWO LIMITS', l2='ONE PER SITUATION', col=gold),
                                                      E('icard', R3[1], 'one birthday', icon='clock', l1='ONE BIRTHDAY', l2='FULL RETIREMENT AGE', col=gold),
                                                      E('icard', R3[2], 'one rule', icon='form', l1='ONE RULE', l2='NOBODY MENTIONS IT', col=green, c2=green)],
          'THE 2027 NUMBERS FROM SOCIAL SECURITY', gold, src=SSA),
]
# ---- 2: MEET ----
S[2] = [
    slide('MEET DAN', 1404, [E('person', (150, 250, 640, 700), None, letter='D', name='DAN, 63', line='STILL WORKS', col=gold),
                            E('card', (720, 250, 1770, 700), 'started his benefit', head='HE STARTED HIS BENEFIT AT', val='62', vsize=240, vcol=goldL, sub='AND KEEPS WORKING', col=gold)],
          'COLLECTING AND WORKING', gold),
    slide('MEET RUTH', 1405, [E('person', (150, 250, 640, 700), None, letter='R', name='RUTH', line='BORN IN 1960', line2='STILL WORKS', col=green),
                             E('cal', (720, 250, 1770, 700), 'turns sixty-seven', head='SHE TURNS 67 IN', big='AUGUST 2027', size=100, sub='FULL RETIREMENT AGE', col=green)],
          'HER BIG BIRTHDAY MONTH', green),
    slide('SAME JOB, VERY DIFFERENT RESULT', 1406, [E('icard', R2[0], 'both still have', icon='brief', l1='DAN', l2='A PAYCHECK', col=gold),
                                                   E('icard', R2[1], 'same kind of money', icon='brief', l1='RUTH', l2='A PAYCHECK', col=green, c2=green),
                                                   E('stamp', (700, 400, 1220, 520), 'very different', t='VERY DIFFERENT', col=red, ang=-6, size=84)],
          'LET US SEE WHY', gold),
]
# ---- 3: SOURCES ----
S[3] = [
    slide('EVERY NUMBER IS OFFICIAL', 1407, [E('icard', R3[0], 'earnings test page', icon='doc', l1='EARNINGS TEST', l2='OFFICIAL PAGE', col=gold),
                                            E('icard', R3[1], 'cost of living fact sheet', icon='chart', l1='2027 COLA', l2='FACT SHEET', col=gold),
                                            E('icard', R3[2], 'how work affects', icon='doc', l1='HOW WORK AFFECTS', l2='YOUR BENEFITS', col=gold)],
          'FROM SOCIAL SECURITY ITSELF', gold, src=SSA),
    slide('NO GUESSES', 1408, [E('chip', (200, 300, 960, 420), 'no news articles', t='NEWS ARTICLES', ic=red),
                              E('chip', (200, 460, 960, 580), 'no guesses', t='GUESSES', ic=red),
                              E('big', (1000, 270, 1770, 620), 'the basic idea', val='THE IDEA', sub='FIRST, THE BASIC IDEA', size=130, vcol=goldL)],
          'FIRST, THE BASIC IDEA', gold, src=SSA),
]
# ---- 4: BASIC IDEA ----
S[4] = [
    slide('CLAIM EARLY, KEEP WORKING', 1409, [E('icard', R3[0], 'claim your retirement', icon='doc', l1='CLAIM EARLY', l2='BEFORE FULL AGE', col=gold),
                                             E('icard', R3[1], 'keep working', icon='brief', l1='KEEP WORKING', l2='STILL EARNING', col=gold),
                                             E('icard', R3[2], 'compares your earnings', icon='chart', l1='A YEARLY LIMIT', l2='YOUR EARNINGS CHECKED', col=blue)],
          'SOCIAL SECURITY CHECKS YOUR PAY', gold, tag=T1, src=SSA),
    slide('UNDER OR OVER THE LIMIT', 1410, [E('vs', (150, 250, 1770, 650), 'stay under', cols=[('STAY UNDER', 'NOTHING', 'HAPPENS', green), ('GO OVER', 'PART', 'IS HELD BACK', red)], size=100),
                                           E('line', (150, 670, 1770, 730), 'this rule is called', t='THIS RULE IS CALLED THE EARNINGS TEST', size=46, col=goldL)],
          'THE EARNINGS TEST', gold, tag=T1, src=SSA),
]
# ---- 5: FULL RETIREMENT AGE ----
S[5] = [
    slide('YOUR FULL RETIREMENT AGE', 1411, [E('card', (150, 260, 960, 690), 'for anyone born', head='BORN IN', val='1960 OR LATER', vsize=84, col=gold, icon='clock', s=0.7),
                                            E('ring', (1010, 250, 1770, 700), 'sixty-seven', val='67', sub='FULL RETIREMENT AGE', frac=1.0, col=green, size=150)],
          'SIXTY-SEVEN FOR EVERYONE BORN 1960+', gold, tag=T1, src=SSA),
    slide('FROM THAT MONTH: NO LIMIT', 1412, [E('big', (150, 250, 1770, 520), 'any amount', val='NO LIMIT', sub='FROM THE MONTH YOU REACH IT', size=190, vcol=green),
                                             E('line', (150, 590, 1770, 650), 'no benefit is ever', t='NO BENEFIT IS EVER HELD BACK', size=54, col=goldL)],
          'EARN ANY AMOUNT', green, tag=T1, src=SSA),
    slide('AGES 62 TO 67', 1413, [E('tline', (150, 250, 1770, 690), 'that means', pts=[('62', 'CLAIM', gold), ('63', '', gold), ('64', '', gold), ('65', '', gold), ('66', '', gold), ('67', 'FULL AGE', green)], span=(0, 4, 'THE YEARS THAT MATTER', red))],
          'COLLECT AND WORK AT THE SAME TIME', red, (255, 255, 255), tag=T1, src=SSA),
]
# ---- 6: LIMIT 1 ----
S[6] = [
    slide('LIMIT NUMBER ONE', 1414, [E('card', (150, 260, 840, 690), 'limit number one', head='UNDER FULL RETIREMENT AGE', val='THE WHOLE YEAR', vsize=50, col=gold, icon='clock', s=0.7),
                                    E('big', (900, 260, 1770, 690), 'twenty-five thousand', val='$25,560', sub='THE 2027 LIMIT', size=190, vcol=goldL)],
          'THE FIRST LIMIT FOR 2027', gold, tag=T2, src=SSA),
    slide('2026 VERSUS 2027', 1415, [E('vbars', (250, 250, 1670, 700), 'this year it is', vals=[('2026', 24480, '$24,480', (110, 130, 160)), ('2027', 25560, '$25,560', gold)])],
          'THE LIMIT GOES UP', gold, tag=T2, src=SSA),
    slide('ONE DOLLAR FOR EVERY TWO', 1416, [E('rule', (180, 290, 1740, 450), 'earn up to', n='$', text='EARN UP TO THE LIMIT', val='LOSE NOTHING', vc=green, col=green),
                                            E('rule', (180, 500, 1740, 660), 'for every two dollars', n='2', text='EVERY $2 ABOVE THE LIMIT', val='$1 HELD BACK', vc=red, col=red)],
          'FOR EVERY $2 OVER, $1 HELD BACK', red, (255, 255, 255), tag=T2, src=SSA),
]
# ---- 7: DAN'S NUMBERS ----
S[7] = [
    slide("DAN'S NUMBERS", 1417, [E('pay', (150, 260, 900, 690), 'one thousand five hundred', amount='$1,500', sub='PER MONTH', head='DAN\'S CHECK', size=130, col=gold),
                                 E('card', (960, 260, 1770, 690), 'thirty-seven thousand', head='HE EARNS IN 2027', val='$37,560', vsize=120, vcol=goldL, col=blue, icon='wallet', s=0.7)],
          'HIS CHECK AND HIS PAY', gold, tag=T3, src=SSA),
    slide('$12,000 OVER THE LIMIT', 1418, [E('gauge', (150, 250, 650, 700), 'that is exactly', limit=25560, val=37560, top=40000, lim_l='LIMIT $25,560', label='DAN: $37,560'),
                                          E('big', (700, 260, 1770, 690), 'twelve thousand dollars above', val='$12,000', sub='ABOVE THE LIMIT', size=190, vcol=red)],
          'EXACTLY $12,000 OVER', red, (255, 255, 255), tag=T3, src=SSA),
    slide('HALF IS HELD BACK', 1419, [E('calc', (150, 300, 1770, 520), 'half of twelve', parts=[('$12,000', white, 90), ('÷', goldL, 90), ('2', white, 90), ('=', goldL, 90), ('$6,000', red, 100)], col=gold),
                                     E('stamp', (700, 570, 1220, 690), 'that is the amount', t='HELD BACK', col=red, ang=-5, size=90)],
          '$6,000 IS HELD BACK', red, (255, 255, 255), tag=T3, src=SSA),
]
# ---- 8: WHOLE MONTHS ----
S[8] = [
    slide('TAKEN IN WHOLE CHECKS', 1420, [E('calc', (150, 300, 1770, 520), 'six thousand dollars divided', parts=[('$6,000', red, 88), ('÷', goldL, 88), ('$1,500', white, 88), ('=', goldL, 88), ('4', green, 130)], col=gold),
                                         E('line', (150, 570, 1770, 630), 'is exactly four', t='EXACTLY FOUR WHOLE MONTHLY CHECKS', size=52, col=goldL)],
          'WHOLE MONTHLY CHECKS', gold, tag=T3, src=SSA),
    slide("DAN'S YEAR, MONTH BY MONTH", 1421, [MG('so dan receives'),
                                              MT([0], 'january', 'held', '$0'), MT([1], 'february', 'held', '$0'), MT([2], 'march', 'held', '$0'), MT([3], 'april', 'held', '$0'),
                                              MT([4, 5], 'full check from may', 'paid', '$1,500'), MT([6, 7, 8, 9, 10, 11], 'on', 'paid', '$1,500')],
          'NO CHECKS UNTIL MAY', red, (255, 255, 255), tag=T3, src=SSA),
    slide('THE FIRST CHECKS OF THE YEAR', 1422, [E('cal', (150, 260, 960, 690), 'taken from the first', head='TAKEN FROM', big='THE FIRST CHECKS', size=80, sub='OF THE YEAR', col=gold),
                                                E('icard', (1010, 260, 1770, 690), 'works the same way', icon='doc', l1='SOCIAL SECURITY\'S', l2='OWN EXAMPLE', col=gold)],
          'THE SAME WAY EVERY TIME', gold, tag=T3, src=SSA),
]
# ---- 9: NOT LOST ----
S[9] = [
    slide('IT IS NOT LOST', 1423, [E('big', (150, 250, 1770, 560), 'that money is not lost', val='NOT LOST', sub='THE HELD BACK MONEY', size=210, vcol=green),
                                  E('stamp', (1280, 520, 1760, 640), 'not lost', t='RETURNS LATER', col=green, ang=-7, size=64)],
          'IT COMES BACK', green, tag=T3, src=SSA),
    slide('AT FULL RETIREMENT AGE', 1424, [E('icard', R3[0], 'when you reach', icon='clock', l1='REACH FULL AGE', l2='SIXTY-SEVEN', col=gold),
                                          E('icard', R3[1], 'the months that were', icon='bill', l1='MONTHS HELD BACK', l2='ARE COUNTED', col=gold),
                                          E('icard', R3[2], 'is increased', icon='chart', l1='BENEFIT INCREASED', l2='EVERY MONTH', col=green, c2=green)],
          'YOUR MONTHLY BENEFIT GOES UP', green, tag=T3, src=SSA),
    slide("SOCIAL SECURITY'S OWN EXAMPLE", 1425, [E('bars', (150, 250, 900, 700), 'in its own illustration', vals=[('12 MONTHS HELD', 910, '$910'), ('AT FULL AGE', 975, '$975')], lo=0.6),
                                                 E('card', (980, 260, 1770, 690), 'dan gets', head='FOR DAN', val='4 CHECKS BACK', vsize=70, vcol=green, col=green, sub='AS A HIGHER CHECK', icon='check', s=0.6)],
          'PERMANENTLY HIGHER', green, tag=T3, src=SSA),
]
# ---- 10: LIMIT 2 ----
S[10] = [
    slide('LIMIT NUMBER TWO', 1426, [E('person', (150, 250, 640, 700), 'which belongs to ruth', letter='R', name='RUTH', line='YEAR OF FULL AGE', col=green),
                                    E('big', (700, 260, 1770, 690), 'sixty-seven thousand', val='$67,920', sub='THE LIMIT IN THE YEAR YOU REACH 67', size=170, vcol=goldL)],
          'RUTH\'S LIMIT FOR 2027', green, tag=T4, src=SSA),
    slide('A GENTLER RATE', 1427, GRID((150, 250, 1770, 700), ['', 'ALL YEAR UNDER 67', 'YEAR YOU REACH 67'], [0.26, 0.37, 0.37],
                                      [('LIMIT', '$25,560', '$67,920'), ('HELD BACK', '$1 PER $2', '$1 PER $3')], ['gentler too', 'one dollar held back'], first='the rate is gentler', col=gold),
          'ONE DOLLAR FOR EVERY THREE', gold, tag=T4, src=SSA),
    slide('ONLY BEFORE THAT MONTH', 1428, [YG('and only'), YT(list(range(0, 7)), 'before the month', 'gold'),
                                          YM(7, 'you reach full', 'FULL RETIREMENT AGE'), YB(0, 6, 'counts', 'EARNINGS COUNT', 'BEFORE THAT MONTH')],
          'AFTER THAT, NO LIMIT', gold, tag=T4, src=SSA),
]
# ---- 11: RUTH'S MATH ----
S[11] = [
    slide('RUTH TURNS 67 IN AUGUST', 1429, [YG(None), YM(7, 'in august', 'TURNS 67'), YT(list(range(0, 7)), 'from january', 'gold'),
                                           YB(0, 6, 'through july', 'JAN-JUL: $79,920', 'SHE EARNS')],
          'SUPPOSE SHE EARNS $79,920', gold, tag=T4, src=SSA),
    slide('OVER THE LIMIT', 1430, [E('calc', (150, 260, 1770, 440), 'that is exactly', parts=[('$79,920', white, 80), ('−', goldL, 90), ('$67,920', white, 80), ('=', goldL, 90), ('$12,000', red, 90)], col=gold),
                                  E('calc', (150, 490, 1770, 670), 'one dollar for every', parts=[('$12,000', red, 80), ('÷', goldL, 90), ('3', white, 90), ('=', goldL, 90), ('$4,000', red, 90)], col=red)],
          '$4,000 IS HELD BACK', red, (255, 255, 255), tag=T4, src=SSA),
    slide('TWO CHECKS', 1431, [E('calc', (150, 260, 1770, 480), 'with a benefit', parts=[('$4,000', red, 84), ('÷', goldL, 84), ('$2,000', white, 84), ('=', goldL, 84), ('2', green, 120)], col=gold),
                              E('chip', (400, 540, 1520, 650), 'two checks', t='TWO CHECKS HELD BACK', ic=red)],
          'TWO CHECKS HELD BACK', red, (255, 255, 255), tag=T4, src=SSA),
    slide('FROM AUGUST: NOT COUNTED', 1432, [YG(None), YT(list(range(7, 12)), 'everything she earns', 'free'), YM(7, 'from august on', 'AUGUST'),
                                            YB(7, 11, 'not counted', 'NOT COUNTED AT ALL', 'NO LIMIT', green)],
          'EVERY DOLLAR FROM AUGUST ON', green, tag=T4, src=SSA),
]
# ---- 12: MONTHLY TEST ----
S[12] = [
    slide('THE RULE NOBODY MENTIONS', 1433, [E('big', (150, 250, 1770, 520), 'monthly test', val='MONTHLY TEST', sub='IN THE FIRST YEAR OF RETIREMENT', size=150, vcol=goldL),
                                            E('chip', (500, 580, 1420, 690), 'also uses', t='ALONGSIDE THE YEARLY LIMIT', ic=green, good=True)],
          'A SECOND TEST', gold, tag=T5, src=SSA),
    slide('THE 2027 MONTHLY LIMITS', 1434, [E('vs', (150, 250, 1770, 690), 'for twenty twenty-seven', cols=[('UNDER FULL AGE', '$2,130', 'PER MONTH', gold), ('YEAR YOU REACH IT', '$5,660', 'PER MONTH', green)], size=130)],
          'TWO MONTHLY LIMITS', gold, tag=T5, src=SSA),
    slide('LESS THAN THE LIMIT = FULL CHECK', 1435, [E('icard', (150, 260, 760, 690), 'you earn less', icon='wallet', l1='EARN LESS', l2='THAN THE MONTHLY LIMIT', col=gold),
                                                    E('arrow', (800, 400, 1000, 540), 'you get', col=goldL),
                                                    E('icard', (1040, 260, 1770, 690), 'full check', icon='check', l1='FULL CHECK', l2='FOR THAT MONTH', col=green, c2=green)],
          'ANY MONTH UNDER THE LIMIT', green, tag=T5, src=SSA),
]
# ---- 13: LENA ----
S[13] = [
    slide('MEET LENA', 1436, [E('person', R3[0], None, letter='L', name='LENA, 64', line='RETIRES IN JUNE', col=gold),
                             E('card', R3[1], 'works until', head='WORKS UNTIL', val='END OF MAY', vsize=70, col=gold, icon='brief', s=0.6),
                             E('card', R3[2], 'well over', head='EARNS', val='WELL OVER THE LIMIT', vsize=40, col=red, vcol=red, icon='wallet', s=0.6)],
          'WELL OVER THE YEARLY LIMIT', gold, tag=T5, src=SSA),
    slide('JUNE TO DECEMBER', 1437, [E('mbars', GBAR, None, gbox=GBAR, limit_label='MONTHLY LIMIT'),
                                    E('mbar', GBAR, 'in june she retires', gbox=GBAR, idx=[0, 1, 2, 3, 4], h=[0.92, 0.88, 0.96, 0.9, 0.94], col=red),
                                    E('mbar', GBAR, 'she earns nothing', gbox=GBAR, idx=[5, 6, 7, 8, 9, 10, 11], h=0.0, col=green, lab='$0'),
                                    E('stamp', (1000, 330, 1720, 470), 'full check for each', t='FULL CHECK EACH MONTH', col=green, ang=-6, size=68)],
          'EVERY MONTH UNDER THE MONTHLY LIMIT', green, tag=T5, src=SSA),
    slide('ONE WARNING', 1438, [E('icard', R2[0], 'one year', icon='clock', l1='ONE YEAR ONLY', l2='USUALLY THE FIRST YEAR', col=gold),
                               E('icard', R2[1], 'if you run', icon='brief', l1='YOUR OWN BUSINESS?', l2='SUBSTANTIAL SERVICES', col=red, c2=red)],
          'THE MONTHLY TEST HAS LIMITS', red, (255, 255, 255), tag=T5, src=SSA),
]
# ---- 14: WHAT COUNTS ----
S[14] = [
    slide('WHAT COUNTS AS EARNINGS', 1439, [E('icard', R2[0], 'wages from a job', icon='brief', l1='WAGES', l2='FROM A JOB', col=green, c2=green),
                                           E('icard', R2[1], 'net earnings', icon='bag', l1='NET EARNINGS', l2='FROM SELF-EMPLOYMENT', col=green, c2=green),
                                           E('line', (150, 660, 1770, 720), 'bonuses', t='BONUSES, COMMISSIONS AND VACATION PAY TOO', size=44, col=goldL)],
          'ONLY WORK INCOME COUNTS', green, tag='WHAT COUNTS', src=SSA),
    slide('WHEN IT COUNTS', 1440, [E('vs', (150, 250, 1770, 690), 'wages count', cols=[('WAGES', 'EARNED', 'COUNT WHEN YOU EARN THEM', gold), ('SELF-EMPLOYMENT', 'RECEIVED', 'COUNTS WHEN YOU RECEIVE IT', blue)], size=100)],
          'TWO DIFFERENT TIMINGS', gold, tag='WHAT COUNTS', src=SSA),
    slide('WHAT DOES NOT COUNT', 1441, [E('chip', (150, 250, 940, 380), 'pensions', t='PENSIONS', ic=red), E('chip', (980, 250, 1770, 380), 'annuities', t='ANNUITIES', ic=red),
                                       E('chip', (150, 420, 940, 550), 'investment income', t='INVESTMENT INCOME', ic=red), E('chip', (980, 420, 1770, 550), 'interest', t='INTEREST', ic=red),
                                       E('chip', (150, 590, 940, 720), 'veterans benefits', t='VETERANS BENEFITS', ic=red), E('chip', (980, 590, 1770, 720), 'other government', t='GOV. OR MILITARY RETIREMENT', ic=red, size=34)],
          'NONE OF THIS COUNTS', red, (255, 255, 255), tag='WHAT COUNTS', src=SSA),
    slide('A PENSION NEVER REDUCES IT', 1442, [E('icard', R2[0], 'so a pension check', icon='bank', l1='A PENSION CHECK', l2='NOT COUNTED', col=gold),
                                              E('icard', R2[1], 'never reduces', icon='check', l1='YOUR SOCIAL SECURITY', l2='NEVER REDUCED BY IT', col=green, c2=green)],
          'PENSIONS ARE SAFE', green, tag='WHAT COUNTS', src=SSA),
]
# ---- 15: CHECKLIST ----
S[15] = [
    slide('YOUR CHECKLIST: 1 AND 2', 1443, [E('numcol', R2[0], 'find out', n=1, icon='doc', l1='FIND YOUR LIMIT', l2='BIRTH YEAR + FULL AGE'),
                                           E('numcol', R2[1], 'add up', n=2, icon='wallet', l1='ADD UP YOUR PAY', l2='COMPARE TO THE LIMIT')],
          'BEFORE JANUARY', gold, tag=T6, src=SSA),
    slide('YOUR CHECKLIST: 3 AND 4', 1444, [E('numcol', R2[0], 'three if you are close', n=3, icon='clock', l1='FIND THE MONTH', l2='FULL AGE BEGINS'),
                                           E('numcol', R2[1], 'four if you plan', n=4, icon='phone', l1='RETIRING MID-YEAR?', l2='ASK ABOUT THE MONTHLY TEST')],
          'NO SURPRISES', green, tag=T6, src=SSA),
]
# ---- 16: RECAP ----
S[16] = [
    slide('RECAP: 1 AND 2', 1445, [E('rule', (180, 290, 1740, 450), 'one twenty-five thousand', n=1, text='UNDER FULL AGE: $25,560', val='$1 PER $2 OVER'),
                                  E('rule', (180, 500, 1740, 660), 'two sixty-seven thousand', n=2, text='YEAR YOU REACH 67: $67,920', val='$1 PER $3', vc=green)],
          'TWO YEARLY LIMITS', gold, tag='RECAP', src=SSA),
    slide('RECAP: 3 AND 4', 1446, [E('rule', (180, 290, 1740, 450), 'three two thousand', n=3, text='MONTHLY TEST: $2,130', val='FULL CHECK'),
                                  E('rule', (180, 500, 1740, 660), 'four held back', n=4, text='HELD BACK MONEY', val='ADDED LATER', vc=green)],
          'TWO MORE TO KEEP', green, tag='RECAP', src=SSA),
    slide('RECAP: 5', 1447, [E('rule', (180, 330, 1740, 530), 'five dan\'s', n=5, text="DAN'S 4 CHECKS", val='CAME BACK HIGHER', vc=green)],
          'THE FIFTH NUMBER', green, tag='RECAP', src=SSA),
]
# ---- 17: CTA + DISCLAIMER ----
def final14(t, seed=214):
    Dd = CUR['D']
    fr = base(t); fr = amb(fr, t, seed, 7, 55); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('General information,', white, 250), ('not financial advice.', white, 315), ('Rules, amounts and ages change,', goldL, 410),
             ('so confirm with Social Security', goldL, 475), ('before you act. Not affiliated', white, 570), ('with Social Security.', white, 635)]
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
S[17] = [
    slide('SEND IT TO SOMEONE', 1448, [E('icard', (500, 260, 1420, 690), None, icon='mail', l1='SOMEONE WHO WORKS', l2='WHILE COLLECTING', col=gold)],
          'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 1449, [E('line', (200, 330, 1720, 430), None, t='DID ANYONE EXPLAIN', size=88, col=white),
                                           E('line', (200, 470, 1720, 570), 'before you claimed', t='THE EARNINGS LIMIT TO YOU?', size=88, col=goldL)],
          'ANSWER IN THE COMMENTS'),
    frozen(final14),
]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
CUTS = {1: ['in twenty twenty-seven', 'the difference is'], 2: ['ruth was born', 'both still have'], 3: ['no news articles'], 4: ['stay under'],
        5: ['from the month', 'that means everything'], 6: ['this year it is', 'earn up to'], 7: ['that is exactly', 'half of twelve'],
        8: ['so dan receives', 'social security\'s own'], 9: ['social security says', 'in its own'], 10: ['the rate is gentler', 'and only'],
        11: ['that is exactly', 'with a benefit', 'and everything'], 12: ['for twenty twenty-seven', 'in any month'], 13: ['in june', 'one warning'],
        14: ['wages count', 'what does not count', 'so a pension'], 15: ['three if you are close'], 16: ['three two thousand', 'five dan\'s'], 17: ['and tell me', 'one last thing']}
for _b, _ph in CUTS.items():
    _tot = sum(SPEC[_b]); _c = [0] + [round((V.at(_b, p) - 0.2) * 30) for p in _ph] + [_tot]
    SPEC[_b] = [_c[i + 1] - _c[i] for i in range(len(_c) - 1)]
if os.environ.get('PV'):   # solo anteprima layout dei blocchi senza voce: durate finte uguali
    for _b in SLIDES:
        if not os.path.exists(os.path.join(VID, 'voce', f'b{_b}.wav')): SPEC[_b] = [750 // len(SLIDES[_b])] * len(SLIDES[_b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v14', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
