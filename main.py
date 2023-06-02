"""
Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.

||| Test this with: https://markdownlivepreview.com/ |||
"""

# =====

VOTE_OPTIONS = """
## Voting Options

YES: Agree to proceed with increasing the global minimum fee.

NO: Disagree with this increase of the global minimum fee.

NO WITH VETO: Disagree with the increase and want depositors penalized.

ABSTAIN: Decline to give an opinion on this increase of gas minimum fees.

"""

proposal_text = f"""
# Increase Minimum Gas Prices

[Commonwealth thread](https://commonwealth.im/juno/discussion/11088-param-change-increase-gas-prices)

With the previous v14 Juno upgrade, Fees are now controlled through governance.

This proposes we multiply the current gas rates by x3 for ATOM and 30x for JUNO due to current market prices.

*(A slight premium is added to ATOM since JUNO is the native currency of this network.)*

- Current Gas: 0.0025ujuno,0.001uatom
- New Gas:     0.0750ujuno,0.003uatom

---

## Reasons

- Juno's cost per transaction is extremely cheap relative to network activity. The average cost of a transaction with default gas (683,665) is just $0.00146 USD.
- This increases developers' fee-share revenue 30x. However, contract usage premium will still make up a larger portion of income.

## Notes

- IBC packet relaying cost will remain at 0 costs for relayers & IBC transfers.
- This will break scripts & MEV bots which have the old gas prices set.
- Keplr, Leap, and Cosmostation will require an update to their configs for Juno's gas prices.
- uatom is channel-1 ibc/C4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9
- You can verify current fees with `junod q globalfee minimum-gas-prices --node https://https://rpc.juno.strange.love:443`

---

## Technical Analysis

- [Indexer/Script used](https://github.com/Reecepbcups/cosmos-indexer/blob/main/scripts/get_all_gas_cost.py). Cut off was block 7,990,650
- [Weekly Tx Fees since Genesis](https://gist.github.com/Reecepbcups/a300c9973bec1de595eb371f9ddc2dd0)

### Last ~5 million Txs

- Total Txs: 4,998,636
- Total Gas Spent = 3,417,396,545,806
- Average gas usage per Tx: 683,665
- Total ujuno fees paid: 18,520,786,312 = 18,520 $JUNO
- Average Fees per Tx: 3,705ujuno

### ATOM $10.57

```
- Average Gas:  683,665
- Current Gas:  0.001uatom * 683,665 = 683.665uatom = 0.000683665ATOM * $10.57 = $0.0072 per Tx
- New Proposal: x3 = gas price of 0.003uatom 
- Fees Per Tx: 2050.995uatom = 0.002050995atom = $0.0217 per Tx
```

### JUNO $0.3947

```
- Average Gas:  683,665
- Current Gas: 0.0025ujuno * 683,665 = 1709uatom = 0.001709JUNO*$0.3947 = $0.0006745423
- New Proposal: x30 = gas price 0.075ujuno 
- Fees Per Tx: 51,274ujuno = 0.0512juno = $0.0202 per Tx
```

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
