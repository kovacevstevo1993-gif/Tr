"""Genera PUBBLICAZIONE-VIDEO15.md con i capitoli dalla fine dei blocchi (fine_blocchi.txt), arrotondati per difetto."""
import re
fin = [int(x) for x in open('fine_blocchi.txt') if x.strip()]
starts = [0] + fin[:-1]
names = {1: 'A home sale after 65: is the profit tax free?', 2: 'Meet Ray and Donna', 3: 'Official sources and the five things to know', 4: 'Who qualifies: the $250,000 and $500,000 exclusion',
         5: 'The details: 730 days, married couples, nursing homes', 6: 'How the gain is counted', 7: 'What goes into your basis', 8: 'Ray and Donna: the math', 9: 'Why your receipts matter',
         10: 'The federal tax rate on the gain', 11: 'Net investment income tax, state tax, depreciation', 12: 'The paperwork: Form 1099-S and Form 8949', 13: 'The ripples: Medicare looks back two years',
         14: 'The Part B premium surcharge (2026 brackets)', 15: 'When Social Security becomes taxable', 16: 'The partial exclusion', 17: 'The surviving spouse and the two-year window',
         18: 'A new basis for the survivor', 19: 'Inherited home vs gifted home', 20: 'What to do before you sign', 21: 'The 5-point recap', 22: 'Share, comment and disclaimer'}
def ts(fr):
    s = fr // 30; return f'{s // 60}:{s % 60:02d}'
