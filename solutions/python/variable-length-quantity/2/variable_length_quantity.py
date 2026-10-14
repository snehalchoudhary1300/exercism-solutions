
"""Encode and decode variable length quantities."""


def encode(numbers):
    """Encode a list of integers into VLQ bytes."""
    result = []

    for number in numbers:
        if number < 0 or number > 0xFFFFFFFF:
            raise ValueError("number must be a 32-bit unsigned integer")

        remaining_number = number
        chunks = [remaining_number & 0x7F]
        remaining_number >>= 7

        while remaining_number > 0:
            chunks.append((remaining_number & 0x7F) | 0x80)
            remaining_number >>= 7

        result.extend(reversed(chunks))

    return result


def decode(bytes_):
    """Decode VLQ bytes into a list of integers."""
    result = []
    number = 0
    incomplete = False

    for byte in bytes_:
        if byte < 0 or byte > 0xFF:
            raise ValueError("byte must be between 0 and 255")

        number = (number << 7) | (byte & 0x7F)
        incomplete = bool(byte & 0x80)

        if not incomplete:
            result.append(number)
            number = 0

    if incomplete:
        raise ValueError("incomplete sequence")

    return result
