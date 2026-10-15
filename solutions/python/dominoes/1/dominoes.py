
"""Create a valid chain of dominoes."""


def can_chain(dominoes):
    """Return a valid domino chain, or None if impossible."""
    if not dominoes:
        return []

    if len(dominoes) == 1:
        return dominoes if dominoes[0][0] == dominoes[0][1] else None

    def build_chain(chain, remaining):
        if not remaining:
            if chain[-1][1] == chain[0][0]:
                return chain
            return None

        last_number = chain[-1][1]

        for index, domino in enumerate(remaining):
            left, right = domino

            if left == last_number:
                result = build_chain(
                    chain + [(left, right)],
                    remaining[:index] + remaining[index + 1:],
                )
                if result is not None:
                    return result

            if right == last_number and left != right:
                result = build_chain(
                    chain + [(right, left)],
                    remaining[:index] + remaining[index + 1:],
                )
                if result is not None:
                    return result

        return None

    for index, domino in enumerate(dominoes):
        remaining = dominoes[:index] + dominoes[index + 1:]
        result = build_chain([domino], remaining)

        if result is not None:
            return result

        if domino[0] != domino[1]:
            result = build_chain([(domino[1], domino[0])], remaining)

            if result is not None:
                return result

    return None
