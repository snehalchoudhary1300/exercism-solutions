
"""Convert OCR representations of digits into numbers."""


DIGITS = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}


def convert(string):
    """Convert OCR digits into a string."""
    if len(string) % 4 != 0:
        raise ValueError(
            "Number of input lines is not a multiple of four"
        )

    if any(len(line) % 3 != 0 for line in string):
        raise ValueError(
            "Number of input columns is not a multiple of three"
        )

    result = []

    for group_start in range(0, len(string), 4):
        group_lines = string[group_start:group_start + 4]
        group_digits = []

        for column_start in range(0, len(group_lines[0]), 3):
            digit = "".join(
                line[column_start:column_start + 3]
                for line in group_lines
            )
            group_digits.append(DIGITS.get(digit, "?"))

        result.append("".join(group_digits))

    return ",".join(result)
