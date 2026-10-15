"""Simulate a game of Camicia."""

from collections import deque

PENALTIES = {
    "J": 1,
    "Q": 2,
    "K": 3,
    "A": 4,
}


def normalize_deck(deck):
    """Ignore number-card values when checking for loops."""
    return tuple(
        card if card in PENALTIES else "N"
        for card in deck
    )


def simulate_game(player_a, player_b):
    """Return the game status, total cards played, and tricks."""
    decks = [deque(player_a), deque(player_b)]
    pile = []
    cards_played = 0
    tricks = 0
    current_player = 0
    penalty = 0
    last_payment_player = None
    seen = set()

    def collect_pile(winner):
        """Give the pile to the winner and finish the trick."""
        nonlocal tricks, penalty, last_payment_player

        decks[winner].extend(pile)
        pile.clear()
        tricks += 1
        penalty = 0
        last_payment_player = None

    def result(status):
        return {
            "status": status,
            "cards": cards_played,
            "tricks": tricks,
        }

    while True:
        if not pile and penalty == 0:
            state = (
                normalize_deck(decks[0]),
                normalize_deck(decks[1]),
            )

            if state in seen:
                return result("loop")

            seen.add(state)

        if not decks[current_player]:
            collect_pile(1 - current_player)

            if len(decks[1 - current_player]) == sum(
                len(deck) for deck in decks
            ):
                return result("finished")

            current_player = 1 - current_player
            continue

        card = decks[current_player].popleft()
        pile.append(card)
        cards_played += 1

        if card in PENALTIES:
            penalty = PENALTIES[card]
            last_payment_player = current_player
            current_player = 1 - current_player
            continue

        if penalty > 0:
            penalty -= 1

            if penalty == 0:
                winner = last_payment_player
                collect_pile(winner)

                if len(decks[winner]) == sum(
                    len(deck) for deck in decks
                ):
                    return result("finished")

                current_player = winner
            # The same player continues paying the penalty.
            continue

        current_player = 1 - current_player
