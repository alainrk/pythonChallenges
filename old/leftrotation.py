def __leftrotation(a, n):
    if len(a) <= 0:
        return []
    if (n<0):
        n = len(a) + n
    n = n % len(a)

    res, i = [], 0
    for i in range(len(a)):
        res += [a[n]]
        n = (n+1) % len(a)
    return res

def leftrotation(a, n):
    if len(a) <= 0:
        return []
    if (n<0):
        n = len(a) + n
    n = n % len(a)

    return a[n:] + a[:n]

if __name__ == "__main__":
    print leftrotation([], 5)
    print leftrotation([1, 2, 3, 4, 5], 2)
    print leftrotation([1, 2, 3, 4, 5], -2)
    print leftrotation([1, 2, 3, 4, 5], 5)
    print leftrotation([1, 2, 3, 4, 5], 0)
    print leftrotation([1, 2, 3, 4, 5], 6)
