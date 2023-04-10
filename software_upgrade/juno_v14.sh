# JUNOD_NODE="http://localhost:26657"
# KEY="juno1"
# KEYRING="test"
# CHAIN_ID="local-1"

# TESTNET
# JUNOD_NODE="https://uni-rpc.reece.sh:443"
# KEY="reece"
# KEYRING="os"
# CHAIN_ID="uni-6"
# DENOM="ujunox"
# UPGRADE_HEIGHT="770462"
# DEPOSIT="500000000$DENOM" # 500 JUNO

# MAINNET
JUNOD_NODE="https://rpc.juno.strange.love:443"
KEY="reece"
KEYRING="os"
CHAIN_ID="juno-1"
DENOM="ujuno"
DEPOSIT="200000000$DENOM" # 200 JUNO
UPGRADE_HEIGHT="7875721"  # https://www.mintscan.io/juno/blocks/7875721 ( Mon Apr 17 2023 11:44:53 GMT-0500 )

# Info
UPGRADE_NAME="v14" # upgradehandler
FEES="50000$DENOM" # 0.05 JUNO


junod tx gov submit-proposal software-upgrade $UPGRADE_NAME \
    --title "Juno Upgrade: Aurora v14" \
    --description "# Juno Aurora Upgrade (v14)\n\n[Juno Medium v14 Article](https://medium.com/@JunoNetwork/jun%C3%B8-aurora-ac67a8143e22)\n\nThis upgrade brings the following major changes to Juno Network:\n- x/GlobalFee Module\n- x/IBC-Hooks Module\n- 0 Fee IBC Relaying\n- Stargate Staking Queries\n- Tokenfactory: ForceTransfer, MintTo, and BurnFrom (admin only)\n- x/wasmd 0.31\n- wasmvm 1.2.1\n- Skip's mev CometBFT by default\n\n## x/GlobalFee Module\n\n[Signaling proposal from December 13th, 2022: PASSED](https://www.mintscan.io/juno/proposals/68)\n\nCurrently on cosmos based chains, the validators are fully in control of the network fees. With this new module, a minimum gas fee is set by governance to set the gas floor.\n\nAt the upgrade, gas fees are set to our [setup documentation gas prices default](https://docs.junonetwork.io/validators/joining-mainnet#set-minimum-gas-prices):\n- 0.0025ujuno\n- 0.001uatom (ibc/C4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9)\n\nAt any time, governance can increase these fees across the network to help deliver more for developers (through feeshare) and stakers. It can also add new tokens to be accepted as fees, such as OSMO and/or USDC in the future.\nIf an transaction attack occurs on Juno, validators are still able to raise their fees ABOVE the minimum gas fee to protect the network as needed.\n\nThe only exception to this are bypassed messages for IBC relaying and transfers. These messages are exempt from the minimum gas fee within reasonable limits. For this to work, validators **must** set their fees to be: '0ujuno,0ibc/C4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9' in their app.toml. No other denoms can be accepted UNLESS governance passes a proposal to do so.\n\n## x/IBCHooks Module\n\nThis [module from the osmosis team](https://github.com/osmosis-labs/osmosis/tree/main/x/ibc-hooks) allows for token transfers (of the [ICS-20 spec](https://github.com/cosmos/ibc/tree/main/spec/app/ics-020-fungible-token-transfer) ) to call contracts cross chain. The primary importantance of this is allowing cross chain swaps. \n\n## x/wasmd 0.31 & wasmv 1.2.1\n\n[Wasmd 0.31 Confio Article](https://medium.com/cosmwasm/wasmd-v0-31-0-released-a2e2ed440148)\n[wasmvm 1.2.1 Confio Article](https://medium.com/cosmwasm/cosmwasm-1-2-5f10f4f653ea)\n\nThe main feature from this update which many development teams have requested is instantiate2 to replicate a contract with predictable addresses. You can find an example of this with the [contract example](https://github.com/CosmWasm/cosmwasm/tree/v1.2.1/contracts/virus). Some other notable improvements include:\n- Governance based weighted votes\n- new queries from wasmvm 1.2 (add the cosmwasm_1_2 feature in your contract toml)\n- Uint128/Decimal multiplication\n- A new 'Never' type\n\n## New Token Factory Methods\n\nFrom the previous upgrade, v13, we added the x/TokenFactory module to deliver a better UX for developers and users alike. As the admin of a token denomination you can now Force transfer tokens between accounts, Mint directly to an account, and burn from another account. In the future we will also add support for disabling the sending of tokens, and only allowing minting/burning for specific application needs.\n\n## Stargate Staking Queries\n\nContracts can now query the chain for an accounts: Delegation, Redelegations, and Unbonding information.\n\n## Skip MEV by default\n\nWith the passing of [Juno proposal 275](https://www.mintscan.io/juno/proposals/275), Skip's MEV CometBFT consensus is now used by default.\n\n## Command Line improvements\n\nYou can now specify the following configurations for any transaction commands you run:\n- Gas\n- Gas Prices\n- Gas Adjustment\n- Fees\n- Fee-Account\n- Note (memo)\n\nSet these with **junod config fees 5000ujuno** or **junod config gas-prices 0.0025ujuno**.\n\n---\n\n\n## Voting Options\n\nYES: Agree to proceed with Juno v14 network upgrade.\n\nNO: Disagree with the Juno v14 network upgrade.\n\nNO WITH VETO: Disagree with the Juno v14 network upgrade and want depositors penalized.\n\nABSTAIN: Decline to give an opinion on the Juno v14 network upgrade.\n\n" \
    --upgrade-info='{"binaries":{"linux/amd64":"https://github.com/CosmosContracts/juno/releases/download/v14.0.0/junod"}}' \
    --deposit=$DEPOSIT --upgrade-height="$UPGRADE_HEIGHT" --from=$KEY --keyring-backend=$KEYRING --chain-id=$CHAIN_ID --broadcast-mode=block --node $JUNOD_NODE --fees $FEES --gas=2000000