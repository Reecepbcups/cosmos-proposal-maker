"""
Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.
"""

# =====

VOTE_OPTIONS = """
## Voting Options

YES: Agree to proceed with Juno v13 network upgrade.
NO: Disagree with the Juno v13 network upgrade.
NO WITH VETO: Disagree with the Juno v13 network upgrade and want depositors penalized.
ABSTAIN: Decline to give an opinion on the Juno v13 network upgrade.

"""

proposal_text = f"""
# Juno v13 Upgrade

[Original Medium Article Post](https://medium.com/@reecepbcups/juno-v12-update-4bab64640a62)

This network upgrade brings the following changes to Juno Network:

- x/FeeShare Module
- x/TokenFactory Module
- CosmWasm v0.30
- IBC v4
- Packet Forward Middleware

Due to deterministic issues with the oracle module on our testnet, it has been pushed to v14 or later.

---

## x/FeeShare Module

This module's addition was passed in [Juno Proposal 51](https://www.mintscan.io/juno/proposals/51)

If you're a smart contract developer on Juno, you can now earn a cut of all gas fees generated on your contract. Initially this is set to 50% of all gas fees which interact with your contract directly. 
Governance at any time can change this percentage to any value between 0% and 100%, add new tokens to be paid in (ex; USDC, OSMO, etc), or toggle this feature entirely.
This module helps incentivize developers to build on Juno Network and bring new business models that are not directly DeFi related.

## x/TokenFactory Module

This module allows anyone to create a native token on Juno Network. This drastically increases the UX and UI of the networks utility tokens. As a developer, it also removes the need to support both native assets and CW20 in your contracts.
DAOs/SubDAOs can control a contract which mints tokens for other business logic in your contracts through our [TokenFactory Middleware Contract](https://github.com/CosmosContracts/tokenfactory-contracts).

## CosmWasm v0.30

You can read all of the great features in x/wasmd v0.30.0 in Confio's [medium article here](https://medium.com/cosmwasm/wasmd-0-30-released-8e9932929238).

## Packet Forward Middleware

This new middleware allows for the forwarding of IBC packets through Juno's infrastructure to final destination chains. As cosmos zones expand, the need for multi-hop transactions will increase for scaling. 
This new module allows for Juno to be a "relay" chain for other zones. Where a newly launched chain can just focus on relaying to and from Juno, and in return can route these packets to all the zones Juno is connected too. 
With this, public relayers will be able to earn fees in the future with these transactions along with the [ICS29 IBCFees module added in this update](https://github.com/cosmos/ibc-go/tree/main/docs/middleware/ics29-fee).

## Other Changes

- Complete overhaul of the main app for easier upgradeability
- ICA Host and Controller
- Allow all ICA messages
- Latest IAVL, Tendermint, and Cosmos SDK (v0.45)
- `junod debug bech32-convert`
- `junod debug export-derive-balances`
- `junod debug forceprune`
- `junod reset [app|wasm]` directory files


{VOTE_OPTIONS}
"""

# replace res new lines to the \n character
res = proposal_text.replace("\n", "\\n")
# res = res.replace("'", "\\'") # I do not think we need to do this? does this break text props?
res = res.replace("’", "'")  # when you copy paste from the web
res = res.replace('"', '\\"')
res = res.replace("    ", "\\t")  # tabs
print("=" * 20)

if res.startswith("\\n"):
    res = res[2:]
if res.endswith("\\n"):
    res = res[:-2]

print(res)
