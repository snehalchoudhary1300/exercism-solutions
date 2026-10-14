
"""Flatten a nested list into a single list."""


def flatten(iterable):
    """Return a flattened list, excluding None values."""
    result = []

    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)

    return result
