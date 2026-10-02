# LEGGIMI — COME SI FANNO I VIDEO DI THE MONEY BACKSTORY
**Per il Claude della chat nuova.** Prima di fare QUALSIASI slide, miniatura o copione leggi tutto questo file. Lo stile dei video è già deciso e approvato dall'utente: non si reinventa niente. Il video 1 e il video 2 sono stati fatti così, e i video 3, 4, 5… devono avere **esattamente lo stesso aspetto e lo stesso ritmo**.

## 0. Cosa NON deve succedere (errori già fatti da un'altra chat)
- Colori diversi da quelli qui sotto, grafici tipo "stelle", sfondi diversi, cornici diverse.
- Slide lunghe 20-30 secondi con lo stesso grafico fermo. Ritmo lento, noioso.
- Un video con un aspetto diverso dall'altro. Tutti i video del canale devono sembrare della stessa serie.
- Chiedere all'utente di ripetere cose già scritte qui.

## 1. Il canale
Canale YouTube faceless **The Money Backstory** (@TheMoneyBackstoryUSA): pensione USA per over 50 (Social Security, Medicare, tasse, 401k, assistenza, ecc.). Pubblico americano, voce inglese. Mai cripto/trading/finanza per giovani.

## 2. Il ritmo (la cosa più importante)
- **Ogni frase (o massimo due frasi) del copione ha la sua slide.** L'immagine cambia di continuo.
- Una slide dura in media **4-12 secondi**. Mai una slide ferma per 20-30 secondi. Se un gruppo di frasi dura tanto, dentro la slide gli elementi entrano uno alla volta ESATTAMENTE quando la voce li dice.
- **Ogni slide ha un grafico diverso**: colonne che salgono, linee, anelli, torte, linee del tempo, schede che entrano, calcolatrici, icone (clessidra, scudo, lucchetto, busta, portafoglio), contatori che salgono, mattoncini, scale, confronti a due riquadri… Mai lo stesso grafico due volte di seguito.
- Numeri grandi che **contano** da 0 al valore. Barre e linee che si disegnano. Elementi che entrano con effetto "pop" (rimbalzo).
- Sempre una **fonte scritta in piccolo** in basso quando c'è un dato (es. "Source: Fidelity 2026").
- Lo sfondo non è mai fermo: particelle d'oro che salgono e luce che passa (già nel codice).

## 3. Lo stile visivo (già nel codice, qui per chiarezza)
- Video MP4 **1920×1080, 30 fps**.
- Sfondo blu navy (10,24,40) con alone azzurro al centro e griglia leggera. **Cornice 3D oro** con bagliore esterno e ombra interna su TUTTE le slide (funzione `frame()` di common2.py).
- Colori: oro (212,172,82), oro chiaro (246,214,140), bianco (236,240,245), **rosso** (232,84,84) per pericoli/soldi persi, **verde** (84,200,124) per cose giuste/guadagni, **blu** (110,160,230), viola (170,130,230), rosa (230,140,190), grigio (150,165,185), card (22,40,64).
- Font (già installati in `/mnt/skills/examples/canvas-design/canvas-fonts/`): titoli **Gloock-Regular** (`SER`), testo **InstrumentSans-Bold** (`BOLD`) e **InstrumentSans-Regular** (`REG`).
- Titolo della slide in alto in oro chiaro con Gloock; numeri enormi con InstrumentSans-Bold.
- Vedi l'immagine `RIFERIMENTO-STILE-SLIDE-video2.png`: è come devono venire tutte le slide.

## 4. Il metodo di lavoro con l'utente (CapCut da telefono)
1. Claude scrive il **copione completo** del video (25 blocchi circa, oltre 10 minuti, ~9.500 caratteri), lo tiene lui e lo consegna **un blocco per messaggio**, in un riquadro di codice da copiare. Velocità reale della voce ≈ 15 caratteri al secondo: verifica che il totale superi i 10 minuti PRIMA di cominciare.
2. L'utente genera la voce di quel blocco in CapCut ("Analista preciso", inglese) e manda **due screenshot della timeline** (inizio e fine, con secondi e fotogrammi) oppure una **registrazione dello schermo**. **La durata delle slide si prende SOLO da lì** (linea bianca al centro). Fotogrammi a 30 fps.
3. Se la durata non torna con la lunghezza del testo (~15 caratteri/s), avvisare: probabilmente manca metà frase.
4. Claude divide il tempo tra le frasi in proporzione ai caratteri (lunghezza+10), raggruppa le frasi in slide e genera gli MP4 con lo **script del blocco** (vedi esempi sotto). Verifica a colpo d'occhio un fotogramma per slide (niente sovrapposizioni di testo).
5. Consegna **tutti i file di quel blocco insieme**, con la sola indicazione "vanno in ordine dopo il blocco N". **Niente elenchi di fotogrammi, durate, conti o descrizioni slide per slide** nella risposta.
6. Ogni video finisce con: like/subscribe + rimando al video precedente, con un **riquadro tratteggiato a destra** dove l'utente metterà l'elemento video della schermata finale.

