def maxSub(l):
    s = [l[0], max(l[1], l[2])]

    for i in xrange(2,len(l)):
        s.append(max(s[i-1],l[i]+s[i-2], l[i] + s[i-3]))

    return s[len(s)-1]

print maxSub([1, 6, 3, 2, 5, 4])
print maxSub([1, 6, 2, 2, 3])
