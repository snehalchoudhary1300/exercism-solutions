
"""Convert a phrase into an acronym."""

import re


def abbreviate(words):
    """Return the acronym formed from the given phrase."""
    words = words.replace("-", " ")
    words = re.sub(r"[^a-zA-Z\s]", "", words)

    return "".join(word[0].upper() for word in words.split())

