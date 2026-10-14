
"""Encode and decode text using the Atbash cipher."""

import string


def encode(plain_text):
    """Encode text and group letters into blocks of five."""
    result = []

    for character in plain_text.lower():
        if character.isalpha() and character.isascii():
            result.append(chr(ord('z') - (ord(character) - ord('a'))))
        elif character.isdigit():
            result.append(character)

    encoded_text = "".join(result)
    return " ".join(
        encoded_text[index:index + 5]
        for index in range(0, len(encoded_text), 5)
    )


def decode(ciphered_text):
    """Decode Atbash text without spaces."""
    result = []

    for character in ciphered_text.lower():
        if character.isalpha() and character.isascii():
            result.append(chr(ord('z') - (ord(character) - ord('a'))))
        elif character.isdigit():
            result.append(character)

    return "".join(result)
