
"""Functions for tracking poker rounds and calculating card averages."""


def get_rounds(number):
    """Return the current round and the next two rounds."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Combine two lists of rounds."""
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check whether a round exists in the list."""
    return number in rounds


def card_average(hand):
    """Calculate the average value of the cards."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Check whether an approximate average equals the actual average."""
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    average = card_average(hand)

    return average in (first_last_average, middle_card)


def average_even_is_average_odd(hand):
    """Check whether even-position and odd-position averages are equal."""
    even_average = sum(hand[::2]) / len(hand[::2])
    odd_average = sum(hand[1::2]) / len(hand[1::2])

    return even_average == odd_average


def maybe_double_last(hand):
    """Double the last card if its value is 11."""
    if hand and hand[-1] == 11:
        hand[-1] = 22
    return hand
