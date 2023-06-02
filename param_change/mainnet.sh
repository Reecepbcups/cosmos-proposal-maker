JUNOD_NODE="https://rpc.juno.strange.love:443"
KEY="reece"
KEYRING="file"
CHAIN_ID="juno-1"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode block --gas=1000000 --fees 2500ujuno"

junod tx gov submit-proposal param-change param_change/GlobalFee.json $FLAGS

junod tx gov vote 274 yes $FLAGS --yes


junod tx gov deposit 297 800000000ujuno $FLAGS --yes