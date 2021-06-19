def canSum(arr, num):
  sums = [False] * (num + 1)
  sums[0] = True

  '''
  [3, 4, 5], 7

  0th step => True, apply
  [T, F, F, F, F, F, F, F]
   |______+3|  |  |
   |_________+4|  |
   |____________+5|

  [T, F, F, T, T, T, F, F]
   |______+3|  |  |
   |_________+4|  |
   |____________+5|


  1th, 2th steps => False, so only go on
  [T, F, F, T, T, T, F, F]
      |______+3|  |  |
      |_________+4|  |
      |____________+5|

  3th step => True, apply
  [T, F, F, T, T, T, T, T] x
            |______+3|  |  |
            |_________+4|  |
            |____________+5|
  '''
  for s in range(len(sums)):
    for n in range(len(arr)):
      if sums[s] is False:
        continue
      # print(s, arr[n], sums)
      currSum = s + arr[n]
      if currSum <= num:
        sums[currSum] = True

  return sums[num]

assert(canSum([1], 7) == True)
assert(canSum([5, 3, 4], 1) == False)
assert(canSum([5, 3, 4], 2) == False)
assert(canSum([5, 3, 4], 7) == True)
assert(canSum([6, 5], 19) == False)
assert(canSum([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 7) == True)