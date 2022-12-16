KEY = str.maketrans({
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
})

def to_rna(dna_strand):
    return dna_strand.translate(KEY)
