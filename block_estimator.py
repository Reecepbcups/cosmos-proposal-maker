from datetime import datetime, timezone

# https://www.mintscan.io/juno/blocks
CURRENT_BLOCK = 7276751

AVERAGE_BLOCK_TIME = 6.015

CURRENT_TIME = datetime.now(timezone.utc)

PLANNED_RELEASE_DATE = "2023-mar-13"
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

# 7378401 is the planned block, roughly 300 off from what the above gave me
