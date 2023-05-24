"""
A copy from the main.py so I don't have to change it all the time

Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.

||| Test this with: https://markdownlivepreview.com/ |||
"""

# =====

UPGRADE_NAME = "v15"
UPGRADE_HUMAN_NAME = "TokenFactory"

VOTE_OPTIONS = f"""
## Voting Options

YES: Agree to proceed with Juno {UPGRADE_NAME} network upgrade.

NO: Disagree with the Juno {UPGRADE_NAME} network upgrade.

NO WITH VETO: Disagree with the Juno {UPGRADE_NAME} network upgrade and want depositors penalized.

ABSTAIN: Decline to give an opinion on the Juno {UPGRADE_NAME} network upgrade.

"""

# [Juno Medium {UPGRADE_NAME} Article](https://medium.com/@JunoNetwork/jun%C3%B8-aurora-ac67a8143e22)

proposal_text = f"""
# Juno {UPGRADE_HUMAN_NAME} Upgrade ({UPGRADE_NAME})

This upgrade brings the following major changes to Juno Network:
- New TokenFactory DenomCreationGasConsume parameter

This change is required for DeFi contract developers for a simpler UX when using the tokenfactory. Specifically, this enables protocols such as ICS-999 to be launched on Juno Network.

---

{VOTE_OPTIONS}
"""

# replace res new lines to the \n character
res = proposal_text.replace("\n", "\\n")
# res = res.replace("'", "\\'") # I do not think we need to do this? does this break text props?
res = res.replace("’", "'")  # when you copy paste from the web
res = res.replace('"', '\\"')
res = res.replace("`", "'")  # can not do ` or else linux tries to run it in the CMD
res = res.replace("    ", "\\t")  # tabs
print("=" * 20)

if res.startswith("\\n"):
    res = res[2:]
if res.endswith("\\n"):
    res = res[:-2]

print(res)
