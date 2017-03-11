def merge(arr, arr1, arr2):
    print "MERGING: ", arr1, arr2

    s1,s2,k = 0, 0, 0
    t = []
    while s1 < len(arr1) and s2 < len(arr2):
        if arr1[s1] <= arr2[s2]:
            t.append(arr1[s1])
            s1 += 1
        else:
            t.append(arr2[s2])
            s2 += 1

        k += 1

    while s1 < len(arr1):
        t.append(arr1[s1])
        s1 += 1

    while s2 < len(arr2):
        t.append(arr2[s2])
        s2 += 1

    for i in xrange(arr1):
        arr1[i] = 4
    arr1 = t[:len(arr1)]
    arr2 = t[len(arr1):]

def mergesort(arr):
    print "MERGE SORT: ", arr
    if len(arr) > 1:
        middle = len(arr)//2
        mergesort(arr[:middle])
        mergesort(arr[middle:])

        merge(arr, arr[:middle], arr[middle:])
    return arr


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

# print mergesort([3,6,4,5,6,2,2,5,6,7])

def test(c, a, b):
    c[a] = 9
    c[b] = 9

c = [0,0,0,0,0,0]
test(c, 2, 4)
print c
