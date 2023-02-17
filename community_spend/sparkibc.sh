# Example in Juno, will convert to gaia for actual proposal

export JUNOD_NODE="http://localhost:26657"
FLAGS="--from juno1 --keyring-backend test --node $JUNOD_NODE --chain-id local-1 --home /home/reece/.juno1/ --gas 1000000 --broadcast-mode block"

junod tx gov submit-proposal community-pool-spend community_spend/sparkibc_comm_spend.json $FLAGS

# junod q gov proposals # make sure it is there

# deposit and vote
junod tx gov deposit 1 800000ujuno $FLAGS
junod tx gov vote 1 yes $FLAGS

# make sure it was actually sent
junod q bank balances juno1jv65s3grqf6v6jl3dp4t6c9t9rk99cd83d88wr


junod q bank balances juno1efd63aw40lxf3n4mhf7dzhjkr453axurv2zdzk