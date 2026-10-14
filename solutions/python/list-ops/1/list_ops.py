
"""Implement basic list operations."""


def append(list1, list2):
    """Append the second list to the first."""
    result = []
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result


def concat(lists):
    """Combine all lists into one list."""
    result = []
    for current_list in lists:
        for item in current_list:
            result.append(item)
    return result


def filter(function, list1):
    """Return items that satisfy the predicate."""
    result = []
    for item in list1:
        if function(item):
            result.append(item)
    return result


def length(list1):
    """Count the items in a list."""
    count = 0
    for item in list1:
        count += 1
    return count


def map(function, list1):
    """Apply a function to each item."""
    result = []
    for item in list1:
        result.append(function(item))
    return result


def foldl(function, list1, initial):
    """Fold items from left to right."""
    accumulator = initial
    for item in list1:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list1, initial):
    """Fold items from right to left."""
    accumulator = initial
    index = length(list1) - 1

    while index >= 0:
        accumulator = function(accumulator, list1[index])
        index -= 1

    return accumulator


def reverse(list1):
    """Return a reversed copy of the list."""
    result = []
    index = length(list1) - 1

    while index >= 0:
        result.append(list1[index])
        index -= 1

    return result
