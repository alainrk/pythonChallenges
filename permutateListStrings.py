def solve(words):
    if not words:
        return ['']
    print words
    return [char + r for char in words[0] for r in solve(words[1:])]

res = solve(['red', 'fox', 'super', 'cuo'])
print len(res), res
