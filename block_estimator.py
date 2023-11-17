from datetime import datetime, timezone

# https://www.mintscan.io/juno/blocks
CURRENT_BLOCK = 5292755

# Get a future block from mintscan
# -> https://testnet.mintscan.io/juno-testnet/blocks/999999999
AVERAGE_BLOCK_TIME = 2.900

CURRENT_TIME = datetime.now(timezone.utc)

PLANNED_RELEASE_DATE = "2023-nov-20"
PLANNED_UTC_TIME = "17:00:00"
PLANNED_TIME = datetime.strptime(
    f"{PLANNED_RELEASE_DATE} {PLANNED_UTC_TIME}", "%Y-%b-%d %H:%M:%S"
)
PLANNED_TIME = PLANNED_TIME.replace(tzinfo=timezone.utc)

# =====

diff = PLANNED_TIME - CURRENT_TIME
blocks = diff.total_seconds() / AVERAGE_BLOCK_TIME

print(f"Estimated blocks until release: {int(blocks)}")
print(f"Which is roughly block: {CURRENT_BLOCK + int(blocks)}")
