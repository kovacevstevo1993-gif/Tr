import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8b12_15 import *
from v7b2_5 import ic_med
from v7b46_53 import dashed, warn, thumb
from v6b2 import logo
import textwrap

def wrap2(text, w, size):
    if fit(text, w, size).size >= size - 4 or ' ' not in text: return [text]
    words = text.split(); best = None
    for k in range(1, len(words)):
        a, b = ' '.join(words[:k]), ' '.join(words[k:]); sc = max(len(a), len(b))
        if best is None or sc < best[0]: best = (sc, a, b)
    return [best[1], best[2]]

def icon(C, kind, arg, cx, cy, col, u, s=1.0):
    if kind == 'house': house(C, cx, cy - 45, 1.0 * s, col)
    elif kind == 'bldg': building(C, cx, cy - 20, 220 * s, 160 * s, col)
    elif kind == 'phone': phone(C, cx, cy - 35, 0.72 * s, 255, u * 3, True)
    elif kind == 'coin': coin_stack(C, cx, cy + 60, 5, 60)
    elif kind == 'wallet': wallet(C, cx, cy, 1.4 * s)
    elif kind == 'form': tax_form(C, cx - 70, cy - 125, 140, 180, 255, 'FORM')
    elif kind == 'check': check(C, cx, cy, 80 * s, green)
    elif kind == 'cross': cross(C, cx, cy, 80 * s, red)
    elif kind == 'lock': padlock(C, cx, cy, 1.5 * s, col)
    elif kind == 'clock': clock(C, cx, cy, 80 * s, u * 6, goldL)
    elif kind == 'bill': bill(C, cx, cy, int(280 * s), int(140 * s), 0, 255)
    elif kind == 'med': ic_med(C, cx, cy)
    elif kind == 'warn': warn(C, cx, cy, 1.6 * s)
    elif kind == 'person': avatar(C, cx, cy - 5, col, 1.55 * s); txt(C, arg, BOLD(50), cy - 150, goldL, 255, x=cx)
    elif kind == 'ring':
        ring_(C, cx, cy, 105 * s, ease(u), col, 26); txt(C, arg[0], BOLD(36), cy - 52, white, 255, x=cx); txt(C, arg[1], fit(arg[1], 150, 62), cy - 14, goldL, 255, x=cx)
    elif kind == 'cal': cal_card(C, cx - 190, cy - 115, cx + 190, cy + 105, arg[0], arg[1], 84 if len(arg[1]) <= 6 else (44 if len(arg[1]) <= 12 else 34), col)
    elif kind == 'logo': logo(C, cx, cy, 110)
    elif kind == 'thumb': thumb(C, cx, cy, 1.5 * s)

def numdraw(C, x0, x1, arg, col, u):
    head, val, fmt, sub = arg[:4]
    txt(C, head, fit(head, x1 - x0 - 30, 36), 270, col, 255, x=(x0 + x1) / 2)
    v = val * ease(u); txt(C, fmt.format(v), fit('$000,000', x1 - x0 - 30, 110), 350, goldL, 255, x=(x0 + x1) / 2)
    if sub: txt(C, sub, fit(sub, x1 - x0 - 30, 34), 600, grey, 255, x=(x0 + x1) / 2)

PAL = {'g': gold, 'b': blue, 'r': red, 'n': green, 'p': pink}
def build(title, cards, chips, pill, pcol=gold, seed=140, tsize=56):
    def fn(t):
        fr = stage_live(t, title, seed, tsize)
        n = len(cards); gap = 60; w = (1660 - gap * (n - 1)) / n if n > 1 else 860; x0s = [130 + k * (w + gap) for k in range(n)] if n > 1 else [530]
        ts = []
        for k, (kind, arg, label, cue, col) in enumerate(cards):
            t0 = min(tm(cue), LASTP() - 0.9) if cue else 0.15 + 0.15 * k
            if k == 0: t0 = min(t0, 0.3)
            ts.append(t0)
            if t > t0:
                C = new(); x0, x1 = x0s[k], x0s[k] + w; cx = (x0 + x1) / 2; card_(C, x0, 250, x1, 670, col, None, None, None)
                u = (t - t0) / 1.4
                if kind == 'num': numdraw(C, x0, x1, arg, col, (t - t0) / max(0.5, min(max(0.9, min(nxt(k, cards, chips)) - t0), 3.0, LASTA() - t0 - 0.15)))
                else:
                    icon(C, kind, arg, cx, 420, col, u)
                    if label:
                        L = wrap2(label, w - 40, 46); sz = min(46, 42 if len(L) > 1 else 46)
                        for j, ln in enumerate(L): txt(C, ln, fit(ln, w - 40, sz), 548 + j * 54 - (27 if len(L) > 1 else 0) + (10 if len(L) == 1 else 0), white, 255, x=cx)
                fr = E(fr, C, (x0 - 20, 230, x1 + 20, 690), t, t0)
        for (text, cue, col, idx) in chips:
            tc = min(tm(cue), LASTP() - 0.7); sz = 40 if len(text) < 24 else 36
            cw = ImageDraw.Draw(Image.new('RGBA', (10, 10))).textlength(text, font=BOLD(sz)) + 90
            cxx = max(130 + cw / 2, min(1790 - cw / 2, x0s[idx] + w / 2))
            fr = chipE(fr, text, cxx, 705, t, tc, col=col, size=sz)
        return frame(pill_last(fr, t, pill, PILL_Y, pcol, navy if pcol in (gold, green, goldL) else (255, 255, 255), 52 if len(pill) < 36 else 46))
    return fn
