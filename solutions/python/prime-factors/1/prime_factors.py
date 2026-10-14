
"""Calculate the prime factors of a number."""


def factors(value):
    """Return the list of prime factors of the given number."""
    prime_factors = []
    divisor = 2

    while value > 1:
        if value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
        else:
            divisor += 1

    return prime_factors
