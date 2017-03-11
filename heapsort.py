# Invariant l[k] >= l[2k+1] AND l[k] >= l[2k+2]

def getHeap(l):
    for i in reversed(xrange(0, len(l)/2)):
        print i, l[i]

l = [2,7,26,25,19,17,1,90,3,36]
getHeap(l)
