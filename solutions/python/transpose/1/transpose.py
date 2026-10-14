
"""Transpose rows of text into columns."""


def transpose(text):
    """Return the transposed text."""
    if not text:
        return ""

    rows = text.split("\n")
    max_length = max(len(row) for row in rows)
    result = []

    for column in range(max_length):
        new_row = ""

        for row_index, row in enumerate(rows):
            if column < len(row):
                new_row += row[column]
            elif any(len(other_row) > column for other_row in rows[row_index + 1:]):
                new_row += " "

        result.append(new_row)

    return "\n".join(result)
