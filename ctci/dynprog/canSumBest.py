def canSum(arr, num):
  sums = [None for i in range(num + 1)]
  sums[0] = []

  '''
  [3, 4, 5], 7

  0th step => True, apply
  [[], N, N, [3], [4], [5], N, N]
   |_________+3|   |    |
   |_____________+4|    |
   |__________________+5|

  1th, 2th steps => False, so only go on
  [[], N, N, [3], [4], [5], N, N]
       |_________+3|   |    |
       |_____________+4|    |
       |__________________+5|

  3th step => True, apply
  [[], N, N, [3], [4], [5], [3,3], [3,4]]  x
              |______________+3|    |      |
              |___________________+4|      |
              |__________________________+5|
  '''
  for s in range(len(sums)):
    for n in range(len(arr)):
      if sums[s] is None:
        continue
      # print(s, arr[n], sums)
      currSum = s + arr[n]
      if currSum > num:
        continue
      # copy over and add the current num
      newSum = sums[s] + [arr[n]]
      sums[currSum] = newSum if sums[currSum] is None or len(newSum) <= len(sums[currSum]) else sums[currSum]

  return sums[num]

print(canSum([1], 7))
print(canSum([1, 1], 7))
print(canSum([1, 1, 1], 7))
print(canSum([1, 1, 1, 7], 7))
print(canSum([7, 1, 1, 1], 7))
print(canSum([1, 1, 1, 6], 7))
print(canSum([6, 1, 7], 7))
print(canSum([5, 3, 4, 1], 7))
print(canSum([5, 3, 4], 7))
print(canSum([3, 4], 5))