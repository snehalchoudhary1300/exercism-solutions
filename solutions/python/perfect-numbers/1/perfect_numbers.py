"""Classify numbers as perfect, abundant, or deficient."""


def classify(number):
    """Return the classification of a positive integer.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        return "perfect"

    if divisor_sum > number:
        return "abundant"

    return "deficient"