
"""Pick the best poker hand or hands."""

from collections import Counter


def best_hands(hands):
    """Return the best poker hand or hands."""

    def hand_rank(hand):
        cards = hand.split()
        card_values = {
            "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9,
            "10": 10, "J": 11, "Q": 12,
            "K": 13, "A": 14,
        }

        values = sorted(
            [card_values[card[:-1]] for card in cards],
            reverse=True,
        )
        suits = [card[-1] for card in cards]
        counts = Counter(values)
        frequencies = sorted(counts.values(), reverse=True)
        unique_values = sorted(set(values), reverse=True)

        is_flush = len(set(suits)) == 1
        is_straight = (
            len(unique_values) == 5
            and unique_values[0] - unique_values[-1] == 4
        )

        if set(values) == {14, 2, 3, 4, 5}:
            is_straight = True
            straight_high = 5
        else:
            straight_high = unique_values[0]

        if is_straight and is_flush:
            return (8, straight_high)

        if frequencies == [4, 1]:
            four = max(value for value, count in counts.items() if count == 4)
            kicker = max(value for value, count in counts.items() if count == 1)
            return (7, four, kicker)

        if frequencies == [3, 2]:
            three = max(value for value, count in counts.items() if count == 3)
            pair = max(value for value, count in counts.items() if count == 2)
            return (6, three, pair)

        if is_flush:
            return (5, *values)

        if is_straight:
            return (4, straight_high)

        if frequencies == [3, 1, 1]:
            three = max(value for value, count in counts.items() if count == 3)
            kickers = sorted(
                (value for value, count in counts.items() if count == 1),
                reverse=True,
            )
            return (3, three, *kickers)

        if frequencies == [2, 2, 1]:
            pairs = sorted(
                (value for value, count in counts.items() if count == 2),
                reverse=True,
            )
            kicker = max(value for value, count in counts.items() if count == 1)
            return (2, *pairs, kicker)

        if frequencies == [2, 1, 1, 1]:
            pair = max(value for value, count in counts.items() if count == 2)
            kickers = sorted(
                (value for value, count in counts.items() if count == 1),
                reverse=True,
            )
            return (1, pair, *kickers)

        return (0, *values)

    highest_rank = max(hand_rank(hand) for hand in hands)

    return [
        hand for hand in hands
        if hand_rank(hand) == highest_rank
    ]
