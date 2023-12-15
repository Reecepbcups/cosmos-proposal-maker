# import acc0 key into test keyring locally for usage. Could also do all upstream with CURL but ehh
JUNOD_NODE="http://localhost:42669"
KEY="acc0"
KEYRING="test"
CHAIN_ID="localjuno-1"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode block --gas=1000000 --fees 500ujuno"

junodv15 tx gov submit-proposal param-change param_change/MinimumDeposit.json $FLAGS

# deposit

# junod tx gov vote 2 yes $FLAGS --yes

# Vote with the validator on the machine throught rest endpoint
curl http://localhost:8080/ --include --header "Content-Type: application/json" -X POST --data '{"chain-id":"localjuno-1","action":"bin","cmd":"tx gov vote 1 yes --yes --gas=500000 --fees 500ujuno --node %RPC% --home %HOME% --chain-id %CHAIN_ID% --from validator --keyring-backend=test"}'

junodv15 q gov proposals --node $JUNOD_NODE