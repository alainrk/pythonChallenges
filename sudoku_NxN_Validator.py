'''

Input format structure

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

Works with NxN!

'''

from math import *
import numbers

class Sudoku(object):

    def __init__(self, m):
        self.m = m
        self.n = len(m)
        self.q = int(sqrt(self.n))
        self.summa = (self.n * (self.n+1))/2

    def is_valid(self):

        if self.n == 1 and (type(self.m[0][0]) != type(1) or self.m[0][0] != 1):
            return False

        for i in self.m:
            if (len(i) != self.n):
                print "Invalid number of columns"
                return False

        for c in range(self.n):
            checkRow = [False for i in range(1,self.n+1)]
            # Rows check
            for col in self.m[c]:
                if checkRow[col-1] or not 0<col<=self.n or type(col) != type(1):
                    print "Duplicates in row or invalid number"
                    return False
                else:
                    checkRow[col-1] = True

            # Columns check
            if reduce(lambda x,y: x+y, [colu[c] for colu in self.m]) != self.summa:
                print "Duplicates in column"
                return False

        # Boxes check
        sums = [0 for i in range(self.n)]
        dq = 0
        for k in range(self.n):
            dq = dq+self.q if k!=0 and k%self.q==0 else dq
            for w in range(self.n):
                sums[dq + w/self.q] += self.m[k][w]
        if  not all(map(lambda x: x == self.summa, sums)):
            print "Duplicates in boxes"
            return False

        return True
