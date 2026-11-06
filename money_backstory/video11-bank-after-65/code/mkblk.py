import json
B = [
"Two hundred fifty thousand dollars. Most people over sixty-five have heard that number about their bank. But it is not a limit on how much money you have. It is a limit on how your money is set up, and there are five rules behind it that most seniors never check.",
"Meet Frank and Mary. Frank is sixty-seven, and he keeps everything at one bank in town: three hundred eighty thousand dollars from selling his house. Mary is seventy, a widow, and her son is on her checking account so he can help pay the bills.",
"Every number in this video comes from official sources: the F D I C, the Social Security Administration, the Consumer Financial Protection Bureau and Medicare. Let's start with the rule behind the famous number.",
"Rule number one. The F D I C insures at least two hundred fifty thousand dollars per depositor, per insured bank, for each ownership category. Credit unions have the same two hundred fifty thousand dollar coverage through the N C U A.",
"The F D I C says that since it began in nineteen thirty-four, no depositor has ever lost a penny of insured deposits. The key word is insured. Money above the limit, in the same name and the same category, is not covered if the bank fails.",
"So look at Frank. Three hundred eighty thousand dollars, one bank, one name, one single account. Two hundred fifty thousand is covered. The other one hundred thirty thousand dollars is not. If that bank failed, that part of his money would be at risk.",
"That is why the real answer is not one magic number. How much you can safely keep in one bank depends on the names on the account and the type of account. Which brings us to rule number two.",
"Rule number two: each ownership category is insured separately. A single account in your name is one category. A joint account is another. Certain retirement accounts, like I R A deposits at a bank, are a third.",
"With a joint account, each co-owner is insured up to two hundred fifty thousand dollars for their share. So a married couple with a joint account at one bank can have up to five hundred thousand dollars covered, on top of their single accounts.",
"Then there are trust accounts, and that includes payable on death accounts. The coverage is two hundred fifty thousand dollars for each eligible beneficiary, up to one point two five million dollars per owner, per bank, once you name five or more.",
"Frank has two grown daughters. He named them as payable on death beneficiaries on his account. That moved his coverage at the same bank from two hundred fifty thousand to five hundred thousand dollars. Same bank, same money, and now all of it is covered.",
"Before you change anything, the F D I C has a free tool called Edie, the Electronic Deposit Insurance Estimator. You enter your accounts, and it shows you what is insured and what is not.",
"Now the warning that comes with joint accounts. The Consumer Financial Protection Bureau says that in most cases, either owner on a joint checking account can withdraw the money, and can even close the account.",
"That was Mary's situation. She added her son only so he could pay her bills. But a joint owner can take money for their own use, and the account can be exposed to the joint owner's creditors. That is the risk the C F P B warns about.",
"The C F P B points to other options: a convenience signer, who can help pay bills but does not own the money, a carefully written power of attorney, and alerts or withdrawal limits on the account.",
"Rule number three: not everything you buy at a bank is insured. The F D I C does not cover stocks, bonds, mutual funds, annuities, life insurance, crypto, or what you keep in a safe deposit box, even if you bought it in the same building.",
"And watch the apps. The F D I C says nonbank companies themselves are never F D I C insured. If an app tells you your money is insured, ask which bank holds it, and check that bank on the F D I C's free Bank Find tool.",
"Rule number four is about your Social Security check. If a debt collector gets a court order against your account, your bank must look back two months. Federal benefits that were direct deposited in those two months are protected and stay in your account.",
"That covers Social Security, S S I, veterans benefits and federal retirement. But here is the catch. If you get a paper check and deposit it yourself, the bank does not have to protect those two months. Your whole balance could be frozen until you prove where the money came from.",
"And this protection has limits. Social Security can still be taken for some debts you owe the government, like back taxes or federal student loans, and for child or spousal support. S S I is protected even from those.",
"Rule number five is the limit nobody talks about, and it is much lower. If you get Supplemental Security Income, your countable resources cannot be more than two thousand dollars, or three thousand dollars for a couple.",
"Your home and one car do not count. But money in the bank does. One large deposit, or a gift from family sitting in your checking account, can push you over that line and put your S S I payment at risk.",
"The same idea applies to the Medicare Savings Programs, which can help pay your Part B premium. In twenty twenty-six, the federal resource limit is nine thousand nine hundred fifty dollars for one person, and fourteen thousand nine hundred ten for a married couple.",
"Medicare also says some states use higher limits, or do not count certain resources. So if your savings are close to that line, check with your state before you decide you do not qualify.",
"So, five rules. One: two hundred fifty thousand dollars per bank, per owner, per category. Two: categories and beneficiaries can raise your coverage. Three: investments and apps are not insured deposits. Four: direct deposit protects two months of benefits. Five: help programs have much lower limits.",
"Three things to do this week. First, add up what you have at each bank, by name and by type of account. Second, put those numbers into the F D I C's Edie tool. Third, check who is on each account, and whether your beneficiaries are named.",
"Frank named his daughters as beneficiaries, and now every dollar at his bank is covered. Mary changed her son from owner to helper, and turned on alerts for every withdrawal. Same money, a much safer setup.",
"If this helped, send it to one person over sixty-five, especially someone who keeps everything at one bank. And tell me in the comments: do you use one bank, or more than one?",
"Rules, amounts and limits change and differ by state and by bank. Always confirm with the official source, like f d i c dot gov, before you rely on them. This is general information, not financial advice. Subscribe to The Money Backstory, so you don't miss the next one.",
]
json.dump({'B': {str(i + 1): t for i, t in enumerate(B)}}, open('code/blk.json', 'w'), indent=0)
md = ['# VIDEO 11 - "Never Keep More Than This in One Bank Account After 65 — 5 Rules Most Seniors Miss"',
      'Voce: gemini-2.5-flash-preview-tts, Fenrir, senza istruzioni (stessa dei video 9 e 10). Fonti: FONTI-VERIFICATE.md.', '']
for i, t in enumerate(B): md += [f'**BLOCCO {i+1}**', t, '']
open('copione-video11.md', 'w').write('\n'.join(md))
print(len(B), 'blocchi', sum(len(t.split()) for t in B), 'parole')