def nxt(k, cards, chips):
    out = []
    for kk in range(k + 1, len(cards)):
        c = cards[kk][3]
        if c: out.append(tm(c))
    return out or [tm(cards[k][3] or 'the') + 3.0] if False else (out or [10 ** 6])

def N(head, val, fmt, sub, cue, col): return ('num', (head, val, fmt, sub), '', cue, col)
D1 = '${:,.0f}'; D2 = '${:,.2f}'; PL = '+${:,.0f}'; PC = '{:.0f}%'
B, G, R, Gr, P_ = blue, gold, red, green, pink
BL = {}   # blocco -> (frasi di taglio, [slide])
BL[16] = (['That is', 'Far below'], [
 build('ONE SINGLE PERSON', [('person', 'S', 'SINGLE PERSON', 'single', B), N('AVERAGE CHECK', 2071, D1, 'A MONTH', 'average', G)], [('ONLY INCOME', 'only', goldL, 0)], 'THE AVERAGE CHECK', gold, 161),
 build('IN ONE YEAR', [N('PER YEAR', 24800, D1, 'ABOUT', 'twenty four', B), N('HALF OF IT', 12400, D1, 'ABOUT', 'Half', G)], [('TWELVE MONTHS', 'year', goldL, 0)], 'ABOUT $12,400 COUNTS', gold, 162),
 build('FAR BELOW THE LINE', [N('THE LINE', 25000, D1, 'SINGLE PERSON', 'twenty five', R), N('THEIR HALF', 12400, D1, 'COUNTED', 'Far', G), ('check', None, 'FEDERAL TAX: ZERO', 'zero', Gr)], [('FAR BELOW', 'below', goldL, 1)], 'FEDERAL TAX ON SOCIAL SECURITY: ZERO', green, 163)])
BL[17] = (['That money'], [
 build('TAX TAKEN OUT OF EVERY CHECK', [('form', None, 'A FORM FILLED OUT YEARS AGO', 'because', B), ('clock', None, 'OUT OF HABIT', 'habit', G), ('cross', None, 'TAX TAKEN FROM EVERY CHECK', 'taken', R)], [('STILL HAVE TAX TAKEN', 'still', goldL, 2)], 'STILL TAKEN OUT OF HABIT', gold, 171),
 build('AN INTEREST FREE LOAN', [('check', None, 'A REFUND LATER', 'refund', Gr), ('bldg', None, 'A LOAN TO THE GOVERNMENT', 'loan', R), N('INTEREST', 0, D1, 'EVERY MONTH', 'zero', G)], [('NOT LOST', 'lost', goldL, 0)], 'A LOAN WITH ZERO INTEREST', red, 172)])
BL[18] = (['So before'], [
 build('ONLY EIGHT STATES TAX IT', [N('IN 2026', 8, '{:.0f}', 'STATES TAX SOCIAL SECURITY', 'eight', G), ('bldg', None, 'ALL THE OTHER STATES: NO TAX', 'all', Gr)], [('IN TWENTY TWENTY SIX', 'six', goldL, 0)], 'ONLY EIGHT STATES TAX IT', gold, 181),
 build('ADD UP YOUR PROVISIONAL INCOME', [('warn', None, 'BEFORE YOU ASSUME IT IS TAXED', 'assume', R), ('form', None, 'ADD UP YOUR PROVISIONAL INCOME', 'provisional', B), ('check', None, 'OFTEN ZERO OR MUCH SMALLER', 'smaller', Gr)], [('FOR MANY RETIREES', 'many', goldL, 2)], 'THIS BILL MAY BE ZERO', green, 182)])
BL[19] = (['In twenty'], [
 build('BILL NUMBER THREE: INCOME TAX', [('ring', ('BILL', '#3'), 'YOUR INCOME TAX ITSELF', 'part', G), ('form', None, 'A BIGGER STANDARD DEDUCTION', 'bigger', Gr)], [('AT SIXTY FIVE', 'five', goldL, 1)], 'A BIGGER DEDUCTION AT 65', gold, 191),
 build('THE 2026 STANDARD DEDUCTION', [N('SINGLE PERSON', 16100, D1, '2026', 'sixteen', B), N('MARRIED COUPLE', 32200, D1, '2026', 'thirty two', Gr)], [('THE NORMAL AMOUNT', 'normal', goldL, 0)], '$16,100 SINGLE, $32,200 MARRIED', gold, 192)])
