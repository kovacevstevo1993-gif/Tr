import json, re, collections
B = [
# 1 gancio
"If your Medicare Advantage plan is not renewed, it ends on December thirty-first. If you have not joined another plan by then, Medicare moves you into Original Medicare, and if your plan included drug coverage, that coverage ends with it. Medicare says the warning arrives as a letter in October. And the same rules name a second window, one that runs past December seventh. Stay with me, because that window has its own dates, its own trap, and a penalty that Medicare says is added permanently.",
# 2 iscrizione + Gloria
"This is The Money Backstory, where we turn official rules into real numbers. If this helps, subscribe now and tap the bell, so the next breakdown finds you. Now meet Gloria, seventy-one. She has a Medicare Advantage plan with drug coverage. In October, a letter arrives from her plan. It says her plan will leave the Medicare program next year. Gloria is about to learn that the date everyone repeats is not the only date that counts.",
# 3 la lettera
"First, let us look closely at what this letter actually is. Medicare calls it the Plan Non-Renewal Notice. Medicare says you get it if your plan is leaving the Medicare program in the coming year. It comes in October, and your plan sends it. Medicare gives one instruction: you must look for a new plan for coverage next year. The word is must, not may. So this letter is not an advertisement and it is not a reminder. It is the start of a deadline.",
# 4 quadro nazionale
"Before anyone panics, here is the national picture. On September twenty-eighth, the Centers for Medicare and Medicaid Services said the number of Advantage plans is expected to go from five thousand five hundred fifty-three this year to about five thousand five hundred thirty-two next year. That agency also said about eight in ten Advantage members can stay in their current plan with the same or a lower premium. A national average cannot tell you about your own plan. Only your own letter can.",
# 5 le date
"Now let us look at the dates, because the dates are where this gets tricky. Open enrollment runs from October fifteenth to December seventh, and changes made then start on January first. That is the date everyone repeats. But Medicare's own chart lists a second window for people whose plan will not continue. It opens on December eighth and closes on the last day of February. So for Gloria, December seventh is not the end of the road. It is the end of the ordinary window.",
# 6 date di inizio
"Here is how the start dates work in that second window, from the enrollment guidance for twenty twenty-seven. A request received from December eighth through December thirty-first starts on January first. A request received in January starts on February first. A request received in February starts on March first. So Gloria is allowed to wait. But every month she waits is another month when she has no Advantage plan.",
# 7 il default
"Now the default, because this is where people get caught. Medicare's chart says you will be enrolled in Original Medicare if you do not join another Advantage plan before your current plan ends. Original Medicare is Part A and Part B. Drug coverage is not inside it. In Original Medicare, drug coverage is a separate plan that you join yourself. So if Gloria does nothing, on January first she has hospital and doctor coverage, and no drug plan.",
# 8 penale part D
"That gap can have a price. Medicare charges a Part D late enrollment penalty if there is a stretch of sixty-three days or more in a row without Medicare drug coverage or other creditable drug coverage. The penalty is one percent of the national base beneficiary premium, which Medicare lists as thirty-eight dollars and ninety-nine cents for twenty twenty-six, for each full month without coverage. Medicare says it is added to your premium permanently, for as long as you have drug coverage.",
# 9 conta dei giorni
"So count the days, the way Medicare does. Suppose Gloria's coverage stops at the end of December and she joins a drug plan that starts on March first. January has thirty-one days and February has twenty-eight, so the gap is fifty-nine days. That is under the sixty-three day line. Medicare's own example shows what crossing it means: fourteen months without coverage, and you owe a fourteen percent penalty on top of your plan premium. People who get Extra Help do not pay it.",
# 10 consolidamento
"Here is a trap inside the letter itself. Not every change is a non-renewal. The enrollment guidance says people whose plan was merged into another plan, called a consolidation, do not get this special enrollment period, because a consolidation is not a termination and not a non-renewal. So read the wording of your letter. Leaving the Medicare program is one thing. Moving you into a different plan is another, and then the ordinary dates apply.",
# 11 avviso blu Extra Help
"If you get Extra Help, there is a second letter. Medicare calls it the Medicare Advantage Plan Reassignment Notice, and it is blue. It arrives in late October or early November, and it says that unless you choose a new Advantage plan or a drug plan yourself, Medicare will reassign you to a Medicare drug plan for the coming year. Medicare's advice is simple: keep the notice, compare plans, and change in early December if you choose.",
# 12 passo 1 data
"So what should Gloria do this week? Step one: find the date. The rules require a plan to give each affected member the effective date of the end of the plan, and a description of other ways to get Medicare benefits. If your letter does not make the date clear, call your plan. You can also call one eight hundred Medicare, which the agency says is open twenty-four hours a day, seven days a week.",
# 13 passo 2 plan finder
"Step two is to compare your options, and Medicare gives you a tool for that. The Medicare Plan Finder at medicare dot gov lets you compare health and drug plans, including premiums, costs and benefits. This year it also lets you save your doctors, link straight to a plan's drug list and summary of benefits, and see messages about changes affecting your current plan for twenty twenty-seven. Gloria can check her doctors and her drugs in one sitting before she picks anything.",
# 14 passo 3 Original Medicare
"Step three: if Gloria wants Original Medicare instead, she must add a drug plan herself, and a Medigap policy is a separate decision with its own rules. Medicare says your right to buy one after an Advantage plan ends runs from sixty days before your coverage ends to no more than sixty-three days after, and your state may give you more time. Keep every letter from your plan, because you may need it to prove when the coverage ended.",
# 15 riepilogo
"To sum up, here are the five facts that matter. One: a non-renewal letter arrives in October, and Medicare says you have to find a new plan. Two: December seventh is the ordinary deadline, but non-renewal adds a second window that closes at the end of February. Three: join nothing, and you land in Original Medicare. Four: Original Medicare has no drug plan, and sixty-three days in a row without drug coverage can start a penalty. Five: a merged plan is not a non-renewal.",
# 16 CTA + disclaimer
"If this helped, send it to someone with an Advantage plan, and tell me in the comments which date surprised you. One last thing: this video is general information, not insurance advice. Rules and plans differ by plan and by state, so confirm with Medicare or your plan before you act. This channel is not affiliated with Medicare or any government agency.",
]
J = {str(i + 1): b for i, b in enumerate(B)}
json.dump({'B': J}, open('code/blk.json', 'w'), indent=0)
bad = 0
for i, b in enumerate(B, 1):
    flag = ''
    if len(b) > 500: flag += ' >500'; bad += 1
    if re.search(r'\d', b): flag += ' CIFRE'; bad += 1
    print(i, len(b), len(b.split()), flag)
print('TOT', sum(len(b) for b in B), sum(len(b.split()) for b in B), 'min a 145wpm ~', round(sum(len(b.split()) for b in B) / 145, 1))
W = [(i + 1, re.findall(r"[a-z']+", b.lower())) for i, b in enumerate(B)]
seen = collections.defaultdict(set)
for i, w in W:
    for k in range(len(w) - 4): seen[tuple(w[k:k + 5])].add(i)
for k, v in seen.items():
    if len(v) > 1: print('RIPETUTA', ' '.join(k), sorted(v))
print('PROBLEMI', bad)
