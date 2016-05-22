# Amazon recruiting test

def revertSubsetList(l,n):
    res = []
    for i in range(1, n+1):
        print i
        for j in range(1,n+1):
            res += [ l[i*n-j] ]
    return res

print revertSubsetList([1,2,3,4,5,6,7,8,9], 3) # [3, 2, 1, 6, 5, 4, 9, 8, 7]
