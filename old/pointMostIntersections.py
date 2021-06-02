
def allIntersect(intervals):
        # sortedIntervals = sorted(intervals, key=lambda x: x[0])
        sets = []
        for s in intervals:
            print s
            sets.append(set([x for x in range(s[0],s[1]+1)]))

        return reduce(lambda x, y: x.intersection(y), sets)

def mostIntersectHeavy(intervals):
        mini = min(list(map(lambda x: x[0], intervals)))
        maxi = max(list(map(lambda x: x[1], intervals)))
        maxCount, maxPoint = 0, None
        for curr in xrange(mini, maxi+1):
            currCount = 0
            for i in intervals:
                if curr > i[0] and curr < i[1]:
                    currCount += 1
            if currCount > maxCount:
                maxCount, maxPoint = currCount, curr
                if currCount == len(intervals):
                    break
        return maxPoint, maxCount

def mostIntersect(intervals):
    arr = []
    for i,j in intervals:
        arr.append((i,"S"))
        arr.append((j,"E"))
    arr.sort(key=lambda x: x[0])
    count,maxsofar,maxi = 0,None,-1
    for c in arr:
        tmp = count + (1 if c[1] == "S" else -1)
        if tmp > count:
            maxsofar = c[0]
            maxi = tmp
        count = tmp
    return maxsofar,maxi

print mostIntersectHeavy([[0,5],[1,9],[2,4],[1,3],[0,34]])
print mostIntersectHeavy([[0,5],[1,9],[2,4],[1,3],[0,340]])
print mostIntersectHeavy([[-20,5],[-10,9],[-2,4],[1,3],[0,340]])
print mostIntersectHeavy([[0,50],[19,60],[22,45],[1,3],[0,340]])
print mostIntersectHeavy([[100,500],[2,9],[-4,-2],[0,1],[10,34]])
print "---------------------------"
print mostIntersect([[0,5],[1,9],[2,4],[1,3],[0,34]])
print mostIntersect([[0,5],[1,9],[2,4],[1,3],[0,340]])
print mostIntersectHeavy([[-20,5],[-10,9],[-2,4],[1,3],[0,340]])
print mostIntersectHeavy([[0,50],[19,60],[22,45],[1,3],[0,340]])
print mostIntersect([[100,500],[2,9],[-4,-2],[0,1],[10,34]])

'''
0123456789

------|-
    --|-------
 ---  |
  ----|-----
      |  --------
    --|---------
      |
'''
