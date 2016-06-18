'''
Examples:

N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]

1    2    3
8    9    4
7    6    5
N = 4 Output: [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
N = 5 Output: [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]

1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9
'''

def createSpiral(n,c=0,i=0,j=0,d=0):
    if (not isinstance(n, int) or n<=0): return []
    a = [[0 for p in range(n)] for q in range(n)]

    while c < n**2:
        c+=1
        a[i][j] = c
        if d == 0: #right
            if j==n-1 or a[i][j+1] != 0:
                d=1
                i+=1
            else: j+=1
        elif d == 1: #bottom
            if i==n-1 or a[i+1][j] != 0:
                d=2
                j-=1
            else: i+=1
        elif d == 2: #left
            if j==0 or a[i][j-1] != 0:
                d=3
                i-=1
            else: j-=1
        elif d == 3: #up
            if i==0 or a[i-1][j] != 0:
                d=0
                j+=1
            else: i-=1
    return a
