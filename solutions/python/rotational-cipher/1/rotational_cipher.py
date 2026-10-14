
"""Encrypt text using a rotational cipher."""


def rotate(text, key):
    """Return text with each letter shifted by the given key."""
    result = ""

    for character in text:
        if "a" <= character <= "z":
            result += chr((ord(character) - ord("a") + key) % 26 + ord("a"))
        elif "A" <= character <= "Z":
            result += chr((ord(character) - ord("A") + key) % 26 + ord("A"))
        else:
            result += character

    return result
