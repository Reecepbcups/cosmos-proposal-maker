JUNOD_NODE="http://localhost:26657"
KEY="juno1"
KEYRING="test"
CHAIN_ID="local-1"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode block --gas=1000000"

TITLE="Use Skip Tendermint By Default"
DESCRIPTION="# Skip Tendermint By Default in Juno\n\n[Commonwealth Discussion](https://commonwealth.im/juno/discussion/10223-use-skip-by-default)\n\nJuno has the highest adoption of [Skip](https://skip.money/) in Cosmos. To simplify validator operations, this proposal, if passed, signals for the Juno binary use Skip by default. This approach has been tested by Notional while comparing Tendermint and comet, and there is no operational difference.\n\nUsing Skip by default does not require validators to use Skip (opt-in), it purely just uses their implementation by default for validators who do use Skip. Each validator will still have the option to use skip or not, as they choose.\n\n---\n\n## Will other MEV providers be considered?\n\nRight now, Skip MEV is the leading MEV provider in Cosmos. If another provider comes up and validators decide to switch to it, governance can always be used to change to the new MEV provider by default. This is more of a QOL addition for validators, which just ensures those who use it have it pre-installed during upgrades. Validators can continue to use other MEV solutions if they choose.\n\n## How will this MEV build be integrated into the Juno codebase?\n\nIt will be replaced in the go.mod from standard Tendermint to Skip's version. You can find [a PR of this here](https://github.com/CosmosContracts/juno/pull/587).\n\n\n\n## Voting Options\n\nYES: Agree to proceed with using Skip Tenmdermint by default.\n\nNO: Disagree with using Skip Tenmdermint by default.\n\nNO WITH VETO: Disagree with using Skip Tenmdermint by default and want depositors penalized.\n\nABSTAIN: Decline to give an opinion on using Skip Tenmdermint by default.\n\n"

junod tx gov submit-proposal --type="text" --title="$TITLE" --description="$DESCRIPTION" $FLAGS --deposit=1000000ujuno

junod tx gov vote 1 yes $FLAGS --yes