from math import sqrt

p = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,907]

for n in p:
    if (n < 2):
        print n
        print "Not prime"
        continue
    b = False
    for i in xrange(2, int(sqrt(n))+1):
        if (n % i == 0):
            b = True
            break
    print n
    print "Not prime" if b else "Prime"
    print
