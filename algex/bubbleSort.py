def bubbleSort(array):
	curr = 0
	last = len(array) - 1
	while True:
		if curr == last:
			return array
		if array[curr] > array[curr + 1]:
			array[curr], array[curr + 1] = array[curr + 1], array[curr]
		curr += 1
		if curr == last:
			last -= 1
			curr = 0
