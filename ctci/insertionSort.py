def insertionSort(arr):
  for i in range(1, len(arr)):
    j = i-1
    curr = arr[i]
    while curr < arr[j] and j >= 0:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = curr
  return arr

assert insertionSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert insertionSort([]) == []
assert insertionSort([1]) == [1]
assert insertionSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert insertionSort([10, 5, 5, 5, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 5, 5, 5, 10]