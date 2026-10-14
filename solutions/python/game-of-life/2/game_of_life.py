
"""Calculate the next generation in Conway's Game of Life."""


def tick(matrix):
    """Return the next generation of the game board."""
    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])
    next_generation = []

    for row in range(rows):
        new_row = []

        for column in range(columns):
            live_neighbors = 0

            for row_offset in (-1, 0, 1):
                for column_offset in (-1, 0, 1):
                    if row_offset == 0 and column_offset == 0:
                        continue

                    neighbor_row = row + row_offset
                    neighbor_column = column + column_offset

                    if (
                        0 <= neighbor_row < rows
                        and 0 <= neighbor_column < columns
                    ):
                        live_neighbors += matrix[neighbor_row][neighbor_column]

            if matrix[row][column] == 1:
                new_row.append(
                    1 if live_neighbors in {2, 3} else 0
                )
            else:
                new_row.append(1 if live_neighbors == 3 else 0)

        next_generation.append(new_row)

    return next_generation
