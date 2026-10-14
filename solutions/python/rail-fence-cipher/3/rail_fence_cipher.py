"""Encode and decode messages using the Rail Fence Cipher."""


def encode(message, rails):
    """Encode a message using the given number of rails."""
    if rails == 1 or rails >= len(message):
        return message

    fence = [[] for rail_index in range(rails)]
    rail = 0
    direction = 1

    for character in message:
        fence[rail].append(character)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return "".join("".join(row) for row in fence)


def decode(encoded_message, rails):
    """Decode a message encoded with the Rail Fence Cipher."""
    if rails == 1 or rails >= len(encoded_message):
        return encoded_message

    pattern = []
    rail = 0
    direction = 1

    for character in encoded_message:
        pattern.append(rail)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    rail_counts = [
        pattern.count(rail_index) for rail_index in range(rails)
    ]

    rail_messages = []
    position = 0

    for count in rail_counts:
        rail_messages.append(
            list(encoded_message[position:position + count])
        )
        position += count

    result = []

    for rail_index in pattern:
        result.append(rail_messages[rail_index].pop(0))

    return "".join(result)
    