BL[20] = (['A married', 'So Frank'], [
 build('SINGLE PERSON: PLUS $2,050', [('ring', ('AGE', '65'), 'AT SIXTY FIVE', 'single', G), N('A SINGLE PERSON ADDS', 2050, PL, '2026', 'two thousand', B)], [('EXTRA DEDUCTION', 'adds', goldL, 1)], 'PLUS $2,050 AT AGE 65', gold, 201),
 build('MARRIED COUPLE: PLUS $1,650 EACH', [N('PER SPOUSE', 1650, PL, '65 OR OLDER', 'one thousand', Gr), ('person', 'F', 'FOR EACH SPOUSE', 'each', B)], [('A MARRIED COUPLE', 'married', goldL, 0)], 'PLUS $1,650 FOR EACH SPOUSE', green, 202),
 build('FRANK AND MARY: PLUS $3,300', [('person', 'F', 'FRANK', 'Frank', B), ('person', 'M', 'MARY', 'Mary', P_), N('TOGETHER', 3300, PL, 'JUST FOR THEIR AGE', 'three thousand', G)], [('1,650 PLUS 1,650', 'add', goldL, 2)], 'THEIR AGE ADDS $3,300', gold, 203)])
BL[21] = (['If you use', 'If someone'], [
 build('HERE IS THE TRAP', [('warn', None, 'THE EXTRA AMOUNT', 'extra', R), ('cal', ('DATE OF BIRTH', 'ON THE RETURN'), 'MUST BE RIGHT', 'depends', B)], [('THE TRAP', 'trap', red, 0)], 'YOUR BIRTH DATE TRIGGERS IT', red, 211),
 build('CHECK YOUR TAX SOFTWARE', [('form', None, 'TAX SOFTWARE', 'software', B), ('check', None, 'BOTH BIRTH DATES ENTERED', 'both', Gr)], [('CHECK IT', 'check', goldL, 1)], 'CHECK BOTH BIRTH DATES', green, 212),
 build('IF SOMEONE PREPARES YOUR RETURN', [('person', 'P', 'YOUR PREPARER', 'prepares', G), ('check', None, 'AGE 65 AMOUNT ON THE FORM', 'confirm', Gr), ('clock', None, 'TWO MINUTES', 'minutes', B)], [('ASK THEM TO CONFIRM', 'ask', goldL, 1)], 'IT TAKES TWO MINUTES', gold, 213)])
BL[22] = (['Starting with'], [
 build('BILL NUMBER FOUR: BRAND NEW', [('ring', ('BILL', '#4'), 'BRAND NEW', 'brand', G), ('cross', None, 'MANY WILL MISS IT', 'miss', R)], [('A NEW DEDUCTION', 'new', goldL, 0)], 'A BRAND NEW DEDUCTION', gold, 221),
 build('THE NEW SENIOR DEDUCTION', [('cal', ('FROM TAX YEAR', '2025'), '', 'Starting', B), ('cal', ('THROUGH', '2028'), '', 'through', B), N('UP TO', 6000, D1, 'SENIOR DEDUCTION', 'six thousand', Gr)], [('EVERY TAXPAYER 65 PLUS', 'taxpayer', goldL, 2)], 'UP TO $6,000 MORE', green, 222)])
BL[23] = (['If you are'], [
 build('ON TOP OF EVERYTHING', [('form', None, 'STANDARD DEDUCTION', 'standard', B), ('ring', ('AGE', '65'), 'AGE 65 AMOUNT', 'age', G), ('check', None, 'NEW SENIOR DEDUCTION', 'comes', Gr)], [('PLUS, ON TOP', 'top', goldL, 2)], 'THE NEW ONE COMES ON TOP', green, 231),
 build('MARRIED: UP TO $12,000', [N('BOTH 65 OR OLDER', 12000, D1, 'UP TO', 'twelve thousand', Gr), ('check', None, 'EVEN IF YOU ITEMIZE', 'itemize', B)], [('A MARRIED COUPLE', 'married', goldL, 0)], 'UP TO $12,000 FOR A COUPLE', green, 232)])
BL[24] = (['It disappears'], [
 build('THE DEDUCTION STARTS TO SHRINK', [('warn', None, 'THERE IS AN INCOME LIMIT', 'limit', R), N('SINGLE PERSON', 75000, D1, 'SHRINKS ABOVE', 'seventy five', B), N('MARRIED COUPLE', 150000, D1, 'SHRINKS ABOVE', 'one hundred fifty', Gr)], [('MODIFIED ADJUSTED GROSS INCOME', 'modified', goldL, 1)], 'THE DEDUCTION STARTS TO SHRINK', red, 241),
 build('GONE COMPLETELY', [N('SINGLE PERSON', 175000, D1, 'DISAPPEARS AT', 'one hundred seventy', B), N('MARRIED COUPLE', 250000, D1, 'DISAPPEARS AT', 'two hundred fifty', Gr)], [('IT DISAPPEARS', 'disappears', red, 0)], 'GONE AT $175,000 AND $250,000', red, 242)])
