
"""Calculate the fewest coins needed to make change."""


def find_fewest_coins(coins, target):
    """Return the fewest coins that add up to the target."""
    if target < 0:
        raise ValueError("target can't be negative")

    if target == 0:
        return []

    if not coins or any(coin <= 0 for coin in coins):
        raise ValueError("can't make target with given coins")

    minimum_coins = [float("inf")] * (target + 1)
    last_coin = [0] * (target + 1)
    minimum_coins[0] = 0

    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount and minimum_coins[amount - coin] + 1 < minimum_coins[amount]:
                minimum_coins[amount] = minimum_coins[amount - coin] + 1
                last_coin[amount] = coin

    if minimum_coins[target] == float("inf"):
        raise ValueError("can't make target with given coins")

    result = []
    amount = target

    while amount > 0:
        coin = last_coin[amount]
        result.append(coin)
        amount -= coin

    return sorted(result)
