# junodv15 keys add reece --recover --keyring-backend=file --home=/home/reece/.juno

JUNOD_NODE="https://rpc.juno.strange.love:443"
KEY="reece"
KEYRING="file"
CHAIN_ID="juno-1"
JUNO_HOME="/home/reece/.juno"

FLAGS="--from $KEY --keyring-backend=$KEYRING --home=$JUNO_HOME --chain-id=$CHAIN_ID --node=$JUNOD_NODE --broadcast-mode=sync --gas=1000000 --fees 2500ujuno"

junodv15 tx gov submit-proposal param-change param_change/MinimumDeposit.json $FLAGS


junodv15 tx gov deposit 304 800000000ujuno $FLAGS --yes

junodv15 tx gov vote 304 yes $FLAGS --yes
