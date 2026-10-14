
"""Convert numbers between different bases."""


def rebase(input_base, digits, output_base):
    """Convert digits from one base to another."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert the input number to decimal.
    decimal_number = 0

    for digit in digits:
        decimal_number = decimal_number * input_base + digit

    # Return zero for an empty list or a number consisting of zeros.
    if decimal_number == 0:
        return [0]

    # Convert decimal to the output base.
    result = []

    while decimal_number > 0:
        result.append(decimal_number % output_base)
        decimal_number //= output_base

    return result[::-1]
