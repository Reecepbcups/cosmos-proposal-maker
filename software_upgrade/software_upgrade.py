"""
A copy from the main.py so I don't have to change it all the time

Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.

||| Test this with: https://markdownlivepreview.com/ |||
"""

# =====

UPGRADE_NAME = "v14"
UPGRADE_HUMAN_NAME = "Aurora"

VOTE_OPTIONS = f"""
## Voting Options

YES: Agree to proceed with Juno {UPGRADE_NAME} network upgrade.

NO: Disagree with the Juno {UPGRADE_NAME} network upgrade.

NO WITH VETO: Disagree with the Juno {UPGRADE_NAME} network upgrade and want depositors penalized.

ABSTAIN: Decline to give an opinion on the Juno {UPGRADE_NAME} network upgrade.

"""

proposal_text = f"""
# Juno {UPGRADE_HUMAN_NAME} Upgrade ({UPGRADE_NAME})

[Juno Medium {UPGRADE_NAME} Article](https://medium.com/@JunoNetwork/jun%C3%B8-aurora-ac67a8143e22)

This upgrade brings the following major changes to Juno Network:
- x/GlobalFee Module
- x/IBC-Hooks Module
- 0 Fee IBC Relaying
- Stargate Staking Queries
- Tokenfactory: ForceTransfer, MintTo, and BurnFrom (admin only)
- x/wasmd 0.31
- wasmvm 1.2.1
- Skip's mev CometBFT by default

## x/GlobalFee Module

[Signaling proposal from December 13th, 2022: PASSED](https://www.mintscan.io/juno/proposals/68)

Currently on cosmos based chains, the validators are fully in control of the network fees. With this new module, a minimum gas fee is set by governance to set the gas floor.

At the upgrade, gas fees are set to our [setup documentation gas prices default](https://docs.junonetwork.io/validators/joining-mainnet#set-minimum-gas-prices):
- 0.0025ujuno
- 0.001uatom (ibc/C4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9)

At any time, governance can increase these fees across the network to help deliver more for developers (through feeshare) and stakers. It can also add new tokens to be accepted as fees, such as OSMO and/or USDC in the future.
If an transaction attack occurs on Juno, validators are still able to raise their fees ABOVE the minimum gas fee to protect the network as needed.

The only exception to this are bypassed messages for IBC relaying and transfers. These messages are exempt from the minimum gas fee within reasonable limits. For this to work, validators **must** set their fees to be: `0ujuno,0ibc/C4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9` in their app.toml. No other denoms can be accepted UNLESS governance passes a proposal to do so.

## x/IBCHooks Module

This [module from the osmosis team](https://github.com/osmosis-labs/osmosis/tree/main/x/ibc-hooks) allows for token transfers (of the [ICS-20 spec](https://github.com/cosmos/ibc/tree/main/spec/app/ics-020-fungible-token-transfer) ) to call contracts cross chain. The primary importantance of this is allowing cross chain swaps. 

## x/wasmd 0.31 & wasmv 1.2.1

[Wasmd 0.31 Confio Article](https://medium.com/cosmwasm/wasmd-v0-31-0-released-a2e2ed440148)
[wasmvm 1.2.1 Confio Article](https://medium.com/cosmwasm/cosmwasm-1-2-5f10f4f653ea)

The main feature from this update which many development teams have requested is instantiate2 to replicate a contract with predictable addresses. You can find an example of this with the [contract example](https://github.com/CosmWasm/cosmwasm/tree/v1.2.1/contracts/virus). Some other notable improvements include:
- Governance based weighted votes
- new queries from wasmvm 1.2 (add the cosmwasm_1_2 feature in your contract toml)
- Uint128/Decimal multiplication
- A new 'Never' type

## New Token Factory Methods

From the previous upgrade, v13, we added the x/TokenFactory module to deliver a better UX for developers and users alike. As the admin of a token denomination you can now Force transfer tokens between accounts, Mint directly to an account, and burn from another account. In the future we will also add support for disabling the sending of tokens, and only allowing minting/burning for specific application needs.

## Stargate Staking Queries

Contracts can now query the chain for an accounts: Delegation, Redelegations, and Unbonding information.

## Skip MEV by default

With the passing of [Juno proposal 275](https://www.mintscan.io/juno/proposals/275), Skip's MEV CometBFT consensus is now used by default.

## Command Line improvements

You can now specify the following configurations for any transaction commands you run:
- Gas
- Gas Prices
- Gas Adjustment
- Fees
- Fee-Account
- Note (memo)

Set these with **junod config fees 5000ujuno** or **junod config gas-prices 0.0025ujuno**.

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