BL[25] = (['Now'], [
 build('TO CLAIM IT', [('check', None, 'A VALID SOCIAL SECURITY NUMBER', 'valid', B), ('check', None, 'MARRIED: FILE A JOINT RETURN', 'married', Gr)], [('YOU NEED', 'need', goldL, 0)], 'VALID NUMBER AND JOINT RETURN', gold, 251),
 build('NOW FRANK AND MARY', [('person', 'F', 'FRANK', 'Frank', B), ('person', 'M', 'MARY', 'Mary', P_)], [('BILLS THREE AND FOUR', 'three', goldL, 0), ('THIS GETS INTERESTING', 'interesting', goldL, 1)], 'WHAT DO BILLS THREE AND FOUR DO?', gold, 252)])
BL[26] = (['Their provisional'], [
 build('FRANK AND MARY: THEIR INCOME', [N('FROM THE I R A', 40000, D1, 'EACH YEAR', 'forty thousand', B), N('HALF OF SOCIAL SECURITY', 21600, D1, 'EACH YEAR', 'twenty one', Gr)], [('PLUS', 'plus', goldL, 1)], 'I R A PLUS HALF OF SOCIAL SECURITY', gold, 261),
 build('PROVISIONAL INCOME', [N('PROVISIONAL INCOME', 61600, D1, 'THEIR TOTAL', 'sixty one', G), N('THE LINE', 44000, D1, 'MARRIED COUPLE', 'forty four', R), ('warn', None, 'PART IS TAXABLE', 'taxable', R)], [('ABOVE THE LINE', 'above', goldL, 1)], 'PART OF SOCIAL SECURITY IS TAXED', red, 262)])
BL[27] = (['Their total'], [
 build('THE I R S FORMULA', [('form', None, 'THE I R S FORMULA', 'formula', B), N('TAXABLE SOCIAL SECURITY', 20960, D1, 'ABOUT', 'twenty thousand', G)], [('USING THE FORMULA', 'Using', goldL, 0)], 'AND $20,960 IS TAXABLE', gold, 271),
 build('THEIR TOTAL TAXABLE INCOME', [N('TOTAL INCOME FOR TAXES', 60960, D1, 'THEIR TOTAL', 'sixty thousand', G), ('check', None, 'NOW WATCH EACH DEDUCTION', 'watch', Gr)], [('FOR TAX PURPOSES', 'purposes', goldL, 0)], 'TOTAL TAXABLE INCOME: $60,960', gold, 272)])
BL[28] = ([], [
 build('ONLY THE REGULAR DEDUCTION', [N('STANDARD DEDUCTION', 32200, D1, 'MARRIED COUPLE, 2026', 'thirty two', B), ('form', None, 'FEDERAL INCOME TAX', 'federal', G), N('THE TAX WOULD BE', 2955, D1, 'ABOUT', 'two thousand', R)], [('ONLY THE REGULAR AMOUNT', 'only', goldL, 0), ('FOR 2026', 'six', goldL, 2)], 'THEIR TAX WOULD BE ABOUT $2,955', red, 281)])
BL[29] = (['Add the new'], [
 build('ADD THE AGE 65 AMOUNT', [N('ADD', 3300, PL, 'THE AGE 65 AMOUNT', 'three thousand', B), N('THE TAX DROPS TO', 2559, D1, 'ABOUT', 'two thousand five', Gr)], [('AGE SIXTY FIVE AMOUNT', 'age', goldL, 0)], 'THE TAX DROPS TO ABOUT $2,559', green, 291),
 build('ADD THE SENIOR DEDUCTION', [N('ADD', 12000, PL, 'THE NEW SENIOR DEDUCTION', 'twelve thousand', B), N('THE TAX DROPS TO', 1346, D1, 'ABOUT', 'one thousand three', Gr)], [('FOR THE TWO OF THEM', 'two of them', goldL, 0)], 'THE TAX DROPS TO ABOUT $1,346', green, 292)])
