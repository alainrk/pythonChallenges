def insertionSort(array):
  for i in range(1, len(array)):
    curr = i
    while curr > 0 and array[curr] < array[curr - 1]:
      array[curr], array[curr - 1] = array[curr - 1], array[curr]
      curr -= 1
  return array
