def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    strand_a, strand_b = list(strand_a), list(strand_b)

    errors = 0

    for index, gene in enumerate(strand_a):
        if strand_b[index] != gene:
            errors += 1

    return errors