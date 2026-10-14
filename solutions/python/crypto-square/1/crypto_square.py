
"""Encode text using the square code."""


import math
import string


def cipher_text(plain_text):
    """Normalize and encode text using a square."""
    normalized_text = "".join(
        character.lower()
        for character in plain_text
        if character.isalnum()
    )

    if not normalized_text:
        return ""

    columns = math.ceil(math.sqrt(len(normalized_text)))
    rows = math.ceil(len(normalized_text) / columns)

    rectangle = [
        normalized_text[index:index + columns]
        for index in range(0, len(normalized_text), columns)
    ]

    encoded_chunks = []

    for column_index in range(columns):
        chunk = "".join(
            row[column_index] if column_index < len(row) else " "
            for row in rectangle
        )
        encoded_chunks.append(chunk)

    return " ".join(encoded_chunks)
