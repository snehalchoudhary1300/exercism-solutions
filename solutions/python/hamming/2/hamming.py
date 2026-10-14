
"""Calculate the Hamming distance between two DNA strands."""

def distance(strand_a, strand_b):
    """Return the number of positions where the strands differ."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0

    for position, nucleotide in enumerate(strand_a):
        if nucleotide != strand_b[position]:
            count += 1

    return count
