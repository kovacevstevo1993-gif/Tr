"""Genera PUBBLICAZIONE-VIDEO17.md con i capitoli dalla fine dei blocchi (fine_blocchi.txt), arrotondati per difetto."""
fin = [int(x) for x in open('fine_blocchi.txt') if x.strip()]
starts = [0] + fin[:-1]
names = {1: 'Your plan is not renewed: what happens on January 1', 2: 'Meet Gloria and her letter', 3: 'The Plan Non-Renewal Notice', 4: 'The national picture (CMS numbers)',
         5: 'The dates: December 7 and the second window', 6: 'When your new plan starts (January, February, March)', 7: 'The default: Original Medicare and no drug plan',
         8: 'The Part D late enrollment penalty', 9: 'Count the days: 59 vs 63', 10: 'A merged plan is not a non-renewal', 11: 'Extra Help: the blue notice',
         12: 'Step 1: find the end date (and 1-800-MEDICARE)', 13: 'Step 2: compare in the Medicare Plan Finder', 14: 'Step 3: Original Medicare and the Medigap timing',
         15: 'The five facts recap', 16: 'Comment and disclaimer'}
def ts(fr):
    s = fr // 30; return f'{s // 60}:{s % 60:02d}'
ch = '\n'.join(f'{ts(starts[b - 1])} {names[b]}' for b in range(1, 17))
tot = fin[-1]
TITLE = 'Medicare Advantage Plan Not Renewed for 2027? Why December 7 Is Not Your Last Chance'
tags = ','.join(['medicare advantage plan not renewed', 'medicare advantage non renewal notice', 'medicare advantage plan ending 2027', 'medicare plan non renewal letter', 'medicare 2027',
                 'medicare open enrollment 2027', 'medicare open enrollment dec 7', 'medicare special enrollment period', 'medicare advantage plans 2027', 'part d late enrollment penalty',
                 'medicare advantage to original medicare', 'medicare plan finder', 'medicare 2027 changes', 'medicare for seniors', 'retirement over 65'])
DESC_HEAD = ("Medicare Advantage plan not renewed for 2027? Medicare's own rules say that if you join nothing before your plan ends, you are moved into Original Medicare, and your drug coverage ends with it. "
             "But the same rules give you a second window that runs past December 7, and they also set a penalty that is added permanently. In this video you will see the exact dates and numbers, from Medicare.gov and CMS.")
DESC_LEARN = ("We follow one fictional person. Gloria is 71, has a Medicare Advantage plan with drug coverage, and gets a letter in October saying her plan is leaving the Medicare program. "
              "What you will learn: 1) what the Plan Non-Renewal Notice is and what Medicare says you must do, 2) the national numbers from CMS: about 5,553 Advantage plans this year and about 5,532 next year, and about 8 in 10 members who can keep their plan at the same or a lower premium, "
              "3) the ordinary window (October 15 to December 7) and the second window (December 8 to the last day of February), 4) when your new plan starts if you ask in December, January or February, "
              "5) what happens if you join nothing: Original Medicare, with no drug plan, 6) the Part D late enrollment penalty: 63 days in a row without drug coverage, 1% of the national base beneficiary premium ($38.99 for 2026) per full month, added permanently, "
              "7) the day count: January 1 to the end of February is 59 days, under the 63-day line, 8) why a plan that is merged into another plan does not get the special window, 9) the blue notice for people with Extra Help, "
              "10) your three steps: find the end date, compare in the Medicare Plan Finder, and what choosing Original Medicare means: a drug plan you add yourself, and the Medigap window of 60 days before to 63 days after.")
txt = f'''# VIDEO 17 - Piano Medicare Advantage non rinnovato (06/11/2026) - testi da incollare
Struttura identica ai video 10-16. Capitoli = inizio di ogni blocco (fine_blocchi.txt, {tot} fotogrammi = {ts(tot)}), arrotondati per difetto.
Ricerca (tema del canale: Medicare over 65): curl YouTube 06/11 (canali piccoli con oltre 100.000 view sul tema: Neal K. Shah, 8.450 iscritti, "Medicare Is Quietly Canceling Plans (Check Your Mail Now)" 573.643 view in 2 settimane e "The Medicare Advantage Bloodbath Has Begun" 338.062; Medicare 365, 32.900 iscritti, 325.892); check_tema.py: zero HIT su non-renewal, special enrollment, late enrollment penalty (video 10 ha l'Annual Notice of Change e la finestra gennaio-marzo, video 14 il diritto Medigap: qui solo un cenno). vidIQ: keyword 'medicare advantage plan ending 2027' <750/mese (5 crediti), score_title 3 titoli (15 crediti): 95 (scelto), 95, 92. Saldo 32.
Fonti verificate: FONTI-VERIFICATE.md (Medicare.gov, CMS: comunicato 28/09/2026, guida iscrizioni 2027).

## Dove va
Playlist "Retirement After 50" (non esiste ancora sul canale: crearla). Schermata finale -> video 14 "Every Senior Must Know This Medigap Rule Before December 7 (Don't Drop It)" (https://youtu.be/u9VnlXdae2g), il piu' legato (piano Advantage che finisce, Original Medicare, Medigap).

## Titolo
{TITLE}

## Descrizione
{DESC_HEAD}

{DESC_LEARN}

CHAPTERS
{ch}

WATCH NEXT
Every Senior Must Know This Medigap Rule Before December 7 (Don't Drop It)
https://youtu.be/u9VnlXdae2g

SOURCES
Medicare.gov: Plan Non-Renewal Notice, Special Enrollment Periods, Part D late enrollment penalty, When can I buy a Medigap policy, Medicare Advantage Plan Reassignment Notice. CMS (cms.gov): press release of September 28, 2026, Medicare Advantage and Part D Enrollment and Disenrollment Guidance for contract year 2027.

Disclaimer: This video is for education only and is not insurance, legal or financial advice. Gloria is a fictional example. Rules, plans, prices and dates change and differ by plan and by state. Always confirm with Medicare or your plan before you act. This channel is not affiliated with Medicare or any government agency.

Subscribe to The Money Backstory for more clear explanations of retirement for Americans over 50: https://www.youtube.com/@TheMoneyBackstoryUSA?sub_confirmation=1

#Medicare #MedicareAdvantage #Retirement

## Tag
{tags}

## Commento da fissare
Which date surprised you most: December 7, the end of February, or the 63 days? Tell me, and send this to someone who has a Medicare Advantage plan.

## Impostazioni
IA No. Promozione No. Schermata finale 20 s -> video 14 (u9VnlXdae2g). Miniatura: test A/B con le 2 miniature in miniature_video17/ (codice code/thumbs_video17.py).
'''
open('PUBBLICAZIONE-VIDEO17.md', 'w').write(txt)
print('titolo', len(TITLE), 'tag caratteri', len(tags), 'descrizione', len(DESC_HEAD) + len(DESC_LEARN)); print(ch)
