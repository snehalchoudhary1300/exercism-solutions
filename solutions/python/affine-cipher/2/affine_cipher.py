
"""Implement the affine cipher."""


def encode(plain_text, multiplier, shift):
    """Encrypt text using the affine cipher."""
    if gcd(multiplier, 26) != 1:
        raise ValueError("a and m must be coprime.")

    encrypted_characters = []

    for character in plain_text.lower():
        if character.isascii() and character.isalpha():
            letter_index = ord(character) - ord("a")
            encrypted_index = (multiplier * letter_index + shift) % 26
            encrypted_characters.append(chr(encrypted_index + ord("a")))
        elif character.isdigit() and character.isascii():
            encrypted_characters.append(character)

    encrypted_text = "".join(encrypted_characters)
    return " ".join(
        encrypted_text[index:index + 5]
        for index in range(0, len(encrypted_text), 5)
    )


def decode(ciphered_text, multiplier, shift):
    """Decrypt text using the affine cipher."""
    if gcd(multiplier, 26) != 1:
        raise ValueError("a and m must be coprime.")

    inverse = pow(multiplier, -1, 26)
    decrypted_characters = []

    for character in ciphered_text.lower():
        if character.isascii() and character.isalpha():
            letter_index = ord(character) - ord("a")
            decrypted_index = (inverse * (letter_index - shift)) % 26
            decrypted_characters.append(chr(decrypted_index + ord("a")))
        elif character.isdigit() and character.isascii():
            decrypted_characters.append(character)

    return "".join(decrypted_characters)


def gcd(first_number, second_number):
    """Return the greatest common divisor of two integers."""
    while second_number:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )
    return abs(first_number)
