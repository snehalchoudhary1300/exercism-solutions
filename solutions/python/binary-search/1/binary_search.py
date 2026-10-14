
"""Search for a value in a sorted list using binary search."""


def find(search_list, value):
    """Return the index of value or raise ValueError if not found."""
    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if search_list[middle] == value:
            return middle
        if search_list[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    raise ValueError("value not in array")
