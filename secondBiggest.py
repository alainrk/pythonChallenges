def secbig(arr):
    maxi, res = arr[0], arr[0] - abs(arr[1])
    for i in arr[1:]:
        if i > maxi:
            res, maxi = maxi, i
        elif i < maxi:
            if i > res:
                res = i
    return maxi, res

print secbig([25678,-3456789,6,6,5,7,7,7,7,7,7,7,7,2,10,2,1,45,6,7,3,4,7,3,-123,456,4])
