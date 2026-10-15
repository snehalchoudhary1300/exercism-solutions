
"""Generate rows of Pascal's triangle."""


def rows(row_count):
    """Return the first row_count rows of Pascal's triangle."""

    if row_count < 0:
        raise ValueError("number of rows is negative")

    if row_count == 0:
        return []

    previous_row = rows(row_count - 1)

    if not previous_row:
        return [[1]]

    last_row = previous_row[-1]
    new_row = [1]

    for index in range(len(last_row) - 1):
        new_row.append(last_row[index] + last_row[index + 1])

    new_row.append(1)
    previous_row.append(new_row)

    return previous_row
