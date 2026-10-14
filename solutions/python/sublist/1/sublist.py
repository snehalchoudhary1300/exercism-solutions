
"""Determine the relationship between two lists."""

EQUAL = "equal"
SUBLIST = "sublist"
SUPERLIST = "superlist"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    """Return the relationship between two lists."""
    if list_one == list_two:
        return EQUAL

    if len(list_one) < len(list_two):
        for index in range(len(list_two) - len(list_one) + 1):
            if list_two[index:index + len(list_one)] == list_one:
                return SUBLIST
        return UNEQUAL

    for index in range(len(list_one) - len(list_two) + 1):
        if list_one[index:index + len(list_two)] == list_two:
            return SUPERLIST

    return UNEQUAL