ch = '\n'.join(f'{ts(starts[b - 1])} {names[b]}' for b in range(1, 23))
tot = fin[-1]
txt = f'''# VIDEO 15 - Vendere casa dopo i 65 anni (28-29/10/2026) - testi da incollare
Struttura identica ai video 10-14. Capitoli = inizio di ogni blocco (fine_blocchi.txt, {tot} fotogrammi = {ts(tot)}), arrotondati per difetto.
Ricerca: curl YouTube 28/10 (video virali sul tema: "Beware of the HUGE Medicare Penalty for Selling Your Home After 63" 1,49M view; "Capital Gains Tax on Selling Your Home After 65" 2.748 view in 1 giorno); vidIQ (15 crediti, saldo 22 -> 12, poi 2 per altre chat): keyword 'social security payment schedule' <750/mese (tema scartato); score_title "Every Senior Must Know This Before Selling Their Home After 65 (Tax and Medicare Trap)" = 96 (scelto); "Selling Your Home After 65: The $250,000 Tax Rule Most Seniors Get Wrong (Medicare Trap)" = 93. Tag da suggerimenti di ricerca YouTube (gratis).
Fonti verificate: FONTI-VERIFICATE.md (IRS Pub 523, Topic 701/409/559, Pub 915, Rev. Proc. 2025-32, CMS 2026, SSA POMS).

## Dove va
Playlist "Retirement After 50" (non esiste ancora sul canale: crearla). Schermata finale -> video 4 "Medicare IRMAA Explained: The $974 Trap at Age 61" (https://youtu.be/3BdbOvrO4Sc), il piu' legato (spiega il surcharge Medicare a 2 anni).

## Titolo
Every Senior Must Know This Before Selling Their Home After 65 (Tax and Medicare Trap)

## Descrizione
Selling your home after 65? The I R S lets you exclude up to $250,000 of profit, or $500,000 on a joint return, but part of the profit can still be taxed, and that same profit can raise your Medicare premiums two years later and make more of your Social Security taxable. In this video you will see the exact rules and the exact math, step by step. Every fact comes from the I R S, the Social Security Administration and Medicare.

We follow two fictional people. Ray and Donna are both 72, married and filing jointly. They paid $140,000 for their home, spent $60,000 on a new roof and a kitchen, and now plan to sell for $900,000. Their other income is about $90,000 a year. What you will learn: 1) who qualifies for the exclusion: you must have owned the home and lived in it as your main home for at least 24 months (730 days, not necessarily in a row) during the 5 years before the sale; for a joint return one spouse must meet the ownership test but both must meet the use test; you can use it once every 2 years; time in a licensed nursing home can count, 2) the gain formula: selling price minus selling costs gives the amount realized, minus your adjusted basis gives the gain; losses on a home are not deductible, 3) what goes into your basis (closing costs and improvements such as a new roof, kitchen remodel, addition, heating system) and what does not (repairs, painting, loan fees and points), and why you must keep your receipts, 4) the math for Ray and Donna: basis $200,000, amount realized $846,000, gain $646,000, exclusion $500,000, taxable gain $146,000, 5) the federal capital gains rates for 2026 (0%, 15%, 20%; 0% up to $98,900 of taxable income on a joint return and 15% up to $613,700), the 3.8% net investment income tax and the depreciation rule, 6) the paperwork: Form 1099-S and Form 8949, withholding and estimated payments, 7) how the taxable gain can raise your Medicare Part B premium two years later (an illustration with the 2026 brackets: $81.20 more per person per month, $1,948.80 for the year), 8) when Social Security benefits become taxable ($25,000 single, $32,000 joint, and up to 85% above $34,000 or $44,000), 9) the partial exclusion for a work move, a health reason or an unforeseeable event, 10) the surviving spouse: the $500,000 exclusion if you sell within 2 years of the death and have not remarried, and the new basis for the half of the home that belonged to the spouse who died, 11) inherited homes get a new basis equal to the value at death, while a gifted home usually keeps your basis, 12) five steps to take before you sign a contract.

CHAPTERS
{ch}

WATCH NEXT
Medicare IRMAA Explained: The $974 Trap at Age 61
https://youtu.be/3BdbOvrO4Sc

SOURCES
Internal Revenue Service (irs.gov): Publication 523 Selling Your Home, Topic 701 Sale of your home, Topic 409 Capital gains and losses, Topic 559 Net investment income tax, Publication 915 Social Security and equivalent railroad retirement benefits, Revenue Procedure 2025-32; Centers for Medicare and Medicaid Services (cms.gov): 2026 Medicare Parts A and B premiums and income-related amounts; Social Security Administration (ssa.gov): Program Operations Manual, income-related monthly adjustment amount

Disclaimer: This video is for education only and is not tax, financial or legal advice. Ray and Donna are fictional examples. Rules, amounts and ages change and differ by location, by state and by person. The Medicare numbers are the 2026 ones and are an illustration only. Always confirm with the I R S, a qualified tax professional or the official source before you act. This channel is not affiliated with the I R S, the Social Security Administration, Medicare or CMS.

Subscribe to The Money Backstory for more clear explanations of retirement for Americans over 50: https://www.youtube.com/@TheMoneyBackstoryUSA?sub_confirmation=1

#SellingYourHome #HomeSaleTax #Retirement

## Tag
selling home after 65,selling your home after 65,capital gains,selling your home taxes,selling a house taxes,home sale tax exclusion,home sale capital gains exclusion,capital gains tax on home sale,capital gains on home sale,home sale tax,section 121 exclusion,medicare part b premium,medicare irmaa,taxable social security,surviving spouse home sale,inherited home basis,step up in basis,retirement taxes,retirement over 65,senior taxes

## Commento da fissare
Would you sell your home, or stay? Tell me below, and send this to someone who is thinking about selling.

## Impostazioni
IA No. Promozione No. Schermata finale 20 s -> video 4 (IRMAA, 3BdbOvrO4Sc). Miniatura: test A/B con le 2 miniature in miniature_video15/ (codice code/thumbs_video15.py).
'''
open('PUBBLICAZIONE-VIDEO15.md', 'w').write(txt)
tags = re.search(r'## Tag\n(.*)\n', txt).group(1); print('tag caratteri', len(tags)); print(ch)
