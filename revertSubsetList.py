# Amazon recruiting test

def revertSubsetList(l,n,res=[]):
    for i in range(1, len(l)/n+1):
        for j in range(1,n+1):
            res += [ l[i*n-j] ]
    return res

print revertSubsetList([1,2,3,4,5,6,7,8,9,10,11,12], 3)
