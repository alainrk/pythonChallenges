'''
From: https://www.codewars.com/kata/padovan-numbers/train/python

The Padovan sequence is the sequence of integers P(n) defined by the initial values

P(0)=P(1)=P(2)=1

and the recurrence relation

P(n)=P(n-2)+P(n-3)

The first few values of P(n) are

1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, ...
'''


def padovan(n):
    pad = [0,1,1]
    for c in range(2,n):
        pad.append(pad[0]+pad[1])
        del(pad[0])
    return pad[0] + pad[1]
