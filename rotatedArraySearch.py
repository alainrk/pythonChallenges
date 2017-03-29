def search(arr, key):
    start, end = 0, len(arr)
    compare = arr[0]
    first = -1

    while start <= end:
        middle = (start + end)/2
        # print start, middle, end

        if middle == 0:
            if arr[0] < arr[1]:
                first = 0
            if arr[1] < arr[0]:
                first = 1
            break
        elif middle == len(arr)-1:
            first = len(arr)-1 if arr[middle] < arr[middle-1] else 0
            break

        elif arr[middle] > arr[middle+1]:
            first = middle + 1
            break
        elif arr[middle] < arr[middle-1]:
            first = middle
            break
        elif arr[middle] > compare:
            start = middle + 1
        else:
            end = middle-1

    # print "First",first
    if key < arr[0]:
        start, end = first, len(arr)-1
    else:
        start, end = 0, first-1

    while start <= end:
        middle = (start+end)/2
        # print middle, arr[middle]
        if arr[middle] == key:
            # print middle
            return middle
        elif arr[middle] < key:
            start = middle+1
        else:
            end = middle-1
    return None

print 7 == search([6,8,9,11,1,2,4,5],5)
print 10 == search([6,8,9,11,12,13,15,1,2,4,5],5)
print 6 == search([6,8,9,1,2,4,5],5)
print 5 == search([6,8,9,1,2,4,5],4)
print 2 == search([6,8,9,1,2,4,5],9)
print 0 == search([6,11,1,2,4,5],6)

print 4 == search([10,1,2,4,5,6,7,8],5)
print 4 == search([11,1,2,4,5],5)
print 4 == search([12,1,2,4,5,0],5)
print 0 == search([5,1,2,4],5)
print 1 == search([4,5,1,2],5)
print 1 == search([4,5,1,2],5)
print 3 == search([4,5,1,2],2)
print 2 == search([5,1,2],2)
print 4 == search([5,6,7,8,1],1)
