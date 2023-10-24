# flake8: noqa

"""
A copy from the main.py so I don't have to change it all the time

Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.

||| Test this with: https://markdownlivepreview.com/ |||
"""

# =====

UPGRADE_NAME = "v18"
UPGRADE_HUMAN_NAME = "Epona"

VOTE_OPTIONS = f"""
## Voting Options
YES: Agree to proceed with the {UPGRADE_NAME} network upgrade.
NO: Disagree with the {UPGRADE_NAME} network upgrade.

"""

# [Juno Medium {UPGRADE_NAME} Article](https://medium.com/@JunoNetwork/jun%C3%B8-aurora-ac67a8143e22)
# [{UPGRADE_HUMAN_NAME} Article](https://medium.com/@JunoNetwork/pioneering-continues-a-status-update-on-the-upcoming-upgrade-invictus-29ce631cf99f)

proposal_text = f"""
# Juno {UPGRADE_HUMAN_NAME} Upgrade ({UPGRADE_NAME})

[Release Notes](https://github.com/CosmosContracts/juno/releases/tag/v18.0.0)

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