BL[30] = (['And if'], [
 build('ABOUT $1,609 LESS EVERY YEAR', [N('LESS TAX', 1609, D1, 'EVERY YEAR', 'one thousand six', Gr), ('person', 'F', 'THE SAME COUPLE', 'couple', B), ('wallet', None, 'THE SAME INCOME', 'income', G)], [('EVERY YEAR', 'every', goldL, 0)], '$1,609 LESS, SAME INCOME', green, 301),
 build('THE WITHHOLDING TRAP', [('form', None, 'WITHHOLDING SET YEARS AGO', 'withholding', B), ('bldg', None, 'LENDING TO THE GOVERNMENT', 'lending', R)], [('BEFORE THESE DEDUCTIONS', 'before', goldL, 0), ('ALL YEAR LONG', 'long', red, 1)], 'YOU LEND THE MONEY ALL YEAR', red, 302)])
BL[31] = (['In twenty', 'It comes'], [
 build('BILL NUMBER FIVE: MEDICARE PART B', [('ring', ('BILL', '#5'), 'THE ONE TO STAY FOR', 'Bill', G), ('med', None, 'MEDICARE PART B PREMIUM', 'Medicare', R)], [('STAY FOR THIS ONE', 'stay', goldL, 0)], 'BILL FIVE: MEDICARE PART B', red, 311),
 build('THE 2026 PREMIUM', [('cal', ('IN', '2026'), '', 'twenty twenty', B), N('STANDARD PREMIUM', 202.90, D2, 'A MONTH', 'two hundred two', R)], [('PART B PREMIUM', 'premium', goldL, 1)], '$202.90 A MONTH', red, 312),
 build('TAKEN BEFORE YOU SEE IT', [('form', None, 'TAKEN FROM YOUR CHECK', 'comes', B), ('cross', None, 'MANY PEOPLE FORGET', 'forget', R)], [('BEFORE IT REACHES YOU', 'before', goldL, 0)], 'TAKEN OUT BEFORE YOU SEE IT', red, 313)])
BL[32] = (['And there'], [
 build('FRANK AND MARY: PART B', [('person', 'F', 'FRANK', 'Frank', B), ('person', 'M', 'MARY', 'Mary', P_), N('FOR THE TWO OF THEM', 4870, D1, 'A YEAR', 'four thousand', R)], [('PART B', 'year', goldL, 2)], 'ABOUT $4,870 A YEAR', red, 321),
 build('TWO WAYS TO SHRINK IT', [('ring', ('TWO', 'WAYS'), 'THE BILL CAN SHRINK', 'two ways', G), ('check', None, 'MEDICARE SAVINGS PROGRAMS', 'called', Gr)], [('OR DISAPPEAR', 'completely', goldL, 0), ('ALMOST NOBODY EXPLAINS THEM', 'nobody', goldL, 1)], 'WAY ONE: MEDICARE SAVINGS PROGRAMS', green, 322)])
BL[33] = (['The most'], [
 build('YOUR STATE PAYS PART B', [('wallet', None, 'INCOME AND SAVINGS UNDER THE LIMITS', 'limits', B), ('bldg', None, 'YOUR STATE PAYS PART B', 'state', G), ('check', None, 'ALL OF IT', 'All', Gr)], [('NOT PART OF IT', 'Not', red, 1)], 'THE STATE PAYS ALL OF IT', green, 331),
 build('THE MOST GENEROUS LEVEL', [('ring', ('LEVEL', 'Q M B'), 'THE MOST GENEROUS', 'generous', G), ('check', None, 'THE PART B DEDUCTIBLE', 'deductible', Gr), ('check', None, 'MOST OF YOUR COINSURANCE', 'coinsurance', Gr)], [('ALSO COVERS', 'also', goldL, 1)], 'Q M B ALSO COVERS THE EXTRA COSTS', green, 332)])
BL[34] = (['The savings'], [
 build('2026 INCOME LIMIT, LEVEL Q I', [('cal', ('FOR', '2026'), '', 'twenty', G), N('ONE PERSON', 1816, D1, 'A MONTH', 'one thousand eight', B), N('A COUPLE', 2455, D1, 'A MONTH', 'two thousand four', Gr)], [('THE HIGHEST INCOME LIMIT', 'highest', goldL, 0)], 'INCOME LIMIT: $1,816 / $2,455 A MONTH', gold, 341),
 build('THE SAVINGS LIMIT', [N('ONE PERSON', 9950, D1, 'IN SAVINGS', 'nine thousand', B), N('A COUPLE', 14910, D1, 'IN SAVINGS', 'fourteen thousand', Gr)], [('THE SAVINGS LIMIT', 'savings', goldL, 0)], 'SAVINGS LIMIT: $9,950 / $14,910', gold, 342)])
