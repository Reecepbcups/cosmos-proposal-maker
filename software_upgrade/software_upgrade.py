# flake8: noqa

"""
A copy from the main.py so I don't have to change it all the time

Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.

||| Test this with: https://markdownlivepreview.com/ |||
"""

# =====

UPGRADE_NAME = "v16"
UPGRADE_HUMAN_NAME = "Invictus"

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
- Migrates Juno's entire codebase to SDK v47 & CometBFT v0.37
- Adds Async Interchain Queries
- Adds Skip's protocol-owned MEV builder (x/POB).
- Adds x/NFT module.
- Brings GlobalFee & TokenFactory into the core repository.
- Governance-controlled smart contracts can now register for FeeShare.

Other:
- Migrates all params from deprecated x/params to standalone keepers.
- `DelegationRewards` stargate query now accessible
- TokenAFactory denoms now follow x/bank denom specs (metadata)
- Testing every module in the codebase (including upstream)
- General cleanup

[Release Notes](https://github.com/CosmosContracts/juno/releases/tag/v16.0.0)

[Full Change Log](https://github.com/CosmosContracts/juno/compare/v15.0.0...v16.0.0)

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
