JUNOD_NODE="http://localhost:26657"
KEY="juno1"
KEYRING="test"
CHAIN_ID="local-1"

UPGRADE_NAME="v12" # upgrasdeHandler
UPGRADE_HEIGHT="7075551"
DEPOSIT="200000000ujuno" # 200 JUNO
FEES="50000ujuno" # 0.05 JUNO

junod tx gov submit-proposal software-upgrade $UPGRADE_NAME \
    --title "Juno v12 Upgrade (Stop Governance Spam)" \
    --description "# Juno v12 Upgrade Proposal\n\nTo reduce spamming in the Juno governance system, we propose requiring a 20% deposit (200 JUNO) on proposal creation. This will ensure that only quality proposals are submitted and deter malicious governance spam. Should you wish to make a proposal, but don\'t have 200 Juno, you can reach out to a member of the core team or Sub-DAOs for assistance. The minimum deposit is meant to deter spam, not participation.\n\nTag v12.0.0-beta.1 has been tested on our testnet, uni-6, and will be finalized as v12.0.0 if this proposal passes.\n\n**NOTE** This subsequently renames the previous [v12 upgrade to v13 from our medium blog post](https://medium.com/@reecepbcups/juno-v12-update-4bab64640a62)\n\nProvided this upgrade passes, it is scheduled for block [7075551](https://www.mintscan.io/juno/blocks/7075551). Roughly expected Monday, February 20th around 1700UTC.\n\n## Voting Options\n\nYES: Agree to proceed with the Juno v12 upgrade and stop governance spam with the deposit requirement.\nNO: Disagree with the v12 upgrade and the deposit requirement.\nNO WITH VETO: Disagree with the upgrade and want depositors penalized.\nABSTAIN: Decline to give an opinion on the upgrade.\n" \
    --deposit $DEPOSIT --upgrade-height $UPGRADE_HEIGHT --from $KEY --keyring-backend $KEYRING --chain-id $CHAIN_ID --yes --broadcast-mode block --node $JUNOD_NODE --fees $FEES