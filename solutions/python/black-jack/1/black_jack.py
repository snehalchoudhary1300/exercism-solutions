

"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card. See below for values.

        1. 'J', 'Q', or 'K' = 10
        2. 'A' = 1
        3. '2' - '10' = numerical value.
    """
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.
        card_two (str): Second card dealt in the hand.

    Returns:
        str or tuple: The higher card, or both cards if equal.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.
        card_two (str): Second card dealt in the hand.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    if card_one == 'A' or card_two == 'A':
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    if total <= 10:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.
        card_two (str): Second card dealt in the hand.

    Returns:
        bool: Is the hand a blackjack (two cards worth 21)?
    """
    return (
        (card_one == 'A' and value_of_card(card_two) == 10)
        or (card_two == 'A' and value_of_card(card_one) == 10)
    )


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

        Returns:
            bool: Can the hand be split into two pairs?
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card dealt in the hand.
        card_two (str): Second card dealt in the hand.

    Returns:
        bool: Can the hand be doubled down?
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)


