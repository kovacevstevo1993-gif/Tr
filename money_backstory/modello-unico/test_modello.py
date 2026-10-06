import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modello_unico import *
SPEC = {1: [150, 150], 2: [357]}
def sa(t):
    fr = stage(t, 'TEST DEL MODELLO', 1); T = sp(3)
    fr = eq(fr, t, 230, [('c', 'SAVINGS', '$1,625', 'A MONTH', gold), ('o', '+'), ('c', 'SOCIAL SECURITY', '$1,868', 'A MONTH', blue), ('o', '='), ('c', 'TOTAL', '$3,493', 'A MONTH', green)], [T[0], T[1], T[2]], 270, 420, 150)
    return frame(pill_last(fr, t, 'ONE MODEL FOR EVERY VIDEO', 800, green, (10, 24, 40), 54))
def sb(t):
    fr = stage(t, 'SECOND SLIDE', 2); T = sp(2)
    fr = bars3(fr, t, 700, [('A', '$10', 0.5, gold, white), ('B', '$20', 0.9, green, white)], T, 520, 240, 120)
    return frame(pill_last(fr, t, 'LAST ELEMENT AT 80 PERCENT', 800, red, (255, 255, 255), 54))
SLIDES = {1: [sa, sb], 2: [final_slide]}
if __name__ == '__main__':
    run(SPEC, SLIDES, 'test', os.environ.get('OUT', '/tmp/claude-0/-home-user-Tr/55d6a1e9-5107-5859-80b6-50141ae1d070/scratchpad/mu/'))
