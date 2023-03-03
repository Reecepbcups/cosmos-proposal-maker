JUNOD_NODE="http://localhost:26657"
KEY="juno1"
KEYRING="test"
CHAIN_ID="local-1"

UPGRADE_NAME="v13" # upgrasdeHandler
UPGRADE_HEIGHT="7500000"
DEPOSIT="200000000ujuno" # 200 JUNO
FEES="50000ujuno" # 0.05 JUNO

junod tx gov submit-proposal software-upgrade $UPGRADE_NAME \
    --title "Juno v13 Upgrade" \
    --description "..............." \
    --upgrade-info '{"binaries":{"linux/amd64":"https://github.com/CosmosContracts/juno/releases/download/v13.0.0/junod"}}'
    --deposit $DEPOSIT --upgrade-height $UPGRADE_HEIGHT --from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --yes --broadcast-mode block --node $JUNOD_NODE --fees $FEES