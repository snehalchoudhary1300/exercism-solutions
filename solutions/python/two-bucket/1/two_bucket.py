"""Solve the two bucket measuring problem."""

from collections import deque
import math


def measure(bucket_one, bucket_two, goal, start_bucket):
    """Measure the goal amount using two buckets."""
    # Validation checks
    if goal > max(bucket_one, bucket_two):
        raise ValueError("Goal cannot be larger than both buckets.")
    
    if goal % math.gcd(bucket_one, bucket_two) != 0:
        raise ValueError("Goal cannot be measured with these bucket sizes.")

    if start_bucket not in ("one", "two"):
        raise ValueError("Starting bucket must be 'one' or 'two'.")

    # Queue stores tuples of: (actions, bucket_one_vol, bucket_two_vol)
    queue = deque()
    seen = set()

    if start_bucket == "one":
        # Initial action: Fill bucket one
        queue.append((1, bucket_one, 0))
        seen.add((bucket_one, 0))
        # Invalid state check: starting bucket empty, other full
        seen.add((0, bucket_two))
    else:
        # Initial action: Fill bucket two
        queue.append((1, 0, bucket_two))
        seen.add((0, bucket_two))
        seen.add((bucket_one, 0))

    while queue:
        actions, b1, b2, = queue.popleft()

        # Check if we reached the goal
        if b1 == goal:
            return actions, "one", b2
        if b2 == goal:
            return actions, "two", b1

        # Generate possible next states
        # 1. Empty a bucket
        next_states = [
            (0, b2),  # Empty bucket one
            (b1, 0),  # Empty bucket two
            # 2. Fill a bucket
            (bucket_one, b2),  # Fill bucket one
            (b1, bucket_two),  # Fill bucket two
            # 3. Pour bucket one into bucket two
            (
                b1 - min(b1, bucket_two - b2),
                b2 + min(b1, bucket_two - b2),
            ),
            # 4. Pour bucket two into bucket one
            (
                b1 + min(b2, bucket_one - b1),
                b2 - min(b2, bucket_one - b1),
            ),
        ]

        for next_b1, next_b2 in next_states:
            state = (next_b1, next_b2)
            if state not in seen:
                seen.add(state)
                queue.append((actions + 1, next_b1, next_b2))

    raise ValueError("Goal cannot be reached.")