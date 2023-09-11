# JUNOD_NODE="http://localhost:26657"
# KEY="juno1"
# KEYRING="test"
# CHAIN_ID="local-1"

# Run this on the testnet node itself.
# JUNOD_NODE="https://uni-rpc.reece.sh:443"
# KEY="validator"
# KEYRING="os"
# CHAIN_ID="uni-6"
# DENOM="ujunox"
# UPGRADE_HEIGHT="3040483"
# DEPOSIT="500000000$DENOM" # 500 JUNOX

# MAINNET
JUNOD_NODE="https://rpc.juno.strange.love:443"
KEY="reece-main"
KEYRING="os"
CHAIN_ID="juno-1"
DENOM="ujuno"
DEPOSIT="1000000000$DENOM" # 1,000 JUNO
UPGRADE_HEIGHT="10078449"  # https://www.mintscan.io/juno/blocks/10078449

# Info
UPGRADE_NAME="v17" # upgradehandler
UPGRADE_HUMAN_NAME="Vesta"
FEES="500000$DENOM" # 0.5 


TITLE="Juno Upgrade: $UPGRADE_HUMAN_NAME ($UPGRADE_NAME)"
# TODO: This has a metadata problem???
# DESC="# Juno Vesta Upgrade (v17)\n\nThis upgrade brings the following major changes to Juno Network:\n- x/drip module (single block stake weighted airdrop for all delegators).\n- x/clock module (Allow smart contracts to 'tick' every end block)\n- 3 second block times (down from 6 seconds).\n\nOther:\n- DAODAO can now natively register contracts with FeeShare if it is the admin or creator.\n- We now bypass IBC transactions up to 2M gas (from 1 million) due to the use of TFM with PFM & IBC Hooks.\n\n[Release Notes](https://github.com/CosmosContracts/juno/releases/tag/v17.0.0-alpha.1)\n\n[Full Change Log](https://github.com/CosmosContracts/juno/compare/v16.0.0...v17.0.0-alpha.1)\n\n---\n\n\n## Voting Options\n\nYES: Agree to proceed with the v17 network upgrade.\n\nNO: Disagree with the v17 network upgrade.\n\nNO WITH VETO: Disagree with the v17 network upgrade and want depositors penalized.\n\nABSTAIN: Decline to give an opinion on the v17 network upgrade.\n\n"
DESC="# Juno Vesta Upgrade (v17)\n\n[Release Notes](https://github.com/CosmosContracts/juno/releases/tag/v17.0.0)\n---\n\n## Voting Options\nYES: Agree to proceed with the v17 network upgrade.\nNO: Disagree with the v17 network upgrade."
UPGRADE_INFO='{"binaries":{"linux/amd64":"https://github.com/CosmosContracts/juno/releases/download/v17.0.0/junod"}}'

junod tx gov submit-legacy-proposal software-upgrade $UPGRADE_NAME --title="$TITLE" --description="$DESC" --deposit="$DEPOSIT" --upgrade-height="$UPGRADE_HEIGHT" --from=$KEY --keyring-backend=$KEYRING --chain-id=$CHAIN_ID --broadcast-mode=sync --node=$JUNOD_NODE --no-validate --upgrade-info=$UPGRADE_INFO --fees=$FEES --gas=2000000