BL[35] = (['So people', 'And getting'], [
 build('WHAT MOST PEOPLE MISS', [('bldg', None, 'SOME STATES: HIGHER LIMITS', 'higher', G), ('cross', None, 'SOME DO NOT COUNT SAVINGS', 'count', B)], [('WHAT MOST PEOPLE MISS', 'miss', goldL, 0)], 'MANY STATES ARE MORE GENEROUS', gold, 351),
 build('THEY OFTEN QUALIFY', [('person', '?', 'I MAKE TOO MUCH', 'think', R), ('check', None, 'OFTEN THEY QUALIFY', 'qualify', Gr)], [('PEOPLE WHO THINK SO', 'people', goldL, 0)], 'THEY OFTEN QUALIFY', green, 352),
 build('ONE PROGRAM, EXTRA HELP', [('check', None, 'MEDICARE SAVINGS PROGRAM', 'getting', B), ('med', None, 'EXTRA HELP', 'Extra', Gr)], [('LOWER DRUG COSTS', 'lowers', goldL, 1)], 'ONE PROGRAM CAN UNLOCK EXTRA HELP', green, 353)])
BL[36] = (['If your', 'In twenty'], [
 build('WAY TWO: THE OPPOSITE', [('ring', ('WAY', '2'), 'THE SECOND WAY', 'second', G), ('cross', None, 'THE OPPOSITE SITUATION', 'opposite', B)], [('A DIFFERENT CASE', 'situation', goldL, 1)], 'WAY TWO: AN EXTRA CHARGE', gold, 361),
 build('IRMAA: AN EXTRA CHARGE', [('cal', ('YOUR INCOME', '2 YEARS AGO'), 'WAS HIGH', 'high', B), ('bill', None, 'AN EXTRA MEDICARE CHARGE', 'extra', R), ('ring', ('CALLED', 'IRMAA'), 'I R M A A', 'called', G)], [('TWO YEARS AGO', 'years', goldL, 0)], 'IRMAA: AN EXTRA MEDICARE CHARGE', red, 362),
 build('THE 2026 STARTING POINT', [('cal', ('INCOME FROM', '2024'), '', 'four', B), N('SINGLE PERSON', 109000, D1, 'ABOVE', 'one hundred nine', G), N('A COUPLE', 218000, D1, 'ABOVE', 'two hundred eighteen', Gr)], [('IT STARTS IN 2026', 'starts', goldL, 0)], 'STARTS ABOVE $109,000 / $218,000', gold, 363)])
BL[37] = (['But if', 'Like stopping'], [
 build('THE FIRST LEVEL', [('bill', None, 'THE FIRST LEVEL ALONE', 'first', R), N('IT COSTS ABOUT', 974, D1, 'A YEAR', 'nine hundred', R)], [('PER PERSON', 'person', goldL, 1)], 'ABOUT $974 A YEAR', red, 371),
 build('A LIFE CHANGING EVENT', [('ring', ('LIFE', 'EVENT'), 'A LIFE CHANGING EVENT', 'life', G), ('cross', None, 'YOUR INCOME DROPPED', 'dropped', B)], [('BECAUSE OF', 'because', goldL, 0)], 'A LIFE CHANGING EVENT', gold, 372),
 build('WHAT COUNTS AS AN EVENT', [('clock', None, 'STOPPING WORK', 'stopping', B), ('form', None, 'LOSING A PENSION', 'pension', G), ('person', 'S', 'DEATH OF A SPOUSE', 'spouse', P_)], [('CUTTING YOUR HOURS', 'hours', goldL, 0), ('ASK SOCIAL SECURITY', 'ask', green, 2)], 'ASK TO USE YOUR LOWER INCOME', gold, 373)])
BL[38] = ([], [
 build('FORM S S A 44', [('form', None, 'FORM S S A 44', 'called', B), ('cross', None, 'THEY WILL NOT SEND IT', 'send', R), ('check', None, 'ONE FORM, CHARGE REMOVED', 'One', Gr)], [('YOU HAVE TO ASK', 'ask', goldL, 1)], 'ONE FORM CAN REMOVE THE CHARGE', green, 381)])
BL[39] = (['For Social', 'For a pension'], [
 build('A BONUS THAT COSTS NOTHING', [('check', None, 'A BONUS THAT COSTS NOTHING', 'bonus', Gr), ('cross', None, 'TAX TAKEN OUT OF YOUR CHECKS', 'taken', R)], [('LOOK AT YOUR WITHHOLDING', 'Look', goldL, 1)], 'LOOK AT THE TAX TAKEN OUT', green, 391),
 build('FORM W-4V: CHOOSE YOUR RATE', [N('CHOOSE', 7, PC, 'OF EACH PAYMENT', 'seven', B), N('OR', 10, PC, 'OF EACH PAYMENT', 'ten', B), N('OR', 12, PC, 'OF EACH PAYMENT', 'twelve', B), N('OR', 22, PC, 'OF EACH PAYMENT', 'twenty two', B)], [('FORM W-4V', 'W-4V', goldL, 0), ('OR NOTHING AT ALL', 'nothing', goldL, 3)], 'SEVEN, TEN, TWELVE, TWENTY TWO PERCENT, OR NONE', gold, 392),
 build('FOR A PENSION', [('form', None, 'FOR A PENSION', 'pension', G), ('form', None, 'FORM W-4P', 'W-4P', B)], [('A DIFFERENT FORM', 'form', goldL, 1)], 'PENSION: FORM W-4P', gold, 393)])
