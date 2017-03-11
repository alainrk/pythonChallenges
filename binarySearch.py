from math import floor

def binSearch(l, n):
    start, end = 0, len(l)-1

    while start <= end:
        # middle = int(floor((start+end)/2))
        middle = (start+end)/2
        if l[middle] == n:
            return middle
        if l[middle] < n:
            start= middle+1
        else:
            end = middle-1
    return None


print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], -1)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 0)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 7)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 9)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 10)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12)
print binSearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 13)
