'''
How many zeroes are at the end of the factorial of 10? 10! = 3628800, i.e. there are two zeroes.
16! in hexadecimal would be 0x130777758000, which results in three zeroes.

Unfortunately machine integer numbers has not enough precision for larger values. Floats drops the tail we need. We can fall back to arbitrary-precision ones - built-ins or from a library, but calculating the full product isn't an efficient way to find the tail of the factorial. Calculating 100'000! takes around 10 seconds on my machine, let alone 1'000'000!.

base is an integer from 2 to 256
number is an integer from 1 to 1'000'000
'''

from math import *

def zeroes (b, n):
    zeros = n
    j = b
    for i in range(2,b+1):
        if j%i == 0:
            p = 0
            while j%i == 0:
                p+=1
                j/=i
            c=0
            k=n
            while k/i > 0:
                c+=k/i
                k/=i
            zeros = min(zeros,c/p)
    return zeros
