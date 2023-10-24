JUNOD_NODE="http://localhost:26657"
KEY="juno1"
KEYRING="test"
CHAIN_ID="local-1"

FLAGS="--from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --node $JUNOD_NODE --broadcast-mode=sync --gas=1000000 --fees=2500ujuno"


# SDK v45
# TITLE="Use Skip Tendermint By Default"
# DESCRIPTION="# Skip Tendermint By Default in Juno\n\n[Commonwealth Discussion](https://commonwealth.im/juno/discussion/10223-use-skip-by-default)\n\nJuno has the highest adoption of [Skip](https://skip.money/) in Cosmos. To simplify validator operations, this proposal, if passed, signals for the Juno binary use Skip by default. This approach has been tested by Notional while comparing Tendermint and comet, and there is no operational difference.\n\nUsing Skip by default does not require validators to use Skip (opt-in), it purely just uses their implementation by default for validators who do use Skip. Each validator will still have the option to use skip or not, as they choose.\n\n---\n\n## Will other MEV providers be considered?\n\nRight now, Skip MEV is the leading MEV provider in Cosmos. If another provider comes up and validators decide to switch to it, governance can always be used to change to the new MEV provider by default. This is more of a QOL addition for validators, which just ensures those who use it have it pre-installed during upgrades. Validators can continue to use other MEV solutions if they choose.\n\n## How will this MEV build be integrated into the Juno codebase?\n\nIt will be replaced in the go.mod from standard Tendermint to Skip's version. You can find [a PR of this here](https://github.com/CosmosContracts/juno/pull/587).\n\n\n\n## Voting Options\n\nYES: Agree to proceed with using Skip Tenmdermint by default.\n\nNO: Disagree with using Skip Tenmdermint by default.\n\nNO WITH VETO: Disagree with using Skip Tenmdermint by default and want depositors penalized.\n\nABSTAIN: Decline to give an opinion on using Skip Tenmdermint by default.\n\n"
# junod tx gov submit-proposal --type="text" --title="$TITLE" --description="$DESCRIPTION" $FLAGS --deposit=1000000ujuno

# SDK v47
# junod tx gov submit-proposal --type="text" --title="$TITLE" --description="$DESCRIPTION" $FLAGS --deposit=1000000ujuno
# junod tx gov submit-proposal ./text/max_val_commission.json $FLAGS
TITLE="Set Validator Max Commission Change Rate To 5%"
DESCRIPTION="# Set Validator Max Commission Change Rate To 5%\n\n[Commonwealth Thread](https://commonwealth.im/juno/discussion/12035-set-validator-max-commission-change-rate-up-to-5)\n\nIn reference to the recent event on Cosmos Hub, where a validator has increased their commission rate by 99.35% in a single transaction, a safe hard limit on max commission change rate should be set for all validators as good practice to protect delegators.\n\nThis proposal is signaling a future upgrade to set all validators max change rate (within a 24 hour period) to be no more than 5% if currently set above.\n\nThis would not affect the minimum nor maximum commission rate limits, rather ensures that network validators would not be able to increase their commission rate by more than 5% within 24 hours.\n\n*(This means for a validator to go from 5% to 100% commission, it would take 19 days.)*\n\n\n## Voting Options\n\n**YES**: Agree to a future upgrade to set all validators max change rate to be no more than 5%.\n\n**NO**: Disagree to a future upgrade to set all validators max change rate to be no more than 5%.\n\n**NO WITH VETO**: Disagree with the proposal and want depositors penalized.\n\n**ABSTAIN**: Decline to give an opinion on this proposal.\n\n"
junod tx gov submit-legacy-proposal --type="text" --title="$TITLE" --description="$DESCRIPTION" $FLAGS --deposit=1000000ujuno

junod tx gov vote 1 yes $FLAGS --yes