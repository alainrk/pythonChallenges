def canSum(arr, num):
  sums = [[] for i in range(num + 1)]
  sums[0].append([])

  for s in range(len(sums)):
    for n in range(len(arr)):
      if not len(sums[s]):
        continue
      # print(s, arr[n], sums)
      currSum = s + arr[n]
      if currSum > num:
        continue
      for way in sums[s]:
        sums[currSum].append(way + [arr[n]])

  return sums[num]

print(canSum([1], 7))
# double-counting => print(canSum([1, 1], 7))
# double-counting => print(canSum([1, 1, 1], 7))
print(canSum([5, 3, 4], 7))
print(canSum([3, 4], 5))