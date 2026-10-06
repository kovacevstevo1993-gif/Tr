import subprocess,sys,re
from concurrent.futures import ThreadPoolExecutor
src=open('render.py').read();FR=eval(re.search(r'FR=(\{.*?\})',src).group(1))
def run(b):
    r=subprocess.run(['python3','/home/user/Tr/conti_in_pensione/qa/qa_slide.py','blocco%d.html'%b,'0',str(FR[b])],capture_output=True,text=True);return b,r.stdout.strip(),r.stderr.strip()[-200:]
bl=[int(x) for x in sys.argv[1:]] or sorted(FR)
with ThreadPoolExecutor(4) as ex:
    for b,o,e in ex.map(run,bl):
        print('== blocco',b,o,e)
