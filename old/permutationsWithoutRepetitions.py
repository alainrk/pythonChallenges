'''
perms(1)==1
perms(45)==2
perms(115)==3
perms("abc")==6
'''

import math
def perms(x):
    return math.factorial(len(str(x))) / reduce(lambda x,y: x*y, [math.factorial(v) for k,v in {k:str(x).count(k) for k in list(str(x))}.items()])
