"""Video 16 - Lettera di sovrapagamento Social Security (Carol) - 17 blocchi. Uso: python3 v16.py render|preview|spec <blocco> [slide,slide]
Sfondo/testata/schede cambiati un po' rispetto al video 15 (v16eng.py), elementi nuovi: lettera ufficiale con righe, assegno diviso a meta', linea dei giorni, porte, modulo SSA, cartellina.
Solo cio' che la voce dice, ogni elemento compare sulla sua parola (max 80%)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v16eng import *
import v16eng

R2 = row(2); R3 = row(3); R4 = row(4, y1=560); R3s = row(3, y1=560); R3b = row(3, y0=290, y1=640)
SRC = 'SSA.GOV'
G1, G2, G3, G4, G5, G6 = 'THE LETTER', 'MOVE 1 OF 4', 'MOVE 2 OF 4', 'MOVE 3 OF 4', 'MOVE 4 OF 4', 'RECAP'
T14, T15, T16 = 'IF NOTHING', 'APRIL TWIST', 'AVOID IT'
PB = (150, 245, 1110, 715)
def NR(i, n, cue, label, val, vc='navy', hl=False): return E('nrow', nrow_box(PB, i, n), cue, pbox=PB, i=i, n=n, label=label, val=val, vc=vc, hl=hl)
def CH(box, cue, t, good=True, size=40): return E('chip', box, cue, t=t, good=good, ic=(green if good else red), size=size)
def DAYS(zones, marks, mx=60): return dict(zones=zones, marks=marks, mx=mx)
S = {}
# ---- 1: GANCIO ----
S[1] = [
    slide('A LETTER ARRIVES', 4101, [E('ovsel', (160, 290, 650, 600), 'a letter arrives', l1='FROM SOCIAL SECURITY', col=gold),
                                     E('card', (780, 310, 1250, 560), 'it says you were overpaid', head='THE MESSAGE', val='YOU WERE OVERPAID', vsize=54, vcol=white, col=red),
                                     E('card', (1320, 310, 1770, 560), 'wants the money back', head='THEY WANT', val='IT BACK', vsize=88, vcol=goldL, col=gold)],
          'A LETTER, A DEBT', gold, src=SRC),
    slide('IF YOU DO NOT ANSWER', 4102, [E('paycut', (170, 260, 1750, 560), 'half of every monthly check', head='YOUR MONTHLY CHECK', total='EVERY MONTH', kept='HALF KEPT', held='HALF GONE', kept_l='YOU RECEIVE', held_l='THE AGENCY KEEPS', frac=0.5),
                                         E('stamp', (1100, 600, 1700, 720), 'automatically', t='AUTOMATIC', col=red, ang=-5, size=70),
                                         CH((170, 600, 1060, 700), 'until the debt is gone', 'UNTIL THE DEBT IS GONE', False, 46)],
          'HALF OF EVERY CHECK', red, (255, 255, 255), src=SRC),
    slide('FOUR MOVES', 4103, [E('card', R4[0], 'four moves', head='MOVE', val='1', vsize=150, vcol=goldL, col=gold, sub='?'),
                              E('card', R4[1], None, head='MOVE', val='2', vsize=150, vcol=goldL, col=gold, sub='?'),
                              E('card', R4[2], None, head='MOVE', val='3', vsize=150, vcol=goldL, col=gold, sub='?'),
                              E('card', R4[3], None, head='MOVE', val='4', vsize=150, vcol=goldL, col=gold, sub='?'),
                              CH((220, 600, 960, 700), 'two of them freeze', '2 FREEZE THE DEDUCTIONS', True, 40),
                              CH((990, 600, 1700, 700), 'one has no deadline', '1 HAS NO DEADLINE', True, 40)],
          'WHICH ONE FITS YOUR LETTER?', gold, src=SRC),
]
# ---- 2: ISCRIZIONE + CAROL ----
S[2] = [
    slide('THE MONEY BACKSTORY', 4104, [E('line', (200, 280, 1720, 360), 'where we turn official rules', t='OFFICIAL RULES  >  REAL NUMBERS', size=70, col=goldL),
                                       E('subbtn', (600, 450, 1320, 600), 'subscribe now', t='SUBSCRIBE')],
          'IF THAT HELPS, SUBSCRIBE', gold),
    slide('MEET CAROL', 4105, [E('person', (170, 260, 700, 700), 'meet carol', letter='C', name='CAROL, 66', line='RETIRED', line2='SOCIAL SECURITY', col=blue),
                              E('pay', (820, 290, 1760, 650), 'two thousand one hundred', amount='$2,100', sub='PER MONTH', head='CAROL\'S SOCIAL SECURITY CHECK', size=150)],
          'HER MONTHLY CHECK', gold, src=SRC),
    slide('THEN COMES THE ENVELOPE', 4106, [E('ovsel', (150, 300, 430, 540), 'then comes the envelope', col=gold),
                                           E('card', (490, 290, 810, 570), 'six hundred dollars too much', head='TOO MUCH', val='$600', sub='EVERY MONTH', vsize=96, vcol=red, col=red),
                                           E('op', (820, 380, 910, 480), None, t='x', size=100),
                                           E('card', (920, 290, 1220, 570), 'fifteen months', head='FOR', val='15', sub='MONTHS', vsize=110, vcol=white, col=blue),
                                           E('op', (1230, 380, 1320, 480), None, t='=', size=100),
                                           E('card', (1330, 290, 1770, 570), 'nine thousand', head='SHE OWES', val='$9,000', sub='IN TOTAL', vsize=96, vcol=red, col=red)],
          'THE TOTAL SHE OWES', red, (255, 255, 255), src=SRC),
]
# ---- 3: LA LETTERA ----
S[3] = [
    slide('INSIDE THE ENVELOPE', 4107, [E('paper', PB, 'what is inside', head='NOTICE OF OVERPAYMENT', bars=True),
                                       E('icard', (1200, 290, 1770, 650), 'the notice must list', icon='doc', l1='THE NOTICE MUST LIST', l2='ALL FIVE ITEMS', col=gold)],
          'THE MANUAL: WHAT MUST BE LISTED', gold, tag=G1, src='SSA POMS'),
    slide('THE FIVE ITEMS', 4158, [E('paper', PB, None, head='NOTICE OF OVERPAYMENT'),
                                  NR(0, 5, 'the total', 'THE TOTAL OWED', '$9,000', 'red', True),
                                  NR(1, 5, 'what you were paid', 'WHAT YOU WERE PAID', '$2,100 / MONTH'),
                                  NR(2, 5, 'what you should have been paid', 'WHAT YOU SHOULD HAVE BEEN PAID', '$1,500 / MONTH'),
                                  NR(3, 5, 'why the amount was different', 'WHY IT WAS DIFFERENT', 'THE REASON'),
                                  NR(4, 5, 'the months involved', 'THE MONTHS INVOLVED', '15 MONTHS')],
          'ALL FIVE, ON ONE PAGE', gold, tag=G1, src='SSA POMS'),
    slide('THREE RIGHTS', 4108, [E('icard', R3[0], 'a reconsideration', icon='check', l1='RECONSIDERATION', l2='DISPUTE THE DEBT', col=green, c2=green),
                                E('icard', R3[1], 'a waiver', icon='doc', l1='WAIVER', l2='ASK TO CANCEL IT', col=gold),
                                E('icard', R3[2], 'a different repayment rate', icon='coins', l1='DIFFERENT RATE', l2='ASK FOR LESS', col=blue, c2=goldL)],
          'YOUR THREE RIGHTS', gold, tag=G1, src='SSA POMS'),
    slide('READ EVERY LINE', 4109, [E('big', (170, 270, 1750, 560), 'a number of days', val='? DAYS', sub='ONE LINE MATTERS MORE THAN THE REST', size=210, vcol=goldL)],
          'IT IS ABOUT A NUMBER OF DAYS', red, (255, 255, 255), tag=G1, src='SSA POMS'),
]
# ---- 4: IL 50% ----
S[4] = [
    slide('THE DANGER', 4110, [E('card', (160, 270, 760, 600), 'the letter asks for', head='THE LETTER ASKS FOR', val='$9,000', sub='FULL AND IMMEDIATE REFUND', vsize=120, vcol=red, col=red),
                              E('arrow', (790, 380, 900, 480), 'if the money does not'),
                              E('icard', (940, 270, 1770, 600), 'withhold part of your monthly benefit', icon='bill', l1='NO REFUND? THEY WITHHOLD', l2='PART OF EVERY MONTHLY BENEFIT', col=gold, size=48)],
          'REFUND FIRST, THEN DEDUCTIONS', red, (255, 255, 255), tag=G1, src='SSA EM-25029'),
    slide('THE DEFAULT RATE', 4111, [E('cal', (160, 300, 820, 540), 'april twentyfifth', head='NOTICES SENT ON OR AFTER', big='APR 25, 2025', size=76, col=gold),
                                    E('big', (900, 280, 1760, 600), 'fifty percent', val='50%', sub='UP TO HALF OF THE MONTHLY BENEFIT', size=230, vcol=red)],
          'THE DEFAULT: UP TO 50%', red, (255, 255, 255), tag=G1, src='SSA EM-25029'),
    slide('CAROL\'S CHECK', 4112, [E('paycut', (160, 240, 1760, 548), 'for carol', head='CAROL\'S CHECK', total='$2,100', kept='$1,050', held='$1,050', kept_l='SHE RECEIVES', held_l='HELD BACK EVERY MONTH', frac=0.5),
                                  E('mgrid', (160, 575, 1760, 705), None, gbox=(160, 575, 1760, 705), ncols=12, nrows=1, hmax=130, small=True),
                                  E('mtile', (160, 575, 1760, 705), 'nine months', gbox=(160, 575, 1760, 705), ncols=12, nrows=1, hmax=130, idx=list(range(9)), status='held', small=True),
                                  E('stamp', (640, 236, 1280, 326), 'no phone call', t='NO CALL NEEDED', col=red, ang=-3, size=50)],
          'THE $9,000 IS GONE IN ABOUT 9 MONTHS', red, (255, 255, 255), tag=G1, src='SSA EM-25029'),
    slide('HOLD ON TO THAT DATE', 4113, [E('cal', (560, 330, 1360, 570), 'hold on to that', head='REMEMBER THE DATE', big='APR 25, 2025', size=100, col=gold)],
          'IT MATTERS LATER', gold, tag=G1, src='SSA EM-25029'),
]
# ---- 5: I TRENTA GIORNI ----
S[5] = [
    slide('THE NUMBER OF DAYS', 4114, [E('dtl', (150, 240, 1770, 720), 'the number of days', zones=[(0, 30, green, '30 DAYS TO RESPOND'), (30, 60, (60, 82, 112), 'MORE TIME TO FIGHT')],
                                       marks=[(0, 'DAY 0', 'DATE ON THE NOTICE', goldL), (30, 'DAY 30', 'COLLECTION STOPS', green)], mx=60),
                                    E('stamp', (900, 625, 1700, 715), 'stop collection activity', t='COLLECTION STOPS', col=green, ang=-3, size=56)],
          'RESPOND WITHIN 30 DAYS', green, navy, tag=G1, src='SSA POMS'),
    slide('TIME TO FIGHT IT', 4115, [E('icard', R2[0], 'the notice itself sets', icon='clock', l1='REFUND DATE', l2='AT LEAST 30 DAYS AWAY', col=gold),
                                    E('icard', R2[1], 'does not begin withholding', icon='check', l1='NO WITHHOLDING', l2='RIGHT AWAY', col=green, c2=green)],
          'THE RULES GIVE YOU TIME', gold, tag=G1, src='SSA EM-25029'),
    slide('THE FOUR MOVES', 4116, [E('step', (170, 245, 1750, 345), 'four moves', n=1, text='CHECK THE DEBT', val='STOP IT', col=gold),
                                  E('step', (170, 370, 1750, 470), None, n=2, text='ASK FOR A WAIVER', val='ERASE IT', col=gold),
                                  E('step', (170, 495, 1750, 595), None, n=3, text='ASK FOR A SMALLER PAYMENT', val='SHRINK IT', col=gold),
                                  E('step', (170, 620, 1750, 720), None, n=4, text='THE PERSONAL CONFERENCE', val='SECOND CHANCE', col=gold)],
          'TIME ONLY HELPS WHO USES IT', gold, tag=G1, src='SSA POMS'),
]
# ---- 6: MOSSA 1 ----
S[6] = [
    slide('CHECK THE DEBT', 4117, [E('icard', (500, 260, 1420, 690), 'move number one', icon='check', l1='CHECK THE DEBT', l2='IS IT EVEN CORRECT?', col=green, c2=green, size=56)],
          'MOVE 1: CHECK THE DEBT', gold, tag=G2, src='SSA POMS'),
    slide('FACT, AMOUNT, 60 DAYS', 4118, [E('icard', (150, 250, 940, 540), 'the fact', icon='check', l1='THE FACT', l2='WAS I OVERPAID AT ALL?', col=green, c2=green),
                                         E('icard', (980, 250, 1770, 540), 'or the amount', icon='bill', l1='THE AMOUNT', l2='IS THE TOTAL RIGHT?', col=blue, c2=goldL),
                                         E('card', (400, 570, 1520, 720), 'the deadline is sixty', head='ASK FOR A RECONSIDERATION  -  DEADLINE', val='60 DAYS FROM THE NOTICE', vsize=60, vcol=red, col=red)],
          'MOVE 1: A RECONSIDERATION', gold, tag=G2, src='SSA POMS'),
    slide('THREE WAYS TO START', 4119, [E('icard', R3[0], 'the national number', icon='phone', l1='CALL', l2='1-800-772-1213', col=gold),
                                       E('icard', R3[1], 'visiting a field office', icon='bank', l1='VISIT', l2='A FIELD OFFICE', col=blue, c2=goldL),
                                       E('icard', R3[2], 'or writing', icon='mail', l1='WRITE', l2='A SIGNED REQUEST', col=green, c2=green)],
          'CALL, VISIT OR WRITE', gold, tag=G2, src='SSA POMS'),
    slide('GIVE A SPECIFIC REASON', 4120, [CH((200, 270, 1720, 380), 'i did not work', 'I DID NOT WORK', True, 56),
                                          CH((200, 410, 1720, 520), 'i did not receive a pension', 'I DID NOT RECEIVE A PENSION', True, 56),
                                          CH((200, 550, 1720, 660), 'i do not agree', 'I DO NOT AGREE  (TOO VAGUE)', False, 56)],
          'BE SPECIFIC', gold, tag=G2, src='SSA POMS'),
]
# ---- 7: AUDIZIONE VS RINUNCIA ----
S[7] = [
    slide('WHILE THEY DECIDE', 4121, [E('paycut', (170, 270, 1750, 560), 'while the agency decides', head='WHILE THE AGENCY DECIDES', total='$2,100', kept='FULL CHECK', held='', kept_l='NO DEDUCTIONS', held_l='', frac=0.0),
                                     E('stamp', (1150, 590, 1700, 700), 'stops collecting', t='PAUSED', col=green, ang=-5, size=80),
                                     CH((170, 600, 1090, 700), 'does not fully reverse', 'THE DEBT IS NOT FULLY REVERSED', False, 44)],
          'COLLECTION STOPS', green, navy, tag=G2, src='SSA EM-25029'),
    slide('IF THE DEBT STANDS', 4122, [E('card', (170, 280, 760, 620), 'recovery will begin', head='RECOVERY BEGINS', val='60 DAYS', sub='AFTER THE DECISION', vsize=100, vcol=red, col=red),
                                      E('icard', (880, 280, 1770, 620), 'even if you then ask for a hearing', icon='clock', l1='EVEN IF YOU ASK', l2='FOR A HEARING', col=gold)],
          'THE DEBT IS NOT FULLY REVERSED', red, (255, 255, 255), tag=G2, src='SSA POMS'),
    slide('HEARING VS WAIVER', 4123, [E('vs', (170, 250, 1750, 700), 'a hearing request does not', cols=[('A HEARING REQUEST', 'NO PAUSE', 'THE DEDUCTIONS KEEP GOING', red), ('A WAIVER REQUEST', 'PAUSE', 'NO DEDUCTIONS UNTIL A DECISION', green)], size=120)],
          'ON TO MOVE TWO', gold, tag=G2, src='SSA POMS'),
]
# ---- 8: MOSSA 2 ----
S[8] = [
    slide('MOVE 2: THE WAIVER', 4124, [E('big', (170, 270, 1750, 560), 'move number two', val='THE WAIVER', sub='ASK TO CANCEL THE DEBT', size=190, vcol=goldL),
                                    E('stamp', (500, 570, 1420, 700), 'it has no deadline', t='NO DEADLINE', col=green, ang=-3, size=110)],
          'ASK ANY TIME', gold, tag=G3, src='SSA POMS'),
    slide('YOU MAY ASK AT ANY TIME', 4125, [CH((200, 245, 1720, 330), 'when the notice arrives', 'WHEN THE NOTICE ARRIVES', True, 48),
                                           CH((200, 345, 1720, 430), 'at the same time as your appeal', 'AT THE SAME TIME AS YOUR APPEAL', True, 48),
                                           CH((200, 445, 1720, 530), 'after the deductions have started', 'AFTER THE DEDUCTIONS HAVE STARTED', True, 48),
                                           CH((200, 545, 1720, 630), 'even after the whole debt', 'EVEN AFTER THE WHOLE DEBT IS COLLECTED', True, 48),
                                           CH((200, 645, 1720, 730), 'even after an earlier request', 'EVEN AFTER AN EARLIER REQUEST WAS DENIED', True, 48)],
          'THERE IS NO DEADLINE', gold, tag=G3, src='SSA POMS'),
    slide('IF IT IS APPROVED', 4126, [E('icard', (500, 260, 1420, 690), 'refund what it already', icon='bill', l1='REFUND OF WHAT WAS WITHHELD', l2='THE AGENCY MAY PAY IT BACK', col=green, c2=green, size=48)],
          'A POSSIBLE REFUND', green, navy, tag=G3, src='SSA POMS'),
    slide('HOW TO ASK', 4127, [E('ssaform', (150, 250, 650, 720), 'you ask on form', code='FORM SSA-632-BK', name='REQUEST FOR WAIVER OF\nOVERPAYMENT RECOVERY', lines=4, ticks=(0, 1), col=gold),
                              CH((760, 270, 1760, 360), 'by mail', 'BY MAIL', True, 52), CH((760, 385, 1760, 475), 'by fax', 'BY FAX', True, 52),
                              CH((760, 500, 1760, 590), 'at the office', 'AT THE OFFICE', True, 52), CH((760, 615, 1760, 705), 'by uploading it', 'UPLOAD: my Social Security', True, 48)],
          'FORM SSA-632-BK', gold, tag=G3, src='SSA POMS'),
]
# ---- 9: PRIMO CANCELLO ----
S[9] = [
    slide('TWO GATES', 4128, [E('icard', R2[0], 'two gates', icon='lock', l1='GATE ONE', l2='FAULT', col=gold),
                             E('icard', R2[1], None, icon='lock', l1='GATE TWO', l2='COMING UP', col=blue, c2=goldL)],
          'A WAIVER HAS TWO GATES', gold, tag=G3, src='SSA POMS'),
    slide('AT FAULT ONLY WITH EVIDENCE', 4129, [CH((180, 250, 1740, 340), 'gave information you knew', 'GAVE INFORMATION YOU KNEW WAS WRONG', False, 50),
                                               CH((180, 365, 1740, 455), 'failed to give information', 'DID NOT GIVE INFORMATION YOU KNEW MATTERED', False, 46),
                                               CH((180, 480, 1740, 570), 'accepted a payment you knew', 'ACCEPTED A PAYMENT YOU KNEW WAS INCORRECT', False, 46),
                                               E('stamp', (700, 610, 1720, 710), 'without that evidence', t='NO EVIDENCE = NOT AT FAULT', col=green, ang=-2, size=52)],
          'FAULT NEEDS EVIDENCE', red, (255, 255, 255), tag=G3, src='SSA POMS'),
    slide('PRESUMED NOT AT FAULT', 4130, [CH((180, 270, 1740, 390), 'reported a change on time', 'YOU REPORTED A CHANGE ON TIME', True, 54),
                                         CH((180, 420, 1740, 540), 'payments kept coming', 'PAYMENTS KEPT COMING AFTER YOU REPORTED', True, 50),
                                         CH((180, 570, 1740, 690), 'error in computing', 'THE AGENCY MADE AN ERROR IN COMPUTING YOUR BENEFIT', True, 44)],
          'THE MANUAL PRESUMES: NOT AT FAULT', green, navy, tag=G3, src='SSA POMS'),
]
# ---- 10: TRE PORTE ----
D1 = (230, 250, 560, 725); D2 = (795, 250, 1125, 725); D3 = (1360, 250, 1690, 725)
S[10] = [
    slide('THE SECOND GATE', 4131, [E('door', D1, 'three doors', n=1, l1='SMALL DEBTS', l2='DOOR ONE', col=green),
                                   E('door', D2, None, n=2, l1='HARDSHIP', l2='DOOR TWO', col=gold),
                                   E('door', D3, None, n=3, l1='FAIRNESS', l2='DOOR THREE', col=blue)],
          'YOU NEED ONLY ONE DOOR', gold, tag=G3, src='SSA POMS'),
    slide('DOOR 1: SMALL DEBTS', 4132, [E('door', (150, 250, 440, 725), 'door one is small', n=1, l1='SMALL DEBTS', l2='DOOR ONE', col=green),
                                       E('card', (540, 260, 1130, 560), 'two thousand dollars or less', head='ORIGINAL OVERPAYMENT', val='$2,000', sub='OR LESS', vsize=130, vcol=green, col=green),
                                       CH((540, 600, 1770, 710), 'fault is not an issue', 'AND FAULT IS NOT AN ISSUE', True, 50),
                                       E('card', (1220, 260, 1770, 560), 'ask by phone', head='YOU CAN ASK', val='BY PHONE', sub='NO LONG FORM NEEDED', vsize=84, vcol=goldL, col=gold)],
          'SMALL DEBT: WAIVED', green, navy, tag=G3, src='SSA POMS'),
    slide('DOOR 2: HARDSHIP', 4133, [E('door', (150, 250, 440, 725), 'door two is hardship', n=2, l1='HARDSHIP', l2='DOOR TWO', col=gold),
                                    E('card', (540, 260, 1130, 600), 'two hundred fifty', head='INCOME OVER LIVING COSTS', val='$250', sub='A MONTH, AT MOST', vsize=130, vcol=goldL, col=gold),
                                    E('card', (1220, 260, 1770, 600), 'six thousand dollars or less', head='YOUR RESOURCES', val='$6,000', sub='SAVINGS AND OTHER ASSETS', vsize=100, vcol=goldL, col=gold),
                                    CH((540, 630, 1770, 715), 'or ten thousand', 'OR $10,000 WITH A SPOUSE OR DEPENDENT', True, 44)],
          'CANNOT AFFORD IT', gold, tag=G3, src='SSA POMS'),
    slide('DOOR 3: FAIRNESS', 4134, [E('door', (700, 250, 1000, 725), 'door three is about fairness', n=3, l1='FAIRNESS', l2='DOOR THREE', col=blue),
                                    E('big', (1050, 330, 1770, 600), 'fairness', val='FAIRNESS', sub='DOOR THREE', size=110, vcol=goldL)],
          'THE THIRD DOOR', blue, (255, 255, 255), tag=G3, src='SSA POMS'),
]
# ---- 11: PORTA 3 + CAROL ----
S[11] = [
    slide('AGAINST EQUITY AND GOOD CONSCIENCE', 4135, [E('door', (150, 250, 440, 725), 'the manual calls the third door', n=3, l1='FAIRNESS', l2='DOOR THREE', col=blue),
                                                      CH((540, 290, 1770, 400), 'relied on a payment', 'YOU RELIED ON A PAYMENT NOT DUE', True, 54),
                                                      CH((540, 440, 1770, 550), 'your finances changed for the worse', 'AND YOUR FINANCES GOT WORSE', True, 54),
                                                      E('line', (540, 600, 1770, 660), None, t='NO INCOME OR SAVINGS LIMIT', size=44, col=goldL)],
          'THE FAIRNESS TEST', blue, (255, 255, 255), tag=G3, src='SSA POMS', tsize=50),
    slide('BACK TO CAROL', 4136, [E('person', (170, 270, 700, 690), 'back to carol', letter='C', name='CAROL, 66', line='$9,000 OWED', col=blue),
                                 CH((800, 300, 1770, 420), 'made the error', 'THE AGENCY MADE THE ERROR', True, 52),
                                 CH((800, 470, 1770, 590), 'not at fault', 'SO SHE IS PRESUMED NOT AT FAULT', True, 50),
                                 E('stamp', (1000, 610, 1700, 710), 'the first gate is open', t='GATE ONE: OPEN', col=green, ang=-4, size=60)],
          'THE FIRST GATE IS OPEN', green, navy, tag=G3, src='SSA POMS'),
    slide('CAROL IS ABOVE THE LINE', 4137, [E('card', (160, 280, 640, 620), 'nine thousand dollars', head='CAROL OWES', val='$9,000', vsize=100, vcol=red, col=red),
                                           E('op', (650, 400, 760, 500), None, t='>', size=110),
                                           E('card', (770, 280, 1150, 620), 'the small-debt line', head='SMALL-DEBT LINE', val='$2,000', vsize=84, vcol=green, col=green),
                                           E('card', (1190, 280, 1770, 620), 'weigh hardship or fairness', head='THE AGENCY WEIGHS', val='HARDSHIP', sub='OR FAIRNESS', vsize=56, vcol=goldL, col=gold)],
          'IF NO, THERE IS A MOVE FOUR', gold, tag=G3, src='SSA POMS'),
]
# ---- 12: MOSSA 3 ----
S[12] = [
    slide('MOVE 3: ASK FOR LESS', 4138, [E('line', (200, 245, 1720, 325), 'move number three', t='SHRINK THE PAYMENT', size=76, col=goldL),
                                  E('bigvs', (170, 350, 1750, 715), 'withholding is available', cols=[('THE DEFAULT', '50%', 'OF THE MONTHLY BENEFIT', red), ('YOU CAN ASK', 'LESS', 'A DIFFERENT RATE', green)], mid='>')],
          'A DIFFERENT RATE OF WITHHOLDING', gold, tag=G4, src='SSA POMS'),
    slide('THE RATE LADDER', 4139, [E('step', (170, 270, 1750, 420), 'staff first try', n=1, text='WITHIN 12 MONTHS  /  NEVER BELOW $10', val='NO FORMS', col=green),
                                   E('step', (170, 460, 1750, 610), 'for up to sixty months', n=2, text='UP TO 60 MONTHS', val='INCOME + COSTS', col=gold)],
          'THE LONGER IT TAKES, THE MORE THEY ASK', gold, tag=G4, src='SSA POMS'),
    slide('CAROL ASKS FOR $300', 4140, [E('card', (170, 280, 600, 600), 'carol asks for three hundred', head='SHE ASKS', val='$300', sub='A MONTH', vsize=120, vcol=goldL, col=gold),
                                       E('op', (610, 380, 720, 500), None, t='=', size=110),
                                       E('card', (730, 280, 1160, 600), 'which finishes in thirty', head='FINISHED IN', val='30', sub='MONTHS', vsize=130, vcol=green, col=green),
                                       E('card', (1240, 280, 1770, 600), 'finishes in thirty months', head='THE AGENCY ASKS FOR', val='INCOME', sub='EXPENSES AND RESOURCES', vsize=64, vcol=goldL, col=blue)],
          '$9,000 / $300 = 30 MONTHS', gold, tag=G4, src='SSA POMS'),
    slide('LONGER THAN 60 MONTHS', 4141, [E('ssaform', (200, 250, 700, 720), 'longer than that', code='FORM SSA-634', name='REQUEST FOR CHANGE IN\nOVERPAYMENT RECOVERY RATE', lines=4, ticks=(0, 2), col=gold),
                                         E('card', (860, 300, 1750, 620), 'six thirty-four', head='THE LONGER FORM', val='SSA-634', sub='FOR RECOVERY BEYOND 60 MONTHS', vsize=110, vcol=goldL, col=gold)],
          'THE LONGER FORM', gold, tag=G4, src='SSA POMS'),
]
# ---- 13: MOSSA 4 ----
S[13] = [
    slide('MOVE 4: THE SECOND CHANCE', 4142, [E('line', (200, 240, 1720, 320), 'move number four', t='THE SECOND CHANCE', size=76, col=goldL),
                                             E('stamp', (170, 335, 860, 425), 'cannot approve your waiver', t='WAIVER NOT APPROVED', col=red, ang=-3, size=50),
                                             E('card', (160, 495, 880, 715), 'a file review', head='STEP ONE', val='FILE REVIEW', sub='BEFORE ANY DENIAL', vsize=70, vcol=goldL, col=gold),
                                             E('icard', (1000, 340, 1770, 715), 'and a personal conference', icon='phone', l1='PERSONAL CONFERENCE', l2='YOUR VOICE IS HEARD', col=green, c2=green, size=46)],
          'THE AGENCY MUST OFFER BOTH', gold, tag=G5, src='SSA POMS'),
    slide('AT THE FILE REVIEW', 4143, [E('folder', (250, 260, 850, 690), 'at the file review', l1='YOUR CLAIMS FILE', l2='ALL THE EVIDENCE'),
                                      E('icard', (980, 280, 1770, 640), 'read the evidence', icon='check', l1='YOU CAN READ', l2='THE EVIDENCE AGAINST YOU', col=green, c2=green)],
          'READ THE EVIDENCE', gold, tag=G5, src='SSA POMS'),
    slide('AT THE CONFERENCE', 4144, [E('icard', R3s[0], 'by phone', icon='phone', l1='BY PHONE', l2='', col=gold),
                                     E('icard', R3s[1], 'by video', icon='chart', l1='BY VIDEO', l2='', col=blue),
                                     E('icard', R3s[2], 'or in the office', icon='bank', l1='IN THE OFFICE', l2='', col=green),
                                     CH((200, 620, 960, 710), 'you can testify', 'TESTIFY', True, 42), CH((990, 620, 1720, 710), 'bring documents and witnesses', 'BRING DOCUMENTS + WITNESSES', True, 38)],
          'YOU CAN BRING A REPRESENTATIVE', gold, tag=G5, src='SSA POMS'),
    slide('STILL APPEALABLE', 4145, [E('card', (400, 280, 1520, 620), 'can still be appealed', head='A WAIVER DECISION CAN BE', val='APPEALED', sub='A NEW LOOK AT THE FACTS', vsize=140, vcol=goldL, col=gold)],
          'A NEW LOOK AT THE FACTS', gold, tag=G5, src='SSA POMS'),
]
# ---- 14: SE NON FAI NIENTE ----
S[14] = [
    slide('IF YOU DO NOTHING', 4146, [CH((200, 245, 1720, 335), 'you do nothing', 'YOU DO NOTHING', False, 60),
                                  E('paycut', (170, 370, 1750, 660), 'begin on their own', head='THE DEDUCTIONS BEGIN ON THEIR OWN', total='UP TO 50%', kept='THE REST', held='UP TO HALF', kept_l='YOU RECEIVE', held_l='WITHHELD EVERY MONTH', frac=0.5)],
          'SILENCE IS THE WORST MOVE', red, (255, 255, 255), tag=T14, src='SSA EM-25029'),
    slide('NO LONGER RECEIVING BENEFITS', 4147, [E('icard', R2[0], 'federal tax refund', icon='bank', l1='TAX REFUND KEPT', l2='FEDERAL REFUND', col=red, c2=red),
                                                E('icard', R2[1], 'credit bureaus', icon='doc', l1='CREDIT BUREAUS', l2='A DENIED LOAN', col=red, c2=red)],
          'OTHER COLLECTION TOOLS', red, (255, 255, 255), tag=T14, src='SSA POMS'),
    slide('THE ONE EXCEPTION', 4148, [E('card', (170, 270, 880, 600), 'fraud or similar fault', head='FRAUD OR SIMILAR FAULT', val='NO WAIVER', sub='NO LOWER RATE', vsize=90, vcol=red, col=red),
                                     E('card', (1000, 270, 1770, 600), 'for everyone else', head='EVERYONE ELSE', val='ALL MOVES', sub='STAY OPEN', vsize=90, vcol=green, col=green)],
          'EVEN THE SMALLEST MOVE BEATS SILENCE', gold, tag=T14, src='SSA POMS'),
]
# ---- 15: LA SVOLTA DI APRILE ----
S[15] = [
    slide('THE APRIL TWIST', 4149, [E('bigvs', (170, 260, 1750, 700), 'letters dated before', cols=[('BEFORE APR 25, 2025', '10%', 'THE OLD RATE STAYS', gold), ('ON OR AFTER', '50%', 'THE DEFAULT RATE', red)], mid='vs')],
          'OLD LETTERS KEEP 10%', gold, tag=T15, src='SSA EM-25029'),
    slide('A NEW OVERPAYMENT', 4150, [E('card', (170, 280, 760, 620), 'unless you get a new', head='OLD BALANCE', val='10%', sub='BEFORE THE NEW ONE', vsize=140, vcol=goldL, col=gold),
                                     E('arrow', (790, 390, 910, 490), 'every balance you owe'),
                                     E('card', (940, 280, 1770, 620), 'moves to fifty percent', head='ONCE NEW WITHHOLDING BEGINS', val='50%', sub='ON EVERY BALANCE', vsize=140, vcol=red, col=red)],
          'ONE NEW DEBT RESETS ALL', red, (255, 255, 255), tag=T15, src='SSA EM-25029'),
    slide('SSI IS DIFFERENT', 4151, [E('card', (170, 280, 860, 620), 'for s s i', head='SSI  (LOW INCOME)', val='10%', sub='THE RATE STAYS AT TEN PERCENT', vsize=150, vcol=goldL, col=gold),
                                      E('card', (980, 280, 1770, 620), 'title two benefits', head='THIS VIDEO', val='TITLE II', sub='RETIREMENT, SURVIVORS, DISABILITY', vsize=96, vcol=goldL, col=blue)],
          'TWO DIFFERENT PROGRAMS', gold, tag=T15, src='SSA EM-25029'),
]
# ---- 16: PREVENZIONE + PIANO ----
S[16] = [
    slide('AVOID THE LETTER', 4152, [E('line', (200, 240, 1720, 315), 'how do you avoid', t='HOW DO YOU AVOID THE LETTER?', size=62, col=goldL),
                                    CH((200, 335, 1720, 425), 'report changes on time', 'REPORT CHANGES ON TIME', True, 56),
                                    E('folder', (230, 450, 800, 725), 'keep proof', l1='KEEP PROOF', l2='DATE, NAME, COPY'),
                                    CH((900, 490, 1720, 580), 'the date', 'THE DATE', True, 46), CH((900, 610, 1720, 700), 'the name of the person', 'THE NAME OF THE PERSON', True, 46)],
          'REPORT, THEN KEEP THE PROOF', gold, tag=T16, src='SSA POMS'),
    slide('A REPORT COUNTS', 4153, [E('icard', R2[0], 'a report you made', icon='mail', l1='YOU REPORTED', l2='OR TRIED TO REPORT', col=gold),
                                   E('icard', R2[1], 'in your favor', icon='check', l1='COUNTS IN YOUR FAVOR', l2='ON THE FAULT QUESTION', col=green, c2=green, size=46)],
          'IT HELPS ON FAULT', green, navy, tag=T16, src='SSA POMS'),
    slide('CAROL\'S PLAN', 4154, [E('step', (170, 250, 1750, 350), 'carol\'s plan', n=1, text='ANSWER WITHIN 30 DAYS', val='DAY 30', col=gold),
                                 E('step', (170, 375, 1750, 475), 'ask for a waiver', n=2, text='ASK FOR A WAIVER', val='ANY TIME', col=gold),
                                 E('step', (170, 500, 1750, 600), 'request a smaller payment', n=3, text='REQUEST A SMALLER PAYMENT', val='WHILE SHE WAITS', col=gold),
                                 E('step', (170, 625, 1750, 725), 'every paper in one folder', n=4, text='KEEP EVERY PAPER IN ONE FOLDER', val='PROOF', col=gold)],
          'FOUR STEPS FOR CAROL', gold, tag=T16, src='SSA POMS'),
]
# ---- 17: RIEPILOGO + CTA + DISCLAIMER ----
def final16(t, seed=216):
    Dd = CUR['D']
    fr = v16eng.base16(t); fr = amb(fr, t, seed, 5, 40); fr = title_layer(fr, 'IMPORTANT', t, size=64)
    lines = [('General information,', white, 240), ('not advice.', white, 296), ('Rules and amounts change.', goldL, 372),
             ('Confirm with the Social Security', goldL, 428), ('Administration before you act.', white, 504), ('Not affiliated with the', white, 560), ('Social Security Administration.', white, 616)]
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
S[17] = [
    slide('THE FOUR MOVES', 4155, [E('rule', (170, 245, 1750, 345), 'one check the debt', n=1, text='CHECK THE DEBT', val='60 DAYS', col=gold),
                                  E('rule', (170, 370, 1750, 470), 'two the waiver', n=2, text='THE WAIVER', val='ANY TIME', col=gold),
                                  E('rule', (170, 495, 1750, 595), 'three a smaller monthly', n=3, text='A SMALLER MONTHLY RATE', val='ASK FOR LESS', col=gold),
                                  E('rule', (170, 620, 1750, 720), 'four the personal conference', n=4, text='THE PERSONAL CONFERENCE', val='IF DENIED', col=gold)],
          'ONE LETTER, FOUR MOVES', gold, tag=G6, src='SSA POMS'),
    slide('SEND IT TO SOMEONE', 4156, [E('icard', (500, 260, 1420, 690), 'send it to someone', icon='mail', l1='SOMEONE WHO GETS', l2='SOCIAL SECURITY MAIL', col=gold)], 'SHARE IT WITH ONE PERSON'),
    slide('TELL ME IN THE COMMENTS', 4157, [E('line', (200, 310, 1720, 410), 'did your letter match', t='DID YOUR LETTER', size=88, col=white), E('line', (200, 450, 1720, 550), 'what we described', t='MATCH THIS ONE?', size=88, col=goldL)],
          'ANSWER IN THE COMMENTS'),
    frozen(final16),
]

SLIDES = S
SPEC = {b: V.plan(b, len(SLIDES[b])) for b in SLIDES}
CUTS = {1: ['if you do not answer', 'but inside the official'], 2: ['now meet carol', 'then comes the envelope'], 3: ['the total', 'it must also tell', 'read every line'], 4: ['for notices sent', 'for carol', 'hold on to'],
        5: ['the notice itself sets', 'so here are the four'], 6: ['if you disagree', 'you can start by', 'the manual tells staff'], 7: ['but watch what happens', 'a hearing request does not'],
        8: ['the manual says you may', 'if the waiver is approved', 'you ask on form'], 9: ['the agency can find', 'the manual also presumes'], 10: ['door one is small', 'door two is hardship', 'door three is about'],
        11: ['back to carol', 'her nine thousand'], 12: ['staff first try', 'carol asks for three', 'longer than that'], 13: ['at the file review', 'at the conference', 'and a waiver decision'],
        14: ['if you are no longer', 'one exception covers'], 15: ['if you do every balance', 'one more split'], 16: ['a report you made', 'carol\'s plan'], 17: ['if this helped', 'and tell me', 'this is general']}
def _clause_starts(b):
    ws = V.words(b); s0 = V.start(b)
    return [ws[i][1] - s0 for i in range(1, len(ws)) if ws[i - 1][0][-1:] in ',.;:?!']
AUTO_OFF = set()
for _b, _ph in CUTS.items():
    _tot = sum(SPEC[_b]); n = len(SLIDES[_b]); man = [round((V.at(_b, p) - 0.2) * 30) for p in _ph]
    auto = []
    for i in range(1, n):
        els = getattr(SLIDES[_b][i], 'els', None) or []; cue = els[0]['cue'] if els else None
        if cue is None or _b in AUTO_OFF: auto.append(man[i - 1]); continue
        t = V.at(_b, cue); cand = [x for x in _clause_starts(_b) if t - 1.4 <= x <= t + 0.1]
        c = max(cand) if cand else t - 0.1
        auto.append(round((c - 0.15) * 30))
    _c = [0] + auto + [_tot]
    if min(_c[k + 1] - _c[k] for k in range(len(_c) - 1)) < 72: _c = [0] + man + [_tot]      # slide troppo corte: tagli a mano
    SPEC[_b] = [_c[k + 1] - _c[k] for k in range(len(_c) - 1)]
if os.environ.get('PV'):   # solo anteprima layout dei blocchi senza voce: durate finte uguali (750 fotogrammi = 25 s)
    for _b in SLIDES:
        if not os.path.exists(os.path.join(VID, 'voce', f'b{_b}.wav')): SPEC[_b] = [750 // len(SLIDES[_b])] * len(SLIDES[_b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        for b in SLIDES: print(b, SPEC[b], sum(SPEC[b]), 'OK' if len(SPEC[b]) == len(SLIDES[b]) else 'MISMATCH')
    else: run(SPEC, SLIDES, 'v16', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
