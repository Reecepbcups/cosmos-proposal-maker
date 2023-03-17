# Skip Tendermint By Default in Juno

[Commonwealth Discussion](https://commonwealth.im/juno/discussion/10223-use-skip-by-default)

Juno has the highest adoption of [Skip](https://skip.money/) in Cosmos. To simplify validator operations, this proposal, if passed, signals for the Juno binary use Skip by default. This approach has been tested by Notional while comparing Tendermint and comet, and there is no operational difference.

Using Skip by default does not require validators to use Skip (opt-in), it purely just uses their implementation by default for validators who do use Skip. Each validator will still have the option to use skip or not, as they choose.

---

## Will other MEV providers be considered?

Right now, Skip MEV is the leading MEV provider in Cosmos. If another provider comes up and validators decide to switch to it, governance can always be used to change to the new MEV provider by default. This is more of a QOL addition for validators, which just ensures those who use it have it pre-installed during upgrades. Validators can continue to use other MEV solutions if they choose.

## How will this MEV build be integrated into the Juno codebase?

It will be replaced in the go.mod from standard Tendermint to Skip's version. You can find [a PR of this here](https://github.com/CosmosContracts/juno/pull/587).
