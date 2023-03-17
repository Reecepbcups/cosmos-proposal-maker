"""
Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.
"""

# =====

VOTE_OPTIONS = """
## Voting Options

YES: Agree to proceed with increasing block gas to 100 million (from 10 million).

NO: Disagree with the increase of block gas to 100 million.

NO WITH VETO: Disagree with the increase of block gas to 100 million and want depositors penalized.

ABSTAIN: Decline to give an opinion on the increase of block gas.

"""

proposal_text = f"""
# Increase Per Block Gas

[Commonwealth Discussion](https://commonwealth.im/juno/discussion/10396-increase-maximum-per-block-gas-to-100-million)

Previously in [Juno proposal 6](https://www.mintscan.io/juno/proposals/6), the team lowered per block gas to 10 million *(from 100 million)* to stop potential attacks against the network. Since then, we have tested on our testnet (Uni-6) and have confirmed these attacks are no longer possible after the v13 upgrade. With this, the chain is now safe to increase back to 100 million gas per block.

This has been a major pain point for many projects including NFTs (minting), DeFi, CW20 migrations, and oracle data submissions. With this change, it allows more complex logic to be built on Juno and provide a better user experience, as well as increasing the number of possible transactions per block.

**NOTE** The transaction size limit will remain at 22,020,096 bytes per block (22Mb). We have not had any need or requests to alter this.


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
