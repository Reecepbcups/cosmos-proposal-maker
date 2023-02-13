proposal_text = """
# Juno v12 Upgrade Proposal

To reduce spamming in the Juno governance system, we propose requiring a 20% deposit (200 JUNO) on proposal creation. This will ensure that only quality proposals are submitted and deter malicious governance spam. Should you wish to make a proposal, but don't have 200 Juno, you can reach out to a member of the core team or Sub-DAOs for assistance. The minimum deposit is meant to deter spam, not participation!

Tag v12.0.0-beta.1 has been tested on our testnet, uni-6, and will be finalized as v12.0.0 if this proposal passes.

**NOTE** This subsequently renames the previous [v12 upgrade to v13 from our medium blog post](https://medium.com/@reecepbcups/juno-v12-update-4bab64640a62)

## Voting Options

YES: Agree to proceed with the Juno v12 upgrade and stop governance spam with the deposit requirement.
NO: Disagree with the v12 upgrade and the deposit requirement.
NO WITH VETO: Disagree with the upgrade and want depositors penalized.
ABSTAIN: Decline to give an opinion on the upgrade.

"""

# replace res new lines to the \n character
res = proposal_text.replace("\n", "\\n")
res = res.replace("'", "\\'")
res = res.replace('"', '\\"')
print("=" * 20)

if res.startswith("\\n"):
    res = res[2:]
if res.endswith("\\n"):
    res = res[:-2]

print(res)