BL[40] = ([], [
 build('LOWER TAX, LOWER WITHHOLDING', [('check', None, 'YOUR TAX IS NOW LOWER', 'lower', Gr), ('form', None, 'YOUR WITHHOLDING SHOULD BE LOWER TOO', 'withholding', B), ('clock', None, 'OTHERWISE YOU WAIT A YEAR', 'wait', R)], [('BECAUSE OF THE DEDUCTIONS', 'deductions', goldL, 0), ('FOR YOUR OWN MONEY', 'own', red, 2)], 'LOWER TAX, LOWER WITHHOLDING', green, 401)])
BL[41] = (['The bridge'], [
 build('EXEMPT IS NOT THE SAME', [('warn', None, 'THE POINT OF THE VIDEO', 'point', G), ('check', None, 'EXEMPT FROM A BILL', 'exempt', Gr), ('cross', None, 'ACTUALLY NOT PAYING IT', 'paying', R)], [('TWO DIFFERENT THINGS', 'different', goldL, 2)], 'EXEMPT IS NOT THE SAME AS NOT PAYING', gold, 411),
 build('THE BRIDGE IS A FORM', [('form', None, 'THE BRIDGE IS A FORM', 'bridge', G), ('bldg', None, 'THE AGENCIES WILL NOT FILL IT OUT', 'agencies', R)], [('ALMOST ALWAYS', 'always', goldL, 0)], 'THE BRIDGE IS A FORM', gold, 412)])
BL[42] = (['Two'], [
 build('WHAT TO DO THIS WEEK', [('ring', ('DO THIS', 'WEEK'), 'WHAT TO DO', 'week', G), ('phone', None, 'CALL YOUR COUNTY ASSESSOR', 'call', B), ('house', None, 'HOMESTEAD, SENIOR, FREEZE', 'homestead', Gr)], [('STEP ONE', 'One', goldL, 1)], 'STEP ONE: CALL THE ASSESSOR', gold, 421),
 build('STEP TWO: YOUR NUMBERS', [('form', None, 'ADD UP YOUR PROVISIONAL INCOME', 'add', B), ('check', None, 'CHECK WHAT IS WITHHELD', 'check', Gr)], [('STEP TWO', 'Two', goldL, 0)], 'STEP TWO: INCOME AND WITHHOLDING', green, 422)])
BL[43] = (['Four', 'It is free'], [
 build('STEP THREE: YOUR TAX RETURN', [('form', None, 'BEFORE YOUR NEXT TAX RETURN', 'before', B), ('ring', ('AGE', '65'), 'THE AGE 65 AMOUNT', 'age', G), ('check', None, 'THE NEW SENIOR DEDUCTION', 'new', Gr)], [('STEP THREE', 'Three', goldL, 0)], 'STEP THREE: CHECK YOUR RETURN', gold, 431),
 build('STEP FOUR: CALL SHIP', [('phone', None, 'CALL YOUR STATE SHIP OFFICE', 'call', B), ('ring', ('S', 'SHIP'), 'STATE HEALTH INSURANCE ASSISTANCE PROGRAM', 'State', G)], [('STEP FOUR', 'Four', goldL, 0)], 'STEP FOUR: CALL SHIP', gold, 432),
 build('FREE HELP FROM SHIP', [('check', None, 'IT IS FREE', 'free', Gr), ('check', None, 'CHECK A MEDICARE SAVINGS PROGRAM', 'qualify', B), ('form', None, 'HELP WITH FORM S S A 44', 'help', G)], [('THEY CAN CHECK', 'check', goldL, 1)], 'FREE HELP WITH BOTH', green, 433)])
BL[44] = (['The Medicare', 'The Social'], [
 build('SOURCES: THE TAX NUMBERS', [('form', None, 'THE TAX NUMBERS', 'tax', B), ('bldg', None, 'INTERNAL REVENUE SERVICE', 'Internal', G)], [('A WORD ABOUT SOURCES', 'sources', goldL, 0)], 'SOURCE: THE I R S', gold, 441),
 build('SOURCES: THE MEDICARE NUMBERS', [('med', None, 'THE MEDICARE NUMBERS', 'Medicare', R), ('bldg', None, 'CMS AND MEDICARE.GOV', 'Centers', G)], [('FROM THE OFFICIAL SITES', 'dot', goldL, 1)], 'SOURCE: CMS AND MEDICARE.GOV', gold, 442),
 build('SOURCES: SOCIAL SECURITY', [('bldg', None, 'SOCIAL SECURITY ADMINISTRATION', 'Administration', B), ('check', None, 'EVERY SOURCE IS IN THE DESCRIPTION', 'Every', Gr)], [('THE SOCIAL SECURITY RULES', 'rules', goldL, 0)], 'EVERY SOURCE IS IN THE DESCRIPTION', green, 443)])
