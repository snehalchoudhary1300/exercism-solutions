
"""Find suitable trees for building a tree house."""


def saddle_points(matrix):
    """Return the positions of all saddle points."""
    if not matrix:
        return []

    row_length = len(matrix[0])

    if any(len(row) != row_length for row in matrix):
        raise ValueError("irregular matrix")

    column_count = row_length
    row_maximums = [max(row) for row in matrix]
    column_minimums = [
        min(row[column] for row in matrix)
        for column in range(column_count)
    ]

    points = []

    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            if (
                value == row_maximums[row_index]
                and value == column_minimums[column_index]
            ):
                points.append(
                    {"row": row_index + 1, "column": column_index + 1}
                )

    return points
