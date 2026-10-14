
"""Functions for working with matrices."""


class Matrix:
    """Represent a matrix and provide row and column access."""

    def __init__(self, matrix_string):
        self.matrix = [
            [int(number) for number in row.split()]
            for row in matrix_string.splitlines()
        ]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
