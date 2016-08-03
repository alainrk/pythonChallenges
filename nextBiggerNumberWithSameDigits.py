'''
next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
'''

from itertools import permutations

def getn(l):
    return int("".join(map(lambda x: str(x),l)))

def getNextGreater(l,n):
    return min(filter(lambda x: x>n, l))

def next_bigger(n):
    s = map(lambda x: int(x), list(str(n)))
    curr = len(s)-2
    prev = len(s)-1

    if s[curr] < s[prev]:
        res = s[:curr] + [s[prev]] + sorted(s[prev+1:]+[s[curr]])
        return getn(res)

    while curr >= 0:
        if s[curr] >= s[prev]:
            curr-=1
            prev-=1
            continue

        if s[curr] < s[prev+1]:
            next = getNextGreater(s[prev:],s[curr])
            rem = s[prev:]
            rem.remove(next)
            res = s[:curr] + [next] + sorted(rem+[s[curr]])
            return getn(res)

        if s[curr] >= s[prev+1]:
            res = s[:curr] + [s[prev]] + sorted(s[prev+1:]+[s[curr]])
            return getn(res)
    return -1
