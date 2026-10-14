
"""Transcribe DNA nucleotides into RNA."""


def to_rna(dna_strand):
    """Return the RNA complement of a DNA strand."""
    complements = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join(complements[nucleotide] for nucleotide in dna_strand)

