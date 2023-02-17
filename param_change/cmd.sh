JUNOD_NODE="http://localhost:26657"
KEY="juno1"
KEYRING="test"
CHAIN_ID="local-1"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode block"

junod tx gov submit-proposal param-change param_change/FeeShare.json $FLAGS --deposit 200000ujuno
junod tx gov submit-proposal param-change param_change/TokenFactory.json $FLAGS --deposit 200000ujuno

junod tx gov vote 2 yes $FLAGS
junod tx gov vote 3 yes $$FLAGS