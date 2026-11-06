"""Genera PUBBLICAZIONE-VIDEO16.md con i capitoli dalla fine dei blocchi (fine_blocchi.txt), arrotondati per difetto."""
import re
fin = [int(x) for x in open('fine_blocchi.txt') if x.strip()]
starts = [0] + fin[:-1]
names = {1: 'The letter that can take half of your check', 2: 'Meet Carol: a $9,000 overpayment letter', 3: 'What the notice must tell you', 4: 'The danger: up to 50% withheld',
         5: 'The 30-day rule and the four moves', 6: 'Move 1: dispute the debt (reconsideration, 60 days)', 7: 'Why a hearing request does not pause the deductions', 8: 'Move 2: the waiver (no deadline)',
         9: 'Waiver gate 1: fault', 10: 'Waiver gate 2: three doors (small debt, hardship)', 11: 'Door 3: fairness, and back to Carol', 12: 'Move 3: ask for a lower monthly rate',
         13: 'Move 4: file review and personal conference', 14: 'What happens if you do nothing', 15: 'The April 25, 2025 twist (10% vs 50%) and SSI', 16: 'How to avoid the letter, and Carol\'s plan', 17: 'The 4 moves recap, comment and disclaimer'}
def ts(fr):
    s = fr // 30; return f'{s // 60}:{s % 60:02d}'
ch = '\n'.join(f'{ts(starts[b - 1])} {names[b]}' for b in range(1, 18))
tot = fin[-1]
TITLE = 'Social Security Overpayment Letter? They Can Take Up to 50% of Your Check (Do This First)'
tags = 'social security overpayment,social security overpayment letter,social security overpayment waiver,social security overpayment not my fault,ssa overpayment,overpayment waiver ssa 632,request for reconsideration social security,social security 50 percent withholding,social security overpayment appeal,social security debt,social security clawback,how to stop social security overpayment withholding,ssa 634 lower repayment rate,social security benefits,retirement over 65,senior money'
txt = f'''# VIDEO 16 - Lettera di sovrapagamento Social Security (30-31/10/2026) - testi da incollare
Struttura identica ai video 10-15. Capitoli = inizio di ogni blocco (fine_blocchi.txt, {tot} fotogrammi = {ts(tot)}), arrotondati per difetto.
Ricerca: curl YouTube 30/10 (virali sul tema: 60 Minutes "Social Security recipients struggle to pay back agency after unexpected overpayments" 1,36M view, "Social Security overpayments: Tips to prevent them" 262K, "3 New Rules Quietly Taking Money From Your Check Starting October" 236K in 3 settimane, "BANKS JUST STARTED FLAGGING SOCIAL SECURITY DIRECT DEPOSITS" 138K); vidIQ 5 crediti (saldo 7 -> 2): keyword 'social security overpayment' volume esatto <750/mese (concorrenza 59, overall 17): le view del tema vengono dai suggeriti, non dalla ricerca; suggerimenti di ricerca YouTube gratis: "social security overpayment waiver", "social security overpayment not my fault". Titolo non scorato su vidIQ (crediti finiti): struttura diversa dai video 11-15 ("Every ..."), parola chiave all'inizio.
Fonti verificate: FONTI-VERIFICATE.md (SSA Emergency Message EM-25029 REV, POMS GN 02201, GN 02210, GN 02250, GN 02270).

## Dove va
Playlist "Retirement After 50" (non esiste ancora sul canale: crearla). Schermata finale -> video 9 "5 New Social Security Numbers for 2027 (It's Not Just the COLA)" (https://youtu.be/AcJedeubAv4), il piu' legato (regole sull'assegno e sul limite di guadagno, causa di molti sovrapagamenti).

## Titolo
{TITLE}

## Descrizione
Got a Social Security overpayment letter? The agency's own rules say the default can be up to 50% of your monthly benefit withheld until the debt is repaid, but the same rules give you four moves that can freeze, shrink or erase it. In this video you will see the exact steps and the exact numbers, from the Social Security Administration's own manuals.

We follow one fictional person. Carol is 66 and gets $2,100 a month. Her letter says she was paid $600 too much for 15 months, a $9,000 debt. What you will learn: 1) what the notice must tell you: the total, what you were paid, what you should have been paid, the reason, the months, and your three rights, 2) the default rate: up to 50% of the monthly benefit for notices sent on or after April 25, 2025, and why you should answer inside 30 days, 3) move 1, reconsideration: dispute the fact or the amount within 60 days, with a specific reason, 4) why a hearing request does not pause the deductions but a waiver request does, 5) move 2, the waiver: no deadline, Form SSA-632-BK, not at fault plus one of three doors (small debt of $2,000 or less, hardship, or fairness), 6) move 3, a lower monthly rate, and Form SSA-634 for longer plans, 7) move 4, the file review and the personal conference, 8) what happens if you do nothing, and the April 2025 twist, with SSI at 10%.

CHAPTERS
{ch}

WATCH NEXT
5 New Social Security Numbers for 2027 (It's Not Just the COLA)
https://youtu.be/AcJedeubAv4

SOURCES
Social Security Administration (ssa.gov): Emergency Message EM-25029 REV (overpayment default withholding rate), Program Operations Manual System (POMS) GN 02201 (overpayment notice, reconsideration, collection), GN 02210 (recovery rate), GN 02250 (waiver), GN 02270 (personal conference)

Disclaimer: This video is for education only and is not legal, tax or financial advice. Carol is a fictional example. Rules, amounts and ages change and differ by person and by case. Always confirm with the Social Security Administration or the official source before you act. This channel is not affiliated with the Social Security Administration.

Subscribe to The Money Backstory for more clear explanations of retirement for Americans over 50: https://www.youtube.com/@TheMoneyBackstoryUSA?sub_confirmation=1

#SocialSecurity #Overpayment #Retirement

## Tag
{tags}

## Commento da fissare
Did your overpayment letter match what we described? Tell me what it said, and send this to someone who gets Social Security mail.

## Impostazioni
IA No. Promozione No. Schermata finale 20 s -> video 9 (AcJedeubAv4). Miniatura: test A/B con le 2 miniature in miniature_video16/ (codice code/thumbs_video16.py).
'''
open('PUBBLICAZIONE-VIDEO16.md', 'w').write(txt)
print('titolo', len(TITLE), 'tag caratteri', len(tags)); print(ch)
