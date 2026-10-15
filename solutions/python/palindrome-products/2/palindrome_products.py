
"""Find the smallest and largest palindrome products in a given range."""


def is_palindrome(number):
    """Check whether a number is a palindrome."""
    return str(number) == str(number)[::-1]


def smallest(max_factor, min_factor=0):
    """Return the smallest palindrome product and all its factor pairs."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    result = None
    factors = []

    for first in range(min_factor, max_factor + 1):
        for second in range(first, max_factor + 1):
            product = first * second

            if result is not None and product >= result:
                break

            if is_palindrome(product):
                result = product
                factors = [(first, second)]

        if result is not None and first * first >= result:
            break

    return result, factors


def largest(max_factor, min_factor=0):
    """Return the largest palindrome product and all its factor pairs."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    result = None
    factors = []

    for first in range(max_factor, min_factor - 1, -1):
        for second in range(first, min_factor - 1, -1):
            product = first * second

            if result is not None and product < result:
                break

            if is_palindrome(product):
                if result is None or product > result:
                    result = product
                    factors = [(second, first)]
                elif product == result:
                    factors.append((second, first))

        if result is not None and first * first < result:
            break

    return result, factors
