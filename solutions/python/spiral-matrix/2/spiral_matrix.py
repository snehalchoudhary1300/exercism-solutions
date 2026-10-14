
"""Create a square matrix filled in clockwise spiral order."""


def spiral_matrix(size):
    """Return a square matrix filled with numbers in spiral order."""
    if size == 0:
        return []

    matrix = [
        [0] * size
        for row_index in range(size)
    ]

    top = 0
    bottom = size - 1
    left = 0
    right = size - 1
    number = 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            matrix[top][col] = number
            number += 1
        top += 1

        for row in range(top, bottom + 1):
            matrix[row][right] = number
            number += 1
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = number
                number += 1
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = number
                number += 1
            left += 1

    return matrix
