"""Calculate the square of sums, sum of squares, and their difference."""


def square_of_sum(number):
    """Return the square of the sum of the first number natural numbers."""
    total = sum(range(1, number + 1))
    return total ** 2


def sum_of_squares(number):
    """Return the sum of the squares of the first number natural numbers."""
    return sum(value ** 2 for value in range(1, number + 1))


def difference_of_squares(number):
    """Return the difference between the square of sum and sum of squares."""
    return square_of_sum(number) - sum_of_squares(number)