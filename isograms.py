# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    l = list(string.lower())
    return True if len(set(x for x in l if l.count(x) > 1)) == 0 else False
