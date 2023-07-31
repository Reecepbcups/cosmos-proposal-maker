# JUNOD_NODE="http://localhost:26657"
# KEY="juno1"
# KEYRING="test"
# CHAIN_ID="local-1"

# Run this on the testnet node itself.
JUNOD_NODE="https://uni-rpc.reece.sh:443"
KEY="reece"
KEYRING="os"
CHAIN_ID="uni-6"
DENOM="ujunox"
UPGRADE_HEIGHT="2401803"
DEPOSIT="500000000$DENOM" # 500 JUNO

# MAINNET
# JUNOD_NODE="https://rpc.juno.strange.love:443"
# KEY="reece"
# KEYRING="os"
# CHAIN_ID="juno-1"
# DENOM="ujuno"
# DEPOSIT="200000000$DENOM" # 200 JUNO
# UPGRADE_HEIGHT="8577241"  # https://www.mintscan.io/juno/blocks/8577241 ( Mon Apr 17 2023 11:44:53 GMT-0500 )

# Info
UPGRADE_NAME="v16" # upgradehandler
FEES="50000$DENOM" # 0.05 JUNO


junod tx gov submit-proposal software-upgrade $UPGRADE_NAME \
    --title "Juno Upgrade: $UPGRADE_NAME" \
    --description "# Juno Invictus Upgrade (v16)\n\n[Invictus Article](https://medium.com/@JunoNetwork/pioneering-continues-a-status-update-on-the-upcoming-upgrade-invictus-29ce631cf99f)\n\nThis upgrade brings the following major changes to Juno Network:\n- Migrates Juno's entire codebase to SDK v47 & CometBFT v0.37\n- Adds Async Interchain Queries\n- Adds Skip's protocol-owned MEV builder (x/POB).\n- Adds x/NFT module.\n- Brings GlobalFee & TokenFactory into the core repository.\n- Governance-controlled smart contracts can now register for FeeShare.\n\nOther:\n- Migrates all params from deprecated x/params to standalone keepers.\n- 'DelegationRewards' stargate query now accessible\n- TokenAFactory denoms now follow x/bank denom specs (metadata)\n- Testing every module in the codebase (including upstream)\n- General cleanup\n\n[Release Notes](https://github.com/CosmosContracts/juno/releases/tag/v16.0.0)\n\n[Full Change Log](https://github.com/CosmosContracts/juno/compare/v15.0.0...v16.0.0)\n\n---\n\n\n## Voting Options\n\nYES: Agree to proceed with the v16 network upgrade.\n\nNO: Disagree with the v16 network upgrade.\n\nNO WITH VETO: Disagree with the v16 network upgrade and want depositors penalized.\n\nABSTAIN: Decline to give an opinion on the v16 network upgrade.\n\n" \
    --upgrade-info='{"binaries":{"linux/amd64":"https://github.com/CosmosContracts/juno/releases/download/v16.0.0/junod"}}' \
    --deposit=$DEPOSIT --upgrade-height="$UPGRADE_HEIGHT" --from=$KEY --keyring-backend=$KEYRING --chain-id=$CHAIN_ID --broadcast-mode=sync --node $JUNOD_NODE --fees $FEES --gas=2000000