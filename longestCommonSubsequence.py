'''
lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"
'''

def lcs(x, y):
    if x == y:
        return x
    if (len(x) == len(y) == 1 and x!=y) or min(len(x), len(y)) == 0:
        return ""

    if x[len(x)-1] == y[len(y)-1]:
        return lcs(x[:len(x)-1], y[:len(y)-1])+x[len(x)-1]
    else:
        p = lcs(x[:len(x)-1], y)
        q = lcs(x, y[:len(y)-1])
        return p if len(p) > len(q) else q 
