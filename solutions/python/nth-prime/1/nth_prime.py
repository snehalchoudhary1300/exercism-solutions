
"""Find the nth prime number."""


def prime(number):
    """Return the nth prime number."""
    if number < 1:
        raise ValueError("there is no zeroth prime")

    prime_count = 0
    candidate = 1

    while prime_count < number:
        candidate += 1
        is_prime = True

        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            prime_count += 1

    return candidate
