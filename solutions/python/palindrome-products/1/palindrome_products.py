
def is_palindrome(number):
    return str(number) == str(number)[::-1]


def smallest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    for product in range(min_factor * min_factor, max_factor * max_factor + 1):
        if not is_palindrome(product):
            continue

        factors = []
        for first in range(min_factor, max_factor + 1):
            if product % first == 0:
                second = product // first
                if first <= second <= max_factor and second >= min_factor:
                    factors.append((first, second))

        if factors:
            return product, factors

    return None, []


def largest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    for product in range(max_factor * max_factor, min_factor * min_factor - 1, -1):
        if not is_palindrome(product):
            continue

        factors = []
        for first in range(min_factor, max_factor + 1):
            if first != 0 and product % first == 0:
                second = product // first
                if first <= second <= max_factor and second >= min_factor:
                    factors.append((first, second))

        if factors:
            return product, factors

    return None, []
