
"""Implement the affine cipher."""


def encode(plain_text, a, b):
    """Encrypt text using the affine cipher."""
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    result = []

    for character in plain_text.lower():
        if character.isalpha() and character.isascii():
            number = ord(character) - ord("a")
            encrypted = (a * number + b) % 26
            result.append(chr(encrypted + ord("a")))
        elif character.isdigit():
            result.append(character)

    text = "".join(result)
    return " ".join(
        text[index:index + 5] for index in range(0, len(text), 5)
    )


def decode(ciphered_text, a, b):
    """Decrypt text using the affine cipher."""
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    inverse = pow(a, -1, 26)
    result = []

    for character in ciphered_text.lower():
        if character.isalpha() and character.isascii():
            number = ord(character) - ord("a")
            decrypted = (inverse * (number - b)) % 26
            result.append(chr(decrypted + ord("a")))
        elif character.isdigit():
            result.append(character)

    return "".join(result)


def gcd(a, b):
    """Return the greatest common divisor of two integers."""
    while b:
        a, b = b, a % b
    return abs(a)
