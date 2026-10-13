
"""Respond to Bob's remarks."""


def response(hey_bob):
    """Return Bob's response based on the statement."""
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    has_letters = any(char.isalpha() for char in hey_bob)
    is_yelling = has_letters and hey_bob.upper() == hey_bob

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."
