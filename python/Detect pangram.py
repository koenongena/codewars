import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
