
"""Calculate the lowest price for a basket of books."""

from functools import lru_cache


def total(basket):
    """Return the minimum price in cents."""
    prices = {
        1: 800,
        2: 1520,
        3: 2160,
        4: 2560,
        5: 3000,
    }

    counts = [0] * 5

    for book in basket:
        counts[book - 1] += 1

    @lru_cache(maxsize=None)
    def find_minimum(remaining):
        if not any(remaining):
            return 0

        available = [
            index
            for index, count in enumerate(remaining)
            if count > 0
        ]

        best_price = float("inf")

        for mask in range(1, 1 << len(available)):
            selected = [
                available[index]
                for index in range(len(available))
                if mask & (1 << index)
            ]

            updated = list(remaining)

            for index in selected:
                updated[index] -= 1

            group_size = len(selected)
            price = prices[group_size] + find_minimum(tuple(updated))
            best_price = min(best_price, price)

        return best_price

    return find_minimum(tuple(counts))
