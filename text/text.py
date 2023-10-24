# flake8: noqa
"""
Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.
"""

# =====

VOTE_OPTIONS = """
## Voting Options

**YES**: Agree to a future upgrade to set all validators max change rate to be no more than 5%.

**NO**: Disagree to a future upgrade to set all validators max change rate to be no more than 5%.

**NO WITH VETO**: Disagree with the proposal and want depositors penalized.

**ABSTAIN**: Decline to give an opinion on this proposal.

"""

proposal_text = f"""
# Set Validator Max Commission Change Rate To 5%

[Commonwealth Thread](https://commonwealth.im/juno/discussion/12035-set-validator-max-commission-change-rate-up-to-5)

In reference to the recent event on Cosmos Hub, where a validator has increased their commission rate by 99.35% in a single transaction, a safe hard limit on max commission change rate should be set for all validators as good practice to protect delegators.

This proposal is signaling a future upgrade to set all validators max change rate (within a 24 hour period) to be no more than 5% if currently set above.

This would not affect the minimum nor maximum commission rate limits, rather ensures that network validators would not be able to increase their commission rate by more than 5% within 24 hours.

*(This means for a validator to go from 5% to 100% commission, it would take 19 days.)*

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
