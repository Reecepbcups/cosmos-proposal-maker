JUNOD_NODE="https://juno-rpc.reece.sh:443"
KEY="reece"
KEYRING="os"
CHAIN_ID="juno-1"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode block --gas=1000000"

junod tx gov submit-proposal param-change param_change/BlockGas.json $FLAGS

junod tx gov vote 274 yes $FLAGS --yes