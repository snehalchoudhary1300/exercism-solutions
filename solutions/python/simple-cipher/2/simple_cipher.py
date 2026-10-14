
"""Implement the Vigenère cipher."""

import secrets
import string


class Cipher:
    """Encode and decode messages using the Vigenère cipher."""

    def __init__(self, key=None):
        """Initialize the cipher with a key."""
        if key is None:
            self.key = "".join(
                secrets.choice(string.ascii_lowercase)
                for key_position in range(100)
            )
        elif not key or any(
            letter not in string.ascii_lowercase for letter in key
        ):
            raise ValueError("Invalid key")
        else:
            self.key = key

    def encode(self, text):
        """Encode plaintext using the key."""
        result = []

        for index, letter in enumerate(text):
            shift = ord(self.key[index % len(self.key)]) - ord("a")
            encoded_letter = chr(
                (ord(letter) - ord("a") + shift) % 26 + ord("a")
            )
            result.append(encoded_letter)

        return "".join(result)

    def decode(self, text):
        """Decode ciphertext using the key."""
        result = []

        for index, letter in enumerate(text):
            shift = ord(self.key[index % len(self.key)]) - ord("a")
            decoded_letter = chr(
                (ord(letter) - ord("a") - shift) % 26 + ord("a")
            )
            result.append(decoded_letter)

        return "".join(result)
