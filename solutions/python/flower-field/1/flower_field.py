"""Annotate a Flower Field board with adjacent flower counts."""


def annotate(minefield):
    """Return the board with counts of adjacent flowers."""
    if not minefield:
        return []

    width = len(minefield[0])

    if any(len(row) != width for row in minefield):
        raise ValueError("The board is invalid with current input.")

    if any(
        character not in (" ", "*")
        for row in minefield
        for character in row
    ):
        raise ValueError("The board is invalid with current input.")

    result = []

    for row_index, row in enumerate(minefield):
        new_row = ""

        for col_index, character in enumerate(row):
            if character == "*":
                new_row += "*"
                continue

            count = 0

            for row_offset in (-1, 0, 1):
                for col_offset in (-1, 0, 1):
                    if row_offset == 0 and col_offset == 0:
                        continue

                    neighbor_row = row_index + row_offset
                    neighbor_col = col_index + col_offset

                    if (
                        0 <= neighbor_row < len(minefield)
                        and 0 <= neighbor_col < width
                        and minefield[neighbor_row][neighbor_col] == "*"
                    ):
                        count += 1

            new_row += str(count) if count else " "

        result.append(new_row)

    return result