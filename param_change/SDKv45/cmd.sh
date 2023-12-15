JUNOD_NODE="http://localhost:26657"
KEY="juno1"
KEYRING="test"
CHAIN_ID="local-1"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode block --gas=1000000"

junod tx gov submit-proposal param-change param_change/BlockGas.json $FLAGS

junod tx gov vote 1 yes $FLAGS --yes