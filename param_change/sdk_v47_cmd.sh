# test_node.sh in Juno repo

JUNOD_NODE="http://localhost:26657"

junod tx gov submit-proposal /home/reece/Desktop/Programming/Python/cosmos-proposal-maker/param_change/v47-POB.json --gas=500000 --from=juno1 --home=$HOME/.juno1/ --fees=10000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes

# deposit 1000000 ujuno
junod tx gov deposit 1 1000000ujuno --from=juno1 --home=$HOME/.juno1/ --fees=10000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes

junod tx gov vote 1 yes --from=juno1 --home=$HOME/.juno1/ --fees=10000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes


junod q gov proposal 1

# testing the above
# JUNOD_NODE="http://localhost:26657"
# junod tx gov submit-proposal /home/reece/Desktop/Programming/Python/cosmos-proposal-maker/param_change/v47_GlobalFee_FeeShare.json --gas=500000 --from=juno1 --home=$HOME/.juno1/ --fees=10000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes
# junod tx gov vote 1 yes --from=juno1 --home=$HOME/.juno1/ --fees=10000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes
# junod tx bank send juno1 juno1efd63aw40lxf3n4mhf7dzhjkr453axurv2zdzk 1ujuno --fees=4630ibc/EAC38D55372F38F1AFD68DF7FE9EF762DCF69F26520643CF3F9D292A738D8034 --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes

# test with feeshare too.
# junod tx wasm store /home/reece/Desktop/Programming/CosmWasm/clock-example/artifacts/clock_example.wasm --from=juno1 --home=$HOME/.juno1/ --fees=150000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes --gas=1500000
# junod tx wasm instantiate 1 '{}' --from=juno1 --home=$HOME/.juno1/ --fees=150000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes --gas=1500000 --label=l --admin=juno1hj5fveer5cjtn4wd6wstzugjfdxzl0xps73ftl
# junod tx feeshare register juno14hj2tavq8fpesdwxxcu44rty3hh90vhujrvcmstl4zr3txmfvw9skjuwg8 juno1hj5fveer5cjtn4wd6wstzugjfdxzl0xps73ftl --home=$HOME/.juno1/ --fees=150000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes --gas=1500000 --from juno1
# junod tx feeshare update juno14hj2tavq8fpesdwxxcu44rty3hh90vhujrvcmstl4zr3txmfvw9skjuwg8 juno1efd63aw40lxf3n4mhf7dzhjkr453axurv2zdzk --home=$HOME/.juno1/ --fees=150000ujuno --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes --gas=1500000 --from juno1
# junod q feeshare contract juno14hj2tavq8fpesdwxxcu44rty3hh90vhujrvcmstl4zr3txmfvw9skjuwg8
# junod tx wasm execute juno14hj2tavq8fpesdwxxcu44rty3hh90vhujrvcmstl4zr3txmfvw9skjuwg8 '{"increment":{}}' --home=$HOME/.juno1/ --fees=18700ibc/EAC38D55372F38F1AFD68DF7FE9EF762DCF69F26520643CF3F9D292A738D8034 --keyring-backend=test --chain-id=local-1 --node=http://localhost:26657 --yes --gas=500000 --from juno1
