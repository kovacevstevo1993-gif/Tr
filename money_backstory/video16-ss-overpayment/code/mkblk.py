import json, re, collections
B = [
# 1 gancio
"A letter arrives from Social Security. It says you were overpaid, and it wants the money back. If you do not answer, the agency can start keeping half of every monthly check, automatically, until the debt is gone. Half. But inside the official rules are four moves that can stop it, shrink it, or erase it. Two of them freeze the deductions the day you use them. One has no deadline at all. And by the end, you will know which move fits your letter.",
# 2 iscrizione + Carol
"This is The Money Backstory, where we turn official rules into real numbers. If that helps, subscribe now and tap the bell, so the next breakdown finds you. Now, meet Carol, sixty-six. Her Social Security check is two thousand one hundred dollars a month. Then comes the envelope. It says she was paid six hundred dollars too much, every month, for fifteen months. The total she owes: nine thousand dollars.",
# 3 la lettera
"First, what is inside that envelope. The Social Security Administration's own manual says the notice must list the total, what you were paid, what you should have been paid, why the amount was different, and the months involved. It must also tell you three rights: to ask for a reconsideration, to ask for a waiver, and to ask for a different repayment rate. Read every line. One of them matters more than all the others, and it is about a number of days.",
# 4 il 50%
"Here is the danger. The letter asks for a full and immediate refund. If the money does not come, the agency plans to withhold part of your monthly benefit. For notices sent on or after April twenty-fifth, twenty twenty-five, the default is up to fifty percent. For Carol, that is about one thousand fifty dollars held back from each check, and the nine thousand is gone in about nine months. No phone call from Carol is needed to start it. Hold on to that April date. It matters later.",
# 5 i trenta giorni
"Now, the number of days. The manual says that if you respond within thirty days of the date on the notice, the agency must stop collection activity while it looks at your request. The notice itself sets a refund date at least thirty days away, and the agency says it does not begin withholding right away, so people have time to fight it. Time only helps the people who use it. So here are the four moves, in the order they matter.",
# 6 mossa 1
"Move number one is to check whether the debt is even correct. If you disagree with the fact or the amount of the overpayment, you can ask for a reconsideration, and the deadline is sixty days from the date of the notice. You can start by calling the national number, one, eight hundred, seven seven two, one two one three, visiting a field office, or writing. The manual tells staff to record a specific reason, like I did not work, or I did not receive a pension, not just I do not agree.",
# 7 trappola audizione vs rinuncia
"While the agency decides your reconsideration, it stops collecting. But watch what happens if it does not fully reverse the debt. The notice that follows says recovery will begin, or resume, in sixty days, even if you then ask for a hearing. A hearing request does not pause the deductions. A waiver request does. The same notice says recovery will not begin, or will stop, until the agency makes a final decision on the waiver. Which brings us to move number two.",
# 8 mossa 2 waiver basi
"Move number two is the waiver, and it has no deadline. The manual says you may ask at any time: when the notice arrives, at the same time as your appeal, after the deductions have started, even after the whole debt is collected, and even after an earlier request was denied. If the waiver is approved, the agency may refund what it already withheld. You ask on Form S S A six thirty-two B K, by mail, by fax, at the office, or by uploading it in your my Social Security account.",
# 9 primo cancello: colpa
"But a waiver has two gates, and the first one is fault. The agency can find you at fault only with evidence that you gave information you knew was wrong, failed to give information you knew mattered, or accepted a payment you knew was incorrect. Without that evidence, you are not at fault. The manual also presumes you are not at fault if you reported a change on time, if payments kept coming after you reported it, or if the agency itself made an error in computing your benefit.",
# 10 secondo cancello: tre porte
"The second gate has three doors, and you need only one. Door one is small debts. If the original overpayment is two thousand dollars or less and fault is not an issue, the agency waives it, and you can ask by phone. Door two is hardship. Your income cannot exceed your ordinary living costs by more than two hundred fifty dollars a month, and your resources must be six thousand dollars or less, or ten thousand with a spouse or dependent. Door three is about fairness.",
# 11 porta 3 + Carol + conferenza
"The manual calls the third door against equity and good conscience. It applies when you relied on a payment that was not due, and your finances changed for the worse. Back to Carol. If the agency made the error in computing her benefit, the manual presumes she is not at fault, so the first gate is open. Her nine thousand dollars is above the small-debt line, so the agency must weigh hardship or fairness. And if the answer might be no, there is a move four. First, move three.",
# 12 mossa 3 tasso
"Move number three is shrinking the payment. The notice itself says a different rate of withholding is available when the agency proposes fifty percent, so you can ask for less. Staff first try for a rate that finishes within twelve months, never below ten dollars a month. For up to sixty months, the agency asks about your income, expenses and resources. Carol asks for three hundred dollars a month, which finishes in thirty months. Longer than that needs the longer form, number six thirty-four.",
# 14 mossa 4 conferenza
"Move number four is the second chance. If the agency cannot approve your waiver after its first review, it must offer you a file review and a personal conference before any denial. At the file review, you can read the evidence in your own claims file. At the conference, by phone, by video, or in the office, you can testify, bring documents and witnesses, and have a representative speak for you. And a waiver decision can still be appealed, with a new look at the facts.",
# 15 se non fai niente
"What happens if you do nothing? The deductions begin on their own, up to fifty percent of the check. If you are no longer receiving benefits, the agency can keep your federal tax refund, and it can report an unpaid debt to the credit bureaus, which can lead to a denied loan. One exception covers every move: when the agency finds fraud or similar fault, it will not approve a lower rate or a waiver. For everyone else, even the smallest move beats silence. And now, the twist about that April date.",
# 16 vecchie lettere + SSI
"Letters dated before that day in April keep the old ten percent rate, according to the agency's emergency message, unless you get a new overpayment. If you do, every balance you owe moves to fifty percent once the new withholding begins. One more split: for S S I, the supplemental program for people with low income, the rate stays at ten percent. Everything in this video is about Title Two benefits, which are retirement, survivors, and disability.",
# 17 prevenzione + Carol piano
"How do you avoid the letter in the first place? The manual's own presumptions point the way: report changes on time, and keep proof of when you did it, the date, the name of the person, and a copy of what you sent. A report you made, or tried to make, counts in your favor on the fault question. Carol's plan: answer inside thirty days, ask for a waiver, request a smaller payment while she waits, and keep every paper in one folder.",
# 18 riepilogo + CTA + disclaimer
"To sum up. One: check the debt, with a reconsideration inside sixty days. Two: the waiver, any time. Three: a smaller monthly rate. Four: the personal conference, if the waiver is denied. If this helped, send it to someone who gets Social Security mail, and tell me in the comments: did your letter match what we described? This is general information, not advice. Rules and amounts change, so confirm with the Social Security Administration. This channel is not affiliated with it.",
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
