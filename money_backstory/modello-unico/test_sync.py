import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modello_unico import *
from sync_voce import Voice
# esempio: blocco 1 con voce di prova; ogni elemento compare quando la voce dice la sua parola
def s1(t):
    fr = stage(t, 'FIVE HUNDRED THOUSAND SAVED', 3)
    t1, t2, t3 = cue('five hundred thousand dollars'), cue('ahead of most Americans'), cue('is that enough')
    for tt, lab, x in [(t1, '$500,000', 480), (t2, 'AHEAD OF MOST', 960)]:
        if t > tt:
            C = new(); card_(C, x - 220, 250, x + 220, 480, gold, None, lab, None, 70); fr = P2(fr, C, (x - 240, 230, x + 240, 500), t, tt)
    return frame(pill_last(fr, t, 'IS IT ENOUGH?', 800, red, (255, 255, 255), 54, t0=t3) if t > t3 else fr)
if __name__ == '__main__':
    V = Voice(sys.argv[3]); print("SPEC proposto:", V.plan(1, 1))
    run({1: [341]}, {1: [s1]}, 'sync', os.environ.get('OUT', '/tmp/o/'), argv=sys.argv[:3], voice=sys.argv[3])
