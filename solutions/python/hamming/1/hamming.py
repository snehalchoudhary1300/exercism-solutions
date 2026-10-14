
"""Calculate the Hamming distance between two DNA strands."""

def distance(strand_a, strand_b):
    """Return the number of positions where the strands differ."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0

    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            count += 1

    return count
