
"""Count the number of eggs represented by 1 bits."""


def egg_count(display_value):
    """Return the number of 1 bits in the binary representation."""
    count = 0

    while display_value > 0:
        if display_value % 2 == 1:
            count += 1

        display_value //= 2

    return count
