
"""Translate RNA codons into proteins."""


def proteins(strand):
    """Return the list of proteins translated from an RNA strand."""
    codons = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }

    result = []

    for index in range(0, len(strand), 3):
        codon = strand[index:index + 3]

        if codon in ("UAA", "UAG", "UGA"):
            break

        result.append(codons[codon])

    return result
