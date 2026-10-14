
"""Calculate scores for the game of Yacht."""

from collections import Counter

ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"
YACHT = "yacht"


def score(dice, category):
    """Calculate the score for the given dice and category."""
    counts = Counter(dice)
    dice_sum = sum(dice)

    number_categories = {
        ONES: 1,
        TWOS: 2,
        THREES: 3,
        FOURS: 4,
        FIVES: 5,
        SIXES: 6,
    }

    if category in number_categories:
        value = number_categories[category]
        return value * counts[value]

    if category == FULL_HOUSE:
        return dice_sum if sorted(counts.values()) == [2, 3] else 0

    if category == FOUR_OF_A_KIND:
        for value, count in counts.items():
            if count >= 4:
                return value * 4
        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    if category == CHOICE:
        return dice_sum

    if category == YACHT:
        return 50 if len(counts) == 1 else 0

    return 0
