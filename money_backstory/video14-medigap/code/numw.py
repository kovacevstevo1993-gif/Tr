import re
ONES="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS="_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def num2words(n):
    if isinstance(n, float):
        i = int(n); fr = str(n).split('.')[1]
        return num2words(i) + ' point ' + ' '.join(ONES[int(c)] for c in fr)
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10] + ('' if n % 10 == 0 else ' ' + ONES[n % 10])
    if n < 1000: return ONES[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' ' + num2words(n % 100))
    if n < 1000000: return num2words(n // 1000) + ' thousand' + ('' if n % 1000 == 0 else ' ' + num2words(n % 1000))
    return str(n)
def norm_words(t):
    t = t.replace('½', ' and a half').replace('%', ' percent'); t = re.sub(r'\$(\d[\d,]*(?:\.\d+)?)', r'\1 dollars', t)
    t = re.sub(r'(\d),(\d)', r'\1\2', t)
    def nm(m):
        x = m.group(0)
        try: return ' ' + num2words(float(x) if '.' in x else int(x)).replace(' and ', ' ').replace(',', '').replace('-', ' ').replace(' point ', ' point ') + ' '
        except: return x
    t = re.sub(r'\d+(?:\.\d+)?', nm, t)
    t = re.sub(r'\bI\.? ?R\.? ?S\.?\b', 'i r s', t); t = re.sub(r'\bIRAs?\b', 'i r a', t, flags=re.I); t = re.sub(r'\bIRS\b', 'i r s', t)
    t = t.replace('-', ' ')
    w = re.sub(r"[^a-z' ]", ' ', t.lower()).split()
    return w