## 5. Regole del video
- **Aggancio** nei primi secondi: prima frase con una cifra precisa che sorprende ("$185,500 solo per la sanità"), poi la promessa e il mistero ("il numero 3 sorprende quasi tutti"), poi la mappa dei punti.
- Frank e Mary sono i personaggi fissi di esempio: **presentarli da zero in ogni video** (chi guarda può non aver visto gli altri).
- Numeri **sempre verificati** su fonti ufficiali e su più fonti (ssa.gov, medicare.gov, cms.gov, irs.gov, Fidelity, HHS). Se non concordano si usa il dato più recente e prudente.
- Niente musica di sottofondo. Niente sottotitoli scritti nel video (restano quelli automatici di YouTube).
- Al caricamento: contenuti sintetici/IA = **No**; promozione a pagamento = **No**.
- Miniatura: si capisce subito l'argomento, numeri grandi, contrasto forte (formula dei concorrenti americani: sfondo chiaro, MISTAKES in rosso, parola evidenziata in giallo, freccia rossa, soldi che calano). Scripts in `codice/miniature/`.
- Titolo con parola chiave a bassa concorrenza + curiosità; descrizione con la ricerca principale nella prima frase + capitoli ai tempi reali + fonti + disclaimer; tag; hashtag pertinenti (mai #medicare se il video non parla di Medicare).

## 6. Come si rendono le slide (importante per non bloccarsi)
- Ogni comando ha un limite di 300 secondi: **massimo 2-3 slide per comando**, oppure lancia in background.
- Copia `common.py` e `common2.py` in `/home/claude/`, poi ogni blocco è un file `v2bN.py` che fa `from common2 import *` e chiama `render(funzione_disegno, durata_secondi, percorso_output)`.
- Gli MP4 vanno in `/mnt/user-data/outputs/` e si consegnano con `present_files`.
- Dopo ogni blocco controlla un fotogramma per slide (`view`) prima di consegnare.
- La chat ha un limite di 100 immagini: usa contact sheet (più slide in un'unica immagine) e chiedi all'utente registrazioni dello schermo invece di tanti screenshot.

## 7. CODICE — common.py (utilità: colori, font, testo, animazioni, render)
```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, os, shutil, math
W,H=1920,1080; F='/mnt/skills/examples/canvas-design/canvas-fonts/'
navy=(10,24,40); gold=(212,172,82); goldL=(246,214,140); white=(236,240,245); red=(232,84,84); green=(84,200,124); grey=(150,165,185); blue=(110,160,230); card=(22,40,64)
FPS=30
def font(n,s): return ImageFont.truetype(F+n,s)
SER=lambda s: font('Gloock-Regular.ttf',s); BOLD=lambda s: font('InstrumentSans-Bold.ttf',s); REG=lambda s: font('InstrumentSans-Regular.ttf',s)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def back(t):
    t=max(0,min(1,t)); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
def make_bg(grid=False):
    bg=Image.new('RGBA',(W,H),navy+(255,))
    g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W/2-950,H/2-520,W/2+950,H/2+520],fill=(32,62,98,255))
    bg=Image.alpha_composite(bg,g.filter(ImageFilter.GaussianBlur(230)))
    v=Image.new('RGBA',(W,H),(0,0,0,0)); vd=ImageDraw.Draw(v); vd.rectangle([0,0,W,H],fill=(0,0,0,120)); vd.ellipse([-200,-150,W+200,H+150],fill=(0,0,0,0))
    bg=Image.alpha_composite(bg,v.filter(ImageFilter.GaussianBlur(120)))
    if grid:
        gr=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(gr)
        for y in range(0,H,60): gd.line([0,y,W,y],fill=(255,255,255,8),width=1)
        for x in range(0,W,60): gd.line([x,0,x,H],fill=(255,255,255,8),width=1)
        bg=Image.alpha_composite(bg,gr)
    return bg
def txt(L,t,f,y,col,alpha=255,x=None,anchor='c'):
    d=ImageDraw.Draw(L); b=d.textbbox((0,0),t,font=f); w=b[2]-b[0]
    X=(W-w)/2-b[0] if x is None else (x-w/2-b[0] if anchor=='c' else (x-b[0] if anchor=='l' else x-w-b[0]))
    d.text((X,y-b[1]),t,font=f,fill=col+(int(max(0,min(255,alpha))),)); return w
def pop(fr,layer,box,s):
    s=max(0.01,s); piece=layer.crop(box); pw,ph=piece.size
    piece=piece.resize((max(1,int(pw*s)),max(1,int(ph*s))))
    fr.alpha_composite(piece,(int((box[0]+box[2])/2-piece.width/2),int((box[1]+box[3])/2-piece.height/2))); return fr
def render(draw,dur,out):
    d='/home/claude/_fr'; shutil.rmtree(d,ignore_errors=True); os.makedirs(d)
    N=int(round(FPS*dur))
    for fn in range(N):
        draw(fn/FPS).convert('RGB').save(f'{d}/{fn:04d}.png')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{d}/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','18',out],check=True)
def pill(L,text,y,col=gold,alpha=255,size=32,fill=(38,48,52)):
    d=ImageDraw.Draw(L); f=BOLD(size); b=d.textbbox((0,0),text,font=f); pw=b[2]-b[0]+60; ph=b[3]-b[1]+30
    d.rounded_rectangle([(W-pw)/2,y,(W+pw)/2,y+ph],radius=ph/2,fill=fill+(int(alpha),),outline=col+(int(alpha),),width=3)
    d.text(((W-(b[2]-b[0]))/2-b[0],y+15-b[1]),text,font=f,fill=col+(int(alpha),))
def bar(h,col,bw=280):
    im=Image.new('RGBA',(bw,max(2,int(h))),(0,0,0,0)); d=ImageDraw.Draw(im)
    for y in range(im.height):
        t=y/im.height; cc=tuple(int(col[k]*(1-0.38*t)) for k in range(3)); d.line([0,y,bw,y],fill=cc+(255,))
    m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,bw-1,im.height-1],radius=min(20,im.height//2),fill=255); im.putalpha(m); return im

```

## 8. CODICE — common2.py (sfondo animato + cornice 3D oro: usare SEMPRE base(t) e frame())
```python
from common import *
import random
random.seed(7)
M=46  # frame margin
def _frame_layers():
    # outer gold glow
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    gd.rounded_rectangle([M-6,M-6,W-M+6,H-M+6],radius=38,outline=(230,185,90,200),width=26)
    glow=glow.filter(ImageFilter.GaussianBlur(22))
    # bevel ring: vertical+horizontal gradient
    grad=Image.new('RGBA',(W,H)); g2=ImageDraw.Draw(grad)
    for y in range(H):
        t=y/H
        c=(int(255-95*t),int(226-100*t),int(150-95*t))
        g2.line([0,y,W,y],fill=c+(255,))
    ring=Image.new('L',(W,H),0); rd=ImageDraw.Draw(ring)
    rd.rounded_rectangle([M,M,W-M,H-M],radius=34,fill=255); rd.rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,fill=0)
    bevel=Image.new('RGBA',(W,H),(0,0,0,0)); bevel.paste(grad,(0,0),ring)
    # highlight line + inner shadow
    hl=Image.new('RGBA',(W,H),(0,0,0,0)); hd=ImageDraw.Draw(hl)
    hd.rounded_rectangle([M+3,M+3,W-M-3,H-M-3],radius=32,outline=(255,245,200,160),width=2)
    hd.rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,outline=(90,60,15,255),width=3)
    inner=Image.new('RGBA',(W,H),(0,0,0,0)); idd=ImageDraw.Draw(inner)
    idd.rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,outline=(0,0,0,200),width=30)
    inner=inner.filter(ImageFilter.GaussianBlur(18))
    m=Image.new('L',(W,H),0); ImageDraw.Draw(m).rounded_rectangle([M+16,M+16,W-M-16,H-M-16],radius=22,fill=255)
    inner.putalpha(Image.composite(inner.split()[3],Image.new('L',(W,H),0),m))
    # outside dark
    out=Image.new('RGBA',(W,H),(4,10,18,255)); om=Image.new('L',(W,H),255); ImageDraw.Draw(om).rounded_rectangle([M,M,W-M,H-M],radius=34,fill=0)
    out.putalpha(om)
    return out,glow,bevel,hl,inner
_FR=_frame_layers()
_OV=Image.new('RGBA',(W,H),(0,0,0,0))
for _l in [_FR[4],_FR[0],_FR[1],_FR[2],_FR[3]]: _OV=Image.alpha_composite(_OV,_l)
_SW=Image.new('RGBA',(W+1400,H),(0,0,0,0)); ImageDraw.Draw(_SW).polygon([(700,0),(920,0),(520,H),(300,H)],fill=(255,230,160,18)); _SW=_SW.filter(ImageFilter.GaussianBlur(40))
BG=make_bg(grid=True)
parts=[(random.uniform(0,W),random.uniform(0,H),random.uniform(1.5,4),random.uniform(8,25),random.uniform(0,6.28)) for _ in range(55)]
def base(t):
    fr=BG.copy()
    off=int((t*140)%(W+800)); fr.alpha_composite(_SW.crop((1100-off+400, 0, 1100-off+400+W, H)) if False else _SW.crop((max(0,min(W+1400-W, 1100-off)),0,max(0,min(W+1400-W,1100-off))+W,H)))
    P=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(P)
    for (px,py,r,sp,ph) in parts:
        y=(py-t*sp)%H; a=int(70+60*math.sin(t*1.5+ph))
        pd.ellipse([px-r,y-r,px+r,y+r],fill=(246,214,140,a))
    return Image.alpha_composite(fr,P)
def frame(fr):
    return Image.alpha_composite(fr,_OV)

```

## 9. ESEMPIO COMPLETO DI UN BLOCCO — v2b9.py (4 slide con grafici diversi, sincronizzate frase per frase)
```python
from common2 import *
import shutil, sys
S=["Here's the scary part.","Fidelity's research found that the average American expects to spend only about seventy five thousand dollars.","That's less than half of the real number.","Just the standard Medicare Part B premium is two hundred two dollars and ninety cents a month in 2026.","That's more than two thousand four hundred dollars a year, per person, before a single doctor visit, before dental, before vision, before prescriptions.","And if your income is higher, Medicare adds extra charges on top, called IRMAA, based on the tax return you filed two years earlier.","Many retirees only find out when the first bill arrives."]
TOTF=1241
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
G=[[0,1,2],[3],[4],[5,6]]; durs=[sum(fs[i] for i in g) for g in G]; print(fs,durs,sum(durs))
def rel(g): return [sum(fs[g[0]:k])/30 for k in g]
def drawA(t):
    r=rel(G[0]); fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,"HERE'S THE SCARY PART",SER(70),100,red,255*ease(t/0.35))
    cx,cy,R=W/2-330,560,230
    d.ellipse([cx-R,cy-R,cx+R,cy+R],outline=(40,62,92,255),width=50)
    if t>r[1]:
        p=ease((t-r[1])/1.6); frac=75000/185500
        d.arc([cx-R,cy-R,cx+R,cy+R],start=-90,end=-90+360*frac*p,fill=blue+(255,),width=50)
        txt(L,f'{int(frac*100*p)}%',BOLD(90),cy-60,blue,255,x=cx)
        txt(L,'what people expect',REG(30),cy+50,grey,255,x=cx)
        txt(L,f'EXPECTED: ${int(75000*p/100)*100:,}',BOLD(52),380,blue,255,x=W/2+120,anchor='l')
        txt(L,'REAL: $185,500',BOLD(52),480,red,255*ease((t-r[1]-0.8)/0.4),x=W/2+120,anchor='l')
        txt(L,'Source: Fidelity research',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L)
    if t>r[2]:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(52); lab='LESS THAN HALF'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=W/2+120; y=620
        cd.rounded_rectangle([bx,y,bx+bw,y+100],radius=50,fill=red+(255,)); cd.text((bx+40-b[0],y+50-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+105),back((t-r[2])/0.4))
    return frame(fr)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'MEDICARE PART B · STANDARD PREMIUM 2026',SER(56),110,goldL,255*ease(t/0.4))
    # card
    C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x0,y0,x1,y1=W/2-480,260,W/2+480,820
    cd.rounded_rectangle([x0,y0,x1,y1],radius=36,fill=(236,240,245,255)); cd.rectangle([x0,y0+60,x1,y0+150],fill=blue+(255,))
    txt(C,'MEDICARE',BOLD(56),y0+72,(255,255,255),255,x=W/2)
    p=ease((t-0.5)/1.6); v=202.90*p
    txt(C,f'${v:,.2f}',BOLD(150),y0+220,navy,255,x=W/2); txt(C,'PER MONTH · PER PERSON',BOLD(40),y0+420,(90,100,120),255,x=W/2)
    fr=pop(fr,C,(int(x0)-5,y0-5,int(x1)+5,y1+5),back(t/0.45))
    L2=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L2,'Source: CMS (Centers for Medicare & Medicaid Services)',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L); fr=Image.alpha_composite(fr,L2); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'12 MONTHS × $202.90',SER(62),100,goldL,255*ease(t/0.4)); fr=Image.alpha_composite(fr,L)
    # calendar grid
    for m in range(12):
        st=0.2+m*0.12
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); x=260+(m%6)*150; y=240+(m//6)*150
        cd.rounded_rectangle([x,y,x+130,y+130],radius=16,fill=card+(255,),outline=blue+(255,),width=3)
        txt(C,['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][m],BOLD(28),y+14,white,255,x=x+65); txt(C,'$203',BOLD(34),y+62,red,255,x=x+65)
        fr=pop(fr,C,(x-5,y-5,x+135,y+135),back((t-st)/0.35))
    p=ease((t-1.8)/1.2)
    if p>0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,f'${2434.80*p:,.2f}',BOLD(96),290,red,255,x=1480); txt(L,'PER YEAR',BOLD(40),410,white,255*p,x=1480); txt(L,'per person',REG(32),470,grey,255*p,x=1480)
        fr=Image.alpha_composite(fr,L)
    items=['DOCTOR VISITS','DENTAL','VISION','PRESCRIPTIONS']
    for k,it in enumerate(items):
        st=4.0+k*0.9
        if t<st: continue
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(36); lab='+ '+it; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+60; x=260+k*380; y=640
        cd.rounded_rectangle([x,y,x+bw,y+80],radius=40,fill=card+(255,),outline=red+(255,),width=3); cd.text((x+30-b[0],y+40-(b[3]-b[1])/2-b[1]),lab,font=f,fill=red+(255,))
        fr=pop(fr,C,(x-5,y-5,int(x+bw)+5,y+85),back((t-st)/0.4))
    if t>4.0:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); txt(L,'...and that is BEFORE all of these',BOLD(40),780,white,255*ease((t-4.0)/0.4)); fr=Image.alpha_composite(fr,L)
    return frame(fr)
def drawD(t):
    r=rel(G[3]); fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'HIGHER INCOME = EXTRA MEDICARE CHARGES',SER(54),95,goldL,255*ease(t/0.4))
    # staircase
    base_=760; x0=280
    for k in range(5):
        p=ease((t-0.4-k*0.35)/0.5)
        if p<=0: continue
        h=(80+k*80)*p; x=x0+k*150; col=tuple(int(gold[i]+(red[i]-gold[i])*k/4) for i in range(3))
        d.rounded_rectangle([x,base_-h,x+130,base_],radius=10,fill=col+(255,))
    d.line([x0-20,base_,x0+760,base_],fill=gold+(255,),width=3); txt(L,'YOUR INCOME →',BOLD(30),base_+16,grey,255,x=x0,anchor='l'); txt(L,'EXTRA PREMIUM',BOLD(30),base_-450,grey,255,x=x0,anchor='l')
    if t>1.6:
        txt(L,'IRMAA',BOLD(120),260,red,255*ease((t-1.6)/0.4),x=1400)
        txt(L,'based on your tax return',REG(38),420,white,255*ease((t-2.4)/0.4),x=1400)
        txt(L,'from 2 years earlier',BOLD(44),475,white,255*ease((t-2.4)/0.4),x=1400)
    fr=Image.alpha_composite(fr,L)
    if t>r[1]:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); cx,cy=1400,720
        cd.rectangle([cx-170,cy-100,cx+170,cy+100],fill=(236,240,245,255)); cd.polygon([(cx-170,cy-100),(cx,cy+10),(cx+170,cy-100)],outline=(160,170,190,255),width=5)
        cd.rounded_rectangle([cx-120,cy+20,cx+120,cy+80],radius=10,fill=red+(255,)); txt(C,'FIRST BILL',BOLD(34),cy+32,(255,255,255),255,x=cx)
        fr=pop(fr,C,(cx-175,cy-105,cx+175,cy+105),back((t-r[1])/0.45))
    return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b9-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y9{i}.png')

```

## 10. SECONDO ESEMPIO — v2b3.py (5 slide: clessidra, linea del tempo, persone, barre, confronto)
```python
from common2 import *
import shutil, sys
S=["Mistake number one: planning for the wrong number of years.","Most people plan their retirement as if it will last fifteen or twenty years.","But according to the Social Security Administration, about one in four sixty five year olds today will live past ninety.","And about one in ten will live past ninety five.","That means your money may need to last thirty years or more.","And women, on average, live even longer than men, which makes this mistake even more dangerous for a surviving wife."]
TOTF=979
w=[len(x)+10 for x in S]; T=sum(w); fs=[round(x/T*TOTF) for x in w]; fs[-1]=TOTF-sum(fs[:-1])
durs=[fs[0],fs[1],fs[2]+fs[3],fs[4],fs[5]]; print(fs,durs,sum(durs)); s4=fs[2]/30
pink=(230,140,190)
def person(d,cx,cy,col,s=1.0):
    d.ellipse([cx-18*s,cy-52*s,cx+18*s,cy-16*s],fill=col); d.rounded_rectangle([cx-30*s,cy-10*s,cx+30*s,cy+46*s],radius=int(22*s),fill=col)
def drawA(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    a=ease(t/0.35); txt(L,'MISTAKE #1',BOLD(110),170,gold,255*a)
    cx,cy=W/2,520; f=(t*0.5)%1
    d.polygon([(cx-80,cy-110),(cx+80,cy-110),(cx,cy)],outline=gold+(255,),width=6); d.polygon([(cx-80,cy+110),(cx+80,cy+110),(cx,cy)],outline=gold+(255,),width=6)
    d.polygon([(cx-80*(1-f),cy-110+110*f),(cx+80*(1-f),cy-110+110*f),(cx,cy)],fill=gold+(255,))
    d.polygon([(cx-80*f,cy+110-60*f),(cx+80*f,cy+110-60*f),(cx+80,cy+110),(cx-80,cy+110)],fill=gold+(255,))
    d.line([cx,cy,cx,cy+110],fill=goldL+(200,),width=3)
    txt(L,'PLANNING FOR THE WRONG NUMBER OF YEARS',BOLD(50),720,white,255*ease((t-0.3)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def timeline(d,L,y,a0,a1,col,label,p,x0=260,x1=1660,alpha=255):
    def ax(a): return x0+(a-65)/(100-65)*(x1-x0)
    xe=ax(a0)+(ax(a1)-ax(a0))*p
    d.rounded_rectangle([ax(a0),y,xe,y+70],radius=35,fill=col+(alpha,))
    if p>0.9: txt(L,label,BOLD(40),y+14,navy,255,x=(ax(a0)+xe)/2)
    return ax
def axis(d,L,y,x0=260,x1=1660):
    d.line([x0,y,x1,y],fill=gold+(255,),width=3)
    for a in range(65,101,5):
        x=x0+(a-65)/(35)*(x1-x0); d.line([x,y-8,x,y+8],fill=gold+(255,),width=3); txt(L,str(a),REG(30),y+18,grey,255,x=x)
def drawB(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WHAT MOST PEOPLE PLAN FOR',SER(66),120,goldL,255*ease(t/0.4))
    axis(d,L,760)
    p=ease((t-0.4)/1.4); timeline(d,L,470,65,85,grey,'15-20 YEARS',p)
    txt(L,'retire at 65  →  money lasts until ~85',REG(36),600,white,255*ease((t-1.6)/0.4))
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawC(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'HOW LONG 65-YEAR-OLDS REALLY LIVE',SER(58),100,goldL,255*ease(t/0.4))
    # row 1: 1 in 4
    a=ease((t-0.3)/0.5)
    for k in range(4):
        col=gold if k==0 else (90,110,140); person(d,420+k*120,360,col+(int(255*a),),1.3)
    if t>1.2:
        txt(L,'1 IN 4',BOLD(80),300,gold,255*ease((t-1.2)/0.4),x=1100,anchor='l'); txt(L,'will live past 90',REG(40),395,white,255*ease((t-1.2)/0.4),x=1100,anchor='l')
    if t>s4:
        b=ease((t-s4)/0.5)
        for k in range(10):
            col=red if k==0 else (90,110,140); person(d,300+k*75,700,col+(int(255*b),),0.95)
        txt(L,'1 IN 10',BOLD(80),640,red,255*b,x=1100,anchor='l'); txt(L,'will live past 95',REG(40),735,white,255*b,x=1100,anchor='l')
    txt(L,'Source: Social Security Administration',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawD(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'YOUR MONEY MAY NEED TO LAST',SER(66),110,goldL,255*ease(t/0.4))
    axis(d,L,800)
    timeline(d,L,400,65,85,grey,'WHAT YOU PLANNED',1.0,alpha=160)
    p=ease((t-0.4)/1.6); timeline(d,L,560,65,95,gold,'30+ YEARS',p)
    if p>0.95:
        x85=260+(85-65)/35*1400; x95=260+(95-65)/35*1400
        d.rounded_rectangle([x85,540,x95,650],radius=20,outline=red+(255,),width=5)
        txt(L,'UNFUNDED?',BOLD(40),670,red,255*ease((t-2.1)/0.4),x=(x85+x95)/2)
    fr=Image.alpha_composite(fr,L); return frame(fr)
def drawE(t):
    fr=base(t); L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
    txt(L,'WOMEN LIVE LONGER ON AVERAGE',SER(64),110,goldL,255*ease(t/0.4))
    x0,x1=640,1640
    def ax(a): return x0+(a-65)/(95-65)*(x1-x0)
    for i,(lab,age,col,st) in enumerate([('MEN',84,blue,0.3),('WOMEN',87,pink,0.9)]):
        p=ease((t-st)/1.2)
        if p<=0: continue
        y=300+i*190; person(d,300,y+50,col+(255,),1.3); txt(L,lab,BOLD(44),y+28,col,255,x=390,anchor='l')
        xe=x0+(ax(age)-x0)*p; d.rounded_rectangle([x0,y,xe,y+100],radius=24,fill=col+(255,)); txt(L,f'~{int(65+(age-65)*p)}',BOLD(64),y+14,navy,255,x=max(x0+90,xe-90))
    if t>3.0:
        C=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(C); f=BOLD(44); lab='THE BIGGEST RISK: A SURVIVING WIFE'; b=cd.textbbox((0,0),lab,font=f); bw=b[2]-b[0]+80; bx=(W-bw)/2; y=760
        cd.rounded_rectangle([bx,y,bx+bw,y+96],radius=48,fill=red+(255,)); cd.text((bx+40-b[0],y+48-(b[3]-b[1])/2-b[1]),lab,font=f,fill=(255,255,255,255))
        fr=Image.alpha_composite(fr,L); L=Image.new('RGBA',(W,H),(0,0,0,0)); fr=pop(fr,C,(int(bx)-5,y-5,int(bx+bw)+5,y+101),back((t-3.0)/0.45))
    txt(L,'Life expectancy at 65 · Source: Social Security Administration',REG(26),985,grey,200)
    fr=Image.alpha_composite(fr,L); return frame(fr)
sel=[int(x) for x in sys.argv[1:]] or [1,2,3,4,5]
for i,(fn,f) in enumerate(zip([drawA,drawB,drawC,drawD,drawE],durs),1):
    if i not in sel: continue
    render(fn,f/30,f'/mnt/user-data/outputs/v2-b3-0{i}.mp4'); shutil.copy(f'/home/claude/_fr/{f-3:04d}.png',f'/home/claude/y3{i}.png')

```

Tutti gli altri blocchi (25 del video 2, 16 del video 1) e le miniature sono nei file `codice/` del kit: aprili per riprendere idee di grafici.
