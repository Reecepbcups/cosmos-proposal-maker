"""
Reece Williams (reece.sh) | 2023
Easily make a proposal for a network, shrinking the markdown to a single line for the description.
"""

# =====

VOTE_OPTIONS = """
## Voting Options

YES: Agree to proceed with the funding for interchain info.
NO: Disagree with the funding for interchain info.
NO WITH VETO: Disagree with the funding for interchain info and want depositors penalized.
ABSTAIN: Decline to give an opinion on the funding.

"""


proposal_text = f"""
# Overview

[Original Cosmos Forum Post](https://forum.cosmos.network/t/proposal-last-call-2023-02-21-interchain-info-hub-funding/9822)

Built by Spark IBC, Interchain Info (ICI) is a truly multi-chain & chain-agnostic hub for information and tooling to make navigating the rapidly growing Interchain easier for both new and old users alike. At Spark IBC, we believe that, currently, “Cosmos” and the greater Interchain are extremely fragmented, as communities, educational resources, NFT collections, Dapps and tools each reside in their own remote corners of the ecosystem.

ICI aims to change this by taking the first step toward building the unified, multi-chain future that the community has been waiting for, and that we believe is paramount to Cosmos gaining mass adoption in the next market cycle. We are currently running an ICI funding campaign on the Spark IBC platform, found here, [https://sparkibc.zone](https://sparkibc.zone) 4 along with more details about ICI itself.

We are avoiding VCs and private investors in this endeavor, because ICI is only a valuable resource if it remains unbiased and beholden to no one but the community that uses it. Therefore, all ICI costs so far have come out of our own pockets, and going forwards, we’re raising funds entirely through grants and donations from users and community pools.

## Request

We request 1% of community pool funds, capped at $20,000 from a number of chains, including The Cosmos Hub, to contribute to The ICI Campaign on Spark IBC. For The Hub, this makes our total ask ~$20k or 1,438 ATOM at the time of writing.

If passed,

- 50% of issued funds will be donated directly to ICI for general development, hosting and maintenance, to be used alongside other funding sources like private contributions done through the Spark platform.
- The remaining 50% will be used as incentives for community members to create and submit content about general cosmos tech. For other chains, this 50% is reserved for content about stuff built in that chains ecosystem, but since the Hub is positioned a bit differently, we think it’s match made in heaven to direct these funds towards content on things like IBC, CosmWasm, the Cosmos SDK, etc.
- For The Hub, this amounts to ~20k USD in Atom total, which is about 1,438 ATOM, which will then be split 50/50 as outlined above.

Each network that approves funding will be rewarded with Spark Points based on their full donation amount and a customized entry on our leaderboard labeled “[chain name] Community.” Spark Points are used within the Spark IBC system to recognize users for their contributions to the Interchain. In this case, there would be an entry made for “The Cosmos Hub Community” with 20k Spark Points.

One Spark Point is representative of one dollar (or USDC, or, in this case, token equivalent) donated, and is tracked through the soulbound $SPARK token on Juno Network. For these donations, Spark IBC will set up a wallet on Juno, or use the Bech32 converted version of the community pools address on Juno, label it accordingly on our leaderboard, and mint $SPARK equivalent to the USD value of the donated amount into it, measured by the price at the time of distribution. Slippage and fees for conversion will not be taken into account, as that’s beyond the communities control.

One significant benefit of multi-chain projects is the unique ability to distribute our funding requests across different sources to minimize sell pressure and the burden on any single community pool/token. This sort of effort is something that Spark IBC plans to pioneer and offer as a potential service to any who use the Spark IBC platform for fundraising in future.


Similar funding requests will also be submitted to the following Cosmos chains:

- Agoric
- Akash
- Band
- Carbon
- Cheqd
- Chihuahua
- Comdex
- Cosmos Hub
- Evmos
- Fetch AI
- Injective
- Juno
- Kava
- Kujira
- Osmosis
- Persistence
- Secret
- Sommelier
- Stargaze
- Teritori
- LUNC
- Terra

[Funding Ask Amounts Spreadsheet](https://global.discourse-cdn.com/standard11/uploads/cosmos1/optimized/2X/e/edd7c2b885e321d82eefd114a7be03f232534462_2_629x500.png)

## Spending Details

### Base Contribution

In addition to the ICI info on SparkIBC.zone, we also have a rough breakdown of how funds will be spent given hitting certain funding tiers, found here 2
Link: [ICI Budget Outline for Initial Raise](https://docs.google.com/spreadsheets/d/13GYFnJYozptojj3ytE_OYbo03inoQ1dEJxnHnmparWQ/edit#gid=0)

### Incentives Program

As stated, 50% of the requested $20k will be used exclusively to incentivize content related to general Cosmos tech & terminology on the Index and Resource hub. This allows community members and content creators the ability to earn a little income while contributing something beneficial to the entire interchain. It also ensures that a portion of the allotted funding amount returns to the community in a very direct way.

Note: the Spark & ICI Team reserve the right to deny payment, both pre/post-production, to anyone on the basis of content quality or attempts to manipulate this proposed system (i.e. needlessly long articles, videos, copy others existing work as a full new submission etc.); this is not a “trustless” incentive program. At this time, we will only accept English submissions meeting basic literary standards; however, we may expand this program to include other languages in the future and/or add a translation tier to the list of incentives below (we are open to feedback on these details):

[Submission outline](https://global.discourse-cdn.com/standard11/uploads/cosmos1/optimized/2X/9/92c9a4e08b05afbc1cf46e0da69df8b0c827f1ee_2_450x500.png)

*$0.05/word (written content) and $5.00/min. (video content) are below industry standards, but the crux of this project is to further incentivize creators who are already producing original content, while refining and updating existing material that needs to constantly be updated. In its entirety, this project will both promote new material and provide house-keeping for fresh, up-to-date information in order to attract new ecosystem investors and users.

## Misc. Details

How will payment be distributed and handled?

- We will be asking for the requested amount as a single lump sum payment. The amount granted will then be split into two chunks, each comprising 50% of the total.
    - 50% will be DCA’d out into stables over the following 15 days. Meaning a maximum daily sell pressure of no more than ~$666 per day for chains granting the full 20k, such as the Hub, and far less for others. This will be the base contribution.
    - The other 50% will be set aside for the content incentives program outlined above, and we will be gauging community sentiment on doing one of the three following options
        - Keep in the native currency
        - DCA out to stables along with the rest. Sell pressure will be kept to the above figure or less.
        - DCA out half (of the 50%, or 25% of the total) along with the base contribution.

Will the incentives program be transparent?
    - Of course! We will keep records of payouts and the work done to receive them for the community to review. This also serves to provide a metric for results, and should help communities gauge whether a continuation of this program later down the road would be something of interest to them or not.

How long do you intend the incentive programs to last?
    - Due to the drastically different ask amounts amongst various chains, as well as the amount of content relevant to them, some chains’ incentives may dry up much quicker than others. We believe that with the program we’ve outlined above, regardless of the duration, the general amount of work achieved per dollar spent should be similar.

What happens if a chain does not pass the proposal, are they to be treated any differently?
    - Absolutely not. All chains and projects in the Cosmos are equal in our eyes, and no community will be penalized for failing to support our effort, except by missing out on the incentives program and, of course, contributing to something crucially important for the entire Interchain.


{VOTE_OPTIONS}
"""

# TODO: escape all special characters?

# replace res new lines to the \n character
res = proposal_text.replace("\n", "\\n")
# res = res.replace("'", "\\'") # I do not think we need to do this? does this break text props?
res = res.replace("’", "'")  # when you copy paste from the web
res = res.replace('"', '\\"')
res = res.replace("    ", "\\t")  # tabs
print("=" * 20)

if res.startswith("\\n"):
    res = res[2:]
if res.endswith("\\n"):
    res = res[:-2]

print(res)
