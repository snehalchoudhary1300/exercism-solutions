
"""Generate secret handshake commands."""


def commands(binary_str):
    """Return the handshake actions for a binary string."""
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = []

    for index, action in enumerate(actions):
        if binary_str[-(index + 1)] == "1":
            result.append(action)

    if binary_str[-5] == "1" if len(binary_str) >= 5 else False:
        result.reverse()

    return result
