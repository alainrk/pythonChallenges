class num:
    def __init__(self, n):
        self.n = n


def merge(arr, brr, counter):
    print ("MERGE", arr, brr)
    i, j, res = 0, 0, []
    while i<len(arr) and j<len(brr):
        if arr[i] <= brr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(brr[j])
            counter.n+=(len(arr)-1)
            j+=1
    if i<len(arr):
        for x in arr[i:]:
            res.append(x)
    if j<len(brr):
        for x in brr[j:]:
            res.append(x)
    return res

def mergesort(arr, counter):
    print ("SORT", arr)
    if len(arr) <= 1:
        return arr
    
    half = int(len(arr)/2)
    print ("HALF", len(arr), half, arr)
    
    left = mergesort(arr[:half], counter)
    right = mergesort(arr[half:], counter)

    return merge(left, right, counter)


d = [1, 6, 8, 8, 34, 3, 5, 7, 3, 2, 45, 57, 67, 23, 6, 56, 3, 43, 45, 57, 67, 67, 43, 3, 3, 2, 2, 2, 4, 5, 56, 67, 6]
c = num(0)
print (mergesort(d, c))
print c.n