'''
From codewars

Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C# or C++ and as an array of arrays in other languages.

Example:

I = [12, 15] 
result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes: It can happen that a sum is 0 if some numbers are negative!

Typescript return is the same as Javascript or Coffeescript return (Description doesn't accept reference to typescript...)

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

'''

def primes(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(set(factors))
    
def flatprimes(p):
    ps = []
    for i in p:
        for j in i:
            ps += [j]
    return list(set(ps))

def sum_for_list(l):
    listprimes = [primes(x) for x in list(map(lambda x: abs(x), l))]
    allprimes = flatprimes(listprimes)
    print(l, "\n", listprimes, "\n", allprimes, "\n\n")
    
    res = []
    for i in sorted(allprimes):
        sum = 0
        for c in range(len(l)):
            sum += l[c] if i in listprimes[c] else 0
        res += [[i, sum]]
    print(res)
    return res