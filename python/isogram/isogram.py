def is_isogram(string):
    letters = [char for char in (string.lower()) if char.isalpha()]
    return len(letters) == len(set(letters))
