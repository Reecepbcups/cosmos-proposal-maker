# flake8: noqa

"""
A copy from the main.py so I don't have to change it all the time

Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.

||| Test this with: https://markdownlivepreview.com/ |||
"""

# =====

UPGRADE_NAME = "v17"
UPGRADE_HUMAN_NAME = "Vesta"

VOTE_OPTIONS = f"""
## Voting Options

YES: Agree to proceed with the {UPGRADE_NAME} network upgrade.

NO: Disagree with the {UPGRADE_NAME} network upgrade.

NO WITH VETO: Disagree with the {UPGRADE_NAME} network upgrade and want depositors penalized.

ABSTAIN: Decline to give an opinion on the {UPGRADE_NAME} network upgrade.

"""

# [Juno Medium {UPGRADE_NAME} Article](https://medium.com/@JunoNetwork/jun%C3%B8-aurora-ac67a8143e22)

proposal_text = f"""
# Juno {UPGRADE_HUMAN_NAME} Upgrade ({UPGRADE_NAME})

[{UPGRADE_HUMAN_NAME} Article](https://medium.com/@JunoNetwork/pioneering-continues-a-status-update-on-the-upcoming-upgrade-invictus-29ce631cf99f)

This upgrade brings the following major changes to Juno Network:
- x/drip module (single block stake weighted airdrop for all delegators).
- x/clock module (Allow smart contracts to 'tick' every end block)
- 3 second block times (down from 6 seconds).

Other:
- DAODAO can now natively register contracts with FeeShare if it is the admin or creator.
- We now bypass IBC transactions up to 2M gas (from 1 million) due to the use of TFM with PFM & IBC Hooks.

[Release Notes](https://github.com/CosmosContracts/juno/releases/tag/v17.0.0-alpha.1)

[Full Change Log](https://github.com/CosmosContracts/juno/compare/v16.0.0...v17.0.0-alpha.1)

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
