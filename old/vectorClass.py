'''
a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([5,6,7,8])
a.add(b) # should return Vector([4,6,8])
a.subtract(b) # should return Vector([-2,-2,-2])
a.dot(b) # should return 1*3+2*4+3*5 = 26
a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
a.add(c) # raises an exception
'''

from math import sqrt

class Vector:
    def __init__(self, a):
        self.a = a

    def getArr(self):
        return self.a

    def __str__(self):
        return (tuple(self.a)).__str__().replace(" ","")

    def equals(self, b):
        return self.a == b.getArr()

    def add(self, b):
        if len(self.a) != len(b.getArr()):
            raise ValueError('Different Lengths!')
        else:
            return Vector([x+y for x,y in zip(self.a, b.getArr())])

    def subtract(self, b):
        if len(self.a) != len(b.getArr()):
            raise ValueError('Different Lengths!')
        else:
            return Vector([x-y for x,y in zip(self.a, b.getArr())])


    def dot(self, b):
        if len(self.a) != len(b.getArr()):
            raise ValueError('Different Lengths!')
        else:
            return reduce(lambda p,q: p+q, [x*y for x,y in zip(self.a, b.getArr())])


    def norm(self):
        return sqrt(reduce(lambda x,y: x+y, [i**2 for i in self.a]))
