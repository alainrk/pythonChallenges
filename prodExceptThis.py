def prodExceptThis(l):
    part = []
    for i, v in enumerate(l):
        if i == 0:
            part.append([1,0])
            continue
        before = l[i-1]*part[i-1][0]
        part.append([ before , 0 ])

    res = []

    for i, v in reversed(list(enumerate(l))):
        if i == len(l)-1:
            part[i][1] = 1
            res.append(part[i][0])
            continue
        part[i][1] = l[i+1] * part[i+1][1]
        res.append(part[i][0] * part[i][1])

    return list(reversed(res))

print prodExceptThis([1, 2, 6, 5, 9])
