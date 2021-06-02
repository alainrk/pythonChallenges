'''
Description:

Write a function which reduces fractions to their simplest form! Fractions will be presented as an array, and the reduced fraction must be returned as an array
'''

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def reduce(n):
    div = gcd(n[0],n[1])
    return [int(n[0]/div), int(n[1]/div)]
