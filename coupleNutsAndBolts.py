def comp(a,b):
    return -1 if a[0] < b[0] else (1 if a[0] > b[0] else 0)

def couple(nuts, bolts):
    ns, bs = [], [] # 2*O(n)
    for i,n in enumerate(nuts):     # O(n)
        ns.append([n,i])
    for i,b in enumerate(bolts):    # O(n)
        bs.append([b,i])

    print ns,bs
    ns, bs = sorted(ns, comp), sorted(bs, comp) # 2*O(nlogn)
    print ns,bs

    res = []
    for i in xrange(len(nuts)):             #O(n)
        res.append(( ns[i][1], bs[i][1] ))

    return res

print couple([2, 1, 3, 5, 7], [7, 5, 1, 3, 2])
print couple([7, 5, 1, 3, 2],[7, 5, 1, 3, 2])
