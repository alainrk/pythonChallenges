from random import randint

def init(m, n, q):
    matrix = [[randint(2, q) for c in range(n)] for r in xrange(m)]
    matrix[0][0], matrix[1][1] = 1, 1
    if m>n:
        matrix[2][0] = 1
    else:
        matrix[0][2] = 1
    return matrix

print init(4,3,3)
