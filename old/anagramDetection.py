def is_anagram(test, original):
    return sorted(list(test.lower())) == sorted(list(original.lower()))