BL[45] = (['It costs'], [
 build('SEND IT TO ONE PERSON', [('person', '1', 'ONE PERSON OVER 65', 'one', G), ('person', 'P', 'A PARENT', 'parent', B), ('person', 'N', 'A NEIGHBOR', 'neighbor', Gr), ('person', 'F', 'A FRIEND', 'friend', P_)], [('IF THIS HELPED', 'helped', goldL, 0)], 'SEND IT TO ONE PERSON OVER 65', gold, 451),
 build('IT COSTS NOTHING', [('check', None, 'IT COSTS NOTHING', 'costs', Gr), ('wallet', None, 'HUNDREDS OR THOUSANDS BACK', 'hundreds', G)], [('IN THEIR POCKET', 'pocket', goldL, 1)], 'IT COSTS NOTHING', green, 452)])
BL[46] = (['Tap like'], [
 build('TELL ME IN THE COMMENTS', [('person', '?', 'TELL ME IN THE COMMENTS', 'comments', B), ('ring', ('5', 'BILLS'), 'WHICH ONE ARE YOU STILL PAYING?', 'which', G)], [('FIVE BILLS', 'five', goldL, 1)], 'WHICH BILLS ARE YOU STILL PAYING?', gold, 461),
 build('LIKE, SUBSCRIBE, THE BELL', [('thumb', None, 'LIKE THE VIDEO', 'like', G), ('logo', None, 'SUBSCRIBE', 'subscribe', B), ('clock', None, 'TURN ON THE BELL', 'bell', R)], [('THE NEXT VIDEO', 'next', goldL, 2)], 'LIKE, SUBSCRIBE, TURN ON THE BELL', gold, 462)])
def s47(t):
    fr = stage_live(t, 'THE NEXT VIDEO IS ON YOUR SCREEN', 471, 54)
    t1, t2, t3 = 0.2, tm('one hundred twenty'), tm('right')
    if t > t1 and t <= t2:
        C = new(); card_(C, 130, 250, 900, 670, blue, None, None, None); txt(C, 'THE AGE YOU CLAIM', fit('THE AGE YOU CLAIM', 700, 54), 380, goldL, 255, x=515); txt(C, 'SOCIAL SECURITY', fit('SOCIAL SECURITY', 700, 60), 470, white, 255, x=515); fr = E(fr, C, (110, 230, 920, 690), t, t1)
    if t > t2:
        C = new(); card_(C, 130, 250, 900, 670, blue, None, None, None); numdraw(C, 130, 900, ('LIFETIME INCOME', 124000, D1, 'MORE THAN'), blue, (t - t2) / max(0.5, min(1.2, LASTA() - t2 - 0.15))); fr = E(fr, C, (110, 230, 920, 690), t, t2 - 0.4)
        fr = E(fr, C, (110, 230, 920, 690), t, t2)
    if t > t3:
        C = new(); dashed(C, 1020, 250, 1750, 670); txt(C, 'WATCH NEXT', BOLD(64), 410, goldL, 255, x=1385); txt(C, 'RIGHT HERE', BOLD(46), 500, white, 255, x=1385); fr = E(fr, C, (1000, 230, 1810, 690), t, t3)
    fr = chipE(fr, 'CLAIM AT THE RIGHT AGE', 515, 705, t, tm('claim'), col=goldL, size=40); fr = chipE(fr, 'CHANGE YOUR INCOME', 515, 785, t, tm('change'), col=goldL, size=40) if False else fr
    return frame(pill_last(fr, t, 'THE VIDEO IS RIGHT ON YOUR SCREEN', PILL_Y, gold, navy, 50))
BL[47] = ([], [s47])
BL[48] = ([], [final_slide])

SLIDES = {b: [frozen(f) for f in v[1]] for b, v in BL.items()}
RAW = {b: list(v[1]) for b, v in BL.items()}
SPEC = {}
for b, (cuts_, sl) in BL.items(): SPEC[b] = spec(b, cuts_)
DUR = {16:512,17:483,18:472,19:507,20:523,21:530,22:476,23:447,24:555,25:417,26:501,27:393,28:334,29:447,30:423,31:548,32:472,33:463,34:603,35:519,36:548,37:523,38:322,39:543,40:317,41:453,42:411,43:649,44:530,45:376,46:340,47:352,48:389}
for b in SPEC:
    assert len(SPEC[b]) == len(BL[b][1]), (b, SPEC[b]); assert sum(SPEC[b]) == DUR[b], (b, SPEC[b], DUR[b])
if __name__ == '__main__':
    if sys.argv[1] == 'spec': print({b: v for b, v in SPEC.items()})
    else: run(SPEC, SLIDES, 'v8', os.environ.get('OUT', os.path.join(VID, 'slide') + '/'))
