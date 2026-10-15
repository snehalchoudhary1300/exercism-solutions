"""Solve the knapsack problem using dynamic programming."""


def maximum_value(maximum_weight, items):
    """Return the maximum value that fits within the weight limit."""
    values = [0] * (maximum_weight + 1)

    for item in items:
        weight = item["weight"]
        value = item["value"]

        for capacity in range(maximum_weight, weight - 1, -1):
            values[capacity] = max(
                values[capacity],
                values[capacity - weight] + value
            )

    return values[maximum_weight]
