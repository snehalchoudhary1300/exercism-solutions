"""Check whether a sentence is a pangram."""


def is_pangram(sentence):
    """Return True if the sentence contains every letter of the alphabet."""
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_letters = set(sentence.lower())

    return alphabet.issubset(sentence_letters)