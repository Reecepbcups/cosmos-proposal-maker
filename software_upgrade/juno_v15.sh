# JUNOD_NODE="http://localhost:26657"
# KEY="juno1"
# KEYRING="test"
# CHAIN_ID="local-1"

# Run this on the testnet node itself.
# JUNOD_NODE="https://uni-rpc.reece.sh:443"
# KEY="reece"
# KEYRING="os"
# CHAIN_ID="uni-6"
# DENOM="ujunox"
# UPGRADE_HEIGHT="1619811"
# DEPOSIT="500000000$DENOM" # 500 JUNO

# MAINNET
JUNOD_NODE="https://rpc.juno.strange.love:443"
KEY="reece"
KEYRING="os"
CHAIN_ID="juno-1"
DENOM="ujuno"
DEPOSIT="200000000$DENOM" # 200 JUNO
UPGRADE_HEIGHT="8577241"  # https://www.mintscan.io/juno/blocks/8577241 ( Mon Apr 17 2023 11:44:53 GMT-0500 )

# Info
UPGRADE_NAME="v15" # upgradehandler
FEES="50000$DENOM" # 0.05 JUNO


junod tx gov submit-proposal software-upgrade $UPGRADE_NAME \
    --title "Juno Upgrade: $UPGRADE_NAME" \
    --description "# Juno TokenFactory Upgrade (v15)\n\nThis upgrade brings the following major changes to Juno Network:\n- New TokenFactory DenomCreationGasConsume parameter (2 million gas consumption to create a new token)\n- Cleanup for the next release (SDK v47)\n\nThis change is required for DeFi contract developers for a simpler UX when using the tokenfactory in their contracts.\n\n---\n\n\n## Voting Options\n\nYES: Agree to proceed with Juno v15 network upgrade.\n\nNO: Disagree with the Juno v15 network upgrade.\n\nNO WITH VETO: Disagree with the Juno v15 network upgrade and want depositors penalized.\n\nABSTAIN: Decline to give an opinion on the Juno v15 network upgrade.\n\n" \
    --upgrade-info='{"binaries":{"linux/amd64":"https://github.com/CosmosContracts/juno/releases/download/v15.0.0/junod"}}' \
    --deposit=$DEPOSIT --upgrade-height="$UPGRADE_HEIGHT" --from=$KEY --keyring-backend=$KEYRING --chain-id=$CHAIN_ID --broadcast-mode=block --node $JUNOD_NODE --fees $FEES --gas=2000000