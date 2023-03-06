# JUNOD_NODE="http://localhost:26657"
# KEY="juno1"
# KEYRING="test"
# CHAIN_ID="local-1"

JUNOD_NODE="https://rpc.juno.strange.love:443"
KEY="reece"
KEYRING="os"
CHAIN_ID="juno-1"

UPGRADE_NAME="v13" # upgradehandler
UPGRADE_HEIGHT="7374801"
DEPOSIT="200000000ujuno" # 200 JUNO
FEES="50000ujuno" # 0.05 JUNO

junod tx gov submit-proposal software-upgrade $UPGRADE_NAME \
    --title "Juno v13 Upgrade" \
    --description "# Juno v13 Upgrade\n\nThis network upgrade brings the following changes to Juno Network:\n\n- x/FeeShare Module\n- x/TokenFactory Module\n- CosmWasm v0.30\n- IBC v4\n- Packet Forward Middleware\n\nDue to deterministic issues with the oracle module on our testnet, it has been pushed to v14 or later.\n\n---\n\n## x/FeeShare Module\n\nThis module's addition was passed in [Juno Proposal 51](https://www.mintscan.io/juno/proposals/51)\n\nIf you're a smart contract developer on Juno, you can now earn a cut of all gas fees generated on your contract. Initially this is set to 50% of all gas fees which interact with your contract directly. \nGovernance at any time can change this percentage to any value between 0% and 100%, add new tokens to be paid in (ex; USDC, OSMO, etc), or toggle this feature entirely.\nThis module helps incentivize developers to build on Juno Network and bring new business models that are not directly DeFi related.\n\n## x/TokenFactory Module\n\nThis module allows anyone to create a native token on Juno Network. This drastically increases the UX and UI of the networks utility tokens. As a developer, it also removes the need to support both native assets and CW20 in your contracts.\nDAOs/SubDAOs can control a contract which mints tokens for other business logic in your contracts through our [TokenFactory Middleware Contracts](https://github.com/CosmosContracts/tokenfactory-contracts).\n\n## CosmWasm v0.30\n\nYou can read all of the great features in x/wasmd v0.30.0 in [Confio's medium article here](https://medium.com/cosmwasm/wasmd-0-30-released-8e9932929238).\n\n## Packet Forward Middleware\n\nThis new middleware allows for the forwarding of IBC packets through Juno's infrastructure to final destination chains. As cosmos zones expand, the need for multi-hop transactions will increase for scaling. \nThis new module allows for Juno to be a \"relay\" chain for other zones. Where a newly launched chain can just focus on relaying to and from Juno, and in return can route these packets to all the zones Juno is connected too. \nWith this, public relayers will be able to earn fees in the future with these transactions along with the [ICS29 IBCFees module added in this update](https://github.com/cosmos/ibc-go/tree/main/docs/middleware/ics29-fee).\n\n## Other Changes\n\n- Complete overhaul of the main app for easier upgradeability\n- ICA Host and Controller\n- Allow all ICA messages\n- Latest IAVL, Tendermint, and Cosmos SDK (v0.45.14)\n- junod debug bech32-convert\n- junod debug export-derive-balances\n- junod debug forceprune\n- junod reset [app|wasm] directory files\n\n\n\n## Voting Options\n\nYES: Agree to proceed with Juno v13 network upgrade.\n\nNO: Disagree with the Juno v13 network upgrade.\n\nNO WITH VETO: Disagree with the Juno v13 network upgrade and want depositors penalized.\n\nABSTAIN: Decline to give an opinion on the Juno v13 network upgrade.\n\n" \
    --upgrade-info='{"binaries":{"linux/amd64":"https://github.com/CosmosContracts/juno/releases/download/v13.0.0/junod"}}' \
    --deposit=$DEPOSIT --upgrade-height=$UPGRADE_HEIGHT --from=$KEY --keyring-backend=$KEYRING --chain-id=$CHAIN_ID --broadcast-mode=block --node $JUNOD_NODE --fees $FEES --gas=2000000