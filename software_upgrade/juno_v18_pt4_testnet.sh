# JUNOD_NODE="http://localhost:26657"
# KEY="juno1"
# KEYRING="test"
# CHAIN_ID="local-1"

# Run this on the testnet node itself.
JUNOD_NODE="https://uni-rpc.reece.sh:443"
KEY="validator"
KEYRING="os"
CHAIN_ID="uni-6"
DENOM="ujunox"
UPGRADE_HEIGHT="5640033"
DEPOSIT="500000000$DENOM" # 500 JUNOX

# MAINNET
# JUNOD_NODE="https://rpc.juno.strange.love:443"
# KEY="reece-main"
# KEYRING="os"
# CHAIN_ID="juno-1"
# DENOM="ujuno"
# DEPOSIT="1000000000$DENOM" # 1,000 JUNO
# UPGRADE_HEIGHT="10078449"  # https://www.mintscan.io/juno/blocks/10078449

# Info
UPGRADE_NAME="v1800alpha4" # upgradehandler
UPGRADE_HUMAN_NAME="Alpha4-Patch"
FEES="500000$DENOM" # 0.5


TITLE="Juno Upgrade: $UPGRADE_HUMAN_NAME ($UPGRADE_NAME)"
DESC="# Juno Epona Upgrade (v18)\n\n[Release Notes](https://github.com/CosmosContracts/juno/releases/tag/v18.0.0-alpha.4)\n\n---\n\n\n## Voting Options\nYES: Agree to proceed with the v18 network upgrade.\nNO: Disagree with the v18 network upgrade."
UPGRADE_INFO='{"binaries":{"linux/amd64":"https://github.com/CosmosContracts/juno/releases/download/v18.0.0-alpha.4/junod"}}'

junod tx gov submit-legacy-proposal software-upgrade $UPGRADE_NAME --title="$TITLE" --description="$DESC" --deposit="$DEPOSIT" --upgrade-height="$UPGRADE_HEIGHT" --from=$KEY --keyring-backend=$KEYRING --chain-id=$CHAIN_ID --broadcast-mode=sync --node=$JUNOD_NODE --no-validate --upgrade-info=$UPGRADE_INFO --fees=$FEES --gas=2000000

# junod tx gov deposit

# junod tx gov vote