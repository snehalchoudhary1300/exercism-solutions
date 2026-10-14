
"""Count the frequency of words in a phrase."""

import re


def count_words(sentence):
    """Return a dictionary containing each word's frequency."""
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)*", sentence.lower())

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
