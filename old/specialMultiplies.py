'''
ome numbers have the property to be divisible by 2 and 3. Other smaller subset of numbers have the property to be divisible by 2, 3 and 5. Another subset with less abundant numbers may be divisible by 2, 3, 5 and 7. These numbers have something in common: their prime factors are contiguous primes.

Create a function count_specMult() that finds the amount of numbers that have the first n primes as factors below a given value, maxVal

count_specMult(3, 200) -------> 6

'''

def count_specMult(n, m):
    return int(m / reduce(lambda x,y: x*y, [2,3,5,7,11,13,17,19,23][:n]))
