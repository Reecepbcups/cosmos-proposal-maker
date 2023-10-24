JUNOD_NODE="https://uni-rpc.reece.sh:443"
KEY="validator"
KEYRING="os"
CHAIN_ID="uni-6"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode=sync --gas=1000000 --fees=50000ujunox"

# SDK v47
# junod tx gov submit-proposal --type="text" --title="$TITLE" --description="$DESCRIPTION" $FLAGS --deposit=1000000ujuno
junod tx gov submit-proposal ./text/max_val_commission.json $FLAGS

junod tx gov vote 1 yes $FLAGS --yes