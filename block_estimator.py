from datetime import datetime, timezone

# https://www.mintscan.io/juno/blocks
CURRENT_BLOCK = 9393861

# Get a future block from mintscan
# -> https://testnet.mintscan.io/juno-testnet/blocks/999999999
AVERAGE_BLOCK_TIME = 6.0343

CURRENT_TIME = datetime.now(timezone.utc)

PLANNED_RELEASE_DATE = "2023-aug-7"
PLANNED_UTC_TIME = "16:00:00"
PLANNED_TIME = datetime.strptime(
    f"{PLANNED_RELEASE_DATE} {PLANNED_UTC_TIME}", "%Y-%b-%d %H:%M:%S"
)
PLANNED_TIME = PLANNED_TIME.replace(tzinfo=timezone.utc)

# =====

diff = PLANNED_TIME - CURRENT_TIME
blocks = diff.total_seconds() / AVERAGE_BLOCK_TIME

print(f"Estimated blocks until release: {int(blocks)}")
print(f"Which is roughly block: {CURRENT_BLOCK + int(blocks)}")
