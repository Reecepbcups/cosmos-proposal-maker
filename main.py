"""
Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.

||| Test this with: https://markdownlivepreview.com/ |||
"""

# =====

VOTE_OPTIONS = """
## Voting Options

YES: Agree to proceed with increasing the minimum deposit.

NO: Disagree with this increase of the minimum deposit.

NO WITH VETO: Disagree with the increase and want depositors penalized.

ABSTAIN: Decline to give an opinion on this increase of the minimum deposit.

"""

proposal_text = f"""
## Increase Juno's Deposit Minimum

[Commonwealth Thread](https://commonwealth.im/juno/discussion/11579-increase-governance-deposit-to-5000juno)

With the decline in JUNO's price the past few months, we have seen an uptick in scam proposals making it to voting period. With this, this proposal will update Juno's current governance deposit from 1000JUNO to 5000JUNO if passed.
Currently this includes: 296, 298, 299, 300, 301, 302, 303. All of these are used to phish for users wallet mnemonics and drain their personal funds. 

By increasing this, it increases the cost of the attack which makes it unprofitable to execute on.
The minimum deposit rate to enter deposit period will remain at the same at 20%, which would now be 1000 JUNO.

If you do not have enough Juno to make a proposal, you can reach out to a Core-1, Core-2, or SubDAO to help get your proposal live.


---

{VOTE_OPTIONS}
"""


# replace res new lines to the \n character
res = proposal_text.replace("\n", "\\n")

# This fixes it so code blocks work
res = res.replace("```", "_$$_;")

# res = res.replace("'", "\\'") # I do not think we need to do this? does this break text props?
res = res.replace("’", "'")  # when you copy paste from the web
res = res.replace('"', '\\"')
res = res.replace("`", "'")  # can not do ` or else linux tries to run it in the CMD
res = res.replace("    ", "\\t")  # tabs

# code blocks re-replacement
res = res.replace("_$$_;", "```")

print("=" * 20)

if res.startswith("\\n"):
    res = res[2:]
if res.endswith("\\n"):
    res = res[:-2]

print(res)
