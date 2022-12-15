def is_pangram(sentence):
    pangram = 'the quick brown fox jumps over the lazy dog'
    alphabet = set(pangram) - {' '}

    chars = set(sentence.lower())
    
    return alphabet <= chars
